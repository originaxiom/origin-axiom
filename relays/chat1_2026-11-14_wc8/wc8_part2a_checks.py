#!/usr/bin/env python3
"""W-C8, part 2a: the Gieseking manifold m000 built from its tick, in the free-cusp and class-index frames, and the
twisted-duality census. Data-free; this seat's own code (no SnapPy; exact arithmetic over two prime fields).

    python3 -I -u wc8_part2a_checks.py

DEFINITIONS
  The tick sigma: a -> ab, b -> a (abelianisation [[1,1],[1,0]] = LP, det -1); sigma^2 abelianises to LR. Level n is the
  mapping torus of sigma^n: G_n = <a, b, t | t a t^-1 = sigma^n(a), t b t^-1 = sigma^n(b)>. Odd n: non-orientable
  (level 1 is m000); even n: orientable (level 2k is level k of m004). The orientation character w: w(t) = (-1)^n,
  w = 1 on the fibre. lambda = [a, b] = a b a^-1 b^-1. The cusp group P = <mu, lambda>, mu = g^-1 t with g in F such that
  sigma^n(lambda) = g lambda^(+-1) g^-1 (a torus for even n, a Klein bottle for odd n).
  Fibre-torsion characters (B1438: trivial on mu, non-trivial on the fibre): chi(a) = z^k1, chi(b) = z^k2 with
  chi o sigma^n = chi, and chi(t) = chi(g) so that chi(mu) = 1; values in F_p with z of order e (e the exponent of
  coker(sigma^n - I)). g_n is found by the recursion g_1 = a, g_(k+1) = sigma(g_k) a, and checked on every level. The record's sector modules (TERMINOLOGY; B1438):
  V(l, alpha) = [[alpha, c beta], [0, beta]], beta = alpha / l, c the class of H^1(G; l) normalised by c(lambda) = 1;
  l, alpha, beta non-trivial. V* is the dual; V* (x) w the dual twisted by w.
  h^i(W) = dim H^i(G; W) by Fox calculus; n(W) = the dimension of the classes whose restriction to P is a coboundary
  (main's interior classes, B1297); h^1_rel(W) = n(W) + h^0(P; W) - h^0(G; W) = dim H^1(M, dM; W).
  The free-cusp frame (GENESIS section 5): a chiral count needs the cusp's rank in H_1(M; Q) below b_1.
  The slope s(chi) = u_chi(mu) with u_chi(lambda) = 1 (B1438).

EXPECTATIONS, written before the run:
  E1  sigma abelianises to [[1,1],[1,0]] with det -1, and sigma^2 to LR; level n is non-orientable exactly for odd n.
  E2  The fibre torsion |coker(sigma^n - I)| at n = 1..8 is 1, 1, 4, 5, 11, 16, 29, 45 (= |(-1)^n - L_n + 1|, Lucas L_n).
  E3  Free-cusp frame: at every level n = 1..8, b_1 = 1 and the cusp's rank in H_1(M; Q) is 1: no free cusp, closed.
  E4  Class-index frame at level 1: there is no fibre-torsion character, so no sector module: the frame is empty on
      m000 itself, as on m004 (level 2).
  E5  Twisted duality (Poincare-Lefschetz with the orientation character): for every sector module V at levels 3..8,
      h^2(V) = h^1_rel(V* (x) w). Control: on the odd levels, h^2(V) = h^1_rel(V*) (w left out) fails for some V.
  E6  Reported, with no expectation of this seat's: for each level, the census of gap(V) = h^1(V) - h^1(V* (x) w) and
      of I_w(V) = n(V) - n(V* (x) w); and whether B1438's firing law n(V(l, alpha)) = [s(alpha) = s(l)] holds on the odd
      levels as on the even ones. Main's expectation (M19), "the gap between h^1(V) and h^1(V* (x) w) follows the tick
      parity w", is compared with the census in the note.
  Both primes must give the same counts (a second method for every rank).
"""
from math import gcd


def say(*a):
    print(*a, flush=True)


# ---------- free group on a=1, b=2, t=3 ----------
def red(w):
    out = []
    for g in w:
        if out and out[-1] == -g:
            out.pop()
        else:
            out.append(g)
    return tuple(out)


def inv(w):
    return tuple(-g for g in reversed(w))


SIG = {1: (1, 2), 2: (1,)}


def apply(aut, w):
    out = []
    for g in w:
        im = aut[abs(g)]
        out.extend(im if g > 0 else inv(im))
    return red(out)


def sig_pow(n):
    f = {1: (1,), 2: (2,)}
    for _ in range(n):
        f = {k: apply(SIG, v) for k, v in f.items()}
    return f


def abel2(w):
    v = [0, 0]
    for g in w:
        if abs(g) <= 2:
            v[abs(g) - 1] += 1 if g > 0 else -1
    return v


LAM = (1, 2, -1, -2)


def conjugator(n):
    """g_n, s_n with sigma^n(lambda) = g_n lambda^s_n g_n^-1: g_1 = a, s_1 = -1, g_(k+1) = sigma(g_k) a, s_(k+1) = -s_k."""
    g, s = (1,), -1
    for _ in range(n - 1):
        g, s = red(apply(SIG, g) + (1,)), -s
    return g, s


# ---------- linear algebra over F_p ----------
def rank_mod(M, p):
    M = [[x % p for x in row] for row in M]
    r, rows, cols = 0, len(M), len(M[0]) if M else 0
    for c in range(cols):
        piv = next((i for i in range(r, rows) if M[i][c]), None)
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        iv = pow(M[r][c], p - 2, p)
        M[r] = [x * iv % p for x in M[r]]
        for i in range(rows):
            if i != r and M[i][c]:
                f = M[i][c]
                M[i] = [(x - f * y) % p for x, y in zip(M[i], M[r])]
        r += 1
    return r


def nullspace_mod(M, p, ncols):
    M = [[x % p for x in row] for row in M]
    rows = len(M)
    piv_cols, r = [], 0
    for c in range(ncols):
        piv = next((i for i in range(r, rows) if M[i][c]), None)
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        iv = pow(M[r][c], p - 2, p)
        M[r] = [x * iv % p for x in M[r]]
        for i in range(rows):
            if i != r and M[i][c]:
                f = M[i][c]
                M[i] = [(x - f * y) % p for x, y in zip(M[i], M[r])]
        piv_cols.append(c)
        r += 1
    free = [c for c in range(ncols) if c not in piv_cols]
    basis = []
    for fc in free:
        v = [0] * ncols
        v[fc] = 1
        for i, pc in enumerate(piv_cols):
            v[pc] = (-M[i][fc]) % p
        basis.append(v)
    return basis


def mm(A, B, p):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) % p for j in range(len(B[0]))] for i in range(len(A))]


def ident(d):
    return [[1 if i == j else 0 for j in range(d)] for i in range(d)]


def madd(A, B, p, s=1):
    return [[(x + s * y) % p for x, y in zip(ra, rb)] for ra, rb in zip(A, B)]


class Rep:
    def __init__(self, mats, p):  # mats: {1: A, 2: B, 3: T}
        self.p, self.m = p, mats
        self.d = len(mats[1])
        self.inv = {k: self._inv(v) for k, v in mats.items()}

    def _inv(self, A):
        d, p = len(A), self.p
        aug = [list(A[i]) + ident(d)[i] for i in range(d)]
        for c in range(d):
            piv = next(i for i in range(c, d) if aug[i][c] % p)
            aug[c], aug[piv] = aug[piv], aug[c]
            iv = pow(aug[c][c], p - 2, p)
            aug[c] = [x * iv % p for x in aug[c]]
            for i in range(d):
                if i != c and aug[i][c] % p:
                    f = aug[i][c]
                    aug[i] = [(x - f * y) % p for x, y in zip(aug[i], aug[c])]
        return [row[d:] for row in aug]

    def of(self, w):
        M = ident(self.d)
        for g in w:
            M = mm(M, self.m[g] if g > 0 else self.inv[-g], self.p)
        return M

    def fox(self, w, gen):
        """rho applied to the Fox derivative d w / d gen."""
        p, d = self.p, self.d
        S = [[0] * d for _ in range(d)]
        pref = ident(d)
        for g in w:
            if abs(g) == gen:
                if g > 0:
                    S = madd(S, pref, p)
                else:
                    S = madd(S, mm(pref, self.inv[-g], p), p, -1)
            pref = mm(pref, self.m[g] if g > 0 else self.inv[-g], p)
        return S

    def cocycle_value(self, z, w):
        """z: {1: vec, 2: vec, 3: vec}; value on word w by the cocycle rule."""
        p, d = self.p, self.d
        val = [0] * d
        pref = ident(d)
        for g in w:
            if g > 0:
                zg = z[g]
            else:
                ginv = self.inv[-g]
                zg = [(-x) % p for x in mv(ginv, z[-g], p)]
            val = [(x + y) % p for x, y in zip(val, mv(pref, zg, p))]
            pref = mm(pref, self.m[g] if g > 0 else self.inv[-g], p)
        return val


def mv(A, v, p):
    return [sum(a * b for a, b in zip(row, v)) % p for row in A]


def cohomology(rep, rels, mu, lam):
    p, d = rep.p, rep.d
    # Fox matrix: rows = relators x d, cols = generators x d
    F = []
    for r in rels:
        blocks = [rep.fox(r, g) for g in (1, 2, 3)]
        for i in range(d):
            F.append([blocks[g][i][j] for g in range(3) for j in range(d)])
    rkF = rank_mod(F, p)
    Dm = []  # coboundary map V -> V^3
    for g in (1, 2, 3):
        A = madd(rep.m[g], ident(d), p, -1)
        Dm.extend(A)
    rkD = rank_mod(Dm, p)
    h0 = d - rkD
    z1 = 3 * d - rkF
    h1 = z1 - rkD
    h2 = 2 * d - rkF
    # interior classes
    Z = nullspace_mod(F, p, 3 * d)
    Mmu, Mlam = rep.of(mu), rep.of(lam)
    Cmu, Clam = madd(Mmu, ident(d), p, -1), madd(Mlam, ident(d), p, -1)
    # vectors (z(mu), z(lam)) for basis of Z, and P-coboundaries
    imgs = []
    for zb in Z:
        z = {g + 1: zb[g * d:(g + 1) * d] for g in range(3)}
        imgs.append(rep.cocycle_value(z, mu) + rep.cocycle_value(z, lam))
    Pcob = [[Cmu[i][j] for i in range(d)] + [Clam[i][j] for i in range(d)] for j in range(d)]
    # dim of {z in Z : img(z) in span(Pcob)} = dim Z - (rank(imgs + Pcob) - rank(Pcob))
    rk_all = rank_mod(imgs + Pcob, p) if imgs else rank_mod(Pcob, p)
    rk_P = rank_mod(Pcob, p)
    interior = len(Z) - (rk_all - rk_P)
    n = interior - rkD
    h0P = d - rank_mod(Cmu + Clam, p)
    return dict(h0=h0, h1=h1, h2=h2, n=n, h0P=h0P, rel1=n + h0P - h0)


def find_prime(mod, start):
    k = start
    while True:
        q = mod * k + 1
        if all(q % r for r in range(2, int(q ** 0.5) + 1)):
            return q
        k += 1


EXP = {}
results = {}
LUC = [2, 1, 3, 4, 7, 11, 18, 29, 47]
say("E1 sigma abelianises to", [abel2(SIG[1]), abel2(SIG[2])], "(columns); sigma^2:",
    [abel2(sig_pow(2)[1]), abel2(sig_pow(2)[2])])

for n in range(1, 9):
    f = sig_pow(n)
    A = [[abel2(f[1])[0], abel2(f[2])[0]], [abel2(f[1])[1], abel2(f[2])[1]]]
    det = A[0][0] * A[1][1] - A[0][1] * A[1][0]
    tor = abs((A[0][0] - 1) * (A[1][1] - 1) - A[0][1] * A[1][0])
    # Smith form of A - I for the exponent
    g1 = gcd(gcd(A[0][0] - 1, A[0][1]), gcd(A[1][0], A[1][1] - 1))
    expo = tor // g1 if g1 else 0
    want = abs((-1) ** n - LUC[n] + 1)
    g, s = conjugator(n)
    lam_s = LAM if s == 1 else inv(LAM)
    ok_conj = red(g + lam_s + inv(g)) == apply(f, LAM) and s == det
    mu = red(inv(g) + (3,))
    # free-cusp frame: b1 = 1 + dim ker(A - I) over Q; H1(M; Q) is spanned by t when A - I is invertible.
    # The cusp's rank in H1(M; Q): mu has t-exponent 1, lambda has exponent 0 in every generator.
    b1 = 1 + (2 - (2 if tor != 0 else (1 if any(x for r in A for x in r) else 0)))
    t_exp = sum(1 if x == 3 else -1 if x == -3 else 0 for x in mu)
    cusp_rank = (1 if t_exp != 0 else 0) + (0 if abel2(LAM) == [0, 0] else 1)
    say("level", n, "det", det, "orientable", det == 1, "| torsion", tor, "(expected", want, ") exponent", expo,
        "| conjugator checked", ok_conj, "length", len(g), "| b1", b1, "cusp rank", cusp_rank)
    EXP[n] = dict(f=f, A=A, det=det, tor=tor, expo=expo, mu=mu, g=g, want=want, b1=b1, cusp_rank=cusp_rank,
                  ok_conj=ok_conj)

e1 = EXP[1]["det"] == -1 and EXP[2]["A"] == [[2, 1], [1, 1]] and all((EXP[n]["det"] == 1) == (n % 2 == 0) for n in EXP)
e2 = all(EXP[n]["tor"] == EXP[n]["want"] for n in EXP) and [EXP[n]["tor"] for n in EXP] == [1, 1, 4, 5, 11, 16, 29, 45]
e3 = all(EXP[n]["b1"] == 1 and EXP[n]["cusp_rank"] == 1 and EXP[n]["ok_conj"] for n in EXP)
say("E1 holds:", e1, "; E2 holds:", e2, "; E3 holds:", e3)


def characters(n, p, z, e):
    A = EXP[n]["A"]
    chars = []
    for k1 in range(e):
        for k2 in range(e):
            if (k1, k2) == (0, 0):
                continue
            # chi o sigma^n = chi: k . (A col) = k . e_i
            if ((k1 * A[0][0] + k2 * A[1][0] - k1) % e == 0) and ((k1 * A[0][1] + k2 * A[1][1] - k2) % e == 0):
                ga, gb = abel2(EXP[n]["g"])
                ct = pow(z, (k1 * ga + k2 * gb) % e, p)  # chi(t) = chi(g), so chi(mu) = 1
                chars.append((pow(z, k1, p), pow(z, k2, p), ct))
    return chars


def run_level(n, p):
    e, f, mu = EXP[n]["expo"], EXP[n]["f"], EXP[n]["mu"]
    rels = [red((3, 1, -3) + inv(f[1])), red((3, 2, -3) + inv(f[2]))]
    if e <= 1:
        return dict(nchar=0, mods=[])
    gen = next(x for x in range(2, p) if pow(x, (p - 1) // 2, p) != 1 and all(pow(x, (p - 1) // q, p) != 1
                                                                                 for q in prime_factors(p - 1)))
    z = pow(gen, (p - 1) // e, p)
    chars = characters(n, p, z, e)
    w = (p - 1) if n % 2 else 1  # w(t) = -1 on odd levels
    one_d = {}
    slopes = {}
    for ch in chars:
        rep = Rep({1: [[ch[0]]], 2: [[ch[1]]], 3: [[ch[2]]]}, p)
        F = []
        for r in rels:
            F.append([rep.fox(r, g)[0][0] for g in (1, 2, 3)])
        Zb = nullspace_mod(F, p, 3)
        # pick a cocycle not a coboundary, normalised on lambda
        cand = None
        for zb in Zb:
            zz = {1: [zb[0]], 2: [zb[1]], 3: [zb[2]]}
            lv = rep.cocycle_value(zz, LAM)[0]
            if lv % p:
                il = pow(lv, p - 2, p)
                cand = {k: [v[0] * il % p] for k, v in zz.items()}
                break
        one_d[ch] = cand
        if cand is not None:
            slopes[ch] = rep.cocycle_value(cand, mu)[0]
    mods = []
    for l in chars:
        c = one_d[l]
        if c is None:
            continue
        for al in chars:
            be = tuple(al[i] * pow(l[i], p - 2, p) % p for i in range(3))
            if be[:2] == (1, 1):
                continue
            mats = {gi: [[al[gi - 1], c[gi][0] * be[gi - 1] % p], [0, be[gi - 1]]] for gi in (1, 2, 3)}
            V = Rep(mats, p)
            dual = {gi: [list(r) for r in zip(*V.inv[gi])] for gi in (1, 2, 3)}
            Vd = Rep(dual, p)
            Vdw = Rep({1: dual[1], 2: dual[2], 3: [[x * w % p for x in r] for r in dual[3]]}, p)
            cV, cVd, cVdw = cohomology(V, rels, mu, LAM), cohomology(Vd, rels, mu, LAM), cohomology(Vdw, rels, mu, LAM)
            fire = int(slopes.get(al) is not None and slopes.get(l) is not None and slopes[al] == slopes[l])
            mods.append(dict(l=l, al=al, V=cV, Vd=cVd, Vdw=cVdw, fire=fire))
    return dict(nchar=len(chars), mods=mods)


def prime_factors(m):
    fs, d = set(), 2
    while d * d <= m:
        while m % d == 0:
            fs.add(d)
            m //= d
        d += 1
    if m > 1:
        fs.add(m)
    return fs


MOD = 2 * 16 * 9 * 5 * 11 * 29
P1, P2 = find_prime(MOD, 1), find_prime(MOD, 50)
say("primes:", P1, P2)
summary = {}
for p in (P1, P2):
    for n in range(1, 9):
        r = run_level(n, p)
        mods = r["mods"]
        euler = True  # h0 - h1 + h2 = 0 is an identity of the Fox computation here, not a check
        dual_tw = all(m["V"]["h2"] == m["Vdw"]["rel1"] for m in mods)
        dual_plain = all(m["V"]["h2"] == m["Vd"]["rel1"] for m in mods)
        gaps = {}
        for m in mods:
            key = (m["V"]["h1"] - m["Vdw"]["h1"], m["V"]["n"] - m["Vdw"]["n"])
            gaps[key] = gaps.get(key, 0) + 1
        firing_law = all(m["V"]["n"] == m["fire"] for m in mods)
        summary[(p, n)] = (r["nchar"], len(mods), euler, dual_tw, dual_plain, tuple(sorted(gaps.items())), firing_law)
        say("p", p, "level", n, "| characters", r["nchar"], "| sector modules", len(mods), "| Euler", euler,
            "| h2(V) = h1_rel(V* w):", dual_tw, "| h2(V) = h1_rel(V*):", dual_plain,
            "| census (h1 gap, n gap): count", sorted(gaps.items()), "| n(V) = [s(alpha) = s(l)] on all:", firing_law)

same = all(summary[(P1, n)] == summary[(P2, n)] for n in range(1, 9))
e4 = summary[(P1, 1)][0] == 0 and summary[(P1, 2)][0] == 0
e5 = all(summary[(P1, n)][3] for n in range(3, 9))
ctrl5 = any(not summary[(P1, n)][4] for n in (3, 5, 7))
say("E4 holds:", e4)
say("E5 holds:", e5, "; control (w left out on odd levels) fails somewhere:", ctrl5)
say("both primes give the same counts:", same)
