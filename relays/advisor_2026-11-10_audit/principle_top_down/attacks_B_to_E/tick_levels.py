#!/usr/bin/env python3
"""The record's level structures read again with the exchange (the tick's second debt), and what the draft forbids
at a level. Integers only; nothing is measured. Sealed with PREREGISTRATION.md before it was run.

    python3 -B tick_levels.py [B]       B = the largest departure enumerated, in letters (default 14)

A departure is a run sequence S = (r_1 .. r_m), r_1 != 1 and r_m != 1, put in place of m runs of the golden ground
(all runs 1). E(S) is the departure's matrix against the matrix of what it replaced. Two ways to write it:
  two acts:  D_alt(S) = L^r1 R^r2 L^r3 ..          against  L R L ..  (m letters)
  the tick:  D_tick(S) = G(r_1) .. G(r_m), G(c) = L^(c-1).F          against  F^m"""
import sys, collections

B = int(sys.argv[1]) if len(sys.argv) > 1 else 14
I2 = (1, 0, 0, 1); L = (1, 1, 0, 1); R = (1, 0, 1, 1); P = (0, 1, 1, 0)
def mul(A, C): return (A[0]*C[0]+A[1]*C[2], A[0]*C[1]+A[1]*C[3], A[2]*C[0]+A[3]*C[2], A[2]*C[1]+A[3]*C[3])
def mm(A, C, N): return tuple(x % N for x in mul(A, C))
def red(A, N): return tuple(x % N for x in A)
def det(A): return A[0]*A[3] - A[1]*A[2]
def inv(A):
    d = det(A); assert d in (1, -1)
    return (A[3]*d, -A[1]*d, -A[2]*d, A[0]*d)
F = mul(L, P); A_LR = mul(L, R)
def G(c): return (c, 1, 1, 0)
def Lp(r): return (1, r, 0, 1)
def Rp(r): return (1, 0, r, 1)
assert mul(F, F) == A_LR and mul(inv(F), F) == I2 and mul(G(3), I2) == mul(mul(L, L), F)

out = []
def say(s=""):
    out.append(s); print(s, flush=True)

# ---------------------------------------------------------------- H11: the group at each level, with and without the exchange
def closure(gens, N):
    seen = {I2}; todo = [I2]
    while todo:
        X = todo.pop()
        for g in gens:
            Z = mm(X, g, N)
            if Z not in seen: seen.add(Z); todo.append(Z)
    return seen
def units(N):
    from math import gcd
    return [u for u in range(1, N) if gcd(u, N) == 1] if N > 1 else [0]
def projective(Gs, N):
    us = units(N)
    return len({min(tuple((u * x) % N for x in X) for u in us) for X in Gs})
say("H11  THE GROUP OF THE ACTS AT LEVEL N: the two acts (L, R); with the exchange (L, R, P)")
say("     N | two acts | with exchange | two acts up to scalars | with exchange up to scalars | scalars inside (with exchange) | -1 a square mod N")
for N in (2, 3, 4, 5, 7, 8, 9, 11, 13):
    G2 = closure((red(L, N), red(R, N)), N); G3 = closure((red(L, N), red(R, N), red(P, N)), N)
    sc = sorted(u for u in units(N) if (u % N, 0, 0, u % N) in G3)
    sq = any((c * c + 1) % N == 0 for c in range(N))
    p2 = projective(G2, N); p3 = projective(G3, N)
    say("    %2d | %8d | %13d | %22d | %27d | %-30s | %s%s" % (N, len(G2), len(G3), p2, p3, sc, sq,
        "   <- up to scalars the exchange adds nothing" if p3 == p2 else ""))

# ---------------------------------------------------------------- H12, H13: level 5
N = 5
G2 = closure((red(L, N), red(R, N)), N); G3 = closure((red(L, N), red(R, N), red(P, N)), N)
centre = sorted(X for X in G3 if all(mm(X, g, N) == mm(g, X, N) for g in (red(L, N), red(R, N), red(P, N))))
say("\nH12, H13  AT LEVEL 5")
say("    the centre of the group with the exchange: %s" % centre)
U = red(tuple(2 * x for x in F), N)                       # F / 3, since 3.2 = 1 mod 5
Nil = tuple((a - b) % N for a, b in zip(U, I2))
def order(M, N):
    X = red(M, N); k = 1
    while X != I2:
        X = mm(X, M, N); k += 1
    return k
say("    F = 3.U with U = %s (3.U = %s, F = %s); (U - I)^2 = %s mod 5; order of F: %d, of L.R: %d" % (
    U, tuple((3 * x) % N for x in U), red(F, N), mm(Nil, Nil, N), order(F, N), order(A_LR, N)))
def act(M, v): return ((M[0]*v[0] + M[1]*v[1]) % N, (M[2]*v[0] + M[3]*v[1]) % N)
v = (1, 2)
say("    the mark v = (1,2): L.R v = %s = %d.v; F v = %s = %d.v; F^2 v = %s" % (act(A_LR, v), next(u for u in range(N) if tuple((u*x) % N for x in v) == act(A_LR, v)),
    act(F, v), next(u for u in range(N) if tuple((u*x) % N for x in v) == act(F, v)), act(mul(F, F), v)))
vec = [(a, b) for a in range(N) for b in range(N) if (a, b) != (0, 0)]
def kept(M, how):
    if how == "sign": return [w for w in vec if act(M, w) in (w, tuple((-x) % N for x in w))]
    return [w for w in vec if any(act(M, w) == tuple((u*x) % N for x in w) for u in range(1, N))]
say("    non-zero vectors kept up to sign by L.R: %d; by F: %d.   kept up to any scalar by L.R: %d; by F: %d" % (
    len(kept(A_LR, "sign")), len(kept(F, "sign")), len(kept(A_LR, "any")), len(kept(F, "any"))))

# ---------------------------------------------------------------- the departures, in both grammars
say("\nH12  EVERY DEPARTURE WITH AT MOST %d LETTERS, written with two acts and with the tick" % B)
Fpow = [I2]
for k in range(1, 40): Fpow.append(mul(Fpow[-1], F))
Fpow_mod = [red(X, N) for X in Fpow[:20]]
cnt = 0; diff = 0
sets = collections.defaultdict(list)
def rec(S, Dt, Da, Dbg, n):
    global cnt, diff
    i = len(S)
    X = Lp if i % 2 == 0 else Rp
    for r in range(1, B - n + 1):
        if i == 0 and r == 1: continue
        S2 = S + (r,); Dt2 = mul(Dt, G(r)); Da2 = mul(Da, X(r)); Dbg2 = mul(Dbg, X(1))
        if r != 1:
            cnt += 1; m = len(S2)
            Et = mul(Dt2, inv(Fpow[m])); Ea = mul(Da2, inv(Dbg2))
            if Et != Ea: diff += 1
            E = red(Ea, N); letters = n + r
            if E == I2: sets["charge+"].append((letters, S2))
            if E in (I2, (4, 0, 0, 4)): sets["charge+-"].append((letters, S2))
            if E in ((2, 0, 0, 2), (3, 0, 0, 3)): sets["scalar 2 or 3"].append((letters, S2))
            if mm(E, A_LR, N) == mm(A_LR, E, N): sets["line, against L.R"].append((letters, S2))
            if mm(E, F, N) == mm(F, E, N): sets["line, against F"].append((letters, S2))
            Dm = red(Dt2, N)
            if any(Dm == tuple((u * x) % N for x in Fk) for u in range(1, N) for Fk in Fpow_mod): sets["a scalar times a power of F"].append((letters, S2))
        if n + r < B: rec(S2, Dt2, Da2, Dbg2, n + r)
rec((), I2, I2, I2, 0)
say("    departures enumerated: %d;  E written with the tick differs from E written with two acts: %d times" % (cnt, diff))
for k in ("charge+", "charge+-", "scalar 2 or 3", "line, against L.R", "line, against F", "a scalar times a power of F"):
    h = sorted(sets.get(k, []))
    if not h: say("    %-28s none" % k); continue
    n0 = h[0][0]; least = [s for l, s in h if l == n0]; nxt = next(((l, s) for l, s in h if l > n0), None)
    say("    %-28s %5d allowed; least %d letters: %s; next: %s" % (k, len(h), n0, least[:6], nxt))
say("    the line reading gives the same departures against L.R and against F: %s" % (sorted(sets["line, against L.R"]) == sorted(sets["line, against F"])))
say("    the line reading is 'a scalar times a power of F': %s" % (sorted(sets["line, against F"]) == sorted(sets["a scalar times a power of F"])))

open(__file__.replace(".py", "_out.txt"), "w").write("\n".join(out) + "\n")
