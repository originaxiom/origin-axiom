# ADDENDUM (2026-09-17, S15) — the matrix is right, the NAME was wrong: it is LR, not RL

This arc writes **"M² = [[2,1],[1,1]] = RL exactly"**. The matrix is correct and every computation here is
unaffected. The *name* is not: with the convention this project fixes in `docs/UNIQUENESS_THEOREM.md` (A4),
`L = [[1,1],[0,1]]` and `R = [[1,0],[1,1]]`, so

    LR = [[2,1],[1,1]]   (= M², the figure-eight monodromy)
    RL = [[1,1],[1,2]]   (conjugate to LR, hence the same class, hence invisible to trace/det/spectrum)

This arc does not define L and R, so it inherited the convention and mislabelled the product. The label
propagated to `docs/THE_LADDER.md` (X23) and `docs/THE_FORCED_AND_THE_FREE.md`, both corrected today, and is
described (not asserted) in two campaign documents.

**Why it is worth a file rather than a silent edit.** The order `LR` vs `RL` is the project's *single irreducible
inserted bit* (A7): the two products are conjugate, so trace, determinant, characteristic polynomial and spectrum
cannot see the difference — which is exactly why the mislabel survived — while the **based** Möbius fixed-point
polynomial does see it (`τ² − τ − 1` for LR, `τ² + τ − 1` for RL: φ against −φ). A programme whose smallest
inserted structure is an order should not write that order both ways. The paper states it as LR throughout.
