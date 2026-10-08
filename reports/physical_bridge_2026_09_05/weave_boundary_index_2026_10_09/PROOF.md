# The coefficient blind boundary has zero net charged index

This is a conditional argument for the supplied curved E8 action on
one smooth compact finite cusp truncation X. Its metric, spin, gauge
embedding, cut and boundary pairing are inputs. The result concerns
net chiral multiplicities, not the absence of matter, bosonic
stationarity, anomaly completion or the parameter-free SM/TOE.

## The physical source and target

Retain all independent left Weyl slots (lambda,a,u,v). Their coordinate
Hilbert weights are (Omega^2,1/2,Omega,Omega). The actual mass M and
trace-dual target are those derived in
../weave_physical_mass_2026_10_08/PROOF.md. In particular its target in
a representation R is the conjugate Hilbert bundle of the left
conjugate(R) sector. This is not an additional set of left particles.

At zero coefficient connection/Higgs fields, the DENSITY derivative
matrix, before Hilbert normalization, is

    h M = Ax partial_x + Ay partial_y,
    Ax = diag([[0,-1/sqrt(2)],[1/sqrt(2),0]], [[0,1],[-1,0]]),
    Ay = diag(-i Ax_first, i Ax_second).

Both matrices are skew under ordinary transpose. Integration by parts
therefore gives a symmetric complex bilinear in the bulk, with
boundary pairing f^T (Ax n_x+Ay n_y) g. It is NOT symmetric on a
boundary domain until that pairing vanishes. The zero-order Higgs
terms obey the trace-dual transpose relation Qdual=-Q^T, Rdual=-R^T,
as the pinned actual mass computation checks. The metric weights
cannot be replaced by a flat density in the curved interior.

In the kinetic-normalized outward collar frame the original normal
symbol is V=diag(-sigma2,-sigma2). Normalizing the target by V gives
Mnormal=partial_t+i R0 exp(t) partial_theta+lower order, with
R0=diag(1,1,-1,-1). The prior boundary uses

    B(theta)=i diag(exp(i theta/2),exp(-i theta/2)),
    Sigma=[[0,B],[Bdagger,0]], Pplus=(I+Sigma)/2.

The internal left trace is Sigma=+1. Since the normal symbol is now
I, its Hilbert-adjoint trace is Sigma=-1, not +1. The physical
anti-linear source-to-target map in these coordinates is C=V complex
conjugation. Its collar formula obeys

    V conjugate(Sigma) V=-Sigma,
    Pplus^T V Pplus=0.

Thus the actual boundary bilinear vanishes between the two allowed
left conjugate sectors; C takes precisely their allowed traces to
the adjoint trace. It is an invertible anti-linear map on Sobolev
domains. There is no assumption of zero boundary values.

C squared in this collar representation is -I. At the coefficient
trivial cusp endpoint with density dxdt,

    Mnormal0=partial_t+i R0 exp(t) partial_theta
                    +diag(1/2,-1/2,0,0),
    C Mnormal0 = -Mnormal0 dagger C.

The minus sign matters; it does not alter the kernel bijection.
This coordinate check is not the global proof. Globally use the
natural conjugation between a left bundle and the physical trace-dual
target furnished by the Weyl Hessian. The normal target identification
and V are needed only near the boundary. Extending an outward normal
vector field across X is neither required nor asserted.

## Fredholm domains

The kinetic-normalized internal principal map has symbol
xi_x I+xi_y J, J=diag(-i,-i,i,i), whose adjoint product is
(xi_x^2+xi_y^2)I. Thus it is Dirac type between its actual Hermitian
source and target bundles. In the normal collar the adapted tangential
symbol is proportional to i R0. Sigma anticommutes with R0 and is a
smooth Hermitian involution. The half-frequency entries descend under
the actual spin transition diag(G,G,-G,-G); G is common in all slots.

Consequently both source and adjoint boundary conditions are local
elliptic. Bar--Ballmann Corollary3.18 gives the local criterion,
Theorems3.6/3.9 the adjoint and boundary regularity, and Theorem5.3
gives Fredholmness on compact X:
https://arxiv.org/html/1307.3021v1.
These results provide the analytic framework, not this model's index.

The domain is exactly

    D_R={f in H1(X,F_R): Pminus trace(f)=0}.

Its graph norm is equivalent to H1 by the boundary elliptic estimate
and the first-order upper bound. The adjoint domain is the analogous
H1 space with Pplus trace(g)=0 in normal target coordinates. No
stationary-point or complex-integrability assumption enters this
elliptic-domain argument.

## Removing coefficient backgrounds without changing the boundary

Assume an unbroken compact gauge group H so the background and
operator preserve its isotypic decomposition. Write each left sector
as R tensor (Fgeo tensor E_R), where Fgeo contains the four ORIGINAL
geometric slots and E_R is the multiplicity bundle. Do not divide
out an H factor unless this decomposition is actually preserved.

The compact surface X has nonempty boundary and retracts to a finite
graph. Any Hermitian complex rank-d bundle over this graph is trivial:
choose vertex frames and frames along a spanning tree, then extend
frames on each remaining edge between its prescribed endpoints using
path-connectedness of U(d). Retraction and smooth approximation give
a smooth unitary trivialization over X. This is a topological bundle
statement, not a statement that its connection has trivial holonomy.
The trace-dual trivialization is used for the conjugate bundle.

After these trivializations the boundary remains exactly
Sigma tensor I_d, since it is coefficient-blind. We have not altered
spin, geometric connections or the prescribed winding of B. Turning
off the coefficient connection and Higgs endomorphisms changes M only
by a smooth order-zero map L. On this FIXED compact X,
L:D_R subset H1 -> L2 is compact by Rellich embedding. The fixed-domain
family M_s=M_0+sL has the same principal symbol and boundary, remains
Fredholm, and has constant index. It may change holonomy, flux and
stationarity along the interpolation: it is an operator homotopy,
not a proposed path of physical vacua. Compactness at each finite cut
does not justify taking the complete-cusp limit.

## The representation resolved conclusion

At the coefficient-trivial endpoint R and conjugate(R) have the same
multiplicity rank, geometric operator and boundary pairing. Hence

    ind M_R(0)=ind M_conjugate(R)(0).

The actual global Weyl transpose map, now with compatible boundary
domains, separately gives

    ker M_R dagger anti-linearly isomorphic to ker M_conjugate(R),
    ind M_R=-ind M_conjugate(R).

Together these imply ind M_R(0)=0, and compact index invariance gives

    ind M_R=0 for every such smooth H-preserving background.

This is an equality of representation multiplicities, not merely of
their total dimensions. For the supplied SM embedding the positive
integer-Z charges1..6 have multiplicity ranks5,10,10,5,1,5 and gauge
dimensions6,3,2,3,6,1 respectively. Their conjugates all occur; the
exotic q=5 is retained. The actual248 weight reconstruction checks
212 charged dimensions and36 neutral ones. The net charged index
vector for this compact boundary problem is (0,0,0,0,0,0).
The proof does not compute the separate finite kernel dimensions;
paired zero modes can remain.

A symmetric full bilinear ALONE does not imply this conclusion.
For a rank-two map K:C^5 -> C^2, ind K=3, ind K^T=-3 although
[[0,K^T],[K,0]] is symmetric. That control retains the physical
transpose pairing but lacks the identical charged-endpoint problem.
It prevents a trace symmetry from being misreported as a universal
chirality obstruction.

## A concrete boundary change outside the argument

The same spin seam admits the supplied pair, for integer n,

    B_R,n=i diag(exp(i(1/2+n)theta),exp(-i theta/2)),
    B_barR,n=i diag(exp(i theta/2),exp(-i(1/2+n)theta)).

Each gives the same local principal complementing/current properties.
Together they obey V conjugate(Sigma_barR,n) V=-Sigma_R,n,
so the physical conjugate fields and cross-sector boundary bilinear
remain compatible. But for n nonzero the two coefficient-trivial
boundary problems are no longer identical. Their relative
determinants with respect to B_0 have windings n and -n. A homotopy
of nonsingular unitary boundary maps cannot remove that winding.

This is a precise escape from a HYPOTHESIS, not a computed nonzero
physical index or a three-family claim. The construction uses
representation-specific projectors: it is equivariant under the
retained H but is not by itself a covariant full-E8 boundary law.
An actual Higgs/defect/registering field and surface action must
generate such projectors and their winding, or this is another input.
No selection of n, boundary source, new index formula or stationary
bosonic completion is inferred here.

## Scope and next physical test

The compact homotopy strategy already appears for the different silver
parent in ../silver_spectral_completion_2026_10_05/PROOF.md section1.
The present work supplies the actual four-Weyl operator, collar reality,
spin and representation-domain checks for this boundary. It is not a
rediscovery of the general method or a transfer of silver spectra.

Preserve the previous local kinetic positive and the earlier
complete-cusp nonzero indices at magnetic saddles. They are different
domains. The source three/zero and silver formal chiral constructions
are also unchanged. This proof excludes net chirality only for this
coefficient-blind compact boundary with its stated field content and
smooth isotypic lower-order deformations. It excludes neither other
boundary classes nor the generated architecture.

The next useful test is a specified operator-class change generated
by one action: derive a representation-sensitive boundary response
or a relative/nonlocal end mechanism, then compute its index and
complete charged spectrum on that SAME stationary positive theory.
An index without its physical boundary mechanism would not meet
the mission. Analytic acceptance by a nonauthor remains outstanding.
