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

**BANKED FACT (the gate's pre-registered purpose, G5): the naive
Bianchi–Hecke relations FAIL on Γ₄₁ newforms at level (4). No Hecke
claim runs. Stage 1 (doublet surgery in the mult-2 eigenspaces) is
BLOCKED pending a correct level-(4) double-coset operator
construction — a registered follow-up.** Structured residual worth
recording (residual-hint per METHOD.md): the vanishing of newform
coefficients at O₃^∨-points of split primes (λ_π7 ≈ 0 raw) is itself
a pattern — consistent with newforms being supported away from (part
of) the parent sublattice; the correct level-(4) theory should
explain it. Revisit only with the correct operator in hand.

Instrument note (E31 discipline, on the record): the gate's own
construction caught two embedding errors before producing a trustable
verdict — (i) O₃^∨ ≠ (i/√3)·O₃; (ii) the module map is complex
multiplication by d1, not the additive dual-basis map. Both fixed
with exact integer coordinates; base-point lookups then resolve at
distance 0. The failures above are therefore statements about the
RELATIONS, not the lookup.

## CELL 1 — GH LADDER: IN FLIGHT

scanE running: r ∈ (10, 13.5), dr = 0.002, Y = 0.75, 874 modes,
plus the λ < 1 sector re-scan. On landing: two-system refinement,
eigenspace projection (old/new), parity census per prereg.

## CELL 9 LADDER — rung (i) status

Feasibility ANSWERED (cell9_feasibility_probe): reachable; arb
installed. Rung (i) (25-digit) prereg with its (d, H) power box is
the next seal after Wave 1 lands.
