# R56 authored argument: a paired cubic, no neutral self-cubic

September 30, 2026. Conditional on R50's complete-domain two-jet,
R54's actual paired overlap and R55's complete light-kernel census,
with their inherited geometry/action/domain hypotheses and grades.
Finite symbolic tests are not independent acceptance of this analysis.

## 1. The tensor being classified

Fix any one of the exceptional canonical backgrounds of R54/R55.
The supplied twisted parent action has an invariant holomorphic
trilinear proportional to

    T(u,v,w) = integral kappa(u wedge [v wedge w]).

Here kappa is the fixed parent invariant bilinear, not the positive
Hermitian kinetic pairing. The Lie bracket is antisymmetric while the
one-form wedge changes sign too, so this is the symmetric cubic tensor
on commuting four-dimensional chiral coordinates. It is obtained from
the fermion term Tr(psi wedge D psi) and its auxiliary curvature partner,
not by guessing a new superpotential. The general nonabelian action is
[Braun et al. (2.13), (B.12)](https://arxiv.org/html/1812.06072v2).
Appendix B.2's commuting Morse ansatz is NOT imposed on this background.

Write the complete degree-one space as

    L = C alpha + (V tensor C beta) + (V* tensor C gamma),
    fields: S, Q in V, Qtilde in V*,  dim V = 16.

Interchanging the two charged labels is a convention. R55 gives no
additional normalizable singlet or vector-10 one-form here. R46/R49
give the Lp properties needed for absolute convergence: each relevant
triple is controlled by one L2 and two L4 norms. Invariant matrix
contraction has a uniform finite-dimensional bound in the positive
coefficient metric, including the end. We classify the DIRECT CLASSICAL
holomorphic cubic only, not every gauge interaction or D-term.

## 2. Gauge invariance exhausts the candidates

The actual E8 root branching, already established by R39/R45, identifies
the charged weights with the two D5 half-spin sets. Their five coordinates
are half-integers; hence any sum of three charged weights has half-integer
coordinates and cannot be zero. Two charged weights sum to zero only
when taken from opposite half-spin sets (D5 has odd rank). A single
charged weight is nonzero. Thus degree-three invariant candidates are
only S^3 and S times a V--V* pairing.

Cartan weight conservation alone does NOT prove uniqueness. The literal
Clifford matrices give 45 generators on V. Their Cartan weights are
distinct, so any commuting endomorphism is diagonal in that basis.
The graph joining two basis vectors when a generator has a nonzero
entry between them is connected; commuting with those entries forces
all diagonal values equal. Thus End_Spin(10)(V)=C, and the V--V* invariant
bilinear is unique. The dual matrices are -T^T, not -T or T by name.
The code checks this against the actual parent weight sets and all
generator Ward identities. Its coordinate census is a finite check
of these arguments, not a numerical physics fit.

## 3. The neutral cubic vanishes in the actual complete domain

R50, NEUTRAL_SECOND_ORDER_PROOF.md section 3, constructs a smooth
adjoint-valued one-form b=b_flat with

    D alpha = 0,    D b = -alpha wedge alpha,
    alpha in L2 intersect L4,    b in L2 and Dom D.

Its explicit polynomial primitive is
b=c2-[c,sigma]+[D sigma,sigma]/2. The second-order flat identity and
admissibility are inherited results, not a new claim that every neutral
direction integrates. Graded invariance of the trace gives

    d tr(alpha wedge b) = tr(alpha wedge alpha wedge alpha).

Use the complete smooth exhaustion cutoffs chi_R from the domain proof,
with uniformly bounded |d chi_R|, tending to one and derivative supported
outside an increasing compact set. Stokes on compact support gives

    integral chi_R tr(alpha^3)
      = -integral d chi_R wedge tr(alpha wedge b).

The absolute value on the right is bounded by a constant times
||alpha||_(L2,tail R) ||b||_(L2,tail R), which tends to zero. On the left,
alpha^3 is absolutely integrable by L2/L4/L4, so dominated convergence
applies. Therefore integral tr(alpha^3)=0. The invariant parent trace
restricted to sl4 is a fixed nonzero multiple of this trace (R39), and
[alpha wedge alpha]=2 alpha^2 in this convention. Consequently

    T(alpha,alpha,alpha)=0.

This is an INTEGRATED exactness result, not a pointwise commutativity
claim. Generic noncommuting matrix-valued one-forms have nonzero trace
cube, as the control demonstrates. Nor is H3 of ordinary cohomology
being used to discard an uncontrolled boundary term: the L2 primitive
and the displayed tail bound do the work. A different end or source
can change these premises. Complex multiples of alpha have the same
zero cubic; no all-orders complex-moduli theorem follows.

## 4. The surviving coefficient and its honest normalization

R54, NEUTRAL_MATTER_PROOF.md sections 2--4, identifies the actual
harmonic overlap with the banked nonzero connecting homomorphism.
At every admitted exceptional point it proves

    Z = integral gamma wedge (alpha wedge beta) != 0.

This is the actual dual gamma, not a copied profile in a different
metric. Parent invariance gives a nonzero multiple of the unique
V--V* pairing. Define y to be its full coefficient in the supplied
action's cubic polynomial, INCLUDING that action's trace, coupling,
orientation and field conventions. Then the complete direct cubic is

    W3 = y S sum_(A=1)^16 Q_A Qtilde^A,    y != 0.

Defining y this way does not evaluate it or assert that an arbitrary
Fox cochain number equals it. R54 supplies nonvanishing, not its value.

The positive kinetic Gram is Spin(10)-invariant. The three representations
1,V,V* are inequivalent with multiplicity one, hence it has blocks
K_S, K_Q I16, K_Qtilde I16 in orthonormal representation bases. Each
K is finite and strictly positive by the earned L2 norms and supplied
positive action. With canonically normalized coordinates, the tensor is

    W3 = lambda S_c Q_c.Qtilde_c,
    lambda = y / sqrt(K_S K_Q K_Qtilde) != 0.

All sixteen singular values of the charged bilinear tensor equal
|lambda|. This is representation degeneracy, NOT sixteen generations
or a measured Yukawa hierarchy. Rescaling profiles by a,b,c multiplies
y by abc and the K factors by |a|^2,|b|^2,|c|^2 respectively; lambda
changes only by a removable phase. Its magnitude and nonvanishing are
basis invariant. General coordinate changes require transforming the
kinetic Gram too; ordinary singular values of an oblique matrix are
not invariant physical couplings. No numerical overlap integral is
computed here and no absolute physical scale is derived.

## 5. What follows, and what still must be earned

The formal Hessian of W3 in the two charged sectors is lambda S_c I16,
and the combined symmetric charged block is off-diagonal with rank 32
when lambda S_c != 0. This is a statement about this leading tensor,
not a proved spectrum of the full operator at nearby backgrounds.
Both dual sectors enter the SAME pairing; it supplies no mirror-only
mass mechanism. The pure neutral direct cubic is zero even though the
mixed cubic is nonzero. R52's exact real stationary curve and R54's
mixed obstruction therefore fit the same interaction picture.

We have not integrated out the complement, proved a finite EFT
truncation, computed higher products/nonlocal terms, or established
quantum nonrenormalization/vacuum selection. Gauge interactions and
D-terms are not absent. A zero projected cubic does not settle all
higher neutral obstructions. The separate finite-unitary rank-five
model has different profiles and a different zero-cubic argument;
its result is neither imported nor contradicted here.

Next earn complementary-mode scale/domain control and actual normalized
overlaps before a quantitative low-energy or quantum-selection claim.
Continue the separate source/end/component chirality programme with its
own global hypotheses. Independent analytic scrutiny, SM breaking,
anomaly/end completion, scales, gravity and empirical predictions remain
mission obligations. The parent, geometry and g7 remain supplied inputs.
