# Coupling transport and the missing joining law

October 18, 2026. Analytical successor to
[the shared matter and boundary action](MATTER_AND_BOUNDARY_COMMON_REGISTER.md).
[Independent analytical review](MATTER_COUPLING_REVIEW_INTAKE.md) is
recorded separately, with no new scientific execution or admission.

The paper's existing bilinear coupling admits an exact simultaneous
transport of its Higgs and matter matrices. The transport preserves
its determinant factors and, for the unitary registered operations,
its singular values. This derives a consistency law for the supplied
coupling tensor, not the physical interaction between different states.
An explicit example shows how averaging frame-transformed copies can
manufacture full rank even though transporting them to one frame
retains their original null space.

## The actual supplied coupling tensor

Use the tensor in main B1659 and the paper's Theorem T7. With

    epsilon=[[0,1],[-1,0]],
    (C1,C2,C3)=(j,i,k),
    Y(S,M)_ab=sum_mn (C_a^T epsilon S C_b)_mn M_mn,    (1)

S and M are arbitrary complex 2-by-2 matrices. The transpose and
entrywise contraction are bilinear, not Hermitian. This is exactly the
twisted-frame tensor in the source, not a choice of an arbitrary matrix
with a desired spectrum.

B1659 supplies the polynomial identity

    det Y=4 det S det M tr(epsilon S M^T).             (2)

The source's proof and verification code were read, not rerun. The
transport calculation below is independent of the source's floating
outputs and does not assert a new certificate for all its other claims.
The choice of this tensor, the meaning of S and M, and its physical
identification remain the paper's scoped inputs.

## Simultaneous transport derived from the contraction

For g in SL(2,C) define O_g by g C_b g^-1=sum_a C_a (O_g)_ab.
Conjugation preserves the trace form, so O_g^T O_g=I. It has
determinant one: it preserves the bracket and the associated oriented
volume form on the three-dimensional traceless matrices.
Transport the two inputs by

    S'=g S g^-1,     M'=g M g^T.                     (3)

The second law is congruence, not conjugation. It is the one obtained
when M=p q^T is assembled from two doublets transported by g, and it
extends linearly to every M. Write B_ab=C_a^T epsilon S C_b. The
identity g^T epsilon g=epsilon gives

    Y(S',M')_ab
      =tr[g^T C_a^T epsilon g S g^-1 C_b g M^T]
      =tr[(g^-1 C_a g)^T epsilon S (g^-1 C_b g) M^T].

Expanding in C_a proves

    Y(S',M')=O_g Y(S,M) O_g^T.                      (4)

This is exact for all S,M,g of the stated types and composes because
both transformations in (3) compose. It provides a simultaneous
coefficient-level transport on the previously constructed E through
its g component. It does not yet provide a geometric transport of the
actual theta residues, cutoff, Wilson lines, or their automorphy weights.
It is a compatible transport, not a classification proving that no
other transport can preserve the supplied tensor.

Every factor of (2) is preserved by (3): det S and det M separately,
and

    tr(epsilon S' (M')^T)
      =tr(g^T epsilon g S M^T)
      =tr(epsilon S M^T).

For g in SU(2), O_g is real orthogonal, so (4) also preserves all
singular values and their multiplicities. This last statement does not
extend to arbitrary SL(2,C) changes with a fixed Hermitian metric.
Such changes require transporting the kinetic metric as well before
interpreting singular values as masses.

## The matter phase is a separate compatibility condition

The registered triplet from the companion proof is U_e=z_e O_g,
where z=mu_+ or mu_- is a character, not merely O_g. To illustrate
the resulting duty, suppose two column fields both transform by U_e
and a bilinear scalar is written psi_L^T Y psi_R. Its covariance
requires

    Y(e x)=U_e^-T Y(x) U_e^-1
          =z_e^-2 O_g Y(x) O_g^T.                  (5)

Using (3) without its missing scalar would only satisfy this law when
z_e^2=1 or the fields/line factors supplied the compensating phase.
For the general scalar-character transports

    S'=alpha(e) g S g^-1,
    M'=beta(e) g M g^T,

bilinearity of the actual tensor forces the product condition

    alpha beta=z^-2.                               (6)

It does not determine alpha and beta separately. The choices
(alpha,beta)=(z^-2,1) and (1,z^-2) both satisfy composition and (5),
but assign the phase to different named inputs. These are conditional
kinematic assignments, not two derived physical theories. Existing
geometric weights or a derived field identification could constrain
them further; none is removed by (6).

For an explicit check, e=Delta^2 J_c^-1 has g=1 and z=-i on T_+.
The unscaled transport (3) is the identity, but (5) requires Y->-Y.
Thus the phase compensation is a genuine part of this contraction's
compatibility, not a notation change in the quaternion action.

For a Hermitian contraction with a conjugated left field, the analogous
phase condition is different. So is the condition if the two matter
fields carry opposite hands. Equation (6) is not a universal Yukawa
law; it makes explicit which supplied field and contraction assumptions
are required to claim that all parts transform together.

## Transport is not an interaction between different states

Suppose different labels e name copies of one state transported by
(3). Their coupling matrices are Y_e=O_g Y_0 O_g^T. If those copies
are compared at a common reference frame, their matrices are

    Y_e at the reference frame = O_g^T Y_e O_g=Y_0.

Therefore any weighted sum made after this specified transport is
(sum_e w_e)Y_0. It cannot increase rank by including more word labels;
normalized weights preserve it, and a zero total weight cancels it.
With the character factors in (5), the return transport
must undo those factors too. This statement concerns copies in one
transport orbit, not arbitrary interacting configurations.

The difference is visible inside the paper's own tensor. Take

    S0=[[1,0],[0,0]],
    M0=S0 epsilon^-1=[[0,-1],[0,0]].

Only M_01=-1 contributes to (1), giving

    Y0_ab=(C_a)_10 (C_b)_01,
    Y0=[[-1,0,-i],[0,0,0],[i,0,-1]].                (7)

It is the outer product (-1,0,i)^T (1,0,i), has rank one and
trace -2. Now average O Y0 O^T over all 24 octahedral rotations
in the fixed coordinate array. Averaging first over diagonal sign
rotations kills off-diagonal entries, and then over axis permutations
equalizes the three diagonal entries. Thus

    (1/24) sum_O O Y0 O^T = (tr Y0/3) I = -2 I/3.  (8)

The untransported average has rank three. Yet every term in it has
rank one, and returning each term to the reference frame before
averaging gives precisely Y0, of rank one.

Equation (8) deliberately averages the unphased rotation action (3),
not the character-compensated action (5) over the full common group K.
The latter average is zero: the element (g,z)=(1,-i) lies in K and
acts on Y by -1, pairing cancelling terms in the group sum. Thus the
rotation-only average, the full compensated group average and the
common-frame average are three different operations with different
answers; none is selected as a physical join by mere admissibility.

Equation (8) is a valid Reynolds average, not an arithmetic error.
The unsupported step would be to identify it with a physically joined
mass matrix solely because every rotated word state is admitted. That
identification selects the relative frames, weights, and meaning of
the sum. If the copies represent genuinely distinct physical sectors,
such data may be part of a real interaction law, but that law must be
derived or declared. Conversely, this example does not establish that
all different word histories are just redescription; the faithful
register retains distinctions beyond the finite action used here.

## What is and is not fixed

The supplied contraction determines compatible transport laws (3)-(4).
The supplied matter representation plus a specified scalar bilinear
determines the product condition (6). Neither fixes S or M at a
particular point of their allowed spaces. Even with this same tensor
and group action, (7) is a rank-one input pair, while S=I and
M=epsilon^-1 give Y=-2I of full rank directly from (1). These are
values of one kinematic law, not stationary backgrounds selected by
that law. The two determinant invariants distinguish their orbits;
no number of unitary frame changes connects them.

Thus the remaining joining question is more precise than whether all
words are counted: which retained relative data couple distinct
configurations, by what equation, and with which operator and boundary
domain? Equivariance restricts an answer but is not itself the dynamics
that chooses the defects or their pairing. Imposing an arbitrary
potential to select them would add the very input this goal asks to
derive.

The next source-complete specification should distinguish:

1. Change of register or frame, with all fields and kinetic metrics
   transported together and the old spectra recovered.
2. A family of physical states over a varying modulus, including its
   actual automorphy line, puncture and end data.
3. A coupling between different states or carriers, with a derived or
   explicitly priced relative identification, composition and domain.

The same distinction applies to boundary conditions. A covariant family
Lambda(e x)=A_e Lambda(x) is not a single domain invariant under every
operation. A fixed domain only has to respect the stabilizer of the
full state when that is the symmetry being imposed. Enlarging a group
while silently freezing part of that state can produce a spurious
exclusion; discarding a genuine stabilizer condition is equally invalid.

## Evidence and verification scope

Source pin main 2e5716bd9bea013d69f3cd733f083b61a6f59dbd:
the complete paper section s05_couplings.tex and B1659's complete
verification/the_joint_law.py were read directly. The producer's
Ysym uses the same ordered basis, epsilon and entrywise contraction as
(1). B1659's stated frozen-frame scope is preserved. The earlier
joining analysis already separates relative placement from existence
of joins; (7)-(8) is a concrete control in this actual coupling tensor,
not a claim that this general distinction is new.

The derivations have received separate non-authoring analytical review.
The unrun v3 scientific controls remain unchanged. Any executable
successor must seal this exact tensor, the conjugation/congruence and
inverse-action conventions, the phase compensation, both examples,
and the correct and deliberately untransported aggregation controls.
Main acceptance and prospective admission remain required. No boundary
selection, physical spectrum, full interacting weave, or input payment
is claimed.
