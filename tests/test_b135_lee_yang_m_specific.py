"""Locks for B135 -- the Lee-Yang bridge is m=1-specific; the m=1 match is at modular-data level."""
import importlib.util
import pathlib

_ROOT = pathlib.Path(__file__).resolve().parents[1]


def _load():
    spec = importlib.util.spec_from_file_location(
        "b135_probe", _ROOT / "frontier/B135_lee_yang_m_specific/probe.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


B135 = _load()


def test_lee_yang_is_m1_specific():
    r = B135.m_specificity()
    assert r["only_m1_is_quantum_dim"]                # lambda_m < 2 iff m=1 -> no metallic Lee-Yang family
    assert r["rows"][1]["is_quantum_dim"] and not r["rows"][2]["is_quantum_dim"]


def test_fibonacci_galois_to_yang_lee():
    r = B135.fibonacci_vs_yang_lee()
    assert r["galois_phi_to_minus_inv_phi"]           # sigma_3: phi -> -1/phi (Fibonacci -> Yang-Lee)
    assert r["fibonacci"]["S4_is_identity"] and r["yang_lee"]["S4_is_identity"]
