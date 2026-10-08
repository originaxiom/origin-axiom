# Physical fermion map and the magnetic charged index

Authored conditional derivation in the pinned curved E8 parent.
The metric, spin line, embedding, action and domain remain supplied.
The backgrounds are stationary saddles at nonzero integer flux; no
stable observed vacuum or parameter-free selection is inferred.

## Actual fermion bilinear

Let Dbar=partial_x+i partial_y-i ad A, Dz=partial_x-i partial_y-i ad A dagger.
The four independent LEFT Weyl coefficients are (lambda,a,u,v), with
coordinate kinetic densities (Omega^2,1/2,Omega,Omega) under dxdy.
lambda is the vector multiplet's scalar gaugino; a,u,v are the A,Q,R
chiral fermions. Their right fields are Hermitian conjugates, not four
additional independent left fields.

The parent W=(1/2)integral kappa(q Dbar r-r Dbar q) has quadratic part

    W2(x)=integral kappa(u Dbar v+i a([q,v]-[r,u])),

for x=(a,u,v). Polarizing and integrating by parts gives the density
dual coefficients of its Hessian:

    (i*t, p2, -p1),
    p1=Dbar u+i[q,a], p2=Dbar v+i[r,a],
    t=[q,v]-[r,u].

All background and fluctuation commutators remain. Cyclic trace and
the complete-domain integration by parts make this Hessian symmetric
as a complex BILINEAR on left Weyl profiles. It is not a Hermitian
quadratic form and does not equate opposite-charge left fields.

Use the normalized gauge Killing operator from the same kinetic metric,

    D0 epsilon=sqrt(2)*(Dbar epsilon,-i[q,epsilon],-i[r,epsilon]),
    D0 dagger x=-[Dz a-2i Omega([q dagger,u]+[r dagger,v])]
                                                   /(sqrt(2)*Omega^2).

Choose once the harmless constant gaugino phase in which its mass
bilinear is integral Omega^2 kappa(lambda D0 dagger x). This is the
metric dual of sqrt(2) times the actual affine gauge tangent, not a
freely assigned Yukawa. Its transpose is obtained explicitly:

    integral kappa[(Dz lambda/sqrt(2))*a
       -sqrt(2)*i*Omega*[q dagger,lambda]*u
       -sqrt(2)*i*Omega*[r dagger,lambda]*v].

Consequently the mass map, with the bilinear trace dual identified by
the positive Hilbert metric, has rows

    M(lambda,a,u,v) = (
       D0 dagger x,
       2i*t+sqrt(2)*Dz lambda,
       p2/Omega-sqrt(2)*i*[q dagger,lambda],
       -p1/Omega-sqrt(2)*i*[r dagger,lambda] ).

Its target is the conjugate Hilbert space of the opposite-charge LEFT
profiles; this is what a gauge-invariant Weyl mass bilinear requires.
The output coefficients are written in the trace-dual frames, not
incorrectly given the input spin/form transformation laws.

There is no new diagonal fermion term proportional to the nonzero
D moment. Such a term occurs in the BOSONIC squared masses. The
fermion masses follow from W Hessian and gauge coupling even at a
stationary point with nonzero D. The same-action neutral lambda
parallel to Z is a zero-mode control: all displayed derivatives and
commutators vanish. Its norm is finite since the area is finite.
It is not removed by a bosonic gauge quotient.

The component mass structure agrees with Martin, A Supersymmetry
Primer, equations3.4.9 and7.1.3; only those structures and their
surrounding sections are used. The infinite-dimensional affine,
curved and complete-domain realization is our explicit derivation,
not a theorem attributed to that finite-dimensional example.
Source: https://arxiv.org/html/hep-ph/9709356v7.

## The exhibited isometries and their faithful action

Use the previous complex with C1 the physical A/Q/R tangent,
C3=E tensor K tensor barK, metrics
h0=Omega^2, h1=diag(1/2,Omega,Omega),
h2=diag(Omega^-1,Omega^-1,2), h3=2Omega^-2,
and T(x,sigma)=(D0 dagger x,D1 x+D2 dagger sigma).

The input and output maps are

    Uin(lambda,a,u,v)=((a,u,v), i*Omega^2*lambda/sqrt(2)),
    Uout(g,p1,p2,t)=(g,2i*t,p2/Omega,-p1/Omega).

The input map uses the metric volume form to identify the physical
scalar gaugino with the C3 bundle. It adds no degree of freedom.
The output map uses S tensor S=K, the metric and invariant E8 trace.
Thus its image is precisely the dual-conjugate fermion Hilbert bundle.
Their norms are the displayed physical norms term by term.

In coordinates the adjoint relation map is

    D2 dagger sigma = (
        (2/Omega)*[r dagger,sigma],
        -(2/Omega)*[q dagger,sigma],
        -Dz(Omega^-2*sigma) ).

Putting sigma=i*Omega^2*lambda/sqrt(2) gives, after Uout, exactly the
three transpose gauge couplings above. The Omega derivative cancels
inside Omega^-2*sigma; it may not be dropped before this substitution.
The D1 part gives the three W-Hessian rows. Therefore

    M=Uout T Uin

as actual operators, not only principal symbols, spectra or dimensions.
Both maps are unitary between their declared weighted bundles.
Tests check every matrix entry, wrong-phase/weight controls and the
variable-metric derivative. The relation even holds algebraically
off the commuting background, although then the complex identities
and subsequent index proof need not apply.

## Trace pairing and complete domains

For a charge-q coefficient representation, use the trace-dual
opposite-charge representation. Its background matrices are
Q_dual=-Q^T and R_dual=-R^T; covariant derivative transpose includes
integration by parts. In a frozen Fourier symbol p for Dbar, the
opposite momentum has p_dual=-p. The density mass matrices obey

    B_q(p)=B_dual(-p)^T.

This explicit transpose check differs from assuming a literal
self-duality inside one charge sector. It establishes that the
Hilbert adjoint kernel of M_q is anti-linearly the opposite-charge
left kernel. Hence, after dividing out the common gauge representation,

    ind M_R = number of left R zero modes
                      - number of left conjugate(R) zero modes.

A real adjoint in the higher-dimensional action does not supply a
second constraint identifying those independent four-dimensional
left coefficients. Nor are right antiparticles counted again.

The exhibited maps are smooth bundle isometries, map compact-support
cores onto each other, and satisfy the operator identity on those
cores. Their graph norms are therefore equal; they extend onto the
complete graph closures without a new boundary condition. Possible
unbounded coordinate factors at infinity are harmless only because
these are isometries between the ACTUAL weighted bundles.

The pinned two-neutral proof supplies both shifted end blocks and
all unpaired extremes, with squared thresholds at least1/4 through
the principal-field operator homotopy. Complete Dirac cutoffs and
local ellipticity give the same adjoint domains. Finite neutral c,d
are bounded decaying graph-compact perturbations. Thus M is Fredholm
on the same domain and its index equals that of T for every finite
c,d. This homotopy is not a family of stationary intermediate vacua.

## Full representation resolved index

The structure factor is the principal spin-two SO3 inside SU5_b,
and the faithful unbroken gauge group is S(U3 x U2). The parent248 is

    (24_g,1)+(1,24_b)+(10_g,5_b)+(bar10_g,bar5_b)
                             +(bar5_g,10_b)+(5_g,bar10_b).

The integer cocharacter Z has eigenvalues(-2,-2,-2,3,3) on5_g.
Using the actual color and weak Cartans, the positive-charge blocks are

| Z charge | Gauge representation | Internal principal module |
|---|---|---|
| 1 | (3,2) | V2 |
| 2 | (bar3,1) | V1+V3 |
| 3 | (1,2) | V1+V3 |
| 4 | (3,1) | V2 |
| 5 | (bar3,2) | V0 |
| 6 | (1,1) | V2 |

All negative-charge conjugates, neutral adjoints and both Cartans
are retained in the full root/tensor reconstruction. The q=5 block
comes from the gauge24; it must not be dropped because it is exotic.

For E weight m, beta=m+2nq. The COMPLETE cusp index of S^a is
J(a)=h(b(a))-h(b(2-a)), with b(a)=floor(a/2) for a<=0,
b(a)=ceil(a/2)-1 otherwise, h(D)=0 for D<0, h(0)=1,
h(D)=D for D>=1. The exact endpoint and global proof are pinned.

The physical index contribution per weight is now EARNED as

    I(beta)=2J(1-beta)-J(-beta)-J(2-beta)
           =0 at beta=0,
           =-sign(beta)*(-1)^beta otherwise.

An independent zero-Higgs kernel-minus-cokernel count has numerator

    h0(2+beta)+2h0(1-beta)+h0(beta)

and denominator

    h0(-beta)+2h0(1+beta)+h0(2-beta),

where h0(a)=h(b(a)). This retains all four physical Weyl slots and
their adjoints; it is not the old A/Q-only index.

The actual weight bound/parity proves the following all-integer
net multiplicities (not representation dimensions and not total modes):

| Positive charge | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---:|---:|---:|---:|---:|---:|
| n>=2 | -1 | 2 | 2 | -1 | -1 | -1 |
| n=1 | 0 | 2 | 2 | -1 | -1 | -1 |
| n=0 | 0 | 0 | 0 | 0 | 0 | 0 |

Negative n reverses all signs. A negative multiplicity denotes net
left-handed conjugates of the listed representation. The first-flux
endpoint is real, not rounded away. Unknown additional vector-like
pairs leave these indices unchanged. No actual full kernel count,
three-generation spectrum or wavefunction-overlap Yukawa is claimed.

This is conditional net charged chirality of the ACTUAL fermion
operator at a supplied stationary saddle. It is stronger than the
preceding bosonic index and weaker than an anomaly-free stable chiral
physical vacuum. Zero-flux SM gauge minima and their zero charged
index remain intact.

## Perturbative anomaly diagnostic and its exact scope

Use A(3)=1, A(bar3)=-1 for SU3 cubic traces and T(fund)=1/2
for both simple factors. Keep integer Z; conventional Y=Z/6 is a
supplied normalization label, not derived here.

For one representative of each conjugate pair with signed net
multiplicity nu, the coefficients are

    A333=sum nu*d2*A(color),
    A33Z=sum nu*d2*T(color)*q,
    A22Z=sum nu*d3*T(weak)*q,
    AZZZ=sum nu*d3*d2*q^3,
    AgravZ=sum nu*d3*d2*q.

The five expected coefficients for n>=2 are
(-3,-6,-6,-1008,-30), and for n=1
(-1,-5,-9/2,-1002,-24). Negative flux reverses them; n=0 gives zero.
Root-weight traces and a separate tensor construction calculate these
without reading a precomputed anomaly table. A known anomaly-free
generation and conjugate pairs are opposite controls. Dropping the
q=5 exotic or counting both conjugates without the compensating1/2
changes the result and must be detected.

The rule that these symmetric traces diagnose perturbative
four-dimensional gauge anomalies, and that vector-like pairs cancel,
is the use of Bilal, Lectures on Anomalies, sections7.1--7.2:
https://arxiv.org/html/0802.0634v1. No global-anomaly or noncompact
determinant theorem is inferred from those sections.

Nonzero traces mean that the finite zero-mode spectrum alone cannot
be gauged as a standalone four-dimensional quantum theory without
compensation. It is NOT yet a calculation of the regulated complete
noncompact parent determinant, end response or anomaly inflow. These
could change the physical completion, but their cancellation cannot
be assumed. R23's older local inflow explicitly retained the anomaly
of internally constant gauge transformations at its outer end;
it belongs to a different parent and supplies no free cancellation here.

Likewise, the bosonic saddle remains. Charged condensation, changes of
asymptotic data or an admitted end sector have not been solved or
excluded. Stability, anomaly completion and genesis selection are
separate obligations; a nonzero physical index discharges none of
them automatically. No observer, qualia or gravity identification.
