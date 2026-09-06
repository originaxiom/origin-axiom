"""R67 -- exact Chevalley e8 (Frenkel-Kac cocycle, B351's construction at rank 8) and the Tits lifts of L_g, w_A2, w_3.
Orders and Ad-eigenvalue multiplicities decide the E8 conjugacy classes without the order-3-lift assumption of R64 s.4."""
import sys, itertools, random, io, contextlib, time
from fractions import Fraction as Fr
t0 = time.time()
# ---------- E8 root system, Bourbaki: chain 1-3-4-5-6-7-8, node 2 on 4
A = [[2 if i == j else 0 for j in range(8)] for i in range(8)]
for (i, j) in [(1,3),(3,4),(4,5),(5,6),(6,7),(7,8),(2,4)]:
    A[i-1][j-1] = A[j-1][i-1] = -1
def pair(a, b): return sum(a[i]*A[i][j]*b[j] for i in range(8) for j in range(8))
simple = [tuple(int(i == j) for j in range(8)) for i in range(8)]
pos, fr = set(simple), list(simple)
while fr:
    beta = fr.pop()
    for i in range(8):
        p, b = 0, list(beta); b[i] -= 1
        while tuple(b) in pos: p += 1; b[i] -= 1
        if p - pair(beta, simple[i]) > 0:
            nb = list(beta); nb[i] += 1; nb = tuple(nb)
            if nb not in pos: pos.add(nb); fr.append(nb)
POS = sorted(pos, key=lambda r: (sum(r), r)); ROOTS = POS + [tuple(-x for x in r) for r in POS]
assert len(ROOTS) == 240
RIDX = {r: k for k, r in enumerate(ROOTS)}; DIM = 8 + 240
# ---------- Frenkel-Kac cocycle and brackets (B351's conventions)
Bup = [[1 if i == j else (A[i][j] % 2 if i < j else 0) for j in range(8)] for i in range(8)]
def eps(a, b): return -1 if sum(a[i]*Bup[i][j]*b[j] for i in range(8) for j in range(8)) % 2 else 1
def bracket(i, j):   # sparse {idx: int}
    out = {}
    if i < 8 and j < 8: return out
    if i < 8:
        b = ROOTS[j-8]; c = pair(simple[i], b)
        if c: out[j] = c
        return out
    if j < 8:
        for k, c in bracket(j, i).items(): out[k] = -c
        return out
    a, b = ROOTS[i-8], ROOTS[j-8]; s = tuple(x+y for x, y in zip(a, b))
    if all(x == 0 for x in s):
        for k in range(8):
            if a[k]: out[k] = -a[k]
        return out
    if s in RIDX: out[8 + RIDX[s]] = eps(a, b)
    return out
BR = {}
for i in range(DIM):
    for j in range(DIM):
        d = bracket(i, j)
        if d: BR[(i, j)] = d
def brk(x, y):
    out = {}
    for i, ci in x.items():
        for j, cj in y.items():
            for k, c in BR.get((i, j), {}).items():
                out[k] = out.get(k, 0) + ci*cj*c
                if out[k] == 0: del out[k]
    return out
# Jacobi on a random sample + all mixed triples (e_a, e_-a, e_b) (the B351 sign trap)
def jac(x, y, z):
    s = {}
    for term in (brk(x, brk(y, z)), brk(y, brk(z, x)), brk(z, brk(x, y))):
        for k, c in term.items():
            s[k] = s.get(k, 0) + c
    return all(v == 0 for v in s.values())
random.seed(1)
bad = 0; N = 30000
for _ in range(N):
    i, j, k = (random.randrange(DIM) for _ in range(3))
    if not jac({i: 1}, {j: 1}, {k: 1}): bad += 1
mixed_bad = 0
for a in POS[:40]:
    ia, ima = 8 + RIDX[a], 8 + RIDX[tuple(-x for x in a)]
    for b in ROOTS:
        if pair(a, b) == -1 and not jac({ia: 1}, {ima: 1}, {8 + RIDX[b]: 1}): mixed_bad += 1
print(f"[e8] 240 roots, dim {DIM}; Jacobi violations: random sample {bad}/{N}, mixed (e_a,e_-a,e_b) triples {mixed_bad}   ({time.time()-t0:.0f}s)")
assert bad == 0 and mixed_bad == 0
# ---------- lifts of simple reflections: n_i = exp(ad e_i) exp(ad e_-i) exp(ad e_i), sparse integer matrices (columns)
def ad_sparse(x):   # returns dict column j -> {row: coef}
    cols = {}
    for j in range(DIM):
        d = brk(x, {j: 1})
        if d: cols[j] = d
    return cols
def apply_cols(cols, v):   # cols: sparse matrix as dict of columns; v: sparse vector
    out = {}
    for j, cj in v.items():
        for k, c in cols.get(j, {}).items():
            out[k] = out.get(k, 0) + cj*c
            if out[k] == 0: del out[k]
    return out
def exp_ad_apply(x, v):   # exp(ad x) v = v + [x,v] + [x,[x,v]]/2  (ad x nilpotent of degree 3)
    a1 = brk(x, v); a2 = brk(x, a1); a3 = brk(x, a2)
    assert not a3, "ad x not nilpotent of degree 3"
    out = dict(v)
    for k, c in a1.items(): out[k] = out.get(k, 0) + c
    for k, c in a2.items():
        assert c % 2 == 0; out[k] = out.get(k, 0) + c // 2
    return {k: c for k, c in out.items() if c}
def evec(i, sign): return {8 + RIDX[tuple(sign*(1 if k == i else 0) for k in range(8))]: 1}
def n_apply(i, v): return exp_ad_apply(evec(i, 1), exp_ad_apply(evec(i, -1), exp_ad_apply(evec(i, 1), v)))
# check n_i acts on the Cartan as s_i
for i in range(8):
    for j in range(8):
        img = n_apply(i, {j: 1}); exp_ = {j: 1}
        exp_[i] = exp_.get(i, 0) - A[i][j]; exp_ = {k: c for k, c in exp_.items() if c}
        assert img == exp_, (i, j, img, exp_)
print("[lifts] n_i act on the Cartan as the simple reflections: OK")
# ---------- the three elements from R64 (icosian lattice), transported to Bourbaki coordinates
src = open('r64_founding_ratio_type.py').read().split("# ---- E8 conjugacy type")[0]
buf = io.StringIO()
with contextlib.redirect_stdout(buf): exec(src)
for seed in range(3, 200):
    random.seed(seed); f = [Fr(random.randint(-997, 997)) for _ in range(8)]
    if all(sum(a*b for a, b in zip(f, [Fr(c) for c in vec(r)])) != 0 for r in roots): break
fval = lambda q: sum(a*b for a, b in zip(f, [Fr(c) for c in vec(q)]))
pos8 = [r for r in roots if fval(r) > 0]; assert len(pos8) == 120
pset = set(pos8)
def qadd(p, q): return tuple(fadd(a, b) for a, b in zip(p, q))
simple8 = [r for r in pos8 if not any(qadd(s, t) == r for s in pos8 for t in pos8)]
assert len(simple8) == 8
cart = [[int(2*B(a, b)) for b in simple8] for a in simple8]
# match to Bourbaki A: build the permutation from the diagram (node degrees: 3 = node 4; its neighbours ...) by search over 8! with pruning via degree sequence
deg_target = [sum(1 for j in range(8) if A[i][j] == -1) for i in range(8)]
deg_have = [sum(1 for j in range(8) if cart[i][j] == -1) for i in range(8)]
perm = None
for p in itertools.permutations(range(8)):
    if any(deg_have[p[i]] != deg_target[i] for i in range(8)): continue
    if all(cart[p[i]][p[j]] == A[i][j] for i in range(8) for j in range(8)): perm = p; break
assert perm is not None
simpleB = [simple8[perm[i]] for i in range(8)]
import sympy as sp
G = sp.Matrix(8, 8, lambda i, j: sp.Rational(2*B(simpleB[i], simpleB[j])))
def coords8(r):
    c = G.solve(sp.Matrix([sp.Rational(2*B(r, s)) for s in simpleB])); assert all(x.is_integer for x in c); return tuple(int(x) for x in c)
rc = {r: coords8(r) for r in roots}; assert set(rc.values()) == set(ROOTS)
def weyl_matrix(Mlat):   # 8x8 on simple-root coordinates, columns = images of simple roots
    cols = []
    for s in simpleB:
        v = Mlat*coords(s); q = quat_from_vec(list(Bm.T*v)); cols.append(rc[q])
    return [[cols[j][i] for j in range(8)] for i in range(8)]
elements = {"L_g (founding ratio)": weyl_matrix(Lg), "w_A2 (family rotation)": weyl_matrix(wA2), "w_3 (E6 factor)": weyl_matrix(w3)}
# ---------- reduced word by descent: while w != 1: pick i with w(alpha_i) < 0, then w <- w s_i, word.append(i) (word read left-to-right = s_{i_k}...s_{i_1}? we record and rebuild carefully)
def mmul8(X, Y): return [[sum(X[i][k]*Y[k][j] for k in range(8)) for j in range(8)] for i in range(8)]
def smat(i):
    M = [[int(a == b) for b in range(8)] for a in range(8)]
    for j in range(8): M[i][j] -= A[i][j]
    return M
S8 = [smat(i) for i in range(8)]
I8 = [[int(a == b) for b in range(8)] for a in range(8)]
def reduced_word(W):
    W = [row[:] for row in W]; word = []
    while W != I8:
        i = next(i for i in range(8) if sum(W[k][i] for k in range(8)) < 0)   # w(alpha_i) negative <=> column i has negative height
        W = mmul8(W, S8[i]); word.append(i)          # w = w' s_i  =>  w' = w s_i
    return word[::-1]                                  # w = s_{word[0]} s_{word[1]} ... (leftmost first)
def lift_matrix(word):   # columns of the lift of s_{word[0]} ... s_{word[-1]}: apply rightmost first
    cols = []
    for j in range(DIM):
        v = {j: 1}
        for i in reversed(word): v = n_apply(i, v)
        cols.append(v)
    return cols
def compose(cols1, cols2):   # (cols1 . cols2) as columns: apply cols2 then cols1
    return [apply_cols_dict(cols1, c) for c in cols2]
def apply_cols_dict(cols, v):
    out = {}
    for j, cj in v.items():
        for k, c in cols[j].items():
            out[k] = out.get(k, 0) + cj*c
            if out[k] == 0: del out[k]
    return out
def rank_modp(cols, p):
    M = [[cols[j].get(i, 0) % p for j in range(DIM)] for i in range(DIM)]
    r = 0; rows = len(M)
    for c in range(DIM):
        piv = next((i for i in range(r, rows) if M[i][c]), None)
        if piv is None: continue
        M[r], M[piv] = M[piv], M[r]; inv = pow(M[r][c], p-2, p); M[r] = [v*inv % p for v in M[r]]
        for i in range(rows):
            if i != r and M[i][c]:
                fct = M[i][c]; M[i] = [(vi - fct*vr) % p for vi, vr in zip(M[i], M[r])]
        r += 1
    return r
ID = [{j: 1} for j in range(DIM)]
for name, W in elements.items():
    word = reduced_word(W)
    # verify the word reproduces W
    chk = I8
    for i in word: chk = mmul8(chk, S8[i])
    assert chk == W, name
    L = lift_matrix(word); L2 = compose(L, L); L3 = compose(L2, L)
    is_id3 = (L3 == ID)
    # multiplicities: fixed = DIM - rank(L - I); omega+omegabar = DIM - rank(L^2 + L + I)
    LmI = [dict(L[j]) for j in range(DIM)]
    for j in range(DIM): LmI[j][j] = LmI[j].get(j, 0) - 1
    Q = [dict(L2[j]) for j in range(DIM)]
    for j in range(DIM):
        for k, c in L[j].items(): Q[j][k] = Q[j].get(k, 0) + c
        Q[j][j] = Q[j].get(j, 0) + 1
    res = {}
    for p in (10007, 1000003):
        res[p] = (DIM - rank_modp(LmI, p), DIM - rank_modp(Q, p))
    print(f"[{name}] reduced word length {len(word)}; lift^3 == identity: {is_id3}; (fixed, omega+omegabar) mod 10007 / 1000003: {res[10007]} / {res[1000003]}   ({time.time()-t0:.0f}s)")
print("Kac classes: SU(9) (80, 84+84); E6xSU(3) (86, 81+81); E7xU(1) (134, 57+57).")

# ---------- order-3 lifts via a sign-character correction: find eta in Hom(Q, F2) with eta + eta.w + eta.w^2 = delta, delta from w-hat^3
def sign_char_of(cols):   # cols must be a torus element with +-1 on root vectors: return delta on simple roots (0/1 bits)
    bits = []
    for i in range(8):
        col = cols[8 + RIDX[simple[i]]]; assert list(col.keys()) == [8 + RIDX[simple[i]]] and col[8 + RIDX[simple[i]]] in (1, -1), col
        bits.append(0 if col[8 + RIDX[simple[i]]] == 1 else 1)
    return bits
def t_eta_cols(eta):   # torus element acting by (-1)^{sum eta_i a_i} on e_a, trivially on the Cartan
    cols = [{j: 1} for j in range(8)]
    for r in ROOTS:
        s = sum(eta[i]*r[i] for i in range(8)) % 2
        cols.append({8 + RIDX[r]: -1 if s else 1})
    return cols
def solve_f2(Mrows, rhs):   # rows of an 8x8 F2 system; returns a solution or None
    M = [row[:] + [rhs[i]] for i, row in enumerate(Mrows)]; piv = []; r = 0
    for c in range(8):
        p_ = next((i for i in range(r, 8) if M[i][c]), None)
        if p_ is None: continue
        M[r], M[p_] = M[p_], M[r]
        for i in range(8):
            if i != r and M[i][c]: M[i] = [(a ^ b) for a, b in zip(M[i], M[r])]
        piv.append(c); r += 1
    if any(all(v == 0 for v in row[:8]) and row[8] for row in M): return None
    sol = [0]*8
    for i, c in enumerate(piv): sol[c] = M[i][8]
    return sol
for name, W in elements.items():
    word = reduced_word(W); L = lift_matrix(word); L2 = compose(L, L); L3 = compose(L2, L)
    if L3 == ID:
        print(f"[{name}] Tits lift already of order 3"); continue
    delta = sign_char_of(L3)
    # eta.w on simple root alpha_j = eta(w alpha_j) = sum_i eta_i (w alpha_j)_i ; matrix rows: coefficient of eta_i in (eta + eta.w + eta.w^2)(alpha_j)
    W2 = mmul8(W, W)
    rows = [[(int(i == j) + W[i][j] + W2[i][j]) % 2 for i in range(8)] for j in range(8)]
    eta = solve_f2(rows, delta)
    if eta is None:
        print(f"[{name}] no sign-character correction gives order 3 (would need an omega-valued torus element)"); continue
    Lc = compose(L, t_eta_cols(eta)); Lc2 = compose(Lc, Lc); Lc3 = compose(Lc2, Lc)
    ok3 = (Lc3 == ID)
    LmI = [dict(Lc[j]) for j in range(DIM)]
    for j in range(DIM): LmI[j][j] = LmI[j].get(j, 0) - 1
    Q = [dict(Lc2[j]) for j in range(DIM)]
    for j in range(DIM):
        for k, c in Lc[j].items(): Q[j][k] = Q[j].get(k, 0) + c
        Q[j][j] = Q[j].get(j, 0) + 1
    res = {p: (DIM - rank_modp(LmI, p), DIM - rank_modp(Q, p)) for p in (10007, 1000003)}
    print(f"[{name}] corrected lift w-hat.t_eta with eta = {eta}: order 3: {ok3}; (fixed, omega+omegabar) mod 10007 / 1000003: {res[10007]} / {res[1000003]}")
