# Card AGY-C7: The open-flute Selberg–Lefschetz weave test (`s = 2` geodesic overtones, dynamic `m004` dominance without `SE1`/`SE3`, and `t = 4` lepton-down splitting)

*Seat: `agy` (`agy/cusp-action-2026-11-20`, extending `a87de0f18` from `origin/main` `60a52d359`). Date: `2026-11-20`. Pre-registered before any script or run (`expectations committed first`). Data-free: `0 of 19`.*

---

## One. Package and question

Register rows `P-776`, `P-845`, `M4`, `B1928`, `B1942`, and `B1943`: if **all** primitive hyperbolic threads `[gamma]` in `PSL(2, Z)` contribute on the universal torus fibre `(R / Z)^two` via their anti-fixed Lefschetz torsion loci `ker(gamma + I_2) \ {0}` weighted by Selberg's geodesic propagator `exp(minus s * l(gamma))` at the lowest convergent modular weight `2 s = 4` (`s = 2`, zero `SE1` or `SE3` selection), does `[LR]` (`m004`, `t = 3`, order `5`) dominate dynamically while the first overtone `[L^two R], [L R^two]` (`t = 4`, order `6 = 2 * 3`) automatically breaks `Y_e = Y_d^T` without washing out the cusp hierarchy?

## Two. Deliverables and what done means

- Exact continued-fraction primitive `(L, R)` necklace enumeration of all hyperbolic conjugacy classes in `PSL(2, Z)` for traces `3 <= t <= 50` (`cross-checked against narrow binary-quadratic class numbers h^+(t^two minus 4)`), computing exact `Smith(gamma + I_2)` torsion spectra and `s`-dependent partition weights `Z_weave(s)` across `s` in `{0, 1, 2, 3}`.
- `45`-digit `mpmath` evaluation of the holomorphic `(S, S, S)` Szegő couplings `(Y_u, Y_d, Y_e)` across all primitive torsion orbits `P_d` excited by `3 <= t <= 20` (`orders d` in `{2, 3, 4, 5, 6, ...}`) at cusp moduli `16 + 8 i` and `(13 / 100) + 8 i`.
- Honest side-by-side test of three weave-aggregation rules at `s = 2`: (a) arithmetic ratio mean (`B1940`/`B1942`), (b) geometric log-Yukawa action mean `exp <ln(m_i / m_j)>`, and (c) coherent `3 x 3` family Gramian `H_f(s = 2; tau) = sum w_s(gamma) <Y_f Y_f^dag>` (`both unweighted on ker(gamma + I_2) and Boltzmann-damped by exp(minus F_w(tau))` on `a = 0` cusp-divergent modes).
- Zero-shared-code independent countercheck (`recomputed independently` + `tested against planted errors`) and mask-clean result relay.

## Three. Pre-committed expectations and how it could come out wrong

- **E1 (dynamic `m004` plurality without `SE1` or `SE3`, and `lcm(5, 6) = 30` overtone structure):** At `s = 2` (`lowest convergent modular weight 2 s = 4`, since `s -> 1^+` hits Selberg's entropy pole), the fundamental `[LR]` (`t = 3`, order `5`) must carry the largest single-thread weight (`exceeding two-fifths of the entire infinite sum`), while `t = 4` (`[L^two R], [L R^two]`, `Smith(gamma + I_2) = (1, 6)`) supplies orders `{2, 3, 6}` (`giving joint torsion lcm(5, 6) = 30` with `t = 3`, answering `B1942`'s level-`10` vs level-`15` fork) and `t = 6` (`L^two R^two`, `L^4 R`) supplies dyadic orders `{4, 8}`.
- **E2 (automatic `Y_e != Y_d^T` splitting from the `t = 4` overtone):** Truncated to `t = 3` (`order 5`), `e` and `d` ratios must be identical to `< ten to the minus thirty`; with all primitive threads `3 <= t <= 20` active at `s = 2`, `(minus 3, 6) == (0, 0) mod 3` and `(3, 0) mod 6` on the `t = 4` overtone must split both lepton-versus-down generation ratios by more than `one-tenth` (`without any hand-inserted level 10 or 15`).
- **E3 (honest wash-out vs hierarchy survival audit across the three aggregation rules):** Arithmetic averaging of linear ratios across `a = 0` zero-row torsion points is expected to suffer partial `a = 0` floor wash-out (`lifting m_1 / m_2`), whereas the geometric log-Yukawa action mean and/or Casimir-damped coherent `3 x 3` Gramian `H_f(s = 2)` must test whether multi-decade hierarchy and CKM alignment (`min_k |V_kk| > 95 / 100`) survive on the open weave; whichever rules wash out vs survive will be reported verbatim.

## Four. Premises and firewall boundaries

- Rests on `GENESIS` sections two through four, `B1928`, `B1938`, `B1940`, `B1942`, `B1943`, and `AGY-C1` through `AGY-C6`; Guardrails one through six enforced throughout (`s = 2` fixed a priori as lowest convergent modular weight `2 s = 4`, zero parameter fitting).
- Must **never** read, compute, or compare any of the nineteen empirical Standard Model targets (`0 of 19`), and must leave `origin/agy/audit-2026-11-02` untouched at `4319f47e2`.

## Five. Mandatory planted negative control

1. **Taped-holes (`t = 3` only) plant:** Zero out all overtones `t >= 4` in the weave aggregator: the relative lepton-versus-down ratio split `|r_e minus r_d| / r_d` **must** collapse to `< ten to the minus thirty` (`recovering B1934's exact e = d degeneracy`).
2. **Unweighted white-noise (`s = 0`) plant:** Set `s = 0` across `3 <= t <= 30` (`flat equal weight per conjugacy class, mimicking B1944`): `[LR]`'s weight share **must** collapse below `one-fiftieth`, catching loss of fundamental root dominance without Selberg damping `s > 1`.

## Six. What is needed from main or other seats

Nothing needed to run; offered as a data-free weave-versus-thread investigation on `agy/cusp-action-2026-11-20`.

0 of 19.
