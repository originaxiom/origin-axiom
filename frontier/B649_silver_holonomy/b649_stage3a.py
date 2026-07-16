"""B649 stage 3a — the silver double's dimensions (prereg 9db17956)."""
import json
import os
import time
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
MOD = [Fr(16), Fr(0), Fr(8), Fr(0)]


def pmulred(p, q):
    out = [Fr(0)] * 7
    for i, a in enumerate(p):
        if a == 0:
            continue
        for j, b in enumerate(q):
            out[i + j] += a * b
    for k in range(6, 3, -1):
        c = out[k]
        if c != 0:
            out[k] = Fr(0)
            for t, m in enumerate(MOD):
                out[k - 4 + t] += c * m
    return out[:4]


class L:
    __slots__ = ("re", "im")

    def __init__(self, re=None, im=None):
        self.re = re if re is not None else [Fr(0)] * 4
        self.im = im if im is not None else [Fr(0)] * 4

    def __add__(self, o):
        return L([a + b for a, b in zip(self.re, o.re)],
                 [a + b for a, b in zip(self.im, o.im)])

    def __sub__(self, o):
        return L([a - b for a, b in zip(self.re, o.re)],
                 [a - b for a, b in zip(self.im, o.im)])

    def __mul__(self, o):
        rr, ii = pmulred(self.re, o.re), pmulred(self.im, o.im)
        ri, ir = pmulred(self.re, o.im), pmulred(self.im, o.re)
        return L([a - b for a, b in zip(rr, ii)],
                 [a + b for a, b in zip(ri, ir)])

    def conj(self):
        return L(self.re[:], [-x for x in self.im])

    def is_zero(self):
        return all(c == 0 for c in self.re) and all(c == 0 for c in self.im)

    def vec8(self):
        return self.re + self.im

    def inv(self):
        cols = []
        for k in range(8):
            b = L([Fr(1) if t == k else Fr(0) for t in range(4)], None) \
                if k < 4 else \
                L(None, [Fr(1) if t == k - 4 else Fr(0) for t in range(4)])
            cols.append((self * b).vec8())
        n = 8
        A = [[cols[j][i] for j in range(n)] + [Fr(1) if i == 0 else Fr(0)]
             for i in range(n)]
        for c in range(n):
            piv = next(r for r in range(c, n) if A[r][c] != 0)
            A[c], A[piv] = A[piv], A[c]
            pv = A[c][c]
            A[c] = [x / pv for x in A[c]]
            for r in range(n):
                if r != c and A[r][c] != 0:
                    f = A[r][c]
                    A[r] = [x - f * y for x, y in zip(A[r], A[c])]
        x = [A[r][n] for r in range(n)]
        return L(x[:4], x[4:])


def Lc(q):
    return L([Fr(q), Fr(0), Fr(0), Fr(0)], None)


L0, L1 = Lc(0), Lc(1)

pr = json.load(open(os.path.join(HERE, "e6_principal_rational.json")))
E_PR = [[Lc(Fr(x)) for x in row] for row in pr["e_pr"]]
F_PR = [[Lc(Fr(x)) for x in row] for row in pr["f_pr"]]
H_PR = [[Lc(Fr(x)) for x in row] for row in pr["h_pr"]]


def meye(n):
    return [[L1 if i == j else L0 for j in range(n)] for i in range(n)]


def mmul(A, B):
    n = len(A)
    Bt = list(zip(*B))
    out = [[L0] * n for _ in range(n)]
    for i in range(n):
        Ai = A[i]
        nz = [(k, Ai[k]) for k in range(n) if not Ai[k].is_zero()]
        for j in range(n):
            acc = L0
            col = Bt[j]
            for k, a in nz:
                b = col[k]
                if not b.is_zero():
                    acc = acc + a * b
            out[i][j] = acc
    return out


def mscale(c, M):
    return [[c * x for x in row] for row in M]


def madd(A, B):
    return [[a + b for a, b in zip(ra, rb)] for ra, rb in zip(A, B)]


def mconj27(M):
    return [[x.conj() for x in row] for row in M]


def mexp_nil(N):
    out = meye(27)
    term = meye(27)
    k = 1
    while True:
        term = mmul(term, N)
        term = mscale(Lc(Fr(1, k)), term)
        if all(x.is_zero() for row in term for x in row):
            break
        out = madd(out, term)
        k += 1
        if k > 40:
            raise RuntimeError("not nilpotent?")
    return out


def lift_sl2(g):
    p, q, r_, s = g[0][0], g[0][1], g[1][0], g[1][1]
    det = p * s - q * r_
    if p.is_zero():
        w27 = mmul(mmul(mexp_nil(E_PR),
                        mexp_nil(mscale(Lc(-1), F_PR))), mexp_nil(E_PR))
        return mmul(w27, lift_sl2([[L0 - r_, L0 - s], [p, q]]))
    lower = mexp_nil(mscale(r_ * p.inv(), F_PR))
    upper = mexp_nil(mscale(q * p.inv(), E_PR))
    t2 = (p * p) * det.inv()
    D = meye(27)
    t2i = t2.inv()
    for i in range(27):
        wgt = int(H_PR[i][i].re[0])
        e = wgt // 2
        val = L1
        base = t2 if e >= 0 else t2i
        for _ in range(abs(e)):
            val = val * base
        D[i][i] = val
    return mmul(mmul(lower, D), upper)


# ---- the exact letters ---------------------------------------------------------
d27 = json.load(open(os.path.join(HERE, "letters27_L.json")))


def mat27(nm):
    return [[L([Fr(x) for x in d27[nm][i][j][:4]],
               [Fr(x) for x in d27[nm][i][j][4:]])
             for j in range(27)] for i in range(27)]


S1 = {nm: mat27(nm) for nm in "abcABC"}

dent = json.load(open(os.path.join(HERE, "entries_L.json")))


def gen2(nm):
    return [[L([Fr(x) for x in dent[f"{nm}{i}{j}"][0]],
               [Fr(x) for x in dent[f"{nm}{i}{j}"][1]])
             for j in range(2)] for i in range(2)]


def mm2(A, B):
    return [[A[i][0] * B[0][j] + A[i][1] * B[1][j] for j in range(2)]
            for i in range(2)]


def adj2(M):
    return [[M[1][1], L0 - M[0][1]], [L0 - M[1][0], M[0][0]]]


G2 = {nm: gen2(nm) for nm in "abc"}
for nm in "abc":
    G2[nm.upper()] = adj2(G2[nm])   # det = 1 exactly (stage 2a)


def word2(w):
    m = None
    for ch in w:
        m = G2[ch] if m is None else mm2(m, G2[ch])
    return m


MU2 = word2("CCB")
LAM2 = word2("caCA")
LAM2i = adj2(LAM2)

print("== S3a-G1: the weld solve at SL2(L) ==", flush=True)
# unknown u: 4 L-entries = 32 rational unknowns (re4+im4 each).
# equations: u*conj(M) - T*u = 0 for (M,T) in ((MU2,MU2),(LAM2,LAM2i)).
# Assemble as a rational 64x32 system: each L-equation gives 8 rational rows.
def lin_u(Mc, T):
    """rows for u*Mc - T*u = 0; u indexed (i,j) -> unknown 4*(2i+j)+..8 basis."""
    rows = []
    # (u*Mc)[i][j] = sum_k u[i][k]*Mc[k][j]; (T*u)[i][j] = sum_k T[i][k]*u[k][j]
    BAS = []
    for t in range(8):
        BAS.append(L([Fr(1) if q == t else Fr(0) for q in range(4)], None)
                   if t < 4 else
                   L(None, [Fr(1) if q == t - 4 else Fr(0) for q in range(4)]))
    for i in range(2):
        for j in range(2):
            # coefficient of unknown u[p][q]-basis-t in this L-equation
            cols = {}
            for p in range(2):
                for q in range(2):
                    for t in range(8):
                        coef = L0
                        if p == i:
                            coef = coef + BAS[t] * Mc[q][j]
                        if q == j:
                            coef = coef - T[i][p] * BAS[t]
                        if not coef.is_zero():
                            cols[(p, q, t)] = coef
            # this L-valued linear form = 0 -> 8 rational equations
            for comp in range(8):
                row = [Fr(0)] * 32
                for (p, q, t), coef in cols.items():
                    row[8 * (2 * p + q) + t] = coef.vec8()[comp]
                rows.append(row)
    return rows


rows = lin_u(mconj2(MU2) if False else [[x.conj() for x in r] for r in MU2],
             MU2)
rows += lin_u([[x.conj() for x in r] for r in LAM2], LAM2i)

# rational nullspace of rows (64ish x 32)
def rat_nullspace(rows, ncols):
    A = [r[:] for r in rows]
    m = len(A)
    piv_cols = []
    r = 0
    for c in range(ncols):
        piv = next((k for k in range(r, m) if A[k][c] != 0), None)
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        pv = A[r][c]
        A[r] = [x / pv for x in A[r]]
        for k in range(m):
            if k != r and A[k][c] != 0:
                f = A[k][c]
                A[k] = [x - f * y for x, y in zip(A[k], A[r])]
        piv_cols.append(c)
        r += 1
        if r == m:
            break
    free = [c for c in range(ncols) if c not in piv_cols]
    basis = []
    for fc in free:
        v = [Fr(0)] * ncols
        v[fc] = Fr(1)
        for rr, pc in enumerate(piv_cols):
            v[pc] = -A[rr][fc]
        basis.append(v)
    return basis


null = rat_nullspace(rows, 32)
print(f"  weld solution space dim (rational) = {len(null)}", flush=True)
u = None
for v in null:
    cand = [[L(list(map(Fr, v[8 * (2 * i + j): 8 * (2 * i + j) + 4])),
               list(map(Fr, v[8 * (2 * i + j) + 4: 8 * (2 * i + j) + 8])))
             for j in range(2)] for i in range(2)]
    det = cand[0][0] * cand[1][1] - cand[0][1] * cand[1][0]
    if not det.is_zero():
        u = cand
        print(f"  invertible weld intertwiner FOUND (det != 0)", flush=True)
        break
if u is None and len(null) >= 2:
    v = [a + b for a, b in zip(null[0], null[1])]
    cand = [[L(list(map(Fr, v[8 * (2 * i + j): 8 * (2 * i + j) + 4])),
               list(map(Fr, v[8 * (2 * i + j) + 4: 8 * (2 * i + j) + 8])))
             for j in range(2)] for i in range(2)]
    det = cand[0][0] * cand[1][1] - cand[0][1] * cand[1][0]
    if not det.is_zero():
        u = cand
        print("  invertible weld intertwiner FOUND (combination)", flush=True)

if u is None:
    print("  S3a-G1 FAIL: no invertible intertwiner — OBSTRUCTION banked",
          flush=True)
else:
    t0 = time.time()
    U27 = lift_sl2(u)
    U27i = lift_sl2(adj2(u))
    print(f"  U27 lifted ({time.time()-t0:.1f}s)", flush=True)

    S2 = {}
    for nm in "abcABC":
        S2[nm] = mmul(mmul(U27, mconj27(S1[nm])), U27i)

    print("\n== S3a-G2: side-2 relators ==", flush=True)
    prim2 = {"d": "a", "e": "b", "f": "c", "D": "A", "E": "B", "F": "C"}

    def word27_side2(w):
        m = None
        for ch in w:
            g = S2[prim2[ch].lower() if ch.islower() else prim2[ch]]
            m = g if m is None else mmul(m, g)
        return m

    for rel in ("dEDeff", "ddFefE"):
        R = word27_side2(rel)
        ok = all((R[i][j] - (L1 if i == j else L0)).is_zero()
                 for i in range(27) for j in range(27))
        print(f"  {rel}: = I27 exactly: {ok}", flush=True)

    LETS = {"a": S1["a"], "b": S1["b"], "c": S1["c"],
            "A": S1["A"], "B": S1["B"], "C": S1["C"],
            "d": S2["a"], "e": S2["b"], "f": S2["c"],
            "D": S2["A"], "E": S2["B"], "F": S2["C"]}

    RELATORS = ["aBAbcc", "aaCbcB", "dEDeff", "ddFefE",
                "CCBeff", "caCAfdFD"]
    GENS = "abcdef"
    prim = {g: g for g in GENS}
    for g in GENS:
        prim[g.upper()] = g

    print("\n== S3a-G3: Fox rows and dimensions ==", flush=True)
    t0 = time.time()
    rows27 = []
    for w in RELATORS:
        Lb = {g: [[L0] * 27 for _ in range(27)] for g in GENS}
        P = meye(27)
        for ch in w:
            g = prim[ch]
            if ch.islower():
                term = P
            else:
                term = mscale(Lc(-1), mmul(P, LETS[ch]))
            Lb[g] = madd(Lb[g], term)
            P = mmul(P, LETS[ch])
        for i in range(27):
            rows27.append([Lb[g][i][j] for g in GENS for j in range(27)])
    print(f"  {len(rows27)} rows built ({time.time()-t0:.1f}s)", flush=True)

    # nullspace over L via Gaussian elimination
    def L_nullspace_dim(rows, ncols):
        A = [r[:] for r in rows]
        m = len(A)
        r = 0
        pivs = []
        for c in range(ncols):
            piv = next((k for k in range(r, m) if not A[k][c].is_zero()),
                       None)
            if piv is None:
                continue
            A[r], A[piv] = A[piv], A[r]
            pv_inv = A[r][c].inv()
            A[r] = [x * pv_inv for x in A[r]]
            for k in range(m):
                if k != r and not A[k][c].is_zero():
                    f = A[k][c]
                    A[k] = [x - f * y for x, y in zip(A[k], A[r])]
            pivs.append(c)
            r += 1
            if r == m:
                break
        return ncols - r

    t0 = time.time()
    z1 = L_nullspace_dim(rows27, 162)
    print(f"  dim Z1 = {z1}   ({time.time()-t0:.1f}s)", flush=True)

    cob = []
    for j in range(27):
        v = [L1 if t == j else L0 for t in range(27)]
        entry = []
        for g in GENS:
            gv = [sum((LETS[g][i][k] * v[k] for k in range(27)
                       if not v[k].is_zero()), L0) for i in range(27)]
            entry.extend([gv[i] - v[i] for i in range(27)])
        cob.append(entry)
    b1 = 27 - L_nullspace_dim(cob, 162) if False else None
    # rank of coboundary block = 27 - dim(common fixed vectors)
    # compute rank directly:
    def L_rank(rows, ncols):
        return ncols and (ncols - L_nullspace_dim(
            [list(x) for x in zip(*rows)], len(rows)))
    rk = 27 - L_nullspace_dim([list(x) for x in zip(*cob)], 27)
    h0 = 27 - rk
    h1 = z1 - rk
    print(f"  rank B1 = {rk}; h0(D) = {h0}; h1(D) = {h1}", flush=True)

    print("\n== solo dimensions (M_silver, 3 generators) ==", flush=True)
    rows_solo = []
    for w in ("aBAbcc", "aaCbcB"):
        Lb = {g: [[L0] * 27 for _ in range(27)] for g in "abc"}
        P = meye(27)
        for ch in w:
            g = ch.lower()
            if ch.islower():
                term = P
            else:
                term = mscale(Lc(-1), mmul(P, S1[ch]))
            Lb[g] = madd(Lb[g], term)
            P = mmul(P, S1[ch])
        for i in range(27):
            rows_solo.append([Lb[g][i][j] for g in "abc" for j in range(27)])
    z1s = L_nullspace_dim(rows_solo, 81)
    cob_s = []
    for j in range(27):
        v = [L1 if t == j else L0 for t in range(27)]
        entry = []
        for g in "abc":
            gv = [sum((S1[g][i][k] * v[k] for k in range(27)
                       if not v[k].is_zero()), L0) for i in range(27)]
            entry.extend([gv[i] - v[i] for i in range(27)])
        cob_s.append(entry)
    rks = 27 - L_nullspace_dim([list(x) for x in zip(*cob_s)], 27)
    print(f"  solo: dim Z1 = {z1s}; rank B1 = {rks}; "
          f"h0 = {27 - rks}; h1 = {z1s - rks}", flush=True)

print("\nB649 stage 3a DONE", flush=True)
