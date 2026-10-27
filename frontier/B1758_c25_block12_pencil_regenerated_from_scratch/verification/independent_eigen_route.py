"""B1758 (main's re-banking): main's audit, the independent numerical route -- det14 at mu's three real roots by eigendecomposition on W4 at 60 digits (no F-trace, no Newton identities), against B1758's polynomial and B893's floats; and B892's wall semantics. Written by main's read-only auditor, carried with the B854 path made repository-relative.
"""
"""Independent audit of B1758 (numerical parts + B892 wall semantics). Uses the patched B854 (shown identical in audit1)."""
import io, contextlib, time
from fractions import Fraction as Fr
import numpy as np
import sympy as sp
from sympy.polys.matrices import DomainMatrix
import mpmath
from mpmath import mp

import pathlib
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
B854 = str(ROOT / "frontier" / "B854_centralizer_exact" / "e6_centralizer.py")
t0 = time.time()
src = open(B854).read()
pat = src.replace("for _ in range(4000):", "for _ in range(0):")
old_loop = """for n in [8, 14, 16, 22]:
    P = sp.zeros(n+1, n+1)
    for M in G:
        P += symn(M, n)
    P = sp.simplify(P / 24)
    col = [P.col(j) for j in range(n+1) if any(P.col(j))][0]
    d = sp.lcm([sp.Rational(c).q for c in col]); g = sp.gcd([sp.Rational(c*d).p for c in col])
    Ipoly[n] = [sp.Rational(c*d/g) for c in col]"""
new_loop = """for n in [8, 14, 16]:
    for k_col in range(n+1):
        col = [sp.Integer(0)] * (n+1)
        for M in G:
            X = M[0,0]*x + M[1,0]*y; Y = M[0,1]*x + M[1,1]*y
            p = sp.Poly(sp.expand(X**(n-k_col)*Y**k_col), x, y)
            for j in range(n+1):
                col[j] += p.coeff_monomial(x**(n-j)*y**j)
        col = [sp.simplify(c / 24) for c in col]
        if any(col):
            break
    d = sp.lcm([sp.Rational(c).q for c in col]); g = sp.gcd([sp.Rational(c*d).p for c in col])
    Ipoly[n] = [sp.Rational(c*d/g) for c in col]"""
pat = pat.replace(old_loop, new_loop).replace("for n in [8, 14, 16, 22]:", "for n in [8, 14, 16]:")
pat = pat.split("# ---------------------------------------------------------------- VERIFY closure")[0]
env = {}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(pat, "b854_pat", "exec"), env)
br, hvec, evec, ROOTS, DIM, N, INV = (env[k] for k in ("br", "hvec", "evec", "ROOTS", "DIM", "N", "INV"))

def admat(v):
    cols = [br(v, hvec(j) if j < N else evec(ROOTS[j - N])) for j in range(DIM)]
    return sp.Matrix(DIM, DIM, lambda i, j: sp.Rational(cols[j][i].numerator, cols[j][i].denominator))
A = {n: admat(INV[n]) for n in (8, 14, 16)}
t = sp.Symbol("t")
f6 = sp.Poly(t**6 + 19856793600*t**4 + 98573063018250240000*t**2 + 142198242829436706619392000000, t)
D14 = DomainMatrix.from_Matrix(A[14]).convert_to(sp.QQ)
Pf = DomainMatrix.zeros((78, 78), sp.QQ); powk = DomainMatrix.eye(78, sp.QQ)
for k, c in enumerate(f6.all_coeffs()[::-1]):
    if k > 0:
        powk = powk * D14
    if c:
        Pf = Pf + powk.scalarmul(sp.QQ.from_sympy(sp.Rational(c)))
Nb = sp.Matrix(Pf.nullspace().to_Matrix().T)
G = (Nb.T * Nb).inv()
def restrict(M):
    R = G * Nb.T * M * Nb
    assert M * Nb == Nb * R
    return R
R8, R14, R16 = (restrict(A[n]) for n in (8, 14, 16))
print(f"built in {time.time()-t0:.1f}s; N12 dim {Nb.cols}")

rho = sp.Symbol("rho")
det14_x = sp.Rational(9084997258444800000, 28561)*rho**2 + sp.Rational(77253378048000, 2197)*rho + sp.Rational(461060812800, 169)
e_x = -sp.Rational(752150557025548369920000, 4826809)*rho**2 + sp.Rational(159895951748628480000, 371293)*rho + sp.Rational(82022486586163200, 28561)
B893 = [3854784701.3353987, 2792616188.7290025, 13209392709.935598]

# (f) direct numerical route at each real root (60 digits): W4 = null(R8 + rho R16); R16|W4 eigenspaces; det of R14 on +gamma eigenspace
mp.dps = 60
def tomp(M):
    return mp.matrix([[mp.mpf(sp.Rational(M[i, j]).p) / mp.mpf(sp.Rational(M[i, j]).q) for j in range(M.cols)] for i in range(M.rows)])
m8, m14, m16 = tomp(R8), tomp(R14), tomp(R16)
roots = sorted([mp.re(z) for z in mpmath.polyroots([mp.mpf(c) for c in (500716339200, -2075673600, -4769856, 2197)], maxsteps=500, extraprec=300)])
def solve_mat(Amat, Bmat):
    cols = [mpmath.lu_solve(Amat, Bmat[:, j]) for j in range(Bmat.cols)]
    X = mp.matrix(Amat.cols, Bmat.cols)
    for j, c in enumerate(cols):
        for i in range(Amat.cols):
            X[i, j] = c[i]
    return X
rows = []
for i, r in enumerate(roots):
    U, S, V = mpmath.svd_r(m8 + r * m16)
    nul = [k for k in range(12) if S[k] < S[0] * mp.mpf(10) ** -40]
    gap = (min(S[k] for k in range(12) if k not in nul) / S[0], max(S[k] for k in nul) / S[0])
    W = mp.matrix(12, len(nul))
    for c, k in enumerate(nul):
        for j in range(12):
            W[j, c] = V[k, j]
    T16, T14 = W.T * m16 * W, W.T * m14 * W
    ev, Q = mpmath.eig(T16)
    gam = max(mp.re(x) for x in ev)
    plus = [k for k in range(len(ev)) if abs(ev[k] - gam) < abs(gam) * mp.mpf(10) ** -30]
    Qp = mp.matrix(len(nul), len(plus))
    for c, k in enumerate(plus):
        for j in range(len(nul)):
            Qp[j, c] = Q[j, k]
    X = solve_mat(Qp.H * Qp, Qp.H * (T14 * Qp))
    resid = mpmath.mnorm(T14 * Qp - Qp * X, 1)
    d2 = X[0, 0] * X[1, 1] - X[0, 1] * X[1, 0]
    tr2 = X[0, 0] + X[1, 1]
    rr = sp.Float(mpmath.nstr(r, 55), 55)
    print(f"[f] root {i}: rho = {mpmath.nstr(r, 17)}; dim W4 = {len(nul)} (sv gap: smallest nonnull/s0 = {mpmath.nstr(gap[0],3)}, largest null/s0 = {mpmath.nstr(gap[1],3)}); +gamma dim {len(plus)}")
    print(f"      gamma^2 direct = {mpmath.nstr(gam**2, 20)};  e(rho) poly = {sp.N(e_x.subs(rho, rr), 20)}")
    print(f"      det(R14|V+) direct = {mpmath.nstr(mp.re(d2), 20)} (Im {mpmath.nstr(mp.im(d2), 2)}; |tr| {mpmath.nstr(abs(tr2), 2)}; invariance resid {mpmath.nstr(resid, 2)})")
    print(f"      det14 poly (B1758) = {sp.N(det14_x.subs(rho, rr), 20)};  B893 float = {B893[i]}")
    rows.append((float(r), float(gam), float(mp.re(d2))))

# (w) B892's wall semantics on full e6 (78-dim, numpy complex128): nullity of [ad x1; ad y] for
#     y* = gamma x14 - a x16 with a^2 = -det14 (a imaginary), vs controls a = sqrt(+det14) (real) and a generic y
An = {n: np.array(A[n].evalf(30).tolist(), dtype=float) for n in A}
def nullity(Ms):
    St = np.vstack(Ms)
    s = np.linalg.svd(St, compute_uv=False)
    k = int(np.sum(s < s[0] * 1e-9))
    return k, s
for i, (r, gam, d) in enumerate(rows):
    x1 = An[8] + r * An[16]
    for label, a in (("a = i*sqrt(det14) [B892]", 1j * np.sqrt(d)), ("control a = +sqrt(det14)", np.sqrt(d) + 0j), ("control generic y", None)):
        y = (gam * An[14] - a * An[16]) if a is not None else (An[14] + 0.37 * An[16])
        k, s = nullity([x1.astype(complex), y.astype(complex)])
        s_sorted = np.sort(s)
        print(f"[w] root {i} {label:28s}: nullity {k}  (sigma_k/s0 around the cut: {s_sorted[k-1]/s[0]:.1e} | {s_sorted[k]/s[0]:.1e})")
    k1, s1 = nullity([(An[8] + r * An[16]).astype(complex)])
    print(f"[w] root {i} dim ker ad(x1) alone = {k1}")
print(f"done in {time.time()-t0:.1f}s")
