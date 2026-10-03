"""CampBreak parametric model (build123d), TRL 3, constructable design (CBK-DDR-002).

Run from the repo root:  python3 cad/src/model.py          (exports and checks)
                         python3 cad/src/model.py --check  (constructability checks only)
Exports STEP and STL into cad/step and cad/stl:
    campbreak-assembly   block station with the hose cart parked under its roof and the water drum
    campbreak-cart       hand-pumped hose cart (frame, wheels, pump, lever, reel, hoses, tray)
    campbreak-station    block station (posts, roof, station alarm box, siren, panel, sign)
    campbreak-alarm      one rate-of-rise heat alarm on a stub of bamboo roof pole

Axes (cart and station): X across the cart (right +X), Y along it with the pull handle at -Y
(front) and the pump at +Y (rear), Z up from the ground at z = 0. The cart is parked level on its
two wheels and two front legs, under the station roof, ready to be pulled straight out to -Y.
The heat alarm has its own axes: its mounting plate top at z = 0 under a roof pole along X.

Revised 2026-10-03 (CBK-DDR-003, Amish's R9 decision): the foot valve has a positive check so the pump
and suction hose stay primed, and the suction hose is stowed coupled to the pump inlet by its cam-lever
adaptor, along the top of the left rail under two rubber straps and onto its coil in the tray.

Revised 2026-10-03 to make the concept buildable (CBK-DDR-002, "Design for construction"): every
part is a cut, drilled, welded, folded or bought item, and every joint has a fixing. Main
dimensions and interfaces only; tolerances are TRL 4 work. The same PARAMS feed
docs/04-calcs/sizing.py (CBK-CAL-001), the drawing CBK-DWG-001 (cad/src/sheets.py), the concept
media (cad/src/concept_media.py), the build plan pictures (cad/src/build_plan_media.py) and the
appearance model (cad/src/product_model.py).
"""
import math
import sys
from dataclasses import dataclass
from pathlib import Path

from build123d import (Axis, Box, Compound, Cylinder, Pos, Rot, Spline, Plane, Circle, sweep,
                       Vector, export_step, export_stl, Wire, Transition)

# Top-level parameters (mm). Edit these, not the geometry below.
P = {
    # cart frame: square tube side and wall (30 x 30 x 2 mm steel)
    "T": 30.0, "TW": 2.0,
    "RAIL_X": 300.0,            # outer face of each side rail from the centre line
    "RAIL_Y": (-650.0, 350.0),  # front and rear ends of the side rails
    "DECK_Z": 215.0,            # underside of the frame tubes above the ground
    "BEARER_X": 130.0,          # inner face of the two deck bearers from the centre line
    "CROSS_Y": {"front": -650.0, "mid": -300.0, "rear": 320.0},   # front face of each cross member
    # wheels and axle
    "WHEEL_D": 400.0, "TYRE_W": 100.0, "HUB_D": 70.0, "HUB_L": 75.0, "AXLE_D": 20.0,
    "AXLE_Y": 150.0, "AXLE_L": 850.0, "HUB_X": 330.0,          # inner face of each hub
    "AXLE_PLATE": (80.0, 8.0, 160.0),     # axle plate width (Y), thickness, bottom z
    "SPACER_D": 32.0, "COLLAR_L": 12.0,
    # legs and feet
    "FOOT": (40.0, 25.0),                 # rubber foot square, height
    # handle
    "BAR_D": 33.7, "BAR_HALF": 410.0, "BAR_Y": -1200.0, "BAR_Z": 800.0, "ARM_FOOT_Y": -628.0,
    "GRIP": (40.0, 95.0),                 # rubber grip diameter, length
    # pump stand and pump (semi-rotary double-acting hand pump, 25 mm ports)
    "STAND": (320.0, 10.0, 600.0),        # plate width (X), thickness (Y), top z
    "STAND_Y": 330.0,                     # front face of the stand plate
    "GUSSET": (8.0, 130.0, 250.0),        # thickness, length along the bearer, height at the plate
    "PUMP_Z": 440.0, "PUMP_BODY": (180.0, 95.0), "PUMP_FLANGE": (220.0, 12.0), "PUMP_PORT_D": 42.0,
    "PORT_Y": 400.0,
    # lever extension
    "LEVER_D": 33.7, "LEVER_R": 610.0, "TGRIP_D": 27.0, "TGRIP_HALF": 200.0, "SWING": 40.0,
    # hose reel (bought drum on a through spindle with a swivel inlet)
    "REEL_Y": 20.0, "REEL_Z": 535.0, "REEL_FLANGE_D": 500.0, "REEL_DRUM_D": 200.0, "REEL_W": 210.0,
    "REEL_FLANGE_T": 5.0, "SPINDLE_D": 25.0, "UPRIGHT": (50.0, 8.0, 580.0),
    "HOSE_OD": 28.0, "HOSE_L": 30.0, "WOUND_D": 440.0,
    # hose tray and what it carries
    "TRAY": (400.0, 370.0, 80.0, 1.5), "TRAY_Y": -460.0,
    "COIL": (360.0, 300.0, 70.0),          # suction hose coil outer, inner diameter, height
    # suction hose stowed coupled to the pump inlet (CBK-DDR-003): 25 mm bore, 34 mm outside,
    # run along the top of the left rail, held by two rubber straps, into the coil in the tray
    "SUC_OD": 34.0, "SUC_X": -280.0, "STRAP_Y": (-60.0, 240.0), "STRAP": (20.0, 2.0),
    # block station
    "ST_Y": 700.0, "POST": (60.0, 3.0), "POST_X": 650.0, "POST_TOP": 2400.0, "POST_EMBED": 600.0,
    "COLLAR_D": 300.0, "BEAM": (40.0, 2.0), "BEAM_Y": (-1900.0, 100.0), "FALL": 5.0,
    "POST_DY": (-1800.0, 0.0),           # front and back post centres from ST_Y
    "PURLIN": (40.0, 20.0), "PURLIN_DY": (-1870.0, -1240.0, -600.0, 40.0),
    "SHEET": (1500.0, 2050.0, 18.0),
    "BOX": (150.0, 300.0, 300.0, 1400.0), # station alarm box depth (X), width (Y), height, bottom z
    "SIREN": (110.0, 120.0, 1900.0), "PANEL": (350.0, 290.0, 25.0), "SIGN": (440.0, 300.0, 3.0, 1100.0),
    "DRUM": (585.0, 880.0), "DRUM_XY": (1050.0, 600.0),
    # heat alarm (its own axes)
    "AL_BOX": (100.0, 100.0, 40.0, 2.5), "AL_SPLIT": 22.0, "AL_PLATE": (140.0, 50.0, 3.0),
    "AL_POLE_D": 80.0,
}

BOM = {  # BOM line: name
    1: "Heat alarm, complete", 2: "Station alarm box with siren and solar panel", 3: "Station shade frame and roof",
    4: "Station sign board", 5: "Water drum, 200 L", 6: "Cart frame, welded", 7: "Wheels, axle, spacers and collars",
    8: "Hand pump, semi-rotary, 25 mm ports", 9: "Lever extension with T-grip", 10: "Hose reel drum, spindle and swivel inlet",
    11: "Delivery hose 19 mm x 30 m and connecting hose", 12: "Nozzle, jet and spray, with shut-off",
    13: "Suction hose 25 mm x 4 m with check foot valve", 14: "Quick couplings, 25 mm", 15: "Tap adaptor",
    16: "Hose tray", 17: "Fasteners", 18: "Paint, reflective tape, labels and drill card", 19: "Pressure relief valve, 4 bar",
    20: "Suction hose straps",
}


@dataclass
class Comp:
    key: str
    name: str
    shape: object
    color: str
    bom: int
    explode: tuple = (0.0, 0.0, 0.0)
    group: str = "cart"        # cart, station, alarm
    make: str = "buy"          # how it is made


# ---------------------------------------------------------------- primitives
def bx(x0, x1, y0, y1, z0, z1):
    return Pos((x0 + x1) / 2, (y0 + y1) / 2, (z0 + z1) / 2) * Box(x1 - x0, y1 - y0, z1 - z0)


def tube(x0, x1, y0, y1, z0, z1, axis, wall):
    """Rectangular hollow section between two corners, hollow along axis 'x', 'y' or 'z'."""
    o = bx(x0, x1, y0, y1, z0, z1)
    w = wall
    if axis == "x":
        i = bx(x0 - 1, x1 + 1, y0 + w, y1 - w, z0 + w, z1 - w)
    elif axis == "y":
        i = bx(x0 + w, x1 - w, y0 - 1, y1 + 1, z0 + w, z1 - w)
    else:
        i = bx(x0 + w, x1 - w, y0 + w, y1 - w, z0 - 1, z1 + 1)
    return o - i


def cyl(axis, c, r, a0, a1):
    """Cylinder of radius r along axis from a0 to a1; c is the (u, v) centre in the other two axes."""
    h = a1 - a0
    m = (a0 + a1) / 2
    if axis == "x":
        return Pos(m, c[0], c[1]) * Rot(0, 90, 0) * Cylinder(r, h)
    if axis == "y":
        return Pos(c[0], m, c[1]) * Rot(90, 0, 0) * Cylinder(r, h)
    return Pos(c[0], c[1], m) * Cylinder(r, h)


def pipe(axis, c, ro, ri, a0, a1):
    return cyl(axis, c, ro, a0, a1) - cyl(axis, c, ri, a0 - 1, a1 + 1)


def fuse(shapes):
    shapes = list(shapes)
    out = shapes[0]
    for s in shapes[1:]:
        out = out + s
    return out


def mirror_x(shape):
    return shape.mirror(Plane.YZ)


def strut(p0, p1, side, depth, ext=0.0):
    """Square-section member (side x depth) between points p0 and p1 in a Y-Z plane at x = p0[0],
    extended by ext past each end. side runs along X, depth in the Y-Z plane."""
    a = Vector(*p0)
    b = Vector(*p1)
    d = (b - a)
    L = d.length
    u = d / L
    ang = math.degrees(math.atan2(u.Z, u.Y))  # angle of the member above +Y in the Y-Z plane
    mid = (a + b) / 2
    return Pos(mid.X, mid.Y, mid.Z) * Rot(ang, 0, 0) * Box(side, L + 2 * ext, depth)


# ---------------------------------------------------------------- derived values
def derived(p=P):
    T = p["T"]
    z0, z1 = p["DECK_Z"], p["DECK_Z"] + T
    ax_z = p["WHEEL_D"] / 2
    hub_c = p["HUB_X"] + p["HUB_L"] / 2
    return dict(z0=z0, z1=z1, ax_z=ax_z, hub_c=hub_c, track=2 * hub_c,
                width=2 * (hub_c + p["TYRE_W"] / 2), rail_in=p["RAIL_X"] - T,
                bear0=p["BEARER_X"], bear1=p["BEARER_X"] + T,
                stand_back=p["STAND_Y"] + p["STAND"][1])


# ---------------------------------------------------------------- cart
def cart_frame_parts(p=P):
    """The welded cart frame, as separate pieces (for checks and making sketches)."""
    T, W = p["T"], p["TW"]
    D = derived(p)
    z0, z1 = D["z0"], D["z1"]
    X, ri = p["RAIL_X"], D["rail_in"]
    y0, y1 = p["RAIL_Y"]
    b0, b1 = D["bear0"], D["bear1"]
    cy = p["CROSS_Y"]
    pc = {}
    pc["rails"] = [tube(-X, -ri, y0, y1, z0, z1, "y", W), tube(ri, X, y0, y1, z0, z1, "y", W)]
    pc["cross_front"] = [tube(-ri, ri, cy["front"], cy["front"] + T, z0, z1, "x", W)]
    pc["cross_rear"] = [tube(-ri, ri, cy["rear"], cy["rear"] + T, z0, z1, "x", W)]
    m0 = cy["mid"]
    pc["cross_mid"] = [tube(-ri, -b1, m0, m0 + T, z0, z1, "x", W), tube(-b0, b0, m0, m0 + T, z0, z1, "x", W),
                       tube(b1, ri, m0, m0 + T, z0, z1, "x", W)]
    bf, br = cy["front"] + T, cy["rear"]
    pc["bearers"] = [tube(-b1, -b0, bf, m0, z0, z1, "y", W), tube(-b1, -b0, m0 + T, br, z0, z1, "y", W),
                     tube(b0, b1, bf, m0, z0, z1, "y", W), tube(b0, b1, m0 + T, br, z0, z1, "y", W)]
    fh, ft = p["FOOT"]
    pc["legs"] = [tube(-X, -ri, y0, y0 + T, ft, z0, "z", W), tube(ri, X, y0, y0 + T, ft, z0, "z", W)]
    aw, at, ab = p["AXLE_PLATE"]
    ay, az, ar = p["AXLE_Y"], D["ax_z"], p["AXLE_D"] / 2 + 0.5
    plates = []
    for s in (-1, 1):
        for xa, xb in ((X, X + at), (ri - at, ri)):
            pl = bx(min(s * xa, s * xb), max(s * xa, s * xb), ay - aw / 2, ay + aw / 2, ab, z1)
            plates.append(pl - cyl("x", (ay, az), ar, -500, 500))
    pc["axle_plates"] = plates
    return pc


def handle_parts(p=P):
    T, W = p["T"], p["TW"]
    D = derived(p)
    X, ri = p["RAIL_X"], D["rail_in"]
    by, bz, br = p["BAR_Y"], p["BAR_Z"], p["BAR_D"] / 2
    bar_env = cyl("x", (by, bz), br, -p["BAR_HALF"], p["BAR_HALF"])
    bar = bar_env - cyl("x", (by, bz), br - 2.6, -p["BAR_HALF"] - 1, p["BAR_HALF"] + 1)
    arms = []
    for s in (-1, 1):
        xc = s * (X - T / 2)
        foot, top = (0, p["ARM_FOOT_Y"], D["z1"]), (0, by, bz)
        keep = bx(xc - 50, xc + 50, -2000, 0, D["z1"], 3000)
        env = ((Pos(xc, 0, 0) * strut(foot, top, T, T, ext=40)) & keep) - bar_env
        inner = (Pos(xc, 0, 0) * strut(foot, top, T - 2 * W, T - 2 * W, ext=60)) & keep
        arms.append(env - inner)
    gd, gl = p["GRIP"]
    grips = [cyl("x", (by, bz), gd / 2, s * p["BAR_HALF"] - gl if s > 0 else -p["BAR_HALF"],
                 s * p["BAR_HALF"] if s > 0 else -p["BAR_HALF"] + gl) - bar_env for s in (-1, 1)]
    return dict(arms=arms, bar=[bar], grips=grips, bar_env=bar_env)


def stand_parts(p=P):
    D = derived(p)
    w, t, top = p["STAND"]
    sy = p["STAND_Y"]
    plate = bx(-w / 2, w / 2, sy, sy + t, D["z1"], top)
    gt, gl, gh = p["GUSSET"]
    gus = []
    gx = D["bear0"] + p["T"] / 2
    for s in (-1, 1):
        x0 = s * gx - gt / 2
        # triangle in the Y-Z plane: along the bearer top from sy - gl to sy, up the plate to gh
        from build123d import Polyline, make_face, extrude
        tri = make_face(Polyline((sy - gl, D["z1"]), (sy, D["z1"]), (sy, D["z1"] + gh), close=True))
        sol = extrude(Plane.YZ.offset(x0) * tri, amount=gt)
        gus.append(sol)
    return dict(stand_plate=[plate], gussets=gus)


def pump_parts(p=P):
    D = derived(p)
    sy = D["stand_back"]
    zc = p["PUMP_Z"]
    fd, ft = p["PUMP_FLANGE"]
    bd, bl = p["PUMP_BODY"]
    flange = cyl("y", (0, zc), fd / 2, sy, sy + ft)
    body = cyl("y", (0, zc), bd / 2, sy + ft, sy + ft + bl)
    boss = cyl("y", (0, zc), 25, sy + ft + bl, sy + ft + bl + 20)
    pr = p["PUMP_PORT_D"] / 2
    py = p["PORT_Y"]
    inlet = cyl("z", (0, py), pr, zc - bd / 2 - 60, zc - bd / 2 + 20)
    outlet = cyl("z", (0, py), pr, zc + bd / 2 - 20, 600.0)
    tail = cyl("z", (0, py), 13, 600.0, 640.0)
    pump = fuse([flange, body, boss, inlet, outlet, tail])
    bolts = fuse([cyl("y", (s1 * 75, zc + s2 * 75), 9.5, sy + ft, sy + ft + 8) for s1 in (-1, 1) for s2 in (-1, 1)]
                 + [cyl("y", (s1 * 75, zc + s2 * 75), 9.5, p["STAND_Y"] - 10, p["STAND_Y"]) for s1 in (-1, 1) for s2 in (-1, 1)])
    zi = zc - bd / 2 - 60
    coupling = cyl("z", (0, py), 25, zi - 45, zi)
    # the suction hose's cam-lever adaptor stays coupled in the coupler (CBK-DDR-003); a 90 deg elbow
    # hose tail under it turns the hose towards the left rail
    ze = zi - 100
    adaptor = fuse([cyl("z", (0, py), 22, zi - 80, zi - 45), cyl("z", (0, py), 15, ze, zi - 80),
                    cyl("x", (py, ze), 15, -55, 0)])
    zr = zc + bd / 2 + 35
    relief = fuse([cyl("x", (py, zr), 12, pr - 1, 70), cyl("z", (85, py), 18, zr - 30, zr + 45),
                   cyl("z", (85, py), 8, zr - 65, zr - 30)])
    relief = relief - cyl("z", (0, py), pr, 0, 1000)
    return dict(pump=[pump], pump_bolts=[bolts], inlet_coupling=[coupling], suction_adaptor=[adaptor], relief=[relief])


def lever_parts(p=P, swing=0.0):
    D = derived(p)
    zc = p["PUMP_Z"]
    y0 = D["stand_back"] + p["PUMP_FLANGE"][1] + p["PUMP_BODY"][1] + 20
    hub = bx(-25, 25, y0, y0 + 38, zc - 25, zc + 25)
    ly = y0 + 19
    lr = p["LEVER_D"] / 2
    ztop = zc + p["LEVER_R"]
    tgrip_env = cyl("x", (ly, ztop), p["TGRIP_D"] / 2, -p["TGRIP_HALF"], p["TGRIP_HALF"])
    lever = pipe("z", (0, ly), lr, lr - 2.6, zc + 25, ztop) - tgrip_env
    tgrip = tgrip_env - cyl("x", (ly, ztop), p["TGRIP_D"] / 2 - 2.3, -p["TGRIP_HALF"] - 1, p["TGRIP_HALF"] + 1)
    grips = [cyl("x", (ly, ztop), 17, s * p["TGRIP_HALF"] - 100 if s > 0 else -p["TGRIP_HALF"],
                 p["TGRIP_HALF"] if s > 0 else -p["TGRIP_HALF"] + 100) - tgrip_env for s in (-1, 1)]
    out = dict(lever_hub=[hub], lever=[lever], tgrip=[tgrip], lever_grips=grips)
    if swing:
        for k in out:
            out[k] = [Pos(0, 0, zc) * Rot(0, swing, 0) * Pos(0, 0, -zc) * s for s in out[k]]
    return out


def reel_parts(p=P):
    yc, zc = p["REEL_Y"], p["REEL_Z"]
    hw = p["REEL_W"] / 2
    ft = p["REEL_FLANGE_T"]
    fr = p["REEL_FLANGE_D"] / 2
    drum = pipe("x", (yc, zc), p["REEL_DRUM_D"] / 2, p["REEL_DRUM_D"] / 2 - 3, -hw, hw)
    flanges = [cyl("x", (yc, zc), fr, -hw - ft, -hw) - cyl("x", (yc, zc), 13, -500, 500),
               cyl("x", (yc, zc), fr, hw, hw + ft) - cyl("x", (yc, zc), 13, -500, 500)]
    uw, ut, utop = p["UPRIGHT"]
    D = derived(p)
    b0 = D["bear0"]
    ups = [bx(s * b0 - (ut if s > 0 else 0) if s > 0 else -b0, s * b0 if s > 0 else -b0 + ut, yc - uw / 2, yc + uw / 2,
              D["z0"], utop) for s in (-1, 1)]
    ups = [bx(-b0, -b0 + ut, yc - uw / 2, yc + uw / 2, D["z0"], utop),
           bx(b0 - ut, b0, yc - uw / 2, yc + uw / 2, D["z0"], utop)]
    ups = [u - cyl("x", (yc, zc), p["SPINDLE_D"] / 2 + 0.5, -500, 500) for u in ups]
    spacers = [pipe("x", (yc, zc), 20, 13, -(b0 - ut), -hw - ft), pipe("x", (yc, zc), 20, 13, hw + ft, b0 - ut)]
    spindle = cyl("x", (yc, zc), p["SPINDLE_D"] / 2, -b0 - 10, b0 + 20)
    collar = pipe("x", (yc, zc), 20, 12.5, -b0 - 10, -b0)
    sw0 = b0 + 2
    swivel = fuse([cyl("x", (yc, zc), 22.5, sw0, sw0 + 40),
                   cyl("y", (sw0 + 20, zc), 13, yc, yc + 60)])
    wound = pipe("x", (yc, zc), p["WOUND_D"] / 2, p["REEL_DRUM_D"] / 2, -hw + 0.5, hw - 0.5)
    return dict(reel_drum=[drum] + flanges, reel_uprights=ups, reel_spacers=spacers, spindle=[spindle, collar],
                swivel=[swivel], wound_hose=[wound])


def connecting_hose(p=P):
    D = derived(p)
    b0 = D["bear0"]
    yc, zc = p["REEL_Y"], p["REEL_Z"]
    py = p["PORT_Y"]
    x1 = b0 + 2 + 20
    pts = [(0, py, 640.0), (40, py, 705.0), (x1, 300, 705.0), (x1, 170, 575.0), (x1, yc + 60, zc)]
    path = Spline(*pts, tangents=[(0, 0, 1), (0, -1, 0)])
    prof = Plane(origin=pts[0], z_dir=(0, 0, 1)) * Circle(p["HOSE_OD"] / 2)
    return sweep(prof, path)


def connecting_hose_segments(p=P, n=10):
    """The same hose as connecting_hose() drawn as straight segments with round joints, for 2D views
    (the swept spline projects to curves the SVG exporter cannot write)."""
    from build123d import Sphere
    D = derived(p)
    b0 = D["bear0"]
    yc, zc = p["REEL_Y"], p["REEL_Z"]
    py = p["PORT_Y"]
    x1 = b0 + 2 + 20
    pts = [(0, py, 640.0), (40, py, 705.0), (x1, 300, 705.0), (x1, 170, 575.0), (x1, yc + 60, zc)]
    sp = Spline(*pts, tangents=[(0, 0, 1), (0, -1, 0)])
    r = p["HOSE_OD"] / 2
    q = [sp @ (i / n) for i in range(n + 1)]
    segs = []
    for a, b in zip(q[:-1], q[1:]):
        d = b - a
        segs.append(Pos(*((a + b) / 2)) * (Plane(origin=(0, 0, 0), z_dir=d.normalized()) * Cylinder(r, d.length)))
    segs += [Pos(*v) * Sphere(r) for v in q[1:-1]]
    return fuse(segs)


def suction_run_path(p=P):
    """Path of the stowed suction hose (CBK-DDR-003): out of the adaptor's elbow under the pump inlet heading
    left, climbing to rail-top height, turning forward round behind the left rail end, straight along the top
    of the left rail, then up over the tray's back corner and down onto the coil. Tightest bend about 63 mm
    radius (the hose bought must allow 60 mm or less)."""
    from build123d import Line
    D = derived(p)
    r = p["SUC_OD"] / 2
    py = p["PORT_Y"]
    x = p["SUC_X"]
    ze = suction_elbow_z(p)
    zr = D["z1"] + r                                             # hose centre on the rail top
    zh = zr + 6                                                  # crossing height behind the rail end
    zt = D["z1"] + p["TRAY"][3] + p["COIL"][2] + r               # hose centre on the coil top
    yc = p["TRAY_Y"]
    y1, y2 = 310.0, -100.0                                       # straight run on the rail
    k = [1.3, 1.3]
    r1 = Spline((-55, py, ze), (-122, py, (ze + zh) / 2), (-190, py, zh), tangents=[(-1, 0, 0), (-1, 0, 0)], tangent_scalars=k)
    r2 = Spline((-190, py, zh), (-257, py - 23, (zh + zr) / 2), (x, y1, zr), tangents=[(-1, 0, 0), (0, -1, 0)], tangent_scalars=k)
    run = Line((x, y1, zr), (x, y2, zr))
    f1 = Spline((x, y2, zr), (-269, -220, zr + 52), (-224, -300, zr + 95), (-155, yc + 60, zt),
                tangents=[(0, -1, 0), (0.6, -0.8, 0)])
    return Wire([r1, r2, run, f1])


def suction_elbow_z(p=P):
    return p["PUMP_Z"] - p["PUMP_BODY"][0] / 2 - 60 - 100


def suction_run(p=P):
    path = suction_run_path(p)
    prof = Plane(origin=path @ 0, z_dir=(-1, 0, 0)) * Circle(p["SUC_OD"] / 2)
    return sweep(prof, path, transition=Transition.RIGHT)


def suction_run_segments(p=P, n=24):
    """The stowed suction hose as straight segments with round joints, for 2D views."""
    from build123d import Sphere
    sp = suction_run_path(p)
    r = p["SUC_OD"] / 2
    q = [sp @ (i / n) for i in range(n + 1)]
    segs = []
    for a, b in zip(q[:-1], q[1:]):
        d = (b - a).normalized()
        # a segment within 3 deg of an axis is drawn exactly along it: nearly edge-on circles make
        # degenerate ellipses the SVG exporter cannot write; the joint spheres hide the small step
        for ax in ((1, 0, 0), (0, 1, 0), (0, 0, 1)):
            if abs(d.dot(Vector(*ax))) > math.cos(math.radians(3)):
                d = Vector(*ax) * (1 if d.dot(Vector(*ax)) > 0 else -1)
        segs.append(Pos(*((a + b) / 2)) * (Plane(origin=(0, 0, 0), z_dir=d) * Cylinder(r, (b - a).length)))
    segs += [Pos(*v) * Sphere(r) for v in q[1:-1]]
    return fuse(segs)


def hose_straps(p=P):
    """Two rubber straps, each round the left rail and the suction hose lying on it."""
    D = derived(p)
    x, r = p["SUC_X"], p["SUC_OD"] / 2
    w, t = p["STRAP"]
    X = p["RAIL_X"]
    out = []
    for y in p["STRAP_Y"]:
        x0, x1 = -X - 0.5, x + r + 0.5
        inner = bx(x0, x1, y - w / 2 - 1, y + w / 2 + 1, D["z0"], D["z1"] + 2 * r)
        out.append(bx(x0 - t, x1 + t, y - w / 2, y + w / 2, D["z0"] - t, D["z1"] + 2 * r + t) - inner)
    return out


def tray_parts(p=P):
    D = derived(p)
    W_, L_, H_, t = p["TRAY"]
    yc = p["TRAY_Y"]
    z = D["z1"]
    outer = bx(-W_ / 2, W_ / 2, yc - L_ / 2, yc + L_ / 2, z, z + H_)
    inner = bx(-W_ / 2 + t, W_ / 2 - t, yc - L_ / 2 + t, yc + L_ / 2 - t, z + t, z + H_ + 1)
    tray = outer - inner
    for hx in (-120, 0, 120):
        for hy in (-100, 100):
            tray = tray - cyl("z", (hx, yc + hy), 6, z - 1, z + t + 1)
    co, ci, ch = p["COIL"]
    zc = z + t
    coil = pipe("z", (0, yc), co / 2, ci / 2, zc, zc + ch)
    strainer = cyl("z", (-70, yc - 60), 30, zc, zc + 100)
    nozzle = cyl("x", (yc + 70, zc + 22.5), 22.5, -95, 95)
    tap = cyl("z", (80, yc - 70), 20, zc, zc + 60)
    bolts = fuse([cyl("z", (s * (D["bear0"] + 15), yc + d), 6, zc, zc + 5) for s in (-1, 1) for d in (-120, 120)])
    return dict(tray=[tray], suction_coil=[coil], strainer=[strainer], nozzle=[nozzle], tap_adaptor=[tap],
                tray_bolts=[bolts])


def wheel_parts(p=P):
    D = derived(p)
    ay, az = p["AXLE_Y"], D["ax_z"]
    R = p["WHEEL_D"] / 2
    tw = p["TYRE_W"]
    wheels, spacers, collars = [], [], []
    for s in (-1, 1):
        xc = s * D["hub_c"]
        tyre = pipe("x", (ay, az), R, R - 70, xc - tw / 2, xc + tw / 2)
        rim = pipe("x", (ay, az), R - 70, p["HUB_D"] / 2 - 1, xc - 4, xc + 4)
        hub = pipe("x", (ay, az), p["HUB_D"] / 2, p["AXLE_D"] / 2, xc - p["HUB_L"] / 2, xc + p["HUB_L"] / 2)
        wheels.append(fuse([tyre, rim, hub]))
        xo = p["RAIL_X"] + p["AXLE_PLATE"][1]
        a0, a1 = (xo, p["HUB_X"]) if s > 0 else (-p["HUB_X"], -xo)
        spacers.append(pipe("x", (ay, az), p["SPACER_D"] / 2, p["AXLE_D"] / 2, a0, a1))
        h1 = p["HUB_X"] + p["HUB_L"]
        c0, c1 = (h1, h1 + p["COLLAR_L"]) if s > 0 else (-h1 - p["COLLAR_L"], -h1)
        collars.append(pipe("x", (ay, az), p["SPACER_D"] / 2, p["AXLE_D"] / 2, c0, c1))
    axle = cyl("x", (ay, az), p["AXLE_D"] / 2, -p["AXLE_L"] / 2, p["AXLE_L"] / 2)
    return dict(wheels=wheels, axle=[axle], wheel_spacers=spacers, collars=collars)


def feet(p=P):
    fs, fh = p["FOOT"]
    T = p["T"]
    y0 = p["RAIL_Y"][0]
    xs = p["RAIL_X"] - T / 2
    return [bx(s * xs - fs / 2, s * xs + fs / 2, y0 + T / 2 - fs / 2, y0 + T / 2 + fs / 2, 0, fh) for s in (-1, 1)]


# ---------------------------------------------------------------- station
def roof_tf(p=P):
    """Location that tilts the roof by the fall about the post tops (front edge rises)."""
    ys, zt = p["ST_Y"], p["POST_TOP"]
    return Pos(0, ys, zt) * Rot(-p["FALL"], 0, 0) * Pos(0, -ys, -zt)


def station_parts(p=P):
    ys, zt = p["ST_Y"], p["POST_TOP"]
    ps, pw = p["POST"]
    bs, bw = p["BEAM"]
    tf = roof_tf(p)
    beam_y0, beam_y1 = ys + p["BEAM_Y"][0], ys + p["BEAM_Y"][1]
    above = tf * bx(-3000, 3000, -4000, 4000, zt, zt + 3000)
    posts, post_env, collars, beams, beam_env = [], [], [], [], []
    for s in (-1, 1):
        xc = s * p["POST_X"]
        for dy in p["POST_DY"]:
            yc = ys + dy
            env = bx(xc - ps / 2, xc + ps / 2, yc - ps / 2, yc + ps / 2, -p["POST_EMBED"], zt + 400) - above
            post_env.append(env)
            posts.append(env - bx(xc - ps / 2 + pw, xc + ps / 2 - pw, yc - ps / 2 + pw, yc + ps / 2 - pw,
                                  -p["POST_EMBED"] - 1, zt + 500))
            collars.append(cyl("z", (xc, yc), p["COLLAR_D"] / 2, -p["POST_EMBED"], 0) - env)
        be = tf * bx(xc - bs / 2, xc + bs / 2, beam_y0, beam_y1, zt, zt + bs)
        beam_env.append(be)
        beams.append(tf * tube(xc - bs / 2, xc + bs / 2, beam_y0, beam_y1, zt, zt + bs, "y", bw))
    ph, pt = p["PURLIN"]
    purlins = []
    for dy in p["PURLIN_DY"]:
        y = ys + dy
        purlins.append(tf * tube(-p["SHEET"][0] / 2, p["SHEET"][0] / 2, y - ph / 2, y + ph / 2, zt + bs, zt + bs + pt, "x", 2.0))
    sw, sl, st = p["SHEET"]
    zs = zt + bs + pt
    ymid = ys + (p["PURLIN_DY"][0] + p["PURLIN_DY"][-1]) / 2
    sheet = tf * bx(-sw / 2, sw / 2, ymid - sl / 2, ymid + sl / 2, zs, zs + st)
    # station alarm box on the outside face of the left post; siren above it; panel on the roof; sign
    bd, bwid, bh, bz = p["BOX"]
    x0 = -p["POST_X"] - ps / 2
    box = bx(x0 - bd, x0, ys - bwid / 2, ys + bwid / 2, bz, bz + bh)
    sd, sh, sz = p["SIREN"]
    sbr = bx(x0 - 60, x0, ys - 30, ys + 30, sz - 6, sz)
    siren = cyl("x", (ys, sz + sd / 2 + 4), sd / 2, x0 - sh, x0 - 4) + bx(x0 - 70, x0 - 30, ys - 20, ys + 20, sz, sz + 6)
    pw_, pl_, pt_ = p["PANEL"]
    yp = ys + p["PURLIN_DY"][-1] - pl_ / 2 - 40
    panel = tf * bx(-pw_ / 2, pw_ / 2, yp - pl_ / 2, yp + pl_ / 2, zs + st + 20, zs + st + 20 + pt_)
    rails = tf * fuse([bx(-pw_ / 2 + 20, -pw_ / 2 + 50, yp - pl_ / 2 - 20, yp + pl_ / 2 + 20, zs + st, zs + st + 20),
                       bx(pw_ / 2 - 50, pw_ / 2 - 20, yp - pl_ / 2 - 20, yp + pl_ / 2 + 20, zs + st, zs + st + 20)])
    gw, gh, gt, gz = p["SIGN"]
    xs_ = p["POST_X"]
    sign = bx(xs_ - gw / 2, xs_ + gw / 2, ys - ps / 2 - gt, ys - ps / 2, gz, gz + gh)
    dd, dh = p["DRUM"]
    drum = cyl("z", p["DRUM_XY"], dd / 2, 0, dh)
    return dict(posts=posts, post_env=post_env, collars=collars, beams=beams, beam_env=beam_env,
                purlins=purlins, sheet=[sheet], station_box=[box], siren=[siren, sbr], panel=[panel],
                panel_rails=[rails], sign=[sign], drum=[drum])


# ---------------------------------------------------------------- heat alarm
def alarm_parts(p=P):
    a, b, h, w = p["AL_BOX"]
    sp = p["AL_SPLIT"]
    pw, pd, pt = p["AL_PLATE"]
    z_top = -pt
    base = bx(-a / 2, a / 2, -b / 2, b / 2, z_top - sp, z_top) - bx(-a / 2 + w, a / 2 - w, -b / 2 + w, b / 2 - w, z_top - sp - 1, z_top - w)
    cz0 = z_top - h
    cover = bx(-a / 2, a / 2, -b / 2, b / 2, cz0, z_top - sp) - bx(-a / 2 + w, a / 2 - w, -b / 2 + w, b / 2 - w, cz0 + w, z_top - sp + 1)
    for hx in (-12, 0, 12):
        for hy in (-12, 0, 12):
            if hx == 0 and hy == 0:
                continue
            cover = cover - cyl("z", (hx + 25, hy), 2.5, cz0 - 1, cz0 + w + 1)
    cover = cover - cyl("z", (0, 0), 6, cz0 - 1, cz0 + w + 1)
    plate = bx(-pw / 2, pw / 2, -pd / 2, pd / 2, -pt, 0)
    for sx in (-1, 1):
        for sy in (-1, 1):
            plate = plate - bx(sx * 58 - 4, sx * 58 + 4, min(sy * 23.8, sy * 26.8), max(sy * 23.8, sy * 26.8), -pt - 1, 1)
    inner_back = z_top - w
    batt = bx(-31, 31, -23.5, 23.5, inner_back - 16, inner_back)
    pcb_z1 = inner_back - 16 - 12
    pcb = bx(-45, 45, -45, 45, pcb_z1 - 1.6, pcb_z1)
    stand = fuse([cyl("z", (sx * 40, sy * 40), 3, pcb_z1, inner_back) for sx in (-1, 1) for sy in (-1, 1)])
    piezo = cyl("z", (25, 0), 15, pcb_z1 - 1.6 - 5, pcb_z1 - 1.6)
    guard = pipe("z", (0, 0), 12, 10, cz0 - 12, cz0) + cyl("z", (0, 0), 12, cz0 - 14, cz0 - 12)
    for k in range(6):
        ang = k * 60
        guard = guard - (Rot(0, 0, ang) * bx(9, 13, -2, 2, cz0 - 10, cz0 - 2))
    therm = cyl("z", (0, 0), 1.5, cz0 - 8, pcb_z1 - 1.6)
    pr = p["AL_POLE_D"] / 2
    pole_env = cyl("x", (0, pr), pr, -160, 160)
    ties = []
    for sx in (-1, 1):
        x0, x1 = sx * 58 - 3.5, sx * 58 + 3.5
        ring = pipe("x", (0, pr), pr + 1.6, pr, x0, x1) & bx(-500, 500, -500, 500, 8, 500)
        legs = fuse([bx(x0, x1, s_ * 24.5 - (1.6 if s_ > 0 else 0) if False else min(s_ * 24.5, s_ * 26.1),
                        max(s_ * 24.5, s_ * 26.1), -pt - 1.2, 12) for s_ in (-1, 1)])
        under = bx(x0, x1, -26.1, 26.1, -pt - 1.2, -pt)
        ties.append((ring + legs + under) - pole_env)
    pole = cyl("x", (0, p["AL_POLE_D"] / 2), p["AL_POLE_D"] / 2, -160, 160)
    screws = fuse([cyl("z", (sx * 30, 0), 4, 0, 2.5) for sx in (-1, 1)])
    return dict(al_plate=[plate], al_base=[base], al_cover=[cover], al_battery=[batt], al_pcb=[pcb],
                al_standoffs=[stand], al_piezo=[piezo], al_guard=[guard], al_thermistor=[therm],
                al_ties=ties, al_screws=[screws], al_pole=[pole])


# ---------------------------------------------------------------- components
C_STEEL = "#3F4A56"
C_RED = "#B42318"


def components(p=P):
    fr = cart_frame_parts(p)
    hd = handle_parts(p)
    st = stand_parts(p)
    pm = pump_parts(p)
    lv = lever_parts(p)
    rl = reel_parts(p)
    tr = tray_parts(p)
    wh = wheel_parts(p)
    sn = station_parts(p)
    al = alarm_parts(p)
    C = []

    def add(key, name, shapes, color, bom, explode=(0, 0, 0), group="cart", make="buy"):
        C.append(Comp(key, name, fuse(shapes) if isinstance(shapes, list) else shapes, color, bom, explode, group, make))

    # cart, in build order
    add("frame", "Base frame: rails, cross members, bearers, legs and axle plates",
        fr["rails"] + fr["cross_front"] + fr["cross_mid"] + fr["cross_rear"] + fr["bearers"] + fr["legs"] + fr["axle_plates"],
        C_RED, 6, (0, 0, 0), make="weld")
    add("feet", "Rubber feet", feet(p), "#1F2937", 17, (0, 0, -120), make="buy")
    add("handle", "Handle: two arms and a cross bar", hd["arms"] + hd["bar"], C_RED, 6, (0, -250, 150), make="weld")
    add("grips", "Handle grips", hd["grips"], "#1F2937", 6, (0, -350, 200), make="buy")
    add("stand", "Pump stand plate and gussets", st["stand_plate"] + st["gussets"], C_RED, 6, (0, 0, 300), make="weld")
    add("uprights", "Reel uprights", rl["reel_uprights"], C_RED, 6, (0, 0, 380), make="weld")
    add("axle", "Axle", wh["axle"], "#9CA3AF", 7, (0, 0, -300), make="cut")
    add("wheel_spacers", "Wheel spacers", wh["wheel_spacers"], "#9CA3AF", 7, (0, 0, -300), make="cut")
    add("wheels", "Wheels, 400 mm puncture-proof", wh["wheels"], "#111827", 7, (0, 0, -300), make="buy")
    add("collars", "Axle collars", wh["collars"], "#9CA3AF", 7, (0, 0, -300), make="buy")
    add("pump", "Hand pump, semi-rotary, 25 mm ports", pm["pump"], "#1D4ED8", 8, (0, 350, 0), make="buy")
    add("pump_bolts", "Pump bolts, 4 x M12", pm["pump_bolts"], "#9CA3AF", 17, (0, 350, 0), make="buy")
    add("relief", "Pressure relief valve, set at 4 bar", pm["relief"], "#DC2626", 19, (250, 350, 0), make="buy")
    add("inlet_coupling", "Inlet quick coupling", pm["inlet_coupling"], "#9CA3AF", 14, (0, 350, -150), make="buy")
    add("lever", "Lever extension with T-grip", lv["lever_hub"] + lv["lever"] + lv["tgrip"], "#E5A50A", 9, (0, 650, 300), make="weld")
    add("lever_grips", "T-grip sleeves", lv["lever_grips"], "#1F2937", 9, (0, 650, 300), make="buy")
    add("spindle", "Reel spindle and collar", rl["spindle"], "#9CA3AF", 10, (-500, 0, 650), make="cut")
    add("reel_spacers", "Reel spacers", rl["reel_spacers"], "#9CA3AF", 10, (0, 0, 650), make="cut")
    add("reel", "Hose reel drum", rl["reel_drum"], "#B42318", 10, (0, 0, 650), make="buy")
    add("wound_hose", "Delivery hose, 19 mm x 30 m, wound", rl["wound_hose"], "#C2410C", 11, (0, 0, 650), make="buy")
    add("swivel", "Swivel inlet", rl["swivel"], "#B8BEC6", 10, (300, 0, 650), make="buy")
    add("conn_hose", "Connecting hose, pump to reel", [connecting_hose(p)], "#111827", 11, (0, 0, 950), make="buy")
    add("tray", "Hose tray", tr["tray"], "#6B7280", 16, (0, -150, 500), make="fold")
    add("tray_bolts", "Tray bolts, 4 x M8", tr["tray_bolts"], "#9CA3AF", 17, (0, -150, 500), make="buy")
    add("suction", "Suction hose, 25 mm x 4 m, coiled", tr["suction_coil"], "#0F766E", 13, (0, -150, 750), make="buy")
    add("suction_adaptor", "Suction hose adaptor, coupled to the pump inlet", pm["suction_adaptor"], "#B8BEC6", 14,
        (0, 350, -300), make="buy")
    add("suction_run", "Suction hose run, pump inlet to the tray", [suction_run(p)], "#0F766E", 13, (-250, 0, 300), make="buy")
    add("hose_straps", "Suction hose straps, rubber", hose_straps(p), "#1F2937", 20, (-250, 0, 300), make="buy")
    add("strainer", "Foot valve with check and strainer", tr["strainer"], "#9CA3AF", 13, (0, -150, 900), make="buy")
    add("nozzle", "Nozzle, jet and spray", tr["nozzle"], "#E5A50A", 12, (0, -150, 900), make="buy")
    add("tap", "Tap adaptor", tr["tap_adaptor"], "#B8BEC6", 15, (0, -150, 900), make="buy")
    # station, in build order
    add("collars_c", "Concrete post collars", sn["collars"], "#A8A29E", 3, (0, 0, -300), "station", "cast")
    add("posts", "Station posts", sn["posts"], "#4B5563", 3, (0, 0, 0), "station", "cut")
    add("beams", "Roof beams", sn["beams"], "#4B5563", 3, (0, 0, 500), "station", "cut")
    add("purlins", "Purlins", sn["purlins"], "#6B7280", 3, (0, 0, 800), "station", "cut")
    add("sheet", "Roof sheet, corrugated", sn["sheet"], "#B8BEC6", 3, (0, 0, 1100), "station", "buy")
    add("panel", "Solar panel, 10 W, on two rails", sn["panel"] + sn["panel_rails"], "#1E3A8A", 2, (0, 0, 1400), "station", "buy")
    add("station_box", "Station alarm box", sn["station_box"], "#E5E7EB", 2, (-400, 0, 0), "station", "buy")
    add("siren", "Block siren on its bracket", sn["siren"], "#DC2626", 2, (-400, 0, 200), "station", "buy")
    add("sign", "Station sign", sn["sign"], "#0F766E", 4, (0, -300, 0), "station", "cut")
    add("drum", "Water drum, 200 L", sn["drum"], "#2563EB", 5, (500, 0, 0), "station", "buy")
    # heat alarm, in build order
    add("al_plate", "Alarm mounting plate", al["al_plate"], "#9CA3AF", 1, (0, 0, 40), "alarm", "cut")
    add("al_base", "Alarm box base", al["al_base"], "#F3F4F6", 1, (0, 0, 0), "alarm", "drill")
    add("al_battery", "Battery holder, 3 x AA alkaline", al["al_battery"], "#1F2937", 1, (0, 0, -30), "alarm", "buy")
    add("al_standoffs", "Board standoffs", al["al_standoffs"], "#9CA3AF", 1, (0, 0, -45), "alarm", "buy")
    add("al_pcb", "Alarm board (controller, radio, sensor input)", al["al_pcb"], "#166534", 1, (0, 0, -60), "alarm", "buy")
    add("al_piezo", "Piezo sounder", al["al_piezo"], "#E5A50A", 1, (0, 0, -60), "alarm", "buy")
    add("al_thermistor", "Thermistor on its lead", al["al_thermistor"], "#B42318", 1, (0, 0, -100), "alarm", "buy")
    add("al_cover", "Alarm box cover", al["al_cover"], "#F3F4F6", 1, (0, 0, -100), "alarm", "drill")
    add("al_guard", "Sensor guard", al["al_guard"], "#E5E7EB", 1, (0, 0, -140), "alarm", "print")
    add("al_screws", "Plate screws", al["al_screws"], "#9CA3AF", 17, (0, 0, 60), "alarm", "buy")
    add("al_ties", "Cable ties, UV-stable", al["al_ties"], "#111827", 1, (0, 0, 80), "alarm", "buy")
    return C


def by_key(C):
    return {c.key: c for c in C}


def alarm_pole(p=P):
    return alarm_parts(p)["al_pole"][0]


# ---------------------------------------------------------------- checks
def _vol(a, b):
    try:
        return (a & b).volume
    except Exception:
        return float("nan")


def _gap(a, b):
    try:
        return a.distance_to(b)
    except Exception:
        return float("nan")


def checks(p=P):
    C = by_key(components(p))
    fr = cart_frame_parts(p)
    hd = handle_parts(p)
    sn = station_parts(p)
    rows = []

    def chk(desc, a, b, expect, vol=True):
        v = _vol(a, b) if vol else 0.0
        g = _gap(a, b)
        ok = v < 1.0 and (g < 0.05 if expect == "touch" else g >= expect - 1e-6)
        rows.append((desc, v, g, expect, ok))

    S = lambda k: C[k].shape  # noqa: E731
    rails = fuse(fr["rails"])
    chk("Cross members against the rails", fuse(fr["cross_front"] + fr["cross_rear"] + fr["cross_mid"]), rails, "touch")
    chk("Bearers against the front and rear cross members", fuse(fr["bearers"]), fuse(fr["cross_front"] + fr["cross_rear"]), "touch")
    chk("Bearers against the middle cross member pieces", fuse(fr["bearers"]), fuse(fr["cross_mid"]), "touch")
    chk("Legs under the rails", fuse(fr["legs"]), rails, "touch")
    chk("Axle plates against the rails", fuse(fr["axle_plates"]), rails, "touch")
    chk("Feet under the legs", S("feet"), fuse(fr["legs"]), "touch")
    chk("Feet on the ground", S("feet"), bx(-2000, 2000, -3000, 3000, -50, 0), "touch")
    chk("Wheels on the ground", S("wheels"), bx(-2000, 2000, -3000, 3000, -50, 0), "touch")
    for i, arm in enumerate(hd["arms"]):
        chk(f"Handle arm {i + 1} on the rail top", arm, rails, "touch")
        chk(f"Handle arm {i + 1} coped to the cross bar", arm, fuse(hd["bar"]), "touch")
        chk(f"Handle arm {i + 1} against the end of the front cross member", arm, fuse(fr["cross_front"]), "touch")
    chk("Grips on the cross bar", S("grips"), fuse(hd["bar"]), "touch")
    stp = stand_parts(p)
    chk("Stand plate on the rear cross member", fuse(stp["stand_plate"]), fuse(fr["cross_rear"]), "touch")
    chk("Gussets on the bearers", fuse(stp["gussets"]), fuse(fr["bearers"]), "touch")
    chk("Gussets against the stand plate", fuse(stp["gussets"]), fuse(stp["stand_plate"]), "touch")
    chk("Reel uprights against the bearers", S("uprights"), fuse(fr["bearers"]), "touch")
    chk("Axle through the axle plates (clearance hole)", S("axle"), fuse(fr["axle_plates"]), 0.4)
    chk("Axle clear of the frame tubes", S("axle"), rails + fuse(fr["bearers"]), 3.0)
    chk("Axle in the wheel hubs", S("axle"), S("wheels"), "touch")
    chk("Wheel spacers between plate and hub", S("wheel_spacers"), S("wheels"), "touch")
    chk("Wheel spacers against the outer axle plates", S("wheel_spacers"), fuse(fr["axle_plates"]), "touch")
    chk("Collars against the hubs", S("collars"), S("wheels"), "touch")
    chk("Tyres clear of the axle plates", S("wheels"), fuse(fr["axle_plates"]), 5.0)
    chk("Tyres clear of the rails", S("wheels"), rails, 10.0)
    chk("Pump flange on the stand plate", S("pump"), S("stand"), "touch")
    chk("Pump clear of the rear cross member", S("pump"), fuse(fr["cross_rear"]), 10.0)
    chk("Relief valve on the pump outlet", S("relief"), S("pump"), "touch")
    chk("Relief valve clear of the stand plate", S("relief"), S("stand"), 20.0)
    chk("Relief valve clear of the connecting hose", S("relief"), S("conn_hose"), 15.0, vol=False)
    chk("Inlet coupling on the pump inlet", S("inlet_coupling"), S("pump"), "touch")
    chk("Inlet coupling clear of the frame", S("inlet_coupling"), S("frame"), 10.0)
    chk("Lever hub on the pump shaft boss", S("lever"), S("pump"), "touch")
    for ang in (-P["SWING"], P["SWING"]):
        lv = lever_parts(p, swing=ang)
        lvs = fuse(lv["lever_hub"] + lv["lever"] + lv["tgrip"] + lv["lever_grips"])
        chk(f"Lever swung {ang:+.0f} deg clear of the wheels", lvs, S("wheels"), 50.0)
        chk(f"Lever swung {ang:+.0f} deg clear of the stand and frame", lvs, S("stand") + S("frame"), 30.0)
    chk("Spindle through the reel uprights (clearance hole)", S("spindle"), S("uprights"), "touch")
    chk("Reel spacers against the drum flanges", S("reel_spacers"), S("reel"), "touch")
    chk("Reel spacers against the uprights", S("reel_spacers"), S("uprights"), "touch")
    chk("Reel flanges clear of the bearers", S("reel"), S("frame"), 30.0)
    chk("Reel clear of the stand and gussets", S("reel"), S("stand"), 20.0)
    chk("Wound hose inside the reel", S("wound_hose"), S("reel"), "touch")
    chk("Swivel clear of the right upright", S("swivel"), S("uprights"), 1.0)
    chk("Connecting hose on the pump outlet tail", S("conn_hose"), S("pump"), "touch", vol=False)
    chk("Connecting hose on the swivel tail", S("conn_hose"), S("swivel"), "touch", vol=False)
    chk("Connecting hose clear of the stand plate", S("conn_hose"), S("stand"), 20.0, vol=False)
    chk("Connecting hose clear of the reel and uprights", S("conn_hose"), S("reel") + S("uprights") + S("wound_hose"), 10.0, vol=False)
    chk("Tray on the bearers and cross members", S("tray"), S("frame"), "touch")
    chk("Tray clear of the reel", S("tray"), S("reel") + S("wound_hose"), 30.0)
    chk("Tray clear of the handle arms", S("tray"), S("handle"), 30.0)
    chk("Suction coil in the tray", S("suction"), S("tray"), "touch")
    for k in ("strainer", "nozzle", "tap"):
        chk(f"{C[k].name} on the tray floor", S(k), S("tray"), "touch")
        chk(f"{C[k].name} inside the coil", S(k), S("suction"), 2.0)
    # stowed suction hose, coupled to the pump (CBK-DDR-003)
    chk("Suction adaptor in the inlet coupler", S("suction_adaptor"), S("inlet_coupling"), "touch")
    chk("Suction adaptor clear of the frame", S("suction_adaptor"), S("frame"), 10.0)
    chk("Suction hose on the adaptor's elbow tail", S("suction_run"), S("suction_adaptor"), "touch")
    chk("Suction hose lying on the left rail top", S("suction_run"), fuse(fr["rails"]), "touch")
    chk("Suction hose clear of the ground", S("suction_run"), bx(-2000, 2000, -3000, 3000, -50, 0), 150.0)
    chk("Suction hose clear of the wheels", S("suction_run"), S("wheels"), 15.0, vol=False)
    chk("Suction hose clear of the axle, spacers and collars", S("suction_run"), S("axle") + S("wheel_spacers") + S("collars"), 10.0, vol=False)
    chk("Suction hose clear of the pump, stand and relief valve", S("suction_run"), S("pump") + S("stand") + S("relief"), 10.0, vol=False)
    chk("Suction hose clear of the reel, uprights and hoses", S("suction_run"), S("reel") + S("uprights") + S("wound_hose") + S("conn_hose"), 20.0, vol=False)
    chk("Suction hose clear of the tray walls", S("suction_run"), S("tray"), 2.0, vol=False)
    chk("Suction hose clear of the handle", S("suction_run"), S("handle"), 30.0, vol=False)
    chk("Suction hose run ends on the coil", S("suction_run"), S("suction"), "touch")
    chk("Hose straps round the hose", S("hose_straps"), S("suction_run"), "touch")
    chk("Hose straps round the rail", S("hose_straps"), fuse(fr["rails"]), "touch")
    chk("Hose straps clear of the wheels", S("hose_straps"), S("wheels"), 10.0)
    chk("Hose straps clear of the axle plates", S("hose_straps"), fuse(fr["axle_plates"]), 10.0)
    for ang in (-P["SWING"], P["SWING"]):
        lv = lever_parts(p, swing=ang)
        lvs = fuse(lv["lever_hub"] + lv["lever"] + lv["tgrip"] + lv["lever_grips"])
        chk(f"Lever swung {ang:+.0f} deg clear of the suction hose", lvs, S("suction_run") + S("suction_adaptor"), 50.0, vol=False)
    chk("Strainer, nozzle and tap adaptor apart", S("strainer"), S("nozzle") + S("tap"), 2.0)
    chk("Nozzle clear of the tap adaptor", S("nozzle"), S("tap"), 2.0)
    # station
    cart = fuse([c.shape for c in C.values() if c.group == "cart" and c.key not in ("conn_hose", "suction_run")])
    lvs = [fuse(sum((v for v in lever_parts(p, swing=a).values()), [])) for a in (-P["SWING"], P["SWING"])]
    for i in range(4):
        chk(f"Post {i + 1} in its concrete collar", sn["posts"][i], sn["collars"][i], "touch")
        chk(f"Roof beam on post {i + 1} top", sn["beams"][i // 2], sn["posts"][i], "touch")
    chk("Purlins on the beams", S("purlins"), S("beams"), "touch")
    chk("Roof sheet on the purlins", S("sheet"), S("purlins"), "touch")
    chk("Panel rails on the roof sheet", fuse(sn["panel_rails"]), S("sheet"), "touch")
    chk("Panel on its rails", fuse(sn["panel"]), fuse(sn["panel_rails"]), "touch")
    chk("Station box on the left post", S("station_box"), fuse(sn["posts"]), "touch")
    chk("Siren bracket on the left post", S("siren"), fuse(sn["posts"]), "touch")
    chk("Siren clear of the station box", S("siren"), S("station_box"), 50.0)
    chk("Sign on the right post", S("sign"), fuse(sn["posts"]), "touch")
    chk("Drum on the ground", S("drum"), bx(-3000, 3000, -3000, 3000, -50, 0), "touch")
    chk("Cart clear of the posts and sign", cart, fuse(sn["posts"] + sn["sign"]), 50.0)
    chk("Cart clear of the roof", cart, S("beams") + S("purlins"), 400.0)
    chk("Lever swung both ways clear of the posts", lvs[0] + lvs[1], fuse(sn["posts"]), 50.0)
    chk("Drum clear of the station and cart", S("drum"), fuse(sn["posts"] + sn["sign"]) + cart, 50.0)
    # heat alarm
    pole = alarm_pole(p)
    chk("Alarm plate against the roof pole", S("al_plate"), pole, "touch")
    chk("Alarm base on the plate", S("al_base"), S("al_plate"), "touch")
    chk("Alarm cover on the base", S("al_cover"), S("al_base"), "touch")
    chk("Battery holder on the base back wall", S("al_battery"), S("al_base"), "touch")
    chk("Standoffs on the base back wall", S("al_standoffs"), S("al_base"), "touch")
    chk("Board on the standoffs", S("al_pcb"), S("al_standoffs"), "touch")
    chk("Board clear of the battery holder", S("al_pcb"), S("al_battery"), 5.0)
    chk("Board clear of the box walls", S("al_pcb"), S("al_base") + S("al_cover"), 0.5)
    chk("Piezo on the board", S("al_piezo"), S("al_pcb"), "touch")
    chk("Piezo clear of the cover", S("al_piezo"), S("al_cover"), 0.3)
    chk("Sensor guard on the cover", S("al_guard"), S("al_cover"), "touch")
    chk("Cable ties round the pole", S("al_ties"), pole, "touch")
    chk("Cable ties through the plate slots and tight under the plate", S("al_ties"), S("al_plate"), "touch")
    chk("Plate screws on the plate", S("al_screws"), S("al_plate"), "touch")
    return rows


def print_checks(p=P):
    rows = checks(p)
    bad = 0
    for desc, v, g, e, ok in rows:
        bad += not ok
        es = "touch" if e == "touch" else f">= {e:.1f}"
        print(f"{'ok  ' if ok else 'FAIL'} {desc}: overlap {v:.2f} mm3, gap {g:.2f} mm ({es})")
    print(f"{len(rows) - bad} of {len(rows)} constructability checks pass")
    return bad


def groups(p=P):
    C = components(p)
    out = {"cart": [], "station": [], "alarm": []}
    for c in C:
        out[c.group].append(c)
    return out


if __name__ == "__main__":
    if "--check" in sys.argv:
        sys.exit(1 if print_checks() else 0)
    out = Path(__file__).resolve().parents[1]
    (out / "step").mkdir(exist_ok=True)
    (out / "stl").mkdir(exist_ok=True)
    G = groups()
    sets = {
        "campbreak-cart": [c.shape for c in G["cart"]],
        "campbreak-station": [c.shape for c in G["station"]],
        "campbreak-assembly": [c.shape for c in G["cart"] + G["station"]],
        "campbreak-alarm": [c.shape for c in G["alarm"]] + [alarm_pole()],
    }
    for name, shapes in sets.items():
        c = Compound(shapes)
        export_step(c, str(out / "step" / f"{name}.step"))
        export_stl(c, str(out / "stl" / f"{name}.stl"), tolerance=0.5, angular_tolerance=0.3)
        bb = c.bounding_box()
        print(f"{name}: {bb.size.X:.0f} x {bb.size.Y:.0f} x {bb.size.Z:.0f} mm")
    print_checks()
