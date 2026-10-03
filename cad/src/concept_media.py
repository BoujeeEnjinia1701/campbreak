"""CampBreak concept media from the TRL 3 parametric model (constructable design, CBK-DDR-002).

Run from the repo root:  python3 cad/src/concept_media.py [hero|cutaway|exploded|flow|web|blueprint ...]
With no argument it draws everything; on a small machine run one picture per process.
Geometry comes from cad/src/model.py; the flow values come from CBK-CAL-001 (docs/04-calcs/sizing.py).

hero       block station with the hose cart parked under its roof, the water drum and a 1.75 m person
cutaway    the heat alarm cut in half (the inside matters: battery, board, sounder, thermistor)
exploded   the hose cart pulled apart, one part per BOM line, numbers matching bom/bom.csv
flow       water pressure along the line from drum to nozzle (estimates)
web        model.glb and viewer.html
blueprint  concept sheet CBK-DWG-010 (cart views, key figures)
"""
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / ".kit"))
sys.path.insert(0, str(ROOT / "cad/src"))
sys.path.insert(0, str(ROOT / "docs/04-calcs"))
import concept as K  # noqa: E402
from concept import Part  # noqa: E402
import model as M  # noqa: E402

PROJECT, TITLE, DWG, DATE = "CampBreak", "Block fire kit concept: hose cart, station and heat alarm", "CBK-DWG-010", "2026-10-03"
MD = ROOT / "media"


def parts(groups=("cart", "station")):
    """Parts above the ground: the concrete collars and the buried 600 mm of each post are left out."""
    ground = M.bx(-5000, 5000, -5000, 5000, 0, 6000)
    out = []
    for c in M.components():
        if c.group not in groups or c.key == "collars_c":
            continue
        sh = c.shape & ground if c.key == "posts" else c.shape
        out.append(Part(c.name, sh, c.color, c.bom, c.explode))
    return out


def cart_by_bom():
    """Cart parts merged by BOM line, so each callout is one BOM number."""
    by = {}
    for c in M.components():
        if c.group != "cart" or c.key in ("conn_hose",):
            continue
        by.setdefault(c.bom, []).append(c)
    out = []
    for bom, cs in sorted(by.items()):
        name = M.BOM[bom]
        out.append(Part(name, M.fuse([c.shape for c in cs]), cs[0].color, bom, cs[0].explode))
    return out


def hero():
    ps = parts()
    return K._render(K.with_scale_figure(ps), MD / "hero.png", title=PROJECT,
                     note="Seen from the front right and above, 24 deg elevation. Hose cart parked in its block station "
                          "beside the 200 L drum. Grey figure: 1.75 m person for scale")


def cutaway():
    al = [p for p in parts(("alarm",)) if p.name != "Cable ties, UV-stable"]
    pole = Part("Bamboo roof pole (context)", M.alarm_pole(), "#D6C08D", None)
    return K._render(K.cutaway_parts(al + [pole]), MD / "cutaway.png", azim=-90, elev=18,
                     title=f"{PROJECT}: heat alarm cutaway",
                     note="Front half removed; seen from the front and above, 18 deg elevation. The alarm hangs "
                          "under a roof pole; box 100 x 100 x 40 mm")


def exploded():
    return K._render(cart_by_bom(), MD / "exploded.png", offsets=True, labels=True, size=(9, 7),
                     title=f"{PROJECT}: hose cart, exploded view",
                     note="Seen from the front right and above, 24 deg elevation; numbers match bom/bom.csv")


def flow():
    import sizing
    a = sizing.pump()
    kpa = lambda v: round(v / 1000.0, 1)  # noqa: E731
    stages = [("Pump outlet (est.)", kpa(a["p_out"])),
              ("After connecting hose, swivel and fittings (est.)", kpa(a["p_out"] - a["dp_conn"] - a["dp_fit"])),
              ("After 30 m of 19 mm hose (est.)", kpa(a["p_out"] - a["dp_conn"] - a["dp_fit"] - a["dp_hose"])),
              ("At the 6 mm jet (est.)", kpa(a["p_noz"]))]
    losses = [(0, "Connecting hose and fittings (est.)", kpa(a["dp_conn"] + a["dp_fit"])),
              (1, "Hose friction at 20.4 L/min (est.)", kpa(a["dp_hose"])),
              (2, "Lift of 1 m to the nozzle (est.)", kpa(a["p_out"] - a["dp_conn"] - a["dp_fit"] - a["dp_hose"] - a["p_noz"]))]
    return K.flow_diagram(stages, MD / "flow.png",
                          f"{PROJECT}: water pressure from the hand pump to the nozzle at 20.4 L/min, "
                          f"two people pumping (all values are estimates; relief valve set at 400 kPa)", "kPa", losses)


def web():
    # Coarse mesh (1.0 mm chord, 0.35 rad): the build123d default of 0.001 mm makes a file of several GB here
    import functools
    import build123d
    fine = build123d.export_gltf
    build123d.export_gltf = functools.partial(fine, linear_deflection=1.0, angular_deflection=0.35)
    try:
        return K.export_web_model(parts(), "media", title=f"{PROJECT}: {TITLE}")
    finally:
        build123d.export_gltf = fine


def blueprint():
    import sizing
    from build123d import Compound
    from drawing import Sheet, project_views
    a, b = sizing.pump(), sizing.alarm()
    c = sizing.cart()
    swap = {"Connecting hose": M.connecting_hose_segments, "Suction hose run": M.suction_run_segments}
    ps = [next((Part(q.name, f(), q.color, q.bom) for k, f in swap.items() if q.name.startswith(k)), q)
          for q in parts(("cart",))]
    shown = K.with_scale_figure(ps, gap=900)
    views = project_views(Compound([p.shape for p in ps]), MD / "_views")
    views["iso"] = project_views(Compound([p.shape for p in shown]), MD / "_views_fig")["iso"]
    s = Sheet(project=PROJECT, title="Hand-pumped hose cart for camp blocks: concept", dwg_no=DWG, rev="P2",
              author="Amish Chadha", date=DATE, theme="blueprint", material="Massing model for concept communication",
              revisions=[("P1", "Concept sheet from the constructable TRL 3 model", DATE, "AC"),
                         ("P2", "Suction hose left coupled, check foot valve (CBK-DDR-003)", DATE, "AC")])
    s.add_ortho(views)
    s.add_svg(views["iso"], 276, 37, 140, 103, label="Isometric view", sublabel="Not to scale; figure is a 1.75 m person")
    s.add_notes("Key figures", [
        f"Cart {c['width']:.0f} wide x {c['length']:.0f} long; about {c['mass']:.0f} kg (est.)",
        f"Two people pull {c['per_person']:.0f} N each on a 10 % slope (est.)",
        f"Hand pump {a['q_lmin']:.1f} L/min at 60 double strokes/min (est.)",
        f"Jet reach about {a['reach']:.1f} m with a 6 mm jet (est.)",
        "30 m of 19 mm hose on a reel; 4 m suction hose left coupled",
        "Check foot valve keeps the pump primed between uses",
        "Relief valve at 4 bar; one 200 L drum lasts about 10 min",
        f"Heat alarms alert the station in {b['t_total']:.0f} s worst case (est.)",
        f"Water on target {c['t_r9'] / 60:.1f} min at 100 m, {c['t_r9_sited'] / 60:.1f} min at 70 m (est.)",
        f"Block kit: 24 alarms, station, cart; about USD {sizing.cost()['total']:,.0f}"], x=276, y=158, width=140)
    s.save(MD / "concept-blueprint")
    shutil.rmtree(MD / "_views", ignore_errors=True)
    shutil.rmtree(MD / "_views_fig", ignore_errors=True)
    return MD / "concept-blueprint.png"


if __name__ == "__main__":
    fns = {"hero": hero, "cutaway": cutaway, "exploded": exploded, "flow": flow, "web": web, "blueprint": blueprint}
    for w in sys.argv[1:] or list(fns):
        print(w, "->", fns[w]())
