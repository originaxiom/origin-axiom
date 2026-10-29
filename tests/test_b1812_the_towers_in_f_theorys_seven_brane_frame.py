"""B1812 -- the towers in F-theory's 7-brane frame: the committed monodromy computation."""
import json, pathlib
import sympy as sp
ROOT = pathlib.Path(__file__).resolve().parents[1]
V = ROOT / "frontier" / "B1812_the_towers_in_f_theorys_seven_brane_frame" / "verification"


def test_the_trace_law_and_the_conjugator():
    d = json.loads((V / "e_n_monodromy.json").read_text(encoding="utf-8"))
    assert all(d["K(E_N)"][str(N)]["trace"] == N - 7 for N in range(1, 13))
    g = sp.Matrix(d["g with g K(E_10) g^-1 = LR (GENESIS)"]); K = sp.Matrix(d["K(E_N)"]["10"]["K"])
    assert g.det() == 1 and g * K * g.inv() == sp.Matrix([[2, 1], [1, 1]])
    assert d["E_3, E_4 hyperbolic of negative trace (DHIZ: not collapsible)"] == ["hyperbolic", -4, "hyperbolic", -3]
    assert [d["metallic L^n R^n"][str(n)]["content"] for n in (1, 2, 3, 4)] == [1, 2, 3, 4]
