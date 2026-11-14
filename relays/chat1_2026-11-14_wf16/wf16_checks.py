#!/usr/bin/env python3
"""W-F16: the two-way choices settle each other. Data-free; this seat's own code. The helpers are taken by text from
W-C8 part 2a's sealed script (definitions only), which is not re-run.

    python3 -I -u wf16_checks.py

DEFINITIONS
  J_m = [[m, 1], [1, 0]], K = [[0, 1], [-1, 0]], N = m^2 + 4, the mark v = (m, 2) mod N (odd m). The hand of
  +-J^n K^e at the mark is 1 when it acts on v by a scalar outside {+1, -1} (that is, by +-lambda), 0 when by +-1.
  The mirror at an even level n of the metallic tick tau: phi(a) = tau(a), phi(b) = tau(b), phi(t) = t. Pulling a
  module back by phi: (V o phi)(g) = V(phi(g)) on the generators. Record modules and I(V) = n(V) - n(V*) as in W-F9.
  The F_2 count: bits (h, o, e, r, q, y); relations as linear forms; symmetries as vectors; free bits = (6 - rank of
  the relations) - (rank of the symmetries), with every symmetry checked to preserve the relations.

EXPECTATIONS, written before the run:
  H1  For every odd m = 1..41, every n = 0..7, e in {0, 1} and sign: J_m^n K^e (times the sign) sends v to a multiple
      of v mod N, and the hand equals (n + e) mod 2.
  H2  At golden levels 4, 6, 8 and bronze level 2, the mirror pulls every record module back to a module (the relators
      hold), and I(V o phi) = I(V) on every record module (12, 210, 1,892 and 56 modules).
  H3  The F_2 count of free bits: 0 with symmetries {J, K, D, C} and relations {h + o + e, q + y}; 1 with {J, K, D}
      only; 0 with {J, K, D o C} and relations {h + o + e, q + y, r + y}; 1 with {J, K, D o C} and relations
      {h + o + e, q + y}.
  Plant: the map with t -> t^-1 in place of t -> t fails the relators on some record module at every level of H2.
"""
import os
from math import gcd

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = open(os.path.join(HERE, "..", "chat1_2026-11-14_wc8", "wc8_part2a_checks.py")).read()
ns = {}
exec(SRC.split("EXP = {}")[0], ns)
red, inv, apply, abel2, LAM = ns["red"], ns["inv"], ns["apply"], ns["abel2"], ns["LAM"]
Rep, cohomology, nullspace_mod, find_prime, ident = (ns["Rep"], ns["cohomology"], ns["nullspace_mod"],
                                                     ns["find_prime"], ns["ident"])


def say(*a):
    print(*a, flush=True)


# ---------- H1 ----------
def mm(A, B, N):
    return [[(A[0][0] * B[0][0] + A[0][1] * B[1][0]) % N, (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % N],
            [(A[1][0] * B[0][0] + A[1][1] * B[1][0]) % N, (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % N]]


h1 = True
for m in range(1, 42, 2):
    N = m * m + 4
    J, K = [[m, 1], [1, 0]], [[0, 1], [N - 1, 0]]
    v = (m % N, 2 % N)
    i2 = pow(2, -1, N)
    lam = m * i2 % N
    P = [[1, 0], [0, 1]]
    for n in range(8):
        for e in (0, 1):
            X = mm(P, K, N) if e else P
            for sg in (1, N - 1):
                Y = [[x * sg % N for x in r] for r in X]
                w = ((Y[0][0] * v[0] + Y[0][1] * v[1]) % N, (Y[1][0] * v[0] + Y[1][1] * v[1]) % N)
                s = w[0] * pow(v[0], -1, N) % N if gcd(v[0], N) == 1 else w[1] * pow(v[1], -1, N) % N
                h1 &= ((s * v[0] - w[0]) % N == 0 and (s * v[1] - w[1]) % N == 0)
                hand = 0 if s in (1, N - 1) else 1
                h1 &= s in (1, N - 1, lam, N - lam) and hand == (n + e) % 2
        P = mm(P, J, N)
say("H1 holds:", h1)


# ---------- H2 ----------
def prime_factors(x):
    fs, d = set(), 2
    while d * d <= x:
        while x % d == 0:
            fs.add(d)
            x //= d
        d += 1
    if x > 1:
        fs.add(x)
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


LEVELS = [("golden", 1, 4, 12), ("golden", 1, 6, 210), ("golden", 1, 8, 1892), ("bronze", 3, 2, 56)]
Mtot, data = 1, []
for name, m, n, want in LEVELS:
    f = tick_pow(m, n)
    A = [[abel2(f[1])[0], abel2(f[2])[0]], [abel2(f[1])[1], abel2(f[2])[1]]]
    tor = abs((A[0][0] - 1) * (A[1][1] - 1) - A[0][1] * A[1][0])
    g1 = gcd(gcd(A[0][0] - 1, A[0][1]), gcd(A[1][0], A[1][1] - 1))
    e = max(tor // g1, 1)
    g, s = conj_m(m, n)
    fib = [(a1, a2) for a1 in range(e) for a2 in range(e)
           if (a1 * A[0][0] + a2 * A[1][0] - a1) % e == 0 and (a1 * A[0][1] + a2 * A[1][1] - a2) % e == 0
           and (a1, a2) != (0, 0)]
    rels = [red((3, 1, -3) + inv(f[1])), red((3, 2, -3) + inv(f[2]))]
    data.append((name, m, n, want, e, fib, abel2(g), red(inv(g) + (3,)), rels))
    Mtot = Mtot * e // gcd(Mtot, e)
p = find_prime(Mtot, 300000)
gen = next(x for x in range(2, p) if all(pow(x, (p - 1) // q, p) != 1 for q in prime_factors(p - 1)))
z = pow(gen, (p - 1) // Mtot, p)
say("prime", p)
h2 = plant = True
for name, m, n, want, e, fib, (ga, gb), mu, rels in data:
    T = tick(m)
    phi = {1: T[1], 2: T[2], 3: (3,)}
    phi_bad = {1: T[1], 2: T[2], 3: (-3,)}
    chars = {}
    for (a1, a2) in fib:
        va, vb = pow(z, (Mtot // e) * a1, p), pow(z, (Mtot // e) * a2, p)
        chars[(a1, a2)] = (va, vb, pow(va, ga, p) * pow(vb, gb, p) % p)

    def cls(l):
        r1 = Rep({1: [[l[0]]], 2: [[l[1]]], 3: [[l[2]]]}, p)
        F = [[r1.fox(r, gi)[0][0] for gi in (1, 2, 3)] for r in rels]
        for zb in nullspace_mod(F, p, 3):
            lv = r1.cocycle_value({1: [zb[0]], 2: [zb[1]], 3: [zb[2]]}, LAM)[0] % p
            if lv:
                iv = pow(lv, p - 2, p)
                return [x * iv % p for x in zb]
        return None

    def I_of(mats):
        R = Rep(mats, p)
        d = {gi: [list(row) for row in zip(*R.inv[gi])] for gi in (1, 2, 3)}
        return cohomology(R, rels, mu, LAM)["n"] - cohomology(Rep(d, p), rels, mu, LAM)["n"]

    def pull(mats, f):
        R = Rep(mats, p)
        return {gi: R.of(f[gi]) for gi in (1, 2, 3)}

    def is_hom(mats):
        R = Rep(mats, p)
        return all(R.of(r) == ident(2) for r in rels)

    nmod, bad, badp = 0, 0, 0
    for kl, l in chars.items():
        c = cls(l)
        if c is None:
            continue
        for ka, al in chars.items():
            if ka == kl:
                continue
            be = [al[i] * pow(l[i], p - 2, p) % p for i in range(3)]
            V = {gi: [[al[gi - 1], c[gi - 1] * be[gi - 1] % p], [0, be[gi - 1]]] for gi in (1, 2, 3)}
            W = pull(V, phi)
            if not is_hom(W) or I_of(W) != I_of(V):
                bad += 1
            badp += not is_hom(pull(V, phi_bad))
            nmod += 1
    h2 &= bad == 0 and nmod == want
    plant &= badp > 0
    say(name, "level", n, "| record modules", nmod, "| mirror failures", bad, "| plant failures (t -> t^-1)", badp)
say("H2 holds:", h2)
say("plant fires:", plant)


# ---------- H3 ----------
def rank2(rows):
    rows = [list(r) for r in rows]
    rk, col = 0, 0
    ncol = len(rows[0]) if rows else 0
    while rk < len(rows) and col < ncol:
        piv = next((i for i in range(rk, len(rows)) if rows[i][col]), None)
        if piv is None:
            col += 1
            continue
        rows[rk], rows[piv] = rows[piv], rows[rk]
        for i in range(len(rows)):
            if i != rk and rows[i][col]:
                rows[i] = [(x + y) % 2 for x, y in zip(rows[i], rows[rk])]
        rk += 1
        col += 1
    return rk


# bits: h, o, e, r, q, y
J_, K_, D_, C_ = (1, 1, 0, 0, 0, 0), (1, 0, 1, 0, 0, 0), (0, 0, 0, 1, 0, 0), (0, 0, 0, 0, 1, 1)
DC = tuple((a + b) % 2 for a, b in zip(D_, C_))
R_hoe, R_qy, R_ry = (1, 1, 1, 0, 0, 0), (0, 0, 0, 0, 1, 1), (0, 0, 0, 1, 0, 1)


def free(syms, relsF):
    for s_ in syms:  # each symmetry must preserve each relation: <relation, symmetry> = 0 over F_2
        assert all(sum(a * b for a, b in zip(r_, s_)) % 2 == 0 for r_ in relsF), (s_, relsF)
    return (6 - rank2(relsF)) - rank2(syms)


counts = [free([J_, K_, D_, C_], [R_hoe, R_qy]), free([J_, K_, D_], [R_hoe, R_qy]),
          free([J_, K_, DC], [R_hoe, R_qy, R_ry]), free([J_, K_, DC], [R_hoe, R_qy])]
say("H3 counts (with C; without C; with D o C and criterion 3; with D o C, no criterion 3):", counts)
say("H3 holds:", counts == [0, 1, 0, 1])
