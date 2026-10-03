---
doc_id: CBK-CAL-001
title: CampBreak sizing calculations
project: CampBreak
doc_type: Calculation note
version: "0.1"
status: Draft
date: '2026-10-03'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-10-03'
  author: Amish Chadha
  change: First calculation note at TRL 3, on the constructable design (CBK-DDR-002)
---

# CampBreak sizing calculations

On paper the kit meets nine of its eleven requirements. The hand pump gives about 20.4 L/min with two people pumping at a sustainable 47 W each, the 6 mm jet reaches about 6.9 m, the alarms are loud enough and fast enough, and two people pull the loaded cart up a 10 % slope with about 89 N each. Two requirements are not shown: R2 (no false alarm while cooking) cannot be calculated and needs a cooking trial at TRL 4, and R9 (water on target within 3 min for a shelter 100 m away) is **not met on paper**, at 3.8 min. With the siting rule decided in CBK-DDR-001 (D9), a shelter at most 70 m from a station gets water in about 2.8 min. The kit costs about USD 1,355 against a value-engineering target of USD 1,600.

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
| Suction | 25 mm, 4 m, loss factor 5.0, lift 1.5 m | (est.) worst case from a low open container |
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
| Suction side | 17 kPa below atmosphere; 8.4 m of net positive suction head available |
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

Steel parts are weighed from the model volumes at 7,850 kg/m³; bought parts use catalogue estimates (pump 14 kg, wheels 5.5 kg each, reel drum 9 kg, wound hose 11.4 kg).

*Table 5. Cart mass and balance.*

| Quantity | Result |
| --- | --- |
| Loaded cart mass, dry | 91.4 kg (est.) |
| Centre of mass | On the centre line, 110 mm in front of the axle and 401 mm up |
| Load on the front feet when parked | 126 N |
| Lift at the pull bar to raise the feet | 73 N |
| Tipping sideways | at 42° |
| Overall size | 850 wide x 1,744 long x 1,067 tall |

## D. Pulling effort and speed (R6)

Rolling resistance 0.10 on unpaved ground (est.), slope 10 %, two people. Pull force is the weight times the sine of the slope plus rolling resistance times the cosine: 178 N in all, 89 N each, below a sustainable 100 N per person (est.). At 1.0 m/s, 100 m takes 1.7 min. The cart is 850 mm wide against a 900 mm limit. R6 is met (est.).

## E. Time to water on target (R9)

*Table 6. Time from alarm to water on target.*

| Stage | 100 m, standard | 70 m, sited (D9) |
| --- | --- | --- |
| Alarm to siren | 7 s | 7 s |
| Volunteers muster at the station | 60 s (est.) | 30 s (drilled) |
| Pull the cart out | 15 s | 15 s |
| Walk at 1.0 m/s | 100 s | 70 s |
| Set up suction and pay out hose | 30 s | 30 s |
| Prime the pump | 15 s | 15 s |
| **Total** | **227 s (3.8 min)** | **167 s (2.8 min)** |

R9 is **not met on paper** for a shelter 100 m away (3.8 min against 3 min). The decided mitigation (CBK-DDR-001, D9) keeps the target and sites stations so that no shelter is more than 70 m from one, with a drilled 30 s muster; on those terms the time is 2.8 min. A brisk 1.5 m/s with a 30 s muster would reach 100 m in 2.7 min, but that is not assumed.

## F. Station roof and posts

Wind 30 m/s (est., a strong monsoon gust), net uplift coefficient 1.2 on the 3.1 m² roof: about 1,990 N of uplift, 500 N per post. Each concrete collar (300 mm across, 600 mm deep) weighs about 975 N, so uplift is resisted with a factor of about 2. A horizontal load of 210 N gives a bending stress of about 10 MPa at the foot of each 60 x 60 x 3 mm post, far below the 235 MPa yield of S235. The four-post frame weighs about 86 kg of steel plus 14 kg of roof sheet.

## G. Hose reel capacity

30 m of hose with a 28 mm outside diameter needs 18.5 L of space; the drum (200 mm core, 440 mm wound diameter, 210 mm wide, packing 0.785) offers 19.9 L, a ratio of 1.08. The hose fits with little room to spare, so it must be wound neatly (build plan, step 10).

## H. Cost (R11)

*Table 7. Cost of one block kit, from bom/bom.csv.*

| Part of the kit | USD |
| --- | --- |
| 24 heat alarms | 420 |
| Station (alarm box, frame and roof, sign, drum) | 317 |
| Hose cart | 618 |
| **Total** | **1,355** |

Value-engineering target: USD 1,600. Estimated cost of the constructable design: USD 1,355 (USD 245 under the target).

## Results against every requirement

*Table 8. Results (from results.csv).*

| ID | Requirement | Target | Result | Status |
| --- | --- | --- | --- | --- |
| R1 | Rate-of-rise threshold | 8 °C/min | 8 °C/min over 60 s, plus 57 °C fixed | Met by design |
| R2 | No alarm in 1 h of cooking at 1 m | No alarm | Not calculable on paper | To show at TRL 4 |
| R3 | Sound at 3 m | At least 85 dB(A) | 85.5 dB(A) | Met (est.) |
| R4 | Relay to station and all alarms | 10 s or less | 7.2 s worst case | Met (est.) |
| R5 | Battery life | 12 months or more | Cell shelf life, about 5 years | Met (est.) |
| R6 | Cart on a 10 % slope, 100 m | 3 min or less, width 0.9 m or less | 1.7 min; 89 N per person; 850 mm wide | Met (est.) |
| R7 | Flow for 10 min | 20 L/min or more | 20.4 L/min; 47 W per person | Met (est.) |
| R8 | Jet reach | 6 m or more | 6.9 m | Met (est.) |
| R9 | Water on target 100 m away | 3 min or less | 3.8 min (2.8 min at 70 m with a 30 s muster) | **Not met on paper** |
| R10 | Repairable locally | Hand tools, market parts | Every wear part is a market item | Met by design |
| R11 | Cost | Value-engineering target USD 1,600 | USD 1,355 | USD 245 under the target |
