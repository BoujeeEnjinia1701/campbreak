---
doc_id: CBK-DDR-002
title: CampBreak design for construction
project: CampBreak
doc_type: Design decision record
version: "0.1"
status: Draft
date: '2026-10-03'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-10-03'
  author: Amish Chadha
  change: Changes that make the concept buildable, decided under Amish's 2026-10-03 pre-approval
---

# 0002: Design for construction

- **Date:** 2026-10-03
- **Status:** decided. Amish, 2026-10-03: "start with the first 14 repos from the list of 29 projects. I pre-approve the batch runs along with any recommendations you come up with. I also accept any cost overruns or variations from the assumed scope cost." This covers every change below.

## Context

STANDARDS section 18 requires a constructable design at TRL 3 (Amish, 2026-09-30: "fix the design assumptions to match and be physically feasible"). The TRL 2 massing model showed what CampBreak does (an alarm in each shelter, a station, and a two-wheeled cart with a hand pump, reel and hose) but its parts were blocks with no process and no fixings. The parametric model `cad/src/model.py` was rebuilt so that every part is cut, drilled, welded, folded, cast or bought, and every joint has a fixing. It runs 97 constructability checks (`python3 cad/src/model.py --check`): parts that must touch do touch with no overlap, and parts that must stay apart keep a stated clearance, including the pump lever at both ends of its swing. All 97 pass.

The changes keep what the kit does, its pitch and its safety case: the same alarm principle, station role, pump type, hose, nozzle, cart width and crew of two.

## Decision

*Table 1. Changes made.*

| # | Problem in the concept | Change made | Why this way |
| --- | --- | --- | --- |
| P1 | Cart frame drawn as a solid platform, with no stock size or joints | A welded ladder frame of 30 x 30 x 2 mm square tube: two side rails 1,000 mm, three cross members (the middle one in three pieces), two lines of bearers 260 mm apart under the pump and reel, all tops flush | One tube size, square cuts, every joint a fillet weld on a flat table; the bearers carry the pump stand, reel uprights and tray |
| P2 | Wheels drawn on the frame sides with no axle mounting | A 20 mm through axle in four 80 x 85 x 8 mm axle plates (one each side of each rail), with 22 mm spacers, the wheel hubs, collars and R-clips | The axle is clear of the tube walls by 4.5 mm; two plates per side carry the load in double shear; the wheels come off with an R-clip |
| P3 | Cart stood only on its wheels | Two 190 mm legs under the rail front ends with 40 mm rubber feet | The cart parks level and stays put; lifting the bar by 73 N takes the feet off the ground |
| P4 | Pull bar drawn floating in front of the frame | Two 30 mm tube arms, cut to sit flat on the rail tops with the toe against the front cross member, coped to a 33.7 mm cross bar 820 mm long at 800 mm height, with grips | A welded triangle at each foot; bar height suits two adults pulling side by side |
| P5 | Pump drawn sitting on the deck with no fixing | A 10 mm stand plate, 320 x 355 mm, welded on the rear cross member with two 8 mm gussets to the bearers; the pump flange bolts to its back face with four M12 bolts on a 150 mm square | Puts the shaft 440 mm up, so the lever swings clear of the wheels and frame (checked at both ends of the swing) |
| P6 | Pump handle too short for two people | A clamp-on lever extension: 585 mm of 33.7 mm tube to a 400 mm T-bar, grip 610 mm from the shaft | Two people face each other across the T-bar; the force per person is about 28 N |
| P7 | Hose reel drawn as a cylinder with no support | A bought steel drum on a 25 mm through spindle in two welded 50 x 8 mm uprights, with 12 mm spacers, a collar on the left and a swivel inlet on the right | Uses a stock reel drum; the swivel lets the hose pay out while the pump is connected |
| P8 | No connection from the pump to the reel | 1.2 m of 19 mm reinforced hose from the pump outlet over to the swivel, with two clips; the 4 bar relief valve on a tee at the pump outlet, discharge pointing down | The connection is checked clear of the relief valve, stand and reel; relief water goes to the ground, not at the crew |
| P9 | Station drawn as a two-post cantilever roof | Four posts of 60 x 60 x 3 mm tube, 600 mm into concrete collars 300 mm across, two roof beams, four purlins and a corrugated sheet falling 5° to the back | A cantilever on two posts needed a moment connection at the ground; four posts in collars resist the uplift of a 30 m/s gust with a factor of about 2 using only bolts and welds |
| P10 | Station alarm box, siren, solar panel and sign drawn touching the posts with no fixings | Box and siren bolted to the back left post with U-bolts and a bracket; panel on two rails screwed to the roof sheet; sign on two M8 bolts through the back right post | All fixings are bought hardware |
| P11 | Loose suction hose, strainer, nozzle and tap adaptor | A folded 1.5 mm galvanised tray, 400 x 370 x 80 mm, with drain holes, bolted to the bearers with four M8 bolts; the suction hose coils in it with the small parts inside the coil | Everything needed at the fire travels on the cart and drains after use |
| P12 | Heat alarm drawn as a box glued to the roof | A 140 x 50 x 3 mm aluminium plate screwed to the box base, hung under a roof pole by two UV-stable cable ties through slots; the board on standoffs; the thermistor bead below the box inside a printed guard | Bamboo poles cannot take screws reliably; ties fit any pole from about 50 to 100 mm. The bead in moving air below the box sees the heat first |

*Table 2. Knock-on changes.*

| Item | Change |
| --- | --- |
| Mass | Loaded cart 91.4 kg (est.); 89 N per person on a 10 % slope; R6 still met (CBK-CAL-001, sections C and D) |
| Cost | USD 1,355 for the block kit, USD 245 under the USD 1,600 value-engineering target (`budget_usd` unchanged) |
| Drawings | CBK-DWG-001 Rev P1 (general arrangement) and making sketches CBK-DWG-101 to 112 |
| Documents | CBK-CAL-001 v0.1 written on this design; CBK-PRC-001 and CBK-REQ-001 revised to v0.3 |

## Consequences

- `design_state: constructable` in `project.yaml`. The build plan CBK-BLD-001 shows every component and step in pictures generated from the model (`cad/src/build_plan_media.py`).
- The appearance model `cad/src/product_model.py` uses this design; photoreal renders are made on Amish's Mac.
- The pump's flange pattern, displacement and handle socket, and the reel drum's bore, are confirmed when parts are bought (CBK-DEC-001); the stand plate holes and lever hub follow the pump bought.

## Safety

> **Safety:** CampBreak includes a pressurised hand-pumped water line (relief valve at 4 bar, hose rated 10 bar) and a sealed lead-acid station battery. The kit is for small, early fires only; people leave first, and water is never used on burning oil or live wiring. Safety stops are listed in the build plan, section 6. It is an open engineering reference, not certified equipment.
