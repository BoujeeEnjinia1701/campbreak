---
doc_id: CBK-DDR-004
title: CampBreak delivery hose stowed full (R9)
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
  change: Amish's decision on register open decision 1 (portfolio decision 45) carried into the design
---

# 0004: Delivery hose stowed full (R9)

- **Date:** 2026-10-03
- **Status:** decided by Amish Chadha, 2026-10-03: "i approve all of the 47 recommendations provided by you. Execute them." For CampBreak this is portfolio decision 45, the recommendation on open decision 1 of CBK-DEC-001 v0.2, taken exactly as recommended: option (b).

## Context

After decision 1A (CBK-DDR-003) R9, water on target within 3 minutes for a shelter 100 m from the station, was 191 s at 100 m on paper: 11 s over. The recomputation in CBK-CAL-001 v0.2 counted for the first time the 26 s needed to fill the empty 30 m delivery hose and the 1.2 m connecting hose (8.85 L at 20.4 L/min) once pumping starts.

## Options considered

*Table 1. Options.*

| Option | What it means |
| --- | --- |
| (a) | Leave as is: R9 not met at 100 m by 11 s; the 70 m siting margin holds |
| (b) (chosen) | Stow the 30 m delivery hose full of water behind the shut nozzle: 177 s at 100 m, met with 3 s to spare; 8.9 kg more on the cart, about 101 N per person on a 10 % slope, just over the 100 N assumed sustainable; no new parts |
| (c) | Restate R9 to 3.25 min |

## Decision

Option (b). No part, geometry or price changes; the change is in how the cart is stowed:

*Table 2. Changes.*

| Item | Was | Now |
| --- | --- | --- |
| Delivery and connecting hoses | Run out, drained and wound back empty after priming | Filled by pumping until clear water runs, nozzle shut, wound back full, nozzle last (build plan step 12) |
| Drill card, weekly check | Prime check only | Prime check with the nozzle open; then refill the hose, shut the nozzle and wind it back full |
| Drill card, at the fire | Person 2 runs out the hose and aims | Person 2 runs out the full hose, aims and opens the nozzle |
| First checks (build plan section 5) | Pump stays primed; pull 100 m in 3 min | Pump and hose stay full for a week, no drip from the nozzle; pull force per person recorded against 100 N; drill pass at 100 m set to 3 min |
| Model, drawings | Unchanged geometry | Water in the full line counted in `docs/04-calcs/sizing.py` at the centre of the wound hose; GA CBK-DWG-001 and concept sheet CBK-DWG-010 at Rev P3 for the new figures |

## Consequences

*Table 3. Results (CBK-CAL-001 v0.3).*

| Item | Before | After |
| --- | --- | --- |
| R9 at 100 m | 191 s (3.2 min), not met, 11 s over | **177 s (2.95 min), met (est.) with 3 s to spare** |
| R9 at 70 m (siting margin) | 161 s (2.7 min) | 147 s (2.5 min) |
| Critical path at the fire | Drop, strokes and the 26 s fill (39 s) | The 25 s hose run-out by the second person |
| Cart mass | 94.6 kg | 103.4 kg (11.4 kg of water in all) |
| Pull on a 10 % slope | 92 N per person | 101 N per person, just over the 100 N assumed sustainable: **the TRL 4 pull test should confirm** |
| R6 | Met (est.) | Met (est.) on time (1.7 min) and width (850 mm); effort marginal |
| Front feet, parked / lift at the pull bar | 126 N / 73 N | 140 N / 82 N |
| Tipping sideways | 43° | 42° |
| Reel spindle | Not checked | 287 N on the 25 mm spindle, about 12 MPa (est.) |
| Cost | USD 1,374 | USD 1,374, unchanged (USD 226 under the USD 1,600 value-engineering target) |

- The 3 s margin at 100 m rests on estimates (30 s gather, 15 s pull-out, 25 s run-out, 1.0 m/s walk); the timed drill at TRL 4 decides R9.
- The shut nozzle must hold the hose full for a week, and the full hose must wind neatly onto the reel, which has only 8 % spare room; both are added to the items to confirm when parts are bought.
- The water in the hose is stale after a week; it is fire water only and is pumped through at the weekly check.

## Safety

> **Safety:** CampBreak includes a pressurised hand-pumped water line. The full delivery hose sits behind a shut nozzle; the 4 bar relief valve at the pump outlet, already fitted, lets the water expand as the hose warms in the sun, and the hose is rated 10 bar. The cart is now about 103 kg: two people always move it, a third holds back on slopes steeper than 10 %, nobody walks in front of it downhill, and nobody runs with it. The pull of about 101 N per person is an estimate just over what was assumed sustainable; the TRL 4 pull test confirms it before volunteers are asked to drill with the full cart. The kit is for small, early fires only; people leave first, and water is never used on burning oil or live wiring. It is an open engineering reference, not certified equipment.
