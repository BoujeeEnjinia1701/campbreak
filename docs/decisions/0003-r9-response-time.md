---
doc_id: CBK-DDR-003
title: CampBreak response time (R9) changes
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
  change: Amish's requirement decision 1A on R9 carried into the design
---

# 0003: Response time (R9): primed pump, suction hose left coupled, go when two arrive

- **Date:** 2026-10-03
- **Status:** decided by Amish, 2026-10-03: "1A 2A 3A 4A 5A 6A 7A 8A 9A 10A 11A". For CampBreak this is decision 1A.

## Context

R9 asks for water on target within 3 minutes of the alarm for a shelter 100 m from the station. At TRL 3 (CBK-CAL-001 v0.1) the time was 3.8 min, so R9 was not met on paper; CBK-DDR-001 (D9) kept the target and added a siting rule, no shelter more than 70 m from a station. The time at the fire was spent on a 60 s muster, 30 s to couple the suction hose and run out the hose, and 15 s to prime the pump.

## Options considered

| Option | What it means |
| --- | --- |
| A (chosen) | Fit a foot valve with a check so the pump stays primed; stow the suction hose coupled to the pump with a cam-lever (camlock class) coupling; drill the rule "go when two arrive" with a 30 s gather and put it on the drill card and in the build plan. Keep the 3 min target and keep "stations within 70 m of every shelter" as the siting margin |
| B | Leave the design and rely on the siting rule only |
| C | Lower the target or shorten the distance in R9 |

## Decision

Option A. The changes made:

*Table 1. Changes.*

| Item | Was | Now |
| --- | --- | --- |
| Foot valve (BOM 13) | Plain foot valve strainer | Brass spring-loaded foot valve, 25 mm, with a positive-seal check and a stainless strainer; holds the suction hose and pump full between uses |
| Suction hose stowage (BOM 13, 14) | Coiled loose in the tray; coupled to the pump at the fire | Left coupled to the pump inlet by its cam-lever adaptor with a 90° elbow tail; runs along the top of the left rail and onto its coil in the tray. The model checks it clears the wheels by 20 mm, the ground by 173 mm and the lever by 166 mm |
| Hose straps (new BOM 20) | None | Two rubber straps with buckles, round the left rail and the hose, 300 mm apart |
| Drill card (BOM 18) | Pump instruction label only | Laminated drill card in the station box: go when two arrive, the order of work at the fire, and the weekly prime check |
| Station sign (BOM 4) | Leave first, raise the alarm, fetch the cart | Adds "go when two arrive" |

## Consequences

*Table 2. Results (CBK-CAL-001 v0.2).*

| Item | Result |
| --- | --- |
| R9 at 100 m | 191 s (3.2 min) against 180 s: **still not met on paper, 11 s over**. Like for like, the decision saves 62 s (253 s before, once the hose fill is counted) |
| R9 at 70 m (siting margin) | 161 s (2.7 min): met |
| What remains | 26 s to fill the empty 30 m delivery hose, left out of the earlier figure. Stowing that hose full too would give 177 s (2.95 min); this is posed to Amish in CBK-DEC-001 |
| Mass | Cart 94.6 kg stowed primed (was 91.4 kg), including 2.6 kg of water; 92 N per person on a 10 % slope; R6 still met |
| Effort | The first pumper works alone until others arrive: about 95 W, more than the 75 W assumed sustainable for 10 min (est.), for a minute or two |
| Cost | USD 1,374 for the block kit (USD 19 more), USD 226 under the USD 1,600 value-engineering target (`budget_usd` unchanged) |
| Model | 115 constructability checks (18 new), all pass |
| Drawings | CBK-DWG-001 Rev P2; concept sheet CBK-DWG-010 Rev P2; sign sketch CBK-DWG-111 notes; build plan joint 12 and step 12 |

The foot valve's seal is now a working part: if it leaks, the pump loses its prime and about 15 s is lost at the fire. The drill card's weekly prime check finds it, and the leak-down rate is added to the items to confirm when parts are bought.

## Safety

> **Safety:** CampBreak includes a pressurised hand-pumped water line (relief valve at 4 bar, hose rated 10 bar) and a sealed lead-acid station battery. Going when two arrive must not mean going alone or running with the cart: two people always move it, and people leave the burning shelter first. The kit is for small, early fires only; water is never used on burning oil or live wiring. It is an open engineering reference, not certified equipment.
