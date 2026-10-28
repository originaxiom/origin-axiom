"""Main's own check of the SM seat's W130 (R71-3, P-298), from definitions -- no seat code read.
(1) the fibre's point (3, 3, 3) is a Fuchsian character of the once-punctured torus (the modular torus): x^2 + y^2 + z^2 - xyz = 0, so
    tr[A, B] = -2 (a parabolic commutator); an explicit pair; its eigenvalues are off the unit circle, so it fixes no
    positive-definite Hermitian form (not unitary), for any conjugation.
(2) the uniformizing Higgs bundle (K^1/2 + K^-1/2, Phi = the unit section): Hitchin's equation F_h + [Phi, Phi*] = 0 with
    h = diag(mu^-1/2, mu^1/2) reduces to the Liouville equation; solved by mu of curvature -4, so |Phi| measured in the
    curvature -1 metric is 1/2 and the integral of |Phi|^2 is Area/4 = pi |chi| / 2.
    python3 -B w130_check.py"""
import sympy as sp

# (1) the character
x, y, z = sp.symbols("x y z")
kappa = x**2 + y**2 + z**2 - x*y*z - 2                       # tr[A,B] for A, B in SL(2) with tr A = x, tr B = y, tr AB = z
print("(1) tr[A,B] at (3,3,3):", kappa.subs({x: 3, y: 3, z: 3}))
A = sp.Matrix([[1, 1], [1, 2]]); B = sp.Matrix([[1, -1], [-1, 2]])
C = A * B * A.inv() * B.inv()
print("    A, B in SL(2,Z): det", A.det(), B.det(), "| traces", A.trace(), B.trace(), (A*B).trace(), "| [A,B] =", C.tolist(), "tr", C.trace())
ev = list(A.eigenvals().keys())
print("    eigenvalues of A:", ev, "moduli", [sp.nsimplify(sp.Abs(e)) for e in ev], "-> |tr| = 3 > 2: not in any conjugate of SU(2); no invariant positive-definite Hermitian form")
# a unitary 2x2 with det 1 has eigenvalues e^{+-i t}: trace 2 cos t in [-2, 2]
t = sp.symbols("t", real=True); print("    SU(2) traces: 2cos t, max", sp.maximum(2*sp.cos(t), t, sp.Interval(0, 2*sp.pi)))

# (2) Hitchin's equation for the uniformizing Higgs bundle, local coordinate z = u + i v, metric mu |dz|^2 on K^-1
u, v = sp.symbols("u v", real=True); mu = sp.Function("mu")(u, v)
dzdzb = lambda f: sp.Rational(1, 4) * (sp.diff(f, u, 2) + sp.diff(f, v, 2))   # d_z d_zbar
# line K^1/2 with fibre metric |e1|^2 = mu^-1/2: Chern curvature coefficient (of dz ^ dzbar) = -d_z d_zbar log |e1|^2
F1 = -dzdzb(sp.log(mu**sp.Rational(-1, 2)))
# Phi(e1) = e2 (x) dz, |e2|^2 = mu^1/2: the (Phi* Phi) term on e1 is |Phi(e1)|^2/|e1|^2 = mu, entering with the sign of
# Hitchin's equation F + [Phi, Phi*] = 0 on the e1 line:  F1 - mu = 0  (coefficients of dz ^ dzbar)
liouville = sp.simplify(F1 - mu)
print("(2) Hitchin on K^1/2:", liouville, "= 0")
# try mu = c / v^2 (upper half plane, the hyperbolic metric scaled): solve for c
c = sp.symbols("c", positive=True)
sol = sp.solve(sp.simplify(liouville.subs(mu, c / v**2).doit()), c)
print("    mu = c/v^2 solves it for c =", sol)
cval = sol[0]
# the Gaussian curvature of mu |dz|^2: K = -(1/(2 mu)) Laplacian log mu
K = sp.simplify(-(sp.diff(sp.log(cval / v**2), u, 2) + sp.diff(sp.log(cval / v**2), v, 2)) / (2 * cval / v**2))
print("    curvature of mu|dz|^2:", K)
# |Phi|^2 in the curvature -1 metric g = |dz|^2 / v^2:  |Phi(e1)|^2/|e1|^2 * |dz|^2_g = mu * v^2
absPhi2 = sp.simplify((cval / v**2) * v**2)
print("    |Phi|^2 in curvature -1 units:", absPhi2, "-> |Phi| =", sp.sqrt(absPhi2))
chi = -1; area = 2 * sp.pi * abs(chi)
print("    once-punctured torus: chi = -1, area 2 pi; integral |Phi|^2 =", absPhi2 * area, "= pi(-chi/2):", sp.simplify(absPhi2 * area - sp.pi * (-chi) / 2) == 0)
print("w130_check exit 0")
