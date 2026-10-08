# First determinant check failure

The native run at seal 0102df1f55d90694b7d823484c23a6cfae0a7804 failed
at restricted_symbol_determinant, exit 1. The reference and focused
tests had not run. The literal 915-byte log remains in the local raw
capture with SHA256 1aa15b6b21d7939bba0dea97d11c421d633fbddc7a960d353e6bb0e68cd44990.

A separately captured post-failure diagnostic prints, for both planes:

    actual:   -(x**2 + y**2)**2
    expected: (-x**2 - y**2)*(x**2 + y**2)
    simplified difference: 0
    structural equality: false

Its literal 293-byte stdout has SHA256
acb95809a501ae61a66c9baccefe9cff41369aefc1bd4b47f6c75ff6f1ac7f7c;
diagnostic exit 0. This is a symbolic representation-comparison defect,
not a changed determinant or failed ellipticity theorem. Replace Python
structural equality by exact simplification of the difference. The
focused test also rejects the opposite determinant sign at xi=(1,0).
The proof, coefficient, boundary and acceptance equation are unchanged.

The original source is retained in the pushed first seal. Corrected
producer and test hashes are committed and pushed BEFORE rerunning in a
new raw directory. This is a post-first-attempt verifier repair, not a
first-attempt success. No physical claim is promoted by this correction.
