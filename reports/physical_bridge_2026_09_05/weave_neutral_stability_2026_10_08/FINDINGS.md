# Neutral Higgs fields and magnetic stability

The same supplied curved E8 action admits a new, nonparallel SM gauge
minimum without an extra Wilson line. It does not produce net charged
chirality. The first nonzero magnetic flux remains unstable for every
finite amplitude of this neutral Higgs field. Higher fluxes have a
positive end spectrum, but their global stability is not decided here.

These are conditional classical results on the fixed complete punctured
elliptic surface, not a derivation of the action, metric, spin or vacuum
from genesis. The full parameter-free SM/TOE goal remains unachieved.

## The construction and its positive result

Let S be the extending trivial spin line, with a holomorphic section psi
satisfying psi squared = omega, where omega is the nowhere-zero
holomorphic differential of the compact elliptic curve. Set

    A = s(w+2nZ), Q = Q_principal+c*psi*Z, R = 0.

The symbols and normalization are those of the pinned magnetic packet.
The integer n and finite complex amplitude c are inputs. No new field,
boundary functional, Wilson line or measured constant has been added.

Only this one of the four extending spin lines admits such a nonzero
holomorphic L2 section. The other three degree-zero spin lines do not.
The cusp norm excludes every pole, including the first endpoint;
Laurent orthogonality also excludes essential singularities. The section
belongs to the complete graph domain and has finite quartic norm.

Since Z commutes with the principal triple, the added field changes no
F residual and leaves the moment equal to -nZ. The moment is parallel
and commutes with Q, so the FULL first variation still vanishes.
The energy remains pi*n^2*kappa(Z^2)/g6^2, independently of c.

For c nonzero the connected gauge group is S(U3 x U2), including at
n=0. The commutator with the principal field has constant norm along
the cusp, whereas the neutral term decays there; invariance forces
separate commutation with the principal triple and Z. At n=c=0 the
SU5 control is recovered. The inherited Z6 form is the connected SM
gauge group, not a new charge-normalization result.

At n=0 the full potential is a positive sum of residual squares, all
zero on this configuration. Its physical Hessian is therefore
nonnegative. This is a classical minimum with flat moduli, not an
isolated selected or quantum-stable vacuum. The gauge-invariant norm
depends on abs(c)^2, so its amplitude has not disappeared into a basis
choice. Both spin and amplitude selection remain unpaid.

Its fermion perturbation is bounded, decaying and zeroth order on the
same graph domain. Local ellipticity and Rellich make it graph-compact.
The preceding zero charged index is unchanged, although individual
kernels may jump. Thus this positive gauge construction is not the
chiral Standard Model.

## The complete fluctuation test

The calculation retains the connection, both spin fields, conjugates,
quadratic curvature, all mixed terms, and the physical gauge quotient.
The quadratic potential includes the moment times the SECOND variation
of the moment, not only the squares of linearized residuals. Dropping
that term misses the negative directions.

The full complex E8 adjoint decomposes into charge q and principal
spin j as follows:

    q=0: 12 V0 + V1+V2+V3+V4
    q=+/-1: 6 V2; q=+/-4: 3 V2; q=+/-6: V2
    q=+/-2: 3(V1+V3); q=+/-3: 2(V1+V3)
    q=+/-5: 6 V0.

All 240 roots and eight Cartans are included. An independent abstract
SU5 tensor-weight implementation gives the identical roster. The
canonical coordinate reduction, positive kinetic map and weighted
adjoints are checked, not just an asserted spectral formula.

There are 248 A/Q and 112 R zero-angular scalar channels, plus 136
vector slots. These retain gauge-fixed redundancy and are NOT particle
counts. Extreme-weight channels are retained.

For k=nq, the only potentially negative end channels are the lowest
Q weights at odd j:

    E1(k) = (k-1)^2-3/4
    E3(k) = (k-2)^2-7/4.

The actual odd-j charges are 0, +/-2, +/-3. An artificial q=1,j=1
module fails the positivity control, demonstrating why the full
representation roster matters.

For abs(n)=1, three complex channels have threshold -7/4 and two
have -3/4, in the supplied curvature units. Their actual color/weak
weights identify a color-antitriplet weak-singlet and a color-singlet
weak-doublet at positive flux; negative flux conjugates them.
They are scalar fluctuations, not fermion generations. In particular,
the instability is not merely a desired electroweak Higgs mass.

For n=0 or abs(n)>=2, the full essential bottom is 1/4. Nonzero angular
sectors confine, and the neutral vector channel attains this bottom.
The all-integer statement follows from the exact charge roster and
quadratic inequalities in PROOF.md, not from the finite n=-3,...,3
control grid.

## What the first-flux obstruction really excludes

Long compactly supported packets arbitrarily far down the cusp give
negative physical variations. They satisfy the complete form-domain
conditions; their nonlinear paths have finite quartic norm. At c=0
the lowest Q weight is in the actual gauge slice. For finite c the
added terms decay on the escaping supports; the bare gauge-invariant
quadratic form remains negative, so the directions cannot be pure gauge.

Disjoint supports give infinite physical Morse index at abs(n)=1.
The earlier lower bound of 30abs(n) global negative directions was not
wrong: it was never a full count. This extends it in a different sector.

The neutral physical field behaves as sqrt(y)*exp(-pi*y/ell).
For each fixed finite c it and its relevant unit-frame derivatives
decay. The Hessian change is relatively form-compact, so it cannot
change the essential spectrum or cure this first-flux instability.

Closing scope: in this supplied action, the family
A=A_n, Q=Q_principal+c*psi*Z, R=0 has infinite physical Morse index
at abs(n)=1 for every finite c. This does NOT exclude higher flux,
other end profiles, sources, domains, parents or the generated architecture.

At abs(n)>=2, c=0 still has the preceding admitted negative directions.
A positive essential threshold is not a stable global vacuum. Whether
a finite neutral amplitude removes ALL discrete negative modes remains
open in this packet. NEXT_TEST.md records the next bounded test.

## Verification and remaining acceptance

Pre-execution commit 57f3fd304e8cba57fd8107380482e9739c0305f1 was
pushed and server-confirmed before any scientific import, run or test
collection. Seven scientific files and five pinned-and-working source
files stayed byte-identical.

The first unchanged runs passed 30 native predicates, 17 separate
rational/abstract-weight predicates, and 16 focused tests. Eleven-packet
regression passed 180 tests with the tree read-only and unchanged.
Native elapsed time was 3.879838 seconds; reference 0.097175 seconds;
focused pytest reported 6.64 seconds and regression 33.89 seconds.
RECEIPTS.json and raw outputs preserve the literal exits and hashes.
No scientific failure or source repair occurred.

Both implementations have the same author. They verify finite algebra,
coordinate identities and discriminating controls, not independent
acceptance of the global infinite-domain analysis. PROOF.md is an
authored proof requiring specialist review. The full suite and main-bank
acceptance remain unpaid. Governance output records four inherited
failure categories, not an all-green repository certificate.
The final staged-content gate returned 26 PASS and four inherited FAIL
categories (attribution, test vacuity, seal provenance, relay debt), with
review counter 373. GOVERNANCE_PRESEAL.txt and GOVERNANCE_FINAL.txt retain
the raw outputs. The identification audit retained nine UNEARNED rows
against its baseline of nine; no shared identification was promoted.

Main 6df009415 B1613/B1614 and SM 2abff008c W36 were personally read
at the scope recorded in DESIGN.md. They were not independently replayed
or used as evidence for this result. W36's closed-surface SU5 index
argument must not be broadened to punctured hypercharge backgrounds.
No mixing measurement or observer/qualia identification is adopted here.

Post-run fetch advanced main to87f47afa0 (B1615 couplings) and SM to
7c5d9726c (W37, magnetic reading, owner-choice tags). INTAKE_AFTER_RUN.md
records the personal source/code reads and limits. In particular, B1615's
numerical sum-rule grid is not an exact all-family proof, and the SM
relay's hypercharge bulk-degree formula is not yet this physical index.
No such incoming conclusion is silently promoted into this result.

The next physical milestone still requires a stationary, stable,
interacting chiral sector with its complete spectrum and anomalies on
one action and domain. Three families, vacuum/parameter selection,
quantum consistency and gravity remain distinct duties.
