# W133 — the web seat's PF1-W, its reading of GENESIS PF1, on the Higgs: which weight-3/2 Higgs sections keep the families' joint coupling free of zeros inside the weave? (the rule, committed before the script)

The SM-derivation seat, 2026-10-22. Committed and pushed before the script that reads it exists. Nothing here is a
result.

## Why

- **The web seat's PF1-W,** its reading of GENESIS PF1, was registered by the owner as a reading on 2026-10-22. It
  says the law's holomorphic invariants have their zeros and poles only at the end.
- **Relay §217 asked** which weight-3/2 Higgs sections it admits. The owner asked this seat to take it without waiting
  (2026-10-22).
- **A note in W127** found η⁴R admissible and named the unit's space as open.

## The objects

- **The Higgs at weight 3/2.** A section F of T ⊗ ε_r with n uniform units: W127's space h(r, n), computed by its
  exact route, F = η^r·g.
- **The parity basis** (e_i, e_j, e_k), where ρ is monomial (ζ₈^k times a signed permutation; W126, W128), and
  F = (F_i, F_j, F_k).
  - From W127's line series: F_i = ℓ_{1/8}, F_j = (ℓ_{3/8} + ℓ_{7/8})/2 and F_k = i(ℓ_{3/8} − ℓ_{7/8})/2.
  - On R these are its components (−θ₂², −θ₄², iθ₃²)/(θ₂θ₃θ₄).
- **The families' joint coupling.** If each family couples through its own parity component (Y = diag F), then
  det Y = N(F) = F_i·F_j·F_k.
  - Because ρ is monomial, N(F) is a scalar form of weight 9/2. Its character is det ρ times the sign of the moves'
    permutation of the three parities: ε₁₂·χ_η^{9+3r} = χ_η^{21+3r}.
  - PF1-W, the web seat's reading of GENESIS PF1, asks that N(F) have no zero on the upper half plane.
- **Main's frame, for comparison.** There Y(a) = aRᵀ + Raᵀ − (a·R)𝟙 (B1645), and det Y(a) = (a·R)(a·a)(R·R). This
  vanishes identically because R·R = 0 (Jacobi's identity). So PF1-W read on that frame's determinant excludes it
  everywhere.

## Weave or thread

**WEAVE-type.** The weave's own surface, every allowed twist, end data n ∈ {0, 1}, the moves' joint representation,
and claims about all sections at once.

## The cells, with predictions and priors

| cell | prediction | prior |
| --- | --- | --- |
| P0 | the instrument (exact series in x = q^{1/8}): the line-to-parity change gives R's components exactly; N(R) = i/(θ₂θ₃θ₄) = (i/2)η⁻³ and N(η⁴R) = (i/2)η⁹ to x⁶⁰. Main's det Y(a) = (a·R)(a·a)(R·R) is an identity in a, and R·R = 0 to x⁶⁰ | 95% |
| P1 | the obstruction. A weakly holomorphic form of weight 9/2 with no zero on the upper half plane and poles only at the cusp is cη⁹: its quotient by η⁹ is a zero-free modular function up to a finite character, so it is constant. So N(F) can be zero-free only if χ_η^{21+3r} = χ_η⁹, i.e. r ≡ 4 (mod 8). Checks: det ρ·sgn on S and T equals χ_η²¹ exactly. N's x-exponents lie in 7 mod 8 for every section, while η^{9−3r}'s lie in 3 − r mod 8, which is 7 iff r ≡ 4 (mod 8). So the untwisted field has no Higgs admissible under PF1-W (GENESIS PF1 as the web seat reads it) at any n, the unit's three-dimensional space with ∂R included | 95% |
| P2 | the admissible sections (exact, Gröbner basis over ℚ). For r ∈ {4, 12, 20} and n ∈ {0, 1}, solve N(F) = c·η⁹ with c ≠ 0 over h(r, n): the cubic system N′(g) = η^{9−3r}, where N′ = ℓ_{1/8}(ℓ_{3/8}² − ℓ_{7/8}²) and c is absorbed. Predicted: the solutions are exactly the multiples of η⁴R, three points (cube roots of 1) in each of h(4, 0) and h(4, 1); none in h(12, 1) or h(20, 1) (h(12, 0) = h(20, 0) = 0) | 70% |
| P3 | the read-out: the admissible sections; their chiral counts (W127: η⁴R at the empty end carries one generation); and the fork with the unit route | — |

## What the outcomes mean (fixed now)

- **P0 to P2 hold.** Then PF1-W (the web seat's reading of GENESIS PF1), read on the families' joint coupling,
  admits exactly one Higgs: η⁴R, the twisted empty-end field, carrying one generation.
  - It excludes the whole Higgs space of the record's three-generation route: the unit with ∂R (W123, B1700, main's
    C8). It also excludes main's frame (det ≡ 0).
  - So PF1-W and the unit route are incompatible on this reading. The fork for the owner has three branches:
    - PF1-W is not read on the Higgs's components;
    - the families' couplings are not diagonal in the parity basis;
    - the three is not carried by the unit.
  - It is named, not resolved.
- **P2 finds admissible sections beyond η⁴R** (in h(12, 1) or h(20, 1), where the count is three). Then PF1-W selects
  a three-generation Higgs. That would be the positive this seat does not expect, and it is recorded as found.
- **P1 fails.** The character arithmetic is wrong, and nothing in P2 is read until it is resolved post hoc.

## What stays out

- End data n ≥ 2; per-line end data.
- Couplings not diagonal in the parity basis, except main's frame as stated.
- The mirror hand's weight-½ sections.

## Seen before the rule (disclosed)

- **Read:** the web seat's THE_ZERO_FREE_READING.md and its PF1-W ruling (a reading of GENESIS PF1); W123; W127, with
  its dated PF1-W note; B1645 and B1700.
- **By hand:**
  - N(R) and N(η⁴R) from θ₂θ₃θ₄ = 2η³;
  - the character det ρ·sgn = χ_η²¹ on S and T;
  - the x-exponent classes;
  - det Y(a) = (a·R)(a·a)(R·R).
- **Not run:** no Gröbner basis and no section in h(12, 1) or h(20, 1) has been computed.

## Discipline

- This rule is committed and pushed before the script exists.
- One run; its output is committed before it is read.
- A failed launch is disclosed, with its log kept. Any failed prediction is recorded as failed, and any later check is
  labelled post hoc.

0 of 19.
