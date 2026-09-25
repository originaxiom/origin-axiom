# F14 conditional analytic bridge for a geometric pairing

Pre-execution argument. The representation and geometric matrix
hypotheses are to be decided by the accompanying exact tests. The
analytic implications are authored, not independently reviewed.

## 1. Exact isometries, not a floating trace coincidence

Let the standard faithful discrete Riley representation of the
figure-eight group have m=[[1,1],[0,1]], n=[[1,0],[u,1]],
u=(1+i sqrt(3))/2. A nonsingular complex 2x2 matrix defines an
orientation-preserving hyperbolic isometry; composition with complex
conjugation reverses orientation. Scalar multiples define the same
isometry. Explicit conjugators mapping these generators to words in
them initially give f Gamma f^-1 contained in Gamma.

If f^d belongs projectively to Gamma, then
Gamma contains f Gamma f^-1 contains ... contains f^d Gamma f^-d=Gamma.
Every containment is equality. Thus the map is a genuine normalizing
isometry, not a possibly nonsurjective endomorphism. Exact tests use
this certificate for each of the eight candidate maps. This does not
need a small-word search to prove the size of the whole isometry group.

For theta the matrix diag(-1,1) directly inverts both generators,
has square one, and induces (x,y,z)->(-x,-y,z) on the canonical cusp.
It is holomorphic, hence orientation preserving on the base. Also the
displayed longitude word nMNmmNMn is palindromic, so applying theta
gives its inverse literally, not only up to a guessed peripheral class.

## 2. The representation-level hypothesis

For the same F10 SL4 matrices at fixed q, suppose an invertible J solves

    rho(g)^(-T) J = J rho(theta g),       g=m,n.             (1)

These are 32 linear equations for 16 matrix entries. Exact nullspaces
and determinants at p14 and p34 decide their solvability. The generic
symbolic witness, if found, is checked entrywise and its specializations
must remain nonsingular; generic rank alone is not the certificate.

For rho_chi=chi rho, theta inverts the meridian exponent, so BOTH sides
of (1) acquire chi^-1. It therefore gives a complex-linear flat bundle
map theta*E_chi -> E_chi*, including chi=+/-i, not only real twists.
For other candidate maps with exponent epsilon, a linear map requires
rho(g)^(-T)J=chi^(epsilon+1) J rho(sigma g); an antilinear map replaces
that factor by chi^(1-epsilon), since the untwisted matrices are real.
The tests retain these phases rather than assuming that dualization
commutes with an arbitrary central character.

Scale a successful J by one constant complex fourth root so det J=1.
This chooses only a central phase and the volume normalization of an
isomorphism, not a coupling or background parameter. Before this scaling
the volume vertex carries det J; its modulus must not be discarded
before matching the metrics below.

There is no contradiction with F10. Its forbidden equation had rho(g)
on the right, not rho(theta g). The longitude trace obstruction is
nonzero for q!=1, while theta INVERTS that longitude before dualization.

## 3. The end metric comparison is a separate, explicit step

Use F10's unitary cusp reference frame, with

    Cx=-N/sqrt(u0), Cy=-kD-beta P/u0, Cz=u0'H/(2u0),
    u0=z^2/4-beta^2/L^2, P=N^2.

Let R exchange basis coordinates 0 and 3, leaving 1 and 2 fixed.
It is unitary and satisfies RNR=N^T, RDR=D, RPR=P^T, RHR=-H.
Consequently in ALL coordinate directions

    R (theta* C_ref) R^-1 = -C_ref^T.                    (2)

In particular the radial sign in the dual is not optional. Formula
(2) identifies the reference metrics exactly for one local map.
But the global J need not equal this chosen R in the cusp frame.

Volume-normalize the constant change to F10's peripheral normal form.
In its flat connection frame, the reference unitary-frame change is
S=u0^(H/2). Any other peripheral intertwiner in (1) differs from R by
Z commuting with exp N and q^D(I+beta P). Since log(exp N)=N and the
longitude's q and q^-3 generalized eigenspaces are distinct, this common
centralizer is exactly

    Z=a I+b N+c P+d Pi,       Pi=diag(0,1,0,0).

The three-dimensional Jordan chain and its separate one-dimensional
eigenspace give this description; its dimension four is also tested.
Its determinant is a^3(a+d). Invertibility implies a!=0 and a+d!=0.
In the actual reference frames the corresponding J is

    S^T R Z S = R (a I+b N/sqrt(u0)+c P/u0+d Pi).          (3)

Both this expression and its inverse are uniformly bounded for large z.
An exact inverse follows from N^3=0 and Pi N=N Pi=0. Compact lower
annuli cause no problem. Therefore an arbitrary successful GLOBAL map
J does preserve the bounded-distance/positive-norm equivalence class;
one must not simply assume the global map equals the local R.

## 4. Uniqueness upgrades it to an isometric global operator map

Let h be F12's determinant-one harmonic metric, and h* its induced dual.
Pull h* back through J onto theta*E_chi. It is harmonic: flat-bundle
isomorphisms preserve the harmonic-metric equation, and theta is an
isometry of the base. It has determinant one by the chosen det J=1.
The metric theta*h is another harmonic metric on that same flat bundle.
F12's bound, (2)--(3) and properness of theta show that their target
distance is uniformly bounded on the cusp and compact core.

F13 uniqueness applies: theta preserves irreducibility, and its bounded-
distance proof requires only the distance bound between these two maps.
The two metrics agree. Thus J is a unitary bundle map between the
ACTUAL metrics, not merely a bounded algebraic intertwiner on a model
end. For coefficient-valued forms set U alpha=J theta*alpha. It is a
same-degree unitary map from the E_chi Hilbert space to its dual's:

    U d_E = d_E* U,    U d_E^dagger=d_E*^dagger U,
    U Delta_E=Delta_E* U.                                (4)

The second equation follows from the first and unitarity, not by
formally transposing an unbounded differential. Pullback by a proper
isometry maps smooth compact supports to smooth compact supports;
closure then preserves the complete domains. Thus (4) includes the
global ordinary-L2 domains, all eigenvalues and their multiplicities.
No new finite cusp boundary condition or mode truncation is inserted.

This conclusion is presently about the exceptional base backgrounds
where global existence and irreducibility were earned. No assertion
that arbitrary finite-cover characters admit a lifted theta is made.

## 5. Whole vertex and scalar-block response, not a chosen overlap

Exterior-square J gives the corresponding unitary map U6 on the six
coefficients and complete Hodge domains. The invariant four--four--six
tensor is the determinant-volume pairing already earned in F09/R38.
In a unit exterior basis K_AB,CD=epsilon_ABCD, the identity is

    (exterior^2 J)^T K (exterior^2 J)=(det J) K.

With det J=1 and theta orientation preserving, the integral of the
paired one-form vertex is unchanged under U,U,U6 (up to a harmless
fixed convention phase if other volume conventions are used). The
standard metric volume identifies the dual six with the six itself;
its exterior metric makes this identification unitary. Consequently
whole normalized tensors on corresponding spectral subspaces have
equal singular values and norms. This includes the harmonic matter
modes whose L4 regularity F13 established, so integrability is earned.

This coefficient map can be embedded in the actual parent symmetry:
in the standard E8 coordinates for D5 on the first five axes and A3
on the last three, change signs on axes 0,5,6,7. It is a product of
the root reflections in e0+e5, e0-e5, e6+e7, e6-e7. It therefore has
a compact-group Weyl lift, not just a permutation of weight labels.
Its D5 action exchanges the two spinor halves, while its A3 action
implements dualization up to a compact inner change of basis. The
root-reflection and full-root-set action are tested explicitly.
The lift preserves the Lie bracket and invariant norm; together with
the metric-compatible SL4 bundle identification above it preserves
the source-free adopted classical parent kinetic and interaction terms.
No new unconstrained sign or independent coupling is supplied.

In particular for the properly transformed bilinear source J_source,
unitarity and (4) give the WHOLE scalar-block response equality

    <U6 J_source,(p^2+2 Delta6_dual)^-1 U6 J_source>
      = <J_source,(p^2+2 Delta6)^-1 J_source>, p^2>=0.       (5)

F13 earns the positive gap and finite L2 source at the exceptional
points. Equality (5) includes every mediator profile, not one selected
overlap or an assumed complete finite mode list. This does not by
itself complete the full gauge-fixed physical propagator or quantum
measure; it constrains the claimed internal classical mechanism.

## 6. Honest consequences if the exact tests pass

The geometric symmetry would restore the paired spectra and whole
parent responses in these classical backgrounds, despite their real
escape from every flat fiberwise pairing. Mere nonparallel projective
deformation would then NOT supply the desired asymmetric coupling.
That is a restriction on this specified background/domain/action, not
a theorem excluding chirality in the arithmetic class, other ends,
defects, covers, changed holonomy or symmetry-breaking quantum phases.

If a later construction claims to break this pairing, it must name
which hypothesis changes and solve the resulting equations and domain
again. An exact symmetry can be spontaneously broken; (5) does not
decide that phase question, anomaly constraints, or an experimentally
observed spectrum. The constructive existence, localization, mediator
gap and interaction-admissibility results remain valid either way.
