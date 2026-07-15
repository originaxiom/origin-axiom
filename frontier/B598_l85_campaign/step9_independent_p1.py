"""B598 step 9 — THE INDEPENDENT P1 PIPELINE (failure-enforcing).

A clean-room reproduction of the corrected P1 invariant table by a second
pipeline sharing NO code and NO imported values with the l51/P1 stack:

  * the 27 is built fresh from the E6 Cartan matrix (Bourbaki numbering):
    minuscule weight BFS from omega_1, Frenkel-Kac cocycle signs
    (B(i,j) = C_ij for i<j, B(i,i) = 1), e_i = f_i^T;
  * its own Q(sqrt-3) arithmetic, rref, nullspace (written here);
  * the principal sl2 from r = C^{-1}(2,...,2); A = exp(e), B = exp(omega f);
  * the adjoint 78 from bracket BFS (36 positive root vectors, transposes,
    6 Cartan), the six ad-blocks from the height grading;
  * Fox calculus on the presentation <a,b | abABaBAbaB> per block;
  * the certified longitude lambda = 'abABaaBAbA'.

GATES (all exact; exit nonzero on failure):
  G-A  27 weights; Chevalley gates [e_i,f_j] = delta_ij h_i;
  G-B  principal gates [e,f] = h, [h,e] = 2e; e nilpotent;
  G-C  the relator maps to the exact identity (fresh model = geometric);
  G-D  adjoint dim 78; exponents {1,4,5,7,8,11}; block dims 3..23;
  G-E  per block: dim H1(pi_K; V_m) = 1; the meridian-fixed line is 1-dim;
       the invariant form is Schur-unique; the gauge gate holds;
  G-F  THE TARGET: I_lambda/I_mu = -2*sqrt(-3) at ALL six blocks
       (the banked universal ratio, reproduced independently).

Run: OA_SLOW=1 python3 step9_independent_p1.py   (~1-3 h)
"""
import sys
from fractions import Fraction as Fr

# ---------------------------------------------------------------- Q(sqrt-3)
class Q3:
    __slots__ = ('a', 'b')

    def __init__(self, a=0, b=0):
        self.a = Fr(a)
        self.b = Fr(b)

    def __add__(s, o):
        return Q3(s.a + o.a, s.b + o.b)

    def __sub__(s, o):
        return Q3(s.a - o.a, s.b - o.b)

    def __mul__(s, o):
        return Q3(s.a * o.a - 3 * s.b * o.b, s.a * o.b + s.b * o.a)

    def __neg__(s):
        return Q3(-s.a, -s.b)

    def inv(s):
        n = s.a * s.a + 3 * s.b * s.b
        return Q3(s.a / n, -s.b / n)

    def is_zero(s):
        return s.a == 0 and s.b == 0

    def __eq__(s, o):
        return s.a == o.a and s.b == o.b

    def __repr__(s):
        return f"({s.a}{'+' if s.b >= 0 else ''}{s.b}w)"


Z = Q3(0)
ONE = Q3(1)
ZETA6 = Q3(Fr(1, 2), Fr(1, 2))           # (1 + sqrt(-3))/2 = e^{i pi/3}
ZETA6B = Q3(Fr(1, 2), Fr(-1, 2))         # the conjugate branch
W3 = Q3(0, 1)                            # sqrt(-3)


def zmat(n, m=None):
    m = n if m is None else m
    return [[Z for _ in range(m)] for _ in range(n)]


def eye(n):
    M = zmat(n)
    for i in range(n):
        M[i][i] = ONE
    return M


def mul(X, Y):
    n, p, m = len(X), len(Y), len(Y[0])
    R = zmat(n, m)
    for i in range(n):
        Xi = X[i]
        for k in range(p):
            x = Xi[k]
            if x.is_zero():
                continue
            Yk = Y[k]
            Ri = R[i]
            for j in range(m):
                if not Yk[j].is_zero():
                    Ri[j] = Ri[j] + x * Yk[j]
    return R


def add(X, Y):
    return [[a + b for a, b in zip(r1, r2)] for r1, r2 in zip(X, Y)]


def sub(X, Y):
    return [[a - b for a, b in zip(r1, r2)] for r1, r2 in zip(X, Y)]


def scale(c, X):
    return [[c * x for x in r] for r in X]


def is_zero_mat(X):
    return all(all(x.is_zero() for x in r) for r in X)


def bracket(X, Y):
    return sub(mul(X, Y), mul(Y, X))


def rref_rows(rows):
    """Reduce a list of row vectors; return (reduced_rows, pivots)."""
    red = []
    for r in rows:
        row = list(r)
        for pc, pr in red:
            if not row[pc].is_zero():
                f = row[pc]
                row = [x - f * y for x, y in zip(row, pr)]
        piv = next((k for k, x in enumerate(row) if not x.is_zero()), None)
        if piv is None:
            continue
        inv = row[piv].inv()
        row = [x * inv for x in row]
        red.append((piv, row))
    red.sort()
    return red


def reduce_against(red, vec):
    row = list(vec)
    for pc, pr in red:
        if not row[pc].is_zero():
            f = row[pc]
            row = [x - f * y for x, y in zip(row, pr)]
    return row


def nullspace(rows, ncols):
    red = rref_rows(rows)
    pivs = [pc for pc, _ in red]
    free = [j for j in range(ncols) if j not in pivs]
    out = []
    for fj in free:
        v = [Z] * ncols
        v[fj] = ONE
        for pc, pr in reversed(red):
            v[pc] = -sum((pr[k] * v[k] for k in range(ncols)
                          if k != pc and not v[k].is_zero()), Z)
        out.append(v)
    return out


def rank_rows(rows):
    return len(rref_rows(rows))


# ---------------------------------------------------------------- the 27
N = 6
edges = [(1, 3), (3, 4), (4, 5), (5, 6), (2, 4)]
C = [[2 if i == j else 0 for j in range(N)] for i in range(N)]
for (i, j) in edges:
    C[i - 1][j - 1] = C[j - 1][i - 1] = -1

hw = (1, 0, 0, 0, 0, 0)
weights = {hw: (0,) * N}
front = [hw]
while front:
    nf = []
    for mu in front:
        n = weights[mu]
        for i in range(N):
            if mu[i] > 0:
                child = tuple(mu[j] - C[i][j] for j in range(N))
                cn = tuple(n[j] + (1 if j == i else 0) for j in range(N))
                if child not in weights:
                    weights[child] = cn
                    nf.append(child)
    front = nf
WTS = sorted(weights, key=lambda m: (sum(weights[m]), m))
assert len(WTS) == 27, f"G-A FAIL: {len(WTS)} weights"
pos = {m: k for k, m in enumerate(WTS)}

Bfk = lambda i, n: sum(C[i][j] * n[j] for j in range(N) if j > i) + n[i]
fs = []
for i in range(N):
    F = zmat(27)
    for mu in WTS:
        if mu[i] > 0:
            child = tuple(mu[j] - C[i][j] for j in range(N))
            sgn = 1 if Bfk(i, weights[mu]) % 2 == 0 else -1
            F[pos[child]][pos[mu]] = Q3(sgn)
    fs.append(F)
es = [[[fs[i][jj][ii] for jj in range(27)] for ii in range(27)]
      for i in range(N)]
# G-A Chevalley gates
for i in range(N):
    for j in range(N):
        comm = bracket(es[i], fs[j])
        if i == j:
            ok = all(comm[pos[mu]][pos[mu]] == Q3(mu[i]) for mu in WTS) and \
                 all(comm[k][l].is_zero() for k in range(27)
                     for l in range(27) if k != l)
        else:
            ok = is_zero_mat(comm)
        assert ok, f"G-A FAIL at ({i},{j})"
print("G-A PASS: 27 weights; Chevalley gates exact", flush=True)

# ---------------------------------------------------------------- principal
# r = C^{-1} (2,...,2): solve C r = 2*ones over Fractions
rows_c = [[Fr(C[i][j]) for j in range(N)] + [Fr(2)] for i in range(N)]
for c in range(N):
    piv = next(r for r in range(c, N) if rows_c[r][c] != 0)
    rows_c[c], rows_c[piv] = rows_c[piv], rows_c[c]
    pv = rows_c[c][c]
    rows_c[c] = [x / pv for x in rows_c[c]]
    for r in range(N):
        if r != c and rows_c[r][c] != 0:
            f = rows_c[r][c]
            rows_c[r] = [x - f * y for x, y in zip(rows_c[r], rows_c[c])]
rvec = [rows_c[i][N] for i in range(N)]
e_pr = zmat(27)
f_pr = zmat(27)
for i in range(N):
    e_pr = add(e_pr, es[i])
    f_pr = add(f_pr, scale(Q3(rvec[i]), fs[i]))
h_pr = bracket(e_pr, f_pr)
gB = is_zero_mat(sub(bracket(h_pr, e_pr), scale(Q3(2), e_pr)))
assert gB, "G-B FAIL: [h,e] != 2e"
hd = all(h_pr[i][j].is_zero() for i in range(27) for j in range(27) if i != j)
assert hd, "G-B FAIL: h not diagonal"
P = e_pr
k = 1
while not is_zero_mat(P):
    P = mul(P, e_pr)
    k += 1
print(f"G-B PASS: principal sl2 exact; r = {rvec}; e nilpotent order {k}",
      flush=True)


def exp_nil(X):
    R = eye(27)
    P = eye(27)
    fact = 1
    kk = 1
    while True:
        P = mul(P, X)
        if is_zero_mat(P):
            break
        fact *= kk
        R = add(R, scale(Q3(Fr(1, fact)), P))
        kk += 1
    return R


A = exp_nil(e_pr)
Ai = exp_nil(scale(Q3(-1), e_pr))
REL = "abABaBAbaB"
Bm = Bmi = None
branch = None
for name, z in (("zeta6", ZETA6), ("zeta6bar", ZETA6B)):
    Bt = exp_nil(scale(z, f_pr))
    Bti = exp_nil(scale(-z, f_pr))
    LET = {'a': A, 'b': Bt, 'A': Ai, 'B': Bti}
    Rm = eye(27)
    for ch in REL:
        Rm = mul(Rm, LET[ch])
    if is_zero_mat(sub(Rm, eye(27))):
        Bm, Bmi, branch = Bt, Bti, name
        break
assert branch is not None, "G-C FAIL: relator != 1 on both zeta6 branches"
print(f"G-C PASS: the relator is the exact identity (fresh model, "
      f"branch {branch})", flush=True)

# ---------------------------------------------------------------- adjoint 78
rootvecs = {}                              # tuple(root in simple coords) -> mat
heights = {}
for i in range(N):
    al = tuple(1 if j == i else 0 for j in range(N))
    rootvecs[al] = es[i]
    heights[al] = 1
front = list(rootvecs)
while front:
    nf = []
    for al in front:
        for i in range(N):
            nal = tuple(al[j] + (1 if j == i else 0) for j in range(N))
            if nal in rootvecs:
                continue
            X = bracket(es[i], rootvecs[al])
            if not is_zero_mat(X):
                rootvecs[nal] = X
                heights[nal] = heights[al] + 1
                nf.append(nal)
    front = nf
assert len(rootvecs) == 36, f"G-D FAIL: {len(rootvecs)} positive roots"
basis = []                                 # (matrix, ad-h eigenvalue 2*height)
for al, X in rootvecs.items():
    basis.append((X, 2 * heights[al]))
    Xt = [[X[j][i] for j in range(27)] for i in range(27)]
    basis.append((Xt, -2 * heights[al]))
his = [bracket(es[i], fs[i]) for i in range(N)]
for H in his:
    basis.append((H, 0))
assert len(basis) == 78
flatrows = [[M[i][j] for i in range(27) for j in range(27)]
            for M, _ in basis]
assert rank_rows(flatrows) == 78, "G-D FAIL: adjoint basis degenerate"
# grading gate: [h_pr, x] = lam x for each basis element
for M, lam in basis:
    assert is_zero_mat(sub(bracket(h_pr, M), scale(Q3(lam), M))), \
        "G-D FAIL: grading"
EXPECTED_EXP = [1, 4, 5, 7, 8, 11]
tops = {}
for m in EXPECTED_EXP:
    cand = [M for M, lam in basis if lam == 2 * m]
    rws = []
    for M in cand:
        X = bracket(e_pr, M)
        rws.append([X[i][j] for i in range(27) for j in range(27)])
    ker = nullspace([[rws[r][c] for r in range(len(cand))]
                     for c in range(729)], len(cand))
    assert len(ker) == 1, f"G-D FAIL: top multiplicity {len(ker)} at m={m}"
    T = zmat(27)
    for cf, M in zip(ker[0], cand):
        if not cf.is_zero():
            T = add(T, scale(cf, M))
    tops[m] = T
blocks = {}
for m in EXPECTED_EXP:
    vecs = [tops[m]]
    cur = tops[m]
    for _ in range(2 * m):
        cur = bracket(f_pr, cur)
        vecs.append(cur)
    assert not is_zero_mat(vecs[-1]), f"G-D FAIL: short string at m={m}"
    assert is_zero_mat(bracket(f_pr, vecs[-1])), f"G-D FAIL: long string m={m}"
    blocks[m] = vecs
assert sum(len(v) for v in blocks.values()) == 78
print(f"G-D PASS: adjoint 78; exponents {EXPECTED_EXP}; "
      f"block dims {[len(blocks[m]) for m in EXPECTED_EXP]}", flush=True)

# ------------------------------------------------- block coordinate actions
LONGITUDE = "abABaaBAbA"


def block_setup(m):
    vecs = blocks[m]
    d = len(vecs)
    rows_ = [[M[i][j] for i in range(27) for j in range(27)] for M in vecs]
    red = rref_rows(rows_)
    pivcols = [pc for pc, _ in red]
    # coords via the pivot-column subsystem: S coords = v[pivcols]
    S = [[rows_[k][pc] for k in range(d)] for pc in pivcols]

    def solve_coords(vflat):
        aug = [list(S[i]) + [vflat[pivcols[i]]] for i in range(d)]
        for c in range(d):
            piv = next(r for r in range(c, d) if not aug[r][c].is_zero())
            aug[c], aug[piv] = aug[piv], aug[c]
            inv = aug[c][c].inv()
            aug[c] = [x * inv for x in aug[c]]
            for r in range(d):
                if r != c and not aug[r][c].is_zero():
                    f = aug[r][c]
                    aug[r] = [x - f * y for x, y in zip(aug[r], aug[c])]
        coords = [aug[i][d] for i in range(d)]
        # membership gate: reconstruct exactly
        rec = [Z] * 729
        for cf, rw in zip(coords, rows_):
            if not cf.is_zero():
                rec = [x + cf * y for x, y in zip(rec, rw)]
        assert all((x - y).is_zero() for x, y in zip(rec, vflat)), \
            f"membership FAIL at block m={m}"
        return coords

    acts = {}
    for ch, (P, Pi) in {'a': (A, Ai), 'b': (Bm, Bmi),
                        'A': (Ai, A), 'B': (Bmi, Bm)}.items():
        cols = []
        for Mv in vecs:
            X = mul(P, mul(Mv, Pi))
            cols.append(solve_coords([X[i][j] for i in range(27)
                                      for j in range(27)]))
        acts[ch] = [[cols[j][i] for j in range(d)] for i in range(d)]
    return d, acts


def word_act(acts, word, d):
    Wm = eye(d)[:]
    Wm = [row[:] for row in eye(d)]
    for ch in word:
        Wm = mul(Wm, acts[ch])
    return Wm


def matvecd(M, v):
    d = len(v)
    return [sum((M[i][j] * v[j] for j in range(d) if not v[j].is_zero()), Z)
            for i in range(d)]


def fox_pair(acts, d):
    Da = zmat(d)
    Db = zmat(d)
    P = eye(d)
    for ch in REL:
        if ch == 'a':
            Da = add(Da, P)
        elif ch == 'A':
            Da = sub(Da, mul(P, acts['A']))
        elif ch == 'b':
            Db = add(Db, P)
        else:
            Db = sub(Db, mul(P, acts['B']))
        P = mul(P, acts[ch])
    return Da, Db


def cocycle_eval(acts, xa, xb, word, d):
    val = [Z] * d
    P = eye(d)
    for ch in word:
        if ch == 'a':
            inc = xa
        elif ch == 'b':
            inc = xb
        elif ch == 'A':
            inc = [-x for x in matvecd(acts['A'], xa)]
        else:
            inc = [-x for x in matvecd(acts['B'], xb)]
        val = [v + x for v, x in zip(val, matvecd(P, inc))]
        P = mul(P, acts[ch])
    return val


allok = True
print("THE INDEPENDENT TABLE:", flush=True)
for m in EXPECTED_EXP:
    d, acts = block_setup(m)
    Da, Db = fox_pair(acts, d)
    big = [[Da[i][j] for j in range(d)] + [Db[i][j] for j in range(d)]
           for i in range(d)]
    sols = nullspace(big, 2 * d)
    cobs = []
    for j in range(d):
        ev = [ONE if i == j else Z for i in range(d)]
        ca = [ev[i] - x for i, x in enumerate(matvecd(acts['a'], ev))]
        cb = [ev[i] - x for i, x in enumerate(matvecd(acts['b'], ev))]
        cobs.append(ca + cb)
    rc = rank_rows(cobs)
    dimH1 = len(sols) - rc
    gH1 = dimH1 == 1
    rep = next(s for s in sols if rank_rows(cobs + [list(s)]) > rc)
    xa, xb = list(rep[:d]), list(rep[d:])
    # the invariant form G (Schur gate)
    grows = []
    for g in ('a', 'b'):
        Ag = acts[g]
        for i in range(d):
            for j in range(d):
                row = [Z] * (d * d)
                for kk in range(d):
                    if Ag[kk][i].is_zero():
                        continue
                    for l in range(d):
                        if not Ag[l][j].is_zero():
                            row[kk * d + l] = row[kk * d + l] + Ag[kk][i] * Ag[l][j]
                row[i * d + j] = row[i * d + j] - ONE
                grows.append(row)
    Gs = nullspace(grows, d * d)
    gG = len(Gs) == 1
    G = [[Gs[0][i * d + j] for j in range(d)] for i in range(d)]
    # the meridian-fixed line
    Am1 = sub(acts['a'], eye(d))
    ws = nullspace(Am1, d)
    gw = len(ws) == 1
    wv = ws[0]
    pairf = lambda u, v: sum((u[i] * sum((G[i][j] * v[j] for j in range(d)
                             if not v[j].is_zero()), Z) for i in range(d)), Z)
    e0 = [ONE if i == 0 else Z for i in range(d)]
    cob_mu = [e0[i] - x for i, x in enumerate(matvecd(acts['a'], e0))]
    ggauge = pairf(cob_mu, wv).is_zero()
    xl = cocycle_eval(acts, xa, xb, LONGITUDE, d)
    I_mu = pairf(xa, wv)
    I_lam = pairf(xl, wv)
    gnv = not I_mu.is_zero()
    ratio = I_lam * I_mu.inv() if gnv else None
    gratio = gnv and ratio == Q3(0, -2)
    print(f"  m={m:2d} (dim {d:2d}): dimH1=1[{gH1}] G-unique[{gG}] "
          f"w-line[{gw}] gauge[{ggauge}] ratio I_lam/I_mu = {ratio} "
          f"[-2w: {gratio}]", flush=True)
    allok &= gH1 and gG and gw and ggauge and gratio

assert allok, "STEP 9 FAILED"
print("STEP 9 DONE: the invariant table reproduced by the clean-room "
      "pipeline — dim H1 = 1 and I_lam/I_mu = -2*sqrt(-3) at all six blocks.",
      flush=True)
