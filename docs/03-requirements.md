---
doc_id: CBK-REQ-001
title: CampBreak requirements
project: CampBreak
doc_type: Requirements
version: "0.3"
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
---

# CampBreak requirements

Measurable requirements for one block kit, with the TRL 3 result from the calculation note CBK-CAL-001. Nine are met on paper or by design, R2 can only be shown in a cooking trial at TRL 4, and **R9 is not met on paper** for a shelter 100 m from the station.

*Table 1. Requirements and TRL 3 status.*

| ID | Requirement | Target | Verification (TRL 4 or later) | TRL 3 result | Status |
| --- | --- | --- | --- | --- | --- |
| R1 | Alarm detects a fast temperature rise | Alarms at a rise of 8 °C (14 °F) per minute or faster, plus a 57 °C fixed threshold | Heat chamber test with logged temperature ramp | Threshold set in firmware, averaged over 60 s | Met by design |
| R2 | Alarm ignores normal cooking | No alarm during 1 hour of stove cooking at 1 m distance | Cooking trial in a mock shelter | Not calculable on paper | To show at TRL 4 |
| R3 | Alarm is loud enough to wake the block | At least 85 dB(A) at 3 m | Sound level meter test | 85.5 dB(A) | Met (est.) |
| R4 | Alarm reaches neighbours and the block station | Every alarm in the block and the station within 10 s | Field test across a mock block layout | 7.2 s worst case | Met (est.) |
| R5 | Alarm runs without mains power | At least 12 months on batteries | Current draw measurement | Limited by cell shelf life, about 5 years | Met (est.) |
| R6 | Cart can be moved on camp paths | Two adults move the loaded cart 100 m on an unpaved 10 % slope in 3 minutes or less; cart width 0.9 m or less | Timed trial on a test track | 1.7 min; 89 N per person; 850 mm wide | Met (est.) |
| R7 | Hand pump delivers useful flow | At least 20 L/min (5.3 US gal/min) at the nozzle, pumped by two people for 10 minutes | Bench flow test with timed volume | 20.4 L/min at 47 W per person | Met (est.) |
| R8 | Jet reaches a burning shelter from a safe distance | Jet reach of 6 m (20 ft) or more | Measured throw test | 6.9 m | Met (est.) |
| R9 | Fast deployment | Water on target within 3 minutes of alarm for a shelter 100 m from the station | Timed drill with volunteers | 3.8 min at 100 m; 2.8 min at 70 m with a 30 s muster | **Not met on paper** |
| R10 | Repairable locally | All wear parts replaceable with hand tools and parts sold in local markets | Maintenance walkthrough with a camp workshop | Every wear part is a market item | Met by design |
| R11 | Cost against the value-engineering target | Value-engineering target: USD 1,600 for one block kit | Costed bill of materials | USD 1,355, USD 245 under the target | Met |

R9 stays at 100 m. The decided mitigation (CBK-DDR-001, D9) is a siting rule: no shelter more than 70 m along the path from a station, with a drilled 30 s muster.

## Assumptions

- A block has a drum or tap within reach of most shelters, or drums are placed at stations.
- Camp management allows alarms in shelters and a station in each block.
- Volunteers are trained and drill regularly, so a 30 s muster is realistic.
- The estimates marked (est.) in CBK-CAL-001 hold within the margins shown; the pump displacement is the most important one.

## Safety

> **Safety:** These requirements describe a pressurised hand-pumped water system and battery-powered alarms. The kit is for small, early fires only, people leave first, and water is never used on burning oil or live wiring. It is an open engineering reference, not certified equipment.
