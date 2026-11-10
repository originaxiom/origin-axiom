#!/usr/bin/env python3
"""B1868 -- the web seat's sealed card on what concentrates under the move count (P-756 (b), the tau side), verified by main
with its own code and another method.  Data-free: no coupling, no frame output, no value of the nineteen; nothing is
compared with measurement.  The seat's code was read and not run.

The seat sampled 4 x 10^7 random moves.  Main uses no random numbers:

  nu      Minkowski's measure on (0, oo): the law of the endpoint of a history whose letters are fair.  Its distribution
          function is F(x) = ?(x)/2 on [0, 1] and 1 - ?(1/x)/2 beyond, ? being Minkowski's function, evaluated from the
          continued fraction.  nu gives each Stern-Brocot interval of depth n the mass 2^-n.
  Part 1  the exponent per move and the correlation dimension D2, from the Stern-Brocot intervals' lengths alone.
  Part 2  the mass of histories passing within delta of a point iy of the imaginary axis.  A history crossing that axis has
          endpoints xi > 0 and -zeta < 0, independent and each of law nu, and its distance d from iy is exact:
              sinh d = |xi zeta - y^2| / (y (xi + zeta)).
          So the mass is C_y(s) = (nu x nu){ |xi zeta - y^2| < s y (xi + zeta) }, s = sinh delta: for each xi an interval of
          zeta, whose nu-mass is a difference of two values of F.  The integral over xi is taken at the 2^n nu-midpoints of
          the Stern-Brocot intervals of depth n -- a quadrature, not a sample -- at three depths.
  Part 3  from C_1 the time a history spends within eps of i, by the exact chord length; its exponent against area's 2.
  Part 4  the walk at level 5, exactly: the distance from uniform after 10, 20, 40, 80 moves, and the second modulus.
  Part 5  the seat's exact facts at level 5 for the claim about all histories together (its script's F1 to F5 and F7).
  Part 6  three facts from the advisor seat's result of its ambiguity attack, in integers: the conserved quantity under a move;
          that a history's commutator with the ground is not a property of the cyclic history; and its divisibility by 25
          when the history commutes with the ground at level 5.

    python3 -B frontier/B1868_what_concentrates_under_the_move_count_verified/verification/move_count_tau_side.py
"""
import itertools
import math
from fractions import Fraction

import numpy as np

say = print
r3 = lambda x: "%.3f" % x
r4 = lambda x: "%.4f" % x

# ------------------------------------------------------------------ Part 1: the Stern-Brocot sums
def depth_pairs(n):
    """the denominators (q, q') of the endpoints of the 2^n Stern-Brocot intervals of (0, 1) at depth n; the length is 1/(q q')"""
    q = np.array([1], dtype=np.int64); r = np.array([1], dtype=np.int64)
    for _ in range(n):
        m = q + r
        q, r = np.concatenate([q, m]), np.concatenate([m, r])
    return q, r
NMAX = 22
logs = {}
for n in range(10, NMAX + 1):
    q, r = depth_pairs(n)
    logs[n] = np.log(q.astype(np.float64)) + np.log(r.astype(np.float64))        # -log(length)
M = {n: float(logs[n].mean()) for n in logs}
lam = {n: M[n + 1] - M[n] for n in range(10, NMAX)}
def d2_at(n):
    """beta with sum over depth n+1 of length^-beta = 4 x the same sum at depth n (the measure's square is 4^-n on every interval)"""
    f = lambda b: math.log(np.exp(b * (logs[n + 1] - logs[n + 1].max())).sum()) + b * logs[n + 1].max() - (math.log(np.exp(b * (logs[n] - logs[n].max())).sum()) + b * logs[n].max()) - math.log(4)
    lo, hi = 0.5, 1.2
    for _ in range(60):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if f(mid) < 0 else (lo, mid)
    return (lo + hi) / 2
D2 = {n: d2_at(n) for n in (12, 15, 18, 21)}
say("Part 1. Stern-Brocot sums to depth %d (main's own; exact integers, then logarithms)" % NMAX)
say("  the exponent per move (the growth of -log length per level): %s at depths 12, 16, 21  -> %.6f" % (", ".join("%.6f" % lam[n] for n in (12, 16, 21)), lam[21]))
say("  the correlation dimension D2 (the lengths' sum of order -D2 grows by 4 per level): %s at depths 12, 15, 18, 21  -> %.6f" % (", ".join("%.6f" % D2[n] for n in (12, 15, 18, 21)), D2[21]))
say("  the dimension of the measure itself, log 2 over the exponent: %.4f; D2 lies below it: %s" % (math.log(2) / lam[21], D2[21] < math.log(2) / lam[21]))
assert abs(lam[21] - 0.792425) < 2e-6 and abs(D2[21] - 0.844609) < 2e-6 and abs(D2[12] - D2[21]) < 5e-6

# ------------------------------------------------------------------ Minkowski's function, vectorised, with an exact control
def qmark(x):
    """Minkowski's ?(x) for an array x in [0, 1], from the continued fraction: ?(x) = 2 sum (-1)^(k+1) 2^-(a1 + ... + ak)"""
    x = np.asarray(x, dtype=np.float64)
    res = np.zeros_like(x); frac = x.copy(); expo = np.zeros_like(x); sign = 1.0
    alive = frac > 0
    for _ in range(70):
        if not alive.any(): break
        inv = np.where(alive, 1.0 / np.where(alive, frac, 1.0), 0.0)
        a = np.floor(inv)
        expo = expo + np.where(alive, a, 0.0)
        term = np.where(alive & (expo < 1000), np.exp2(1.0 - np.minimum(expo, 1000.0)), 0.0)
        res = res + sign * term
        frac = np.where(alive, inv - a, 0.0)
        alive = alive & (frac > 1e-15) & (expo < 80)
        sign = -sign
    return res
def F(x):
    """the distribution function of nu on [0, oo]"""
    x = np.asarray(x, dtype=np.float64)
    out = np.empty_like(x)
    small = x <= 1.0
    out[small] = qmark(np.clip(x[small], 0.0, 1.0)) / 2
    big = ~small
    with np.errstate(divide="ignore"):
        out[big] = 1.0 - qmark(np.where(np.isinf(x[big]), 0.0, 1.0 / x[big])) / 2
    return out
def qmark_exact(fr):
    """?(x) for a Fraction in [0, 1], exactly, as a Fraction"""
    res, sign, expo = Fraction(0), 1, 0
    p, q = fr.numerator, fr.denominator
    while p:
        a = q // p
        expo += a
        res += sign * Fraction(2, 2 ** expo)
        p, q = q - a * p, p
        sign = -sign
    return res
assert [qmark_exact(Fraction(1, 2)), qmark_exact(Fraction(1, 3)), qmark_exact(Fraction(2, 3)), qmark_exact(Fraction(2, 5))] == [Fraction(1, 2), Fraction(1, 4), Fraction(3, 4), Fraction(3, 8)]
rng_free = np.array([Fraction(k, 9973) for k in range(1, 9973, 37)])            # a fixed list of rationals, no random numbers
err = max(abs(float(qmark_exact(fr)) - float(qmark(np.array([float(fr)]))[0])) for fr in rng_free)
say("Minkowski's function: the vectorised evaluation against exact rational arithmetic on %d rationals: largest difference %.1e" % (len(rng_free), err))
assert err < 1e-9

# ------------------------------------------------------------------ Part 2: the correlation integrals on the imaginary axis
def midpoints(n):
    """the nu-midpoints of the 2^n Stern-Brocot intervals of (0, oo) at depth n: the mediants at depth n + 1"""
    a = np.array([0], dtype=np.int64); b = np.array([1], dtype=np.int64); c = np.array([1], dtype=np.int64); d = np.array([0], dtype=np.int64)
    for _ in range(n):
        ma, mb = a + c, b + d
        a, b, c, d = np.concatenate([a, ma]), np.concatenate([b, mb]), np.concatenate([ma, c]), np.concatenate([mb, d])
    return (a + c).astype(np.float64) / (b + d).astype(np.float64)
def C(y, s, xi):
    lo = np.maximum((y * y - s * y * xi) / (xi + s * y), 0.0)
    with np.errstate(divide="ignore", invalid="ignore"):
        hi = np.where(xi > s * y, (y * y + s * y * xi) / np.where(xi > s * y, xi - s * y, 1.0), np.inf)
    return float((F(hi) - F(lo)).mean())
XI = {n: midpoints(n) for n in (14, 16, 18)}
xs_sorted = np.sort(XI[18])
sym = float(np.abs(xs_sorted * xs_sorted[::-1] - 1).max())                  # the measure is symmetric under x -> 1/x: the midpoints pair off
say("Part 2. the mass of histories within delta of a point iy of the axis, C_y(s), s = sinh delta; quadrature at the 2^n nu-midpoints, n = 14, 16, 18")
say("  controls: the midpoints pair off under x -> 1/x (largest defect of the products from 1: %.1e); the mass with no restriction is %s; half the midpoints lie below 1: %s" % (
    sym, r4(C(1.0, 1e9, XI[14])), int((XI[18] < 1).sum()) == len(XI[18]) // 2))
assert sym < 1e-9 and abs(C(1.0, 1e9, XI[14]) - 1) < 1e-12 and int((XI[18] < 1).sum()) == len(XI[18]) // 2
KS = list(range(3, 13))
points = [("i", 1.0), ("i sqrt 2", math.sqrt(2)), ("i sqrt 3", math.sqrt(3)), ("1.34 i", 1.34)]
table = {}
for name, y in points:
    table[name] = {n: [C(y, 2.0 ** -k, XI[n]) for k in KS] for n in (14, 16, 18)}
def slopes(v): return [(math.log(v[j + 1]) - math.log(v[j])) / (-math.log(2)) for j in range(len(v) - 1)]
def fit(v, k0, k1):
    xs = [-k * math.log(2) for k in KS if k0 <= k <= k1]; ys = [math.log(v[KS.index(k)]) for k in KS if k0 <= k <= k1]
    mx, my = sum(xs) / len(xs), sum(ys) / len(ys)
    return sum((a - mx) * (b - my) for a, b in zip(xs, ys)) / sum((a - mx) ** 2 for a in xs)
res = {}
for name, y in points:
    v = table[name]
    stab = max(abs(v[18][j] / v[16][j] - 1) for j in range(len(KS)))
    e = {n: fit(v[n], 5, 11) for n in (14, 16, 18)}
    res[name] = e
    say("  %-9s exponent of C over s = 2^-5 .. 2^-11: %s at depths 14, 16, 18; minus 1: %s; local exponents at depth 18: %s; depth 18 against 16: within %.1e" % (
        name, ", ".join(r4(e[n]) for n in (14, 16, 18)), r4(e[18] - 1), " ".join(r3(x) for x in slopes(v[18])[2:9]), stab))
say("  the seat's card, slope of the density against area: -0.1542 at i (and -0.1557 by its second code), -0.0759 at i sqrt 2, +0.0061 at i sqrt 3, +0.0177 at 1.34 i (its Q4)")
say("  main: %s at i against D2 - 1 = %s; %s at i sqrt 2; %s at i sqrt 3; %s at 1.34 i" % (r4(res["i"][18] - 1), r4(D2[21] - 1), r4(res["i sqrt 2"][18] - 1), r4(res["i sqrt 3"][18] - 1), r4(res["1.34 i"][18] - 1)))
assert abs(res["i"][18] - D2[21]) < 0.01 and abs(res["i"][18] - res["i"][16]) < 0.003
assert abs((res["i sqrt 2"][18] - 1) - (-0.0759)) < 0.01 and abs(res["i sqrt 3"][18] - 1) < 0.03 and abs(res["1.34 i"][18] - 1) < 0.03

# ------------------------------------------------------------------ Part 3: the time spent within eps of i
ss = [2.0 ** (-k / 4.0) for k in range(8, 53)]                              # s from 2^-2 to 2^-13, four steps per octave
Cs = [C(1.0, s, XI[18]) for s in ss]
def mass(eps):
    """the expected length of a history's path inside the disc of radius eps about i, per crossing of the axis: the chord of a
    geodesic at distance d is 2 arccosh(cosh eps / cosh d); a Stieltjes sum against C"""
    tot, prev_d, prev_C = 0.0, 0.0, 0.0
    for s, c in sorted(zip(ss, Cs)):
        d = math.asinh(s)
        if d >= eps: break
        dm = (d + prev_d) / 2
        tot += (c - prev_C) * 2 * math.acosh(math.cosh(eps) / math.cosh(dm))
        prev_d, prev_C = d, c
    return tot
E = [2.0 ** -k for k in range(4, 11)]
ms = [mass(e) for e in E]
me = [(math.log(ms[j + 1]) - math.log(ms[j])) / (-math.log(2)) for j in range(len(ms) - 1)]
say("Part 3. the time within eps of i: local exponents for eps = 2^-4 .. 2^-10: %s; area's exponent is 2, so the density against area goes as eps^(%s on average)" % (
    " ".join(r3(x) for x in me), r3(sum(me) / len(me) - 2)))
say("  the time within eps of i is of order eps^%s: it tends to zero. No value of tau holds a share of the weight." % r3(sum(me) / len(me)))
assert abs(sum(me) / len(me) - (1 + D2[21])) < 0.02 and all(x > 1.7 for x in me)

# ------------------------------------------------------------------ Part 4: the walk at level 5, exactly
def sl2(N): return [(a, b, c, d) for a, b, c, d in itertools.product(range(N), repeat=4) if (a * d - b * c) % N == 1]
def mul(A, B, N): return ((A[0] * B[0] + A[1] * B[2]) % N, (A[0] * B[1] + A[1] * B[3]) % N, (A[2] * B[0] + A[3] * B[2]) % N, (A[2] * B[1] + A[3] * B[3]) % N)
G5 = sl2(5); idx = {g: i for i, g in enumerate(G5)}
Lm, Rm = (1, 1, 0, 1), (1, 0, 1, 1)
P = np.zeros((120, 120))
for g in G5:
    P[idx[mul(g, Lm, 5)], idx[g]] += 0.5
    P[idx[mul(g, Rm, 5)], idx[g]] += 0.5
p = np.zeros(120); p[idx[(1, 0, 0, 1)]] = 1.0
tv = {}
for step in range(1, 81):
    p = P @ p
    if step in (10, 20, 40, 80): tv[step] = 0.5 * np.abs(p - 1 / 120).sum()
mods = np.sort(np.abs(np.linalg.eigvals(P)))[::-1]
second = mods[1]; mult = int(np.sum(np.abs(mods - second) < 1e-9))
say("Part 4. the walk on SL(2, F5), 120 elements, exact transition matrix: distance from uniform after 10, 20, 40, 80 moves: %s" % ", ".join("%.2e" % tv[k] for k in (10, 20, 40, 80)))
say("  the second modulus of the step is %.6f (sqrt 3 / 2 = %.6f), %d times; the rate between 40 and 80 moves: %.4f per move" % (second, math.sqrt(3) / 2, mult, (tv[80] / tv[40]) ** (1 / 40)))
assert len(G5) == 120 and abs(second - math.sqrt(3) / 2) < 1e-9 and mult == 8 and tv[80] < 1e-3 and tv[10] > tv[20] > tv[40] > tv[80]

# ------------------------------------------------------------------ Part 5: the seat's exact facts at level 5 (its convention: L = [[1,0],[1,1]], R = [[1,1],[0,1]])
def act(A, v, N): return ((A[0] * v[0] + A[1] * v[1]) % N, (A[2] * v[0] + A[3] * v[1]) % N)
def eigenlines(N):
    seen, out = set(), []
    for v in [(a, b) for a in range(N) for b in range(N) if math.gcd(math.gcd(a, b), N) == 1]:
        Cg = frozenset(((c * v[0]) % N, (c * v[1]) % N) for c in range(N))
        if Cg not in seen: seen.add(Cg); out.append((v, Cg))
    return out
def fixes_set(A, Cg, N): return frozenset(act(A, v, N) for v in Cg) == Cg
Ls, Rs, Sm = (1, 0, 1, 1), (1, 1, 0, 1), (0, -1, 1, 0)
LR5 = mul(Ls, Rs, 5)
EL = eigenlines(5)
fixed_by_LR = [v for v, Cg in EL if fixes_set(LR5, Cg, 5)]
v0 = fixed_by_LR[0]
st_vec = [g for g in G5 if act(g, v0, 5) == v0]
st_line = [g for g in G5 if act(g, v0, 5) in (v0, ((-v0[0]) % 5, (-v0[1]) % 5))]
st_eig = [g for g in G5 if fixes_set(g, dict(EL)[v0], 5)]
tr = lambda g: (g[0] + g[3]) % 5
lines5 = {frozenset([v, ((-v[0]) % 5, (-v[1]) % 5)]) for v in [(a, b) for a in range(5) for b in range(5) if (a, b) != (0, 0)]}
fix_line = sorted({tr(g) for g in G5 if any(frozenset(act(g, v, 5) for v in ln) == ln for ln in lines5)})
fix_eig = sorted({tr(g) for g in G5 if any(fixes_set(g, Cg, 5) for _, Cg in EL)})
none_line = sorted(set(range(5)) - set(fix_line)); none_eig = sorted(set(range(5)) - set(fix_eig))
S5 = tuple(x % 5 for x in Sm)
s_fixed = [v for v, Cg in EL if fixes_set(S5, Cg, 5)]
say("Part 5. level 5, the seat's exact facts: LR has trace %d and fixes %d eigenline, spanned by %s, acting on it by %d; stabilisers of a vector, a line, an eigenline: %d, %d, %d" % (
    tr(LR5), len(fixed_by_LR), v0, next(c for c in range(5) if act(LR5, v0, 5) == ((c * v0[0]) % 5, (c * v0[1]) % 5)), len(st_vec), len(st_line), len(st_eig)))
say("  traces of elements fixing some line: %s (none: %s); fixing some eigenline: %s (none: %s); S fixes %d of the %d eigenlines: %s" % (fix_line, none_line, fix_eig, none_eig, len(s_fixed), len(EL), s_fixed))
f7 = []
for N in range(2, 14):
    GN_S = tuple(x % N for x in Sm); ST = mul(GN_S, (1, 1, 0, 1), N)
    ELN = eigenlines(N)
    f7.append((N, sum(1 for _, Cg in ELN if fixes_set(GN_S, Cg, N)), sum(1 for _, Cg in ELN if fixes_set(ST, Cg, N))))
say("  N: eigenlines fixed by S, by ST, for N = 2 .. 13: %s" % " ".join("%d:%d,%d" % t for t in f7))
assert (len(st_vec), len(st_line), len(st_eig)) == (5, 10, 20) and fix_line == [2, 3] and fix_eig == [0, 2, 3] and len(s_fixed) == 2
assert f7 == [(2, 1, 0), (3, 0, 1), (4, 0, 0), (5, 2, 0), (6, 0, 0), (7, 0, 2), (8, 0, 0), (9, 0, 0), (10, 2, 0), (11, 0, 0), (12, 0, 0), (13, 2, 2)]

# ------------------------------------------------------------------ Part 6: three facts from the advisor seat's attack result (integers)
def m2(A, B): return ((A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]), (A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]))
def inv2(A): return ((A[1][1], -A[0][1]), (-A[1][0], A[0][0]))
def tr2(A): return A[0][0] + A[1][1]
LL, RR, I2 = ((1, 1), (0, 1)), ((1, 0), (1, 1)), ((1, 0), (0, 1))
def wd(w):
    M = I2
    for c in w: M = m2(M, LL if c == "L" else RR)
    return M
def ctr(w, g="LR"):
    W, G = wd(w), wd(g)
    return tr2(m2(m2(W, G), m2(inv2(W), inv2(G))))
# (i) the quantity kappa = x^2 + y^2 + z^2 - xyz - 2 (x, y, z the traces of a, b, ab) is unchanged by the move a -> ab
# checked on every integer triple with entries from -6 to 6: both sides are polynomials of degree at most 4 in each variable, and 13
# points in each variable decide a polynomial identity of that degree, so this is a proof and not a sample
grid = range(-6, 7)
ok_k = all((z * z + y * y + (z * y - x) ** 2 - z * y * (z * y - x) - 2) == (x * x + y * y + z * z - x * y * z - 2) for x in grid for y in grid for z in grid)
# (ii) the commutator with the ground depends on where a repeating history is started
rot = lambda w: [w[s:] + w[:s] for s in range(len(w))]
vals_llr = sorted({ctr(w) - 2 for w in rot("LLR")}); vals_llrr = sorted({ctr(w) - 2 for w in rot("LLRR")})
# (iii) if a history commutes with the ground at level 5, the commutator's trace less two is divisible by 25
com5 = lambda w: all((a - b) % 5 == 0 for ra, rb in zip(m2(wd(w), wd("LR")), m2(wd("LR"), wd(w))) for a, b in zip(ra, rb))
hist = ["".join(tt) for n in range(2, 12) for tt in itertools.product("LR", repeat=n)]
comm = [w for w in hist if com5(w)]
div25 = all((ctr(w) - 2) % 25 == 0 for w in comm)
other = sorted({(ctr(w) - 2) % 25 for w in hist if not com5(w)})
say("Part 6. from the advisor seat's attack result: the conserved quantity is unchanged by a move, as a polynomial identity (all 2197 integer triples from -6 to 6): %s" % ok_k)
say("  the trace of a history's commutator with the ground LR, less two, over the rotations of LLR: %s; of LLRR: %s  -> it is not a property of the cyclic history" % (vals_llr, vals_llrr))
say("  of the %d words of length 2 to 11, %d commute with the ground at level 5, and for all of them that number is divisible by 25: %s (run of 6: %d; (2,2,2): %d); for the others it takes %d residues mod 25" % (
    len(hist), len(comm), div25, ctr("LLLLLLRLR") - 2, ctr("LLRRLLRLR") - 2, len(other)))
assert ok_k and len(vals_llr) > 1 and len(vals_llrr) > 1 and div25 and com5("LLLLLLRLR") and (ctr("LLLLLLRLR") - 2) % 25 == 0 and len(other) > 1
