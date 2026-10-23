"""B1730 -- the zero-free Higgs lines (P-300's W133 part), PROVED. Live: the character identity exactly; h(4, 0) and
h(4, 1) rebuilt exactly with their zero-free members. Stored: the multiplier checks and every space's dimension and
members."""
import json, pathlib, sys
A = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1730_the_zero_free_higgs_lines"
sys.path.insert(0, str(A / "verification"))


def _stored():
    return json.loads((A / "verification" / "the_zero_free_lines.json").read_text(encoding="utf-8"))


def test_the_stored_checks():
    d = _stored()
    assert d["A"]["rho_T_from_R_vs_W64"] < 1e-25 and d["A"]["rho_S_from_R_vs_W64"] < 1e-25
    assert d["A"]["monomial_product_T_is_chi_eta^21"] and d["A"]["monomial_product_S_is_chi_eta^21"]
    assert d["A"]["r_mod_24_with_trivial_character_of_N_over_eta9"] == [4, 12, 20]
    assert max(d["B"]["worst_relative"].values()) < 1e-25
    dims = {k: (v["dim_M4"], v["dim_M6"]) for k, v in d["C"].items()}
    want = {(0, 0): 0, (0, 1): 3, (0, 2): 6, (4, 0): 1, (4, 1): 4, (4, 2): 7, (12, 0): 0, (12, 1): 3, (12, 2): 6,
            (20, 0): 0, (20, 1): 3, (20, 2): 6}
    for (r, n), dim in want.items():
        v = d["C"]["h(%d,%d)" % (r, n)]
        assert dims["h(%d,%d)" % (r, n)] == (dim, dim)
        assert len(v["members_a"]) == (dim if r else 0) and v["members_in_span_exactly"] and v["members_distinct_orders"]
    assert d["C"]["h(4,1)"]["members_a"] == [-10, 2, 14, 26] and d["C"]["h(12,1)"]["members_a"] == [-6, 6, 18]
    assert d["C"]["h(20,1)"]["members_a"] == [-2, 10, 22] and d["C"]["h(4,0)"]["members_a"] == [2]


def test_the_character_identity_live():
    import sympy as sp
    z = sp.exp(sp.I * sp.pi / 4)
    rT = z * sp.Matrix([[1, 0, 0], [0, 0, 1], [0, -1, 0]]); rS = z * sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
    mono = lambda M: sp.prod([e for e in M if e != 0])
    assert sp.simplify(mono(rT) - sp.exp(2 * sp.pi * sp.I / 24) ** 21) == 0
    assert sp.simplify(mono(rS) - sp.exp(-sp.I * sp.pi / 4) ** 21) == 0
    assert [r for r in range(24) if (12 + 3 * r) % 24 == 0] == [4, 12, 20]


def test_the_twisted_spaces_live():
    import the_zero_free_lines as Z
    for (r, n), want in (((4, 0), [2]), ((4, 1), [-10, 2, 14, 26])):
        basis, _ = Z.space(r, n, 4); bd = Z.bounds(r, n)
        mem = [a for a in range(-30, 71, 4) if (2 * a - r) % 24 == 0 and all(Z.member(a, r)[i].ord() >= bd[i] for i in range(3))]
        assert len(basis) == len(want) and mem == want and all(Z.in_span(Z.member(a, r), basis) for a in mem)
    assert Z.bounds(0, 1) == [-7, -1, -5] and len(Z.space(0, 1, 4)[0]) == 3          # B1700's unit space
