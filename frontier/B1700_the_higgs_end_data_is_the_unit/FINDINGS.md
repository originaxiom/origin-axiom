# B1700 — THE HIGGS'S END DATA IS THE UNIT (P-245): FK10'S TAGGED UNIT, AS W46 DEFINES IT, ALREADY CONTAINS THE END-DATA HIGGS ∂R — NO SECOND POSTULATE — BUT IT ALLOWS A THREE-DIMENSIONAL FAMILY OF WEIGHT-3/2 HIGGS DIRECTIONS, AND ONLY ∂R, THE ONE WITH THE COUPLING TRIPLET'S OWN END CONDITION, GIVES A HIERARCHY

**Verdict: PROVED (exact; no data).** cc (main), 2026-10-22. The fork P-245 registered (B1697 item 1): the cusp
hierarchy of the newest frame exists only if the Higgs carries end data on v₊ — is that FK10's tagged unit (GENESIS
v1.39, the owner's working postulate for the chiral three) or a second datum? Decided by the math. 0 of 19.
- **The unit, as defined.** W46's end condition is n uniform units at the cusp: its index is −χ_{3/2+12n}(ρ_T) (B1641,
  verified on main), so one unit makes the weight-3/2 sections of ρ_T the space Δ⁻¹·M_{27/2}(ρ_T) with the canonical
  exponents — every eigenline of ρ(T) one unit lower. ρ_T is the matter's ρ_R (B1634: ρ_T = χ_η²¹ ⊗ ρ_θ², the multiplier of
  R = θ²/(2πη³)).
- **Computed exactly** (`verification/the_units_sheaf.py`; q-series in x = q^{1/8} with Gaussian-rational coefficients,
  B1691's module): the eigenline orders at the cusp (lines P, M = v₊, N, exponents ⅛, −⅛, ⅜ mod 1) are R (1, −1, 3),
  ∂R (1, −1, 3), ∂²R (9, −1, 3). On the free module's weight-27/2 piece (E₄²E₆R, E₄³∂R, Δ∂R, E₄E₆∂²R) the canonical
  conditions are one: no x⁻¹ on v₊. **So the unit's weight-3/2 space is three-dimensional** — W46's three (B1641's table:
  −χ_{27/2} = −3; at n = 0, χ_{3/2} = 0 and no canonical weight-3/2 form exists) — with the basis
  - **∂R** (Δ∂R is canonical), line orders (1, −1, 3);
  - **E₄²(E₄∂R + E₆R/12)/Δ** and **E₄E₆·a₀/Δ** (a₀ = ∂²R − E₄R/48, B1697's unit-free Higgs), line orders (−7, −1, −5).
- **Where ∂R sits.** It lies in the unit's space, and it is the space's **only member (up to scale) holomorphic on the two
  lines other than v₊** — the end condition of the coupling triplet R itself (R's own orders (1, −1, 3)): ∂R uses the unit
  on v₊ alone, as R does.
- **The hierarchy.** The second-to-third exponent at the cusp (B1691's census formula): m₂/m₃ ~ ∣q∣^{1/2} for ∂R; **0 — no
  hierarchy — for the other two basis members and for three generic members.** The unit's other directions carry poles
  x⁻⁷ and x⁻⁵ off v₊, which dominate at the cusp.
- **The ruling (by the math).** The end data the hierarchy needs are FK10's tagged unit, not a second postulate: ∂R is a
  section of the unit's own weight-3/2 space, the space whose dimension is the chiral three. But the unit does not select
  it: the hierarchy needs the member with the coupling triplet's end condition — the Higgs in the module R generates,
  which is how H-cov was used from B1691 on. So the hierarchy arcs (B1691, B1694–B1699) hold **given Λ, the unit, and
  H-cov in R's own module**; B1697's "end data on v₊, a datum of FK10's kind" sharpens to "FK10's unit, used as R uses
  it". The GENESIS sentence for FK10 joins v1.52's batch (P-237).
- **A structural remark (a reading, not a claim).** At weight 3/2, given the unit, the Higgs direction ∂R and the chiral
  three's zero modes (W45: the triplet's index at weight 3/2) are sections of one and the same three-dimensional space;
  ∂R is its member with R's end condition.
- **What it does not do.** It does not derive the unit (FK10 stays a tagged postulate) or H-cov (P-115); no data.

## 0. Seen first

`VERDICT topic-sweep /units? of end data|end data at the cusp|uniform units?|canonical cusp condition|one unit on v|chi_\{?3/2|χ_\{?3/2/ (full text): 13 of 1471 arcs on main match (NEGATIVE 4, PROVED 9)` —
B1627, B1629, B1631 (the unit kept open, sharpened, tagged), B1632, B1634, B1641 (W45, W46 and ρ_T on main), B1691,
B1694–B1697, B1699. None computes the unit's weight-3/2 space or places ∂R in it. **Literature:** vector-valued modular
forms as a free module over M_* (Marks and Mason; Bantay and Gannon), as context.

## 1. Files

- `verification/the_units_sheaf.py` → `the_units_sheaf.json`, `the_units_sheaf_run.txt`.
- The lock: `tests/test_b1700_the_higgs_end_data_is_the_unit.py`.
