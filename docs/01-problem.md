---
doc_id: CBK-PRB-001
title: CampBreak problem statement
project: CampBreak
doc_type: Problem statement
version: "0.4"
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
  change: "Estimated cost updated after Amish's R9 decision (CBK-DDR-003)"
---

# CampBreak problem statement

In a dense camp, a shelter fire becomes a block fire within minutes. The people who are there in those minutes are residents, and they have almost nothing to fight it with.

## The problem

Camp shelters are built from bamboo, tarpaulin and thatch, packed closer than planning standards allow, and cooked in with open flames. Residents in the January 2024 Camp 5 fire described flames spreading with the wind through thatch roofs, while hilly ground slowed vehicles and hydrants ran dry ([The New Humanitarian, 2024](https://www.thenewhumanitarian.org/news-feature/2024/01/10/fire-bangladesh-rohingya-refugee-camp-where-is-support)). In informal settlements more widely, residents raise the alarm, evacuate, gather water and fight fires themselves, but with poor equipment and little training ([Engineering X](https://engineeringx.raeng.org.uk/media/03cd1j4l/engx-a-comparative-study-of-fire-risk-emergence-in-informal-settlements-in-dhaka-and-cape-town-short.pdf)).

Parts of the answer exist separately. Lumkani's networked heat detectors raise the alarm across neighbouring homes and have been installed in South Africa, Kenya and Bangladesh ([Wikipedia](https://en.wikipedia.org/wiki/Lumkani)), and a 2026 study found rate-of-rise heat detection better suited than smoke alarms to homes that cook with open flames ([Afrin and Rush, 2026](https://www.sciencedirect.com/science/article/pii/S0379711226002171)). Camp agencies have deployed three-wheeler mobile firefighting units ([The New Humanitarian, 2024](https://www.thenewhumanitarian.org/news-feature/2024/01/10/fire-bangladesh-rohingya-refugee-camp-where-is-support)). What is missing is an open kit that links the alarm to water at block level, is hand-powered, and can be built and repaired in the camp.

## Users and context

| User | Need | Context |
| --- | --- | --- |
| Camp residents and block fire volunteers | Hear the alarm fast and get water onto a burning shelter within minutes | Night and day, narrow paths, slopes, no power at the shelter |
| Camp management and site planning agencies | A low-cost, repairable block kit that fits existing fire safety plans | Planned and unplanned camps, dry-season water shortages |
| Local fire services | Fires held small until engines or mobile units arrive | Long travel times and poor vehicle access |
| Community groups in urban informal settlements | A shared station they can own, maintain and train on | Dense shack neighbourhoods with communal standpipes |

## Operating environment

- Outdoor block station and indoor shelter alarms; ambient 5 to 45 °C (41 to 113 °F), monsoon rain, dust and high humidity.
- Unpaved, sloping and muddy paths, often under 1.5 m (5 ft) wide, with steps and drains to cross.
- Water from 200 L drums, jerrycans, tube wells or taps; supply may be low in the dry season.
- Cooking smoke and open flames inside or beside shelters, which rule out smoke-based detection.
- No mains power at the shelter; alarms run on batteries or small solar cells.

## Constraints

- Value-engineering target of USD 1,600 for one block kit (24 alarms, one station and one hose cart), a hypothetical control target rather than a limit; off-the-shelf parts and workshop fabrication. Estimated cost of the constructable design: USD 1,374 (USD 226 under the target).
- Hand-powered pumping only; no fuel engine on the cart.
- Cart must be moved by two adults on the paths above.
- Alarm detection by rate of rise of temperature, not smoke, to avoid cooking false alarms.
- Open design: hardware under CERN-OHL-S-2.0, firmware under MIT.
- No claims of alarm or extinguisher certification; published as an engineering reference.

## Out of scope

- Fighting fully developed block fires; that remains the fire service's job.
- Arson prevention, security and policing in camps.
- Shelter materials, fire-retardant treatments and site layout.
- Certified smoke or heat alarms and certified extinguishers.
- Motorised pumps and hydrant networks.

## Prior work

| Prior work | What it does | Gap for these users | Source |
| --- | --- | --- | --- |
| Lumkani networked heat detector | Rate-of-rise heat detector that alarms all homes within about 60 m and sends SMS alerts through a gateway | Raises the alarm but gives residents nothing to fight the fire with; the mesh network is described as patented | [link](https://en.wikipedia.org/wiki/Lumkani) |
| Stirrup pump | Portable hand pump used with a bucket of water to control small fires, used widely in civil defence | Needs constant bucket refilling and a crew; no stored hose or station at block level | [link](https://en.wikipedia.org/wiki/Stirrup_pump) |
| Hand-pumped fire engines and hose carts (1700s to 1800s) | Manually pumped engines with hose, drawn by crews and fed by buckets or cisterns | Large crews and heavy apparatus; not sized for narrow camp paths or modern parts | [link](https://hallofflame.org/hand-and-horse-drawn-apparatus/) |
| Indian 5-gallon backpack firefighting pump | Backpack water tank with hand-operated pump used in wildland firefighting | Small water volume per trip and no alarm link | [link](https://www.forestry-suppliers.com/product_pages/products.php?mi=15791&itemnum=85700) |
| Camp mobile firefighting units (MFFU) | Three-wheeler firefighting vehicles deployed in the Cox's Bazar camps | Limited by terrain and vehicle access and by hydrant water in the dry season | [link](https://www.thenewhumanitarian.org/news-feature/2024/01/10/fire-bangladesh-rohingya-refugee-camp-where-is-support) |

## Co-design

A camp management or shelter agency with an existing community fire volunteer programme, ideally working with a local fire service, so that the kit is tested against real drills, real paths and the water sources residents actually have.

## Answers to the open questions

The scaffold's open questions were answered at TRL 2 and TRL 3 and decided under Amish's 2026-10-03 pre-approval (CBK-DDR-001):

- **Alarm relay scheme:** a published star scheme. Each alarm reports to the block station, which sounds its siren and broadcasts once so every alarm sounds. It is not a mesh, and it will be checked against Lumkani's patents before release (D1).
- **Kit size and coverage:** 24 alarms, one station and one cart per block; stations are sited so that no shelter is more than 70 m from one (D4, D9).
- **Flow and pressure:** about 20 L/min through a 6 mm jet reaching about 6.9 m, at about 1.2 bar at the pump, with a 4 bar relief valve (CBK-CAL-001, D7).
- **Theft and misuse:** the cart parks under the station roof in view of the block and the alarm box is a locked enclosure. Arson remains out of scope.
- **First drill:** the first candidate to approach is a camp management agency in the Cox's Bazar camps working with the Bangladesh Fire Service and Civil Defence; nothing is agreed yet (D10).

## Safety

> **Safety:** CampBreak is for small, early fires only. People leave first; nobody enters a burning shelter or stays when the fire spreads. Water is never used on burning cooking oil or live wiring. The pump and hose are pressurised (relief valve at 4 bar); the station holds a sealed lead-acid battery. The kit is an open engineering reference, not certified fire alarms or firefighting equipment.
