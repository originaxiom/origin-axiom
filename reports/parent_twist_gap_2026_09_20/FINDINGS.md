# F05: gauge reduction works; the same background still has no spinor zero modes

2026-09-20. Local branch `audit/fork-2026-09-20`. Scientific design, proof,
producer and tests were sealed and committed at `dad3bd3a` before their
first execution. This is a conditional classical-parent result, not a
Standard Model, physical chirality solution, observed mass or TOE.

## Result and why it changes the next question

The report-guided sweep has now joined three previously separate inputs:
R39's actual noncommuting geometric background, R27's geometric positivity
mechanism, and F02's complete-space operator domain. The useful positive is
a **global order-four Wilson-twisted version of the same classical background
whose unbroken compact Lie algebra is so(10), instead of so(11)**. Its local
field equations and finite Higgs norm are unchanged. Its defining-four
coefficient representation is genuinely non-isomorphic to its dual.

But the positive-metric coefficient operator still satisfies

    Delta_C >= 9/4,    |Q| >= 3/2,    Q=d_C+d_C^*,

in curvature-length-one units on its ordinary bulk-L2 domain. In particular,
**neither the 16 nor conjugate-16 sector has a normalizable zero mode in
this background**. This is stronger information than an equality of two
unknown kernels. It is not a new universal vanishing theorem: the standard
Matsushima--Murakami mechanism was already banked, and here its normalization
and physical-operator match are made explicit.

The resulting distinction is operational: changing the global gauge algebra
and removing a displayed self-duality do not by themselves create matter.
A continuation seeking chiral matter must produce a full background/operator
that can close the gap, then compute its whole spectrum and interactions.
This is not a no-go for different nonsplit, sourced, singular or quantum
constructions.

## 1. Credit and recovery before extension

R39 is now available as a sealed and executed result at local Git object
`8d2cced21cc63772828458fb842e0280513b2f29`, with scientific seal
`ce48016a5b592f625cf71babc4f65cb3bb51543a`. Its six scientific files are
unchanged since that seal. Ten extracted source files were compared byte
for byte with the pinned Git objects; its **16 unchanged tests pass** here.
This supersedes the earlier audit's then-correct classification of R39 as
an unsealed proposal. That historical receipt is not rewritten.

R39 already supplies the homogeneous full BPS background, its global
descent, positive norm and enlarged so(11) centralizer. It also identifies
the failure of treating its scalar flag components as independent physical
spectra. Those are inputs, not missing tasks rediscovered in F05. R27 and
B1420 already distinguish geometric vanishing from self-duality, and B1364
already uses order-four Wilson data in a different construction. F05 makes
no general novelty claim for Wilson lines or geometric cohomology vanishing.

[Reception receipt](R39_RECEPTION.json) and [execution details](RECHECKS.md).
Fresh remote-fetch attempts failed through DNS/authentication. The available
pin was inspected; this is **not** a claim that every branch is now current.

## 2. The positive construction uses the same local action and equations

Choose the existing geometric SL2 lift h and a central character
chi:pi1(m004)->{1,i,-1,-i}. The documented marking allows

    chi(a)=1, chi(b)=i; chi(mu)=i, chi(lambda)=1.
    V_chi = Sym^3(h) tensor L_chi.

The relator, marked peripheral values and determinant-one restriction were
checked exactly. A unitary flat line has parallel unit frames locally;
therefore the existing connection C, compact connection A and Hermitian
Higgs field Psi are unchanged on each patch. The constant central phases
give globally consistent SU4, hence candidate-parent E8, transitions.

The complete E8 branching is retained:

    248=(45,1)+(1,15)+(10,6)+(16,bar4)+(bar16,4).

The extra ten locally parallel gauge generators in (10,6) acquire chi^2,
whereas the D5 generators remain globally parallel. Removing the ten short
B5 roots while retaining its forty long roots and rank-five Cartan gives
compact so(10), not just a dimension count. No global quotient of Spin(10)
is asserted.

The old invariant antisymmetric pairing acquires chi^2 and is not global.
A nonzero exact trace of the b holonomy distinguishes V_chi from its dual,
so non-self-duality is not inferred from literal inequality of two matrices.
An order-two twist retains both that pairing and the extra gauge line, as
a comparator.

The character, parent and background are still supplied choices. This is
a valid same-action construction, **not their dynamical selection**.

## 3. The matter operator, including its actual positive metric

In the R39 curvature-minus-one convention the orthonormal Higgs matrices are

    S=((E+F)/2, i(E-F)/2, H/2),
    E_superdiag=(sqrt(3),2,sqrt(3)), H=diag(3,1,-1,-3).

The full covariant tensor derivative of Psi vanishes, using both the compact
connection and Levi-Civita connection. That is what cancels the mixed terms
in Delta_C=Delta_A+H_p, with H_p=T*T+TT*, T=Psi wedge. Delta_A is its
nonnegative connection Hodge Laplacian, not an unqualified rough Laplacian.

| Form degree | Exact eigenvalues of H_p (multiplicity) |
|---|---|
| 0, 3 | 15/4 (4) |
| 1, 2 | 9/4 (6), 19/4 (4), 25/4 (2) |

Characteristic polynomials, Hermiticity, positivity and a separate block
formula agree exactly. F02's complete-space graph-core argument extends
the compact-support inequality to the unique ordinary-L2 self-adjoint Q.
It applies to V_chi and its dual separately. Flat unitary tensor factors
preserve the local estimate mathematically, even with infinite image; only
the stated scalar-center twists have this rank-four parent realization.

The adopted primary action identifies massless charged fermions with these
harmonic coefficient forms before making the commuting-Higgs restriction.
This was checked in Braun et al., section 2.3, equations 2.34--2.44. Its
wave-equation normalization includes a factor of two multiplying Delta;
therefore **3/2 is not quoted as a physical four-dimensional particle mass**.
The absence of zero modes is unaffected by a positive overall normalization.
For curvature length ell the mathematical Delta bound is 9/(4 ell^2);
no sharp spectral bottom, physical ell or mass hierarchy was computed.
[Primary action](https://arxiv.org/html/1812.06072v2).

The positivity identity is standard; its geometric use and compact-support
argument are independently documented in Menal-Ferrer--Porti, sections
2.1--2.2. The nontrivial-representation qualifier and their normalization
must be retained. Our constants come from the explicit matrices above.
[Primary mathematical source](https://arxiv.org/html/1001.2242v2).

## 4. The removed gauge modes also have an operator check

On the invariant exterior-square line, Psi acts as zero and the remaining
connection is the flat unitary line L_(chi^2). It has meridian holonomy -1.
The shifted cusp dual lattice excludes zero, giving

    q_end(u) >= kappa exp(2R) ||u||^2_end,  kappa>0.

Uniformly small tails and compact-core Rellich compactness imply compact
resolvent for this scalar operator. A zero mode would be parallel, which
the nontrivial line forbids. Its bottom is therefore positive. This removes
the ten extra gauge directions from the normalizable zero sector, rather
than just omitting them from a roster. Its numerical bottom is not computed.
The assertion is specific to the nontrivial cusp character; it is not
transferred to a character trivial at an end.

The exact non-square torus metric used in the finite control is a reference
example, not a fitted or certified normalization of m004's cusp metric.
The written shifted-lattice argument covers any fixed positive cusp metric.

## 5. What a next background must actually change

For a fixed metric and unitary identification of the Hilbert spaces, let
Q'=Q+B with bounded self-adjoint zeroth-order B. If ||B||=b<3/2, then

    ||Q'u|| >= (3/2-b)||u||.

Such a deformation cannot create a massless mode, regardless of whether it
removes a pairing. Crossing that bound is **necessary, not sufficient** in
this perturbation class; it neither produces a BPS solution nor guarantees
chirality. Topology or metric changes, unbounded end behavior, singular
sources, different domains and interacting quantum phases require their
own analysis and lie outside this comparison.

A nonparallel-Higgs oscillator control has a genuine zero mode: its mixed
term does not vanish. Thus the proof itself contains a check against turning
the geometric result into a universal statement about all Higgs backgrounds.
F01--F04's nonsplit m010 bundle is also a different object, not excluded by
this geometric-operator calculation.

The next priority is a **compatible background and gap-changing mechanism**:
reuse the existing source proposals, compute their actual full-parent
representation-valued current and fermion operator, and retain all partner
and core modes. A scalar source trial, a chosen boundary index or another
twist census is not a substitute. A credible continuation must then pass
the anomaly, vacuum, Higgs/exotics, interaction, scale and gravity gates in
one model. None of those gates is declared complete here.

## Verification and mission status

- **24 new exact tests passed** on the first sealed execution.
- **62 unchanged F01-v2/F02/F03/F04 tests passed**; one optional GUI warning.
- **16 unchanged R39 tests passed** in its pinned extracted snapshot.
- All **23 F01-v2 through F05 sealed digests** were unchanged after execution.

These are implementation controls and author-reviewed analytic arguments,
not an independent expert review, full repository green suite or certificate
of every infinite-domain assertion. Earlier failed receipts are retained.

This advances a sharply specified classical physical benchmark: its gauge
reduction is constructive and its missing spinor matter is now quantified.
It does not establish the Standard Model, three chiral generations, quantum
completion, four-dimensional gravity or empirical agreement. The full
physical goal remains open. No shared B number, upstream edits or push.
