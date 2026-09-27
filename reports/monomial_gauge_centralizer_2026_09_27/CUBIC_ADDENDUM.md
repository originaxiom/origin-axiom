# Post-result test: the actual massless cubic overlaps at t=1

2026-09-27, after receipt commit 9561bfd7. This is a separately sealed
design/proof/control, before its first execution. Original sources and
first outputs remain unchanged. No new shared bank or physical completion.

## Why this follows from the result, rather than another count scan

The exact first run found 16+16*+3 singlets in degree one at the enhanced
point. In particular n(ad U)=3, not an assumed single neutral mode. Test
the leading holomorphic interactions of these ACTUAL normalizable modes
before assigning them arbitrary GUT Yukawa couplings.

Proposed result, subject to the controls below: every direct classical
holomorphic cubic among these degree-one zero modes vanishes at t=1.
This is not a statement that gauge interactions vanish, that every mode
is an integrable modulus, that quantum effects vanish or that a gapped
finite-dimensional EFT exists. It is only the cubic overlap tensor of
the supplied local action, at the declared background and norm.

## 1. All three neutral profiles are symmetric endomorphisms

The finite real four-dimensional representation U preserves a positive
real Gram G. The involution tau(X)=G^-1 X^T G on End(U) is parallel,
orthogonal and commutes with the complete Laplacian. Its minus space is
so(U,G), identified by G with Lambda2(U); its plus trace-free space is
Sym0(U,G). Their direct sum is ad U. The scalar trace is a separate
trivial coefficient. The original exact calculation gave

    n(Lambda2 U)=0, n(1)=0, n(End U)=3.

The charged complete-domain theorem therefore forces EVERY harmonic
ad U one-form to lie pointwise in Sym0(U,G). This is stronger than
choosing three symmetric examples. The new producer constructs both
projectors on all sixteen matrix coordinates, restricts every actual
M6 generator to their images, and independently recomputes both interior
groups. In a local real orthonormal frame each matrix coefficient S_i
of each neutral one-form is symmetric, possibly complexified.

The symmetric coefficient splits under the finite group as U plus an
irreducible five. Verify this by the exact character

    char_5(g) = (char_U(g)^2+char_U(g^2))/2 - 1 - char_U(g).

Its character norm is one and it is orthogonal to 1 and U. The already
constructed parallel map H -> QHQ supplies the U summand. Thus one of
the neutral harmonic classes is in this U summand and the other two in
the five; these two are not two additional fermion generations. This
decomposition is only used as context, not as a replacement for the
direct symmetric/skew cohomology check.

## 2. The two spinor profiles share a real internal one-form

The U harmonic space has complex dimension one and is the complexification
of a real harmonic line, since the connection, metric and domain are real.
Choose a nonzero real U-valued harmonic one-form alpha. The actual dual U*
is identified by G, so its single harmonic profile is alpha^T G, up to
a nonzero constant. This is valid at this REAL UNITARY point, not at a
generic nonunitary t. In an orthonormal frame the internal components are
the same scalar one-forms alpha^a for the spinor and its conjugate.

All these harmonic one-forms decay rapidly on the finite-unitary cusp.
Indeed use the preceding proof's compact representative and reduced
zero-form Green operator: on the cusp the primitive is an L2 unitary
harmonic function, whose zero Fourier part is constant and whose other
parts are the decaying Bessel branches. Differentiation removes the
constant. This is the same full-series estimate already used for beta,
now on finite coefficient bundles. The modes are bounded and in Lp, so
their triple overlaps are absolutely integrable before evaluating them.

## 3. The actual cubic from the action

Expansion of the supplied nonabelian local action gives the invariant
holomorphic trilinear overlap proportional to

    integral_M <u wedge [v wedge w]>.

The overall trace/coupling convention cannot change whether it vanishes.
This follows directly from the covariant derivative in the fermionic
Yukawa term and the auxiliary curvature term, not by assuming a new
superpotential coefficient. Braun et al. equations 6.2--6.5 were personally
read for that action/overlap identification.[1] Their localized-Morse
instanton interpretation is NOT transferred to this unsourced finite
holonomy background. No instanton geometry is constructed here.

Gauge invariance in so(10) permits only singlet cubics and
singlet x 16 x 16* among the present degree-one representation slots.
Three spinors cannot have zero weight because three half-integer weights
have half-integer coordinate sums; two same-chirality spinors have no
opposite weights, whereas the two distinct spinor sets are contragredient.
No 10-valued degree-one mode exists at this point. The actual weight sets
are checked, not inferred merely from the names of representations.

For three singlet profiles the coefficient contraction is

    tr(S_i [T_j,R_k]) = 0:

the commutator of symmetric matrices is skew, and its trace pairing with
a symmetric matrix is zero. This holds pointwise for arbitrary members of
the full symmetric profile space, not just for the special tangent beta.

For a singlet, spinor and conjugate spinor, the SU4 coefficient contraction
is proportional to

    sum_ab S_ab wedge alpha^a wedge alpha^b = 0,

because S_ab=S_ba while the last two one-forms are antisymmetric in a,b.
The gauge factor is the invariant pairing of 16 and 16*. Its value is
irrelevant to the identically zero internal factor. These two identities
cover every allowed cubic, including all three independent singlets.

## 4. Controls and interpretation

Check the matrix identities symbolically with independent coordinates,
not by fitting a profile. Require nonzero controls if a skew neutral
matrix is substituted, and if the two internal spinor profiles are made
independent. This guards against an identically-zero implementation or
a false general prohibition of Yukawa interactions. The skew coefficient
has no harmonic one-form here; independence fails because n(U)=1.

The kinetic Gram on a linearly independent finite set of nonzero L2
modes is positive definite. Canonical normalization is an invertible
basis change and therefore leaves the zero cubic tensor zero. No
numerical norm is required to establish that statement. Gauge couplings,
D-terms, higher operators, interactions with nonzero-mode/continuum
states and quantum effects are not zeroed by this calculation. In
particular, zero cubic projection does NOT imply that the nonlinear
obstruction itself vanishes in every direction or that the full moduli
space is smooth. The known gapless sector prevents silently integrating
out all complementary states.

The addendum also locks the observed original outputs: all-t centralizer
dimensions and the 35-mode count. Those post-result locks are explicit
regression guards, not pre-discovery predictions or independent evidence.

[1] Braun et al., [Higgs Bundles for M-theory on G2-Manifolds](https://arxiv.org/html/1812.06072v2),
sections 6.1--6.2 read personally and sectionally. The universal action
terms are used; their singular-source or compact-G2 constructions are not
asserted to hold on this model. Analytic prerequisites retain authored,
not independent-specialist, evidence grade.
