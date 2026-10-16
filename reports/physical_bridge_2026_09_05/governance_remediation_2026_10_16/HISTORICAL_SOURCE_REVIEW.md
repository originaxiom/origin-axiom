# Historical design scope and restored audit evidence

The first five paths printed by the provenance failure have now been
read in full and checked against their Git history. Their unchanged
original texts contain scope and prior-work context, but do not all
contain the literal labels the current checker requires. This is a
source review, not a retrospective preregistration or permission to
waive the rule.

The corrected record is HISTORICAL_DESIGN_AUDIT_BYTE_CHECKED.json.
Each of EXTENSION_2, its disclosed control, UPSTREAM_3_DESIGN, its
serialization repair and GLOBAL_SINGULAR_DESIGN is unchanged since
creation, has a matching latest seal, and precedes its first committed
output in the Git ancestry. This does not certify the time of actual
first execution. The controls and repair reuse explicitly declared
context rather than constituting fresh blind tests. GLOBAL_SINGULAR's
findings already disclosed the marker debt at first landing.

Only these five design cases have this historical reading here.
The full gate population remains 647 unique paths across 6174 seal
rows, including data and source pins as well as design documents.
Neither five inspected paths nor missing literal markers establish
647 historical failures to search prior work. Conversely, the semantic
context of these five does not clear every design's rule obligations.
The seal-role/history question remains addressed to main.

## R40 custody and a repaired metadata comparison

R40's six scientific source files match the seal at
9e2d43ec8a6710ece4906b0b8468b58fdb84c0a5, and all 24 frozen input
files match. The stored native output and saved remote capture agree
under their documented custody checks. This is consistency of source
and saved results, not a new mathematical execution or independent
certificate of historical execution timing. The source's disclosed
post-execution ledger repair remains post-execution.

The first completed metadata audit falsely marked one of those six
files changed, even though both displayed hashes were identical.
Its string comparison mixed UTF-8 and binary encodings. The byte-wise
repair now checks both the unchanged file and an altered-byte rejecting
control. The faulty JSON and both earlier scripts are retained. The
preceding Ruby-version launch failure is also documented, not relabeled
as a successful run. See BYTE_COMPARISON_REPAIR and
HISTORICAL_METADATA_FIRST_ATTEMPT.

## Four full state inventories recovered by exact published hash

The older temporary capture directories were no longer accessible
after continuation. The previously committed public logs, receipts
and original hashes remain. No original historical process receipt
has been invented to replace them.

restore_state_from_git.rb reconstructs each complete tracked state,
index and original 16 source pins from its immutable Git commit. It
accepts a reconstruction only when the serialized bytes match the
published before and after SHA256 exactly. All four checks succeeded:

| Published state | Tracked files | Recovered state SHA256 |
|---|---:|---|
| First attempt | 18047 | cb0c905b1ee68774a45742835dc9729d222ce487456c4b9b4023a9df49c85b31 |
| Execution successor | 18074 | 4f84b3e97c7bc6a14da6ae5df0e075eed1ddf89618bf188f1eb4831be846ebab |
| Ledger attempt | 18104 | cd2ab76f977ef99d2a0a1d9fbd50905b234ce29f74e2b6598d0de2b4933bf9ab |
| Corrected validation | 18134 | 85cf18735e876271f4b5fc3d338df90e9b5b25cb6a97369a1f4a9cebef64c606 |

The deterministic compressed inventories, reconstruction receipts and
the current terminal metadata-run receipts are in
results/historical_source_review. Their compressed and decompressed
hashes were checked again after publication. They are labeled
Git-derived reconstructions, not the original captured inventories or
new evidence that the old executions complied with every rule. Current
captures now live outside Git in the persistent task workspace rather
than relying only on a temporary directory.

No scientific producer, gate, attribution baseline, old seal or failed
output was modified by this review. The last full governance result is
still the earlier corrected validation, 28 pass and two fail at
f2c8355cb. It is not a certificate for the current documentation tree.
