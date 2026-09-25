# R45: parent gauge kernel and the end sectors that remain

September 25, 2026. Authored application, frozen before finite tests.
External density theorem and R44's authored global argument are inputs;
neither becomes independently certified by the controls in this packet.

## 1. The same parent, with the actual coefficient

Reuse R39's explicit root map, not a new dimension match:

    248=(45,1)+(1,15)+(10,6)+(16,bar4)+(bar16,4).

The connection is R42/R44's actual real defining SL4 coefficient E,
possibly tensored with a flat scalar line chi in mu4. The five
coefficients are respectively 1, End0(E), exterior-square(E), E*, E.
The twists on them are 1,1,chi^2,chi^-1,chi. The complete positive
metric is induced from the canonical H and an invariant compact E8
metric. All local harmonic-flat equations survive the Lie embedding.
The whole adjoint Higgs norm is sixty times the defining trace norm
(R39's full-Cartan identity), so R44 supplies finite total Higgs norm.
This remains a supplied classical parent on a supplied product spacetime,
not a solution of four-dimensional gravity or a derived quantum action.

Do not confuse two rank-four inputs: R39 used holomorphic Sym3 of
SL2; R42/R44 use the real projective four. At q=1 the latter is the
SO(3,1) vector representation, not Sym3. Its meridian has a size-three
nilpotent block, whereas Sym3 has size four. R39's extra wedge singlet
and so(11) are therefore not data that can be carried into this family.

## 2. Full global gauge kernel

Ballas--Long (2015), Theorem 4.3, establishes Zariski closure SL4(R)
for this actual family at t!=1/2, with q=2t>0. The parameter match and
literal matrices are fixed in R42/R44. Complexifying its Lie algebra
gives sl4(C). Passing to the kernel of a finite scalar twist preserves
this connected Zariski closure. Therefore invariant vectors in every
algebraic coefficient equal sl4 invariants. Their dimensions on
4, dual4, 6, 15 are all zero, checked by explicit Lie-action kernels.
Only the (45,1) summand has global flat invariant sections.

In the supplied compact parent, a vector zero mode has positive form

    Q0(s)=integral (|d_A s|^2+|[Psi,s]|^2).

A zero has both terms zero, hence is flat for D=A+Psi; it belongs
to the 45 just identified. Conversely these commuting compact so(10)
generators are parallel for A, commute with Psi, and have constant
positive norm. Finite volume makes them L2. Complete-space cutoffs
with bounded gradient tending to zero approximate them in the form
norm, so they lie in the natural closure. The compact-real kernel is
exactly so(10), dimension 45. This identifies its inherited bracket,
not merely a 45-dimensional vector space. No assertion about a full
disconnected gauge group or its quotient is needed here.

The density and finite-volume inputs also persist under finite covers.
Extra boundary breaking, defects, a different physical domain or a
different parent action change the problem and are not excluded.

## 3. All end weights and their actual operators

In R44's frame the induced connection on a representation r is

    Bx=r(N)/sqrt(R), Bt=k r(D)+beta r(P)/R, BR=r(J)/R.

The Lie homomorphisms preserve ALL flatness equations, including the
radial ones. The whole E8 longitudinal weight multiplicities are

    weight:  -4 -3 -2 -1  0  1  2  3  4
    count:    3 16 30 48 54 48 30 16  3.

The zero space is 45 trivial coefficients plus nine in End0(E).
The 194 nonzero directions split into invariant END subbundles:
r(D) commutes with r(N), r(P), r(J). These weight subbundles need
not extend over the compact core. In particular they are not
independent globally chosen matter fields or gauge factors.

On a nonzero summand and longitudinal Fourier frequency omega,
A=i omega+k r(D) has a bounded inverse. Since r(P) is nilpotent
and commutes with A, the inverse of T=A+beta r(P)/R is the finite sum

    T^-1=sum_j (-A^-1 beta r(P)/R)^j A^-1.

The actual induced positive norms are uniformly comparable with fixed
ones by R44; partial_t is bounded. Thus i_t T^-1 is a bounded full
end contraction on these summands. R44's radial/Cartan identity and
complete-domain cutoff proof apply, also to the entire 6 coefficient.
This identifies its L2, compact and ordinary cohomology but does not
compute their dimensions. On the full adjoint the zero weights remain,
so this is not a contraction of the entire parent complex.

Every induced Hodge--Dirac operator has the complete smooth natural
closure: the cutoff commutator is Clifford multiplication by dchi,
and local Friedrichs regularization applies. This gives a domain,
not automatically Fredholmness, a gap or cohomology comparison in the
zero sector. None of those is inferred from the nonzero-sector inverse.

## 4. Zero weight is a concrete peripheral complex, not a global kernel

Let V3=span(e0,e2,e3) and L=span(e1). The zero adjoint weight space is

    W0={diag_on_(V3,L)(X,a): tr X+a=0}, dimension 9.

On it the meridian and longitude logarithms act as ad(N) and
beta ad(P). N is the regular size-three nilpotent on V3, P=N^2.
The common kernel is span(D,N,P), dimension three. For example an
endomorphism commuting with regular N is a polynomial in N on V3;
the scalar on L is fixed by the trace constraint. Conversely all
three displayed matrices commute with both logarithms.

The longitude alone has kernel dimension five: on V3, P has Jordan
type (2,1), whose commuting endomorphisms have dimension five, and
the extra scalar/traceless constraint cancel. It has rank four on
W0 and is nilpotent. In particular it is not invertible at zero
longitudinal frequency, despite k!=0 in the defining coefficient.

The torus Koszul complex is

    W0 --(ad N, beta ad P)--> W0+W0
       --(-beta ad P, ad N)--> W0.

Both differentials have rank six, so its cohomology dimensions are
(3,6,3). Finite controls compare this logarithmic complex with the
actual commuting exponentials, not only the Euler count. The other
six adjoint weights are torus-acyclic. Consequently the COMPLETE
parent torus cohomology has dimensions (48,96,48), adding the
(45,90,45) from the trivial gauge coefficient. These are local
peripheral groups, not 48 global vector modes or 96 particles.

Radial transport is essential even on the invariant subspace. In
the actual comparison frame, the three cusp-flat sections are

    D, R^(-1/2) N, R^(-1) P.

They solve every covariant derivative, not just the tangential ones.
Their squared norm-volume powers are respectively R^(-3/2),
R^(-5/2), R^(-7/2); all are integrable on a tail. None extends to
a global adjoint flat section by section 2. They directly prevent
using the defining-sector contraction on the whole end: a degree-zero
closed nonzero section cannot be contracted by a degree-minus-one K.

Even the trivial coefficient distinguishes meridian and longitude:
dt is L2 on a tail, while dx is not, since |dt|^2 is bounded and
|dx|^2 is comparable to R. No global H1 count follows. The remaining
neutral/adjoint H1 problem must use the complete radial operator and
global matching, not plain torus dimensions or Euler characteristic.

## 5. What has and has not been paid

Subject to the cited inputs, the same classical parent has finite
Higgs norm, a complete specified fluctuation domain, exactly so(10)
vector zero modes, and the received exceptional paired spinor-sector
H1 modes. The extra 6 and the zero-weight sectors are explicitly
retained, not declared empty. Neutral H1, parameter kinetics, full
interactions, selective mirror removal, anomalies and gravity are
not computed here. This is neither a chiral vacuum nor a TOE.

Source: Ballas--Long, Algebraic & Geometric Topology 15 (2015),
3009--3022, especially Theorems 2.1 and 4.3 and the appendix:
https://msp.org/agt/2015/15-5/agt-v15-n5-p16-s.pdf . The full article
was read at R43; section 4 and the parameter identification were
reread personally for R45. The published proof is an external input.
R39, R42, R44 remain the frozen in-repo mathematical predecessors.
