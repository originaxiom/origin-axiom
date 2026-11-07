"""B1851 -- the web seat's three relays of 2026-11-06/07, their checkable facts re-derived with main's own code (data-free;
symbols, integer matrices and SnapPy topology; no knot invariant, level, scale or coupling evaluated).
A. The product's leading exponent (DGLZ's t = k + sigma, tbar = k - sigma; S0 = (i/2)(Vol + i CS)) is
   sigma*Vol/2pi + i*k*CS/2pi: the modulus is sigma's, the phase k's; orientation reversal (CS -> -CS) is k -> -k;
   one factor alone is tbar = 0, i.e. sigma = k. B1012's display (t = k + i sigma, sigma real) gives a REAL action
   -k CS - sigma Vol, i.e. a pure phase in exp(iS).
B. The open book of the word LR (main's L = [[1,1],[0,1]], R = [[1,0],[1,1]]): L is the right-handed twist about (1,0),
   R the inverse of the right-handed twist about (0,1), R a right-handed twist about no primitive class, S L S^-1 = R^-1;
   det(phi - I) = 2 - tr(phi); among positive words with both letters only LR's cyclic class has trace 3; the excursion
   members' open books have |H_1| = tr - 2 > 1; SnapPy: 4_1 = b++LR, and 4_1's meridian filling is simply connected.
   B132's convention (R = T, L = S T S^-1) makes its m = 1 word the periodic trace-1 class, not LR.
C. The one-loop B-test: with alpha_i^-1(M_Z) = a + c_i L, (alpha_1^-1 - alpha_2^-1)/(alpha_2^-1 - alpha_3^-1) =
   (c_1 - c_2)/(c_2 - c_3), free of a and L, and free of a common shift of the c_i (complete generations)."""
import itertools, warnings
warnings.filterwarnings("ignore")
import sympy as sp

out = []
# ---- A
k, s, V, C = sp.symbols("k sigma Vol CS", real=True)
t, tb = k + s, k - s
S0 = sp.I / 2 * (V + sp.I * C)
E = sp.expand(t / (2 * sp.pi * sp.I) * S0 + tb / (2 * sp.pi * sp.I) * sp.conjugate(S0))
assert sp.simplify(E - (s * V / (2 * sp.pi) + sp.I * k * C / (2 * sp.pi))) == 0
assert sp.simplify(sp.re(E) - s * V / (2 * sp.pi)) == 0 and sp.simplify(sp.im(E) - k * C / (2 * sp.pi)) == 0
Erev = E.subs(C, -C); assert sp.simplify(Erev - E.subs(k, -k)) == 0                      # the hand is k -> -k
one_factor = sp.expand(t / (2 * sp.pi * sp.I) * S0)
assert sp.simplify(E.subs(s, k) - one_factor.subs(s, k)) == 0 and tb.subs(s, k) == 0      # one hand: sigma = k, t = 2k
ch = sp.I * (V + sp.I * C); tW, tWb = k + sp.I * s, k - sp.I * s
SW = sp.expand(tW / 2 * ch + tWb / 2 * sp.conjugate(ch))
assert sp.simplify(SW - (-k * C - s * V)) == 0 and sp.im(SW) == 0                          # B1012's display: real
out.append("A: exponent = sigma*Vol/2pi + i*k*CS/2pi; hand = (k -> -k); one factor at sigma = k (t = 2k); "
           "B1012's t = k + i*sigma form gives the real action -k*CS - sigma*Vol (a phase): ALL HOLD")
# ---- B
M = sp.Matrix
L, R = M([[1, 1], [0, 1]]), M([[1, 0], [1, 1]])
J = M([[0, 1], [-1, 0]])
def rtwist(p, q):
    c = M([p, q]); return sp.eye(2) + c * c.T * J
assert rtwist(1, 0) == L and rtwist(0, 1) == R.inv()
assert all(rtwist(p, q)[1, 0] <= 0 for p in range(-20, 21) for q in range(-20, 21) if sp.gcd(p, q) == 1)
S = M([[0, -1], [1, 0]]); assert S * L * S.inv() == R.inv()
a, b, c_, d = sp.symbols("a b c d"); P = M([[a, b], [c_, d]])
assert sp.expand((P - sp.eye(2)).det() - (2 - P.trace())).subs(a * d, 1 + b * c_) == 0 or \
       sp.simplify(((P - sp.eye(2)).det() - (2 - P.trace())).subs(d, (1 + b * c_) / a)) == 0
LR = L * R; assert LR == M([[2, 1], [1, 1]]) and (LR - sp.eye(2)).det() in (1, -1)
def word(w):
    X = sp.eye(2)
    for ch_ in w: X = X * (L if ch_ == "L" else R)
    return X
tr3 = set()
for n in range(2, 13):
    for w in itertools.product("LR", repeat=n):
        if "L" in w and "R" in w and word(w).trace() == 3:
            tr3.add("".join(w))
assert tr3 == {"LR", "RL"}, tr3
members = ["L" * 5 + "R" + "LR" * kk for kk in range(13)] + ["L" * 6 + "R" + "LR" * kk for kk in range(13)] + ["L" * 10 + "RLR"]
assert all(word(w).trace() - 2 > 1 for w in members)
T = M([[1, 1], [0, 1]]); Lb = S * T * S.inv(); Wb = Lb * T                                 # B132: R = T, L = S T S^-1
assert Wb.trace() == 1 and Wb ** 6 == sp.eye(2) and Wb ** 3 != sp.eye(2)
out.append("B: L, R are twists of opposite hand (R a right twist about no primitive class, |p|,|q| <= 20); S L S^-1 = R^-1; "
           "det(phi - I) = 2 - tr phi; trace 3 among positive words with both letters (lengths 2-12): only LR, RL; "
           "the 27 excursion members have |H_1(open book)| = tr - 2 > 1; B132's m = 1 word has trace 1, order 6: ALL HOLD")
import snappy
K = snappy.Manifold("4_1"); B = snappy.Manifold("b++LR")
iso = K.is_isometric_to(B)
F = snappy.Manifold("4_1"); F.dehn_fill((1, 0)); G = F.fundamental_group()
out.append("B (SnapPy): 4_1 isometric to b++LR: %s; 4_1(1,0) fundamental group generators %d, homology %s"
           % (iso, len(G.generators()), F.homology()))
assert iso and len(G.generators()) == 0
# ---- C
a0, Lg, c1, c2, c3, n, g = sp.symbols("a L c1 c2 c3 n g")
ai = [a0 + ci * Lg for ci in (c1, c2, c3)]
ratio = sp.simplify((ai[0] - ai[1]) / (ai[1] - ai[2]))
assert sp.simplify(ratio - (c1 - c2) / (c2 - c3)) == 0
shifted = sp.simplify(((c1 + n * g) - (c2 + n * g)) / ((c2 + n * g) - (c3 + n * g)))
assert sp.simplify(shifted - (c1 - c2) / (c2 - c3)) == 0
out.append("C: (a1^-1 - a2^-1)/(a2^-1 - a3^-1) = (c1 - c2)/(c2 - c3), free of alpha(mu*), of L and of a common shift: HOLDS")
print("\n".join(out))
