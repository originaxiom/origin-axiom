"""P-419, frame card F2h (FRAME_CARD.md, written first): inversion by 'three generations' in B1804's holomorphic flux frame.
Exploratory, audit room, data-free.  For A = LR and the null matrices B_t = [[0,-1],[1,t]] (t = 4..7):
  (1) Lambda_A = the A-invariant integral 2-forms on T^4 = W (x) H (A (x) I on H^1; B1804's r7 convention), a Z-basis by
      PARI's matkerint; its intersection form Q (F ^ F' on vol), signature and determinant;
  (2) the complex orientation s, so that chi(L) = s Q(F,F)/2 (Riemann-Roch on an abelian surface);
  (3) whether some invariant class has chi = -3 or +3 (three generations), by a search over small coefficients;
  (4) for such a class w, the (1,1) locus w ^ Omega(tau1, tau2) = 0: tau2 = M_w(tau1), a Moebius map -- a curve in H^2
      iff det M_w > 0;
  (5) isolated points: w with a second invariant class u, both (1,1) at one point of H^2; the NS lattice's Gram matrix
      there (saturated), for small u -- to see whether 'three' leaves one point or infinitely many.
    python3 three_generations_in_f2h.py      # writes three_generations_in_f2h.json beside itself
"""
import itertools, json, math, pathlib, subprocess
from fractions import Fraction as Fr
import sympy as sp

HERE = pathlib.Path(__file__).resolve().parent
PAIRS = list(itertools.combinations(range(4), 2))          # (x1, y1, x2, y2) = 0..3


def gp(cmd):
    r = subprocess.run(["gp", "-q", "-f"], input=cmd + "\n", capture_output=True, text=True, timeout=120)
    return r.stdout.strip()


def Qform(F, G):                                            # coefficient of e0^e1^e2^e3 in F ^ G (F, G dicts on pairs)
    return (F[(0, 1)] * G[(2, 3)] - F[(0, 2)] * G[(1, 3)] + F[(0, 3)] * G[(1, 2)]
            + F[(1, 2)] * G[(0, 3)] - F[(1, 3)] * G[(0, 2)] + F[(2, 3)] * G[(0, 1)])


def frame(A):
    A = sp.Matrix(A); t = A.trace()
    g = sp.Matrix(sp.BlockMatrix([[A[i, j] * sp.eye(2) for j in range(2)] for i in range(2)]))
    # the linear map F -> g^T F g - F on the 6 pair-coordinates
    M = sp.zeros(6, 6)
    for k, p in enumerate(PAIRS):
        F = sp.zeros(4, 4); F[p] = 1; F[p[1], p[0]] = -1
        G = g.T * F * g - F
        for m, q in enumerate(PAIRS): M[m, k] = G[q]
    Mtxt = str([[int(M[i, j]) for j in range(6)] for i in range(6)]).replace("], [", ";").replace("[[", "[").replace("]]", "]")
    K = gp("K = matkerint(" + Mtxt + "); print(vector(matsize(K)[1], i, K[i,]))")
    Kmat = json.loads(K)                                                         # 6 x r
    r = len(Kmat[0]); basis = [{PAIRS[i]: Kmat[i][j] for i in range(6)} for j in range(r)]
    Gram = [[Qform(basis[a], basis[b]) for b in range(r)] for a in range(r)]
    # eigenvectors (row) of A: f A = mu f
    D = t * t - 4; sq = sp.sqrt(D)
    mus = [(t + sq) / 2, (t - sq) / 2]
    fs = []
    for mu in mus:
        # f = (1, x): f A = mu f -> A[0,0] + x A[1,0] = mu
        x = sp.simplify((mu - A[0, 0]) / A[1, 0]); fs.append((sp.Integer(1), x))
    t1, t2 = sp.symbols("t1 t2")
    dzp = [fs[0][0], fs[0][0] * t1, fs[0][1], fs[0][1] * t1]
    dzm = [fs[1][0], fs[1][0] * t2, fs[1][1], fs[1][1] * t2]
    Om = {p: sp.expand(dzp[p[0]] * dzm[p[1]] - dzp[p[1]] * dzm[p[0]]) for p in PAIRS}
    # orientation: (i/2)^2 dz+ ^ dz+bar ^ dz- ^ dz-bar at a sample point, coefficient on e0^e1^e2^e3
    smp = {t1: sp.I * sp.Rational(3, 2) + sp.Rational(1, 5), t2: sp.I * sp.Rational(7, 5) - sp.Rational(1, 3)}
    a = [complex(sp.N(v.subs(smp))) for v in dzp]; b = [complex(sp.N(v.subs(smp))) for v in dzm]
    w1 = {p: a[p[0]] * a[p[1]].conjugate() - a[p[1]] * a[p[0]].conjugate() for p in PAIRS}
    w2 = {p: b[p[0]] * b[p[1]].conjugate() - b[p[1]] * b[p[0]].conjugate() for p in PAIRS}
    vol = ((0.5j) ** 2) * Qform(w1, w2)
    s = 1 if vol.real > 0 else -1
    return dict(A=A, D=D, basis=basis, Gram=Gram, Om=Om, t1=t1, t2=t2, s=s, r=r)


def combo(fr, c):
    return {p: sum(ci * b[p] for ci, b in zip(c, fr["basis"])) for p in PAIRS}


def cond(fr, F):                                            # F ^ Omega as a polynomial in t1, t2
    return sp.expand(Qform(F, fr["Om"]))


def moebius(fr, F):                                         # F ^ Omega = alpha + beta t1 + gamma t2 + delta t1 t2 = 0
    P = sp.Poly(cond(fr, F), fr["t1"], fr["t2"])
    al = P.coeff_monomial(1); be = P.coeff_monomial(fr["t1"]); ga = P.coeff_monomial(fr["t2"]); de = P.coeff_monomial(fr["t1"] * fr["t2"])
    # t2 = -(alpha + beta t1)/(gamma + delta t1) = (-beta t1 - alpha)/(delta t1 + gamma)
    Mw = sp.Matrix([[-be, -al], [de, ga]])
    return Mw, sp.simplify(Mw.det())


def analyse(name, A, N=3):
    fr = frame(A); r = fr["r"]; G = sp.Matrix(fr["Gram"])
    ev = [complex(e) for e in G.evalf().eigenvals(multiple=True)]
    out = {"matrix": [[int(x) for x in row] for row in A], "rank Lambda_A": r, "Gram Q": fr["Gram"],
           "det Q": int(G.det()), "signature (+,-)": [sum(1 for e in ev if e.real > 0), sum(1 for e in ev if e.real < 0)],
           "orientation s": fr["s"]}
    three, seen = [], set()
    for c in itertools.product(range(-N, N + 1), repeat=r):
        if all(x == 0 for x in c) or math.gcd(*c) != 1: continue
        F = combo(fr, c); chi = fr["s"] * Qform(F, F) // 2
        if abs(chi) == 3: three.append((c, chi))
    out["classes with |chi| = 3 (coefficients <= %d)" % N] = len(three)
    out["chi signs among them"] = sorted(set(ch for _, ch in three))
    curves = []
    for c, chi in [x for x in three if x[1] == -3][:3] + [x for x in three if x[1] == 3][:3]:
        Mw, dt = moebius(fr, combo(fr, c))
        dtn = complex(sp.N(dt))
        curves.append({"class": list(c), "chi": chi, "det M_w (sign: >0 a curve in H^2)": "%.6g" % dtn.real})
    out["the (1,1) curves of the first six such classes"] = curves
    # isolated points: pairs (w, u), w with |chi| = 3, u small, both (1,1) at one point of H^2
    pts = []
    if three:
        wc = next(c for c, ch in three if ch == -3); out["w (chi = -3)"] = list(wc)
        w = combo(fr, wc); Mw, _ = moebius(fr, w)
        t1 = fr["t1"]
        for cu in itertools.product(range(-2, 3), repeat=r):
            if all(x == 0 for x in cu) or math.gcd(*cu) != 1: continue
            u = combo(fr, cu)
            # rank 2?
            if all(sp.simplify(u[p] * 1 - 0) == 0 for p in PAIRS): continue
            e = sp.expand(sp.numer(sp.together(cond(fr, u).subs(fr["t2"], (Mw[0, 0] * t1 + Mw[0, 1]) / (Mw[1, 0] * t1 + Mw[1, 1])))))
            if e == 0: continue
            cs = [complex(sp.N(cf, 30)) for cf in sp.Poly(e, t1).all_coeffs()]
            while cs and abs(cs[0]) < 1e-20: cs = cs[1:]
            if len(cs) < 2: continue
            import numpy as _np
            for root in _np.roots(cs):
                z1 = complex(root); m = [[complex(sp.N(Mw[i, j])) for j in range(2)] for i in range(2)]
                den = m[1][0] * z1 + m[1][1]
                if abs(den) < 1e-14: continue
                z2 = (m[0][0] * z1 + m[0][1]) / den
                if z1.imag > 1e-12 and z2.imag > 1e-12:
                    Gm = [[fr["s"] * Qform(x, y) for y in (w, u)] for x in (w, u)]
                    dG = Gm[0][0] * Gm[1][1] - Gm[0][1] ** 2
                    if dG <= 0: continue                     # (1,1) invariant pairs span a negative-definite plane
                    pts.append({"u": list(cu), "tau1": "%.10f%+.10fi" % (z1.real, z1.imag), "tau2": "%.10f%+.10fi" % (z2.real, z2.imag),
                                "Gram(w,u) (oriented)": Gm, "det": dG})
        out["isolated points on w's curve with a second class u (|u| <= 2)"] = len(pts)
        out["distinct det Gram(w,u) among them"] = sorted(set(p["det"] for p in pts))[:40]
        out["examples"] = pts[:6]
    return out


res = {"LR": analyse("LR", [[1, 1], [1, 2]])}
for t in (4, 5, 6, 7):
    res["B_%d" % t] = analyse("B_%d" % t, [[0, -1], [1, t]])
(HERE / "three_generations_in_f2h.json").write_text(json.dumps(res, indent=1, default=str), encoding="utf-8")
for k, v in res.items():
    print(k, {kk: vv for kk, vv in v.items() if kk not in ("examples",)})
