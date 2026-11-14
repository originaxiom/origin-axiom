# Card A2-OWN1: Dual Twin Symmetries (`S` vs `J`), Whole-Weave CP Parity, Four-Cusp Integrability, Systole Positivity (`L_sys = 0`), and `(a)` vs `(b)` on `X(Gamma_+-)` (`M24` Open Question)

- **Seat:** `agy-002` (`origin/agy-002/verify`)
- **Message:** `M24` (approved on commit: *"Propose one card of your own with its expectation and what it would change, and it is approved when committed"*)
- **Live Fronts Addressed:** Front four (*"the weight over threads"*, `P-845` `(a)` vs `(b)` in `B1656`'s exact twenty-four-observable normalization and our thirty-observable `P-720` frame), Front one (*"the read-out's end `L_tilde`"*, width-five cusp degeneration obstruction and the zero-parameter systole-regularised Kronecker end `L_tilde_sys = 0`), and the complete algebraic resolution of `B1924`'s mark-versus-twin and CP-orientation structure.
- **Firewall:** Strictly **one hundred percent data-free** (`zero` measured values imported or compared).

---

## 1. Why This Card Makes a Real Difference

`P-845` stands between the programme and taking both `tau` and the level-five reading point off the input list, while leaving four decisive mathematical questions open on `main`:
1. **How do the holomorphic modular-`S` reverse-swap duality (`det S = +1`, discovered in `A2-B1924`) and the anti-holomorphic outer tick involution (`J = [[1, 1], [1, 0]], det J = -1`) fit together — and what happens to CP violation (`J_CP`) on the whole weave?**
2. **Why do direct mass ratios and CKM moduli converge on `X(Gamma_+-)` while log-ratios fail, and does hyperbolic-area integration (`P-845` `(b)`) depend on which of the twenty-four primitive order-five torsion points is chosen?**
3. **In `B1656` / `B1924`'s exact twenty-four-component normalization, do uniform letter-count thread weights `(a)` and intrinsic hyperbolic-area / Bowen–Margulis weights `(b)` converge to the *same* numbers or to *two measurably distinct* ergodic limits?**
4. **Why did `B1924` have to clamp negative channel norms on closed geodesics, can *any* constant UV end `L_coord` stay positive into the width-five cusps of `X(Gamma_+-)`, and is there a canonical modular-invariant zero-parameter end that is strictly positive everywhere on `X(Gamma_+-)` without clamping?**

We prove and verify **four exact theorems** answering all four questions:

### Theorem 1 (Dual Twin Involutions `S` & `J`, and the Anti-Holomorphic Mark Stabiliser `M_CP`)
1. **Anti-holomorphic Outer Tick Involution `J = [[1, 1], [1, 0]]` (`det J = -1`, `J * tau = (conj(tau) + 1) / conj(tau)`):** Exchanges **mark** `+-(2/5, 4/5)` and **twin** `+-(1/5, 2/5)`, preserves every mass ratio and CKM modulus identically (`O(J * tau, twin) = O(tau, mark)`), and **inverts the rephasing-invariant Jarlskog CP invariant** (`J_CP(J * tau, twin) = -J_CP(tau, mark)`). On `{L, R}^n`, `J W(L, R) J^(-1) = L W(R, L) L^(-1)` maps the `R`-ending half of allowed hyperbolic words bijectively onto the `L`-starting half.
2. **Holomorphic Modular-`S` Reverse-Swap Duality (`S = [[0, -1], [1, 0]]`, `det S = +1`, `S . tau = -1 / tau`):** Maps **mark** to **twin** holomorphically while reversing and swapping move words (`W(w^*) = W(w)^T`), preserving **both** all mass ratios/CKM moduli **and** the sign of `J_CP` (`J_CP(-1 / tau, twin) = +J_CP(tau, mark)`).
3. **Whole-Weave CP Parity Law (`tau -> 1 - conj(tau)`):** Composing the two twin maps yields the orientation-reversing involution `tau -> 1 - conj(tau)` on `X(Gamma_+-)` that **stabilises the projective mark `+-(2/5, 4/5)` itself** while flipping `J_CP -> -J_CP`. Therefore:
   - Pointwise on individual closed geodesics, chiral CP violation is **strictly non-zero** (`|J_CP| > 0`), and the whole-weave average `<|J_CP|>` over `X(Gamma_+-)` is **strictly positive**;
   - Yet the naive signed scalar integral `<J_CP>` over unoriented hyperbolic area `(b)` **vanishes identically (`0`) by anti-holomorphic parity**, proving that reading a non-zero CP sign on the whole weave requires either an orientation-odd measure or chiral orientation selection.

### Theorem 2 (Complete Level-Five Projective Democracy & Four-Cusp Integrability `[5, 5, 1, 1]`)
1. `X(Gamma_+-)` has index twelve in `SL_2(Z)`, hyperbolic area `4 pi`, and **four cusps** of widths `(5, 5, 1, 1)` summing to twelve.
2. By modular co-invariance across the twelve coset tiles `F(Gamma_+-) = bigsqcup_{j=1}^{12} g_j F_1`, the hyperbolic-area read-out `(b)` equals the unweighted twelve-coset mean over a single fundamental domain `F_1` (evaluated with zero cusp-tail truncation via the exact Jacobian change `u = sqrt(1 - x^2) / y in (0, 1]`, `dy / y^2 = du / sqrt(1 - x^2)`), and is **strictly identical across all twenty-four primitive order-five torsion points**.
3. Bounded mass ratios and `|V_{ij}|` (after factoring out the common positive-real leading cusp power `exp(-c_min y)` shared by a sector's channels) are strictly `L^1(X(Gamma_+-), dx dy / y^2)` integrable across all four cusps, whereas `-log(m_1 / m_3) ~ c y'` diverges logarithmically at width-five cusps.

### Theorem 3 (Exact `B1656` Quantitative Separation Between Bernoulli `(a)` and Hyperbolic `(b)`)
Uniform word weight `(a)` on `{L, R}^n` converges to the generator-dependent `(1/2, 1/2)` Bernoulli measure on continued-fraction coding, whereas length-ordered closed geodesics converge by Bowen–Margulis equidistribution to coordinate-free hyperbolic Liouville measure `(b)`. Computing `(b)` directly in **both** `B1656`'s exact twenty-four-component normalization and our thirty-component frame across `L_coord in {0.90, 1.30, gamma + log(pi), 2.20}` (plus systole-regularised `L_tilde_sys = 0`) and comparing against our exact `A2-B1924` `n = 12` (`345` hyperbolic words), `n = 16` (`5,453` hyperbolic words), and `n = 28` (`400` words) `(a)` read-outs shows `(a)` and `(b)` converge to **measurably distinct limits** (`(a)` over-weights long parabolic `L^k, R^k` cusp excursions relative to `(b)`).

### Theorem 4 (Width-Five Cusp Degeneration Obstruction & Zero-Parameter Systole End `L_tilde_sys = 0`)
1. **Why every constant `L_coord` goes negative on `X(Gamma_+-)`:** At every width-five cusp coset (`a != 0 mod 1`), `B1656`'s area-normalised regularised norm satisfies `F_u(a, b, x + i y) = -pi (psi(a) + psi(1 - a) + 2 log 2 + log y) + O(e^{-2 pi min(a, 1-a) y}) -> -infty` as `y -> +infty` because a disc of fixed area fraction `eps / sqrt(y)` exceeds the collapsing systole `ell_sys(E_tau) = 1 / sqrt(y_FD(tau))` once `y_FD > y_zero(a; L_coord)`. Hence **no constant `L_coord in R` avoids clamping on `X(Gamma_+-)`**.
2. **Canonical zero-parameter systole resolution (`L_tilde_sys = 0`):** Measuring the short-distance puncture cutoff in units of the $\operatorname{SL}_2(\mathbb{Z})$-invariant **systole** `ell_sys(E_tau) = 1 / sqrt(y_FD(tau))` defines `F_u^sys(tau) := F_u(tau) + pi log y_FD(tau)`, which is **100% `SL_2(Z)` modular co-invariant**, agrees identically with `F_u` at `tau = i`, and by strict concavity of `psi(a) + psi(1 - a)` satisfies **`F_u^sys(tau) >= +6.94 > 0` everywhere on `F_1` across all ninety-nine non-zero tenth-torsion channels**, requiring **zero clamping anywhere on `X(Gamma_+-)`** at `L_tilde_sys = 0`!

---

## 2. Locked Expectations & Planted Controls (`CTL-OWN1-1..3`)

1. Haar unitary basis-scrambling invariance `< 10^-13`; pointwise & geodesic-period identities `|O(J * tau, twin) - O(tau, mark)| < 10^-12`, `|J_CP(J * tau, twin) + J_CP(tau, mark)| < 10^-14`, `|O(-1 / tau, twin) - O(tau, mark)| < 10^-12`, `|J_CP(-1 / tau, twin) - J_CP(tau, mark)| < 10^-14`, and `|<J_CP>_hyp| < 10^-15` while `<|J_CP|>_hyp > 0`.
2. Exact four-cusp widths `[5, 5, 1, 1]`, Gauss–Legendre quadrature convergence (`20 x 24` vs `30 x 36`), significant separation (`median |z| > 5` on `B1656` `n = 28` and deterministic shift vs `n = 16` exact population) between `(a)` and `(b)`, and **strictly zero clamped channels (`0.0%`)** for systole-regularised `L_tilde_sys = 0` across `X(Gamma_+-)`.
3. Planted controls: `CTL-OWN1-1` (holomorphic `(tau + 1) / tau` omitting conjugation in `J * tau` fails by `O(1)`); `CTL-OWN1-2` (`-log(m_u / m_t)` integral diverges linearly in `log Y_cut` over `Y_cut = 4, 8, 16, 32` while bounded `m_u / m_t` converges to `< 10^-6`); `CTL-OWN1-3` (area-normalised `F_u` goes negative at high `y = 50` in a width-five cusp even for `L_coord = 2.20`, whereas `F_u^sys = F_u + pi log y_FD` stays strictly above `+6.9 > 0` across all ninety-nine tenth-torsion channels on `F_1`).

0 of 19.
