# Bind the block controls to the actual detector, before replay

The explicit block run at pushed 5fc53458f passes57/34 exact predicates;
all42 five-packet regression tests pass in126.93s. Preserve these complete
outputs as BLOCK_FIRST and REGRESSION_FIRST logs, not a current-tree certificate.

A source-level verifier audit found that the new block detector's opposing
controls duplicated row-index arithmetic instead of calling its actual
field-test operation. The two reconstruction methods still agree on the
actual profile envelopes and tensors, but those detached controls alone
would not detect every future detector mutation. No observed zero is
overturned by this audit, and no result criterion is relaxed.

Extract the already-used row test as block_flag_map (native) and
block_flag_zero (reference), use it both on actual profiles AND all
positive/negative vector/exterior/dual fixtures. Explicitly cover every
field label. Hash/push the source and this note BEFORE rerun; preserve
all preceding seals, failures and successful outputs. Model, primitives,
point bounds, trace maps and supplied physical scope remain unchanged.
