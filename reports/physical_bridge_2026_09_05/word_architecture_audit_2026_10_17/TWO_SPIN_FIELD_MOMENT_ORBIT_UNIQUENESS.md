# The same moment equation fixes a bounded Hermitian orbit representative

October 26, 2026. Authored analytical continuation, UNREVIEWED. No
scientific import, symbolic engine, test collection, numerical experiment
or banking. This is a direct calculation in the existing two-spin-field
parent, not an invocation of ordinary-Higgs nonabelian Hodge theory.

## Reduction duty and actual prior work

Question: after a holomorphic field orbit is fixed, can an additional
bounded Hermitian deformation supply freely adjustable moment-flat
profiles in the same finite-norm complete-surface class?

The [real-Cartan comparison](GLOBAL_CARTAN_AMPLITUDE_MATCHING.md) already
answers a scalar subcase. Here both q and r and a non-Cartan generator
are retained. This does not select a holomorphic orbit, prove existence,
derive the action or select a physical state among all allowed words.
It concerns every configuration satisfying the hypotheses below, not
one privileged manifold or one chosen compact triple.

Read sources: the complete [curved parent](../weave_curved_action_2026_10_08/PROOF.md),
[spinor joint](../spinor_uniformization_joint_2026_10_14/PROOF.md),
[neutral family](../weave_neutral_stability_2026_10_08/PROOF.md), global
Cartan comparison, [compact-cover stationary proof](../silver_cover_stationary_2026_10_13/PROOF.md),
and [earlier selection intake](../QUANTUM_SELECTION_INTAKE_2026_10_05.md).
The received projective_global_metric_2026_09_21/PROOF.md was read
completely too: its flat SL4 harmonic-map existence/excess-energy
problem is different and is not transferred here. Targeted source
searches used complex gauge orbit, Kempf--Ness, harmonic metric
uniqueness and moment map convexity in this lane, LAW_MAP, OPEN_LEADS
and frontier source files. These are navigation, not a complete absence
sweep or claim of literature novelty. The convexity mechanism is
standard; the task here is its exact two-spin action and end scope.

## Hypotheses, including the ends

Fix the original compact unitary gauge bundle, positive invariant trace
kappa, spin line S and finite-area complete surface with
g=Omega^2(dx^2+dy^2). There is no physical boundary or inserted source.
Use the source's real Hermitian connection, complex q,r in ad(P) tensor S,

    D_a=partial_a-i[A_a,.],
    F=partial_x A_y-partial_y A_x-i[A_x,A_y],
    mu=F+Omega([q,q dagger]+[r,r dagger]).

Let xi be one FIXED smooth Hermitian adjoint section. It is globally
defined, uniformly bounded and independent of the path parameter s.
Consider a smooth path for 0<=s<=1 satisfying

    partial_s A_x = D_y xi,
    partial_s A_y = -D_x xi,
    partial_s q = [xi,q],
    partial_s r = [xi,r].                                  (1)

These are actual field deformations, not compact gauge equivalences.
They are the Hermitian exponential direction of the complexified gauge
action, in the old compact-reality coordinates. They preserve the spin
degree and do not identify S with K.

Require q_0,r_0 to have finite source kinetic norm and D_(A0) xi to
be L2 in the conformally invariant connection norm:

    integral Omega (|q_0|^2+|r_0|^2) dxdy < infinity,
    integral (|D_x xi|^2+|D_y xi|^2)_(s=0) dxdy < infinity.  (2)

Assume the smooth path exists globally in the same bundles. To interpret
it as a comparison of physical configurations, also require its actual
domain, nonlinear products and differentiability conditions of the old
parent; the proof below does not establish that every formal complex
gauge change preserves them. Assume the two endpoints satisfy mu=0.

Use the source's compactly supported exhausting cutoffs chi_R, with
0<=chi_R<=1, chi_R increasing to 1 and
sup |d chi_R|_g tending to zero. Bounded xi and finite area imply
xi is L2(dvol_g). This end hypothesis, rather than a discarded formal
surface term, will justify the global comparison. An unbounded exponent,
infinite-area norm class, physical cut or singular defect requires a
new estimate and is not covered automatically.

## Check the path, all residuals and reality

Hermiticity of xi and A implies the first two derivatives in (1) are
Hermitian. In the holomorphic connection coordinate A=A_x+i A_y,

    partial_s A=-i Dbar_A xi.

Using the derivation rule and -i times -i equal to -1 gives

    partial_s(Dbar_A q)=[xi,Dbar_A q],
    partial_s(Dbar_A r)=[xi,Dbar_A r],
    partial_s[q,r]=[xi,[q,r]].                              (3)

Thus zero holomorphic and commuting residuals remain zero if initially
zero. The moment equation is a further constraint, not automatic from
(3). No q/r interaction has been deleted.

Along the path, q_s=exp(s xi) q_0 exp(-s xi), and likewise r.
Uniform boundedness of xi on a finite s interval preserves their L2
bounds. Also

    partial_s(D_x xi)= i[xi,D_y xi],
    partial_s(D_y xi)=-i[xi,D_x xi].                         (4)

Finite-dimensional commutator bounds and the differential inequality
for their squared sum give a uniform L2 bound on D_(As) xi by
Gronwall, starting from (2). All estimates below are therefore uniform
in s. This does not require xi to be parallel or the fields to lie in
a chosen sl2 subalgebra.

## Positive real moment differential with its actual factor two

Variation of the curvature in (1) gives

    partial_s F=-(D_x D_x+D_y D_y)xi.                      (5)

For either spin field, put U=[xi,q]. Since xi is Hermitian,
partial_s q dagger=U dagger=-[xi,q dagger]. Invariant trace gives

    kappa(xi,partial_s[q,q dagger])
      =Tr(xi([U,q dagger]+[q,U dagger]))
      =2 Tr(U dagger U).                                 (6)

The same formula holds for r. This checks the sign and multiplicity
directly in the old action; no freely chosen moment coefficient enters.
For compactly supported chi define

    F_chi(s)=integral chi kappa(xi,mu_s) dxdy.

There is no boundary term at infinity at this finite-cutoff stage.
From (5)--(6), integration by parts gives

    partial_s F_chi
      = integral chi [ |D_x xi|^2+|D_y xi|^2
              +2 Omega(|[xi,q]|^2+|[xi,r]|^2) ] dxdy
        + integral sum_a (partial_a chi) kappa(xi,D_a xi) dxdy.
                                                               (7)

The first line is the actual real field-space metric evaluated on
the compact gauge tangent: with the source's complex metric G it is
2 G(k_xi,k_xi). This supplies a normalization cross-check of (6).

## The global identity, with the cutoff error controlled

Both endpoints have mu=0, so F_chi(1)-F_chi(0)=0 exactly.
The magnitude of the s-integrated second line of (7) is bounded by

    sup |d chi|_g * ||xi||_(L2 dvol_g)
         * sup_(0<=s<=1) ||D_(As) xi||_(L2 dxdy).           (8)

A fixed harmless coordinate Cauchy--Schwarz constant can be included.
All factors other than the cutoff derivative are finite by the stated
hypotheses and (4). Consequently the error tends to zero. Integrating
(7) in s and taking the increasing-cutoff limit yields

    0 = integral_0^1 ds integral dxdy
           [ |D_x xi|^2+|D_y xi|^2
             +2 Omega(|[xi,q]|^2+|[xi,r]|^2) ].             (9)

This uses positivity and monotone convergence, not an assumed global
primitive for the moment functional or the cancellation of divergent
energies. Smoothness upgrades the almost-everywhere vanishing to

    D_(As) xi=0, [xi,q_s]=[xi,r_s]=0, for every s.           (10)

Every derivative in (1) vanishes. Hence the two endpoint FIELD
CONFIGURATIONS coincide; the entire path is constant. xi itself need
not be zero: a common parallel stabilizer can act trivially on the fields.

This is uniqueness along the stated bounded Hermitian path, conditional
on existence of endpoints and the end/norm hypotheses. It is NOT an
existence theorem, coercive inverse estimate, classification of all
complex gauge transformations or proof that any two configurations can
be connected by such an admitted path. To extend to a general polar
decomposition, its compact factor, global logarithm and this path's
domain/norm requirements must actually be checked. No such extension
is silently assumed.

## Recovery and surviving freedom

For the older compact triple choose xi=u H0/2, starting at q0 and r0=0.
Then q_s=exp(su)q0 and A_s=A0-s(H0/2)*du. The integrand in (9) is

    kappa(H0,H0)/4 * [ |du|_flat^2+Omega^2 u^2 exp(2su) ].

Here Tr(H0^2)=2 Tr(E0 dagger E0) fixes the second factor. When u is
bounded and du has the required finite norm, the only possibility is
u=0. This recovers the previous matching conclusion on its overlap,
without pretending that a scalar proof already treated non-Cartan fields.

The neutral family Q0+c psi Z, the different two-field solutions and
changes of holomorphic data are not eliminated: the argument requires
the two endpoints to be related by (1) with all its hypotheses. It
does not establish that relation between different values of c. In
particular the neutral invariant norm remains genuine source evidence.
Nonzero-moment stationary phases are not mu=0 endpoints and are outside
the comparison. Changed ends, defects and physical boundaries retain
their own laws and boundary contributions.

Even when a transformation stabilizes the bulk fields, its action on
an external measuring sector or registered lift cannot be erased from
the full relational record without checking that action. Equality of
the displayed fields is not a theorem that every registering act is
the identity. The result does not derive an observer or qualia.

## Before/after input account and next physical step

Before: holomorphic data plus a potentially independently chosen real
profile. After: within a fixed bounded admissible Hermitian path class,
there is at most one moment-flat field configuration. There is no new
freely adjustable real profile inside that class once it exists.

Still supplied: the parent, metric, spin/gauge bundle, holomorphic orbit,
physical domain, common action coefficient and physical identification.
No foundational input row or SM parameter is paid. The full generated
architecture is not reduced to one orbit. This result could reduce a
conditional search over representatives to the genuinely distinct
holomorphic data, with an existence/admission duty for each class.

The useful next question is which such data the complete generated
registered architecture actually admits and how its coefficient map
acts on the full physical fields. One cannot choose a desired chiral
domain or favourable orbit in place of deriving that map. Conversely,
failure of one orbit does not exclude the others.

Separate proof review must scrutinize the compact-reality path signs,
trace identity, uniform end estimates, two-field preservation and the
limited uniqueness statement. The radial v2 review does NOT cover
this successor. Any finite controls require their own sealed design
and review/admission before execution; finite matrices cannot certify
global existence or the cutoff hypotheses. No science has been run.
