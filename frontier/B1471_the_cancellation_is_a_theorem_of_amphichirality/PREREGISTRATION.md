# B1471 — PREREGISTRATION: IS THE CANCELLATION A THEOREM OF AMPHICHIRALITY? — the geometric twisted Alexander function across the 112-family, the lane's five counter-examples, and the two steps of the argument checked member by member

**Sealed before any computation on the population.** cc (main), 2026-10-04. Lead L245 (the sep16 lane's claims about
main): xB011, *"B425's '√−3 cancels in every determinant' is an AMPHICHIRALITY ARTEFACT, not a general fact"*, with
its table *"chiral ⟹ √−3 survives, 8/8; the converse is FALSE — five amphichiral members (m206, m207, s957, s960,
s961) are complex everywhere"*. This arc verifies the claim with main's own instrument and asks the question the lane
did not: whether the cancellation on amphichiral members is a theorem, and if so what its five exceptions are.

## 0. Seen first

- **Repo, by sweep.** `topic_sweep.py "twisted Alexander|chiral.*torsion|torsion.*chiral|amphichiral.*real|Wada"`:
  VERDICT 43 of 1342 arcs on main match (NEGATIVE 6, OPEN 7, PROVED 30). Read: B425 (the geometric torsion of m004 at
  Sym^{2m}, exact; "√−3 cancels in every determinant" — stated of m004, its guard section on the un-normalised Fox
  determinant), V30/V31 (Porti's adjoint torsion −3), B581 (the six torsions at the E₆ exponents, sign (−1)^m), B152
  (amphichiral ⟹ CS 2-torsion, 240 manifolds, m208 the converse failure), B849 (amphichirality forces every
  orientation-odd invariant to 2-torsion), B1186 + B1235 (the 112-family and its amphichirality column, 38 of 112,
  `chirality_112.json`), B1453's addendum on B1186 (99 of the 112 in m004's commensurability class; 13 with a
  non-integral trace). `already_banked.py`: no settled arc computes the twisted polynomial across the family against
  chirality. **Nothing on main states the cancellation beyond m004.** The lane's xB011 read at the pin `3205984b`
  (`verification/family_odd.py`): its test is the value at t = 2 only, labelled REAL when |Im|/|v| < 10⁻¹⁵, its
  population xB007's 21 members ≤ 6 tetrahedra (16 with H₁ of rank 1), its amphichirality `symmetry_group().is_amphicheiral()`.
- **Literature.** The symmetry step is standard: an orientation-reversing self-isometry f has ρ_geo∘f_* conjugate to
  the complex conjugate of ρ_geo (Mostow–Prasad), and the twisted polynomial is a homeomorphism invariant; the duality
  step is Turaev's duality for Reidemeister torsion on a manifold with torus boundary with a self-dual coefficient
  system (Sym^n of SL(2) is self-dual). Dunfield–Friedl–Jackson's hyperbolic torsion polynomial (Exp. Math. 2012) is
  the n = 1 knot case; **not re-read here** — what they record about real coefficients is not cited as theirs until read.

## 1. The objects and the instrument, fixed now

The 112 members of `frontier/B1235_two_seat_harvest/verification/chirality_112.json` (B1186's family: shape field
ℚ(√−3)), each at SnapPy's HP holonomy (≈64 digits) with the SL(2,ℂ) lift repaired over 𝔽₂ when the relators map to −I,
φ: π₁ → ℤ the primitive class (members with H₁ of rank ≠ 1 reported, not dropped), the Wada function
R_n(t) = det(Fox matrix of Sym^n ρ ⊗ t^φ, one column deleted) / det(Sym^n ρ(g_j) t^{φ(g_j)} − 1), n = 1, 2, 3, 4;
`verification/realness.py` (sha256 2d4c5c0e30ce40b2 at the seal; `--family` runs the 112), run on m004 only before the seal (`verification/control_m004.json`) (the control: B425's exact (t² − 4t + 1)/t²,
(t − 1)(t² − 5t + 1)/t³, (t² − 4t + 1)²/t⁴ reproduced at t = 2 up to the unit −1, as the lane also found). Tested on the
function, not one value, at t ∈ {2, 3, 0.6, 1.7} and two unit-circle points, tolerance 10⁻²⁵:
- **T1** conj R(t) = ±R(t) at real t — real up to a unit (all coefficients real, or all purely imaginary: the second case
  the lane's |Im|/|v| test labels CPLX);
- **T2** R(1/t) = ±t^k R(t) — duality;
- **T3** conj R(t) = ±t^k R(1/t) — the symmetry step alone.
And the geometry per member: every self-isometry from `isomorphisms_to` with its cusp map's determinant (−1 =
orientation-reversing) and its sign s(f) = ±1 on φ read from the peripheral curves — so **amphichirality is decided by
the isometries, not by `is_amphicheiral()` alone**, and the theorem's two steps are checked separately:
amphichiral ⟹ conj R(t) ≐ R(t^{s(f)}); duality ⟹ R(1/t) ≐ R(t); together ⟹ T1. Even n is the clean case (no lift
sign); odd n is reported with the lift's ℤ/2 named. One control of presentation-independence: three members
retriangulated (`randomize`) must give the same R up to ±t^k.

## 2. Predictions, with priors

| | prediction | prior |
|---|---|---|
| P1 | T2 (duality) holds at even n on every member with H₁ of rank 1 | 90% |
| P2 | T1 holds at even n on every member that has an orientation-reversing self-isometry: **the cancellation is a theorem of amphichirality**, not an artefact of m004 | 75% |
| P3 | the lane's five (m206, m207, s957, s960, s961) are the discriminating case: each either has no orientation-reversing isometry (the column wrong, the E51/B1235 kind), or fails T2, or is purely imaginary (T1 holds with phase i and the lane's test mislabelled it) | 70% |
| P4 | on chiral members T1 fails for most but not all (the lane's "8/8, no exception" is a small sample; the converse direction is empirical, not a theorem) | 60% |
| P5 | the odd-n pattern (real at even only on some amphichiral members) is the lift's ℤ/2: on those members the reversing isometry's sign character does not factor through φ | 60% |

**What a failure would mean.** P2 false with P1 true: the symmetry step fails on an amphichiral member — the
holonomy is not conjugated to its complex conjugate by the isometry, which would contradict Mostow–Prasad and so would
mean an instrument error (to be found before any verdict). P2 false with P1 false: duality fails for members with
H₁ torsion or with φ vanishing on the cusp — then the lane's "artefact" reading is right and the theorem is only for
knot-like members. P3 false (the five are amphichiral by isometry, satisfy T2, and are genuinely complex): the theorem
argument is wrong somewhere and the arc says where.

## 3. Disclosed

Computed before the seal: m004 at n = 1..4 (the control, above). Not computed: any other member. The lane's table
is known (read at the pin): 16 usable of 21, 8 chiral all complex, 8 amphichiral split 1/2/5. B1235's amphichirality
column (38 of 112) is known. The theorem argument of §1 was written before any member other than m004 was run; it is
the reason P2 is at 75% against the lane's data.

## 4. Scope

Frame F-CI (invariants of the geometric representation); object the 112-family (B1186), level one; reach *family*
for the census and *general* for the theorem if P1–P2 hold (the argument uses nothing of ℚ(√−3)). Nothing here is a
count on a vacuum or an SM quantity: the question is whether a banked sentence of B425 generalises, and whether the
lane's correction of it is itself correct.
