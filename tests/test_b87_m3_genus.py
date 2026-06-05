"""B87 (Task 3, V70) -- locking test: the metallic spectral-curve genus 3,1 (m=1,2) and the m=3
trace-relation refinement (F_3 is genus 1, disc3 factors with the golden quadratic)."""
import importlib.util
import pathlib

import sympy as sp

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location(
    "b87_m3", _ROOT / "frontier" / "B87_m3_genus" / "probe.py")
B87 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(B87)


def test_spectral_genus_3_1():
    """m=1 figure-eight spectral curve genus 3; m=2 m136 genus 1 (a minimum)."""
    g1, _ = B87.spectral_genus_from_apoly(B87.APOLY[1])
    g2, _ = B87.spectral_genus_from_apoly(B87.APOLY[2])
    assert g1 == 3 and g2 == 1


def test_m3_trace_relation_is_genus_1_with_golden_factor():
    """m=3 trace-relation double cover w^2=disc3 is genus 1; disc3 factors, incl. the golden x^2-x-1."""
    x = sp.Symbol("x")
    g3, sq3 = B87.hyperelliptic_genus(B87.DISC3, x)
    assert g3 == 1, ("m=3 trace-relation curve is genus 1, not >=2", g3)
    # disc3 contains the golden factor x^2 - x - 1 (shared with m=1's branch)
    factors = [f for f, _ in sp.factor_list(B87.DISC3)[1]]
    assert any(sp.expand(f - (x**2 - x - 1)) == 0 for f in factors), factors
