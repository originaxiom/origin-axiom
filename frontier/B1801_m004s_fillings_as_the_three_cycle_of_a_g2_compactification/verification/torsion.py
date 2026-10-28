"""The object as Q (Friedmann-Witten's G2 frame; data-free).  For hyperbolic Dehn fillings Q = m004(p/q) with 3 | p:
(1) H1 and hyperbolicity (SnapPy); (2) the Z/3 hypercharge Wilson line diag(w,w,w,1,1): commutant S(U(3)xU(2)) = the SM, the
doublet (6Y = 3) untwisted, the triplet (6Y = -2) and the X,Y bosons (6Y = -+5) twisted; (3) the Reidemeister torsion of Q with the
order-3 character, by Turaev's surgery formula |tau| = |Delta(zeta)| / (|zeta - 1| |zeta^r - 1|), r = -q^{-1} mod p, with the figure-
eight's Delta(t) = t - 3 + 1/t, checked by Fox calculus on the knot group <a, b | a b^-1 a^-1 b a b^-1 a b a^-1 b^-1> (meridians
a, b -> t); (4) Friedmann-Witten's T_omega = -log|tau|, T_O = -log|H1|, L(Q) = exp(T_omega - T_O) = |H1| / |tau|."""
import math, cmath
import sympy as sp
import snappy
t = sp.symbols("t")
# Fox calculus: figure-eight group, one relator; Alexander polynomial = det(d r / d b) at a, b -> t, divided appropriately
a, b = sp.symbols("a b", commutative=False)
word = "aBAbaBabAB"           # a b^-1 a^-1 b a b^-1 a b a^-1 b^-1 (a standard figure-eight relator; checked below)
def fox(word, gen):
    """the Fox derivative d(word)/d(gen) abelianised at every generator -> t"""
    total = 0; prefix = 0           # exponent sum of the prefix (abelianised: each letter -> t^{+-1})
    for ch in word:
        e = 1 if ch.islower() else -1; g = ch.lower()
        if g == gen:
            total += t**prefix if e == 1 else -t**(prefix - 1)
        prefix += e
    return sp.expand(total)
db = fox(word, "b"); da = fox(word, "a")
G = snappy.Manifold("m004").fundamental_group()
print("SnapPy m004 relators:", G.relators(), "| our relator abelianises to", sum(1 if c.islower() else -1 for c in word))
alex = sp.factor(sp.simplify(db))
print("Fox d r/d b at a,b -> t:", alex, "| expected (up to units) t^2 - 3t + 1")
Delta = lambda z: z - 3 + 1 / z
w3 = cmath.exp(2j * math.pi / 3)
print("|Delta(omega)| =", abs(Delta(w3)), "| Fox value |d r/d b (omega)| =", abs(complex(db.subs(t, w3))))
rows = []
for p in range(3, 31, 3):
    for q in range(1, 12):
        if math.gcd(p, q) != 1: continue
        M = snappy.Manifold("m004"); M.dehn_fill((p, q))
        if M.solution_type() != "all tetrahedra positively oriented": continue
        H = M.homology(); order = abs(p)
        r = (-pow(q, -1, p)) % p
        for k in (p // 3, 2 * p // 3):                     # the order-3 characters of Z/p: zeta = e^{2 pi i k/p}
            z = cmath.exp(2j * math.pi * k / p)
            tau = abs(Delta(z)) / (abs(z - 1) * abs(z**r - 1))
        L = order / tau
        rows.append((p, q, str(H), float(M.volume()), tau, L))
for p, q, H, V, tau, L in sorted(rows, key=lambda x: x[3])[:14]:
    print("  m004(%2d,%2d): H1 %-6s vol %.6f | |tau(Q, order-3 char)| = %.6f | L(Q) = |H1|/|tau| = %.6f, L^(2/3) = %.4f" % (p, q, H, V, tau, L, L**(2/3)))
# the Wilson line: diag(w,w,w,1,1) in SU(5); hypercharge charges seen
for name, q6 in (("Q", 1), ("u^c", -4), ("d^c", 2), ("L", -3), ("e^c", 6), ("H doublet", 3), ("T triplet", -2), ("X,Y bosons", 5)):
    print("  %-11s 6Y = %+d: holonomy %s" % (name, q6, "trivial" if q6 % 3 == 0 else "omega^%d" % (q6 % 3)))
print("torsion exit 0")
