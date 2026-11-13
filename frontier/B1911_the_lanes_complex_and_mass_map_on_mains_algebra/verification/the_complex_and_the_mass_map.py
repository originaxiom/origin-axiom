"""WP-2.1, its first step: the physical lane's elliptic complex and fermion mass map, checked with main's own algebra.

Read through main's binding-minimum mask (statements only, none of the lane's code run):
  reports/physical_bridge_2026_09_05/weave_two_neutral_index_2026_10_08/PROOF.md   (the complex: C0..C3, D0, D1, D2, metrics)
  reports/physical_bridge_2026_09_05/weave_physical_mass_2026_10_08/PROOF.md      (W2, its Hessian, D0+, D2+, M, Uin, Uout)
at the lane's 1aa76251f.

THE MODEL. The algebraic identities are local, so they are checked on a periodic square (a spectral grid, N x N), with
gl(3)-valued fields that are smooth and random, a smooth positive Omega, and Dbar = d_x + i d_y - i ad A,
Dz = d_x - i d_y - i ad A^dagger (A a smooth background). kappa(X, Y) = tr(XY) is the bilinear pairing; the Hermitian
pairing is tr(X^dagger Y); integration is the mean over the grid. The spectral derivative is exactly skew-adjoint on the
grid, so adjoint identities hold to rounding; the Leibniz rule holds up to aliasing, small for smooth fields.
WHAT IS NOT CHECKED: the punctured hyperbolic surface, the cusp, the complete domains, the Fredholm property and the index;
the background's existence (D-bar q = D-bar r = [q, r] = 0 is a hypothesis of the complex, and E4 shows it is exactly what
the complex needs).

THE CHECKS (each with a planted wrong form that must fail):
  E1 the Hessian of W2 = int kappa(u Dbar v + i a([q,v] - [r,u])) has density dual coefficients (i t, p2, -p1),
     p1 = Dbar u + i[q,a], p2 = Dbar v + i[r,a], t = [q,v] - [r,u]                       [plant: (i t, p2, +p1)]
  E2 D0 eps = sqrt2 (Dbar eps, -i[q,eps], -i[r,eps]) has adjoint D0+ x = -[Dz a - 2i Omega([q+,u] + [r+,v])]/(sqrt2 Omega^2)
     in the metrics C0: Omega^2, C1: diag(1/2, Omega, Omega)                                [plant: C1 weight 1 on a]
  E3 D2(p1,p2,t) = Dbar t - [q,p2] + [r,p1] has adjoint D2+ sigma = ((2/Omega)[r+,s], -(2/Omega)[q+,s], -Dz(Omega^-2 s))
     in C2: diag(Omega^-1, Omega^-1, 2) and C3: 2 Omega^-2; the weight 2 on t is derived here (the mask hides the page's)
                                                                                           [plant: t weight 1]
  E4 D1 D0 eps = -i sqrt2 ([Dbar q, eps], [Dbar r, eps], [[q,r], eps]) and D2 D1 x = [Dbar q, v] - [Dbar r, u] - i[[q,r], a],
     identically: the complex closes exactly when Dbar q = Dbar r = [q,r] = 0
  E5 M = Uout T Uin, T(x, s) = (D0+ x, D1 x + D2+ s), Uin(l,a,u,v) = ((a,u,v), i Omega^2 l/sqrt2),
     Uout(g,p1,p2,t) = (g, 2i t, p2/Omega, -p1/Omega): M's four rows as the page writes them      [plant: Uin without Omega^2]
  E6 Uin and Uout are isometries when the four fermion densities are (Omega^2, 1/2, Omega, Omega) for (l, a, u, v)
     (two of the lane's files list three entries for four fields; these four are what isometry requires)
No data.   OMP_NUM_THREADS=1 python3 -B the_complex_and_the_mass_map.py"""
import json, pathlib
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
rng = np.random.default_rng(2101)
N, n, K = 40, 3, 3                                        # grid, gl(n), bandwidth of the random fields
x = np.arange(N) * 2 * np.pi / N
X, Y = np.meshgrid(x, x, indexing="ij")
kx = np.fft.fftfreq(N, 1.0 / N)
KX, KY = np.meshgrid(kx, kx, indexing="ij")

def smooth_scalar(amp=1.0):
    f = np.zeros((N, N))
    for a in range(-K, K + 1):
        for b in range(-K, K + 1):
            c = rng.normal() * amp / (1 + a * a + b * b)
            ph = rng.uniform(0, 2 * np.pi)
            f += c * np.cos(a * X + b * Y + ph)
    return f
def field():
    """a smooth gl(n)-valued field: shape (N, N, n, n)"""
    return np.stack([np.stack([smooth_scalar() + 1j * smooth_scalar() for _ in range(n)], -1) for _ in range(n)], -2)

def d(f, which):
    F = np.fft.fft2(f, axes=(0, 1))
    k = KX if which == "x" else KY
    return np.fft.ifft2(1j * k[..., None, None] * F, axes=(0, 1))
def com(a, b): return a @ b - b @ a
def dag(a): return np.conj(np.swapaxes(a, -1, -2))
def tr(a): return np.trace(a, axis1=-2, axis2=-1)

Om = np.exp(0.3 * smooth_scalar())[..., None, None]      # a smooth positive weight
A, q, r = field(), field(), field()
def Dbar(f): return d(f, "x") + 1j * d(f, "y") - 1j * com(A, f)
def Dz(f): return d(f, "x") - 1j * d(f, "y") - 1j * com(dag(A), f)
def herm(f, g, w): return np.mean(tr(w * (dag(f) @ g)))          # int w tr(f^dagger g)
def bil(f, g): return np.mean(tr(f @ g))                          # int kappa(f g)
CHECKS = []
def check(name, ok, detail):
    CHECKS.append({"check": name, "holds": bool(ok), "detail": detail}); print("%s  %s  [%s]" % ("ok  " if ok else "FAIL", name, detail))
TOL = 1e-9

# E1: the Hessian's dual coefficients
a, u, v = field(), field(), field(); a2, u2, v2 = field(), field(), field()
def W2pol(a, u, v, a2, u2, v2):                                   # the symmetric bilinear polarisation of W2
    return (bil(u, Dbar(v2)) + bil(u2, Dbar(v)) + 1j * bil(a, com(q, v2) - com(r, u2)) + 1j * bil(a2, com(q, v) - com(r, u)))
p1 = Dbar(u) + 1j * com(q, a); p2 = Dbar(v) + 1j * com(r, a); t = com(q, v) - com(r, u)
lhs = W2pol(a, u, v, a2, u2, v2); scale = abs(lhs)
e1 = abs(lhs - (bil(a2, 1j * t) + bil(u2, p2) + bil(v2, -p1))) / scale
e1p = abs(lhs - (bil(a2, 1j * t) + bil(u2, p2) + bil(v2, +p1))) / scale
check("E1 the Hessian's dual coefficients are (i t, p2, -p1)", e1 < TOL, "%.1e" % e1)
check("E1 plant: (i t, p2, +p1) fails", e1p > 1e-3, "%.1e" % e1p)

# E2: D0 and its adjoint
def D0(e): return (np.sqrt(2) * Dbar(e), -1j * np.sqrt(2) * com(q, e), -1j * np.sqrt(2) * com(r, e))
def D0dag(a, u, v): return -(Dz(a) - 2j * Om * (com(dag(q), u) + com(dag(r), v))) / (np.sqrt(2) * Om ** 2)
eps = field()
def C1(f, g, wa=0.5): return herm(f[0], g[0], wa) + herm(f[1], g[1], Om) + herm(f[2], g[2], Om)
l2 = C1(D0(eps), (a, u, v)); r2 = herm(eps, D0dag(a, u, v), Om ** 2)
e2 = abs(l2 - r2) / abs(l2)
e2p = abs(C1(D0(eps), (a, u, v), wa=1.0) - r2) / abs(l2)
check("E2 D0+ is D0's adjoint in C0: Omega^2, C1: diag(1/2, Omega, Omega)", e2 < TOL, "%.1e" % e2)
check("E2 plant: weight 1 on a in C1 fails", e2p > 1e-3, "%.1e" % e2p)

# E3: D2 and its adjoint
def D2(p1, p2, t): return Dbar(t) - com(q, p2) + com(r, p1)
def D2dag(s): return ((2 / Om) * com(dag(r), s), -(2 / Om) * com(dag(q), s), -Dz(s / Om ** 2))
P1, P2, T3, sig = field(), field(), field(), field()
def C2(f, g, wt=2.0): return herm(f[0], g[0], 1 / Om) + herm(f[1], g[1], 1 / Om) + herm(f[2], g[2], wt)
l3 = herm(D2(P1, P2, T3), sig, 2 / Om ** 2); r3 = C2((P1, P2, T3), D2dag(sig))
e3 = abs(l3 - r3) / abs(l3); e3p = abs(l3 - C2((P1, P2, T3), D2dag(sig), wt=1.0)) / abs(l3)
check("E3 D2+ is D2's adjoint in C2: diag(Omega^-1, Omega^-1, 2), C3: 2 Omega^-2", e3 < TOL, "%.1e" % e3)
check("E3 plant: weight 1 on t in C2 fails", e3p > 1e-3, "%.1e" % e3p)

# E4: the complex closes exactly on the background conditions
def D1(a, u, v): return (Dbar(u) + 1j * com(q, a), Dbar(v) + 1j * com(r, a), com(q, v) - com(r, u))
dd = D1(*D0(eps)); want = (-1j * np.sqrt(2) * com(Dbar(q), eps), -1j * np.sqrt(2) * com(Dbar(r), eps), -1j * np.sqrt(2) * com(com(q, r), eps))
e4a = max(np.max(np.abs(dd[i] - want[i])) for i in range(3)) / max(np.max(np.abs(w)) for w in want)
dd2 = D2(*D1(a, u, v)); want2 = com(Dbar(q), v) - com(Dbar(r), u) - 1j * com(com(q, r), a)
e4b = np.max(np.abs(dd2 - want2)) / np.max(np.abs(want2))
check("E4 D1 D0 eps = -i sqrt2 ([Dbar q, eps], [Dbar r, eps], [[q,r], eps])", e4a < 1e-6, "%.1e (aliasing of products)" % e4a)
check("E4 D2 D1 x = [Dbar q, v] - [Dbar r, u] - i[[q,r], a]", e4b < 1e-6, "%.1e (aliasing of products)" % e4b)

# E5: M = Uout T Uin, row by row
lam = field()
def Uin(l, a, u, v, om_power=2): return (a, u, v), 1j * Om ** om_power * l / np.sqrt(2)
def Uout(g, p1, p2, t): return (g, 2j * t, p2 / Om, -p1 / Om)
def T(xx, s):
    d1 = D1(*xx); d2 = D2dag(s)
    return D0dag(*xx), d1[0] + d2[0], d1[1] + d2[1], d1[2] + d2[2]
def M_page(l, a, u, v):
    p1 = Dbar(u) + 1j * com(q, a); p2 = Dbar(v) + 1j * com(r, a); t = com(q, v) - com(r, u)
    return (D0dag(a, u, v), 2j * t + np.sqrt(2) * Dz(l), p2 / Om - np.sqrt(2) * 1j * com(dag(q), l), -p1 / Om - np.sqrt(2) * 1j * com(dag(r), l))
got = Uout(*T(*Uin(lam, a, u, v))); page = M_page(lam, a, u, v)
e5 = max(np.max(np.abs(got[i] - page[i])) / np.max(np.abs(page[i])) for i in range(4))
gotp = Uout(*T(*Uin(lam, a, u, v, om_power=0)))
e5p = max(np.max(np.abs(gotp[i] - page[i])) / np.max(np.abs(page[i])) for i in range(4))
check("E5 M = Uout T Uin: the page's four rows", e5 < TOL, "%.1e" % e5)
check("E5 plant: Uin without Omega^2 fails", e5p > 1e-3, "%.1e" % e5p)

# E6: Uin and Uout are isometries for the densities (Omega^2, 1/2, Omega, Omega)
def phys(l, a, u, v): return herm(l, l, Om ** 2) + herm(a, a, 0.5) + herm(u, u, Om) + herm(v, v, Om)
(xa, xu, xv), s = Uin(lam, a, u, v)
e6a = abs(phys(lam, a, u, v) - (C1((xa, xu, xv), (xa, xu, xv)) + herm(s, s, 2 / Om ** 2))) / abs(phys(lam, a, u, v))
g = field()
out = Uout(g, P1, P2, T3)
e6b = abs(phys(*out) - (herm(g, g, Om ** 2) + C2((P1, P2, T3), (P1, P2, T3)))) / abs(phys(*out))
check("E6 Uin is an isometry onto C1 + C3 for the densities (Omega^2, 1/2, Omega, Omega)", e6a < TOL, "%.1e" % e6a)
check("E6 Uout is an isometry from C0 + C2 for the same densities", e6b < TOL, "%.1e" % e6b)

# E7: the gauge-fixed potential. A real connection (A_x, A_y Hermitian), a in one charge block q of a diagonal Z with
# k = n_flux q, a_x = (a + a^dagger)/2, a_y = (a - a^dagger)/(2i); m0 = -n_flux Z Omega^2.
def herm_field():
    f = field(); return (f + dag(f)) / 2
Ax, Ay = herm_field(), herm_field()
A_saved = A
A = Ax + 1j * Ay                                                  # Dbar and Dz read this name
def Dx(f): return d(f, "x") - 1j * com(Ax, f)
def Dy(f): return d(f, "y") - 1j * com(Ay, f)
zdiag = np.array([1.0, 0.0, -1.0]); Zm = np.diag(zdiag).astype(complex); qch = 1.0; nflux = 2.0; kk = nflux * qch
mask = (np.subtract.outer(zdiag, zdiag) == qch).astype(complex)          # the entries of charge q
ac, uc, vc = field() * mask, field() * mask, field() * mask
ax, ay = (ac + dag(ac)) / 2, (ac - dag(ac)) / 2j
f1 = Dx(ay) - Dy(ax)
P = Om * (com(dag(q), uc) + com(dag(r), vc))
M1 = f1 + Om * (com(uc, dag(q)) + com(q, dag(uc)) + com(vc, dag(r)) + com(r, dag(vc)))
M2 = -1j * com(ax, ay) + Om * (com(uc, dag(uc)) + com(vc, dag(vc)))
G = Dx(ax) + Dy(ay) - 1j * Om * (com(dag(q), uc) + com(q, dag(uc)) + com(dag(r), vc) + com(r, dag(vc)))
m0 = -nflux * Zm * Om ** 2
p1c = Dbar(uc) + 1j * com(q, ac); p2c = Dbar(vc) + 1j * com(r, ac); tc = com(q, vc) - com(r, uc)
V2 = (np.mean(tr((1 / Om) * (dag(p1c) @ p1c + dag(p2c) @ p2c))) + np.mean(tr(2 * dag(tc) @ tc))
      + np.mean(tr(M1 @ M1 / (2 * Om ** 2))) + np.mean(tr(m0 @ M2 / Om ** 2)))
V2gf = V2 + np.mean(tr(G @ G / (2 * Om ** 2)))
xnorm = herm(ac, ac, 0.5) + herm(uc, uc, Om) + herm(vc, vc, Om)
rhs = herm(D0dag(ac, uc, vc), D0dag(ac, uc, vc), Om ** 2) + C2(D1(ac, uc, vc), D1(ac, uc, vc)) - kk * xnorm
e7 = abs(V2gf - rhs) / abs(rhs)
check("E7 g6^2 V2_gf = |D0+ x|^2 + |D1 x|^2 - k|x|^2 (the conjugate-pair identity and the soft term on a charge block)", e7 < 1e-9, "%.1e" % e7)
dz_split = np.max(np.abs((Dz(ac) - 2j * P) - (G + 1j * M1))) / np.max(np.abs(G))
check("E7 Dz a - 2i Omega([q+,u] + [r+,v]) = G + i M1, with G and M1 Hermitian", dz_split < 1e-9 and np.max(np.abs(G - dag(G))) < 1e-9 and np.max(np.abs(M1 - dag(M1))) < 1e-9, "%.1e" % dz_split)
e7p = abs(V2gf - (rhs + kk * xnorm - 2 * kk * xnorm)) / abs(rhs)                 # planted: the soft term with +k
check("E7 plant: the soft term as +k|x|^2 fails", abs(V2gf - (rhs + 2 * kk * xnorm)) / abs(rhs) > 1e-3, "%.1e" % (abs(V2gf - (rhs + 2 * kk * xnorm)) / abs(rhs)))
A = A_saved

# E9: on a background where the complex closes (A, q, r diagonal, so commuting), |T(x,s)|^2 splits with no cross term
A_saved2, q_saved, r_saved = A, q, r
def diag_field():
    return np.stack([np.stack([(smooth_scalar() + 1j * smooth_scalar()) if i == j else np.zeros((N, N)) for j in range(n)], -1) for i in range(n)], -2)
A = diag_field(); q = np.diag(rng.normal(size=n) + 1j * rng.normal(size=n))[None, None] * np.ones((N, N, 1, 1)); r = np.diag(rng.normal(size=n) + 1j * rng.normal(size=n))[None, None] * np.ones((N, N, 1, 1))
closes = np.max(np.abs(D2(*D1(a, u, v)))) / np.max(np.abs(D1(a, u, v)[0]))
Tx = T((a, u, v), sig)
lhs9 = herm(Tx[0], Tx[0], Om ** 2) + C2(Tx[1:], Tx[1:])
rhs9 = herm(D0dag(a, u, v), D0dag(a, u, v), Om ** 2) + C2(D1(a, u, v), D1(a, u, v)) + C2(D2dag(sig), D2dag(sig))
e9 = abs(lhs9 - rhs9) / abs(rhs9)
check("E9 on a closed background (|D2 D1 x| = %.0e) |T(x,s)|^2 = |D0+ x|^2 + |D1 x|^2 + |D2+ s|^2" % closes, e9 < 1e-9, "%.1e" % e9)
A, q, r = A_saved2, q_saved, r_saved
Tg = T((a, u, v), sig)
lhsg = herm(Tg[0], Tg[0], Om ** 2) + C2(Tg[1:], Tg[1:]); rhsg = herm(D0dag(a, u, v), D0dag(a, u, v), Om ** 2) + C2(D1(a, u, v), D1(a, u, v)) + C2(D2dag(sig), D2dag(sig))
check("E9 control: on a generic background (the complex open) the cross term is not zero", abs(lhsg - rhsg) / abs(rhsg) > 1e-3, "%.1e" % (abs(lhsg - rhsg) / abs(rhsg)))

# E8: the cusp block at h = 1, from the second half of the complex (symbolic)
import sympy as sy
tt, kS, mS, ellS = sy.symbols("t k m ell", real=True)
vf, al = sy.Function("v")(tt), sy.Function("alpha")(tt)
yS = sy.exp(tt)
h = 1; delta = kS + (mS + 1 - h) / sy.Integer(2); bS = ellS / sy.sqrt(2)
vy = sy.diff(vf, tt) / yS                                          # d/dy = e^-t d/dt
sigma = al / (sy.sqrt(2) * yS ** sy.Rational(3, 2)); sigy = sy.diff(sigma, tt) / yS
res1 = sy.I * (vy + (mS + 2 * kS) * vf / (2 * yS)) - ellS * al / (sy.sqrt(2) * yS)
res2 = ellS * vf / (2 * sy.sqrt(yS)) + sy.I * (yS ** 2 * sigy + (3 - mS - 2 * kS) * yS * sigma / 2)
b1 = sy.simplify(sy.expand(yS * res1 - (sy.I * (sy.diff(vf, tt) + delta * vf) - bS * al)))
b2 = sy.simplify(sy.expand(sy.sqrt(2 * yS) * res2 - (bS * vf + sy.I * (sy.diff(al, tt) - delta * al))))
check("E8 the h = 1 cusp block: y * residual 1 = i(d_t + delta)v - b alpha, sqrt(2y) * residual 2 = b v + i(d_t - delta)alpha", b1 == 0 and b2 == 0, "%s, %s" % (b1, b2))

if __name__ == "__main__":
    json.dump({"grid": N, "algebra": "gl(%d)" % n, "checks": CHECKS, "failing": [c["check"] for c in CHECKS if not c["holds"]]},
              open(HERE / "the_complex_and_the_mass_map.json", "w"), indent=1)
