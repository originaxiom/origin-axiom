# B796 WAVE-1 FINDINGS (interim; prereg sealed 8424a335 before compute)

cc3 audit seat, 2026-07-29. Owner greenlight; executed independently;
cc = merge gate. Gate 5-Q. Nothing to CLAIMS.

## CELL 3 — SPIN FORK: EXECUTED (exact, sympy)

Setup verified: exactly two SL(2,C) lifts (mixed sign assignments
FAIL the relator, consistent with H¹(m004;Z/2) = Z/2): ρ₁ = (A, B)
(the banked Riley lift), ρ₂ = (−A, −B).

Exact peripheral trace patterns (meridian a; longitude bABaaBAb,
parabolic, c-entry 0 in both lifts):

    ρ₁: (tr m̃, tr l̃) = (+2, −2)
    ρ₂: (tr m̃, tr l̃) = (−2, −2)

VERDICT (per the sealed fork):
- **Convention-independent half: ρ₁ (the Riley lift) is NON-Lie under
  BOTH sign dictionaries ⇒ its Dirac spectrum is DISCRETE ⇒ the
  Dirac–Hejhal follow-up is AUTHORIZED unconditionally.**
- Convention-dependent half: under C1 (tr = −2 ⟺ trivial along the
  curve) ρ₂ is the Lie structure ⇒ essential spectrum ℝ ⇒ the
  fermionic spectral-action family CLOSES for ρ₂; under C2 neither
  lift is Lie. Resolving C1-vs-C2 is ONE named literature lookup
  (Bär's sign dictionary) — flagged, not assumed.
- Cross-check: the two structures are distinguished by cusp data;
  consistent with P52 (τ fixes both spin structures — τ acts on each,
  neither is exchanged).

Artifacts: cell3_spin_fork.py / .txt.

## CELL 2 — DOUBLET SURGERY, STAGE 0: GATE FAILED ⇒ ABORT (as designed)

The validation gate ran on three certified mult-1 newforms
(r = 4.900085373, 5.912917882, 7.406615600) with the correct O₃-dual
embedding (O₃^∨ = d1·O₃, d1 = 1 + i/√3; module map ν = p + qω ↦
integer coords (p−q, 2p+2q) in Λ*; base points resolve at machine
distance 0). Result:

    raw λ_π7 ≈ 0 on both testable forms (the coefficient at the
    O₃^∨-point of π₇ VANISHES to instrument precision);
    T1 eigen-relations: rel dev ~1 for all α ∈ {−1, 0, 1};
    T2 multiplicativity (7 = π·π̄): rel dev ~1;
    μ₆-averaged variant: c(1)-average near-cancels (expected — Γ₄₁'s
    cusp stabilizer has no unit rotations; the average is not
    justified for newforms and behaves accordingly).

**BANKED FACT (re-scoped per chat1's relay, 2026-07-29): the NAIVE
Bianchi–Hecke construction fails on Γ₄₁ mult-1 newforms at level (4),
with a STRUCTURED residual at split primes; the lift/CM reading is
UNTESTED.** Not banked: "Hecke fails for Γ₄₁" — that stronger reading
is unearned. Scoping facts:
- The gate ran on MULT-1 FORMS ONLY (r = 4.900085373, 5.912917882,
  7.406615600), per the sealed prereg — chat1's mult-2
  precondition concern (arbitrary basis of a 2-plane is not a Hecke
  eigenvector; Rayleigh ≈ 0 for generic vectors on a trace-0 plane)
  does NOT apply to this run. It WILL apply to Stage 1, where
  simultaneous diagonalization on each 2-plane is the required
  method, not a per-vector test.
- TWO signatures, separated per chat1: (i) λ_π₇ ≈ 0 raw on the forms
  r = 4.900 and 7.407 — a STRUCTURED ZERO at a split prime
  (7 ≡ 1 mod 3), classically the fingerprint of CM forms or
  base-change LIFTS; (ii) diffuse order-1 deviations in all relation
  families — the signature of a wrong double-coset construction.
  Also (iii): on r = 5.913 the coefficient c(1) at the d1-point
  near-vanishes (support pattern, distinct from (i)). Different
  causes possible; no single explanation is banked.
- NEW SOURCE (chat1, provenance hunt; NOT yet in-repo — verify
  before citing in any write-up): **Steil 1999, "Eigenvalues of the
  Laplacian for Bianchi Groups", IMA vol. 109, Springer, 617–641** —
  covers D = 1, 2, 3, 7, 11, 19; proves the spectra are NOT simple;
  states some eigenvalues are LIFTS from PSL(2,Z). Lifted forms
  satisfy BASE-CHANGE relations, not naive Bianchi–Hecke — if some
  of the 17 are lifts, the abort is the correct outcome of the WRONG
  construction, not evidence against Hecke theory.
- THEORY-FIRST NEXT TEST (chat1's discipline, adopted): get the
  base-change archimedean normalization from the literature, derive
  ONE prediction, test that (DOF ≥ 1 or it is not a test). chat1's
  own numerical lift-matching (3 hits at 0.07–0.17% across 4
  normalizations × 10 sources × 17 targets) was base-rated by chat1
  itself to P(≥3) = 0.14 — NOT usable, and not used.
Stage 1 remains BLOCKED pending: (a) the Steil read, (b) the correct
level-(4)/base-change operator, (c) simultaneous diagonalization
methodology for the 2-planes.

Instrument note (E31 discipline, on the record): the gate's own
construction caught two embedding errors before producing a trustable
verdict — (i) O₃^∨ ≠ (i/√3)·O₃; (ii) the module map is complex
multiplication by d1, not the additive dual-basis map. Both fixed
with exact integer coordinates; base-point lookups then resolve at
distance 0. The failures above are therefore statements about the
RELATIONS, not the lookup.

## CELL 1 — GH LADDER: SCAN DONE, PRIORITY REFINEMENTS IN

scanE (r ∈ (10, 13.5), dr = 0.002): **27 dips, no exceptional
eigenvalues.** The three pre-stated GH rungs all have dips at the
predicted positions. Priority refinements (GH-first):

    GH rung #2 (pred. 12.5016): r = 12.50010017, λ = 157.252504,
      S-dev = 5.7e−10 → **OLD (PARENT), STABLE — CONFIRMED**
    GH rung #3 (pred. 13.2960): r = 13.29316271, λ = 177.708175,
      S-dev = 8.9e−9 → **OLD (PARENT), STABLE — CONFIRMED**
    GH rung #1 (pred. 11.0086): UNRESOLVED — the 11.008 dip sits in
      a cluster (double at 10.9960 adjacent); the ±6e−3 golden
      bracket straddled neighbors (|dr| = 4e−3, σ ~ 1e−4, wandered
      to 11.002). Full refinement separates the cluster.

Consequence: **two of the three GH transcription values
(12.5016, 13.2960) are now computationally retro-corroborated as
parent eigenvalues** — the same pattern as 51.014 (targeted
confirmation; the solver was never tuned to them; the falsifier did
not fire against GH on these rungs). 122.19 (rung #1) remains
uncorroborated pending the cluster resolution. Full 27-dip
refinement + parity census in flight; the parity census additionally
requires the J-normalization check (does z ↦ −z̄ normalize Γ₄₁) —
part of the cell, not assumed.

## CELL 9 LADDER — rung (i) status

Feasibility ANSWERED (cell9_feasibility_probe): reachable; arb
installed. Rung (i) (25-digit) prereg with its (d, H) power box is
the next seal after Wave 1 lands.
