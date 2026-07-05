"""Locks for B430 -- the sl2 landscape: fermionic content exists (root sl2) but is unforced."""
import os, sys

HERE = os.path.join(os.path.dirname(__file__), "..", "frontier", "B430_sl2_landscape")
sys.path.insert(0, HERE)
import sl2_landscape as SL


def test_root_sl2_gives_six_spin_half_doublets():
    r = SL.root_sl2()
    assert r["eigs"] == {-1: 6, 0: 15, 1: 6}     # 27 = (2,6bar) + (1,15) under A1xA5
    assert r["doublets"] == 6 and r["singlets"] == 15
    assert r["spinorial"] is True                # fermionic content EXISTS in the landscape


def test_principal_sl2_is_bosonic():
    assert SL.principal_sl2()["all_even"] is True   # the forced embedding: no fermions (B428)
