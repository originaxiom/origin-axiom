"""B675 locks — H-CUSP predicts (artifact-level)."""
import os

_B = os.path.join(os.path.dirname(__file__), "..", "frontier",
                  "B675_hcusp_sweep")


def test_silver_tau_and_assignment():
    out = open(os.path.join(_B, "cell_output.txt"),
               errors="ignore").read()
    assert "-2i" in out or "-2*I" in out or "2i" in out
    assert "A3" in out


def test_addendum_presealed():
    t = open(os.path.join(_B, "PREREG_ADDENDUM_OUTCOMES.md")).read()
    assert "ENTANGLEMENT-CONFOUNDED" in t


def test_bronze_certified():
    import sympy as sp
    u, X = sp.symbols("u X")
    q = 192*u**4 - 112*u**3 + 20*u**2 - 21*u + 7
    assert sp.Poly(q, u).is_irreducible
    assert sp.expand(q.subs(u, -X**2)
                     - (192*X**8 + 112*X**6 + 20*X**4 + 21*X**2 + 7)) == 0
    assert sp.expand(u**4*q.subs(u, 1/u)
                     - (7*u**4 - 21*u**3 + 20*u**2 - 112*u + 192)) == 0
    assert sp.factorint(sp.Poly(q, u).discriminant()) == \
        {2: 24, 7: 1, 617: 1, -1: 1}
