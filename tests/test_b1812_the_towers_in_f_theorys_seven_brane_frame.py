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


def test_review73_the_a_stacks_collapse_inside_the_same_configuration():
    """Review 73 (2026-10-30): main's check of its reader's finding. A^5 < A^5BC < A^5BCC inside A^9BCC are Kodaira fibres
    with matching brane numbers (I_5 < I_1* < IV*); E_3 and E_4 are not. Recomputed here by a second route (sympy)."""
    d = json.loads((V / "review73_subcollections.json").read_text(encoding="utf-8"))
    assert d["chain"]["AAAAA"] == ["I_5", "su(5)"] and d["chain"]["AAAAABC"] == ["I_1*", "so(10)"] and d["chain"]["AAAAABCC"] == ["IV*", "e6"]
    assert d["chain"]["AAABCC"] is None and d["chain"]["AABCC"] is None
    K = lambda p, q: sp.Matrix([[1 + p * q, -p * p], [q * q, 1 - p * q]])
    A, B, C = K(1, 0), K(1, -1), K(1, 1)
    assert C * B * A ** 5 == sp.Matrix([[-1, 1], [0, -1]])          # A^5 B C = -T^-1: I_1*, so(10)
    assert (C * C * B * A ** 5).trace() == -1 and (C * C * B * A ** 5) ** 3 == sp.eye(2)   # A^5 B C C: order 3, IV*
    assert (C * C * B * A ** 3).trace() == -3                          # E_4: hyperbolic, the control that fails to collapse

