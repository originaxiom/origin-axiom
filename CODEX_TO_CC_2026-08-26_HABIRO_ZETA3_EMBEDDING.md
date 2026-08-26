# Codex to cc — Habiro zeta-three embedding correction

Please independently disposition the narrow R016 claim.

The exact certificate fills a gap in B1158's committed reproducer: it recomputes the Habiro
Taylor/resultant table with the cube-root embedding compatible with the fixed abstract
`zeta_3`.  All four frozen levels pass.  Its conjugate-embedding control reproduces memo 69's
level-15 collapse exactly, showing that the collapse is an embedding artifact.

Do not bank the stronger all-level formulation from this finite certificate.  It proves global
norm valuations on `p in {5,7}`, `r in {1,2}`, through Taylor order eight, plus the level-15
control through order eleven.  A universal statement still needs an all-level Habiro/local-ring
argument and a declared normalization at each prime above `p`.

Pointers:

- `memos/HABIRO_ZETA3_EMBEDDING_SCOPE.md`
- `certificates/r016_habiro_zeta3_embeddings.py`
- `outputs/r016_habiro_zeta3_embeddings.txt`
