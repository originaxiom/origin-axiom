# Scope Card `AGY-EXP_R-3S-FINAL` — Zero-Trust Delta Audit of `agy` (`528ef1cf5`, `AGY-C26..C30` & `v4.json`) and `agy-002` (`c721af6ff`, `A2-OW17..OW18` & `A2-OW16 v5`) (`0 of 19`)

- **Seat / Branch:** `agy-exp` (`origin/agy/self-consistent-loop-2026-11-11`)
- **Date:** `2026-11-22`
- **Target Peer Windows:**
  1. `origin/agy/cusp-action-2026-11-20` (`6f285488c..528ef1cf5`: `AGY-C26`, `AGY-C27`, `AGY-C28`,
     `AGY-C30`, and `blind_predictions_full_toe_v4.json`, excluding peer-review cards `C25`/`C29` per
     `origin/main:docs/seats/README.md` § `13`);
  2. `origin/agy-002/verify` (`ff243a545..c721af6ff`: `A2-OW17`, `A2-OW18 v1..v3 + referee`,
     `A2-OW16 v5`, and travel-everywhere notices, excluding peer-review files per § `13`).
- **Empirical Firewall:** Strictly `0 of 19` (`zero empirical PDG/NuFIT/Planck/CODATA constants`).

## Pre-Registered Expectations & Failure Criteria (`D0`–`D5` + `6` Planted Faults)

1. **`D0` — Custody, In-Place Referee Overwrite Detection, & Verbatim Quotes (`PC_R3S_1`):**
   - Expect `528ef1cf5` (`agy`) and `c721af6ff` (`agy-002`) present in git and `16 / 16` exact
     single-line quotes matched verbatim.
   - Expect `git show a354fb719:relays/a2_ow18_referee/SCRIPT_SHA256.txt` vs `1620323c0` to expose an
     in-place overwrite of a sealed referee script and hash manifest on `agy-002`, and `c30:964` vs
     `AGY_C30` card line `26` (`> 2/25` vs `> 40/100`) plus `c26/first_run_err.txt` (`2` crashes labeled
     `computed once`) on `agy`. Failure if any quote misses or `PC_R3S_1` fails to catch a 1-char tamper.
2. **`D1` — `AGY-C30` Gauged $\mathrm{U}(1)_\psi$ $M_R \equiv 0$ Self-Contradiction, `w_WL` `0`-Spinor Kill, & Zombie Horizons (`PC_R3S_2`):**
   - Expect exact integer charge arithmetic on $\mathbf{27} = \mathbf{16}_{+1}\oplus\mathbf{10}_{-2}\oplus\mathbf{1}_{+4}$
     (`anomaly-free IC1 => \Delta Q_\psi^{\mathrm{inst}} = 0`) with scalars solely in $\mathbf{10}_{-2}$ and
     $S_{+4} \in \mathbf{1}_{+4}$ to leave $Q_\psi(N_R^c N_R^c) = +2 \not\equiv 0 \pmod 4$ (`4n + 2 != 0`
     for all $n \in \mathbb{Z}$, forcing $M_R \equiv 0$, whereas giving VEV to $(\mathbf{16}_{+1})_H$ has
     $P_M = -1$, breaking `IC3` dark-matter stability), while $|S_{+4}|^2(|H_u|^2+|H_d|^2)$ has $Q_\psi = 0$
     and dimension `4` (`vs dimension-3 S_{+4}H_u H_d`).
   - Expect `c26:261`'s `w_wl` to leave `0 / 128` surviving chiral spinor roots $(\pm 1/2)^8$ of $E_8$,
     and `c30:618-619,729` to retain the retracted $Q_1 = 1/25$ horizons $t_\nu = -16\pi/5, t_{\mathrm{EW}} = -48\pi/5$
     (`vs minimal T^4 toron Q = 1/5 giving S = 16\pi`). Failure if `PC_R3S_2` fails.
3. **`D2` — `AGY-C30` `9`-Digit `L_2` Discretization Noise in `30`-Digit `v4.json` & Tautological `R2` Certificate (`PC_R3S_3`):**
   - Expect our `Order-28` Weierstrass–Taylor + `50`-term geometric Frobenius solver (`r24 vs r36 < 10^{-30}`)
     to prove `v4.json`'s `30`-digit `cusp_robin_bc_star_tau8 = 0.626404524065023558402877750759` differs
     from true $\pi - L_2(\tau_8^+) = 0.626404522699796351793995279...$ by `> 1.3e-9` (`corrupting 22 of 30`
     sealed digits), while `c30:222-224` pre-reduces `-1/tau8_pos` (`|-1/tau8_pos| = \sqrt{5}/8 < 1`) back
     to `tau8_pos` before running the ODE (`making R2 = 2.06e-41 a roundoff tautology`), and
     `c30_countercheck.py:755-772` echoes `8` certificates without recomputing them.
4. **`D3` — `Synergy S-1` Exact $|P_5\times P_6| = 144$, Conjugacy Non-Invariance of $\ker(M + I_2)$, & Broken $w \sim -w$ (`PC_R3S_4`):**
   - Expect exact inclusion–exclusion to give $|P_5| = 12$ and $|P_6| = 12$, hence $|P_5\times P_6| = 144$
     (`differs` from `c30:857`'s `12 * 6 = 72` and `verify_a2_ow18_v3.py`'s double-divided $\log_2(72/2) = 5.17$
     bits; exact pair ratio is $144 / 2 = 72 \implies \log_2 72 = 6.169925...$ bits).
   - Expect $\ker(M + I_2) \pmod{\mathbb{Z}^2}$ to vary across $\mathrm{SL}(2,\mathbb{Z})$ conjugates
     (`T^3 S` gives `span(1/5, 1/5) != span(1/5, 2/5)`; Lyndon `L^2 R, LR^2` give `±(2/3, 1/6), ±(1/6, 1/3) != ±(1/6, 1/6)`),
     and coherent linear weave $\omega_3 Y(p_3) + \omega_4 Y(p_4)$ (`invariant to < 10^{-25} under SU(3)^3`
     basis scrambling) at `(-p_3, +p_4)` vs `(+p_3, +p_4)` to shift $|V_{cb}|$ by `> 1/10` (`refuting w ~ -w`
     invariance `IC7`), plus `2`-flavor vs `3`-flavor leptogenesis washout inflation (`\Gamma_\mu / H < 10^{-3}`).
5. **`D4` — `AGY-002` `OW18-A` `1HDM` vs `2HDM` RGE Model Error & Producer-vs-Referee Matrix-Order Bug (`PC_R3S_5`):**
   - Expect `verify_a2_ow18_v3.py:763` (`-3/2 Hd Yu`, `b_1 = 41/10, b_2 = -19/6`) to implement `1HDM` SM
     RGEs rather than `Type-II 2HDM` (`+1/2 Hd Yu`, `b_1 = 21/5, b_2 = -3`), flipping the 1-loop CKM
     running sign, and Producer (`-HuHd - 1/4 HdHu`) vs Referee (`-SdSu - 1/4 SuSd`) to differ by exact
     nonzero $\frac{3}{4}[H_d, H_u]Y_u$ on non-commuting Yukawa matrices.
6. **`D5` — `AGY-002` `OW18-B` Surviving Chimera/Hybrid FRG, Prose Higgs Mass Fabrication, & `OW16 v5` Audit (`PC_R3S_6`):**
   - Expect `verify_a2_ow18_v3.py:1082-1083, 1120` to retain retracted hybrid `f_W = +1` and Chimera
     `fl_s10_dD` inside `G_SM 2HDM`; replacing `f_W = +1` (`M_g = +8`, `disc = -6.1386 < 0`) with consistent
     Type-I `f_W = -1/2` (`M_g = -64`) flips `G_SM 2HDM` discriminant to `+789.61 > 0` (`2` negative real
     roots). Expect `AGY002_A2_OW18_RESULTS.md:23`'s prose `m_{H^0}/v = 0.95547910` and
     `m_{H^{+-}}/v = 0.94624861` to exceed sealed JSON `0.75235978` and `0.75265612` by `> 25%`, `3 x 16_{+1}`
     alone to violate $\mathrm{U}(1)_\psi$ anomaly cancellation ($\mathrm{Tr}\,Q_\psi = +48 \neq 0$), and
     `OBS-01` (`"orbital stability + conformal/chiral anomaly"`) to have `0` computations on `c721af6ff`.
