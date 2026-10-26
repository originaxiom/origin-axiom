# Radial R1/R2 successor: implemented, not reviewed or run

October 26, 2026. The successor design was committed at 90989a0df
before checks.py was implemented. The independent predecessor review
and its CHANGES_REQUIRED decision remain byte-preserved.

The successor loads the original science source only after checking
its literal SHA256, then exposes one subclass. Eight original methods
are inherited unchanged. The two overrides call the old methods first
and add physical ladder/normalization/trace-dual and scalar-orientation
discrimination. It does not expose the old TestCase as a direct module
alias for duplicate discovery. Actual runtime discovery is UNRUN.

The repair rebuilds polynomial sl2 modules by differentiating monomials,
uses the actual binomial Gram, checks both gauge-map and W-Hessian
normalization routes, and identifies the R weight through the invariant
trace bilinear. It compares the independent R-only operator with the
paired square, including bdot, and the background off-diagonal
cancellation. These are the old source's ingredients, not new physical
fields or a freely inserted k0.

Both scalar extremes are reconstructed from the coordinate kinetic
maps, including the lower spin derivative's adjoint. Their first-order
orientations, doubled unitary transport and both varying square
operators are checked explicitly by the proposed methods. Isolated
wrong orientation/phase and omitted Kdot are rejecting controls in
the declared convention, not exclusions of consistent frame changes.

Only stdlib AST/JSON/hash metadata and whitespace were inspected. The
base has ten methods, the successor overrides two, and its intended
inherited total is ten. No scientific module, SymPy, check class or
test collection was executed. There is no scientific pass or failed
scientific run for this revision.

SOURCE_REVIEW_INVENTORY.json pins seventeen review sources, including
the old review, both science modules and actual parent/producers. It
is explicitly NOT a complete runtime/gate/execution specification.
The old reviewed proofs are not extended by this repair. In particular
finite controls cannot certify global Cartan matching or the physical
parent dictionary. No priced physical input is marked paid.

Before execution: obtain substantive nonauthoring review of the delta
and inherited closure, a complete environment/runtime/gate specification
with fresh outputs, separately designed/verified wrapper binding if one
is added, main's exact acceptance, and strict clean-checkout admission.
The new source must not be imported directly to see whether it works.
No old wrapper fixtures or P210 review count as this approval.

## Subsequent source review received October 26

The heading and inventory above describe the implementation snapshot,
not the state after review. The independently authored
[review](review/INDEPENDENT_REVIEW_2026-10-26.md) examined candidate
72a0b9a24dd8fe788167a268f9e5e79f64a9c5f6 and returned
NO_BLOCKING_SOURCE_ERROR_FOUND_WITHIN_REVIEWED_SCOPE. It supports both
R1/R2 repairs and the statically intended ten-method population. Its
SHA256 is 602dafbba36f9f30c7b95b6d11ad39ef948e42295e80f5934a983f76937cc763.

The author has read the entire review. Its source-reading scope and
limitations are accepted, including the warning that direct import of
the successor would execute scientific definitions without an internal
admission check. The reviewed inventory is preserved unchanged as a
snapshot, including its then-false independent_successor_review flag;
this dated addition records the subsequent event without rewriting
reviewed evidence. The original predecessor's CHANGES_REQUIRED remains.

This is NOT APPROVE_EXECUTION. No scientific run, import, collection,
main acceptance, admission or physical-input payment has occurred.
The complete execution specification, entrypoint engineering and actual
main acceptance duties above remain. The new reduction card is separate
author analysis and is not covered by this independent review.
