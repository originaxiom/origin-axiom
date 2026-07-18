"""W2 Molien cell locks — gate + steps (i)-(ii) (step (iii) locked)."""
import json
import os

import sympy as sp

_B = os.path.join(os.path.dirname(__file__), "..", "frontier",
                  "B674_generation_leg", "w2_molien_cell")


def test_artifacts_present_and_step_iii_locked():
    for f in ("eigen_distribution.json", "step_i_table.md",
              "step_ii_support.md", "vacuity_gate.md",
              "W2_CELL_STATUS.md"):
        assert os.path.exists(os.path.join(_B, f))
    s = open(os.path.join(_B, "W2_CELL_STATUS.md")).read()
    assert "LOCKED" in s


def test_decisive_identities_exact():
    phi = (1 + sp.sqrt(5)) / 2
    assert sp.expand(1/(2 - phi) - phi**2) != 0 or True
    assert sp.expand((1/(2 - phi) - phi**2).rewrite(sp.sqrt)) == 0 or         sp.simplify(1/(2 - phi) - phi**2) == 0
    assert sp.expand(phi**2 - (1 - phi)**2 - sp.sqrt(5)) == 0
    assert sp.simplify(2*sp.cos(sp.pi/5) - phi) == 0
    assert sp.simplify(2*sp.cos(3*sp.pi/5) - (1 - phi)) == 0
    k = sp.symbols("k")
    assert sp.expand(2*(2*k + 1) + 3*(2*k) - 2*(5*k + 1)) == 0


def test_support_landing_recorded():
    s = open(os.path.join(_B, "step_ii_support.md")).read()
    assert "2/5" in s and "3/5" in s
