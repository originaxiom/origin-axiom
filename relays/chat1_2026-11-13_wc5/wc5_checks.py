#!/usr/bin/env python3
"""W-C5: a second computation of B1914 and B1915 on this seat's own code, and the agy lane's cusp statement.

Data-free. Exact integer arithmetic and sympy; nothing of main's arcs is read by this script.

    python3 -I wc5_checks.py

DEFINITIONS (this seat's reading of M15; main's own definitions are read only after this file is committed):
  A = LR = [[2,1],[1,1]] with L = [[1,1],[0,1]], R = [[1,0],[1,1]], acting on columns. D = diag(1,-1), A' = D A D.
  A map is an integer matrix X with det X = ±1 and X S X^-1 = T^e (e = ±1), for sides S, T in {A, A'}.
  Its orientation sign is det X times e. Mod 5, A has one eigenline, spanned by v_A = (1, 2); A' has v_A' = D v_A
  = (1, 3). The scalar of X is the λ in F_5 with X v_S = λ v_T (mod 5).
  Modulo the powers of A: X ~ X A^k. Since A acts on its line by -1 mod 5, the scalar of a class is a pair {λ, -λ}.
  A placement is (side, hand, twin) with side in {A, A'}, hand = ±1, twin = ±1: eight in all. A map from S to T sends
  (S, h, t) to (T, h·sign, t·τ), where τ = +1 if its scalar is ±1 and τ = -1 if it is ±2.

EXPECTATIONS, written before the run:
  P1  The search (entries |x| <= 12) finds maps of A to itself, X A X^-1 = A or A^-1, in exactly 8 classes modulo the
      powers of A: ±I, ±M, ±J, ±JM, with M = [[1,1],[1,0]] (M^2 = A) and J = [[0,1],[-1,0]].
  P2  Every map found keeps A's line mod 5. The 4 classes with orientation sign +1 have scalars {1, 4} = ±1; the 4 with
      sign -1 have scalars {2, 3} = ±2. Main's statement holds on every class.
  P3  Control: the opposite statement (keeping ones by ±2) fails on at least one class.
  Q1  The eight placements fall into 2 orbits under all maps between the two bundles (4 placements each), and into 4
      orbits under the orientation-keeping ones, each of which holds one placement of side A and one of side A'.
  Q2  The orbit of (A, +1, +1) under all maps holds (A, -1, -1): hand and twin flip together. No map keeps the hand
      and swaps the twin. Control: with the twin left out of the action (τ = +1 always) the orbits are again 2, but
      the orbit of (A, +1, +1) then does not hold (A, -1, -1).
  R1  With w = exp(2πi z), z = x + i y: |dw|^2 / (|w| log|w|)^2 = |dz|^2 / y^2.
  R2  For w^(-n) (dw)^(a/2), |s|^2 dA = r^(a-2n-1) |log r|^(a-2) dr dθ near r = 0, which with t = -log r is
      e^(-(a-2n) t) t^(a-2) dt dθ on (T, ∞). It is finite exactly when a - 2n > 0, or a - 2n = 0 and a - 2 < -1.
      This equals n <= b(a), with b(a) = (a-1)//2 for a >= 1 and a//2 for a <= 0, on every integer a in [-8, 9] and
      n in [-8, 8], checked against sympy's integral on the same grid.
  R3  Control: b'(a) = a//2 for every a (the rule without its split) disagrees with the integral at some a >= 1.
"""
import itertools
import sympy as sp

A = sp.Matrix([[2, 1], [1, 1]])
L, R = sp.Matrix([[1, 1], [0, 1]]), sp.Matrix([[1, 0], [1, 1]])
D = sp.diag(1, -1)
AP = D * A * D
assert L * R == A
SIDES = {"A": A, "A'": AP}
LINE = {"A": sp.Matrix([1, 2]), "A'": D * sp.Matrix([1, 2])}
for s in SIDES:  # each line is an eigenline mod 5
    w = (SIDES[s] + sp.eye(2)) * LINE[s]
    assert all(x % 5 == 0 for x in w)
B = 12
APOW = {k: A ** k for k in range(-12, 13)}
out = []


def say(*a):
    print(*a)


def scalar(X, s, t):
    v, w = (X * LINE[s]).applyfunc(lambda x: x % 5), LINE[t]
    for lam in range(5):
        if all((lam * w[i] - v[i]) % 5 == 0 for i in range(2)):
            return lam
    return None


def maps(s, t):
    S, T = SIDES[s], SIDES[t]
    Ti = T.inv()
    found = []
    for a, b, c, d in itertools.product(range(-B, B + 1), repeat=4):
        det = a * d - b * c
        if det not in (1, -1):
            continue
        X = sp.Matrix([[a, b], [c, d]])
        for e, Te in ((1, T), (-1, Ti)):
            if X * S == Te * X:
                found.append((X, det, e))
    return found


# ---- P: B1914
own = maps("A", "A")
key = lambda X: tuple(X)
seen, classes = {}, []
for X, det, e in own:
    if key(X) in seen:
        continue
    cls = len(classes)
    classes.append((X, det, e))
    for k, P in APOW.items():
        seen.setdefault(key(X * P), cls)
for X, det, e in own:
    assert key(X) in seen
say("P1 maps found:", len(own), "classes modulo the powers of A:", len(classes))
rows = []
for X, det, e in classes:
    members = [Y for Y, _, _ in own if seen[key(Y)] == seen[key(X)]]
    lams = sorted({scalar(Y, "A", "A") for Y in members})
    small = min(members, key=lambda Y: (max(abs(x) for x in Y), tuple(Y)))
    rows.append((list(small), det, e, det * e, lams))
for r in sorted(rows, key=lambda r: (-r[3], r[0])):
    say("P1 class: smallest", r[0], "det", r[1], "exponent", r[2], "orientation sign", r[3], "scalars mod 5", r[4])
M, J = sp.Matrix([[1, 1], [1, 0]]), sp.Matrix([[0, 1], [-1, 0]])
named = {"I": sp.eye(2), "M": M, "J": J, "JM": J * M}
say("P1 named classes present:", {n + s: key(sg * X) in seen for n, X in named.items() for s, sg in (("+", 1), ("-", -1))})
say("P1 the eight named classes are distinct:", len({seen[key(sg * X)] for X in named.values() for sg in (1, -1)}) == 8)
every_keeps_line = all(scalar(X, "A", "A") is not None for X, _, _ in own)
holds = all((set(r[4]) <= {1, 4}) if r[3] == 1 else (set(r[4]) <= {2, 3}) for r in rows)
say("P2 every map keeps A's line mod 5:", every_keeps_line, "; main's statement holds on every class:", holds)
say("P2 classes by sign: keeping", sum(r[3] == 1 for r in rows), "reversing", sum(r[3] == -1 for r in rows))
opposite = all((set(r[4]) <= {2, 3}) if r[3] == 1 else (set(r[4]) <= {1, 4}) for r in rows)
say("P3 control, the opposite statement holds on every class:", opposite)

# ---- Q: B1915
allmaps = []
for s in SIDES:
    for t in SIDES:
        for X, det, e in maps(s, t):
            lam = scalar(X, s, t)
            assert lam is not None and lam != 0
            allmaps.append((s, t, det * e, 1 if lam in (1, 4) else -1))
say("Q0 maps between the bundles found:", len(allmaps), "; of them orientation-keeping:", sum(m[2] == 1 for m in allmaps))
PLACES = [(s, h, t) for s in SIDES for h in (1, -1) for t in (1, -1)]


def orbits(ms, use_twin=True):
    parent = {p: p for p in PLACES}

    def find(p):
        while parent[p] != p:
            p = parent[p]
        return p
    for s, t, sign, tau in ms:
        for (ps, h, tw) in PLACES:
            if ps == s:
                q = (t, h * sign, tw * (tau if use_twin else 1))
                parent[find((ps, h, tw))] = find(q)
    groups = {}
    for p in PLACES:
        groups.setdefault(find(p), []).append(p)
    return sorted(sorted(g) for g in groups.values())


all_orb = orbits(allmaps)
keep_orb = orbits([m for m in allmaps if m[2] == 1])
say("Q1 orbits under every map:", len(all_orb), [len(g) for g in all_orb])
for g in all_orb:
    say("Q1   ", g)
say("Q1 orbits under the orientation-keeping maps:", len(keep_orb),
    "; each holds one placement of each side:", all(sorted(p[0] for p in g) == ["A", "A'"] for g in keep_orb))
for g in keep_orb:
    say("Q1   ", g)
together = lambda orb: any(("A", 1, 1) in g and ("A", -1, -1) in g for g in orb)
say("Q2 the orbit of (A, +1, +1) holds (A, -1, -1):", together(all_orb), "; a map keeps the hand and swaps the twin:",
    any(m[2] == 1 and m[3] == -1 for m in allmaps), "; a map swaps the hand and keeps the twin:",
    any(m[2] == -1 and m[3] == 1 for m in allmaps))
nt = orbits(allmaps, use_twin=False)
say("Q2 control, the twin left out: orbits", len(nt), "; the orbit of (A, +1, +1) holds (A, -1, -1):", together(nt))

# ---- R: the cusp
x, y = sp.symbols("x y", real=True)
z = x + sp.I * y
w = sp.exp(2 * sp.pi * sp.I * z)
dwdz = sp.diff(w, x)  # holomorphic: dw = w'(z) dz
lhs = sp.simplify(sp.Abs(dwdz) ** 2 / (sp.Abs(w) * sp.log(sp.Abs(w))) ** 2)
say("R1 |dw|^2/(|w| log|w|)^2 divided by |dz|^2/y^2:", sp.simplify(lhs * y ** 2))
t = sp.symbols("t", positive=True)


def finite(a, n):
    c = a - 2 * n
    I = sp.integrate(t ** (a - 2) * sp.exp(-c * t), (t, 1, sp.oo))
    return bool(I.is_finite)


def b(a):
    return (a - 1) // 2 if a >= 1 else a // 2


grid = [(a, n) for a in range(-8, 10) for n in range(-8, 9)]
by_integral = {(a, n): finite(a, n) for a, n in grid}
by_rule = {(a, n): n <= b(a) for a, n in grid}
by_hand = {(a, n): (a - 2 * n > 0) or (a - 2 * n == 0 and a - 2 < -1) for a, n in grid}
say("R2 grid points:", len(grid), "; the rule agrees with sympy's integral at all:", by_integral == by_rule,
    "; the convergence test of the header agrees too:", by_hand == by_integral)
say("R2 where the boundary 2n = a falls: finite at", sorted(a for a, n in grid if 2 * n == a and by_integral[(a, n)]),
    "; infinite at", sorted(a for a, n in grid if 2 * n == a and not by_integral[(a, n)]))
wrong = {(a, n): n <= a // 2 for a, n in grid}
say("R3 control, b'(a) = a//2: disagrees at", sorted({a for a, n in grid if wrong[(a, n)] != by_integral[(a, n)]}))
