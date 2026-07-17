"""Cell 9 (B666 leads campaign) — exact arithmetic in L = Q(s,i),
s^4 = 8 s^2 + 16, i^2 = -1  ([L:Q] = 8; zeta_8 in L).

Element representation: tuple of 8 Fractions, coordinates in the basis
  (1, s, s^2, s^3, i, i s, i s^2, i s^3)
index = j + 4*k  for s^j i^k.
"""
from fractions import Fraction

ZERO8 = tuple([Fraction(0)] * 8)
ONE8 = tuple([Fraction(1)] + [Fraction(0)] * 7)


def Lel(re4=None, im4=None):
    """Build an L element from rational coordinate lists (len-4 each) in
    basis (1, s, s^2, s^3) for the real-tag and i*(...) for the im-tag."""
    v = [Fraction(0)] * 8
    if re4 is not None:
        for j, c in enumerate(re4):
            v[j] = Fraction(c)
    if im4 is not None:
        for j, c in enumerate(im4):
            v[4 + j] = Fraction(c)
    return tuple(v)


def ladd(a, b):
    return tuple(x + y for x, y in zip(a, b))


def lsub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def lneg(a):
    return tuple(-x for x in a)


def lscal(q, a):
    q = Fraction(q)
    return tuple(q * x for x in a)


def lmul(a, b):
    """Multiply in L: polynomial mult in s (deg<8 with s^4=8s^2+16),
    i-grading mod 2 with i^2=-1."""
    # split into i-parts: a = A0 + i A1 (each a poly in s of deg<4)
    A0, A1 = a[:4], a[4:]
    B0, B1 = b[:4], b[4:]
    # complex-style: (A0+iA1)(B0+iB1) = (A0B0 - A1B1) + i(A0B1 + A1B0)
    def pmul(P, Q):
        r = [Fraction(0)] * 7
        for j, pj in enumerate(P):
            if pj:
                for k, qk in enumerate(Q):
                    if qk:
                        r[j + k] += pj * qk
        # reduce s^4 = 8 s^2 + 16, s^5 = 8 s^3 + 16 s, s^6 = 64 s^2 + 128 + 16 s^2? do iteratively
        for deg in (6, 5, 4):
            c = r[deg]
            if c:
                r[deg] = Fraction(0)
                r[deg - 2] += 8 * c
                r[deg - 4] += 16 * c
        return r[:4]

    def psub(P, Q):
        return [x - y for x, y in zip(P, Q)]

    def padd(P, Q):
        return [x + y for x, y in zip(P, Q)]

    re = psub(pmul(A0, B0), pmul(A1, B1))
    im = padd(pmul(A0, B1), pmul(A1, B0))
    return tuple(re + im)


def linv(a):
    """Inverse in L via linear algebra over Q: solve a*x = 1."""
    # build multiplication matrix M: columns = a * basis_e
    cols = []
    for idx in range(8):
        e = [Fraction(0)] * 8
        e[idx] = Fraction(1)
        cols.append(lmul(a, tuple(e)))
    # solve sum_idx x_idx * cols[idx] = ONE8  -> 8x8 system
    M = [[cols[j][i] for j in range(8)] for i in range(8)]
    rhs = [Fraction(1) if i == 0 else Fraction(0) for i in range(8)]
    n = 8
    # gaussian elimination
    for col in range(n):
        piv = None
        for r in range(col, n):
            if M[r][col] != 0:
                piv = r
                break
        assert piv is not None, "singular (a=0?)"
        M[col], M[piv] = M[piv], M[col]
        rhs[col], rhs[piv] = rhs[piv], rhs[col]
        pv = M[col][col]
        M[col] = [x / pv for x in M[col]]
        rhs[col] = rhs[col] / pv
        for r in range(n):
            if r != col and M[r][col] != 0:
                f = M[r][col]
                M[r] = [x - f * y for x, y in zip(M[r], M[col])]
                rhs[r] = rhs[r] - f * rhs[col]
    return tuple(rhs)


# ---- 2x2 matrices over L ----

def mmul(A, B):
    return [[ladd(lmul(A[0][0], B[0][0]), lmul(A[0][1], B[1][0])),
             ladd(lmul(A[0][0], B[0][1]), lmul(A[0][1], B[1][1]))],
            [ladd(lmul(A[1][0], B[0][0]), lmul(A[1][1], B[1][0])),
             ladd(lmul(A[1][0], B[0][1]), lmul(A[1][1], B[1][1]))]]


def mdet(A):
    return lsub(lmul(A[0][0], A[1][1]), lmul(A[0][1], A[1][0]))


def minv2(A):
    d = mdet(A)
    di = linv(d)
    return [[lmul(di, A[1][1]), lneg(lmul(di, A[0][1]))],
            [lneg(lmul(di, A[1][0])), lmul(di, A[0][0])]]


def meye():
    return [[ONE8, ZERO8], [ZERO8, ONE8]]


def word_matrix(word, gens):
    """gens: dict lowercase letter -> 2x2 L-matrix; uppercase = inverse."""
    M = meye()
    for ch in word:
        g = gens[ch.lower()]
        if ch.isupper():
            g = minv2(g)
        M = mmul(M, g)
    return M


def load_silver_gens(path):
    import json
    d = json.load(open(path))
    gens = {}
    for g in 'abc':
        M = [[None, None], [None, None]]
        for r in range(2):
            for c in range(2):
                re4, im4 = d[f"{g}{r}{c}"]
                M[r][c] = Lel([Fraction(x) for x in re4],
                              [Fraction(x) for x in im4])
        gens[g] = M
    return gens


if __name__ == '__main__':
    gens = load_silver_gens(
        '/Users/dri/origin-axiom/frontier/B649_silver_holonomy/entries_L.json')
    # verify dets
    for g in 'abc':
        assert mdet(gens[g]) == ONE8, f"det({g}) != 1"
    print("dets: a, b, c all exactly 1 in L")
    # verify relators aBAbcc, aaCbcB  == identity
    for rel in ['aBAbcc', 'aaCbcB']:
        M = word_matrix(rel, gens)
        ok = (M[0][0] == ONE8 and M[1][1] == ONE8 and M[0][1] == ZERO8
              and M[1][0] == ZERO8)
        print(f"relator {rel}: exactly I in SL2(L): {ok}")
        assert ok
    # traces (cross-check against B649 S1-G2)
    tra = ladd(gens['a'][0][0], gens['a'][1][1])
    trb = ladd(gens['b'][0][0], gens['b'][1][1])
    print("tr(a) coords (1,s,s^2,s^3, i,is,is^2,is^3):", [str(x) for x in tra])
    print("tr(b) coords:", [str(x) for x in trb])
    ac = mmul(gens['a'], gens['c'])
    trac = ladd(ac[0][0], ac[1][1])
    print("tr(ac) coords:", [str(x) for x in trac])
    abc = mmul(ac, gens['b'])  # careful: ac*b vs a*b*c -- compute a*b*c properly
    ab = mmul(gens['a'], gens['b'])
    abc = mmul(ab, gens['c'])
    trabc = ladd(abc[0][0], abc[1][1])
    print("tr(abc) coords:", [str(x) for x in trabc])
    print("VERIFICATION OF THE EXACT SILVER REP: PASS")
