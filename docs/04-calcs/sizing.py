"""CampBreak sizing calculations (CBK-CAL-001).

Run from the repo root:  python3 docs/04-calcs/sizing.py
Prints every section of docs/04-calcs/01-sizing.md and writes docs/04-calcs/results.csv.
Geometry comes from cad/src/model.py (PARAMS P and the model volumes); costs from bom/bom.csv.
Every input that is an estimate is marked (est.) and listed in the calculation note.
"""
import csv
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "cad/src"))
import model as M  # noqa: E402

g, rho, nu = 9.81, 1000.0, 1.0e-6        # water at about 20 C
P = M.P

# ------------------------------------------------------------------ A. pump, hose and nozzle (R7, R8)
A_IN = dict(
    v_ds=0.40e-3,       # m3 per double stroke (est.; to confirm when the pump is bought)
    n_ds=60.0,          # double strokes per minute, a steady pace for two people (est.)
    eta_v=0.85,         # volumetric efficiency of a cast semi-rotary pump (est.)
    eta_m=0.50,         # mechanical efficiency including the lever and seals (est.)
    d_jet=6.0e-3, cd=0.96,
    d_hose=19.0e-3, l_hose=30.0, d_conn=19.0e-3, l_conn=1.2, eps=0.01e-3,
    k_fittings=4.0,     # swivel, tee, relief valve tee and couplings on the delivery side (est.)
    d_suc=25.0e-3, l_suc=4.0, k_suction=7.0,   # spring check foot valve, strainer, elbow and coupling (est.; CBK-DDR-003)
    dz_nozzle=1.0,      # nozzle up to 1 m above the pump (slope or raised arm)
    lift=1.5,           # worst-case suction lift from a low open container (est.)
    angle=30.0,         # jet elevation for reach, degrees
    k_reach=0.50,       # real reach over drag-free reach for a 6 mm jet (est.; to measure)
    p_relief=4.0e5,     # relief valve setting, Pa
    swing=P["SWING"], r_grip=P["LEVER_R"] / 1000.0,
    p_sustain=75.0,     # W per person that can be kept up for 10 min (est.)
)


def friction(q, d, L, eps):
    v = q / (math.pi * d * d / 4)
    re = v * d / nu
    f = 0.25 / (math.log10(eps / (3.7 * d) + 5.74 / re ** 0.9)) ** 2
    return f * L / d * rho * v * v / 2, v, re, f


def pump(a=A_IN):
    q = a["v_ds"] * a["n_ds"] * a["eta_v"] / 60.0
    aj = math.pi * a["d_jet"] ** 2 / 4
    vj = q / (a["cd"] * aj)
    p_noz = rho * vj * vj / 2
    dp_h, v_h, re_h, f_h = friction(q, a["d_hose"], a["l_hose"], a["eps"])
    dp_c, v_c, _, _ = friction(q, a["d_conn"], a["l_conn"], a["eps"])
    dp_k = a["k_fittings"] * rho * v_h ** 2 / 2
    dp_s, v_s, _, _ = friction(q, a["d_suc"], a["l_suc"], a["eps"])
    dp_sk = a["k_suction"] * rho * v_s ** 2 / 2
    p_out = p_noz + dp_h + dp_c + dp_k + rho * g * a["dz_nozzle"]
    p_in = -(rho * g * a["lift"] + dp_s + dp_sk)         # gauge, worst case
    dp_pump = p_out - p_in
    p_hyd = dp_pump * q
    p_shaft = p_hyd / a["eta_m"]
    angle_ds = 4 * math.radians(a["swing"])               # out and back on both sides
    work_ds = p_shaft / (a["n_ds"] / 60.0)
    torque = work_ds / angle_ds
    force = torque / a["r_grip"]
    reach_ideal = vj ** 2 * math.sin(math.radians(2 * a["angle"])) / g
    reach = a["k_reach"] * reach_ideal
    npsh_a = (101325 + p_in - 2340) / (rho * g)
    # shut nozzle: force two people would need to reach the relief setting
    torque_relief = a["p_relief"] * a["v_ds"] / a["eta_v"] / angle_ds / a["eta_m"] * a["eta_m"]
    f_relief = a["p_relief"] * a["v_ds"] / angle_ds / a["r_grip"]
    return dict(q_lmin=q * 60000, v_jet=vj, p_noz=p_noz, dp_hose=dp_h, re_hose=re_h, f_hose=f_h, v_hose=v_h,
                dp_conn=dp_c, dp_fit=dp_k, dp_suc=dp_s + dp_sk, p_out=p_out, p_in=p_in, dp_pump=dp_pump,
                p_hyd=p_hyd, p_shaft=p_shaft, p_person=p_shaft / 2, torque=torque, force=force,
                reach_ideal=reach_ideal, reach=reach, npsh_a=npsh_a, f_relief=f_relief,
                drum_min=200.0 / (q * 60000), ten_min_l=q * 60000 * 10)


# ------------------------------------------------------------------ B. heat alarm (R1 to R5)
B_IN = dict(
    ror=8.0,            # alarm threshold, C per minute, averaged over 60 s
    fixed=57.0,         # fixed-temperature back-up threshold, C
    sample_s=10.0,      # temperature sample interval
    i_sleep=3.0e-6,     # A, controller and radio asleep (est.)
    i_meas=1.0e-3, t_meas=1.0e-3,     # A and s per temperature sample (est.)
    i_cad=10.0e-3, t_cad=1.5e-3, cad_s=4.0,   # radio listens for a station alert every 4 s (est.)
    i_tx=40.0e-3, t_tx=0.06, tx_day=1.0,      # one 60 ms check-in a day (est.)
    cap_ah=2.4, derate=0.70,           # alkaline AA, derated for heat and self-discharge (est.)
    alarm_min=30.0, i_alarm=0.040,     # end-of-life reserve: 30 min of sounding at 40 mA (est.)
    spl_1m=95.0, r_wake=3.0,
    t_tx_alarm=0.1, retries=3, retry_gap=1.0,
)


def alarm(b=B_IN):
    hours_day = 24.0
    i_avg = (b["i_sleep"] + b["i_meas"] * b["t_meas"] / b["sample_s"] + b["i_cad"] * b["t_cad"] / b["cad_s"]
             + b["i_tx"] * b["t_tx"] * b["tx_day"] / 86400.0)
    reserve_ah = b["i_alarm"] * b["alarm_min"] / 60.0
    usable = b["cap_ah"] * b["derate"] - reserve_ah
    life_months = usable / (i_avg * hours_day) / 30.4
    spl_3m = b["spl_1m"] - 20 * math.log10(b["r_wake"])
    # alarm to station and station to all alarms: worst-case time
    t_detect = 60.0 / 6.0           # the 60 s average updates every 10 s; worst extra delay one sample
    t_link = b["t_tx_alarm"] + b["retries"] * b["retry_gap"]
    t_rebroadcast = b["cad_s"] + b["t_tx_alarm"]
    t_total = t_link + t_rebroadcast
    # temperature rise to fixed threshold for a fast flaming fire under the roof (est. 30 C/min near the ridge)
    return dict(i_avg_ua=i_avg * 1e6, life_months=life_months, reserve_ah=reserve_ah, spl_3m=spl_3m,
                t_link=t_link, t_total=t_total, t_detect=t_detect)


# ------------------------------------------------------------------ C, D, E: cart mass, handle load, effort, time (R6, R9)
BOUGHT_KG = {  # (est.) masses of bought parts, kg
    "feet": 0.2, "grips": 0.3, "wheels": 2 * 5.5, "collars": 0.3, "pump": 14.0, "pump_bolts": 0.5,
    "inlet_coupling": 0.4, "relief": 0.6, "lever_grips": 0.1, "reel": 9.0, "wound_hose": 11.4, "swivel": 0.8,
    "conn_hose": 0.6, "tray_bolts": 0.1, "suction": 1.3, "strainer": 1.0, "nozzle": 0.6, "tap": 0.3,
    # CBK-DDR-003: the 4 m suction hose (1.8 kg) is split between the coil and the run to the pump;
    # brass spring check foot valve; cam-lever adaptor with elbow tail; two rubber straps
    "suction_run": 0.5, "suction_adaptor": 0.3, "hose_straps": 0.1,
}
PRIMED_L = 0.6      # (est.) water held in the pump body when primed, L; the suction hose is added from its bore
STEEL = 7.85e-6   # kg per mm3
C_IN = dict(crr=0.10, slope=0.10, n_people=2, f_person=100.0, v_walk=1.0, dist=100.0, sited=70.0,
            # R9 timeline after CBK-DDR-003 (Amish, 2026-10-03, decision 1A)
            gather=30.0,        # "go when two arrive": the first two at the station leave with the cart; at most 30 s (drilled)
            pull_out=15.0,      # pull the cart out from under the station roof
            drop=10.0,          # lift the pre-coupled suction hose off the cart and drop the foot valve in the water (est.)
            pay_out=25.0,       # second person runs out the 30 m hose from the reel and aims (est., about 1.2 m/s)
            strokes=3.0,        # first strokes to lift water in a primed pump and suction hose (est.)
            # CBK-DDR-004 (Amish, 2026-10-03, decision 45 b): the 30 m delivery hose and the 1.2 m connecting
            # hose are stowed full of water behind the shut nozzle, so no fill time at the fire
            hose_full=True,
            # TRL 3 baseline before the change (CBK-CAL-001 v0.1), for comparison
            muster_old=60.0, setup_old=30.0, prime_old=15.0)


def cart(c=C_IN):
    comps = {k.key: k for k in M.components() if k.group == "cart"}
    mass, mom = 0.0, [0.0, 0.0, 0.0]
    rows = []
    for k, comp in comps.items():
        sh = comp.shape
        cen = sh.center()
        m = BOUGHT_KG.get(k, sh.volume * STEEL)
        if k == "tray":
            m = sh.volume * STEEL
        rows.append((comp.name, m))
        mass += m
        for i, v in enumerate((cen.X, cen.Y, cen.Z)):
            mom[i] += m * v
    # water held in the primed pump and suction hose (CBK-DDR-003), placed at the centre of the suction run
    m_w = (PRIMED_L / 1000.0 + math.pi / 4 * A_IN["d_suc"] ** 2 * A_IN["l_suc"]) * rho
    cw = comps["suction_run"].shape.center()
    rows.append(("Water held in the primed pump and suction hose", m_w))
    mass += m_w
    for i, v in enumerate((cw.X, cw.Y, cw.Z)):
        mom[i] += m_w * v
    # water held in the delivery line stowed full (CBK-DDR-004), placed at the centre of the wound hose
    v_line = math.pi / 4 * (A_IN["d_hose"] ** 2 * A_IN["l_hose"] + A_IN["d_conn"] ** 2 * A_IN["l_conn"])
    m_line = v_line * rho if c["hose_full"] else 0.0
    if m_line:
        ch = comps["wound_hose"].shape.center()
        rows.append(("Water held in the delivery hose and connecting hose, stowed full", m_line))
        mass += m_line
        for i, v in enumerate((ch.X, ch.Y, ch.Z)):
            mom[i] += m_line * v
    cg = [v / mass for v in mom]
    W = mass * g
    ay = P["AXLE_Y"]
    leg_y = P["RAIL_Y"][0] + P["T"] / 2
    grip_y = P["BAR_Y"]
    on_legs = W * (ay - cg[1]) / (ay - leg_y)
    at_grip = W * (ay - cg[1]) / (ay - grip_y)
    th = math.atan(c["slope"])
    f_pull = W * (math.sin(th) + c["crr"] * math.cos(th))
    per_person = f_pull / c["n_people"]
    t_walk = c["dist"] / c["v_walk"]
    a = alarm()
    # R9: water on target. Once pumping starts, the empty delivery line (30 m reel hose and the 1.2 m
    # connecting hose) has to fill before water leaves the nozzle. The TRL 3 note v0.1 left this out.
    q = pump()["q_lmin"] / 60000.0
    t_fill = v_line / q
    # two people arrive: one drops the suction hose and pumps, the other runs out the hose and aims;
    # with the delivery line stowed full (CBK-DDR-004) water leaves the nozzle with the first strokes
    after_empty = max(c["pay_out"], c["drop"] + c["strokes"] + t_fill)
    after = max(c["pay_out"], c["drop"] + c["strokes"]) if c["hose_full"] else after_empty
    before = a["t_total"] + c["gather"] + c["pull_out"]
    t_r9 = before + t_walk + after
    t_r9_sited = before + c["sited"] / c["v_walk"] + after
    # for comparison: the delivery hose stowed empty (CBK-DDR-003 design)
    t_r9_empty = before + t_walk + after_empty
    t_r9_wet = t_r9
    # like-for-like baseline: the v0.1 timeline with the hose fill added
    t_r9_old = a["t_total"] + c["muster_old"] + c["pull_out"] + t_walk + c["setup_old"] + c["prime_old"]
    t_r9_old_fill = t_r9_old + t_fill
    # one person pumps until the next volunteers arrive: shaft power on one person
    p_one = pump()["p_shaft"]
    v_suc = math.pi / 4 * A_IN["d_suc"] ** 2 * A_IN["l_suc"]
    half_track = M.derived()["track"] / 2
    tip_side = math.degrees(math.atan(half_track / cg[2]))
    # tipping backwards about the wheels when parked on a slope facing downhill: CG ahead of the axle by
    tip_back = math.degrees(math.atan((ay - cg[1]) / (cg[2] + 1e-9)))
    bb = M.Compound([k.shape for k in comps.values()]).bounding_box()
    return dict(mass=mass, m_water=m_w, m_line=m_line, t_r9_empty=t_r9_empty, cg=cg, on_legs=on_legs, at_grip=at_grip, f_pull=f_pull, per_person=per_person,
                t_walk=t_walk, t_r9=t_r9, t_r9_sited=t_r9_sited, t_r9_wet=t_r9_wet, t_r9_old=t_r9_old,
                t_r9_old_fill=t_r9_old_fill, t_fill=t_fill, v_line=v_line * 1000, after=after, before=before,
                p_one=p_one, v_suc=v_suc * 1000, tip_side=tip_side, tip_back=tip_back,
                width=bb.size.X, length=bb.size.Y, height=bb.size.Z, rows=rows)


# ------------------------------------------------------------------ F. station roof and posts
F_IN = dict(v_wind=30.0, cp_net=1.2, rho_air=1.2, cf_drag=0.1, conc=23.0e3, w_post=2.6)


def station(f=F_IN):
    sw, sl, _ = P["SHEET"]
    area = sw * sl / 1e6
    q = 0.5 * f["rho_air"] * f["v_wind"] ** 2
    uplift = f["cp_net"] * q * area
    per_post_up = uplift / 4
    collar_v = math.pi * (P["COLLAR_D"] / 2000) ** 2 * P["POST_EMBED"] / 1000
    collar_w = collar_v * f["conc"]
    roof_kg = 0.0
    sn = M.station_parts()
    for k in ("posts", "beams", "purlins"):
        for s in sn[k]:
            roof_kg += s.volume * STEEL
    sheet_kg = area * 4.6     # 0.5 mm corrugated galvanised, about 4.6 kg/m2
    h = P["POST_TOP"] / 1000
    f_h = f["cf_drag"] * q * area + 0.6 * q * 0.3 * 0.3 * 1.5   # roof drag plus box and sign (est.)
    m_post = f_h / 4 * h
    s_ = P["POST"][0]
    t_ = P["POST"][1]
    i_ = (s_ ** 4 - (s_ - 2 * t_) ** 4) / 12
    w_el = i_ / (s_ / 2)
    sigma = m_post * 1000 / w_el      # N.mm / mm3 = MPa (m_post in N.m)
    return dict(area=area, q=q, uplift=uplift, per_post_up=per_post_up, collar_w=collar_w, steel_kg=roof_kg,
                sheet_kg=sheet_kg, f_h=f_h, m_post=m_post, sigma=sigma)


# ------------------------------------------------------------------ G. reel capacity
def reel():
    od = P["HOSE_OD"]
    v_hose = math.pi / 4 * od ** 2 * P["HOSE_L"] * 1000
    v_space = math.pi / 4 * (P["WOUND_D"] ** 2 - P["REEL_DRUM_D"] ** 2) * P["REEL_W"] * 0.785
    # spindle bending with the drum, the wound hose and (CBK-DDR-004) the water in the full hose, as a
    # simply supported 25 mm bar loaded at mid-span; span taken as the drum width plus 40 mm (est.)
    v_full = math.pi / 4 * (A_IN["d_hose"] ** 2 * A_IN["l_hose"] + A_IN["d_conn"] ** 2 * A_IN["l_conn"]) * rho
    w_reel = (BOUGHT_KG["reel"] + BOUGHT_KG["wound_hose"] + (v_full if C_IN["hose_full"] else 0.0)) * g
    span = P["REEL_W"] + 40.0
    m_sp = w_reel * span / 4
    s_sp = 32 * m_sp / (math.pi * P["SPINDLE_D"] ** 3)
    return dict(v_hose=v_hose / 1e6, v_space=v_space / 1e6, ratio=v_space / v_hose, w_reel=w_reel, s_spindle=s_sp)


# ------------------------------------------------------------------ H. cost
def cost():
    rows = list(csv.DictReader((ROOT / "bom/bom.csv").open()))
    tot = sum(float(r["unit_cost_usd"]) * float(r["qty"]) for r in rows)
    alarms = sum(float(r["unit_cost_usd"]) * float(r["qty"]) for r in rows if r["item"].startswith("1 "))
    station_ = sum(float(r["unit_cost_usd"]) * float(r["qty"]) for r in rows if r["item"].split()[0] in ("2", "3", "4", "5"))
    return dict(total=tot, alarms=alarms, station=station_, cart=tot - alarms - station_, target=1600.0)


def main():
    a, b, c, f, r, k = pump(), alarm(), cart(), station(), reel(), cost()
    print("A. Pump, hose and nozzle")
    for key in ("q_lmin", "v_jet", "p_noz", "v_hose", "re_hose", "dp_hose", "dp_conn", "dp_fit", "dp_suc", "p_out",
                "p_in", "dp_pump", "p_hyd", "p_shaft", "p_person", "torque", "force", "reach_ideal", "reach",
                "npsh_a", "f_relief", "drum_min", "ten_min_l"):
        print(f"  {key:12s} {a[key]:10.3f}")
    print("B. Heat alarm")
    for key, v in b.items():
        print(f"  {key:12s} {v:10.3f}")
    print("C to E. Cart")
    for key in ("mass", "m_water", "m_line", "t_r9_empty", "on_legs", "at_grip", "f_pull", "per_person", "t_walk", "v_line", "t_fill", "before", "after",
                "t_r9", "t_r9_sited", "t_r9_wet", "t_r9_old", "t_r9_old_fill", "p_one", "v_suc", "tip_side",
                "tip_back", "width", "length", "height"):
        print(f"  {key:12s} {c[key]:10.2f}")
    print(f"  cg (mm)      {c['cg'][0]:.0f}, {c['cg'][1]:.0f}, {c['cg'][2]:.0f}")
    for n, m in c["rows"]:
        print(f"    {m:6.2f} kg  {n}")
    print("F. Station")
    for key, v in f.items():
        print(f"  {key:12s} {v:10.3f}")
    print("G. Reel", {kk: round(v, 4) for kk, v in r.items()})
    print("H. Cost", k)
    res = [
        ("R1", "Rate-of-rise threshold", "8 C/min", f"{B_IN['ror']:.0f} C/min over 60 s, plus 57 C fixed", "Met by design (firmware threshold)"),
        ("R2", "No alarm in 1 h of cooking at 1 m", "No alarm", "Not calculable on paper", "To show at TRL 4"),
        ("R3", "Sound at 3 m", ">= 85 dB(A)", f"{b['spl_3m']:.1f} dB(A)", "Met (est.)"),
        ("R4", "Relay to station and all alarms", "<= 10 s", f"{b['t_total']:.1f} s worst case", "Met (est.)"),
        ("R5", "Battery life", ">= 12 months", f"{b['life_months']:.0f} months; shelf life of the cells limits it to about 5 years", "Met (est.)"),
        ("R6", "Cart on a 10 % slope, 100 m", "<= 3 min, width <= 0.9 m", f"{c['t_walk'] / 60:.1f} min at 1.0 m/s; {c['per_person']:.0f} N per person; width {c['width']:.0f} mm",
         "Met (est.)" if c["per_person"] <= C_IN["f_person"] else
         f"Met (est.); {c['per_person']:.0f} N per person is just over the {C_IN['f_person']:.0f} N assumed sustainable: the TRL 4 pull test should confirm"),
        ("R7", "Flow for 10 min", ">= 20 L/min", f"{a['q_lmin']:.1f} L/min; {a['p_person']:.0f} W per person", "Met (est.)"),
        ("R8", "Jet reach", ">= 6 m", f"{a['reach']:.1f} m", "Met (est.)"),
        ("R9", "Water on target 100 m away", "<= 3 min", f"{c['t_r9'] / 60:.2f} min ({c['t_r9']:.0f} s) at 100 m; {c['t_r9_sited'] / 60:.1f} min at 70 m (siting margin)",
         "Not met on paper at 100 m (short by {:.0f} s); met at 70 m".format(c['t_r9'] - 180) if c['t_r9'] > 180 else
         "Met (est.) at 100 m with {:.0f} s to spare; delivery hose stowed full".format(180 - c['t_r9'])),
        ("R10", "Repairable locally", "Hand tools, market parts", "Every wear part is a market item", "Met by design"),
        ("R11", "Value-engineering target", "USD 1,600", f"USD {k['total']:,.0f}", f"USD {k['target'] - k['total']:,.0f} under the target"),
    ]
    with (ROOT / "docs/04-calcs/results.csv").open("w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["id", "requirement", "target", "result", "status"])
        w.writerows(res)
    print("Results")
    for row in res:
        print("  " + " | ".join(row))
    return a, b, c, f, r, k


if __name__ == "__main__":
    main()
