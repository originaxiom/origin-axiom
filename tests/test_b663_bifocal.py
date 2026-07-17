"""B663 locks — the bifocal adjudication + anatomy loop 1 (verified)."""
import json
import os
from collections import defaultdict
from fractions import Fraction as Fr

_ROOT = os.path.join(os.path.dirname(__file__), "..")
_PK = os.path.join(_ROOT, "frontier", "B663_bifocal_anatomy")


def test_a1_jordan_unit_direction_from_banked_cubic():
    cub = json.load(open(os.path.join(_ROOT, "frontier",
                                      "B649_silver_holonomy",
                                      "cubic_rational.json")))
    N = defaultdict(Fr)
    for k, v in cub.items():
        i, j, l = map(int, k.split(","))
        N[(i, j, l)] = Fr(v)
    v0 = {12: Fr(1), 13: Fr(-1), 14: Fr(1)}
    s = defaultdict(Fr)
    for (i, j, l), c in N.items():
        if i in v0 and j in v0:
            s[l] += c * v0[i] * v0[j]
    supp = {m: x for m, x in s.items() if x != 0}
    assert sorted(supp) == [12, 13, 14]
    assert [supp[12], supp[13], supp[14]] == [Fr(-2), Fr(2), Fr(-2)]
    assert sum(supp[m] * v0[m] for m in v0) == Fr(-6)   # N(v0,v0,v0)


def test_a2_table_gates():
    d = json.load(open(os.path.join(_PK, "anatomy_packet", "loop1",
                                    "a2_phases", "a2_table.json")))
    assert d["law_holds_all"] is True
    assert d["gates"]["magnitude_gate"] == {"pass": 101, "total": 101}
    assert d["gates"]["identification"]["fallback_used"] == 0


def test_a3_su3_central_character_numeric():
    import importlib.util
    import numpy as np
    spec = importlib.util.spec_from_file_location(
        "b238a3", os.path.join(_ROOT, "frontier", "B238_su32_levelrank",
                               "su32_wrt.py"))
    b238 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(b238)
    w, S, T, c = b238.su3_data(6)
    np_ = np
    Si, Ti = np_.linalg.inv(S), np_.linalg.inv(T)
    M = T @ (Si @ Ti @ S)
    prs = [(i, w.index((wt[1], wt[0]))) for i, wt in enumerate(w)
           if (wt[1], wt[0]) > wt]
    odd = np_.zeros((len(w), len(prs)))
    for j, (a, b) in enumerate(prs):
        odd[a, j], odd[b, j] = 1 / np_.sqrt(2), -1 / np_.sqrt(2)
    B = odd.T @ M @ odd
    assert np_.allclose(np_.linalg.matrix_power(B, 18),
                        -np_.eye(len(prs)), atol=1e-8)


def test_bifocal_s_entry_field_correction():
    """1/D is not in Q(sqrt5): D^2 = 3+3*phi^2 is not a square there."""
    import sympy as sp
    a = sp.symbols('a')
    # (a + b sqrt5)^2 = D^2 with 2ab = 3/2 -> 16a^4 - 120a^2 + 45 = 0
    roots = sp.solve(16 * a**4 - 120 * a**2 + 45, a)
    assert all(not r.is_rational for r in roots)
