"""CampBreak product appearance model (build123d), TRL 3, constructable design (CBK-DDR-002).

Finished-product look for photoreal renders. Every part is a component of cad/src/model.py components(),
used as it is, so every main dimension comes from the model: the hose cart (frame, handle, pump stand, reel
uprights, axle, wheels, pump, relief valve, lever, reel and hoses, tray and its kit), the block station
(four posts, beams, purlins, roof sheet, alarm box, siren, solar panel, sign, drum) and the heat alarm on a
bamboo roof pole. Only context is added: packed-earth ground, a 1.75 m mannequin standing beside the drum,
and a forearm and hand beside the heat alarm. The buried 600 mm of each post and the concrete collars are
left out (below ground). APPEARANCE MODEL ONLY: no tolerances, no fabrication detail. CONCEPT, NOT FOR
FABRICATION.

Axes as model.py. Groups: "shell" (cart and station), "alarm" (heat alarm and pole), "context".
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path[:0] = [str(HERE), str(HERE.parents[1] / ".kit")]

from build123d import Pos, Rot  # noqa: E402
import model as M  # noqa: E402

TITLE = "CampBreak: hand-pumped hose cart and heat alarms for camp blocks"

RENDER_VIEWS = [
    {"name": "hero", "groups": ["shell", "context"], "explode": False, "el": 22, "az": -40,
     "note": "Product render from the front right and above (about 22 deg elevation): the hose cart parked "
             "under its block station roof beside the 200 L drum, with the station alarm box, siren, solar "
             "panel and sign; 1.75 m person beside the drum for scale"},
    {"name": "exploded", "groups": ["cart"], "explode": True, "el": 26, "az": -50,
     "note": "Exploded view of the hose cart from the front right and above (about 26 deg elevation): frame, "
             "handle, pump stand, reel uprights, axle and wheels, hand pump and relief valve, lever, reel and "
             "hoses, tray with suction hose, strainer, nozzle and tap adaptor"},
    {"name": "detail", "groups": ["alarm", "hand"], "explode": False, "el": 12, "az": -60,
     "note": "Detail from the front right and slightly below (about 12 deg elevation): one rate-of-rise heat "
             "alarm hung under a bamboo roof pole by two cable ties, sensor guard underneath; forearm and "
             "hand for scale"},
]

MAT = {"frame": "painted", "handle": "painted", "stand": "painted", "uprights": "painted", "lever": "painted",
       "reel": "painted", "feet": "rubber", "grips": "rubber", "lever_grips": "rubber", "wheels": "rubber",
       "wound_hose": "rubber", "conn_hose": "rubber", "suction": "rubber", "tray": "metal", "sheet": "metal",
       "posts": "painted", "beams": "painted", "purlins": "painted", "station_box": "plastic", "siren": "painted",
       "panel": "screen", "sign": "painted", "drum": "plastic", "al_base": "plastic", "al_cover": "plastic",
       "al_guard": "plastic", "al_ties": "plastic", "al_battery": "plastic", "al_pcb": "plastic", "al_piezo": "metal"}


def product_parts():
    out = []
    ground_cut = M.bx(-5000, 5000, -5000, 5000, 0, 6000)
    for c in M.components():
        if c.key == "collars_c":
            continue
        shape = c.shape & ground_cut if c.key == "posts" else c.shape
        group = {"cart": "shell", "station": "shell", "alarm": "alarm"}[c.group]
        out.append(dict(name=c.name, shape=shape, color=c.color, material=MAT.get(c.key, "metal"), bom=c.bom,
                        group=group, explode=c.explode))
        if c.group == "cart":      # the same cart part again for the cart-only exploded view
            out.append(dict(name=c.name, shape=c.shape, color=c.color, material=MAT.get(c.key, "metal"), bom=c.bom,
                            group="cart", explode=c.explode))
    out.append(dict(name="Bamboo roof pole", shape=M.alarm_pole(), color="#C8AD72", material="wood", bom=None,
                    group="alarm", explode=(0, 0, 0)))
    out.append(dict(name="Packed earth ground", shape=M.bx(-2200, 2400, -2600, 1700, -20, 0), color="#B7A58A",
                    material="paper", bom=None, group="context", explode=(0, 0, 0)))
    from context_parts import forearm_hand, mannequin
    person = Pos(1250, -450, 0) * mannequin(1750, "stand")
    out.append(dict(name="Person, 1.75 m mannequin (scale)", shape=person, color="#B9B4AC", material="clay",
                    bom=None, group="context", explode=(0, 0, 0)))
    hand = Pos(-150, -60, -70) * Rot(0, 0, 20) * forearm_hand("right", "flat", forearm_len=180.0)
    out.append(dict(name="Forearm and hand (scale)", shape=hand, color="#B9B4AC", material="clay",
                    bom=None, group="hand", explode=(0, 0, 0)))
    return out


if __name__ == "__main__":
    for p in product_parts():
        print(f"{p['name']:52s} {p['group']:8s} {p['material']:8s} valid={p['shape'].is_valid}")
