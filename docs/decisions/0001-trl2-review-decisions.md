---
doc_id: CBK-DDR-001
title: CampBreak TRL 2 review decisions
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
  change: TRL 2 review items decided under Amish's 2026-10-03 pre-approval
---

# 0001: TRL 2 review decisions

- **Date:** 2026-10-03
- **Status:** decided. Amish, 2026-10-03: "start with the first 14 repos from the list of 29 projects. I pre-approve the batch runs along with any recommendations you come up with. I also accept any cost overruns or variations from the assumed scope cost." Every item below is the recommendation made in the TRL 2 review and is therefore decided as recommended.

## Context

The scaffold (CBK-PRB-001 and CBK-PRC-001 v0.1) left five open questions: the alarm relay scheme, the size of a block kit, the flow and pressure needed, theft and misuse, and the first drill partner. Populating the repo to TRL 2 raised further choices: the pump type, the station power source, pressure protection, the hose and the response-time target. Amish pre-approved every recommendation for this batch on 2026-10-03, so each is recorded here as decided. Choices that touch safety take the conservative option, and the evidence that would relax them is stated.

## Options considered

*Table 1. Options for each item.*

| # | Item | Options |
| --- | --- | --- |
| D1 | Alarm relay scheme | (a) mesh in which every alarm repeats every other; (b) star: each alarm reports to the block station, which sounds the siren and sends one broadcast that every alarm repeats with its sounder; (c) wired loop |
| D2 | Detection rule | (a) smoke; (b) fixed temperature only; (c) rate of rise with a fixed-temperature back-up |
| D3 | Alarm electronics at TRL 3 | (a) design the board now; (b) specify the board by function and price it as a module assembly, leaving the board design and firmware to TRL 4 |
| D4 | Block kit size | (a) 12 shelters; (b) 24 shelters; (c) 48 shelters |
| D5 | Pump | (a) self-built piston pump; (b) bought double-acting semi-rotary (wing) pump; (c) stirrup pump |
| D6 | Station and alarm power | (a) lithium cells with solar charging; (b) 12 V sealed lead-acid battery with a 10 W panel at the station, alkaline AA cells in the alarms |
| D7 | Pressure protection | (a) none, the operators stop pumping; (b) a 4 bar spring relief valve on the pump outlet, hose rated 10 bar |
| D8 | Hose and nozzle | (a) 25 mm layflat; (b) 19 mm semi-rigid hose, 30 m, on a reel, with a 6 mm jet and spray nozzle |
| D9 | Response-time shortfall (R9) | (a) lower the target; (b) keep the 3 min target and add a siting rule: no shelter more than 70 m along the path from a station, with a 30 s muster drilled by volunteers |
| D10 | First partner and region | (a) Cox's Bazar camps, Bangladesh; (b) Northwest Syria; (c) informal settlements in South Africa |

## Decision

*Table 2. Items decided, 2026-10-03.*

| # | Item | Decision | Status |
| --- | --- | --- | --- |
| D1 | Alarm relay scheme | (b) star scheme on a sub-GHz licence-free radio band: the alarm sends its alert with three retries, the station sounds the 110 dB(A) siren and broadcasts once, and every alarm in range sounds. The scheme is published in full. It is not a mesh, and it will be checked against Lumkani's patents before release. | Decided by Amish, 2026-10-03 (pre-approval) |
| D2 | Detection rule | (c) rate of rise of 8 °C per minute averaged over 60 s, plus a 57 °C fixed back-up, from an NTC thermistor below the box | Decided by Amish, 2026-10-03 (pre-approval) |
| D3 | Alarm electronics | (b) specified by function (low-power controller, sub-GHz radio, thermistor input, sounder driver) and priced as a module assembly; board design and firmware are TRL 4 work | Decided by Amish, 2026-10-03 (pre-approval) |
| D4 | Block kit size | (b) 24 alarms, one station and one cart per drill block | Decided by Amish, 2026-10-03 (pre-approval) |
| D5 | Pump | (b) bought cast-iron semi-rotary pump, 25 mm ports, at least 0.40 L per double stroke; it is sold in markets in most target regions and is repairable with hand tools | Decided by Amish, 2026-10-03 (pre-approval) |
| D6 | Power | (b) no lithium cells anywhere in the kit: sealed lead-acid at the station, alkaline AA cells in the alarms. Conservative choice; lithium iron phosphate could be reconsidered with evidence of safe charging in 45 °C shade temperatures and a local recycling route. | Decided by Amish, 2026-10-03 (pre-approval) |
| D7 | Pressure protection | (b) 4 bar relief valve on a tee at the pump outlet, discharge pointing down, hose rated at least 10 bar. Conservative choice; the setting could rise only with a burst test of the bought hose and fittings at TRL 4. | Decided by Amish, 2026-10-03 (pre-approval) |
| D8 | Hose and nozzle | (b) 19 mm semi-rigid hose, 30 m on a reel, 6 mm jet and spray nozzle with shut-off; the hose pays out without being fully unrolled | Decided by Amish, 2026-10-03 (pre-approval) |
| D9 | R9 shortfall | (b) keep the target; stations are sited so that no shelter is more than 70 m along the path from one, and volunteers drill a 30 s muster. R9 is still reported as not met on paper for 100 m. | Decided by Amish, 2026-10-03 (pre-approval) |
| D10 | First partner and region | (a) Cox's Bazar camps, Bangladesh: the first candidate to approach is a camp shelter or site management agency with an existing community fire volunteer programme, together with the Bangladesh Fire Service and Civil Defence. Recorded as the first candidate, not as agreed. | Decided by Amish, 2026-10-03 (pre-approval) |

## Consequences

- CBK-PRB-001, CBK-PRC-001 and CBK-REQ-001 are revised to v0.3; the open questions are answered by D1, D4, D7, D9 and D10.
- Theft and misuse (an open question in CBK-PRB-001) are handled by the station layout: the cart parks under the station roof in view of the block, and the alarm box is a locked IP65 enclosure. No further parts were added.
- `budget_usd` stays at USD 1,600, a value-engineering target. The pitch and problem are unchanged.
- Nothing in this record authorizes building or testing; TRL 4 needs a new instruction from Amish.

## Safety

> **Safety:** CampBreak includes a pressurised hand-pumped water line (relief valve at 4 bar, hose rated 10 bar) and a sealed lead-acid station battery. The kit is for small, early fires only; people leave first, and water is never used on burning oil or live wiring. Safety stops are listed in the build plan, section 6. It is an open engineering reference, not certified equipment.
