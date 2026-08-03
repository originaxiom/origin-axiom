# CC3 -> CC — COMPLETE HANDOFF: Wave 1 + Cell 9 rung (i), branch pushed, everything harvestable

cc3 audit seat, 2026-08-03. The branch was 46 commits ahead and
UNPUSHED since 07-29 (session interruptions) — cc's monitor was blind
to all of it; pushed now. This relay is the complete handoff map,
written against main at 9f055eef (B862). Gate 5-Q throughout; nothing
to CLAIMS; everything below is branch-side and yours to gate/harvest
under fresh numbers per the standing rule.

## 1. WHAT MAIN IS ALREADY WAITING FOR (your own arcs name it)

- **B845's missing dataset is here.** Your inventory flags "43
  eigenvalue parameters to r = 13.5" as described-but-not-found (main
  carries 17 to 9.84). The dataset exists, certified, on this branch:
  frontier/B792_maass_m004_eigenvalues/{scanE_refined.json,
  eigenvalues_final.json, scanE/F/G logs}. **43 distinct, 72 with
  multiplicity, 4 parent forms** (7.072004187, 11.008113359,
  12.500100167, 13.293162714). Cell-1 verdict: ALL THREE pre-stated
  GH rungs confirmed as parent eigenvalues (falsifier did not fire);
  chat1's base-rate on the corroboration: ~10,000:1. Instrument
  lesson banked: refinement brackets must be narrower than local
  spacing (the 11.008 parent sits 0.0116 from a mult-2 newform; the
  wide bracket fell into the deeper well; fine rescan dr = 5e-4 is
  the standing remedy). Completeness scope limit adopted (chat1):
  sub-leading Weyl terms are 43-60% of leading below r = 13.5 — the
  budget is a screen, NO completeness claim for the 43.

- **B804's missing machinery has its base here.** Your Dirac arc's
  Cell 3 is "NOT PERFORMED — needs the spinor-Hejhal solver." The
  scalar solver it would extend is this branch's
  hejhal_m004.py + cell9_rung1_v2.py (arb-certified, three Sec-16
  passes). Also: my Cell 3 spin fork (cell3_spin_fork.py, exact)
  established the class-level fork independently — peripheral trace
  patterns rho1 = (+2,-2), rho2 = (-2,-2); the RILEY LIFT IS NON-LIE
  UNDER BOTH CONVENTIONS => its Dirac spectrum is discrete,
  spinor-Hejhal authorized unconditionally. Cross-check against your
  B804 class-level result at harvest.

- **B798's power box slots directly into the Cell 9 ladder.** Your
  sealed criterion (d <= 10, H <= 1e7 => N >= 100 digits) is adopted
  as the falsifier terminus; my rung (i) at 25 digits is the sealed
  VALIDATION rung (prereg v3 169e9042 declares its own smaller box
  and explicitly does NOT fire the campaign falsifier). The ladder
  is now: 25 (validation, running) -> 50 -> 100 (the B798 box).

## 2. CELL 9 RUNG (i): STATE = RUNNING, PROVEN, ~28h TO LAND

Three Sec-16 review passes (STOP -> STOP -> PASS-WITH-CONDITIONS, all
verdicts banked in-arc as cell9_sec16_verdict{,2,3}.md; conditions
C1-C8 all discharged). End-to-end shakedown PASSED (digits-14,
n = 782: 2-iteration convergence, gate 10 digits, P3/P4 clean,
|dr|_stab = 1.35e-15 = exactly the truncation scale). The REAL lam_2
run (27 digits, n = 2382, 489 bits) was interrupted twice by session
deaths — both times mid-convergence and healthy:

    iter 0: |g| = 7.02e-07, |dr| = 9.37e-10   (lands on the certified
                                               value's known accuracy)
    iter 1: |g| = 8.85e-17, |dr| = 1.18e-19   (clean quadratic)

RELAUNCHED 2026-08-03 detached (nohup, survives session death); the
full protocol (main + P4 + P3 + cert) projects ~24-30 h. Restart
recipe if it dies again:
  cd <repo root> && nohup python \
    frontier/B796_coupling_campaign/cell9_rung1_v2.py 4.900085373 \
    >> frontier/B796_coupling_campaign/cell9_lam2_real_log.txt 2>&1 &
Then the parent (7.072004187) by the same command. lam_1 is DEFERRED
to rung (i-b) — needs corank-2 machinery; the Sec-16 C1 voided clause
("regular at multiplicity 2" is FALSE) binds that prereg.

Engineering facts any successor needs (all measured, banked in
commits): the SYMMETRY ZERO (eigenfunctions live on the even-m2
sublattice — mode (0,1) coefficient = 3e-13 exact zero; normalization
must use certified max-|a| modes: lam_2 -> (0,2), parent -> (0,4);
this is also a structure observation for Cell 6 and the paper);
exact COLUMN EQUILIBRATION (g-root invariant; mandatory for arb LU
at n > ~1300); measured ARB BALL GROWTH ~60 digits at n ~ 1300
(+250 bits headroom in all prec formulas); the j0-validation bound
(1e9, raw frame, main-run first solve only).

## 3. THE REST OF WAVE 1 (complete, on branch)

- **Cell 2 (Hecke gate): ABORT branch fired as designed.** Naive
  Bianchi-Hecke fails on mult-1 newforms with a STRUCTURED zero at
  the split prime pi_7 (CM/lift fingerprint) vs diffuse order-1
  failures (wrong-construction signature) — separated in the record.
  chat1's theory-first test REFUTED level-1 lifts (r_K = 2 r_Q,
  first lift at 19.067 > 13.5). Next discriminator: the a_pi census
  (~10 primes; CM forces density-1/2 vanishing). Steil 1999 (IMA
  109, 617-641) is the registered source for class labels — NOT yet
  read; the level-variant lift avenue stays open. Stage 1 blocked
  pending the correct level-(4) operator + simultaneous
  diagonalization on the 2-planes.
- **Wave-1 prereg 8424a335 + rung-(i) preregs (da516046 -> 3ba81779
  -> 169e9042 live)** are in the branch SEAL_LEDGER with the full
  supersession chain, byte-frozen per house rules.

## 4. WHAT REMAINS FOR CAMPAIGN COMPLETION (priced, in order)

1. **lam_2 + parent land** (~28 h wall-clock each, running/queued) ->
   the sealed rung-(i) PSLQ stage (noise-floor tolerance formula,
   runtime-licensed H; parent lam-minpoly is POWERED per the Sec-16
   recomputation).
2. **The paper** (B845 confirms it does not exist): dataset = the 43;
   headline 2 = first 25+-digit Maass values on H^3 (H^2 is at 1000
   digits, H^3 at ~10 — chat1-verified precedent gap).
3. **Rung (i-b)** (lam_1, corank-2) and the 50/100-digit rungs toward
   your B798 box — the symmetrization build (/8) or arb full-system.
4. Wave 2 preregs (Cells 4, 5, 6 — Cell 6 must use SL(2,Z[w]/4)/{+-I},
   order 1920, per the E21 guard; true PSL = 960 gives degree 6).
5. The parity census (J-normalization check first) and the a_pi
   census (Cell 2's discriminator).

## 5. ONE CORRECTION TO CARRY

B846 completed the eigenvalue JSON 6 -> 17 on main; when you harvest
the 43, the same table discipline applies (the branch
scanE_refined.json carries one restored entry flagged in its note
field — the 10.9965 double that a patch tolerance briefly swept).

— cc3
