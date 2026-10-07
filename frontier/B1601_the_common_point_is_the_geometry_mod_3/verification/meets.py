#!/usr/bin/env python3
"""B1601 -- THE COMMON POINT IS THE GEOMETRY MOD 3.  Where does a thread's geometry meet the weave's common point?

For a word w in L, R (a thread of either sign; the sign acts trivially on characters) the Fricke map of w acts on the
fibre's characters (x, y, z) = (tr a, tr b, tr ab); its fixed points on the parabolic Markov surface x^2 + y^2 + z^2 = xyz
are the fibre characters that extend over the bundle.  The geometric one is identified by the cusp shape of SnapPy's
b++w (the representation is built from the point, the lift of the base element found as the intertwiner, the puncture's
fixed point sent to infinity, the lattice compared with SnapPy's up to SL(2, Z) and the mirror).  In K = Q(geometric
point) the ideal (x, y, z) is an invariant of the thread (invariant under Aut(F2) and the sign): a prime p of K not
above 2 contains it exactly when the fibre's holonomy reduces mod p to the quaternion point a -> i, b -> j -- the origin
of the Markov surface over the residue field, where trace 0 means order four.  Above 2 the origin is the trivial
representation instead.  The instrument reports the ideal's norm, its prime factorisation with residue characteristics
and degrees, the primes above 3 of K, and the integrality of the traces.

The lemma (mode `lemma`): the linear part of the Fricke maps at the origin is the signed parity permutation of the
three lines (W1/W4): dL = a quarter turn about the x-axis, dR = about the y-axis, generating the cube's rotation group
S4; for a word of odd trace d(phi)(0) is a third turn about a body diagonal, whose axis (+-1, +-1, +-1) is isotropic for
the quadratic part x^2 + y^2 + z^2 exactly in characteristic 3; for even trace the fixed axis is a coordinate axis or
a face diagonal, not isotropic -- unless d(phi)(0) = I.

    python3 meets.py WORD ...          one JSON row per word on stdout
    python3 meets.py threads N         the unsigned odd-trace primitive words to length N, up to rotation and L<->R
    python3 meets.py census odd|even N  -> meets_<odd|even>_<N>.json beside this file
    python3 meets.py lemma N           -> linear_part_<N>.json beside this file"""
import sys, json, itertools, time, pathlib
import sympy as sp
import mpmath as mp
import numpy as np
import snappy
from snappy import pari
HERE = pathlib.Path(__file__).resolve().parent

x, y, z = sp.symbols("x y z")
Lm = {x: x, y: z, z: x * z - y}          # a -> a, b -> ab
Rm = {x: z, y: y, z: y * z - x}          # a -> ab, b -> b
MATS = {"L": ((1, 1), (0, 1)), "R": ((1, 0), (1, 1))}


def trace(w):
    A = ((1, 0), (0, 1))
    for c in w:
        B = MATS[c]
        A = tuple(tuple(sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)) for i in range(2))
    return A[0][0] + A[1][1]


def words(nmax, parity):
    """the unsigned primitive words with both letters to length nmax, up to rotation and L<->R, of the given trace parity"""
    seen, out = set(), []
    for n in range(2, nmax + 1):
        for t in itertools.product("LR", repeat=n):
            w = "".join(t)
            if "L" not in w or "R" not in w or any(w == w[:d] * (n // d) for d in range(1, n) if n % d == 0):
                continue
            ex = w.translate(str.maketrans("LR", "RL"))
            c = min(min(v[i:] + v[:i] for i in range(n)) for v in (w, ex))
            if c in seen:
                continue
            seen.add(c)
            if trace(c) % 2 == parity:
                out.append(c)
    return out


def threads(nmax):
    return words(nmax, 1)


def fricke(word):
    cur = (x, y, z)
    for ch in word:
        mv = Lm if ch == "L" else Rm
        cur = tuple(sp.expand(mv[v].subs({x: cur[0], y: cur[1], z: cur[2]}, simultaneous=True)) for v in (x, y, z))
    return cur


def phi_words(w):
    imgs = ("a", "b")
    for ch in w:
        imgs = (imgs[0], imgs[0] + imgs[1]) if ch == "L" else (imgs[0] + imgs[1], imgs[1])
    return imgs


u = sp.symbols("u")
PRIM = (1, 2, 5)   # the primitive element u = x + 2 y + 5 z (a generic linear form; shape position checked)


def fixed_points(word):
    """the fixed points of the word's Fricke map on the Markov surface in shape position: over z when the lex basis
    allows it, else over the primitive element u = x + 2y + 5z.  Returns (variable, its polynomial, {x, y, z: expr},
    the non-origin irreducible factors)"""
    fx, fy, fz = fricke(word)
    eqs = [sp.expand(fx - x), sp.expand(fy - y), sp.expand(fz - z), x**2 + y**2 + z**2 - x * y * z]
    G = sp.groebner(eqs, x, y, z, order="lex")
    ex = list(G.exprs)
    zp = [g for g in ex if g.free_symbols <= {z}]
    xs = [g for g in ex if x in g.free_symbols]
    ys = [g for g in ex if y in g.free_symbols and x not in g.free_symbols]
    if len(zp) == 1 and len(xs) == 1 and len(ys) == 1 and xs[0].as_poly(x).degree() == 1 and ys[0].as_poly(y).degree() == 1 \
            and xs[0].free_symbols <= {x, z} and ys[0].free_symbols <= {y, z}:
        sol = {x: sp.solve(xs[0], x)[0], y: sp.solve(ys[0], y)[0], z: z}
        facs = [(f, m) for f, m in sp.factor_list(zp[0])[1] if f != z]
        return z, zp[0], sol, facs
    G = sp.groebner(eqs + [u - PRIM[0] * x - PRIM[1] * y - PRIM[2] * z], x, y, z, u, order="lex")
    ex = list(G.exprs)
    up = [g for g in ex if g.free_symbols <= {u}][0]
    sol = {}
    for v in (x, y, z):
        cands = [g for g in ex if v in g.free_symbols and g.free_symbols <= {v, u}]
        assert len(cands) == 1 and cands[0].as_poly(v).degree() == 1, (word, ex)
        sol[v] = sp.solve(cands[0], v)[0]
    facs = [(f, m) for f, m in sp.factor_list(up)[1] if f != u]
    return u, up, sol, facs


# ---- numerics: the representation at a point and the cusp shape of the bundle ----
def inv(w):
    return "".join(c.swapcase() for c in reversed(w))


def reduce_word(w):
    out = []
    for c in w:
        if out and out[-1] == c.swapcase():
            out.pop()
        else:
            out.append(c)
    return "".join(out)


def conjugator(w):
    """[phi(a), phi(b)] = u [a, b] u^-1 as reduced words; returns u (phi orientation-preserving)"""
    pa, pb = phi_words(w)
    r = reduce_word(pa + pb + inv(pa) + inv(pb))
    u = ""
    while len(r) > 4 and r[0] == r[-1].swapcase():
        u += r[0]; r = r[1:-1]
    rots = {"abAB": "", "bABa": "a", "ABab": "ab", "BabA": "abA"}   # c = p [a,b] p^-1 with [a,b] = q p, c = p q
    assert r in rots, (w, r)
    return u + rots[r]


def mat_word(w, A, B):
    M = mp.eye(2)
    for c in w:
        M = M * ({"a": A, "b": B, "A": mp.inverse(A), "B": mp.inverse(B)}[c])
    return M


def rep(xv, yv, zv):
    A = mp.matrix([[xv, -1], [1, 0]])
    xi = (zv + mp.sqrt(zv * zv - 4)) / 2
    B = mp.matrix([[0, xi], [-1 / xi, yv]])
    return A, B


def intertwiner(A, B, A2, B2):
    """T with T A = A2 T, T B = B2 T, det 1 (least squares on the 8 x 4 system)"""
    rows = []
    for X, X2 in ((A, A2), (B, B2)):
        for i in range(2):
            for j in range(2):
                r = [mp.mpc(0)] * 4
                for k in range(2):
                    r[2 * i + k] += X[k, j]      # (T X)_{ij} = sum_k T_{ik} X_{kj}
                    r[2 * k + j] -= X2[i, k]     # (X2 T)_{ij} = sum_k X2_{ik} T_{kj}
                rows.append(r)
    Mx = mp.matrix(rows)
    U, s, Vh = mp.svd_c(Mx, full_matrices=True)
    v = Vh[3, :].H
    T = mp.matrix([[v[0], v[1]], [v[2], v[3]]])
    d = mp.det(T)
    return T / mp.sqrt(d), abs(s[3]) / abs(s[0])


def cusp_shape(w, xv, yv, zv):
    A, B = rep(xv, yv, zv)
    pa, pb = phi_words(w)
    A2, B2 = mat_word(pa, A, B), mat_word(pb, A, B)
    T, resid = intertwiner(A, B, A2, B2)
    U = mat_word(conjugator(w), A, B)
    Tp = mp.inverse(U) * T                      # the lift of t fixing the puncture's fixed point
    Lam = A * B * mp.inverse(A) * mp.inverse(B)
    # fixed point p of the parabolic Lam: (Lam - sgn I) p = 0
    s = 1 if abs(Lam[0, 0] + Lam[1, 1] - 2) < abs(Lam[0, 0] + Lam[1, 1] + 2) else -1
    Mx = Lam - s * mp.eye(2)
    p = mp.matrix([[-Mx[0, 1]], [Mx[0, 0]]]) if abs(Mx[0, 0]) + abs(Mx[0, 1]) > abs(Mx[1, 0]) + abs(Mx[1, 1]) else mp.matrix([[-Mx[1, 1]], [Mx[1, 0]]])
    # C sends p to infinity: C = [[q1, q2],[p2, -p1]] with det 1 normalisation irrelevant for the translation ratio
    C = mp.matrix([[0, 1], [p[1], -p[0]]]) if abs(p[0]) > abs(p[1]) else mp.matrix([[1, 0], [p[1], -p[0]]])
    Ci = mp.inverse(C)
    tr = lambda Mx_: (C * Mx_ * Ci)
    L1, T1 = tr(Lam), tr(Tp)
    cl = L1[0, 1] / L1[0, 0]; ct = T1[0, 1] / T1[0, 0]
    comm = mp.norm(Tp * Lam - Lam * Tp)
    return ct / cl, resid, comm, abs(T1[1, 0]) + abs(L1[1, 0])


def reduce_tau(t):
    t = mp.mpc(t)
    if mp.im(t) < 0:
        t = -t
    for _ in range(200):
        t = t - mp.nint(mp.re(t))
        if abs(t) < 1:
            t = -1 / t
        else:
            break
    return t


def same_lattice(t1, t2, tol=1e-6):
    a, b = reduce_tau(t1), reduce_tau(t2)
    return min(abs(a - b), abs(a + mp.conj(b)), abs(a - mp.conj(b) + 1), abs(a + mp.conj(b) - 1)) < tol


def geometric_factor(w, var, sol, facs, dps=60):
    mp.mp.dps = dps
    M = snappy.Manifold("b++" + w)
    shape = mp.mpc(*map(float, (M.cusp_info()[0]["shape"].real(), M.cusp_info()[0]["shape"].imag())))
    hits = []
    for f, m in facs:
        coeffs = [mp.mpf(int(c)) for c in sp.Poly(f, var).all_coeffs()]
        for r in mp.polyroots(coeffs, maxsteps=500, extraprec=300):
            rs = sp.Float(mp.nstr(mp.re(r), dps), dps) + sp.I * sp.Float(mp.nstr(mp.im(r), dps), dps)
            xv, yv, zv = (mp.mpc(sp.N(sol[v].subs(var, rs), dps)) for v in (x, y, z))
            if abs(mp.im(zv)) < mp.mpf(10) ** -20 and abs(mp.im(xv)) < mp.mpf(10) ** -20 and abs(mp.im(yv)) < mp.mpf(10) ** -20:
                continue    # a real point is not the holonomy of a hyperbolic bundle
            tau, resid, comm, offdiag = cusp_shape(w, xv, yv, zv)
            if same_lattice(tau, shape):
                hits.append((str(f), r, tau, resid, comm))
    return shape, hits


# ---- the ideal in K ----
def ideal_data(f, var, sol):
    fp = sp.Poly(f, var)
    fs = str(fp.as_expr()).replace("**", "^").replace(str(var), "u")
    nf = pari("nfinit(%s)" % fs)
    def elt(e):
        num, den = sp.fraction(sp.together(e))
        p = sp.Poly(sp.rem(sp.expand(num), fp.as_expr(), var), var)
        return pari("Mod(%s, %s)" % (str(p.as_expr() / den).replace("**", "^").replace(str(var), "u"), fs))
    xe, ye, ze = elt(sol[x]), elt(sol[y]), elt(sol[z])
    I = nf.idealadd(nf.idealadd(nf.idealhnf(xe), nf.idealhnf(ye)), nf.idealhnf(ze))
    N = int(nf.idealnorm(I))
    fac = nf.idealfactor(I)
    primes = []
    for i in range(fac.nrows()):
        pr = fac[i, 0]; e = int(fac[i, 1])
        primes.append({"p": int(pr.pr_get_p()), "f": int(pr.pr_get_f()), "e_in_ideal": e})
    odd = N
    while odd % 2 == 0:
        odd //= 2
    return {"field": str(fp.as_expr()), "degree": fp.degree(), "disc": int(nf[2]), "norm": N, "odd_part": odd, "primes": primes,
            "integral": all(c.type() == "t_INT" for e in (xe, ye, ze) for c in nf.nfalgtobasis(e)),
            "primes_above_3": [{"f": int(p.pr_get_f()), "e": int(p.pr_get_e())} for p in nf.idealprimedec(3)]}


DL = np.array([[1, 0, 0], [0, 0, 1], [0, -1, 0]]); DR = np.array([[0, 0, 1], [0, 1, 0], [-1, 0, 0]])


def linear_part(w):
    A = np.eye(3, dtype=int)
    for c in w:
        A = A @ (DL if c == "L" else DR)
    return A


def lemma(nmax):
    """the linear parts of L and R at the origin against the table; every word's fixed axis and its isotropy mod 3"""
    out = {"L_R_linear_parts_as_tabled": all(
        sp.Matrix([[sp.diff(mv[v], t) for t in (x, y, z)] for v in (x, y, z)]).subs({x: 0, y: 0, z: 0}) == sp.Matrix(D)
        for mv, D in ((Lm, DL), (Rm, DR))), "rows": []}
    for parity in (1, 0):
        for w in words(nmax, parity):
            A = linear_part(w)
            fixed = sp.Matrix(A - np.eye(3, dtype=int)).nullspace()
            # the fixed space of A over F_3 and its non-zero isotropic vectors for x^2 + y^2 + z^2
            f3 = [v for v in itertools.product(range(3), repeat=3) if any(v) and all(int(c) % 3 == 0 for c in (A @ np.array(v) - np.array(v)))]
            iso = [v for v in f3 if sum(c * c for c in v) % 3 == 0]
            out["rows"].append({"word": w, "trace": trace(w), "odd": parity == 1, "det": int(round(np.linalg.det(A))),
                                "fixed_space": [[int(v) for v in f] for f in fixed], "fixed_vectors_mod_3": len(f3),
                                "isotropic_fixed_vector_mod_3": bool(iso), "isotropic_examples": iso[:4],
                                "identity": bool((A == np.eye(3, dtype=int)).all())})
    odd = [r for r in out["rows"] if r["odd"]]; even = [r for r in out["rows"] if not r["odd"]]
    out["summary"] = {"max_length": nmax, "odd": len(odd), "even": len(even), "all_det_one": all(r["det"] == 1 for r in out["rows"]),
                      "odd_all_body_diagonal": all(len(r["fixed_space"]) == 1 and all(abs(v) == 1 for v in r["fixed_space"][0]) for r in odd),
                      "odd_all_isotropic": all(r["isotropic_fixed_vector_mod_3"] for r in odd),
                      "even_isotropic": [r["word"] for r in even if r["isotropic_fixed_vector_mod_3"]],
                      "even_identity": [r["word"] for r in even if r["identity"]]}
    return out


def run(w):
    t0 = time.time()
    var, vp, sol, facs = fixed_points(w)
    t1 = time.time()
    shape, hits = geometric_factor(w, var, sol, facs)
    row = {"word": w, "trace": trace(w), "shape_variable": str(var), "fixed_degree": sp.degree(vp, var),
           "components": [(str(f), sp.degree(f, var)) for f, _ in facs], "cusp_shape": mp.nstr(shape, 12), "geometric_hits": len(hits)}
    if hits:
        fset = {h[0] for h in hits}
        row["geometric_components"] = sorted(fset)
        f = sp.sympify(hits[0][0])
        row["max_intertwiner_residual"] = mp.nstr(max(h[3] for h in hits), 3)
        row["max_commutation_defect"] = mp.nstr(max(h[4] for h in hits), 3)
        row.update(ideal_data(f, var, sol))
    row["s_groebner"] = round(t1 - t0, 1); row["s"] = round(time.time() - t0, 1)
    return row


if __name__ == "__main__":
    if sys.argv[1] == "threads":
        print(" ".join(threads(int(sys.argv[2]))))
    elif sys.argv[1] == "lemma":
        n = int(sys.argv[2]); res = lemma(n)
        (HERE / f"linear_part_{n}.json").write_text(json.dumps(res, indent=1) + "\n"); print(json.dumps(res["summary"]))
    elif sys.argv[1] == "census":
        parity, n = {"odd": 1, "even": 0}[sys.argv[2]], int(sys.argv[3]); rows = []
        for w in words(n, parity):
            rows.append(run(w)); print(json.dumps(rows[-1], default=str), flush=True)
        (HERE / f"meets_{sys.argv[2]}_{n}.json").write_text(json.dumps(rows, indent=1, default=str) + "\n")
    else:
        for w in sys.argv[1:]:
            print(json.dumps(run(w), default=str), flush=True)
