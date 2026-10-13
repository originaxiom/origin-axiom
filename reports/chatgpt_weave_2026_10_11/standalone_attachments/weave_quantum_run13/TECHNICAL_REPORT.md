# Run 13 — Coupled quadratic modes in the same compact parent

**Date:** 11 October 2026. **Evidence grade:** authored conditional analytic
application, supported by exact finite controls. The inherited global
Hilbert-complex, physical-metric, background-admission and boundary-duality
arguments have not received independent analytic acceptance in this run.

## Executive result

At the fixed flat, moment-zero background of the supplied compact E8 model,
the mixed vector/scalar kinetic term, compact gauge constraint, Weyl mass
operator and the previously admitted boundary complex organize into a
consistent **quadratic spectral decomposition**. Positive degree-zero modes
supply massive vector multiplets: one scalar is the gauge degree of freedom,
but its imaginary partner is a physical real scalar. The co-closed degree-one
sector supplies massive chiral multiplets. Their masses agree with the
singular values of the actual symmetric Weyl bilinear, not its ordinary
eigenvalues. Harmonic gauge and matter sectors remain.

A common smooth spectral core is preserved by the internal profile maps in
the inherited linear N=1 transformations, with an admissible compact gauge
compensator when a gauge slice is used. This is NOT the assertion that an
unbounded supersymmetry transformation maps the entire second-order operator
domain into itself. An explicit derivative-loss control rejects that stronger
and unnecessary requirement.

The free reduced modes have a positive oscillator Hamiltonian and ordinary
unitary free evolution at the fixed compact core. This does NOT construct the
full nonlinear constrained Hamiltonian, a quantum gauge/anomaly completion,
a selected boundary law, or a parameter-free physical theory. No new numerical
silver masses or cohomology populations are computed.

## 1. Repository update and nonduplication

The live branch inventory returned ten heads. Main and the audit fork are
unchanged from Run 12. The physical branch advanced from 2f5cfef7 to
**8016cd2e318d86b3885a3883a9bb990c301a83dd**. Its new
`silver_bosonic_quotient_2026_10_11/PROOF.md` and `FINDINGS.md` establish a
conditional smooth real scalar-null quotient and its equality with the
already mapped Weyl H1. These were read in full, not rerun. They substantially
overlap the zero-mode portion of Run 12 and are explicitly reused here.

The new report at the START pin names vector/constraint and all-degree
multiplets as the next duty. The present calculation addresses the quadratic
spectral organization; it does not relabel the scalar-zero result as new.

**Post-calculation refresh:** before packaging, the physical branch advanced to
7afab07d4b2c446d5dc1336fe5594b736a704eda. Its newly posted
`silver_physical_multiplets_2026_10_11/PROOF.md` was read in full AFTER all
three instruments and their final replays. It independently develops the
external vector/scalar kinetic and homogeneous-vector boundary steps, the
MASSLESS physical dictionary, boundary-plane intersection strata and the local
SU5 cubic anomaly condition. Those overlapping vector/zero-mode observations
are now corroborating work, not claimed exclusive discoveries here. The
positive-mass exact/co-closed multiplet split, explicit Gauss reduction and
common smooth spectral-core analysis remain the distinct continuation in this
packet. No priority or corpus-wide novelty claim is made.

The later commit preserves a reference-instrument type failure and a repair
reseal. It reports an unchanged 96-predicate native pass but does not establish
a completed independent acceptance in that commit. Its census, normalization
claims and regression were NOT replayed or adopted as verified results here.
The new proof is consistent with our mixed kinetic expression and explicitly
retains its external total derivative before using the same falloff condition.
The next task is therefore not another local SU5 anomaly formula: preserve
that update and proceed to physical interactions and complete boundary/quantum
consistency on the same model.

The canonical Weyl operator section was fetched again at the new pin. Its
blob is unchanged. The strict boundary, auxiliary elimination and superspace
covariance reports read in Run 12 remain premises. No full repository clone,
all-head content audit, producer replay, push or merge is claimed. All numerical
claims in the repository retain their source grade. A list of references and
pins is in SOURCES.json.

## 2. Fixed construction and notation

Let X be the supplied smooth compact internal three-core with closed boundary
Sigma, fixed positive metric and compatible coefficient metric. External
spacetime is supplied flat Minkowski space; Euclidean external momentum is
used below only for the gauge-fixed quadratic-symbol check. No spacetime or
compactification is derived here.

The structure background is

    Phi_star=A+iB,       H_star=0,       mu_star=div_A B=0.

A and B have Hermitian components. The coefficient differential is

    D = d_A - ad(B) wedge,           D_plus=d_A+ad(B) wedge.

The complex conjugation J is actual compact Hermitian conjugation of
coefficients, extended antilinearly; it is not a new imposed real structure
on a charged harmonic space. It obeys J D = D_plus J. The positive formal
adjoint is D^dagger. In degree one, D^dagger=-div_Dplus.

The supplied strict cyclic boundary is

    Acal^0=k_C,
    Acal^1=im(h_2) direct-sum L,
    Acal^2=ann_B(k_C).

Here k is the internally parallel compact gauge algebra, B in ann_B is the
integrated bilinear wedge pairing, and L is any one of the already admitted
harmonic polarizations. The derivative notation B_i remains the Higgs field;
these two uses should not be conflated. Pi_k is the finite-rank INTEGRATED
projection onto parallel k, not a pointwise field restriction.

The graph-closed Hilbert complex with this tangential boundary and the
selfadjoint elliptic Q=D+D^dagger are inherited. The signed Hodge-conjugation
map, its boundary compatibility and the physical Weyl/Hodge identification
are also inherited. Flatness is required for D^2=0. The harmonic equation is
required for the degree-zero Laplacian to preserve compact reality. All
internal reference data are independent of external spacetime.

Write u=a+ib for the internal scalar fluctuation, a_mu for the external
vector fluctuation (the subscript distinguishes it from the one-form a),
and lambda,rho for the normalized Weyl fields, a coefficient scalar and a
coefficient one-form. Compact real gauge parameters are denoted epsilon_g.

## 3. The same action's vector/scalar mixed kinetic term

Expansion of the covariant field strengths in the existing parent gives,
to first order in fluctuations,

    E_mu = partial_mu u - D a_mu,
    f_mu_nu = partial_mu a_nu-partial_nu a_mu.

Indeed E_mu is the complex combination of F_mu_i and i D_mu B_i. Terms
bilinear in fluctuations do not enter its quadratic norm because the
background has E_star=0. This derivation uses the gauge-covariant kinetic
terms, not an inferred mass degeneracy. It retains the background Higgs
part of D.

At this order the allowed compact transformations are

    delta a_mu=partial_mu epsilon_g,
    delta u=D epsilon_g.

Thus delta E_mu=0 and delta f_mu_nu=0. Epsilon_g has an internally parallel
k boundary VALUE. Before boundary gauge fixing its normal derivative is
not frozen.

For u=a+ib define the real Hermitian expressions inherited from Run 12:

    G(u)=div_A a+i[B_i,b_i],
    M(u)=div_A b-i[B_i,a_i],
    D^dagger u=-G(u)-i M(u).

The Euclidean quadratic bosonic action, with canonical real-field kinetic
normalization, is

    S_B2 = integral_R4 [ ||f||^2/4
              + ||partial_mu u-D a_mu||^2/2
              + (||D u||^2+||M(u)||^2)/2 ].               (3.1)

The external kinetic expression is understood after external integration by
parts with the declared falloff or periodicity. In superfield components the
extra quadratic divergence is +partial_mu Tr(b_i partial^mu b_i)/2; dropping
that external divergence is NOT permission to discard an internal boundary
surface. The late repository proof makes this same distinction.

The two-form norm in the last term counts i<j. A complex four-dimensional
chiral coordinate is its real/imaginary coefficient divided by sqrt(2).
The normalized fermions are the source's lambda,rho; no relative physical
coupling has been tuned. Equation (3.1) follows from the same canonical
kinetic terms and static Hessian, not from adding a new potential.

### Boundary and gauge fixing

The actual vector trace is a_mu|Sigma in parallel k. Variation of its mixed
kinetic term requires Pi_k E_mu,n=0. The imaginary normal scalar projection
already vanishes in the physical response. Choose Pi_k a_n=0 for the real
normal scalar by the admitted compact boundary gauge fixing. This is a gauge
choice, not a stronger original physical boundary law.

Then Pi_k E_mu,n=0 becomes

    Pi_k nabla_A,n a_mu=0.                                (3.2)

The vector operator has precisely the mixed degree-zero domain

    Dom(P0): f|Sigma in k_C, Pi_k nabla_A,n f=0,
    P0=D^dagger D=-nabla_A^2+sum ad(B_i)^2.               (3.3)

For physical real vectors, take its compact-real part. The equality in (3.3)
uses mu_star=0. Its zero space is the residual parallel k, not nonexistent
vector states. All other eigenvalues are positive at the fixed compact core.

Gauge transformations preserving the boundary gauge choice have the
homogeneous domain (3.3). This homogeneous normal condition is a RESIDUAL
condition after gauge fixing; the original unrestricted normal gauge jets
were essential in reaching the boundary gauge slice. It is not legitimate
to freeze them before that step.

In Euclidean Feynman gauge add

    S_gf2=1/2 ||partial_mu a_mu+G(u)||^2.                  (3.4)

Integration by parts cancels the mixed term. The internal surface term
vanishes because Pi_k a_n=0 and the vector boundary value is parallel k.
The result is

    a_mu: -partial_ext^2+P0,
    u:    -partial_ext^2+Delta_1,
    ghost: -partial_ext^2+P0.                            (3.5)

Delta_1 and its full domain are those of Run 12. The ghost comes from

delta(partial a+G)=partial_ext^2 epsilon_g-P0 epsilon_g.

The residual constant gauge kernel must be handled as residual gauge
symmetry; it is not deleted from the physical massless vector sector.
These are a quadratic Faddeev–Popov and background-gauge construction, not
a nonlinear Gribov analysis or an anomaly calculation.

### Exact symbol control

For one positive internal mass m and real Euclidean four-momentum p, the
vector plus gauge-scalar Hessian before gauge fixing is

    H = [ (p^2+m^2) I_4 - p p^T      -i m p ]
        [          i m p^T                p^2 ].

Its exact gauge null vector is (i p,m). The gauge-fixing row is
F=(i p^T,-m), with F(i p,m)=-(p^2+m^2), and

    H+F^dagger F=(p^2+m^2) I_5.                          (3.6)

Changing the relative gauge-fixing sign fails. This checks cancellation of
every off-diagonal entry, not only equality of determinant degrees.

## 4. Exact one-forms furnish massive vector multiplets

Let f be a normalized COMPACT-REAL eigenfunction of P0 with m^2>0:

    P0 f=m^2 f,           ||f||=1.

Because P0 preserves compact reality, such a real basis exists. Set

    e=D f/m.                                            (4.1)

The Hilbert-complex identities, including domains, give

    ||e||=1, D e=0, D^dagger e=m f,
    Delta_1 e=m^2 e.                                    (4.2)

A mode of the original fields is

    a_mu(x,y)=v_mu(x) f(y),
    u(x,y)=(s(x)+i h(x)) e(y).

For these profiles, G(u)=-m s f and M(u)=-m h f. The Lorentzian quadratic
Lagrangian with metric (-+++) is

    L=-F_mu_nu F^mu_nu/4
      -(partial_mu s-m v_mu)(partial^mu s-m v^mu)/2
      -(partial h)^2/2-m^2 h^2/2.                        (4.3)

Gauge transformations act by delta v=partial epsilon, delta s=m epsilon,
delta h=0. Thus s is the Stückelberg (gauge/Goldstone) scalar. In unitary gauge
s=0 it supplies the longitudinal polarization of a massive vector. The
imaginary exact component h is a PHYSICAL real scalar of the same mass.

Quotienting by complex gauge would remove h incorrectly. Flatness alone
does not make it gauge: M(i D f/m)=-m f is nonzero. This extends the source's
zero-mode warning to the positive-mass spectrum.

### Two actual Weyl profiles, not a doubled particle count

The source's symmetric internal Weyl bilinear has Euler operator

    R(lambda,rho)=(div_Dplus rho, *D rho-D_plus lambda).

Use z0=(f,0) and z1=(0,e). Since f is compact-real,

    R z0=-m J z1,          R z1=-m J z0.                 (4.4)

The physical Weyl mass block is therefore an off-diagonal symmetric block
with singular value m on both components: two Weyl fermions of mass m.
Together with the three vector polarizations and h, this has four on-shell
bosonic and four on-shell fermionic degrees of freedom: one massive N=1
vector multiplet. The auxiliary Hodge doubling is not another set of
independent Weyl particles.

### Constraint and free positive Hamiltonian

Before unitary gauge the Gauss equation is

    partial_i E_i - T^dagger pi_u=0,

up to an overall constraint-generator sign, where T is D on compact-real
parameters and pi_u is the real scalar momentum. It is the variation of
a_0 and generates the transformations above.

A real Fourier quadrature gives an especially explicit all-momentum check.
With longitudinal momentum p, vector coordinate v and Goldstone s, choose

    C=-p E+m pi_s,
    H0=[E^2+pi_s^2+(p s+m v)^2]/2
       +[pi_h^2+(p^2+m^2)h^2]/2.

Poisson brackets give {C,H0}=0, {v,C}=-p and {s,C}=m. After s=0 and C=0,

    Hred=[(1+p^2/m^2)E^2+m^2 v^2]/2
         +[pi_h^2+(p^2+m^2)h^2]/2.                     (4.5)

This is positive and its longitudinal frequency is sqrt(p^2+m^2), the same
as its two transverse polarizations, h, and the paired Weyl fermions.
The rescaling q=m v/sqrt(p^2+m^2), P=sqrt(p^2+m^2)E/m is canonical and
makes its longitudinal oscillator manifest. There is NO division by m at
zero mass: that sector has to be retained separately.

## 5. Co-closed one-forms furnish massive chiral multiplets

At each positive eigenvalue the complex Hodge decomposition is

    E_1(m^2)=D E_0(m^2) direct-sum C_1(m^2),
    C_1=E_1(m^2) intersect ker D^dagger.                 (5.1)

The first summand was treated above. On the second, G=M=0, so there is no
vector mixing; the physical scalar mass squared is m^2.

Let J be actual coefficient conjugation. Define the ANTILINEAR map

    K=* J D: C_1(m^2) -> C_1(m^2).                      (5.2)

The inherited cyclic boundary/Hodge reality is crucial here. The map must
act on the admitted full adjoint plus dual sectors; it is not a new demand
that a charged harmonic polarization itself be separately real. On smooth
spectral spaces the boundary map is well-defined, and the differential and
adjoint identities give

    K^2=D^dagger D=m^2,
    ||K u||=m ||u||.                                   (5.3)

Thus K/m is an antiunitary involution. Choosing an orthonormal fixed basis
is the Takagi form of the symmetric Weyl mass tensor. Every complex
co-closed profile supplies a complex scalar and one Weyl field of the same
mass m, namely one massive chiral multiplet. A negative eigenvalue in a
real-curl convention can be removed by the corresponding complex field
phase; ordinary eigenvalues of a complex symmetric mass matrix are not
physical masses.

For charged representations K exchanges the appropriate conjugate charge
slots. The diagonal Takagi basis may mix those slots and need not make the
unbroken gauge symmetry manifest. This argument does not force pairing of
chiral ZERO modes: K/m is unavailable at m=0.

## 6. Harmonic and all-degree accounting

The massless vector sector is ker P0=k, with its gaugino furnished by the
signed Hodge-conjugate harmonic degree-three sector. A parallel f has
D f=0: it supplies no exact scalar e, and there is no Stückelberg division
by zero.

The massless matter sector is harmonic H1(K_boundary), the same space in the
source's Weyl map and real scalar quotient. Each complex profile has its
complex scalar and left Weyl field. The H2 modes are the actual conjugate
sector in the doubled operator; they must not be counted twice. Charged
W and W* multiplicities must still be distinguished in H1 itself.

At a positive eigenvalue let a=dim_C E0 and b=dim_C C1. Hodge duality and
(5.1) give

    (dim E0,dim E1,dim E2,dim E3)=(a,a+b,a+b,a).

The physical content is

    a massive vector multiplets + b massive chiral multiplets.

Direct physical counting gives

    bosons = 3a + [2(a+b)-a] = 4a+2b,
    fermions = 2[(a+b)+a] = 4a+2b.                      (6.1)

The removed a are REAL gauge scalars, not a complex quotient. The whole
Hodge complex has not been re-labelled as particles; vector polarizations,
gauge constraints and the actual Weyl identification account for (6.1).

These are formulas, not a fresh numerical silver census. All earlier
allowed L values remain. No mass eigenvalues of the actual nonsplit
background or normalized zero-profile overlap tensors are computed here.

## 7. Domains, supersymmetry and what free evolution means

Let E_infty^p be the intersection of the domains of all powers of Delta_p.
Finite sums of its smooth internal eigenprofiles form a common dense core.
The inherited Hilbert complex and Hodge conjugation imply the spectral
intertwining identities

    Delta_(p+1) D = D Delta_p,
    Delta_(p-1) D^dagger = D^dagger Delta_p,
    Delta_(3-p) (*J) = (*J) Delta_p,

with the appropriate domains. They are first established on finite spectral
sums and extended in graph norms of the appropriate orders. Consequently
D, D^dagger, actual reality in degree zero, and K preserve the common smooth
spectral core with their changed form degrees. Internal data are fixed, so
external derivatives commute with all these internal spectral operations.

The inherited linear N=1 transformations have internal profile content

    delta a_mu: lambda and its actual conjugate;
    delta u: rho;
    delta lambda: external f_mu_nu and M(u);
    delta rho: partial_mu u-D a_mu and *J D u.

Their canonical component signs and external spin matrices are the source's,
not newly substituted conventions. The equations above demonstrate that
every internal entry and its boundary trace remains on the common smooth
core. The source's superspace calculation supplies the off-shell algebra;
this run adds its profile/domain organization after the quadratic spectral
reduction. A rest-frame Clifford-supercharge calculation is only a
normalization and degree-count control, not a rederivation of every parent
superspace term.

If a compact Coulomb/unitary slice is used, delta u can contain a real exact
piece. The compensator uses P0^-1 on k-perp. Its k compatibility follows from
the retained integrated normal trace. Mode by mode it is simply the allowed
-m^-1 times that gauge coefficient. It preserves the core and has the
homogeneous admitted boundary trace. Residual k is retained. No nonlinear
field-dependent global slice or Gribov theorem is inferred.

The higher normal-auxiliary and gaugino conditions are respected on the
smooth compatible core/eigenmodes as inherited equations or higher
compatibility conditions. They are NOT appended as independent traces on
all H1 or H2 graph domains. This retains the Run 12 distinction.

### Why whole second-order-domain invariance would be the wrong test

On an interval, f_N=sum_(j<=N) cos(j r)/j^3 consists of smooth Neumann
modes. The series converges in the Neumann Laplacian graph norm: the
weighted square tail includes sum j^-2. Its derivative is a legitimate
first-order Dirichlet-domain vector but need not belong to the second-order
Dirichlet domain: that stronger graph sum includes sum 1 and diverges.
Every finite sum nevertheless has the exact derivative/mass and boundary
intertwining identities. Supersymmetry involves first derivatives; it is
unbounded and naturally shifts Sobolev order. Failure of the stronger
whole-Dom(Delta) demand is not a failure of the symmetry on the smooth
solution core.

### Quadratic evolution versus the full nonlinear theory

After the Gauss reduction, (4.5) and the co-closed sector are free positive
oscillators. Their direct-sum/direct-integral one-particle energies are
sqrt(|p|^2+m_n^2). Multiplication by these real energies with its natural
weighted L2 domain gives ordinary selfadjoint FREE time evolution. Finite
internal spectral sums with Schwartz external data form a convenient dense
core. This construction is conditional on the inherited compact operators
and the quadratic action dictionary.

It is not a proof of a closed NONLINEAR multiplet Hamiltonian, nonlinear
boundary well-posedness, interacting BRST cohomology, large-gauge invariance,
or boundary anomaly cancellation. Free canonical supersymmetry can be
organized on the mode core; a full interacting quantum theory remains a
separate obligation. No uniform mass separation is obtained as the compact
cut is removed or the metric changes.

## 8. Independent controls and declared failures

`verify_coupled.py` constructs a deliberately nonreal self-dual finite
complex, not a discretization of the silver manifold. Its defining spaces
have dimensions (3,6,6,3). A rational complex unitary change of basis makes
the compact-real gauge directions nontrivial. It checks the symmetric Weyl
bilinear, Hermitian mass square, compact gauge projector and physical scalar
quotient separately. Its artificial control masses 2,3,4,5 are NOT physical
predictions. Zero gauge and harmonic matter modes are retained.

`verify_slab_reference.py` uses actual derivatives on a flat slab times a
torus and shares no finite-complex builder with the first instrument. For
all positive integers n,k it uses

    f=sin(n r) cos(k x),
    e=grad f/sqrt(n^2+k^2),
    g=(0,cos(n r)cos(k x),0),
    g_partner=curl(g)/sqrt(n^2+k^2).

Their value and derivative traces satisfy the same NONZERO-tangential-
frequency boundary symbol. The test deliberately does not model the silver
carrier's global harmonic sector. A value-only wrong scalar profile and a
wrong vector trace fail. Equal kinetic integrals are checked exactly at
three integer-mode pairs; all field equations and intertwining identities
are symbolic for arbitrary positive n,k.

`verify_constraints.py` independently checks the finite canonical Gauss
constraint, its preservation, the longitudinal positive Hamiltonian and
Dirac dispersion for every real p and positive m.

Final results: **59 + 34 + 15 = 108 exact checks passed.** All instruments
share an author. They are not independent analytic acceptance of global
operator claims, and the check count is not a confidence score.

Two implementation events are preserved:
1. The first main execution exceeded the 200-second tool timeout without
   flushed output. The script and empty first log remain. Exact rational-
   complex expansion of intermediate matrices and progress flushing were
   added; no model or assertion changed.
2. The second main execution passed its preceding field/operator checks,
   then raised a SymPy TypeError multiplying by a Python bool in the
   rest-frame Kronecker delta. Replacing that bool by int fixed the type;
   the prior script/log and a pre-third-run hash remain. The full main
   instrument then passed. The slab and constraint instruments passed
   their first executions.

A failed attempt to request an interactive container session did not run a
script; it is a tool-interface event, not another scientific test. Terminal
shutdown printed an unrelated TERM warning after successful Python exits;
raw logs retain it. No failed scientific predicate was turned into a passing
criterion, and no first-run-success claim is made for the main instrument.

## 9. Mission effect and next test

This connects the vector constraint, scalar quotient and fermion mass
operator at positive as well as zero internal eigenvalues, within ONE
supplied compact parent and boundary construction. It is stronger than
matching a kernel dimension or a formal Laplacian in the interior.

It does not pick L, the cut, background metric, parent, coupling or scale.
The necessary free multiplet organization holds for every admitted choice
covered by the hypotheses, so this test alone cannot select three families.
Gauge-chiral harmonic counts, boundary anomalies, normalized interaction
tensors and their physical light-state consequences still need the same
model. An apparent massive scalar must not be discarded as complex gauge,
and harmonic modes must not be called exact nonlinear moduli by default.

The next distinct gate is to combine the retained PHYSICAL harmonic multiplet
dictionary with normalized same-action interactions and complete boundary/
quantum consistency. The late repository update already supplies its local
SU5 cubic anomaly formula at its stated grade; do not rerun it or its
cohomology census as though absent. Do not rerun the old scalar quotient. The full nonlinear boundary
Hamiltonian remains another analytic duty; the free evolution result does
not discharge it. Origin of spacetime, normalized empirical predictions and
gravity remain open. No TOE completion or impossibility is inferred.

## 10. Reproduction and source scope

    python verify_coupled.py
    python verify_slab_reference.py
    python verify_constraints.py

Python 3 with SymPy is sufficient. The tested SymPy version and source
hashes are recorded with the execution metadata. No PDF, original report or
remote repository file was modified. Only this local run directory is new.

Primary literature supplies the framework, not independent acceptance of
this boundary application:
- C. Lüdeling, arXiv:1102.0285v1, sections 3-4: covariant seven-dimensional
  kinetic action, mixed F_mu_i+iD_mu B_i, and N=1 organization.
- A. P. Braun et al., arXiv:1812.06072v2, section 2 and Appendix B.1:
  supplied twisted local parent. Its specialized/closed reductions do not
  replace this relative-boundary domain.
- C. Bär and W. Ballmann, arXiv:1307.3021v1, compact elliptic spectral and
  boundary regularity setting. The inherited Hilbert-complex application
  remains explicitly conditional.

Pinned repository paths, read ranges and URLs are in SOURCES.json. No claim
of literature novelty for Stückelberg fields, supersymmetric multiplets,
Hodge decompositions or singular-value mass diagonalization is made.
