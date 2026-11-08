# AGY e094: useful constructions, supplied dynamics and an index mismatch

2026-11-08. **Author source and hand-mathematics audit, not an executed
reproduction or blanket branch verdict.** Exact source head:
e094ae0d0 (full commit and file hashes in the accompanying receipt).
Read the W1--W5 producer functions, new relay sections 6--8, the new
dynamic-control function and the changed C1/core-rank/magnetic blocks.
No AGY module was imported, collected or run here.

## 1. Preserve the genuine positives and classify the new premises

W1 makes several previously implicit premises explicit: a reversible
unitary quantum graph, a two-dimensional single irreducible fibre,
loop-trace invariance under Nielsen changes, and deeper-register survival.
Within that category, the determinant/trace argument recovers the
quaternion pair. For 2x2 matrices det M=((tr M)^2-tr(M^2))/2; retaining
both trace observables under a shear fixes the other determinant to one.
The SU2 trace identity then gives the familiar zero-trace quaternion
alternative after excluding the trivial representation. The geometrical
orthogonal-axis argument is stronger than sampling twenty random pairs.

This is a clearer conditional characterization, not a derivation of
unitarity, rank two, single irreducibility, graph realization, trace
observability or marking invariance from non-cancellation. Calling the
package one postulate does not eliminate those independent requirements.
In particular O2 excludes the larger covariant-family counterexamples
by stipulation; it does not show they violate the weaker OA principle.

W2's finite induced unitary register is a useful positive. Its block
formula follows from the affine cocycle law: block multiplication adds
the phases k.R_q P_u and k.R_(q rho(u)) P_w, giving k.R_q P_(uw).
One nonzero unitary block in each row/column makes the matrix unitary.
This hand argument explains the finite homomorphism checks without
promoting floating-point tolerance to an exact proof.

It changes the representation space and adds the dual momentum k. It
does not unitarily conjugate the old finite affine shear into a compact
matrix, select k or its measure/state, or derive the physical E8 field
and end law. The three separated character signatures in code do not
alone compute a full S3 action. Retain this as a compatible unitary
register construction with a precisely stated information quotient.

## 2. W3's nonzero boundary value is supplied by a displaced source

The new function writes, with a=1/A_c+1/A_t and c=A_cz,

    Gamma(b,alpha)=a b^2/2-k alpha b
                         +(alpha-alpha0)^2/(2c).

Its stationary point and Hessian determinant are correctly derived:

    b*=k alpha0/(a-c k^2),
    alpha*=a alpha0/(a-c k^2),
    det Hessian=a/c-k^2.

The positive-Hessian benchmark is legitimate algebra in THIS new
two-variable potential. It has nonzero b because alpha0=1/2 is supplied,
along with k=1/3, c=3 and the potential itself. Set alpha0=0: the same
strictly positive Hessian forces b=alpha=0. Removing the restoring term
does not reveal a free positive-Hessian nonzero solution either.

The parent did not contain this displaced handle potential or its mixed
boundary term. A flat compact holonomy is periodic modulo the actual
cocharacter lattice; alpha^2 and alpha b require a global gauge/sector
completion before they can be called its gauge-invariant potential.
A local coordinate model can be useful, but its branch, source and
coefficient must remain priced. A Chern--Simons/BF name does not derive
the required fields, degree, quantization or variation from our action.
The old core is a two-dimensional surface with a boundary circle; the
new H1(m003) and boundary torus belong to a different proposed carrier.
Its action/bundle/domain map is not supplied by b1(m003)=1.

Zero TOTAL flux does not imply zero local curvature. With b!=0 at Phi=0,
the old minimizing core has f_c=-b/A_c and the tail has f_t=b/A_t.
The original residual-zero charged operator therefore cannot simply be
reused. Substitution n=0 into the old quantized, uniform-field magnetic
eigenvalue does not compute stability of this new sign-changing sourced
background. A positive 2x2 seam Hessian is not the full E8 Hessian.

Nor is choosing nu=3/2 a computed spectral gap: in the response law
s=(nu^2-1)/(4 ell^2), s is the external Euclidean momentum parameter.
It can approach zero continuously. The declared positive value 1/8
does not minimize an actual internal spectrum, and does not remove the
previously retained gauge-centralizer spin continuum.

Repair: derive an actual permissible boundary/defect term and the
equation selecting its source from the same parent, or declare a new
candidate with all inputs. Then solve its FULL stationary equations,
domains and charged Hessian. Preserve the two-variable algebra as a
conditional model; remove the claim that it closes the old physical duty.

## 3. W4 contains a valid toy mechanism but not a derived SM3 spectrum

For a regular real mass m on a finite interval I=[-L,L], define

    D_+=partial_s+m, Dom D_+=H1(I),
    D_-=-partial_s+m, Dom D_-=H1_0(I).

Integration by parts gives the boundary form [conj(v)u]_-L^L. Thus
D_- is the actual Hilbert adjoint of D_+ in the continuum with these
domains. The exact solutions are

    u=C exp(-integral_0^s m(t)dt),
    v=C' exp(+integral_0^s m(t)dt).

On a finite interval both profiles have finite norm. The first satisfies
the unrestricted H1 domain; the second satisfies both zero endpoint
conditions only when C'=0. Variation of constants makes D_+ surjective:
for f in L2 choose u=e^-M integral_0^s e^M f. Therefore its Fredholm index
is ONE per scalar copy for EVERY such regular m, including m=0. Tensor
with an externally supplied I_3 and the index is three. A kink is not
what selects three in this finite-interval construction.

On the whole real line a tanh kink can instead give an L2 zero for one
chirality and not the other. That is a different problem: the asymptotic
mass signs and complete domain carry the selection. Neither interval
nor whole-line toy becomes the full physical OA operator by its label.

The current DISCRETE pair is not an adjoint pair. The code constructs
D_L_1d as a square 65x65 collocation matrix with no endpoint restriction.
It constructs D_R_aps_1d as (-D_s+diag(m))[:,1:-1], a 65x63 matrix.
These cannot be adjoints of each other in ANY positive Gram matrices:
the adjoint of a square 65x65 map is still 65x65. The quadrature/domain
discretization was not derived. A square finite matrix has equal kernel
and cokernel dimensions, even when singular values approximate zeros.
Subtracting kernels of these two unrelated discrete maps does not compute
the Fredholm index of a single admitted operator.

The function changes BOTH mass and domain when comparing the periodic
m=0 baseline to the wall case. It has no same-domain m=0 opposite control,
which the continuum calculation above predicts already has index one
per copy. The assigned three-dimensional family tensor factor explains
the reported multiple three. Colour commutation follows for any operator
tensored with I_colour and does not establish weak chirality, complete
SM multiplets, anomaly cancellation or a derived generation count.

No actual tangential boundary operator or its signed spectral projector
is constructed in this function. Calling the endpoint rule APS is not
its derivation from the cusp. The chosen m0=1.5, w=2 and L=4 also need
their physical action/source equations. This is not a proof that every
physical boundary mechanism fails; it identifies the missing map in this
particular implementation.

Repair: first choose the actual physical Dirac operator, Hilbert metrics
and variationally compatible domain. Discretize D and ITS weighted
adjoint on corresponding domain/codomain spaces. Compare m=0 and kink
on that SAME domain, retain conjugates and boundary modes, then earn the
mass profile and the multiplicity from the actual carrier/representation.
Keep the ordinary domain-wall mechanism as a positive recovery control.

## 4. W5's transport is on the parameter half-plane, not a 3D PDE

The code's geodesic lies in the upper-half-plane tau coordinate with
metric (dx^2+dy^2)/y^2. Its circle, distance, connection integral and real
orthogonal transport give useful internal consistency controls. An SO3
matrix preserves h.h and h-dagger h for every vector, so preservation of
their ratio follows for any such rotation. A shared left unitary change
of two Yukawa matrices preserves CKM invariants by linear algebra.

Those checks do not identify this parameter-space Levi--Civita connection
with the actual physical gauge/flavour/fermion transport on a 3-manifold.
No 3D hyperbolic Green function or joined physical Dirac/Yukawa operator
is solved in the function. The field-map, representation, metric and
norm-preserving connection must be exhibited. The chosen Wilson arguments
(0.4,0.2), square-root branch and nonlinear Yukawa map remain visible.
Basis invariance validates an implementation, not the physical choice.

## 5. Review and additional-check grades remain distinct

AGY section 6 explicitly cites our d1a commit and correct specification
hash. It is useful nonauthoring commentary. However its metric sentence
calls our two-dimensional cusp a 3D hyperbolic metric; our actual source
is a 4D theory valued on a two-dimensional internal surface. It also
writes the magnetic energy with g_eff^2 rather than establishing the
source's c_H/g6^2 convention. Its wrapper paragraph does not enumerate
the thirteen infrastructure sources, before/after custody, exact gate
bindings or main acceptance. Do not turn this paragraph into an exact
source-complete/admission artifact for our packet.

Section 8 ports useful finite algebra from our seven-control DESIGN,
including Bessel polynomials, response derivatives and handle cancellation.
It correctly labels the spectral example a surrogate. Its matrix-order
and group examples use floating-point arithmetic, so the blanket
description 'all seven exact controls' should be narrowed accordingly.
It does not run our subsequently implemented source, certify the actual
core PDE, or supply its independent analytic review.

The new relative cellular ranks improve on the literal 2. The stated
relative C0 has dimension zero, while its code retains a 1x2 zero row;
that leaves H1 unchanged but is not the actual degree-zero quotient.
The new magnetic 2x2 matrix has eigenvalue -5|n| by construction; it
has not been derived there from the old full charged polarization operator.
The forged-mode algebra now supplies a real counterexample, though the
dead `... is False and False` variable should be removed and it is still
a local dictionary comparator, not injection into our frozen tests.

## Verdict and next physical opportunity

Preserve the unitary-register construction, conditional quadratic source
algebra, ordinary kink mechanism and transport consistency tests. They
are useful constructions and recovery controls. Their current joins do
not derive boundary dynamics, chirality or three SM generations from OA;
no additional foundational or observed-parameter reduction is established.

The promising next question remains the one already adopted: can the
register and common action FORCE a permissible boundary/source law and
its physical operator domain? Derive that map before adding a displaced
source or chiral projector. The actual compact-core response and same-
action nonlinear backreaction are our contribution toward that duty.
This audit scopes the new constructions; it does not exclude the wider
generated architecture or negate earlier banked positives.
