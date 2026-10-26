# Extending the local core: compact ordinary-Higgs geometry and its price

October 27, 2026. UNREVIEWED author analytical continuation. No
scientific executable, symbolic engine, test collection or numerical
experiment was run. This is a conditional compact-fibre construction,
not the full physical parent, a four-dimensional SM vacuum or a
foundationally selected Higgs state.

## 1. Which continuation is being tested?

The existing genus-three quaternion cover Y is reused from
weave_form_parent_2026_10_08 and THETA_ROOT_COVER_AND_GLOBAL_SCOPE.
QUATERNION_ORBIFOLD_DOMAIN_AND_METRIC_PRICE supplies a local smooth
noncommuting normal core, with its changed physical metric and spin/R
isotropy costs explicit. The question here is whether its ordinary
K-valued local form has a genuine compact continuation, instead of
gluing arbitrary copies and calling their free amplitude a prediction.

This question was already named in surface_variational_join/NEXT_TEST
and surface_interacting_domain/NEXT_TEST: recover the cover/Hodge data,
then check the correct stability theorem and physical dictionary. The
spinor_uniformization_joint proof was reread and its field-degree
warning is binding. The two-spin parent has fields in ad(P) tensor S,
S^2=K; it is NOT the ordinary Higgs system used in the next sections.

## 2. Exact local dictionary to the classical curve equations

Keep the local fundamental root convention

    H=diag(1,-1), E+=upper unit matrix,
    E-=-lower unit matrix, E+^dagger=-E-,
    [E+,E-]=-H, [H,E+]=2E+.

For a complex coordinate w set Phi=(Q_w/2)dw. Then

    F_A+[Phi,Phi^dagger]=0, Dbar_A Phi=0             (1)

becomes exactly the previous normal equations

    F_xy-(i/2)[Q_w,Q_w^dagger]=0, Dbar_A Q_w=0.

Indeed dw wedge dbar(w)=-2i dx wedge dy. There is no freely assigned
relative factor between the curvature and Higgs terms in this dictionary.
These are the ordinary curve Hitchin equations, conformally invariant
with Phi a one-form; they are not identified with the two-spin equations.

In the old local core k=4lambda^2, s=1-k|w|^2,

    A=i k(-y dx+x dy)H/s, Q_w=4lambda E+/s.

Define u=log(sqrt(k))-log(s), for k>0. Direct differentiation gives

    u_wbarw=k/s^2=exp(2u),
    A_barw=-(1/2)u_barw H,
    Q_w=2 exp(u)E+.                                (2)

The metric exp(2u)|dw|^2 has curvature
-exp(-2u) Delta u=-4. Thus this local core is the standard ordinary
uniformizing solution in a disk chart. This is a mathematical map,
not an inference from equal coefficients or a new discovery of
uniformization. With W=sqrt(k)w, its auxiliary metric is
|dW|^2/(1-|W|^2)^2; changing k changes the normalization of the local
coordinate chart. If a physical cutoff/metric/measuring frame is held
fixed instead, the old local family can still have physically different
amplitudes. The global construction must specify which data travel.

## 3. Compact flux balance prevents an unpriced trivial-line gluing

For a compact continuation with a globally defined diagonal splitting
E=L direct-sum L^(-1), suppose Phi is nonzero, nilpotent and takes
L^(-1) into L tensor K_Y, annihilating L. Let the unitary connection
preserve this splitting. Locally A=i a H and Q_w=f E+. Equation (1)
gives

    da=(1/2)|f|^2 dx wedge dy.

Using the convention deg L=(i/2pi) integral F_L,

    deg L=-(1/4pi) integral_Y |f|^2 dx dy.           (3)

The integrand is globally defined as the squared norm of the K-valued
coefficient times area; its conformal factors cancel. A nonzero field
therefore requires deg L<0. A preserved trivial degree-zero line cannot
support this particular source-free compact root ansatz. This is not
a no-go for non-diagonal connections, defects, other Higgs data or the
full architecture. If the Cartan is not globally preserved, do not
integrate a chosen local H as if it were a global line splitting.

Write deg L=-d, d a positive integer. Holomorphy means that the nonzero
coefficient is a section of K_Y L^2. Since deg K_Y=4, its zero divisor
has degree

    deg D=4-2d>=0.

Within this split nilpotent class on genus three, d is consequently
1 or 2. d=1 carries a degree-two divisor. d=2 has no zeros and
L^2=K_Y^(-1). Choosing the zero-free branch is an additional condition,
not implied by the old local core being nonzero on a small disk.
The d=1 alternatives are retained; not every degree-minus-one line
automatically has the required nonzero section.

This supplies an explicit global consistency test before gluing the
root charts. It also prevents treating their integrated Higgs size
as independent of the degree in that specified compact problem.

## 4. A nonzero compact solution exists in the zero-free ordinary branch

Fix a holomorphic square root S of K_Y, set L=S^(-1) and
E=S^(-1) direct-sum S. Take the nonzero constant holomorphic map

    Phi: S -> S^(-1) tensor K_Y = S,

and zero on S^(-1). This is the nilpotent Higgs field in (1), with
the relative coefficient fixed by section 2's convention. At a generic
point it is a single nonzero Jordan block. Its only invariant line is
its kernel L; saturation extends this line across the compact curve.
Since deg L=-2<0=deg E/2, the pair is stable. It meets the hypotheses
of the ordinary rank-two compact existence theorem.

Equivalently, take the unique curvature-minus-four metric in Y's fixed
conformal class. Its induced connection on S^(-1) and the above Higgs
give (2) in unitary local frames. The coordinate and bundle factors
transform together, so these local solutions define a global ordinary
Higgs pair on Y. It is smooth at the old four branch points. The compact
fibre has no physical boundary there, and its smooth-field action/Dirac
domain has no independently adjustable puncture projector.

The uniqueness of the auxiliary constant-curvature metric also has a
short independent check. If g1=exp(2v)g0 and both have curvature -4,
the curvature transformation gives Delta_g0 v=4(exp(2v)-1), using
Delta=div grad. A positive maximum contradicts Delta v<=0; a negative
minimum contradicts Delta v>=0. Compactness therefore gives v=0.
This compares metrics in one fixed conformal class, not different Y's.

The mathematical existence/uniqueness statements used here are classical.
I personally read Hitchin, The Self-Duality Equations on a Riemann
Surface, the reduction and Example 1.5 (printed pp.64--66), Theorems
2.1 and 2.7 and their arguments, and the complete proof of Theorem 4.3
with Corollary 4.23 (printed pp.78--84), on October 27:
https://pagine.dm.unipi.it/~a019210/Hitchin_Self-duality%20Equation%20on%20a%20Riemann%20surface.pdf
The paper's whole 68 pages were not reread in this checkpoint. The
application to the already specified Y and the normalization/degree
checks here are authored deductions, not independently reviewed results.

For fixed holomorphic pair the harmonic representative is unique up to
the stated unitary gauge equivalence. This does not select the complex
curve, holomorphic orbit or global physical gauge embedding. Multiplying
the nonzero holomorphic nilpotent coefficient by a constant can be
undone by a constant complex diagonal bundle automorphism. Re-solving
the harmonic metric stays in the same fixed complex gauge orbit; it
does not generate an extra physical size parameter of that orbit.
Transport the metric and all fields; do not rescale Q alone.

Equation (3) in d=2 fixes integral |f|^2 dxdy=8pi in the declared root
normalization (multiply by the actual coefficient norm if using another
invariant trace). This is a compact geometric norm, not an observed
mass, electroweak expectation value or dimensionless SM prediction.

## 5. Which metric, and which quotient lift?

The metric encoded by u is the harmonic-bundle/uniformizing metric
in this construction. A separate physical metric chosen in the same
conformal class need not be identical to it. Equation (1)'s conformal
invariance does not certify the full untwisted reduced-YM action or
its physical fermion operator under every rescaling. The ordinary-Higgs
twist, curvature terms, kinetic map and full parent must still be shown.
No physical scale is derived by setting an auxiliary curvature to -4.

Every holomorphic deck transformation of Y preserves its unique
uniformizing metric. At the ADJOINT/SO(3) level the bundle is

    End_0(E)=O_Y direct-sum K_Y^(-1) direct-sum K_Y,

so this geometric solution has a natural spin-root-independent
description. Changing S by a two-torsion line leaves these adjoint
summands unchanged. This is useful descent data, not the complete
full-E8 gauge/fermion lift. Individual S choices need not be preserved
or linearized by the whole Q8 action. A projective action is not an
earned honest SU(2) action on all charged modules.

There is a concrete local compatibility test. The nontrivial stabilizer
c at a ramification point has order two and sends w to -w. Its induced
action on the canonical cotangent fibre is -1. A lift to S compatible
with S^2=K must therefore act there by a scalar t with t^2=-1. But an
honest order-two action on S would require t^2=1. Thus this square-root
bundle cannot carry an honest stabilizer action compatible with the
canonical square map alone. In E=S^(-1) plus S the corresponding local
matrix diag(t^(-1),t) has square -I; its adjoint action has square I.
This is the local reason the adjoint descent does not settle charged
doublet descent. An extended spin/R/gauge action can compensate it;
this argument does not exclude such a combined lift or determine its
global based relations. It is not a claim that every invariant line
bundle lacks every possible linearization: compatibility with the
specified canonical square map is essential.

In particular the actual root SU(2) in E8 has nontrivial central action
on its doublet sectors. An SO(3)-only construction cannot be transplanted
to those sectors without the actual spin/R/gauge compensation, all
based relations, the measuring register and the complementary modes.
The previous local -T lift remains a local positive; it does not prove
the missing global lift. Nor is the old flat Q8 coefficient retained
unchanged after introducing this nonflat harmonic connection.

## 6. Before/after input account and connection to the main mission

| Duty | Conditional progress | Still supplied or open |
|---|---|---|
| Can the smooth local ordinary core have a compact nonzero continuation? | Yes, on fixed Y in the specified stable uniformizing branch | Why this branch/ordinary parent is physically generated |
| Is its harmonic metric an independent function after the holomorphic pair is fixed? | No: the compact theorem supplies a unique representative up to gauge | Curve, holomorphic pair, lift and physical metric/separation map |
| Is the nilpotent size independent of compact flux degree? | No, equation (3) fixes its integrated size in this ansatz | Physical amplitude, units and coupling map |
| Is a puncture plane still free in this completed smooth model? | No: regular completed domain | Admission of the completion, global E8/fermion transport |
| Does it derive agy's inverse-Gram Higgs or order-ten state? | No such identification follows | Actual same-parent Hessian, source/partner equations and selector |

This is a constructive background worth testing for the actual induced
response, rather than inventing a source. It is not a completed global
field on the whole elliptic/modular surface: tau-dependence, mixed
equations, cusp behavior and the physical field/action map remain.
No old zero-Higgs particle count or index is transferred to this
nonzero ordinary background. The spin-valued parent and its existing
graded condensates keep their own separate equations and successes.

The full mission stays active. This note pays a bounded existence/
harmonic-metric dependence inside a supplied model, pending review;
it pays no foundational input or physical SM3/gravity obligation.
All frozen experiments and historical failures remain unchanged.
