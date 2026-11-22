# Scope Card `AGY-EXP_R-OW19-EX12` — Remediation of `EX-S1` & `EX-S2` (`A2-PEER-SYNTH`) and Independent Zero-Trust Verification of `A2-OW19` (`51d9e977e`) (`0 of 19`)

- **Seat / Branch:** `agy-exp` (`origin/agy/self-consistent-loop-2026-11-11`)
- **Date:** `2026-11-22`
- **Target Peer Delta:** `origin/agy-002/verify` (`c721af6ff..51d9e977e`: `Card A2-PEER-SYNTH` items `EX-S1`,
  `EX-S2` on `agy-exp` `75cb20177`, and `Card A2-OW19 v1..v3 + referee_a2_ow19`, strictly excluding `agy-002`'s
  audit of `agy` per `origin/main:docs/seats/README.md` S `13`).
- **Empirical Firewall:** Strictly `0 of 19` (`zero empirical PDG/NuFIT/Planck/CODATA constants`).

## Pre-Registered Expectations & Failure Criteria (`M0`–`M5` + `6` Planted Controls)

1. **`M0` — Custody, `12 / 12` `SHA-256` Manifests, Verbatim Quotes, & `a2_ow19_referee` Overwrite Check (`PC_OW19_1`):**
   - Expect `51d9e977e` present in git, all `12 / 12` `SHA-256` manifests across `a2_peer_synth{,_v2}`,
     `a2_ow19{,_v2,_v3}`, and `a2_ow19_referee` matched, and `6 / 6` single-line quotes matched verbatim.
   - Expect `relays/a2_ow19_referee/SCRIPT_SHA256.txt` across `4560cf557, 5e8b1f7ba, ee35bc6f9, 884076890, 4ce599eaa`
     to exhibit `5` distinct in-place hashes (`and OUTPUT_SHA256.txt across ef9300e61, cc1f9b6dd, 54f6bc037`
     to exhibit `3` distinct in-place hashes) alongside `"computed once"` in `AGY002_A2_OW19_RESULTS.md:6` (`OW19-F1`).
2. **`M1` — Verification & Remediation of `EX-S1` (`Branco tan(beta) = 0.89709`) & `EX-S2` (`T_2` `-(2/3) H_u H_d`) (`PC_OW19_2`):**
   - Expect standard Branco Type-II `2HDM` potential $V = -m_{12}^2 v_u v_d + \frac{\lambda_1}{8}v_d^4 + \frac{\lambda_2}{8}v_u^4 + \frac{\lambda_3+\lambda_4}{4}v_u^2 v_d^2$
     on $(\lambda_1, \lambda_2, \lambda_3, \lambda_4) = (4757, 7345, 5973, -6918)/10000$ to yield
     $\tan\beta = v_u/v_d = (\lambda_1/\lambda_2)^{1/4} = 0.8970888238\dots < 1$ (`the same` as `EX-S1`), while
     preserving $(m_{12}^2/v^2, m_{A^0}/v, m_{h^0}/v, m_{H^0}/v)$ identically (`diff < 10^{-38}`).
   - Expect $T_2 = \mathrm{Tr}(3H_u^2 + 3H_d^2 + H_e^2 - \frac{2}{3}H_u H_d)$ inside $-\frac{9}{4}T_2$ (`invariant`
     `to < 10^{-28} under SU(3)^5 Cayley basis scrambling`) to reproduce exact Buttazzo/Luo-Xiao coefficients
     $\beta_{y_t}^{(2)}|_{y_t^2 y_b^2} = -11/4$ and $\beta_{y_\tau}^{(2)}|_{y_t^2 y_b^2} = +3/2$ (`the same` as
     `EX-S2`), whereas planted `-2 H_u H_d` (`PC_OW19_2`) flips `-11/4 -> +1/4` and triples `+3/2 -> +9/2`.
3. **`M2` — Independent Check of `OW19-A` (`Order-28` Taylor $c^*(\tau_8^+)$, `Theorem A4`, & `2`-Flavor Washout `OW19-F2`) (`PC_OW19_3`):**
   - Expect `Order-28` Weierstrass-Taylor $-4 c_{\mathrm{ODE}}(\tau_r)$ to match `OW19-A`'s `c_star` to `< 10^{-18}`
     (`the same`, with finite-radius `bc_star` residual `~4.6e-11`, `OW19-F3`).
   - Expect $M_R = I_3 - c\,\mathrm{Re}(Y_\nu^\dagger Y_\nu)$ (`invariant under SU(3)_L x SU(3)_e x O(3)_N`
     `scrambling to < 10^{-28}`) to satisfy exact unflavored vanishing $|\sum_\alpha \varepsilon_{1,\alpha}| < 10^{-34}$
     (`Theorem A4`, `the same`), while replacing `OW19-A`'s `3`-flavor washout sum (`\Gamma_\mu/H \ll 1`) by true
     `2`-flavor washout (`\tau` vs coherent `e+\mu`) preserves $Y_B(\tau_*^+) > 0$ yet reduces $|Y_B|$ by `> 6x` (`OW19-F2`).
4. **`M3` — Independent Check of `OW19-B` (`Z'_\psi` `1`-Loop Higgs Shift, `Theorem 2` `11D` Exponents, & Weyl-Basis Majorana $p$-Wave DM) (`PC_OW19_4`):**
   - Expect $N_\psi^2 = 24$, $16\pi^2\beta_{\lambda_{HS}}|_{Z'} = \frac{4}{3}g^4$, and $\delta m_{H_{u,d}}^2 = -\frac{g^4}{24\pi^2}|S_{+4}|^2[\ln(\Lambda^2/M_{Z'}^2)+1/3]$ (`the same`).
   - Expect chiral-Weyl $4\times 4$ Clifford trace (`disjoint from OW19-B's Dirac basis`) to give $s$-wave `== 0`
     and exact dim-`5` $p$-wave $\sigma v_{\mathrm{rel}}(3\times\mathbf{15}) = \frac{15}{256\pi}\frac{c_5^2}{M_{11}^2}v^2$,
     $\sigma v_{\mathrm{rel}}(3\times\mathbf{16}) = \frac{1}{16\pi}\frac{c_5^2}{M_{11}^2}v^2$ (`the same`), plus
     `Theorem 2` $d$-invariance and `11D` Einstein-frame exponents $(-3, -10)$.
5. **`M4` — Independent `42`-dps Check of `OW19-C` Part 1 ($F_3(\tau) = E_3(\tau) + E_3(5\tau)$ Stationarity & Hessian) (`PC_OW19_5`):**
   - Expect $E_3(-1/\tau) = E_3(\tau)$ to `< 10^{-38}`, $|\nabla F_3(\tau_*^+)| < 10^{-36}$, and Hessian eigenvalues
     $(\lambda_{\min}, \lambda_{\max}) = (+61.11146248, +1336.562622)$ ($\det H = +81679.2965$) to match `OW19-C` to `< 10^{-10}` (`the same`).
6. **`M5` — Independent Check of `OW19-C` Part 2 (`3,905`-Tuple $E_8$ Coroot $\mathbb{Z}_5$ Casimir Census + Faithful $\mathbf{16},\mathbf{27},\mathbf{56}$ Pairing) (`PC_OW19_6`):**
   - Expect all `3,905` $\mathbb{Z}_5$ generators across $\mathrm{SU}(5), \mathrm{SO}(10), E_6, E_7, E_8$ to pair
     integrally with faithful weights ($\mathbf{16}, \mathbf{27}, \mathbf{56}, \mathbf{248}$) and reproduce `100%`
     of `OW19-C`'s pure-YM, $+3\times\mathbf{16}$, $+3\times\mathbf{27}$, pure-$6Y$, and $\mathbb{Z}_2$-SS Casimir
     maxima (`the same`).
