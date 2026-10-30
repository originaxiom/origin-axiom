"""The outcome map (the fourth review's F4-F6): PASS only for all four; SUPPORT WITHOUT SPECIFICITY whenever X2 fails;
the CKM leg needs its chi2_4 clause; K UNJUDGED cannot pass; strict gates on the bounds; m >= 53; NaN and p > 1 raise;
T's grades required, NEGATIVE under every clock overrides."""
import pathlib, sys
import pytest
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / 'scripts' / 'stepb')); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import outcome as O

OK = dict(in_support=True, p2_up=0.0001, K_grade="JUDGED", C_ten=5.0, pK_up=0.0001, pckm_up=0.0001, ckm_clause=True, m=53)


def L(**kw):
    a = dict(OK); a.update(kw); return O.legs(**a)


def test_pass_only_for_all_four():
    assert O.reading(L(), ("CONSISTENT",)).startswith("PASS")
    t = O.table()
    assert len(t) == 16 and sum(r.startswith("PASS") for _, r in t) == 1


def test_without_specificity_whenever_x2_fails():
    for k_ok, c_ok in ((True, True), (True, False), (False, True), (False, False)):
        r = O.reading(L(p2_up=0.5, C_ten=5.0 if k_ok else -1.0, ckm_clause=c_ok), ("CONSISTENT",))
        assert r.startswith("SUPPORT WITHOUT SPECIFICITY"), r
    assert O.reading(L(in_support=False), ("CONSISTENT",)).startswith("NO SUPPORT")
    assert O.reading(L(C_ten=-1.0), ("CONSISTENT",)).startswith("SUPPORT WITH SPECIFICITY")


def test_ckm_clause_and_K_unjudged():
    assert not L(ckm_clause=False)["CKM"]
    u = L(K_grade="UNJUDGED", C_ten=None, pK_up=None)
    assert not u["K"] and "K UNJUDGED" in O.reading(u, ("CONSISTENT",))


def test_strict_gates_and_guards():
    g = 0.01 / 53
    assert not L(p2_up=g)["X2"] and not L(C_ten=0.0)["K"]
    for bad in (dict(m=52), dict(p2_up=float("nan")), dict(pckm_up=1.5), dict(C_ten=float("nan")), dict(K_grade="maybe")):
        with pytest.raises(ValueError):
            L(**bad)


def test_T_required_and_override():
    with pytest.raises(ValueError):
        O.reading(L(), ())
    with pytest.raises(ValueError):
        O.reading(L(), ("UNKNOWN",))
    assert O.reading(L(), ("NEGATIVE", "NEGATIVE")).startswith("NEGATIVE")
    assert O.reading(L(), ("NEGATIVE", "CONSISTENT")).startswith("PASS")


def test_p_exact_and_the_gate_in_bits():
    import compression as Kc
    assert O.p_exact(-3.0) == 1.0 and O.p_exact(0.0) == 1.0 and abs(O.p_exact(10.0) - 2 ** -10) < 1e-18
    m = 53; g = Kc.gate_bits(m)
    L1 = O.legs(True, 0.0, "JUDGED", g + 0.01, O.p_exact(g + 0.01), O.p_exact(g + 0.01), True, m)
    L2 = O.legs(True, 0.0, "JUDGED", g - 0.01, O.p_exact(g - 0.01), O.p_exact(g - 0.01), True, m)
    assert L1["K"] and L1["CKM"] and not L2["K"] and not L2["CKM"]
