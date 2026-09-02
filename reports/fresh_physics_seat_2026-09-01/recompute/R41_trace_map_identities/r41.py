#!/usr/bin/env python3
"""R41 — small exact identities the readers marked reproducible-unknown: B518 (the trace map preserves kappa),
B344 (det d(phi_m) = 1, m = 1,2,3, with B344's own twist definitions), B332 (g = -R L^-1 exactly, traces/discriminants),
B331 cross-reference (g = [[0,-1],[1,-1]], eigenvalues omega, omega^2)."""
import sympy as sp, importlib.util
x, y, z = sp.symbols('x y z')
kappa = x**2 + y**2 + z**2 - x*y*z
lines = []
def say(s): print(s); lines.append(s)
T = (z, x, x*z - y)
say('B518: kappa(T(x,y,z)) - kappa(x,y,z) = %s  (T = (z, x, xz - y))' % sp.simplify(kappa.subs({x: T[0], y: T[1], z: T[2]}, simultaneous=True) - kappa))
# B344's own twists
Ta = lambda X, Y, Z: (X, Z, X*Z - Y); Tb = lambda X, Y, Z: (Z, Y, Y*Z - X)
def jac(f): 
    out = f(x, y, z); return sp.Matrix([[sp.diff(o, v) for v in (x, y, z)] for o in out])
say('B344: det J(Ta) = %s, det J(Tb) = %s; kappa preserved by Ta: %s, by Tb: %s' % (jac(Ta).det(), jac(Tb).det(),
    sp.simplify(kappa.subs(dict(zip((x, y, z), Ta(x, y, z))), simultaneous=True) - kappa) == 0, sp.simplify(kappa.subs(dict(zip((x, y, z), Tb(x, y, z))), simultaneous=True) - kappa) == 0))
spec = importlib.util.spec_from_file_location('b344', '/home/user/origin-axiom/frontier/B344_deviation_symplectic_pairing/' + __import__('os').listdir('/home/user/origin-axiom/frontier/B344_deviation_symplectic_pairing')[0] if False else None)
import glob
src = [f for f in glob.glob('/home/user/origin-axiom/frontier/B344_deviation_symplectic_pairing/*.py')][0]
spec = importlib.util.spec_from_file_location('b344', src); b344 = importlib.util.module_from_spec(spec)
try:
    spec.loader.exec_module(b344)
    say('B344 (its own script %s): det_is_one(m) for m=1,2,3 -> %s' % (src.split('/')[-1], [b344.det_is_one(m) for m in (1, 2, 3)]))
except Exception as e:
    say('B344 script import: %r' % e)
R = sp.Matrix([[1, 1], [0, 1]]); L = sp.Matrix([[1, 0], [1, 1]]); g = -R * L.inv(); RL = R * L
say('B332: g = -R L^-1 = %s, tr %s, disc %s; RL tr %s, disc %s; g == B331 matrix [[0,-1],[1,-1]]: %s; eigenvalues %s' % (
    g.tolist(), g.trace(), g.trace()**2 - 4*g.det(), RL.trace(), RL.trace()**2 - 4, g == sp.Matrix([[0, -1], [1, -1]]), list(g.eigenvals())))
open('r41_out.txt', 'w').write('\n'.join(lines) + '\n')
