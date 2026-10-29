"""Referee B1808, check 2: the isolated points on a chi = -3 curve, exactly (no root finding).

For a primitive w with Q(w) = -6 and a class u, the pair (w, u) is (1,1) at a point of H x H iff <w, u> is a
negative-definite plane (then its orthogonal complement is a positive plane whose two isotropic lines are Omega and
conj(Omega), one in H x H, one in H- x H-).  So the author's root-finding count must equal the number of primitive u in
[-2, 2]^4 with det Gram(w, u) > 0, and the number of distinct POINTS is the number of distinct planes Qw + Qu.
NS_A at the point is the saturation (Qw + Qu) cap Lambda_A; its determinant and the CM field Q(sqrt5, sqrt(-5 det NS))
(the transcendental plane has discriminant det Lambda_A * det NS mod squares) are recorded.
The author's coordinates are translated with the author's own basis routine (PARI matkerint), used here only to read
the author's w and u; the point itself is recomputed from the plane and checked against the author's printed tau's.
"""
import itertools, json, math, subprocess, pathlib
import sympy as sp
import mpmath as mp

mp.mp.dps = 50
HERE = pathlib.Path(__file__).resolve().parent
AUTH = json.loads((HERE.parent / "three_generations_in_f2h.json").read_text())
PAIRS = list(itertools.combinations(range(4), 2))


def gp(cmd):
    return subprocess.run(["gp", "-q", "-f"], input=cmd + "\nquit\n", capture_output=True, text=True, timeout=120).stdout.strip()


def perm_sign(seq):
    s, a = 1, list(seq)
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[i] > a[j]: s = -s
            elif a[i] == a[j]: return 0
    return s


def wedge22(F, G):
    return sum(F[p] * G[q] * perm_sign(p + q) for p in PAIRS for q in PAIRS)


def author_basis(A):
    A = sp.Matrix(A)
    g = sp.Matrix(sp.BlockMatrix([[A[i, j] * sp.eye(2) for j in range(2)] for i in range(2)]))
    M = sp.zeros(6, 6)
    for k, p in enumerate(PAIRS):
        F = sp.zeros(4, 4); F[p] = 1; F[p[1], p[0]] = -1
        G = g.T * F * g - F
        for m, q in enumerate(PAIRS): M[m, k] = G[q]
    txt = "[" + ";".join(",".join(str(int(M[i, j])) for j in range(6)) for i in range(6)) + "]"
    K = json.loads(gp("K = matkerint(%s); print(vector(matsize(K)[1], i, K[i,]))" % txt))
    return [{PAIRS[i]: K[i][j] for i in range(6)} for j in range(len(K[0]))]


def saturate_det(G, w, u):
    """det of (Qw + Qu) cap Z^4 under G, via PARI: the Z-basis of the saturation is matrixqz([w,u], -2)."""
    txt = "[" + ";".join("%d,%d" % (w[i], u[i]) for i in range(4)) + "]"
    S = json.loads(gp("S=matrixqz(%s,-2); print(vector(4,i,S[i,]))" % txt))
    S = sp.Matrix(S)
    Gm = S.T * G * S
    idx = abs(sp.Matrix([[w[i], u[i]] for i in range(4)]).T * G * sp.Matrix([[w[i], u[i]] for i in range(4)])).det() / Gm.det()
    return int(Gm.det()), Gm.tolist(), int(sp.sqrt(idx))


def sqfree(n):
    n = int(n); s = 1 if n > 0 else -1; n = abs(n); out = 1
    for p, e in sp.factorint(n).items():
        if e % 2: out *= p
    return s * out


def point_from_plane(basis, G, fs, w, u):
    """Omega in the complexified orthogonal complement of <w, u>, isotropic; return (tau1, tau2) with Im > 0 pair."""
    t1, t2 = sp.symbols("t1 t2")
    dzp = [fs[0][0], fs[0][0] * t1, fs[0][1], fs[0][1] * t1]
    dzm = [fs[1][0], fs[1][0] * t2, fs[1][1], fs[1][1] * t2]
    Om = {p: dzp[p[0]] * dzm[p[1]] - dzp[p[1]] * dzm[p[0]] for p in PAIRS}
    def cond(c):
        F = {p: sum(ci * b[p] for ci, b in zip(c, basis)) for p in PAIRS}
        return sp.expand(wedge22(F, Om))
    e1, e2 = cond(w), cond(u)
    sols = sp.solve([e1, e2], [t1, t2], dict=True)
    out = []
    for s in sols:
        a, b = complex(sp.N(s[t1], 30)), complex(sp.N(s[t2], 30))
        if a.imag > 0 and b.imag > 0:
            out.append((s[t1], s[t2], a, b))
    return out


res = {}
for name, A in [("LR", [[1, 1], [1, 2]]), ("B_4", [[0, -1], [1, 4]]), ("B_5", [[0, -1], [1, 5]]),
                ("B_6", [[0, -1], [1, 6]]), ("B_7", [[0, -1], [1, 7]])]:
    au = AUTH[name]
    G = sp.Matrix(au["Gram Q"])
    w = au["w (chi = -3)"]
    wv = sp.Matrix(w)
    assert (wv.T * G * wv)[0] == -6
    Dlat = int(G.det())
    # exact count of the author's search space
    us = []
    for cu in itertools.product(range(-2, 3), repeat=4):
        if all(x == 0 for x in cu) or math.gcd(*cu) != 1: continue
        uv = sp.Matrix(cu)
        Quu = (uv.T * G * uv)[0]; Qwu = (wv.T * G * uv)[0]
        d = -6 * Quu - Qwu ** 2
        if d > 0: us.append((cu, int(d)))
    # distinct planes: project u into w-perp: 6u + Q(w,u) w, primitive, sign-normalised
    planes = {}
    for cu, d in us:
        uv = sp.Matrix(cu); Qwu = (wv.T * G * uv)[0]
        p = 6 * uv + Qwu * wv
        gg = math.gcd(*[int(x) for x in p]); p = [int(x) // gg for x in p]
        if next(x for x in p if x != 0) < 0: p = [-x for x in p]
        planes.setdefault(tuple(p), []).append((cu, d))
    rows = []
    for p, lst in planes.items():
        cu = lst[0][0]
        dNS, GNS, idx = saturate_det(G, w, list(cu))
        rows.append({"plane (w-perp generator)": list(p), "u's": [list(x[0]) for x in lst],
                     "det Gram(w,u)": sorted(set(x[1] for x in lst)), "det NS (saturated)": dNS, "NS Gram": GNS,
                     "CM: Q(sqrt(D_A), sqrt(%d))" % 0: None,
                     "sqrt(-D_A det NS) squarefree": sqfree(-Dlat * dNS)})
    res[name] = {"author count": au["isolated points on w's curve with a second class u (|u| <= 2)"],
                 "exact count of u with det Gram(w,u) > 0": len(us),
                 "distinct points (planes)": len(planes),
                 "author's 'distinct det' list": au["distinct det Gram(w,u) among them"],
                 "distinct det Gram(w,u) (exact)": sorted(set(d for _, d in us)),
                 "distinct det NS (saturated)": sorted(set(r["det NS (saturated)"] for r in rows)),
                 "distinct CM squarefree -D det NS": sorted(set(r["sqrt(-D_A det NS) squarefree"] for r in rows)),
                 "rows": rows}
    print(name, {k: v for k, v in res[name].items() if k != "rows"})

# verify the author's six LR example points against an exact recomputation from the plane, and with my own wedge
basis = author_basis([[1, 1], [1, 2]])
phi = (1 + sp.sqrt(5)) / 2
fs = [(sp.Integer(1), phi), (sp.Integer(1), 1 - phi)]
w = AUTH["LR"]["w (chi = -3)"]
chk = []
for ex in AUTH["LR"]["examples"]:
    pts = point_from_plane(basis, sp.Matrix(AUTH["LR"]["Gram Q"]), fs, w, ex["u"])
    a = complex(ex["tau1"].replace("i", "j")); b = complex(ex["tau2"].replace("i", "j"))
    best = min(abs(p[2] - a) + abs(p[3] - b) for p in pts) if pts else None
    chk.append({"u": ex["u"], "points in HxH (exact)": len(pts), "max |author - exact|": best,
                "exact": [str(sp.nsimplify(sp.radsimp(p[0]))) for p in pts][:1]})
print("LR example points vs exact:", json.dumps(chk, indent=0, default=str))
res["LR examples check"] = chk
(HERE / "q2_points.json").write_text(json.dumps(res, indent=1, default=str))
print("q2 exit 0")
