# B296 — Arc II verification of the seam arc: red-teamed, novelty-audited, firewall-clean

**Status: banked (frontier). The verification round (Arc II) for the seam arc B287–B295. Nothing to `CLAIMS.md`.**
Two artifacts: `VERDICTS.md` (the adversarial red-team) and `NOVELTY.md` (the prior-art audit). This FINDINGS is the
short summary; the verdict module + test encode the outcome.

## Red-team — all SURVIVE
A multi-agent adversarial pass re-ran every reproducer and attacked each banked claim (hidden genericity / overclaim /
firewall-leak / counterexample / convention-artifact / triangulation-dependence). **Result: every probe SURVIVES; 0
refutations; 0 firewall leaks; nothing wrongly promoted to `CLAIMS.md`.** Two results were *strengthened* —
- **B287**: uniqueness is **homology-forced** (a torus bundle needs `b₁≥1`; every non-zero exceptional filling has
  finite `H₁` or is `S³`), independent of Regina's recognizer;
- **B288**: extended to `|p|,|q|≤12` (**174 closings, still 0 arithmetic**), consistent with Garoufalidis–Jeon
  finiteness;
- **B291**: min-volume `(5,1)` confirmed stable over the larger grid —

and four FINDINGS were tightened with honest caveats (B287 homology-forced uniqueness; B290 the clean real coefficient
is m004-specific because `τ=2√3·i` is purely imaginary; B293 `k_um=−1` is frame-dependent and the Casimir check is a
Nambu-construction with the Goldman identification imported; B295 the potential is a cubic with one minimum, so cannot
be the degenerate double-well SSB needs). **No retraction; no substantive weakening; the B294 verdict stands.**

## Novelty — classical math KNOWN, the connections candidate-novel
The audit **confirms the classical attribution** (so the program does not claim the math as new):
- **KNOWN**: claim 1 (0-surgery = Sol bundle `[[2,1],[1,1]]`, 10 exceptional fillings — Thurston); claim 2
  (arithmeticity lost on closing / trace-field degree growth — **Garoufalidis–Jeon**, Hodgson, Neumann–Reid); claim 4a
  (Goldman/NZ peripheral symplectic — Goldman, Neumann–Zagier).
- **APPEARS-NOVEL / NEEDS-SPECIALIST** (the genuinely-new *connections*, firewalled): claim 3 (handedness = `ℚ(√−3)`
  Galois conjugation = the `±π/6` Eisenstein phase flip); claim 4b (the Goldman/NZ clock ↔ Λ-conjugate-to-CS-time);
  claim 5 (the seam reframe). A fuller prior-art round on these is **pending the next pass**.

## Net judgment
The seam arc is **firewall-clean and honestly scoped**: every probe reproduces, every physics-facing statement is
HELD/[LEAP]/stop-gated, `CLAIMS.md` is untouched, and the novel content is correctly identified as a **reframe + a set
of connections**, not new theorems. The adversarial round made the arc *stronger*, not weaker.

`VERDICTS.md` · `NOVELTY.md` · `verdict.py` · `tests/test_b296_seam_arc_verification.py`. Related: `B287`–`B295` (the
probes), `B294` (the verdict), `B286` (the seam). Lit: Thurston, Garoufalidis–Jeon, Goldman, Neumann–Zagier,
Alexander–Magueijo–Smolin (arXiv:1807.01381).
