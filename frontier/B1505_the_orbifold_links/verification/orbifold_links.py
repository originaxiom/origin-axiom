"""B1505 -- THE ORBIFOLD LINKS: the known G2 cones whose links are orbifolds but not global quotients of smooth nearly Kaehler
manifolds, and whether any of them has an ADE locus coned over a torus (the local model a cusp point needs).

The class (Acharya-Witten 2001; Anguelova-Lazaroiu 2002; Calderbank-Singer 2006):
  (A) AW section 2: cones over WCP^3_{n,n,m,m}/Z_r (G2 metrics argued by heterotic duality, not constructed);
  (B) AW section 3: cones over the twistor space Z(M) of a compact self-dual Einstein 4-orbifold M of positive scalar curvature
      (explicit metrics); M known: every toric one (Calderbank-Singer Theorem A: quaternion-Kaehler torus quotients) and
      Hitchin's SO(3)-invariant family;
  (C) quotients of (B) by finite groups of orientation-preserving isometries of M.

Five parts, all own code:
A. THE CENSUS OF TORIC DATA.  Calderbank-Singer's data (a_i, b_i) (2a_i, 2b_i integers, a_i > 0, b_i/a_i increasing, the edge
   vectors v_j integral), k = 3..6 poles: exceptional surfaces (label, e, chi_orb; CS's inequality e < chi_orb), smoothness, the
   combinatorial automorphisms (B in GL(2,Z) on characters with a dihedral permutation of the edges) and, for each orientation-
   preserving one, its 2-dimensional fixed components by T3's case analysis.
B. THE CURVATURE IDENTITY.  Calderbank-Pedersen's metric (1.1) from the multipole eigenfunction F = sum sqrt(a^2 rho^2 +
   (a eta - b)^2)/sqrt(rho): selfdual Einstein with s = 12 checked from the full curvature tensor (mpmath); the closed forms
   D = 4 rho sum_{i<j} c_ij^2/(r_i r_j), u1 = -2 sum (w_i/r_i)(b_i, a_i), u2 = 2 rho sum (a_i/r_i)(b_i, a_i) checked against the
   symbolic build; then T2 in its orbifold form, e_orb = chi_orb - s area_orb/(24 pi), on every exceptional surface of four data
   sets (areas from the closed forms at rho -> 0) and on the real projective plane of CP^2.
C. THE PAIRING.  The normal degrees of the two twistor sections over a surface F fixed by an isometry of M, and their cubic
   inflows +-(N/2)(2e - chi): B1503's banked CP^3 pair (d1, d2) = (-2, 0), (0, -2) reproduced; a torus would give +-N e(N_F).
D. HITCHIN'S FAMILY.  SO(3) on S^4 in Sym^2_0(R^3): the fixed sets of rotations (a 2-sphere for order 2, two points otherwise)
   and the singular orbit (RP^2).
E. AW SECTION 2.  The singular strata of WCP^3_{n,n,m,m}/Z_r (and of the weighted spaces in general): weighted projective lines.

Run:  python3 orbifold_links.py [census | identity | pairing | hitchin | aw2 | record]
"""
import itertools
import json
import sys
import time
from collections import Counter
from fractions import Fraction as Fr
from math import gcd
from pathlib import Path

HERE = Path(__file__).resolve().parent


# ---------------------------------------------------------------------------------------------- A. the census of toric data
def det(u, v):
    return u[0] * v[1] - u[1] * v[0]


def data_vs(data):
    """CS: v_j = sum_{i<=j}(a_i,b_i) - sum_{i>j}(a_i,b_i), j = 0..k (v_k = -v_0); edge C_j (j = 1..k) carries v_j"""
    k = len(data)
    return [(sum(a for a, _ in data[:j]) - sum(a for a, _ in data[j:]), sum(b for _, b in data[:j]) - sum(b for _, b in data[j:]))
            for j in range(k + 1)]


def invariants(data):
    v = [(int(m), int(n)) for m, n in data_vs(data)]
    k = len(data)
    edges = v[1:k + 1]
    ext = [v[0]] + edges + [(-edges[0][0], -edges[0][1])]
    rows = []
    for j in range(1, k + 1):
        d1, d2, d0 = det(ext[j - 1], ext[j]), det(ext[j], ext[j + 1]), det(ext[j - 1], ext[j + 1])
        rows.append(dict(edge=j, v=edges[j - 1], label=gcd(*edges[j - 1]), e=Fr(d0, d1 * d2), chi=Fr(d1 + d2, d1 * d2),
                         d_prev=d1, d_next=d2))
    vertex_orders = [abs(det(ext[j], ext[j + 1])) for j in range(1, k + 1)]
    return v, edges, rows, vertex_orders


def matvec(B, u):
    return (B[0][0] * u[0] + B[0][1] * u[1], B[1][0] * u[0] + B[1][1] * u[1])


def automorphisms(edges):
    """(B, pi, kind): B in GL(2,Z) acting on characters, pi a dihedral permutation of the cyclic edge list with
    B v_j = +-v_pi(j) for every edge; the torus acts by A = B^{-T}"""
    k = len(edges)
    perms = []
    for s in range(k):
        perms.append(("rot" if s else "id", [(j + s) % k for j in range(k)]))
        perms.append(("ref", [(s - j) % k for j in range(k)]))
    out = set()
    v1, v2 = edges[0], edges[1]
    dv = det(v1, v2)
    inv = ((Fr(v2[1], dv), Fr(-v2[0], dv)), (Fr(-v1[1], dv), Fr(v1[0], dv)))
    for kind, pi in perms:
        for e1, e2 in itertools.product((1, -1), repeat=2):
            w1 = (e1 * edges[pi[0]][0], e1 * edges[pi[0]][1])
            w2 = (e2 * edges[pi[1]][0], e2 * edges[pi[1]][1])
            W = ((w1[0], w2[0]), (w1[1], w2[1]))
            B = tuple(tuple(sum(W[r][t] * inv[t][c] for t in range(2)) for c in range(2)) for r in range(2))
            if any(x.denominator != 1 for row in B for x in row):
                continue
            B = tuple(tuple(int(x) for x in row) for row in B)
            if abs(B[0][0] * B[1][1] - B[0][1] * B[1][0]) != 1:
                continue
            if all(matvec(B, edges[j]) in (edges[pi[j]], (-edges[pi[j]][0], -edges[pi[j]][1])) for j in range(k)):
                out.add((B, tuple(pi), kind))
    return sorted(out)


def A_of(B):
    d = B[0][0] * B[1][1] - B[0][1] * B[1][0]
    Binv = ((B[1][1] * d, -B[0][1] * d), (-B[1][0] * d, B[0][0] * d))
    return ((Binv[0][0], Binv[1][0]), (Binv[0][1], Binv[1][1]))


def fixed_surfaces(edges, B, pi, kind, orders, labels):
    """the 2-dimensional fixed components of an isometry of combinatorial type (B, pi), by T3's case analysis; None if the
    isometry reverses orientation (it then does not lift to the twistor space's G2 structure)"""
    k = len(edges)
    A = A_of(B)
    detA = A[0][0] * A[1][1] - A[0][1] * A[1][0]
    if detA * (1 if kind in ("id", "rot") else -1) != 1:
        return None
    I, mI = ((1, 0), (0, 1)), ((-1, 0), (0, -1))
    if kind == "id":
        if A == I:
            return dict(type="identity")
        assert A == mI, A
        return dict(type="real locus", chi=4 - k,
                    meets_orbifold_locus=any(l > 1 for l in labels) or any(o > 1 for o in orders))
    if kind == "rot":
        return dict(type="rotation", fixes_principal_orbit=(A == I))
    ends = [("edge", j) for j in range(k) if pi[j] == j]
    ends += [("vertex", j) for j in range(k) if pi[j] == (j + 1) % k and pi[(j + 1) % k] == j]
    assert len(ends) == 2, (pi, ends)
    if detA != -1:
        return dict(type="reflection", topology="none (A = +-I: the fixed set is a curve)")
    u = next(c for c in ((A[0][1], 1 - A[0][0]), (1 - A[1][1], A[1][0])) if c != (0, 0))   # A u = u
    joins = []
    for typ, j in ends:
        if typ == "vertex":
            joins.append("cap")
            continue
        m, n = edges[j]
        joins.append("cap" if det((n, -m), u) == 0 else "glue")      # the collapsing direction on C_j against u
    topo = "torus" if joins == ["glue", "glue"] else ("sphere" if "glue" in joins else "two spheres")
    return dict(type="reflection", ends=[e[0] for e in ends], joins=joins, topology=topo)


def enumerate_data(k, amax=1, bmax=3):
    """CS data with 2a_i in 1..2 amax, 2b_i in -2 bmax..2 bmax, b_i/a_i strictly increasing, v_j integral (deduplicated by v)"""
    half = [Fr(t, 2) for t in range(1, 2 * amax + 1)]
    bs = [Fr(t, 2) for t in range(-2 * bmax, 2 * bmax + 1)]
    pairs = sorted(((a, b) for a in half for b in bs), key=lambda p: (p[1] / p[0], p[0]))
    seen = set()
    for combo in itertools.combinations(pairs, k):
        ys = [b / a for a, b in combo]
        if any(ys[i] >= ys[i + 1] for i in range(k - 1)):
            continue
        v = data_vs(list(combo))
        if any(Fr(x).denominator != 1 for p in v for x in p):
            continue
        key = tuple((int(m), int(n)) for m, n in v)
        if key in seen:
            continue
        seen.add(key)
        yield list(combo)


def census(ks=(3, 4, 5, 6)):
    tally = Counter()
    examples = {}
    for k in ks:
        for data in enumerate_data(k):
            v, edges, rows, orders = invariants(data)
            labels = [r["label"] for r in rows]
            assert all(r["d_prev"] > 0 and r["d_next"] > 0 for r in rows), ("cyclic order", data)
            assert all(r["e"] < r["chi"] for r in rows), ("CS inequality", data)
            smooth = all(l == 1 for l in labels) and all(o == 1 for o in orders)
            tally[f"k={k} data"] += 1
            tally[f"k={k} smooth"] += smooth
            tally[f"k={k} exceptional surfaces (all e < chi_orb)"] += len(rows)
            for B, pi, kind in automorphisms(edges):
                f = fixed_surfaces(edges, B, pi, kind, orders, labels)
                if f is None:
                    tally[f"k={k} orientation-reversing automorphisms (no twistor lift)"] += 1
                    continue
                t = f["type"]
                if t == "rotation":
                    tally[f"k={k} rotations fixing a principal orbit"] += f["fixes_principal_orbit"]
                    tally[f"k={k} rotations"] += 1
                elif t == "reflection":
                    tally[f"k={k} reflections: {f['topology']}"] += 1
                    if f["topology"] == "torus":
                        examples.setdefault("reflection torus", (data, B, pi))
                elif t == "real locus":
                    tally[f"k={k} real loci chi={f['chi']}, meeting the orbifold locus={f['meets_orbifold_locus']}"] += 1
                    if f["chi"] == 0:
                        examples.setdefault("chi-0 real locus", [str(x) for x in data])
    return dict(tally=dict(sorted(tally.items())), examples=examples)


# ---------------------------------------------------------------------------------------------- B. the curvature identity
def _sympy_metric(data, dps=30):
    import mpmath as mp
    import sympy as sp
    mp.mp.dps = dps
    R, E = sp.symbols("rho eta", positive=True)
    F = sum(sp.sqrt(sp.Rational(a) ** 2 * R ** 2 + (sp.Rational(a) * E - sp.Rational(b)) ** 2) for a, b in data) / sp.sqrt(R)
    Fr_, Fe_ = sp.diff(F, R), sp.diff(F, E)
    D = F ** 2 - 4 * R ** 2 * (Fr_ ** 2 + Fe_ ** 2)
    P, Q, S = F - 2 * R * Fr_, -2 * R * Fe_, F + 2 * R * Fr_
    sr = sp.sqrt(R)
    u1 = (P * sr + Q * E / sr, Q / sr)
    u2 = (Q * sr + S * E / sr, S / sr)
    comps = {(0, 0): D / (4 * F ** 2 * R ** 2), (1, 1): D / (4 * F ** 2 * R ** 2),
             (2, 2): (u1[0] ** 2 + u2[0] ** 2) / (F ** 2 * D), (2, 3): (u1[0] * u1[1] + u2[0] * u2[1]) / (F ** 2 * D),
             (3, 3): (u1[1] ** 2 + u2[1] ** 2) / (F ** 2 * D)}
    lap = sp.lambdify((R, E), R ** 2 * (sp.diff(F, R, 2) + sp.diff(F, E, 2)) - sp.Rational(3, 4) * F, "mpmath")
    c = {}
    for key, ex in comps.items():
        d = {(0, 0): ex, (1, 0): sp.diff(ex, R), (0, 1): sp.diff(ex, E)}
        d[(2, 0)], d[(1, 1)], d[(0, 2)] = sp.diff(d[(1, 0)], R), sp.diff(d[(1, 0)], E), sp.diff(d[(0, 1)], E)
        c[key] = {o: sp.lambdify((R, E), v, "mpmath") for o, v in d.items()}
    return c, lap


def _curvature(c, r, e):
    """Ricci residual, scalar curvature and the curvature operator's blocks on Lambda^+ and Lambda^- (orientation
    d rho d eta d phi d psi), from the metric's first and second derivatives (the metric depends on rho, eta only)"""
    import mpmath as mp
    r, e = mp.mpf(r), mp.mpf(e)
    n = 4
    g = mp.zeros(n, n)
    dg = [mp.zeros(n, n) for _ in range(n)]
    ddg = [[mp.zeros(n, n) for _ in range(n)] for _ in range(n)]
    for (i, j), f in c.items():
        g[i, j] = g[j, i] = f[(0, 0)](r, e)
        for a, o in ((0, (1, 0)), (1, (0, 1))):
            dg[a][i, j] = dg[a][j, i] = f[o](r, e)
        for (a, b), o in (((0, 0), (2, 0)), ((0, 1), (1, 1)), ((1, 1), (0, 2))):
            val = f[o](r, e)
            for (p, q) in ((a, b), (b, a)):
                ddg[p][q][i, j] = ddg[p][q][j, i] = val
    gi = g ** -1
    G = [[[sum(gi[a, d] * (dg[b][d, cc] + dg[cc][d, b] - dg[d][b, cc]) for d in range(n)) / 2 for cc in range(n)]
          for b in range(n)] for a in range(n)]
    dgi = [-(gi * dg[x] * gi) for x in range(n)]
    dG = [[[[sum(dgi[x][a, d] * (dg[b][d, cc] + dg[cc][d, b] - dg[d][b, cc]) / 2
                 + gi[a, d] * (ddg[x][b][d, cc] + ddg[x][cc][d, b] - ddg[x][d][b, cc]) / 2 for d in range(n))
             for cc in range(n)] for b in range(n)] for a in range(n)] for x in range(n)]
    Rm = {}
    for a, b, cc, d in itertools.product(range(n), repeat=4):
        Rm[a, b, cc, d] = (dG[cc][a][b][d] - dG[d][a][b][cc]
                           + sum(G[a][cc][k] * G[k][b][d] - G[a][d][k] * G[k][b][cc] for k in range(n)))
    Ric = mp.matrix(n, n)
    for b, d in itertools.product(range(n), repeat=2):
        Ric[b, d] = sum(Rm[a, b, a, d] for a in range(n))
    s = sum(gi[b, d] * Ric[b, d] for b in range(n) for d in range(n))
    einstein = max(abs(Ric[i, j] - s / 4 * g[i, j]) for i in range(n) for j in range(n))
    Rl = {key: sum(g[key[0], p] * Rm[p, key[1], key[2], key[3]] for p in range(n)) for key in Rm}
    Ev = (mp.cholesky(g) ** -1).T
    def Rf(i, j, k, l):
        return sum(Ev[p, i] * Ev[q, j] * Ev[u, k] * Ev[v, l] * Rl[p, q, u, v]
                   for p in range(n) for q in range(n) for u in range(n) for v in range(n))
    pairs = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
    Op = mp.matrix(6, 6)
    for A_, (i, j) in enumerate(pairs):
        for B_, (k, l) in enumerate(pairs):
            Op[A_, B_] = Rf(i, j, k, l)            # <R(e_i ^ e_j), e_k ^ e_l>, K(e_i, e_j) = R_ijij
    h = 1 / mp.sqrt(2)
    Pm = mp.matrix([[h, 0, 0, 0, 0, h], [0, h, 0, 0, -h, 0], [0, 0, h, h, 0, 0]])
    Mm = mp.matrix([[h, 0, 0, 0, 0, -h], [0, h, 0, 0, h, 0], [0, 0, h, -h, 0, 0]])
    I3 = mp.eye(3)
    dev = lambda X: max(abs(X[i, j]) for i in range(3) for j in range(3))
    return dict(s=float(s), einstein=float(einstein), minus_block_minus_s_over_12=float(dev(Mm * Op * Mm.T - s / 12 * I3)),
                plus_block_minus_s_over_12=float(dev(Pm * Op * Pm.T - s / 12 * I3)), mixed_block=float(dev(Pm * Op * Mm.T)),
                sectional_rho_eta=float(Op[0, 0]))


def closed_metric(data, r, e):
    """the closed forms: g_rho_rho = g_eta_eta = sum_{i<j} c_ij^2/(r_i r_j) / (sum r)^2 and the torus block
    (u1 u1^T + u2 u2^T)/(F^2 D) with F^2 D = 4 (sum r)^2 sum_{i<j} c_ij^2/(r_i r_j), in (d phi, d psi)"""
    import numpy as np
    a = [float(x) for x, _ in data]
    b = [float(y) for _, y in data]
    k = len(a)
    w = [a[i] * e - b[i] for i in range(k)]
    rr = [np.sqrt(a[i] ** 2 * r * r + w[i] ** 2) for i in range(k)]
    c2 = sum((a[i] * b[j] - a[j] * b[i]) ** 2 / (rr[i] * rr[j]) for i in range(k) for j in range(i + 1, k))
    S = sum(rr)
    u1 = -2 * np.array([sum(w[i] / rr[i] * b[i] for i in range(k)), sum(w[i] / rr[i] * a[i] for i in range(k))])
    u2 = 2 * r * np.array([sum(a[i] / rr[i] * b[i] for i in range(k)), sum(a[i] / rr[i] * a[i] for i in range(k))])
    return c2 / S ** 2, (np.outer(u1, u1) + np.outer(u2, u2)) / (4 * S ** 2 * c2)


def edge_area_orb(data, j):
    """the orbifold area of the exceptional surface over C_j, divided by 2 pi: at rho -> 0 the area density per d eta is
    2 pi sum_{i<l} c_il^2/(|w_i||w_l|) / ((sum |w|)^2 |sum_i a_i (b_i m - a_i n)/|w_i||), (m, n) = v_j"""
    import numpy as np
    from scipy import integrate
    a = [float(x) for x, _ in data]
    b = [float(y) for _, y in data]
    m, n = [float(x) for x in data_vs(data)[j]]
    k = len(a)
    c2 = [[(a[i] * b[l] - a[l] * b[i]) ** 2 for l in range(k)] for i in range(k)]
    def f(e):
        w = [abs(a[i] * e - b[i]) for i in range(k)]
        num = sum(c2[i][l] / (w[i] * w[l]) for i in range(k) for l in range(i + 1, k))
        return num / (sum(w) ** 2 * abs(sum(a[i] * (b[i] * m - a[i] * n) / w[i] for i in range(k))))
    ys = [float(Fr(y) / Fr(x)) for x, y in data]
    kw = dict(limit=400, epsabs=1e-13, epsrel=1e-12)
    if j < k:
        return integrate.quad(f, ys[j - 1], ys[j], **kw)[0]
    return integrate.quad(f, ys[-1], np.inf, **kw)[0] + integrate.quad(f, -np.inf, ys[0], **kw)[0]


def real_locus_area(data):
    """the fixed set of (phi, psi) -> (-phi, -psi): four horizontal sections over H^2, area 4 int int g_rho_rho"""
    import numpy as np
    from scipy import integrate
    val = integrate.dblquad(lambda e, r: closed_metric(data, r, e)[0], 0, np.inf, -np.inf, np.inf, epsabs=1e-11,
                            epsrel=1e-10)[0]
    return 4 * val


IDENTITY_DATA = {
    "CP2": [(Fr(1, 2), Fr(0)), (Fr(1), Fr(1, 2)), (Fr(1, 2), Fr(1, 2))],
    "k3, labels (1,1,3)": [(Fr(1, 2), Fr(0)), (Fr(3, 2), Fr(1)), (Fr(1), Fr(2))],
    "k4 symmetric, labels (2,8,2,4)": [(Fr(1), Fr(-3)), (Fr(1), Fr(-1)), (Fr(1), Fr(1)), (Fr(1), Fr(3))],
    "k5": [(Fr(1, 2), Fr(-1)), (Fr(1, 2), Fr(-1, 2)), (Fr(1, 2), Fr(0)), (Fr(1), Fr(1)), (Fr(1, 2), Fr(3, 2))],
}


def identity():
    import mpmath as mp
    import numpy as np
    out = {}
    for name, data in IDENTITY_DATA.items():
        v = data_vs(data)
        assert all(Fr(x).denominator == 1 for p in v for x in p), (name, v)
        t0 = time.time()
        c, lap = _sympy_metric(data)
        pts = [(0.7, 0.3), (1.9, -1.2), (0.2, 2.5)]
        curv = [_curvature(c, r, e) for r, e in pts]
        worst = 0.0
        for r, e in pts:
            grr, gT = closed_metric(data, r, e)
            sym = [float(c[(0, 0)][(0, 0)](mp.mpf(r), mp.mpf(e))), float(c[(2, 2)][(0, 0)](mp.mpf(r), mp.mpf(e))),
                   float(c[(2, 3)][(0, 0)](mp.mpf(r), mp.mpf(e))), float(c[(3, 3)][(0, 0)](mp.mpf(r), mp.mpf(e)))]
            clo = [grr, gT[0, 0], gT[0, 1], gT[1, 1]]
            worst = max(worst, max(abs(x - y) for x, y in zip(sym, clo)) / max(abs(x) for x in sym))
        _, edges, rows, _ = invariants(data)
        surf = []
        for row in rows:
            area = edge_area_orb(data, row["edge"])                  # area_orb / (2 pi)
            pred = row["chi"] - row["e"]                             # s area_orb/(24 pi) with s = 12: area_orb/(2 pi)
            surf.append(dict(edge=row["edge"], v=row["v"], label=row["label"], e=str(row["e"]), chi_orb=str(row["chi"]),
                             area_orb_over_2pi=area, predicted=str(pred), deviation=abs(area - float(pred))))
        out[name] = dict(v=[(int(m), int(n)) for m, n in v], laplacian_residual=float(abs(lap(mp.mpf("0.7"), mp.mpf("0.3")))),
                         curvature=curv, closed_form_deviation=worst, surfaces=surf, seconds=round(time.time() - t0, 1))
    A = real_locus_area(IDENTITY_DATA["CP2"])
    out["CP2 real locus (RP^2: chi 1, e -1)"] = dict(area_over_4pi=A / (4 * np.pi), predicted=1.0,
                                                     deviation=abs(A / (4 * np.pi) - 1))
    return out


# ---------------------------------------------------------------------------------------------- C. the pairing
def pair_degrees(chi, e):
    """the two twistor sections over a surface F (Euler characteristic chi, normal Euler number e in M) fixed by an isometry
    rotating N_F by theta: normal degrees (d_+, d_-) of the lines where the generator acts by e^{+i theta}, e^{-i theta},
    each computed on the section with its own complex orientation (J_NK: horizontal = tautological, vertical reversed;
    c_1 = 0).  Section + (J agrees with F): T = chi, H(N) = -e (e^{-i theta}), V = e - chi (e^{+i theta}).
    Section - (J reverses F): T = chi, H(N) = -e (e^{+i theta}), V = e - chi (e^{-i theta})."""
    plus = (e - chi, -e)
    minus = (-e, e - chi)
    for T, (d1, d2) in ((chi, plus), (chi, minus)):
        assert T + d1 + d2 == 0                                      # c_1(Y, J_NK) = 0 along each section
    return plus, minus


def pairing():
    out = {}
    plus, minus = pair_degrees(2, 0)            # a great 2-sphere in S^4 fixed by a rotation: B1503's CP^3 pair
    assert (plus, minus) == ((-2, 0), (0, -2))
    out["great sphere in S^4 (CP^3's pair, B1503 P1)"] = dict(plus=plus, minus=minus,
                                                             inflows_over_N=[Fr(plus[0] - plus[1], 2), Fr(minus[0] - minus[1], 2)])
    for e in (-1, -2, -3):                       # a torus: e(N_F) = -s area/(24 pi) < 0 by T2
        p, m = pair_degrees(0, e)
        out[f"torus, e = {e}"] = dict(plus=p, minus=m, inflows_over_N=[Fr(p[0] - p[1], 2), Fr(m[0] - m[1], 2)])
        assert Fr(p[0] - p[1], 2) == e and Fr(m[0] - m[1], 2) == -e
    return {k: {kk: [str(x) for x in vv] if isinstance(vv, list) else vv for kk, vv in v.items()} for k, v in out.items()}


# ---------------------------------------------------------------------------------------------- D. Hitchin's family
def hitchin():
    """SO(3) acting on S^4 = unit traceless symmetric 3x3 matrices by conjugation"""
    import numpy as np
    basis = []
    for (i, j) in ((0, 1), (0, 2), (1, 2)):
        Mx = np.zeros((3, 3)); Mx[i, j] = Mx[j, i] = 1 / np.sqrt(2); basis.append(Mx)
    basis.append(np.diag([1, -1, 0]) / np.sqrt(2))
    basis.append(np.diag([1, 1, -2]) / np.sqrt(6))
    def rep(Rm):
        return np.array([[np.trace(bi @ Rm @ bj @ Rm.T) for bj in basis] for bi in basis])
    rows = []
    for order in range(2, 13):
        t = 2 * np.pi / order
        Rz = np.array([[np.cos(t), -np.sin(t), 0], [np.sin(t), np.cos(t), 0], [0, 0, 1]])
        fixed = int(np.sum(np.abs(np.linalg.eigvals(rep(Rz)) - 1) < 1e-9))
        rows.append(dict(order=order, fixed_subspace_of_R5=fixed, fixed_set_in_S4="2-sphere" if fixed == 3 else "two points"))
    X0 = np.diag([1, 1, -2]) / np.sqrt(6)
    stab = []
    for th in np.linspace(0, 2 * np.pi, 13)[:-1]:
        Rz = np.array([[np.cos(th), -np.sin(th), 0], [np.sin(th), np.cos(th), 0], [0, 0, 1]])
        stab.append(np.allclose(Rz @ X0 @ Rz.T, X0))
    flip = np.diag([1, -1, -1])
    singular = dict(point="diag(1, 1, -2)", fixed_by_rotations_about_its_axis=all(stab),
                    fixed_by_the_half_turn_swapping_the_axis=bool(np.allclose(flip @ X0 @ flip.T, X0)),
                    orbit="SO(3)/O(2) = RP^2")
    assert all(r["fixed_subspace_of_R5"] == (3 if r["order"] == 2 else 1) for r in rows)
    return dict(rotations=rows, singular_orbit=singular)


# ---------------------------------------------------------------------------------------------- E. AW section 2
def aw2(max_w=7, max_r=4):
    """AW (2.7)-(2.10): the cone over WCP^3_{n,n,m,m}/Z_r, gcd(n, m) = 1, the U(1) acting with weights (n, n, m, m) and Z_r by
    (zeta, zeta, 1, 1).  A point's isotropy depends only on its support S (its nonzero coordinates): the pairs (t mod 1,
    k mod r) with t q_i + k z_i / r integral on S, modulo the generic isotropy (support = all four), which acts on nothing.
    The singular strata are the weighted projective spaces of the supports with extra isotropy; the 2-dimensional ones are
    weighted projective lines, i.e. 2-spheres."""
    rows = Counter()
    z = (1, 1, 0, 0)
    for n, m in itertools.product(range(1, max_w + 1), repeat=2):
        if gcd(n, m) != 1:
            continue
        q = (n, n, m, m)
        for r in range(1, max_r + 1):
            def iso(S):
                L = 1
                for i in S:
                    L = L * q[i] // gcd(L, q[i])
                den = L * r
                return sum(1 for num in range(den) for kk in range(r)
                           if all((Fr(num, den) * q[i] + Fr(kk * z[i], r)).denominator == 1 for i in S))
            generic = iso((0, 1, 2, 3))
            for S in itertools.chain.from_iterable(itertools.combinations(range(4), s) for s in (1, 2, 3)):
                extra = iso(S) // generic
                dim = 2 * (len(S) - 1)
                if extra > 1:
                    if dim == 2:
                        rows[f"2-dimensional strata: the line {tuple(sorted(S))} (a 2-sphere)"] += 1
                    else:
                        rows[f"{dim}-dimensional strata"] += 1
            rows["cones (n, m, r)"] += 1
    return dict(sorted(rows.items()))


# ---------------------------------------------------------------------------------------------- run
if __name__ == "__main__":
    what = sys.argv[1] if len(sys.argv) > 1 else "record"
    if what == "census":
        print(json.dumps(census(), indent=1, default=str))
    elif what == "identity":
        print(json.dumps(identity(), indent=1, default=str))
    elif what == "pairing":
        print(json.dumps(pairing(), indent=1, default=str))
    elif what == "hitchin":
        print(json.dumps(hitchin(), indent=1, default=str))
    elif what == "aw2":
        print(json.dumps(aw2(), indent=1, default=str))
    elif what == "record":
        t0 = time.time()
        rec = dict(note="B1505 recorded run (orbifold_links.py record)", census=census(), identity=identity(),
                   pairing=pairing(), hitchin=hitchin(), aw2=aw2())
        rec["seconds"] = round(time.time() - t0, 1)
        (HERE / "orbifold_links.json").write_text(json.dumps(rec, indent=1, default=str) + "\n")
        lines = ["CENSUS"] + [f"  {k}: {v}" for k, v in rec["census"]["tally"].items()]
        lines += ["", "IDENTITY (s = 12; area_orb/2pi against chi_orb - e)"]
        for name, d in rec["identity"].items():
            if "surfaces" in d:
                c = d["curvature"]
                lines.append(f"  {name}: v = {d['v']}, closed forms {d['closed_form_deviation']:.1e}, s = "
                             f"{[round(x['s'], 12) for x in c]}, Einstein {max(x['einstein'] for x in c):.1e}, Lambda^- block "
                             f"{max(x['minus_block_minus_s_over_12'] for x in c):.1e}")
                for srf in d["surfaces"]:
                    lines.append(f"    edge {srf['edge']} v={srf['v']} label {srf['label']}: {srf['area_orb_over_2pi']:.12f} vs "
                                 f"{srf['predicted']} (dev {srf['deviation']:.1e})")
            else:
                lines.append(f"  {name}: area/4pi = {d['area_over_4pi']:.12f} (dev {d['deviation']:.1e})")
        lines += ["", "PAIRING"] + [f"  {k}: {v}" for k, v in rec["pairing"].items()]
        lines += ["", "HITCHIN"] + [f"  order {r['order']}: {r['fixed_set_in_S4']}" for r in rec["hitchin"]["rotations"]]
        lines += [f"  singular orbit: {rec['hitchin']['singular_orbit']}", "", "AW SECTION 2"]
        lines += [f"  {k}: {v}" for k, v in rec["aw2"].items()]
        lines += ["", f"seconds {rec['seconds']}"]
        (HERE / "orbifold_links_run.txt").write_text("\n".join(lines) + "\n")
        print("\n".join(lines))
