---
doc_id: CBK-DEC-001
title: CampBreak design decisions register
project: CampBreak
doc_type: Design decisions register
version: "0.2"
status: Draft
date: '2026-10-03'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-10-03'
  author: Amish Chadha
  change: Register opened at TRL 3; all decisions made under Amish's 2026-10-03 pre-approval
- version: "0.2"
  date: '2026-10-03'
  author: Amish Chadha
  change: "Amish's R9 decision 1A recorded (CBK-DDR-003); one new open decision: stow the delivery hose full"
---

# CampBreak design decisions register

Every design decision still to be made, and every decision made, in one place. Each decision is argued in full in its decision record under `docs/decisions/`; this register is the index Amish works from. The build plan (`docs/05-build-plan.md`) describes the design as it stands and does not list decisions.

## Open decisions

| # | Decision | State | Options | Recommendation |
| --- | --- | --- | --- | --- |
| 1 | Stow the 30 m delivery hose full of water (R9) | Proposed, awaiting Amish. After decision 1A (CBK-DDR-003) R9 is 191 s at 100 m, 11 s over the 180 s target. The rest of the gap is the 26 s needed to fill the empty delivery hose at the fire (CBK-CAL-001, section E) | (a) Leave as is: R9 not met on paper at 100 m by 11 s; the 70 m siting margin holds (161 s). (b) Stow the delivery hose full behind the shut nozzle, refilled at the weekly check: 177 s at 100 m (met, 3 s margin), 8.9 kg more on the cart (about 101 N per person on a 10 % slope, just over the 100 N assumed sustainable; the R6 time is still met), no new parts; the 4 bar relief valve already protects the full hose from heating in the sun. (c) Restate R9 to 3.25 min at 100 m | (b): the only option that meets R9 on paper at 100 m without new parts; check at TRL 4 that the nozzle shut-off and the pump hold the hose full for a week |

## To confirm when parts are bought

| # | What to confirm | Why it matters | Source |
| --- | --- | --- | --- |
| 1 | The hand pump displaces at least 0.40 L per double stroke | R7 is met with only 2 % margin on flow; a smaller pump misses it | CBK-CAL-001, section A |
| 2 | The pump's flange hole pattern (150 mm square assumed), shaft height and handle socket | They set the stand plate holes and the lever hub bore | CBK-DDR-002, P5 and P6 |
| 3 | The reel drum's bore suits a 25 mm spindle, and the swivel inlet's thread suits the 19 mm hose tail | Sets the spindle size or a sleeve | CBK-DDR-002, P7 |
| 4 | The delivery hose's outside diameter is 28 mm or less | The 30 m hose fills the drum with only 8 % spare room | CBK-CAL-001, section G |
| 5 | The nozzle's jet orifice is 6 mm | Sets the flow, pressure and reach together | CBK-CAL-001, section A |
| 6 | The piezo sounder gives at least 95 dB(A) at 1 m | R3 is met with 0.5 dB margin | CBK-CAL-001, section B |
| 7 | The wheels have 20 mm bores and 75 mm hubs | Sets the axle, spacer and collar lengths | CBK-DDR-002, P2 |
| 8 | The relief valve opens at 4 bar ± 0.5 bar | Pressure limit for the hose and fittings | CBK-DDR-001, D7 |
| 9 | The foot valve's check holds the suction hose and pump full for a week, and the suction hose bends to 60 mm radius or less | The pump stays primed (R9); the stowed hose path has a 63 mm bend | CBK-DDR-003 |

## Value engineering

Value-engineering target: USD 1,600 (a hypothetical control target, not a limit). Estimated cost of the constructable design: USD 1,374 (USD 226 under the target). Main cost drivers and savings worth trying:

- The 24 heat alarms are the largest share (USD 420, USD 17.50 each). The board price is a prototype module estimate; a single board with the radio, controller and sounder driver, made in a batch, should fall to about USD 10 to 12 each at TRL 4.
- The station costs USD 317: steel frame and roof USD 157, alarm box with battery, siren and panel USD 105. Where a block already has a shaded structure, the station can be built against it and the frame dropped.
- The cart costs USD 637: pump USD 120, reel drum USD 95, hoses USD 83, wheels USD 69, frame USD 59, suction hose with the brass check foot valve USD 40. A reel welded from tube and sheet in the camp workshop could save about USD 50; a second-hand pump is worth trying if its displacement is checked.

## Decisions made

| Date | Decision | Decided by | Record |
| --- | --- | --- | --- |
| 2026-10-03 | Alarm relay: published star scheme on a sub-GHz band (alarm to station, one station broadcast to all alarms); no mesh; checked against Lumkani's patents before release | Amish, pre-approval: "I pre-approve the batch runs along with any recommendations you come up with." | CBK-DDR-001, D1 |
| 2026-10-03 | Detection: rate of rise of 8 °C per minute over 60 s plus a 57 °C fixed back-up, thermistor below the box | Amish, same pre-approval | CBK-DDR-001, D2 |
| 2026-10-03 | Alarm board specified by function and priced as a module; board design and firmware left to TRL 4 | Amish, same pre-approval | CBK-DDR-001, D3 |
| 2026-10-03 | Block kit of 24 alarms, one station and one cart | Amish, same pre-approval | CBK-DDR-001, D4 |
| 2026-10-03 | Bought cast-iron semi-rotary pump, 25 mm ports, at least 0.40 L per double stroke | Amish, same pre-approval | CBK-DDR-001, D5 |
| 2026-10-03 | No lithium cells: sealed lead-acid at the station, alkaline AA cells in the alarms (conservative; lithium iron phosphate only with evidence of safe charging at 45 °C and a recycling route) | Amish, same pre-approval | CBK-DDR-001, D6 |
| 2026-10-03 | 4 bar relief valve at the pump outlet, discharge down, hose rated 10 bar (conservative; raised only after a burst test of the bought hose and fittings) | Amish, same pre-approval | CBK-DDR-001, D7 |
| 2026-10-03 | 19 mm semi-rigid hose, 30 m on a reel, with a 6 mm jet and spray nozzle | Amish, same pre-approval | CBK-DDR-001, D8 |
| 2026-10-03 | R9 kept at 3 min; stations sited within 70 m of every shelter with a drilled 30 s muster; R9 reported as not met on paper at 100 m | Amish, same pre-approval | CBK-DDR-001, D9 |
| 2026-10-03 | First partner to approach: a camp management agency in the Cox's Bazar camps, Bangladesh, with the Bangladesh Fire Service and Civil Defence (first candidate, not agreed) | Amish, same pre-approval | CBK-DDR-001, D10 |
| 2026-10-03 | Design for construction: welded tube frame, through axle in axle plates, legs and feet, handle, pump stand, lever extension, reel on uprights, connecting hose and relief tee, four-post station, fixings for the station fittings, hose tray and the alarm's plate and ties (P1 to P12) | Amish, same pre-approval | CBK-DDR-002 |
| 2026-10-03 | `budget_usd` left at USD 1,600 as the value-engineering target; cost variations accepted | Amish: "I also accept any cost overruns or variations from the assumed scope cost." | CBK-DDR-001 |
| 2026-10-03 | R9 (decision 1A): brass check foot valve so the pump stays primed; suction hose left coupled to the pump inlet with a cam-lever coupling and strapped along the left rail; drilled rule "go when two arrive" with a 30 s gather on the drill card, the station sign and in the build plan; 3 min target and "stations within 70 m of every shelter" kept as the siting margin. Result: 3.2 min at 100 m (not met, 11 s over), 2.7 min at 70 m | Amish: "1A 2A 3A 4A 5A 6A 7A 8A 9A 10A 11A" | CBK-DDR-003 |

## Safety

> **Safety:** CampBreak includes a pressurised hand-pumped water line (relief valve at 4 bar, hose rated 10 bar) and a sealed lead-acid station battery. The kit is for small, early fires only; people leave first, and water is never used on burning oil or live wiring. Safety stops are listed in the build plan, section 6. It is an open engineering reference, not certified equipment.
