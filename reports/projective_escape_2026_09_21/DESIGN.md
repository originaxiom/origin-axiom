# F10 pre-execution design: a real projective escape with its actual cusp

September 21, 2026. Local fork at 9c0d1c67. Previous turn: progress.

## Quantifier and honest prior

Test Ballas' displayed one-parameter representation of the figure-eight
knot group, its finite-cover restrictions and its complete cusp end.
This is not a classification of the arithmetic class or every physical
completion. Retain F08's supplied SU4-in-E8 parent and positive kinetic
metric. A global harmonic metric away from the geometric point is NOT
assumed. Geometric finite Busemann volume is NOT that physical metric.

Write q=2t>0, with q=1 the geometric point. Use the actual determinant-one
generator matrices in section 6, not its later projectively rescaled
longitude. The relation is m w=w n, w=n m^-1 n^-1 m; longitude
l=w reverse(w)=n m^-1 n^-1 m m n^-1 m^-1 n.

Expected exact facts: longitude eigenvalues q,q,q,q^-3, determinant one,
and trace minus inverse trace equal to -(q-q^-1)^3. Thus q!=1 removes
both flat linear and antilinear coefficient-to-dual isomorphisms, not
merely the displayed constant J. This need not remove every nonlocal
or base-isometry-induced spectral equivalence. At q=1 explicitly solve
a simultaneous intertwiner to the balanced tensor of the parabolic
SL2 generators [[1,1],[0,1]], [[1,0],[u,1]], u=(1+i sqrt(3))/2.

For q!=1 expect a simultaneous cusp normal form

    M=exp(N), L=q^D (I+beta P),
    N=E02+E23, P=E03=N^2, D=diag(1,-3,1,1),
    beta=6/(q-q^-1).

Construct its conjugator from the longitude's simple-eigenvalue projector
and the meridian's nilpotent Jordan chain. This is a faithful actual map.
Do not copy the source's printed longitude formula, which contains an
unbound x in one entry; compute the specified word from its two generators.

## Local full-equation positive

On the cusp metric z^-2(dx^2+L^2 dy^2+dz^2), with unit-period x,y,
let H=diag(1,0,0,-1), k=log(q), f^2=z^2/4-beta^2/L^2 and take z>2|beta|/L.

    Cx=-N/f,
    Cy=-k D-beta P/f^2,
    Cz=(f'/f)H.

Expected: exact flatness AND full matrix moment equation for this
noncommuting connection. A, Psi are its real-matrix anti/symmetric
parts in a positive unitary frame. Its parallel holonomies are conjugate
to the normal form above, so the cusp is the actual deformed one, not
a rank-one toy. L can be any positive rectangular shape, including
2 sqrt(3) for the complete figure-eight marking up to orientation.
This is a tail solution only, not an extension over the compact core.

Its norm density per unit coordinate torus area is expected to be

    L/(z f^2)+12 k^2/(L z)+beta^2/(2L z f^4)+2L(f'/f)^2/z.

It diverges logarithmically for k!=0 despite zero residual potential.
For ANY positive Hermitian metric on the flat cusp, parallel transport
of an eigenvector gives a lower bound on integral |Psi|^2 per unit log z.
A separate analytic reviewer checked this inequality and the cohomology
scope, without reading/summarizing the paper or running probes. This is
not external peer review or a substitute for the author's argument.

## Boundary and controls

Since L-I is invertible for q>0, q!=1, the whole torus local system is
acyclic, with an explicit Koszul contraction. On a compact oriented core
with all torus ends so acyclic, Euler and Poincare-Lefschetz imply equal
ordinary H1 dimensions for E and E*. No individual H1 count or physical
L2 identification is predicted. Pullbacks to finite covers retain this
condition because each lifted cusp contains a positive longitude power.

Controls: recover the hyperbolic self-dual point; show projective
longitude rescaling changes determinant/linear local system; one
off-unit eigenvalue plus a trivial summand is NOT acyclic; include a
positive residual when f is incorrectly replaced by z/2 at beta!=0;
and verify zero residual with infinite norm in a diagonal cusp control.
Use exact symbolic identities, no empirical inputs or floating tolerance.

## Retrieval and custody

already_banked: `projective deformation Lorentz` and `cubic Codazzi`.
Inspected flagged B1115/B1122 and read B101; the latter concerns a different
surface/SL3 construction. papers/sl4_dehn_filling/README.md already
credits Ballas' distinct convex-projective family: no new-to-literature
or absent-from-repository claim. Scoped additional name queries and
the previous all-history receipt supply navigation, not latest coverage.

Personally read all 26 pages of Ballas' author PDF dated March 28, 2014,
including the Busemann definition, cusp construction and theorem proof.
Rendered and inspected page 22 for matrices and projective normalization.
PDF SHA256 cdb095d17aba2f228ede3bfc52731afd66caa569c02bbf32ed97ed621d874468.
The published nearby convex-structure theorem is credited, not reproved.
No subagent paper summary. Heusener-Porti was discovered but not read or
used as a theorem in this calculation. No new remote-head sweep.

Seal this design, proof, producer and tests before first execution;
preserve failures. No shared B number, other-seat edit or publication.
