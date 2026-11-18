# The action join and the one remaining selection calculation

2026-11-18. P-C8 author hand derivation; not independently checked.
No scientific execution, CAS, imports, quadrature or tests ran.
This completes the bounded source/action map in the P-C8 card. It
does not claim completion of a physical construction or the mission.

## 1. Preserve the two actual constructions

The magnetic model in main's level6_higgs.py declares a compact torus,
fluxes (3,3,6), characteristics, Wilson assignments, a set of points
and sector weights, the golden geodesic and its mode transport. It
then defines a quadratic prescription K-c B, with c positive. These
are model premises. The geometric connection in this package earns
part of K conditionally on that embedding and propagation law. It
does not derive physical propagation in moduli space or the meaning
of summing over different Wilson backgrounds.

The curved E8 action in weave_curved_action_2026_10_08/PROOF.md
instead has a complete punctured surface, a specified metric and spin
and gauge bundles, a positive field metric, a gauge coupling, an
affine connection field and two spin fields q,r. Its actual potential is

    g6² V = integral kappa(
       Omega^-1 (|Dbar_A q|²+|Dbar_A r|²)
       +2|[q,r]|²
       +|F+Omega([q,q†]+[r,r†])|²/(2 Omega²)).          (1)

Its stationary zero-residual equations involve all three terms. Its
fermion terms follow from the same superpotential Hessian and gauge
Killing map. The complete-domain and nonlinear-response analysis
remains conditional on the unverified analytic lemmas already listed
in P-C3 to C7; the bounded complete-cusp inverse is still owed.

Nothing in the magnetic source specifies a map taking its modes,
flux, spin and compact domain to the fields and complete domain of
(1). Conversely (1) does not contain the source's radiative bubble
prescription merely because it has cubic couplings. Keeping both
positives does not make their states or actions identical.

## 2. An action-derived comparison must include the Gauss response

There is a concrete route for earning a comparison instead of typing
one. Let X(p) be a family of actual stationary backgrounds of one
parent, with positive kinetic metric G and infinitesimal gauge map
k_X. A change v of p has raw tangent partial_v X. The mixed kinetic
term, including the connection, depends on

    delta_v^hor X=partial_v X-k_X a_v,

where a_v is the compensating gauge field along that variation.
Varying its quadratic norm gives the Gauss equation

    k_X† k_X a_v=k_X† partial_v X.                    (2)

The adjoints and domain here are those of G and the parent's end
law. A stabilizer in ker k_X is retained as the unbroken gauge sector,
not inverted. Range, solvability and end flux cannot be inferred from
a finite positive matrix example. Equation (2) is the variational
identity; this note proves no new complete-cusp inverse for it.

For actual matter zero modes e_a(p), the corresponding connection is

    Gamma_ab(v)=<e_a, nabla_v^hor e_b>_physical,       (3)

including (2), spin/metric transport and the actual field representation.
The normalized magnetic functions give a candidate before this full
gauge/source problem is solved. Their unit-cell connection and geometric
kinetic term were derived in WILSON_FAMILY_TRANSPORT.md. They are not
a substitute for (2) in a different parent.

The shared action must also decide whether its Wilson labels are
alternative vacua, sectors that coexist, sites with link fields, or a
measure over configurations. Parallel transport of Hilbert spaces
alone does not supply a physical interaction or averaging measure.
This is where a sector-composition input could otherwise return.

## 3. The field map has testable conditions

A proposed linearized map F from magnetic coefficients to actual
parent modes must carry, at a minimum,

    F† G_parent F=G_magnetic,
    F rho_magnetic(g)=rho_parent(g) F,
    D_parent F=F D_magnetic,                           (4)

on the stated operator domains, with the actual spin, central lifts,
end transitions and zero modes. Here D denotes the claimed operator,
not a numerical dimension count. The interaction tensor must pull
back to the actual source overlap with the same norms. If a massive
or continuum complement is eliminated, its constrained response must
be included rather than declaring the zero-mode restriction exact.
These conditions identify specific failures of a proposed join; they
do not assert that no such join can exist.

For example the existing physical transverse-response proof has two
spin coefficients t_+,t_- of opposite Q_em charges, with a neutral A
and W_light=y A t_+ t_-. The two C8 ground coefficients are two
internal modes. Their monodromy signs are not Q_em charges.

If both magnetic coefficients have one fixed nonzero gauge charge q,
a complex-linear equivariant map into one +q and one -q line has
rank at most one. This follows immediately by applying a gauge
rotation to (4). An identification t_-=bar z_- can instead change
that charge, but is real-linear, changes the complex structure and
makes y A z_+ bar z_- nonholomorphic in those z variables. Its
fermion, conjugation and superpotential map must then be earned too.
This is a conditional typing obstruction, not a universal no-go for
other embeddings or a claim that the magnetic source has already
assigned Q_em to these two coefficients.

## 4. Derive the full relaxed quartic, not a frozen-field value

There is an exact abstract formula for the next classical calculation
once a common stationary parent and its domains are given. Include
the factor 1/sqrt(2) in the moment residual and the actual kinetic
weights, so its potential is V=||R(X)||² and R(X0)=0. For a zero
mode h, let L=dR_X0 and Q(h)=(1/2)d²R_X0[h,h]. A controlled two-jet
X=X0+epsilon h+epsilon² beta+o(epsilon²) then has

    V4(h;beta)=||L beta+Q(h)||².                     (5)

If the allowed second-order corrections form the stated linear domain,

    inf_beta V4(h;beta)
        =||P_ker(L†) Q(h)||².                        (6)

The equality of the infimum uses orthogonal projection onto the
closure of ran L. It does not require that range to be closed. A
minimizing beta or a stationary solution realizing that infimum DOES
require additional range and nonlinear existence analysis. Diverging
corrections in a minimizing sequence are not one controlled two-jet.
If nonlinear boundary constraints give an affine allowed beta-space,
their derived quadratic source first has to be added to Q. Boundary
sources and complete-domain surface terms cannot be discarded in (6).

Equation (6) is thus a useful target and a lower-envelope calculation,
not an existence proof. It makes the complete-cusp analytic duty
visible instead of assuming an inverse while eliminating heavy modes.

The protected spin quartic of 2026-11-16 explicitly constructs only
some bounded elements of ker L†. Its bound is preserved:

    V4 >= |y|² (|t_+ t_-|²+|A|² N)+(e²/2) Delta²,
    N=|t_+|²+|t_-|², Delta=|t_+|²-|t_-|²,
    |y|²/e²>2 in that stated curved background.       (7)

It proves an unavoidable interaction for those charged tangents,
conditional on its source/domain lemmas. It does not prove saturation
of (6). In particular the negative Delta² coefficient obtained by
rewriting its right side does not establish the sign of a complete
quartic anisotropy. A further positive residual contribution c Delta²
with c>=0 would preserve the lower bound and change that sign. This
is an algebraic adverse control, not a term added to the programme.
Taking the difference of two lower bounds cannot establish the
difference of the actual two energies. The charge typing of section 3
is an independent reason not to transfer (7) onto the C8 ground pair.

## 5. A bounded, consequential target replaces an assumed selector

In the stated two-mode magnetic quadratic problem, the exact proof
in this package shows a complex two-dimensional ground space. Modulo
a common phase it is CP1, before additional physical equivalences or
interactions. The tick protects its quadratic degeneracy.

With an independently carried odd reference epsilon, the most general
tick-covariant Hermitian quadratic response is

    H_epsilon=alpha I+kappa epsilon J,
    J=(U-U†)/(2i sin(pi/6)) on the ground space.        (8)

The tensor multiplying kappa is fixed; neither its nonzero value nor
its sign is forced by that covariance. If the reference is derived
from the state rather than independent, the derivation of that
registering map replaces, rather than evades, this duty.

Without such a reference, and assuming the common phase gauge and an
analytic tick-invariant local quartic, the exact form is

    V4_eff=A N²+B Delta².                            (9)

Its consequential calculation, using (5)-(6) or the actual admitted
radiative functional when appropriate, is

    B=V4_eff(v_+)-V4_eff((v_++v_-)/sqrt(2)).           (10)

The source's scalar twirl has kappa=0 and selects no direction at
quadratic order. B<0 would reduce the fixed-amplitude directions to
two pure eigenlines; B>0 would prefer equal magnitudes; B=0 leaves
the CP1 degeneracy at that order. Even B<0 needs a relative alignment
law if an independent measuring reference is retained. A nonzero
vacuum amplitude requires its own stationary dynamics. A positive
classical quartic alone has its minimum at zero amplitude; no negative
mass or selected nonzero vacuum is inserted here.

The targeted next proof is therefore: identify one stationary parent
realizing the magnetic field/operator data, derive (2)-(3) with its
end law, and compute either kappa or the **complete** coefficient B
without changing its fields, metric, domain or reference. If the
appropriate gauge equivalence removes that apparent choice instead,
exhibit it on all these data. A chosen coefficient of either sign is
a recovery control, not a reduction of independent inputs.

## 6. Input account and mission limits

| Data | Status in this package |
|---|---|
| Compact torus, fluxes, spins, charges and mode norm | Reused model premises |
| Prime/order-five Wilson set and sector weights | Reused; no existence or ensemble law derived |
| Fibonacci/golden act and geodesic propagation | One supplied/generated thread; not the whole relational architecture |
| Six-mode transport spectrum, tick square, leakage and scalar twirl | Exact author derivations given; not independently checked |
| Magnetic projected connections and geometric kinetic terms | Derived from the declared common-bundle embedding; full Gauss/action response not proved |
| Half-point cover and order-five half | Four-sheet geometry clarified; existing native half reused with transitions |
| E8 parent, metric, coupling, background, spin and end domains | Reused conditional physical construction; no foundational derivation claimed |
| Physical field/operator/interaction map between the constructions | Missing |
| Physical composition/measure over the Wilson backgrounds | Missing |
| Alignment/reference map, actual kappa or full B, and nonzero stationary vacuum | Missing |
| Actual three chiral SM families, anomalies, physical scales and gravity | Not established by this package |

Foundational independent inputs counted removed: **zero**. Conditional
kinematic consequences have been derived instead of being supplied
again. The registering reference remains explicit; identifying it
with a physical observer, and earning any statement about qualia,
requires an additional mathematical and empirical map. It is not
inferred from an antiunitary matrix or from the existence of a norm.

This source analysis provides neither a universal impossibility nor a
derived physical selector. It supplies explicit positive transport
calculations and the exact remaining action/selection obligation.
