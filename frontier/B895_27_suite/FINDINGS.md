# B895 — The 27-suite closed: exact color, the ℤ₆ kernel read, the belt confirms B884, the solo-suite locks (D2+D3+N1+N6)

**Date:** 2026-08-05 · **Seat:** cc (banking) · **Status:** computed; z6c exact over ℚ, z6d/belt mod-p with two-seed control

Pays the last Phase-0 debts of the masterplan (v2 D2/D3; v3 N1/N6). The solo
seat's 27-suite (handoff 4) now runs end-to-end on this build with foreign
paths patched; every output READ and banked — nothing left orphaned.

## Cell 1 (z6c) — the color algebra, exact over ℚ

The floor (joint centralizer stack) has **dim 12 over ℚ**; inside it the color
algebra is **su(3): dim 8, Cartan 2**, and the exact color Casimir on the 27
has eigenvalues **0 (multiplicity 9) and 4/9 (multiplicity 18)** — the 27 =
9 color singlets ⊕ 18 triplet dimensions. **tr(h³) = 0 on the triplet space:
the color content is 3 ⊕ 3̄ exactly — vector-like**, matching the two-chirality
picture (the object is θ-symmetric; chirality is the observer's closing).
All the solo seat's gates (9, 18, 2, 0) pass exactly.

## Cell 2 (z6d) — the ℤ₆-kernel readout (the never-read run, now read)

At the tower prime 40123: the 27 decomposes into **9 singlet cells (covered
9/9)** and **6 triplet cells of multiplicity 3 (covered 18/18)**, each labeled
by its (x₁, y, w₃) charges. Every triplet cell carries a hypercharge-fit tuple
(two values seen — the 3 vs 3̄ branches); the color-Casimir (CasW) splits the
cells cleanly. The readout is banked as data; the global-structure
interpretation (the SU(3)×SU(2)×U(1)/ℤ₆ question) stays with the solo seat's
fence — this arc claims the decomposition and its coverage gates only.

## Cell 3 (belt639 + the projection diagnostic) — THE 17-vs-11 ANOMALY DISSOLVES; B884 CONFIRMED AT A SECOND PRIME

belt639 (fresh prime q = 40639, fresh seed) initially reported **17 allowed
couplings against B884's 11** — flagged, not banked, per the two-seeds rule.
The diagnosis (`belt_project.py`): belt639's cells are joint eigenspaces of a
**four-operator combo** (X₁, Y, W₃, R₁₄) — strictly finer than B884's (X₁,Y)
charge-pair classification. The projection test:

- **15 fine cells → exactly 11 coarse (X₁,Y) classes** (= B884's cell count);
- **17 fine allowed triples → exactly 11 coarse couplings, at BOTH rng seeds
  (7 and 11)**.

So the fresh-seed, fresh-prime belt **confirms the charge-forced Yukawa
support 11** — the 17 was refinement bookkeeping. Also from belt639: the
Y-solve at 40639 passes for **exactly the conjugation pair** of assignments
(expected 2 — the hypercharge direction reproduced at a second prime).

## Cell 4 (N6) — the solo-suite verdict locks

The four verifications logged in B892's FINDINGS ("also verified") now carry
dedicated locks (`tests/test_b895_solo_suite.py`): the hypercharge fit
(conjugation pair rank 3, mixed rank 4), G₂₀ (20/19/1), the ℤ₂ commutation
obstruction (∏c = −1, no all-commuting configuration), and the texture
count (11 = 11 vs B884).

## Files

- `results.json` (consolidated: z6c / z6d / belt / solo-suite verdicts)
- `belt_project.py` (the projection diagnostic, path-scrubbed: set
  `HANDOFF4_RUN` to the handoff-4 run dir to re-run); the rest of the suite
  remains the solo seat's handoff-4 scripts (patched paths), run in the
  session scratchpad; all numbers locked from `results.json`.
- Locks: `tests/test_b895_solo_suite.py`

## Depends on

B883 (the 27), B884 (the 11 cells), B892 (the SMT + also-verified list),
B854 (the build). Solo handoff 4 (integrate-don't-merge).
