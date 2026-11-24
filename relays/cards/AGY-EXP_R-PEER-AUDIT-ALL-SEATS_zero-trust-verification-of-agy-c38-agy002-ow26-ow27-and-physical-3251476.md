# Scope Card: `AGY-EXP_R-PEER-AUDIT-ALL-SEATS` — Zero-Trust Verification & Countercheck of Active Peer Heads `AGY` (`b06c8fc1e`, Cards `C35–C38` & `v7.json`), `AGY-002` (`22b08aff1`, `A2-OW26 v8`, `A2-OW27 v8`, `OW16 v18/v22`, & `LOCK_V2/V3`), and `physical` (`32514763f`, Static Gauge Quartic)

- **Seat / Branch:** `AGY-EXP` (`agy/self-consistent-loop-2026-11-11`)
- **Date:** `2026-11-24`
- **Firewall:** **Strictly `0 of 19`** (`zero empirical PDG, NuFIT, Planck, DESI, or CODATA constants; zero Python float/complex AST literals; zero binary64 casts; zero JSON float tokens; zero imports from frontier/, snappy, or peer scripts`).
- **Pre-Hashed Custody:** Standalone Producer (`relays/r_peer_audit_all_seats_verify/`) and disjoint zero-shared-code Cold-Room Referee (`relays/r_peer_audit_all_seats_referee/`) commit `SCRIPT_SHA256.txt` before execution and commit raw JSON outputs unread alongside `OUTPUT_SHA256.txt`.

## 1. Scientific & Forensic Scope (`4` Modules `PA_1..PA_4`)

1. **`PA_1` — Cryptographic Custody & Chronological Pre-Hash Verification (`AGY` `C35..C38` @ `b06c8fc1e` & `AGY-002` `OW26 v8 / OW27 v8` @ `22b08aff1`):**
   - Verify all `SHA256` manifest entries across `AGY` (`C35..C38`) and `AGY-002` (`OW26 v8`, `OW16 v18`, `OW26 Referee v3`, `OW27 v8`, `OW16 v22`, `OW27 Referee v3`), chronological `git ls-tree` pre-hash ordering (`Referee`), and canonical SHA-256 digests of `B4_UV_MZ_BLIND_LOCK_V2` (`dab1f7...`) and `B4_UV_MZ_BLIND_LOCK_V3` (`ce81cd...`).

2. **`PA_2` — Independent Zero-Shared-Code Countercheck of `AGY` (`C37/C38` & `v7.json`):**
   - Recompute `m11_over_mgut_zero_knob` (`Lobachevsky quadrature` in Producer vs. `Hurwitz zeta` in Referee), conformal $S_{+4}$ $N=60$ `(n_s, r)` (`Newton` vs. `Lambert W_{-1}`), `C38` `2HDM` quartics at $s_*$, `6/6` $G_{\mathrm{SM}}\times\mathrm{U}(1)_\chi$ anomalies + $\nu^c$-omission `(0,0,0,0,5,125)` control (`weights` vs. `32x32 Cl(10)`), symbolic $\operatorname{STr}\mathcal{M}_{Z'_\chi}^2 \equiv 0$, `BL1-F1` $M_{\mathrm{SS}}/A_*^{-1/2}$ & $B_{\mathrm{eff}}$, and forensic catch **`AGY-C38-N1`** ($|\tau_* - \frac{1}{2}|^2 - \frac{1}{4} = 1.70\times 10^{-32}$ on `C38`'s `45`-digit string).

3. **`PA_3` — Independent Zero-Shared-Code Countercheck of `AGY-002` (`OW26 v8` & `OW27 v8` @ `22b08aff1`):**
   - Verify three-seat convergence on $\mathcal{G}^{(s=1/2)}(\tau_8^+)$ (`< 2e-6`), $M=8$ CIM $(8,8,16)$ triple overlaps (`< 1e-10`), closed-form analytic gluino FCNC dilution & exact $\frac{25}{58}$ Bino LSP (`< 1e-10`), symbolic `DISC-V7-2` Sirlin–Zucchini RG invariance (`0`) & `DISC-OW27-1` 5-flavor QED top decoupling $\beta_e^{(t)} = +\frac{16}{9}$, stiff MSSM Boltzmann $Y_B(\tau_8^+)$ (`4th-order Crank-Nicolson` in Producer vs. `L-stable Alexander SDIRK2` in Referee, `< 1e-5`), Borromean $j(\frac{2+i}{5}) = 1728$ (`< 1e-35`), Guardrail-5 catch **`A2-OW26-F1`** (`6`th continuous lever `m_0 / v_EW` shifting $\alpha_3(M_Z)$ by `0.0386`), and pure-math resolution **`A2-OW27-F2`** showing $\Gamma_0(2)$-equivariant $\mathrm{Out}(D_5)$ branch `(3, 0, 2)` hits all `3` blind `OW24-C` PMNS intervals simultaneously where non-equivariant `(3, 2, 0)` gave `0/192`.

4. **`PA_4` — Independent Symbolic Verification of `physical` (`32514763f`):**
   - Verify offset-`2` ratio product `1`, absence of $+1$ interior eigenvalue on $W_2\oplus W_{-2}$, double-return polynomial $(z+1)^2$, and complete-cusp collar scaling $\|F(A_\varepsilon)\|^2 = \mathcal{O}(\varepsilon^5) = o(\varepsilon^4)$ (`cubic Hermite bump` in Producer vs. `quintic C^2 bump` in Referee).

## 2. Planted Controls (`4/4` Producer `PC_PA_1..4` + `4/4` Referee `R_PC_PA_1..4` = `8` New, `122` Cumulative)
1. `PC_PA_1` / `R_PC_PA_1`: Single-byte lock perturbation invalidates `LOCK_V3` SHA-256, and pre-hash `ls-tree` distinguishes pre-run vs. post-run commits.
2. `PC_PA_2` / `R_PC_PA_2`: Omitting $\nu^c$ breaks `grav^2 U(1)_chi = 5` & `[U(1)_chi]^3 = 125`, `C38` semicircle residual sits in `(10^{-34}, 10^{-30})`, and principal Lambert branch $W_0$ fails $y_{60} > 1$.
3. `PC_PA_3` / `R_PC_PA_3`: Non-equivariant `(3, 2, 0)` misses `OW24-C` while equivariant `(3, 0, 2)` hits, `m_0/v_EW` shifts $\alpha_3$ by `> 0.03`, and inverted $\varepsilon_{\mathrm{flav}}$ flips $\operatorname{sign}(Y_B)$.
4. `PC_PA_4` / `R_PC_PA_4`: Fixed-cut $L = \ell$ retains $\mathcal{O}(\varepsilon^4)$ energy (`deg 4`), whereas $L = \ell/\varepsilon$ relaxes to $\mathcal{O}(\varepsilon^5)$ (`deg 5`).
