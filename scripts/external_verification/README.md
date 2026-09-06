# External verification scripts (fresh seat, clean clone, 2026-09-06)

Standalone re-derivations written without importing the repository's own verification code
(the one exception is `nonselfdual_w1w2.py`, which imports `frontier/B71_sl3_apoly/peripheral.py`
only as the *source* of the W1/W2 representations it tests). Companion document:
`docs/EXTERNAL_VERIFICATION_2026-09-06.md`.

| script | what it checks | runtime |
|---|---|---|
| `spine_recompute.py` | the spine: `A = LR`, the Riley representation and trace field, the mod-(√−3) image `SL(2,F₃) = 2T`, the McKay graph of 2T = affine E₆, `Vol(m004) = (3√3/2)·L(χ₋₃,2)`, `sin²θ_W = 3/8` on 5̄/10/16/27 alike, the ℤ₆ kernel, the anomaly argument for Y with and without ν^c, self-duality of every Sym^n | ~2 s (numeric-first longitude search; the Sym^n invariant-form kernel is a numeric SVD) |
| `fox_symn_and_lemma.py` | Fox calculus on m004 (2-bridge presentation), exact over two primes: the Menal-Ferrer–Porti law `h¹(Sym^n) = 1, 0` (n even, odd) and the net-chirality lemma on the self-dual `Sym^n` | ~2 min |
| `nonselfdual_psl27_extension.py` | non-self-dual representations of the knot group: the two 3-dimensional irreducibles of `PSL(2,7)` through every homomorphism class, and a non-semisimple extension of a character by the geometric representation | ~1 min |
| `nonselfdual_w1w2.py` | the computation `frontier/B1260_where_chirality_can_live/FINDINGS.md` names and leaves unrun: `h¹(V)` versus `h¹(V*)` on B71's non-self-dual SL(3) components W1/W2, at generic points and on the locus where the cusp holonomy has fixed vectors, for all three central twists of the monodromy | ~5 min |

Run from the repository root with `python3 scripts/external_verification/<script>`. Dependencies are the
pinned core (`numpy`, `scipy`, `sympy`, `mpmath`); no SnapPy or Sage is needed.
