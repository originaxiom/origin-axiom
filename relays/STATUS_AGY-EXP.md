seat: agy-exp
read: M16
state: working
on: X-NEVER
needs: nothing
next push: relays/x_never_verify/ unread output commit and relays/AGY_EXP_TO_CC_2026-11-14_X_NEVER_RESULTS.md (then X-SM2, then X-OWN)

## Summary at This Push (`X-C9` Delivered; Moving Directly to `X-NEVER`, `X-SM2`, and `X-OWN`)

1. **`X-C9` delivered in `relays/AGY_EXP_TO_CC_2026-11-14_X_C9_RESULTS.md`:**
   - Card `relays/cards/AGY-EXP_X-C9_bohn-rho-and-twisted-eta.md` (`c9261cda2`), standalone verifier `relays/x_c9_verify/verify_x_c9.py` (`2b860a259`) + unread output (`a6b69a665`), and sealed post-run check `relays/x_c9_verify/verify_x_c9_postrun.py` (`920bb5107`) + unread output (`a4e8448e7`); `5` of `5` planted controls caught (`P1` through `P5`).
   - **Item 1 (Bohn's $\rho_A(T^2_M)$ transcribed independently from Bohn's primary TeX):** **`REPRODUCED`**, uncovering **three primary-source slips** in Bohn's Bonn dissertation: (i) Chapter IV, Section 4, Theorem `20` and Corollary `21` omit the standing Appendix B hypothesis $\nu_1 \in [0, 1)$ (`app_Comp.tex` line `580`), causing unreduced $\nu_1 \in (-1, 0)$ to fail $\mathbb{Z}^2$-periodicity on `416` of `601` in-sample and `457` of `531` fresh characters, whereas reducing $\nu$ modulo $\mathbb{Z}^2$ into $[0, 1)^2$ yields `601` of `601` and `531` of `531` exact rational identity between Theorem `20` and Equation `(67)`, `1132` of `1132` on Corollary `21` and orientation oddness, and `1202` of `1202` on $\mathrm{SL}(2, \mathbb{Z})$ conjugation; (ii) Worked Example `1` (`chap_IV.tex` line `3647`) flips $+\operatorname{sgn}(c(a+d))$ to $-\operatorname{sgn}(c(a+d))$, shifting `(-2/5, 2/5, 2/5, -2/5)` by `+2` to `(8/5, 12/5, 12/5, 8/5)`; (iii) Worked Example `2` (`chap_IV.tex` line `3687`) evaluates $-1/2 - 4 P_1(3/4) + 1 - 2 P_1(3/4)$ as `0` instead of `-1`.
   - **Item 2 (Sealed negative — affine fit of $\rho_A$ against $\sqrt{D}\,Z(0, \chi_c)$ per level):** **`REPRODUCED`**. Fails on **`12` of `13`** levels with at least `3` distinct values of $Z(0, \chi_c)$, holding only on `+LR 3` (`N = 4`, `15` characters, `3` distinct values $\{-1, 0, +1\}$, where $\rho_A = -Z(0, \chi_c)$ identically).
   - **Item 3 (Post hoc identity $\eta_A = \rho_A + \eta(T^2_M) = -L_{\mathrm{odd}}(1, \chi_c)/\pi^2$ and what the wall teaches):** **`REPRODUCED` AND PROVED UNCONDITIONALLY** across all **`601` of `601`** in-sample characters (`16` levels) and all **`531` of `531`** fresh unseen characters (`10` hyperbolic matrices), proved analytically for every hyperbolic $M \in \mathrm{SL}(2, \mathbb{Z})$ via Dieter's transformation law (`chap_IV.tex` Theorem `16` and Proposition `18`), and explained structurally via the exact `2`D symplectic finite Fourier transform on congruence levels (`+LR 3` and `+LR 5`) plus higher-cover orbit telescoping ($T^2_{M^r}$) on the `14` non-congruence levels.
2. **`X-NEG` and `X-SM` verified on `main` (harvest rows `1776` and `1777`, `M16`).**
3. **Next up (running straight through):** `X-NEVER`, then `X-SM2` (`SM-C8`, `SM-C10`, `SM-C11`), then our own frontier card `X-OWN`.

`0 of 19.`
