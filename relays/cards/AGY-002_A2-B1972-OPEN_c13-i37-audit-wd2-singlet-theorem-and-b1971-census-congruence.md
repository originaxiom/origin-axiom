# Scope Card `A2-B1972-OPEN` (`2026-11-24`): Independent Zero-Trust Resolution of `B1972`'s Remaining Tier-A Open Queue (`agy` `C13` vs. `I-37`, `chat1` `W-D2 § 3–4` Singlet Theorem) & `B1971`'s Open Census Congruence (`0 of 19`)

- **Seat / Branch:** `agy-002` (`origin/agy-002/verify`), answering `origin/main` `27a9353e5` (`B1971` & `B1972` `"What is open"`).
- **Firewall:** Strictly **`0 of 19`** (zero empirical SM / PDG / NuFIT / Planck / DESI / CODATA numbers; zero Python `float`/`complex` AST literals; zero binary64 casts; zero JSON float tokens; zero edits outside `relays/`).
- **Zero-Shared-Code Pledge:** Zero lines of `agy` `C13`, `chat1` `W-D2`, or `main` `B1971` Python scripts were copied or imported. The standalone script depends ONLY on Python stdlib, `sympy`, and `mpmath` (zero external files, zero subprocesses — 100% sandbox-runnable).

## 1. Pre-Registered Expectations & Disagreement Criteria (`expectations committed first`)

### Block `OPEN-1` — Zero-Trust Audit of `agy` `C13` Schur-Uniqueness Argument Against `I-37` (`B1972` Open #2, Tier A)
1. **Pure-Math Core (`recomputed independently`):**
   - Exact $E_8 \supset E_6 \times \mathrm{SU}(3)_{\text{fam}}$ `248` branching `(78,1)+(1,8)+(27,3)+(27bar,3bar)` from $\mathbb{R}^8$ roots: `81` roots in `(27,3)` splitting as `48 + 30 + 3` under $\mathrm{Spin}(10)\times\mathrm{U}(1)$; `40` `SO(10)` `10*16*16` Yukawa terms splitting under Kawamura parity into `24` color-triplet + `16` electroweak channels (`6 Qu^c H_u + 6 Qd^c H_d + 2 Le^c H_d + 2 Lnu^c H_u`).
   - Exact SymPy $q^{1/8}$-series & 60-digit `mpmath` proof of Halphen–Serre identity $24\eta(\tau)^3(c_0, c_1, -i c_2) = (-\theta_2^2(\theta_3^4+\theta_4^4), +\theta_4^2(\theta_2^4+\theta_3^4), +\theta_3^2(\theta_2^4-\theta_4^4))$, verifying $N_0 + N_1 - N_2 = 0$ identically.
   - Exact $S_3 = \mathrm{SL}(2,\mathbb{Z})/\Gamma(2)$ representation on $M_{2k}(\Gamma(2))$ (`k = 1..4`):
     - $k = 1$ (`wt 2`, $\eta S$): $\chi = (2, 0, -1) = \mathbf{2}_{\text{std}}$, $\dim \operatorname{Hom}_{S_3}(\mathbf{2}_{\text{std}}, M_2(\Gamma(2))) = 1$ (**confirms `C13`'s conditional Schur uniqueness inside weight-`3/2` holomorphic triplets**);
     - $k = 2$ (`wt 4`, $\eta S^{(7/2)}$): $\operatorname{Sym}^2(\mathbf{2}_{\text{std}}) = \mathbf{1} \oplus \mathbf{2}_{\text{std}}$ ALSO has multiplicity **`1`** of $\mathbf{2}_{\text{std}}$, yielding a **distinct** holomorphic weight-`7/2` $S_3$-equivariant triplet (proving `C13`'s uniqueness requires fixing modular weight to `3/2`, not $S_3$ equivariance alone!);
     - $k = 4$ (`wt 8`): $\operatorname{Sym}^4(\mathbf{2}_{\text{std}}) = \mathbf{1} \oplus 2\,\mathbf{2}_{\text{std}}$ has multiplicity **`2`**.
   - Exact 6D $(1,0)$ gravitational $\operatorname{tr} R^4$ anomaly from SymPy $\hat{A}(R)$, Rarita–Schwinger $+245$, and self-dual $B_2$ $+28$: $N_H - N_V + 29 n_T = 273$, giving $\Delta_{244} = 175$ (`N_V=12`) and `177` (`N_V=14`) at `N_H=81, n_T=1`.
2. **Record-Level Verdict on `I-37`:** `C13`'s pure math holds `THE SAME`, and proves conditional shared-$S$ uniqueness **given** holomorphy + exact weight `3/2` + $S_3$-equivariance, **but `I-37` remains `UNEARNED`** (holomorphy and weight `3/2` are assumed rather than derived, Kawamura parity is imported, no weave-to-$\mathbf{10}$ map or prediction is supplied).

### Block `OPEN-2` — Exact Algebraic Proof of `chat1` `W-D2 § 3` Singlet Identity & Resolution of `W-D2 § 4`'s Two Uncomputed Questions (`B1972` Open #3)
1. **Exact Closed Form & Algebraic Proof of `Y_lep(R + s 1) = lambda Y_down(R - s 1)^T`:**
   - Prove symbolically in SymPy from `B1656`'s contraction $Y_{ab}(H; M) = \sum_{m,n} (C_a^T \varepsilon H C_b)_{mn} M_{mn}$ that:
     - $Y(h, s; u, w) = \big(u h^T + h u^T - (u\cdot h)I_3 + w[h]_\times\big) + s\,\big(w I_3 + [u]_\times\big)$ (up to fixed basis sign verified symbolically);
     - $Y(h, s; M^T) = Y(h, -s; M)^T$ identically for all $(h, s, M)$, proving `W-D2 § 3`'s identity $Y_{\text{lep}}(R + s\mathbf{1}) = \lambda Y_{\text{down}}(R - s\mathbf{1})^T$ to exact symbolic `0` (and `< 1e-50` numerically on Frame C's act line).
   - Derive the **exact cubic polynomial $\det Y(h, s; u, w) = D_0 + D_1 s + D_2 s^2 + D_3 s^3$** in SymPy, proving that the linear odd-$s$ coefficient $D_1$ splits $|\det Y_{\text{lep}}|$ from $|\det Y_{\text{down}}|$ (splitting $m_1$), while deriving the exact analytic cusp scaling exponent $\kappa_*(\tau) \sim \varepsilon^{\alpha_*}$ of the first-generation split window.
2. **Answering `W-D2 § 4`'s Two Uncomputed Questions (`(S, S, S)` shared doublet + same-sign singlet `s` on down & leptons at the mark `(2/5, 4/5)` and twin `(1/5, 2/5)` across heights `10, 20, 30`):**
   - **Question 1 (Does the 1st-gen split survive while `(S, S, S)` keeps CKM alignment AND hierarchy?):** Test across $\kappa = 10^{k/2}$ ($k \in [-30, +4]$) and $\phi \in \frac{\pi}{4}\mathbb{Z}_8$: expect **YES** — `(S, S, S) + s` preserves `min_i |V_{ii}| > 0.99` AND `m_2/m_3 < 10^{-2}` while achieving `|\ln D_1| > 1.0` in the exact analytic $D_1 s \sim D_0$ window!
   - **Question 2 (Does any singlet split the 2nd generation `m_2/m_3` while preserving hierarchy?):** Expect **NO** — prove analytically and verify numerically that wherever `m_2/m_3 <= 10^{-2}`, `|\ln D_2|` vanishes exponentially with height (`< 10^{-2}` at `y = 10`, `< 10^{-3}` at `y = 20, 30`), because splitting `m_2` requires $|s| \sim |h| |u| / |u_{\max}|$ which simultaneously destroys the heavy-pair hierarchy!

### Block `OPEN-3` — Independent Verification of `B1971` (`N1–N5`) & Closed-Form Proof of the Order-5 Lock + Orders-8/10 Unalignment Census (`B1971` `"What is open"`)
1. Independently verify `B1971` `N1..N5` at `x = 13/100`, `y = 20, 30` (rates `(3/5, 3/10, 11/10)` at mark, `(9/10, 1/10, 1)` at twin; Higgs nullity `h.h / (eta^6/4) == 1`; cancellation of all `5` rate-`1/2` entries; order-5 `24/24` aligned `[10, 10, 4]`; orders-8,10 `104/112` aligned with `8` unaligned on `a = 1/2`).
2. **Closed-Form Congruence Proof (Answering `B1971` Open #1):** Derive from the exact leading $q$-exponents $d(c) = \frac{1}{2}\operatorname{dist}(c, \mathbb{Z})^2$ of $\vartheta_{c_a, c_b}(0, \tau)$ the exact congruence on $a \in E[5]$ explaining why ALL `24` order-5 points partition purely by $\tilde{a} = \min(a, 1-a)$:
   - $\tilde{a} = 2/5$ (`10` points): `u_up` along `n`, `u_down` along `e` with `w/u_e = +i`, assignment `(n, n_bar, e)`;
   - $\tilde{a} = 1/5$ (`10` points): `u_up` along `n_bar`, `u_down` along `e` with `w/u_e = -i`, assignment `(n, e, n_bar)`;
   - $\tilde{a} = 0$ (`4` points): both `u_up, u_down` along `n_bar`, assignment `(n, e, n_bar)`;
   proving algebraically why the up null-direction bit and the down `sgn(Im(w/u_e))` bit are locked together at order 5!
3. **Multi-Column & Multi-Height Census (`B1971` Open #4 — Reconciling `B1963` `12` vs. `B1971` `8`):** Evaluate all `112` order-8 and order-10 points across `x in {0, 13/100, 1/4, 1/2}` and `y in {10, 20, 30}` to classify exact alignment counts on `a = 1/2` (`8` points) vs `a in {1/4, 3/4}` (`8` order-8 points) vs all remaining `96` points!

### Block `OPEN-4` — Planted Fault Controls (`6/6` Must Trigger)
- `PF-1`: Non-modular `B1742` `F_6` fails `S_3` weight-`2` equivariance (`C13` control).
- `PF-2`: Opposite-sign singlet `(down: +s, lep: -s)` collapses `|\ln D_1| == 0` (`< 1e-45`).
- `PF-3`: Corrupting `N_H - N_V + 29 n_T = 273` by `+1` fails 6D `tr R^4` cancellation.
- `PF-4`: Replacing `Y_lep(R + s 1)` with `Y_down(R + s 1)^T` (wrong sign of `s`) breaks `W-D2 § 3`'s identity by `> 1e-1`.
- `PF-5`: Conjugating the up Higgs (`(S_tilde, S, S)`) destroys `(S, S, S)` CKM alignment on the act line (`min |V_{ii}| < 0.2`).
- `PF-6`: Perturbing `h` away from `h.h = eta^6/4` breaks `B1971` `N3` identity and lifts rate-`1/2` cancellation.

0 of 19.
