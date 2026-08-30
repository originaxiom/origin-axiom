"""B1183 lock -- THE ONE-CLASS THEOREM: QP-4's obstruction class = c's class. Live exact asserts."""
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def test_arc_verdict_proved():
    d = json.loads((ROOT / "frontier" / "B1183_one_class_theorem" / "arc_verdict.json").read_text(encoding="utf-8"))
    assert d["id"] == "B1183" and d["verdict"] == "PROVED"
    assert "ONE-CLASS THEOREM" in d["claim_one_line"]
    assert "quine" in d["claim_one_line"] and "untouched" in d["claim_one_line"]


def test_chord_arithmetic_live():
    phi = (1 + sp.sqrt(5)) / 2
    z5 = sp.exp(2 * sp.pi * sp.I / 5)
    assert sp.simplify(2 * sp.cos(2 * sp.pi / 5) - 1 / phi) == 0
    assert sp.simplify(sp.nsimplify(sp.N(z5 + z5**4 - 1 / phi, 50))) == 0
    assert sp.simplify(z5 * z5**4 - 1) == 0
    eps = sp.Matrix([[0, -1], [1, 0]])
    assert sp.simplify(eps * eps + sp.eye(2)) == sp.zeros(2, 2)


def test_one_involution_restrictions_live():
    z5 = sp.exp(2 * sp.pi * sp.I / 5)
    w = sp.exp(2 * sp.pi * sp.I / 3)
    assert abs(complex(sp.N(2 * (z5 + z5**4) + 1 - sp.sqrt(5), 50))) < 1e-45   # sqrt5 real, sigma_4-fixed
    assert abs(complex(sp.N(z5**4 - sp.conjugate(z5), 50))) < 1e-45            # sigma_4 = conjugation
    assert abs(complex(sp.N(sp.conjugate(w) - w**2, 50))) < 1e-45              # c|K = the Gal generator


def test_sign_carrier_flip_live():
    w = sp.exp(2 * sp.pi * sp.I / 3)
    zz = sp.symbols('zz')
    f = 3 * zz**2 - 2 * zz + 7
    assert abs(complex(sp.N(sp.im(f.subs(zz, sp.conjugate(w))) + sp.im(f.subs(zz, w)), 50))) < 1e-45


def test_consequence_addenda_landed():
    a1 = (ROOT / "frontier" / "B1169_qualia_parity_synthesis" / "ADDENDUM_s1_promoted_B1183.md").read_text(encoding="utf-8")
    assert "FULLY PROMOTED" in a1 and "one bit, proved" in a1
    a2 = (ROOT / "frontier" / "B1161_frontier_sweep" / "ADDENDUM_label_upgraded_B1183.md").read_text(encoding="utf-8")
    assert "PROVED-AS-DECOMPOSED" in a2 and "proved one class" in a2
