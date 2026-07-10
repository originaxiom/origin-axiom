"""B511/D5 locks — the generation door's closing battery."""
import sympy as sp

x, y, z = sp.symbols('x y z')


def test_chebyshev_control():
    # the m-power verb's fixed traces = roots of 2*T_m(x/2) = x; orders m-1, m+1
    fixed = {m: set(sp.solve(sp.expand(2*sp.chebyshevt(m, x/2) - x), x)) for m in (2, 3)}
    assert fixed[2] == {2, -1}            # order 3 (and trivial): the "forced 3" is m+1 at m=2
    assert fixed[3] == {2, -2, 0}         # order 4 (and orders 1,2): cubing forces 4 — control fires


def test_minimal_verb_fixes_curve_kappa2():
    # period-doubling (|det|=2, the minimal stratum-2 citizen) fixes (z, z^2-2, z), kappa == 2
    kap = x**2 + y**2 + z**2 - x*y*z - 2
    on_curve = kap.subs({x: z, y: z**2 - 2})
    assert sp.simplify(on_curve - 2) == 0
    # and it IS a fixed curve of T_pd = (z, x^2-2, (x^2-1)z - x*y)
    T = (z, x**2 - 2, (x**2 - 1)*z - x*y)
    img = [t.subs({x: z, y: z**2 - 2, z: z}, simultaneous=True) for t in T]
    assert [sp.simplify(img[i] - v) for i, v in enumerate((z, z**2 - 2, z))] == [0, 0, 0]


# --- D3.3 lock ---
import os as _os, sys as _sys
_sys.path.insert(0, _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..",
                                  "frontier", "B511_physics_verdict"))
import d3_wild_access as _D3


def test_d3_wild_dynamically_suppressed():
    # the measure concentrates classical; the wild register has small stationary mass
    c, w = _D3.accessibility(n=2000, steps=1500)
    assert c > 0.8 and w < 0.15
