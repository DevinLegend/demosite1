# Hilltop Market — image labels

Labels + page assignments only. Do not treat this as a redesign brief.

**Pages:** Home | Meat | Produce | Groceries | Gas | Visit | skip

**Rotation note (this commit):** `meat-02.jpg` was sideways (Rodeo tortillas / meat-case price tags read vertical). Rotated **90° clockwise** so text is upright. `hero-01.jpg` and `hero-02.jpg` pixel data were already upright (OCR: HILLTOP MARKET / window decals read L→R); no rotation applied.

---

## Present in `images/` (on main)

| Filename | Label | Page | Notes |
|---|---|---|---|
| `hero-03.jpg` | Front of shop with big wall letters MEAT / PRODUCE / GROCERIES / LIQUOR; oranges and potatoes outside | **Home** | **First / only exterior on Home.** |
| `hero-01.jpg` | HILLTOP MARKET red letters, Packaged ICE chest, MetaBank ATM, window decals | **Visit** | Fine photo; **not** on Home next to hero-03. Already upright on disk. |
| `hero-02.jpg` | Another storefront angle (red HILLTOP MARKET letters, ice chest, ATM) | **Visit** | Do **not** pair with hero-01 or hero-03 on the same page. Already upright on disk. |
| `store-01.jpg` | Hilltop Market seen through a rainy car windshield (steering wheel in frame) | **skip** | Skip for Home. |
| `meat-01.jpg` | Fresh marbled arrachera / skirt steak on the board (USDA Prime pack visible) | **Meat** | Meat only — **never Home.** |
| `meat-02.jpg` | Meat case with prepared carne + shelf of Rodeo / corn tortillas | **Meat** | Was sideways on live site; **rotated 90° CW** this commit. Not Home. |
| `aisle-01.jpg` | Produce aisle: citrus, papaya, leafy greens, dried chiles hanging | **Produce** | Also usable on Groceries if needed. |
| `produce-01.jpg` | Refrigerated dairy, eggs, and fresh produce (cabbage, celery, broccoli) | **Groceries** | Mix of butter/eggs + bottom produce. |
| `liquor-01.jpg` | Specialty Score Tequila Reposado soccer-ball bottle in gift box | **Groceries** | Liquor specialty; keep off Home hero. |
| `gas-01.jpg` | Mobil pumps and price sign with HILLTOP MARKET branding | **Gas** | New Gas tab reference. |

---

## KEY IDs (honor these)

| ID | Rule |
|---|---|
| `hero-03.jpg` | FIRST picture on Home. Only one exterior on Home. |
| `hero-01.jpg` | Not on Home next to hero-03. Prefer Visit. |
| `hero-02.jpg` | Do not pair with hero-01 or hero-03 on the same page. |
| `store-01.jpg` | Skip for Home. |
| `meat-01.jpg` | Meat page only. Never Home. |
| `store-02.jpg` | Meat page. Label: **Fresh corn tortillas.** *(file missing from this checkout — see below)* |
| `gas-01.jpg` | Gas tab. |
| `meat-02.jpg` | Meat (Rodeo tortillas + meat case). Not Home. |

---

## Expected dump files not present on disk

The agent prompt attached **38** shop JPGs expected under `demos/hilltop-market/images/`, but only the **10** files already on `main` were available in this environment. Labels below are from the attachment brief / vision descriptions so a follow-up can drop files in without re-triaging.

| Filename | Label | Page | Status |
|---|---|---|---|
| `store-02.jpg` | Fresh corn tortillas | **Meat** | Missing — La Selecta cooler by meat case |
| `hero-04.jpg` | *(unclassified exterior / interior — attach dump)* | skip until reviewed | Missing |
| `aisle-02.jpg` … `aisle-06.jpg` | Grocery / produce aisle shots | Produce or Groceries | Missing |
| `liquor-02.jpg` … `liquor-04.jpg` | Liquor aisle / coolers | Groceries | Missing |
| `meat-03.jpg` … `meat-12.jpg` | Meat case / cuts / prepared meat | **Meat** | Missing — find pork rinds here |
| `prepared-01.jpg` | Freshly prepared nachos with marinated meat, cheese, salsa verde | **Meat** | Missing (described in attach set) |
| `prepared-02.jpg` … `prepared-05.jpg` | Prepared salsas / guacamole / ceviche / roasted seeds | Meat or Groceries | Missing — find pork rinds / extra tortilla shots |
| `produce-02.jpg` … `produce-04.jpg` | Fresh produce displays | **Produce** | Missing |

### Find-on-arrival checklist

When the missing dump lands, search **`prepared-*.jpg`** and **`meat-*.jpg`** for:

1. **Pork rinds / chicharrones** → site English label: **Fresh pork rinds (chicharrones)** → **Meat**
2. Any other **tortilla** shots (besides `store-02` / `meat-02`) → **Meat**
3. Any still-sideways frames (price tags or bag text vertical) → rotate upright before publish

### Review refs (not site assets)

| Ref | Purpose |
|---|---|
| `hero-03-front.jpg` | Confirms Home exterior identity |
| `hero-01-sideways.jpg` | Review of ice-chest / ATM storefront (repo `hero-01.jpg` pixels already upright) |
| `meat-01-arrachera.jpg` | Confirms Meat-only arrachera shot |
| `gas-01-mobil.jpg` | Confirms Gas / Mobil identity |
| `live-home-safari.png` | Live Home screenshot reference |

---

## Suggested Home set (labels only — no HTML edits in this agent)

1. `hero-03.jpg` — sole exterior
2. Interior / department shots as needed — **exclude** `hero-01`, `hero-02`, `store-01`, `meat-01`, `meat-02`
