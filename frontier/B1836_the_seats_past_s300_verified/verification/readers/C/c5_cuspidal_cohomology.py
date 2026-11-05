"""C5 (P-634, Theorem 62 Part 2): cuspidal (parabolic) cohomology computed, not asserted. Exact arithmetic in Q(sqrt-3)
(a small field class; Gaussian elimination), so the dimensions are exact.
 (A) the lane's group: Gamma' = <A, B> = [SL(2,Z), SL(2,Z)], A = [[2,1],[1,1]], B = [[1,1],[1,2]] (free of rank 2, one cusp,
     K = ABA^-1B^-1), coefficients Sym^{2k}(C^2), k = 1..4: dim H^1 and dim H^1_par = ker(H^1 -> H^1(<K>)).
     Eichler-Shimura check: dim H^1_par = 2 dim S_{2k+2}(Gamma'); Gamma' (image in PSL2: index 6, genus 1, one cusp, no elliptic
     points) has dim S_w = w/2 - 1 for even w >= 4 (the genus formula).
 (B) what P-634 asks: m004's own group pi_1 = <x, y | x y^-1 x^-1 y x y^-1 x y x^-1 y^-1> (C4: Riley's rep satisfies it),
     with Riley's holonomy x -> [[1,1],[0,1]], y -> [[1,0],[-z,1]], z = -1/2 - sqrt(-3)/2, in SL(2, Z[omega]), and the Bianchi
     coefficients E_{k,k} = Sym^k (x) conj Sym^k, k = 0..3: dim H^1 and dim H^1_cusp = ker(H^1 -> H^1(peripheral Z^2)); the
     longitude found by a float search and verified exactly.
No SM quantity."""
from fractions import Fraction as Fr
import itertools, pathlib
import numpy as np

class F:
    __slots__ = ("a", "b")                                   # a + b*s, s^2 = -3
    def __init__(self, a=0, b=0): self.a, self.b = Fr(a), Fr(b)
    def __add__(s, o): o = o if isinstance(o, F) else F(o); return F(s.a + o.a, s.b + o.b)
    __radd__ = __add__
    def __neg__(s): return F(-s.a, -s.b)
    def __sub__(s, o): return s + (-(o if isinstance(o, F) else F(o)))
    def __rsub__(s, o): return F(o) - s
    def __mul__(s, o): o = o if isinstance(o, F) else F(o); return F(s.a * o.a - 3 * s.b * o.b, s.a * o.b + s.b * o.a)
    __rmul__ = __mul__
    def inv(s): n = s.a * s.a + 3 * s.b * s.b; return F(s.a / n, -s.b / n)
    def conj(s): return F(s.a, -s.b)
    def iszero(s): return s.a == 0 and s.b == 0
    def c(s): return complex(float(s.a), float(s.b) * 3 ** 0.5)

Z0, O1 = F(0), F(1)
def mat(rows): return [[x if isinstance(x, F) else F(x) for x in r] for r in rows]
def eye(n): return [[O1 if i == j else Z0 for j in range(n)] for i in range(n)]
def zeros(n, m): return [[Z0] * m for _ in range(n)]
def mm(A, B): return [[sum((A[i][k] * B[k][j] for k in range(len(B))), Z0) for j in range(len(B[0]))] for i in range(len(A))]
def madd(A, B, sg=1): return [[A[i][j] + (B[i][j] if sg == 1 else -B[i][j]) for j in range(len(A[0]))] for i in range(len(A))]
def inv2(g): (a, b), (c, d) = g; det = a * d - b * c; di = det.inv(); return [[d * di, -b * di], [-c * di, a * di]]
def mconj(A): return [[x.conj() for x in r] for r in A]
def hstack(*Ms): return [sum((M[i] for M in Ms), []) for i in range(len(Ms[0]))]
def vstack(*Ms): return [r for M in Ms for r in M]
def kron(A, B): return [[A[i][j] * B[k][l] for j in range(len(A[0])) for l in range(len(B[0]))] for i in range(len(A)) for k in range(len(B))]
def rank(M):
    M = [r[:] for r in M]; rk = 0; rows = len(M); cols = len(M[0]) if M else 0
    for c in range(cols):
        p = next((r for r in range(rk, rows) if not M[r][c].iszero()), None)
        if p is None: continue
        M[rk], M[p] = M[p], M[rk]; iv = M[rk][c].inv()
        M[rk] = [x * iv for x in M[rk]]
        for r in range(rows):
            if r != rk and not M[r][c].iszero():
                f = M[r][c]; M[r] = [M[r][j] - f * M[rk][j] for j in range(cols)]
        rk += 1
    return rk
def polymul(p, q):
    out = [Z0] * (len(p) + len(q) - 1)
    for i, x in enumerate(p):
        for j, y in enumerate(q): out[i + j] = out[i + j] + x * y
    return out
def sym_power(g, n):
    """g on Sym^n(C^2), basis e1^(n-i) e2^i: g e1 = a e1 + c e2, g e2 = b e1 + d e2; coefficient lists in powers of e2."""
    (a, b), (c, d) = g
    M = zeros(n + 1, n + 1)
    for i in range(n + 1):
        p = [O1]
        for _ in range(n - i): p = polymul(p, [a, c])
        for _ in range(i): p = polymul(p, [b, d])
        for j in range(n + 1): M[j][i] = p[j]
    return M
def apply(word, rep):
    n = len(next(iter(rep.values()))); P = eye(n)
    for g, e in word: P = mm(P, rep[g] if e == 1 else rep[g + "inv"])
    return P
def cocycle_cols(word, rep, gens):
    """matrix (d x (len(gens) d)) of the linear map (u_g) -> u_word, u_{gh} = u_g + g u_h."""
    d = len(rep[gens[0]]); blocks = {g: zeros(d, d) for g in gens}; prefix = eye(d)
    for g, e in word:
        if e == 1: blocks[g] = madd(blocks[g], prefix); prefix = mm(prefix, rep[g])
        else: prefix = mm(prefix, rep[g + "inv"]); blocks[g] = madd(blocks[g], prefix, -1)
    return hstack(*[blocks[g] for g in gens]), prefix

out = []
# ---------------- (A)
A = mat([[2, 1], [1, 1]]); Bm = mat([[1, 1], [1, 2]])
for k in (1, 2, 3, 4):
    n = 2 * k; d = n + 1
    rep = {"A": sym_power(A, n), "B": sym_power(Bm, n)}; rep["Ainv"] = sym_power(inv2(A), n); rep["Binv"] = sym_power(inv2(Bm), n)
    I = eye(d)
    H0 = d - rank(vstack(madd(rep["A"], I, -1), madd(rep["B"], I, -1)))
    dimB1 = d - H0; dimH1 = 2 * d - dimB1
    UK, rK = cocycle_cols([("A", 1), ("B", 1), ("A", -1), ("B", -1)], rep, ["A", "B"])
    imK = madd(rK, I, -1)
    r_img = rank(hstack(UK, imK)) - rank(imK)
    out.append("(A) Gamma', Sym^%d: dim H^0 = %d, dim H^1 = %d, dim H^1_par = %d ; Eichler-Shimura 2 dim S_%d = %d"
               % (n, H0, dimH1, dimH1 - r_img, n + 2, 2 * ((n + 2) // 2 - 1)))

# ---------------- (B)
z = F(Fr(-1, 2), Fr(-1, 2))
X = mat([[1, 1], [0, 1]]); Y = [[O1, Z0], [-z, O1]]
lane = [("x", 1), ("y", -1), ("x", -1), ("y", 1), ("x", 1), ("y", -1), ("x", 1), ("y", 1), ("x", -1), ("y", -1)]
base = {"x": X, "y": Y, "xinv": inv2(X), "yinv": inv2(Y)}
Rimg = apply(lane, base)
out.append("(B) Riley's rep satisfies the lane's relator exactly: %s" % all((Rimg[i][j] - (O1 if i == j else Z0)).iszero() for i in range(2) for j in range(2)))
fl = {k: np.array([[v.c() for v in r] for r in M]) for k, M in base.items()}
lam = None
letters = [("x", 1), ("x", -1), ("y", 1), ("y", -1)]
for Lw in range(2, 11):
    for wd in itertools.product(letters, repeat=Lw):
        if any(wd[i][0] == wd[i + 1][0] and wd[i][1] == -wd[i + 1][1] for i in range(Lw - 1)): continue
        Mf = np.eye(2, dtype=complex)
        for g, e in wd: Mf = Mf @ fl[g if e == 1 else g + "inv"]
        if abs(Mf[1, 0]) < 1e-9 and abs(Mf[0, 0] - Mf[1, 1]) < 1e-9 and abs(abs(Mf[0, 0]) - 1) < 1e-9 and abs((Mf[0, 1] / Mf[0, 0]).imag) > 1e-6:
            Me = apply(list(wd), base)
            if Me[1][0].iszero() and (Me[0][0] - Me[1][1]).iszero():
                lam = list(wd); break
    if lam: break
Ml = apply(lam, base)
out.append("    longitude word %s : rho = %s * [[1, %s],[0, 1]] (exact)" % ("".join(g if e == 1 else g.upper() for g, e in lam),
           Ml[0][0].c().real, complex((Ml[0][1] * Ml[0][0].inv()).c())))
for k in (0, 1, 2, 3):
    def E(g): return kron(sym_power(g, k), sym_power(mconj(g), k))
    rep = {g: E(M) for g, M in base.items()}
    d = len(rep["x"]); I = eye(d)
    J, Rk = cocycle_cols(lane, rep, ["x", "y"])
    H0 = d - rank(vstack(madd(rep["x"], I, -1), madd(rep["y"], I, -1)))
    rJ = rank(J); dimZ1 = 2 * d - rJ; dimB1 = d - H0; dimH1 = dimZ1 - dimB1
    # cusp: restriction (u_x, u_lambda) of a cocycle must be a peripheral coboundary ((x - 1)v, (lambda - 1)v)
    Ul, rl = cocycle_cols(lam, rep, ["x", "y"])
    Ux = hstack(I, zeros(d, d))                                         # (u_x, u_y) -> u_x
    Res = vstack(Ux, Ul)                                                # (2d) x (2d)
    Bper = vstack(madd(rep["x"], I, -1), madd(rl, I, -1))
    # image of Z^1 in H^1(P) = rank([Res restricted to Z^1 | Bper]) - rank(Bper); restrict via [J; Res] trick:
    # dim{z in Z^1 : Res z in im Bper} = dim ker [[J, 0], [Res, -Bper]] projected to z; compute via ranks
    big = vstack(hstack(J, zeros(len(J), d)), hstack(Res, [[-x for x in r] for r in Bper]))
    ker_big = (2 * d + d) - rank(big)                                    # pairs (z, v) with z in Z^1 and Res z = Bper v
    ker_v = d - rank(Bper)                                               # pairs (0, v) with Bper v = 0
    dimZcusp = ker_big - ker_v                                           # z in Z^1 with Res z in im Bper (contains B^1)
    out.append("    E_{%d,%d} (dim %d): dim H^0 = %d, dim H^1 = %d, dim H^1_cusp = %d" % (k, k, d, H0, dimH1, dimZcusp - dimB1))
print("\n".join(out))
pathlib.Path(__file__).with_name("c5_run.txt").write_text("\n".join(out) + "\n")
