# B1102 — THE EXACT HYPERCHARGE SOLVE AT THE LANDING (PREREGISTRATION)

**The question, one line:** does the A2 landing's rank-4 Cartan contain a direction
whose 27 hypercharge values equal the banked 6Y multiset **exactly** — and does the
exhibited su(2) sit beside it as the SM's structure requires?

**Standing:** B1100's named residual, attacked head-on. Owner-elected 2026-08-20
(scheduled before the aperiodic sitting, so the sitting rules with the sharpest picture
of the landing). Structure-level throughout: the banked 6Y multiset is the program's
own integer assignment (B950's ledger), not a measured value — Gate 5 untouched, same
license B1100 ran under.

## Prior state (all banked, none re-derived here)

- **B1098**: A2-class centralizer = su(3)⊕su(3) exact; the I₁/I₂ ideal split EXHIBITED
  (explicit bases); an su(2)×u(1) exhibited concretely inside I₂ commuting with all of
  I₁; verifier PASS ×3 independent paths.
- **B1100**: joint weight table exact (15 weight classes, sizes 3⁶·1⁹); the 27 complex,
  witnessed; hypercharge **bijective form EXCLUDED exact**; **collapse form GENERIC**
  (trial-0 float hit reproduced the target degeneracy pattern (6,6,4,3,3,2,2,1);
  t_float recorded in b1100_hypercharge.json).

## Operations (MB12: each non-trivial, each can genuinely not-work)

1. **Adapted re-basis.** Build Cartans FROM B1098's exact I₁/I₂ ideal bases (one per
   su(3) factor), replacing B1100's random-kernel Cartan whose coordinates are cubic
   CRootOf. Non-trivial: if the ℚ-form's non-splitness lives inside each factor, the
   coordinates stay in extensions and the solve proceeds on the B1100-proven
   cubic-CRootOf path instead (slower, same logic).
2. **Joint weight table in the adapted basis** — stacked kernels (B1100's proven
   method), modular rank cross-checks over ≥2 primes.
3. **The collapse solve.** Fix the assignment combinatorics from the trial-0 float
   direction's collapse pattern (which weight classes share which target value); solve
   the induced linear system for the direction t (4 unknowns over the weight field).
   If the float assignment fails exactly: enumerate ALL multiplicity-respecting collapse
   assignments (bounded — 15 classes onto 8 values with size bookkeeping) and solve
   each. Floats guide assignments only; no float enters a banked number.
4. **Exact verification.** All 27 values symbolic; multiset-compare to the banked
   target.
5. **The su(2) beside it.** Verify the B1098-exhibited su(2) (or an I₂-conjugate)
   commutes with the solved Y; decompose the 27 under su(3)×su(2)×u(1)_Y; compare reps
   and multiplicities to the 16-per-generation structure (structure-level only;
   chirality-at-count NOT claimed — the standing fence carries verbatim).

## Sealed criteria (MB12: each can pass AND fail — vacuity-checked)

- **C1 MATCH-EXACT.** Some admissible assignment+direction reproduces the banked
  multiset exactly. CAN PASS: the compatible cone is generic (trial-0). CAN FAIL: the
  bijective form already failed exact — pattern-compatible ≠ value-compatible, proven
  in this very arc-pair.
- **C2 UNIQUENESS/PRICE.** If C1 passes: is the solving direction unique up to the
  residual Weyl/rescaling freedom? Unique → zero new bits; a family → priced in bits,
  stated.
- **C3 SU(2)-COMPATIBILITY.** The doublet structure lands (3 Q-doublets + 3 L-doublets
  + singlets per the trinification branching). CAN FAIL: the exhibited su(2) could
  misalign with the solved Y.

## Outcome grammar (typed before any computation)

- **MATCH-EXACT + aligned** → the landing carries the banked hypercharge;
  "Standard-Model-shaped" upgrades toward "SM-contained at the A2 stratum"; residual
  freedom priced; the doc sentence ("a computation, not a theorem") updates to cite
  the computation.
- **NO-EXACT-MATCH** (all admissible assignments fail) → typed NEGATIVE: the landing's
  u(1) cone is hypercharge-shaped but not hypercharge-valued; the hatch's SM door
  closes at value level; kill node routed; the wave's honest sentence stands as
  written.
- **UNSTABLE / DEGENERATE-FAMILY** → the family priced; no forcing; escalation per
  house rules.

Either decisive outcome moves the program; neither is celebrated as such (firewall
gate: block overclaims, not physics; don't celebrate negatives).

## Method constraints

- Exact throughout (sympy); independent own-code verifier (sonnet) re-derives the
  solved direction from scratch given ONLY the I₁/I₂ bases + the target multiset,
  before banking.
- `B1098_TRIPLE` env var honored (§CE path discipline); all staging in scratchpad;
  landing by explicit filename post-certification.
- Bench-scale: ≤1 day. Fallback path named in Op 1.
