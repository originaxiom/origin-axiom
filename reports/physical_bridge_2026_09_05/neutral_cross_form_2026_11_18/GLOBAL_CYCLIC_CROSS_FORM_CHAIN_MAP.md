# The completed cyclic cross-form has an exact global spinor chain map

2026-11-18. P-C3i source/hand scope 3cbb86bd2. **Not independently
checked.** No scientific imports, execution, CAS, quadrature or tests.
This continues the existing P-C3f endpoint duty and PHYSICAL-C5's
finite-series source review. It does not start a numerical campaign.

The fixed curved action, carrier, coherent bundle, spin/flavour map,
reference, kinetic metric and complete-domain premises remain supplied.
All statements concern the displayed completed connection class, not
every D5 connection, neutral field or generated architecture.

## 1. The earlier finite result and its remaining global duty

At af08bc3d272c01a85e7341da91cfcc43d230d64c the relevant producer is
relays/x_frontier_3_verify/verify_x_frontier_3.py:571-703. Its decisive
Clifford and contraction segment was personally read as text. It reports
a cross-form commuting with the two cyclic fields and cancellation of
its coefficient from the finite transferred differential. It does not
solve the actual global Dolbeault or nonlinear moment problem.

The completed line is

    a_N=b[X_(2,2)+(f_+ X_(-2,2)+f_- X_(2,-2))/sqrt(2)
                                      +f_+ f_- X_(-2,-2)/2].       (1)

The prior CROSS_FORM_FINITE_SERIES.md supplies a stopping certificate
for that source's finite expansion. Here a different exact chain map
addresses the global question. Its kernel result does not certify the
source's assigned comparison mass matrix or numerical mass constant.

## 2. A polynomial identity in the actual Spin5 spinors

In one principal four use the normalized source cyclic form

    Q=p e12+r e23+p e34+f e41, p r!=0.

Multiplication, with no division by f, gives

    Q²=p r(e13+e24)+p f(e31+e42).                    (2)

It has no scalar term. The two displayed sums are the highest and
lowest vector-five Clifford matrices in End(4). Their relative entries
are fixed by the principal raising action and the symplectic condition.
Thus Q² lies in that vector-five summand, not in a freely chosen
endomorphism. The other factor R has the same identity.

On either Spin10 half-spinor, Q acts on the first four and R on the
second. The D5 cross-generator action is a fixed nonzero Clifford
multiple of their vector-five product. Hence the completed cross
endomorphism is proportional to

    P_N=Q² R².                                      (3)

The fixed scalar can differ by the inherited chirality sign between
the two half-spinors; it is not an independently chosen coupling.

The coefficients in (1) can be checked directly in the producer's
Clifford normalization, without trusting its computed commutators.
Use {gamma_a,gamma_b}=2 delta_ab and
sigma_ab=gamma_a gamma_b/2 for a!=b. Then

    [sigma_ab,gamma_c]=delta_bc gamma_a-delta_ac gamma_b.

For its first five-space put v_+=gamma_2-i gamma_3,
v_-=gamma_2+i gamma_3 and w=gamma_0+i gamma_1. The literal source
E and T3 matrices give

    [E,v_+]=0, [E,v_-]=-sqrt(2) w,
    [T3,v_+]=w, [T3,v_-]=0.

Thus E+f T3 centralizes v_++(f/sqrt(2))v_- exactly. The second
five-space is the identical calculation on indices (6,7,8,9,5).
Their exterior product has ratios 1/sqrt(2),1/sqrt(2),1/2, precisely
the four source X matrices. This check is in the full Clifford algebra
before restricting its even products to either chiral spinor.
Equation (2) identifies the same line in that spinor realization,
with its highest coefficient fixed and nonzero independently of f.

This identifies the literal completed line, rather than declaring that
every operator commuting with Q,R is their product. In the vector-five
realization the cyclic matrix has four fixed raising pivots: its
kernel is the line v_top+c f v_bottom for every f. Their exterior
product is the common cross centralizer line. It agrees with (3)
on the faithful spinor action and has the prescribed nonzero highest
coefficient. No all-Lie-algebra uniqueness theorem is needed.

## 3. Global bundle and multiplier data

Let Q,R now denote the ACTUAL two Koszul generators, including their
source constant -i. Each is S-valued. Their fourth product is
S^4=K²-valued in the cross Lie subbundle. The actual marked core acts
by swapping them with phase -i, or by opposite phases -i,+i. Thus
Q² R² has trivial flat core character. This is the existing highest
B character, rather than an identification from equal dimensions.

Let beta be an actual (0,1)-form with values in S^-4, with that trivial
flat factor. Use the two physical B Hodge profiles at the reference
point to parameterize beta. A fixed nonzero normalization divides
only the reference raising pivots and the Clifford coefficient in (2).
The connection field is the D5 Lie section whose half-spinor action
is beta P_N. For the two chiral representations the fixed scalar is
carried in beta_R; its signs are determined by the same Lie section.
The connection insertion in the total Dolbeault differential includes
its original -i/2 and dbar(z); these are included in beta_R below.

The native cyclic coefficients f_+,f_- are the source's sections of
the exchanged S^4 flat lines with their one-pole allowance. They
make Q,R holomorphic for the original connection. Completing the
connection by (1) keeps [a_N,Q]=[a_N,R]=0 exactly. The raw fields
therefore satisfy every F equation on the whole carrier.

All products are physically bounded. The normalized Q,R are bounded
and approach their parallel reference values; their cyclic corrections
decay. The physical norm of beta, as an S^-4-valued one-form, is
O(rho log(1/rho)^3) at its largest allowed pole. Fixed physical
derivatives have the same decay up to logarithmic powers. The other
three terms of (1) multiply it by bounded decaying cyclic ratios.
No inverse of f, beta or a section with zeros enters this construction.

## 4. The exact full-complex equivalence

On the actual spinor tensor complex let

    delta=Q wedge e_+ + R wedge e_-,
    d_N=bar(partial)+(-1)^l delta,

where l is Dolbeault degree, and e_+,e_- denote the flavour exterior
directions with their S factors carried by Q,R. They commute as gauge
endomorphisms. With the flavour contraction operators i_+,i_-, set

    h_F=(Q R² i_+ + Q² R i_-)/2.                    (4)

The exterior anticommutator gives exactly

    delta h_F+h_F delta=Q² R².                      (5)

h_F lowers Koszul degree one and has S^4 tensor weight: contraction
in the FLAVOUR factor alone leaves one S factor when the exterior
degree is reduced. Combining it with beta gives a total-degree-zero
operator H=beta h_F, which raises Dolbeault degree one. It is zero
on l=1. In this convention

    H²=0, H d_N H=0,
    [d_N,H]=-beta P_N.                              (6)

The minus in (6) is the (-1)^l on delta after H. The Dolbeault terms
have degree two and vanish on a curve. For d_(N,b)=d_N+beta P_N,

    d_(N,b)=(1+H) d_N (1-H).                         (7)

Thus 1+H is an EXACT chain isomorphism with inverse 1-H, not a
finite-order approximation. It acts on all four total degrees.
There is no assumption that the complementary propagator is local.

The symmetrized expression (4) glues. Under the core swap, the three
gauge factors contribute i and the contraction contributes -i; the
two terms exchange. Under the diagonal core each product has the
same cancellation. The S^-4 factor of beta cancels (4)'s spin weight.
The source spin, flavour and gauge data are therefore all carried.

In the actual tensor metrics H and its inverse are bounded, with
bounded required derivatives and decaying perturbation from identity,
by section 3. They preserve compact-support cores. The identities
d_(N,b)(1+H)=(1+H)d_N and its inverse give graph-norm bounds and
extend to the complete closed domains by the same core approximation.
This is the global/domain step absent from a formal horizontal matrix.

The identity is for the spinor representations. In the vector ten
the two generators act on separate five-spaces and their product is
zero, whereas the cross Lie generator is not. Formula (3) is NOT
transferred to that representation. The pure-B up analysis remains
the separate argument of P-C3h.

## 5. The same action supplies the coupled stationary representative

Use the two existing native cyclic coordinates and two existing B
coordinates, sufficiently small. Their raw completed family is exactly
F-flat by section 3. Its full moment lies in D5, so its Q projection
is identically zero. At the origin its linear moment vanishes: each
of those four complex tangent modes is an actual reference zero mode.
The completion terms start at products of the state coordinates.

The raw moment is consequently second order in those coordinates
and is in the existing decaying weighted target class. Products,
two physical derivatives and Hermitian exponentials give the same
analytic moment map. Its reference D5 derivative is the invertible
gauge operator of P-C3e/B1959 under the stated actual-background
premises. The implicit-function theorem supplies a small bounded
decaying Hermitian response, beginning at second order, cancelling
the whole moment while retaining every F equation.

Under those analytic hypotheses this is a coupled local stationary
family of the SAME full E8 action at fixed supplied metric, with
zero internal residual potential and nonnegative bosonic Hessian.
Colour and Q remain. No arbitrary boundary condition, new scalar
interaction or finite Q balancing datum is added. The amplitudes
remain state coordinates; this existence argument selects none.

That Hermitian transformation and its inverse preserve the complete
holomorphic domains. The actual Hodge/mass isometry with its trace-dual
target then reads physical source and adjoint kernels. All adjoint
terms, including b†, enter that Hodge realization. They are not set
to zero because (7) uses only the holomorphic differential.

## 6. The retained endpoint quotient survives this completed class

Equation (7) preserves the full 128 cohomology of the native cyclic
family. The source's compact line complex has, when both cyclic
coefficients are nonzero, common divisor Z=p and length-one cohomology
in degrees one and two for each complementary gauge coefficient.
Their actual normalizable source and adjoint modes therefore survive
the completed B field and its Hermitian response. The remaining
charge-one singlet pair stays exactly zero on this coupled family.

The physical mode is a smooth L2 graph-domain representative; the
compact point-supported description does not introduce a delta-function
boundary multiplet. No numerical source mass matrix is needed for this
zero-mode statement. The complete nonzero mass spectrum is not computed.

The A3 operator commutes with all these D5 fields and with their
Hermitian response. Its additional charged threshold continua therefore
remain as well. No assertion that this finite kernel is the full
low-energy spectrum, or that the vector-ten/neutral sectors are solved,
is made by the spinor chain map.

For the chi=0, eta=O reference used in P-C3g/h, the full 128 origin
kernel is 24, becomes 16 on either nonzero single cyclic axis, and
8 when both cyclic coordinates are nonzero, independent of the
completed B coordinate. These are the source's divisor counts with
the ACTUAL chi=0 origin restored. The older 18 at retained nontrivial
Wilson is a different origin and is not inserted into this table.
Other Wilson/spin choices retain their own zero-origin character test.

This constrains exactly the completed centralizer class (1). It
does not exclude other coupled field equations, ends, carriers or
interactions. In particular a generic incomplete b X_(2,2) at
nonzero f violates the F equation and is not an admissible countermodel.

## 7. Cohomological cancellation is not input reduction

The map 1+H is not a unitary physical gauge transformation. It mixes
tensor slots of the same total degree. Pulling the physical kinetic
form back gives (1+H)† K(1+H), which depends on B. The adjoint,
normalized currents, massive spectrum and other measuring data must
travel with it. Declaring B physically absent after using (7) would
hide the state in that metric. P-C3g's pure-B vector response is an
explicit control that this direction remains physically observable.

A nontrivial 1+H with H²=0 cannot be unitary in a positive K metric:
(1+H)^n=1+nH, whose norm on any x with Hx!=0 grows with n; unitary
powers would preserve that norm. If the coordinates vary in spacetime,
derivatives of this change also enter the kinetic connection and Gauss
response. None is discarded by a static cohomology equivalence.

What is earned conditionally is a global same-action completion and
an exact reason the old endpoint pair survives this route. The local
four-term completion coefficients are derived within the displayed
ansatz, without new fitted ratios. No independent foundational input
is counted removed. Stationarity, domain estimates, the polynomial
identification, core gluing, both chirality signs and the Hodge passage
require non-authoring checking. Vacuum selection, a physical chiral
SM3 spectrum, a derived end/source law and gravity remain open.
