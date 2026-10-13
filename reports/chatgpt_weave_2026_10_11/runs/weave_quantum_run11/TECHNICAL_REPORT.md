# Quantum realization of the weave — Run 11
## Repository-integrated four-dimensional comparison: exact projective uplift, different metric, and the full zero-mode count

**Date:** 11 October 2026.

**Inputs:** the conversation's Run 10 and the pinned repository sources listed in `REPOSITORY_MAP.md`.

**Scope:** a supplied classical Yang–Mills comparator on a centre-twisted Euclidean four-torus, with an adjoint test Weyl operator. This is not the repository's E8/hyperbolic parent, not an action derived from Origin Axiom, and not a four-dimensional generation or gravity construction. General toron and compactification physics is known prior art.

## Executive result

An explicit connection on a centre-twisted four-torus has commuting compact-direction holonomies whose theta coordinates are exactly the Run 10 projective field. It solves Yang–Mills and is anti-self-dual for an arbitrary common complex shape of the two tori, with their areas independent. Thus a small-fibre limit is compatible with the classical solution.

The map does **not** equate the physical theories. The induced holonomy metric is flat away from four orbifold points, whereas Run 10 used the smooth round CP1 metric. The profile reaches a point where omitted charged gauge modes have zero local compactification mass. There is no uniform scalar-only mass separation established by this reduction.

The rectangular constant-curvature background remains stationary when shapes are detuned, but its charged vector Hessian has lowest eigenvalue `-abs(B1-B2)`. It is unstable unless the two orthonormal flux strengths coincide. This is an instability of that background at a supplied metric, not a dynamical mechanism selecting the metric.

The adjoint complex Weyl index is -2. At the periodic spin structure, the **actual** kernels have dimensions (n_plus,n_minus)=(2,4): six modes in total. The other fifteen spin structures give (0,2). Counting only the index would miss neutral paired modes. Neither number is a generation count.

Repository reading changes the broader plan: existing complete parent backgrounds, conditional L2 comparisons, quotient admission, phase classifications and cubic tests must be reused. In particular, a September strategy's proposed quotient test was already completed in an October successor. It was not rerun here. The current same-action boundary/domain task remains separate and unpaid.

---

## 1. Repository intake and evidence grades

The live branch list and selected source files were fetched, not a complete clone or every file on every branch. The pinned main head is `6c148ddd495d133213140995976ff08849793d5d`; the detailed audit fork is `8b89d8fb247a7c08811e3a3ccfa59a0e742d78a0`. Readings are not producer replays.

The main lift inventory already distinguishes gauge lifting, dimensional extension, and conditional actions. The audit fork has a supplied E8 parent with nonlinear backgrounds, a conditional complete-domain matter interpretation, full gauge-centralizer calculations, and a direct cubic constraint on a specific background. These are more substantial prerequisites than a search for another matching representation. Their analytic claims retain their authored grade; finite tests do not independently certify their infinite-domain proofs.

The quotient-admission successor explicitly admits backgrounds excluded by separate structure and hypercharge lifts, and distinguishes them from additional liftable monomial components. The current roadmap then records the later mode classifications and boundary investigations. Therefore this packet does not rediscover that quotient, rerun the old line scans, or call a phase-family classification open.

`REPOSITORY_MAP.md` gives the paths and historical/successor distinction. The present T4 comparison is not a replacement for their hyperbolic carrier or silver boundary problem. In particular, a closed four-dimensional Atiyah–Singer index is not the boundary-cohomology or complete-domain kernel difference used in those reports.

## 2. Supplied geometry, action and global form

Let (a,b,c,d) be coordinates of period one. The base is the (a,b) torus; the compactification fibre is (c,d). Set

\[
 t_3=\tfrac12\operatorname{diag}(1,-1),\qquad
 \operatorname{tr}(t_3^2)=\tfrac12,
\]

and use Hermitian gauge-field convention `D=d-iA`. The connection is

\[
 \boxed{\mathcal A=2\pi t_3(b\,dc-a\,dd).}
\]

Its curvature is

\[
 \boxed{F=2\pi t_3H,\qquad H=db\wedge dc-da\wedge dd.}
\]

Transitions can be chosen as

\[
 \Omega_a(d)=e^{-2\pi i d t_3},\qquad
 \Omega_b(c)=e^{2\pi i c t_3},\qquad \Omega_c=\Omega_d=I.
\]

They reproduce the connection shifts. Their cocycles are -I on the AD and BC two-tori; all other twist components vanish. They define an honest SO3 bundle, or SU2 theory coupled to the corresponding centre background. They do not define an ordinary fundamental SU2 bundle with unconstrained doublet sections.

The action is

\[
 S_{\rm YM}=\frac1{2g_4^2}\int\sqrt{g}\,
 \operatorname{tr}(F_{\mu\nu}F^{\mu\nu})\,d^4x.
\]

The four-torus, its metric, compactification interpretation, global form, action and coupling are supplied. No spacetime/gravity derivation is inferred.

**Twist placement is essential.** The compactification fibre has F_CD=0 and commuting holonomies. Placing the irreducible Q8 twist on that small fibre instead would give an isolated flat SU2-conjugacy class and no adjoint invariant infinitesimal flat directions. It would not supply the two-dimensional holonomy target used below. This is why mixed base/fibre twists, rather than a literal duplicate of the original punctured fibre, are specified.

These are the known intersecting-twist compactification and toron constructions [H, YY]. The explicit coefficient and global-form comparison is checked here, not claimed as a new solution class.

## 3. Exact Yang–Mills solution for an arbitrary common complex shape

Let `tau=x+iy`, y>0, and let A_B,A_F>0 be independent areas. Use

\[
 ds^2=\frac{A_B}{y}|da+\tau db|^2+
       \frac{A_F}{y}|dc+\tau dd|^2.
\]

The exact tensor calculation gives

\[
 *H=-H,\qquad D^\mu F_{\mu\nu}=0,\qquad D F=0.
\]

No rectangular restriction is used in this Hodge calculation. The areas need not be equal; in particular A_F can be arbitrarily smaller than A_B while the classical self-duality relation remains true.

With orientation da db dc dd,

\[
 \int H\wedge H=-2,
\]

and consequently

\[
 \boxed{Q_4=\frac1{8\pi^2}\int\operatorname{tr}(F\wedge F)=-\frac12,
 \qquad S_{\rm YM}=\frac{4\pi^2}{g_4^2}.}
\]

Reversing the orientation reverses Q and Weyl-index signs, not the action. Run 10 used the positive CP1 charge convention; the comparison is of a chosen orientation, not a selection of handedness.

The mixed pairing is preserved by simultaneously applying any determinant-one integral change of basis to both two-tori: `M^T J M=J`. This is an exact all-word covariance statement for the supplied simultaneous transformation. It does not derive the extra torus or the decision that the original record move also acts on it.

## 4. The holonomy coordinate gives exactly the Run 10 theta profile

The compact-direction holonomies are

\[
 P_C=\operatorname{diag}(e^{i\pi b},e^{-i\pi b}),\qquad
 P_D=\operatorname{diag}(e^{-i\pi a},e^{i\pi a}).
\]

They commute. Write their eigenphases as phi_C=pi b and phi_D=-pi a. The complex eigenvalue coordinate is

\[
 \zeta=\frac{-\phi_D+\tau\phi_C}{2\pi}
       =\frac{a+\tau b}{2}=\frac z2.
\]

The two eigenvalues correspond to zeta and -zeta. Their Weyl quotient is `E_tau/{+/-1}`, with homogeneous theta coordinates

\[
 \mathfrak H_\tau(\zeta)=
 [\theta_3(2\zeta|2\tau):\theta_2(2\zeta|2\tau)].
\]

Substitution yields

\[
 \boxed{\mathfrak H_\tau(z/2)=
 [\theta_3(z|2\tau):\theta_2(z|2\tau)],}
\]

which is the exact Run 10 doublet, projectivized. There is no relative fitted coefficient. The half-period translations reproduce its Pauli-Z and Pauli-X projective actions. Direct theta sums verify the two full periods, reflection, both half-period actions and the gauge-holonomy substitution at three complex shapes.

This construction uses the known theta isomorphism of the holonomy quotient [H]. It matches a classical configuration in complex coordinates. It does not identify a quantum measure, the complete metaplectic coefficient line, or the physical species acted upon by that line.

## 5. Derive the metric instead of importing the round CP1 action

For rectangular fibre lengths L_C,L_D, the Yang–Mills kinetic term for these eigenphases is

\[
 S_{\rm hol}=\frac2{g_4^2}\int
 \left(\frac{L_D}{L_C}|d\phi_C|^2+
       \frac{L_C}{L_D}|d\phi_D|^2\right).
\]

Put rho=i L_D/L_C and zeta=(-phi_D+rho phi_C)/(2pi). Then

\[
 S_{\rm hol}=\frac{8\pi^2}{g_4^2\operatorname{Im}\rho}
 \int|d\zeta|^2.
\]

The target is flat in zeta before the Weyl quotient. In the affine CP1 coordinate

\[
 \xi=f(\zeta)=\theta_2(2\zeta|2\rho)/\theta_3(2\zeta|2\rho),
\]

its metric is

\[
 ds^2_{\rm YM}=C\,|f'(\zeta)|^{-2}|d\xi|^2.
\]

It is flat on its regular set and has cone angle pi at the four images of the half-periods. Near a branch, xi-xi_0 is proportional to zeta squared, so the quotient metric is proportional to `|d xi|^2/|xi-xi_0|`. The smooth round CP1 metric instead has positive regular curvature. No common normalization equates them.

The literature explicitly warns that this reduction is not the standard Fubini–Study sigma model [Y, H]. This packet computes the distinction for the actual theta map. A numerical negative control evaluates the YM-to-round metric ratio at two points and obtains approximately 0.3535786082 and 0.2132217340; it is not constant.

### The projection reaches an extra-light-mode locus

In the rectangular compact directions, an off-diagonal gauge component has local compactification masses

\[
 m_{n,m}^2(a,b)=4\pi^2\left[
 \frac{(n+b)^2}{L_C^2}+\frac{(m-a)^2}{L_D^2}\right].
\]

At integer a,b, the lowest value is zero. This is one of the quotient branch points encountered by the profile. Therefore the background does not stay in a region with a uniform positive mass gap for every omitted charged field. Taking the fibre area small does not remove the exact zero at that point.

This is a local adiabatic mass diagnostic, not a claim that every global fluctuation becomes massless. The full magnetic operator is analyzed separately below. The four-dimensional connection is smooth; the scalar-only coordinate description becomes singular because it has omitted relevant fields.

There is also a physical distinction in the energy density: the four-dimensional curvature here is constant. A nonuniform-looking normalized theta direction does not imply a localized four-dimensional energy lump. The appropriate induced metric compensates the nonlinear coordinate profile.

## 6. Rectangular detuning: a stationary solution need not be stable

For arbitrary rectangular lengths L_A,L_B,L_C,L_D, keep the same connection. It still solves Yang–Mills because its curvature is constant and Abelian. Define

\[
 B_1=\frac{2\pi}{L_A L_D},\qquad B_2=\frac{2\pi}{L_B L_C}.
\]

Its action is

\[
 S=\frac{2\pi^2}{g_4^2}(r+r^{-1}),\qquad
 r=\frac{L_A L_D}{L_B L_C}.
\]

It is anti-self-dual precisely when B_1=B_2, equivalently r=1. This matches the equality of the two complex aspect ratios; it does not require the base and fibre areas to be equal.

A charged scalar has magnetic levels

\[
 \lambda_{n_1n_2}=(2n_1+1)B_1+(2n_2+1)B_2.
\]

In background gauge, the vector fluctuation adds the spin-one shifts

\[
 -2B_1,\quad +2B_1,\quad -2B_2,\quad +2B_2.
\]

Hence

\[
 \boxed{\lambda_{\min}=-|B_1-B_2|.}
\]

The negative-helicity polarization uses a lowest-Landau-level wavefunction, so its divergence is a magnetic annihilation operator and vanishes. It is a physical transverse direction, not a pure-gauge mode: the scalar ghost operator has positive lowest eigenvalue B_1+B_2.

At equality the charged Hessian is nonnegative with zero polarizations. This does not classify the full nonlinear deformation space; higher-order integrability is a separate question. Away from equality the explicit constant-curvature background is unstable. Non-Abelian self-dual solutions on detuned twisted tori are known [AP, AP2]; no such solution is constructed here.

The metric has not been made dynamical. The instability says the gauge field cannot be left at this Abelian saddle for a detuned metric, not that the universe is forced to adjust its geometry until r=1. General toron stability is known prior art [AP].

## 7. Actual adjoint Weyl kernels, not only an index

The complexified adjoint bundle splits as

\[
 (\operatorname{ad}P)_{\mathbb C}=\mathcal O\oplus L\oplus L^{-1},
 \qquad c_1(L)=H.
\]

Since T4 has trivial Pontryagin contribution,

\[
 \operatorname{ind}D_L=\tfrac12\int c_1(L)^2=-1,
 \qquad \operatorname{ind}D_{L^{-1}}=-1.
\]

Thus

\[
 \boxed{\operatorname{ind}D_{\rm ad}=-2=2T(\mathrm{ad})Q_4.}
\]

### Charged and neutral kernels must be counted separately

Each charged line has one unit of magnetic flux in each of two planes. Its orbital ground-state degeneracy is one. The exact Euclidean Clifford calculation leaves one spin polarization, of negative chirality, for each root charge. Thus the charged sector contributes two complex negative-chirality modes.

An independent numerical construction uses, for a positive unit flux on a rectangular two-torus,

\[
 \psi(x,y)=\sum_{n\in\mathbb Z}
 \exp\left(\frac{2\pi i n y}{L_y}
 -\frac B2(x-nL_x)^2\right),\qquad B=2\pi/(L_xL_y).
\]

It verifies the transition conditions and `(D_x+iD_y)psi=0`; conjugation gives negative flux. Taking the product on the AD and BC planes and an explicit four-component spinor verifies the unsquared four-dimensional Dirac equation, not only a determinant of D squared.

The neutral Cartan line has ordinary flat spinors. With periodic boundary conditions on every cycle, it contributes two constant complex spinors of each chirality. Any antiperiodic cycle removes those neutral constants.

| Spin structure | n_plus | n_minus | Difference |
|---|---:|---:|---:|
| All four cycles periodic | 2 | 4 | -2 |
| Any of the other 15 structures | 0 | 2 | -2 |

Flat spin twists preserve the charged magnetic degeneracy. Therefore the periodic problem has **six total zero modes**, not two. This is the known reducible-toron subtlety discussed explicitly in [AP]. That paper's supersymmetric condensate calculation is not imported into this pure-gauge-plus-probe comparator.

These counts are for the rectangular family; the generic common-shape Hodge calculation above is exact, but no separate all-shape full-kernel theorem is claimed here. They are complex Weyl counts before imposing any extra reality condition. They are not a numerical singular-Dirac eigenvalue calculation.

### Which representations are globally allowed?

An ordinary fundamental doublet cannot be put on this SO3 bundle: a transition cocycle acting as -I would not close on it. Extra combined flavour/gauge or U1 data can change that question, but have not been supplied. This obstruction must not be confused with the repository's separately calculated U5/mu5 lifting problem.

For an honest integer-spin-j SO3 representation, the torus index is

\[
 \operatorname{ind}D_j=-\sum_{m=-j}^{j}m^2
 =-\frac{j(j+1)(2j+1)}3.
\]

It is even by pairing m and -m. This is a result for this background and allowed coefficient class, not a general prohibition on an odd number of particle generations.

If T4 is Euclidean spacetime, instanton zero modes are part of tunnelling/correlation amplitudes. If T4 is to be an internal space generating four-dimensional particles, a higher-dimensional parent and its field dictionary must first be supplied. Neither reading follows from the integer index alone.

## 8. What changed and how this rejoins the repository

The Run 10 proposed uplift is now resolved at a precise classical level: a known supplied four-dimensional action admits a connection whose holonomy theta coordinates reproduce that exact projective profile. The physical metric, stability conditions and honest matter bundle substantially qualify the match.

This is not an uplift of the entire round CP1 action, an equality of quantum theories, a metaplectic matter construction, or a derivation of dimensions from OA. In particular, projectivization still removes the scalar line; no full source-T transport on the Weyl kernels is claimed calculated. No measured parameter or gravitational field equation is obtained.

The repository's existing parent work should now remain the main continuity anchor. Its current roadmap prioritizes deriving the same physical core/end variations and charged domain for existing candidates. The tests above are reusable controls: keep global form, compare metrics, test stability rather than stationarity alone, retain paired H0-type modes, and do not transplant a closed index into a boundary-domain problem. They do not discharge those source-specific obligations.

There is no basis for another broad scan of separately lifted lines or for calling the already completed quotient admission a new route. Likewise, constructing another familiar gauge theory would not by itself improve the source-to-physics dictionary.

## 9. Verification and integrity

Commands:

```text
python verify_exact.py
python verify_numerical.py --dps 50
python verify_numerical.py --dps 80
```

The exact script has **40 named checks**, including arbitrary-common-shape Hodge duality, the explicit connection and cocycles, action/charge, full modular covariance of the mixed flux, detuned magnetic Hessian and Clifford kernel, all sixteen spin-structure counts, and an all-integer-spin index formula.

The numerical script has **61 comparisons at each precision**: 59 strict identities and two finite branch-limit tests. It constructs direct theta series and separate magnetic wavefunctions; the latter also check the unsquared four-dimensional Dirac equation.

At 80 decimal digits:

- largest strict normalized residual: `8.306290401665642e-80`;
- largest finite-branch normalized residual: `3.887555046709509e-39`.

These are finite-truncation corroborations, not interval-certified tail bounds. The infinite-dimensional kernel statements rest on the magnetic decomposition and analytic counting, with [AP] as a literature cross-check, not only finite matrix ranks.

All formal exact and numerical scripts passed on their first execution. The plan was written after exploration and literature/repository reading, then locally hashed; it is not blind, externally timestamped, or a repository seal. No repository producer was rerun. Earlier reports and source files were not edited. The stale-strategy correction and retrieval limits are retained in the integration map.

## References and limited roles

[H] Y. Hayashi, T. Misumi, M. Nitta, K. Ohashi and Y. Tanizaki, *Fractional instantons in 2d CP^{N-1} model and 4d Yang–Mills theory with 't Hooft twists*, arXiv:2507.12802v1, especially section 5. Intersecting twists, theta holonomy map, torons and the non-Fubini–Study metric. https://arxiv.org/html/2507.12802v1

[Y] M. Yamazaki, *Relating 't Hooft Anomalies of 4d Pure Yang-Mills and 2d CP^{N-1} Model*, arXiv:1711.04360v2, section 2. The twist is not on the torus of commuting small-fibre holonomies; metric singularities and additional W modes. Its anomaly match is not a complete matter-spectrum construction. https://arxiv.org/html/1711.04360v2

[YY] M. Yamazaki and K. Yonekura, *From 4d Yang–Mills to 2d CP^{N-1} model: IR problem and confinement at weak coupling*, arXiv:1704.05852. Original compactification framework. https://arxiv.org/abs/1704.05852

[AP] M. M. Anber and E. Poppitz, *The gaugino condensate from asymmetric four-torus with twists*, arXiv:2210.13568v3, section 1.2 and appendix B. Toron instability away from self-duality and the six-versus-two reducible-background zero-mode issue. No supersymmetric condensate or its normalization is borrowed as an OA prediction. https://arxiv.org/html/2210.13568v3

[AP2] M. M. Anber and E. Poppitz, *Multi-fractional instantons in SU(N) Yang–Mills theory on the twisted T4*, JHEP 09 (2023) 095, arXiv:2307.04795. Context for different non-Abelian detuned solutions, not a solution constructed by this run. https://arxiv.org/abs/2307.04795

[Repo] Pinned repository paths and evidence boundaries: `REPOSITORY_MAP.md`.

No novelty claim is made for constant-curvature twisted connections, the holonomy quotient, Landau levels, the index theorem or the dimensional-reduction framework. This packet supplies a tested comparison with the conversation's exact profile and integrates its scope with the actual repository programme.
