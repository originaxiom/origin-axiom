"""Locks for B429 -- the first-order Bosonic Rigidity Theorem."""
import os, sys

HERE = os.path.join(os.path.dirname(__file__), "..", "frontier", "B429_bosonic_rigidity")
sys.path.insert(0, HERE)
import rigidity as RG


def test_block_decomposition_and_sl2_identification():
    dims = [2*m + 1 for m in RG.E6_EXPONENTS]
    assert dims == [3, 9, 11, 15, 17, 23] and sum(dims) == 78
    assert dims[0] == 3     # the Sym^2 block IS the embedded principal sl2


def test_whitehead_rigidity_every_block():
    # H^1(sl2, Sym^{2m}) = 0: cocycle space == coboundary space, exactly, for all six blocks
    for m in RG.E6_EXPONENTS:
        coc, cob, ok = RG.h1_sl2_sym_is_zero(2*m)
        assert ok and coc == cob == 2*m + 1
