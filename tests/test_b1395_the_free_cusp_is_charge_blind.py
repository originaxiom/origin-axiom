"""B1395 lock -- THE FREE CUSP IS CHARGE-BLIND AT FINITE ENERGY (PROVED; the cusp integrals exact).

In the cusp (dx^2 + dy^2 + dh^2)/h^2: a Higgs class alive on the torus has L^2 norm A(a^2 + b^2) log(H/h0) (divergent: sealed classes
are fixed boundary data); a free cusp's modes are L^2; a gauge flux through the torus has energy A phi^2 (H^2 - h0^2)/2 (divergent);
chi(T^2) = 0, so a condition uniform over the torus adds nothing, and the index of a degree-n line bundle on T^2 is n."""
import importlib.util
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
VER = ROOT / "frontier" / "B1395_the_free_cusp_is_charge_blind" / "verification"


def _load():
    spec = importlib.util.spec_from_file_location("b1395_cusp_ends", VER / "cusp_ends.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_the_sealed_higgs_class_and_the_flux_diverge():
    C = _load()
    h, h0, H, A = C.h, C.h0, C.H, C.A
    a, b, phi = C.a, C.b, C.phi
    n2, I, lim = C.sealed_higgs_norm()
    assert sp.simplify(n2 - h ** 2 * (a ** 2 + b ** 2)) == 0
    assert sp.simplify(sp.expand_log(I, force=True) - A * (a ** 2 + b ** 2) * (sp.log(H) - sp.log(h0))) == 0
    assert lim == sp.oo
    n2, I, lim = C.flux_energy()
    assert sp.simplify(n2 - phi ** 2 * h ** 4) == 0
    assert sp.simplify(I - A * phi ** 2 * (H ** 2 - h0 ** 2) / 2) == 0
    assert lim == sp.oo


def test_the_free_mode_is_normalizable_and_the_torus_adds_nothing():
    C = _load()
    val, tail = C.free_mode_norm()
    assert 0 < float(val) < 1e-4
    assert all(float(t) < 1e-20 for t in tail)
    chi, rr = C.uniform_torus_condition()
    assert chi == 0 and rr == [-2, -1, 0, 1, 2, 3]
