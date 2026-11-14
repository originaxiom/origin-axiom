#!/usr/bin/env python3
"""W-F6: the character-gap law and the normaliser, as theorems, with computed checks.

Data-free; this seat's own code. The helpers (free group, Fox calculus over F_p) are taken by text from W-C8 part 2a's
sealed script (definitions only, up to its census), which is not re-run.

    python3 -I -u wf6_checks.py

THE GAP LAW (proof by hand, in the note). G = F_2 x| <t>, t f t^-1 = phi(f), phi a hyperbolic automorphism of
<a, b> with phi(lambda) = g lambda^s g^-1 (lambda = [a, b], s = +-1 = det of phi's abelianisation A), mu = g^-1 t.
For a character chi with fibre part theta != 1: h^1(G; chi) = [chi(mu) = s], and the class has c(lambda) != 0.
For theta = 1: h^1(G; chi) = [chi = 1] (in characteristic 0; over F_p for p outside a finite set).
Hence, with w(t) = s: gap(chi) = h^1(chi) - h^1(chi^-1 w) = [chi(mu) = s] - [chi(mu) = 1] for theta != 1, and
gap(1) = [s = -1], gap(w) = -[s = -1].

THE NORMALISER (proof by hand, in the note). J_m = [[m, 1], [1, 0]], A_m = J_m^2, K = [[0, 1], [-1, 0]]. The centraliser
of A_m (and of J_m) in GL(2, Z) is +-<J_m>, since x = (m + sqrt(m^2 + 4))/2 is the fundamental unit of Z[x]; and the
normaliser of <A_m> in GL(2, Z) is {+-J_m^n K^e}.

DEFINITIONS FOR THE CHECKS
  Monodromies, as word automorphisms of <a, b> (a = 1, b = 2): the metallic ticks tau_m: a -> a^m b, b -> a for
  m = 1 (golden, levels 1..8), m = 2 (silver, levels 1..4), m = 3 (bronze, levels 1..3); and two non-metallic ones
  built from L: (a, b) -> (a, ab), R: (a, b) -> (ab, b), P: (a, b) -> (b, a): phi_A = R o L o L (det +1) and
  phi_B = P o R o L o L (det -1), levels 1..3. g and s are found by cyclically reducing phi^n(lambda).
  Characters: fibre part on coker(A_n - I) (exponent e), t-value every 2e-th root of unity (the "root" characters) and
  3 further pseudo-random elements of F_p^* per fibre part. Two primes p = 1 mod M, M the lcm of all 2e.

EXPECTATIONS, written before the run:
  G1  On every monodromy and level, for every character: h^1 = [chi(mu) = s] if theta != 1, with c(lambda) != 0 on the
      class; h^1 = [chi = 1] if theta = 1.
  G2  Among the root characters: at s = -1 the characters with gap +1, and those with gap -1, number exactly the fibre
      torsion |T| (golden 1, 4, 11, 29 at n = 1, 3, 5, 7; silver 2, 14; bronze 3, 36; phi_B its own); at s = +1 every
      gap is 0, and the characters with theta != 1, chi(mu) = 1 (the record's data) number |T| - 1.
  N1  For m = 1..60, the integer solutions of a^2 + m a b - b^2 = +-1 with |a|, |b| <= 2000 are exactly the pairs
      +-(a_k, b_k) with x^k = a_k + b_k x (k in Z) that lie in the box.
  N2  For m = 1..60: K J_m K^-1 = -J_m^-1 and K A_m K^-1 = A_m^-1; and among +-J_m^k, |k| <= 20, the only ones with
      trace m and det -1 are J_m and -J_m^-1.
  Plants: GP, the law with -s in place of s, fails on some level of each sign of s; NP, the unit group taken as
  +-<x^2>, misses solutions for every m.
  Both primes must give the same counts.
"""
import os
import random
from math import gcd, isqrt

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = open(os.path.join(HERE, "..", "chat1_2026-11-14_wc8", "wc8_part2a_checks.py")).read()
ns = {}
exec(SRC.split("EXP = {}")[0], ns)
red, inv, apply, abel2, LAM = ns["red"], ns["inv"], ns["apply"], ns["abel2"], ns["LAM"]
Rep, nullspace_mod, rank_mod, find_prime = ns["Rep"], ns["nullspace_mod"], ns["rank_mod"], ns["find_prime"]


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


def compose(f, g):  # f o g
    return {k: apply(f, v) for k, v in g.items()}


def tick(m):
    return {1: tuple([1] * m + [2]), 2: (1,)}


Lm, Rm, Pm = {1: (1,), 2: (1, 2)}, {1: (1, 2), 2: (2,)}, {1: (2,), 2: (1,)}
phiA = compose(Rm, compose(Lm, Lm))
phiB = compose(Pm, phiA)
MONOS = [("golden", tick(1), 8), ("silver", tick(2), 4), ("bronze", tick(3), 3), ("phi_A", phiA, 3),
         ("phi_B", phiB, 3)]


def power(phi, n):
    f = {1: (1,), 2: (2,)}
    for _ in range(n):
        f = compose(phi, f)
    return f


def conjugator(f):
    w = apply(f, LAM)
    u = []
    while len(w) > 1 and w[0] == -w[-1]:
        u.append(w[0])
        w = w[1:-1]
    for s, Ls in ((1, LAM), (-1, inv(LAM))):
        for r in range(4):
            if tuple(Ls[r:] + Ls[:r]) == tuple(w):
                g = red(tuple(u) + inv(Ls[:r]))
                assert red(g + Ls + inv(g)) == apply(f, LAM)
                return g, s
    raise AssertionError("no conjugator")


class Lev:
    def __init__(self, phi, n):
        f = power(phi, n)
        self.f = f
        A = [[abel2(f[1])[0], abel2(f[2])[0]], [abel2(f[1])[1], abel2(f[2])[1]]]
        self.A = A
        self.det = A[0][0] * A[1][1] - A[0][1] * A[1][0]
        self.g, self.s = conjugator(f)
        assert self.s == self.det
        tor = abs((A[0][0] - 1) * (A[1][1] - 1) - A[0][1] * A[1][0])
        g1 = gcd(gcd(A[0][0] - 1, A[0][1]), gcd(A[1][0], A[1][1] - 1))
        self.tor, self.e = tor, max(tor // g1, 1)
        e = self.e
        self.fib = [(a1, a2) for a1 in range(e) for a2 in range(e)
                    if (a1 * A[0][0] + a2 * A[1][0] - a1) % e == 0 and (a1 * A[0][1] + a2 * A[1][1] - a2) % e == 0]
        assert len(self.fib) == max(tor, 1)
        self.mu = red(inv(self.g) + (3,))
        self.rels = [red((3, 1, -3) + inv(f[1])), red((3, 2, -3) + inv(f[2]))]
        self.ga, self.gb = abel2(self.g)


LEVELS = [(name, n, Lev(phi, n)) for name, phi, top in MONOS for n in range(1, top + 1)]
Mtot = 1
for _, _, L in LEVELS:
    Mtot = Mtot * (2 * L.e) // gcd(Mtot, 2 * L.e)
say("M =", Mtot)


def run(p):
    gen = next(x for x in range(2, p) if all(pow(x, (p - 1) // q, p) != 1 for q in prime_factors(p - 1)))
    z = pow(gen, (p - 1) // Mtot, p)
    rnd = random.Random(20261114)
    ok = dict(G1=True, G2=True)
    census, plant = {}, {1: 0, -1: 0}
    for name, n, L in LEVELS:
        e, s = L.e, L.s
        sp = s % p
        rootsT = [pow(z, (Mtot // (2 * e)) * j, p) for j in range(2 * e)]
        h1 = {}
        bad1, nchar = 0, 0
        for (a1, a2) in L.fib:
            va, vb = pow(z, (Mtot // e) * a1, p), pow(z, (Mtot // e) * a2, p)
            extra = [rnd.randrange(2, p - 1) for _ in range(3)]
            for vt in rootsT + extra:
                r1 = Rep({1: [[va]], 2: [[vb]], 3: [[vt]]}, p)
                F = [[r1.fox(r, gi)[0][0] for gi in (1, 2, 3)] for r in L.rels]
                Z = nullspace_mod(F, p, 3)
                cob = [(va - 1) % p, (vb - 1) % p, (vt - 1) % p]
                base = [cob] if any(cob) else []
                cl = []
                for zz in Z:
                    if rank_mod(base + cl + [zz], p) > len(base) + len(cl):
                        cl.append(zz)
                chig = pow(va, L.ga, p) * pow(vb, L.gb, p) % p
                chimu = pow(chig, p - 2, p) * vt % p
                fib_triv = (a1, a2) == (0, 0)
                if fib_triv:
                    want = 1 if vt == 1 else 0
                    good = len(cl) == want
                else:
                    want = 1 if chimu == sp else 0
                    good = len(cl) == want and all(
                        r1.cocycle_value({1: [c[0]], 2: [c[1]], 3: [c[2]]}, LAM)[0] % p for c in cl)
                    plant[s] += len(cl) != (1 if chimu == (-s) % p else 0)
                bad1 += not good
                nchar += 1
                if vt in rootsT:
                    h1[(va, vb, vt)] = (len(cl), chimu, fib_triv)
        ok["G1"] &= bad1 == 0
        plus = minus = rec = 0
        for (va, vb, vt), (h, chimu, ft) in h1.items():
            dual_w = (pow(va, p - 2, p), pow(vb, p - 2, p), pow(vt, p - 2, p) * sp % p)
            gap = h - h1[dual_w][0]
            plus += gap == 1
            minus += gap == -1
            rec += (not ft) and chimu == 1 and h == 1
        T = max(L.tor, 1)
        if s == -1:
            g2 = plus == T and minus == T
        else:
            g2 = plus == 0 and minus == 0 and rec == T - 1
        ok["G2"] &= g2
        census[(name, n)] = dict(s=s, T=T, chars=nchar, G1_bad=bad1, gap_plus=plus, gap_minus=minus, record=rec)
        say(p, name, "n=%d" % n, census[(name, n)])
    ok["GP"] = plant[1] > 0 and plant[-1] > 0
    return ok, census


primes, k0 = [], 1
while len(primes) < 2:
    q = find_prime(Mtot, k0)
    primes.append(q)
    k0 = (q - 1) // Mtot + 1
say("primes", primes)
res = [run(q) for q in primes]
say("G1 holds:", res[0][0]["G1"] and res[1][0]["G1"])
say("G2 holds:", res[0][0]["G2"] and res[1][0]["G2"])
say("GP fires:", res[0][0]["GP"] and res[1][0]["GP"])
say("both primes give the same census:", res[0][1] == res[1][1])


# ---------- the normaliser ----------
def mul(X, Y):
    return [[X[0][0] * Y[0][0] + X[0][1] * Y[1][0], X[0][0] * Y[0][1] + X[0][1] * Y[1][1]],
            [X[1][0] * Y[0][0] + X[1][1] * Y[1][0], X[1][0] * Y[0][1] + X[1][1] * Y[1][1]]]


def inv2(X):  # for det +-1
    d = X[0][0] * X[1][1] - X[0][1] * X[1][0]
    return [[X[1][1] * d, -X[0][1] * d], [-X[1][0] * d, X[0][0] * d]]


B = 2000
n1, n2, npl = True, True, True
for m in range(1, 61):
    sols = set()
    for b in range(-B, B + 1):
        for sgn in (1, -1):
            D = m * m * b * b + 4 * (b * b + sgn)
            if D < 0:
                continue
            r = isqrt(D)
            if r * r != D:
                continue
            for num in (-m * b + r, -m * b - r):
                if num % 2 == 0 and abs(num // 2) <= B:
                    a = num // 2
                    if a * a + m * a * b - b * b in (1, -1):
                        sols.add((a, b))
    U = set()
    a_, b_ = 1, 0
    for _ in range(80):
        U.update({(a_, b_), (-a_, -b_)})
        a_, b_ = b_, a_ + m * b_
    a_, b_ = 1, 0
    for _ in range(80):
        U.update({(a_, b_), (-a_, -b_)})
        a_, b_ = b_ - m * a_, a_
    Ubox = {u for u in U if abs(u[0]) <= B and abs(u[1]) <= B}
    n1 &= sols == Ubox
    # the plant: units taken as +-<x^2>
    U2, a_, b_ = set(), 1, 0
    for k in range(160):
        if k % 2 == 0:
            U2.update({(a_, b_), (-a_, -b_)})
        a_, b_ = b_, a_ + m * b_
    a_, b_ = 1, 0
    for k in range(160):
        if k % 2 == 0:
            U2.update({(a_, b_), (-a_, -b_)})
        a_, b_ = b_ - m * a_, a_
    npl &= sols != {u for u in U2 if abs(u[0]) <= B and abs(u[1]) <= B}
    J = [[m, 1], [1, 0]]
    K = [[0, 1], [-1, 0]]
    Ji, Ki = inv2(J), inv2(K)
    A = mul(J, J)
    n2 &= mul(mul(K, J), Ki) == [[-x for x in r] for r in Ji]
    n2 &= mul(mul(K, A), Ki) == inv2(A)
    hits = []
    P, Pinv = [[1, 0], [0, 1]], [[1, 0], [0, 1]]
    for k in range(1, 21):
        P, Pinv = mul(P, J), mul(Pinv, Ji)
        for sg in (1, -1):
            for kk, X in ((k, P), (-k, Pinv)):
                Y = [[sg * x for x in r] for r in X]
                if Y[0][0] + Y[1][1] == m and Y[0][0] * Y[1][1] - Y[0][1] * Y[1][0] == -1:
                    hits.append((sg, kk))
    n2 &= sorted(hits) == [(-1, -1), (1, 1)]
say("N1 holds:", n1)
say("N2 holds:", n2)
say("NP fires:", npl)
