# An interacting pair constrains its line coupling

## The fixed parent

Use the supplied curved parent on an internal curve Sigma: a vector multiplet V, an affine gauge-connection chiral field A and two adjoint chiral fields Q,R in a spin line S with S squared equal to K_Sigma. Its spin kinetic metric is the same positive metric for Q and R. Write X=(Q,R)^T and J=[[0,1],[-1,0]]. The spin superpotential is

    W = (1/2) integral kappa(Q Dbar_A R - R Dbar_A Q).

The derivative includes the gauge-connection cubic. Superspace coordinates and the coefficient of W are held fixed. The antisymmetric surface pairing is likewise kappa(Q delta R-R delta Q). The original four-Weyl operator and its domains remain those of the source; no new physical chirality definition is introduced here.

## The exact linear symmetry

Let U be a constant complex 2 by 2 matrix acting only on the Q,R label. It commutes with Dbar_A. Direct multiplication gives

    U^T J U = det(U) J.

Consequently W(UX)=det(U) W(X). The non-Abelian interaction obeys the same identity because [aQ+bR,cQ+dR]=(ad-bc)[Q,R]. The antisymmetric surface pairing scales by det(U) too. Since the functional is not identically zero, invariance of the fixed W for arbitrary fields requires det(U)=1. Its coefficient is not allowed to transform as a compensating spurion.

The fixed positive kinetic metric requires U dagger U=I. Intersecting these two conditions gives SU(2), acting on this two-field label. Unitarity also preserves [Q,Q dagger]+[R,R dagger]. Thus the D-term source is unchanged. Constant SU(2) transformations preserve the displayed bulk superfield functional and its surface pairing, before any domain is imposed.

A unitary transformation of determinant different from one still preserves the bosonic commutator norm, because its determinant has modulus one. That does not make it a symmetry of the fixed superpotential. A compensating R transformation or change of superspace convention could enlarge the transformation being considered, but would lie outside the fixed-input statement. This result is not a classification of all symmetries of the physical theory.

## Compatible line charges

For the diagonal subgroup write Q -> exp(i a theta)Q and R -> exp(i b theta)R. The infinitesimal pairing condition is

    H^T J + J H = (a+b)J = 0,  H=diag(a,b).

Thus a+b=0 for a continuous circle. If the circle has period 2pi and its action is single-valued, a and b are integers; this is the character condition, not a selected nonzero value. The trivial choice is allowed.

Given a Hermitian line L with unitary connection B, the rank-two flavour bundle L^a plus L^-a has determinant canonically trivial, dual metrics, and the parallel alternating pairing J. The induced connections have curvatures aF_B and -aF_B. Their trace vanishes, so they satisfy the infinitesimal pairing condition. This constructs compatible bundle and interaction data, conditional on the supplied L and connection. Introducing B into the derivative is a background coupling, not a derivation of B from the old action.

For a local change of frame with phase theta, our convention is nabla_Q=d+i a b and nabla_R=d-i a b with real connection one-form b. The change b -> b-d theta compensates Q -> exp(i a theta)Q and R -> exp(-i a theta)R. The product derivative has no residual flavour connection, since the charges sum to zero. Omitting that compensator for position-dependent theta fails covariance. Constant flavour rotations alone do not verify local bundle gluing.

Putting the SAME line L on both fields instead gives flavour determinant L squared, with connection curvature 2F_B. A nonzero F_B cannot admit the unchanged parallel alternating pairing: applying the squared covariant derivative to a parallel determinant trivialization would give 2F_B=0. A flat order-two line can evade this curvature obstruction when a compatible square trivialization is supplied; the common sign -I is already in SU(2).

On an open surface L squared can be holomorphically trivial even when the chosen Hermitian connection has nonzero curvature. A holomorphic trivialization need not be parallel or preserve the fixed positive pairing. It therefore does not erase this connection-compatibility requirement. One may introduce a transforming coefficient, a different pairing, a different superspace/R twist or a changed parent, but those additional choices must be accounted for rather than silently treated as the original coupling.

In particular, IF the modular line from cusp_connection is transported to this role by a specified map, its F=-6in dA gives determinant curvature -12in dA for a common Q,R twist. For n nonzero it fails this restricted parallel-pairing condition. The opposite twist passes the algebraic condition for every n, including zero. This neither rules out all uses of the modular line nor selects one unit. No base map from the modular surface to Sigma is supplied by this argument.

## Why a uniform adjoint twist is not an existing gauge field

An internal gauge generator acts on the Lie algebra as a derivation: ad(Z)[X,Y]=[ad(Z)X,Y]+[X,ad(Z)Y], by Jacobi. In contrast a scalar endomorphism cI has defect

    c[X,Y] - [cX,Y] - [X,cY] = -c[X,Y].

On a nonabelian algebra this vanishes for all X,Y only when c=0. Likewise a nonzero scalar automorphism uI preserves the bracket only when u=u squared, hence u=1. This statement concerns scaling the WHOLE adjoint; it does not forbid a nontrivial cocharacter that assigns different charges to different root spaces. Nor does it forbid scalar action on one representation block when compatible conjugate and interaction blocks are retained.

The existing physical magnetic background is precisely a specified cocharacter construction, not a uniform scalar twist of all adjoint components. Its charged index and its separate anomaly/stability qualifications are not changed here.

## Domain and physical scope

The source's original identical Q,R complete graph cores at the flat origin are compatible with constant SU(2) mixing: the coefficient maps are bounded unitary, commute with the corresponding spin differential, and map compact-support cores onto themselves. This is not a claim that every chosen Higgs background or finite boundary projector is invariant. Such extra data must be transformed or checked separately.

The newly coupled L^a plus L^-a operator would need its own global analytic and physical acceptance. A trace-zero flavour curvature is not a proof of zero charged physical index, anomaly cancellation, stable vacuum or selected family count. It is also not a determinant line of a family of matter operators. The present result constrains one possible coupling of the already-defined interacting fields; it does not identify the W45 modular index with the complete parent index.

The useful reduction is that two independent diagonal line charges are not free within this fixed action: one determines the other. The remaining line, connection, charge normalization, end conditions and any required map from genesis remain inputs until separately derived.
