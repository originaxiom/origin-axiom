#!/usr/bin/env python3
"""B1522 -- route R (Reidemeister-Schreier): the same census with no fibre model.

pi = <m, n | mnMNmNMnmN> (Ballas' presentation; B1521 C1 proves it is SnapPy's pi_1(m004)).  pi_n = ker(pi -> Z/n), m, n -> 1,
with the Schreier transversal t_k = m^k (0 <= k < n).  The generators gamma_{k,g} = t_k g t_{k+1 mod n}^-1; gamma_{k,m} is trivial
for k < n - 1 and gamma_{n-1,m} = m^n = z.  H_1(pi_n) by own Smith normal form with unimodular transforms (no library SNF).

The four symmetries are given only as words in m and n (B1512's table):
    iota : m -> mnM,  n -> mNmnM          (the fibre's hyperelliptic involution)
    eps  : m -> mNM,  n -> mnMNM          (the strong inversion)
    alpha: m -> mnM,  n -> nmNMnnM        (the amphichiral map)
    tau  : m -> m,    n -> mnM            (conjugation by m: the deck transformation on pi_n)
Each is checked here to send the relator to a cyclic conjugate of R^+-1 in the free group.  Its action on H_1(pi_n) is computed by
substituting into the transversal words of the generators and rewriting.  The dualising flags (eps, alpha dualise rho_q; iota, tau
do not) are B1512's and are re-derived in controls.py at a rational q with exact intertwiners.

The characters of H_1(pi_n) = Z + T_n are read in the SNF basis.  The free coordinate's sign under a symmetry is its sigma.
A character of route F, (a, b) with nu_F(x) = zeta_N^a, nu_F(y) = zeta_N^b, lam = nu(z), is carried to route R by its values on the
generators: gamma_{k,n} = phi^k(x) for k < n - 1 (x = n m^-1), and gamma_{n-1,n} = phi^(n-1)(x) z."""
from fractions import Fraction

R_WORD = "mnMNmNMnmN"
SYMS = {
    "iota": ({"m": "mnM", "n": "mNmnM"}, 0),
    "eps": ({"m": "mNM", "n": "mnMNM"}, 1),
    "alpha": ({"m": "mnM", "n": "nmNMnnM"}, 1),
    "tau": ({"m": "m", "n": "mnM"}, 0),
}


# ------------------------------------------------------------------ free-group words
def inv(w):
    return "".join(c.swapcase() for c in reversed(w))


def red(w):
    out = []
    for c in w:
        if out and out[-1] == c.swapcase():
            out.pop()
        else:
            out.append(c)
    return "".join(out)


def sub(w, im):
    return red("".join(im[c] if c.islower() else inv(im[c.lower()]) for c in w))


def cyc(w):
    w = red(w)
    while len(w) >= 2 and w[0] == w[-1].swapcase():
        w = w[1:-1]
    return w


def is_automorphism_of_R(im):
    """the image of R is a cyclic conjugate of R or R^-1 (a sufficient condition, with invertibility checked separately)"""
    c = cyc(sub(R_WORD, im))
    rots = {R_WORD[i:] + R_WORD[:i] for i in range(len(R_WORD))}
    rinv = inv(R_WORD)
    rots |= {rinv[i:] + rinv[:i] for i in range(len(rinv))}
    return c in rots


# ------------------------------------------------------------------ Reidemeister-Schreier
def exp_sum(w):
    return sum(1 if c.islower() else -1 for c in w)


def gen_index(n, k, g):
    """column index of gamma_{k,g}: m-generators first (k = 0..n-1), then n-generators"""
    return k if g == "m" else n + k


def rewrite_abelian(w, n, start=0):
    """the abelianised Reidemeister-Schreier rewrite of a word read from coset `start`; returns (vector, end coset)"""
    vec = [0] * (2 * n)
    k = start % n
    for c in w:
        g = c.lower()
        if c.islower():
            vec[gen_index(n, k, g)] += 1
            k = (k + 1) % n
        else:
            k = (k - 1) % n
            vec[gen_index(n, k, g)] -= 1
    return vec, k


def transversal_word(n, k, g):
    """t_k g t_{k+1}^-1 as a word in m, n"""
    return red("m" * k + g + "M" * ((k + 1) % n))


def relation_rows(n):
    rows = []
    for k in range(n):
        v, end = rewrite_abelian(R_WORD, n, k)
        assert end == k
        rows.append(v)
    # the trivial generators gamma_{k,m}, k < n - 1, are identities of the transversal
    for k in range(n - 1):
        e = [0] * (2 * n)
        e[gen_index(n, k, "m")] = 1
        rows.append(e)
    return rows


# ------------------------------------------------------------------ Smith normal form with transforms (own code)
def snf(A):
    """A (r x c integer matrix) -> (U, D, V) with U A V = D diagonal (U, V unimodular). Returns lists of lists."""
    r, c = len(A), len(A[0])
    D = [row[:] for row in A]
    U = [[int(i == j) for j in range(r)] for i in range(r)]
    V = [[int(i == j) for j in range(c)] for i in range(c)]

    def swap_rows(M_, i, j):
        M_[i], M_[j] = M_[j], M_[i]

    def swap_cols(M_, i, j):
        for row in M_:
            row[i], row[j] = row[j], row[i]
    t = 0
    while t < min(r, c):
        # pivot: smallest nonzero |entry| in the submatrix
        best = None
        for i in range(t, r):
            for j in range(t, c):
                if D[i][j] != 0 and (best is None or abs(D[i][j]) < abs(D[best[0]][best[1]])):
                    best = (i, j)
        if best is None:
            break
        i, j = best
        swap_rows(D, t, i), swap_rows(U, t, i)
        swap_cols(D, t, j), swap_cols(V, t, j)
        done = False
        while not done:
            done = True
            for i in range(t + 1, r):
                if D[i][t] != 0:
                    q = D[i][t] // D[t][t]
                    D[i] = [a - q * b for a, b in zip(D[i], D[t])]
                    U[i] = [a - q * b for a, b in zip(U[i], U[t])]
                    if D[i][t] != 0:
                        swap_rows(D, t, i), swap_rows(U, t, i)
                        done = False
            for j in range(t + 1, c):
                if D[t][j] != 0:
                    q = D[t][j] // D[t][t]
                    for row in D:
                        row[j] -= q * row[t]
                    for row in V:
                        row[j] -= q * row[t]
                    if D[t][j] != 0:
                        swap_cols(D, t, j), swap_cols(V, t, j)
                        done = False
            if done:
                # divisibility: the pivot must divide every remaining entry
                for i in range(t + 1, r):
                    for j in range(t + 1, c):
                        if D[i][j] % D[t][t] != 0:
                            D[t] = [a + b for a, b in zip(D[t], D[i])]
                            U[t] = [a + b for a, b in zip(U[t], U[i])]
                            done = False
                            break
                    if not done:
                        break
        if D[t][t] < 0:
            D[t] = [-a for a in D[t]]
            U[t] = [-a for a in U[t]]
        t += 1
    return U, D, V


def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]


def inverse_unimodular(V):
    """exact inverse of an integer unimodular matrix (Fraction Gaussian elimination)"""
    n = len(V)
    Mx = [[Fraction(x) for x in row] + [Fraction(int(i == j)) for j in range(n)] for i, row in enumerate(V)]
    for col in range(n):
        p = next(r for r in range(col, n) if Mx[r][col] != 0)
        Mx[col], Mx[p] = Mx[p], Mx[col]
        pv = Mx[col][col]
        Mx[col] = [x / pv for x in Mx[col]]
        for r in range(n):
            if r != col and Mx[r][col] != 0:
                f = Mx[r][col]
                Mx[r] = [a - f * b for a, b in zip(Mx[r], Mx[col])]
    out = [[x for x in row[n:]] for row in Mx]
    assert all(x.denominator == 1 for row in out for x in row)
    return [[int(x) for x in row] for row in out]


class Level:
    """H_1(pi_n) = Z^free + sum Z/d_i in the SNF basis; coordinates of a generator vector v are (V^-1 v)."""

    def __init__(self, n):
        self.n = n
        rows = relation_rows(n)
        U, D, V = snf(rows)
        self.D = D
        self.V = V
        self.Vinv = inverse_unimodular(V)
        c = 2 * n
        diag = [D[i][i] if i < len(D) else 0 for i in range(c)]
        # SNF coordinates: diag entry 1 -> killed; d > 1 -> Z/d; 0 -> free
        self.coords = [(i, diag[i]) for i in range(c) if diag[i] != 1]
        self.free = [i for i, d in self.coords if d == 0]
        self.tors = [(i, d) for i, d in self.coords if d > 1]
        assert len(self.free) == 1, (n, self.free)
        self.order = 1
        for _, d in self.tors:
            self.order *= d

    def coordinates(self, vec):
        """generator (row) vector x -> (free coordinate, torsion coordinates mod d). The relations are rows and U Rel V = D,
        so the coordinates are y = x V (row convention), and the i-th basis element of H_1 is the row i of V^-1."""
        y = [sum(vec[j] * self.V[j][i] for j in range(len(vec))) for i in range(len(vec))]
        f = y[self.free[0]]
        t = tuple(y[i] % d for i, d in self.tors)
        return f, t

    def action(self, sym):
        """the induced map of a symmetry on H_1, in the split H_1 = Z z + T_n: (sigma, B, c) with beta(z) = sigma z + c and
        B[i] = the torsion coordinates of beta(e_i) for the torsion basis e_i. Nothing about c is assumed: it is computed."""
        im, _ = SYMS[sym]
        n = self.n
        imgs = []
        for g in ("m", "n"):
            for k in range(n):
                w = sub(transversal_word(n, k, g), im)
                v, end = rewrite_abelian(w, n, 0)
                assert end == 0, (sym, g, k)
                imgs.append(v)

        def apply_vec(vec):
            out = [0] * (2 * n)
            for j, coef in enumerate(vec):
                if coef:
                    out = [a + coef * b for a, b in zip(out, imgs[j])]
            return out
        z = [0] * (2 * n)
        z[gen_index(n, n - 1, "m")] = 1
        fz, tz = self.coordinates(z)
        assert fz in (1, -1), ("z must generate the free part", fz)
        fbz, tbz = self.coordinates(apply_vec(z))
        assert fbz in (fz, -fz), (sym, fbz, fz)
        sigma = fbz // fz
        ds = [d for _, d in self.tors]
        c = tuple((tbz[i] - sigma * tz[i]) % ds[i] for i in range(len(ds)))
        basis = {i: list(self.Vinv[i]) for i, _ in self.tors}
        B = []
        for i, _ in self.tors:
            f, t = self.coordinates(apply_vec(basis[i]))
            assert f == 0, (sym, "torsion maps into the free part")
            B.append(t)
        return sigma, B, c


def characters(level):
    """all characters of the torsion part, as tuples (c_1, ..., c_r) with c_i mod d_i (chi(e_i) = exp(2 pi i c_i / d_i))"""
    import itertools
    ds = [d for _, d in level.tors]
    return list(itertools.product(*[range(d) for d in ds])), ds


def apply_el(B, t, ds):
    """the image of a torsion element t = sum t_i e_i under the map with B[i] = image of e_i"""
    out = [0] * len(ds)
    for i, ti in enumerate(t):
        if ti:
            out = [(a + ti * b) % d for a, b, d in zip(out, B[i], ds)]
    return tuple(out)


def char_value(chi, t, ds, L):
    """chi(t) as an exponent mod L (chi(e_j) = exp(2 pi i chi_j / d_j))"""
    return sum(chi[j] * (L // ds[j]) * t[j] for j in range(len(ds))) % L


def pull(chi, B, ds, L):
    """chi o beta on the torsion basis, in the same coordinates"""
    out = []
    for i, d in enumerate(ds):
        e = char_value(chi, B[i], ds, L)
        assert (e * d) % L == 0
        out.append((e * d // L) % d)
    return tuple(out)


def census(n):
    """flags per torsion character from the group generated by the four symmetries, with the cross term c kept:
    an element is (B, sigma, d, c) with beta(z) = sigma z + c.  Composition beta1 beta2: B = B1 o B2,
    sigma = sigma1 sigma2, d = d1 + d2, c = sigma2 c1 + B1(c2).
    A count-odd element (d = 1) fixes (chi, lam) without conjugation iff chi o B = -chi and lam^-sigma chi(c)^-1 = lam;
    with complex conjugation of the twist (count-even) iff chi o B = chi and lam^sigma chi(c) = lam (unitary lam).
    E (generic or real lam): some element with sigma = -1, chi(c) = 1 and chi o B = -chi (or, with conjugation, = chi).
    A (unitary lam, with conjugation): some element with sigma = +1, chi(c) = 1 and chi o B = chi."""
    from math import lcm
    lv = Level(n)
    chars, ds = characters(lv)
    L = 1
    for d in ds:
        L = lcm(L, d)
    k = len(ds)
    ident_B = [tuple(int(i == j) for j in range(k)) for i in range(k)]
    gens = []
    for s, (_, d) in SYMS.items():
        sigma, B, c = lv.action(s)
        gens.append((tuple(tuple(r) for r in B), sigma, d, c))

    def compose(e1, e2):
        B1, s1, d1, c1 = e1
        B2, s2, d2, c2 = e2
        B = tuple(apply_el(B1, B2[i], ds) for i in range(k))
        c = tuple((s2 * a + b) % dd for a, b, dd in zip(c1, apply_el(B1, c2, ds), ds))
        return (B, s1 * s2, (d1 + d2) % 2, c)
    ident = (tuple(ident_B), 1, 0, tuple(0 for _ in ds))
    elems = {ident}
    frontier = [ident]
    while frontier:
        nxt = []
        for e in frontier:
            for g in gens:
                el = compose(e, g)
                if el not in elems:
                    elems.add(el)
                    nxt.append(el)
        frontier = nxt
    flags = {}
    neg = lambda chi: tuple((-x) % d for x, d in zip(chi, ds))
    for chi in chars:
        E = A = False
        for (B, s, d, c) in elems:
            if d != 1 or char_value(chi, c, ds, L) != 0:
                continue
            p = pull(chi, B, ds, L)
            if s == -1 and (p == neg(chi) or p == chi):
                E = True
            if s == 1 and p == chi:
                A = True
            if E and A:
                break
        flags[chi] = {"E": E, "A": A}
    nonzero_c = sum(1 for (B, s, d, c) in elems if any(c))
    return {"n": n, "order": lv.order, "invariant_factors": ds, "group_order": len(elems), "flags": flags,
            "elements_with_nonzero_c": nonzero_c, "level": lv, "gens": gens}


# ------------------------------------------------------------------ structure only, and the bridge to route F
def lcm_all(ds):
    from math import lcm
    L = 1
    for d in ds:
        L = lcm(L, d)
    return L


def census_structure(n):
    """the generated group's order on the torsion characters (with sigma and d), without reading any flag"""
    lv = Level(n)
    chars, ds = characters(lv)
    k = len(ds)
    gens = []
    for s, (_, d) in SYMS.items():
        sigma, B, c = lv.action(s)
        gens.append((tuple(tuple(r) for r in B), sigma, d, c))
    index = {c: i for i, c in enumerate(chars)}
    L = lcm_all(ds)

    def perm(B):
        return tuple(index[pull(ch, B, ds, L)] for ch in chars)
    ident = (tuple(tuple(int(i == j) for j in range(k)) for i in range(k)), 1, 0, tuple(0 for _ in ds))
    seen = {ident}
    frontier = [ident]
    while frontier:
        nxt = []
        for e in frontier:
            for g in gens:
                B1, s1, d1, c1 = e
                B2, s2, d2, c2 = g
                B = tuple(apply_el(B1, B2[i], ds) for i in range(k))
                c = tuple((s2 * a + b) % dd for a, b, dd in zip(c1, apply_el(B1, c2, ds), ds))
                el = (B, s1 * s2, (d1 + d2) % 2, c)
                if el not in seen:
                    seen.add(el)
                    nxt.append(el)
        frontier = nxt
    acting = {(perm(B), s, d) for (B, s, d, c) in seen}
    return {"n": n, "group_order": len(acting), "elements_on_H1": len(seen)}


def chi_from_fibre(lv, ab, N):
    """route F's character (a, b) mod N (lam = 1) restricted to route R's torsion basis: chi_j = value on e_j, as c_j mod d_j"""
    n = lv.n
    a, b = ab
    PHI = ((0, -1), (1, 3))
    vals = [0] * (2 * n)   # exponents over N on the generators gamma
    row = (a % N, b % N)
    for k in range(n):
        vals[gen_index(n, k, "n")] = row[0] % N           # value on phi^k(x) is the x-coordinate of (a, b) Phi^k
        row = ((row[0] * PHI[0][0] + row[1] * PHI[1][0]) % N, (row[0] * PHI[0][1] + row[1] * PHI[1][1]) % N)
    out = []
    for i, d in lv.tors:
        e = sum(lv.Vinv[i][g] * vals[g] for g in range(2 * n)) % N
        assert (e * d) % N == 0, ("not a character of the torsion", ab, i, d)
        out.append((e * d // N) % d)
    return tuple(out)
