# 05 — The n=5 wall

> Narrative, not claim. Cites the mathematics one-way.

Every route the program tried stalled at the same place: `n = 5`. The honest characterization of *why* took three
audits and a withdrawn narrative.

The first telling was tidy: "one collision causes all the walls." It was **withdrawn** (V91). The truth is that
`n = 5` is a **threshold where three *distinct* `A₄` obstacles degenerate together** — not one cause:

- **degree=rank** (**B95**, V79; sharpened by **B153**, V143/V145): the principal spectrum (forced *given* the
  mult-(n−2) ansatz) `2cos θ = 3 − n` reaches `−1` at `n = 5`. A principal/Dehn-filling representation has its
  boundary element of **finite order** ⟹ semisimple ⟹ `A² = I` ⟹ `⟨A,B⟩` dihedral ⟹ **reducible** — so there is
  **no irreducible principal rep at `n=5`** (now *proven*, not numerical). "exponent = rank" is an `n ∈ {3,4}`
  phenomenon. (A 2026-06-15 self-audit corrected an earlier "`0/120`, no irreducibles" reading: non-semisimple
  reps with the same eigenvalue spectrum — boundary element of *infinite* order, hence not Dehn-filling — *do*
  exist and are irreducible, but degree=rank fails on them, so they live outside the wall.)
- **the tower / eps-series** (**B62**): the `A₄` height-2 root space splits `(4,2)` under `θ = −w₀`, giving
  `char(M²)²` — pure root-system combinatorics, the golden `φ²`, with *no* reference to the spectrum above.
- **trace-ring non-closure** (engine-free): the `n²−1` coordinates stop generating the SL(n) trace ring, an onset
  at `n = 4`, purely algebraic.

Different eigenvalues (`−1` vs `φ²`), independent derivations, different onsets. Two further audit corrections
(V90) were banked *visibly* rather than silently: the seed-variation of the unresolved SL(5) factors is the
eps-series rank-deficiency *signature*, **uninformative** about the truth there (so a structural deviation is
neither ruled in nor out); and there is **no proved "natural boundary"** at `n=4` — `char(J(n))` is a class
function for all `n` (chapter 04), so the wall is a *methodological ceiling*, not a theorem.

The explicit `n ≥ 5` catalog is therefore **OPEN** — walled from two independent methods, with the structural
`ρ_n` proof (chapter 04) as the way through. The discipline of this chapter — *withdraw the tidy story, keep the
three honest obstacles* — is itself one of the project's results.

→ `06_three_fixed_point_classes.md`.
