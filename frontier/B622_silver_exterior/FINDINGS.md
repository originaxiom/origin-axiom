# B622 — the TRUE m136 (silver RRLL) exterior adjoint torsion: −16 exactly; the sign law's second exterior data point; the field crossover

**Status: banked (frontier). Cell C of the campaign (Tran–Yamaguchi
route, arXiv:2109.07058), verified in-loop via the exact eigenvalue
identity. Reproducers `compute_m136_torsion.py`, `ty_core.py` (agent's
code, copied). Companion: cell B's convention reconciliation.**

## The result (verified exactly in-loop)

The census manifold m136 = the RRLL silver bundle (monodromy [[5,2],[2,1]],
trace 6; SnapPy isometry-verified — this run also exposed and corrected
the naming error propagating from chat-1's handoff, see B621). Its
EXTERIOR adjoint Reidemeister torsion at the discrete rep, by the
Tran–Yamaguchi once-punctured-torus-bundle formula (pipeline calibrated
on the fig-8 → −3 = the banked B581 value):

> **T(m136, adjoint) = −16 exactly** — the character-variety tangent
> monodromy has eigenvalues {1 (omitted), φ⁶, φ⁻⁶} and
> (1−φ⁶)(1−φ⁻⁶) = 2 − (φ⁶+φ⁻⁶) = 2 − 18 = −16 (in-loop exact check).

- **The exterior sign law's second data point: NEGATIVE at m = 1,
  matching the fig-8's τ₁ = −3 < 0.** The exterior sign question
  (B617's sharpened residual) now reads: two objects agree at the
  adjoint level; the full six-exponent exterior family is the next
  round.
- **The field crossover (new, flagged):** the fig-8's adjoint tangent
  eigenvalue satisfies μ + 1/μ = 5 (μ = (5+√21)/2 ∈ ℚ(√21) — the
  trace-5 world!) while the silver bundle's is φ⁶ ∈ ℚ(√5) — the golden
  world. The two objects' adjoint Jacobians SWAP fields. Recorded as
  data (mechanism unknown; note 5 = tr² − 4 of the fig-8 and
  18 = φ⁶+φ⁻⁶ = L₆·... the Lucas number face).
- The torsion is RATIONAL (−16 = −2⁴) despite m136's degree-4 trace
  field — the irrationality cancels, as it does for the fig-8 (−3).

## Cell B's convention reconciliation (companion, verified)

B423's −5 vs B581's −3: different invariants (the closed bundle's
reduced determinant vs the cusped exterior's adjoint torsion) — a
category difference, already correctly diagnosed in the repo. B581's −3
vs Dubois's published 1/5: the SAME invariant in two H¹(∂M)-basis
conventions (meridian-based derivative vs Dubois's normalization); the
sign/normalization chain verified in-sandbox except one OCR-garbled
intermediate in the fetched Dubois text, honestly flagged unresolved
rather than forced.
