"""B1957: agy-exp's X-FUNNEL campaign (four result notes, read in full through the mask): the exact facts under its
statements, computed on main.  Nothing of the seat's is run; its numerical outputs inside its own model are not
recomputed and are registered as conditional on the premises its own page of premises names.
 G1  under w -> w M^-1 the 24 points of order 5 fall into orbits of 2, 2, 10 and 10: the four points with
     w M^-1 = -w, namely (1,2), (2,4), (3,1), (4,3) over 5, are two orbits {w, -w} under M^-1 and one cycle of four
     under J^-1.  So the note's '4 + 10 + 10' is the line and two orbits, not three orbits of the monodromy.
 G2  the phase of frame C's theta product under tau -> tau + 5 is exp(2 pi i (q_L^2 + q_R^2) k^2/5): q_L^2 + q_R^2 is
     2, 0, 0 modulo 5 for the sectors (1, -4), (1, 2), (-3, 6), so the second and third sectors close and the first
     does not; with a flux 3 dividing the phase the denominator is 15 and none closes.
 G3  the charges (-3, 6, -3) are divisible by 3, and (-3, 6) = (2, 1) modulo 5; p/15 = 2p/5 - p/3 modulo 1; the points
     of exact order 15 are 192 = 24 x 8.
 G4  frame C's cusp exponents from MAIN'S OWN rule (B1788's tropical rule, as B1945 uses it), at the points of exact
     order 5, 10, 15 and 30: the seat's tables.
 G5  Bernoulli's multiplication theorem: the mean of B_2({a})/B_2(0) over a = 1/5 .. 4/5 is -1/5; of B_6 it is
     -781/3125, and over the 24 points -26/625; and the arithmetic the note does with them.
 G6  the sublattice identities at s = 3 on a lattice: the sum over the 24 shifts is (5^6 - 1) E and the sum over the
     24 characters is -(624/625) E.
 G7  M modulo 3 has order 4 with two orbits of four on the eight non-zero points, and det(M - 1) = -1: the note's
     'order 8, acting transitively' is false (its root J has order 8)."""
import functools, itertools, math, pathlib, sys
from fractions import Fraction as Fr
import numpy as np
print = functools.partial(print, flush=True)
M, J = ((2, 1), (1, 1)), ((1, 1), (1, 0))
SEC = {"sec1": (1, -4), "sec2": (1, 2), "sec3": (-3, 6)}

def inv(X, n):
    d = (X[0][0] * X[1][1] - X[0][1] * X[1][0]) % n; di = pow(d, -1, n); return ((X[1][1] * di % n, -X[0][1] * di % n), (-X[1][0] * di % n, X[0][0] * di % n))
def act(w, X, n): return tuple(sum(w[k] * X[k][j] for k in range(2)) % n for j in range(2))
def orbits(pts, X, n):
    left, out = set(pts), []
    while left:
        w = min(left); o = {w}; v = act(w, X, n)
        while v not in o: o.add(v); v = act(v, X, n)
        left -= o; out.append(sorted(o))
    return out
def prim(N): return [(a, b) for a in range(N) for b in range(N) if math.gcd(math.gcd(a, b), N) == 1]
def B2(x): return x * x - x + Fr(1, 6)
def B6(x): return x ** 6 - 3 * x ** 5 + Fr(5, 2) * x ** 4 - Fr(1, 2) * x ** 2 + Fr(1, 42)

if __name__ == "__main__":
    P5 = prim(5); Mi, Ji = inv(M, 5), inv(J, 5); orb = orbits(P5, Mi, 5); O4 = [w for w in P5 if act(w, Mi, 5) == ((-w[0]) % 5, (-w[1]) % 5)]
    cyc = [O4[0]]; 
    while act(cyc[-1], Ji, 5) != cyc[0]: cyc.append(act(cyc[-1], Ji, 5))
    print("G1: orbit sizes of M^-1 on the 24 points: %s; the points with w M^-1 = -w: %s (two orbits of two under M^-1); J^-1 moves them in one cycle of length %d; the other twenty are two orbits of ten" % (sorted(len(o) for o in orb), O4, len(cyc)))
    print("G2: q_L^2 + q_R^2 modulo 5 for the three sectors: %s; modulo 15 with the flux 3 (5 (q_L^2 + q_R^2) k^2/15 an integer for every k?): %s"
          % ({s: (l * l + r * r) % 5 for s, (l, r) in SEC.items()}, {s: all((5 * (l * l + r * r) * k * k) % 15 == 0 for k in range(1, 5)) for s, (l, r) in SEC.items()}))
    print("G3: sector 3's charges divisible by 3: %s; (-3, 6) modulo 5 = %s; p/15 = 2p/5 - p/3 modulo 1 for every p: %s; points of exact order 15: %d = 24 x %d"
          % (all(q % 3 == 0 for q in (-3, 6, -3)), ((-3) % 5, 6 % 5), all((Fr(p, 15) - Fr(2 * p, 5) + Fr(p, 3)).denominator == 1 for p in range(15)), len(prim(15)), len(prim(15)) // 24))
    ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
    sys.path.insert(0, str(next((ROOT / "frontier").glob("B1788_*")) / "verification")); import tropical as T
    Ps = T.polys("S"); tab = {}
    for N in (5, 10, 15, 30):
        for s, (l, r) in SEC.items(): tab[(N, s)] = sorted({T.predict(Ps, T.E(l * Fr(a, N), r * Fr(a, N)))[0] for a, b in prim(N)})
    fmt = lambda xs: "{" + ", ".join(str(x) for x in xs) + "}"
    print("G4: main's rule, the first exponent's values: order 5: sec2 %s, sec3 %s; order 10: sec2 %s, sec3 %s; least in the three sectors at order 5: %s"
          % (fmt(tab[(5, "sec2")]), fmt(tab[(5, "sec3")]), fmt(tab[(10, "sec2")]), fmt(tab[(10, "sec3")]), tuple(str(min(tab[(5, s)])) for s in SEC)))
    at = {s: T.predict(Ps, T.E(l * Fr(2, 15), r * Fr(2, 15))) for s, (l, r) in SEC.items()}
    print("    order 15: sec3 %s, sec2 %s (seven values); order 30: sec3 %s, sec2 the same seven: %s; at a = 2/15 the pairs: sec2 (%s, %s), sec3 (%s, %s), so the differences are %s and %s"
          % (fmt(tab[(15, "sec3")]), fmt(tab[(15, "sec2")]), fmt(tab[(30, "sec3")]), tab[(30, "sec2")] == tab[(15, "sec2")], at["sec2"][0], at["sec2"][1], at["sec3"][0], at["sec3"][1], at["sec2"][1] - at["sec2"][0], at["sec3"][1] - at["sec3"][0]))
    m2 = sum(B2(Fr(k, 5)) for k in range(1, 5)) / 4 / B2(0); m6 = sum(B6(Fr(k, 5)) for k in range(1, 5)) / 4 / B6(0); m6P = (4 * B6(0) + 5 * sum(B6(Fr(k, 5)) for k in range(1, 5))) / 24 / B6(0)
    print("G5: the means: B_2 over the four: %s; B_6 over the four: %s; B_6 over the 24 points: %s; 24 - 86 x these: %s, %s, %s (with -86 + 24 = %d)" % (m2, m6, m6P, 24 - 86 * m2, 24 - 86 * m6P, 24 - 86 * m6, -86 + 24))
    tau = complex(0.13, 1.7); R = 60; mm, nn = np.meshgrid(np.arange(-R, R + 1), np.arange(-R, R + 1)); w0 = mm * tau + nn; E = float(np.sum(np.abs(w0[np.abs(w0) > 0]) ** -6.0))
    shift = sum(float(np.sum(np.abs(w0 + (a * tau + b) / 5) ** -6.0)) for a, b in P5); char = sum(float(np.sum((np.exp(2j * np.pi * (a * nn - b * mm) / 5) * np.where(np.abs(w0) > 0, np.abs(w0) + (np.abs(w0) == 0), 1) ** -6.0)[np.abs(w0) > 0]).real) for a, b in P5)
    print("G6: at s = 3, tau = 0.13 + 1.7i: the 24 shifts' sum over (5^6 - 1) E = %.9f; the 24 characters' sum over E = %.9f against -624/625 = %.9f" % (shift / ((5 ** 6 - 1) * E), char / E, -624 / 625))
    P3 = prim(3); o3 = orbits(P3, M, 3); k = 1; X = M
    while tuple(tuple(x % 3 for x in r) for r in X) != ((1, 0), (0, 1)): X = tuple(tuple(sum(X[i][t] * M[t][j] for t in range(2)) for j in range(2)) for i in range(2)); k += 1
    kj = 1; X = J
    while tuple(tuple(x % 3 for x in r) for r in X) != ((1, 0), (0, 1)): X = tuple(tuple(sum(X[i][t] * J[t][j] for t in range(2)) for j in range(2)) for i in range(2)); kj += 1
    print("G7: M modulo 3 has order %d with orbits %s on the eight points; J has order %d; det(M - 1) = %d" % (k, sorted(len(o) for o in o3), kj, (M[0][0] - 1) * (M[1][1] - 1) - M[0][1] * M[1][0]))
