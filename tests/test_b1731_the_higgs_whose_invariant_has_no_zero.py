"""B1731 -- the Higgs whose invariant has no zero, PROVED. Live: the root count of p_n off {0, 1} exactly for odd
|n| <= 9; F_6's invariant against -48 eta^6 and F_2's null at one tau. Stored: the full checks."""
import json, pathlib, sys
A = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1731_the_higgs_whose_invariant_has_no_zero"
ROOT = A.parents[1]


def test_the_stored_checks():
    d = json.loads((A / "verification" / "the_invariant.json").read_text(encoding="utf-8"))
    assert d["A_detS_minus_a.a"] < 1e-12
    assert all(v["rel_dev"] < 1e-30 for k, v in d["B_detS_closed_form"].items() if k != "2")
    assert d["B_detS_closed_form"]["2"]["abs_if_null"] < 1e-30 and d["B_detS_closed_form"]["6"]["vs_-48eta6"] < 1e-30
    assert d["C_zero_free_a"] == [6] and d["C_null_a"] == [2]
    assert all(d["D_detS_at_e^{i pi/3}"][a] < 1e-30 for a in ("2", "10", "14", "-2", "22")) and d["D_detS_at_e^{i pi/3}"]["6"] > 1
    E = d["E_frame"]
    assert E["F2_m1_nonzero"] == 0 and E["F6_m1_nonzero"] == E["sectors"] - len(E["F6_zero_lines_orders"])
    assert set(E["F6_zero_lines_orders"]) <= {4, 12}


def test_the_root_count_live():
    import sympy as sp
    L = sp.symbols("L")
    for n in range(-9, 10, 2):
        num = sp.Poly(sp.numer(sp.together(L ** n + (1 - L) ** n - 1)), L)
        if n == 1:
            assert num.is_zero; continue
        q = num
        while q.eval(0) == 0: q = sp.Poly(sp.quo(q.as_expr(), L), L)
        while q.eval(1) == 0: q = sp.Poly(sp.quo(q.as_expr(), L - 1), L)
        assert (q.degree() == 0) == (n == 3)


def test_F6_and_F2_live():
    sys.path.insert(0, str(ROOT / "frontier" / "B1730_the_zero_free_higgs_lines" / "verification"))
    import the_zero_free_lines as Z
    mp, th2, th3, th4, eta = Z._num()
    t = mp.mpc(0.21, 1.13)
    def F(a):
        eps = 1j ** ((a + 2) // 2); e = eta(t) ** (3 - a)
        return [e * eps * th2(t) ** a, e * eps * th4(t) ** a, e * 1j * th3(t) ** a]
    f6, f2 = F(6), F(2)
    assert abs(sum(x * x for x in f6) / (-48 * eta(t) ** 6) - 1) < 1e-25
    assert abs(sum(x * x for x in f2)) / max(abs(x) for x in f2) ** 2 < 1e-25
