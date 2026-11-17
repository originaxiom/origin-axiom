# Card `X-FOUNDATION-1` — $E_8$ Pure-$Q$ $\mathbb{Z}_3$-Centre Triality ($k = 3$), Stokes-Compatible $\mathrm{SU}(4)/\mathbb{CP}^3$ Cusp Winding, and `3D` Non-Abelian Callias–Anghel $L^2$ Chiral Localization (`ind = 3`) on Cusped `m004` (`0 of 19`)

- **Seat:** `agy-exp`
- **Campaign / Stage:** `X-FOUNDATION` / `Stage 1` (`Commits 1–4` of `16`)
- **Cross-Seat Scope:** `85318a66f` (`main`), `a5d9ab3c6` (`physical` `PHYSICAL-C7` Discriminator `7` & Full $E_8$ Lift), `358d61786` (`agy-002` `Gate 7B`), `d1c71f255` (`agy` `v17`)
- **Empirical Firewall:** Strictly `0 of 19` (`zero SM empirical values read, imported, or compared; zero float literals and zero complex literals module-wide`).

---

## 1. Mathematical Targets & Falsifiable Gates

1. **`Part 1A` ($E_8$ Pure-$Q$ $\mathbb{Z}_3$-Centre Divisibility $c_1(\mathrm{eff}) = 3\,c_1(\text{full }Q)$ & Stokes-Compatible $\mathrm{SU}(4)$ Bundle on `m004` — `E1_E8PureQTriality_and_StokesSU4Bundle_Gate`):**
   - Construct all `240` roots of $E_8$ and evaluate $Q = \frac{2}{3}(e_0 + e_1 + e_2)$: verify `46` roots have $Q = 0$, `32` colour-singlet $E_6^{\mathrm{cent}}$ spinor roots have $Q = \pm 1$, and `162` colour-charged roots have $Q \in \{\pm \frac{1}{3}, \pm \frac{2}{3}, \pm \frac{4}{3}\}$, so $z_3 = \exp(2\pi i Q)$ has exact order `3` (`trivial on all 78 roots of E_6^{\mathrm{cent}} \oplus A_2^{(C)}, non-trivial on all 162 colour roots`) while $\exp(6\pi i Q) = I$.
   - Verify `PHYSICAL-C7` Discriminator `7`: (i) primitive $c_1 = 1$ lifts through $\mathrm{U}(3) \hookrightarrow \mathrm{SU}(4) \subset E_8$ via $\det E_3 = L^{-1}$ (`closed equatorial loop \mathrm{diag}(e^{i\varphi}, e^{-i\varphi}, 1, 1)`), whereas pure-$Q$ loops $\exp(i k \varphi Q_4)$ close at $\varphi = 2\pi$ **if and only if $3 \mid k$** (`minimal positive pure-Q winding k = 3`, rejecting `k = 1, 2` in `PC_FD1_PureQNonMultipleOf3FailsClosure`); (ii) from the `2`-complex spine presentation of `m004`, verify $H^2(m004; \mathbb{Z}) = 0$ (`rejecting smooth abelian flux k = 3 via Stokes' theorem in PC_FD1_SmoothAbelianFluxViolatesStokesOnM004`), while $\mathrm{SU}(4)$ split $L_{+3} \oplus E_{-3}$ has $\operatorname{Tr}(F) = 3 + 3(-1) = 0$.
2. **`Part 1B` (`3D` Non-Abelian Callias–Anghel Monopole Core & Warped Hyperbolic Cusp $L^2$ Chiral Localization `ind = 3` — `E2_Callias3DChiralLocalization_Index3_Gate`):**
   - Construct and diagonalize two explicit `3D` first-order Callias–Dirac operators without literal index shortcuts:
     - **(i) Non-abelian `3D` core-to-infinity radial Callias operator** across monopole/winding charges $k \in \{0, 1, 2, 3\}$ (`including higher partial waves \kappa_{\mathrm{ang}} \ge 1`), verifying $\dim\ker_{L^2}(\mathcal{D}_+) - \dim\ker_{L^2}(\mathcal{D}_-) = k$ (`exact index = 3 at the minimal E_8 pure-Q unit k = 3`, vs `0` at `k = 0` in `PC_FD1_TrivialWindingZeroChiralIndex`).
     - **(ii) Warped `3D` hyperbolic cusp-neck Callias operator** on $[-L_y, L_y]_y \times E_{\tau = i\sqrt{3}}$ ($ds^2 = dy^2 + e^{-2\max(y,0)}|dz|^2$, flux $k = 3$, $M(y) = m_\infty \tanh(y)$ across Landau levels $n \in \{0, 1, 2\}$), verifying `3` normalizable `4D` left-handed zero modes (`\dim\ker_{L^2}(\mathcal{D}_L) = 3`) and `0` normalizable right-handed zero modes (`\dim\ker_{L^2}(\mathcal{D}_R) = 0`, smallest singular value `> m_\infty / 2` and `10`-trial unitary basis scrambling `< (1/1000)^4`), whereas closing $y$ into a compact circle $S^1_y \times E_\tau$ (`PC_FD1_ClosedCompact3ManifoldVectorLikeZeroIndex`) forces `3` left + `3` right modes (`net chiral index = 3 - 3 = 0`, Witten's odd-dimension no-go).

`0 of 19.`
