#!/usr/bin/env python3
"""The periodic curve through a background, and the torsion of every sector along it  (numerics, mpmath).

State (eps, word), level k.  Phi = (tau_{w1} o ... o tau_{wn})^k, composed with iota (g -> c g^-1 c^-1, c = yx) when
eps^k = -1.  A character l of the level (fixed by Phi on the fibre, trivial on the meridian) has a square root v on the
fibre; the diagonal representation diag(v, 1/v) is a torsion point p0 on kappa = 2 with  T(p0) = sigma p0  for a sign
twist sigma.  Through p0 passes one curve of solutions of T(p) = sigma p; it is followed to kappa = 2 - e.  There the
fibre representation rho is irreducible, the meridian is the intertwiner T (det 1, T -> 1 as e -> 0), and the sector with
quotient character beta is the module  x -> (v beta)(x) rho(x), y -> (v beta)(y) rho(y), t -> T.
Its torsion is  det(T - J) / det(T - 1),  J the Fox matrix of Phi.
"""
import sys, itertools, json
from fractions import Fraction
from mpmath import mp, mpf, mpc, matrix, sqrt, det, exp, pi, log, eye, zeros, inverse, lu_solve, svd_c, nstr
mp.dps = 60

# ---------------------------------------------------------------- words (letters 1 = x, 2 = y, negative = inverse)
def inv_word(w): return tuple(-c for c in reversed(w))
def reduce_word(w):
    out = []
    for c in w:
        if out and out[-1] == -c: out.pop()
        else: out.append(c)
    return tuple(out)
def subst(w, img):
    out = []
    for c in w: out.extend(img[c] if c > 0 else inv_word(img[-c]))
    return reduce_word(out)
LET = {"L": {1: (1,), 2: (2, 1)}, "R": {1: (1, 2), 2: (2,)}}
IOTA = {1: (2, 1, -1, -1, -2), 2: (2, 1, -2, -1, -2)}             # g -> c g^-1 c^-1 with c = yx
def monodromy(eps, word, k):
    img = {1: (1,), 2: (2,)}
    one = {1: (1,), 2: (2,)}
    for c in reversed(word): one = {g: subst(one[g], LET[c]) for g in (1, 2)}      # tau_{w1} o ... o tau_{wn}
    if eps < 0: one = {g: subst(one[g], IOTA) for g in (1, 2)}                      # Phi = Phi_+ o iota  (images under iota, then Phi_+): g -> Phi_+(iota(g))
    for _ in range(k): img = {g: subst(img[g], one) for g in (1, 2)}
    return img
def ab(w): return (sum((c == 1) - (c == -1) for c in w), sum((c == 2) - (c == -2) for c in w))

# ---------------------------------------------------------------- characters and slopes
def level_characters(Phi, N):
    (a, b), (c, d) = ab(Phi[1]), ab(Phi[2])
    return [(p, q) for p in range(N) for q in range(N) if (a * p + b * q - p) % N == 0 and (c * p + d * q - q) % N == 0]
def torsion_order(Phi):
    (a, b), (c, d) = ab(Phi[1]), ab(Phi[2]); return abs((a - 1) * (d - 1) - b * c)
def exponent(Phi):
    """the exponent of the fibre torsion: the least N for which the characters of order dividing N are all of them"""
    t = torsion_order(Phi)
    for n in range(1, t + 1):
        if t % n == 0 or True:
            if len(level_characters(Phi, n)) == t: return n
def fox(w, g):
    """Fox derivatives of w in the representation g = {1: gx, 2: gy} (matrices or scalars as 1x1)"""
    n = g[1].rows; D = {1: zeros(n), 2: zeros(n)}; pre = eye(n); gi = {1: inverse(g[1]), 2: inverse(g[2])}
    for c in w:
        if c > 0: D[c] += pre; pre = pre * g[c]
        else: pre = pre * gi[-c]; D[-c] -= pre
    return D[1], D[2], pre
def slope(Phi, p, q, N):
    z = exp(2j * pi / N); g = {1: matrix([[z ** p]]), 2: matrix([[z ** q]])}; cx, cy = g[1][0, 0], g[2][0, 0]
    xx, xy, _ = fox(Phi[1], g); yx, yy, _ = fox(Phi[2], g)
    M = matrix([[1 - xx[0, 0], -xy[0, 0], 1 - cx], [-yx[0, 0], 1 - yy[0, 0], 1 - cy]])
    r = max(([M[i, j] for j in range(3)] for i in range(2)), key=lambda row: sum(abs(c) for c in row))
    o = [M[1, j] for j in range(3)] if r == [M[0, j] for j in range(3)] else [M[0, j] for j in range(3)]
    piv = max(range(3), key=lambda j: abs(r[j]))
    assert all(abs(o[j] * r[piv] - r[j] * o[piv]) < mpf(10) ** (-30) for j in range(3)), "h^1 of a character is a line"
    cands = [(r[1], -r[0], mpc(0)), (r[2], mpc(0), -r[0]), (mpc(0), r[2], -r[1])]      # cocycles; the class is the one not a coboundary
    lamf = lambda zz: (1 - cy) * zz[0] + (cx - 1) * zz[1]
    zx, zy, zt = max(cands, key=lambda zz: abs(lamf(zz))); lam = lamf((zx, zy, zt))
    assert abs(lam) > mpf(10) ** (-20), "the class is non-zero on the longitude"
    s = zt / lam; assert abs(s.imag) < mpf(10) ** (-25), s
    return s.real

# ---------------------------------------------------------------- the fibre representation and the curve
def rep(p):
    X, Y, Z = p; q = (Z + sqrt(Z * Z - 4)) / 2
    return {1: matrix([[X, -1], [1, 0]]), 2: matrix([[0, q], [-1 / q, Y]])}
def wordmat(w, g):
    r = eye(g[1].rows); gi = None
    for c in w:
        if c > 0: r = r * g[c]
        else:
            if gi is None: gi = {1: inverse(g[1]), 2: inverse(g[2])}
            r = r * gi[-c]
    return r
def tr(m): return m[0, 0] + m[1, 1]
def kappa(p): X, Y, Z = p; return X * X + Y * Y + Z * Z - X * Y * Z - 2
def tracemap(Phi, p):
    g = rep(p); a, b = wordmat(Phi[1], g), wordmat(Phi[2], g)
    return (tr(a), tr(b), tr(a * b))
def follow(Phi, p0, sig, e, steps=None):
    """the point of the curve T(p) = sig p through p0 with kappa = 2 - e, by continuation in e from the torsion point"""
    e = mpc(e); first = mpf("1e-6")
    if abs(e) <= first: return newton(Phi, p0, sig, e)
    cur = first * e / abs(e); p = newton(Phi, p0, sig, cur); step = cur
    while abs(cur - e) > mpf(10) ** (-50):
        step = min(abs(e - cur), 2 * abs(step)) * (e - cur) / abs(e - cur)
        while True:
            try: q = newton(Phi, p, sig, cur + step); break
            except (AssertionError, ZeroDivisionError):
                step = step / 4
                if abs(step) < mpf(10) ** (-12): raise AssertionError("continuation stalled at e = %s" % nstr(cur, 8))
        p = q; cur = cur + step
    return p
def newton(Phi, p0, sig, e):
    def F(p):
        q = tracemap(Phi, p); return [q[i] - sig[i] * p[i] for i in range(3)] + [kappa(p) - (2 - e)]
    p = [mpc(c) for c in p0]
    # first step along the tangent: kernel of d(T - sig) at p0, scaled so that d kappa = -e
    h = mpf(10) ** (-20)
    def jac(p):
        f0 = F(p); J = zeros(4, 3)
        for j in range(3):
            pp = list(p); pp[j] += h; f1 = F(pp)
            for i in range(4): J[i, j] = (f1[i] - f0[i]) / h
        return J, f0
    for it in range(60):
        J, f0 = jac(p)
        # Gauss-Newton: least squares on the 4 x 3 system
        A = J.H * J; b = J.H * matrix(f0)
        d = lu_solve(A, -b)
        p = [p[i] + d[i] for i in range(3)]
        if max(abs(d[i]) for i in range(3)) < mpf(10) ** (-45): break
    res = max(abs(c) for c in F(p)); assert res < mpf(10) ** (-35), ("curve point not found", res)
    assert max(abs(p[i] - p0[i]) for i in range(3)) < 1, "jumped to another branch"
    return p
def intertwiner(Phi, g, sig):
    Px, Py = wordmat(Phi[1], g), wordmat(Phi[2], g); rows = []
    for gg, P, s in ((g[1], Px, sig[0]), (g[2], Py, sig[1])):
        for i in range(2):
            for j in range(2):
                row = [mpc(0)] * 4
                for a in range(2):
                    for b in range(2):
                        if a == i: row[2 * a + b] += gg[b, j]
                        if b == j: row[2 * a + b] -= s * P[i, a]
                rows.append(row)
    U, S, Vh = svd_c(matrix(rows)); assert abs(S[3]) < mpf(10) ** (-30) < abs(S[2]), [nstr(S[i], 5) for i in range(4)]
    v = [Vh[3, i].conjugate() for i in range(4)]; T = matrix([[v[0], v[1]], [v[2], v[3]]]); T = T / sqrt(det(T))
    if tr(T).real < 0: T = -T
    return T
def sector_torsion(Phi, g, T, ax, ay, check=True):
    h = {1: ax * g[1], 2: ay * g[2]}
    if check:
        for c in (1, 2):
            e = T * h[c] * inverse(T) - wordmat(Phi[c], h)
            assert max(abs(e[a, b]) for a in range(2) for b in range(2)) < mpf(10) ** (-25), "not a module"
    xx, xy, _ = fox(Phi[1], h); yx, yy, _ = fox(Phi[2], h); Ti = inverse(T)
    # the monodromy on cocycles z = (z(x), z(y)) in V^2:  (Phi^* z)(g) = T^-1 z(Phi(g))
    P = zeros(4); blocks = ((Ti * xx, Ti * xy), (Ti * yx, Ti * yy))
    for I in range(2):
        for J in range(2):
            for a in range(2):
                for b in range(2): P[2 * I + a, 2 * J + b] = blocks[I][J][a, b]
    # coboundaries: v -> ((h_x - 1) v, (h_y - 1) v);  H^1 = V^2 / B^1 ;  Q = two left null vectors of the 4 x 2 matrix
    Bm = zeros(4, 2)
    for a in range(2):
        for b in range(2): Bm[a, b] = h[1][a, b] - (a == b); Bm[2 + a, b] = h[2][a, b] - (a == b)
    U, S, Vh = svd_c(Bm, full_matrices=True)
    assert abs(S[1]) > mpf(10) ** (-20), "no invariants on the fibre"
    Q = zeros(2, 4)
    for r in range(2):
        for cidx in range(4): Q[r, cidx] = U[cidx, 2 + r].conjugate()
    QP = Q * P; Qp = Q.H * inverse(Q * Q.H)                      # right inverse of Q
    Pb = QP * Qp
    assert max(abs((QP - Pb * Q)[i, j]) for i in range(2) for j in range(4)) < mpf(10) ** (-25), "the monodromy preserves the coboundaries"
    return det(eye(2) - Pb), tr(Pb), det(Pb)

class Background:
    def __init__(self, eps, word, k, ell, N=None):
        self.Phi = monodromy(eps, word, k); self.N = N or exponent(self.Phi); N = self.N
        self.chars = level_characters(self.Phi, N); assert tuple(ell) in self.chars
        self.ell = tuple(ell); z = exp(1j * pi / N); self.v = (z ** ell[0], z ** ell[1])
        vx, vy = self.v; self.p0 = (vx + 1 / vx, vy + 1 / vy, vx * vy + 1 / (vx * vy))
        def val(w, a):
            r = mpc(1)
            for c in w: r *= a[abs(c) - 1] if c > 0 else 1 / a[abs(c) - 1]
            return r
        self.val = val
        sx = val(self.Phi[1], self.v) / vx; sy = val(self.Phi[2], self.v) / vy
        assert abs(abs(sx.real) - 1) < mpf(10) ** (-30) and abs(abs(sy.real) - 1) < mpf(10) ** (-30), (sx, sy)
        sx, sy = int(round(sx.real)), int(round(sy.real)); self.sig = (sx, sy, sx * sy)
        q0 = tracemap(self.Phi, self.p0)
        assert all(abs(q0[i] - self.sig[i] * self.p0[i]) < mpf(10) ** (-30) for i in range(3)), "torsion point is not sigma-fixed"
    def point(self, e):
        p = follow(self.Phi, self.p0, self.sig, mpf(e)); g = rep(p); T = intertwiner(self.Phi, g, self.sig); return p, g, T
    def torsions(self, e, betas=None):
        p, g, T = self.point(e); N = self.N; z = exp(2j * pi / N); out = {}
        for be in (betas or self.chars):
            ax, ay = self.v[0] * z ** be[0], self.v[1] * z ** be[1]
            tau, E, dP = sector_torsion(self.Phi, g, T, ax, ay)
            assert abs(dP - 1) < mpf(10) ** (-20), ("the two monodromy eigenvalues are inverse", dP)
            out[be] = tau
        return out, p, T
    def slopes(self):
        return {c: slope(self.Phi, c[0], c[1], self.N) for c in self.chars if c != (0, 0)}

def analyse(eps, word, k, ell, e1="1e-8", e2="1e-10", quiet=False):
    B = Background(eps, word, k, ell); N = B.N; S = B.slopes(); sl = S[B.ell]
    t1, p1, T1 = B.torsions(e1); t2, p2, T2 = B.torsions(e2); rows = []
    add = lambda a, b: ((a[0] + b[0]) % N, (a[1] + b[1]) % N); neg = lambda a: ((-a[0]) % N, (-a[1]) % N)
    for be in B.chars:
        al = add(B.ell, be)
        if be == (0, 0) or al == (0, 0): continue
        sa, sb = S[al], S[neg(be)]; tol = mpf(10) ** (-20)
        ma, mb = abs(sa - sl) < tol, abs(sb - sl) < tol
        if abs(t1[be]) < mpf(10) ** (-30) and abs(t2[be]) < mpf(10) ** (-30):
            rows.append(dict(beta=be, alpha=al, s_alpha=sa, s_betainv=sb, index=int(ma) - int(mb), matches=int(ma) + int(mb), order=None, coeff=mpf(0), predicted=(sa - sl) * (sb - sl)))
            continue
        order = log(abs(t1[be]) / abs(t2[be])) / log(mpf(e1) / mpf(e2)); n = int(round(float(order)))
        assert abs(order - n) < mpf("1e-3"), (be, order)
        c2 = t2[be] / mpf(e2) ** n; c1 = t1[be] / mpf(e1) ** n; coeff = c2 + (c2 - c1) * mpf(e2) / (mpf(e1) - mpf(e2))   # one Richardson step
        sa, sb = S[al], S[neg(be)]; tol = mpf(10) ** (-20)
        ma, mb = abs(sa - sl) < tol, abs(sb - sl) < tol
        rows.append(dict(beta=be, alpha=al, s_alpha=sa, s_betainv=sb, index=int(ma) - int(mb), matches=int(ma) + int(mb), order=n, coeff=coeff,
                         predicted=(sa - sl) * (sb - sl)))
    return B, sl, rows

if __name__ == "__main__":
    eps = 1 if sys.argv[1][0] == "+" else -1; word = sys.argv[1][1:]; k = int(sys.argv[2])
    Phi = monodromy(eps, word, k); N = exponent(Phi); chars = level_characters(Phi, N)
    print("state %s level %d: torsion %d, exponent %d" % (sys.argv[1], k, len(chars), N))
    ells = [tuple(int(t) for t in a.split(",")) for a in sys.argv[3:]] or [c for c in chars if c != (0, 0)][:3]
    for ell in ells:
        B, sl, rows = analyse(eps, word, k, ell)
        print("l = %s  slope %s  sigma %s  p0 = %s" % (ell, nstr(sl, 12), B.sig, [nstr(c, 8) for c in B.p0]))
        bad = 0
        for r in rows:
            if r["order"] is None:
                print("   beta=%s index %+d matches %d  torsion IDENTICALLY ZERO along the curve" % (r["beta"], r["index"], r["matches"])); continue
            ok_order = r["order"] == 1 + r["matches"]
            ok_coeff = r["order"] != 1 or abs(r["coeff"] - r["predicted"]) < mpf("1e-6") * max(1, abs(r["predicted"]))
            bad += (not ok_order) + (not ok_coeff)
            print("   beta=%s index %+d matches %d order %d coeff %s  predicted(first order) %s %s" % (r["beta"], r["index"], r["matches"], r["order"], nstr(r["coeff"], 12),
                  nstr(r["predicted"], 12), "" if ok_order and ok_coeff else "  <-- FAIL"))
        print("   failures:", bad)
