"""B1235 cell 3 -- B1233's '(0,0,0) is the global minimum of K' is LOCAL on R^3 and GLOBAL on the SU(2)
trace box [-2,2]^3 (codex R036, verified). K(x,y,z) = x^2+y^2+z^2-xyz-4 (the Markoff/Fricke form)."""
import sympy as sp
x, y, z = sp.symbols("x y z", real=True)
K = x**2 + y**2 + z**2 - x*y*z - 4
assert K.subs({x: 0, y: 0, z: 0}) == -4
assert K.subs({x: 10, y: 10, z: 10}) == -704          # below -4: NOT a global minimum on R^3
assert sp.limit(K.subs({x: sp.Symbol('t'), y: sp.Symbol('t'), z: sp.Symbol('t')}), sp.Symbol('t'), sp.oo) == -sp.oo
# the box bound: for a,b,c in [0,2],  a^2+b^2+c^2-abc = (a-b)^2 + c^2 + ab(2-c)  (an identity)
a, b, c = sp.symbols("a b c", real=True)
assert sp.expand((a - b)**2 + c**2 + a*b*(2 - c) - (a**2 + b**2 + c**2 - a*b*c)) == 0
# hence K >= -4 on [-2,2]^3 (xyz<=0 is immediate; xyz>0 reduces to |x|,|y|,|z| in [0,2]), equality only at 0
import itertools, random
random.seed(1)
mn = min(float(K.subs({x: u, y: v, z: w})) for u, v, w in
         [(random.uniform(-2, 2), random.uniform(-2, 2), random.uniform(-2, 2)) for _ in range(20000)])
assert mn >= -4 - 1e-12
# critical locus completeness (codex): origin + the four sign-product-(+1) points (+-2,+-2,+-2)
sols = sp.solve([sp.diff(K, v) for v in (x, y, z)], [x, y, z], dict=True)
pts = sorted(tuple(int(s[v]) for v in (x, y, z)) for s in sols)
assert pts == [(-2, -2, 2), (-2, 2, -2), (0, 0, 0), (2, -2, -2), (2, 2, 2)], pts
print("K(0)=-4 local min (Hessian 2I); K(10,10,10)=-704 -> NOT global on R^3")
print("on the trace box [-2,2]^3: K >= -4 with equality only at the origin (identity + 20000-point check)")
print("critical locus:", pts, "-- origin signature (3,0); the four others value 0, signature (2,1)")
print("VERDICT: B1233 row 5 narrowed -- 'global minimum' -> 'unique minimum on the SU(2) trace box'")
