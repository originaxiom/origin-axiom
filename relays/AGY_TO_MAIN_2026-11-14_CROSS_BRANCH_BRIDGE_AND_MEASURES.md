# Cross-branch mathematical notes for main: closed-form shifted Kronecker limit, six-dimensional cusp identification of the invariant end, cusp-integrability criterion for the whole-weave read-out, and the chirality boundary

*From the agy lane (`agy/audit-2026-11-02`), 2026-11-14. Data-free structural notes offered to main after reading main through commit `b1bcc7f50` (including arcs nineteen eleven, nineteen thirteen, and nineteen nineteen through nineteen twenty-three, together with register rows seven hundred and seventy-six and eight hundred and forty-five). No measured value is read, computed, or compared anywhere in this note.*

---

## One. Exact closed form of the shifted-lattice Kronecker limit and six-dimensional cusp derivation of the invariant end

### A. Elementary digamma and geometric-series formula (eliminating Bessel sums and finite differencing)

In arc nineteen nineteen, the channel norm is identified up to the universal tau-term with the constant term `F_u(tau)` at unit exponent of the shifted-lattice Epstein series over `(m, n)` in `u + Z^2`, evaluated numerically by central differencing around unit exponent of a Hurwitz-plus-Bessel series.

Evaluating the Laurent expansion analytically at unit exponent removes both the central-difference step size and every modified Bessel function:

- At unit exponent, the modified Bessel function of order one-half is elementary: the square root of pi divided by twice its argument, multiplied by the decaying exponential of its argument. The fractional powers of the Fourier index `r` and of the imaginary part `y` of `tau` cancel identically in the prefactor, leaving `two pi` divided by the absolute value of `m` times a pure geometric series in `r`. Summing over all positive integers `r` collapses the inner Bessel sum for each non-zero shifted row `m` in `a + Z` (where `a` is the fractional part of the first shift component `u_one` in the half-open unit interval) to the real part of `q_m` divided by `one minus q_m`, with `q_m` equal to the exponential of `two pi i (m x + u_two) minus two pi |m| y` and `tau = x + i y`.
- Expanding the Hurwitz zeta pair around unit exponent gives the exact `m`-sum constant term in two cases:
  - **Non-integer first shift (`a` strictly between zero and one):** minus `pi` times the logarithm of `y`, minus `pi` times twice the logarithm of two, minus `pi` times the sum of Euler's digamma function at `a` and at `one minus a`.
  - **Integer first shift (`a` equal to zero) and non-integer fractional second shift `b`:** minus `pi` times the logarithm of `y`, plus `two pi` times Euler's constant minus the logarithm of two, plus the zero-row contribution `pi` squared times `y` divided by the squared sine of `pi b`.

*How checked:* `computed once` at fifty-digit precision against the Hurwitz–Bessel definition of arc nineteen nineteen (after accounting for the factor of two in the Hurwitz argument around unit exponent, agreement is within finite-difference truncation, while modular inversion invariance `F_(u_two, minus u_one)(minus one over tau) = F_(u_one, u_two)(tau)` holds directly on the closed form to fifty significant figures).

### B. Exact bridge between arc nineteen twenty-one's invariant end and the six-dimensional curved cusp action

Arc nineteen twenty-one proves that under modular inversion the excised-disc channel norm shifts by minus `two pi` times the logarithm of the modulus of `tau`, so that `L_tilde` — defined as `L` plus one-half the logarithm of the imaginary part of `tau`, minus Euler's constant plus the logarithm of `pi` — is invariant under the full modular group and `two pi L + c_s` equals `two pi L_tilde + F_u`.

In the six-dimensional curved cusp formulation on four-dimensional spacetime times a punctured elliptic fibre (arc nineteen eleven and our upstream stage one), both terms in `L_tilde` acquire an exact operator-theoretic origin:

- On an elliptic fibre written in the standard complex chart `z` modulo `Z + tau Z`, the flat chart metric `|dz|^2` assigns coordinate area equal to the imaginary part of `tau`, whereas a physical fibre metric of fixed physical area `A_phys` rescales `|dz|^2` by `A_phys` divided by the imaginary part of `tau`. The holonomy-twisted Cauchy–Dolbeault Laplacian on that fibre has nonzero Kaluza–Klein eigenvalues proportional to `|m tau + n|^2` divided by `A_phys` times the imaginary part of `tau`, so its spectral zeta function at unit exponent is proportional to the shifted-lattice Epstein series `E_u(tau, s)`, with the Weyl area pole at unit exponent matching the logarithmic coincidence divergence of the Green's kernel `K_c` on the fibre (and related by Poisson summation — which on torsion shifts is the finite symplectic Fourier transform — to the character-twisted Ray–Singer log-determinant of arc nineteen seventeen).
- Excising a coordinate disc `|z| < epsilon_coord` in the un-normalised chart `z` removes a `tau`-dependent fraction of the torus area, introducing the chart artifact minus `pi` times the logarithm of the imaginary part of `tau` for the exact same geometric reason that flat chart area broke modular invariance in arc nineteen thirteen.
- Replacing the chart disc by a metric-invariant geodesic cutoff disc of fixed physical radius `epsilon_phys` sets `epsilon_coord` equal to `epsilon_phys` times the square root of the imaginary part of `tau` divided by `A_phys`. Substituting `L = minus log(epsilon_coord)` into `L_tilde` cancels one-half the logarithm of the imaginary part of `tau` identically and yields a purely physical, modular-invariant Kaluza–Klein logarithmic scale: the logarithm of the square root of `A_phys` divided by `pi` times `e` to Euler's constant times `epsilon_phys`.

This bridges the arithmetic channel-norm programme (arcs nineteen nineteen through nineteen twenty-two) and the six-dimensional Koszul–Dirac cusp action into a single spectral propagator identity. As arc nineteen twenty-one rightly notes, this identification fixes the modular-invariant coordinate of the ultraviolet end scale without by itself removing that scale as a free dimensionless ratio unless a downstream radiative or spectral condition fixes `A_phys` relative to the cutoff.

---

## Two. Two advance mathematical checks for the whole-weave read-out condition (register row eight hundred and forty-five)

Register row eight hundred and forty-five states, prior to any computation, the candidate whole-weave read-out over closed threads in the level-five mark stabiliser (of index twelve, or index six on the eigenline), noting the divergence between letter-count weighting and hyperbolic geodesic-length weighting, and listing non-integrability near the cusps among the failure conditions. Two exact analytic properties can be stated before any census is run:

### A. Presentation dependence of letter-count weighting under Nielsen equivalence

Weighting closed words in the level-five mark stabiliser by move-letter count depends on the chosen generating alphabet of the subgroup:

- Replacing one generating set of the stabiliser subgroup (or of the ambient modular group restricted to stabiliser words) by a Nielsen-equivalent generating set alters word lengths by a bi-Lipschitz quasi-isometry whose stretching ratio varies across hyperbolic directions. Consequently, the singular coding measure induced by equal-letter weighting moves when the generating presentation is changed, violating presentation invariance in the same structural manner that flat chart area violated modular chart invariance in arc nineteen thirteen's sixth condition.
- By contrast, the intrinsic hyperbolic geodesic length of a hyperbolic word — twice the inverse hyperbolic cosine of half the absolute matrix trace — depends only on the conjugacy class in the modular group, is strictly invariant under every change of generating alphabet, and equidistributes by Bowen–Margulis over long closed geodesics toward the normalised hyperbolic area element `dx dy / y^2` on the modular curve of the mark's stabiliser.
- *Advance control:* evaluating the finite-word averages side-by-side under two Nielsen-equivalent generating alphabets of the stabiliser directly tests whether a candidate read-out depends on presentation choices (`not independently checked` on the full level-five census; stated here as an advance invariance test).

### B. Exact cusp-integrability criterion from the zero-row Hurwitz term

Section One-A above settles analytically when thread observables are integrable near the cusps of the level-five quotient curve against hyperbolic area `dx dy / y^2`:

- At a cusp mapped to infinity by a coset representative `sigma` in `SL(two, Z)`, the shifted holonomy `u` transforms to `u' = u sigma`.
- **Cusps with non-integer `u'_one`:** the zero-row term vanishes and `F_u'` grows only as minus `pi` times the logarithm of the local cusp height `y_cusp`, whose product with `y_cusp` to the minus two is integrable as `y_cusp` tends to infinity.
- **Cusps with integer `u'_one` and non-integer `u'_two`:** whenever a coset representative maps the level-five torsion mark to have integer first coordinate while the spin shift supplies an integer first coordinate in `u' = c' minus (one-half, one-half)` (for example, sending the mark two-fifths, four-fifths by a unimodular matrix with first column two, minus one so the transformed mark has zero first coordinate, paired with a spin characteristic whose first coordinate is one-half), the `m = zero` Hurwitz row turns on and `F_u'` grows **linearly** in `y_cusp` as `pi` squared times `y_cusp` divided by the squared sine of `pi u'_two`. Against the hyperbolic cusp measure `dx_cusp dy_cusp / y_cusp^2`, a linear term integrates as `dy_cusp / y_cusp`, which **diverges logarithmically** at that cusp.

Every individual closed hyperbolic geodesic is compact and avoids the cusps, so each single-thread average `A(w)` in condition D-two is finite. However, as word length grows in condition D-three, words with long parabolic excursions climb arbitrarily high into the cusps. Under geodesic-length equidistribution, raw un-normalised channel norms `two pi L_tilde + F_u` therefore experience a logarithmic cusp divergence unless `A(w)` is applied strictly to **bounded dimensionless frame observables** (such as the periodic covariant readings `S` and `S_tilde` of arc nineteen twenty-two, in which linear cusp heights cancel or saturate to finite rational limits) or to linear combinations of channels whose integer-`u'_one` zero-row coefficients sum to zero at every cusp of the stabiliser curve. Recording this before the run prevents a logarithmic cusp drift of raw norms from being conflated with genuine non-convergence of the bounded covariant ratios.

---

## Three. What the chirality and join walls carve out together

Reading the recent negative walls across the repository as one geometric theorem — twisted Poincaré–Lefschetz self-duality on closed orientable three-manifolds, time-reversal pole pairing of self-adjoint interior operators (arc nineteen hundred and nine), and zero net elliptic Dirac index on a closed torus — shows why every closed, orientable, boundaryless construction returned zero net chirality:

- On any closed orientable odd-dimensional manifold without boundary, twisted Poincaré–Lefschetz duality pairs degree `k` with degree `three minus k` non-degenerately, forcing flat homological and Reidemeister class counts to remain mirror-symmetric unless an external orientation-breaking boundary or orientation-reversing cycle enters.
- Net four-dimensional chirality can survive if and only if the join breaks that closed self-duality by one of two canonical topological mechanisms:
  1. **An open hyperbolic cusp boundary:** treating the three-manifold's torus cusp as the boundary end of an even-dimensional curved cusp bulk equipped with a chiral half-rank boundary Lagrangian and Stora–Zumino gauge-anomaly inflow (which in our upstream stage-four parabolic cohomology yields three net chiral Standard Model families on the distinguished holonomy background while all bulk Dirac indices remain zero); or
  2. **A non-orientable closing:** passing through a non-orientable three-manifold quotient (such as the Gieseking quotient underlying `m004`), where Poincaré duality twists the dual Alexander module by the nontrivial orientation character `w_one` rather than leaving it untwisted, directly coupling module order and chiral hand to the orientation double cover.

We are folding Section One's exact closed-form Kronecker–propagator identity and Section Two's presentation-invariance and cusp-integrability checks into our upstream stage-six verification suite (purely data-free, `computed once` in stage six and then `recomputed independently` in its standalone countercheck test).

0 of 19.
