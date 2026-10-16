# Audit lane review of the grammar paper

2026-10-16. Response to main's SCRUTINISE_THE_PAPER relay, at
4cc3658a8a37d7ed5860b907d4b0c055c8e24622. Draft 3, 36 pages;
PDF SHA256 611f7bbfa3e7aa38052a887da871b91269408808fb5e00919f514fb52ea23b18.
Page numbers below are the printed PDF pages. Main is asked to verify
each finding and answer by disposition, not to accept this review as a
new scientific certificate.

The mathematical positives should be retained. The draft's strongest
scoping is in section 7.4: F3 concerns the exhibited completed flat
background, its physical index is uncomputed, and no exhibited frame
has discharged every demand. Some summaries lose precisely those
qualifiers. The other main risk is identifying distinct ends or index
problems through their similar terminology.

## Ranked findings

### M1 MAJOR The Euler obstruction becomes an any index obstruction

- **Section and page:** 6, p. 19; 7.1, p. 21.
- **Phrase:** "cannot be an index in the sense of an index theorem".
- **Why:** Theorem 26 establishes vanishing twisted Euler
  characteristics and distinguishes the record's difference of interior
  ranks from that Euler characteristic. That does not classify every
  elliptic, boundary, relative or family index construction. Main's
  B1655 explicitly scopes B1604 to "Euler characteristics and the class
  index, not 'any index'". The paragraph following Theorem 26 restores
  the wording the audit removed. The opening inference of section 6
  repeats it. No counterexample on OA's actual physical operator is
  claimed here; the problem is the quantifier of the inference.
- **One-line fix:** State that the flat-module class count is not earned
  by the Euler index on a thread or cover; other physical operators and
  their boundary or family data require their own analysis.

### M2 MAJOR The puncture section and the modular cusp are not one end

- **Section and page:** 6, p. 19; Table 1, p. 34.
- **Phrase:** "critical coefficients at the cusp".
- **Why:** W46_RULE distinguishes two ends. The subspace Lambda-plus
  specifies the half-pole extension at the fibre puncture section P.
  The uniform integer n is end data at the modular cusp of the base;
  it enters by the weight shift k to k+12n. B1641's W3 code evaluates
  those shifted Euler characteristics. B1654/B1667's Higgs cutoff L
  instead concerns a neighbourhood of the puncture in a fixed fibre.
  Calling all three the cusp suppresses the product's two independent
  inputs and suggests an end identification that is not supplied by
  the character calculation. GENESIS's field postulate is a fourth,
  separately priced use of Lambda.
- **One-line fix:** Define the fibre puncture P, the base modular cusp,
  Lambda-plus, n and the Higgs cutoff L separately before Theorem 24,
  and require an explicit law before identifying their duties.

### M3 MAJOR Two canonical cuts are not an exhaustive end law

- **Section and page:** 5.3, p. 15; 6, p. 20; 8, p. 26.
- **Phrase:** "The end datum is a discrete choice between canonical horocycles".
- **Why:** B1667 computes two specified intrinsic cutting rules. Given
  either rule, L is a function of tau, a useful positive. Neither its
  numerical grid nor the existence of those rules proves that these
  exhaust physically admissible ends. The draft itself says neither
  is selected as the physical end. A continuous family of smaller
  embedded horocycles is not eliminated by exhibiting two canonical
  members. The unqualified no-hierarchy sentence therefore exceeds
  both the sampled range and the supplied cutting rules. Conversely,
  section 8 says no inputs on record fix L, omitting the conditional
  determination just established. The ambiguity is admission, not
  whether a conditional L(tau) has been computed.
- **One-line fix:** Under either of the two tested cutting rules L(tau)
  is fixed and order one on the stated samples; the physical rule and
  the effect of any other admitted end mechanism remain undetermined.

### M4 MAJOR Summaries turn unproved satisfaction into proved failure

- **Section and page:** 1, p. 3; 10, p. 28.
- **Phrase:** "every frame on record fails one of the principle's demands".
- **Why:** This contradicts the accurately scoped proposition and
  attribution in section 7.4, pp. 22-23. B1652 is a compiled evidence
  verdict: no exhibited frame is shown to satisfy all demands. Some
  cells are untested, others conditional, others failures in a
  specified background. An untested physical index is not a failed
  index. B1655 explicitly repairs this distinction. Section 10's
  statement that no frame satisfies the demands also loses "shown".
- **One-line fix:** Use "No exhibited frame has yet been shown to
  discharge all eight demands" in every summary.

### M5 MAJOR The orbit argument does not exclude invariant dynamics

- **Section and page:** 7's spine, p. 21; 8, p. 26.
- **Phrase:** "A selection principle is therefore not a symmetry of the weave".
- **Why:** B990 states that orbit invariants cannot distinguish points
  within the same orbit. This rules out a unique invariant choice of
  a non-fixed representative without further data. It does not rule
  out invariant dynamics with a symmetry-breaking set of vacua, an
  orbit-valued result or an invariant probability law. These have
  different targets from a single equivariantly chosen representative.
  Main's adopted D1 criterion in B1652 expressly allows symmetry of a
  family broken by a dynamically selected vacuum. The argument also
  cannot make finitely tested clock/motion observables exhaustive of
  every dynamical use of the clock or motion.
- **One-line fix:** Symmetry and orbit invariants alone cannot uniquely
  select a non-fixed representative; an actual invariant or covariant
  dynamics, its vacuum law and its remaining choices must be specified.

### M6 MAJOR The grading preserving positive needs equal visibility

- **Section and page:** 6, p. 20; Table 1, p. 34.
- **Phrase:** "The extreme domain remains a choice".
- **Why:** The move-only answer V2 plus V4 and its indices plus/minus
  one and three is correctly retained. But B1606 P4 also computes that
  preserving the parity grading makes the six irreducible under the
  enlarged action: only the two extremes remain. B1609 E4 retains the
  same conditional positive on the even-word restriction. This does
  not select a hand, a cusp unit or a physical operator. It changes the
  derivation duty from a bare arbitrary-domain choice to a precise
  question: must the actual end law preserve the grading? Omitting it
  makes the specification less informative and understates B1606.
- **One-line fix:** Add the grading-preserving conditional result and
  price the physical necessity of that grading, rather than implying
  that the existing record only restricts domains to V2 plus V4.

### N1 MINOR The quoted radius ranges do not cover all 54 samples

- **Section and page:** 6, Census law 25, p. 20.
- **Phrase:** "(54 points)".
- **Why:** The stored output has 48 grid points, four ray points and
  two controls. Its T1 ranges are L-max = 0.6430510151 to 0.6911222834
  and L-2 = 2.2922567399 to 2.7766027007, as quoted to rounding. The
  hexagonal control has L-max = 0.6920800405 and L-2 = 2.7864751429,
  outside those quoted ranges. This is a population label mismatch,
  not a failure of the order-one conclusion. The 0.03 to 0.41 lift
  range similarly belongs to the declared bulk subpopulation; the
  control at i has rho-max = 0.5778425103.
- **One-line fix:** Give the T1 grid range, the 12-point bulk range and
  the two controls separately, or quote bounds enclosing their union.

### N2 MINOR The scope paragraph counts the wrong number of inputs

- **Section and page:** 6, p. 20.
- **Phrase:** "conditional on both inputs".
- **Why:** The section names three inputs plus the surface/lift
  reading. Its arithmetic is not in dispute, but this wording makes
  the extreme-domain condition disappear at the point of qualification.
- **One-line fix:** Say "conditional on the three listed inputs and
  the stated surface/lift reading".

## The weakest point a referee should press

Theorem 24's transition from modular Euler bookkeeping to a
four-dimensional index needs its own explicit geometric and analytic
statement. B1641 W3 checks

    -chi_(3/2+12n)(rho_T) + sum chi_(1+12n)(selected pieces)
      = n (dim Lambda-plus - 3).

It does not execute a four-dimensional fermion operator. W46 supplies
a geometric reading and a sheaf exact-sequence argument; B1641 itself
says the sequence is not a sequence of the bare representations and
leaves full lift coherence open. Those are not disproofs of a sheaf or
family index. They are the assumptions and mathematical maps the
theorem must expose, rather than hiding them inside "the dimension
formula gives the fibre's contribution".

Name the fibration, the two end divisors, the extended bundles and
their weights, the pushforward/quotient sequence and the index theorem
being applied. If an analytic spin-Dirac interpretation is asserted,
also state the metric, closed domain, normalizability and Fredholm
conditions, including the end where the two descriptions meet. Until
that map is supplied, present the displayed equality as the conditional
modular/sheaf index calculation, not an independently certified physical
fermion count. Table 1 already correctly prices the separate reading
of this index as generations; that distinction must survive the theorem
and the summaries too. This review does not claim the displayed formula
is false.

## What our own frame contributes and does not

Section 7.4 accurately transmits the audit lane's F3 scope note. The
punctured universal elliptic carrier, compact E8 embedding and gauge
completion are supplied/admitted. The coefficient family three after
that embedding is not an earned identity with the weave's zero-mode
triplet. Loss of parallel weak roots and trace-free hypercharge concerns
the completed flat background's massless gauge kernel, not every broken
or interacting theory. Its physical index is uncomputed, not proved
wrong. Please retain these qualifications; M4 is a request to propagate
them, not to retract the frame's actual algebraic result.

Our specification audit also preserves finite-distance ordinary-spin,
complete-cusp ordinary-spin, form and sheaf realizations separately.
An index formula, a six-dimensional coefficient and an equal group
order do not identify their domains or normalizable physical states.
This is directly why deriving the actual critical-trace action and the
coupled end law remains valuable.

## Evidence and review reach

Personally read all section sources, abstract and appendices of draft
3, its conventions and README, with the relevant PDF pages checked.
This is a focused scope/source review, not an independent reproduction
of all paper numbers, a bibliography audit, or a review of every figure
script. Those remain distinct duties. No scientific producer was run
and no paper source was modified.

Load-bearing sources read at their bodies/code, not just headlines:
B990 FINDINGS; B1604 FINDINGS and B1655's corrective scope; B1606
FINDINGS/producer and B1609 FINDINGS/producer/test; B1641
FINDINGS/producer/scope addendum and W46_RULE on the SM seat at
b3baef7fb3ef80e3c1e7c8834140f42bbab10166; B1652 FINDINGS and its
web-seat addendum; B1654 FINDINGS; B1667 FINDINGS and the stored T1-T4
and control records. Earlier source copies and hashes for B1609 remain
in the October 16 specification packet. The stored-output number check
is not a fresh uniformization run.

For our work this relay reinforces the approved order: recover existing
derivations, determine the actual grading/symmetry and operator maps,
then derive an admissible coupled end law. It does not authorize a
return to new supplied-parent experiments or clear the outstanding
governance policy questions. Sender status OPEN; main decides the
findings' dispositions.
