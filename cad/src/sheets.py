"""CampBreak general arrangement drawing CBK-DWG-001 (Rev P1), hand-pumped hose cart.

Run from the repo root:  python3 cad/src/sheets.py
Builds cad/drawings/CBK-DWG-001.svg, .pdf and .png from the constructable model in cad/src/model.py
(CBK-DDR-002). The concept sheet in media/ is CBK-DWG-010; the making sketches are CBK-DWG-101 onward
(cad/src/build_plan_media.py). Figures in the notes come from CBK-CAL-001 (docs/04-calcs/sizing.py).
"""
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / ".kit"), str(ROOT / "cad/src"), str(ROOT / "docs/04-calcs")]
from build123d import Compound  # noqa: E402
from drawing import Sheet, project_views  # noqa: E402
import model as M  # noqa: E402
import sizing  # noqa: E402

DATE = "2026-10-03"


def main():
    shapes = [M.connecting_hose_segments() if c.key == "conn_hose" else c.shape
              for c in M.components() if c.group == "cart"]
    work = ROOT / "cad/drawings/_views_ga"
    views = project_views(Compound(children=shapes), work)
    a, c, b = sizing.pump(), sizing.cart(), sizing.alarm()
    D = M.derived()
    P = M.P
    s = Sheet(project="CampBreak", title="Hand-pumped hose cart for camp blocks: general arrangement",
              dwg_no="CBK-DWG-001", rev="P1", author="Amish Chadha", date=DATE,
              concept="CONCEPT, NOT FOR FABRICATION",
              material="S235 steel tube, welded and painted; bought pump, reel, hoses and wheels",
              revisions=[("P1", "First issue from the constructable TRL 3 model (CBK-DDR-002)", DATE, "AC")])
    s.add_ortho(views)
    s.add_svg(views["iso"], 276, 37, 140, 105, label="Isometric view",
              sublabel="Not to scale; seen from the front right and above, about 30 deg elevation")
    s.add_notes("Main sizes and figures", [
        f"Overall {c['width']:.0f} wide x {c['length']:.0f} long x {c['height']:.0f} tall",
        f"Wheel track {D['track']:.0f}; 400 mm wheels on a 20 mm axle",
        f"Frame of 30 x 30 x 2 mm tube; deck {P['DECK_Z']:.0f} above the ground",
        f"Pull bar 33.7 mm, {P['BAR_Z']:.0f} up, {2 * P['BAR_HALF']:.0f} long",
        f"Pump shaft {P['PUMP_Z']:.0f} up; lever grip {P['LEVER_R']:.0f} from the shaft",
        f"Reel 500 mm flanges, spindle {P['REEL_Z']:.0f} up; 30 m of 19 mm hose",
        f"About {c['mass']:.0f} kg dry; {c['per_person']:.0f} N each for two on a 10 % slope (est.)",
        f"{a['q_lmin']:.1f} L/min; jet reach about {a['reach']:.1f} m (est.)",
        "Block station and heat alarm: making sketches CBK-DWG-108 to 111",
    ], x=276, y=150, width=140)
    s.save(ROOT / "cad/drawings/CBK-DWG-001")
    shutil.rmtree(work, ignore_errors=True)
    print("CBK-DWG-001 written")


if __name__ == "__main__":
    main()
