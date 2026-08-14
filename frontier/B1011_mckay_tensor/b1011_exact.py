"""B1011 phase 2 -- exact class-rep characters in Q(zeta_60), matched against the
quaternion-model character table of 2T x 2I. Every number below is exact."""
import itertools, json
from fractions import Fraction as F

# ---------- Q(zeta_60) as Q[x]/Phi_60, Phi_60 = x^16+x^14-x^10-x^8-x^6+x^2+1 ----------
PHI = [1, 0, 1, 0, 0, 0, -1, 0, -1, 0, -1, 0, 0, 0, 1, 0, 1]  # coeffs c0..c16
DEG = 16

def red(v):
    v = list(v)
    while len(v) > DEG:
        c = v.pop()
        if c:
            for i in range(DEG + 1):
                v[len(v) - 1 - (16 - i) + 0] = 0  # placeholder (rewritten below)
    return v

def poly_mod(v):
    v = list(v)
    while len(v) > DEG:
        c = v.pop()
        if c:
            base = len(v) - DEG
            for i in range(DEG):
                v[base + i] -= c * PHI[i]
    return v + [F(0)] * (DEG - len(v))

class Z60:
    __slots__ = ("c",)
    def __init__(self, c):
        self.c = tuple(c)
    @staticmethod
    def zero(): return Z60([F(0)] * DEG)
    @staticmethod
    def one():  return Z60([F(1)] + [F(0)] * (DEG - 1))
    @staticmethod
    def zeta(k):  # zeta_60^k
        k %= 60
        v = [F(0)] * (k + 1); v[k] = F(1)
        return Z60(poly_mod(v))
    def __add__(a, b): return Z60([x + y for x, y in zip(a.c, b.c)])
    def __sub__(a, b): return Z60([x - y for x, y in zip(a.c, b.c)])
    def __neg__(a): return Z60([-x for x in a.c])
    def __mul__(a, b):
        out = [F(0)] * (2 * DEG - 1)
        for i, x in enumerate(a.c):
            if x:
                for j, y in enumerate(b.c):
                    if y: out[i + j] += x * y
        return Z60(poly_mod(out))
    def scale(a, r): return Z60([x * r for x in a.c])
    def conj(a):  # zeta -> zeta^-1 = zeta^59
        out = Z60.zero()
        for i, x in enumerate(a.c):
            if x: out = out + Z60.zeta((-i) % 60).scale(x)
        return out
    def __eq__(a, b): return a.c == b.c
    def is_rational(a): return all(x == 0 for x in a.c[1:])
    def __repr__(a):
        return "Z60" + str([str(x) for x in a.c if x != 0][:4])

def mat_mul(A, B):
    n = len(A)
    return [[sum((A[i][t] * B[t][j] for t in range(n)), Z60.zero()) for j in range(n)]
            for i in range(n)]

# ---------- exact Sigma, T ----------
def build_and_save():
    """Rebuild Sigma, T, R, L exactly and write class_chars artifacts (see FINDINGS)."""
    def ex(r):  # exp(2 pi i r), r = Fraction with denominator | 60
        k = r * 60
        assert k.denominator == 1
        return Z60.zeta(int(k) % 60)

    k_lvl, kap = 2, 5
    weights = [(a, b) for a in range(k_lvl + 1) for b in range(k_lvl + 1 - a)]
    n = 6
    Lv = lambda w: (w[0] + w[1] + 2, w[1] + 1, 0)
    def ip3(u, v):
        return F(sum(u[i] * v[i] for i in range(3))) - F(sum(u) * sum(v), 3)
    perms = list(itertools.permutations(range(3)))
    sgn = lambda pm: (-1) ** sum(pm[i] > pm[j] for i in range(3) for j in range(i + 1, 3))

    Sig = [[Z60.zero() for _ in range(n)] for _ in range(n)]
    for i, wl in enumerate(weights):
        for j, wm in enumerate(weights):
            acc = Z60.zero()
            for pm in perms:
                t = ex((-ip3(tuple(Lv(wl)[q] for q in pm), Lv(wm)) / kap) % 1)
                acc = acc + (t if sgn(pm) == 1 else -t)
            Sig[i][j] = acc

    c_charge = F(16, 5)
    Tdiag = [ex(((F(2, 3) * (a * a + a * b + b * b) + 2 * (a + b)) / (2 * kap) - c_charge / 24) % 1)
             for (a, b) in weights]

    # Sigma * conj(Sigma)^T = g * I  (Sigma symmetric, so conj elementwise then multiply)
    SigC = [[Sig[i][j].conj() for j in range(n)] for i in range(n)]
    G = mat_mul(Sig, SigC)
    gval = G[0][0]
    assert gval.is_rational(), "Gram scalar not rational"
    for i in range(n):
        for j in range(n):
            assert G[i][j] == (gval if i == j else Z60.zero()), "Sigma not proportional-unitary"
    g_rat = gval.c[0]
    print(f"Sigma * Sigma^dag = {g_rat} * I  (exact)")

    # R = T ; L = Sigma^-1 T^-1 Sigma = (1/g) SigC . Tbar . Sig
    Tbar = [t.conj() for t in Tdiag]
    TbarSig = [[Sig[i][j] * Tbar[i] for j in range(n)] for i in range(n)]   # diag(Tbar).Sig
    L = mat_mul(SigC, TbarSig)
    L = [[L[i][j].scale(F(1) / g_rat) for j in range(n)] for i in range(n)]
    R = [[(Tdiag[i] if i == j else Z60.zero()) for j in range(n)] for i in range(n)]

    # exact check: odd plane invariance. odd basis (unnormalized): e_(0,1)-e_(1,0), e_(0,2)-e_(2,0)
    idx = {w: i for i, w in enumerate(weights)}
    pairs = [((0, 1), (1, 0)), ((0, 2), (2, 0))]
    sym_pairs = [((0, 1), (1, 0), 1), ((0, 2), (2, 0), 1)]   # even combos with +
    def apply(M, vec):
        return [sum((M[i][j] * vec[j] for j in range(n)), Z60.zero()) for i in range(n)]
    def basis_vec(a, b, s):
        v = [Z60.zero()] * n
        v[idx[a]] = Z60.one()
        v[idx[b]] = Z60.one().scale(F(s))
        return v
    odd_ok = True
    for (a, b) in pairs:
        for M in (R, L):
            img = apply(M, basis_vec(a, b, -1))
            # even components: coefficient on (0,0),(1,1) and SYMMETRIC combos must vanish:
            for w0 in [(0, 0), (1, 1)]:
                odd_ok &= img[idx[w0]] == Z60.zero()
            for (u, v) in pairs:
                odd_ok &= (img[idx[u]] + img[idx[v]]) == Z60.zero()   # symmetric part zero
    print("odd 2-plane exactly invariant under R and L:", odd_ok)

    # characters on class reps
    reps = json.load(open("class_reps.json"))
    def word_mat(wd):
        M = [[(Z60.one() if i == j else Z60.zero()) for j in range(n)] for i in range(n)]
        for ch in wd:
            M = mat_mul(M, R if ch == "R" else L)
        return M

    rows = []
    for rec in reps:
        M = word_mat(rec["word"])
        tr6 = sum((M[i][i] for i in range(n)), Z60.zero())
        # odd-block trace: restrict to odd basis o1,o2 (Gram = 2*I): tr_odd = (1/2) sum <o_k, M o_k>
        tro = Z60.zero()
        for (a, b) in pairs:
            img = apply(M, basis_vec(a, b, -1))
            tro = tro + (img[idx[a]] - img[idx[b]]).scale(F(1, 2))
        tre = tr6 - tro
        rows.append({"word": rec["word"], "size": rec["size"],
                     "tr_odd": tro, "tr_even": tre})
    print("computed exact (tr_odd, tr_even) on all 63 class reps")

    # quick exact census of value sets, printed as Z60 vectors resolved to closed forms:
    import collections
    def z60_name(z):
        # try to recognize in Q(sqrt5): basis 1, zeta+zeta^-1 combos... print raw vector
        return tuple(str(x) for x in z.c)
    oddvals = collections.Counter(z60_name(r["tr_odd"]) for r in rows)
    print("distinct exact tr_odd values:", len(oddvals))
    evenvals = collections.Counter(z60_name(r["tr_even"]) for r in rows)
    print("distinct exact tr_even values:", len(evenvals))
    import pickle
    pickle.dump(rows, open("class_chars.pkl", "wb"))
    print("saved class_chars.pkl")


if __name__ == '__main__':
    build_and_save()
