# B629 — FINDINGS: the interaction-layer value bank (the interaction round, part 1 of 3)

**Date: 2026-07-15. Status: BANKED (values sealed; hash in
frontier/B598_l85_campaign/ARTIFACT_HASHES.txt). Scope: values only —
NO comparison of any kind happens in this arc. The one authorized
comparison (the 3×3 hearing form vs the measured mixing-moduli table)
runs under B630's separately sealed design in B631.**

## Why this arc exists

The Branch-3 nulls (B615/B616/B627/B628) tested single-layer object
invariants. The program's own three-layer result (B611/B613: spectrum =
chirality, trace = field, matrix elements = listener coupling) locates
value content in the INTERACTION layer — which had never been extracted
as matrices. The interaction-round directive (chat-1 + the owner,
2026-07-15) authorized exactly one new comparison on held-out
interaction-layer data and deferred everything else. This arc computes
and seals the interaction-layer values; the directive's discipline
(one comparison; no re-testing; no composite curve-fitting) is binding.

## The four cells (all values-only, independently computed)

### 1. The E₆₂ 3×3 odd hearing form has an exact closed form (NEW)

B594's matrix B, rebuilt at 100-digit precision with exact integer
W(E₆) data: **B is exactly unitary**, eigenvalues exactly {i, −i, −1}
(B⁴ = I), trace −1, and every entry is B_ij = A_k(i,j)·ζ₁₄^m(i,j) with
A_k = (2/√7)sin(2πk/7) — the A-indices forming the 3×3 Latin square
[[1,2,3],[2,3,1],[3,1,2]]. Consequences:

- |B_ij|² is EXACTLY the circulant of (A₁², A₂², A₃²) — doubly
  stochastic (rows/cols sum to 1 exactly), the same mathematical class
  as a measured mixing-moduli table. This is the framework side of the
  authorized comparison, sealed in SEALED_INTERACTION_VALUES.md §1.
- The whole matrix lives in ℚ(ζ₁₄, √7) ⊂ ℚ(ζ₂₈), the diagonal
  amplitudes' known field.
- The eigenframe is basis-canonical (non-degenerate spectrum); the SVD
  frame is an algorithm ARTIFACT (all singular values = 1 identically) —
  recorded so nobody reads structure into it later.
- Held-out accounting disclosed at sealing: the three moduli² are
  B615's A3–A5 scalars; the held-out content is the ARRANGEMENT and the
  matrix-to-matrix geometry, not nine virgin numbers.

### 2. The golden frame angle is arctan(1/φ) exactly (NEW), and κ=10 is 16×16, not 8×8

B601's B_odd(κ=5) in closed form, off-diagonals never before published
(∓φ/2 − i·sin(π/5)/√5); exactly unitary, det 1, trace 1/φ. The
eigenvector mixing angle: **tan θ_frame = 1/φ exactly**
(θ_frame = 31.7174744…°), with |V₁₁|² = (5+√5)/10, |V₂₁|² = (5−√5)/10.

**The structural identity |V₂₁|² = |h₃|²** — the frame's mixing weight
equals the hearing amplitude's modulus² — means the frame angle adds no
new comparable scalar (that number was already tested, null, as B615's
A1); it is sealed as structure, excluded from comparison on that stated
ground.

The premise correction: at κ=10 the odd form is 16×16 (dim_odd sequence
2,4,6,9,12,16,20,…; 8 never occurs). It is also exactly unitary, obeys
the trace law (trace = 1/φ), has all-unimodular clockwork spectrum
(8 conjugate pairs, arguments multiples of 6°), and contains the κ=5
golden pair e^{±2πi/5} as a genuine 2-dim eigenspace DELOCALIZED over
10 of 16 pair-directions with golden-rational weights — the naive 2×2
submatrix on the κ=5 directions is not golden (B601's banked defect,
now quantified).

### 3. The composite inventory is sealed and frozen (NOT-FOR-COMPARISON)

~40 exact Rosetta-weighted values (§3 of the seal). Deferred per the
directive's point 3: comparing compositions requires a structural
derivation of which composition ↔ which observable, stated BEFORE any
distance; freezing the values now removes tuning freedom from any such
future design.

### 4. The object-scale coupling targets are sealed and frozen (NOT-FOR-COMPARISON)

Measured PDG-2024 couplings run by pure-SM RGEs (1-loop closed form
verified in-loop; 2-loop gauge-only) to Λ_A = |τ₈|/|τ₄|·GeV ≈ 3.86e14,
Λ_B ≈ 3.52e16, μ_ref = 1e16 GeV (§4 of the seal). Deferred per the
directive's point 2: running measured couplings to a new scale and
re-comparing is re-testing; it needs its own preregistration with the
principled scale argument first. The targets are frozen now so a future
design cannot move them.

## In-loop verification (main seat, independent of the cells)

`tests/test_b629_interaction_values.py` recomputes, from the closed
forms alone (sympy exact + mpmath): B's unitarity/trace/charpoly and
diagonal identification; the |B|² row values; B_odd's
unitarity/det/trace/eigenvalues; the θ_frame and (5±√5)/10 identities;
the |V₂₁|² = |h₃|² identity; cell L spot products; and cell M's 1-loop
closed-form runnings (max dev < 5e-6 vs the sealed table). The sealed
file's SHA-256 is locked against the hash ledger.

## What this arc does NOT do

No distances, no measured mixing values anywhere in this arc, no
verdicts. The design (B630) and the run (B631) are separate arcs so the
hash order is auditable: values first, design second, run third.
