"""CampBreak prototype build plan pictures (CBK-BLD-001, STANDARDS section 18).

Run from the repo root (one group per process on a small machine):
    python3 cad/src/build_plan_media.py overview
    python3 cad/src/build_plan_media.py sheets [101 102 ...]
    python3 cad/src/build_plan_media.py joints [1 2 ...]
    python3 cad/src/build_plan_media.py steps [1 2 ...]
Every picture is drawn from cad/src/model.py (components()), so the pictures and the model never disagree:
    docs/05-build-plan/overview.png        every component pulled apart, numbered in build order
    cad/drawings/CBK-DWG-101 to 112        making sketches for the made components
    docs/05-build-plan/joint-NN.png        close-ups of the joints that need explaining
    docs/05-build-plan/step-NN.png         one picture per assembly step
Uses .kit/build_views.py. BUILD PLAN ILLUSTRATION, PLAN NOT YET BUILT.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / ".kit"), str(ROOT / "cad" / "src")]
import build_views as bv  # noqa: E402
from build_views import Part  # noqa: E402
import model as M  # noqa: E402
from build123d import Compound, Pos  # noqa: E402

OUT = ROOT / "docs" / "05-build-plan"
DWG = ROOT / "cad" / "drawings"
DATE = "2026-10-03"
P = M.P
_C = {}


def comps():
    if not _C:
        _C.update({c.key: c for c in M.components()})
    return _C


def fuse(*keys):
    return Compound([comps()[k].shape for k in keys])


def win(shape, x0, x1, y0, y1, z0, z1):
    """The part of a shape inside a box (for close-ups)."""
    try:
        r = shape & M.bx(x0, x1, y0, y1, z0, z1)
        return r if r is not None and r.volume > 1e-3 else None
    except Exception:
        return None


def part(name, shape, color, explode=(0, 0, 0), alpha=1.0):
    return Part(name, shape, color, None, tuple(explode), alpha)


def K(key, name=None, color=None, explode=(0, 0, 0)):
    c = comps()[key]
    return part(name or c.name, c.shape, color or c.color, explode)


def W(shape, name, color, box):
    s = win(shape, *box)
    return part(name, s, color) if s is not None else None


COL = {"frame": "#B42318", "handle": "#DC6803", "stand": "#7A271A", "upright": "#B54708", "axle": "#6B7280",
       "wheel": "#111827", "pump": "#1D4ED8", "relief": "#DC2626", "lever": "#E5A50A", "reel": "#9F1239",
       "hose": "#C2410C", "tray": "#4B5563", "kit": "#0F766E", "post": "#374151", "collar": "#A8A29E",
       "beam": "#4B5563", "roof": "#9CA3AF", "box": "#64748B", "panel": "#1E3A8A", "sign": "#0F766E",
       "drum": "#2563EB", "alarm": "#166534"}

# ----------------------------------------------------------------- groups in build order
GROUPS = [
    ("frame", "Base frame and rubber feet", ("frame", "feet"), COL["frame"]),
    ("handle", "Handle and grips", ("handle", "grips"), COL["handle"]),
    ("stand", "Pump stand plate and gussets", ("stand",), COL["stand"]),
    ("uprights", "Reel uprights", ("uprights",), COL["upright"]),
    ("wheels", "Axle, spacers, wheels and collars", ("axle", "wheel_spacers", "wheels", "collars"), COL["wheel"]),
    ("pump", "Hand pump, bolts and inlet coupling", ("pump", "pump_bolts", "inlet_coupling"), COL["pump"]),
    ("relief", "Pressure relief valve, 4 bar", ("relief",), COL["relief"]),
    ("lever", "Lever extension with T-grip", ("lever", "lever_grips"), COL["lever"]),
    ("reel", "Reel spindle, spacers, drum and swivel", ("spindle", "reel_spacers", "reel", "swivel"), COL["reel"]),
    ("hose", "Delivery hose and connecting hose", ("wound_hose", "conn_hose"), COL["hose"]),
    ("tray", "Hose tray and bolts", ("tray", "tray_bolts"), COL["tray"]),
    ("kit", "Suction hose coupled to the pump, straps, foot valve, nozzle, tap adaptor",
     ("suction_adaptor", "suction_run", "hose_straps", "suction", "strainer", "nozzle", "tap"), COL["kit"]),
    ("posts", "Station posts in concrete collars", ("posts", "collars_c"), COL["post"]),
    ("beams", "Roof beams", ("beams",), COL["beam"]),
    ("roof", "Purlins and roof sheet", ("purlins", "sheet"), COL["roof"]),
    ("sbox", "Station alarm box, siren, solar panel", ("station_box", "siren", "panel"), COL["box"]),
    ("sign", "Station sign", ("sign",), COL["sign"]),
    ("drum", "Water drum, 200 L", ("drum",), COL["drum"]),
]


def G(key, explode=(0, 0, 0), color=None, name=None):
    for k, n, keys, c in GROUPS:
        if k == key:
            return part(name or n, fuse(*keys), color or c, explode)
    raise KeyError(key)


# ----------------------------------------------------------------- overview
def overview():
    cx = -3000          # the cart is drawn to the left of the station
    off = {"frame": (cx, 0, 0), "handle": (cx, -300, 250), "stand": (cx, 0, 450), "uprights": (cx, 0, 650),
           "wheels": (cx, 0, -350), "pump": (cx, 450, 450), "relief": (cx + 300, 600, 700),
           "lever": (cx, 800, 900), "reel": (cx, 0, 1050), "hose": (cx, 0, 1500), "tray": (cx, -300, 600),
           "kit": (cx, -300, 900), "posts": (0, 0, 0), "beams": (0, 0, 500), "roof": (0, 0, 1000),
           "sbox": (-350, 0, 0), "sign": (300, -500, 0), "drum": (900, -500, 0)}
    parts = [G(k, off[k]) for k, *_ in GROUPS]
    al = Compound([c.shape for c in comps().values() if c.group == "alarm"]).scale(5.0)
    parts.append(part("Heat alarm, one per shelter (drawn 5 x size)", Pos(2200, -1500, 1400) * al, COL["alarm"]))
    return bv.overview(parts, OUT / "overview.png", "CampBreak prototype: every component, pulled apart",
                       subtitle="Numbered in build order: hose cart (1 to 12), block station (13 to 18), heat alarm (19). "
                                "Seen from the front right and above",
                       elev=20, azim=-52, size=(13, 9), dpi=150, key=True)


# ----------------------------------------------------------------- making sketches
def sheet(n, shape, name, color, neighbours, title, material, notes, view_shape=None, inset=(24, -58)):
    return bv.component_sheet(part(name, shape, color), neighbours, project="CampBreak", dwg_no=f"CBK-DWG-{n}",
                              title=f"CampBreak {title}: making sketch", material=material, notes=notes, date=DATE,
                              view_shape=view_shape, inset_view=inset, out_dir=str(DWG))


def sheets(which=None):
    c = comps()
    sn = M.station_parts()
    g = lambda *ks: [G(k) for k in ks]  # noqa: E731
    S = {}
    S[101] = lambda: sheet(101, c["frame"].shape, "Base frame", COL["frame"], g("handle", "stand", "wheels"),
        "cart base frame", "30 x 30 x 2 mm square tube and 8 mm plate, S235; MIG welded",
        ["Side rails: two tubes 1,000 long, 540 apart inside (600 outside).",
         "Cross members, 540 long, between the rails: front, flush with the rail",
         "  front ends; rear, its back face 30 in from the rail back ends; middle,",
         "  350 behind the front one, cut in three (110, 260, 110) round the bearers.",
         "Bearers: two lines of tube 260 apart inside, 320 long in front of the",
         "  middle cross member and 590 behind it, all tops flush.",
         "Legs: 190 long under each rail's front end; a 40 mm rubber foot below.",
         "Axle plates: four, 80 x 85 x 8 mm, a 21 mm hole 40 up from the bottom;",
         "  one each side of each rail, centred 800 behind the rail front ends,",
         "  tops flush with the rail top. Drill the four as a stack, then weld",
         "  with a 20 mm bar through all four holes so they line up.",
         "Weld all round on a flat table; check the diagonals before welding.",
         "Check: diagonals equal within 3 mm; the 20 mm bar turns by hand."], inset=(26, -55))
    S[102] = lambda: sheet(102, c["handle"].shape, "Handle", COL["handle"], g("frame", "tray"),
        "pull handle (two arms and a cross bar)", "30 x 30 x 2 mm square tube; 33.7 x 2.6 mm tube; S235",
        ["Arms: two 30 mm tubes about 800 long, cut at 44 deg at the foot so they",
         "  sit flat on the rail tops, the foot end against the front cross member.",
         "Cope the top end of each arm to the 33.7 mm bar (a saddle cut).",
         "Cross bar: 33.7 x 2.6 mm tube 820 long, 800 above the ground and 550",
         "  in front of the rail front ends; the arms meet it 125 from each end.",
         "Grips: 95 mm rubber grips on both bar ends, pushed on with soapy water.",
         "Tack the arms to the frame in a jig, check, then weld all round.",
         "Check: bar level within 3 mm and square to the cart centre line."], inset=(22, -60))
    S[103] = lambda: sheet(103, c["stand"].shape, "Pump stand", COL["stand"], g("frame", "pump"),
        "pump stand plate and gussets", "10 mm plate 320 x 355 mm; two 8 mm gussets; S235",
        ["Plate: 320 wide x 355 tall x 10 mm. Mark its centre line.",
         "Pump holes: four 13 mm holes on a 150 mm square, centred on the",
         "  centre line 195 up from the bottom edge (the pump shaft height).",
         "  Check the square against the pump flange before drilling.",
         "Gussets: two 8 mm right triangles, 130 along the bottom and 250 tall.",
         "Fit: the plate stands on the rear cross member, its front face 10",
         "  behind the member's front face, square to the bearers. The gussets",
         "  sit on the bearer tops, centred on them, against the plate front.",
         "Weld the plate to the cross member both sides; weld each gusset to",
         "  the bearer and the plate.",
         "Check: plate upright within 1 deg; holes clear of the gusset welds."], inset=(24, 40))
    S[104] = lambda: sheet(104, c["uprights"].shape, "Reel uprights", COL["upright"], g("frame", "reel"),
        "reel uprights (make 2)", "50 x 8 mm flat bar 365 mm long; S235",
        ["Cut two flat bars 50 x 8 mm, 365 long, square ends.",
         "Hole: 26 mm, centred on the bar width, 320 up from the bottom end.",
         "  Drill the two bars clamped together so the holes line up.",
         "Fit: each bar stands against the inside face of a bearer, its bottom",
         "  end flush with the bearer bottom, its centre 130 in front of the",
         "  axle centre line (back edge 275 in front of the rear cross member).",
         "Weld along both edges where it touches the bearer.",
         "Check: a 25 mm bar slides through both holes at once and is level."], inset=(24, -58))
    S[105] = lambda: sheet(105, fuse("axle", "wheel_spacers", "collars"), "Axle and spacers", COL["axle"],
        g("frame", "wheels"), "axle, wheel spacers and collars", "20 mm bright steel bar; 32 x 22 mm tube; bought collars",
        ["Axle: 20 mm bright steel bar, 850 long, ends chamfered 1 mm.",
         "  Drill a 4 mm cross hole 6 from each end for the R-clips.",
         "Spacers: two 32 x 22 mm tube pieces, 22 long, ends square and",
         "  deburred; they sit between the outer axle plate and the wheel hub.",
         "Collars: two 20 mm shaft collars with set screws, 12 wide, against",
         "  the outside of each hub.",
         "Order on each side, from the middle out: inner plate, rail, outer",
         "  plate, spacer, wheel hub (75 long), collar, R-clip.",
         "Check: with both wheels on, the axle end float is 1 to 2 mm."], inset=(20, -40))
    S[106] = lambda: sheet(106, fuse("spindle", "reel_spacers"), "Reel spindle", COL["axle"], g("uprights", "reel"),
        "reel spindle and spacers", "25 mm bright steel bar; 40 x 26 mm tube; bought collar",
        ["Spindle: 25 mm bright steel bar, 290 long, ends chamfered 1 mm.",
         "Spacers: two 40 x 26 mm tube pieces, 12 long; one each side of the",
         "  drum, between the drum flange boss and the upright.",
         "Collar: a 25 mm collar with a set screw against the outside of the",
         "  left upright; the swivel inlet holds the right-hand end.",
         "Fit: the spindle passes through the left upright, a spacer, the drum,",
         "  the other spacer and the right upright into the swivel.",
         "Check: the drum turns by hand with 1 to 2 mm of side float."], inset=(20, -40))
    S[107] = lambda: sheet(107, c["lever"].shape, "Lever extension", COL["lever"], g("pump", "stand"),
        "lever extension with T-grip", "33.7 x 2.6 and 27 x 2.3 mm tube; 50 mm square bar hub; S235",
        ["Hub: 50 x 50 mm block, 38 thick, bored and slotted to clamp on the",
         "  pump's handle socket with two M10 bolts (fit it to the pump bought).",
         "Lever: 33.7 x 2.6 mm tube 585 long, welded on top of the hub.",
         "T-bar: 27 x 2.3 mm tube 400 long, welded across the lever top, square",
         "  to the pump shaft, 610 above the shaft centre.",
         "Grips: 100 mm rubber grips on both T-bar ends.",
         "Fit: the lever stands upright at mid-stroke and swings 40 deg each",
         "  way. Two people face each other across the T-bar.",
         "Check: at both ends of the swing the grip is at least 50 from the",
         "  wheels and 30 from the frame."], inset=(24, 40))
    S[108] = lambda: sheet(108, c["tray"].shape, "Hose tray", COL["tray"], g("frame", "handle"),
        "hose tray", "1.5 mm galvanised steel sheet, blank 560 x 530 mm",
        ["Blank 560 x 530 mm. Cut an 80 mm square out of each corner.",
         "Holes in the floor, before folding: six 12 mm drain holes at 120 mm",
         "  spacing across and 200 mm along; four 9 mm bolt holes, 145 each",
         "  side of the centre line, 120 in front of and behind the middle.",
         "Fold the four sides up 90 deg to 80 tall; tray 400 x 370 outside.",
         "Pop-rivet or spot-weld the corners; paint the cut edges.",
         "Fit: the tray sits on the bearers and front cross member tops,",
         "  centred, its front edge 5 behind the front cross member's front",
         "  face; four M8 bolts through the bearer tops, nuts below.",
         "Check: the tray sits flat and clears the handle arms by 30 mm."], inset=(24, -58))
    S[109] = lambda: sheet(109, Compound([sn["posts"][0], sn["posts"][1], sn["collars"][0], sn["collars"][1]]),
        "Station posts", COL["post"], [G("beams"), G("roof")], "station posts and concrete collars (left pair drawn)",
        "60 x 60 x 3 mm square tube, S235; concrete collars 300 mm across",
        ["Four posts: two front (3,160 long) and two back (3,000 long), each",
         "  set 600 into the ground; the tops are cut at 5 deg so the roof",
         "  falls to the back. Back posts stand 2,400 above the ground.",
         "Layout: 1,300 between post centres across, 1,800 front to back.",
         "Holes: two 13 mm holes across each post top, 60 down, for the beam",
         "  cleats; 9 mm holes for the box, siren and sign brackets on site.",
         "Paint the buried 700 mm with bitumen; cap the tops.",
         "Collars: auger 300 mm holes 650 deep; 50 mm of gravel; stand the post",
         "  plumb on it and pour concrete to ground level, sloped to shed water.",
         "Check: posts plumb within 5 mm over 2 m; diagonals equal within 10."], inset=(18, -50))
    S[110] = lambda: sheet(110, fuse("beams", "purlins"), "Roof frame", COL["beam"], g("posts", "sbox"),
        "roof beams and purlins", "40 x 40 x 2 and 40 x 20 x 2 mm tube; S235",
        ["Beams: two 40 x 40 x 2 tubes 2,000 long, one over each pair of posts,",
         "  reaching 100 past the front and the back post centres.",
         "Fix each beam to its post tops with a 40 x 40 x 4 angle cleat and",
         "  two M8 bolts, or weld it on site.",
         "Purlins: four 40 x 20 x 2 tubes 1,500 long across the beams, at",
         "  30, 660, 1,300 and 1,940 from the beams' front ends; weld or bolt",
         "  with an M8 bolt through each crossing.",
         "Roof sheet: corrugated galvanised 1,500 x 2,050, fixed to each purlin",
         "  with roofing screws and washers on every second crest.",
         "Check: the roof falls 5 deg to the back; no sheet edge overhangs a",
         "  path by more than 100."], inset=(26, -55))
    S[111] = lambda: sheet(111, c["sign"].shape, "Station sign", COL["sign"], [part("Back right post", sn["posts"][3], "#9CA3AF")],
        "station sign board", "3 mm aluminium sheet 440 x 300 mm; printed vinyl",
        ["Cut 440 x 300 mm from 3 mm aluminium; round the corners 10 mm.",
         "Two 9 mm holes on the centre line, 60 from the top and bottom edges.",
         "Print the instructions in the camp languages with pictograms:",
         "  leave first, raise the alarm, fetch the cart, small fires only,",
         "  never water on oil or live wires, call the fire service, and",
         "  go when two arrive: the first two take the cart, within 30 s.",
         "Fit: on the front face of the back right post, bottom edge 1,100",
         "  above the ground, two M8 bolts through the post.",
         "Check: readable from 5 m in daylight."], inset=(20, -60))
    S[112] = lambda: sheet(112, fuse("al_plate", "al_base", "al_cover", "al_guard"), "Heat alarm housing", COL["alarm"],
        [part("Bamboo roof pole", M.alarm_pole(), "#D6C08D")], "heat alarm mounting plate, box and sensor guard",
        "3 mm aluminium plate; stock ABS box 100 x 100 x 40; printed PETG guard",
        ["Plate: 140 x 50 x 3 mm aluminium. Four slots 8 x 3 mm, 58 each side",
         "  of the middle, 24 to 27 from the long centre line, for the ties.",
         "  Two 4.5 mm holes 30 each side of the middle for M4 screws.",
         "Box base (22 deep): two 3.3 mm holes to match the plate; screw the",
         "  plate on from inside with two M4 screws.",
         "Box cover (18 deep): a 12 mm hole in the middle for the thermistor;",
         "  eight 5 mm sound holes round a point 25 from the middle.",
         "Guard: printed PETG cup 24 across, 14 tall, six side slots; glued",
         "  over the 12 mm hole so the bead sits in moving air.",
         "Fit: plate flat under a roof pole, held by two UV-stable ties.",
         "Check: the cover closes on its seal with the board inside."], inset=(24, -58))
    out = []
    for n in sorted(S):
        if which and n not in which:
            continue
        out.append(S[n]())
        print("sheet", n, "->", out[-1], flush=True)
    return out


# ----------------------------------------------------------------- joints
def joints(which=None):
    c = comps()
    fr = M.cart_frame_parts()
    hd = M.handle_parts()
    rails = Compound(fr["rails"])
    J = {}
    # 1 axle through the axle plates, spacer, hub and collar (right side, cut open through the axle)
    b1 = (240, 440, 90, 210, 120, 280)
    J[1] = lambda: bv.joint([x for x in [
        W(rails, "Side rail", COL["frame"], b1),
        W(Compound(fr["axle_plates"]), "Axle plates, 8 mm, either side of the rail", "#7A271A", b1),
        W(c["axle"].shape, "Axle, 20 mm, through 21 mm holes", COL["axle"], b1),
        W(c["wheel_spacers"].shape, "Spacer, 22 long", "#0F766E", b1),
        W(c["wheels"].shape, "Wheel hub, 75 long", COL["wheel"], b1),
        W(c["collars"].shape, "Collar and R-clip", "#E5A50A", b1)] if x],
        OUT / "joint-01.png", "Joint 1: axle, axle plates, spacer and wheel hub (right side, cut open)",
        subtitle="Cut through the axle; seen from the front right and above", cut="+Y", elev=20, azim=-60)
    # 2 handle arm foot on the rail and against the front cross member
    b2 = (220, 340, -720, -560, 170, 330)
    J[2] = lambda: bv.joint([x for x in [
        W(rails, "Side rail", COL["frame"], b2),
        W(Compound(fr["cross_front"]), "Front cross member", "#7A271A", b2),
        W(Compound(fr["legs"]), "Leg", "#9F1239", b2),
        W(c["handle"].shape, "Handle arm, cut at 44 deg", COL["handle"], b2)] if x],
        OUT / "joint-02.png", "Joint 2: handle arm foot on the rail top",
        subtitle="The arm sits flat on the rail and its toe touches the end of the front cross member; welded all round",
        elev=22, azim=-35)
    # 3 arm coped to the cross bar
    b3 = (180, 420, -1290, -1110, 720, 880)
    J[3] = lambda: bv.joint([x for x in [
        W(hd["arms"][1], "Handle arm, coped to the bar", COL["handle"], b3),
        W(hd["bar"][0], "Cross bar, 33.7 mm tube", "#7A271A", b3),
        W(c["grips"].shape, "Rubber grip", COL["wheel"], b3)] if x],
        OUT / "joint-03.png", "Joint 3: handle arm coped to the cross bar",
        subtitle="Saddle cut on the arm end, welded all round", elev=25, azim=-40)
    # 4 pump flange bolted to the stand plate (seen from the back right)
    b4 = (-170, 170, 190, 470, 245, 620)
    J[4] = lambda: bv.joint([x for x in [
        W(c["stand"].shape, "Stand plate and gussets", COL["stand"], b4),
        W(Compound(fr["cross_rear"] + fr["bearers"]), "Rear cross member and bearers", COL["frame"], b4),
        W(c["pump"].shape, "Pump flange and body", COL["pump"], b4),
        W(c["pump_bolts"].shape, "Four M12 bolts on a 150 mm square", "#E5A50A", b4)] if x],
        OUT / "joint-04.png", "Joint 4: hand pump bolted to the stand plate",
        subtitle="Seen from the back right and above; flange flat on the plate's back face", elev=22, azim=55)
    # 5 reel spindle through the right upright, spacer, drum flange and swivel (cut open)
    b5 = (40, 200, -40, 80, 470, 600)
    J[5] = lambda: bv.joint([x for x in [
        W(c["uprights"].shape, "Reel upright, 26 mm hole", COL["upright"], b5),
        W(c["spindle"].shape, "Spindle, 25 mm", COL["axle"], b5),
        W(c["reel_spacers"].shape, "Spacer, 12 long", "#0F766E", b5),
        W(c["reel"].shape, "Drum flange and core", COL["reel"], b5),
        W(c["swivel"].shape, "Swivel inlet on the spindle end", "#E5A50A", b5)] if x],
        OUT / "joint-05.png", "Joint 5: reel spindle, spacer and swivel inlet (right side, cut open)",
        subtitle="Cut through the spindle; seen from the front right and above", cut="+Y", elev=20, azim=-60)
    # 6 pump outlet, relief valve tee and connecting hose (seen from the back right)
    b6 = (-80, 220, 300, 480, 480, 760)
    J[6] = lambda: bv.joint([x for x in [
        W(c["pump"].shape, "Pump outlet and hose tail", COL["pump"], b6),
        W(c["relief"].shape, "Relief valve on a tee, outlet down", COL["relief"], b6),
        W(c["conn_hose"].shape, "Connecting hose to the reel, two clips", COL["wheel"], b6)] if x],
        OUT / "joint-06.png", "Joint 6: pump outlet, relief valve and connecting hose",
        subtitle="Seen from the back right and above", elev=25, azim=50)
    # 7 hose tray bolted to the bearers
    b7 = (40, 260, -700, -520, 190, 340)
    J[7] = lambda: bv.joint([x for x in [
        W(Compound(fr["bearers"] + fr["cross_front"]), "Bearer and front cross member", COL["frame"], b7),
        W(c["tray"].shape, "Hose tray, 1.5 mm sheet", COL["tray"], b7),
        W(c["tray_bolts"].shape, "M8 bolt through the bearer top", "#E5A50A", b7)] if x],
        OUT / "joint-07.png", "Joint 7: hose tray on the bearers",
        subtitle="Tray floor flat on the tube tops; nut and washer under the bearer", elev=30, azim=-60)
    # 8 post in its concrete collar (front left post, cut open)
    sn = M.station_parts()
    b8 = (-850, -450, -1300, -900, -650, 300)
    J[8] = lambda: bv.joint([x for x in [
        W(sn["posts"][0], "Post, 60 mm tube, 600 in the ground", COL["post"], b8),
        W(sn["collars"][0], "Concrete collar, 300 across", COL["collar"], b8)] if x],
        OUT / "joint-08.png", "Joint 8: station post in its concrete collar (cut open)",
        subtitle="Cut through the post; ground level is the top of the collar", cut="+Y", elev=18, azim=-60, size=(6, 6))
    # 9 roof beam on the back right post top, purlin and sheet
    b9 = (560, 760, 600, 820, 2300, 2520)
    J[9] = lambda: bv.joint([x for x in [
        W(sn["posts"][3], "Back post, top cut at 5 deg", COL["post"], b9),
        W(c["beams"].shape, "Roof beam, 40 mm tube", COL["frame"], b9),
        W(c["purlins"].shape, "Purlin, 40 x 20 mm tube", COL["upright"], b9),
        W(c["sheet"].shape, "Roof sheet", COL["roof"], b9)] if x],
        OUT / "joint-09.png", "Joint 9: roof beam, purlin and sheet on a back post",
        subtitle="Seen from the front right and above", elev=22, azim=-55)
    # 10 heat alarm hung under the roof pole
    al = ["al_plate", "al_base", "al_cover", "al_guard", "al_ties", "al_screws"]
    names = {"al_plate": "Aluminium plate", "al_base": "Box base", "al_cover": "Box cover",
             "al_guard": "Printed sensor guard", "al_ties": "Two UV-stable cable ties", "al_screws": "Two M4 screws"}
    J[10] = lambda: bv.joint([K(k, names[k]) for k in al] + [part("Bamboo roof pole", M.alarm_pole(), "#D6C08D")],
        OUT / "joint-10.png", "Joint 10: heat alarm under a roof pole",
        subtitle="Ties round the pole, through the plate slots and tight under the plate", elev=18, azim=-60)
    # 11 inside the heat alarm (cut open)
    inside = {"al_base": "Box base", "al_battery": "3 x AA holder", "al_standoffs": "Standoffs",
              "al_pcb": "Alarm board", "al_piezo": "Piezo sounder", "al_thermistor": "Thermistor bead",
              "al_cover": "Box cover", "al_guard": "Sensor guard"}
    J[11] = lambda: bv.joint([K(k, v) for k, v in inside.items()], OUT / "joint-11.png",
        "Joint 11: inside the heat alarm (cut open)",
        subtitle="Cut through the middle; the thermistor bead sits in the guard, below the box", cut="+Y", elev=12, azim=-70)
    # 12 suction hose coupled to the pump inlet and lying on the left rail (seen from the back left)
    b12 = (-330, 60, 180, 470, 150, 320)
    J[12] = lambda: bv.joint([x for x in [
        W(rails + Compound(fr["cross_rear"]), "Left rail and rear cross member", COL["frame"], b12),
        W(c["pump"].shape, "Pump inlet", COL["pump"], b12),
        W(c["inlet_coupling"].shape, "Cam-lever coupler on the pump inlet", "#9CA3AF", b12),
        W(c["suction_adaptor"].shape, "Hose adaptor with elbow, left coupled", "#E5A50A", b12),
        W(c["suction_run"].shape, "Suction hose, full of water, on the rail top", COL["kit"], b12),
        W(c["hose_straps"].shape, "Rubber strap round rail and hose", COL["wheel"], b12)] if x],
        OUT / "joint-12.png", "Joint 12: suction hose left coupled to the pump inlet",
        subtitle="Seen from the back left and below the deck; the foot valve at the far end keeps the hose and pump full",
        elev=12, azim=130)
    out = []
    for n in sorted(J):
        if which and n not in which:
            continue
        out.append(J[n]())
        print("joint", n, "->", out[-1], flush=True)
    return out


# ----------------------------------------------------------------- steps
CART_STEPS = [
    ("Base frame on its feet", ["frame", "feet"], {"feet": (0, 0, -150)}, "Stand the welded frame on its two rubber feet"),
    ("Handle", ["handle", "grips"], {"handle": (0, -300, 200), "grips": (0, -300, 200)}, "Weld the two arms and the cross bar on; push the grips on"),
    ("Pump stand", ["stand"], {"stand": (0, 0, 350)}, "Weld the stand plate and the two gussets"),
    ("Reel uprights", ["uprights"], {"uprights": (0, 0, 400)}, "Weld the two uprights to the bearers"),
    ("Axle and wheels", ["axle", "wheel_spacers", "wheels", "collars"],
     {"axle": (-700, 0, 0), "wheel_spacers": (0, 0, -250), "wheels": (0, 0, -250), "collars": (0, 0, -250)},
     "Slide the axle through the plates; fit spacer, wheel, collar and R-clip each side"),
    ("Hand pump", ["pump", "pump_bolts", "inlet_coupling"], {"pump": (0, 450, 0), "pump_bolts": (0, 450, 0), "inlet_coupling": (0, 450, -150)},
     "Bolt the pump to the back of the stand plate with four M12 bolts"),
    ("Relief valve", ["relief"], {"relief": (300, 0, 150)}, "Fit the relief valve tee on the pump outlet, outlet pointing down"),
    ("Lever extension", ["lever", "lever_grips"], {"lever": (0, 0, 450), "lever_grips": (0, 0, 450)},
     "Clamp the lever hub on the pump handle socket"),
    ("Hose reel", ["spindle", "reel_spacers", "reel", "swivel"],
     {"spindle": (-500, 0, 0), "reel_spacers": (0, 0, 500), "reel": (0, 0, 500), "swivel": (400, 0, 0)},
     "Hold the drum between the uprights; slide the spindle in; fit the swivel"),
    ("Hoses", ["wound_hose", "conn_hose"], {"wound_hose": (0, 0, 500), "conn_hose": (0, 0, 400)},
     "Connect the pump outlet to the swivel; wind the 30 m hose on"),
    ("Hose tray", ["tray", "tray_bolts"], {"tray": (0, 0, 350), "tray_bolts": (0, 0, 350)}, "Bolt the tray to the bearers with four M8 bolts"),
    ("Suction kit", ["suction_adaptor", "suction_run", "hose_straps", "suction", "strainer", "nozzle", "tap"],
     {"suction_adaptor": (0, 0, -200), "suction_run": (-250, 0, 250), "hose_straps": (-250, 0, 400), "suction": (0, 0, 300),
      "strainer": (0, 0, 450), "nozzle": (0, 0, 450), "tap": (0, 0, 450)},
     "Couple the suction hose to the pump inlet; strap it along the left rail; coil the rest in the tray"),
]
STATION_STEPS = [
    ("Posts in their collars", ["collars_c", "posts"], {"posts": (0, 0, 900), "collars_c": (0, 0, 0)}, "Set the four posts plumb and pour the collars"),
    ("Roof beams", ["beams"], {"beams": (0, 0, 600)}, "Fix one beam across each pair of post tops"),
    ("Purlins and roof sheet", ["purlins", "sheet"], {"purlins": (0, 0, 500), "sheet": (0, 0, 900)}, "Fix the purlins, then screw the sheet down"),
    ("Station alarm box, siren and solar panel", ["station_box", "siren", "panel"],
     {"station_box": (-500, 0, 0), "siren": (-500, 0, 0), "panel": (0, 0, 500)}, "Bolt the box and siren to the back left post; fit the panel rails and panel"),
    ("Sign, drum and cart", ["sign", "drum", "cart"], {"sign": (0, -400, 0), "drum": (700, 0, 0), "cart": (0, -1500, 0)},
     "Bolt the sign on, stand the drum, and push the cart in under the roof"),
]
ALARM_STEPS = [
    ("Plate on the box base", ["al_plate", "al_base", "al_screws"], {"al_plate": (0, 0, 40), "al_screws": (0, 0, 60), "al_base": (0, 0, 0)},
     "Screw the plate to the box base with two M4 screws from inside"),
    ("Battery holder and board", ["al_battery", "al_standoffs", "al_pcb", "al_piezo"],
     {"al_battery": (0, 0, -60), "al_standoffs": (0, 0, -80), "al_pcb": (0, 0, -110), "al_piezo": (0, 0, -110)},
     "Stick the battery holder in; screw the board onto its standoffs"),
    ("Cover, thermistor and guard", ["al_thermistor", "al_cover", "al_guard"],
     {"al_thermistor": (0, 0, -60), "al_cover": (0, 0, -110), "al_guard": (0, 0, -160)},
     "Lead the thermistor out through the 12 mm hole; close the cover; glue the guard on"),
    ("Hang it under a roof pole", ["al_ties"], {"al_ties": (0, 0, 120)}, "Two UV-stable ties round the pole and through the plate slots"),
]


def steps(which=None):
    c = comps()
    cart_all = Compound([x.shape for x in c.values() if x.group == "cart"])
    nice = {"frame": "Base frame", "feet": "Rubber feet", "collars_c": "Concrete collars"}
    out, n = [], 0
    for grp, seq, view in (("cart", CART_STEPS, (24, -58)), ("station", STATION_STEPS, (22, -55)), ("alarm", ALARM_STEPS, (18, -60))):
        done = []
        for title, keys, ex, sub in seq:
            n += 1
            new = []
            for k in keys:
                if k == "cart":
                    new.append(part("Hose cart", cart_all, COL["frame"], ex[k]))
                else:
                    new.append(K(k, nice.get(k), None, ex.get(k, (0, 0, 0))))
            ctx = [part("Bamboo roof pole", M.alarm_pole(), "#D6C08D")] if title.startswith("Hang it") else []
            if not which or n in which:
                out.append(bv.step(done, new, OUT / f"step-{n:02d}.png", f"Step {n}: {title}", subtitle=sub,
                                   context=ctx, elev=view[0], azim=view[1], label_done=False))
                print("step", n, "->", out[-1], flush=True)
            done += [part(x.name, x.shape, x.color) for x in new if x.name != "Hose cart"] + \
                    ([part("Hose cart", cart_all, "#D1D5DB")] if any(x.name == "Hose cart" for x in new) else [])
    return out


if __name__ == "__main__":
    args = sys.argv[1:] or ["overview", "sheets", "joints", "steps"]
    what, nums = args[0], {int(a) for a in args[1:]} or None
    {"overview": lambda _: overview(), "sheets": sheets, "joints": joints, "steps": steps}[what](nums)
