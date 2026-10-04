---
doc_id: CBK-BLD-001
title: CampBreak prototype build plan
project: CampBreak
doc_type: Build plan
version: "0.3"
status: Draft
date: '2026-10-03'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
  - version: "0.1"
    date: '2026-10-03'
    author: Amish Chadha
    change: First build plan; design made constructable (CBK-DDR-002)
  - version: "0.2"
    date: '2026-10-03'
    author: Amish Chadha
    change: "Amish's R9 decision 1A (CBK-DDR-003): check foot valve, suction hose left coupled to the pump and strapped to the rail, go-when-two-arrive drill card"
  - version: "0.3"
    date: '2026-10-03'
    author: Amish Chadha
    change: "Amish's round-2 decision 1A (CBK-DDR-004): delivery hose stowed full of water, filled at Step 12 and topped up at the weekly check; cart weight and pull updated"
---

# CampBreak prototype build plan

**Plan, not yet built.** How to build the first proof-of-concept prototype, component by component. Building and testing to it is TRL 4 work. Decisions are kept in the design decisions register ([docs/06-design-decisions.md](06-design-decisions.md)), not here.

## 1. What you are building

![Figure 1. Every component, pulled apart and numbered in build order](05-build-plan/overview.png)

*Figure 1. Every component pulled apart and numbered in build order: the hose cart (1 to 12), the block station (13 to 18) and one heat alarm (19, drawn five times its size).*

The prototype is one block kit: a two-wheeled hose cart with a hand pump, a shaded block station for the cart with a siren and a water drum, and a heat alarm of the kind hung in each shelter (a drill block has 24). Figure 1 shows the 19 component groups in the order you make or fit them. The made parts are the welded cart frame, handle, pump stand and reel uprights, the axle and spindle pieces, the lever extension, a folded sheet-steel hose tray, the four station posts with their roof frame, the sign and the alarm's mounting plate and drilled box. Everything else is bought and fitted: wheels, pump, relief valve, reel drum, hoses, nozzle, couplings, roof sheet, drum, the station's box, battery, siren and panel, and the alarm's board, cells and sounder. The work is sawing, drilling and MIG welding mild steel tube and plate, folding thin sheet, pouring four concrete collars, and drilling plastic boxes. The parts cost about USD 1,374 from the bill of materials.

> **Safety:** The finished cart is a pressurised water system: two people can push the pump to several bar against a shut nozzle, so the 4 bar relief valve must be fitted before the first pumping, discharge pointing at the ground. Welding needs a screen, gloves, a mask and a fire watch; grind and weld well away from fuel and shelters. The loaded cart weighs about 103 kg, with its pump, suction hose and delivery hose kept full of water: two people lift and move it. The station roof is put up from a stepladder by two people, never in wind. The station battery is sealed lead-acid: connect its fuse last.

## 2. What changed to make it buildable

The concept showed what the kit does; its parts were blocks with no stock size and no fixings. Each change below keeps what the kit does, and all of them are recorded in decision record CBK-DDR-002.

*Table 1. Changes from the concept.*

| Component | The concept had | The buildable design has | Why |
| --- | --- | --- | --- |
| Cart frame | A solid platform | A welded frame of 30 mm square tube with two lines of bearers (Figure 2) | One tube size, square cuts, every joint a weld on a flat table |
| Wheels | Wheels on the frame sides, no axle mounting | A 20 mm through axle in four 8 mm axle plates, with spacers, collars and R-clips (Figure 15) | The axle runs in two plates each side and clears the tubes |
| Legs | None; the cart stood on its wheels only | Two short legs with rubber feet at the front | The cart parks level |
| Handle | A bar floating in front | Two arms sitting on the rail tops, coped to a cross bar (Figures 4 and 5) | A welded triangle at each foot |
| Pump mounting | Pump on the deck, no fixing | A 10 mm stand plate with two gussets; four M12 bolts (Figure 7) | Puts the shaft 440 mm up so the lever clears the wheels |
| Lever | The pump's own short handle | A clamp-on lever with a T-bar for two people (Figure 12) | About 28 N per person |
| Reel | A cylinder, no support | A bought drum on a 25 mm spindle in two welded uprights with a swivel inlet (Figure 9) | The hose pays out while the pump stays connected |
| Pump to reel | Nothing | A 1.2 m connecting hose and the 4 bar relief valve on a tee (Figure 16) | The relief water goes to the ground |
| Small parts | Loose | A folded tray bolted to the bearers (Figures 13 and 14) | Everything travels on the cart and drains |
| Station | Two posts holding a cantilever roof | Four posts in concrete collars, two beams, four purlins and a sheet (Figures 18 to 21) | Resists monsoon uplift with plain bolts and welds |
| Suction hose | Coiled loose in the tray, coupled and primed at the fire | Left coupled to the pump inlet, strapped along the left rail, with a check foot valve that keeps the pump full (Figure 17; CBK-DDR-003) | Nothing to couple or prime at the fire: water about 30 s sooner |
| Heat alarm | A box glued to the roof | An aluminium plate on the box, hung on a roof pole by two ties (Figures 24 and 25) | Fits any bamboo pole; no screws into bamboo |

## 3. Making the components

Make and check each component before the assembly step that needs it. Sizes are in millimetres. "Front" is the pull handle end of the cart; "left" and "right" are as seen standing behind the handle, facing the cart. Workshop tolerance is 1 mm on the cart and 5 mm on the station unless a step says otherwise; drawings carry no tolerances before TRL 4.

### 3.1 Cart base frame

![Figure 2. Making sketch of the cart base frame](../cad/drawings/CBK-DWG-101.png)

*Figure 2. Cart base frame making sketch (CBK-DWG-101).*

**What it is and what it is made from.** The ladder frame everything on the cart hangs from. Mild steel square tube 30 x 30 x 2 mm (S235), about 7.6 m in all, and 8 mm flat plate for the four axle plates.

**How to make it.**

1. Cut two side rails 1,000 long, three cross members 540 long (cut the middle one later into pieces of 110, 260 and 110), two front bearers 320 long, two rear bearers 590 long and two legs 190 long. Square all ends and deburr.
2. Lay the side rails on a flat table, 540 apart inside. Weld the front cross member flush with the rail front ends and the rear one with its back face 30 in from the rail back ends. Check that the diagonals are equal within 3 mm, then weld.
3. Mark the middle cross member line 350 behind the front cross member. Fit its two 110 pieces from the rails inward and the 260 piece in the middle, leaving a 30 gap each side for the bearers.
4. Fit the bearers in those gaps, 260 apart inside: the front pair from the front cross member to the middle line, the rear pair from the middle line to the rear cross member. All tube tops flush. Weld.
5. Cut four axle plates 80 x 85 x 8. Clamp them as a stack and drill a 21 mm hole centred across the width, 40 up from the bottom edge.
6. Weld one plate on each side of each rail, centred 800 behind the rail front ends, tops flush with the rail top, with a 20 mm bar through all four holes so they line up. Remove the bar after cooling.
7. Weld a leg under each rail's front end, square to the rail.

**How it fits the parts next to it.** The handle arms sit on the rail tops at the front (Figure 4). The pump stand plate sits on the rear cross member and its gussets on the rear bearers (Figure 7). The reel uprights stand against the inner faces of the rear bearers (Figure 9). The axle runs through the four plates (Figure 15). The tray sits on the bearers and the front cross member (Figure 14).

**Check before moving on.** The frame sits flat on the table without rocking; the 20 mm bar turns by hand in all four plates at once.

### 3.2 Pull handle

![Figure 3. Making sketch of the pull handle](../cad/drawings/CBK-DWG-102.png)

*Figure 3. Pull handle making sketch (CBK-DWG-102).*

**What it is and what it is made from.** Two arms and a cross bar that two people pull side by side. 30 x 30 x 2 mm square tube for the arms; 33.7 x 2.6 mm round tube, 820 long, for the bar; two rubber grips.

**How to make it.**

1. Cut two arms about 820 long. Cut the foot end of each at 44° so it lies flat on the rail top with its toe touching the front cross member's end.
2. Cope the top end of each arm to fit round the 33.7 mm bar (a saddle cut with a hole saw or a grinder and a paper template).
3. Set the frame on the table, clamp the bar 800 above the floor and 550 in front of the rail front ends, centred, and tack the arms to the rails and the bar, 125 in from each bar end.
4. Check that the bar is level and square to the frame, then weld all round.
5. Push a grip onto each bar end with soapy water.

**How it fits the parts next to it.**

![Figure 4. Joint 2: handle arm foot on the rail top](05-build-plan/joint-02.png)

*Figure 4. The arm foot sits flat on the rail top and its toe touches the end of the front cross member; welded all round.*

![Figure 5. Joint 3: arm coped to the cross bar](05-build-plan/joint-03.png)

*Figure 5. The saddle-cut arm end wraps the bar; welded all round.*

**Check before moving on.** The bar is level within 3 mm. Lift the frame by the bar: nothing flexes visibly.

### 3.3 Pump stand plate and gussets

![Figure 6. Making sketch of the pump stand](../cad/drawings/CBK-DWG-103.png)

*Figure 6. Pump stand making sketch (CBK-DWG-103).*

**What it is and what it is made from.** An upright plate the pump bolts to, braced by two triangles. 10 mm plate 320 x 355; two 8 mm triangles 130 x 250.

**How to make it.**

1. Cut the plate 320 wide and 355 tall. Mark the centre line.
2. Lay the bought pump's flange on the plate, centred on the centre line with the shaft 195 up from the bottom edge, and mark its four holes (on a 150 mm square for the pump specified). Drill 13 mm.
3. Cut two right-angled triangles, 130 along the bottom and 250 tall.
4. Stand the plate on the rear cross member, its front face 10 behind the member's front face and square to the bearers. Weld it to the cross member on both sides.
5. Stand each gusset on a rear bearer, centred on it, against the plate's front face. Weld to the bearer and the plate.

**How it fits the parts next to it.**

![Figure 7. Joint 4: hand pump bolted to the stand plate](05-build-plan/joint-04.png)

*Figure 7. The pump flange sits flat on the plate's back face; four M12 bolts with washers both sides.*

**Check before moving on.** The plate is upright within 1°; the pump's bolts pass through all four holes without forcing.

### 3.4 Reel uprights

![Figure 8. Making sketch of the reel uprights](../cad/drawings/CBK-DWG-104.png)

*Figure 8. Reel upright making sketch (CBK-DWG-104).*

**What it is and what it is made from.** Two flat bars that carry the reel spindle. 50 x 8 mm flat bar, two pieces 365 long.

**How to make it.**

1. Cut both bars 365 long and clamp them together.
2. Drill a 26 mm hole through both, centred across the width, 320 up from the bottom end.
3. Stand each bar against the inside face of a rear bearer, bottom end flush with the bearer bottom, its centre 130 in front of the axle centre line. Pass a 25 mm bar through both holes to hold them in line, then weld along both edges.

**How it fits the parts next to it.**

![Figure 9. Joint 5: reel spindle, spacer and swivel (cut open)](05-build-plan/joint-05.png)

*Figure 9. The spindle passes through the upright, a 12 mm spacer and the drum; the swivel inlet sits on the right-hand end.*

**Check before moving on.** The 25 mm bar slides through both holes at once and is level within 2 mm.

### 3.5 Axle, wheel spacers and collars

![Figure 10. Making sketch of the axle and spacers](../cad/drawings/CBK-DWG-105.png)

*Figure 10. Axle and spacers making sketch (CBK-DWG-105).*

**What it is and what it is made from.** A 20 mm bright steel bar 850 long, two spacers cut from 32 x 22 mm tube, two bought 20 mm collars and two R-clips.

**How to make it.**

1. Cut the axle 850 long; chamfer both ends 1 mm.
2. Drill a 4 mm cross hole 6 from each end for the R-clips.
3. Cut two spacers 22 long from the tube; square and deburr the ends.

**How it fits the parts next to it.** See Figure 15 in section 3.9. From the middle out on each side: inner axle plate, rail, outer axle plate, spacer, wheel hub, collar, R-clip.

**Check before moving on.** With both wheels on, the axle end float is 1 to 2 mm and the wheels spin freely.

### 3.6 Reel spindle and spacers

![Figure 11. Making sketch of the reel spindle](../cad/drawings/CBK-DWG-106.png)

*Figure 11. Reel spindle making sketch (CBK-DWG-106).*

**What it is and what it is made from.** A 25 mm bright steel bar 290 long, two spacers cut from 40 x 26 mm tube, one bought 25 mm collar.

**How to make it.**

1. Cut the spindle 290 long; chamfer both ends 1 mm.
2. Cut two spacers 12 long; deburr.
3. Check the reel drum's bore against the spindle; if the bore is larger, sleeve it (see the register, to confirm).

**How it fits the parts next to it.** Figure 9: left upright, spacer, drum, spacer, right upright, swivel. The collar sits against the outside of the left upright.

**Check before moving on.** The drum turns by hand with 1 to 2 mm of side float.

### 3.7 Lever extension with T-grip

![Figure 12. Making sketch of the lever extension](../cad/drawings/CBK-DWG-107.png)

*Figure 12. Lever extension making sketch (CBK-DWG-107).*

**What it is and what it is made from.** A clamp hub that fits the pump's handle socket, a 585 mm lever of 33.7 x 2.6 mm tube and a 400 mm T-bar of 27 x 2.3 mm tube with two grips.

**How to make it.**

1. Cut a 50 x 50 block 38 thick. Bore it to fit the pump's handle socket (measured on the pump bought), slot it on one side and drill and tap for two M10 clamp bolts.
2. Weld the lever tube upright on the hub.
3. Weld the T-bar across the top, square to the pump shaft, so the bar centre is 610 above the shaft centre.
4. Push the grips on.

**How it fits the parts next to it.** The hub clamps on the pump's handle socket with the lever upright at mid-stroke. Two people face each other across the T-bar and swing it 40° each way.

**Check before moving on.** At both ends of the swing the grip is at least 50 from the wheels and 30 from the frame.

### 3.8 Hose tray

![Figure 13. Making sketch of the hose tray](../cad/drawings/CBK-DWG-108.png)

*Figure 13. Hose tray making sketch (CBK-DWG-108).*

**What it is and what it is made from.** An open tray that carries the suction hose and small parts. 1.5 mm galvanised steel sheet, blank 560 x 530.

**How to make it.**

1. Cut the blank and cut an 80 mm square from each corner.
2. Drill six 12 mm drain holes in the floor (three across at 120 spacing, two rows 200 apart) and four 9 mm bolt holes, 145 each side of the centre line and 120 in front of and behind the middle.
3. Fold the four sides up 90° to 80 tall. The tray is 400 x 370 outside.
4. Pop-rivet the corners and paint the cut edges with zinc-rich paint.

**How it fits the parts next to it.**

![Figure 14. Joint 7: hose tray on the bearers](05-build-plan/joint-07.png)

*Figure 14. The tray floor sits flat on the tube tops; an M8 bolt through each bearer top, nut and washer below.*

**Check before moving on.** The tray sits flat and clears the handle arms by 30 mm.

### 3.9 Bought cart parts

What to buy for the cart (full specifications in the bill of materials), and what to do to each:

- **Wheels:** two 400 mm puncture-proof wheelbarrow wheels, 100 mm wide, with 20 mm bore ball-bearing hubs 75 long. Nothing to do.
- **Hand pump:** a cast-iron double-acting semi-rotary pump with 25 mm ports, at least 0.40 L per double stroke and rated for at least 40 m head. Measure its flange holes and handle socket before drilling the stand plate (3.3) and boring the lever hub (3.7).
- **Relief valve:** a 19 mm spring relief valve set at 4 bar, with a tee. Fit it at the pump outlet with the discharge pointing down.
- **Reel drum:** a steel reel drum with a 200 mm core and 500 mm flanges, 210 apart, and a 19 mm swivel inlet with a hose tail.
- **Hoses:** 30 m of 19 mm semi-rigid hose rated at least 10 bar; 1.2 m of 19 mm reinforced hose and two clips for the pump to reel connection; 4 m of 25 mm wire-reinforced suction hose that bends to 60 mm radius or less.
- **Foot valve:** a 25 mm brass spring-loaded foot valve with a check that seals and a stainless strainer. It keeps the suction hose and the pump full of water between uses. Before you buy, fill one on its hose, hang it up and see that it holds water overnight.
- **Nozzle, couplings and tap adaptor:** a jet and spray nozzle with shut-off and a 6 mm jet; three 25 mm cam-lever coupling sets, the suction hose's one with a 90° elbow hose tail; a push-on tap connector to a 25 mm hose tail.
- **Hose straps:** two rubber straps with buckles, 20 mm wide, long enough to go round the rail and the hose.

![Figure 15. Joint 1: axle, axle plates, spacer and wheel hub (cut open)](05-build-plan/joint-01.png)

*Figure 15. The axle passes through 21 mm holes in both axle plates; the spacer holds the hub clear of the outer plate; the collar and R-clip hold it on.*

![Figure 16. Joint 6: pump outlet, relief valve and connecting hose](05-build-plan/joint-06.png)

*Figure 16. Seen from the back right: the relief valve sits on a tee at the pump outlet with its discharge pointing down; the connecting hose runs from the outlet tail over to the reel swivel, a clip at each end.*

![Figure 17. Joint 12: suction hose left coupled to the pump inlet](05-build-plan/joint-12.png)

*Figure 17. Seen from the back left: the suction hose's adaptor stays locked in the coupler under the pump. Its elbow sends the hose left, up behind the end of the left rail and forward along the rail top, under a rubber strap. The foot valve at the far end keeps the hose and the pump full of water.*

### 3.10 Station posts and concrete collars

![Figure 18. Making sketch of the station posts](../cad/drawings/CBK-DWG-109.png)

*Figure 18. Station posts making sketch (CBK-DWG-109), left pair drawn.*

**What it is and what it is made from.** Four posts of 60 x 60 x 3 mm square tube, two front posts 3,160 long and two back posts 3,000 long, each set 600 into a concrete collar 300 across. Four bags of concrete and some gravel.

**How to make it.**

1. Cut the posts to length with the tops cut at 5° so the roof falls toward the back.
2. Drill two 13 mm holes across each post top, 60 down, for the beam cleats.
3. Paint the bottom 700 of each post with bitumen and cap the tops.
4. Peg out the four post centres: 1,300 apart across and 1,800 front to back; check the diagonals are equal within 10.
5. Auger four holes 300 across and 650 deep. Put 50 of gravel in each.
6. Stand each post on the gravel, plumb it in both directions and brace it. Pour concrete to ground level, sloped away from the post. Leave three days before loading.

**How it fits the parts next to it.**

![Figure 19. Joint 8: station post in its concrete collar (cut open)](05-build-plan/joint-08.png)

*Figure 19. The post stands 600 into its collar; the top of the collar is ground level.*

**Check before moving on.** Each post is plumb within 5 mm over 2 m; the back post tops are 2,400 above the ground.

### 3.11 Roof frame: beams, purlins and sheet

![Figure 20. Making sketch of the roof frame](../cad/drawings/CBK-DWG-110.png)

*Figure 20. Roof beams and purlins making sketch (CBK-DWG-110).*

**What it is and what it is made from.** Two beams of 40 x 40 x 2 mm tube, 2,000 long; four purlins of 40 x 20 x 2 mm tube, 1,500 long; one corrugated galvanised sheet 1,500 x 2,050; angle cleats, M8 bolts and roofing screws.

**How to make it.**

1. Cut the beams and purlins. Cut four cleats from 40 x 40 x 4 angle and drill them to match the post top holes.
2. Bolt a cleat to each post top. Lift each beam onto a pair of posts so it reaches 100 past the front and back post centres, and bolt or weld it to the cleats.
3. Fix the purlins across the beams at 30, 660, 1,300 and 1,940 from the beams' front ends.
4. Screw the sheet to every purlin through every second crest, with sealing washers.

**How it fits the parts next to it.**

![Figure 21. Joint 9: roof beam, purlin and sheet on a back post](05-build-plan/joint-09.png)

*Figure 21. The beam sits on the cut post top; the purlins sit on the beams; the sheet sits on the purlins.*

**Check before moving on.** The roof falls 5° to the back and does not move when pushed at a corner.

### 3.12 Station sign

![Figure 22. Making sketch of the station sign](../cad/drawings/CBK-DWG-111.png)

*Figure 22. Station sign making sketch (CBK-DWG-111).*

**What it is and what it is made from.** A 440 x 300 x 3 mm aluminium sheet with printed instructions in the camp languages and pictograms.

**How to make it.**

1. Cut the sheet and round the corners.
2. Drill two 9 mm holes on the centre line, 60 from the top and bottom edges.
3. Apply the printed vinyl: leave first, raise the alarm, fetch the cart, small fires only, never water on oil or live wires, call the fire service.

**How it fits the parts next to it.** It bolts to the front face of the back right post with two M8 bolts, bottom edge 1,100 above the ground.

**Check before moving on.** It reads clearly from 5 m in daylight.

### 3.13 Bought station parts

- **Station alarm box:** a lockable IP65 box 300 x 300 x 150 holding the receiver board (the alarm board with a relay output), a solar charge controller and a 12 V 7 Ah sealed lead-acid battery with an inline fuse at its positive terminal. Drill it for the cable glands; mount it with U-bolts on the outer face of the back left post, bottom 1,400 above the ground.
- **Siren:** a 12 V siren of at least 110 dB(A) at 1 m on a bolted bracket on the same post, 1,900 up.
- **Solar panel:** a 10 W 12 V panel 350 x 290 on two rails screwed to the roof sheet near the back edge.
- **Water drum:** a 200 L food-grade drum with lid, beside the right of the station.

### 3.14 Heat alarm: mounting plate, box and guard

![Figure 23. Making sketch of the heat alarm housing](../cad/drawings/CBK-DWG-112.png)

*Figure 23. Heat alarm housing making sketch (CBK-DWG-112).*

**What it is and what it is made from.** A 140 x 50 x 3 mm aluminium plate, a stock two-part ABS box 100 x 100 x 40, and a small printed guard cup in PETG. Bought parts inside: the alarm board (low-power controller and sub-GHz radio with a thermistor input), a thermistor on a 40 mm lead, a piezo sounder of at least 95 dB(A) at 1 m, a 3 x AA holder with alkaline cells, four standoffs, and two UV-stable cable ties.

**How to make it.**

1. Cut the plate. Mark and file four slots 8 x 3, 58 each side of the middle, from 24 to 27 off the long centre line. Drill two 4.5 mm holes 30 each side of the middle.
2. Drill the box base to match the plate holes (3.3 mm) and screw the plate on from inside with two M4 screws.
3. Drill a 12 mm hole in the middle of the cover and eight 5 mm sound holes round a point 25 from the middle, over where the sounder will sit.
4. Print the guard (24 across, 14 tall, six side slots).
5. Fit the battery holder to the base with double-sided foam tape, screw the board onto its standoffs, lead the thermistor bead out through the 12 mm hole, close the cover and glue the guard over the hole.

**How it fits the parts next to it.**

![Figure 24. Joint 10: heat alarm under a roof pole](05-build-plan/joint-10.png)

*Figure 24. Two ties go round the pole, down through the plate slots and tight under the plate.*

![Figure 25. Joint 11: inside the heat alarm (cut open)](05-build-plan/joint-11.png)

*Figure 25. The board sits on standoffs 12 clear of the battery holder; the thermistor bead hangs in the guard below the box, in moving air.*

**Check before moving on.** The cover closes on its seal with nothing pinched; the bead does not touch the guard.

## 4. Putting it together

Parts already fitted are grey; the part being fitted is in colour, pulled back along the way it goes in.

### Step 1: Base frame on its feet

![Step 1](05-build-plan/step-01.png)

Push the rubber feet onto the legs (a dab of contact adhesive) and stand the frame on them.

### Step 2: Handle

![Step 2](05-build-plan/step-02.png)

Weld the handle on as in section 3.2 and fit the grips.

### Step 3: Pump stand

![Step 3](05-build-plan/step-03.png)

Weld the stand plate and gussets as in section 3.3.

### Step 4: Reel uprights

![Step 4](05-build-plan/step-04.png)

Weld the two uprights to the rear bearers as in section 3.4. Prime and paint the frame now, before anything is bolted on; mask the axle plate holes and the stand plate's back face.

### Step 5: Axle and wheels

![Step 5](05-build-plan/step-05.png)

Grease the axle. Slide it through all four axle plates. On each side fit a spacer, the wheel, a collar (set screw tightened) and an R-clip.

**Hold point:** the cart rolls straight and both wheels spin freely.

### Step 6: Hand pump

![Step 6](05-build-plan/step-06.png)

Two people lift the pump (about 14 kg) onto the back of the stand plate and fit four M12 x 40 bolts with washers both sides. Fit the 25 mm cam-lever coupler to the inlet, pointing down.

### Step 7: Relief valve

![Step 7](05-build-plan/step-07.png)

Fit the tee and relief valve to the pump outlet with thread sealant, discharge pointing straight down.

### Step 8: Lever extension

![Step 8](05-build-plan/step-08.png)

Clamp the lever hub on the pump's handle socket with the lever upright at mid-stroke and tighten both clamp bolts.

**Hold point:** swing the lever 40° each way: the grip clears the wheels by at least 50 and the frame by at least 30.

### Step 9: Hose reel

![Step 9](05-build-plan/step-09.png)

Hold the drum between the uprights with a spacer each side. Slide the spindle in from the left, fit the collar outside the left upright, and fit the swivel inlet on the right-hand end.

### Step 10: Hoses

![Step 10](05-build-plan/step-10.png)

Fit the connecting hose from the pump outlet tail over to the swivel tail, with a clip at each end. Fit the 30 m hose to the drum's outlet and wind it on in neat even layers; it fills the drum, so a loose wind will not fit. Fit the nozzle to the free end.

### Step 11: Hose tray

![Step 11](05-build-plan/step-11.png)

Bolt the tray to the bearers with four M8 bolts, washers and nyloc nuts.

### Step 12: Suction kit

![Step 12](05-build-plan/step-12.png)

Fit the foot valve to one end of the suction hose and the cam-lever adaptor with its elbow to the other. Push the adaptor into the coupler under the pump and close both cam levers; it stays coupled from now on. Lead the hose to the left, up behind the end of the left rail and forward along the rail top, and fasten it with the two rubber straps. Coil the rest in the tray with the foot valve on top, and lay the tap adaptor inside the coil. Stow the nozzle in the tray when the hose is wound. Fit the reflective tape and the pump instruction label.

**Prime it once.** Stand the foot valve in a bucket of water and pump until water comes out of the nozzle, then lift the foot valve out. From now on the check in the foot valve keeps the pump and the suction hose full (see the weekly check on the drill card, section 5a). 

**Fill the delivery hose.** With the foot valve still in the bucket, run out the 30 m hose, open the nozzle and pump until water runs steadily from it, then close the nozzle shut-off and wind the full hose back onto the reel. The shut-off holds the water in; the 4 bar relief valve protects the full hose if the sun heats it. Top the bucket up if it runs low. A full hose is heavy to wind (about 8.9 kg of water), so wind it with two people.

### Step 13: Posts in their collars

![Step 13](05-build-plan/step-13.png)

Set the posts and pour the collars as in section 3.10.

### Step 14: Roof beams

![Step 14](05-build-plan/step-14.png)

Fix the beams to the post tops as in section 3.11.

**Hold point:** posts plumb and braced; concrete at least three days old.

### Step 15: Purlins and roof sheet

![Step 15](05-build-plan/step-15.png)

Fix the purlins, then screw the sheet down.

### Step 16: Station alarm box, siren and solar panel

![Step 16](05-build-plan/step-16.png)

U-bolt the box to the back left post and bolt the siren bracket above it. Screw the panel rails to the sheet and bolt the panel on. Run the cables through glands into the box. Wire the panel to the charge controller and the siren to the relay output; connect the battery last, through its fuse.

### Step 17: Sign, drum and cart

![Step 17](05-build-plan/step-17.png)

Bolt the sign to the back right post. Stand the drum beside the station and fill it. Push the cart in under the roof, handle to the front.

### Step 18: Plate on the box base

![Step 18](05-build-plan/step-18.png)

Screw the mounting plate to the alarm box base with two M4 screws from inside.

### Step 19: Battery holder and board

![Step 19](05-build-plan/step-19.png)

Fit the battery holder, the standoffs and the board with its sounder. Leave the cells out.

### Step 20: Cover, thermistor and guard

![Step 20](05-build-plan/step-20.png)

Lead the thermistor out through the cover hole, close the cover and glue the guard on.

### Step 21: Hang it under a roof pole

![Step 21](05-build-plan/step-21.png)

Put the cells in, close the box, and hang it under a roof pole about 300 from the ridge with two UV-stable ties through the plate slots, pulled tight under the plate.

## 5. First checks

These are listed here and recorded at TRL 4 in a test report.

*Table 2. First checks.*

| Check | Requirement | How | Pass when |
| --- | --- | --- | --- |
| Cart width | R6 | Tape across the tyres | 900 mm or less |
| Pulling | R6 | Two adults pull the loaded cart (delivery hose full) 100 m up a 10 % unpaved slope; note the effort | 3 min or less; effort per person against the 100 N assumed (about 101 N expected) |
| Flow | R7 | Pump from a drum into a measured container for 1 min, then for 10 min | At least 20 L/min, kept up for 10 min |
| Relief valve | R7, safety | Shut the nozzle and pump slowly; watch a gauge on the tee | Valve opens at 4 bar ± 0.5; nothing leaks |
| Jet reach | R8 | Measure where the jet lands on level ground at 30° | 6 m or more |
| Alarm trigger | R1 | Warm the bead with a hot-air gun through a ramp logged by a reference thermometer | Sounds at 8 °C per minute or faster, and at 57 °C |
| Alarm sound | R3 | Sound meter at 3 m | 85 dB(A) or more |
| Relay | R4 | Trigger one alarm in a mock block | Station siren and every alarm within 10 s |
| Cooking | R2 | One hour of stove cooking 1 m from an alarm in a mock shelter | No alarm |
| Pump stays primed | R9 | Leave the primed cart a week, drop the foot valve in a drum and pump | The lever takes load within 3 strokes; water at the nozzle in about 30 s; no drip from the foot valve |
| Hose stays full | R9 | Leave the cart with the delivery hose full and the nozzle shut for a week, then open the nozzle | Water leaves the nozzle at once with no air; no drip at the nozzle or swivel |
| Drill | R9 | Timed drill from the siren to water on target at 70 m and 100 m, using the drill card | 3 min or less at both distances (2.95 min and 2.5 min expected) |

## 5a. Drill card

The drill card is printed in the camp languages, laminated and kept in the station box; the station sign carries the first line. Volunteers practise it until the first two are away with the cart within 30 s of the siren.

*Table 3. Drill card.*

| When | What to do |
| --- | --- |
| Siren sounds | Everyone in the burning shelter and its neighbours gets out first. Volunteers go to the station |
| At the station | **Go when two arrive.** The first two volunteers take the cart out at once; do not wait for more. Never more than 30 s from the siren. Two people always move the cart; never run with it |
| Others | Follow to the fire; take over the second side of the pump lever when you arrive |
| At the fire | Park the cart on its feet, upwind, at least 6 m from the fire. Person 1: lift the suction hose off the rail, drop the foot valve in the drum or water, and start pumping; it is already coupled and primed. Person 2: run out the hose from the reel and aim at the base of the fire. The hose is already full, so water leaves the nozzle as soon as the first strokes lift water |
| Never | Water on burning oil or live wiring. Go into a burning shelter |
| Every week | Prime check: drop the foot valve in the station drum and pump. The lever should take load within three strokes and water reach the nozzle in about 30 s. If not, re-prime (Step 12) and report the foot valve. Then check that the delivery hose is still full: open the nozzle for a moment; if air comes out, pump until water runs, shut the nozzle and wind the hose back |

## 6. Safety stops

Work stops at each point below until what is listed is true.

1. **Before welding:** screen, gloves and mask on; fire extinguisher and a fire watch in place; no fuel, tarpaulin or shelters within 10 m.
2. **Before the first pumping:** the relief valve is fitted with its discharge pointing down; every hose clip and coupling is tight; the hose shows no cuts or kinks; nobody stands in front of the nozzle.
3. **Before pumping against a shut nozzle (relief check):** a pressure gauge is fitted on the tee, and the person pumping goes slowly and stops at 4.5 bar if the valve has not opened.
4. **Before moving the loaded cart on a slope:** two people on the handle, a third holding back on slopes steeper than 10 %; nobody in front of the cart downhill.
5. **Before putting up the roof:** posts braced and the concrete at least three days old; two people on stepladders; no work in wind.
6. **Before connecting the station battery:** the fuse is out, all wiring is finished and checked, and the box can be locked.
7. **Before any drill with fire:** the fire service or the camp's fire safety focal point is present, the fire is a small controlled test fire in a cleared area, and everyone knows that people leave first and water is never used on burning oil or live wiring.

## 7. Tools, skills and workspace

- **Workshop:** a flat steel or concrete welding table at least 1.2 x 2 m, a bench vice, and space to roll the finished cart out.
- **Tools:** angle grinder with cutting and flap discs, chop saw or hacksaw, pillar drill with bits to 26 mm (or a 21 mm and 26 mm hole saw in a magnetic drill), MIG welder (or stick welder), clamps, square and tape, hand folder or bending brake for 1.5 mm sheet, pop-rivet gun, taps M4 and M10, spanners to 19 mm, post-hole auger, spirit level, stepladders, a small soldering iron and screwdrivers for the alarm, a 3D printer for the guard.
- **Skills:** basic fabrication and fillet welding of thin-wall tube; setting posts in concrete; simple electrical wiring with a fuse. No machining is needed beyond drilling.
- **People:** two for lifting the pump and the roof parts; one for the alarm.

## 8. Where the numbers come from

- Model: `cad/src/model.py` (constructable design and its 115 constructability checks)
- General arrangement: `cad/drawings/CBK-DWG-001` (from `cad/src/sheets.py`)
- Making sketches and pictures: `cad/drawings/CBK-DWG-101` to `112` and `docs/05-build-plan/` (from `cad/src/build_plan_media.py`)
- Calculations: `docs/04-calcs/01-sizing.md` (CBK-CAL-001) and `docs/04-calcs/sizing.py`
- Bill of materials: `bom/bom.csv`
- Decision records: `docs/decisions/0001-trl2-review-decisions.md`, `docs/decisions/0002-design-for-construction.md` and `docs/decisions/0003-r9-response-time.md`
