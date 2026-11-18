# Native signed action: what the moves already fix

2026-11-18. Author hand derivation under scope `fe35fea58`.
**Not independently checked.** No scientific execution, physical input
reduction, canonical edit or claim of a physical state space.

## 1. Source cut and the precise carrier

Read at main `da6f87f5d68d228a121ee8fcd5f5bf517460a315`:

- B1601 `FINDINGS.md`, section 2, and the definitions of `Lm`, `Rm`
  in `verification/meets.py`;
- B1600 `verification/weave_verify.py`, the common-point maps, explicit
  quaternion matrices, and the stated W4 representation;
- `docs/THE_WEAVE.md`, W1-W4 and WM1-WM2.

These already supply the quaternion point and the signed three-axis
action. Neither that action nor its order is a discovery here. The
purpose is to ask what law it fixes, after making its use explicit.

The trace maps on the ambient character coordinates are

    L(x,y,z) = (x,z,xz-y),   R(x,y,z) = (z,y,yz-x).

Their derivatives at zero, acting on column vectors, are

           [1  0  0]              [ 0  0  1]
    ell = [0  0  1],      r =    [ 0  1  0].                 (1)
           [0 -1  0]              [-1  0  0]

Consequently ell fixes e1, sends e2 to -e3 and e3 to e2; r fixes
e2, sends e1 to -e3 and e3 to e1. These signs follow directly from
the displayed maps; they are not inferred from an unsigned permutation.

Use the auxiliary signed register

    X6 = {+e1,-e1,+e2,-e2,+e3,-e3}.                           (2)

There is also a direct quaternion reading of this set: the six
noncentral elements {+i,-i,+j,-j,+k,-k} of Q8. At the quaternion point,
the forward substitutions a -> a, b -> ab and a -> ab, b -> b induce

    alpha_L: i -> i, j -> k, k -> -j,
    alpha_R: i -> k, j -> j, k -> -i.                          (3)

The matrices in (1) are the inverses of these signed actions in the
ordered basis (i,j,k). The generated group and its pair orbits are
therefore the same. This keeps forward substitutions distinct from
the dual convention in (1).

This is one closed orbit of the move action. It is not all of Q8:
the omitted central elements +1 and -1 are individually fixed by every
automorphism. Multiplication of two members of X6 can return a central
element. Nothing here earns their omission from a physical composition
law, or selects this orbit over other generated carriers.

Nor are the six vectors in (2) six geometric representations on the
parabolic Markov surface. Its equation is x^2+y^2+z^2=xyz; a nonzero
coordinate-axis vector does not satisfy it. The quadratic tangent cone
at zero is x^2+y^2+z^2=0, which does not contain these real vectors
either. The use of (2) is as a signed register carrying the existing
linear representation, not as a list of allowed geometric deformations.

## 2. Recover the group without a census

Let G=<ell,r>. Every generator is a signed permutation matrix of
determinant +1. The group of all such matrices has order

    3! * 2^2 = 24.                                          (4)

Forgetting signs maps G onto S3: ell exchanges axes 2 and 3, and r
exchanges axes 1 and 3. The kernel contains

    ell^2 = diag(1,-1,-1),
    r^2   = diag(-1,1,-1),
    ell^2 r^2 = diag(-1,-1,1),   and I.                       (5)

There are only four determinant-one diagonal sign matrices. Thus the
kernel has exactly four elements and the image has six. G is the full
24-element group of proper signed permutations, the cube's rotations.
Its order 24 does not identify it with the binary tetrahedral group 2T.
The quaternion group Q8 is another different group in these statements.

G is transitive on X6. The stabilizer of e1 contains the four powers
of ell and has size 24/6=4, so it is exactly that subgroup. Its orbits
on X6 are

    {e1},  {-e1},  {+e2,-e2,+e3,-e3}.                        (6)

Equivalently, G has three orbits on ordered pairs of signed states:
equal, antipodal, and on different axes. The last relation is called
perpendicular below using the invariant metric derived next.

## 3. The invariant quadratic metric is fixed up to scale

Supply the requirement that a real symmetric quadratic form B be
invariant under the move action: ell^T B ell = r^T B r = B.
This is a fixed-form symmetry hypothesis, not a consequence of merely
transporting B under a change of coordinates.

Invariance under (5) kills every off-diagonal entry: for each distinct
pair of coordinates one of those diagonal matrices reverses exactly
one member of the pair. For the remaining diagonal matrix, ell forces
B22=B33 and r forces B11=B33. Hence

    B = lambda I;    B positive definite iff lambda > 0.     (7)

Conversely every such form is invariant. Thus an invariant positive
quadratic metric has no relative axis scale or angle left to choose.
The overall scale and the requirement of an invariant positive
quadratic metric remain inputs. No positive physical kinetic term is
derived by this calculation, and an independent foundational input is
not counted removed.

The same argument without transposes shows that any linear endomorphism
commuting with G is scalar: (5) makes it diagonal and the unsigned
permutations make all diagonal entries equal. In particular the signed
three-dimensional module is irreducible over R and C. For the complex
claim, an invariant subspace has a commuting orthogonal projector
after averaging a positive Hermitian form over the finite group; the
scalar commutant permits no nontrivial projector.

## 4. The unsigned quotient changes the representation

The map q(sign*ei)=i forgets the sign and yields X3={1,2,3} with
the full S3 permutation action. It recovers the three nonzero parity
labels after the identification

    axis 1 <-> (1,0), axis 2 <-> (0,1), axis 3 <-> (1,1).

The three-dimensional permutation module on X3 contains the constant
line and its two-dimensional sum-zero complement. It is not the
signed irreducible triplet of section 3. Three state labels, an
irreducible triplet of observables, and three physical generations are
different mathematical assertions.

The next file classifies invariant rate laws on X6 and tests exactly
which of their predictions descend through q. It does not infer a
physical law from the existence of this representation.

## 5. Review duties and limits

The requested non-authoring check must verify the derivative convention,
the inverse relation in (3), the kernel/image argument, the stabilizer
orbits, metric uniqueness, and the distinction between the signed
module and the unsigned permutation module. It must retain both
carrier warnings in section 1. A review of a finite numerical example
alone would not check the general arguments.

The move action is reused. Selecting X6 as a complete state space,
interpreting move symmetries as symmetries of one fixed law, introducing
classical probabilities or a physical clock, and identifying these
records with fields all remain separate hypotheses. No conclusion
about SM3, gravity, physical chirality, qualia or absolute nothingness
follows from (7).
