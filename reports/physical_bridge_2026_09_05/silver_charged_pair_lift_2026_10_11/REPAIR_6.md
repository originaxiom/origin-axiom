# Failed whole-family chain predicate and sparse zero storage

At3f3f6fc24c8ea1c6892673b5619e1c9e63c23f0b the native failed the
load-bearing W_literal_full_family_chain assertion after18.459555s.
This is retained as a failed run, not erased or called successful.
The four chain identities must still pass in full; no criterion is weakened.

The guarded converter kept an entry whenever its symbolic expression
was not literally zero, even when exact quadratic conversion returned
the zero field element. The pinned SDM constructor preserves explicitly
stored zeros and its is_zero_matrix returns not self; therefore sparse
storage can make the zero predicate false on an entrywise zero matrix.
Filter converted zeros before constructing the SDM. This is required
sparse canonicalization, not changing an actual matrix or residual.

A live opposing control reproduces the stored-zero trap, then tests an
unevaluated cancelling quadratic expression AND that expression plus1.
The full chain replay decides whether any mathematical residual remains.
Do not assume this diagnosis licenses a physical/theorem pass.
Original matrices, family, ranks, proof/model/inputs/test and independent
reference stay unchanged. Hash/seal/push precedes that replay. Failed
assertion/raw/public hashes remain; outside acceptance is still owed.
