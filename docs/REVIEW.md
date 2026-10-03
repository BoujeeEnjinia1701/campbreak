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
