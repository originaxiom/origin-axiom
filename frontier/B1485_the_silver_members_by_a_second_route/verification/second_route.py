#!/usr/bin/env python3
"""B1485 -- main's second route for the SM seat's sm:B1530 members (one generation in one W on the silver squares).

INPUT: the seat's `members_for_main.json` only (presentation, cusp words, exact holonomy in PGL(2, Q(i)), the four's
convention, the member characters).  It holds no class, index, dimension or reading.
INSTRUMENT: main's banked class index -- B1418's `c2_reducible_index.counts` (exact ranks over a number field by
regular-representation blocks; banked control: m010's witness I = +1), here over K = Q(zeta_8) = Q[x]/(x^4 + 1), which
contains i = x^2 and sqrt 2 = x - x^3.  Everything else in this file is written for this arc and shares no code with
the seat: the four, the cocycles, the extension modules, the exterior square, and a floating-point twin of the counts.
NOT BLIND: main had read the seat's readings before writing this (disclosed in the seal).

  second_route.py controls            the controls only (run before the seal)
  second_route.py census STATE        the eight sign characters on a state: a0, a1, t0, r1, n for V = nu (x) four
  second_route.py members STATE       the readings (I(W1), I(Lambda^2 W1)) at every class type, at the members
"""
import sys, json, pathlib, itertools
from fractions import Fraction as Fr
import math
HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(p for p in [HERE, *HERE.parents] if (p / "frontier" / "B1418_the_family_as_the_object").is_dir())
sys.path.insert(0, str(ROOT / "frontier" / "B1418_the_family_as_the_object" / "verification"))
import c2_reducible_index as CI
from sympy.polys.matrices import DomainMatrix
from sympy import QQ
import mpmath as mp
mp.mp.dps = 50
TOL = mp.mpf(10) ** -30

K = CI.NF([1, 0, 0, 0, 1])                      # Q(zeta_8): x^4 + 1
X = K.alpha(); ONE = K.const(1); ZERO = K.const(0)
I_ = K.pw(X, 2)                                  # i
SQRT2 = K.sub(X, K.pw(X, 3))                     # zeta + zeta^-1, positive at x = exp(i pi/4)
assert K.mul(I_, I_) == K.const(-1) and K.mul(SQRT2, SQRT2) == K.const(2)
ZETA = mp.e ** (mp.j * mp.pi / 4)


def conj(a): return (a[0], -a[3], -a[2], -a[1])  # x -> x^-1 = -x^3
def cx(a): return sum(mp.mpf(a[k].numerator) / a[k].denominator * ZETA ** k for k in range(4))
def gauss(re, im): return K.el([Fr(re), 0, Fr(im), 0])
def kscale(c, M): return [[K.mul(c, x) for x in r] for r in M]
def kadd(P, Q): return [[K.add(a, b) for a, b in zip(r, s)] for r, s in zip(P, Q)]
def is_zero_mat(M): return all(K.is_zero(x) for r in M for x in r)


def rational_sqrt(q):
    """sqrt of a positive rational if it is a rational square, else None"""
    n, d = q.numerator, q.denominator; a, b = math.isqrt(n), math.isqrt(d)
    return Fr(a, b) if a * a == n and b * b == d else None


def abs_det(g):
    """|det g| in K, positive at the standard embedding: a rational, or a rational times sqrt 2"""
    det = K.sub(K.mul(g[0][0], g[1][1]), K.mul(g[0][1], g[1][0])); N = K.mul(det, conj(det))
    assert N[1] == N[2] == N[3] == 0 and N[0] > 0, N
    r = rational_sqrt(N[0])
    if r is not None: return K.const(r)
    r = rational_sqrt(N[0] / 2); assert r is not None, ("norm of det is neither a square nor twice a square", N[0])
    return K.mul(K.const(r), SQRT2)


def four(g):
    """the four: H -> g H g^* / |det g| on H = [[x1, x3 + i x4], [x3 - i x4, x2]], coordinates (x1, x2, x3, x4)"""
    gs = [[conj(g[0][0]), conj(g[1][0])], [conj(g[0][1]), conj(g[1][1])]]
    basis = [[[ONE, ZERO], [ZERO, ZERO]], [[ZERO, ZERO], [ZERO, ONE]], [[ZERO, ONE], [ONE, ZERO]], [[ZERO, I_], [K.neg(I_), ZERO]]]
    s = K.inv(abs_det(g)); half = K.const(Fr(1, 2)); inv2i = K.inv(K.mul(K.const(2), I_)); cols = []
    for H in basis:
        Hp = CI.kmat_mul(K, CI.kmat_mul(K, g, H), gs)
        cols.append([K.mul(s, Hp[0][0]), K.mul(s, Hp[1][1]), K.mul(s, K.mul(half, K.add(Hp[0][1], Hp[1][0]))),
                     K.mul(s, K.mul(inv2i, K.sub(Hp[0][1], Hp[1][0])))])
    return [[cols[j][i] for j in range(4)] for i in range(4)]


def ext2(M):
    n = len(M); pairs = list(itertools.combinations(range(n), 2))
    return [[K.sub(K.mul(M[i][k], M[j][l]), K.mul(M[i][l], M[j][k])) for (k, l) in pairs] for (i, j) in pairs]


def k_nullspace(P):
    """a K-basis of {v : P v = 0}, by the rational regular representation"""
    if not P: return []
    d = K.d; rows = []
    for i in range(len(P)):
        for a in range(d):
            row = []
            for j in range(len(P[0])):
                R = K.regmat(P[i][j]); row += [QQ(int(R[a][b].numerator), int(R[a][b].denominator)) for b in range(d)]
            rows.append(row)
    dm = DomainMatrix(rows, (len(rows), len(rows[0])), QQ); ns = dm.nullspace().to_Matrix()
    out = []
    for r in range(ns.rows):
        v = [K.el([Fr(int(ns[r, j * d + b].p), int(ns[r, j * d + b].q)) for b in range(d)]) for j in range(len(P[0]))]
        if CI.kmat_rank(K, [list(c) for c in zip(*(out + [v]))]) == len(out) + 1: out.append(v)
    assert len(out) * d == ns.rows, (len(out), ns.rows)
    return out


def load(path, state):
    d = json.load(open(path)); s = d["states"][state]
    hol = {g: [[gauss(*e) for e in row] for row in m] for g, m in s["holonomy (PGL(2, Q(i)); entries [re, im])"].items()}
    members = [m["nu on a, b, t"] for m in s["members"]]
    return dict(name=s["SnapPy"], gens=s["generators"], rels=s["relators"], cusp=s["cusp words"], hol=hol, members=members)


def frame(S, nu):
    """V = nu (x) four on the generators"""
    return {g: kscale(K.const(nu[g]), four(S["hol"][g])) for g in S["gens"]}


def setup(S, rep):
    """the cochain matrices of main's instrument, rebuilt here (the instrument's `counts` returns only the numbers)"""
    gens, rels = S["gens"], S["rels"]; mu, lam = S["cusp"]; n = len(rep[gens[0]]); Id = CI.kmat_eye(K, n); D = {}
    for g in gens: D[g] = rep[g]; D[g.upper()] = CI.kmat_inv(K, rep[g])
    d0 = CI.vstack(*[CI.kmat_sub(K, D[g], Id) for g in gens])
    d1 = CI.vstack(*[CI.hstack(*[CI.fox(K, r, D, gens)[1][g] for g in gens]) for r in rels])
    fm, fl = CI.fox(K, mu, D, gens)[1], CI.fox(K, lam, D, gens)[1]
    R = CI.vstack(CI.hstack(*[fm[g] for g in gens]), CI.hstack(*[fl[g] for g in gens]))
    BT = CI.vstack(CI.kmat_sub(K, CI.word_matrix(K, mu, D), Id), CI.kmat_sub(K, CI.word_matrix(K, lam, D), Id))
    return dict(n=n, D=D, d0=d0, d1=d1, R=R, BT=BT)


def classes(S, V):
    """cocycles of V on the generators: a basis of Z^1 modulo B^1 split as (interior, boundary-type).
    interior = restricts to a coboundary on the cusp.  Returned as lists of K-vectors of length 3n."""
    c = setup(S, V); n = c["n"]; ng = len(S["gens"])
    zeros = [[ZERO] * n for _ in range(len(c["d1"]))]
    block = CI.vstack(CI.hstack(c["d1"], zeros), CI.hstack(c["R"], c["BT"]))
    d0cols = [list(col) for col in zip(*c["d0"])]            # B^1 spanned by the columns of d0
    def indep(vs): return CI.kmat_rank(K, [list(col) for col in zip(*vs)]) if vs else 0
    base = list(d0cols); r0 = indep(base); interior = []
    for v in k_nullspace(block):
        z = v[:ng * n]
        if indep(base + interior + [z]) > r0 + len(interior): interior.append(z)
    boundary = []
    for z in k_nullspace(c["d1"]):
        if indep(base + interior + boundary + [z]) > r0 + len(interior) + len(boundary): boundary.append(z)
    return interior, boundary


def extension(S, V, z):
    """W1 = [[V, z], [0, 1]] on the generators"""
    n = 4; out = {}
    for k, g in enumerate(S["gens"]):
        zg = z[k * n:(k + 1) * n]
        out[g] = [list(V[g][i]) + [zg[i]] for i in range(n)] + [[ZERO] * n + [ONE]]
    return out


def reading(S, rep, label):
    """I = n(E) - n(E*) by main's instrument, with the identity I = a0 - a0* + t0* - r1 as a check"""
    mu, lam = S["cusp"]
    nE, (a0, a1, t0, r1) = CI.counts(K, S["gens"], S["rels"], mu, lam, rep, label, verbose=False)
    nD, (b0, b1, s0, q1) = CI.counts(K, S["gens"], S["rels"], mu, lam, CI.dual(K, rep), label + "*", verbose=False)
    I = nE - nD; ident = (a0 - b0) + s0 - r1
    return dict(I=I, identity=ident, ok=(I == ident), E=dict(a0=a0, a1=a1, t0=t0, r1=r1, n=nE), Edual=dict(a0=b0, a1=b1, t0=s0, r1=q1, n=nD))


# ------------------------------------------------------------------------------------------- the floating-point twin
def num_rank(M):
    if M.rows == 0 or M.cols == 0: return 0
    s = mp.svd_c(M, compute_uv=False); top = max(1, abs(s[0]))
    return sum(1 for i in range(len(s)) if abs(s[i]) > TOL * top)


def to_mp(P): return mp.matrix([[cx(x) for x in r] for r in P])


def reading_numeric(S, rep):
    """the same counts from the embedded matrices by SVD ranks; its own code path"""
    def side(rp):
        c = setup(S, rp); n = c["n"]; ng = len(S["gens"])
        d0, d1, R, BT = to_mp(c["d0"]), to_mp(c["d1"]), to_mp(c["R"]), to_mp(c["BT"])
        r0, rd1, rBT = num_rank(d0), num_rank(d1), num_rank(BT)
        block = mp.zeros(d1.rows + R.rows, d1.cols + BT.cols)
        block[:d1.rows, :d1.cols] = d1; block[d1.rows:, :d1.cols] = R; block[d1.rows:, d1.cols:] = BT
        r1 = num_rank(block) - rd1 - rBT; a0 = n - r0; a1 = ng * n - rd1 - r0; t0 = n - rBT
        return dict(a0=a0, a1=a1, t0=t0, r1=r1, n=a1 - r1)
    A = side(rep); B = side(CI.dual(K, rep))
    return dict(I=A["n"] - B["n"], E=A, Edual=B)


# ------------------------------------------------------------------------------------------- controls (before the seal)
def controls(path):
    out = {}
    print("C0  the banked identity of main's instrument (m010's witness, I = +1):", flush=True)
    out["C0 m010 banked identity"] = bool(CI.control_m010())
    for state in ("-LLRR", "+LLRR"):
        S = load(path, state); rec = {}
        # holonomy: every relator is a scalar matrix in PGL; the cusp words commute up to a scalar
        D = {}
        for g in S["gens"]: D[g] = S["hol"][g]; D[g.upper()] = CI.kmat_inv(K, S["hol"][g])
        def scalar(M): return K.is_zero(M[0][1]) and K.is_zero(M[1][0]) and K.is_zero(K.sub(M[0][0], M[1][1]))
        rec["relators scalar in PGL"] = all(scalar(CI.word_matrix(K, r, D)) for r in S["rels"])
        mu, lam = S["cusp"]; A, B = CI.word_matrix(K, mu, D), CI.word_matrix(K, lam, D)
        rec["cusp words commute"] = scalar(CI.kmat_mul(K, CI.kmat_mul(K, A, B), CI.kmat_inv(K, CI.kmat_mul(K, B, A))))
        # the four: a representation, preserving the form x1 x2 - x3^2 - x4^2, determinant one
        F = {g: four(S["hol"][g]) for g in S["gens"]}; FD = {}
        for g in S["gens"]: FD[g] = F[g]; FD[g.upper()] = CI.kmat_inv(K, F[g])
        Id4 = CI.kmat_eye(K, 4); h = K.const(Fr(1, 2))
        J = [[ZERO, h, ZERO, ZERO], [h, ZERO, ZERO, ZERO], [ZERO, ZERO, K.const(-1), ZERO], [ZERO, ZERO, ZERO, K.const(-1)]]
        rec["four: relators are the identity"] = all(is_zero_mat(CI.kmat_sub(K, CI.word_matrix(K, r, FD), Id4)) for r in S["rels"])
        rec["four: preserves the Lorentz form"] = all(is_zero_mat(CI.kmat_sub(K, CI.kmat_mul(K, CI.kmat_mul(K, CI.kmat_T(F[g]), J), F[g]), J)) for g in S["gens"])
        rec["four: entries real"] = all(x == conj(x) for g in S["gens"] for r in F[g] for x in r)
        rec["|det| of a, b, t"] = {g: [str(c) for c in abs_det(S["hol"][g])] for g in S["gens"]}
        # the sign characters are characters: every relator has even exponent sum in each generator mod 2
        rec["every sign character is a character"] = all(sum(1 for ch in r if ch.lower() == g) % 2 == 0 for r in S["rels"] for g in S["gens"])
        rec["members as given"] = S["members"]
        rec["members' values on the cusp words"] = [[math.prod(nu[ch.lower()] for ch in w) for w in S["cusp"]] for nu in S["members"]]
        out[state + " (" + S["name"] + ")"] = rec
        print(state, json.dumps(rec, indent=1), flush=True)
    # C1: the floating-point twin against the instrument on the banked m010 witness
    K3 = CI.NF([1, -1, 1]); M, gens, rels, mu, lam = CI.presentation("m010"); u = K3.alpha()
    A = [[K3.const(0), K3.const(1)], [K3.const(-1), K3.const(1)]]; B = [[K3.const(0), K3.pw(u, 2)], [u, K3.const(-2)]]
    chi = {"a": u, "b": K3.const(-1)}
    V = {g: [[K3.mul(chi[g], x) for x in row] for row in CI.sym_power(K3, {"a": A, "b": B}[g], 3)] for g in gens}
    nV, cV = CI.counts(K3, gens, rels, mu, lam, V, "m010 V", verbose=False); nD, cD = CI.counts(K3, gens, rels, mu, lam, CI.dual(K3, V), "m010 V*", verbose=False)
    w = mp.e ** (mp.j * mp.pi / 3)
    def cx3(a): return mp.mpf(a[0].numerator) / a[0].denominator + mp.mpf(a[1].numerator) / a[1].denominator * w
    def side3(rp):
        n = len(rp[gens[0]]); Id = CI.kmat_eye(K3, n); D = {}
        for g in gens: D[g] = rp[g]; D[g.upper()] = CI.kmat_inv(K3, rp[g])
        tm = lambda P: mp.matrix([[cx3(x) for x in r] for r in P])
        d0 = tm(CI.vstack(*[CI.kmat_sub(K3, D[g], Id) for g in gens]))
        d1 = tm(CI.vstack(*[CI.hstack(*[CI.fox(K3, r, D, gens)[1][g] for g in gens]) for r in rels]))
        fm, fl = CI.fox(K3, mu, D, gens)[1], CI.fox(K3, lam, D, gens)[1]
        R = tm(CI.vstack(CI.hstack(*[fm[g] for g in gens]), CI.hstack(*[fl[g] for g in gens])))
        BT = tm(CI.vstack(CI.kmat_sub(K3, CI.word_matrix(K3, mu, D), Id), CI.kmat_sub(K3, CI.word_matrix(K3, lam, D), Id)))
        r0, rd1, rBT = num_rank(d0), num_rank(d1), num_rank(BT)
        block = mp.zeros(d1.rows + R.rows, d1.cols + BT.cols)
        block[:d1.rows, :d1.cols] = d1; block[d1.rows:, :d1.cols] = R; block[d1.rows:, d1.cols:] = BT
        r1 = num_rank(block) - rd1 - rBT; a1 = len(gens) * n - rd1 - r0
        return a1 - r1, (n - r0, a1, n - rBT, r1)
    tV, tD = side3(V), side3(CI.dual(K3, V))
    out["C1 twin on m010"] = dict(instrument=dict(I=nV - nD, V=list(cV), Vdual=list(cD)), twin=dict(I=tV[0] - tD[0], V=list(tV[1]), Vdual=list(tD[1])),
                                  agree=(nV - nD == tV[0] - tD[0] == 1 and tuple(cV) == tuple(tV[1]) and tuple(cD) == tuple(tD[1])))
    print("C1", json.dumps(out["C1 twin on m010"]), flush=True)
    # C2: the two pieces of linear algebra written for this arc, on random matrices over K (seeded)
    import random; rnd = random.Random(1485)
    def rk(): return K.el([Fr(rnd.randint(-3, 3), rnd.randint(1, 3)) for _ in range(4)])
    A = [[rk() for _ in range(5)] for _ in range(5)]; B = [[rk() for _ in range(5)] for _ in range(5)]
    ext_ok = is_zero_mat(CI.kmat_sub(K, ext2(CI.kmat_mul(K, A, B)), CI.kmat_mul(K, ext2(A), ext2(B))))
    P = [[rk() for _ in range(7)] for _ in range(3)]; P.append([K.add(x, y) for x, y in zip(P[0], P[1])])   # rank 3, seven columns
    ns = k_nullspace(P)
    null_ok = (len(ns) == 7 - CI.kmat_rank(K, P) == 4) and all(is_zero_mat(CI.kmat_mul(K, P, [[x] for x in v])) for v in ns)
    out["C2 exterior square multiplicative; nullspace exact"] = bool(ext_ok and null_ok)
    print("C2", out["C2 exterior square multiplicative; nullspace exact"], flush=True)
    out["all controls pass"] = bool(out["C0 m010 banked identity"] and out["C1 twin on m010"]["agree"] and out["C2 exterior square multiplicative; nullspace exact"] and all(
        v for st in ("-LLRR (m135)", "+LLRR (m136)") for k, v in out[st].items() if isinstance(v, bool)))
    print("ALL CONTROLS PASS:", out["all controls pass"])
    return out


# ------------------------------------------------------------------------------------------- the cells
def census(path, state):
    S = load(path, state); rows = []
    for vals in itertools.product((1, -1), repeat=3):
        nu = dict(zip(S["gens"], vals)); V = frame(S, nu)
        r = reading(S, V, "V"); t = reading_numeric(S, V); interior, boundary = classes(S, V)
        rows.append(dict(nu=nu, member=(nu in S["members"]), cusp=[math.prod(nu[ch.lower()] for ch in w) for w in S["cusp"]],
                         V=r["E"], Vdual=r["Edual"], I_V=r["I"], identity_ok=r["ok"], twin_agrees=(t["E"] == r["E"] and t["Edual"] == r["Edual"]),
                         interior_classes=len(interior), boundary_classes=len(boundary)))
        print(json.dumps(rows[-1]), flush=True)
    return rows


def members(path, state):
    S = load(path, state); out = []
    for nu in S["members"]:
        V = frame(S, nu); interior, boundary = classes(S, V); rec = dict(nu=nu, interior=len(interior), boundary=len(boundary), readings=[])
        def read(z, label):
            W = extension(S, V, z); L2 = {g: ext2(W[g]) for g in S["gens"]}
            a, b = reading(S, W, "W1"), reading(S, L2, "L2W1"); ta, tb = reading_numeric(S, W), reading_numeric(S, L2)
            r = dict(cls=label, I_W1=a["I"], I_L2W1=b["I"], identities_ok=(a["ok"] and b["ok"]),
                     twin=dict(I_W1=ta["I"], I_L2W1=tb["I"]), twin_agrees=(ta["E"] == a["E"] and ta["Edual"] == a["Edual"] and tb["E"] == b["E"] and tb["Edual"] == b["Edual"]),
                     W1=a["E"], W1dual=a["Edual"], L2=b["E"], L2dual=b["Edual"])
            rec["readings"].append(r); print(json.dumps(dict(nu=nu, **r)), flush=True)
        def comb(pairs):
            v = None
            for c, z in pairs:
                w = [K.mul(K.const(c), x) for x in z]; v = w if v is None else [K.add(p, q) for p, q in zip(v, w)]
            return v
        for i, z in enumerate(interior): read(z, f"interior {i}")
        for i, z in enumerate(boundary):
            read(z, f"boundary-type {i}")
            for j, zi in enumerate(interior):
                read(comb([(1, z), (1, zi)]), f"boundary-type {i} + interior {j}"); read(comb([(1, z), (Fr(-3, 7), zi)]), f"boundary-type {i} - 3/7 interior {j}")
        # the split module, for reference
        Wsplit = extension(S, V, [ZERO] * (4 * len(S["gens"]))); rs = reading(S, Wsplit, "V+1"); rl = reading(S, {g: ext2(Wsplit[g]) for g in S["gens"]}, "L2(V+1)")
        rec["split"] = dict(I=rs["I"], I_L2=rl["I"]); out.append(rec)
    return out


if __name__ == "__main__":
    path = HERE / "members_for_main.json"
    cmd = sys.argv[1] if len(sys.argv) > 1 else "controls"
    if cmd == "controls": json.dump(controls(path), open(HERE / "controls.json", "w"), indent=1)
    elif cmd == "census": json.dump(census(path, sys.argv[2]), open(HERE / f"census_{CI and load(path, sys.argv[2])['name']}.json", "w"), indent=1)
    elif cmd == "members": json.dump(members(path, sys.argv[2]), open(HERE / f"members_{load(path, sys.argv[2])['name']}.json", "w"), indent=1)
