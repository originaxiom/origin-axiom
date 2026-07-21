# FINDINGS — B748: the V₄-completion sweep — V₄-SILENT: the ENTIRE forced V₄ is interface-only

cc banking seat, 2026-07-21. Completes the face-triple over the child grid. Prereg sealed
a59ac036 before the run; same sealed input as B747 (sha 77818016). Gate 5; nothing to CLAIMS.

## Verdict: V₄-SILENT — 0/78 on the meeting face ℚ(√−15); consistency 24/24 vs B740

- 54 odd-degree slopes: √−15 excluded by parity (theorem, sealed degrees).
- 24 even-degree slopes: field recomputed (degree cross-checked, 24/24 match — the prec-6000
  ladder rung resolved (3,8) directly this time), exact x²+15 root test — **all False**.
- **Added consistency control:** x²+3 (being) re-derived per even slope — **24/24 reproduce
  B740's sealed per-slope verdicts exactly** (an independent re-derivation of B740's
  even-degree half in passing).
- Controls all pass (ℚ(√−15) routine+; ℚ(√5), ℚ(√−3) routine− for √−15; m004 pipeline).

## The combined statement (three arcs, one census)

Across B288/B740 (being √−3), B747 (hearing √5), and B748 (meeting √−15): **no closed
hyperbolic filling in the |p|,q ≤ 8 grid re-sees ANY of the three forced faces. The entire
forced V₄ (B730) is a property of the OPEN object — it lives at the cusp/interface and is
lost on every tested closing.** This upgrades B288's original reading ("the atom lives at
the cusp, not in any child") from the being face alone to the full forced-face triple, and
sharpens B746's two-column law: closing silences both columns' quadratic identities at once.
Scope honesty: the tested grid is |p|,q ≤ 8 (78 hyperbolic fillings); the statement is a
census fact, not an all-slopes theorem. E20: three quadratics tested against 78 fields with
0 hits — no new positive structure asserted; the content is the clean negative + its
uniformity across the V₄.

Artifacts: `b748_sweep.py` + `b748_out.txt`, sealed input copy. Locks in
`tests/test_b747_b748_sweeps.py`.
