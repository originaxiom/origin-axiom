# Run 12 — The scalar Hessian and the boundary-domain hierarchy

**Date:** 11 October 2026. **Research goal:** advance the same supplied physical
model, not substitute an unrelated construction. **Status:** AUTHORED
CONDITIONAL ANALYTIC COMPLETION with exact finite controls. Neither this
argument nor the inherited analytic prerequisites has independent specialist
acceptance. No new silver cohomology census, physical particle count, or
origin-of-the-action claim is made.

## Executive result

At the repository's fixed, admitted flat harmonic reference, compact gauge
fixing turns the internal scalar Hessian into the degree-one Hodge Laplacian
on the SAME complementary boundary construction used by its fermion operator.
The identification includes the boundary domain, not just the differential
expression in the interior. Subject to the inherited Hilbert-complex and
physical-metric assumptions, this gives a nonnegative selfadjoint quadratic
internal scalar operator and identifies its zero modes modulo compact gauge.

A remaining projected normal-derivative equation has a more delicate status.
It holds on smooth eigenfunctions and compatible smooth evolution solutions;
it is not an additional trace condition on every element of the second-order
operator domain. A direct boundary-layer construction and an independent
smooth Fourier construction show why confusing those domains produces a
nonclosed operator restriction.

This is a scalar, linearized, fixed-background result. It is NOT a closed
nonlinear domain for the entire auxiliary-eliminated supersymmetric multiplet,
a complete Lorentzian Hamiltonian, a boundary-selection mechanism, or a
quantum stability theorem.

## 1. Updated repository basis — what was not recomputed

The branch inventory returned ten live heads. Main remained at
`6c148ddd495d133213140995976ff08849793d5d`; the audit fork remained at
`8b89d8fb247a7c08811e3a3ccfa59a0e742d78a0`. The physical bridge had advanced to
`2f5cfef7ed3ea4c5e167758e9ba3aee926c2d8ab`, confirmed again after the checks.

The fork's `silver_boundary_variation_2026_10_04/FINDINGS.md` and
`silver_cyclic_boundary_2026_10_04/FINDINGS.md` were read as history. They are
not the newest frontier for the physical boundary equations. On the physical
bridge the following whole proofs were read at the new pin:

| Label | Path below `reports/physical_bridge_2026_09_05/` | Reused result |
|---|---|---|
| R1 | `silver_complementary_boundary_2026_10_09/PROOF.md` | Strict cyclic boundary, elliptic Hodge domain, and cone comparison |
| R2 | `silver_static_energy_2026_10_10/PROOF.md` | Actual auxiliary elimination, positive residual potential, scalar derivative conditions |
| R3 | `silver_fermion_action_2026_10_11/PROOF.md` | Canonical fermion-to-Hodge operator and domain map |
| R4 | `silver_superfield_covariance_2026_10_11/PROOF.md` | Whole-superfield covariance including normal compensator jets; full multiplet analytic domain still unpaid |
| R5 | `silver_superfield_covariance_2026_10_11/INPUTS.json` | Provenance of the preceding dependencies |

Their action expansion, E8 branching, cohomology tables, and covariance
producers were NOT rerun. Their authored analytic grades are retained. The
current run supplies the scalar/operator continuation rather than reannouncing
those predecessors. No corpus-wide novelty or absence claim is made.

Connected GitHub reads succeeded. A direct local git request failed DNS, so
there is no local clone or all-file/all-branch audit. One encoded branch-path
request was rejected; the working branch-list endpoint supplied the refreshed
pin. No repository write, push, merge, or shared-bank number was made.

## 2. Fixed model and hypotheses

Let X be the smooth compact three-dimensional core with closed boundary Sigma.
Keep its supplied metric, compact E8 real form, invariant positive kinetic
trace, and admitted reference complex connection

    Phi_star = A + i B,
    H_star = d Phi_star + i Phi_star wedge Phi_star = 0,
    mu_star = div_A B = 0.

A and B have Hermitian matrix components. In an orthonormal frame,

    D_A,i = nabla_i + i ad(A_i),
    D = d + i ad(Phi_star) = d_A - ad(B) wedge.

The covariant exterior notation includes the Levi-Civita terms. The equations
D^2=0 and mu_star=0 are load-bearing, not optional approximations.

The compact parallel gauge algebra k is the supplied gauge factor commuting
with the structure background. Its complexification is denoted k_C. Its
parallel sections extend over X. In particular they are parallel for A and
commute with B; this is also immediate by separating Hermitian and
anti-Hermitian parts of D c=0 for a compact-real c.

R1 supplies the boundary complex, written with a different font in other
packets to avoid confusing it with the connection A:

    Acal^0 = k_C,
    Acal^1 = im(h_2) direct-sum L,
    Acal^2 = ann_B(k_C).

Here h is the fixed cyclic Hodge contraction, L is an already allowed
k-stable harmonic Lagrangian, and B denotes the INTEGRATED invariant wedge
pairing when used in ann_B. Its positive compatible metric is assumed to be
the physical metric, exactly as priced by R3. This assumption is not derived.

Pi_k is defined by pairing over Sigma with internally parallel k. It is a
finite-rank integrated projection, NOT a pointwise projection of arbitrary
k-valued functions. All internal data, including Pi_k and L, are independent
of the external coordinates. No L is selected in this run.

R1/R3's graph-closed Hilbert complex and selfadjoint elliptic Hodge operator
Q=D+D* are inherited prerequisites. This run checks the scalar identification
with that construction; it does not claim an independent proof of the entire
inherited Hilbert-complex analysis.

## 3. The scalar quadratic form and the missing gauge term

Write a physical scalar perturbation as

    u = a + i b,

with a and b Hermitian one-forms. The linearized curvature is D u. The
linearized real moment map is

    M = delta mu = div_A b - i sum_i [B_i,a_i].

R2's exact potential gives the internal Hessian quadratic form

    q(u) = ||D u||^2 + ||M||^2.

The factor convention here is delta^2 V, not the coefficient of t^2 in V.
The latter is q/2. The norm of two-forms counts i<j, as in R2.

Define the compact gauge-divergence expression

    G = div_A a + i sum_i [B_i,b_i].

Since D_A is unitary and ad(B_i) is Hermitian for the positive complex
coefficient metric,

    D* u = -sum_i (D_A,i + ad B_i) u_i = -G - i M.

Both G and M are Hermitian. Trace cyclicity makes the cross contribution to
the squared norm zero. Therefore the full identity is

    q(u) + ||G||^2 = ||D u||^2 + ||D* u||^2.                 (1)

This keeps the noncommuting A/B terms. Replacing G by div_A a alone, or
reversing the commutator in M, changes the identity. The exact controls
explicitly detect these mistakes.

The term ||G||^2 is a gauge-fixing device, not a new physical interaction or
a retuned potential. On the compact-gauge slice G=0 the original quadratic
energy and (1) agree.

### Compact reality is essential to the quotient

On coefficient zero-forms the full interior identity is

    Delta_0 = D*D = -sum_i D_A,i^2 + sum_i ad(B_i)^2 + ad(mu_star).  (2)

At the harmonic reference, the last term vanishes and Delta_0 preserves the
compact-real subspace. Without mu_star=0 this need not hold: ad(mu_star)
maps a Hermitian coefficient to an anti-Hermitian one. The verifier retains
a non-harmonic countercontrol. Flatness is separately needed for the graded
complex and the commutation identities used below.

## 4. The gauge condition also determines the missing normal trace

An infinitesimal compact gauge transformation with Hermitian parameter lambda
acts by

    delta a = D_A lambda,
    delta b = i[B,lambda],
    delta u = D lambda.

Its allowed boundary VALUE is in internally parallel k; its normal derivative
is not frozen. This is the same distinction maintained in R4.

Take the real kinetic pairing of u with D lambda. Integration by parts gives

    (u,D lambda)_real
      = -integral_X Tr(G lambda)
        + integral_Sigma Tr(a_n lambda).                 (3)

The commutator contribution to G is included. Orthogonality to all admissible
compact gauge directions consequently means BOTH

    G=0 in X,
    Pi_k a_n=0 on Sigma.                                 (4)

The physical response already imposes Pi_k b_n=0. Together,

    Pi_k u_n=0.                                          (5)

Thus (5) is not a new matter-polarization choice: its imaginary part is the
inherited natural response, while its real part is the boundary piece of
compact gauge fixing.

For smooth input, one may obtain this slice by minimizing ||u-D lambda||^2
over admissible real parameters. The weak Euler equation is a mixed
Delta_0 problem: the trace lies in k and the integrated normal equation is
fixed by (3). Its principal boundary symbol is Dirichlet at every nonzero
tangential frequency; the k part is finite dimensional. The inherited
elliptic estimate and compactness give closed range and a minimizer modulo
the parallel stabilizer. Compatibility with the stabilizer follows from
(3) itself. Regularity then gives a smooth slice for smooth input.

This is a linear statement at the reference. It does not solve the nonlinear
Gribov problem or authorize arbitrary internally varying boundary gauge
transformations, which would change Acal^1.

## 5. The closed scalar operator and all its first derivative conditions

R1/R3 impose on a form written alpha+dr wedge beta the trace

    alpha in Acal, beta in Acal^perp,

where perpendicular means the positive Hermitian annihilator. For a one-form
u, the form domain becomes

    u_t in Acal^1, Pi_k u_n=0.                            (6)

This is exactly the physical essential scalar trace plus (4). On this domain
(1) is the degree-one Hodge quadratic form. Under the inherited Hilbert-complex
hypotheses its closed selfadjoint operator is

    H_scalar,gf = Delta_1 = (D+D*)^2 restricted to degree one,    (7)
    Dom(Delta_1) = {u in Dom(Q) of degree one: Qu in Dom(Q)}.

The second membership condition in (7) is indispensable. A formal statement
that the bulk expression is a Laplacian would not determine its boundary
realization.

For a smooth u, expand this membership in degrees zero and two:

    D* u |_Sigma in k_C,
    (D u)_t in Acal^2,
    i_n(D u) in (Acal^1)^perp.                           (8)

The middle condition follows from u_t in Acal^1 and the existing strict
boundary subcomplex. Cyclic maximal isotropy and actual Hodge conjugation
identify the last condition with

    (* (D u)^dagger)_t in Acal^1.                        (9)

Up to an immaterial sign, (9) is precisely the linearized tangential-F
condition after R2 eliminates F. On the slice G=0 the first condition in (8)
is M|_Sigma in parallel k. The projected normal-F condition follows from
(D u)_t in Acal^2, as in the existing proof. No independent replacement
polarization has been imposed.

A selfadjoint Q has a nonnegative selfadjoint square. Degree reduction
in (7) uses the flat graded Hilbert complex, not only parity. Compact
ellipticity gives compact resolvent and smooth eigensections. These standard
implications are conditional on the source's operator/domain hypotheses;
Bär--Ballmann Theorems 3.9/3.11/3.15 and Corollary 5.6 provide the relevant
boundary regularity and spectral setting.

Equation (2), with mu_star=0, means the real compact gauge subspace is
preserved by the scalar spectral problem. The complex Hilbert-complex
intertwining Delta_1 D = D Delta_0 restricts to that real gauge subspace;
its real orthogonal complement is therefore a reducing subspace. The
restriction of (7) to (4) supplies the quadratic internal operator on the
compact gauge quotient. It is not a quotient by arbitrary complex gauge.

### An independent high-frequency scalar check

Freeze a smooth boundary point. Let xi=(x,y) be a nonzero real tangential
covector and use a decaying mode exp(i xi.s-s r) v with s>0. At principal
order (6),(8) become

    x v_1+y v_2 = 0,
    s(-y v_1+x v_2) = 0,
    i x v_1+i y v_2-s v_3 = 0.

Their boundary matrix has determinant

    -s^2 (x^2+y^2),                                     (10)

so no nonzero decaying vector survives. This is an all-covector polynomial
identity, not a frequency grid. The second-order Green form also vanishes
on the resulting half-dimensional value/derivative trace. Deleting the
last condition leaves the normal decaying vector and is detected. This
controls the scalar boundary match rather than redoing the source's entire
first-order elliptic proof.

### Kernel consequence

On the gauge slice, q(u)=0 precisely when D u=D* u=0. No nonzero admissible
compact-gauge exact perturbation is such a representative: integration by
parts with (5) makes its squared norm zero. Hence

    ker(physical internal scalar Hessian)
       = degree-one harmonic space of the inherited complex.  (11)

Under R1/R3's cone comparison this is H^1(K), not a fresh rank computation.
It is also the degree-one part already present in the fermion operator map.
This earns a conditional scalar/fermion zero-mode correspondence on one
background and domain. It does not identify every positive-mass multiplet,
remove vector/constraint fields, or turn every linear zero mode into an
exact nonlinear modulus. Interactions and higher obstructions remain.

## 6. The extra normal response is a compatibility equation, not an H2 trace

The remaining eliminated-auxiliary law in R2 is, to first order,

    Pi_k nabla_A,n M = 0.                               (12)

M already contains a derivative of u. Thus (12) is a second derivative of
the scalar field evaluated at the boundary; it is not in general a
continuous trace functional on an H2 operator domain.

There is a direct equation-of-motion identity. For any smooth coefficient
two-form w and c in parallel k, invariance and integration on the CLOSED
boundary give

    integral_Sigma Tr(c i_n D* w)=0.                    (13)

Its local expression is a tangential divergence. The second fundamental
form terms cancel by symmetry against the antisymmetric two-form. The
background commutators vanish after pairing with c. No pointwise zero-flux
assumption is used.

Apply (13) to w=D u, use Delta_1 u=D D* u+D* D u, and impose G=0:

    Pi_k i_n Delta_1 u
      = Pi_k nabla_A,n D* u
      = -i Pi_k nabla_A,n M.                            (14)

For a smooth eigenfunction Delta_1 u=lambda u, (5) makes the left side of
(14) zero. Equation (12) follows. It also follows for compatible smooth
external evolution solutions because the fixed Pi_k commutes with external
derivatives and (5) holds throughout the evolution.

This establishes (12) on those solutions. It does NOT establish it for an
arbitrary vector in Dom(Delta_1), whose image need not obey the original
value trace. Requiring Delta_1 u to obey that trace is a higher domain or
initial-data compatibility condition. Smooth vectors in domains of powers
of Delta_1 are the natural place for the hierarchy.

The claim is deliberately linear and at the fixed reference. At nonlinear
amplitudes the varied moment map, the gauge slice, normal jets, and the
coupled vector/gaugino domain need a new analysis. R4's off-shell covariance
is not being relabeled as that analytic theorem.

## 7. Exact counterexample to the overstrong operator-domain interpretation

Take a collar-channel control with trivial background and a fixed compact
k generator c. Let u=i f(r)c dr on a slab 0<=r<=1 with separate identical
end laws. Then G=0, D u=0 and M=f'(r)c. The normal value law is f(0)=f(1)=0;
the squared Hodge operator in this channel is the ordinary Dirichlet
operator -d^2/dr^2. The extra equation (12) would demand f''(0)=f''(1)=0.

Choose

    f(r)=r(1-r).

It is in H2 intersect H1_0 and has f''=-2. It satisfies the second-order
operator domain but not the extra response trace. This slab is an exact
local domain control, not a new candidate background on the silver carrier.

Two separate constructions verify the distinction.

**Boundary layers.** With p(t)=t^2(1-t)^4 on [0,1], add epsilon^2 p(r/epsilon)
near r=0 and its reflected version near r=1. Both fix the offending second
trace, retain zero endpoint values, and have disjoint support for epsilon<1/2.
Their squared graph-norm error is

    2 epsilon^5 integral p^2 + 2 epsilon integral (p'')^2,

which tends to zero. The polynomial pieces are C3 at their joins; a smooth
cutoff supplies C-infinity layers with the same scaling. The separate
construction below has globally smooth approximants without this refinement.

**Smooth spectral construction.** The exact sine coefficients of f are

    c_n = 4(1-(-1)^n)/(pi^3 n^3).

Every finite sine sum is smooth and obeys BOTH f_N=0 and f_N''=0 at the ends.
Yet those sums converge to f in the Dirichlet Laplacian graph norm. Indeed,
Parseval gives

    sum |c_n|^2/2 = 1/30 = ||f||^2,
    sum (n pi)^4 |c_n|^2/2 = 4 = ||f''||^2.

The nonnegative tails therefore tend to zero. The graph limit violates the
extra trace. Imposing it literally as an extra Dom(Delta) condition makes
a nonclosed restriction, even in this elementary channel.

There is no contradiction with supersymmetry or with the predecessor's
smooth response: each Dirichlet eigenfunction sin(n pi r) obeys f''=-n^2 pi^2 f,
so the response holds on eigenfunctions. Such functions form a graph core.
The distinction is between a closed operator domain and smooth compatible
solutions, not permission to erase a boundary equation from the action.

## 8. What is earned and what remains supplied

**New authored conditional result:** internal scalar gauge quotient,
closed quadratic operator/domain identification, and interpretation of the
remaining projected derivative law at the linearized fixed reference.

**Computed exactly:** 26 primary finite checks and 7 spectral-reference
checks. Both first runs exited 0. They test noncommutative signs, reality,
gauge surface terms, scalar high-frequency complementing conditions,
Green pairing, integrated projection, and the domain counterexample.
The two instruments have the same author and are not nonauthor acceptance.

**Reused rather than recomputed:** full parent, flat/harmonic admission,
strict complementary boundary, fermion operator correspondence, earlier
cohomology/indices, auxiliary elimination, whole-superfield covariance.

At a fixed supplied compact core the inherited elliptic model has discrete
internal spectrum and a gap above its finite zero eigenspace. This gives
neither a numerical mass scale nor a uniform gap as the cut moves or is
removed. It cannot be substituted for a complete noncompact cusp theory,
whose spectral issues are different.

Nothing selects L, the parent, the compact cut, metric, couplings, or the
reference boundary data. No three-generation count, normalized coupling,
anomaly/inflow cancellation, interacting mirror-removal mechanism, quantum
stability, gravitational dynamics, or parameter-free prediction is derived.
The construction does not claim that the source's many boundary choices are
many selected vacua.

## 9. Next logically distinct test

Extend the domain matching to the COUPLED quadratic vector/scalar/gaugino
system, with its actual external kinetic terms and compact-gauge constraint.
Track which normal equations define the closed operator, which are constraints,
and which are higher compatibility equations. The test is whether the
existing supersymmetry transformations intertwine those realizations without
silently restricting independent H1/H2 traces. No re-count of the already
classified charged cohomology is needed for this test.

A successful coupled linear result would still leave a nonlinear boundary
problem, interactions/anomalies and generation of the supplied data. It would
nevertheless advance one common physical model rather than start another.

## 10. Reproduction, custody and references

Run with Python and SymPy:

    python verify.py
    python verify_spectral_reference.py

Expected outputs are 26/26 and 7/7 exact checks. JSON results and unchanged
first logs are included. The primary script and plan were hashed before its
first execution. The spectral follow-through was separately hashed before
its first execution. No scientific repair was required. These are local seals,
not independent timestamps or repository commits. See SOURCES.json for pins,
blob identifiers, and primary-source URLs; FINAL_MANIFEST.json hashes the
completed package.

Primary literature used for the framework, not as proof of this new application:

- C. Bär and W. Ballmann, *Guide to Boundary Value Problems for Dirac-Type
  Operators*, arXiv:1307.3021v1, especially Theorems 3.9, 3.11, 3.15 and
  Corollary 5.6/Remark 5.7.
- C. Lüdeling, *Seven-Dimensional Super-Yang–Mills Theory in N=1 Superfields*,
  arXiv:1102.0285v1, section 4. Canonical component conventions remain those
  explicitly fixed by R2/R3, not silently imported from the paper.
- A. P. Braun et al., arXiv:1812.06072v2, the twisted local gauge model and
  Appendix B.1. Their closed-space or specialized reductions do not supply
  the repository's relative compact-boundary law.

The source-derived claims above are separated from the new authored argument.
No literature novelty is claimed for Hodge gauge fixing or squared Dirac
operators; the contribution is their explicit conditional application to this
same boundary and the higher-trace compatibility question.
