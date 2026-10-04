# B1471 — THE CANCELLATION IS A THEOREM OF AMPHICHIRALITY: at even n the geometric twisted Alexander function is real on every amphichiral member of the 112-family and complex on 40 of 41 chiral ones; the sep16 lane's five counter-examples are real, its instrument was an anti-homomorphism that only passes on m004, and the odd-n story is the lift's ℤ/2

**Verdict: PROVED** (scope: the 112-family (reach *class*), 54 members with H₁ of rank one; the theorem direction general under its
hypotheses; the converse empirical with one exception). cc (main), 2026-10-04. Pre-registration sealed at `39775d66`
(sha256 `0d5f3919…`) before any member but m004 was run. Lead L245 (xB011) verified **with a correction of the lane**;
B425's sentence scoped by addendum. **The prize first:** none for the derivation — this is a fact about a banked
invariant and about the record's opponent. **0 of 19.**

## 0. Seen first

As sealed: `topic_sweep.py "twisted Alexander|chiral.*torsion|torsion.*chiral|amphichiral.*real|Wada"` — VERDICT 43 of
1342 arcs on main match (NEGATIVE 6, OPEN 7, PROVED 30); B425, V30/V31, B581, B152, B849, B1186, B1235, B1453's
addendum read; `already_banked.py`: no settled arc computes the twisted polynomial across the family against chirality.
The lane's xB011 read at the pin `3205984b`. **Literature:** the symmetry step is Mostow–Prasad plus invariance; the
duality step Turaev's; Dunfield–Friedl–Jackson (Exp. Math. 2012) is the n = 1 knot case and was not re-read here.

## 1. What was computed

`verification/realness.py --family` on the 112 members of `chirality_112.json` at SnapPy's HP holonomy (≈64 digits,
SL(2,ℂ) lift repaired over 𝔽₂), φ the primitive class; the Wada function R_n(t) at Sym^n, n = 1..4, tested at
t ∈ {2, 3, 0.6, 1.7} with tolerance 10⁻²⁵: **T1** conj R(t) = ±R(t) (real up to a unit), **T2** R(1/t) = ±t^k R(t)
(duality), **T3** conj R(t) = ±t^k R(1/t), and (post-seal, for P5) **T4** conj R(t) = ±t^k R(−t). Every self-isometry
from `isomorphisms_to` with its cusp map's determinant and its sign on φ. 58 members have H₁ of rank 2–5 and are
reported, not dropped (`realness_run.txt`); **54 usable**, 13 amphichiral (by isometry; `is_amphicheiral()` and
B1235's column agree on all 112 — zero disagreements), 41 chiral. `analyze.py` scores the seal; `odd_characters.py`
finds the odd-n characters; `control_retri.py` is the presentation-independence control.

**Post-seal repair, disclosed.** The sealed `unit_match` capped the unit's exponent at |k| ≤ 12; true units reach
k = 20 (s118 at n = 4), so the first run reported 19 duality "failures" that were the cap. Raised to 80; the 19 all
hold with integer k and sign −1. The sealed retriangulation control (`randomize(3)`) returned the same presentation
on all three members — a vacuous control (MB12) — replaced by `control_retri.py`, which insists on different relators.

## 2. The sealed predictions, scored

| | prediction | prior | outcome |
|---|---|---|---|
| P1 | duality (T2) at even n on every rank-one member | 90% | **HOLDS 54 of 54** (after the cap repair) |
| P2 | T1 at even n on every member with an orientation-reversing isometry — the cancellation a theorem | 75% | **HOLDS 13 of 13**, phase real on all: m003, m004, m206, m207, s955, s957, s960, s961, t12838, t12839, o10_150695, o10_150696, o10_150707 |
| P3 | the lane's five resolve as misclassified, duality-failing, or purely imaginary | 70% | **FAILS as sealed — a fourth way:** all five are amphichiral by isometry, satisfy duality, and are **real** at n = 2 and 4 (R(2) = −5.125, −5.125, 1886.625, −26.875, −3.359375, imaginary parts ≤ 10⁻⁵⁰). The lane's table is an instrument error (§3) |
| P4 | chiral members mostly but not all complex | 60% | **HOLDS: 40 complex, 1 real** (o10_150709) |
| P5 | odd-n complexity on amphichiral members is the lift's ℤ/2; the sign character does not factor through φ | 60% | **HOLDS in mechanism, half in detail:** 7 of 13 are complex at odd n; on every one conj R_n(t) = R_n^{ρ⊗ε}(t) exactly (unit 1) for a sign character ε — through φ (ε = (−1)^φ) on five, a **torsion** character on s955 (ℤ/20) and s957 (ℤ/4) |

**The theorem, as the data state it.** For a one-cusped M with H₁ of rank one and an orientation-reversing
self-isometry f: ρ_geo∘f_* ≅ conj ρ_geo, φ∘f_* = ±φ, so conj R_n(t) ≐ R_n(t^{±1}) (T3 held on all 13 with both signs
present among the reversing isometries); with duality R_n(1/t) ≐ R_n(t) (T2, 54 of 54) this gives conj R_n ≐ R_n at
even n — coefficients real up to a unit; since the unit at real t ≠ 1 is ±1, the value at any real t is real or purely
imaginary, and the census found it real on all 13. At odd n the symmetry holds only up to a sign character
(ρ∘f_* ≅ conj ρ in PSL, lifted), and R_n picks up ε: the odd-n value is **lift-dependent** — `control_retri.py` shows
two presentations of the same member differing at odd n by more than a unit (m003, o10_150709 in the recorded run;
even n agrees up to ±t^k on all six members tried, |k| ≤ 5). The invariant at odd n is the orbit under sign characters.

## 3. The lane's instrument, and why its m004 control could not catch it

xB011's `sym(M, n)` expands (a x + b y)^{n−j}(c x + d y)^j — the **rows** of M, i.e. Sym^n(Mᵀ) — so
`sym(AB) = sym(B)·sym(A)` (checked: residual 1.3·10⁻⁴⁰ that way, 18.2 the other). Its "Sym^n∘ρ" is therefore
Sym^n∘ρ∘σ with σ the automorphism of the free group inverting every generator, and that is a representation of π₁(M)
only when σ preserves the relators. **On m004 it does** (σ(aaabABBAb) is a cyclic conjugate of the relator's
inverse — the strong inversion, B1455's ι, an isometry), **and on m003**, so the lane's F1 control passed and its two
two-generator rows are right (m003 agrees with main to all digits: 1.25 + √3 i, −0.625, −1.4375 − 2.5√3 i, 8.84375).
**On every three-generator member σ fails the relators** (|ρ(σr) ∓ 1| between 25 and 245 on m206, m207, s957, s960,
s961), and the lane's numbers there — −2735 + 10726 i at n = 2 on m206, magnitudes to 10¹⁷ — are the Fox determinant
of a non-representation. The lane's "chiral ⟹ √−3 survives, 8/8" rests on the same instrument and is unverified by
it; main's census gives the direction as 40 of 41. **The control lesson** (the E82 shape, on a lane): a control object
on which the error is invisible is not a control — m004's own symmetry made an anti-homomorphism look like a
representation. Main's B425 is untouched by any of this; the lane's correction of B425 was itself wrong in its
counter-examples and right in its scope note.

## 4. What it changes on main

- **B425** (addendum): "√−3 cancels in every determinant" is m004's sentence; it generalises to **every amphichiral
  member at even n as a theorem**, and fails on 40 of 41 chiral members. B425's values stand (reproduced to 10⁻⁵⁰).
- **L245**: xB011 VERIFIED-WITH-CORRECTION (scope note right; the five counter-examples and the 8/8 void);
  xB027 CONSISTENT with B1440 (the bound is ⌊n/2⌋ on once-punctured-torus bundles, attained at every rank; "≤ 1"
  was B1427's rank-two remark; B1418's |I| = 2 at rank four is the bound attained).
- **New to main:** the odd-n ℤ/2 as a computed fact — the character is (−1)^φ on five amphichiral members and a
  torsion character on two; and **o10_150709**, chiral (symmetry group ℤ/2 × ℤ/2, all orientation-preserving), real
  at even n, the same volume 10.1494 as the amphichiral o10_150707 and cs = ¼: the converse's one exception, a
  question left open here (a hidden symmetry? a mutation?), not a claim.
- **THE_BAR:** no selection is claimed; nothing to grade. **The imported expectation, stated separately:** none.

## 5. Scope

Frame F-CI; object the 112-family at level one; reach *class* (the 112-family) for the census, *general* for the theorem under its
hypotheses (one cusp, H₁ of rank one, an orientation-reversing isometry; duality taken from Turaev and verified on
every member run). Not a count on a vacuum; not an SM quantity. The 58 members with H₁ of higher rank are outside
the instrument (a multivariable polynomial would be needed) and are listed, not folded into either column.

## 6. Errors in this arc

The sealed cap (|k| ≤ 12) and the vacuous retriangulation control, both repaired post-seal and disclosed above; P3's
sealed trichotomy missed the actual fourth resolution (the lane's instrument wrong), which the data forced.

**Provenance.** `verification/realness.py` → `realness.json`, `realness_run.txt`; `analyze.py` → `analysis.json`;
`odd_characters.py` → `odd_characters.json`; `control_retri.py` → `control_retri.json`; `control_m004.json` (pre-seal).
Lock `tests/test_b1471_cancellation_theorem.py`. Cross-refs B425 (scoped), B1235 (column confirmed 112 of 112),
B1440 (xB027), B1455 (ι), B1469/L245 (xB011).
