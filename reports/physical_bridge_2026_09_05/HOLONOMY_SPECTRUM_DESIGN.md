# R19: flat holonomy, the extra pair, and the anomaly obligation

2026-09-08. Pre-execution design; path-local R19, no global B allocation.

BANKED IDENTITY: first reproduce the actual m202 relator and the SM
seat's B1282 Alexander polynomial, pinned at d1a91c7a, using its
`verification/siblings_faces.py::alexander_m202` function. Independently
reuse B787's group-ring Fox engine and triangular cocycle multiplication.
Reuse R15's actual E6-adjoint computation and R18's weighted maximal
complex. B864 already computes the anomaly of a charge-one Spin(10)
spinor. Its anomaly-free full 27 is a different representation; its
normalization must be matched, not imported by the word "E6".

PRIOR ART: Dyer--Vasquez, *Some small aspherical spaces*, Theorem 2.1
and the discussion of Lyndon's identity theorem, pp. 337--338,
https://doi.org/10.1017/S1446788700015147 (primary text read).
Pantev--Wijnholt, https://arxiv.org/pdf/0905.1968, sections 3.4, 3.7
and the flat-line-bundle discussion (3.85)--(3.86), already discuss
inflow and the effect of gauge holonomy on matter. No novelty claim
for that mechanism. SnapPy's primary documentation specifies its
multivariable Alexander and fundamental-group routines:
https://snappy.computop.org/manifold.html. Accessed 2026-09-08.

## Grounding and outcomes

P0: R18's complete finite-volume sourced hyperbolic class, with positive
endpoint density on every cusp and all effective line strengths >=1,
now equipped with a unitary rank-one flat local system pulled back
from the undrilled core Q. For the numerical topology label Q is m202.
The gauge connection is in the SAME compact E6 Cartan direction u as
the prescribed Higgs field, and commutes with it. Its adjoint charged
sectors see characters chi and chi^-1. New drilled meridians have
trivial holonomy because the system extends across the source arcs.
Original cusp peripheral loops need not have trivial holonomy.
This is a larger declared-background class, not an object-selected
connection, parent, source, domain, geometry or theory of everything.

P1/P4: PB-BOUNDARY / X33. R18 settles its W=0 strong maximal complex
as four/one, with an extra pair. Test whether that pair persists for
nontrivial holonomy, without discarding the fixed source construction.
Rank preservation by commuting Wilson lines (B953/B955/B956) remains:
changing charged cohomology is not reducing the gauge rank.

P2/P3: the design-time bank queries included "Wilson line chirality",
"m202 Alexander", "twisted source cohomology" and "Spin10 U1 anomaly".
Read B953, B955 (including its B1240 addendum), B956, B1089, B1096,
B864 and their pertinent producers, plus the actual B1282 addendum and
producer on the SM pin. The atlas is epoch-blind (1161 arcs). The
eleven-head lexical sweep is PRESENT, including B1282. Its deleted
history check searches path names, not exhaustive deleted content.
No absence/novelty claim. HOLONOMY_SPECTRUM_PRIOR.md records the scope.

CC's reservation relay and SM alias specifications were read on fetched
main c78003cd. Other inspected head pins: physics 659487bb, SM d1a91c7a,
outside 6c7aaba6, advancing to 8a5d6e6f at the completed pre-seal refetch
(incoming Cardy/tail work routed in the prior receipt). Only this audit
branch is changed. A path-local R19
does not consume any reserved B1284+ number or another seat's R19.

P6 positive: expect generic unitary holonomy to give (0,3,0,0) for the
positive sector, and (0,0,3,0) for its negative/conjugate sector. Expect
trivial holonomy AND the nontrivial Alexander zero locus to retain
(0,4,1,0) and its reverse. Those are positive and failure controls of
the same mechanism, not a claim that every nontrivial holonomy works.
If these fail, preserve the exact failing character/matrix/domain
step. Do not kill the larger sourced route. Expect the net-three extra
U(1) anomaly to persist in both spectra, absent added completion.

## Analytic extension that must accompany the matrix calculation

Write the unitary covariant differential as d_A and d_(A,H)=d_A+dH wedge.
Multiplication by exp(H) identifies its canonical maximal complex with
the d_A complex weighted by exp(-2H), just as in R18. The bounded real
corrector still changes norms by equivalent factors. On a radial
product collar, parallel transport is unitary and puts a flat connection
in radial gauge, with tangential connection independent of radius.
The R18 radial homotopies therefore work fibrewise with precisely the
same norm bounds. They commute with the covariant tangential complex.
The full punctured-torus construction, weak trace argument, averaged
regular-slab projection, corner order and compact-core closed-range
argument are retained; no angular cutoff at infinity is added.
Compact mixed-boundary de Rham theory applies to a smooth unitary flat
bundle by parallel local trivializations. Thus the candidate groups
are H*(C,T;L_chi) and H*(C,E;L_chi^-1), with the same amplitude/domain
conditions as R18. Neither a finite matrix nor an Euler characteristic
alone proves this analytic comparison.

Let N be k disjoint D^2 x I source neighbourhoods in Q, C their exterior,
and T the lateral annuli. Excision gives (C,T) the cohomology of (Q,N).
N is a union of contractible components, and a flat line on Q restricts
trivially to it. For k>0 restriction on H0 is injective. The exact
sequence gives

 b(C,T;L) = (0, k-b0(Q;L)+b1(Q;L), b2(Q;L), b3(Q;L)).

There is no extra assumption about primitive arc-intersection vectors
in THIS relative formula. The old absolute-exterior calculation had
additional hypotheses; it is not silently being used here. Complementary
boundary Poincare--Lefschetz duality reverses the degree vector while
dualizing the line system. k=0 is a separate full-base control.

## Exact full character calculation and tests

1. Obtain m202's presentation from SnapPy and assert it is <a,b | R>,
   R=aabbAbAABBaB, with exponent sums zero. Verify cyclic reduction and
   every possible period of R; reject a proper-power control. The
   one-relator asphericity theorem then makes its presentation complex
   a K(pi,1), as is the hyperbolic core. This discharges the otherwise
   missing degree-two link between a presentation and manifold cohomology.
   A separate Sage run tests interval hyperbolicity and native Alexander.
   It does not certify source-line geometry or the whole physical model.
2. For a->x, b->y derive delta0=(x-1,y-1)^t and the Fox row delta1.
   Expect P=x^2*y+x^2+x*y^2+x*y+x+y^2+y,
   Fa=-(y-1)*P/x, Fb=(x-1)*P/x. Check nilpotence symbolically and
   compare the pinned B1282 function (its polynomial is -P).
   A triangular-matrix cocycle implementation supplies a second method.
3. A cochain mapping cone for (Q,N) has ranks (1,2+k,1,0), differential
   d0=(x-1,y-1,t1,...,tk)^t and d1=(Fa,Fb,0,...,0), where the ti are
   unitary fibre identifications. Compute all ranks exactly. Compare
   independently with the long exact sequence formula, all degrees,
   k=0,1,2,3 and nontrivial ti. Never read an index as a total count.
4. On |x|=|y|=1, P/(xy)=|1+x+y|^2-2. Derive this identity and inversion
   invariance. Prove the rank classification symbolically for the whole
   character torus, then use exact controls: all characters of orders
   dividing 2, 3 and 4, and both diagonal roots of 2z^2+3z+2. These finite
   grids are controls, not a census or an object-selection principle.
   Nonunitary inputs are rejected for the weighted analytic conclusion.
5. Exact local all-degree covariant homotopy and weighted-conjugacy
   identities, curvature and missing-Fox-term mutants. Re-run the R18
   tests; they are component controls, not independent review of the proof.

## Gauge interpretation and anomaly test

Use R15's E6 root lattice and u=omega_1^vee; charged ADJOINT roots have
u charges +/-1, with two 16-dimensional D5 orbits. Generate the actual
fundamental 27 as a Weyl orbit too. Verify all weight charges, D5 trace
ratios and the distinction between adjoint and 27 charge units.
In simply connected E6, u is not itself a cocharacter: 3u is. Check
this integrally. A character (-1,1) is realized by rho(a)=exp(i*pi*u),
rho(b)=1, with parent order 6 rather than adjoint order 2. Abelianizing
the relator makes this a genuine group representation, not just root
phases. The choice remains external and preserves the Higgs commutant.
It is not claimed to preserve every source-permuting isometry. Also
compute the peripheral exponent matrix of the actual presentation. If
its rank is two, every nonzero infinitesimal abelian holonomy change has
a nonzero cusp period and is not L2 in the canonical metric (R13).
Verify the contrasting constant 0-form and constant cusp 1-form radial
norm integrals. F_A=0 does not make a Wilson modulus normalizable.

Compute Tr(u), Tr(u^3) and the Spin(10)^2-u coefficient from the actual
weights for four/one, three/zero and one/one. In the normalization
T(10)=1, expect (48,48,6) for either net-three spectrum, and zero for
one vectorlike pair. Verify pure D5 cubic traces vanish. Reproduce
B864's full-27 zero after matching its psi=3u normalization; adding
an anomaly-free complete 27 cannot cancel a pre-existing nonzero
anomaly. Do not claim the SM hypercharge itself is anomalous, and do
not repeat uniqueness of Y over a 16 (the old 15-field restriction
excludes the right-handed neutrino).

The canonical 7D gauge action on finite-volume Q gives the commuting
constant gauge mode a finite internal norm. Its extra U(1) cannot just
be called nondynamical by importing a different local model's boundary
conditions. Actual defect/inflow terms, or a derived massive/non-gauged
U(1) realization, remain necessary. Pantev--Wijnholt already discuss
these mechanisms; their existence in the literature is not this
program's completion. Holonomy removes zero modes in a changed operator;
it does not calculate their physical masses or generate a mass term
inside the unchanged W=0 complex.

Seal this design, both instruments, tests and prior receipt before
execution. Verify literal provenance fields and digests before the first
scientific run, preserving the older global-gate debts. Preserve all
failures; repairs require new files and seals. No tree edits while a
scientific or certifying process is live. Independent review and full
repository banking remain unpaid unless actually completed.
