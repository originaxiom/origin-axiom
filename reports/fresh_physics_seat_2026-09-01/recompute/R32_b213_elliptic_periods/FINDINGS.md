# R32 — B213 "Higgs-side periods": every number in `higgs_periods.py` recomputed without Sage

**Target.** `frontier/B213_higgs_side_periods/higgs_periods.py` (E40A1 dict, l.13–58; NULL_L_OVER_OMEGA table) and
`FINDINGS.md` l.10–30. The Phase B reader marked the whole cell IMPORTED / reproducible-unknown: the numbers are
recorded Sage output, the script only re-prints them. B213 also imports B211's identification "the character-variety
polynomial Φ(x,z) = z² − (x²+1)z + (2x²−1) is the curve 40a1".

**What R32 did** (`r32.py`, PARI through SnapPy's cypari, mpmath, scipy): E = 40a1 by its Cremona coefficients
[0,0,0,−7,−6]; conductor, analytic rank, torsion (order and structure), CM test against the 13 rational CM
j-invariants, real period, L(E,1), Tamagawa numbers, BSD ratio; the 9 other rank-0 curves of the null table by
coefficients; the 40a isogeny class from `ellisomat`; the Mahler measure of Φ two ways (Jensen in z + 1-D mpmath
quadrature; direct 2-D torus integral); the j-invariant of the genus-1 curve Φ = 0 (as w² = (z−2)(z²−z−1) via
`ellfromeqn`) against every member of the 40a class; and a Boyd-type test m(Φ) vs L′(E,0).

## 40a1 headline — MATCH under the ω₁ convention

| quantity | bank | R32 | note |
|---|---|---|---|
| conductor / analytic rank / CM | 40 / 0 / no | 40 / 0 / no | j = 148176/25 not a CM value |
| "real period Ω" | 1.4844124734223865 | ω₁ = 1.484412473422386… | bank's Ω is the **least** real period (Sage `omega()` default); Δ > 0 so BSD's Ω = 2ω₁ = 2.96882 |
| L(E,1) | 0.7422811388969421 | 0.7422062367111932 | **bank is off by 7.5e−5** (Sage `lseries().at1()` is a truncated sum); the ratio below is unaffected because L(E,1) = ω₁/2 exactly |
| L(E,1)/Ω | 1/2 | L/ω₁ = 0.5000000000000000000000000 (25 digits) | headline holds |
| torsion | "ℤ/4" (order 4) | order 4, structure **ℤ/2 × ℤ/2** | x³ − 7x − 6 = (x+1)(x+2)(x−3): full rational 2-torsion, no point of order 4 |
| ∏c_p | 8 | **4** (c₂ = 2, c₅ = 2) | bank's 8 = 4 × 2 real components, i.e. it folded the component factor into ∏c_p |
| BSD check | Ш·∏c_p/|T|² = 8/16 = 1/2 | with Ω = 2ω₁: L/Ω = 1/4 = ∏c_p/|T|² = 4/16 ✓ (Ш = 1) | consistent once the conventions are separated |

## Null table (nine other rank-0 curves) — all MATCH under ω₁

11a1 1/5, 14a1 1/6, 15a1 1/4, 17a1 1/4, 19a1 1/3, 20a1 1/6, 21a1 1/4, 24a1 1/4, 37b1 2/3: every value reproduced
as L(E,1)/ω₁ (each also equals ∏c_p/|T|² times the component factor, as BSD requires with Ш = 1).
The bank's two isogenous entries do **not** come from one convention: the 40a class gives L/ω₁ ∈ {1/2, 1/2, 1/2, 1}
and L/Ω_BSD ∈ {1/4, 1/4, 1/2, 1/2}; the bank's "40a2 → 1" is an ω₁ value and its "40a3 → 1/4" is an Ω_BSD value.
Bookkeeping, not a numeric error, but the table cannot be read with a single period convention.

## The two imported identifications

- **"Φ is 40a1" (B211 → B213): not exactly.** Φ = 0 is a genus-1 curve of conductor 40 with j = 55296/5, which is the
  j-invariant of the class member [0,0,0,−32,64], not of 40a1 (j = 148176/25). Φ is **isogenous** to 40a1 (same
  L-function, same isogeny class), so every L-value statement survives; the curve-level identification is wrong by
  a 2-isogeny. **The bank already knows this elsewhere:** B509 ("E: Y²=X³−2X+1, disc 80, conductor 40, j=+55296/5 …
  Cremona label 40a3, isogenous (not isomorphic) to 40a1") and B510 ("the genus-1 cover d²=(c²−1)(c²−5) has Jacobian
  exactly 40a3; 40a3 is 2-isogenous to 40a1, not a quadratic twist") — so B211/B213's "Φ is 40a1" is a
  SUPERSEDED_UNMARKED case (the later arcs corrected the identification without touching B211/B213), not a new error.
- **"m(Φ) ≈ Ω/2 ≈ L(E,1)": near-coincidence, and the bank's number is wrong.** Jensen (30 digits) gives
  m(Φ) = 0.742264063232416; the direct 2-D torus integral gives 0.742267 (±3e−4, scipy's convergence limit) and
  the genus-0 shadow z² − (u+1)z + 2u − 1 (u = x²) gives the same value, as the substitution x → x² must. The bank's
  0.7417527164660 is **5.1e−4 away** from the recomputed value; its origin is not committed. The recomputed m(Φ)
  differs from L(E,1) by 5.8e−5 (relative 7.8e−5): not equal. A Boyd-type identity would relate m(Φ) to L′(E,0),
  not L(E,1); the ratio m(Φ)/L′(E_{40a},0) = 0.76411 with no small rational relation (lindep to 10 digits finds
  none), so there is no Boyd identity with the 40a L-function either.

## Verdict

**MATCH on the headline (L(E,1)/ω₁ = 1/2 and the nine-curve null table), with four corrections for cc**:
torsion structure ℤ/2×ℤ/2 not ℤ/4; ∏c_p = 4 (the 8 double-counts the two real components); L(E,1) misquoted at
7.5e−5; the Mahler measure misquoted at 5.1e−4 and the "≈ L(E,1)" reading is a near-coincidence with no identity
behind it. Plus one provenance finding: Φ = 0 is the 2-isogenous class-mate [−32,64], not 40a1 itself.

**Physics content:** none added. "Higgs-side" is a name; nothing in the cell attaches a mass, a coupling, or a
measurable quantity to L(E,1)/ω₁ = 1/2, which is the BSD formula for a torsion-4 curve with Ш = 1.
"No observable content."
