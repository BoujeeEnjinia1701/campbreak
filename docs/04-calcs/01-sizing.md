---
doc_id: CBK-CAL-001
title: CampBreak sizing calculations
project: CampBreak
doc_type: Calculation note
version: "0.3"
status: Draft
date: '2026-10-03'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-10-03'
  author: Amish Chadha
  change: First calculation note at TRL 3, on the constructable design (CBK-DDR-002)
- version: "0.2"
  date: '2026-10-03'
  author: Amish Chadha
  change: "Amish's R9 decision (CBK-DDR-003): check foot valve, suction hose left coupled, go-when-two-arrive rule; R9 timeline recomputed with the delivery hose fill time added; cart mass and cost updated"
- version: "0.3"
  date: '2026-10-03'
  author: Amish Chadha
  change: "Amish's decision 45 b (CBK-DDR-004): delivery hose stowed full of water behind the shut nozzle; R9 met at 100 m (177 s); cart mass, balance and pull force updated"
---

# CampBreak sizing calculations

On paper the kit meets ten of its eleven requirements. The hand pump gives about 20.4 L/min with two people pumping at a sustainable 47 W each, the 6 mm jet reaches about 6.9 m, the alarms are loud enough and fast enough, and R9 (water on target within 3 min for a shelter 100 m away) is now **met on paper**, at 177 s (2.95 min), with 3 s to spare. Amish's decisions of 2026-10-03 got it there: CBK-DDR-003 (check foot valve, suction hose left coupled to the pump, "go when two arrive" with a 30 s gather) and CBK-DDR-004 (decision 45 b: the 30 m delivery hose stowed full of water behind the shut nozzle, so the 26 s fill at the fire is gone). The full hose adds 8.9 kg: two people now pull the loaded cart up a 10 % slope with about 101 N each, just over the 100 N assumed sustainable, so R6 is met on time and width but the TRL 4 pull test should confirm the effort. R2 (no false alarm while cooking) cannot be calculated and needs a cooking trial at TRL 4. A shelter at most 70 m from a station, the siting margin kept from CBK-DDR-001 (D9), gets water in 2.5 min. The kit costs about USD 1,374 against a value-engineering target of USD 1,600.

Every figure comes from `docs/04-calcs/sizing.py`, which reads its geometry from `cad/src/model.py` and its prices from `bom/bom.csv`, and writes `docs/04-calcs/results.csv`. Inputs marked (est.) are estimates to be confirmed by measurement at TRL 4.

> **Safety:** The pump and hose are a pressurised water system. A shut nozzle with two people pumping could reach several bar; the 4 bar relief valve (CBK-DDR-001, D7) caps it, and the hose is rated at 10 bar. The station battery is sealed lead-acid: it can deliver high short-circuit current and vents hydrogen if overcharged. The kit is for small, early fires only; people leave first, and water is never used on burning oil or live wiring.

## A. Pump, hose and nozzle (R7, R8)

### Assumptions

*Table 1. Inputs for the water line.*

| Input | Value | Note |
| --- | --- | --- |
| Pump displacement | 0.40 L per double stroke | (est.) to confirm on the pump bought |
| Pumping rate | 60 double strokes per minute | (est.) steady pace for two people |
| Volumetric efficiency | 0.85 | (est.) cast semi-rotary pump |
| Mechanical efficiency | 0.50 | (est.) lever, vanes and seals |
| Jet | 6 mm, discharge coefficient 0.96 | Nozzle orifice to confirm when bought |
| Delivery hose | 19 mm bore, 30 m, roughness 0.01 mm | Plus 1.2 m of 19 mm connecting hose |
| Delivery fittings | Loss factor 4.0 | (est.) swivel, tee and couplings |
| Suction | 25 mm, 4 m, loss factor 7.0, lift 1.5 m | (est.) spring check foot valve, strainer, elbow and coupling (CBK-DDR-003); worst case from a low open container |
| Nozzle height | 1 m above the pump | Slope or raised arm |
| Reach factor | 0.50 of the drag-free range at 30° | (est.) to measure |
| Sustained effort | 75 W per person for 10 min | (est.) |

### Method

Flow is displacement x rate x volumetric efficiency. Jet speed comes from the flow and the orifice; nozzle pressure is half the density times the jet speed squared. Hose friction uses the Darcy factor from the Swamee-Jain equation. The pump head is the sum of nozzle pressure, friction, fittings, lift to the nozzle and suction losses. Shaft power is hydraulic power over mechanical efficiency; the lever force follows from the work per double stroke over four 40° swings at a 610 mm grip radius.

### Results

*Table 2. Water line at two people pumping.*

| Quantity | Result |
| --- | --- |
| Flow at the nozzle | 20.4 L/min (R7 target 20) |
| Jet speed | 12.5 m/s |
| Pressure at the nozzle | 78 kPa |
| Hose friction, 30 m | 29.9 kPa at 1.2 m/s, Reynolds number about 22,800 |
| Pump outlet pressure | 122 kPa (1.2 bar), well under the 4 bar relief setting |
| Suction side | 17 kPa below atmosphere; 8.3 m of net positive suction head available |
| Hydraulic power | 47 W; shaft power 95 W, or 47 W per person |
| Force at the grip | 56 N in total, about 28 N per person |
| Force to reach the relief setting against a shut nozzle | 94 N in total, so two people can reach it |
| Jet reach | 6.9 m (13.9 m drag-free); R8 target 6 m |
| One 200 L drum | about 9.8 min of pumping |

Effort is well within the 75 W per person that can be kept up for 10 minutes, so R7 is met with margin on effort, though only with 2 % margin on flow. The flow depends directly on the pump's displacement, which must be confirmed on the pump bought (CBK-DEC-001, to confirm).

Figure 1 (`media/flow.png`) shows the pressure falling from the pump to the nozzle; all values are estimates.

## B. Heat alarm (R1 to R5)

*Table 3. Alarm inputs (est. unless stated).*

| Input | Value |
| --- | --- |
| Threshold | 8 °C per minute over 60 s, plus 57 °C fixed (decided, CBK-DDR-001 D2) |
| Sample interval | 10 s; 1 mA for 1 ms per sample |
| Sleep current | 3 µA |
| Radio listen for station broadcast | every 4 s, 10 mA for 1.5 ms |
| Daily check-in | one 60 ms transmission at 40 mA |
| Cells | 3 x AA alkaline, 2.4 Ah derated to 70 %, with a 30 min sounding reserve |
| Sounder | 95 dB(A) at 1 m |
| Alert | 100 ms transmission with three retries 1 s apart |

*Table 4. Alarm results.*

| Requirement | Result | Status |
| --- | --- | --- |
| R1 rate of rise | 8 °C per minute set in firmware; worst-case extra delay one 10 s sample | Met by design |
| R2 cooking | Not calculable on paper | To show at TRL 4 |
| R3 sound at 3 m | 95 - 20 log10(3) = 85.5 dB(A) | Met (est.), 0.5 dB margin |
| R4 relay time | 3.1 s alarm to station (with retries) plus 4.1 s for the station broadcast to reach every alarm: 7.2 s worst case | Met (est.) |
| R5 battery life | Average 6.9 µA; 331 months on paper, so cell shelf life (about 5 years) is the limit | Met (est.) |

R3 has little margin: a sounder of at least 95 dB(A) at 1 m is specified in the BOM, and a louder one is the first fix if the TRL 4 measurement falls short.

## C. Cart mass and balance (R6)

Steel parts are weighed from the model volumes at 7,850 kg/m³; bought parts use catalogue estimates (pump 14 kg, wheels 5.5 kg each, reel drum 9 kg, wound hose 11.4 kg, brass check foot valve 1.0 kg). Since CBK-DDR-003 the cart is stowed primed: the pump body (about 0.6 L, est.) and the 4 m suction hose (2.0 L) hold 2.6 kg of water, counted at the middle of the suction hose run. Since CBK-DDR-004 the 30 m delivery hose and the 1.2 m connecting hose are also stowed full behind the shut nozzle: 8.85 L, 8.9 kg of water, counted at the centre of the wound hose on the reel.

*Table 5. Cart mass and balance.*

| Quantity | Result |
| --- | --- |
| Loaded cart mass, stowed primed and with the delivery hose full | 103.4 kg (est.), of which 11.4 kg is water: 2.6 kg in the pump and suction hose, 8.9 kg in the delivery and connecting hoses (94.6 kg before CBK-DDR-004) |
| Centre of mass | 5 mm left of the centre line, 109 mm in front of the axle and 409 mm up (was 6, 107 and 397 mm) |
| Load on the front feet when parked | 140 N (was 126 N) |
| Lift at the pull bar to raise the feet | 82 N (was 73 N) |
| Tipping sideways | at 42° (was 43°) |
| Overall size | 850 wide x 1,744 long x 1,067 tall |

## D. Pulling effort and speed (R6)

Rolling resistance 0.10 on unpaved ground (est.), slope 10 %, two people. Pull force is the weight times the sine of the slope plus rolling resistance times the cosine: 202 N in all, 101 N each (185 N and 92 N before the delivery hose was stowed full). That is just over the 100 N per person assumed sustainable (est.), by about 1 %, which is well inside the uncertainty of the rolling resistance and of the 100 N figure itself. At 1.0 m/s, 100 m takes 1.7 min. The cart is 850 mm wide against a 900 mm limit. R6 is met (est.) on time and width; the effort is marginal and the TRL 4 pull test on a 10 % slope should confirm it (build plan, section 5).

## E. Time to water on target (R9)

Amish decided on 2026-10-03 (CBK-DDR-003, decision 1A): "1A 2A 3A 4A 5A 6A 7A 8A 9A 10A 11A". For CampBreak, 1A means three changes, with the 3 min target and the 70 m siting margin kept. On the same day he approved the round 2 recommendation (CBK-DDR-004, decision 45 b), a fourth change:

1. A brass spring-loaded foot valve with a positive-seal check holds the 4 m suction hose and the pump full of water between uses, so the pump does not need priming.
2. The suction hose stays coupled to the pump inlet by its cam-lever coupling and lies along the left rail, so nothing has to be coupled at the fire.
3. The drilled rule "go when two arrive": the first two volunteers at the station take the cart at once, at most 30 s after the siren. Others follow to the fire.
4. The delivery line (30 m of 19 mm hose and 1.2 m of connecting hose, 8.85 L) is stowed full of water behind the shut nozzle and topped up at the weekly check, so it no longer has to fill at the fire (26 s at 20.4 L/min with it empty).

On arrival the two split the work. One lifts the suction hose off the cart, drops the foot valve in the water and starts pumping. The other runs out the full hose from the reel and aims; water leaves the nozzle as soon as it is opened and the pump is stroked.

*Table 6. Time from alarm to water on target.*

| Stage | 100 m (R9) | 70 m (siting margin) | Note |
| --- | --- | --- | --- |
| Alarm to siren | 7 s | 7 s | Section B |
| Gather: go when two arrive | 30 s | 30 s | Drilled; at most 30 s |
| Pull the cart out | 15 s | 15 s | (est.) |
| Walk at 1.0 m/s | 100 s | 70 s | Section D |
| Drop the coupled suction hose in the water | 10 s | 10 s | (est.) no coupling, no priming |
| First strokes to lift water | 3 s | 3 s | (est.) pump and suction already full; at the same time as the run-out |
| Fill the delivery line | 0 s | 0 s | Stowed full (CBK-DDR-004); 26 s if it were empty |
| Run out the hose and aim | 25 s | 25 s | (est.) second person; now the critical path |
| **Total** | **177 s (2.95 min)** | **147 s (2.5 min)** | |

R9 is **met on paper** at 100 m: 177 s against 180 s, 3 s to spare. The margin is small and rests on estimates (the 30 s gather, the 15 s pull-out, the 25 s run-out and a 1.0 m/s walk), so the timed drill at TRL 4 decides it. At 70 m, the siting margin kept from CBK-DDR-001 (D9), it is met with 33 s to spare.

*Table 7. What the decision changed, at 100 m.*

| Case | Time |
| --- | --- |
| Version 0.1 timeline (60 s muster, 30 s set-up, 15 s priming), as published | 227 s (3.8 min) |
| Version 0.1 timeline with the delivery line fill added | 253 s (4.2 min) |
| Decision 1A (CBK-DDR-003), delivery hose empty | 191 s (3.2 min) |
| Decisions 1A and 45 b (CBK-DDR-004), delivery hose stowed full | 177 s (2.95 min) |

On a like-for-like basis decision 1A saves 62 s and decision 45 b a further 14 s: the 26 s fill is gone, but the 25 s run-out by the second person becomes the critical path in its place, so the gain is the 14 s by which the fill outlasted the run-out. The cost is 8.9 kg more on the cart (section D). No new parts are needed: the shut nozzle holds the water in, and the 4 bar relief valve already protects the full hose from pressure as it warms in the sun.

Until the next volunteers arrive, one person pumps alone. Holding 60 double strokes a minute needs about 95 W at the shaft and 56 N at the grip from that person, more than the 75 W assumed sustainable for 10 minutes (est.), but for the minute or two until the others arrive it is a reasonable effort. The drill (build plan, section 5) checks it.

## F. Station roof and posts

Wind 30 m/s (est., a strong monsoon gust), net uplift coefficient 1.2 on the 3.1 m² roof: about 1,990 N of uplift, 500 N per post. Each concrete collar (300 mm across, 600 mm deep) weighs about 975 N, so uplift is resisted with a factor of about 2. A horizontal load of 210 N gives a bending stress of about 10 MPa at the foot of each 60 x 60 x 3 mm post, far below the 235 MPa yield of S235. The four-post frame weighs about 86 kg of steel plus 14 kg of roof sheet.

## G. Hose reel capacity

30 m of hose with a 28 mm outside diameter needs 18.5 L of space; the drum (200 mm core, 440 mm wound diameter, 210 mm wide, packing 0.785) offers 19.9 L, a ratio of 1.08. The hose fits with little room to spare, so it must be wound neatly (build plan, step 10). A full hose is slightly rounder and stiffer than an empty one, so the ratio is a little tighter in practice; winding it full is part of the TRL 4 checks.

With the hose stowed full (CBK-DDR-004) the reel carries the drum (9 kg), the hose (11.4 kg) and 8.9 kg of water: 287 N on the 25 mm spindle. Taken as a simple beam loaded at mid-span over 250 mm (est.), the spindle sees about 12 MPa, far below the 235 MPa yield of S235.

## H. Cost (R11)

*Table 8. Cost of one block kit, from bom/bom.csv.*

| Part of the kit | USD |
| --- | --- |
| 24 heat alarms | 420 |
| Station (alarm box, frame and roof, sign, drum) | 317 |
| Hose cart | 637 |
| **Total** | **1,374** |

Value-engineering target: USD 1,600. Estimated cost of the constructable design: USD 1,374 (USD 226 under the target). CBK-DDR-003 added USD 19: the brass check foot valve (USD 12 more than the plain foot valve), two rubber hose straps (USD 5) and the laminated drill card (USD 2).

## Results against every requirement

*Table 9. Results (from results.csv).*

| ID | Requirement | Target | Result | Status |
| --- | --- | --- | --- | --- |
| R1 | Rate-of-rise threshold | 8 °C/min | 8 °C/min over 60 s, plus 57 °C fixed | Met by design |
| R2 | No alarm in 1 h of cooking at 1 m | No alarm | Not calculable on paper | To show at TRL 4 |
| R3 | Sound at 3 m | At least 85 dB(A) | 85.5 dB(A) | Met (est.) |
| R4 | Relay to station and all alarms | 10 s or less | 7.2 s worst case | Met (est.) |
| R5 | Battery life | 12 months or more | Cell shelf life, about 5 years | Met (est.) |
| R6 | Cart on a 10 % slope, 100 m | 3 min or less, width 0.9 m or less | 1.7 min; 101 N per person; 850 mm wide | Met (est.); 101 N per person is just over the 100 N assumed sustainable: the TRL 4 pull test should confirm |
| R7 | Flow for 10 min | 20 L/min or more | 20.4 L/min; 47 W per person | Met (est.) |
| R8 | Jet reach | 6 m or more | 6.9 m | Met (est.) |
| R9 | Water on target 100 m away | 3 min or less | 2.95 min (177 s) at 100 m; 2.5 min at 70 m (siting margin) | Met (est.) at 100 m with 3 s to spare; delivery hose stowed full |
| R10 | Repairable locally | Hand tools, market parts | Every wear part is a market item | Met by design |
| R11 | Cost | Value-engineering target USD 1,600 | USD 1,374 | USD 226 under the target |
