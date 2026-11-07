# What composition earns for a registering response

2026-11-08. Author hand proofs and personally read sources.
**UNREVIEWED; no scientific import, collection or execution.**
Successor to the carrier audit at `e5a45fcfe`; no frozen record is edited.

## Outcome and actual reduction

An affine registering action determines both a linear coefficient action
and its cocycle law. They need not be independent postulates once that
action is given. This is an exact consistency derivation, not a derivation
of affine responses, complex amplitudes or matter from non-cancellation.

A second response is forced by differentiating a supplied matrix
representation: it takes values in the **adjoint**, not the fundamental
doublet. At the quaternion point its three nontrivial parity lines are
already in the record (B1614). A matter-doublet response requires another
kind of registering structure. The central action gives an exact test
for that missing structure, instead of selecting it by its desired count.

## 1. Seen first and sources personally checked

- Main `217e37c4f`, `frontier/B1614_the_observer_layer_on_the_weave/FINDINGS.md`:
  already distinguishes adjoint deformations, the three parity lines,
  doublet/matter coefficients and their different puncture restrictions.
  The entire findings text was read. Its execution is not rerun here.
- Fork `0c6570bab`, `reports/genesis_root_review_2026_10_11/cohomology_carrier/PROOF.md`:
  already proves the affine cocycle factorization and the different
  carrier depths needed by parity lines and quaternion doublets. The
  preceding carrier report rechecks its whole proof; those results are
  reused, not rediscovered.
- The positive-carrier proof and source-scope note at that fork already
  own the Magnus-style path register and state the universal-completion
  premise. Repo source searches found extensive Fox-derivative usage;
  no novelty or global absence claim follows from a terminology search.
- Ralph H. Fox, *Free Differential Calculus. I* (1953), pp. 548--551:
  personally inspected the rendered original pages, including the group-
  ring derivation law and the free partial derivatives through (2.3).
  https://webhomes.maths.ed.ac.uk/~v1ranick/papers/fox1.pdf
- Andre Weil, *Remarks on the cohomology of groups* (1964), sections 2--3,
  pp. 150--152: personally read the original text and rendered pages
  defining affine cocycles and the adjoint deformation construction.
  https://people.brandeis.edu/~ruberman/math221bs16/weil_Remarks%20on%20the%20cohomology%20of%20groups.pdf

These are classical constructions. The contribution here is their explicit
input accounting and the resulting OA earning duty, not a new theorem
about group cohomology or a claim to have read both complete papers.

## 2. An affine response earns its own cocycle law

Let H be a supplied history group. Let A be a supplied affine space for
a vector space V, and let each history act by an invertible affine map
T_h, with T_(hk)=T_h T_k. Choose an origin to write

    T_h(x) = rho(h) x + z(h).

Comparing the linear and constant parts of the composition gives

    rho(hk) = rho(h)rho(k),
    z(hk) = z(h) + rho(h)z(k).

Conversely these identities construct such an affine action. The identity
and inverse equations follow as well: rho(1)=I, z(1)=0 and
z(h^-1)=-rho(h)^-1 z(h). Changing the origin by v changes z to
z+(rho-I)v. Thus cocycles modulo change of origin give H1(H,V_rho).
This equivalence is already explicit in Weil section 2 and the fork.

**What was earned:** a separate composition/cocycle law and coefficient
homomorphism are redundant *after* the affine-action premise.
**What was not earned:** the affine space, its scalar field and dimension,
why the response is affine, which action is realized, its state, norm or
physical role. Merely replacing two formulas by the name 'affine action'
does not reduce the genuinely independent foundational choices.

This conditional law concerns an accumulated response at fixed rho. It
must not be conflated with varying rho itself.

## 3. There is a universal additive response, at every carrier

For any supplied group H, let Z[H] be its integral group ring and I_H the
augmentation ideal: finite sums sum n_h h with sum n_h=0. Use its left
H-action and define

    d_H(h)=h-1.

Then d_H(hk)=d_H(h)+h d_H(k). For every left H-module V and cocycle z,
there is a unique H-linear map Phi:I_H->V with Phi(d_H(h))=z(h).
Indeed define Phi(sum n_h h)=sum n_h z(h). It is well-defined because
group elements are a basis and the coefficient sum is zero. For g in H,

    sum n_h z(gh) = sum n_h (z(g)+g z(h)) = g sum n_h z(h),

proving H-linearity. The elements h-1 generate I_H additively, proving
uniqueness. Conversely applying any H-linear Phi to d_H gives a cocycle.
This is the universal module statement underlying the Fox calculus.

The map h->h-1 separates every pair of elements of **H**, because they
are distinct group-ring basis elements. It exists for free, metabelian,
finite and abelian H alike. A group homomorphism q:H->K induces a module
map sending d_H(h) to d_K(q(h)); this can erase information when q has
a kernel. Functoriality does not mean that every map preserves all tests.

Thus this constructor introduces no preferred finite coefficient module,
rank, prime or metric. It is a useful complete algebraic response family
once the group and additive-module category are given. Declaring that
all of it is physically retained is an extra requirement, not a proof
selecting H or a physical infinite-dimensional register.

For a free group F_n its Cayley tree gives a direct description. Finite
oriented edge chains form Z[F_n]^n. The boundary map sends its i-th edge
at g to g(x_i-1). Its image is I_(F_n), since the tree is connected;
its kernel is zero, since a finite tree has no nonzero finite 1-cycle.
Hence I_(F_n) is free on the x_i-1. Coefficients of h-1 in this basis
are exactly the left Fox derivatives. Evaluating those coefficients in
a smaller action recovers specialized registers such as the fork's
commutative Laurent-path construction; it can lose signed information.

## 4. Varying matrices forces a different coefficient module

Let rho:H->GL(V) be given. A first-order deformation over dual numbers
(epsilon^2=0) has a unique form

    rho_epsilon(h) = (I+epsilon X(h)) rho(h).

Expanding the homomorphism equation, without an added cocycle postulate,
gives

    X(hk) = X(h) + rho(h) X(k) rho(h)^-1.

Thus X is an **Ad rho** cocycle in End(V). Infinitesimal conjugation
by I+epsilon T changes X by T-Ad(rho)T, a coboundary. Requiring rho_epsilon
to remain in SL(V) gives tr X=0; for unitary deformations the Lie algebra
is real u(V), or su(V) with fixed determinant. Differentiability and the
matrix representation category are premises here, not consequences of
the history group's composition alone. This is Weil section 3.

For an actual smooth one-parameter family, the same result follows from
X(h)=(partial_epsilon rho_epsilon(h))rho(h)^-1. An arbitrary cocycle need
not integrate on a group with relators. On a free group, arbitrary small
deformations of its generator matrices do define a representation.

If variations must also preserve a common Nielsen-fixed SL2 character,
they obey more equations. In trace coordinates (x,y,z), the two moves
act by (x,z,xz-y) and (z,y,yz-x). Differentiating their fixed-point
equations at (0,0,0) forces dx=dy=dz=0. Therefore the ambient deformation
space must not be silently substituted for deformations remaining in
that fixed-character locus. Allowing symmetry-breaking or covariantly
transported states is a separate, explicit specification.

## 5. The quaternion point gives an exact central-action discriminator

Use the record's A=rho(a), B=rho(b) with A^2=B^2=-I and AB=-BA;
put C=AB. In the traceless adjoint basis A,B,C, conjugation gives

| Line | a | b |
|---|---|---|
| span(A) | +1 | -1 |
| span(B) | -1 | +1 |
| span(C) | -1 | -1 |

Thus Ad rho is the sum of the three nontrivial parity characters. This
is already the coefficient distinction in B1614. For each nontrivial
sign character on F2, Z1 has two scalar generator values and B1 has
dimension one, so H1 has dimension one. The adjoint H1 has dimension
three. The fundamental doublet instead has Z1 dimension four and B1
dimension two (A-I invertible), so its H1 has dimension two; the three
labelled supplied parity-doublet blocks give the old algebraic six.
These are different constructions, not conflicting generation counts.

The commutator c=[a,b] acts by rho(c)=-I on every parity-doublet block
but by +I on End(V), the adjoint and all tensor constructions generated
by that adjoint with trivial coefficients. Consequently every H-equivariant
linear map from any such central-even construction to a doublet is zero:

    f(x)=f(c x)=c f(x)=-f(x).

This is a precise scoped obstruction to obtaining a doublet by merely
relabeling matrix deformations or tensoring adjoint-only responses. It
does not obstruct tensoring an already supplied central-odd state or
adding an independently justified spinor/bundle module. Nor does it
prove that a central sign is directly observable: a physical phase test
needs its reference sector, state and interaction map.

**Positive:** the adjoint response and its parity decomposition follow
from the existing rho and first-order matrix variation, without choosing
another coefficient representation. This is an already-known conditional
structure placed at its correct logical level. A fundamental response
requires explaining where central-odd registering data first enter.

The defining doublet V is already present in the supplied rho:H->GL(V).
Its availability is therefore **not another missing representation** once
rho is given. The unearned step is why V must carry a nontrivial affine
registering response and why its cohomology becomes physical matter.
The adjoint comparison must not be used to declare that the programme
has no doublet or needs to supply a second copy just to define it.

## 6. The doublet response is an extension, not a variation in disguise

A rho-valued affine cocycle z can equivalently be written as

    rho_tilde(h) = [[rho(h), z(h)], [0, 1]] on E=V direct_sum C.

This gives an exact sequence of H-modules

    0 -> V_rho -> E -> C_trivial -> 0.

An origin/section change gives the same coboundary relation as above;
the extension splits precisely when [z]=0. Therefore a nontrivial
doublet response has a concrete additional structural meaning. It does
not follow from calling Ad rho a doublet, and the existence of such
extensions does not select an extension class or physical source.

If z factors through the finite group Q8 itself, it is a coboundary.
Let S=sum_(q in Q8) z(q). Permuting the sum by left multiplication gives

    S = 8 z(g) + rho(g) S,
    z(g) = (I-rho(g)) S/8.

Thus nonzero H1(F2,V_rho) detects histories invisible to the bare Q8
image; it is not a nontrivial H1 of that finite image. The fork's witness
z([[a,b],a[a,b]a^-1])=4v measures this distinction explicitly. Its result
that F2/F2''' suffices preserves the extension response, not merely rho.

A further metric duty is immediate. If rho_tilde preserved a constant
positive-definite Hermitian form, the invariant V would have an invariant
orthogonal complement. That complement supplies a splitting, so [z]=0.
A nonsplit finite-dimensional extension is therefore not unitarizable
with one constant positive Hermitian form. This is not a no-go for an
affine isometric action with unitary linear part, a varying bundle metric,
an infinite-dimensional realization, or the programme's nonflat fields.
Each is a different specification with its actual metric and domain.

## 7. Narrowing my own finite-context audit

The prior report's F6 should be read as a diagnostic-coverage suggestion,
not an additional mathematical exclusion. If an exact coefficient image
is already known to have order N, and a signature test obtains N distinct
signatures from sampled images, then

    number of signatures <= number of sampled images <= N

forces full image coverage. This also makes every inverse image available
as a left distinguishing context. Therefore an independently justified
image-order bound plus that passing signature count already supplies an
indirect coverage certificate. A separate coverage assertion improves
diagnosis but is not logically necessary under those hypotheses.

For AGY's floating matrix implementation, exact group membership/order
and numerical separation still specify the test's interpretation. No
failure of its sample is asserted. The general all-context identity-
register theorem remains valid. The source-description mismatch remains:
S3 is in the group-table test, not the matrix free-word dictionary. The
type/quantifier findings F1--F5 are unaffected. The earlier record remains
preserved at `e5a45fcfe`, with this qualification visible rather than a
retrospective rewrite.

## 8. The next derivation question, with prices visible

The question is no longer 'can a cocycle be imposed?' Its composition is
automatic for an affine action, and all such responses have a universal
algebraic home. The unresolved duty is **which kind of registering act
the foundational principle requires**: a deformation of the operator,
an affine state/extension response, a spin-lifted state, or another
specified structure. These alternatives retain different information.

The targeted next card should start with the already available defining
doublet and complete lifted architecture. Earn why a nontrivial response
on it is obligatory, exhibit its actual composition/transport, and connect
that same response to the existing physical field/action/domain dictionary.
Do not repeatedly derive the availability of a module already in rho.
If no obligation is derived, preserve the structure as a conditional
candidate with that input open.

Faithful registration alone does not force a chosen nonzero affine state:
left translation on the already-described regular representation is
faithful and compositional with z=0. This does not deny that other cocycles
may be available. It separates existence of a response from compulsory
realization of one, just as the earlier audit separated existence of a
fixed sector from the properties of one displayed module.

No physical input, SM parameter, generation count, measurement postulate,
qualia claim or gravitational dynamics is marked earned by this note.
No code or frozen verification design is altered. The long-term mission
remains physically consistent SM3 plus gravity through verified reductions.
