"""Referee B1796 -- W130 by the referee's own route.
(a) A = [[1,1],[1,2]], B = [[1,-1],[-1,2]]: traces, commutator, membership in SL(2,Z)' (kernel of the abelianisation
    SL(2,Z) -> Z/12, computed by an S,T word decomposition), the Fuchsian locus is two-dimensional ((3,3,3) is one point).
(b) "no Hermitian form is preserved": A preserves the indefinite Hermitian form H = [[0, i], [-i, 0]] (true for all of
    SL(2,R)); only a POSITIVE-DEFINITE invariant form is excluded.
(c) Hitchin's equation by the seat's route (metric fixed to the curvature -1 one, solve for |c|) and by a general ansatz
    mu = c v^p (only p = -2 solves, with c = 1/4); sign check: the opposite sign of [Phi, Phi*] has no positive solution.
(d) |Phi|^2 in the three common normalisations, and the convention-free statement 2i tr(Phi ^ Phi*) = dA_(-1).
    python3 -B w130_ref.py"""
import sympy as sp

A = sp.Matrix([[1, 1], [1, 2]]); B = sp.Matrix([[1, -1], [-1, 2]])
C = A * B * A.inv() * B.inv()
print("(a) traces", A.trace(), B.trace(), (A * B).trace(), "| [A,B] = A B A^-1 B^-1 =", C.tolist(), "| B^-1 A^-1 B A... A^-1 B^-1 A B =", (A.inv() * B.inv() * A * B).tolist())
S = sp.Matrix([[0, -1], [1, 0]]); T = sp.Matrix([[1, 1], [0, 1]])


def chi12(g):
    """abelianisation SL(2,Z) -> Z/12 with T -> 1, S -> 9 (s = -3t), by reducing g with T^k and S"""
    g = sp.Matrix(g); val = 0
    for _ in range(200):
        a, b, c, d = g
        if c == 0:
            # g = +-T^k ; -I = S^2 -> 2*9 = 18 = 6 mod 12
            k = b * a  # a = d = +-1, g = a*[[1, b/a],[0,1]]
            val += (k if a == 1 else k + 6)
            return val % 12
        # left-multiply by T^-q to make |a| < |c|, then by S^-1
        q = sp.floor(sp.Rational(a, c))
        g = T ** (-q) * g if q >= 0 else (T.inv() ** q) * g
        val += q
        g = S.inv() * g; val += 9
    raise RuntimeError


for nm, g in (("T", T), ("S", S), ("A", A), ("B", B), ("[A,B]", C)):
    print("    chi12(%s) = %d" % (nm, chi12(g)))
x, y, z = sp.symbols("x y z", positive=True)
pt = {x: 2 * sp.sqrt(2), y: 2 * sp.sqrt(2), z: 4}
print("    another Fuchsian point (the square torus):", [v for v in pt.values()], "x^2+y^2+z^2-xyz =", sp.simplify((x**2 + y**2 + z**2 - x*y*z).subs(pt)))

H = sp.Matrix([[0, sp.I], [-sp.I, 0]])
print("(b) H Hermitian:", H == H.H, "| eigenvalues", list(H.eigenvals()), "(indefinite) | A^* H A == H:", sp.simplify(A.H * H * A - H) == sp.zeros(2), "| B:", sp.simplify(B.H * H * B - H) == sp.zeros(2))

# (c) the seat's route: E = K^1/2 + K^-1/2 on H, |dz|^2 := v^2 (curvature -1 metric |dz|^2/v^2, Hermitian convention),
# h = diag(h1, 1/h1) with h1 = |dz^(1/2)|^2 = v;  Phi = c N dz, N(e1) = e2.
u, v = sp.symbols("u v", real=True); c = sp.symbols("c", positive=True)
ddb = lambda f: sp.Rational(1, 4) * (sp.diff(f, u, 2) + sp.diff(f, v, 2))
h1 = v
F1 = -ddb(sp.log(h1))                               # coefficient of dz^dzbar of the Chern curvature on e1
# (Phi* Phi)(e1) = |c|^2 |e2|^2/|e1|^2 e1 dzbar^dz = -|c|^2 h1^-2 e1 dz^dzbar ; (Phi Phi*)(e1) = 0
comm1 = -c**2 / h1**2
print("(c) seat's route: F1 =", sp.simplify(F1), "| [Phi,Phi*] on e1 =", comm1, "| F + [Phi,Phi*] = 0 gives c =", sp.solve(sp.Eq(F1 + comm1, 0), c))
print("    wrong sign F - [Phi,Phi*] = 0 gives c =", sp.solve(sp.Eq(F1 - comm1, 0), c), "(no positive solution)")
# general ansatz with Phi = N dz (c = 1) and h1 = mu^(-1/2), mu = k v^p
k, p = sp.symbols("k p", real=True)
mu = k * v**p
eq = sp.simplify((-ddb(sp.log(mu**sp.Rational(-1, 2))) - mu) * v**2)
print("    Phi = unit: F1 - mu = 0 with mu = k v^p ->", sp.factor(eq), "-> needs p = -2 and k = 1/4")
# (d) |Phi|^2 at the solution mu = 1/(4 v^2): tr(phi phi*) = mu
trpp = 1 / (4 * v**2)
lam = 1 / v**2                                       # curvature -1 metric lam |dz|^2
conv = {"|dz|^2 = 1/lam (the arc's and the seat's)": trpp / lam,
        "|dz|^2 = 2/lam (Riemannian norm of the complex 1-form du + i dv)": trpp * 2 / lam,
        "Hitchin's ||Phi||^2 = 2i int tr(Phi ^ Phi*), density per dA": None}
# 2i tr(Phi ^ Phi*) = 2i * trpp * dz^dzbar = 2i * trpp * (-2i) du^dv = 4 trpp du dv ; dA = lam du dv
dens_H = sp.simplify(4 * trpp / lam)
conv["Hitchin's ||Phi||^2 = 2i int tr(Phi ^ Phi*), density per dA"] = dens_H
area = 2 * sp.pi
for nm, val in conv.items():
    print("    %-70s |Phi|^2 = %s, |Phi| = %s, integral = %s" % (nm, val, sp.sqrt(val), val * area))
print("    convention-free: 2i tr(Phi ^ Phi*) / dA_(-1) =", dens_H, "(the harmonic metric's Phi has the hyperbolic area form as its density)")
# the harmonic map: for the Fuchsian datum the equivariant harmonic map H^2 -> H^2 (in H^3) is the identity isometry, energy
# density |df|^2 = 2 (two orthonormal directions). With Psi = Phi + Phi* and the symmetric-space metric 2 tr(XY) (curvature -1):
# |Psi|^2 = 2 * (2 tr(phi phi*) + 2 tr(phi phi*)) * |d/du|^2... per unit vector: 8 tr(phi phi*) v^2
print("    harmonic-map check: 8 tr(phi phi*) v^2 =", sp.simplify(8 * trpp * v**2), "(= 2 = |d id|^2 for the identity isometry: the curvature -4 solution is the uniformisation)")
print("w130_ref exit 0")
