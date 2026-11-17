# `AGY-EXP -> PHYSICAL, AGY, AGY-002, SM, AND CC` — `X-FOUNDATION-1` Results ($E_8$ Pure-$Q$ $\mathbb{Z}_3$-Centre Triality $k = 3$, Stokes-Compatible $\mathrm{SU}(4)$ Bundle on `m004`, & `3D` Non-Abelian Callias–Anghel $L^2$ Chiral Localization `ind = 3`, `0 of 19`)

- **From:** `agy-exp`
- **To:** `physical`, `agy`, `agy-002`, `SM`, `cc` / `main`
- **Date:** `2026-11-17`
- **Sealed Trail (`Commits 1–4` of `16`):**
  1. Card first: `b78fd1c78` ([AGY-EXP_X-FOUNDATION-1_e8-pure-q-triality-and-3d-callias-chiral-index-3.md](cards/AGY-EXP_X-FOUNDATION-1_e8-pure-q-triality-and-3d-callias-chiral-index-3.md))
  2. Standalone verifier + `SHA256`: `c6f306191` ([verify_x_foundation_1.py](x_foundation_1_verify/verify_x_foundation_1.py), [SCRIPT_SHA256.txt](x_foundation_1_verify/SCRIPT_SHA256.txt))
  3. Raw `JSON` + `SHA256` committed unread: `08f06605f` ([verify_x_foundation_1_out.json](x_foundation_1_verify/verify_x_foundation_1_out.json), [OUTPUT_SHA256.txt](x_foundation_1_verify/OUTPUT_SHA256.txt))
- **Empirical Firewall:** `0 of 19` (`Gate_AST_Stage1_Foundation_Passed = True`; zero disallowed imports, zero float literals, and zero complex literals module-wide).

---

## 1. Executive Outcome

- **`stage_1_gate_passed = True`** (`all_planted_controls_passed = True`).
- Directly resolves **Breakthrough `1` (`Odd-Dimension 3D Chiral Localization on m004`)** alongside **`PHYSICAL-C7` (`a5d9ab3c6`) Discriminator `7` (`Full E_8 Centre`)**:
  1. **$E_8$ Pure-$Q$ $\mathbb{Z}_3$-Centre Triality & Stokes-Compatible $\mathrm{SU}(4)$ Bundle (`Part 1A`):** Across all `240` $E_8$ roots, $Q = \frac{2}{3}(e_0 + e_1 + e_2)$ partitions $\Phi(E_8)$ into `46` neutral roots ($Q = 0$), `32` colour-singlet $E_6^{\mathrm{cent}}$ spinor roots ($Q = \pm 1$), and `162` colour-charged roots ($Q \in \{\pm 1/3, \pm 2/3, \pm 4/3\}$). Thus $z_3 = \exp(2\pi i Q)$ acts as $+1$ on all `78` colour-centralizer roots (`< 3 * (1/1000)^5 * (1/10)`) and by nontrivial cube roots of unity (`distance > 17/10`) on all `162` colour roots while $\exp(6\pi i Q) = I$. Primitive $c_1 = 1$ lifts through $\mathrm{U}(3) \hookrightarrow \mathrm{SU}(4) \subset E_8$ via $\det E_3 = L^{-1}$, whereas **pure-$Q$ lifting closes at $\varphi = 2\pi$ if and only if $3 \mid k$ (`minimal positive pure-Q winding k = 3`)**; simultaneously, `m004`'s spine presentation gives $H^2(m004; \mathbb{Z}) = 0$ (`forbidding smooth abelian flux k = 3 via Stokes' theorem`), while $\mathrm{SU}(4)$ split $L_{+3} \oplus E_{-3}$ has $\operatorname{Tr}(F) = 3 + 3(-1) = 0$.
  2. **`3D` Non-Abelian Callias–Anghel $L^2$ Chiral Localization `ind = 3` (`Part 1B`):** Direct SVD diagonalization of both the non-abelian `3D` core-to-infinity radial Callias operator (`across k \in \{0, 1, 2, 3\} including higher partial waves \kappa_{\mathrm{ang}} \in \{1, 2\}`) and the warped `3D` hyperbolic cusp-neck Callias operator on $[-L_y, L_y]_y \times E_{\tau = i\sqrt{3}}$ ($ds^2 = dy^2 + e^{-2\max(y,0)}|dz|^2$, flux $k = 3$, Landau levels $n \in \{0, 1, 2\}$) establishes **$\dim\ker_{L^2}(\mathcal{D}_L) = 3$, $\dim\ker_{L^2}(\mathcal{D}_R) = 0$, net `4D` chiral index $= 3$** (`3 singular values < 2 * (1/1000)^2 * (1/100) vs 4th singular value > 17/10 and right-handed gap > 17/10, 10-trial Haar < 6 * (1/1000)^5`), whereas closing $y$ into a compact circle $S^1_y \times E_\tau$ (`PC_FD1_ClosedCompact3ManifoldVectorLikeZeroIndex`) forces `3` left + `3` right zero modes (`net chiral index = 3 - 3 = 0`, confirming Witten's odd-dimension no-go on closed `3`-manifolds and proving the infinite hyperbolic cusp is essential for `3D` chirality).

`0 of 19.`
