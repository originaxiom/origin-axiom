"""fc R41 (B518/B344/B332/B331): four exact one-liners, redone from scratch in sympy (not fc's script).
B344's det_is_one(m) is also called from the committed module for m=1,2,3."""
import sympy as sp, importlib.util, pathlib, glob
x, y, z = sp.symbols('x y z')
kappa = x**2 + y**2 + z**2 - x*y*z
T = (z, x, x*z - y)                                   # B518's trace map
print("B518  kappa(T) - kappa =", sp.expand(kappa.subs({x:T[0], y:T[1], z:T[2]}, simultaneous=True) - kappa))
Ta = sp.Matrix([x, z, x*z - y]); Tb = sp.Matrix([z, y, y*z - x])   # B344's two twists
for nm, Tw in (("Ta", Ta), ("Tb", Tb)):
    J = Tw.jacobian([x, y, z]); k2 = kappa.subs({x:Tw[0], y:Tw[1], z:Tw[2]}, simultaneous=True)
    print(f"B344  det J({nm}) = {sp.simplify(J.det())} ; kappa preserved: {sp.expand(k2 - kappa) == 0}")
p = glob.glob('frontier/B344_*/*.py')
print("B344 committed modules:", [pathlib.Path(q).name for q in p])
for q in p:
    src = pathlib.Path(q).read_text()
    if 'def det_is_one' in src:
        spec = importlib.util.spec_from_file_location('b344', q); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
        print("B344  committed det_is_one(m), m=1,2,3:", [m.det_is_one(k) for k in (1,2,3)])
R = sp.Matrix([[1,1],[0,1]]); L = sp.Matrix([[1,0],[1,1]]); g = -R*L.inv()
print("B332  g = -R L^-1 =", g.tolist(), "| tr g =", g.trace(), "| disc(charpoly g) =", sp.discriminant(g.charpoly().as_expr()),
      "| RL tr =", (R*L).trace(), " disc =", sp.discriminant((R*L).charpoly().as_expr()))
ev = list(g.eigenvals().keys()); w = sp.exp(2*sp.pi*sp.I/3)
print("B331  eigenvalues of g:", [sp.simplify(e) for e in ev], "| = {omega, omega^2}:", set(sp.simplify(e - w) == 0 or sp.simplify(e - w**2) == 0 for e in ev) == {True}, "| g^3 = I:", g**3 == sp.eye(2))
