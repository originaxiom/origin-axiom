"""R66 -- the Tits lift of w_3 (the founding ratio's E6 factor) in B351's exact e6: its order and Ad-eigenvalue multiplicities.
Removes R64/R65's 'order-3 lift' caveat for the E6 class."""
import sys, itertools, collections
from fractions import Fraction as Fr
sys.path.insert(0, 'rec/B351_exact_e6_chevalley')
import exact_e6 as X6
# ---- (1) re-run R64's lattice part to get the icosian E6 roots and w_3 (exec the file up to the E8-class section)
src = open('r64_founding_ratio_type.py').read().split("# ---- E8 conjugacy type")[0]
import io, contextlib
buf = io.StringIO()
with contextlib.redirect_stdout(buf): exec(src)
print("[R64 lattice part re-run] E6 roots:", len(E6_roots := E6), "| w_3 order", order_m(w3), "fixed dim", fixdim(w3))
# ---- (2) simple roots of the icosian E6 via a generic functional; Cartan matrix (norm-2 scaling: 2*B)
import random
for seed in range(7, 100):
    random.seed(seed); f = [Fr(random.randint(-97, 97)) for _ in range(8)]
    if all(sum(a*b for a, b in zip(f, [Fr(c) for c in vec(r)])) != 0 for r in E6_roots): break
def fval(q): return sum(a*b for a, b in zip(f, [Fr(c) for c in vec(q)]))
vals = [fval(r) for r in E6_roots]; print("   functional: positives", sum(1 for v in vals if v > 0), "zeros", sum(1 for v in vals if v == 0), "negatives", sum(1 for v in vals if v < 0))
posE6 = [r for r in E6_roots if fval(r) > 0]; assert len(posE6) == 36
pset = set(posE6)
def qadd(p, q): return tuple(fadd(a, b) for a, b in zip(p, q))
simpleE6 = [r for r in posE6 if not any(qadd(s, t) == r for s in posE6 for t in posE6)]
assert len(simpleE6) == 6
cart = [[int(2*B(a, b)) for b in simpleE6] for a in simpleE6]
# match to Bourbaki A (B351's X6.A) by a permutation
A = X6.A
perm = next(p for p in itertools.permutations(range(6)) if all(cart[p[i]][p[j]] == A[i][j] for i in range(6) for j in range(6)))
simpleB = [simpleE6[perm[i]] for i in range(6)]     # simpleB[i] plays Bourbaki's alpha_{i+1}
print("[simple roots] icosian E6 Cartan matrix matched to Bourbaki labelling by permutation", perm)
# express every icosian E6 root in simple-root coordinates: solve integer combination via the Gram
import sympy as sp
G = sp.Matrix(6, 6, lambda i, j: sp.Rational(2*B(simpleB[i], simpleB[j])))
def coords6(r):
    rhs = sp.Matrix([sp.Rational(2*B(r, s)) for s in simpleB]); c = G.solve(rhs)
    assert all(x.is_integer for x in c); return tuple(int(x) for x in c)
rootcoords = {r: coords6(r) for r in E6_roots}
assert set(rootcoords.values()) == set(X6.ROOTS), "root systems do not match"
# w_3 on simple roots -> 6x6 matrix in simple-root coordinates (columns = images)
def w3_on(r):
    v = w3*coords(r); return quat_from_vec(list(Bm.T*v))
Wmat = [[0]*6 for _ in range(6)]
for j, s in enumerate(simpleB):
    img = rootcoords[w3_on(s)]
    for i in range(6): Wmat[i][j] = img[i]
print("[w_3 in W(E6)] matrix on simple-root coordinates:", Wmat)
# ---- (3) BFS in W(E6) for a reduced word
def smat(i):   # s_i(alpha_j) = alpha_j - A[i][j] alpha_i   (symmetric Cartan)
    M = [[int(a == b) for b in range(6)] for a in range(6)]
    for j in range(6): M[i][j] -= A[i][j]
    return M
S = [smat(i) for i in range(6)]
def mmul(X, Y): return [[sum(X[i][k]*Y[k][j] for k in range(6)) for j in range(6)] for i in range(6)]
def key(M): return tuple(tuple(r) for r in M)
I6 = [[int(a == b) for b in range(6)] for a in range(6)]
target = key(Wmat)
seen = {key(I6): ()}; frontier = [I6]; word = None
while frontier and word is None:
    nxt = []
    for M in frontier:
        for i in range(6):
            N = mmul(S[i], M); k = key(N)      # left-multiply: word = (i,) + old word  => element = s_i . old
            if k in seen: continue
            seen[k] = (i,) + seen[key(M)]; nxt.append(N)
            if k == target: word = seen[k]; break
        if word: break
    frontier = nxt
print(f"[word] |W(E6)| explored: {len(seen)}; w_3 = s_" + " s_".join(str(i+1) for i in word), f"(length {len(word)})")
# ---- (4) Tits lifts on the 78 (exact Fractions); ad e nilpotent of degree 3 on the adjoint
DIM = X6.DIM
def matmul(X, Y):
    return [[sum(X[i][k]*Y[k][j] for k in range(DIM) if X[i][k]) for j in range(DIM)] for i in range(DIM)]
def madd(X, Y): return [[X[i][j] + Y[i][j] for j in range(DIM)] for i in range(DIM)]
def mscale(X, c): return [[c*X[i][j] for j in range(DIM)] for i in range(DIM)]
ID = [[Fr(int(i == j)) for j in range(DIM)] for i in range(DIM)]
def expad(x):
    Ad = X6._ad_matrix(x); Ad2 = matmul(Ad, Ad); Ad3 = matmul(Ad2, Ad)
    assert all(v == 0 for row in Ad3 for v in row), "ad x not nilpotent of degree 3"
    return madd(madd(ID, Ad), mscale(Ad2, Fr(1, 2)))
def e_vec(i, sign=1):
    r = tuple(sign*(1 if k == i else 0) for k in range(6)); return {6 + X6.RIDX[r]: 1}
lifts = []
for i in range(6):
    n_i = matmul(matmul(expad(e_vec(i, 1)), expad(e_vec(i, -1))), expad(e_vec(i, 1)))   # exp(e) exp(-f) exp(e), f = -e_{-alpha}
    # check: acts on the Cartan as the reflection s_i:  Ad(n_i) h_j = h_j - A[j][i] h_i ? (h_alpha reflection)
    ok = True
    for j in range(6):
        col = [n_i[k][j] for k in range(DIM)]
        expect = [Fr(0)]*DIM; expect[j] += 1; expect[i] -= A[i][j]
        ok &= (col == expect)
    lifts.append(n_i)
    if not ok: print(f"   [warn] n_{i+1} does not act as s_{i+1} on the Cartan with this sign convention")
W_lift = ID
for i in reversed(word): W_lift = matmul(lifts[i], W_lift)      # word[0] is the leftmost factor: build right-to-left
# ---- (5) order and eigenvalue multiplicities
def rank(M):
    return sp.Matrix(M).rank()
W2 = matmul(W_lift, W_lift); W3 = matmul(W2, W_lift)
is_id = (W3 == ID)
print(f"[lift] w_3-hat^3 == identity on the 78: {is_id}")
if not is_id:
    W6 = matmul(W3, W3); print("       w_3-hat^6 == identity:", W6 == ID)
fixed = DIM - rank(madd(W_lift, mscale(ID, Fr(-1))))
cube_root_space = DIM - rank(madd(madd(W2, W_lift), ID))     # ker(w^2 + w + 1) = omega- and omega-bar-eigenspaces
print(f"[Ad multiplicities] fixed (eigenvalue 1): {fixed};  omega + omega-bar: {cube_root_space};  total {fixed + cube_root_space} of 78")
print("      A2^3 class needs (24, 27+27); D4xT^2 would be (30, 24+24).")
# consistency: Ad(w-hat) restricted to the Cartan equals W (in the h-basis, h_j -> sum_i W... ) -- check images of h_j against Wmat via coroots = roots (simply laced)
cart_ok = all([W_lift[k][j] for k in range(6)] == [Fr(Wmat[k][j]) for k in range(6)] and all(W_lift[k][j] == 0 for k in range(6, DIM)) for j in range(6))
print("[consistency] Ad(w_3-hat) on the Cartan reproduces the Weyl matrix:", cart_ok)
