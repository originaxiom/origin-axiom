# Symbolic boolean counting repair

The first run under pushed seal84b8398773d2824f63636170a790a1d3f546ec41 exited1 after1.516 seconds. It failed when Python sum attempted to add SymPy BooleanAtom comparison values. No complete predicate record was emitted, stdout was empty, and the tests were not launched. It is not a mathematical negative or a passing run.

The repair counts one for each exponent satisfying the unchanged alpha>=1/2 condition. A regression test covers both actual triplet exponent lists, the threshold equality and the empty list. The proof, matrices, exponent convention and acceptance rule are unchanged. The modified verifier and tests are resealed and pushed before the second run.

The first execution receipt preserves the original source hashes. The original source is recoverable at the first seal commit. ARTIFACT_HASHES.txt records that original seal; REPAIR_HASHES.txt records the amended instrument. The raw744-byte stderr remains locally in the first results directory with SHA25697c35b09fca2257dc39e2210a5e43e11957b1cb9583eac5f0a394e7a7536dfa1. The published redacted log replaces only the absolute workspace and interpreter prefixes. Its bytes are not claimed to have the raw digest.
