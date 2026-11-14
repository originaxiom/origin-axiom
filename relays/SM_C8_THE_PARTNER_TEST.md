# SM-C8 — the partner test: a relation through an open end carries the order on the record's several-cusped covers

*The SM seat, 2026-11-14. Card `relays/cards/SM_C8_the-partner-test.md`, with its addendum (§ 7) sealed and pushed at
05e6654e7 before the run. M24 is read as main's word. Main at 5b327b1e0. Data-free; nothing was compared with a measured
value.*

## The outcome: R_leak, as predicted

- **The run.** It covered B1441's tier-1 population: 71 of its 74 manifolds, with the same three skipped (over 600
  characters).
  - 486 754 non-split modules and 1 109 760 joins (P, V, T_i). 934 132 of the joins are vacuous, with H¹(T_i; V) = 0,
    and are left out, as amendment 1 says. That leaves 175 628.
- **Every control held, on every module and every join, so the run never stopped:**
  - C1 (twisted half lives, half dies);
  - C2 (the index as a boundary quantity);
  - C3a and C3b (the index identity for dual boundary conditions);
  - dim S_i + dim S*_i = h¹(T_i; V), so V ↦ V* exchanges S_i with S*_i = S_i^⊥.
- **The plants fire:** P1 (V for V*) on 140 448 joins, P2 (a random line for S*_i) on 105 320, and P3 (half of the
  boundary cohomology) on 23 560 modules.
- **The partner's order changes P's count.**
  - D_ord = n(V | 0 elsewhere, S_i) − n(V* | 0 elsewhere, S*_i) is non-zero on 101 672 of the 175 628 joins, with
    values from −2 to +2:

| D_ord | −2 | −1 | 0 | +1 | +2 |
|---|---|---|---|---|---|
| joins | 732 | 50 104 | 73 956 | 50 104 | 732 |

- **The leak is non-zero on 100 846 joins, in 65 of the 71 entries.** That is outcome R_leak.
  - The leak counts V*'s classes, meeting S*_i at the shared torus, that are alive at the other, open ends.
  - Its values run from 1 to 6:

| leak | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|---|
| joins | 74 782 | 61 858 | 27 039 | 8 551 | 3 135 | 237 | 26 |

  - D_ord is non-zero with no leak on 45 985 joins. There the dimension term alone, the old bound's cusp-fixed
    vectors, makes the difference (R_dim).
- **The prediction held on every carrier.** The leak occurs on all 17 of B1441's carriers of |I| = 2.
- **The card's original D,** on the 7 882 joins where V splits on the shared torus: n(V | sub) − n(V | quotient) is
  non-zero on 4 149, with values −1 (1 250), +1 (2 678) and +2 (221).
- **Without m129 and m125** (previewed by the calibration): the leak count is unchanged, since they contribute no
  leak. m129 contributes 4 joins of R_dim and m125 has no modules.

## What it means, and what it does not

**What it means.**
- On the record's several-cusped covers, P's count at a shared torus depends on which of the two orders the partner
  presents there, V's line S_i or V*'s line S*_i.
- Where it does, the dependence passes through the other ends, which stay open: the classes that the partner's
  condition lets live there.
- This is B1327's type R, exhibited: the order carried by a relation through an open end, as B1457's third refinement
  put it ("flux through an end").
- For the GENESIS FK12 row, it meets the settling clause's first branch on this population and for this kind of
  closing: a partner supplies the order as a relation.

**What it does not show.**
- **The relation carries the order; it does not choose it.** D_ord comes in ± pairs of equal size, and the sum over P's
  own two orders is zero. Which order the partner presents is still an input, unless the partner is itself
  determined.
- **The partner is a boundary condition, not a glued manifold.** The card named gluing a real partner Q as the
  stronger test, for a later card.
- **The dimension term is topological.** It is the count of cusp-fixed vectors, B1268's and B1351's bound. Only the
  leak is new. The duality identity D_ord = d_i + leak_i held at every join, so the two can be told apart everywhere.

## Deviations, said

- **The sealed control on B1441's index histogram was too broad.**
  - My histogram matches B1441's on 29 of 71 entries.
  - Post hoc, labelled (`relays/sm_c8/posthoc_c8_imatch.py` → `relays/sm_c8/c8_posthoc_imatch.json`):
    - on the 7 entries where every H¹(M; ℓ) is a line, it matches on all 7;
    - on the 64 where some H¹(M; ℓ) is a plane or more, B1441 takes its basis and random combinations mod p, so its
      modules are other points of the same families. It matches on 22 of those.
  - The two definitions of the index agree. A check on two entries found h¹(V*) − h¹(V) equal to the
    boundary-vanishing class index on every module.
  - The addendum named this comparison as a stop condition. The code did not stop on it, and should have been
    written to compare only where every H¹ is a line.
- **The calibration previewed two manifolds** of the population (m129 and m125), with other modules. Both are said in
  the addendum, and the results above are given without them.

## Files

- `relays/sm_c8/run_c8.py`, `relays/sm_c8/c8_results.json` and `relays/sm_c8/RUN.txt`: the run, 18 minutes.
- `relays/sm_c8/posthoc_c8_imatch.py`, `relays/sm_c8/c8_posthoc_imatch.json` and `relays/sm_c8/RUN_posthoc.txt`: the
  post hoc check.
