---
doc_id: CBK-REQ-001
title: CampBreak requirements
project: CampBreak
doc_type: Requirements
version: "0.5"
status: Draft
date: '2026-10-03'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-09-30'
  author: Amish Chadha
  change: Initial scaffold
- version: "0.2"
  date: '2026-10-03'
  author: Amish Chadha
  change: "Populated to TRL 2 with concept media, components and first-order numbers"
- version: "0.3"
  date: '2026-10-03'
  author: Amish Chadha
  change: "TRL 3 with the decisions of CBK-DDR-001 and CBK-DDR-002 applied and results from CBK-CAL-001"
- version: "0.4"
  date: '2026-10-03'
  author: Amish Chadha
  change: "R9 result after Amish's decision 1A (CBK-DDR-003): check foot valve, suction hose left coupled, go-when-two-arrive rule; delivery hose fill time added. R6 and R11 results updated. Requirement wording unchanged"
- version: "0.5"
  date: '2026-10-03'
  author: Amish Chadha
  change: "R9 and R6 results after Amish's decision 45 b (CBK-DDR-004): delivery hose stowed full; R9 met at 100 m (177 s); R6 pull effort 101 N per person. Requirement wording unchanged"
---

# CampBreak requirements

Measurable requirements for one block kit, with the TRL 3 result from the calculation note CBK-CAL-001. Ten are met on paper or by design and R2 can only be shown in a cooking trial at TRL 4. R9 is now met on paper for a shelter 100 m from the station, with 3 s to spare, since Amish's decision 45 b to stow the delivery hose full (CBK-DDR-004); the full hose makes R6's pull effort marginal (101 N per person against 100 N assumed sustainable), for the TRL 4 pull test to confirm.

*Table 1. Requirements and TRL 3 status.*

| ID | Requirement | Target | Verification (TRL 4 or later) | TRL 3 result | Status |
| --- | --- | --- | --- | --- | --- |
| R1 | Alarm detects a fast temperature rise | Alarms at a rise of 8 °C (14 °F) per minute or faster, plus a 57 °C fixed threshold | Heat chamber test with logged temperature ramp | Threshold set in firmware, averaged over 60 s | Met by design |
| R2 | Alarm ignores normal cooking | No alarm during 1 hour of stove cooking at 1 m distance | Cooking trial in a mock shelter | Not calculable on paper | To show at TRL 4 |
| R3 | Alarm is loud enough to wake the block | At least 85 dB(A) at 3 m | Sound level meter test | 85.5 dB(A) | Met (est.) |
| R4 | Alarm reaches neighbours and the block station | Every alarm in the block and the station within 10 s | Field test across a mock block layout | 7.2 s worst case | Met (est.) |
| R5 | Alarm runs without mains power | At least 12 months on batteries | Current draw measurement | Limited by cell shelf life, about 5 years | Met (est.) |
| R6 | Cart can be moved on camp paths | Two adults move the loaded cart 100 m on an unpaved 10 % slope in 3 minutes or less; cart width 0.9 m or less | Timed trial on a test track | 1.7 min; 101 N per person; 850 mm wide | Met (est.); 101 N per person is just over the 100 N assumed sustainable, so the TRL 4 pull test should confirm |
| R7 | Hand pump delivers useful flow | At least 20 L/min (5.3 US gal/min) at the nozzle, pumped by two people for 10 minutes | Bench flow test with timed volume | 20.4 L/min at 47 W per person | Met (est.) |
| R8 | Jet reaches a burning shelter from a safe distance | Jet reach of 6 m (20 ft) or more | Measured throw test | 6.9 m | Met (est.) |
| R9 | Fast deployment | Water on target within 3 minutes of alarm for a shelter 100 m from the station | Timed drill with volunteers, from the siren, using the go-when-two-arrive rule | 2.95 min (177 s) at 100 m; 2.5 min at 70 m | Met (est.) at 100 m, 3 s to spare; met at 70 m |
| R10 | Repairable locally | All wear parts replaceable with hand tools and parts sold in local markets | Maintenance walkthrough with a camp workshop | Every wear part is a market item | Met by design |
| R11 | Cost against the value-engineering target | Value-engineering target: USD 1,600 for one block kit | Costed bill of materials | USD 1,374, USD 226 under the target | Met |

R9 stays at 3 minutes and 100 m. On 2026-10-03 Amish chose option A on R9 ("1A 2A 3A 4A 5A 6A 7A 8A 9A 10A 11A"; CBK-DDR-003): a check foot valve so the pump stays primed, the suction hose left coupled to the pump with a cam-lever coupling, and the drilled rule "go when two arrive" with a 30 s gather. That brought the 100 m time from 3.8 min to 3.2 min. The rest of the gap was the 26 s needed to fill the empty 30 m delivery hose. On the same day Amish approved stowing that hose full of water behind the shut nozzle (decision 45 b, CBK-DDR-004), which brings the 100 m time to 177 s (2.95 min), met with 3 s to spare, for 8.9 kg more on the cart. The siting rule of CBK-DDR-001 (D9), no shelter more than 70 m along the path from a station, is kept as the siting margin; there the time is 2.5 min.

## Assumptions

- A block has a drum or tap within reach of most shelters, or drums are placed at stations.
- Camp management allows alarms in shelters and a station in each block.
- Volunteers are trained and drill regularly, so the first two reach the station within 30 s of the siren.
- The foot valve's check holds the pump and suction hose full between uses; the weekly prime check on the drill card confirms it.
- The estimates marked (est.) in CBK-CAL-001 hold within the margins shown; the pump displacement is the most important one.

## Safety

> **Safety:** These requirements describe a pressurised hand-pumped water system and battery-powered alarms. The kit is for small, early fires only, people leave first, and water is never used on burning oil or live wiring. It is an open engineering reference, not certified equipment.
