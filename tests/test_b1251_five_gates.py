"""B1251 — four cross-readings that would otherwise have been lost."""
import importlib.util, pathlib
_SRC = (pathlib.Path(__file__).resolve().parents[1]
        / "frontier" / "B1251_five_gates" / "verification" / "five_gates.py")
_s = importlib.util.spec_from_file_location("b1251", _SRC)
fg = importlib.util.module_from_spec(_s); _s.loader.exec_module(fg)


def test_selftest_passes():
    assert fg.selftest(verbose=False) == []


def test_HIER_is_S3_so_B307s_C3_obstruction_does_not_apply():
    irr, sf, grp = fg.hier_galois()
    assert irr, "HIER must be irreducible over Q"
    assert sf == 77, "squarefree disc must be 77 = 7*11 (B918's disc kernel)"
    assert grp == "S3", "B307 forbids C3; S3 means no conflict"


def test_level1_central_charge_equals_rank_for_simply_laced():
    cc = fg.level1_central_charges()
    for nm, (c, rk) in cc.items():
        if rk is not None:
            assert c == rk, f"{nm}: c={c} != rank {rk}"
        else:
            assert not c.is_Integer, f"{nm} is non-simply-laced; c must not be an integer"
    assert cc["E6"][0] == 6


def test_the_cubic_support_is_uniformly_D2_odd():
    n, signs, comp = fg.cubic_support_grading()
    assert n == 45, "B916's count, re-derived"
    assert signs == {-1: 45}, "uniformity is what gap 1 needs"
    assert comp == {"1·10·10": 5, "10·16·16": 40}, "the textbook E6 cubic under SO(10)"
