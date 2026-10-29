"""Referee B1808, check 1 (independent of the author's script): the invariant lattice, its form, the orientation on all
four A-holomorphic components, the intrinsic Hodge-index sign, and the Moebius determinant identity.

Convention (B1804 r7): coordinates (x1, y1, x2, y2) on H^1 = W (x) H, g = A (x) I_2 acting on 1-forms by row-vector
pullback (dz g = mu dz).  Invariant 2-forms: compound matrix of g on Lambda^2 with eigenvalue 1, kernel by sympy over Q
and saturated by PARI's matrixqz(., -2) (not matkerint).  The intersection form is computed from the wedge of basis
2-vectors with an explicit permutation sign (not the author's Pfaffian expansion).
"""
import itertools, json, subprocess, random
import sympy as sp
import mpmath as mp

mp.mp.dps = 40
PAIRS = list(itertools.combinations(range(4), 2))


def gp(cmd):
    return subprocess.run(["gp", "-q", "-f"], input=cmd + "\nquit\n", capture_output=True, text=True, timeout=120).stdout.strip()


def perm_sign(seq):
    s, a = 1, list(seq)
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[i] > a[j]:
                s = -s
            elif a[i] == a[j]:
                return 0
    return s


def wedge22(F, G):
    """vol-coefficient of F ^ G, F, G dicts on PAIRS meaning sum F_p e_p0 ^ e_p1."""
    return sum(F[p] * G[q] * perm_sign(p + q) for p in PAIRS for q in PAIRS)


def compound2(g):
    """matrix of Lambda^2 of the row-action: (e_i ^ e_j) -> (row_i g) ^ (row_j g)."""
    C = sp.zeros(6, 6)
    for a, (i, j) in enumerate(PAIRS):
        for b, (k, l) in enumerate(PAIRS):
            C[a, b] = g[i, k] * g[j, l] - g[i, l] * g[j, k]
    return C


def lattice(A):
    A = sp.Matrix(A)
    g = sp.Matrix(sp.BlockMatrix([[A[i, j] * sp.eye(2) for j in range(2)] for i in range(2)]))
    # 2-forms F = sum F_p dx^p: pullback g^T F g; on the coefficient vector this is compound2(g)^T acting on columns
    C = compound2(g)
    ker = (C.T - sp.eye(6)).nullspace()
    K = sp.Matrix.hstack(*ker)
    den = sp.ilcm(*[sp.fraction(x)[1] for x in K])
    K = (K * den).applyfunc(sp.Integer)
    txt = "[" + ";".join(",".join(str(K[i, j]) for j in range(K.shape[1])) for i in range(6)) + "]"
    out = gp("M=matrixqz(%s,-2); print(vector(6,i,M[i,]))" % txt)
    Z = json.loads(out)
    r = len(Z[0])
    basis = [{PAIRS[i]: sp.Integer(Z[i][j]) for i in range(6)} for j in range(r)]
    # independent check: each basis vector really invariant under pullback
    for B in basis:
        Fm = sp.zeros(4, 4)
        for (i, j), v in B.items():
            Fm[i, j] = v; Fm[j, i] = -v
        assert g.T * Fm * g == Fm
    G = sp.Matrix(r, r, lambda a, b: wedge22(basis[a], basis[b]))
    return A, g, basis, G


def eig_rows(A):
    t = A.trace(); D = t * t - 4
    out = []
    for mu in ((t + sp.sqrt(D)) / 2, (t - sp.sqrt(D)) / 2):
        # row f with f A = mu f, f = (1, x)
        x = sp.nsimplify((mu - A[0, 0]) / A[1, 0])
        f = sp.Matrix([[1, x]])
        assert sp.simplify(f * A - mu * f) == sp.zeros(1, 2)
        out.append(f)
    return out, D


def one_forms(fs, t1, t2):
    fp, fm = fs
    dzp = [fp[0], fp[0] * t1, fp[1], fp[1] * t1]
    dzm = [fm[0], fm[0] * t2, fm[1], fm[1] * t2]
    return dzp, dzm


def two(a, b):
    return {p: a[p[0]] * b[p[1]] - a[p[1]] * b[p[0]] for p in PAIRS}


def orientation(fs, z1, z2):
    """sign of (i/2)^2 dz+ ^ dz+bar ^ dz- ^ dz-bar on e0^e1^e2^e3, numerically."""
    dzp, dzm = one_forms(fs, z1, z2)
    a = [complex(sp.N(v)) for v in dzp]; b = [complex(sp.N(v)) for v in dzm]
    w1 = {p: a[p[0]] * a[p[1]].conjugate() - a[p[1]] * a[p[0]].conjugate() for p in PAIRS}
    w2 = {p: b[p[0]] * b[p[1]].conjugate() - b[p[1]] * b[p[0]].conjugate() for p in PAIRS}
    v = (0.5j) ** 2 * wedge22(w1, w2)
    return 1 if v.real > 0 else -1


def real11_form(basis, G, fs, z1, z2):
    """the real invariant classes that are (1,1) at (z1, z2): solve Re, Im of F ^ Omega = 0; return the form restricted."""
    dzp, dzm = one_forms(fs, z1, z2)
    Om = two([complex(sp.N(v)) for v in dzp], [complex(sp.N(v)) for v in dzm])
    row = [complex(wedge22(B, Om)) for B in basis]
    import numpy as np
    Mre = np.array([[r.real for r in row], [r.imag for r in row]])
    _, s, vt = np.linalg.svd(Mre)
    N = vt[2:].T                       # 4 x 2 null space (real)
    Gn = np.array(G.tolist(), dtype=float)
    return N.T @ Gn @ N


random.seed(7)
report = {}
for name, A in [("LR", [[1, 1], [1, 2]])] + [("B_%d" % t, [[0, -1], [1, t]]) for t in (3, 4, 5, 6, 7)]:
    A, g, basis, G = lattice(A)
    fs, D = eig_rows(A)
    ev = [float(e) for e in G.evalf().eigenvals(multiple=True)]
    rec = {"rank": len(basis), "det": int(G.det()), "t^2-4": int(D),
           "signature": [sum(e > 0 for e in ev), sum(e < 0 for e in ev)], "Gram": G.tolist()}
    # orientation and the intrinsic Hodge sign on the four components
    comps = {"HxH": (1, 1), "HxH-": (1, -1), "H-xH": (-1, 1), "H-xH-": (-1, -1)}
    import numpy as np
    for cname, (s1, s2) in comps.items():
        signs, fixed_signs = set(), set()
        for _ in range(4):
            z1 = sp.Rational(random.randint(-30, 30), 17) + s1 * sp.I * sp.Rational(random.randint(3, 40), 13)
            z2 = sp.Rational(random.randint(-30, 30), 19) + s2 * sp.I * sp.Rational(random.randint(3, 40), 11)
            o = orientation(fs, z1, z2)
            H = real11_form(basis, G, fs, z1, z2)
            evh = np.linalg.eigvalsh((H + H.T) / 2)
            fixed_signs.add(tuple(int(np.sign(x)) for x in evh))
            signs.add((o, tuple(int(np.sign(o * x)) for x in evh)))
        rec[cname] = {"(complex orientation vs e0123, signs of the form on the invariant (1,1) plane in the COMPLEX "
                      "orientation)": sorted(signs),
                      "signs in the FIXED orientation e0123": sorted(fixed_signs)}
    # the Moebius determinant as a quadratic form, symbolically
    t1, t2 = sp.symbols("t1 t2")
    dzp, dzm = one_forms(fs, t1, t2)
    Om = {p: sp.expand(v) for p, v in two(dzp, dzm).items()}
    c = sp.symbols("c0:4")
    F = {p: sum(ci * B[p] for ci, B in zip(c, basis)) for p in PAIRS}
    P = sp.Poly(sp.expand(wedge22(F, Om)), t1, t2)
    al, be, ga, de = (P.coeff_monomial(m) for m in (1, t1, t2, t1 * t2))
    detM = sp.expand(sp.simplify(al * de - be * ga))
    Qc = sp.expand((sp.Matrix([c]) * G * sp.Matrix(c))[0])
    ratio = sp.simplify(detM / Qc)
    rec["det M_w / Q(w) (identically)"] = str(ratio)
    report[name] = rec
    print(name, json.dumps(rec, default=str))

(pathlib := __import__("pathlib")).Path(__file__).with_suffix(".json").write_text(json.dumps(report, indent=1, default=str))
print("q1 exit 0")
