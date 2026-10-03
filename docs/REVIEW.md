# Review note: CampBreak

## Session 2026-09-30: scaffolded

### What was done

- Repository created from kit 1.6.0 at TRL 1, target TRL 2.
- `docs/01-problem.md` (CBK-PRB-001 v0.1): problem with cited evidence, users, environment, constraints, prior work, open questions.
- `docs/02-concept.md` (CBK-PRC-001 v0.1): how it works, components, patent design-arounds, shared blocks, safety.
- `docs/03-requirements.md` (CBK-REQ-001 v0.1): 11 proposed requirements.
- `README.md` with concept rationale, burning platform, where it could be used, and what sparked the idea.

### Next

- Run `/populate` to bring the repo to a strong TRL 2 with concept media.

## Session 2026-10-03: TRL 2 (populate)

Run under `/to-trl3` with Amish's 2026-10-03 pre-approval: "start with the first 14 repos from the list of 29 projects. I pre-approve the batch runs along with any recommendations you come up with. I also accept any cost overruns or variations from the assumed scope cost."

### What was done

- Kit 1.7.0 installed (`.kit/`, `.claude/commands/`, root `CLAUDE.md` from `.kit/CLAUDE.md`).
- `docs/01-problem.md` (CBK-PRB-001 v0.3): budget worded as a value-engineering target; open questions answered; safety section.
- `docs/02-concept.md` (CBK-PRC-001 v0.3): how it works, components by BOM line, key design choices, first-order numbers, safety.
- `docs/03-requirements.md` (CBK-REQ-001 v0.3): 11 measurable requirements with TRL 3 status.
- Concept media from `cad/src/concept_media.py`: `media/hero.png` (with a 1.75 m figure), `media/concept-blueprint.png` and `.pdf` (CBK-DWG-010), `media/model.glb` and `media/viewer.html`, `media/cutaway.png` (heat alarm), `media/exploded.png` (cart, BOM callouts), `media/flow.png` (pressure along the water line, estimates).
- `bom/bom.csv`: 19 lines, every line priced.

### Results

The concept closes on paper except for response time at 100 m (R9) and the cooking test (R2), which cannot be calculated.

### Decisions made under the pre-approval

TRL 2 review items D1 to D10 (relay scheme, detection rule, board scope, kit size, pump, no lithium, relief valve, hose, R9 siting rule, first partner), recorded in `docs/decisions/0001-trl2-review-decisions.md` (CBK-DDR-001).

## Session 2026-10-03: TRL 3 (advance and build plan)

### What was done

- `cad/src/model.py`: parametric build123d model of the cart, station and heat alarm, made constructable, with 97 constructability checks (all pass). STEP and STL in `cad/step/` and `cad/stl/`.
- `docs/04-calcs/01-sizing.md` (CBK-CAL-001 v0.1) and `docs/04-calcs/sizing.py` with `results.csv`.
- `cad/drawings/CBK-DWG-001` Rev P1: general arrangement of the hose cart (`cad/src/sheets.py`).
- Build plan `docs/05-build-plan.md` (CBK-BLD-001 v0.1) with pictures from `cad/src/build_plan_media.py`: overview, 12 making sketches (CBK-DWG-101 to 112), 11 joint close-ups and 21 assembly steps.
- Design decisions register `docs/06-design-decisions.md` (CBK-DEC-001 v0.1) and decision record `docs/decisions/0002-design-for-construction.md` (CBK-DDR-002).
- Appearance model `cad/src/product_model.py` (hero, exploded and detail views; mannequin and forearm for scale). Scenes exported to `/home/claude/renders/campbreak` for the photoreal render on Amish's Mac. `media/render-hero.png` does not exist yet; the README already leads with it.
- `project.yaml`: trl 3, trl_target 3, `design_state: constructable`, evidence listed. `budget_usd` unchanged at 1,600.

### Results

- Flow 20.4 L/min at 47 W per person; jet reach 6.9 m; pump outlet 1.2 bar.
- Alarm 85.5 dB(A) at 3 m; relay 7.2 s worst case; battery life limited by cell shelf life.
- Cart 850 mm wide, about 91 kg loaded; 89 N per person on a 10 % slope; 1.7 min for 100 m.
- Station roof resists a 30 m/s gust uplift with a factor of about 2 on collar weight.
- Value-engineering target: USD 1,600. Estimated cost of the constructable design: USD 1,355 (USD 245 under the target).

### Requirements not met

- **R9 (water on target within 3 min at 100 m): not met on paper**, 3.8 min. With the decided siting rule (no shelter more than 70 m from a station, 30 s muster) the time is 2.8 min.
- R2 (no false alarm while cooking) cannot be shown on paper; it needs a cooking trial at TRL 4.
- Thin margins: R7 flow (2 %), R3 sound (0.5 dB), reel capacity (8 %).

### Decisions made under the pre-approval

- CBK-DDR-001, D1 to D10 (above).
- CBK-DDR-002, P1 to P12: the design-for-construction changes listed below.
- Open decisions: none. Items to confirm when parts are bought are in CBK-DEC-001 (pump displacement and flange, reel bore, hose diameter, jet orifice, sounder level, wheel hubs, relief setting).

### Build plan findings: design changes made for construction (2026-10-03)

1. Cart frame made a welded ladder frame of 30 mm square tube with bearers (P1).
2. Through axle in four 8 mm axle plates with spacers, collars and R-clips (P2).
3. Front legs with rubber feet so the cart parks level (P3).
4. Handle arms sitting on the rail tops, coped to the cross bar (P4).
5. Pump stand plate with gussets; pump bolted with four M12 bolts (P5).
6. Clamp-on lever extension with a T-bar for two people (P6).
7. Reel drum on a spindle in two welded uprights with a swivel inlet (P7).
8. Connecting hose from pump to reel, relief valve on a tee pointing down (P8).
9. Station on four posts in concrete collars instead of a two-post cantilever (P9).
10. Bought fixings for the station box, siren, panel and sign (P10).
11. Folded hose tray bolted to the bearers (P11).
12. Heat alarm on an aluminium plate hung by two ties under a roof pole; thermistor in a printed guard (P12).

### Appearance model

`cad/src/product_model.py` uses the model components unchanged; it only adds context (ground, a 1.75 m mannequin beside the drum, a forearm and hand beside the alarm) and leaves out the buried post ends and collars. No appearance deviations from `model.py`.

### Safety concerns

- Pressurised water line: relief valve at 4 bar fitted before first pumping, hose rated 10 bar, safety stops in build plan section 6.
- Sealed lead-acid station battery: fused at the terminal, connected last, locked box.
- A 91 kg cart on slopes: two people pulling, a third holding back on steeper slopes.
- Use limits: small, early fires only; people leave first; never water on oil or live wiring; drills only with the fire service or camp fire safety focal point present.
- No certification is claimed for the alarms or the firefighting equipment.

### Recommended next step

Photoreal renders and storefront images on Amish's Mac (`/render-product`). TRL 4 (build and test to CBK-BLD-001, starting with the pump flow and relief check and the cooking trial) needs a new instruction from Amish.

## 2026-10-03: photoreal renders

Rendered with Blender Cycles on Amish's Mac from `cad/src/product_model.py`; captioned with `.kit/photo_caption.py`; `media/card.png` and `media/social-preview.png` made with `.kit/cards.py`. Views: hero, exploded, detail. image_qc passes and `render.py --check` has no FAIL.

## 2026-10-03: Amish's requirement decisions carried out

Amish, 2026-10-03: "1A 2A 3A 4A 5A 6A 7A 8A 9A 10A 11A". For CampBreak this is decision 1A on R9 (water on target within 3 min at 100 m), recorded in `docs/decisions/0003-r9-response-time.md` (CBK-DDR-003) and in the register `docs/06-design-decisions.md` (CBK-DEC-001 v0.2).

### Changes made, with the new result for each

| Change | Files | New result |
| --- | --- | --- |
| Brass spring-loaded foot valve with a positive-seal check, so the pump and suction hose stay primed | `cad/src/model.py`, `bom/bom.csv` line 13 (USD 40, was 28) | No priming at the fire; suction loss factor raised to 7.0 (est.); R7 flow unchanged at 20.4 L/min, 47 W per person |
| Suction hose left coupled to the pump inlet by its cam-lever adaptor with a 90° elbow tail, run along the top of the left rail under two rubber straps and onto its coil in the tray | `cad/src/model.py` (new parts `suction_adaptor`, `suction_run`, `hose_straps`; 18 new checks, 115 of 115 pass), STEP and STL, `bom/bom.csv` lines 14 and 20 (new, USD 5) | Clears the wheels by 20 mm, the ground by 173 mm and the swung lever by 166 mm; tightest hose bend 63 mm radius |
| "Go when two arrive" with a 30 s gather on a laminated drill card, the station sign and in the build plan | `docs/05-build-plan.md` section 5a (drill card), Step 12, first checks; sign sketch CBK-DWG-111; `bom/bom.csv` line 18 (USD 27, was 25) | Gather 30 s instead of the 60 s muster |
| R9 recomputed (CBK-CAL-001 v0.2, section E), now with the 26 s to fill the empty 30 m delivery hose, which v0.1 left out | `docs/04-calcs/sizing.py`, `01-sizing.md`, `results.csv`; `docs/03-requirements.md` v0.4 (wording unchanged, result updated) | **R9 at 100 m: 191 s (3.2 min) against 180 s, still not met on paper, 11 s over** (3.8 min before; 4.2 min like for like with the fill counted). At 70 m, the siting margin kept: 161 s (2.7 min), met |
| Cart mass and pull | `sizing.py`, `01-sizing.md` | 94.6 kg stowed primed (was 91.4), including 2.6 kg of water; 92 N per person on a 10 % slope; R6 still met (1.7 min) |
| Cost | `bom/bom.csv` | Value-engineering target: USD 1,600. Estimated cost of the constructable design: USD 1,374 (USD 226 under the target). `budget_usd` unchanged |

Pictures changed: general arrangement CBK-DWG-001 (Rev P2), concept sheet CBK-DWG-010 (Rev P2), `media/hero.png`, `media/exploded.png`, `media/model.glb`, build plan overview, sign sketch CBK-DWG-111, new joint 12 (Figure 17; later figures renumbered), Step 6 to Step 17. Documents also updated: `docs/02-concept.md` v0.4, `docs/01-problem.md` v0.4 (cost), `README.md`, `project.yaml` (evidence), `cad/src/product_model.py` (materials for the new parts; scenes re-exported to `/home/claude/renders/campbreak`). `Compound(children=...)` replaced by `Compound([...])` in the scripts.

### Decision proposed, awaiting Amish

Stow the 30 m delivery hose full of water as well (CBK-DEC-001, open decision 1). Options: (a) leave as is, R9 not met at 100 m by 11 s, the 70 m margin holds; (b) stow the hose full behind the shut nozzle: 177 s (2.95 min) at 100 m, met with 3 s to spare, 8.9 kg more on the cart (about 101 N per person on a 10 % slope, just over the 100 N assumed sustainable), no new parts; (c) restate R9 to 3.25 min. Recommendation: (b).

### Safety

- The first pumper works alone for a minute or two until others arrive, at about 95 W, above the 75 W assumed sustainable for 10 min (est.); the drill checks it.
- "Go when two arrive" never means one person with the cart or running with it; people leave the shelter first. Both are on the drill card.
- The foot valve's seal is now a working part; the weekly prime check on the drill card finds a leak.

### Recommended next step

Amish decides open decision 1. TRL 4 (build and test to CBK-BLD-001, including the week-long prime hold and the timed drill at 70 m and 100 m) needs a new instruction from Amish.

## 2026-10-03: photoreal renders redone after Amish's requirement decisions

Rendered with Blender Cycles on Amish's Mac from `cad/src/product_model.py`; captioned with `.kit/photo_caption.py`; `media/card.png` and `media/social-preview.png` made with `.kit/cards.py`. Views: hero, exploded, detail. image_qc passes and `render.py --check` has no FAIL.
