# Quantum realization of the weave — Run 10
## A dynamical projective record field: exact fractional instanton, stability, and the obstruction to a full real frame

**Date:** 11 October 2026.  
**Source basis:** the supplied Run 9 report, especially its §7 reference-field diagnostic, and *A Weave of Two Records*, §§1–4 and §7. Earlier run formulas are used only for a declared projective comparison.  
**Scope:** a newly specified two-dimensional nonlinear sigma model in the original fixed projective quaternion background. Analytic classical field equations, topology, stability and bosonic zero modes are calculated. This is not a continuation of the SO(5) coset with unchanged matter content, not a quantum determination of the full source triplet, and not a four-dimensional or gravitational completion.

## Executive result

A smooth, everywhere-invertible **real** colour–flavour frame cannot exist on the compact torus with the smooth adjoint extension of the record background. Its associated oriented rank-three bundle has nonzero second Stiefel–Whitney class. This strengthens Run 9's parallel-frame restriction, but only for the stated real, compact, regular-extension problem.

A weaker object does exist: a unit projective direction field. In the explicitly added CP1/O(3) sigma model, the theta doublet already encountered in the record calculation gives an exact minimum-action configuration:

\[
 w(z;\tau)=\begin{pmatrix}\theta_3(z|2\tau)\\\theta_2(z|2\tau)\end{pmatrix},
 \qquad n_a=\frac{w^\dagger\sigma_a w}{w^\dagger w}.
\]

It obeys the original quaternion rotations around both torus cycles, satisfies the nonlinear equation of motion, and has

\[
 Q=\frac12,\qquad S_{\rm kin}=\frac{2\pi}{g^2}.
\]

The Hessian has no negative directions within the fixed smooth topological sector. Its kernel has **one complex / two real bosonic collective coordinates**, the translations. It does not yield three fermion zero modes.

The solution is not asserted to be new. Fractional CP(N−1) lumps on shift–clock twisted tori, their moduli, and their relation to certain compactified Yang–Mills constructions are established in [H]. The calculation here independently specializes them to the record matrices, derives the charge and stability directly, and distinguishes a true field solution from a full flavour-frame or quantum-triplet identification.

The chosen sigma-model action and interpretation of the torus as a field-theory surface are **new physical hypotheses**. The original manuscript does not select them.

---

## 1. What was asked after Run 9, and what is changed here

Run 9 found that the original colour/geometry moves do not automatically rotate the new flavour triplet after Gauss projection. It also proved that a covariantly constant real adjoint-by-flavour matrix M, with trivial flavour holonomy, must vanish in the specified background. A nonconstant reference field was left as a possible next hypothesis.

This run does not assign the desired metaplectic matrices to a new flavour index. It first tests whether a full smooth real frame is possible, then explicitly replaces that impossible object by a **single projective direction**, not by a secretly equivalent triad.

The new model choices are:

1. The adjoint record connection is a fixed background for a global SO(3) symmetry. Its orientation is not integrated over as the old colour gauge redundancy. Covariance under changing background frames remains, but the old colour Gauss-law projection is not part of this new model.
2. The adjoint fields extend smoothly across the former puncture. Central −I acts trivially on them. The fundamental punctured bundle and its E-plus Dirac domain are not claimed to be unchanged.
3. The dynamical target is CP1, equivalently a real unit vector n in the sphere bundle of the adjoint rank-three bundle. Homogeneous coordinates have their usual local U(1) redundancy. This U(1) is not the old SU(2) gauge theory.
4. The round SO(3)-invariant two-derivative sigma-model action is used, with an unfixed coupling g and an optional topological angle vartheta. No additional potential, higher-derivative term, eta prefactor, or matter multiplet is introduced.
5. The torus is the Euclidean two-dimensional domain of this test theory. Neither its interpretation as physical spacetime nor its identification with an internal compactification of our universe is derived.

Given a CP1 target and SO(3) invariance, the round metric is fixed up to an overall scale; the coupling retains that freedom. Choosing CP1 and the two-derivative truncation is nevertheless additional input.

## 2. A stronger obstruction to a full smooth real frame

Use a Pauli-axis convention with projective quaternion holonomies lifted by

\[
 A=i\sigma_3,\qquad B=i\sigma_1.
\]

This is equivalent to the original quaternion pair by a fixed unitary basis choice and harmless signs. Its adjoint rotations are

\[
 Q_A=\operatorname{diag}(-1,-1,+1),\qquad
 Q_B=\operatorname{diag}(+1,-1,-1).
\]

They commute in SO(3), but their SU(2) lifts anticommute. Let a,b be the two generators of H1(T2;F2). The three real sign lines have first classes

\[
 a,\quad a+b,\quad b.
\]

The Whitney product gives

\[
 w(E)=(1+a)(1+a+b)(1+b)=1+ab,
\]

since a2=b2=0 on the torus. Thus

\[
 w_1(E)=0,\qquad \int_{T^2}w_2(E)=1.
\]

If a smooth real 3×3 matrix M gave an invertible map from a trivial flavour bundle to E at every point, its three columns would be a global frame, implying E is trivial. That contradicts w2(E)≠0. Therefore **every such real frame must lose rank somewhere**, even when it is not parallel.

This is stronger than Run 9's constant/parallel statement and independent of a scalar potential or field equation.

### Boundaries of this obstruction

- It is about the compact smooth adjoint extension. On a genuinely punctured torus H2 vanishes; a frame may exist with nontrivial winding or singular boundary behavior at the puncture. Such end data must be retained rather than discarded.
- It is about a real frame. Complexifying E changes the classification: w2 of the real bundle is not by itself an obstruction to an arbitrary complex frame.
- It does not forbid a single nowhere-zero direction in E. An oriented rank-three bundle over a surface can have one such section while its perpendicular two-plane bundle remains nontrivial.
- It does not show that every possible dynamical colour–flavour mechanism fails.

## 3. The explicitly specified nonlinear action

Let n be a section of the associated unit sphere bundle, locally satisfying n·n=1. In a flat record frame on the covering plane, impose

\[
 n(z+1)=Q_A n(z),\qquad n(z+\tau)=Q_B n(z),\qquad \Im\tau>0.
\]

The local derivatives below are background-covariant derivatives; in this flat frame they are ordinary derivatives. Set

\[
 S_E[n]=\frac{1}{2g^2}\int_{T^2}d^2x\,
 (|D_xn|^2+|D_yn|^2)-i\vartheta Q[n],
\]

\[
 Q[n]=\frac{1}{4\pi}\int n\cdot(D_xn\times D_yn)\,d^2x.
\]

The topological density is globally defined because all transition matrices are constant proper rotations. The background is flat. In more general curved SO(3) backgrounds the appropriate gauged topological density must include the background-curvature terms; no such extra case is silently used here.

The Euler–Lagrange equation of the kinetic part is

\[
 D_x^2n+D_y^2n+(|D_xn|^2+|D_yn|^2)n=0.
\]

The standard Bogomolny completion [BP] is

\[
 S_{\rm kin}=\frac{1}{2g^2}\int|D_xn+n\times D_yn|^2\,d^2x
 +\frac{4\pi Q}{g^2}.
\]

Thus positive-charge solutions of the first-order equation

\[
 D_xn+n\times D_yn=0
\]

are absolute minima within their smooth fixed topological sector. The reverse sign treats negative charge. The term “BPS” here names saturation of this square bound; supersymmetry is not assumed.

## 4. Exact solution from the theta doublet

Theta arguments have period one, and q=exp(2 pi i tau). Define

\[
 u=\theta_3(z|2\tau),\quad v=\theta_2(z|2\tau),\quad N=|u|^2+|v|^2,
\]

\[
 n=\frac{1}{N}\bigl(2\Re(\bar u v),\ 2\Im(\bar u v),\ |u|^2-|v|^2\bigr).
\]

The theta transformation identities [D] give

\[
 w(z+1)=\sigma_3w(z),
\]

\[
 w(z+\tau)=e^{-\pi i\tau/2-\pi iz}\sigma_1w(z).
\]

Scalar factors cancel in n, giving precisely the two required adjoint twists. The scalar transition in the second equation compensates the anticommutation of the two spinor matrices. It is therefore not legitimate to interpret the normalized homogeneous-coordinate U(1) connection as an ordinary independent charge-one line bundle with unrestricted SU(2) lift. The combined twisted structure is essential.

### Smoothness

Theta3(z|2tau) has zeros at 1/2+tau modulo Z+2tau Z, while theta2(z|2tau) has zeros at 1/2 modulo that lattice. They never vanish simultaneously for Im tau>0. Hence N>0 and n is everywhere smooth, including at z=0.

The earlier geometric spinor profile was

\[
 s(z|\tau)=w(z|\tau)/\sqrt{\theta_1(z|\tau)}.
\]

The projectors agree exactly:

\[
 \frac{ss^\dagger}{s^\dagger s}=\frac{ww^\dagger}{w^\dagger w}.
\]

This is a projective identification. It does not turn the sigma model into the old chiral fermion model, preserve the old puncture domain, or identify their quantum determinants.

### Field equation

The ratio v/u is locally holomorphic. Substituting the normalized homogeneous coordinates into the first-order equation gives

\[
 D_xn+n\times D_yn=0.
\]

Therefore the nonlinear second-order equation holds. The code checks both independently using derivatives of the actual normalized three-vector; it does not merely check that v/u is holomorphic.

A useful exact identity, also verified independently, is

\[
 u v'-v u'=-\pi\eta(\tau)^3\theta_1(z|\tau).
\]

It follows by comparing the quasi-periods and zeros of the two sides, and fixing the constant at a half-period. In particular, the texture is smooth and has a critical point at the location that was the spinor puncture. It is not a divergent delta-function core.

## 5. Half-integer topological charge is calculated, not inferred from a plot

For a holomorphic projective field,

\[
 q(x)=\frac{1}{4\pi}\Delta\log N
 =\frac{|u v'-v u'|^2}{\pi N^2}.
\]

Write tau=tau1+i tau2, z=x+i y. The norm satisfies

\[
 \log N(z+1)=\log N(z),
\]

\[
 \log N(z+\tau)-\log N(z)=\pi\tau_2+2\pi y.
\]

Consequently

\[
 p(z)=\log N(z)-\frac{\pi y^2}{\tau_2}
\]

is periodic on the torus. The integral of its Laplacian is zero, whereas

\[
 \int_{T^2}\Delta\left(\frac{\pi y^2}{\tau_2}\right)d^2x=2\pi.
\]

Therefore

\[
 \boxed{Q=\frac12,\qquad S_{\rm kin}=\frac{2\pi}{g^2}.}
\]

The half-integer value is consistent because n is a **twisted section**, not an ordinary globally defined periodic map T2→S2.

More generally, the perpendicular oriented plane bundle n-perp has Euler class whose integral is 2Q. Its mod-two reduction equals w2(E). Hence

\[
 2Q\equiv1\pmod2,\qquad Q\in\mathbb Z+\tfrac12.
\]

Thus a zero-charge configuration cannot occur in this smooth bundle sector. The smallest absolute charges are ±1/2. Target reflection (n1,n2,n3)→(n1,−n2,n3) preserves the displayed boundary rotations and gives the negative-charge partner with the same kinetic action.

Fractional sigma-model instantons in these twisted torus sectors are known [H]. The explicit formulas here place the record's theta doublet in that class and supply direct analytic and numerical checks. No novelty claim is made for fractional topological charge.

## 6. Stability and the actual fluctuation zero modes

Let n0 be the solution and let xi be a smooth tangent perturbation, n0·xi=0, with the same twisted boundaries. Linearize the first-order operator:

\[
 L\xi=D_x\xi+\xi\times D_yn_0+n_0\times D_y\xi.
\]

For a normalized path through n0 preserving its smooth topological sector, the second variation is

\[
 \boxed{\delta^2S_{\rm kin}[\xi]=\frac1{g^2}\int|L\xi|^2\,d^2x\ge0.}
\]

This proves the absence of negative modes in the declared fixed-background classical problem. It is not a statement about stability after adding a dynamical SO(3) gauge connection, arbitrary potentials, higher derivatives, or four-dimensional fields.

### Count the kernel, do not identify three components with three modes

The complex tangent line of the projective section has

\[
 \deg\mathcal L_{\rm tan}=2Q=1.
\]

The linearized first-order equation is its Dolbeault equation. On a torus, Riemann–Roch and the absence of holomorphic sections in a negative-degree line give

\[
 h^0(\mathcal L_{\rm tan})=1,\qquad h^1(\mathcal L_{\rm tan})=0.
\]

Hence the Hessian kernel has **one complex / two real directions**. They are the translations of the texture. This agrees with the minimal twisted-lump moduli dimension in [H], but the count follows directly here from the degree-one tangent line.

The fields w(z−z0) preserve the same projective twists for every complex z0. Before quotienting any discrete target symmetries, z0 has periods 2 and 2tau; a shift by 1 or tau acts by the corresponding nontrivial target rotation rather than leaving the field unchanged. This extended-torus description is also consistent with [H]. Only the local dimension and the translation zero modes are needed for the claim in this report.

In Cartesian translation coordinates the L2 metric is

\[
 G_{XX}=G_{YY}=\frac{2\pi}{g^2},\qquad G_{XY}=0.
\]

The proof uses conformality: Dx n is orthogonal to Dy n, their norms agree pointwise, and their integrated squared norms are 2pi. This is a Euclidean collective-coordinate metric. A Lorentzian soliton mass interpretation would require separately adding and specifying physical time and its normalization.

These are bosonic fluctuation modes. No fermion operator has been added or quantized, and no chiral-generation index follows from this count.

## 7. The original modular moves act on a real texture, not on T

The doublet obeys

\[
 w(z|\tau+1)=\operatorname{diag}(1,i)w(z|\tau),
\]

\[
 w(z/\tau|-1/\tau)=\sqrt{-i\tau}\,
 e^{\pi iz^2/(2\tau)}H w(z|\tau),
\quad H=\frac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}.
\]

After forming n, the scalar factors cancel. In the Pauli order used here,

\[
 O_L=\begin{pmatrix}0&-1&0\\1&0&0\\0&0&1\end{pmatrix},
\quad
 O_S=\begin{pmatrix}0&0&1\\0&-1&0\\1&0&0\end{pmatrix}.
\]

The transformations act on both the modulus and the domain coordinates. R is S L-inverse S-inverse and is checked directly. The rotation group has order 24 and its S-fourth power is +I.

These rotations are in the source's quaternion-normalizer class. The scalar cohomology line would have to be added to obtain the full source coefficient representation. The script prints an exact fixed intertwiner demonstrating that *external* comparison, and checks that the source's central fourth power is −I instead.

Therefore:

- the relation to record transport is derived on this project's physical direction field, not assigned to a new copy/flavour label;
- the projective construction necessarily loses a common spinor phase;
- the full metaplectic T, its three complex cohomology lines, and the weight-23/2 amplitude are **not** recovered by the classical field n;
- a quantum amplitude can carry transport information not visible in a classical projective field. That amplitude has not been calculated here. The classical cancellation is not a universal no-go for every quantization.

The solution exists for every tau in the upper half-plane and transforms under both generators. No special thread or preferred golden-axis value was selected. Its minimum kinetic action is independent of tau. Therefore the classical sigma-model action does not stabilize the shape modulus or select the golden curve.

## 8. A genuine semiclassical consequence, with its boundary

For the action convention above, a positive minimal sector has exponential factor

\[
 \exp(-2\pi/g^2+i\vartheta/2).
\]

Its fluctuation determinant, measure normalization, and renormalized coupling prescription have not been evaluated. This is the classical exponential part, not a complete quantum transition rate or a particle mass.

Because every smooth configuration in the fixed flux background has Q=m+1/2,

\[
 \boxed{Z_{w_2=1}(\vartheta+2\pi)=-Z_{w_2=1}(\vartheta)}
\]

with a fixed choice of background counterterms. This is a background-dependent theta-angle response. It is not a statement that the ordinary zero-background theory must have physical period 4pi, and it is not the eta/metaplectic phase tested in earlier runs. Theta-angle anomalies under twisted compactification are an established framework [Y].

The kinetic action does not choose the positive rather than the negative-charge configuration. It also does not determine g, vartheta, tau, the translation modulus, a physical length scale, or a coupling to observable fermions.

## 9. A separate four-dimensional control — not an uplift

There is a known field-theoretic relationship between certain twisted compactifications of four-dimensional Yang–Mills theory and CP(N−1) sigma models [Y,H]. The induced metric generally differs from the standard round/Fubini–Study metric. Matching the target topology or moduli dimension is not an uplift of a specific solution.

To make the boundary concrete, the exact script includes the following **separate control**. Take a Euclidean four-torus with areas A12 and A34, an su(2) generator t3 with tr(t3²)=1/2, and curvature

\[
 F_{12}=\frac{2\pi}{A_{12}}t_3,\qquad
 F_{34}=\frac{2\pi}{A_{34}}t_3.
\]

Locally it arises from A2=2pi x1 t3/A12 and A4=2pi x3 t3/A34. Its transition functions close up to −I in each plane. Thus it is a Yang–Mills background with nontrivial centre/'t Hooft flux, not an ordinary globally trivial SU(2) bundle supporting arbitrary fundamental matter without additional gluing data.

The curvature is covariantly constant, so it solves the Yang–Mills equations. Direct integration gives

\[
 Q_4=\frac1{8\pi^2}\int\operatorname{tr}F\wedge F=\frac12,
\]

\[
 S_4=\frac{2\pi^2}{g_4^2}
 \left(\frac{A_{12}}{A_{34}}+\frac{A_{34}}{A_{12}}\right)
 \ge\frac{4\pi^2}{g_4^2}.
\]

At equal areas it is self-dual and saturates the bound. The positivity difference is exactly

\[
 \frac{2\pi^2}{g_4^2}\frac{(A_{12}-A_{34})^2}{A_{12}A_{34}}.
\]

This elementary twisted constant-curvature/toron control is consistent with [H]. It requires a new four-dimensional gauge action, a second flux plane, its area data, and a coupling g4. Those have not been obtained from the source. It is **not** shown to reduce to the exact round-metric profile n constructed above. No four-dimensional spacetime selection, fermion spectrum or gravity claim is made.

## 10. Verification and integrity

Scripts:

```
python verify_exact.py
python verify_numerical.py --dps 50
python verify_numerical.py --dps 80
python verify_global.py
```

### Exact and high-precision work

- 27 named exact finite checks: quaternion matrices, cohomology-ring arithmetic for w2, full generator rotations and the source comparison, the square-bound identity, flux arithmetic, and the separate four-dimensional control.
- 200 direct formula checks at each of 50 and 80 digits, using theta series directly in tau. They cover both cycle monodromies, the Wronskian, normalized projector, S/L/R transformations, the first- and second-order field equations, the independent curvature formula, and the reflected solution.
- Largest high-precision normalized residual: approximately 9.14e-50 at 50 digits and 5.40e-80 at 80 digits.

These are finite-cutoff numerical corroborations, not interval-certified bounds. The all-tau charge, minimum-action and zero-mode conclusions have the analytic derivations in §§5–6, rather than being inferred from sampled points.

### Independent global checks

The ordinary-double-precision script contains 51 comparisons. At four distinct torus shapes, on 16×16, 32×32 and 64×64 grids, it computes:

1. the integrated holomorphic density;
2. the three-vector topological density and action using twisted spectral derivatives;
3. the topological charge from oriented spherical triangles with the exact twisted boundary gluing.

The independent charge calculations give 1/2 to ordinary floating-point precision at the final meshes; the action gives 2pi for g²=1. The spectral first-order residual is approximately 3.5e-14 to 4.3e-14 at 64×64. Second derivatives reach a roundoff floor of order 1e-11 and should not be advertised as 80-digit global checks.

Three smooth finite tangent perturbations preserve the twists and increase the action for both signs. Their numerical second variations approach the analytic square-Hessian expression. At epsilon=1e-3 the relative discrepancies are below 8.4e-7. These trials corroborate the proven positivity; they are not a complete numerical diagonalization of the fluctuation operator.

A deliberately wrong relative factor w1→2w1 violates the fixed second holonomy by approximately 0.844 at the stated test point. This tests that arbitrary relative theta coefficients are not being accepted as solutions of the same boundary problem.

The plan was written after source/literature reading and exploratory reasoning, before the formal scripts. It is locally hashed, not blind or independently timestamped. The exploratory script is retained. All final scripts completed successfully. No source file, earlier report, or repository was altered; no earlier verification module was imported.

## 11. Claim grades and next physical question

| Claim | Status |
|---|---|
| Full smooth real frame on the compact smooth adjoint extension | **EXCLUDED by w2; punctured/complex alternatives are not covered** |
| Nonconstant CP1 field with the record projective twists | **CONSTRUCTED EXACTLY in a declared new model** |
| Q=1/2 and kinetic action 2pi/g² | **PROVED; independently checked by three global methods** |
| No negative classical modes in the fixed smooth sector | **PROVED by the square bound** |
| One complex / two real bosonic zero modes | **PROVED via degree-one tangent line; translations checked** |
| Full source metaplectic triplet or physical fermion generations | **NOT DERIVED** |
| Full quantum fluctuation determinant and any dynamical mass scale | **NOT CALCULATED** |
| Specific four-dimensional uplift | **NOT CONSTRUCTED; a separate flux control is included** |
| Gravity or a complete theory | **NOT DERIVED** |

The constructive result is an actual solution of a nonlinear action using the record's existing projective theta data. The next justified task is to determine whether this precise background admits an independently specified matter or higher-dimensional embedding, with its induced metric, allowed gauge bundle, and zero-mode spectrum calculated. Shared half-flux or a shared special function is not sufficient to promote the relationship to a physical equivalence.

## Primary references and source boundaries

[INPUT] Dritëro M., *A Weave of Two Records* (supplied PDF); supplied Run 9 `TECHNICAL_REPORT.md`, especially §7. These set the unresolved reference-field question and the exact geometric target, not the new sigma-model action.

[BP] A. A. Belavin and A. M. Polyakov, *Metastable states of two-dimensional isotropic ferromagnets*, JETP Letters 22 (1975) 245–247. The sigma-model square bound and soliton framework. https://jetpletters.ru/ps/1529/article_23383.shtml

[H] Y. Hayashi, T. Misumi, M. Nitta, K. Ohashi and Y. Tanizaki, *Fractional instantons in 2d CP(N−1) model and 4d Yang–Mills theory with 't Hooft twists*, arXiv:2507.12802v1. Explicit twisted-torus fractional lumps, their moduli, and the distinct metric/data in four-dimensional reductions. https://arxiv.org/html/2507.12802v1

[Y] M. Yamazaki, *Relating 't Hooft Anomalies of 4d Pure Yang–Mills and 2d CP(N−1) Model*, arXiv:1711.04360v2. Twisted compactification, background anomaly comparison, and the warning that the reduced target metric is not generically Fubini–Study. https://arxiv.org/html/1711.04360v2

[D] NIST Digital Library of Mathematical Functions, Chapters 20 and 23, especially theta shifts and modular transformations. Period-one arguments are used here, unlike the period-pi convention of some DLMF formulas. https://dlmf.nist.gov/20.7 ; https://dlmf.nist.gov/23.18

No novelty assertion is made for the sigma model, twisted fractional instantons, theta identities, bundle obstruction, Riemann–Roch, or torons. The contribution is their explicit and reproducible specialization to the supplied weave, with the quantum and spacetime boundaries retained.
