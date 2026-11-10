# Exact hand counterchecks of the P-753 triplet and its proposed field join

2026-11-10. Author derivations by the physical reviewer against AGY
`da5c71251194ad9866264338d4bd1f99f082ba4c`. Source reading and hand
algebra. These calculations ran no scientific producer, CAS or tests.
The new repair arguments need their own nonauthoring review for adoption.

## 1. Recover the weave triplet directly from cocycles

Write I=diag(i,-i), J=[[0,1],[-1,0]], K=IJ, and
gL=(1+I)/sqrt2, gR=(1-J)/sqrt2. For parity p=(pa,pb), put
A=(-1)^pa I and B=(-1)^pb J. Both A-1 and AB-1 are invertible.
Every class in H1(F2,chi_p tensor rhoQ) has a unique representative
z(a)=0, z(b)=t. Explicitly its coordinate is

    t = z(b)-(B-1)(A-1)^(-1)z(a).

For the moves and coefficient lifts used by W10 and this packet,
the parity and t transformations are

    L  p -> (pa,pa+pb),   t -> (-1)^pa gL t,
    R  p -> (pa+pb,pb),   t -> gR^(-1)(1-A-B-AB)t/2.

These follow from the cocycle identity and removal of the resulting
coboundary. In particular (AB-1)^(-1)=-(AB+1)/2 and ABA=B.
No quotient projector or floating-point eigenspace is needed.

Let e0,e1 be the I eigenvectors with eigenvalues i,-i, and set
w=exp(i*pi/4). On the three nonzero parities the R blocks are

| Input parity | Output parity | R block |
| --- | --- | --- |
| (1,0) | (1,0) | gL |
| (0,1) | (1,1) | (J+K)/sqrt2 |
| (1,1) | (0,1) | (J-K)/sqrt2 |

Choose the three cocycle classes

    v0 = -i e1 in parity(0,1),
    v1 =    e0 in parity(1,1),
    v2 =   -e0 in parity(1,0).

Their span is invariant. Direct substitution gives

    TL = [[w^-1,0,0], [0,0,w], [0,w,0]],
    TR = [[0,w^-1,0], [w^-1,0,0], [0,0,w]].

The quaternionic anti-linear map on the coefficient module commutes
with its SU2 operators and yields the conjugate complementary triplet.
Thus V has the exact T plus conjugate-T decomposition, with the
T-label convention characterized here by trace(TL)=w^-1.
Identification with a particular Hodge-sign label also carries the
orientation convention used in B1610. The module pair is independent
of that naming convention.

The monomial matrices generate order96 exactly. Their squared diagonal
operators and their conjugates generate

    D = {diag(i^a,i^b,i^c) | a=b=c mod2},  |D|=16.

All three permutations of i*diag(-1,1,1) occur. Their product is iI,
and they generate the stated D. D is normal. Modulo D, the generators
square to1 and (TL TR)^3=1, so the quotient has at most6 elements.
Their permutation images generate S3, giving exactly6 and hence96.
The center consists of the four scalar matrices i^j I. The projective
order is24. Distinct diagonal characters and the transitive permutation
action also prove irreducibility of this three-dimensional module.

## 2. An explicit symmetric-square intertwiner and the central test

Use the packet's Weil generators

    l=diag(1,i),
    r=(1/2)[[1-i,1+i],[1+i,1-i]],
    U=[[0,1,0],[1/sqrt2,0,1/sqrt2],[1/sqrt2,0,-1/sqrt2]].

U is real orthogonal. On the usual normalized symmetric-square basis,
direct multiplication gives

    U [w Sym2(conj(l))] U^* = TL,
    U [w^-1 Sym2(conj(r))] U^* = TR.

Thus the odd chi3 twist asserted by the packet has an exact algebraic
proof. The untwisted conjugate square becomes, in this basis,

    l0 = [[-i,0,0],[0,0,1],[0,1,0]],
    r0 = [[0,1,0],[1,0,0],[0,0,i]].

Its diagonal kernel consists of all8 diagonal sign matrices. As above the
permutation quotient is S3, proving order48. Complex conjugation gives
the same order for the unconjugated square. This establishes the
48-versus96 distinction without rounded matrix-group closure.

For S=TL TR^(-1) TL, multiplication gives S=w P02. Therefore
S^2=iI, S^4=-I and S^8=I. For a scalar character with
chi_m(L)=exp(2*pi*i*m/24), chi_m(R)=chi_m(L)^(-1),
the character of S^4 is (-1)^m. Every even twist of the untwisted
square has S^4=+I. None equals T.

There is also a proof covering every genuine two-dimensional
representation rho of Mp2Z, without assuming it belongs to the
enumerated Weil-twist family. Its central sheet involution epsilon
has rho(epsilon) eigenvalues a,b in {+1,-1}. The symmetric square
has eigenvalues (1,ab,1), so it cannot act as -I3. Since T(epsilon)
is -I3, T cannot be Sym2(rho). This argument uses the same group
and sheet convention throughout.

These identities support the exact odd-twist relation. They leave the
physical origin of the character and the normalized field map to earn.

## 3. The proposed induced one-form matrices have the wrong character

The source at lines995-996 supplies

    AL=[[1,0,0],[0,0,i],[0,i,0]],
    AR=[[0,-i,0],[-i,0,0],[0,0,1]].

Write b=(0,1,0), the branch fixed by S=AL AR^(-1) AL.
Then AL^2 b=-b and S b=-b. The claimed stabilizer character in
the source comments and relay is instead L^2 -> -1, S -> +1.
The group order and braid relation do not test that character.

For that claimed character, replacing both matrices by their negatives
changes S to -S and preserves L^2. It gives S b=+b and L^2 b=-b.
These replacements repair this matrix/character mismatch. Their
identification with actual transported modes remains a separate proof.

There is a further positive relation worth retaining. The displayed
uncorrected matrices obey exactly

    TL=w^-1 AL,  TR=w AR.

In the packet's character convention T=chi21 tensor A. For the
corrected pair A'=(-AL,-AR), T=chi9 tensor A'. All have the same
projective action. Conjugation by diag(i,1,i) turns AL and AR into
real determinant-one signed permutation matrices, the two quarter-turn
generators of the cubic rotation group. Their image has order24.

Consequently an order24-versus96 comparison cannot, by itself, settle
whether a geometrically earned scalar line completes the field join.
The actual scalar and spin lift must be derived from the full theory.

## 4. The E8 central identity survives with the correct global quotient

Let d5=(1,1,1,1,1,0,0,0) and d3=(0,0,0,0,0,1,1,1).
On integer E8 roots their exponentiated 2*pi phases are both+1.
On every half-root they are both-1. They act trivially on the Cartan.
Thus the images of (-1 in Spin10,1) and (1,-1 in Spin6) coincide
on the faithful248-dimensional E8 adjoint. This proves the paired
sign identity used to reparametrize the holonomies.

The full global subgroup is (Spin10 times Spin6)/Z4. For example take
a Spin10 central generator z acting by i on16 and -1 on10, with the
opposite action on conjugate16. Pair it with -iI4 in SU4. Their
combined action is1 on (45,1), (1,15), (10,6), (16,4) and its
conjugate. This gives the order4 kernel. Its square is the diagonal
(-1,-1) relation tested by the packet. The D5 and D3 root lattices
have combined index4 in E8, consistent with this kernel.

The relay's Z2 quotient describes only that squared relation. Correct
the full global-group statement. The order-two identity itself survives.
The subgroup and its topology are also derived in Distler and Sharpe,
Appendix A, pp.387-388. Only this appendix passage was inspected here.
[Primary paper](https://archive.intlpress.com/site/pub/files/_fulltext/journals/atmp/2010/0014/0002/ATMP-2010-0014-0002-a001.pdf).

## 5. What the theta functions establish

The standard theta and eta transformation identities give the proposed
Jacobi-Dedekind vector weight -1/2, and its conjugate has anti-holomorphic
weight. A full transformation includes the scalar automorphy factor.
The theta numerator has weight1 and eta cubed has weight3/2.
The identities also give the normalized Szego pullbacks below. These
are deductions using the cited formulas. [Theta transformations](https://dlmf.nist.gov/20.7.viii),
[eta transformation](https://dlmf.nist.gov/23.18.E5).

On the stated flat-character meromorphic section spaces, with
S3(z/tau,-1/tau)=tau S3(z,tau), direct differentiation yields

    S3(z/tau,-1/tau)d(z/tau) = S3(z,tau)dz,
    S3'(z/tau,-1/tau)d(z/tau) = tau S3'(z,tau)dz.

For the untwisted basis1,wp the corresponding factors are tau^-1,tau.
Thus both proposed meromorphic two-dimensional spaces admit invariant
lines in this specified family action. An invariant flag alone would
not prove a splitting for an arbitrary infinite group. Here the displayed
identities can supply a complement on these section spaces.

To transport this statement to the physical kernel, use the actual
Serre/Hodge map from H1(S^-3 L), its spin/frame factors, the harmonic
representatives, metric and complete-domain equivariance. Identifying
the degree-two dual line fibrewise with O(2p) does not record all of
its modular transport. A physical family over varying tau also needs
the specified connection/transport used for comparing its fibres.

The two normalized Szego sections S2 dz and S4 dz swap under S.
Their normalized-function L^2 transformations are each+1. Opposite
L^2 eigenvalues in the proposed vector doublet would therefore need
the actual gauge compensator action on the two channels. A swap
alone admits two invariant eigenlines and cannot certify irreducibility.
