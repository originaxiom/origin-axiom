# X-FRONTIER source review and physical continuation

2026-11-16. PHYSICAL-C5. Reviewed AGY-exp at
af08bc3d272c01a85e7341da91cfcc43d230d64c, following the PHYSICAL-C4 review.
The fresh fetch found twenty new commits on the loop branch. Other
advertised scientific branch heads matched the preceding review receipt.

All five X-FRONTIER result relays were read personally. Deciding source
ranges are recorded in SOURCES.json. This is a targeted source and hand
review. Scientific scripts and tests were not executed, imported or
collected. Upstream JSON values below are received outputs. Their hashes
and source files are checked separately from their mathematical coverage.

## C5-01. Preserve the finite algebra and its recovery controls

X-FRONTIER-1 retains useful symbolic quartic identities, E6 root-centralizer
enumeration, core-character and reflection-order controls. The scalar
forced-tail and boundary-momentum identities have the expected hand
derivatives. Its heavy relaxation example builds a six-dimensional
Hessian with prescribed null vectors. It illustrates the projected-square
argument. The actual physical kernel, source adjoints and complete inverse
retain the earlier physical proofs' review duties.

X-FRONTIER-2/3 also contain real Clifford, extreme-weight and cyclic
contraction work. These can help independent verifiers check the finite
representation algebra. A root/Clifford test and an actual complete-cusp
spectral theorem have separate source and domain requirements.

## C5-02. The light coupling calculation changes the metric input

X-FRONTIER-2 lines 183–265 choose tau=i sqrt(3) and the periodic density

    Omega=1/[R(1+|log R|)],
    R=exp[-pi (Im z)^2/Im tau] |theta1(z)/theta1'(0)|.

The source checks periodicity and cusp asymptotics. It does not exhibit
the parent metric's uniformization, its marked curve identification or
an error bound for replacing that metric by this density. Thus its
reported 1.797167999678669 and 1.5505138991551968 are comparator outputs
until that physical identification is earned.

There is a further concrete quadrature omission. The polar region stops
at T=18 for both compared grids. METRIC_TAIL_AND_NORMALIZATION.md derives
the omitted area asymptotic 2pi/(T+1+log 4), with an exponentially smaller
remainder whose constant needs bounds. The same-cutoff grid comparison
cannot detect that area. The ratio of the two couplings cancels this
common area factor, so the area finding alone leaves that ratio open.
The ratio still inherits the metric and remaining quadrature duties.

Requested repair is the actual metric/frame map plus complete norm and
tail error controls. The source's useful rank-one cubic and nonzero
gauge-coefficient tests are retained.

## C5-03. Two-cell moment response tests a finite comparator

X-FRONTIER-2 lines 361–448 use 4-by-4 nilpotent matrices on two cells,
a compensating assigned F0 curvature and a hand discrete Laplacian.
Lines 477–497 solve six scalar variables. This gives a useful nonlinear
moment recovery control. There is no surface-refinement limit or actual
global connection reconstruction in that function. The upstream scope
note correctly retains the infinite-dimensional inverse estimate.
Its assertion that the comparator realizes every physical hypothesis
needs the same qualification.

The vector-mass control at lines 499–508 evaluates the raw first-order
form pair at rho=1, before its solved nonlinear response. It correctly
recovers the leading coefficient 4 e_Q^2 t^2. It does not establish an
exact all-amplitude physical equality. The physical proof explicitly
retains O(t^3).

## C5-04. The mass coefficient shares unverified geometric inputs

X-FRONTIER-3 lines 269–368 use the same chosen metric and a single
16-node norm quadrature. Its Bloch inverse is then refined on grids
16,24,32. The two-route residue agreement is a useful holomorphic-map
control for those common inputs. The Gram metric is shared and its
quadrature stays fixed, so that agreement cannot certify the physical
normalization or its stated narrow interval.

The received JSON reports sigma_2/sigma_1 about 2.44e-11. A small computed
singular value alone does not certify exact rank. The earlier physical
connecting-map proof can supply a conditional exact rank-one theorem
under its global sheaf and complete-domain hypotheses. It must be
verified on its own terms. The numerical computation does not replace it.

The good-sign dbar residual is recorded at lines 490–506 and 560 but
is absent from the success predicate at lines 538–548. The bad-sign
residual is included. A repair should require the proposed physical
map's own residual to pass a declared tolerance with convergence or
analytic bounds. A two-point extraction of holomorphic coordinates also
needs a global error check. This observation concerns the gate's
coverage, and does not claim the recorded good residual is large.

The reported decimal coefficient and exact rank therefore have different
earning duties. The fixed source sqrt(2), zero on either single axis,
and the constructive Fourier/residue comparison are retained.

## C5-05. The cross-form completion is promising and scoped

Lines 636–647 construct a polynomial dressing of the highest cross-form
and test its commutators with both cyclic Higgs matrices. This is a
constructive pointwise candidate. Lines 678–686 stop the finite
homological perturbation sum at k=4. CROSS_FORM_FINITE_SERIES.md derives
a weight-filtration nilpotence certificate that can justify this stop
under the specified contraction and weight identities. This preserves
the local algebraic opportunity.

Global b(z), complete-domain behavior, the coupled real moment response
and the actual induced cohomology map remain to be earned. The source's
rank-two 3-by-3 example at lines 719–723 assigns its zero row and column.
The endpoint comparator at lines 725–730 inserts eps_end=1/5. That
matrix control shows the consequence of a nonzero entry. It does not
derive a physical endpoint change or its coupling. Uniqueness is limited
to the displayed ansatz until a broader classification is supplied.

## C5-06. The joining solver uses a supplied scalar potential

X-FRONTIER-4B lines 2515–2608 solve the scalar functional

    integral [(c')^2+m_Q^2 sin^2(c)] dx.

The caller uses m_Q=2 at line 3108. The function has no E6 field
embedding X(c), no actual Gauss operator or gauge response, no source
quartic and no full normal residual. Its interior collocation residual
checks this scalar ODE. The whole-line kink c=2 arctan exp[m_Q(x-x0)]
has action 4m_Q, explaining the reported action near eight.

A physical completion needs the field embedding and its kinetic and
potential integrals to yield that scalar action, then must solve the
orthogonal equations. The existence of a Higgsed vector mass alone
does not supply the sine-squared scalar potential. SAME_ACTION_END_RESPONSE.md
derives an alternative boundary response from the existing path action,
retains real Gauss and gives the exact missing normal equation.

Its charged stationary-family control also shows why a local zero-
potential branch can coexist with a nonzero vector mass. This prevents
converting that mass into a wall barrier without a field calculation.
It does not rule out a stationary interface with justified source data.

## C5-07. Preserve the first failure and the inherited correction duty

The original X-FRONTIER-4 JSON has stage_4_gate_passed=false and a failed
Part 4A gate. The successor changes the indentation of the selected
minor loop and reports stage_4b_gate_passed=true. Both outputs and
source hashes are preserved. The successful successor's scalar wall
results match the original output. The loop repair cannot change their
physical scope.

The source still carries -24 lambda^2 y2_tr at lines 286 and 1005 of
the 4B verifier. PHYSICAL-C4 finding F12 gives the source-convention
countercheck requiring -48 for its ln(mu) convention. The repaired
mixed Yukawa product is a separate positive. The name of an aggregate
gate does not discharge this remaining term.

## What this review contributes

The new author proofs supply three bounded additions. They give the
missing cusp-area tail and a metric-sensitivity identity, a finite-series
certificate preserving the cross-form algebra, and a nonlinear end
response plus full normal equation from the actual gauge-reduced action.
They reuse existing physical proofs and standard variational methods.
All three require independent review. No foundational input has been
counted removed, and no complete stationary interface, three-generation
physical spectrum or gravity closure is claimed.
