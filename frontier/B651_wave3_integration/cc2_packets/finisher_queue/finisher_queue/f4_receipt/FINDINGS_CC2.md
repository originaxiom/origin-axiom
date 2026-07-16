# F4 — BANKED: B649 STAGES 2a/2b/3a/3b-i ALL VERIFIED ON RECEIPT (track-S lane;
# cc2 + subagents + main-seat completion, 2026-07-16)

Hash audit 20/20; lock tests 6/6 (test_b649_silver.py x4 + test_b650_types.py x2,
the latter confirmed not gating b649). Per-stage:
- 2a/2b (silver holonomy + the 27-letters exact over L): VERIFIED — own-code fresh
  polished holonomy at 800/400 bits (cross-precision 6.5e-121), independent pslq
  identification reproduces entries_L.json; sympy QQ.algebraic_field (independent
  backend) confirms dets = 1, relators = I, all five trace relations exact; the
  27x27 relators re-confirmed = I exactly via an own Fraction-vector class.
- 3a (THE 3/5/1 DIMENSION GRAMMAR on the silver): VERIFIED — solo dims (h0 = 1,
  h1 = 3) independently recomputed with fresh quotient-ring + own Gaussian
  elimination + own Fox rows; double dims (h0 = 1, h1 = 5) via hash-verified
  verbatim rerun matching the sealed output exactly.
- 3b-i (the silver swap + sharpened invariant): VERIFIED — verbatim rerun
  byte-identical to the sealed output except wall-clock stamps (stage3b_diff.txt:
  only two timing lines); G1 J^2 = +1, all five cocycle checks True, dim Z1 = 31,
  the 5x5 sigma*-matrix identical, C.conj(C) = I exact, C s-free (lives in Q(i)).

DEVIATION NOTES (honest, for cc's stage-4+): (1) the STALE-ARTIFACT-TEXT pattern
recurs — b649_stage2a.py's comment block claims "PROJECTIVE-EXACT / det nontrivial"
while its own printed output shows det = 1 exact (same class as stage 1's stale
pslq line; FINDINGS.md itself accurate; recommend a pre-seal grep for stale prose
as house practice). (2) Stage 1's promised primitive-element minimal polynomial was
quietly rescoped in PREREG_STAGE2A.md to product-basis Q(s, i) identification —
mathematically fine, but the substitution deserves a one-line reconciling note.
No recurrence of "output claims an unexecuted method."

THE SIGNIFICANCE FOR GATE B: the 3/5/1 grammar row and the swap structure now
REPRODUCE on the second object with independent verification — the first FORCED
rows to clear the silver control with the verify column filled.
Artifacts: hash_audit.py, verify_stage2.py, verify_stage3_numeric.py,
verify_stage3_solo_exact.py, *_results.json, stage3b_verbatim_rerun.log,
stage3b_diff.txt, b649_copy/. Repo untouched.
