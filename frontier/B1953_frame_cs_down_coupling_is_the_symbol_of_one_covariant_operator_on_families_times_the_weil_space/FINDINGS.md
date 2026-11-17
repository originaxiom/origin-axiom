# B1953 — Frame C's down coupling is the symbol of one covariant operator on families times the Weil space; it splits 3 + 2 under the centre; its hypercharge component is a covariant sum over the 24 points; the up sector is obstructed at level 5

**Verdict: PROVED** (identities checked to 1e-13 or better at two base points and their images under T and S, in both
Higgs readings; the phases are exact fifth roots; data-free). Main, 2026-11-17. It tests hypothesis C1 of P-866, at
the author's word. No measured number is used and nothing is compared. **0 of 19.**

## Seen first

- **Swept:** `VERDICT topic-sweep /Weyl symbol|displacement operator|Parseval|Plancherel|phase table|coboundary|amplitude sum|amplitude read-out|flat connection over the 24/: 10 of 1694 arcs on main match (NEGATIVE 2, OPEN 1, PROVED 7); 1 register rows match (QUEUED 1)`.
- **What the record already holds:**
  - **B1945 § 6** (corrected on agy-002's A2-AMP): the coupling's transformation law over the 24 points, tested in
    three consequences; the left Gramian covariant; the plain sum repairable by phases for down, not for up at level 5.
  - **B1951, B1952:** level 5's Weil space, its centre's split 3 + 2, hypercharge as the commutant's traceless
    element, and the record's lines as its Weyl operators.
  - **B1949:** at order 5 the lepton coupling is the down coupling at another point.
- **What is new:** the law tested point by point under both generators, with its phases in closed form; one phase
  table that turns the 24 pointwise couplings into a single covariant operator; that operator's split under the
  centre; two new covariant family Gramians; and the phased sum's covariance under S as well as T.
- **The literature:** the finite Weyl transform and its Parseval identity, the parity as the phase-point operator at
  the origin, and the Clifford action of the Weil representation on displacement operators in odd dimension
  (standard; Wootters 1987, Gross 2006). Nothing here is new as mathematics of the Weil space.

## 1. Exact facts on the Weil space (`verification/exact_facts.py`)

W is ℂ⁵, X the shift, Z the clock, ζ = e^(2πi/5), and D(a, b) = ζ^(ab/2) X^a Z^b for the 24 points (a, b) ≠ 0.

| fact | check |
|---|---|
| in frame C a field's twist at order 5 is fixed by its degree k in the exterior algebra: 6Y ≡ 3k mod 5 (Q, u, e: 1; d, L: 2; H: 3) | exact |
| the 24 operators D(v) are an orthonormal traceless basis of sl(5); the parity P sends D(v) to D(−v); the 12 even combinations commute with P, and 12 = 8 + 3 + 1 | 6e-16 |
| tr(D(v)P) = 1 for every v, so **6Y = −½ Σ D(v) over the 24 points** | 7e-16 |
| B1951's Weil representation moves them with no phases: ρ(T) D(a, b) ρ(T)⁻¹ = D(a, b − a) and ρ(S) D(a, b) ρ(S)⁻¹ = D(−b, a) | 6e-16 |

So the record's 24 points label the 24 directions of sl(5); the 12 points up to sign label the directions the centre
keeps, which are the Standard Model's; and hypercharge is the equal-weight sum of all 24.

## 2. The law, point by point (`verification/weyl_operator.py`)

At τ₀ = 0.13 + 1.7i and at 0.31 + 1.2i, with the end at −1/τ carried by its own law (B1927; P-864):

**Y(γτ, w) = c · φ(γ, w) · U_L · Y(τ, wγ) · U_R†**, for γ = T and γ = S.

| | down, T | down, S | up, T | up, S |
|---|---|---|---|---|
| the law at all 24 points | 1e-15 | 1e-15 | 1e-15 | 2e-15 |
| U_L and U_R, the same at every point, fixed up to a phase | yes | yes | yes | yes |
| the modulus c, one for all points | 1 | ∣τ∣ | 1 | ∣τ∣ |
| the phases φ | **ζ^(−a²)** | **ζ^(2ab)** | of order 25 | of order 25 |

- The unitaries are found from the pointwise Gramians, and the law is then checked on the couplings themselves.
- For the down sector the phases are fifth roots in closed form, exact to 2e-16 of a turn, in both readings.
- For the up sector they are 25th roots and depend on the representative of the point: agy-002's level-25
  obstruction, seen point by point.
- Y(τ, −w) = Y(τ, w) exactly.

## 3. The operator

**O(τ) = Σ over the 24 points of ζ^(−ab) · Y(τ, w) ⊗ D(w)**, a 15 × 15 matrix on (families) ⊗ W.

| test, down sector, both readings, both base points | result |
|---|---|
| **O(γτ) = c · (U_L ⊗ ρ(γ)) · O(τ) · (U_R ⊗ ρ(γ))†**, with B1951's Weil representation ρ, for T and S | 1e-15 |
| its 15 singular values at τ + 1 and at −1/τ against τ | at most 2e-13 |
| the same without the phase table (a control) | 0.4 to 1.5 |
| **its part mixing W's 3 and W's 2** | 2e-16: O = O₃ ⊕ O₂ |
| the family Gramian with W traced over the 3, and over the 2: their ratios at τ + 1 and −1/τ | at most 3e-14 |
| Parseval: the two Gramians together are 5 times the plain Gramian over the 24 points | 2e-15 |
| **the sum over the 24 points with the phase table**, Σ ζ^(−ab) Y(τ, w): its ratios at τ + 1 and −1/τ | at most 7e-14 |
| the plain sum (a control) | 0.09 to 3.5 |
| the up sector | the operator's singular values move by 0.4 to 5 and its law fails (0.8 to 1); its mixing part is 0.53; the two Gramians move by 0.004 to 0.16; the phased sum by 0.6 to 3.3 |

- **The phase table is forced.** Any table that works must absorb the phases of § 2 under both generators. The modular
  group moves the 24 points transitively, so the table is unique up to one constant, given that it is even like Y.
- **Scaling the labels** (D(cw) for c = 2, 3, 4) gives covariant operators too, with the same two Gramians. So the two
  Weil classes are not told apart by these read-outs.
- **The phased sum is the operator's component along hypercharge:** tr_W(O · 6Y) = −(5/2) Σ ζ^(−ab) Y(τ, w). It is
  also the trace of O₃, and minus the trace of O₂.

## 4. The frame's outputs at the two base points (printed, not compared)

Ratios σ₂/σ₁ and σ₃/σ₁ (for Gramians, of the square roots of the eigenvalues), down sector:

| object | 0.13 + 1.7i, S | 0.13 + 1.7i, S̃ | 0.31 + 1.2i, S | 0.31 + 1.2i, S̃ |
|---|---|---|---|---|
| the Gramian over the 3 | 0.6375, 0.1471 | 0.6160, 0.1492 | 0.7029, 0.5227 | 0.6845, 0.5073 |
| the Gramian over the 2 | 0.9275, 0.0718 | 0.8696, 0.0691 | 0.8967, 0.1739 | 0.8917, 0.1716 |
| the plain Gramian (B1945 § 6) | 0.7255, 0.1514 | 0.6788, 0.1507 | 0.7764, 0.5432 | 0.7554, 0.5248 |
| the phased sum | 0.0787, 0.00046 | 0.2582, 0.0215 | 0.4020, 0.0022 | 0.6973, 0.0269 |

- The two Gramians differ from each other at both points, in both readings.
- The phased sum has a small third ratio at both bulk points. The pointwise ratios and the Gramians do not.
- **Foreknowledge, disclosed.** Main knows the rough sizes of the measured ratios. The first base point is the
  record's test point, used since B1945; the second was fixed before its run as one further generic point. No point
  was scanned and none was chosen by its output. These four columns are not a look, and none may be compared with data
  without a sealed rule.

## What it means

- **The dictionary is tied to the frame's couplings.** The web seat's W-A1 named this as a way its attack could fail:
  that postulate D could not be tied to the frame's own couplings. For the down sector it can: the coupling at the
  point w is the coefficient of the direction D(w), and the whole transforms by B1951's Weil representation on W.
- **The choice among the 24 points is not needed for the down sector.** Three family objects are covariant under the
  whole modular group and use all 24 points with no weights chosen: the Gramian over the 3, the Gramian over the 2,
  and the phased sum. What they still depend on is τ, the Higgs reading and the end.
- **The split 3 + 2 reaches the couplings.** The operator commutes with the centre's parity, so it is a block on
  families ⊗ (the 3) plus a block on families ⊗ (the 2), with different family spectra.
- **The up sector is a specification.** Its phases are of order 25. A sum over points closes at level 5 when the
  right charge is ±2 times the left charge mod 5; down and leptons meet that, and up, with both fields in one degree
  of the exterior algebra, does not (P-866, C2).

## Not claimed

- Which physical sector, if any, each block is. That the 3 is the down quarks and the 2 the leptons is a hypothesis.
- That the phased sum or either Gramian is the read-out. Each is a covariant candidate; a read-out is a declared
  choice, to be sealed before any look.
- Anything for the up sector beyond its failure, or for the leptons beyond B1949's relation.
- The identities at points other than the two base points and their images. The phases are roots of unity, so the
  identities are expected to hold everywhere, but that is not proved here.
- Any comparison with data.
