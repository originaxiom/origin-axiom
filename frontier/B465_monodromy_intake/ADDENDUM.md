# B465 ADDENDUM — Chat-2's shuttle verified: the c-construction, the 15/9 table, and the two-axis complementarity

**Added 2026-07-07 on receipt of Chat-2's shuttle answer to the B465 asks. Everything below
verified in-session (`c_family.py`) before writing. Firewalled.**

## Ask #1 delivered and VERIFIED — the c-family construction

Chat-2's family (as shuttled, implemented verbatim): F = (ζ₁₅^{jk}) fixed;
D_c(p) = diag(ζ₁₅^{p·c·j(j−1)/2}); WR_c = (1/15)·F·D_c(−1)·F^{−1}; W(m,c) = WR_c^m·D_c(m);
U_c = Par·W(1,c). **Their table reproduces exactly:**

| c | 1 | 2 | 4 | 7 | 8 | 11 | 13 | 14 |
|---|---|---|---|---|---|---|---|---|
| distinct eig of U_c | 15 | 9 | 15 | 9 | 9 | 15 | 9 | 15 |

The 9-case multiplicity pattern is (2,2,2,2,2,2,1,1,1), summing to 15 — confirming their
clarification ("9 distinct eigenvalues," never "9 total modes"). All U_c are unitary
(≤ 3.4e-15); the degeneracies are real spectral structure. **The split is exactly (c|5):
QR mod 5 → 15, NQR mod 5 → 9.** C4's INTAKE bin is upgraded from "not reproduced" to
**VERIFIED as constructed** — the original discrepancy was construction identity, exactly
as the a-priori argument said (their proof-not-Galois is accepted on both legs).

## The complementarity remark — verified on both sides, banked as a remark

- Chat-2's quadratic-form family splits {1,4,11,14} vs {2,7,8,13} = **(c|5)** — the √5 axis.
- The B465 Galois family splits {1,4,7,13} vs {2,8,11,14} = **(c|3)** — the √−3 axis.

Two different one-parameter families through the same operator, and their invariant splits
are exactly the **two generators of Gal(ℚ(√5,√−3)/ℚ)** — the banked genus-Klein-four (K020),
now appearing as the classification group OF FAMILIES OF DEFORMATIONS rather than of values.
The seat-level contradiction resolved into complementarity: both classifications correct,
per family.

## Their Q4, now answerable with the delivered construction — and answered

The l=1 two-generator structure per c (M_c = Par·W(1,c)·W(2,c), exact-numeric, gated):

- **(c|5) = +1 (c ∈ {1,4,11,14}): the FULL B465 structure persists** — μ₄-coset spectrum
  (step-15 AP), M⁴ = scalar, multiplicities (4,4,3,4), order-multiset {60:8, 15:4, 30:3}.
  The 8-4-3 is **family-class-shared**, not a c=1 fingerprint.
- **(c|5) = −1 (c ∈ {2,7,8,13}): the structure FAILS STRUCTURALLY** — 11 distinct
  eigenvalues, no μ₄-coset, **M⁴ not scalar**.

## The mechanism caveat (the sharpening to shuttle back)

The scalar-law failure at (c|5) = −1 is *prima facie surprising*: the formal classical
shadow of −W(1,c)W(2,c) has trace ≡ 0 for every unit c (Fricke, conjugation-invariant), so
a Weil/Egorov transport would force order 4 up to scalar for ALL c. The resolution: **the
c-family mixes the ψ_c quadratic-form data with the FIXED ψ₁ Fourier kernel**, so for c
outside the square class it is a *hybrid* operator family, not the ψ_c-Weil representation
— no Egorov guarantee exists, and none is violated. Empirically the 3-part mismatch is
harmless while the **5-part mismatch is what breaks the transport** — and 5 is the ramified
prime of the golden seed (m² + 4 = 5: disc(A₁) ≡ 0 mod 5, the banked m=1-exceptionality
mechanism). The derivation of the 15/9 multiplicities from the 5-part Gauss sums is the
named follow-up; the (c|5) empirics are banked as data.

## Bookkeeping

- Chat-2 verified the B465 core in their data (AP step 15, scalar law, (4,4,3,4), 8 = 4⊕4)
  and owned both corrections (period 6, not 3; grouping-by-property ≠ invariant subspace)
  — the record now three-seat-consistent on the dynamics arc.
- Their branch-merge observation (numeric tracking through exact degeneracies manufactures
  cycle structure) supports the B465 constraint on C5: Chat-1's cycles need algebraic
  continuation + the loop definitions, or stay unverified.
- Outstanding asks are now Chat-1's only: the 32-loop family, the dark-point phase family,
  the per-address max|tr| construction.
- H112 stands endorsed by both seats as the arc's theorem-shaped deliverable.

## Reproduce
```
python3 c_family.py     # the table gate + per-c l=1 structure + unitarity; ALL CHECKS PASS
```
