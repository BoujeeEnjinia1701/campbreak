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
  change: Amish's round-2 decision 1A on R9 carried into the design
---

# 0004: Response time (R9): delivery hose stowed full of water

- **Date:** 2026-10-03
- **Status:** decided by Amish, 2026-10-03 (round 2): "i agree with all the 46 recommendations you provided. please proceed." For CampBreak this is decision 1A, the open decision posed in CBK-DEC-001 v0.2.

## Context

After CBK-DDR-003 (primed pump, coupled suction hose, "go when two arrive") R9 was 191 s at 100 m against 180 s, 11 s over. The rest of the gap was the 26 s needed to fill the empty delivery hose (8.85 L at 20.4 L/min) at the fire.

## Options considered

| Option | What it means |
| --- | --- |
| A (chosen) | Stow the delivery hose full behind the shut nozzle, refilled at the weekly check. No new parts; the 4 bar relief valve already protects the full hose from heating in the sun |
| B | Leave as is: R9 not met at 100 m by 11 s; the 70 m siting margin holds |
| C | Restate R9 to 3.25 min at 100 m |

## Decision

Option A. The geometry does not change: the hose, reel, pump and nozzle are the parts already in the model. What changes is the way the cart is stowed and the drill card.

*Table 1. Changes.*

| Item | Was | Now |
| --- | --- | --- |
| Delivery and connecting hose | Stowed empty and drained | Stowed full of water (8.9 kg) behind the shut nozzle; filled at build plan Step 12 and checked every week |
| Drill card (BOM 18) | Weekly prime check only | The weekly check also confirms the delivery hose is full |
| Build plan | Step 12 drains the hose | Step 12 fills it; new first check "Hose stays full" |

## Consequences

*Table 2. Results (CBK-CAL-001 v0.3).*

| Item | Result |
| --- | --- |
| R9 at 100 m | 177 s (2.95 min) against 180 s: **met on paper, 3 s to spare** (191 s before). The 25 s to run out the hose and aim now sets the pace |
| R9 at 70 m (siting margin) | 147 s (2.5 min) |
| Mass | Cart 103.4 kg stowed (was 94.6 kg), 8.9 kg more |
| Pull per person | 101 N on a 10 % slope (was 92 N). This is **1 N over the 100 N assumed sustainable**, so the assumption is slightly exceeded. R6 time (1.7 min) and width (850 mm) are still met. A third person on the handle or a halt on the way covers it, and the TRL 4 pulling trial measures the real effort |
| Margin | 3 s on R9 is thin; walk speed, gather time and pull-out time are estimates and the TRL 4 drill decides |
| Cost | Unchanged: no new parts. Value-engineering target: USD 1,600. Estimated cost of the constructable design: USD 1,374 (USD 226 under the target); `budget_usd` unchanged |
| Model | Unchanged geometry; 115 of 115 constructability checks still pass; STEP and STL not regenerated |
| Drawings | CBK-DWG-001 Rev P3; concept sheet CBK-DWG-010 Rev P3 |

To confirm at TRL 4: the nozzle shut-off and the pump hold the hose full for a week with no drip.

## Safety

> **Safety:** CampBreak includes a pressurised hand-pumped water line (relief valve at 4 bar, hose rated 10 bar) and a sealed lead-acid station battery. The cart now weighs about 103 kg: two people always move it, a third holds it back on slopes steeper than 10 %, and nobody runs with it. The full hose is kept shut at the nozzle; the relief valve protects it if the sun heats it. The kit is for small, early fires only; people leave first, and water is never used on burning oil or live wiring. It is an open engineering reference, not certified equipment.
