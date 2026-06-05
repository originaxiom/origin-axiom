"""B73 (Path A) -- the degree=rank tower law: SL(2) has no Dehn-filling component; SL(4) gives M^4=L
on the {tr A=tr A^-1=1} component and M^3=L on the {z^4+1} component."""
import importlib.util
import pathlib

import numpy as np
import sympy as sp

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location(
    "b73_df", _ROOT / "frontier" / "B73_sl4_apoly" / "dehn_filling.py")
df = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(df)


def test_sl2_no_dehn_filling_component_and_no_LMk():
    """A0 (exact): SL(2) Fix(T_1^2) is a single (geometric) component; L=M^k not on Cooper-Long."""
    x, y, z = sp.symbols("x y z")
    # T_1^2 on (x,y,z) = (xz-y, z, xz^2-x-yz); fixed equations:
    eqs = [sp.expand(x * z - y - x), sp.expand(z - y), sp.expand(x * z**2 - x - y * z - z)]
    G = sp.groebner(eqs, x, y, z, order="lex")
    # single component: groebner basis {x*z-x-z, y-z} -> y=z, x=z/(z-1) (the geometric curve)
    assert set(G) == {sp.expand(x * z - x - z), sp.expand(y - z)}
    M, L = sp.symbols("M L")
    A_CL = M**4 * L**2 + (-M**8 + M**6 + 2 * M**4 + M**2 - 1) * L + M**4
    for k in (1, 2, 3, -1, -2, -3):
        assert sp.expand(A_CL.subs(L, M**k)) != 0   # L=M^k not on the curve


def _degree_devs(spec, ks, seed=0):
    out = df.realize_bundle_rep(spec, seed=seed)
    assert out is not None, "failed to realize a bundle rep"
    A, B, t = out
    return {k: df.degree_relation_dev(A, B, t, k) for k in ks}


def test_sl4_principal_component_M4_eq_L():
    """SL(4): the {1,1,w,w^2} (tr A=tr A^-1=1) component gives M^4=L (degree=rank); k=3,5 do not."""
    devs = _degree_devs(df.SPEC_W1, (3, 4, 5), seed=5)
    assert devs[4] < 1e-7                     # M^4 = L
    assert devs[3] > 1e-2 and devs[5] > 1e-2  # not M^3 or M^5


def test_sl4_second_component_M3_eq_L():
    """SL(4): the {z^4+1} (tr A=0) component gives M^3=L (a different degree); k=4 does not."""
    devs = _degree_devs(df.SPEC_Z4, (2, 3, 4), seed=2)
    assert devs[3] < 1e-7                     # M^3 = L
    assert devs[2] > 1e-2 and devs[4] > 1e-2


def test_sl4_bundle_rep_genuine():
    """The realized reps are genuine irreducible figure-eight bundle reps (monodromy residual ~0)."""
    out = df.realize_bundle_rep(df.SPEC_W1, seed=5)
    assert out is not None
    A, B, t = out
    _t, res = df.monodromy(A, B)
    assert res < 1e-6
    assert abs(np.linalg.det(A) - 1) < 1e-9 and abs(np.linalg.det(B) - 1) < 1e-9
