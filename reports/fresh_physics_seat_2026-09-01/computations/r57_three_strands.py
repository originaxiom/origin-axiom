"""R57 -- the three strands. Exact checks with sympy."""
import sympy as sp
t = sp.symbols('t')
# reduced Burau representation of B_3
S1 = sp.Matrix([[-t, 1], [0, 1]]); S2 = sp.Matrix([[1, 0], [t, -t]])
def burau(word):
    M = sp.eye(2)
    for g, e in word:
        B = {1: S1, 2: S2}[g]
        M = M * (B if e > 0 else B.inv())
    return sp.simplify(M)
def alexander_of_closure(word):   # Delta(t) = det(I - Burau(beta)) * (1-t)/(1-t^3) for 3-braids
    d = sp.cancel((sp.eye(2) - burau(word)).det() * (1 - t) / (1 - t**3))
    num, den = sp.fraction(sp.together(d))
    # clear the unit t^k in the denominator (Laurent -> polynomial)
    return sp.Poly(sp.cancel(num / den * t**8), t)
def normalize(p):   # up to units +-t^k
    P = sp.Poly(sp.expand(p), t)
    c = P.all_coeffs(); 
    while c and c[-1] == 0: c.pop()
    if c[0] < 0: c = [-x for x in c]
    return c
beta  = [(1, 1), (2, -1)]                 # sigma_1 sigma_2^-1
beta2 = beta * 2                          # (sigma_1 sigma_2^-1)^2
print("[1] closure of (s1 s2^-1)^2:", normalize(alexander_of_closure(beta2).as_expr()), "  (figure-eight: t^2-3t+1 -> [1,-3,1])")
print("    closure of  s1 s2^-1   :", normalize(alexander_of_closure(beta).as_expr()), "  (unknot -> [1])")
assert normalize(alexander_of_closure(beta2).as_expr()) == [1, -3, 1]
# braid index >= 3: 2-braid closures are T(2,n) with Alexander (t^n+1)/(t+1) for odd n (coefficients +-1); 1-braid = unknot
for n in range(1, 12, 2):
    p = sp.Poly(sp.cancel((t**n + 1) / (t + 1)), t)
    assert normalize(p.as_expr()) != [1, -3, 1]
print("[2] no 2-braid closure has Alexander polynomial t^2-3t+1 (checked n<=11; coefficients of T(2,n) are +-1): braid index of 4_1 = 3")
# B_3 -> SL(2,Z): s1 -> R = [[1,1],[0,1]], s2 -> L^-1 = [[1,0],[-1,1]]
R = sp.Matrix([[1, 1], [0, 1]]); Linv = sp.Matrix([[1, 0], [-1, 1]])
img = R * Linv.inv()
M2 = sp.Matrix([[2, 1], [1, 1]])
print("[3] image of s1 s2^-1 in SL(2,Z):", img.tolist(), " = M^2 =", M2.tolist(), "->", img == M2)
assert img == M2
# hyperelliptic involution -I commutes with M^2; action of M^2 on E[2] \ 0
pts = [(1, 0), (0, 1), (1, 1)]
act = {p: tuple(int(x) % 2 for x in (M2 * sp.Matrix(p))) for p in pts}
print("[4] M^2 on the three half-periods (mod 2):", act)
# cycle structure
seen, cycles = set(), []
for p in pts:
    if p in seen: continue
    c, q = [], p
    while q not in c: c.append(q); q = act[q]
    seen |= set(c); cycles.append(c)
print("    cycle structure:", [len(c) for c in cycles], "-> one 3-cycle: the fixed set of -I in m004 is ONE geodesic meeting every fiber in 3 points")
assert [len(c) for c in cycles] == [3]
# PW count: chi of loci
print("[5] chi(open 3-braid: 3 arcs) = 3 - 0 = 3;   chi(its closure = 4_1) = 1 - 1 = 0;   chi(the -I axis geodesic, a loop) = 0")
print("    PW net chiral = chi(Delta-) - chi(Delta+): OPEN braid as charge locus -> 3; any CLOSED locus -> 0")
print("ALL CHECKS PASS")
