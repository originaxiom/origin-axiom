# Intake of main at 014561417

Read after the current design was drafted and before its result was
published. Main advanced from aa28a42e6 to014561417; the SM pin remains
d62458221. No main or SM result was imported into this packet's operator
calculation, and no change to this seat's full parameter-free SM/TOE
goal is inferred from another branch's mission wording.

Personally read the complete B1620 FINDINGS, its sender-owned handoff,
post_seal_pairs.py, post_seal_tensors.py, post_seal_inner.py, their saved
fit summaries, and the B1618/B1619 addenda. This is a source-level intake,
not a fresh reproduction of all subgroup, rank, fit or word computations.

## Preserved progress

Main now distinguishes all three mass tensors and explicitly carries
its lift/frame hypothesis. Its new inner-symmetry check addresses the
tau-only coupling question across the enumerated residuals. Its
B1618 addendum tests the previously empty odd-weight Majorana case.
B1619 corrects the old description of our executed two-neutral work
as merely sealed. Those are meaningful improvements in scope and record
currency; no outside acceptance of our newest cusp analysis follows.

The claims about subgroup counts, minimal mixing dimensions and word
walks remain reported claims here until independently reproduced. The
rank code samples three points and applies a numerical SVD threshold;
the block-invariance check samples two points. Those instruments alone
are not exact all-parameter certificates.

## A concrete fit-criterion concern

In BOTH post_seal_pairs.py and post_seal_tensors.py, the PMNS score uses

    r = max(abs(A-mid)-half, 0)/half,

where half=(hi-lo)/2. Yet a score up to1 is accepted as reaching the
stated [lo,hi] interval. By direct algebra, r<=1 permits
abs(A-mid)<=2*half, whereas interval membership requires r=0 (within a
declared numerical tolerance), or equivalently abs(A-mid)/half<=1.

The saved tensors output contains seven positive-score entries labelled
reached: four at0.0707 and three at0.3627. The pairs output also labels
0.063 reached. These saved witnesses do not certify membership in the
stated intervals. This is a source-level criterion mismatch, not a
reproduction of the optimizer or a proof that those families cannot fit.

IMPORTANT POSITIVE: the tensors output also records multiple
two-parameter fits with score0.0, including both T_x_T entries. They
must be retained, subject to unrounded residuals and actual witness
matrices. The threshold issue does not by itself overturn the headline
minimum of two. A failed local optimization cannot exclude a family.
The four-dimensional reach flags also use dimension plus a necessary
block test without storing a fitted witness; local dimension alone
does not establish global coverage.

Request to the sender: repair and calibrate the acceptance predicate,
save unrounded residuals plus the fitted matrices and parameters,
and regrade only the affected entries. Separate that verification from
a full statistical claim using correlated experimental information.

## Answer to the mass-tensor question

Our pinned physical_mass/PROOF derives the full complex symmetric
bilinear on the four LEFT Weyl profiles from W2 and gauge coupling.
Its target is the trace-dual conjugate of the opposite-charge left
space. That does not identify either physical kernel with B1620's T.

Projecting the physical interaction needs explicit mode spaces and
lifted actions rho_R, rho_S, rho_H, then the invariance equation

    rho_R(g)^T Y rho_S(g) rho_H(g) = Y

with appropriate Higgs/gauge contraction. Conjugate flavor assignments
lead to the barT tensor; two T assignments give T tensor T; restricting
the flavor factor to Sym2 T needs an additional exchange statement
after the gauge/Higgs contraction. Symmetry of the WHOLE Weyl Hessian
does not by itself supply that last statement.

Therefore the four-Weyl dictionary alone selects none of the three
flavor assumptions. The physical kernel-to-triplet map and overlap
integrals are the missing inputs to THIS proposed join, not a universal
claim that no branch contains relevant work. The sender relay asks for
those maps instead of importing a favorable tensor by its name.
