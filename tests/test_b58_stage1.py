"""Tests for B58 Stage 1 -- cotangent spectrum + Sym^{2k} diagnostic (exploratory probes).

Locks the VALIDATED facts: n=3 cotangent dim = 9 (Teranishi traceless, NOT the refuted
brief value 8); the Step-2 predicted spectra (bare Kostant = even-powers-only / overshoot,
coupled = odd-powers-only); and the recorded n=4 = 30 (Djokovic). The full n=4 recompute
(~40s) is opt-in via RUN_SLOW.
"""

from __future__ import annotations

import importlib.util
import json
import os
import sys
from pathlib import Path

import pytest
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def _load(name, rel):
    spec = importlib.util.spec_from_file_location(name, ROOT / rel)
    assert spec is not None and spec.loader is not None
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def test_n3_cotangent_dim_is_9_teranishi():
    """n=3 cotangent = 9 = Teranishi (11 GL generators - 2 traceless), NOT the brief's 8.
    Multiset = Jacobian tower (8) + the deg-6 excess generator det[X,Y] (the extra (t+1))."""
    S = _load("b58_step1", "frontier/B58_stage1/step1_cotangent.py")
    spec, _ = S.cotangent_spectrum(3, 2000003, seed=20, K=80, Lmax=7)
    tot = S.merge(spec)
    dim = sum((2 if "M" in k else 1) * v for k, v in tot.items())
    assert dim == 9
    assert tot == {"char(M^2)": 1, "(t+1)": 2, "char(M^-1)": 1, "char(M^3)": 1, "(t-1)": 1}


def test_step2_bare_kostant_is_even_powers_only():
    S2 = _load("b58_step2", "frontier/B58_stage1/step2_sym2k.py")
    M = sp.Matrix([[1, 1], [1, 0]])
    bare3 = sp.diag(*[S2.sym_power(M, 2 * k) for k in range(1, 3)])
    assert S2.tag_factors(bare3, 5) == {"char(M^2)": 1, "char(M^4)": 1, "char(-M^2)": 1,
                                        "(t-1)": 1, "(t+1)": 1}
    bare4 = sp.diag(*[S2.sym_power(M, 2 * k) for k in range(1, 4)])
    tags4 = S2.tag_factors(bare4, 7)
    assert all("M^1" not in k and "M^3" not in k and "M^5" not in k for k in tags4)  # even only
    assert "char(M^6)" in tags4                                                       # overshoots to M^{2(n-1)}


def test_step2_coupled_is_odd_powers_only():
    S2 = _load("b58_step2b", "frontier/B58_stage1/step2_sym2k.py")
    M = sp.Matrix([[1, 1], [1, 0]])
    coupled3 = sp.diag(*[sp.Matrix(sp.kronecker_product(S2.sym_power(M, 2 * k), M)) for k in range(1, 3)])
    tags = S2.tag_factors(coupled3, 5)
    assert tags == {"char(M^1)": 2, "char(M^3)": 1, "char(M^5)": 1, "char(-M^1)": 2, "char(-M^3)": 2}
    assert all("M^2" not in k and "M^4" not in k for k in tags)                       # odd only


def test_n4_recorded_dim_is_30_djokovic():
    """Lock the validated, recorded n=4 = 30 (Djokovic) and the refuted brief value (19),
    kept visible as a corrected misconception."""
    d = json.loads((ROOT / "frontier" / "B58_stage1" / "cotangent_spectrum.json").read_text())
    r = d["results"]["n=4"]
    assert r["cotangent_dim"] == 30
    assert r["matches_published_count"] is True
    assert r["brief_formula_3n2_10n_11"] == 19          # refuted; recorded, not deleted


@pytest.mark.skipif(not os.environ.get("RUN_SLOW"), reason="slow ~40s; set RUN_SLOW=1 to recompute n=4")
def test_n4_recompute_dim_30():
    S = _load("b58_step1c", "frontier/B58_stage1/step1_cotangent.py")
    spec, _ = S.cotangent_spectrum(4, 2000003, seed=20, K=600, Lmax=11)
    tot = S.merge(spec)
    dim = sum((2 if "M" in k else 1) * v for k, v in tot.items())
    assert dim == 30
