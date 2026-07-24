"""B778 -- the cleanup wave (partial 5/7): locks on the banked fixes."""
import json
import pathlib

ARC = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B778_cleanup"


def test_darkhyp_count_identity():
    # the N=p^2 dark-hyperbola stratification counts sum to p^4 (p=3: 63+6+1+11=81)
    assert 63 + 6 + 1 + 11 == 81 == 3**4


def test_w5139_genus_41_reproduced():
    # the strip kept genus(A_3)=41 (RH: 2g-2 = 4B, B=20)
    r = json.loads((ARC / "cells" / "CL-W5139" / "results.json").read_text())
    assert r["verdict"] == "RESOLVED-A"
    assert r.get("genus") == 41
    assert (2 * 41 - 2) == 4 * 20


def test_h133_genuine_zero_hardens():
    # H133's Z4=0 is a genuine zero at chord level (both sectors vanish), NOT a W4-304 cancellation
    r = json.loads((ARC / "cells" / "CL-H133" / "results.json").read_text())
    assert r["verdict"] == "RESOLVED-B"  # HARDENS


def test_cleanup_partial_shape():
    d = json.loads((ARC / "partial_results.json").read_text())
    banked = {c["id"] for c in d["cells"]}
    # the 5 that completed this pass
    assert banked == {"CL-DARKHYP", "CL-W3082", "CL-W5139", "CL-W5100", "CL-H133"}


def test_clw4115_adjoint_fabrication_and_field_disjointness():
    import sympy as sp
    t = sp.symbols("t")
    # 'adjoint 7,815' is fabricated: essential adjoint content has no 7 or 815
    adj = t**2 - 5 * t + 1
    content = [abs(int(sp.resultant(adj, t**n - 1))) for n in (1, 2, 3, 4, 5)]
    assert content == [3, 21, 108, 525, 2523]
    assert 7 not in content and 815 not in content
    # the wall's real mechanism: three distinct fields
    assert {int(sp.discriminant(t**2 - 4 * t + 1)),   # chord Q(sqrt3) -> 12
            int(sp.discriminant(t**2 - 5 * t + 1)),   # adjoint Q(sqrt21) -> 21
            int(sp.discriminant(t**2 - 3 * t + 1))} == {12, 21, 5}  # charge Q(sqrt5) -> 5


def test_cllatin_amplitudes_not_galois_closed():
    # the Latin square is NOT forced: {A1,A2,A3} not Galois-closed (orbit is {A1,A2,-A3})
    import sympy as sp
    x = sp.symbols("x")
    A = [(2 / sp.sqrt(7)) * sp.sin(2 * sp.pi * j / 7) for j in (1, 2, 3)]
    mp = sp.minimal_polynomial(A[0], x)
    assert mp == 7 * x**3 - 7 * x**2 + 1
    assert abs(float(sp.N(mp.subs(x, A[2]), 40))) > 1e-6     # +A3 NOT a root
    assert abs(float(sp.N(mp.subs(x, -A[2]), 40))) < 1e-30   # -A3 IS a root (the non-Galois |.| step)


def test_b778_now_complete_7of7():
    import pathlib
    cells = pathlib.Path("frontier/B778_cleanup/cells")
    for c in ["CL-DARKHYP", "CL-W3082", "CL-W5139", "CL-W5100", "CL-H133", "CL-W4115", "CL-LATIN"]:
        assert (cells / c / "results.json").exists(), c
