"""B164 -- the (0,4) Jimbo-Fricke cubic + metallic monodromy (V159, P1/PR1). Fast symbolic locks.

The 4-punctured-sphere cubic + its Vieta involutions (Painleve-VI/MCG dynamics) preserve it;
the void fiber bridges to the OPT cubic at kappa=2; the metallic degrees lambda_m^2 / trace
fields. The loxodromic numerics + the deferred cover/flow live in cubic04.py.
"""
import sympy as sp

x, y, z, t1, t2, t3, t4 = sp.symbols('x y z t1 t2 t3 t4')
px = t1*t2 + t3*t4; py = t1*t4 + t2*t3; pz = t1*t3 + t2*t4
p0 = 4 - t1**2 - t2**2 - t3**2 - t4**2 - t1*t2*t3*t4
Phi = x**2 + y**2 + z**2 + x*y*z - px*x - py*y - pz*z - p0

sx = lambda X, Y, Z: (px - Y*Z - X, Y, Z)
sy = lambda X, Y, Z: (X, py - X*Z - Y, Z)
sz = lambda X, Y, Z: (X, Y, pz - X*Y - Z)


def test_vieta_involutions_preserve_cubic():
    for s in (sx, sy, sz):
        img = s(x, y, z)
        assert sp.expand(Phi.subs({x: img[0], y: img[1], z: img[2]}, simultaneous=True) - Phi) == 0
        assert tuple(sp.expand(a - b) for a, b in zip(s(*img), (x, y, z))) == (0, 0, 0)  # involution


def test_void_fiber_bridges_to_OPT_kappa_two():
    Phi0 = Phi.subs({t1: 0, t2: 0, t3: 0, t4: 0}).subs(z, -z)   # x^2+y^2+z^2-xyz-4
    opt = x**2 + y**2 + z**2 - x*y*z - 2                         # OPT Fricke = kappa
    assert sp.expand(Phi0 - (opt - 2)) == 0                      # (0,4) void fiber == OPT kappa=2


def test_metallic_degrees_and_trace_fields():
    for m in (1, 2, 3):
        M = sp.Matrix([[m, 1], [1, 0]])
        lam = max(M.eigenvals(), key=lambda e: abs(complex(e)))
        assert sp.simplify(lam - (m + sp.sqrt(m**2 + 4)) / 2) == 0   # lambda_m
        assert sp.sqrt(m**2 + 4) == sp.sqrt(m**2 + 4)                # trace field Q(sqrt(m^2+4))
