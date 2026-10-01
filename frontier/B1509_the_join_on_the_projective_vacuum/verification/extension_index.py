"""B1509 verification -- main's index on the minimal non-split extensions of the audit lane's projective vacuum.

Written after PREDICTIONS.md was committed and pushed (3edaf1fa).  For each exceptional point (q, mu) of Ballas' family with a
central twist (q = 17 +- 12 sqrt2 with mu = -1; q = 7 +- 4 sqrt3 with mu = +-i), with A = mu rho_q (rank 4) and c a generator of
H^1(pi; A):
  W1 = [[A, c], [0, 1]]            (rank 5, the trivial line as quotient; det = mu^4 = 1)
  W1* (the dual), W1[A*] = [[A*, c*], [0, 1]], W2 = W1[A*]*   (the opposite order),
  Lambda^2 W1, Lambda^2 W2          (rank 10),
and main's index I(V) = n(V) - n(V*), n = dim ker(H^1(pi; V) -> H^1(T; V)) (B1297; this seat's B1374 index_lib conventions).
Two routes:
  exact  -- DomainMatrix over Q(sqrt2, sqrt3, i), a port of index_lib.cohomology_data to exact arithmetic;
  mod p  -- index_lib itself over GF(p) for p = 1009, 1033, 1129 (all = 1 mod 24, so sqrt2, sqrt3 and i exist), both choices of
            each square root (both conjugate q), with index_lib's built-in identity checks (r1 + q1 = t1 = s1, I = (a0-b0)+s0-r1).
Also: the twisted Alexander multiplicity of s = mu in Q(q, s) (T3's mechanism), and the U(1)_T charge of the extension block (D6)."""
import importlib.util
import json
import sys
from pathlib import Path

import sympy as sp
from sympy.polys.matrices import DomainMatrix

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
WORD_R = "mnMNmNMnmN"
WORD_MU = "m"
WORD_L = "nMNmmNMn"
GENS = ("m", "n")

_spec = importlib.util.spec_from_file_location("b1374_index_lib", ROOT / "frontier/B1374_the_class_index_in_the_sm_frame/verification/index_lib.py")
IL = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(IL)

K = sp.QQ.algebraic_field(sp.sqrt(2), sp.sqrt(3), sp.I)
POINTS = [("17-12sqrt2", 17 - 12 * sp.sqrt(2), -1, "-1"), ("17+12sqrt2", 17 + 12 * sp.sqrt(2), -1, "-1"),
          ("7-4sqrt3", 7 - 4 * sp.sqrt(3), sp.I, "i"), ("7+4sqrt3", 7 + 4 * sp.sqrt(3), sp.I, "i"),
          ("7-4sqrt3", 7 - 4 * sp.sqrt(3), -sp.I, "-i"), ("7+4sqrt3", 7 + 4 * sp.sqrt(3), -sp.I, "-i")]


def ballas(qq):
    t = qq / 2
    m = sp.Matrix([[1, 0, 1, t - 1], [0, 1, 1, t], [0, 0, 1, t + sp.Rational(1, 2)], [0, 0, 0, 1]])
    n = sp.Matrix([[1, 0, 0, 0], [2 + 1 / t, 1, 0, 0], [2, 1, 1, 0], [1, 1, 0, 1]])
    return m, n


# ------------------------------------------------------------------ exact route (DomainMatrix)
def dm(M):
    return DomainMatrix.from_Matrix(sp.Matrix(M)).convert_to(K)


class ERep:
    def __init__(self, mats):
        self.M = dict(mats)
        self.d = mats["m"].shape[0]
        for g in GENS:
            self.M[g.upper()] = mats[g].inv()

    def word(self, w):
        X = DomainMatrix.eye(self.d, K)
        for ch in w:
            X = X * self.M[ch]
        return X

    def fox(self, w):
        D = {g: DomainMatrix.zeros((self.d, self.d), K) for g in GENS}
        pre = DomainMatrix.eye(self.d, K)
        for ch in w:
            g = ch.lower()
            D[g] = D[g] + pre if ch.islower() else D[g] - pre * self.M[ch]
            pre = pre * self.M[ch]
        return D

    def dual(self):
        return ERep({g: self.M[g].inv().transpose() for g in GENS})


def nullspace_cols(A):
    """basis of {x : A x = 0} as a list of column DomainMatrices"""
    N = A.nullspace()          # rows spanning the nullspace
    return [N[i:i + 1, :].transpose() for i in range(N.shape[0])] if N.shape[0] else []


def rank(A):
    return A.rank() if A.shape[0] and A.shape[1] else 0


def cohomology_data_exact(rep):
    d = rep.d
    I = DomainMatrix.eye(d, K)
    d0 = (rep.M["m"] - I).vstack(rep.M["n"] - I)
    rk0 = rank(d0)
    a0 = d - rk0
    D = rep.fox(WORD_R)
    J = D["m"].hstack(D["n"])
    Z1 = nullspace_cols(J)
    a1 = len(Z1) - rk0
    Wm, Wl = rep.word(WORD_MU), rep.word(WORD_L)
    Am, Al = Wm - I, Wl - I
    BT = Am.vstack(Al)
    rkBT = rank(BT)
    t0 = d - rkBT
    ZT = (-Al).hstack(Am)
    t1 = 2 * d - rank(ZT) - rkBT
    Dm, Dl = rep.fox(WORD_MU), rep.fox(WORD_L)
    Res = Dm["m"].hstack(Dm["n"]).vstack(Dl["m"].hstack(Dl["n"]))
    if Z1:
        cols = Res * Z1[0].hstack(*Z1[1:]) if len(Z1) > 1 else Res * Z1[0]
        r1 = rank(cols.hstack(BT)) - rkBT
    else:
        r1 = 0
    return a0, a1, t0, t1, r1


def index_exact(rep):
    a0, a1, t0, t1, r1 = cohomology_data_exact(rep)
    b0, b1, s0, s1, q1 = cohomology_data_exact(rep.dual())
    I = (a1 - r1) - (b1 - q1)
    assert r1 + q1 == t1 == s1, ("annihilator identity", r1, q1, t1, s1)
    assert I == (a0 - b0) + s0 - r1, ("B1297 identity", I, a0, b0, s0, r1)
    return I, (a0, a1, t0, r1), (b0, b1, s0, q1)


def generator_cocycle(rep):
    """a 1-cocycle (values on m, n) that is not a coboundary; h^1 must be 1"""
    d = rep.d
    I = DomainMatrix.eye(d, K)
    D = rep.fox(WORD_R)
    Z1 = nullspace_cols(D["m"].hstack(D["n"]))
    B = (rep.M["m"] - I).vstack(rep.M["n"] - I)
    rkB = rank(B)
    for z in Z1:
        if rank(B.hstack(z)) > rkB:
            return {"m": z[0:d, :], "n": z[d:2 * d, :]}
    raise ValueError("no non-coboundary cocycle")


def extension(rep, c):
    """W = [[A(g), c(g)], [0, 1]] on the generators"""
    mats = {}
    for g in GENS:
        top = rep.M[g].hstack(c[g])
        bottom = DomainMatrix.zeros((1, rep.d), K).hstack(DomainMatrix.eye(1, K))
        mats[g] = top.vstack(bottom)
    return ERep(mats)


def ext_square(M):
    """Lambda^2 of a square DomainMatrix on the basis e_i ^ e_j (i < j)"""
    n = M.shape[0]
    S = M.to_Matrix()
    pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
    out = sp.zeros(len(pairs))
    for b, (k, l) in enumerate(pairs):
        for a, (i, j) in enumerate(pairs):
            out[a, b] = S[i, k] * S[j, l] - S[i, l] * S[j, k]
    return DomainMatrix.from_Matrix(out).convert_to(K)


def lam2(rep):
    return ERep({g: ext_square(rep.M[g]) for g in GENS})


def exact_point(qq, mu):
    m, n = ballas(qq)
    A = ERep({"m": dm(mu * m), "n": dm(mu * n)})
    assert A.word(WORD_R) == DomainMatrix.eye(4, K)
    hA = index_exact(A)[1][1]
    Astar = A.dual()
    hAs = index_exact(Astar)[1][1]
    c = generator_cocycle(A)
    W1 = extension(A, c)
    assert W1.word(WORD_R) == DomainMatrix.eye(5, K), "W1 is not a representation"
    cs = generator_cocycle(Astar)
    W1s = extension(Astar, cs)             # W1[A*]
    I_W1 = index_exact(W1)
    I_W1s = index_exact(W1s)
    I_L1 = index_exact(lam2(W1))
    I_L1s = index_exact(lam2(W1s))
    # U(1)_T = diag(1,1,1,1,-4): charge of the off-diagonal block E_{i5}
    T = sp.diag(1, 1, 1, 1, -4)
    E = sp.zeros(5)
    E[0, 4] = 1
    charge = sp.simplify((T * E - E * T)[0, 4])
    return {
        "h1(A)": hA, "h1(A*)": hAs,
        "I(W1)": I_W1[0], "W1 data (a0,a1,t0,r1)": I_W1[1], "W1* data": I_W1[2],
        "I(W2) = -I(W1[A*])": -I_W1s[0],
        "I(Lambda2 W1)": I_L1[0], "I(Lambda2 W2) = -I(Lambda2 W1[A*])": -I_L1s[0],
        "N(10') = -I(W1)": -I_W1[0], "N(5bar') = -I(Lambda2 W1)": -I_L1[0],
        "U(1)_T charge of the extension block": int(charge),
    }


# ------------------------------------------------------------------ mod-p route (index_lib)
PRIMES = (1009, 1033, 1129)


def modp_points(p):
    F = IL.GF(p)
    r2, r3 = F.sqrt(2), F.sqrt(3)
    ii = F.root_of_unity(4)
    pts = []
    for s2 in (r2, p - r2):
        pts.append(("17+-12sqrt2", (17 + 12 * s2) % p, p - 1))
    for s3 in (r3, p - r3):
        for mu in (ii, p - ii):
            pts.append(("7+-4sqrt3", (7 + 4 * s3) % p, mu))
    return F, pts


def modp_rep(F, qq, mu):
    t = qq * F.inv(2) % F.p
    half = F.inv(2)
    m = [[1, 0, 1, (t - 1) % F.p], [0, 1, 1, t], [0, 0, 1, (t + half) % F.p], [0, 0, 0, 1]]
    n = [[1, 0, 0, 0], [(2 + F.inv(t)) % F.p, 1, 0, 0], [2, 1, 1, 0], [1, 1, 0, 1]]
    return {"m": F.scale(mu, m), "n": F.scale(mu, n)}


def modp_cocycle(F, rep):
    d = rep.d
    D = rep.fox(WORD_R)
    J = F.hstack(D["m"], D["n"])
    Z = F.nullspace(J, 2 * d)
    B = F.vstack(F.sub(rep.M["m"], F.eye(d)), F.sub(rep.M["n"], F.eye(d)))
    BT = F.T(B)
    rkB = F.rank(BT)
    for z in Z:
        if F.rank(BT + [z]) > rkB:
            return {"m": [[x] for x in z[:d]], "n": [[x] for x in z[d:]]}
    return None


def modp_ext(F, rep, c):
    mats = {}
    for g in GENS:
        top = F.hstack(rep.M[g], c[g])
        mats[g] = top + [[0] * rep.d + [1]]
    return IL.Rep(F, list(GENS), mats)


def modp_lam2(F, rep):
    def ext2(S):
        n = len(S)
        pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
        return [[(S[i][k] * S[j][l] - S[i][l] * S[j][k]) % F.p for (k, l) in pairs] for (i, j) in pairs]
    return IL.Rep(F, list(GENS), {g: ext2(rep.M[g]) for g in GENS})


def modp_run():
    rows = []
    for p in PRIMES:
        F, pts = modp_points(p)
        for label, qq, mu in pts:
            A = IL.Rep(F, list(GENS), modp_rep(F, qq, mu))
            assert A.check_relators([WORD_R])
            hA = IL.cohomology_data(A, [WORD_R], WORD_MU, WORD_L)[1]
            As = A.dual()
            hAs = IL.cohomology_data(As, [WORD_R], WORD_MU, WORD_L)[1]
            c = modp_cocycle(F, A)
            cs = modp_cocycle(F, As)
            W1 = modp_ext(F, A, c)
            W1s = modp_ext(F, As, cs)
            assert W1.check_relators([WORD_R]) and W1s.check_relators([WORD_R])
            I1 = IL.index(W1, [WORD_R], WORD_MU, WORD_L)[0]
            I1s = IL.index(W1s, [WORD_R], WORD_MU, WORD_L)[0]
            L1 = IL.index(modp_lam2(F, W1), [WORD_R], WORD_MU, WORD_L)[0]
            L1s = IL.index(modp_lam2(F, W1s), [WORD_R], WORD_MU, WORD_L)[0]
            mu_label = "-1" if mu == p - 1 else ("i" if mu == F.root_of_unity(4) else "-i")
            rows.append({"p": p, "point": label, "q mod p": qq, "mu": mu_label, "h1(A)": hA, "h1(A*)": hAs,
                         "I(W1)": I1, "I(W2)": -I1s, "I(L2W1)": L1, "I(L2W2)": -L1s})
    return rows


# ------------------------------------------------------------------ T3's mechanism: multiplicity of s = mu in Q(q, s)
def multiplicities():
    q, s = sp.symbols("q s")
    Q = -q * s ** 4 + 8 * q * s ** 3 + (q ** 2 - 16 * q + 1) * s ** 2 + 8 * q * s - q
    out = []
    for label, qq, mu, ml in POINTS:
        f = sp.expand(Q.subs(q, qq))
        mult = 0
        g = f
        while sp.simplify(g.subs(s, mu)) == 0:
            mult += 1
            g = sp.diff(g, s)
        out.append({"q": label, "mu": ml, "multiplicity_of_mu_in_Q": mult})
    return out


def main():
    exact = []
    for label, qq, mu, ml in POINTS:
        r = exact_point(qq, mu)
        exact.append({"q": label, "mu": ml, **r})
    return {"exact": exact, "mod_p": modp_run(), "multiplicities": multiplicities()}


if __name__ == "__main__":
    res = main()
    txt = json.dumps(res, indent=1, sort_keys=True, default=str)
    print(txt)
    if "--record" in sys.argv:
        (HERE / "extension_index_run.txt").write_text(txt + "\n", encoding="utf-8")
