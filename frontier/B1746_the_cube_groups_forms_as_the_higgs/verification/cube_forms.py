"""B1746 (P-357; the web seat's THE_NEXT_ATTACK step 3 (c)): the frame's family group's own forms as Higgs directions.
The family group is Gamma_4 = PSL(2, Z/4) acting by rho' = the cube's rotations (W136; B1736); its forms are polynomials in
v = (-th2^2, -th4^2, i th3^2) = 2 eta^3 R, which transforms as rho' (x) chi_eta^6.  A degree-d polynomial triplet P is a form in
rho' when P(g v) = parity(g)^d g P(v) for the 24 signed permutations g of determinant 1 (the character chi_eta^(6d) is
parity^(d/2 mod 2): weights 2 and 6 carry the parity, 4 and 8 do not), and in rho' x sgn with one more factor of parity.
(A) the equivariant triplets of degree 2, 4, 6, 8 in both types, counted on the null cone v.v = 0 (W136's table: rho' 1, 1, 2, 2;
    rho' x sgn 0, 1, 1, 2 at weights 2, 4, 6, 8);
(B) their directions at the band: rho' forms are led by e1 (rho'(T)'s exponent-0 line), so far from null; rho' x sgn forms
    are led by a null line;
(C) exact identities: the weight-2 rho' form is Y2 = (v2v3, v3v1, v1v2) (= -4i eta F_-2, W136); the weight-4 rho' x sgn form
    is v1v2v3 v (R's direction, null); the weight-6 rho' x sgn form is collinear with DR (B1691) at every tau tested.
    python3 -B cube_forms.py      # writes cube_forms.json"""
import sys, json, math, pathlib, itertools, contextlib, io
import numpy as np
import mpmath as mp
HERE = pathlib.Path(__file__).resolve().parent; ROOT = HERE.parents[2]

G = []
for p in itertools.permutations(range(3)):
    for s in itertools.product((1, -1), repeat=3):
        M = np.zeros((3, 3))
        for i in range(3): M[i, p[i]] = s[i]
        if round(np.linalg.det(M)) == 1: G.append(M)
PAR = lambda g: round(np.linalg.det(np.abs(g)))
E1 = np.array([1, 0, 0], dtype=complex); N0 = np.array([0, 1, 1j]) / math.sqrt(2); N1 = np.array([0, 1, -1j]) / math.sqrt(2)


def monos(d): return [m for m in itertools.product(range(d + 1), repeat=3) if sum(m) == d]


def equivariant(d, twist):
    """the degree-d triplets P with P(g v) = parity(g)^twist g P(v), as coefficient vectors over the monomials"""
    ms = monos(d); nm = len(ms); rng = np.random.default_rng(100 * d + twist); rows = []
    for _ in range(4):
        v = rng.normal(size=3) + 1j * rng.normal(size=3)
        for g in G:
            gv = g @ v; f = PAR(g) ** twist
            mgv = np.array([np.prod(gv ** np.array(m)) for m in ms]); mv = np.array([np.prod(v ** np.array(m)) for m in ms])
            for a in range(3):
                r = np.zeros(3 * nm, dtype=complex); r[a * nm:(a + 1) * nm] += mgv
                for b in range(3): r[b * nm:(b + 1) * nm] -= f * g[a, b] * mv
                rows.append(r)
    u, s, vh = np.linalg.svd(np.array(rows)); return ms, vh[np.sum(s > 1e-9 * s[0]):].conj()


def ev(ms, c, v):
    nm = len(ms); mon = np.array([np.prod(v ** np.array(m)) for m in ms]); return np.array([c[a * nm:(a + 1) * nm] @ mon for a in range(3)])


def vt(t):
    T = mp.mpc(t.real, t.imag)
    th2 = complex(mp.fsum(mp.exp(1j * mp.pi * T * (n + mp.mpf(1) / 2) ** 2) for n in range(-30, 30)))
    th3 = complex(mp.fsum(mp.exp(1j * mp.pi * T * n * n) for n in range(-30, 31)))
    th4 = complex(mp.fsum((-1) ** n * mp.exp(1j * mp.pi * T * n * n) for n in range(-30, 31)))
    return np.array([-th2 ** 2, -th4 ** 2, 1j * th3 ** 2])


def dec(h):
    c1, c0, c0b = np.vdot(E1, h), np.vdot(N0, h), np.vdot(N1, h); lead = max(abs(c0), abs(c0b))
    return {"|e1|/|leading null|": float(abs(c1) / lead), "invariant |h.h|/|h|^2": float(abs(h @ h) / np.vdot(h, h).real)}


def cone_rank(ms, null, taus):
    return max(int(np.sum((s := np.linalg.svd(np.array([ev(ms, c, vt(t)) for c in null]), compute_uv=False)) > 1e-8 * s[0])) for t in taus)


if __name__ == "__main__":
    res = {}; taus = (complex(0.31, 1.7), complex(0.4375, 2.1), complex(0.8125, 3.2))
    # the weight's character: chi_eta^(6d) = parity^(d/2 mod 2), so rho' forms need twist d/2 mod 2 and rho' x sgn one more
    for d in (2, 4, 6, 8):
        for typ in ("rho'", "rho' x sgn"):
            tw = (d // 2 + (1 if typ == "rho' x sgn" else 0)) % 2
            ms, null = equivariant(d, tw); r = cone_rank(ms, null, taus) if len(null) else 0
            row = {"weight": d, "type": typ, "dimension on the null cone": r}
            if r:
                t = complex(0.4375, 2.1); H = np.array([ev(ms, c, vt(t)) for c in null]); dirs = np.linalg.svd(H)[2][:r]
                row["directions at 0.4375 + 2.1i (an orthonormal basis)"] = [dec(dirs[i]) for i in range(r)]
            res["%s, weight %d" % (typ, d)] = row; print(row, flush=True)
    sys.path.insert(0, str(ROOT / "frontier" / "B1691_the_exponents_at_the_two_fixed_points" / "verification"))
    from importlib import util
    spec = util.spec_from_file_location("te", ROOT / "frontier" / "B1691_the_exponents_at_the_two_fixed_points" / "verification" / "the_exponents.py")
    te = util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(te)
    ms6, null6 = equivariant(6, (3 + 1) % 2); ident = {}
    for t in (complex(0.13, 1.4), complex(0.4375, 2.1), complex(0.7, 2.9), complex(0.25, 3.6)):
        v = vt(t); W6 = np.array([ev(ms6, c, v) for c in null6]); w6 = np.linalg.svd(W6)[2][0]
        DR = np.array([complex(te.ev(c, mp.mpc(t.real, t.imag))) for c in te.B[1]])
        R = v[0] * v[1] * v[2] * v
        cos = lambda a, b: float(abs(np.vdot(a, b)) / np.linalg.norm(a) / np.linalg.norm(b))
        ident[str(t)] = {"1 - |cos(weight-6 rho' x sgn, DR)|": 1 - cos(w6, DR), "R null: |R.R|/|R|^2": float(abs(R @ R) / np.vdot(R, R).real)}
    res["identities"] = ident; print("identities", ident)
    # (D) the weight-6 rho' space against the zero-free pair F_6, F_-6 (W143's h(12, 1)), and the weight-8 spaces against the others
    def F(a, t):
        T = mp.mpc(t.real, t.imag)
        th2 = mp.fsum(mp.exp(1j * mp.pi * T * (n + mp.mpf(1) / 2) ** 2) for n in range(-30, 30)); th3 = mp.fsum(mp.exp(1j * mp.pi * T * n * n) for n in range(-30, 31))
        th4 = mp.fsum((-1) ** n * mp.exp(1j * mp.pi * T * n * n) for n in range(-30, 31)); eps = 1j ** ((a + 2) // 2)
        return np.array([complex(eps * th2 ** a), complex(eps * th4 ** a), complex(1j * th3 ** a)])
    def sin_angle(U, V):
        qu = np.linalg.qr(U.T)[0]; qv = np.linalg.qr(V.T)[0]; s_ = np.linalg.svd(qu.conj().T @ qv, compute_uv=False); return float(np.sqrt(max(0.0, 1 - min(s_) ** 2)))
    spans = {}
    for key, (d, tw), pair in (("rho' w6", (6, 1), (6, -6)), ("rho' w8", (8, 0), (22, -2)), ("rho' w8", (8, 0), (14, -10)), ("rho' x sgn w8", (8, 1), (22, -2))):
        ms, null = equivariant(d, tw); vals = []
        for t in (complex(0.3, 1.9), complex(0.4375, 2.6)):
            H = np.array([ev(ms, c, vt(t)) for c in null]); Bs = np.linalg.svd(H)[2][:2]
            vals.append(sin_angle(Bs, np.array([F(pair[0], t), F(pair[1], t)])))
        spans["%s vs span{F%d, F%d}" % (key, pair[0], pair[1])] = vals
    res["spans"] = spans; print("spans", spans)
    (HERE / "cube_forms.json").write_text(json.dumps(res, indent=1) + "\n")
