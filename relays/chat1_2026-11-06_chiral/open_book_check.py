"""Data-free checks for the web seat's follow-up relay: the knot reading's S³ is the object's own open book.

PRE-REGISTRATION (written before this script was run; its sha256 is recorded before the run)
Cited, not re-derived:
  - Baldwin, arXiv:0804.3624, Lemma 2.1: "If K is the closed 3-braid specified by w then Σ(K) has an open book
    decomposition (T, w(x, y, x^-1, y^-1))", where T is the genus one surface with one boundary component, x and y are
    right-handed Dehn twists about dual non-separating curves, and Σ(K) is the double cover of S³ branched along K.
  - Baldwin, arXiv:math/0607370: "the only GOF-knots in S³ are the right- and left-handed trefoil knots and the figure
    eight knot".
Conventions: the record's L = [[1,1],[0,1]] and R = [[1,0],[1,1]] (GENESIS). A right-handed Dehn twist about a primitive
class c acts on H1 of the torus as v -> v + i(c, v) c, with i(u, v) = u^T J v and J = [[0,1],[-1,0]]; the other
orientation is J -> -J.
Claims and pass rules (each True or False):
  O1 With J: L is the right-handed twist about (1,0); R is the inverse of the right-handed twist about (0,1); and R is
     the right-handed twist about no primitive c with entries in [-20, 20].
  O2 With -J (the other orientation): L is the inverse of a right-handed twist and R is a right-handed twist. So in
     either orientation L and R are twists of opposite handedness about dual curves (i(c, c') = +-1).
  O3 LR = [[2,1],[1,1]] with trace 3. The word x y with both twists right-handed has trace 1 and order 6 in SL(2,Z).
  O4 For phi in SL(2,Z), det(phi - I) = 2 - tr(phi) (symbolic). The Smith normal form of LR - I is diag(1, 1), so the
     cokernel is trivial.
  O5 Among the 2^n words of length n = 2..10 in L and R that contain both letters, trace 3 occurs exactly for LR and
     RL (n = 2); every other such word has trace above 3.
  O6 For the record's members L^5 R (LR)^k and L^6 R (LR)^k (k = 0..12) and for L^10 R L R: trace - 2 > 1. Printed as
     one boolean only.
  O7 The braid word s1 s2^-1 in B3 has permutation a 3-cycle (its closure is a knot), with 2 crossings.
  O8 SnapPy: '4_1' is isometric to 'b++LR'; '4_1' filled along its meridian (1,0) has trivial fundamental group and
     trivial H1.
Predicted before running: every item True.
Nothing here is a coupling, a scale, an inter-sector value or a held-out quantity. Only booleans are printed.
"""
import itertools

import sympy as sp
from sympy.matrices.normalforms import smith_normal_form

I2 = sp.eye(2)
J = sp.Matrix([[0, 1], [-1, 0]])
L = sp.Matrix([[1, 1], [0, 1]])
R = sp.Matrix([[1, 0], [1, 1]])


def twist(c, jm):
    c = sp.Matrix(c)
    return I2 + c * (c.T * jm)


out = {}
x, y = twist((1, 0), J), twist((0, 1), J)
none_r = all(twist((p, q), J) != R for p in range(-20, 21) for q in range(-20, 21)
             if (p, q) != (0, 0) and sp.igcd(p, q) == 1)
out["O1"] = (x == L) and (y.inv() == R) and none_r
xm, ym = twist((1, 0), -J), twist((0, 1), -J)
out["O2"] = (xm.inv() == L) and (ym == R) and abs((sp.Matrix([1, 0]).T * J * sp.Matrix([0, 1]))[0]) == 1
xy = x * y
order6 = (xy ** 6 == I2) and all(xy ** n != I2 for n in range(1, 6))
out["O3"] = (L * R == sp.Matrix([[2, 1], [1, 1]])) and (L * R).trace() == 3 and xy.trace() == 1 and order6
a, b, c, d = sp.symbols("a b c d")
phi = sp.Matrix([[a, b], [c, d]])
det_rel = sp.expand((phi - I2).det() - (2 - (a + d))).subs(a * d, 1 + b * c)
snf = smith_normal_form(L * R - I2, domain=sp.ZZ)
out["O4"] = sp.simplify(det_rel) == 0 and [abs(snf[0, 0]), abs(snf[1, 1])] == [1, 1]
ok5 = True
for n in range(2, 11):
    for w in itertools.product("LR", repeat=n):
        if "L" not in w or "R" not in w:
            continue
        m = I2
        for ch in w:
            m = m * (L if ch == "L" else R)
        tr = m.trace()
        if n == 2:
            ok5 &= tr == 3
        else:
            ok5 &= tr > 3
out["O5"] = ok5


def word(s):
    m = I2
    for ch in s:
        m = m * (L if ch == "L" else R)
    return m


members = [("L" * 5 + "R" + "LR" * k) for k in range(13)] + [("L" * 6 + "R" + "LR" * k) for k in range(13)]
members.append("L" * 10 + "RLR")
out["O6"] = all(word(s).trace() - 2 > 1 for s in members)
perm = [0, 1, 2]
for (i, j) in [(0, 1), (1, 2)]:
    perm[i], perm[j] = perm[j], perm[i]
cycle_len, k0, seen = 0, 0, set()
while k0 not in seen:
    seen.add(k0)
    k0 = perm[k0]
    cycle_len += 1
out["O7"] = cycle_len == 3 and len("s1 s2^-1".split()) == 2

import snappy

M4 = snappy.Manifold("4_1")
iso = bool(M4.is_isometric_to(snappy.Manifold("b++LR")))
F = snappy.Manifold("4_1")
F.dehn_fill((1, 0))
G = F.fundamental_group()
H = F.homology()
out["O8"] = iso and len(G.generators()) == 0 and H.order() == 1

print("sympy", sp.__version__, "snappy", snappy.__version__)
for key in sorted(out, key=lambda s: int(s[1:])):
    print(key, out[key])
print("all as predicted:", all(out.values()))
