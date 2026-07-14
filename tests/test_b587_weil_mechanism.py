"""B587 — the Weyl-twisted Weil factorization (locks).

(D) Z(W; SU(3)_k) = (1/6) sum_w sign(w) tr(rho_Weil(W) P_w) — exact vs banked
B238 values; the stage channels are the +-(anti)symmetrized assemblies over the
twelve terms; LAW-O re-derives from them; the conductor menu gates each term
(silver's 7-tone at d=49; bronze's kap=10 exact cancellation; the golden closed
form (1/12)[(1+5) - 6*sqrt5] = -1/phi).

See frontier/B587_weil_mechanism/FINDINGS.md.
"""
import importlib.util
import os

import numpy as np
import pytest

_ROOT = os.path.join(os.path.dirname(__file__), "..")
_spec = importlib.util.spec_from_file_location(
    "b587m", os.path.join(_ROOT, "frontier", "B587_weil_mechanism", "weil_mechanism.py"))


def _load_module():
    # the module runs its full sweep on import; keep the lock scoped by
    # reimplementing the small pieces instead of importing the script.
    import types
    src = open(os.path.join(_ROOT, "frontier", "B587_weil_mechanism",
                            "weil_mechanism.py")).read()
    head = src[:src.index('WORDS = {')]
    mod = types.ModuleType("b587core")
    mod.__file__ = os.path.join(_ROOT, "frontier", "B587_weil_mechanism",
                                "weil_mechanism.py")
    exec(compile(head, "b587core", "exec"), mod.__dict__)
    return mod


core = _load_module()
_b238spec = importlib.util.spec_from_file_location(
    "b238m3", os.path.join(_ROOT, "frontier", "B238_su32_levelrank", "su32_wrt.py"))
b238 = importlib.util.module_from_spec(_b238spec)
_b238spec.loader.exec_module(b238)

PHI = (1 + 5 ** 0.5) / 2


def _terms(kap, word):
    T, S, perms, n = core.weil_ops(kap)
    M = core.rho_weil(word, T, S)
    return {key: np.trace(M @ P) for key, (P, sg) in perms.items()}


def _channels(t):
    Z = sum(core.WEYL[wi][1] * t[(1, wi)] for wi in range(6)) / 6.0
    Zco = sum(core.WEYL[wi][1] * t[(-1, wi)] for wi in range(6)) / 6.0
    return (Z + Zco) / 2, (Z - Zco) / 2          # stage (odd, even)


@pytest.mark.parametrize("kap", [4, 5, 7, 10, 12])
def test_decomposition_identity(kap):
    w3, S3, T3, c3 = b238.su3_data(kap - 3)
    T, S, perms, n = core.weil_ops(kap)
    for word in ("RL", "RRLL", "RRRLLL"):
        M = core.rho_weil(word, T, S)
        zW = sum(perms[(1, wi)][1] * np.trace(M @ perms[(1, wi)][0])
                 for wi in range(6)) / 6.0
        assert abs(zW - b238.wrt_trace(S3, T3, word)) < 1e-7


@pytest.mark.parametrize("kap", [4, 5, 6, 7, 8, 10, 12])
def test_law_o_rederived(kap):
    odd, even = _channels(_terms(kap, "RL"))
    law = (1.0 if kap % 4 == 0 else 0.0) - (1 / PHI if kap % 5 == 0 else 0.0)
    assert abs(odd - law) < 1e-7


def test_golden_closed_form_at_5():
    t = _terms(5, "RL")
    # identity 1; the d=25 term +5; six reflections sqrt5; rotations 1 and -1
    assert abs(t[(1, 0)] - 1) < 1e-7
    assert abs(t[(-1, 0)] - 5) < 1e-7
    for pm in (1, -1):
        for wi in (1, 2, 5):
            assert abs(t[(pm, wi)] - np.sqrt(5)) < 1e-7
    odd, _ = _channels(t)
    assert abs(odd - (1 - np.sqrt(5)) / 2) < 1e-9        # = -1/phi

def test_silver_seven_tone():
    t7 = _terms(7, "RRLL")
    for wi in (3, 4):
        assert abs(t7[(1, wi)] - 7) < 1e-7               # d=49 fires +7 at 7|kap
    t8 = _terms(8, "RRLL")
    for wi in (3, 4):
        assert abs(t8[(1, wi)] - 1) < 1e-7               # silent off-locus


def test_bronze_kap10_exact_cancellation():
    t = _terms(10, "RRRLLL")
    tot = sum(core.WEYL[wi][1] * (t[(1, wi)] + t[(-1, wi)]) for wi in range(6))
    assert abs(tot) < 1e-7
    # the four ingredients: identity 3+1, reflections 3+1 each (x3), rot -6 and +10
    assert abs(t[(1, 0)] - 3) < 1e-7 and abs(t[(-1, 0)] - 1) < 1e-7
    assert abs(t[(1, 3)] + 6) < 1e-7 and abs(t[(-1, 3)] - 10) < 1e-7


def test_conductor_menu_registered():
    m = core.conductor_menu(core.mono("RL"))
    assert m[(1, 0)] == 1 and m[(-1, 0)] == 25
    assert m[(1, 3)] == 16 and m[(-1, 3)] == 4 and m[(1, 1)] == -5
    ms = core.conductor_menu(core.mono("RRLL"))
    assert ms[(1, 3)] == 49 and ms[(-1, 3)] == 25 and ms[(-1, 0)] == 64
