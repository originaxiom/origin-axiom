# The actual relative gauge trace as a geodesic expression

October 29, 2026. UNREVIEWED authored conditional derivation. No new
scientific producer, CAS, trace-formula solver, numerical determinant or
comparison with data was executed. All conclusions below depend on the
same supplied action, principal parallel phase, complete domains and
hyperbolic once-punctured elliptic carrier of the preceding notes.

## 1. Named dependency and what is already determined

The two-response proof reduces the full physical relative one-loop trace
to E_q(t) and O_q(t), ordinary scalar and spin Dolbeault responses.
These functions were already determined by the action and state. They
were not legitimate independent free parameters. The task here is to
exhibit their full global geometric expression, retaining the core and
cusp, instead of inserting a guessed flat-torus determinant.

Write Sigma = Gamma\H, with its actual torsion-free cofinite Fuchsian
group, and let chi:Gamma->U(1) be the supplied flat Y character. It is
trivial on the peripheral commutator. For the source example chi has
order seven. Let S be the chosen extending spin line. The compact spin
extension eta is retained; no spin has been selected by this calculation.

Primitive classes in this note are ORIENTED hyperbolic conjugacy classes
of Gamma, or closed geodesics of Sigma. These are NOT the weave's
primitive positive L/R update words, the geodesics of the modular surface,
or the geodesics of m004. Identifying those different populations would
need a new map. No such identification or probability law is asserted.

## 2. Reused sources and primary reading scope

Reuse the original TWO_HEAT_RESPONSES_AND_SCALE_FREE_COUPLING.md and its
separate author-audit supplement, the same-action real gauge/FP weights,
the physical mass proof, and the relative heat-existence argument.
They all retain their UNREVIEWED status where stated. Their hypotheses
are not made independently certified by citing a trace formula.

The locator already_banked.py query "twisted Selberg spin determinant"
returned broad settled hits. B1165's full findings were read: its
Ruelle/Selberg language concerns a different three-dimensional gravity
identification and does not supply this action's trace. Main's B1684
findings were read in full and its received W59 producer definitions
located: its determinant is on a FLAT torus. That valid earlier work is
not transferred to our curved complete carrier. No all-branch absence
or literature-priority claim is made.

Primary sources read personally, selected sections only:

* Grigor'yan--Noguchi, The Heat Kernel on Hyperbolic Space, Theorem 1.1
  and equations (1.1)--(1.8), especially the H2 kernel (1.7):
  https://doi.org/10.1112/S0024609398004780.
  The scalar orbital integral below is worked out from that kernel.
* Stan, The Selberg trace formula for spin Dirac operators on degenerating
  hyperbolic surfaces, arXiv:2212.11793v5 / Doc. Math.30 (2025), 1--39,
  DOI 10.4171/DM/986. Read the spin class-function and local-operator
  sections, the pretrace/unfolding argument in section 4, admissibility,
  and the heat specialization in section 6.2. His formula is for one
  chiral square and retains the cusp term. The flat unitary-character
  extension used below is justified explicitly, not attributed to his
  untwisted theorem. https://arxiv.org/pdf/2212.11793.

Accessed October 29. No whole-paper reading claim is made for either.

## 3. Identify the ordinary operators before using a trace formula

In a uniformizing chart Omega=1/y the existing section density for S^a
is y^(a-2) dxdy. The unitary change to the hyperbolic area norm is

    v=y^(a/2) f.

The already-derived K_a^0=-y^2 Delta+i a y D_bar becomes

    y^(a/2) K_a^0 y^(-a/2)
       = -y^2 Delta + i a y partial_x + a(a-2)/4.        (1)

For a=0 this is the ordinary nonnegative scalar Laplacian. For a=1
it is the single-chirality spin Dirac square

    -y^2 Delta + i y partial_x - 1/4.                  (2)

The opposite chirality/sign convention gives its conjugate counterpart;
the relative Serre identity already accounts for that equivalence.
Equation (2) also follows by multiplying the two off-diagonal Dirac
operators in Stan's upper-half-plane expression, with the corresponding
chirality. This fixes the heat time: no factor of two or arbitrary mass
shift may be inserted. The full doubled spin trace would count twice.

The source's extending spin has antiperiodic cusp transport, so its
Dirac square has discrete spectrum. The scalar operator has continuous
spectrum. Our scalar calculation uses a TRACE-CLASS DIFFERENCE, not a
sum of scalar discrete eigenvalues that drops scattering.

## 4. The spin lift is a class function, not a replacement Wilson line

Let epsilon_S(gamma) in {+1,-1} be spin transport along the closed
geodesic, relative to its parallel tangent frame. It is invariant under
conjugacy and inverse and satisfies

    epsilon_S(gamma^n)=epsilon_S(gamma)^n.

It need not be multiplicative on arbitrary products of group elements.
In particular it must not be identified with the flat order-two compact
line eta's character alone. Changing extending spin by a flat order-two
character sigma multiplies epsilon_S(gamma) by sigma(gamma), but the
reference spin lift itself remains. Its primitive parabolic sign is -1.
The actual weight on a repeated loop is

    epsilon_S(gamma)^n chi(gamma)^(q n).

Keeping this lift is necessary to retain the spin dependence; length
or trace magnitude by itself does not register it.

## 5. Derive the scalar orbital coefficient, including its normalization

Put ell=ell_gamma for a primitive class and L=n ell. The scalar H2
heat kernel in the source's nonnegative-Laplacian convention is

    k_t(rho)=sqrt(2) exp(-t/4)/(4 pi t)^(3/2)
             integral_rho^infinity
             u exp(-u^2/(4t))/sqrt(cosh u-cosh rho) du.

Use Fermi coordinates (r,v) about the invariant axis. The volume element
is cosh r dr dv, with primitive centralizer period ell in v. The
displacement under gamma^n satisfies

    cosh rho = cosh L + 2 sinh^2(L/2) sinh^2 r.

Writing x=sinh r, exchanging the positive integrals, and setting
A=cosh u-cosh L, B=2 sinh^2(L/2) gives

    integral_(-sqrt(A/B))^(sqrt(A/B)) dx/sqrt(A-B x^2)
       = pi/sqrt(B).

The remaining u integral is 2t exp(-L^2/(4t)). Thus the orbital heat
integral for ONE oriented primitive class and repetition n is

    ell exp(-t/4-L^2/(4t))
       /[2 sinh(L/2) sqrt(4 pi t)].                     (3)

The coefficient is the primitive ell, not L; the later determinant
integral consequently carries 1/n. Both orientations are in the
population; do not double their coefficient again.

The character-twisted heat kernel is obtained by summing the H2 kernel
over deck transformations with their flat transports. In the difference
between chi^q and 1, the identity term cancels. Every parabolic term
cancels as well, since chi is trivial on the peripheral and hence every
conjugate and power. No elliptic classes occur. Unfolding the remaining
hyperbolic classes with (3) gives

    E_q(t) = exp(-t/4)/sqrt(4 pi t)
       sum_[gamma],n>=1
       ell_gamma [chi(gamma)^(q n)-1]
       exp(-(n ell_gamma)^2/(4t)) /[2 sinh(n ell_gamma/2)]. (4)

For fixed t>0, the Gaussian in n ell makes the sum absolutely convergent.
One can bound the oriented class count by C exp(R) for this FIXED surface:
every closed hyperbolic geodesic meets a fixed compact truncation of the
cusps (a cusp cylinder contains no closed hyperbolic geodesic). Join a
point on it to a fixed core basepoint by a path of bounded length D.
The resulting based deck element moves its lift by at most R+2D.
Separated orbit points and hyperbolic disk volume bound their count by
C exp(R). A fixed systole bounds the repetitions. This argument provides
no uniform constant in a degenerating family and claims none.

Using |chi^n-1|<=2 and the same positive orbital integral justifies
unfolding after the peripheral cancellation. The previous trace-class
proof identifies the integrated diagonal difference with its operator
trace. Scattering is included in (4) through that full relative trace;
it is not set equal to the q=0 scattering matrix or discarded.

## 6. The spin response on the same global carrier

For a positive-time heat function, Stan's one-chirality orbital formula
has Gaussian exp(-L^2/(4t))/sqrt(4 pi t), WITHOUT exp(-t/4), and the
factor epsilon_S(gamma)^n. To extend it by the flat line, multiply each
deck term of the pretrace kernel by chi(gamma)^q. The multiplier has
unit modulus, is constant on conjugacy classes, and is one on each
parabolic. The core bounds in unfolding are unchanged. The alternating
parabolic series and cusp estimates are unchanged as well. Subtracting
the q=0 trace cancels the identity and cusp terms before integration.
The Gaussian satisfies the admissible test-function decay conditions.
This yields the authored flat-character extension

    O_q(t) = 1/sqrt(4 pi t)
       sum_[gamma],n>=1
       ell_gamma epsilon_S(gamma)^n [chi(gamma)^(q n)-1]
       exp(-(n ell_gamma)^2/(4t)) /[2 sinh(n ell_gamma/2)]. (5)

Absolute convergence at fixed t follows from the same class-count bound.
This is one chiral square's response, matching K_1^0, not the sum of
both spin chiralities. The flat twist is trivial on the cusp, so it has
not converted the admitted antiperiodic end into a continuous spin end.

Equations (4)--(5) determine the six responses in the order-seven source
state from its length spectrum, actual spin lift and flat character.
There is no additional character-dependent end constant to fit.

## 7. Shifted relative determinants as absolutely convergent products

Define, for real z>1,

    Z_0(q;z) = product_[gamma] product_(k>=0)
       [1-chi(gamma)^q exp(-(z+k) ell_gamma)],

    Z_S(q;z) = product_[gamma] product_(k>=0)
       [1-epsilon_S(gamma) chi(gamma)^q
                                    exp(-(z+k) ell_gamma)].          (6)

These are oriented products. Inverse classes pair their factors into
positive real values for real z>1. Define logarithms by their convergent
series, tending to zero as z->+infinity. No phase branch is fitted.

For q and r let

    A_qr(z)=log Z_0(q;z)-log Z_0(r;z),
    B_qr(z)=log Z_S(q;z)-log Z_S(r;z).

Using the positive Gaussian integral with a>=0, L>0,

    integral_0^infinity exp(-a^2 t-L^2/(4t))
                             dt/[t sqrt(4 pi t)] = exp(-a L)/L,

equations (4)--(5) imply

    -integral_0^infinity exp(-p t)[E_q(t)-E_r(t)] dt/t
         = A_qr(1/2+sqrt(p+1/4)),          p>0,

    -integral_0^infinity exp(-p t)[O_q(t)-O_r(t)] dt/t
         = B_qr(1/2+sqrt(p)),              p>1/4.        (7)

Indeed log(1-w)=-sum_n w^n/n and
exp(-zL)/(1-exp(-L))=exp(-(z-1/2)L)/(2 sinh(L/2)).
For these strict ranges the count bound permits absolute interchange
of the time integral and the geodesic/repetition sums. There are no
identity or parabolic normalization terms left to integrate: they
cancelled on the heat side, not by a chosen determinant counterterm.

The lower bound p>1/4 in the spin PRODUCT is an absolute-geodesic-sum
condition. It is not a claim that the gapped spin heat integral cannot
exist for other p when its kernels are handled. Only the displayed
range is needed in the following physical combination.

## 8. The convergence-edge term is a limit, not a raw Euler product

The physical expression needs A_32 at z=1. Both chi^2 and chi^3 are
nontrivial in the source order-seven example, so their scalar kernels
vanish. Their relative difference E_3-E_2 tends exponentially to zero
by the already-stated same-domain gap argument. It is also all-orders
small in the ultraviolet. Therefore dominated convergence in the HEAT
integral gives

    A_32(1) := limit_(p down to 0) A_32(1/2+sqrt(p+1/4))
             = -integral_0^infinity [E_3(t)-E_2(t)] dt/t. (8)

This is an Abel limit of the convergent products from z>1. Its existence
here follows from the heat-side hypotheses, rather than assuming raw
absolute convergence of an Euler product at z=1. No theorem about the
individual product at that endpoint is needed. The reference zero-mode
logarithm cancels between these two nontrivial characters.

Rejecting control: E_q by itself has infrared limit -1 for a nontrivial
chi^q. Setting p=0 in its determinant relative to the trivial line
without removing that kernel difference diverges. Equation (8) compares
two nontrivial lines, not one such line with a silently deleted reference
zero mode. This distinction is essential to the scale-free combination.

## 9. A finite list of geometric products for the physical combination

Retain the previously derived SAME-ACTION physical weights and group
coefficients. With x=exp(-t), put

    Psi_q=2[(1+x^2)E_q-(x+x^4)O_q],
    T_q=2[x O_q-x^2 E_q].

For the order-seven state the complete relative combination is

    B_C=-(6/5)(Psi_3-Psi_2)-(9/5)(T_1-T_3),
    C=alpha3^-1-(3/2)alpha2^-1+(1/2)alpha1^-1.

Insert (7)--(8) into L_C=-integral B_C(t) dt/t:

    L_C = -(12/5)[A_32(1)+A_32(2)]
           +(12/5)[B_32(3/2)+B_32(5/2)]
           -(18/5) B_13(3/2)+(18/5) A_13(2),

    Delta C = -L_C/(4 pi).                              (9)

The arguments 1, 2, 3/2 and 5/2 are fixed by the actual curvature and
principal raising normalization. They are not fitted spectral masses.
The only edge term has the explicit limit (8); every other product in
(9) is inside its absolute convergence half-plane. The gauge-adjoint
response has cancelled by its original insertion coefficients, not by
discarding charged gauge fields or their FP/gaugino partners.

This is a candidate geometric expression for a conditional one-loop
observable, not its numerical evaluation or a claimed coupling match.
It inherits the nonexceptional-character scope of the preceding note.
An order-two/order-three state cannot be substituted into (9), because
both the sevenfold charge aliases and the zero-kernel limit can fail.
Use the unspecialized formula and retain its scale term in those cases.

## 10. Controls, state scope and physical interpretation

* At chi=1, every summand of (4)--(5) is zero. With central SU5 holonomy,
  charge responses coincide within each complete gauge representation,
  recovering zero inserted gauge differences without assuming each
  response separately vanishes.
* With both orientations retained, (4) is real and nonpositive for a
  unitary character: chi^n+chi^-n-2=2(cos(theta)-1). A positive scalar
  relative heat trace would contradict this particular flat-line model.
* The spin sign is not universally +1 and is not discarded. Even with
  identical lengths, changing S can change the B-products in (9).
* Omitting the scalar exp(-t/4), doubling one spin chirality or using
  repetition length in place of primitive length changes the product
  arguments or their powers; the operator/orbital derivations reject it.
* If the charge connection has curvature, its universal-cover kernel
  is not the same ordinary kernel times a flat deck character. If its
  peripheral holonomy changes, the parabolic terms need not cancel.
  Those are different calculations, not extensions by notation.
* No numerical geometric spectrum was generated or sampled. This note
  supplies neither a certified truncation error for the edge limit nor
  a global moduli extremum. Degeneration can change the gap and requires
  separate control before exchanging any metric limit with (8).

The geometric weights here are fixed by the heat operator. They are
not a probability measure selecting a history or a world. In particular,
they do not select between main's move clock and geometric clock. The
closed-geodesic sum is over loops on a fixed physical candidate carrier,
not the main campaign's moduli-space population. A bridge would need to
be derived before using this expression as a state-distribution law.

### A same-action relative vacuum control

There is a stronger check against that last conflation. Set the external
gauge field to zero and hold the carrier, kinetic measure and domains
fixed while comparing the Wilson state with its trivial reference.
The already-derived M^dagger M=diag(P_v,P_c) matches the actual fermion
squares to the real bosonic/FP squares. At each proper time and external
Euclidean momentum, the log-determinant weights WITH spin multiplicities
are

| Internal operator | Fields | Total coefficient |
|---|---|---:|
| P_c | complex scalar and one Weyl fermion | 1 - (1/4)*4 = 0 |
| P_v | four real vector components, complex FP pair, one Weyl gaugino | (1/2)*4 - 1 - (1/4)*4 = 0 |

The four-spin-component trace in the Weyl row comes with weight -1/4;
it is not four independent Weyl fields. A common regulator therefore
makes the parity-even RELATIVE Gaussian vacuum functional identically
zero before the internal relative traces or external momentum integral
are performed. This is a fixed-action F/D-flat comparison; it does not
follow from the earlier cochain supertrace. Global zero-momentum gauge
volume factors are treated separately, not retained as propagating
vacuum modes. The zero background values of auxiliaries leave only
Wilson-independent local Gaussian measure factors in this comparison.

The external F^2 insertion changes the spin coefficients and gives
the previously derived +1,-3 response, so its finite threshold (9)
need not vanish. A gauge kinetic threshold is consequently NOT a
Wilson-selecting one-loop vacuum potential in this same construction.
This conditional cancellation does not determine a Wilson-independent
metric potential, determinant phase, anomalous measure or a broken-SUSY
completion. It neither re-computes nor contradicts W59/W62 or B1704,
whose assigned contents/action are different. Adding their potential
to (9) would still need the missing same-action identification.

## 11. Before/after accounting and review duty

Before: two ordinary relative heat functions with explicit operators,
but no displayed global geometric evaluation in this chain. After:
the proposed formulas express them through the same carrier's complete
length/spin/character data and give (9) as a finite list of product
ratios plus one controlled endpoint limit. This removes no additional
foundational premise: the functions and geometric data are two ways to
compute outputs of the same supplied action/state.

The action/field dictionary, carrier and its geometry, E8 embedding,
spin and Wilson state remain unselected. Chirality, three physical
generations, anomalies, supersymmetry breaking, state dynamics and
gravity have not been derived by this spectral calculation. A generic
mathematical spectral theorem alone does not identify a physical theory.

Independent review must inspect the scalar/one-chirality identification,
orientation multiplicities, the unitary-character extension with its
parabolic cancellation, the trace-class/scattering distinction, the
interchange bounds, the endpoint limit and physical signs in (9).
The relative Gaussian vacuum control additionally requires the common
measure, fixed-domain F/D-flat scope and the actual reducing operators;
its zero is not a conclusion about every quantum vacuum or metric.
All new steps await that review. Any numerical implementation needs
its own source-complete sealed design and genuine admission. Neither
P210 acceptance nor the completed governance-only controls approve it.
