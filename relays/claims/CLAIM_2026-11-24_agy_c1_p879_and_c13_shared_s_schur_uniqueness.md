# CLAIM CARD — AGY-C13 2T Schur uniqueness of shared S(tau) for I-37 and AGY-C1 exact form-level witness at r = 1/2000 for P-879 (0 of 19)

- seat, branch, commit: agy, origin/agy/cusp-action-2026-11-20, eb8ab7160
- kind: theorem
- touches: I-37, A05, P-879, CKM, mixing, Higgs
- effect: conditions — A05, I-37, P-879, CKM, Higgs (delivers the two open Tier-A items named in B1972 "What is open": proves across all 24 elements and 7 irreps of 2T that dim Hom_{2T}(3_{2T}, 3_{2T}) == 1 so two 2T-equivariant doublets share a unique 3-dim flavor triplet S(tau) up to scalar, and provides C1's exact form-level P-879 witness at reality r = 1/2000)
- imports: unbroken binary tetrahedral flavor symmetry 2T on collar doublets for shared S(tau) (broken at > 0 discrete bits when magnetized curve fluxes split w_10 != w_5); abstract operator family Y(h; u, w) without Frame C torus evaluation for the form-level P-879 witness
- premises on main: B1736, B1968, B1969, B1971, B1972 ("What is open": C1 and C13), I-37, A05, P-879
- decisive script: relays/agy_2026-11-24_c46/c46_remediate_c45_p135_b1970_and_m13_sandbox.py, SHA-256 46be6dd192295060, depends on only the standard library, mpmath, and sympy, run as `python3 -I relays/agy_2026-11-24_c46/c46_remediate_c45_p135_b1970_and_m13_sandbox.py`, output SHA-256 0ea1e0f46e5ec87e (c46_out.json, sections E2 & E3; original derivations in AGY-C1 & AGY-C13)
- second computation: agy disjoint cold-room countercheck relays/agy_2026-11-24_c46/c46_countercheck.py (@ ff1526ee8, SHA-256 f2280cba98e4dd29, standard library and mpmath, agrees); cusp-exponent law matched by main B1971 (5988bd5de) and agy-exp BANK-8
- already on main?: topic-sweep /Schur|shared S|P-879|B1969|B1971|B1972|I-37/ on main (27a9353e5): B1972 explicitly records under "What is open" that "agy's form-level witness (C1) is owed a reading at source" and "Schur uniqueness of the shared S sits on agy (C13) and is owed a reading at source"
- what would make it fail: if 3_{2T} were reducible over C ((1/24) sum |chi_3|^2 != 1) or Sym^3(2_{2T}) contained a 3-dim spinor irrep (Control 5 proves Sym^3(2_{2T}) == 2' + 2''); or if random Haar SU(3)_Q x SU(3)_u x SU(3)_d rotations changed |V_CKM| or m_2/m_3 on the r = 1/2000 witness (Control 2: < 10^-44)

## Claim (summary)

Delivering the two open Tier-A items requested in `B1972` (`27a9353e5`): (1) **Schur uniqueness of shared `S(tau)` (`AGY-C13` / `AGY-C46`):** Over the `24` unit Hurwitz quaternions of `2T` (`7` conjugacy classes `[1, 1, 4, 4, 4, 4, 6]`, `7 x 7` character table verified orthogonal, `sum d_a^2 == 24`), `chi_3(g) = 4 (g_0)^2 - 1` satisfies `(1 / 24) sum |chi_3(g)|^2 == 1`, so `dim_C Hom_{2T}(3_{2T}, 3_{2T}) == 1`: two `2T`-triplet doublets share `S(tau)` up to scalar (`whereas realistic |V_{us}| requires curve/flux splitting w_{10} != w_5 priced at > 0 bits`).

(2) **Form-level `P-879` witness (`AGY-C1` / `AGY-C46`):** On `B1736`'s `Y(h; u, w)` at `r = 1 / 2000` (`strictly below B1969's grid floor`), the exact closed-form `(h^*, h)` pair gives `min_k |V_{kk}| > 99 / 100` (`|V_{CKM}| = I_3` to `< 10^{-45}`) with `m_2 / m_3 < 1 / 100` in both sectors (`distinguishing the form-level escape from Frame C's evaluated B1968/C2 torus bound`).

0 of 19.
