# Boundary laws and the scope of the cone completion

September 30, 2026. Path-local R60 pre-execution design and authored
argument. This advances PHYSICS_MISSION's boundary-law duty. It does not
select a new physical model or replace the full mission with an audit.

## Question and scope

Separate what B1504 proves about invariant self-dual cone completions
from what the supplied physical action actually requires. Quantify over
its real rank-one torus-link data and the smooth regulated boundary of
the adopted complex Chern-Simons superpotential. No family of physical
vacua, all boundary conditions, or full generated architecture is classified.

Prior: the finite lattice lemma and oriented LR/RL conjugacy survive.
The three-root restriction is valid for B1502's named smoothings, not
all ideal boundary lines. Self-adjointness is weaker than Poincare
self-duality. The action has a boundary variation needing additional
conditions, not a unique condition fixed by a marking alone. These are
authored deductions below; tests can expose algebra/sign/implementation
errors and are not independent analytic or physical verification.

## Reception and prior work

All origin heads were fetched on this date. B1504 is read at
ba41670beeb05b64e680ec3a3f0f822f842820fc, without merging it. Personally
read its complete findings, verdict, producer and tests; B1500's complete
findings and 689-line intersection-chain producer; and B1502 and B1396
findings. Their large censuses are NOT reverified here. B1500 computes
allowable-chain ranks over a finite field; it does not solve the physical
operator, metric, real-fermion boundary condition or supersymmetry.

The local ladder, framework, campaign, LAW_MAP and PB-BOUNDARY record
the same-action duty. R57 already distinguishes marked from unmarked
data and symmetric laws from symmetric vacua; R58 has a generic domain
countercontrol; R28/R37 treat other source variations. The fork's F02
already proves unique ordinary L2 closure for its smooth complete
operator. Reuse these, not rediscover them. The atlas remains early-epoch.
The already-banked query 'self adjoint self dual Cheeger cone boundary
marking Chern Simons' returned broad vocabulary hits, not a completeness
certificate. Source/code and old kill-graph lookups are navigation only.
No whole-repository absence or literature novelty is asserted.

Primary literature personally checked in the cited passages:

- Albin, Leichtnam, Mazzeo and Piazza, arXiv:1307.5473v3, introduction
  Theorems 1 and 2, equation 1.3, Lemma 5.1 and section 6.1. Under suitably
  scaled incomplete edge metrics their arbitrary mezzoperversity gives
  a self-adjoint de Rham operator. Poincare self-duality is an additional
  requirement; its dual uses the intersection pairing, not the positive
  inner product. https://arxiv.org/html/1307.5473v3
- Pantev and Wijnholt, arXiv:0905.1968v1, section 2.3, equations 2.25--27:
  the adopted complex Chern-Simons superpotential, kinetic pairing and
  moment-map potential. https://arxiv.org/html/0905.1968v1

Only those passages are used; this is not a claim to have read either
entire paper in this pass. Both accessed September 30. No theorem about
ordinary hyperbolic cusps follows merely by naming their compactification.

## What the finite symmetry theorem earns

For finite G in GL(2,Z), an element of order 3,4,6 has no real eigenline.
Otherwise every non-scalar element is a reflection. The product of two
reflections has determinant one and must be plus or minus identity, so
the reflections share their eigenlines. Thus a common real line exists
exactly when no such rotation exists. Check all subgroup subsets of D4
and D6 independently, using multiplication tables rather than B1504's
generation from at most two elements. The abstract finite-subgroup
classification is standard input, not proved by those finite checks.

With the EXTRA requirement that each self-conjugate sector uses a
Poincare-self-dual line, B1504's neutral-sector obstruction follows.
Preserve it. It does not classify all self-adjoint operators or symmetry-
breaking solutions of a symmetric action. The two orientation readings
and the physical identification of duality remain separate inputs.

An order-three matrix R=[[0,-1],[1,-1]] preserves H=[[2,-1],[-1,2]].
Its three shortest projective lattice lines have squared length 2.
The primitive line (1,3) has squared length 14 and another three-element
orbit. Every real line in a two-dimensional symplectic space is
Lagrangian. Therefore rotation alone cannot restrict a non-invariant
ideal boundary line to the three shortest ones. B1502's three specified
Bryant-Salamon smooth phases retain their own narrower restriction.

The identity L^-1(LR)L=RL, det L=1, correctly removes the order bit
from the unmarked oriented manifold. It forbids a nontrivial bit-only
choice REQUIRED to descend to that quotient. It does not show that
every physical boundary law factors through the quotient. A comparator
is a torus with retained ordered basis B: ell(B)=span(B e1) obeys
ell(gB)=g ell(B), although the unmarked torus has no distinguished line.
This is not a construction of an A7-dependent chiral law. Its purpose
is to require the physical marking/quotient decision explicitly.

## Two different dualities and two different metrics

Let V=H1(T2;R), with positive pairing H and intersection matrix J.
The doubled Cauchy data (alpha,beta) have Green form

    G((a,b),(a',b')) = a^T H b' - b^T H a'.

For ANY W in V, D_W=W direct-sum W^(perp_H) is a half-dimensional
isotropic subspace of this doubled form. In particular W=0 and W=V
are rotation-invariant and give such domains. In contrast Poincare
duality sends W to W^(perp_J); it interchanges 0 and V and fixes lines.
This directly distinguishes the two hypotheses. Real conjugation fixes
these real subspaces; identifying physical charge conjugation with an
operation also containing Hodge duality needs the actual fermion map.
We do not assert that either extreme satisfies the seven-dimensional
fermion reality condition, supersymmetry, gauge symmetry and interactions
together. That is the next physical test, not a proved counterexample
to B1504's stated self-dual category.

For rho in (0,1] and flat h on T2 compare

    g_cusp = d rho^2/rho^2 + rho^2 h,
    g_cone = d rho^2 + rho^2 h.

The end is infinitely distant for the first metric and finitely distant
for the second. For rho^p times a fixed tangential one-form beta, radial
L2 densities are proportional to rho^(2p-1) and rho^(2p), respectively.
A constant beta fails L2 on the cusp but passes on the cone. This is a
local norm comparison, not a global harmonic mode or particle count.
The same topological compactification therefore does not transport the
physical norm/domain. F02's complete-space closure is not contradicted.

## Boundary variation of the adopted action

On an oriented compact regulator M, use a complex matrix connection C,
invariant trace, outward Stokes orientation and a fixed coefficient c:

    W_bulk = c integral_M tr(C wedge dC + (2/3) C wedge C wedge C),
    delta W_bulk = 2c integral_M tr(delta C wedge F_C)
                   - c integral_boundary tr(C wedge delta C).

The identity follows by the graded Leibniz rule and cyclic trace. Verify
it independently with polynomial noncommuting 2 by 2 matrices in three
coordinates; a wrong boundary sign and an omitted cubic must fail.
This classical variation is not the full real action, a quantum level,
an anomaly calculation, or permission to discard the other fields.

In an abelian, constant boundary chart C=u dx+v dy, with unit coordinate
area, the boundary one-form is theta=c(v du-u dv). Adding the boundary
term c*u*v changes it to 2c*v du. If u is freely varied, an additional
specified potential U(u) gives the stationarity equation

    2c*v + U'(u) = 0.

For c=1 and U=k*u^2 this is v=-k*u; distinct k give distinct graph
conditions in the SAME marked chart. The field-space two-form is
d theta=-2c du wedge dv, unchanged by these exact counterterms. Its
pullback to each graph vanishes. These are local classical polarization
examples. They are NOT asserted globally gauge-invariant under large
transformations, supersymmetric, anomaly-free or physical cone domains.
The action determines the boundary symplectic structure in this chart;
the marking does not by itself choose the boundary functional.

## Execution and acceptance

Seal this design, the independent producer, tests and pinned input
manifest, commit/push and confirm the remote before first execution.
Native checks cover the subgroup census, the non-root orbit, marked
equivariance, Green form versus Poincare duality, metric weights, full
nonabelian variation and distinct graph stationarity conditions. Include
explicit wrong-sign, wrong-domain and wrong-metric controls.

Replay only the unchanged foreign lattice lemma, with its source hash
checked; do not call its census or record writer. Run new tests with the
seven R59 tests. Capture complete output and actual exits in exclusive
files; preserve any first failure. No empirical comparison occurs here.

A pass earns these conditional distinctions and the boundary variation,
not a derived physical end law or a global chirality result. Next derive
the actual twisted-fermion reality/supercharge action on the boundary
data in the SAME parent, then test the admitted bosonic and fermionic
domains and interaction maps together. Do not choose a desired index
before this admissibility test. Do not repeat B1504's large census to
avoid confronting its physical identification hypothesis.
