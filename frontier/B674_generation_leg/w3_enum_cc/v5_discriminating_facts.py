# W3 ENUMERATION (cc seat) — the discriminating facts, computed exactly.
# Governing: PREREG_W3_DECISION.md (563a2858) + ADDENDUM_1.
# Everything here is exact rational arithmetic (fractions.Fraction).
#
# FACT 1  (targets, from scratch — no banked JSON loaded): the reduced
#   target streams F1 = G(q)*(q;q)^{2/5}, F2 = H(q)*(q;q)^{2/5}
#   (the banked identity F_a = N_a*(q;q)^{-3/5}, N1=(q;q)G, N2=(q;q)H)
#   have PURE 5-power denominators with v5 growing without bound;
#   checkpoints v5 = 1, 12, 49, 99, 146 at n = 1, 10, 40, 80, 119
#   (the banked W33/W2 numbers, reproduced independently), secant
#   slopes between checkpoints inside [1.205, 1.25].
#   -> feeds E2 (an eventually-periodic stream takes finitely many
#      values, hence bounded v5: contradiction), E3 (any v5-bounded
#      coefficient ring mismatches from n=1 and the gap grows), and
#      the C7 motivation (linear v5 growth = per-grade S-count).
# FACT 2  (the non-S depth letters are 5-integral): every banked
#   non-S "letter" a depth family could accumulate — T-monomials
#   (roots of unity), the cubic's Eisenstein data (Z[omega]), the
#   sum-rule constant -(7983360/13)*omega — has v5 = 0: 5 does not
#   divide 13 (exact), roots of unity are units, and 5 is inert in
#   Q(omega) (x^2+x+1 irreducible mod 5 — checked), so Z[omega]
#   elements have v5 >= 0. Accumulating such letters to ANY depth
#   leaves v5(denominator) = 0 at every grade: first mismatch with
#   the targets at n = 1 (v5 = 1), gap -> 146 by n = 119.
# FACT 3  (fixed constants cannot bridge): for fixed c != 0 in a
#   number field, v5(c * x) = v5(c) + v5(x): a fixed shift. Max
#   target v5(denom) in-window = 146 > any fixed shift: computed
#   witness printed.

from fractions import Fraction

N = 120  # coefficients 0..119

# ---- (q;q)_infty truncated ----
def euler_product(N):
    P = [Fraction(0)] * N
    P[0] = Fraction(1)
    for k in range(1, N):
        # multiply P by (1 - q^k)
        for n in range(N - 1, k - 1, -1):
            P[n] -= P[n - k]
    return P

E = euler_product(N)

# ---- P^a for rational a, p0 = 1, via the exact ODE recurrence:
#      n c_n = a*sum_{k=1..n} k p_k c_{n-k} - sum_{j=1..n-1} j c_j p_{n-j}
def rational_power(P, a, N):
    c = [Fraction(0)] * N
    c[0] = Fraction(1)
    for n in range(1, N):
        s = Fraction(0)
        for k in range(1, n + 1):
            s += a * k * P[k] * c[n - k]
        for j in range(1, n):
            s -= j * c[j] * P[n - j]
        c[n] = s / n
    return c

A = rational_power(E, Fraction(2, 5), N)   # (q;q)^{2/5}

# ---- Rogers-Ramanujan G, H (exact) ----
def rr_series(shift, N):
    # G: shift=0 (q^{n^2}); H: shift=1 (q^{n^2+n})
    out = [Fraction(0)] * N
    out[0] = Fraction(1)
    n = 1
    while n * n + shift * n < N:
        # q^{n^2+shift*n} / (q;q)_n
        num = [Fraction(0)] * N
        num[n * n + shift * n] = Fraction(1)
        # divide by (1-q)...(1-q^n): multiply by each 1/(1-q^k) = geometric
        for k in range(1, n + 1):
            for m in range(k, N):
                num[m] += num[m - k]
        for m in range(N):
            out[m] += num[m]
        n += 1
    return out

G = rr_series(0, N)
H = rr_series(1, N)

def mul(P, Q, N):
    R = [Fraction(0)] * N
    for i in range(N):
        if P[i] == 0:
            continue
        for j in range(N - i):
            R[i + j] += P[i] * Q[j]
    return R

F1 = mul(G, A, N)
F2 = mul(H, A, N)

def v5_of_denominator(x):
    d = x.denominator
    v = 0
    while d % 5 == 0:
        d //= 5
        v += 1
    return v, d  # d = the 5-free part of the denominator

print("FACT 1 — the reduced target streams (computed from scratch)")
print("anchors: F1[0]=%s F1[1]=%s   F2[0]=%s F2[1]=%s" % (F1[0], F1[1], F2[0], F2[1]))
assert F1[0] == 1 and F1[1] == Fraction(3, 5), "F1 anchor mismatch"
assert F2[0] == 1 and F2[1] == Fraction(-2, 5), "F2 anchor mismatch"
print("  (banked STEP3 anchors 1, 3/5 / 1, -2/5: REPRODUCED)")

pure = True
v5_1 = []
v5_2 = []
for n in range(N):
    v, d = v5_of_denominator(F1[n])
    v5_1.append(v)
    if d != 1:
        pure = False
    v, d = v5_of_denominator(F2[n])
    v5_2.append(v)
    if d != 1:
        pure = False
print("pure 5-power denominators, both streams, all n < %d: %s" % (N, pure))
assert pure

checkpoints = [1, 10, 40, 80, 119]
banked = [1, 12, 49, 99, 146]
got1 = [v5_1[n] for n in checkpoints]
got2 = [v5_2[n] for n in checkpoints]
print("v5(denom) F1 at n=%s : %s  (banked: %s)" % (checkpoints, got1, banked))
print("v5(denom) F2 at n=%s : %s" % (checkpoints, got2))
assert got1 == banked, "banked v5 checkpoints NOT reproduced on F1"

secants = []
for i in range(1, len(checkpoints)):
    s = Fraction(got1[i] - got1[i - 1], checkpoints[i] - checkpoints[i - 1])
    secants.append(s)
print("secant slopes between checkpoints:", ["%s=%.4f" % (s, float(s)) for s in secants])
lo, hi = Fraction(1205, 1000), Fraction(125, 100)
assert all(lo <= s <= hi for s in secants), "secants outside [1.205, 1.25]"
print("all secants in [1.205, 1.25]: True  (the banked linear-growth window)")
print("monotone growth check: v5 non-decreasing on n=1..119:",
      all(v5_1[n + 1] >= v5_1[n] for n in range(1, N - 1)))
print("max v5 in-window:", max(v5_1), "(unbounded growth in-window; an")
print("  eventually-periodic stream takes finitely many values -> bounded v5:")
print("  CONTRADICTION -> the targets are NOT eventually periodic [feeds E2])")

print()
print("FACT 2 — every banked non-S depth letter is 5-integral")
# 5 inert in Q(omega): x^2+x+1 mod 5 has no root
roots = [x for x in range(5) if (x * x + x + 1) % 5 == 0]
print("roots of x^2+x+1 mod 5:", roots, "-> 5 inert in Q(omega):", roots == [])
assert roots == []
import math
print("gcd(13,5) =", math.gcd(13, 5), "-> the sum-rule constant -(7983360/13)*omega has v5 = 0")
assert math.gcd(13, 5) == 1
print("roots of unity are units (norm 1): v5 = 0 per T/congruence letter (two-line theorem,")
print("  the ADJUDICATION_BIFOCAL_OBJECTION mechanism); Z[omega] elements: v5 >= 0 (5 inert).")
print("=> ANY depth family in non-S letters has v5(denom) = 0 at EVERY grade;")
print("   first mismatch with the targets at n = 1 (v5 = 1); gap grows to 146 by n = 119.")

print()
print("FACT 3 — no fixed constant bridges a growing v5 gap")
print("v5(c*x) = v5(c) + v5(x); a fixed c shifts v5 by the constant v5(c).")
print("Target v5(denom) spans 1 -> %d in-window: for any fixed shift s," % max(v5_1))
print("  matching at one n forces mismatch at every n with v5 difference != 0;")
print("  in-window witness: v5 takes %d distinct values." % len(set(v5_1[1:])))

print()
print("ALL ASSERTIONS PASSED — facts banked for ENUM_CC.md")
