# N4 — BANKED: B643/B644/B645 all VERIFIED on receipt (a cc2 subagent + main-seat
# bank; 2026-07-16). Lock tally 13/13 PASS (pytest outside-repo, no cache/bytecode).

B643 (flip-symmetry verdict): VERIFIED. Verbatim rerun reproduces b643_output.txt
byte-for-byte (both families: 172 rows, sol dim 1, d=(0,0,1), invertible False,
b-conjugator ('aBAb',1,-1)). INDEPENDENT path: 27-dim local system rebuilt from
b637_threeform.py; the a-family 172x3 off-diagonal system done in exact sympy over
Q(sqrt-3) (different code path than the arc's hand-rolled Fraction elimination):
rank 2, nullspace dim 1, null vector EXACTLY (0,0,1). (A float64 SVD side-check was
inconclusive — conditioning artifact of this arc's dynamic range; noted, not a
contradiction; the exact result stands.)

B644 (congruence-shadow/McKay): VERIFIED. Independent rebuild via cc2's own
engine_v7 SU(3)_2 construction (structurally different from B644's B629 import):
360-element image, 120-element ker(det), all 9 class traces to full precision;
elementwise vs the corrected golden table: 120/120. The prereg's two disclosed
inconsistent candidate tables score 96/120 and 72/120 — independently CORROBORATING
their own M3 sealing-error adjudication. M4 pentagon: tr rho_hear(RL) = -1/phi exact.

B645 (unit cross-ratio + 13-dial): VERIFIED. Pure-Fraction + hand-rolled Q(sqrt-3)
recompute from byte-checked raw values: unbent weld cross-ratio = 1 exact;
D_bent(m=1): inv1 = 3709/3696 = 1 + 13/3696; inv2 = 1 + 13(6613 + 13 sqrt-3)/21866138
— both match the banked normal forms exactly; deviations divisible by 13 as claimed.

REPRODUCIBILITY FLAGS (house-style, honest, for cc):
- B645 has NO PREREGISTRATION.md / ARTIFACT_HASHES.txt (B643 has both sealed+locked;
  B644 has both but unlocked).
- B644's prereg/script hashes are asserted in FINDINGS prose only, not test-locked;
  agent verified them to match exactly today — nothing catches future drift.

Read-only compliance: git status --porcelain empty before/after.
Scripts: n4_receipt/verify_b64{3,4,5}_independent.py + runs/.
