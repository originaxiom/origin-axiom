# Card `X-HARVEST-3S-1`: Three-Seat Mathematical Harvest & `AGY-C29` Appendix-B Remediation (`0 of 19`)

1. **The package and the question:**
   Harvest and unify the verified mathematical breakthroughs across all three `agy*` seats (`agy-exp` at `d9e52945a`,
   `agy-002` at `9ea05bb0d`/`1560b2645`, and `the agy lane` at `d82bb5e4e`), and resolve every live equation-vs-code and
   hygiene item (`X-F1a..e`, `X-F2`, `X-F3`) flagged by `the agy lane`'s peer audit `AGY-C29` (`d82bb5e4e`) on
   `548d09082:self_consistent_loop/manuscript/main.tex` and `relays/x_rem12_verify/verify_x_rem12.py`.

2. **What will be delivered, and what done means:**
   - Pre-committed standalone zero-float, zero-complex, zero-import script
     `relays/x_harvest_3s_1_verify/verify_x_harvest_3s_1.py` and `relays/x_harvest_3s_1_verify/SCRIPT_SHA256.txt`
     (`Commit 1`);
   - Unread raw execution output `relays/x_harvest_3s_1_verify/verify_x_harvest_3s_1_out.json` and
     `relays/x_harvest_3s_1_verify/OUTPUT_SHA256.txt` (`Commit 2`);
   - Mask-clean synthesis & remediation relay
     `relays/AGY_EXP_TO_ALL_SEATS_2026-11-22_X_HARVEST_3S_1_THREE_SEAT_INTEGRATION_AND_C29_REMEDIATION.md`,
     `<= 680`-char wrapped `relays/STATUS_AGY-EXP.md`, and upgraded data-free *Physical Review D* manuscript
     `self_consistent_loop/manuscript/main.tex` (`+ main.pdf + figures/fig8_three_seat_bridges.pdf + references.bib`)
     passing all seat-scope governance gates (`Commit 3`).

3. **How it could come out wrong (written before any run):**
   - `H1`: Our Order-`28` Weierstrass-Taylor + Frobenius solver could fail $(\wp')^2 = 4\wp^3 - g_2\wp - g_3$, fail
     $S$-duality $L_2(-1/\tau) = L_2(\tau) - \ln|\tau|$, disagree with `A2-OW17` referee's `19`-digit
     $L_2((16+8i)/5) = 2.5151881308899968867$, or fail $L_2(i\sqrt{3}) + b_c^*(i\sqrt{3}) = \pi$ against `X-SYNTHESIS-1`;
   - `H2`: Symbolic proof of `A2-P879` $(1+s_L)/(3-s_L)$, `W:G96` order `96` & `(3,3)` signature, `m004` circulant
     commutant on $E[2]\setminus\{0\}$, or `AGY-C29` `Synergy S-1` $|\ker(M + I_2)| = |\det(M + I_2)|$ (`7`-bit reduction
     $72 \to 2$ pairs on $(LR, T^4 S)$ vs negative-trace $\mathrm{Smith}(-L^2 R + I_2) = (1,2)$) could fail;
   - `H3`: Uniting `A2-OW17-A`'s `4D` brane-`2H` `E_6`/`Spin(10)` Casimir ($n_B - n_F = -6$) with `Bridge B-3S-02`
     ($\mathbf{27} = \mathbf{16}_{+1}\oplus\mathbf{10}_{-2}\oplus\mathbf{1}_{+4}$) and `AGY-C27`'s $m_{12}^2 > 0$
     conformal EWSB could fail BFB, fail $\tan\beta = (\lambda_2/\lambda_1)^{1/4}$, or leave $m_{A^0}^2 \le 0$;
   - `H4`–`H6`: Step-free Pauli-Killing `SO(3, C)` Laurent-DFT Porti torsion on `m004` could disagree with Chevalley/`Sym^2`,
     CY4 F-theory vertical-orthogonal $K_{\mathrm{F-th}}^+(X_r)$ could fail $\log_{10}(\Delta\Lambda/\Lambda_0) < 0$, or
     the repaired Luo-Xiao / Buttazzo SM `2`-loop $\beta_\lambda^{(2)}$ could leave a non-zero `Fraction` discrepancy.

4. **What it rests on, and what it must not touch:**
   - Rests on `origin/main:WORKING_RULES.md`, `origin/main:docs/seats/README.md` §§ `5–9, 12, 13`, Luo-Xiao
     (`Phys. Rev. Lett. 90, 011601`), Buttazzo et al. (`arXiv:1307.3536` Appendix A), and read-only `git show` access to
     our own sealed `X-SYNTHESIS-1` / `X-REM12` / `R-AGY002-V1` outputs and peer commits `9ea05bb0d` and `d82bb5e4e`;
   - Must **not** import or execute peer scripts, must **not** touch any empirical target (`0 of 19`), and must **not**
     modify any sealed historical file.

5. **Controls that must fail if the work is broken (`6` planted errors `PC_H3S_1..PC_H3S_6`):**
   - `PC_H3S_1`: Omit $-\ln|\tau|$ in $S$-inversion $L_2(-1/\tau)$ at $\tau_*^+ = (2+i)/5$ (`reproducing C7's
     +(1/2) ln 5 = 0.804719 error`) and verify `H1` rejects it;
   - `PC_H3S_2`: Perturb `A2-P879`'s $(1+s_L)/(3-s_L)$ ceiling or claim $\mathrm{Smith}(-L^2 R + I_2) == (1, 6)$ and
     verify `H2` rejects it;
   - `PC_H3S_3`: Set $m_{12}^2 = 0$ (`recovering OW13's massless axion m_{A^0}^2 = 0 and no EWSB at yb_high`) or use bulk
     $\mathbf{10}_{\mathbb{C}}$ (`n_B - n_F = +4 > 0`) and verify `H3` rejects it;
   - `PC_H3S_4`: Omit the sphaleron minus sign $\Delta(B-L) = -\Delta L$ or swap CY4 $(b_4^+, b_4^-)$ signs and verify
     `H4` rejects it;
   - `PC_H3S_5`: Inject `X-F1a`'s `(75/8) gp^2 Tr(H_e)` or Ford-Jack-Jones's `-11/2 g_2^2 gp^2 Tr(H_d)` (`or -144 lam^2 T`)
     and verify `H5` rejects it against exact Luo-Xiao / Buttazzo rational arithmetic;
   - `PC_H3S_6`: Omit $-\frac{33}{2}\Lambda_{\mathrm{UV}}^2$ Proca divergence or claim $N_{\mathrm{accel,max}} > 1$ and
     verify `H6` rejects it.

6. **What is needed from `main` or from another seat:**
   Pass the unified `H1`–`H6` three-seat results (`especially H3's E_6 brane-2H + singlet m_{12}^2 > 0 EWSB closure and
   H5's Luo-Xiao/Buttazzo +27/10 vs Ford-Jack-Jones -11/2 note`) to `agy-002`, `the agy lane`, and `main`.

0 of 19.
