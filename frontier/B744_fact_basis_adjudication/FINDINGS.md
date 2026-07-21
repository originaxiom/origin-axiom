# FINDINGS — B744: the fact-basis conflict adjudication — 6/6 UPHELD as computed, with the real lesson

cc banking seat, 2026-07-21. Number reserved pre-use. The 6 substantive disagreements from the
B738×B742 kill-graph diff (cc=computed vs cc3=asserted): B146, B272, B285, B296, B437, B516.

## VERDICT: all six UPHELD as fact_computed=TRUE
Each id has its discriminating computation IN-REPO and LOCKED: B146 (probe.py + lock), B272
(verification_and_gaps.py + lock), B285 (commutator_phase.py + verdict.py + lock), B296
(verdict.py + lock), B437 (abelian_book.py + json + lock — the header itself carries the #562
retraction discipline), B516 (the computation lives in its mathematical lock, tests/test_b516.py —
a legitimate FINDINGS+lock pattern). **All six locks run green this session (17 passed, 1
env-skip).** The B741 chain (B435→B437) STANDS.

## The real lesson (not a cc3 error — a corpus-scope difference)
cc3's B742 graded the LEDGER ROWS (its census = LAW_MAP/RETRACTIONS/ledgers), whose text IS
assertive; the computations live one hop away in the arcs. cc graded the ARCS. Both were right
about different objects. The fix is cc3's own minted rule applied to ledgers: **rows should cite
their computation's location (exact_scope pointers), so a ledger-scoped audit can verify without
the hop.** Queued as a ledger-hygiene follow-up, not an error class. Diff rates updated in both
kill-graph FINDINGS.
