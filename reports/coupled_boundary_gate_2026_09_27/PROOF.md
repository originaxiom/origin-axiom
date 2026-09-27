# Proof of the boundary screen (authored before execution)

## 1. Full identity, including invariant vectors

Let M be a compact connected oriented 3-manifold with nonempty torus
boundary T (a truncated cusp, not an analytic boundary condition). Let V be
a finite-dimensional complex local system, V* its linear dual, and write
a_i=dim H^i(M;V), t_i=dim H^i(T;V), r=rank[H^1(M;V)->H^1(T;V)].
Stars denote the dual coefficient system. Define n=a1-r and I=n-n*.

Restriction H0(M)->H0(T) is injective. H3(M;V)=0 and Euler characteristic
zero give a2=a1-a0. Poincare-Lefschetz duality gives
dim H1(M,T;V)=a2*=a1*-a0*. The start of the pair exact sequence therefore
gives a1*-a0*=(t0-a0)+(a1-r). Consequently

    a1-a1* = a0-a0* + r-t0.

The images of the two H1 restriction maps annihilate each other under
the perfect boundary pairing, so r+r*=t1. Boundary duality and its Euler
characteristic give t1=t0+t0*. Substitution yields

    I = (a0-a0*) + t0* - r.                         (1)

Thus, with delta=a0-a0*, and 0<=r<=t0+t0*,

    delta-t0 <= I <= delta+t0*.                    (2)

If delta=0, -t0<=I<=t0*. Reductivity is sufficient for delta=0, but is not
necessary: it is the equality, not a label "reductive", that is used here.
For arbitrary V, injectivity of H0 gives 0<=a0<=t0 and 0<=a0*<=t0*.
Hence the weaker but universal estimate

    |I| <= t0+t0*.                                 (3)

These are upper bounds, not realization theorems. A multi-torus boundary
uses sums of dimensions; a one-cusp bound cannot be used unchanged when
additional cusps exist. Neither I nor n is identified here with a physical
fermion index or ordinary L2 cohomology.

## 2. Meridian bounds do not require knowing the longitude

For a torus with commuting holonomies U,W,
t0=dim(ker(U-1) intersection ker(W-1)) <= dim ker(U-1).
The meridian bound for the dual has the same dimension, since
rank(U^{-T}-1)=rank(U-1). Common fixed spaces of U,W and of their duals
need NOT have equal dimension. Example on C3: U=1+E12, W=1+E13 commute;
their common fixed spaces have dimensions one and two, respectively.

If d=dim ker(U-1), (2) gives |I|<=d with balanced global H0, and (3)
gives |I|<=2d unconditionally, regardless of the longitude. A principal
unipotent 5x5 U has d=1, so target |I(E)|=3 is impossible in this class,
even for nonsplit E. Multiplying U by a scalar other than one gives no
fixed vector, and forces t0=t0*=a0=a0*=I=0. The principal class remains
excluded under arbitrary scalar meridian twists. No assertion about all
SL5 boundary classes, new source domains, or physical indices follows.

## 3. The desired 2+3 meridian is different

Let P be a cyclic permutation on three coordinates and set

    U2=diag(J2(1/3),P),  J2(s)=1+s E12;
    U6=U2^3=diag(J2(1),1_3).

Both have determinant one. For a compatible boundary-only example choose
W=diag(J2(2),1_3), commuting with both. It is NOT a derived longitude.
For E=A2+B3 the functor decomposition is

    wedge^2 E = wedge^2 A + (A tensor B) + wedge^2 B.

For U2, A has one eigenvalue-one Jordan block, B has three simple cubic
eigenvalues. Thus E has two fixed vectors. Wedge^2 A contributes one,
A tensor B contributes one, wedge^2 B contributes one: wedge^2 E has three.
For U6, E has four, wedge^2 A one, A tensor B three, wedge^2 B three:
wedge^2 E has seven. Hom(B,A) instead has dimensions one and three.
Our W preserves all these meridian-fixed vectors, attaining these bounds
in the boundary example; a different commuting W need not do so.

Consequences for the algebraic target in E: downstairs, balanced global H0
implies |I|<=2, while without balance the screen allows up to four. Upstairs
the balanced bound is four, so this screen does not exclude three. In the
downstairs class, I>=3 requires delta>=1; I<=-3 requires delta<=-1.
This is a necessary condition on global invariant vectors, NOT existence.
The mixed six-dimensional coefficient cannot substitute for E or wedge^2 E.

## 4. Independent Jordan and twist checks

For a unipotent Jordan partition p=(p_i), E has k fixed vectors (one per
block), while wedge^2 E has

    sum_i floor(p_i/2) + sum_{i<j} min(p_i,p_j).

One proof realizes each block as an irreducible sl2 module of dimension
p_i. Its exterior square contains floor(p_i/2) irreducible summands and
the tensor product of two blocks contains min(p_i,p_j) summands; each has
one highest-weight vector. Computing minors of exp(N) is a separate
matrix check. Kernel dimensions are bounds on I, never values of I.

For cubic twists use the rational matrix R=[[0,-1],[1,-1]], multiplication
by omega on Q(omega) in the basis (1,omega). Q(omega)-nullity of
omega^k A-1 is half the Q-nullity of (A tensor R^k)-1. This verifies exact
phases without floating approximations. For U2 the E bounds are two at
phase one and one at either other cubic phase; wedge^2 E bounds are three,
two and two. For U6 every nontrivial scalar phase removes all meridian
invariants. Thus a common hypercharge line L must have L(mu_up)=1 to
support target three in E tensor L (the Q sector). If its longitude is
also unipotent before twisting, L(lambda_up)=1 is necessary as well.
No claim about a non-unipotent longitude is made.

The common exponents are 1,-4,6 for the three E sectors, and 2,-3 for the
wedge-square sectors, in the established 6Y convention. This convention
is not a derivation of physical hypercharge normalization. A downstairs
L(mu_down)=omega obeys L(mu_up)=omega^3=1; do not falsely exclude it.

## Review status

These elementary topology and representation arguments are authored here,
not independently referee-certified. Exact matrix tests audit their finite
comparators, not the general topological theorem or physical interpretation.
