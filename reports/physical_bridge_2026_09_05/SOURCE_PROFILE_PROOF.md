# R80 authored argument: which profiles can carry the source

Pre-execution, October2. Conditional extension of R41/R75/R77, not a
new universal stability theorem or a physical source derivation.

## SP1. The sign is a block norm, not the sign of a selected diagonal

At a point in an orthonormal frame adapted to S, put
Z=[[a,b],[c,d]], P=diag(Id_k,0), xi=nP-kId_n.
The trace of a commutator is zero. The upper diagonal block of
[Z,Zdag] is [a,adag]+bbdag-cdag c. Taking its trace gives

    tr(xi[Z,Zdag])=n(tr(bbdag)-tr(cdag c)).

This is an exact identity for unrestricted complex blocks. It survives
unitary transport of P AND Z. It does not require diagonalizing Z or
its current. If Z(S) is contained in S then c=0, so the projection is
nonnegative, strictly positive when b is nonzero. Positive source
coefficients cannot reverse this sign. Taking Zdag swaps the blocks;
it is an opposite SOURCE, not an automatic physical parity map.

## SP2. Combine the source's sign with the EXISTING bulk identity

Because the connection D preserves S, write its off-diagonal block as
eta in the adapted positive metric. R41's block calculation generalizes
directly to <Psi,d_A xi>=-n|eta|^2/2; diagonal blocks cancel.
For I=-2d_A^*Psi, integration on a truncated domain gives

    integral tr(xi I)=n integral|eta|^2
                       +2 integral_boundary tr(xi Psi(n_out)).

Reuse R41's cutoff argument: on a complete finite-volume boundaryless
base with finite ||Psi||_2, bounded xi and cutoffs |d chi_R|<=C/R,
the cutoff remainder tends to zero by Cauchy-Schwarz. Suppose source
cross-blocks are square-integrable (finite source kinetic norms suffice).
This avoids subtracting two infinite norm integrals. At zero TOTAL D
residual in R77's declared model,

    0 = integral |eta|^2
        +g2 sum_a kappa_a integral (|b_a|^2-|c_a|^2).

Thus nonsplit eta requires

    sum_a kappa_a integral(|c_a|^2-|b_a|^2)
          = integral|eta|^2/g2 > 0.

Strict positivity follows from nonsplitting: eta identically zero would
make the metric-orthogonal complement D-invariant. A split control has
eta=0. If every source preserves S, c_a=0, all remaining terms are
nonnegative, so the nonsplit background cannot be D-flat in this class.
This is a necessary balance, NOT sufficient full-matrix cancellation.

The statement is independent of any internal-profile differential law;
it applies to sources that happen to preserve S. It does not cover
arbitrary nonzero-D stationary points, indefinite kinetic terms, other
source representations, full E8 fields outside this End bundle, extra
end flux, singular/infinite-energy limits or a changed flat coefficient.
It does NOT assert R77's current inverse preserves S; indeed it must
have downward components whenever this balance is positive.

## SP3. The actual triplet's periphery controls parallel endomorphisms

R75 constructs W as an upper extension of its four-dimensional V by
the trivial line. Its longitude L_W=[[L_V,v],[0,1]], and its literal
word calculation gives characteristic polynomial
(z-q)^3(z-q^-3). This is independent of the order-two fibre character:
the boundary commutator has trivial scalar character. Therefore

    det(L_V-Id)=(q-1)^3(q^-3-1).

For g(q)=q^6-34q^3+1 its numerator is coprime to g, and q is nonzero.
Hence im(L_W-Id)=V for ANY extension column v, including the actual
nonzero cocycle. This is an image statement in a flat fibre, not a
claim that the orthogonal projector P is parallel under A or D.

A D-parallel endomorphism Z commutes with every holonomy, in particular
L_W. Commutation implies Z im(L_W-Id) is contained in that image.
It consequently preserves V; the conclusion is invariant under frame
changes and does not assume L_V is diagonalizable. SP2 excludes a
D-flat support for the nonsplit W by such sources alone under its full
energy/domain hypotheses. No new centralizer census is needed.

The q=1 case lacks this argument and is explicitly controlled. Braun's
localized chiral fields have constrained degree-one profiles, not an
asserted D-parallel End(W) zero-form law. Applying SP3 to them without
an exhibited dictionary would be another false kill. Parallel sources
in another coefficient, or nonparallel admitted modes, need new tests.

## SP4. Real boundary flux is a live escape

On a product of a flat unit-area two-torus with s in[-log2,log2], use
C=C_s ds with the real upper triangular matrix in the design.
It is flat because it has only one coordinate component. In unitary
frame convention the full real residual is

    I=partial_s(C+Cdag)+[C,Cdag],
    I11=2 h'+b^2, I12=b'-2hb, I22=-I11.

With t=exp(s), direct rational differentiation gives h'=-b^2/2 and
b'=2hb, so I=0. The nonzero extension block is eta=b. Its integral
is integral_(1/2)^2 b(t)^2 dt/t=6/5. For xi=diag(1,-1),
tr(xi Psi)=2h; outward flux is 2(h(2)-h(1/2))=-6/5.
Thus 2*(6/5)+2*(-6/5)=0. Dropping the boundary term falsely excludes
this smooth, positive-metric, finite-domain solution. The coefficient
on this local domain can split globally; the control tests the positive
extension term and boundary identity, not nonsplit global topology.
No physical end-domain selection, charge quantization or chirality follows.

## SP5. Relational fields export current; they do not erase its cost

For B:E_tail->E_head embedded as an off-block endomorphism of
E_tail plus E_head, [Z,Zdag]=diag(-Bdag B,BBdag). Both are parts of
the same moment map. For orthogonal P_t,P_h, the projector-weighted
trace sum is

    tr(P_h BBdag)-tr(P_t Bdag B)
      =|P_h B(1-P_t)|^2-|(1-P_h)B P_t|^2.

The both-selected and both-complement blocks cancel. A map preserving
the combined selected subspace has its second block zero and again
has the nonnegative sign. To compensate a positive bulk projection it
must send some selected state outside that subspace, or some other term
must change. This is why the registering relation cannot be silently
discarded in a coupled model, but it does not derive a physical observer.

The simplest lower source e_(4,0) cancels the synthetic rank-five
current diag(1,0,0,0,-1) exactly with g2*kappa=1. It transfers the
opposite current to the fifth component and violates the old four's
invariance. It is NOT parallel for C=e_(0,4) ds:
d_C Z=[e_(0,4),e_(4,0)] ds is nonzero despite constant coordinates.
So an algebraic match does not establish profile admission. R77's full
inverse remains a positive construction in its declared relaxed model;
neither this example nor SP2 supplies its finite physical replacement.

## Evidence and physical use boundary

Finite symbolic controls and independent rational entry computations
test these exact local identities. The cutoff/holonomy argument is
authored and awaits independent analytic review. The new gate serves
the SAME-theory source/profile duty: test the actual admitted fields'
downward projection, end flux and full matrix equations before counting
particles. No source count, coupling, action, observer, qualia, spectrum,
physical parity or gravity is selected by this proof. No original claim.
