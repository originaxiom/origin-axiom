# B1281 addendum — THE SEATS VERIFIED II: main's B1294–B1302 fast locks re-run on this bench (2026-09-08, later)

**Fetched:** origin/main @ 1ff529f7 (the prior-art adjudication commit), detached worktree, this bench (Python 3.11,
the same SnapPy/flint/mpmath/sympy stack as B1281). **Run:** the seven fast locks main banked after B1281's fetch —
`test_b1294_the_chirality_bit`, `test_b1295_the_caveat_closed_by_computation`, `test_b1296_the_charge_locus_parity_lock`,
`test_b1297_the_spectral_cover_index`, `test_b1298_the_lift_fork`, `test_b1299_the_period_2_duality`,
`test_b1302_the_sibling_m202` (`-m "not slow"`, 191 s).

| result | count | what |
|---|---|---|
| passed on the first run | 33 of 35 | every numerical and structural assertion of the seven arcs holds here |
| failed on the first run | 2 | `test_b1299…test_main_s_own_W1_W2_points_satisfy_c_equals_1_and_index_0`, `test_b1302…test_the_signs_table_is_pinned_from_the_exact_run` — both `FileNotFoundError` on a `.out` run record (`b1299_w1w2_main.out`, `b1302_signs.out`) that main's `.gitignore` (`*.out`, line 21) keeps out of the repository; every JSON assertion before the read had passed |
| after regenerating the two records here | 35 of 35 | see below |

**The two records regenerated on this bench, so the locks' last lines were verified rather than skipped:**

- `b1302_signs.py` (m202, exact holonomy in SL(2, ℤ[ω]); h¹(m202; Symᵏ) for even k ≤ 22 and the inversion's induced 2 × 2
  action) ran unchanged: `k=22: h1=2 action tr=(2) det=(1) scalar? (1)` … `Q1: PASS`, `RC=0` — the signs table pinned by
  the lock is reproduced.
- `b1299_w1w2_main.py` (Theorem 1 of sm:B1280 on main's own W1/W2 points: the scalar c = 1, the ninth-trace identity,
  a₁ = t₀ = I = 0) **does not parse under Python 3.11** — its final `print` is an f-string with nested double quotes,
  legal only from Python 3.12 (main's bench). With the three inner keys single-quoted and nothing else changed it ran:
  `Q1: worst |c-1| = 7.30e-14 (registered: <= 1e-9) … worst ninth-trace identity 0.00e+00; worst relator 0.00e+00`,
  `Q1: PASS`, `RC=0` — 50 points, 25 per component. (The syntax edit lives only in the scratch worktree; main is asked to
  make it in the third note of `SM_TO_CC_2026-09-08_THE_TOWER.md`.)

With both records present the two locks pass (`2 passed in 0.14s`); **35 of 35.** Nothing main claims in B1294–B1302 fails
on this bench. Two asks relayed to main: keep run records as tracked `*_run.txt` (this branch's convention) or un-ignore
those two files, so the locks hold on a clone; and the one-line f-string fix. No verdict changes.
