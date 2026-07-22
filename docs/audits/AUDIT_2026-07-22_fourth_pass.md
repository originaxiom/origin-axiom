# The fourth-pass audit (multiagent campaign, 2026-07-22) — record

Workflow wf_c75724df: 8 blind lens auditors → 2 adversarial skeptics per finding → fix
designs for survivors. 90 agents, 0 errors. Tally: 32 findings → 18 CONFIRMED / 14 dropped.

## Lock-bite lens (mutation testing, isolated worktree)
VERIFIED GENUINE (fired on verdict-bearing mutation, restored cleanly): test_b753_mixing
(3/5 sub-tests fired on the B00 mutation; the 2 non-firing ones don't depend on B00 —
correct), test_b100_literature_crosscheck, test_repo_gates (framing scan), 
test_sl4_factorization, test_b729_amplitude. FOUND VACUOUS: test_b711_two_z2's
amphichiral sub-test (never consulted CURVE; the third MB12-class lock in three days) —
REWIRED to derive from the curve and mutation-verified on its true dependency (the
y-coefficient; the constant-term invariance is genuine mathematics, not blindness).

## The other confirmed findings and their dispositions
- B756 raw log carried banned model tokens INSIDE the attribution-gate exemption →
  REDACTED with a reconstruction record; the exemption REMOVED (standing pattern change:
  redaction-with-record supersedes exemption — gates stay sighted).
- Gate 5-Q was binding but absent from the mandated read path → WORKING_RULES rule 6a.
- C17's 24-parameters sub-claim uncited → B736 citation added.
- B754 lacked its dedicated ledger entry (rule 10) → retro-entry.
- The B753 seal row predated its addenda → append-only scope note.
- TOMB-L30's seat path: already fixed at #1273 (the audit ran concurrently) — confirmed.
- REPRODUCIBILITY: test-count refreshed (~2736); the OA_SLOW invisible-skip tier and the
  sympy deprecation/pin documented.
- Deferred with a registered review item (R28-9): the 122-file home-dir-path topology sweep
  over non-sealed tracked text artifacts (sealed outputs stay; the paths are low-harm but
  the sweep is due).

## Dropped by skeptics (14) — the informative ones
The assumption-audit's attacks on the two-seat independence claims (B754/B756/B749) were
refuted (grounds: the gate re-executions exist and diverge-zero; DOOR2's cc recompute used
a different toolchain path than claimed; the tally documentation lives in PRs/FINDINGS).
Their kernel is kept as practice anyway: gate re-run outputs are now retained in-arc when
convenient rather than deleted after checking.
