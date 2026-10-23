"""B1736 (P-302): W135's joint family group on main, built independently, and B1656's four channels read against it.  Data-free.
  A  E8 from 2I (Conway-Sloane: the icosians with EN(a + b sqrt5) = a + b, roots = 2I and phi^-1 2I), own exact
     arithmetic over Q(sqrt5): 240 roots of norm 2, simple roots by a generic functional and their Cartan matrix (E8's,
     det 1); 2I's 20 order-3 elements in one class, 10 subgroups; each frame {+-1, +-w, +-w^2} (A2), 72 roots orthogonal
     to 1 and w (E6), 162 in six classes of 27; conjugation by 2I permutes the 10 frames transitively
  B  the object's order-3 element: <R, L> mod 5 = SL(2, 5) -> 2I (R, L to order-5 units, extended along words),
     g = -R L^-1 to g_q of order 3; left multiplication by g_q is an isometry of E8 that preserves g_q's frame, rotates
     its A2, and permutes its six classes in two 3-cycles; B1275's sum rules on that frame; and how left multiplication
     compares with the A2 Weyl rotation s_a s_b (B1275's family element)
  C  W135's K3 with main's rho (B1730 part A): Gamma' = rho (x) chi_eta^k for k = 5, 13, 21 (det 1): orders, real
     rotations, dim of the Sym^3 and Lambda^3 invariants, Sym^3 rho' against Gamma's one-dimensional characters and rho'
  D  B1656's coupling (B1723's b1656_funcs, as every census since) as a tensor: channel 1 = -eps (Lambda^3, E8's family
     coupling), channels (i, j, k) = -d_ab d_cs + d_ac d_bs + d_as d_bc, so with S = h0 + h.(i, j, k) and weights (u1, u):
     Y = h0 (u1 1 + [u]_x)' + u h^T + h u^T - (u.h) 1 - u1 [h]_x   (checked against coupling() on random complex input,
     with B1659's determinant law as a control)
  E  the channel weights under T (B1724's move (tau, b) -> (tau + 1, b - alpha)) and S ((tau, (alpha, b), L) ->
     (-1/tau, (-b, alpha), L + log|tau|)): is (u1, u) -> scalar (u1, R u) with R the rotation by which the Higgs moves?
    python3 -B the_family_group.py      # writes the_family_group.json beside itself
Importing computes nothing."""
import sys, io, json, math, itertools, contextlib, importlib.util, pathlib, collections, random
from fractions import Fraction as F
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())


# ------------------------------------------------------------------ exact Q(sqrt5): pairs (a, b) = a + b sqrt5
def a5(x, y): return (x[0] + y[0], x[1] + y[1])
def m5(x, y): return (x[0] * y[0] + 5 * x[1] * y[1], x[0] * y[1] + x[1] * y[0])
def n5(x): return (-x[0], -x[1])
Z5, O5, H5 = (F(0), F(0)), (F(1), F(0)), (F(1, 2), F(0))
PHI, PHII = (F(1, 2), F(1, 2)), (F(-1, 2), F(1, 2))


def qm(p, q):
    a1, b1, c1, d1 = p; a2, b2, c2, d2 = q
    s = lambda *xs: (sum(x[0] for x in xs), sum(x[1] for x in xs))
    return (s(m5(a1, a2), n5(m5(b1, b2)), n5(m5(c1, c2)), n5(m5(d1, d2))),
            s(m5(a1, b2), m5(b1, a2), m5(c1, d2), n5(m5(d1, c2))),
            s(m5(a1, c2), n5(m5(b1, d2)), m5(c1, a2), m5(d1, b2)),
            s(m5(a1, d2), m5(b1, c2), n5(m5(c1, b2)), m5(d1, a2)))


def qc(p): return (p[0], n5(p[1]), n5(p[2]), n5(p[3]))
def qneg(p): return tuple(n5(x) for x in p)
def EN(x): return x[0] + x[1]
def form(p, q): return 2 * EN(qm(p, qc(q))[0])                 # B(p, q) = 2 EN(Re(p qbar))
ONE = (O5, Z5, Z5, Z5)


def icosians():
    out = set()
    for k in range(4):
        for s in (1, -1):
            v = [Z5] * 4; v[k] = (F(s), F(0)); out.add(tuple(v))
    for sg in itertools.product((1, -1), repeat=4): out.add(tuple((F(s, 2), F(0)) for s in sg))
    vals = (PHI, O5, PHII, Z5)
    for p in itertools.permutations(range(4)):
        if sum(1 for i in range(4) for j in range(i + 1, 4) if p[i] > p[j]) % 2: continue
        for sg in itertools.product((1, -1), repeat=3):
            v = [None] * 4
            for pos in range(4):
                x = vals[pos] if pos == 3 else m5(vals[pos], (F(sg[pos]), F(0)))
                v[p[pos]] = m5(x, H5)
            out.add(tuple(v))
    return sorted(out)


def order(u):
    p, n = u, 1
    while p != ONE: p, n = qm(p, u), n + 1
    return n


def part_a():
    U = icosians(); roots = sorted(set(U) | {tuple(m5(PHII, x) for x in u) for u in U})
    R = set(roots)
    norm2 = all(form(r, r) == 2 for r in roots)
    # simple roots: a generic rational functional on the 8 rational coordinates
    rng = random.Random(302); fvec = [F(rng.randint(1, 10 ** 6), 10 ** 6) for _ in range(8)]
    val = lambda r: sum(fvec[2 * k] * r[k][0] + fvec[2 * k + 1] * r[k][1] for k in range(4))
    pos = [r for r in roots if val(r) > 0]
    pset = set(pos)
    # a positive root is simple iff it is not the sum of two positive roots
    sums = {tuple(a5(x, y) for x, y in zip(a, b)) for a in pos for b in pos}
    simple = [r for r in pos if r not in sums]
    cartan = [[form(a, b) for b in simple] for a in simple]
    import sympy as sp
    detC = sp.Matrix(cartan).det()
    degs = sorted(sum(1 for b in range(len(simple)) if b != a and cartan[a][b] != 0) for a in range(len(simple)))
    # 2I's order-3 elements, subgroups, frames
    o3 = [u for u in U if order(u) == 3]
    cls = {qm(qm(v, o3[0]), qc(v)) for v in U}
    subs = {frozenset({w, qm(w, w)}) for w in o3}
    frames, ok = {}, True
    for sg in subs:
        w = min(sg); a2 = {ONE, w, qm(w, w)}; a2 |= {qneg(x) for x in a2}
        e6 = [r for r in roots if form(r, ONE) == 0 and form(r, w) == 0]
        rest = [r for r in roots if r not in a2 and r not in set(e6)]
        c = collections.Counter((form(r, ONE), form(r, w)) for r in rest)
        ok &= len(e6) == 72 and len(rest) == 162 and sorted(c.values()) == [27] * 6 and a2 <= R
        frames[sg] = frozenset(e6)
    f0 = frames[next(iter(subs))]
    imgs = {frozenset(qm(qm(v, r), qc(v)) for r in f0) for v in U}
    return {"icosians": len(U), "roots": len(roots), "all_norm_2": norm2, "simple_roots": len(simple),
            "cartan_det": int(detC), "cartan_entries": sorted({x for row in cartan for x in row}),
            "dynkin_degrees": degs, "is_E8_diagram": degs == [1, 1, 1, 2, 2, 2, 2, 3] and int(detC) == 1,
            "order3": len(o3), "order3_one_class": cls == set(o3), "subgroups": len(subs),
            "frames_72_and_6x27_with_A2_roots": bool(ok), "frames_distinct": len(set(frames.values())) == 10,
            "conjugation_transitive_on_frames": imgs == set(frames.values())}, U, roots


def part_b(U, roots):
    def mul(A, B): return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(2)) % 5 for j in range(2)) for i in range(2))
    I2, R5, L5 = ((1, 0), (0, 1)), ((1, 1), (0, 1)), ((1, 0), (1, 1))
    o5 = [u for u in U if order(u) == 5]; iso = None
    for r in o5:
        for l in o5:
            img, fr, good = {I2: ONE}, [I2], True
            while fr and good:
                nx = []
                for M in fr:
                    for G, q in ((R5, r), (L5, l)):
                        P, Q = mul(M, G), qm(img[M], q)
                        if P in img:
                            if img[P] != Q: good = False; break
                        else: img[P] = Q; nx.append(P)
                    if not good: break
                fr = nx
            if good and len(img) == 120 and len(set(img.values())) == 120: iso = img; break
        if iso: break
    Linv = ((1, 0), (4, 1)); g = mul(R5, Linv); g = tuple(tuple((-x) % 5 for x in row) for row in g)
    gq = iso[g]; o = order(gq)
    a2 = [ONE, gq, qm(gq, gq)]; a2 += [qneg(x) for x in a2]
    e6 = [r for r in roots if form(r, ONE) == 0 and form(r, gq) == 0]
    rest = [r for r in roots if r not in set(a2) and r not in set(e6)]
    key = lambda r: (form(r, ONE), form(r, gq)); classes = sorted({key(r) for r in rest})
    Lg = lambda r: qm(gq, r)
    iso_ok = all(form(Lg(a), Lg(b)) == form(a, b) for a in roots[:60] for b in roots)
    keeps = set(map(Lg, e6)) == set(e6) and set(map(Lg, a2)) == set(a2)
    perm = {c: collections.Counter(key(Lg(r)) for r in rest if key(r) == c) for c in classes}
    pmap = {c: list(perm[c])[0] for c in classes if len(perm[c]) == 1}
    cyc = []; seen = set()
    for c in classes:
        if c in seen or c not in pmap: continue
        cy, x = [], c
        while x not in seen: seen.add(x); cy.append(x); x = pmap[x]
        cyc.append(len(cy))
    Rs = set(roots)
    add = lambda a, b: tuple(a5(x, y) for x, y in zip(a, b))
    same = sum(1 for c in classes for a in rest if key(a) == c for b in rest if key(b) == c and add(a, b) in Rs)
    # B1275's family element: the A2 Weyl rotation s_a s_b with a = 1, b = gq (B(1, gq) = -1)
    def refl(v, a): k = form(v, a); return tuple(a5(x, m5((F(-k), F(0)), y)) for x, y in zip(v, a))   # B(a, a) = 2
    sab = lambda r: refl(refl(r, gq), ONE)
    weyl_perm = {c: collections.Counter(key(sab(r)) for r in rest if key(r) == c) for c in classes}
    weyl_fixes_e6 = all(sab(r) == r for r in e6)
    left_fixes_e6 = all(Lg(r) == r for r in e6)
    same_perm = all(len(weyl_perm[c]) == 1 and list(weyl_perm[c])[0] == pmap.get(c) for c in classes)
    return {"SL25_to_2I_found": iso is not None, "g = -R L^-1 mod 5": g, "g_q": [[str(x[0]), str(x[1])] for x in gq], "order_g_q": o,
            "left_mult_isometry": iso_ok, "left_mult_preserves_frame": keeps, "six_classes": len(classes),
            "left_mult_cycles_on_classes": sorted(cyc), "same_class_sums_that_are_roots": same,
            "weyl_sab_fixes_E6_pointwise": weyl_fixes_e6, "left_mult_fixes_E6_pointwise": left_fixes_e6,
            "left_mult_and_weyl_same_class_permutation": same_perm}


def part_c():
    w = np.exp(1j * np.pi / 4)
    rT = w * np.array([[1, 0, 0], [0, 0, 1], [0, -1, 0]], dtype=complex); rS = w * np.array([[0, 1, 0], [1, 0, 0], [0, 0, 1]], dtype=complex)
    cT, cS = np.exp(2j * np.pi / 24), np.exp(-1j * np.pi / 4)
    keyf = lambda M: tuple(np.round(M, 8).reshape(-1).view(float))
    out = {}
    for k in (5, 13, 21):
        gens = [rT * cT ** k, rS * cS ** k]
        assert all(abs(np.linalg.det(g) - 1) < 1e-12 for g in gens)
        I3 = np.eye(3, dtype=complex); G, fr = {keyf(I3): I3}, [I3]
        while fr:
            nx = []
            for x in fr:
                for g in gens:
                    y = x @ g; kk = keyf(y)
                    if kk not in G: G[kk] = y; nx.append(y)
            fr = nx
        M = list(G.values()); chi = lambda g: np.trace(g)
        s3 = lambda g: (chi(g) ** 3 + 3 * chi(g @ g) * chi(g) + 2 * chi(g @ g @ g)) / 6
        l3 = lambda g: (chi(g) ** 3 - 3 * chi(g @ g) * chi(g) + 2 * chi(g @ g @ g)) / 6
        avg = lambda f: np.mean([f(g) for g in M])
        orders = collections.Counter()
        for g in M:
            n, P = 1, g.copy()
            while not np.allclose(P, np.eye(3)): P, n = P @ g, n + 1
            orders[n] += 1
        real = all(np.allclose(g.imag, 0) for g in M)
        row = {"order": len(M), "real": real, "element_orders": dict(sorted(orders.items())),
               "dim_Sym3_inv": round(avg(s3).real, 9), "dim_Lambda3_inv": round(avg(l3).real, 9),
               "<Sym3,Sym3>": round(avg(lambda g: abs(s3(g)) ** 2).real, 9),
               "Sym3 x rho'": round(avg(lambda g: s3(g) * np.conj(chi(g))).real, 9)}
        if real:
            sg = lambda g: round(np.linalg.det(np.abs(g)).real)
            row["Sym3 x sign"] = round(avg(lambda g: s3(g) * sg(g)).real, 9)
            row["Sym3 x rho' sign"] = round(avg(lambda g: s3(g) * np.conj(chi(g)) * sg(g)).real, 9)
        out[str(k)] = row
    return out


def _b():
    sys.path.insert(0, str(ROOT / "frontier" / "B1723_the_golden_valley" / "verification")); argv = sys.argv; sys.argv = ["x"]
    with contextlib.redirect_stdout(io.StringIO()): import b1656_funcs as B
    sys.argv = argv
    return B


def cross(v): return np.array([[0, -v[2], v[1]], [v[2], 0, -v[0]], [-v[1], v[0], 0]])


def part_d():
    B = _b(); rng = np.random.default_rng(302)
    # the family blocks are (QJ, QI, QK): index a of coupling() is unit (j, i, k)[a]; read every tensor in the (i, j, k) order
    P = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
    worst, worst_det = 0.0, 0.0
    for _ in range(50):
        h0, u1 = rng.normal(size=2) + 1j * rng.normal(size=2); h = rng.normal(size=3) + 1j * rng.normal(size=3); u = rng.normal(size=3) + 1j * rng.normal(size=3)
        S = h0 * np.eye(2) + h[0] * B.QI + h[1] * B.QJ + h[2] * B.QK
        M = B.weighted_M({"1": u1, "i": u[0], "j": u[1], "k": u[2]})
        Yf = P @ B.coupling(S, M) @ P.T
        Yc = np.outer(u, h) + np.outer(h, u) - (u @ h) * np.eye(3) + u1 * cross(h) + h0 * (u1 * np.eye(3) + cross(u))
        Yc2 = np.outer(u, h) + np.outer(h, u) - (u @ h) * np.eye(3) + u1 * cross(h) + h0 * (u1 * np.eye(3) - cross(u))
        e = min(np.abs(Yf - Yc).max(), np.abs(Yf - Yc2).max()) / np.abs(Yf).max()
        which = "+" if np.abs(Yf - Yc).max() <= np.abs(Yf - Yc2).max() else "-"
        worst = max(worst, e)
        dl = abs(np.linalg.det(Yf) - 4 * np.linalg.det(S) * np.linalg.det(M) * np.trace(B.EPS @ S @ M.T)) / max(1e-300, abs(np.linalg.det(Yf)))
        worst_det = max(worst_det, dl)
    # with u = 0: Y = -u1 [h]_x is rank 2 for every h (the third mass vanishes)
    rk = max(np.linalg.svd(cross(rng.normal(size=3) + 1j * rng.normal(size=3)), compute_uv=False)[2] for _ in range(100))
    return {"closed_form_vs_coupling_rel": float(worst), "h0_cross_sign": which, "B1659_det_law_rel": float(worst_det),
            "u=0: max third singular value of [h]_x over 100 complex h": float(rk)}


def part_e():
    import mpmath as mp
    B = _b()
    P1691 = ROOT / "frontier" / "B1691_the_exponents_at_the_two_fixed_points" / "verification"; sys.path.insert(0, str(P1691))
    spec = importlib.util.spec_from_file_location("te", P1691 / "the_exponents.py"); te = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(te)
    comp = lambda t: np.array([complex(te.ev(cc, mp.mpc(t.real, t.imag))) for cc in te.B[1]])
    SIXY = B.SIXY; SECT = {"up": ("Q", "u"), "down": ("Q", "d"), "lep": ("L", "e")}
    def weights(t, a, b, L=1.0):  # L: the end, passed as B1724 does
        w = float(a) * t + float(b); out = {}
        for sec, (lf, rf) in SECT.items():
            x, y = B.sector_twists(w, t, SIXY[lf], SIXY[rf]); R = B.residues(x, y, t); c = B.cA(x, y, t, R)
            out[sec] = np.array([(math.sqrt(2 * math.pi * L + c[s]) * R[s] if c[s] is not None and 2 * math.pi * L + c[s] > 0 else 0) for s in ("1", "i", "j", "k")])
        return out
    Rm90 = np.array([[1, 0, 0], [0, 0, 1], [0, -1, 0]], dtype=float)
    rows = []
    for t, (a, b) in ((complex(0.3, 1.4), (F(2, 5), F(1, 10))), (complex(-0.2, 1.7), (F(1, 3), F(1, 5))), (complex(0.15, 1.25), (F(3, 7), F(2, 7)))):
        h0, h1 = comp(t), comp(t + 1)
        hfit = np.vdot(Rm90 @ h0, h1) / np.vdot(Rm90 @ h0, Rm90 @ h0)
        w0, w1 = weights(t, a, b), weights(t + 1, a, b - a)
        for sec in w0:
            u0, v1 = w0[sec], w1[sec]
            # the best phase for u1 and for the triplet under R_-90 (the Higgs's rotation), and the residuals
            ph1 = v1[0] / u0[0] if abs(u0[0]) > 1e-14 else 0
            Ru = Rm90 @ u0[1:]; phv = np.vdot(Ru, v1[1:]) / np.vdot(Ru, Ru)
            res_v = np.linalg.norm(v1[1:] - phv * Ru) / np.linalg.norm(v1[1:])
            rows.append({"move": "T", "tau": [t.real, t.imag], "line": [str(a), str(b)], "sector": sec,
                         "higgs_resid_R_-90": float(np.linalg.norm(h1 - hfit * (Rm90 @ h0)) / np.linalg.norm(h1)),
                         "higgs_phase/(2pi)": float(np.angle(hfit) / (2 * np.pi)),
                         "u1_ratio_abs": float(abs(ph1)), "u1_phase/(2pi)": float(np.angle(ph1) / (2 * np.pi)) if ph1 else None,
                         "triplet_resid_R_-90": float(res_v), "triplet_ratio_abs": float(abs(phv)), "triplet_phase/(2pi)": float(np.angle(phv) / (2 * np.pi))})
        # S: tau -> -1/tau, (alpha, b) -> (-b, alpha), L -> L + log|tau| (B1724); the Higgs by rho(S) ~ P (the i-j swap)
        Pm = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 1]], dtype=float)
        hS = comp(-1 / t); kS = np.vdot(Pm @ h0, hS) / np.vdot(Pm @ h0, Pm @ h0)
        wS = weights(-1 / t, -b, a, 1.0 + math.log(abs(t)))
        for sec in w0:
            u0, v1 = w0[sec], wS[sec]
            ph1 = v1[0] / u0[0] if abs(u0[0]) > 1e-14 else 0
            Pu = Pm @ u0[1:]; phv = np.vdot(Pu, v1[1:]) / np.vdot(Pu, Pu)
            rows.append({"move": "S", "tau": [t.real, t.imag], "line": [str(a), str(b)], "sector": sec,
                         "higgs_resid_P": float(np.linalg.norm(hS - kS * (Pm @ h0)) / np.linalg.norm(hS)),
                         "u1_ratio": [float(abs(ph1)), float(np.angle(ph1) / (2 * np.pi))] if ph1 else None,
                         "triplet_resid_P": float(np.linalg.norm(v1[1:] - phv * Pu) / np.linalg.norm(v1[1:])),
                         "triplet_ratio": [float(abs(phv)), float(np.angle(phv) / (2 * np.pi))]})
    return rows


def main():
    a, U, roots = part_a(); print("A", json.dumps(a, default=str))
    b = part_b(U, roots); print("B", json.dumps(b, default=str))
    c = part_c(); print("C", json.dumps(c, default=str))
    d = part_d(); print("D", json.dumps(d, default=str))
    e = part_e(); print("E", json.dumps(e, indent=0, default=str))
    json.dump({"A": a, "B": b, "C": c, "D": d, "E": e}, open(HERE / "the_family_group.json", "w"), indent=1, default=str)


if __name__ == "__main__":
    main()
