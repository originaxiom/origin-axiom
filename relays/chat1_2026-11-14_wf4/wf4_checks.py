#!/usr/bin/env python3
"""W-F4: the non-orientable closing, and the odd tick's matter as the double cover's.

Data-free; this seat's own code. The helpers (free group, Fox calculus over F_p, the cohomology routine) are taken by
text from W-C8 part 2a's sealed script (definitions only, up to its census), which is not re-run.

    python3 -I -u wf4_checks.py

DEFINITIONS
  The metallic tick tau_m: a -> a^m b, b -> a (m = 1 golden, m = 3 bronze). Level n: G_n = <a, b, t | t a t^-1 =
  tau_m^n(a), t b t^-1 = tau_m^n(b)>; odd n is non-orientable, w(t) = (-1)^n, w = 1 on the fibre. lambda = [a, b].
  The cusp conjugator g_n (g_1 = a^m, g_(k+1) = tau_m(g_k) a^m), mu_n = g_n^-1 t. The orientation double cover of an odd
  level n is level 2n, embedded as <a, b, T = t^2>; by the recursion g_2n = tau_m^n(g_n) g_n, so mu_2n = mu_n^2 exactly.
  Characters: chi(a), chi(b) on the fibre torsion coker(A_n - I) (A_n the abelianisation of tau_m^n), chi(t) any 2e-th
  root of unity (e the exponent of the fibre torsion, at least 1). pi* chi = (chi(a), chi(b), chi(t)^2) on level 2n.
  The deck acts on level-2n characters by psi^t(f) = psi(tau_m^n(f)) on the fibre, psi^t(T) = psi(T).
  Ind psi (on G_n): a -> diag(psi(a), psi(tau^n a)), b -> diag(psi(b), psi(tau^n b)), t -> [[0, psi(T)], [1, 0]].
  The record's data at an even level: a fibre-non-trivial psi with psi(mu) = 1 and a class c of H^1 with c(lambda) != 0.
  Closed objects: G_n,k = G_n with lambda^k = 1, k = 1 (the fibre's puncture filled: a closed torus bundle) and
  k = 2..6 (a cone point of order k). Non-split abelian doublets: [[alpha, c beta], [0, beta]], c a non-coboundary class
  of H^1(G; l), l = alpha / beta, for every character alpha and every such class. V* is the dual, V (x) w the twist.
  The untwisted gap: h^1(V) - h^1(V*). The twisted gap: h^1(V) - h^1(V* (x) w).
  Levels: golden n = 1, 3, 5 (double covers 2, 6, 10); bronze n = 1 (double cover 2).

EXPECTATIONS, written before the run (derived by hand from the definitions; N6's numbers are agy-exp's, card X-SM):
  N1  Transfer. For every character chi of every odd level computed: h^i(G_2n; pi* chi) = h^i(G_n; chi) +
      h^i(G_n; chi (x) w) for i = 0, 1, 2, and the same for the interior classes n.
  N2  Main's B1926 addendum. Every fibre-non-trivial chi with chi(mu_n) = -1 pulls back to a level-2n character trivial
      on mu_2n that carries a class with c(lambda) != 0. Their numbers: golden 0, 3, 10 (n = 1, 3, 5); bronze 2.
      And every fibre-non-trivial chi with chi(mu_n) = +1 has h^1(G_n; chi) = 0.
  N3  The whole accounting. At level 2n the record's data number |T_2n| - 1: golden 0, 15, 120; bronze 8. Of these,
      the deck-invariant ones are exactly the pull-backs of N2's characters (golden 0, 3, 10; bronze 2), and the rest
      come in deck pairs (golden 0, 6, 55; bronze 3). For every fibre-non-trivial psi that is not deck-invariant (every
      T-value computed), Ind psi is a module of G_n and h^i(G_n; Ind psi) = h^i(G_2n; psi), i = 0, 1, 2, and n equal.
  N4  The closed objects (k = 1..6) at the odd levels: h^1(G_n,k; l) = 1 for l trivial and 0 for every other character.
      So the only non-split abelian doublets are alpha (x) U, U the unipotent extension by the tick's class.
  N5  On the closed objects at the odd levels, every character, every non-split abelian doublet and every induced
      module Ind psi (psi not deck-invariant on G_2n,k) has untwisted gap 0, and twisted gap equal to
      h^0(V) - h^0(V* (x) w). For every induced module, h^1(G_n,k; Ind psi) = h^1(G_2n,k; psi).
  N6  Control: the instrument registers an untwisted gap where one exists. On N_3 x S^1 (c1, c2, c3, mu; c1^2 c2^2 c3^2,
      [mu, c_i]; omega = (-1, -1, -1, +1)) with alpha = (z3, z3^2, 1, 1), beta = (-1, -1, -1, 1) and the cocycle
      u = (0, 0, 1, 0): (h^0, h^1) is (0, 3), (0, 2), (1, 4) for V, V*, V* (x) omega (or, if this seat's extension
      convention is the other one, the same three for V*, V, V (x) omega). And h^1(V) + h^1(V (x) omega) - h^1(V*) -
      h^1(V* (x) omega) = h^0(V) + h^0(V (x) omega) - h^0(V*) - h^0(V* (x) omega) (the orientation double cover's
      count, by transfer and twisted duality).
  P1  Plant: transfer with w left out, h^1(G_2n; pi* chi) = 2 h^1(G_n; chi), fails for some chi at golden n = 3, 5.
  P2  Plant: Ind built with tau^(n+1) in place of tau^n fails the relations for some psi at golden 2n = 6, 10.
  Both primes must give the same counts.
"""
import os
from math import gcd

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = open(os.path.join(HERE, "..", "chat1_2026-11-14_wc8", "wc8_part2a_checks.py")).read()
ns = {}
exec(SRC.split("EXP = {}")[0], ns)
red, inv, apply, abel2, LAM = ns["red"], ns["inv"], ns["apply"], ns["abel2"], ns["LAM"]
Rep, cohomology, nullspace_mod, rank_mod = ns["Rep"], ns["cohomology"], ns["nullspace_mod"], ns["rank_mod"]
find_prime, madd, ident = ns["find_prime"], ns["madd"], ns["ident"]


def say(*a):
    print(*a, flush=True)


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


def tick(m):
    return {1: tuple([1] * m + [2]), 2: (1,)}


def tick_pow(m, n):
    T, f = tick(m), {1: (1,), 2: (2,)}
    for _ in range(n):
        f = {k: apply(T, v) for k, v in f.items()}
    return f


def conj_m(m, n):
    T, g, s = tick(m), tuple([1] * m), -1
    for _ in range(n - 1):
        g, s = red(apply(T, g) + tuple([1] * m)), -s
    return g, s


M = 264  # every root of unity used has order dividing M (2e for e in 1, 2, 3, 4, 11; and 3, 2 for the control)


def abmat(m, n):
    f = tick_pow(m, n)
    return [[abel2(f[1])[0], abel2(f[2])[0]], [abel2(f[1])[1], abel2(f[2])[1]]]


class Level:
    def __init__(self, m, n):
        self.m, self.n = m, n
        f = tick_pow(m, n)
        self.f = f
        A = [[abel2(f[1])[0], abel2(f[2])[0]], [abel2(f[1])[1], abel2(f[2])[1]]]
        self.A = A
        tor = abs((A[0][0] - 1) * (A[1][1] - 1) - A[0][1] * A[1][0])
        g1 = gcd(gcd(A[0][0] - 1, A[0][1]), gcd(A[1][0], A[1][1] - 1))
        self.tor = tor
        self.e = max(tor // g1, 1)
        assert (2 * self.e) and M % (2 * self.e) == 0
        g, s = conj_m(m, n)
        assert apply(f, LAM) == red(g + (LAM if s == 1 else inv(LAM)) + inv(g)), "cusp conjugator"
        self.g, self.s = g, s
        self.ga, self.gb = abel2(g)
        self.mu = red(inv(g) + (3,))
        self.rels = [red((3, 1, -3) + inv(f[1])), red((3, 2, -3) + inv(f[2]))]
        e = self.e
        self.fib = [(a1, a2) for a1 in range(e) for a2 in range(e)
                    if (a1 * A[0][0] + a2 * A[1][0] - a1) % e == 0 and (a1 * A[0][1] + a2 * A[1][1] - a2) % e == 0]
        assert len(self.fib) == max(tor, 1), (m, n, len(self.fib), tor)
        self.wt = M // 2 if n % 2 else 0

    def chars(self):
        e = self.e
        return [((M // e) * a1 % M, (M // e) * a2 % M, (M // (2 * e)) * j % M) for (a1, a2) in self.fib
                for j in range(2 * e)]

    def chi_mu(self, ch):
        return (ch[2] - ch[0] * self.ga - ch[1] * self.gb) % M

    def deck(self, ch):  # psi^t on the fibre, for psi a character of the double cover; self is the odd level
        A = self.A
        return ((ch[0] * A[0][0] + ch[1] * A[1][0]) % M, (ch[0] * A[0][1] + ch[1] * A[1][1]) % M, ch[2])

    def closed_rels(self, k):
        return self.rels + [red(LAM * k)]


def run(p):
    gen = next(x for x in range(2, p) if all(pow(x, (p - 1) // q, p) != 1 for q in prime_factors(p - 1)))
    zM = pow(gen, (p - 1) // M, p)

    def v(x):
        return pow(zM, x % M, p)

    def rep1(ch):
        return Rep({1: [[v(ch[0])]], 2: [[v(ch[1])]], 3: [[v(ch[2])]]}, p)

    def coh(mats, rels, mu):
        return cohomology(Rep(mats, p), rels, mu, LAM)

    def mats1(ch):
        return {1: [[v(ch[0])]], 2: [[v(ch[1])]], 3: [[v(ch[2])]]}

    def is_hom(mats, rels):
        R = Rep(mats, p)
        d = R.d
        return all(R.of(r) == ident(d) for r in rels)

    def dual(mats):
        R = Rep(mats, p)
        return {gi: [list(r) for r in zip(*R.inv[gi])] for gi in mats}

    def twist(mats, wt):  # multiply t's matrix by w(t)
        s = v(wt)
        out = dict(mats)
        out[3] = [[x * s % p for x in r] for r in mats[3]]
        return out

    def classes(ch, rels):
        r1 = rep1(ch)
        F = [[r1.fox(r, gi)[0][0] for gi in (1, 2, 3)] for r in rels]
        Z = nullspace_mod(F, p, 3)
        cob = [(r1.m[gi][0][0] - 1) % p for gi in (1, 2, 3)]
        base = [cob] if any(cob) else []
        chosen = []
        for z in Z:
            if rank_mod(base + chosen + [z], p) > len(base) + len(chosen):
                chosen.append(z)
        return r1, chosen

    def lam_nonzero(ch, rels):
        r1, cl = classes(ch, rels)
        return any(r1.cocycle_value({1: [c[0]], 2: [c[1]], 3: [c[2]]}, LAM)[0] % p for c in cl)

    def ind(Ln, psi, deckA=None):
        A = deckA or Ln.A
        sa = (psi[0] * A[0][0] + psi[1] * A[1][0]) % M
        sb = (psi[0] * A[0][1] + psi[1] * A[1][1]) % M
        return {1: [[v(psi[0]), 0], [0, v(sa)]], 2: [[v(psi[1]), 0], [0, v(sb)]], 3: [[0, v(psi[2])], [1, 0]]}

    census, plants = {}, {}
    ok = dict(N1=True, N2=True, N3=True, N4=True, N5=True, N6=None, P1=False, P2=False)
    for (m, n) in ((1, 1), (1, 3), (1, 5), (3, 1)):
        L, L2 = Level(m, n), Level(m, 2 * n)
        assert L2.g == red(apply(L.f, L.g) + L.g), "g_2n = tau^n(g_n) g_n"
        name = ("golden" if m == 1 else "bronze") + " n=%d" % n
        # N1 transfer
        bad1, plant1 = 0, 0
        for ch in L.chars():
            h = coh(mats1(ch), L.rels, L.mu)
            hw = coh(mats1((ch[0], ch[1], ch[2] + L.wt)), L.rels, L.mu)
            pb = (ch[0], ch[1], 2 * ch[2] % M)
            h2 = coh(mats1(pb), L2.rels, L2.mu)
            if any(h2[key] != h[key] + hw[key] for key in ("h0", "h1", "h2", "n")):
                bad1 += 1
            plant1 += h2["h1"] != 2 * h["h1"]
        ok["N1"] &= bad1 == 0
        plants[("P1", m, n)] = plant1
        # N2 the pull-back of the twisted characters
        tw = [ch for ch in L.chars() if (ch[0], ch[1]) != (0, 0) and L.chi_mu(ch) == M // 2]
        n2 = sum(1 for ch in tw if L2.chi_mu((ch[0], ch[1], 2 * ch[2] % M)) == 0
                 and lam_nonzero((ch[0], ch[1], 2 * ch[2] % M), L2.rels))
        un = [ch for ch in L.chars() if (ch[0], ch[1]) != (0, 0) and L.chi_mu(ch) == 0]
        n2b = sum(1 for ch in un if coh(mats1(ch), L.rels, L.mu)["h1"] == 0)
        exp2 = {(1, 1): 0, (1, 3): 3, (1, 5): 10, (3, 1): 2}[(m, n)]
        ok["N2"] &= len(tw) == exp2 and n2 == exp2 and n2b == len(un)
        # N3 the whole accounting
        fib2 = [ch for ch in L2.chars() if (ch[0], ch[1]) != (0, 0)]
        R = [ch for ch in fib2 if L2.chi_mu(ch) == 0 and lam_nonzero(ch, L2.rels)]
        Rinv = {ch for ch in R if L.deck(ch) == ch}
        pulled = {(ch[0], ch[1], 2 * ch[2] % M) for ch in tw}
        pairs = (len(R) - len(Rinv)) // 2
        expR = {(1, 1): (0, 0, 0), (1, 3): (15, 3, 6), (1, 5): (120, 10, 55), (3, 1): (8, 2, 3)}[(m, n)]
        bad3, nind, plant2 = 0, 0, 0
        S = abmat(m, n + 1)
        for psi in fib2:
            if L.deck(psi) == psi:
                continue
            mats = ind(L, psi)
            if not is_hom(mats, L.rels):
                bad3 += 1
                continue
            hi = coh(mats, L.rels, L.mu)
            hp = coh(mats1(psi), L2.rels, L2.mu)
            if any(hi[key] != hp[key] for key in ("h0", "h1", "h2", "n")):
                bad3 += 1
            nind += 1
            plant2 += not is_hom(ind(L, psi, S), L.rels)
        ok["N3"] &= (len(R), len(Rinv), pairs) == expR and Rinv == pulled and bad3 == 0
        plants[("P2", m, n)] = plant2
        census[(name, "cusped")] = dict(chars=len(L.chars()), N1_bad=bad1, P1=plant1, twisted=len(tw), N2=n2,
                                        untwisted_h1_zero=n2b, R=len(R), R_inv=len(Rinv), R_pairs=pairs,
                                        ind=nind, N3_bad=bad3, P2=plant2)
        say(p, name, "cusped:", census[(name, "cusped")])
        # N4, N5 the closed objects
        for k in range(1, 7):
            rk, rk2 = L.closed_rels(k), L2.closed_rels(k)
            bad4, nd, bad5u, bad5t, nchar, nindc, badsh = 0, 0, 0, 0, 0, 0, 0
            cls = {}
            for ch in L.chars():
                r1, cl = classes(ch, rk)
                cls[ch] = cl
                triv = ch == (0, 0, 0)
                bad4 += len(cl) != (1 if triv else 0)
                mats = mats1(ch)
                h, hd = coh(mats, rk, L.mu), coh(dual(mats), rk, L.mu)
                hdw = coh(twist(dual(mats), L.wt), rk, L.mu)
                bad5u += h["h1"] != hd["h1"]
                bad5t += (h["h1"] - hdw["h1"]) != (h["h0"] - hdw["h0"])
                nchar += 1
            for l, cl in cls.items():
                for c in cl:
                    for al in L.chars():
                        be = tuple((al[i] - l[i]) % M for i in range(3))
                        mats = {gi: [[v(al[gi - 1]), c[gi - 1] * v(be[gi - 1]) % p], [0, v(be[gi - 1])]]
                                for gi in (1, 2, 3)}
                        if not is_hom(mats, rk):
                            bad4 += 1
                            continue
                        h, hd = coh(mats, rk, L.mu), coh(dual(mats), rk, L.mu)
                        hdw = coh(twist(dual(mats), L.wt), rk, L.mu)
                        bad5u += h["h1"] != hd["h1"]
                        bad5t += (h["h1"] - hdw["h1"]) != (h["h0"] - hdw["h0"])
                        nd += 1
            seen = set()
            for psi in L2.chars():
                if (psi[0], psi[1]) == (0, 0) or L.deck(psi) == psi or psi in seen:
                    continue
                seen.add(psi)
                seen.add(L.deck(psi))
                mats = ind(L, psi)
                if not is_hom(mats, rk):
                    bad5u += 1
                    continue
                h, hd = coh(mats, rk, L.mu), coh(dual(mats), rk, L.mu)
                hdw = coh(twist(dual(mats), L.wt), rk, L.mu)
                hp = coh(mats1(psi), rk2, L2.mu)
                bad5u += h["h1"] != hd["h1"]
                bad5t += (h["h1"] - hdw["h1"]) != (h["h0"] - hdw["h0"])
                badsh += h["h1"] != hp["h1"]
                nindc += 1
            ok["N4"] &= bad4 == 0
            ok["N5"] &= bad5u == 0 and bad5t == 0 and badsh == 0
            census[(name, k)] = dict(chars=nchar, doublets=nd, induced=nindc, N4_bad=bad4, untwisted_bad=bad5u,
                                     twisted_bad=bad5t, shapiro_bad=badsh)
            say(p, name, "closed k=%d:" % k, census[(name, k)])
    # N6 the control on N_3 x S^1 (generators c1 = 1, c2 = 2, c3 = 3, mu = 4)
    rels6 = [(1, 1, 2, 2, 3, 3), (4, 1, -4, -1), (4, 2, -4, -2), (4, 3, -4, -3)]
    z3, mone = M // 3, M // 2
    al = (z3, 2 * z3, 0, 0)
    be = (mone, mone, mone, 0)
    om = (mone, mone, mone, 0)
    u = (0, 0, 1, 0)
    V = {gi: [[v(al[gi - 1]), u[gi - 1] * v(be[gi - 1]) % p], [0, v(be[gi - 1])]] for gi in (1, 2, 3, 4)}

    def h01(mats):
        R = Rep(mats, p)
        d = R.d
        F = []
        for r in rels6:
            blocks = [R.fox(r, g) for g in (1, 2, 3, 4)]
            for i in range(d):
                F.append([blocks[k][i][j] for k in range(4) for j in range(d)])
        rkF = rank_mod(F, p)
        Dm = []
        for g in (1, 2, 3, 4):
            Dm.extend(madd(R.m[g], ident(d), p, -1))
        rkD = rank_mod(Dm, p)
        return (d - rkD, 4 * d - rkF - rkD)

    def tw6(mats):
        return {gi: [[x * v(om[gi - 1]) % p for x in r] for r in mats[gi]] for gi in mats}

    homV = all(Rep(V, p).of(r) == ident(2) for r in rels6)
    Vd = dual(V)
    hV, hVd, hVw, hVdw = h01(V), h01(Vd), h01(tw6(V)), h01(tw6(Vd))
    conv1 = (hV, hVd, hVdw) == ((0, 3), (0, 2), (1, 4))
    conv2 = (hVd, hV, hVw) == ((0, 3), (0, 2), (1, 4))
    cover = (hV[1] + hVw[1] - hVd[1] - hVdw[1]) == (hV[0] + hVw[0] - hVd[0] - hVdw[0])
    ok["N6"] = homV and (conv1 or conv2) and cover
    census["N6"] = dict(hom=homV, V=hV, Vstar=hVd, V_w=hVw, Vstar_w=hVdw, convention=1 if conv1 else (2 if conv2 else 0),
                        cover_identity=cover)
    say(p, "N6:", census["N6"])
    ok["P1"] = plants[("P1", 1, 3)] > 0 and plants[("P1", 1, 5)] > 0
    ok["P2"] = plants[("P2", 1, 3)] > 0 and plants[("P2", 1, 5)] > 0
    return ok, census


PRIMES = []
k0 = 40000
while len(PRIMES) < 2:
    q = find_prime(M, k0)
    PRIMES.append(q)
    k0 = (q - 1) // M + 1
say("primes", PRIMES)
res = [run(q) for q in PRIMES]
same = res[0][1] == res[1][1]
for key in ("N1", "N2", "N3", "N4", "N5", "N6", "P1", "P2"):
    say(key, "holds:" if key[0] == "N" else "fires:", res[0][0][key] and res[1][0][key])
say("both primes give the same census:", same)
