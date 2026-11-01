# Restore the flat family: its physical metric, SM stratum and discrete component

November 1, 2026. UNREVIEWED author source/algebra/geometry derivation.
No scientific producer, CAS, solver, scientific-module import or test execution.
This is a conditional expansion of the existing parent, not a new
foundational selector, whole-architecture census or chiral SM result.

## 1. The missing quantifier in a preferred Wilson example

The old source exhibits a stationary SM gauge phase using one flat Y
holonomy. The same action admits a larger family. Keep its principal
triple, physical compact E8, complete cusp, spin line, metric and action;
vary ALL commuting flat holonomies in the triple's connected centralizer.
This does not restrict the programme to m004 or assert that the family
is the whole generated architecture.

Reuse weave_sm_parallel_2026_10_08/PROOF in full for the explicit regular
SU5_g x SU5_b embedding, its joint Z5 kernel, principal triple and
stationarity. Reuse its compactly supported flat representatives and
same-domain Fredholm/index argument. Reuse the actual kinetic/action
and [gauge response](SAME_ACTION_REAL_GAUGE_FIXING_AND_ONE_LOOP_WEIGHTS.md),
the earlier [Hodge distinction](HODGE_GEOMETRY_REDUCTION_AND_FIBRE_MAP.md)
and [flavour-orbit metric](PARALLEL_FLAVOUR_ORBIT_METRIC_AND_HEAVY_RESPONSE.md).
The ingredients are credited existing results. Their analytic-review
qualifications remain; no prior producer is rerun.

There are TWO new duties: derive the metric on this whole flat family,
and retain the global centralizer rather than silently replace it by
its Lie algebra. The latter reveals a discrete component while leaving
the source's continuous Lie-algebra computation intact.

## 2. The full triple centralizer has a charge-conjugating component

Let P denote the principal SO3 in SU5_b and let K=C_E8(P). The old full
248 decomposition gives Lie(K)=su5_g. SU5_g embeds faithfully, so
K^0=SU5_g, not PSU5. This determines the identity component, not pi0(K).

One can construct an element outside K^0. Choose the Chevalley involution
theta of E8, with compatible matrix convention theta(X)=-X^T on each
regular sl5 factor. It preserves the compact form. Since E8 has no
diagram automorphisms it is inner; write theta=Ad(n) with n in compact
E8. The adjoint E8 is centre-free, so theta^2=1 implies n^2=1.

The old source already supplies

  J=anti-diag(1,-1,1,-1,1) in SU5_b,
  J X J^(-1)=-X^T for X=H,E,E†,
  J^2=1, theta(J)=J.

Thus

  s=J^(-1)n, s^2=1,
  Ad(s)H=H, Ad(s)E=E, Ad(s)E†=E†.                         (1)

It is in K. On su5_g its action is theta, an OUTER automorphism of
that A4 factor. An element of K^0=SU5_g could act there only by an inner
automorphism, hence s is outside the identity component. On its standard
diagonal compact torus it acts by inversion. This is a compact E8 gauge
transformation, not an anti-linear conjugation of four-dimensional fields
or a change of spacetime orientation.

For the exact component count, personally checked Di Bella--de Graaf,
*Computing component groups of stabilizers of nilpotent orbit
representatives*, arXiv:2407.11801v1: sections 2.1--2.2, the centralizer/
double-centralizer definitions and Table 5 with its column definitions.
Its E8 orbit A4 has connected centralizer type A4 and component group S2.
Section 2.2 identifies the nilpotent and triple component groups.
[Primary paper](https://arxiv.org/pdf/2407.11801), Table 5, printed p.18;
that page was rendered and inspected personally. No GAP computation was
run here and the entire paper is not claimed read.

The orbit label applies: our E is principal in a regular A4 Levi. Its
Levi can be recovered as the centralizer of a generic Cartan element in
su5_g; avoiding the finite mixed-root hyperplanes leaves precisely A4_b
and its four-dimensional centre. The principal E is distinguished in
that Levi. The table therefore concerns this embedding, not merely an
unrelated occurrence of the name A4. Polar decomposition of the complex
triple centralizer retracts to its compact form, preserving components.
Together with the explicit involution (1), it gives

  K = SU5_g semidirect Z2,
  s g s^(-1)=bar(g).                                      (2)

This is an authored application/construction using the published count,
not our independent reproduction of that classification table.

The earlier C_E8(SM)=(SU5_b x U1_Y)/Z5 is a DIFFERENT centralizer.
Its connectedness is not refuted: s reverses Y and therefore does not
centralize the full SM subgroup. The old statement “no extra gauge
generators” is likewise correct; discrete components add no Lie generators.

## 3. The entire untwisted commuting family

Fix a marking of the compactified elliptic curve X=C/(Z+tau Z), and
restrict to centralizer holonomies with trivial component class and
trivial peripheral transport. For generators A,B of the surface group,
their holonomies U,V are in SU5_g and obey [U,V]=1. Commuting unitary
matrices are simultaneously diagonalizable: diagonalize U, then V on
each U eigenspace, retaining determinant-one basis changes. Their joint
conjugacy classes are consequently

  U=exp(2 pi i u), V=exp(2 pi i v),
  (u,v) in (t_g/Lambda)^2,
  Lambda={diag(n1,...,n5): n_i integers, sum n_i=0}.

The Weyl S5 permutes the five simultaneous eigenvalue pairs. The extra
gauge transformation s supplies (u,v)->(-u,-v). With the complete
principal gauge data carried along, the untwisted flat family is

  M_flat = [(t_g/Lambda)^2 / (S5 x Z2)].                   (3)

The displayed finite action need not be free. These are orbifold/stratum
coordinates, not a claim of a smooth manifold at enhancement loci.
Its covering torus has real dimension eight. No modular quotient of the
marking, distribution over tau or physical identification with update
words has been supplied. Nor is a fixed external charge/measuring frame
left untransformed while (u,v) is declared equivalent to (-u,-v).

Each pair yields a stationary background A=A_spin+C, Q=Q0,R=0 because
C is flat and commutes with the principal triple. Its harmonic and
compactly supported representatives differ by a globally exact form in
the same compact gauge direction. Near the puncture the harmonic forms
extend across X, have finite norm and an exact primitive. The primitive
can be chosen with a finite limiting constant and lies in the complete
gauge graph space. Thus the harmonic representative is not a different
physical cusp law chosen for convenience.

The entire previously derived CP1 flavour orbit can be applied to every
such flat connection. Extra nonparallel Higgs profiles and other
reduction/topological sectors are not classified by (3).

## 4. Derive its kinetic metric from the same action

Let w=x+tau y, with x,y of period one, tau=tau1+i tau2, tau2>0.
For fixed internal tau the harmonic Cartan-valued representative is

  C=2 pi (u dx+v dy).                                     (4)

The Hodge star on one-forms in two dimensions is conformally invariant.
Thus the actual complete hyperbolic metric and the flat conformal metric
|dx+tau dy|^2 give the same one-form norm. This does NOT identify their
scalar/spin Laplacians or replace the physical cusp by a flat torus.

In these coordinates the flat metric has area density tau2 and inverse
matrix tau2^(-2)[[|tau|^2,-tau1],[-tau1,1]]. Direct integration gives

  integral_Sigma kappa(delta C wedge *delta C)
    = (2 pi)^2/tau2 kappa(delta v-tau delta u,
                                delta v-bar(tau) delta u). (5)

The right side uses complex-bilinear extension of the compact trace,
with the second entry the conjugate of the first; it is positive.
Removing the puncture changes no integral of these smooth forms.

The source's chiral connection metric is one half this real one-form
norm. Its induced external scalar kinetic metric is therefore

  ds_flat^2 = (2 pi)^2/(2 g6^2 tau2)
           kappa(dv-tau du,dv-bar(tau) du).                 (6)

The FULL gauge response has not been set to zero by an ansatz: delta C
is coclosed and commutes with the background Q,R. Its source under the
real gauge adjoint vanishes, so no external gauge compensator lowers
this norm. Gauge directions with zero norm tangent are already quotiented;
unbroken gauge multiplets remain, not massive modes silently eliminated.

In any orthonormal Cartan direction the real coefficient matrix in (6)
is a common factor times

  M_tau=(1/tau2)[[|tau|^2,-tau1],[-tau1,1]],
  det M_tau=1.                                            (7)

At tau=i it is the identity. Under a simultaneous change of homology
marking, periods and tau transform together and preserve (5); holding
the periods fixed while changing only tau is not such a convention.
The lattice and Weyl action are isometries, so (6) descends to (3).
No independent arbitrary metric function on this Wilson family is needed.

The same source has the four-dimensional unbroken gauge coefficient

  g4^(-2)=Area(Sigma)/g6^2=2 pi ell^2/g6^2.                 (8)

Here the trace convention stays fixed, and ell is the hyperbolic curvature
radius. Harmonic one-form norms are conformally invariant, so (6) is
independent of ell at fixed g6, while the vector coefficient in (8) is
not. The ratio is determined by ell; it is not a second free scalar
normalization. The orbit norm from the preceding note restores as

  N0=Area(Sigma) kappa(E†E)/(4 ell^2 g6^2)
    =pi kappa(E†E)/(2g6^2),

because Q0=E/(2 ell) in orthonormal fields. It is 10 pi/g6^2 in the
defining-five convention for every ell. No value of g6 or ell in
external measuring units is derived.

The phase-response current is on H in su5_b; the flat-connection tangent
is on t_g. The two commuting simple factors are orthogonal in the E8
invariant pairing. The resulting induced metric on this stationary
subfamily, at FIXED tau, is locally the product of (6) with the prior
N0 Fubini--Study metric on CP1. This does not prove a dynamically closed
truncation or a product metric when tau itself becomes an additional
physical field with horizontal derivatives.

## 5. Locate the SM stratum without selecting it

Let p_i=(u_i,v_i) modulo the integral period lattice. A gauge root
e_i-e_j survives exactly when BOTH holonomies agree on that pair:

  u_i-u_j and v_i-v_j are integers.                        (9)

The connected unbroken group is S(product_k U(m_k)), where m_k are the
multiplicities of DISTINCT simultaneous pairs. For all five distinct,
it is U1^4. The exact SM group S(U3 x U2) occurs at a joint partition
3+2, and is its usual [SU3 x SU2 x U1]/Z6 subgroup by the old faithful
embedding. Its representatives can be written

  QY=diag(-2,-2,-2,3,3),
  u=p QY, v=q QY, (p,q) in (R/Z)^2.                       (10)

There are no extra disconnected determinant branches in this two-block
torus because gcd(3,2)=1. Within the eight-dimensional covering family,
the six pair-equalities leave a two-dimensional SM stratum. These are
constraints on the state, not six newly fitted constants or a theorem
that genericity is a physical selection law.

The blocks coincide at 5p,5q integers: twenty-five central-holonomy
points restore SU5. The source example is (p,q)=(2/7,0), away from
them. It is not fixed by (6), stationarity or the metric's positivity.
The disconnected component identifies (p,q) with (-p,-q) when all gauge
and registering data are transformed. It does not prefer order seven.

The volume density on the covering torus derived from (6) is constant
in u,v at fixed tau, since (7) has determinant one. This is a classical
kinetic volume, not a probability postulate or a measure on the weave's
histories. The SM stratum has zero eight-dimensional kinetic volume;
that does NOT exclude localization of a quantum state, an admitted
interaction constraint, other branches or a singular selection measure.
None of those mechanisms is computed by calling a state “typical”.

At enhancement loci extra massless fields occur. A fixed light EFT and
the old heavy-only inverse cannot be continued through them without
retaining those fields. The full classical family and induced tangent
norm remain meaningful; integrating out an entire family with one
unchanging roster would not be justified.

## 6. Discrete twists are allowed reductions, not an unseen SM solution

Equation (2) permits nontrivial component-valued holonomy classes

  epsilon in H1(X,Z2)=(Z2)^2.                              (11)

For instance U=s,V=1 is flat in K, commutes with the principal background
and has trivial peripheral commutator. The same local F/D equations and
finite norm apply with those transition functions. This is an explicit
additional flat REDUCTION of the parent; it is not represented by the
old globally Lie-algebra-valued Y form C. The four component labels are
not asserted to be topological superselection sectors of the full E8
field theory: changing the principal Higgs reduction can connect sectors
that are distinct as K bundles.

They cannot preserve a rank-four gauge torus in this same principal
background. Any maximal torus T_g of SU5_g has

  C_K(T_g)=T_g.                                           (12)

For the identity component this is the usual torus centralizer. For an
element g s in the other component, its action on T_g, if it centralized
it, would require a Weyl transformation acting as minus identity on A4.
The A4 Weyl group S5 has no such element: on the sum-zero subspace the
trace of a permutation is (# fixed coordinates)-1>=-1, whereas minus
identity has trace -4. Equivalently C_E8(T_g) has Lie algebra t_g+su5_b,
and centralizing the principal triple leaves only T_g. Thus an outer
holonomy cannot centralize a full rank-four torus. A rank-four surviving
SM subgroup is excluded in these particular twisted reductions, not
elsewhere in the architecture.

For U=s,V=1 the invariant algebra in su5_g is so5, directly from
X=-X^T in the compact form. This is a control, not a complete spectrum
or a new interpretation of so5 as SM. Computing its physical matter,
domains and interactions is a separate task if that branch is pursued.

## 7. What changes for the mission

The preferred order-seven Y state is now placed inside its entire
eight-dimensional commuting flat branch, with a derived SAME-ACTION
kinetic metric, a precise SM enhancement stratum, a disconnected gauge
identification and explicit additional twisted reductions. The source's
connected gauge phase, its zero charged index and its domain-qualified
positive results survive with their actual scopes.

No foundational premise, parent coupling, spin choice or physical
identification is counted as removed. The metric and finite quotient
are determined outputs of the supplied parent. The genuine selection
duty is now sharper: derive a state, interaction law or distribution on
this family from the native architecture, retaining any enhancement
modes, rather than assume the 3+2 degeneracy and order-seven point and
then seek their physics. The family is a control on that duty, not the
entire emergence programme or a replacement target.

The new centralizer construction, compact/complex transfer, complete
gauge-domain admission, full kinetic factors and stratum interpretation
require independent scrutiny. No new numerical producer is admitted by
writing this note or by the earlier P210 execution. The next scientific
run, if needed, needs its own source-complete reviewed specification.
