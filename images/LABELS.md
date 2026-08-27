# Hilltop Market — image & video labels

Rename + page map only. Real shop photos; do not replace pixels with placeholders.

**Pages:** Home | Meat | Produce | Groceries | Gas | Visit | skip

**Visit:** map + NAP + hours only. Do **not** assign storefront photos (`hero-01`, `hero-02`, `hero-03`, `gas-01`) to Visit. `hero-03` is the Home-only exterior. `hero-01` / `hero-02` are not paired on any page.

**Tortillas:** Meat, not Produce. Both tortilla stills are carnicería. Only **one** tortilla shot on Meat: `store-02` (La Selecta cooler). `meat-02` / `meat-03` are extra case+tortilla stills — **skip**. Groceries only if a shot has no meat in frame (none of these).

**Rotation:** `meat-02.jpg` and `meat-03.jpg` were sideways after the scrape (price tags / bag text vertical). Rotated **90° clockwise** (lossless jpegtran) so text reads left-to-right, then renamed. `hero-01.jpg` pixels already read HILLTOP MARKET L→R (landscape 2048×1536); no rotation.

## Duplicate pairs (meat-01 … meat-10)

Do not treat every file as a unique hero. Same-subject `_1` / `_2` / `_3`:

| Cluster | Best for page | Weaker twin(s) |
|---|---|---|
| Instagram arrachera / taquizas still (same board, caption, knife, orange) | `meat-04.jpg` → `meat_arrachera_taquizas_1.jpg` | `meat-05` → `_2`, `meat-09` (720p) → `_3` — **skip** |
| Tomahawk + rib primal on the cutting board | `meat-06.jpg` → `meat_tomahawk_1.jpg` (**Meat**) | `meat-08.jpg` → `meat_tomahawk_2.jpg` — **skip** |
| USDA Prime arrachera with vacuum pack (`meat-01`) | Distinct shot — **Meat**, never Home | Not a twin of the taquizas trio |
| Meat case + tortillas (`meat-02` Rodeo, `meat-03` Santa Fe) | Related, different brands. **skip** (second/third tortilla shots; Meat page uses `store-02` only) | |
| Tomahawks with kale (`meat-10`) | Unique garnish plate — **Meat** | |
| Beef stacks in red bags (`meat-07`) | Unique prep — **skip** as extra | |

Other near-duplicates: `aisle-01` ≈ `produce-03` (same produce aisle; `produce-03` is the high-res `_1`); `hero-02` = `hero-04` (identical ice/ATM storefront; `hero-04` is the downscaled `_3`).

## Locked IDs

| old | new | rule |
|---|---|---|
| `hero-03.jpg` | `produce_oranges_potatoes_storefront_1.jpg` | Home first / only exterior |
| `hero-01.jpg` | `storefront_hilltop_ice_atm_1.jpg` | Not Home. Not Visit. skip |
| `hero-02.jpg` | `storefront_hilltop_ice_atm_2.jpg` | Do not pair with hero-01 or hero-03. skip |
| `store-01.jpg` | `skip_windshield_storefront_1.jpg` | skip / not Home |
| `meat-01.jpg` | `meat_arrachera_1.jpg` | Meat only; never Home |
| `store-02.jpg` | `meat_la_selecta_corn_tortillas_1.jpg` | **The** Meat tortilla shot. Caption: Fresh corn tortillas |
| `meat-02.jpg` | `meat_case_rodeo_tortillas_1.jpg` | Carnicería tortillas (Rodeo / case). skip — not a second Meat tortilla |
| `gas-01.jpg` | `gas_mobil_pumps_1.jpg` | Gas tab. Not Visit |
| `aisle-04.jpg` | `grocery_condiments_1.jpg` | Groceries |
| `aisle-05.jpg` | `grocery_tortilla_chips_1.jpg` | Groceries (chips, not tortillas) |
| `meat-11.jpg` | `meat_case_full_showcase_1.jpg` | Meat tab. Wide case: prime rib, T-bones, hanging longaniza, marinated trays, tortillas, chicharrones on top. Caption: Fresh pork rinds (chicharrones). LONGANIZA $4.99 LB sign is separate from the CHORIZO DE PUERCO tray |
| `meat-12.jpg` | `meat_longaniza_1.jpg` | Meat tab. Hanging U-shaped **longaniza** (not the chorizo tray) |
| `prepared-04.jpg` | `prepared_salsas_1.jpg` | Groceries. Caption: Fresh salsas. Not Home extras |
| `prepared-03.jpg` | `prepared_salsas_and_cheeses_1.jpg` | Groceries |
| `liquor-05.jpg` | `liquor_huichol_skull_tequila_1.jpg` | Not Home. No Liquor tab. skip |
| `meat-13.jpg` | `meat_steaks_butcher_paper_1.jpg` | Meat tab |

---

## Map

| old_filename | new_filename | one-line_label (what you see) | page |
|---|---|---|---|
| aisle-01.jpg | produce_aisle_citrus_chiles_2.jpg | Produce aisle: lemons, limes, oranges, papaya, hanging dried chiles, greens (weaker / low-res duplicate of produce-03) | skip |
| aisle-02.jpg | grocery_instant_birria_2.jpg | Close-up of Instant Birria 4 lb spice packets next to Goya garlic (tighter crop of the same birria display as aisle-03) | skip |
| aisle-03.jpg | grocery_chef_merito_birria_garlic_1.jpg | Chef Merito carne al pastor adobo, Instant Birria $6.99, and Goya minced garlic | Groceries |
| aisle-04.jpg | grocery_condiments_1.jpg | Condiments aisle: ketchup, dressings, cooking oil, mayonnaise, snacks, beer cooler at the back | Groceries |
| aisle-05.jpg | grocery_tortilla_chips_1.jpg | Bagged tortilla chips and tostadas: Hi-Chi's, Rodeo, Selecta | Groceries |
| aisle-06.jpg | grocery_ramen_candy_wine_1.jpg | Aisle with Buldak ramen, Van Camp's beans, hanging candy, and wine bottles | Groceries |
| gas-01.jpg | gas_mobil_pumps_1.jpg | Mobil pumps, tanker hose, and price sign with Hilltop Market | Gas |
| hero-01.jpg | storefront_hilltop_ice_atm_1.jpg | HILLTOP MARKET red letters, Packaged ICE chest, MetaBank ATM, window decals | skip |
| hero-02.jpg | storefront_hilltop_ice_atm_2.jpg | Same ice-chest / ATM storefront, portrait with car-hood reflection (do not pair with hero-01 or hero-03) | skip |
| hero-03.jpg | produce_oranges_potatoes_storefront_1.jpg | Storefront wall letters MEAT / PRODUCE / GROCERIES / LIQUOR; outdoor bins of oranges and potatoes | Home |
| hero-04.jpg | storefront_hilltop_ice_atm_3.jpg | Downscaled duplicate of hero-02 (ice chest, ATM, HILLTOP MARKET letters) | skip |
| liquor-01.jpg | liquor_score_tequila_soccer_ball_1.jpg | Score Tequila Reposado soccer-ball bottle in a Holiday Special box | skip |
| liquor-02.jpg | liquor_score_tequila_soccer_ball_2.jpg | Second Score soccer-ball tequila bottle (red/white/blue) on the counter | skip |
| liquor-03.jpg | liquor_moet_chandon_rose_1.jpg | Moët & Chandon Nectar Impérial Rosé on the checkout counter | skip |
| liquor-04.jpg | liquor_checkout_shelves_1.jpg | Checkout with floor-to-ceiling liquor wall (Glenfiddich, Don Julio 1942, sliding ladder) | skip |
| liquor-05.jpg | liquor_huichol_skull_tequila_1.jpg | Riqueza Cultural Huichol beaded skull tequila añejo, $249.99 | skip |
| meat-01.jpg | meat_arrachera_1.jpg | Thin-sliced USDA Prime arrachera / skirt steak, Upper Iowa / Angus pack, knife, orange | Meat |
| meat-02.jpg | meat_case_rodeo_tortillas_1.jpg | Meat case (carne preparada) with shelf of Rodeo / corn tortillas (rotated 90° CW); extra tortilla still | skip |
| meat-03.jpg | meat_case_santa_fe_tortillas_1.jpg | Beef case (arrachera, carne asada) with Tortilleria Santa Fe tortillas (rotated 90° CW); extra tortilla still | skip |
| meat-04.jpg | meat_arrachera_taquizas_1.jpg | Marbled arrachera on the board with taquizas Instagram caption (best of this trio) | skip |
| meat-05.jpg | meat_arrachera_taquizas_2.jpg | Same taquizas arrachera still, tighter crop (duplicate of meat-04) | skip |
| meat-06.jpg | meat_tomahawk_1.jpg | Five tomahawk steaks and a rib primal on the butcher board | Meat |
| meat-07.jpg | meat_beef_prep_bags_1.jpg | Stacks of raw beef steaks and red bags on the prep counter | skip |
| meat-08.jpg | meat_tomahawk_2.jpg | Same tomahawk + rib primal + arrachera board as meat-06 (weaker twin) | skip |
| meat-09.jpg | meat_arrachera_taquizas_3.jpg | Same taquizas arrachera still, 720p (weaker duplicate of meat-04) | skip |
| meat-10.jpg | meat_tomahawk_kale_1.jpg | Three bone-in steaks on a tray garnished with curly kale and green onion | Meat |
| meat-11.jpg | meat_case_full_showcase_1.jpg | Wide meat case: prime rib, T-bones, hanging longaniza, marinated trays, Rodeo tortillas, chicharrones on top | Meat |
| meat-12.jpg | meat_longaniza_1.jpg | Hanging U-shaped longaniza links over marinated pork adobada and chicken | Meat |
| meat-13.jpg | meat_steaks_butcher_paper_1.jpg | Three marbled steaks stacked on pink butcher paper | Meat |
| prepared-01.jpg | grocery_pinones_1.jpg | Three Meat Dept. tubs of toasted piñones, $19.99/lb, on the checkout counter | skip |
| prepared-02.jpg | prepared_nachos_al_pastor_1.jpg | Two plates of nachos with red marinated meat, cheese, crema, and salsa verde | skip |
| prepared-03.jpg | prepared_salsas_and_cheeses_1.jpg | Kool-It cooler: house salsas, guacamole, ceviche, crema, and packaged cheeses; tortillas on the floor | Groceries |
| prepared-04.jpg | prepared_salsas_1.jpg | Full salsa case: tomatillo verde / oro / rojo, guacamole, shrimp and crab ceviche | Groceries |
| prepared-05.jpg | grocery_roasted_seeds_1.jpg | Stack of six deli tubs of dark roasted seeds on a counter in front of grocery shelves | skip |
| produce-01.jpg | grocery_dairy_eggs_produce_1.jpg | Open case: butter, lard, eggs, potatoes, cucumbers, cabbage, celery, broccoli | Groceries |
| produce-02.jpg | produce_dairy_meat_corner_1.jpg | Corner where produce, dairy/eggs, and the beef case meet | Produce |
| produce-03.jpg | produce_aisle_citrus_chiles_1.jpg | High-res produce aisle: citrus, tortillas, greens, peppers, hanging dried chiles | Produce |
| produce-04.jpg | storefront_atm_produce_sign_1.jpg | Exterior EBT Cash ATM and FRESH QUALITY PRODUCE wall sign | skip |
| store-01.jpg | skip_windshield_storefront_1.jpg | Hilltop Market through a rainy car windshield (steering wheel in frame) | skip |
| store-02.jpg | meat_la_selecta_corn_tortillas_1.jpg | La Selecta all-natural corn tortillas in a cooler by the meat case | Meat |
| vid-01.mp4 | storefront_entrance_walk_1.mp4 | Walk along the MEAT/GROCERIES/PRODUCE/LIQUOR wall to the open door and Chi-Chi's chips | skip |
| vid-02.mp4 | aisle_salsas_meat_walk_1.mp4 | Walk from snacks through the salsa cooler to the meat case, cheese, and tortillas | Meat |
| vid-03.mp4 | meat_arrachera_taquizas_1.mp4 | Arrachera on the board with the taquizas caption (moving version of meat-04) | Meat |
| vid-04.mp4 | meat_pinones_tubs_1.mp4 | Meat Dept. $19.99/lb tubs of toasted piñones being packed | skip |
| vid-05.mp4 | storefront_beer_sign_atm_1.mp4 | Exterior COLD BEER sign, then EBT ATM and produce decal | skip |
| vid-06.mp4 | grocery_condiments_beer_cooler_1.mp4 | Condiments/snacks aisle into the three-door beer and seltzer cooler | Groceries |
