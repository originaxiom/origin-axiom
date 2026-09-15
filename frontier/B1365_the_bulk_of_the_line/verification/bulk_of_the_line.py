#!/usr/bin/env python3
"""B1365 -- THE BULK OF THE LINE: the eta model on Y_3.

B1364 placed a flat E6 connection on Y_3 -- rho = (rho_{Q8} into SU(2)_beta, chi_4 into the U(1)^2 = h_SM^perp cap beta^perp) -- whose
unbroken group is SU(3) x SU(2) x U(1)_Y x U(1)'.  This script computes what that line leaves in four dimensions:
  (A) the charge table of the 27 under the unbroken group -- U(1)' is the Cartan direction gamma orthogonal to the SM and to beta; its
      charges on the eleven Standard-Model field types are compared with B1283's (beta, gamma) table and gamma is identified with the
      E6 literature's U(1)_eta (Q_eta = sqrt(3/8) Q_chi - sqrt(5/8) Q_psi), the Z' of Wilson-line breaking;
  (B) the 4-torsion of the torus T^2 = exp(u(1)^2): every order-4 element g, the roots it kills and the roots it sends to -1; the ones
      that kill exactly the eight SM roots (B1364's condition) and the type of their -1 roots (doublet, triplet or (3,2));
  (C) the bulk zero modes H^1(Y_3; 78_rho) by Fox calculus on the Fibonacci presentation F(2,6) = <a, b | phi^3(a) = a, phi^3(b) = b>,
      sector by sector under SU(2)_beta x SU(6): (3,1), (1,35), (2,20) -- with the controls b_1 = 0, the three sign characters (h^1 = 1)
      and the twelve order-4 characters (h^1 = 0);
  (D) the tree-level vacuum: the SM-singlet fields of the design (apex N_i, nu^c_i; bulk moduli) and the sign of their U(1)' charges;
  (E) the deck test: the 27-character of the line against that of its deck image (E6-conjugate lines have equal characters).
Usage: python3 bulk_of_the_line.py"""
import itertools, math, cmath
from fractions import Fraction as Fr
import numpy as np
import sympy

# ---------------------------------------------------------------- E6 in SO(10) x U(1) coordinates (B1364's conventions)
def roots_e6():
    R = []
    for i in range(5):
        for j in range(i + 1, 5):
            for si in (1, -1):
                for sj in (1, -1):
                    v = [Fr(0)] * 5; v[i] = Fr(si); v[j] = Fr(sj)
                    R.append((tuple(v), Fr(0)))
    for signs in itertools.product((1, -1), repeat=5):
        if signs.count(-1) % 2 == 0:
            w = tuple(Fr(s, 2) for s in signs)
            R.append((w, Fr(1))); R.append((tuple(-x for x in w), Fr(-1)))
    return R
def dot(a, b):
    return sum(x * y for x, y in zip(a[0], b[0])) + Fr(3, 4) * a[1] * b[1]
def vec(*xs):
    return (tuple(Fr(x) for x in xs[:5]), Fr(xs[5]))
def neg(r): return (tuple(-x for x in r[0]), -r[1])
def add(r, s): return (tuple(x + y for x, y in zip(r[0], s[0])), r[1] + s[1])
R = roots_e6(); assert len(R) == 72
sm_roots = [vec(1,-1,0,0,0,0), vec(-1,1,0,0,0,0), vec(0,1,-1,0,0,0), vec(0,-1,1,0,0,0), vec(1,0,-1,0,0,0), vec(-1,0,1,0,0,0),
            vec(0,0,0,1,-1,0), vec(0,0,0,-1,1,0)]
Y = vec(Fr(-1,3), Fr(-1,3), Fr(-1,3), Fr(1,2), Fr(1,2), 0)
beta = vec(Fr(1,2), Fr(1,2), Fr(1,2), Fr(1,2), Fr(1,2), 1)
# the 27: the sixteen with an odd number of minus signs at psi = c/3, the ten +-e_k at psi = -2c/3, the singlet at psi = 4c/3
# (the unique assignment with integral pairings against the roots; checked below)
W27 = []
for signs in itertools.product((1, -1), repeat=5):
    if signs.count(-1) % 2 == 1:
        W27.append((tuple(Fr(s, 2) for s in signs), Fr(1, 3)))
for k in range(5):
    for s in (1, -1):
        v = [Fr(0)] * 5; v[k] = Fr(s); W27.append((tuple(v), Fr(-2, 3)))
W27.append((tuple([Fr(0)] * 5), Fr(4, 3)))
assert len(W27) == 27 and all(dot(w, r).denominator == 1 for w in W27 for r in R)
assert all(dot(w, w) == Fr(4, 3) for w in W27)
print("=== (A) the 27 and the unbroken U(1)' ===")
print(f"27 weights: {len(W27)}, integral pairings with all 72 roots, norm^2 4/3 each (the minuscule orbit)")
# gamma: in the Cartan, orthogonal to the SM roots, to Y and to beta -> proportional to (1,1,1,1,1; -(10/3)c); normalised as B1283
gamma = vec(Fr(1,2), Fr(1,2), Fr(1,2), Fr(1,2), Fr(1,2), Fr(-5, 3))
assert all(dot(gamma, r) == 0 for r in sm_roots) and dot(gamma, Y) == 0 and dot(gamma, beta) == 0
# psi and chi charges of a 27 weight (B1283's conventions: psi = 1/-2/4 on 16/10/1; chi = -1/3/-5 on 10/5bar/1 of the 16, 2/-2 on 5/5bar of the 10)
def psi(w): return 3 * w[1]
def chi(w): return 2 * sum(w[0])
def name(w):
    y, b = dot(Y, w), dot(beta, w)
    table = {(Fr(1,6), 0): "Q", (Fr(-2,3), 0): "u^c", (Fr(1), 0): "e^c", (Fr(1,3), 1): "d^c", (Fr(-1,2), 1): "L", (Fr(0), -1): "nu^c",
             (Fr(0), 1): "N", (Fr(-1,3), 0): "D", (Fr(1,3), -1): "Dbar", (Fr(1,2), 0): "H_u", (Fr(-1,2), -1): "H_d"}
    return table[(y, b)]
from collections import OrderedDict, Counter
rows = OrderedDict()
for w in W27:
    n = name(w)
    rows.setdefault(n, []).append((dot(Y, w), dot(beta, w), dot(gamma, w), psi(w), chi(w)))
b1283 = {"Q": (0, Fr(-2,3)), "u^c": (0, Fr(-2,3)), "e^c": (0, Fr(-2,3)), "d^c": (1, Fr(1,3)), "L": (1, Fr(1,3)), "nu^c": (-1, Fr(-5,3)),
         "N": (1, Fr(-5,3)), "H_u": (0, Fr(4,3)), "D": (0, Fr(4,3)), "H_d": (-1, Fr(1,3)), "Dbar": (-1, Fr(1,3))}
ok_all = True
print(f"{'field':6s} {'mult':>4s} {'Y':>5s} {'beta':>5s} {'gamma':>6s} {'-6gamma':>7s} {'psi':>4s} {'chi':>4s}  B1283 (beta,gamma)  gamma = -(5/12)psi + chi/4")
for n, lst in rows.items():
    vals = set(lst); assert len(vals) == 1
    y, b, g, p, c = lst[0]
    ok = (b, g) == b1283[n] and g == Fr(-5, 12) * p + Fr(1, 4) * c
    ok_all &= ok
    print(f"{n:6s} {len(lst):4d} {str(y):>5s} {str(b):>5s} {str(g):>6s} {str(-6*g):>7s} {str(p):>4s} {str(c):>4s}  {str(b1283[n]):>18s}  {ok}")
print(f"all eleven field types agree with B1283's identification, and gamma = -(5 psi - 3 chi)/12 on every weight: {ok_all}")
# U(1)_eta: Q_eta = sqrt(3/8) Q_chi - sqrt(5/8) Q_psi with Q_psi = psi/(2 sqrt 6), Q_chi = chi/(2 sqrt 10)  ->  Q_eta = (3 chi - 5 psi)/(8 sqrt 15)
eta_ok = True
for n, lst in rows.items():
    y, b, g, p, c = lst[0]
    q_eta = (math.sqrt(3/8) * float(c) / (2 * math.sqrt(10)) - math.sqrt(5/8) * float(p) / (2 * math.sqrt(6)))
    eta_ok &= abs(q_eta - float(g) * 3 / (2 * math.sqrt(15))) < 1e-12
print(f"gamma = (2 sqrt 15 / 3) Q_eta on every field type (U(1)' is the eta model's U(1)): {eta_ok}")
print(f"the SM singlets of the 27 (Y = 0, colour and weak singlets): {[n for n in rows if rows[n][0][0] == 0 and len(rows[n]) == 1]} with gamma = "
      f"{[str(rows[n][0][2]) for n in rows if rows[n][0][0] == 0 and len(rows[n]) == 1]} (equal, same sign)")

# ---------------------------------------------------------------- (B) the 4-torsion of T^2 = exp(u(1)^2)
print("\n=== (B) the order-4 elements of the torus exp(u(1)^2) ===")
# v = s Y + t gamma; v.alpha = s (Y.alpha) + t (gamma.alpha).  The lattice L = { v : v.alpha in Z for all roots } is the dual of the
# lattice Lambda spanned by the pairs (Y.alpha, gamma.alpha); a Z-basis of Lambda by integer row reduction (Euclid), then L = Lambda^*.
pairs = sorted(set((dot(Y, r), dot(gamma, r)) for r in R))
den = 1
for p, q in pairs:
    den = math.lcm(den, p.denominator, q.denominator)
rows_int = [[int(p * den), int(q * den)] for p, q in pairs]
def lattice_basis_2d(rows):
    """a basis {(g1, x), (0, g2)} of the Z-span of integer 2-vectors (row-style Hermite reduction)"""
    rows = [r[:] for r in rows if r != [0, 0]]
    # column 1
    while sum(1 for r in rows if r[0] != 0) > 1:
        nz = sorted([r for r in rows if r[0] != 0], key=lambda r: abs(r[0]))
        piv = nz[0]
        for r in nz[1:]:
            q = r[0] // piv[0]; r[0] -= q * piv[0]; r[1] -= q * piv[1]
        rows = [r for r in rows if r != [0, 0]]
    piv = [r for r in rows if r[0] != 0]; rest = [r for r in rows if r[0] == 0]
    g2 = 0
    for r in rest: g2 = math.gcd(g2, r[1])
    b1 = piv[0] if piv else [0, 0]
    if b1[0] < 0: b1 = [-b1[0], -b1[1]]
    if g2: b1[1] %= g2
    return [b1, [0, g2]]
b1, b2 = lattice_basis_2d(rows_int)
basis_rows = [(Fr(b1[0], den), Fr(b1[1], den)), (Fr(b2[0], den), Fr(b2[1], den))]
Bm = sympy.Matrix([[sympy.Rational(x.numerator, x.denominator) for x in row] for row in basis_rows])
Dual = Bm.inv()        # columns: the dual basis vectors (s, t) with row_i . dual_j = delta_ij
dual = [tuple(Fr(int(Dual[i, j].p), int(Dual[i, j].q)) for i in range(2)) for j in range(2)]
print(f"Lambda = span of the 72 pairs (Y.alpha, gamma.alpha): basis {[tuple(str(x) for x in b) for b in basis_rows]}; L = Lambda^*: basis {[tuple(str(x) for x in d) for d in dual]}")
def v_of(m, n):     # v = (m/4) dual_0 + (n/4) dual_1, in (s, t) coordinates
    return (Fr(m, 4) * dual[0][0] + Fr(n, 4) * dual[1][0], Fr(m, 4) * dual[0][1] + Fr(n, 4) * dual[1][1])
def val(v, r):
    return v[0] * dot(Y, r) + v[1] * dot(gamma, r)
# checks: every pair lies in Lambda (integer coordinates in the basis) and the lattice points of L act trivially on every root
coords = [Bm.T.solve(sympy.Matrix([sympy.Rational(p.numerator, p.denominator), sympy.Rational(q.numerator, q.denominator)])) for p, q in pairs]
assert all(c[i].q == 1 for c in coords for i in range(2))
assert all(val(v_of(4 * m, 4 * n), r).denominator == 1 for m in range(-2, 3) for n in range(-2, 3) for r in R)
perp_beta = [r for r in R if dot(r, beta) == 0]; assert len(perp_beta) == 30
def sm_type(r):
    """(SU(3), SU(2), Y) type of a root by its SM Dynkin labels"""
    c = [dot(r, sm_roots[0]), dot(r, sm_roots[2])]      # pairings with e1-e2, e2-e3
    w = dot(r, sm_roots[6])                             # pairing with e4-e5
    y = dot(Y, r)
    col = 3 if any(x != 0 for x in c) else 1
    wk = 2 if w != 0 else 1
    return (col, wk, y)
def classify(rs):
    return dict(Counter(sm_type(r) for r in rs))
found = []
for m in range(4):
    for n in range(4):
        if m == 0 and n == 0: continue
        v = v_of(m, n)
        vals = {r: val(v, r) for r in R}
        order = max(x.denominator for x in vals.values())
        killed30 = [r for r in perp_beta if vals[r].denominator == 1]
        minus30 = [r for r in perp_beta if vals[r].denominator == 2]
        killed72 = [r for r in R if vals[r].denominator == 1]
        found.append((m, n, order, killed30, minus30, killed72))
print(f"non-trivial 4-torsion points of T^2: {len(found)}; orders: {dict(Counter(f[2] for f in found))}")
print("order-4 points (the candidates for chi_4's generator): roots of su(6) killed / sent to -1, by SM type (SU(3) dim, SU(2) dim, Y):")
minimal = []
for m, n, order, k30, m30, k72 in found:
    if order != 4: continue
    exact_sm = set(k30) == set(sm_roots)
    if exact_sm: minimal.append((m, n))
    print(f"  (m,n) = ({m},{n}): g^2 = ({2*m % 4},{2*n % 4}); killed {len(k30)} of 30 -> unbroken dim {5 + len(k30)} (exactly the SM: {exact_sm}); -1 on {len(m30)}: {classify(m30)}")
print(f"order-4 points killing exactly the SM's eight among the 30 (B1364's condition): {len(minimal)} -> {minimal}")
print("order-2 points (the squares g^2): roots of su(6) killed, by type:")
for m, n, order, k30, m30, k72 in found:
    if order == 2:
        print(f"  (m,n) = ({m},{n}): killed {len(k30)} of 30 = SM 8 + {classify([r for r in k30 if r not in sm_roots])}")

# ---------------------------------------------------------------- (C) H^1(Y_3; 78_rho) by Fox calculus
print("\n=== (C) the bulk zero modes H^1(Y_3; 78_rho) ===")
# the Fibonacci presentation of pi_1(Y_3): F(2,6) = <a, b | phi^3(a) a^-1, phi^3(b) b^-1>, phi: a -> a^2 b, b -> a b  (B1303, B1364)
def phi_word(w):
    out = []
    for (g, e) in w:
        img = [('a',1),('a',1),('b',1)] if g == 'a' else [('a',1),('b',1)]
        if e < 0: img = [(x, -y) for (x, y) in reversed(img)]
        out += img
    return out
a = [('a',1)]; b = [('b',1)]
phi3a = phi_word(phi_word(phi_word(a))); phi3b = phi_word(phi_word(phi_word(b)))
rel = [phi3a + [('a', -1)], phi3b + [('b', -1)]]
def free_reduce(w):
    out = []
    for x in w:
        if out and out[-1][0] == x[0] and out[-1][1] == -x[1]: out.pop()
        else: out.append(x)
    return out
rel = [free_reduce(r) for r in rel]
def fox(word, gen, rho):
    """Fox derivative d(word)/d(gen) evaluated in the representation rho = {'a': A, 'b': B} (left action convention)"""
    n = rho['a'].shape[0]
    D = np.zeros((n, n), dtype=complex); P = np.eye(n, dtype=complex)
    for (g, e) in word:
        X = rho[g] if e > 0 else np.linalg.inv(rho[g])
        if g == gen:
            if e > 0: D += P
            else: D -= P @ X
        P = P @ X
    return D
def h1(rho, tol=1e-8):
    """dim H^1(pi_1(Y_3); V_rho) = dim ker d1 - rank d0"""
    n = rho['a'].shape[0]
    d1 = np.block([[fox(rel[0], 'a', rho), fox(rel[0], 'b', rho)], [fox(rel[1], 'a', rho), fox(rel[1], 'b', rho)]])
    d0 = np.vstack([rho['a'] - np.eye(n), rho['b'] - np.eye(n)])
    r1 = np.linalg.matrix_rank(d1, tol=tol); r0 = np.linalg.matrix_rank(d0, tol=tol)
    assert np.allclose(d1 @ d0, 0, atol=1e-8)     # d1 o d0 = 0: the relators are relations
    return int((2 * n - r1) - r0)
def rep_char(x, y):
    """the character chi(a) = e^{2 pi i x}, chi(b) = e^{2 pi i y} as a 1x1 representation"""
    return {'a': np.array([[cmath.exp(2j * math.pi * float(x))]]), 'b': np.array([[cmath.exp(2j * math.pi * float(y))]])}
def tensor(r1, r2):
    return {'a': np.kron(r1['a'], r2['a']), 'b': np.kron(r1['b'], r2['b'])}
triv = rep_char(0, 0)
print(f"controls: b_1(Y_3) = h^1(trivial) = {h1(triv)} (rational homology sphere)")
chars = [(Fr(m, 4), Fr(n, 4)) for m in range(4) for n in range(4)]
def order_of(x, y):
    return max(x.denominator, y.denominator) if (x, y) != (0, 0) else 1
tab = {}
for x, y in chars:
    tab.setdefault(order_of(x, y), []).append(h1(rep_char(x, y)))
print(f"  the 16 characters of H_1 = (Z/4)^2, h^1 by order: " + ", ".join(f"order {o}: {sorted(v)}" for o, v in sorted(tab.items())))
# the deck on characters: chi o phi: (x, y) -> (2x + y, x + y) mod 1
def deck_char(x, y): return ((2 * x + y) % 1, (x + y) % 1)
fixed = [c for c in chars if deck_char(*c) == c]
orbs = set()
for c in chars:
    if order_of(*c) == 4:
        o = [c]; cur = deck_char(*c)
        while cur != c: o.append(cur); cur = deck_char(*cur)
        orbs.add(len(o))
print(f"  the deck on the characters: fixed points {len(fixed)} (the trivial one); order-4 characters fall in orbits of size {sorted(orbs)}")
# the Q_8 lines of B1364 (quaternion pairs (A, B) with phi^3-invariance and non-abelian image)
def qmul(p, q):
    a0,a1,a2,a3 = p; b0,b1,b2,b3 = q
    return (a0*b0-a1*b1-a2*b2-a3*b3, a0*b1+a1*b0+a2*b3-a3*b2, a0*b2-a1*b3+a2*b0+a3*b1, a0*b3+a1*b2-a2*b1+a3*b0)
def qinv(q): return (q[0], -q[1], -q[2], -q[3])
ONE = (Fr(1),Fr(0),Fr(0),Fr(0)); I = (Fr(0),Fr(1),Fr(0),Fr(0)); J = (Fr(0),Fr(0),Fr(1),Fr(0)); K = qmul(I, J)
def closure(gens):
    G = {ONE}; fr = [ONE]
    while fr:
        new = []
        for g in fr:
            for h in gens:
                p = qmul(g, h)
                if p not in G: G.add(p); new.append(p)
        fr = new
    return sorted(G)
Q8 = closure([I, J]); assert len(Q8) == 8
def word_q(w, A, B):
    r = ONE
    for (g, e) in w:
        x = A if g == 'a' else B
        if e < 0: x = qinv(x)
        r = qmul(r, x)
    return r
def is_abelian(S): return all(qmul(x,y) == qmul(y,x) for x in S for y in S)
lines = [(A, B) for A in Q8 for B in Q8 if word_q(phi3a, A, B) == A and word_q(phi3b, A, B) == B and not is_abelian(closure([A, B]))]
assert len(lines) == 24
def su2(q):
    a0, a1, a2, a3 = (float(x) for x in q)
    return np.array([[a0 + 1j * a1, a2 + 1j * a3], [-a2 + 1j * a3, a0 - 1j * a1]])
def so3(q):
    """the adjoint action of the unit quaternion q on Im H = span(i, j, k)"""
    cols = []
    for e in (I, J, K):
        r = qmul(qmul(q, e), qinv(q)); cols.append([float(r[1]), float(r[2]), float(r[3])])
    return np.array(cols).T
def rep2(line): return {'a': su2(line[0]), 'b': su2(line[1])}
def rep3(line): return {'a': so3(line[0]), 'b': so3(line[1])}
# which elements of pi_1 are the translations?  a^2, b^2, (ab)^2 map to -1 under every line (squares in Q_8 are central):
MINUS = (Fr(-1),Fr(0),Fr(0),Fr(0))
sq_central = all(word_q([('a',1),('a',1)], *L) in (ONE, MINUS) and word_q([('b',1),('b',1)], *L) in (ONE, MINUS) and word_q([('a',1),('b',1),('a',1),('b',1)], *L) in (ONE, MINUS) for L in lines)
print(f"  every Q_8-line sends a^2, b^2, (ab)^2 to +-1 (the squares of Q_8 are central; the translations act by a sign on the 2): {sq_central}")
h1_3 = sorted(set(h1(rep3(L)) for L in lines)); h1_2 = sorted(set(h1(rep2(L)) for L in lines))
print(f"  h^1 of the adjoint (3,1) = Ad o rho_Q8 over the 24 lines: {h1_3}; of the doublet (2) alone: {h1_2}")
# the full 78 for the line (rho_Q8, chi_4) with chi_4 = (x, y) of order 4 and g = exp(2 pi i v): sector by sector
# (3,1): Ad o rho (g acts trivially); (1,35): 5 Cartan (trivial) + the 30 roots orthogonal to beta with character gamma -> e^{2 pi i chi_4(gamma) v.alpha};
# (2,20): the 40 roots with beta.alpha = +-1 pair into 20 doublets (alpha, alpha - beta) carrying rho_2 (x) the character of v.alpha (v.beta = 0).
def char_of(x, y, q):      # the character gamma -> e^{2 pi i chi_4(gamma) q}, chi_4(a) = 4x, chi_4(b) = 4y
    return rep_char(4 * x * q, 4 * y * q)
def bulk_spectrum(line, x, y, v):
    out = {"(3,1)": h1(rep3(line)), "(1,35) Cartan": 5 * h1(triv)}
    charged = Counter()
    for r in perp_beta:
        q = val(v, r); n = h1(char_of(x, y, q))
        if n: charged[("(1,35)",) + sm_type(r) + (dot(gamma, r),)] += n
    doublets = [r for r in R if dot(r, beta) == 1]; assert len(doublets) == 20
    for r in doublets:
        q = val(v, r); n = h1(tensor(rep2(line), char_of(x, y, q)))
        if n: charged[("(2,20)",) + sm_type(r) + (dot(gamma, r),)] += n
    return out, charged
# B1364's line: the first order-4 point that kills exactly the SM, any of the 24 Q_8 lines, any order-4 character
x4, y4 = Fr(1, 4), Fr(0)
print("  the bulk spectrum for each minimal order-4 point (any Q_8 line, the order-4 character (1/4, 0)):")
spectra = {}
for (m, n) in minimal:
    v = v_of(m, n)
    out, charged = bulk_spectrum(lines[0], x4, y4, v)
    spectra[(m, n)] = (out, dict(charged))
    print(f"    g = ({m},{n}): neutral moduli from (3,1): {out['(3,1)']}; Cartan: {out['(1,35) Cartan']}; charged modes: {dict(charged) if charged else 'none'}")
# independence of the Q_8 line and of the order-4 character (the (2,20) sector vanishes for every combination)
indep = set()
for L in lines[::5]:
    for (x, y) in [(Fr(1,4), Fr(0)), (Fr(1,4), Fr(1,4)), (Fr(3,4), Fr(1,2)), (Fr(1,2), Fr(1,4))]:
        for (m, n) in minimal[:2]:
            out, charged = bulk_spectrum(L, x, y, v_of(m, n))
            indep.add((out["(3,1)"], tuple(sorted((k[0], k[1:], c) for k, c in charged.items()))))
print(f"  over 5 lines x 4 order-4 characters x 2 minimal points, the spectrum depends only on the point g: {len(indep)} distinct outcomes")
for s in sorted(indep): print(f"    {s}")

# ---------------------------------------------------------------- (D) the tree-level vacuum
print("\n=== (D) the tree-level vacuum of the design's E6 sector ===")
singlets = [n for n in rows if rows[n][0][0] == 0 and len(rows[n]) == 1]
qs = [rows[n][0][2] for n in singlets]
bulk_singlet_gamma = sorted(set(str(dot(gamma, r)) for r in R if sm_type(r) == (1, 1, 0)))
print(f"  E6-charged SM singlets: apex 27_i's {singlets} with gamma = {[str(q) for q in qs]} (one sign); bulk roots that are SM singlets: "
      f"{[r for r in R if sm_type(r) == (1,1,0)] == [beta, neg(beta)]} (+-beta, gamma = {bulk_singlet_gamma}) -> the (3,1) moduli are U(1)'-neutral")
print("  => the U(1)' D-term restricted to SM-singlet VEVs is (-5/3) sum_i (|N_i|^2 + |nu^c_i|^2) times g'^2: it vanishes only at N_i = nu^c_i = 0.")
print("  => no SM-preserving flat direction breaks U(1)' at tree level; the SM-preserving tree-level moduli are the (3,1) modes alone.")
# the bulk cubic on the three neutral moduli: the triple cup product of the three sign characters is the volume form (their product is trivial)
signs = [(Fr(1,2), Fr(0)), (Fr(0), Fr(1,2)), (Fr(1,2), Fr(1,2))]
prod_trivial = ((sum(s[0] for s in signs)) % 1, (sum(s[1] for s in signs)) % 1) == (0, 0)
print(f"  the three sign characters multiply to the trivial character (their triple cup product can be non-zero: W_bulk = kappa phi_1 phi_2 phi_3): {prod_trivial}")
print("  a modulus phi_i coupling to a charged bulk pair (X, Xbar) needs chi_i chi_X chi_Xbar = 1, i.e. chi_i = 1: no such cubic exists.")

# ---------------------------------------------------------------- (E) the deck test on the 27-character
print("\n=== (E) the deck test: 27-characters of the line and of its deck image ===")
# 27 = (15, 1) + (6bar, 2) under SU(2)_beta x SU(6): the beta-charge 0 weights and the six doublets (w, w - beta) with beta.w = +1
w15 = [w for w in W27 if dot(beta, w) == 0]; w6 = [w for w in W27 if dot(beta, w) == 1]
assert len(w15) == 15 and len(w6) == 6 and all(add(w, neg(beta)) in W27 for w in w6)
def words_up_to(L):
    out = []
    for n in range(1, L + 1):
        for w in itertools.product([('a',1),('a',-1),('b',1),('b',-1)], repeat=n):
            w = free_reduce(list(w))
            if len(w) == n: out.append(w)
    return out
def char27(line, x, y, v, w):
    """trace of the line's holonomy along the word w in the 27"""
    A, B = line
    q = word_q(w, A, B)
    k = sum((4 * x if g == 'a' else 4 * y) * e for (g, e) in w)      # chi_4(w) in Z (mod 4)
    tr2 = np.trace(su2(q))
    t = sum(cmath.exp(2j * math.pi * float(k * val(v, u))) for u in w15) + tr2 * sum(cmath.exp(2j * math.pi * float(k * val(v, u))) for u in w6)
    return t
def deck_line(line):
    A, B = line
    return (word_q(phi_word(a), A, B), word_q(phi_word(b), A, B))
words = words_up_to(6)
v_min = v_of(*minimal[0])
n_diff = 0; n_tested = 0
for L in lines:
    for (x, y) in [c for c in chars if order_of(*c) == 4]:
        xd, yd = deck_char(x, y); Ld = deck_line(L)
        diff = any(abs(char27(L, x, y, v_min, w) - char27(Ld, xd, yd, v_min, w)) > 1e-9 for w in words)
        n_tested += 1; n_diff += diff
print(f"  lines (24 Q_8 x 12 order-4 characters) whose 27-character differs from their deck image's on some word of length <= 6: {n_diff} of {n_tested}")
print("  (a differing character rules out E6-conjugacy: the deck-transformed flat connection is a different point of the moduli space)")
# and the Q_8 part alone, for comparison (B1364: conjugate inside 2T)
n_same_q8 = sum(1 for L in lines if all(abs(np.trace(su2(word_q(w, *L))) - np.trace(su2(word_q(w, *deck_line(L))))) < 1e-9 for w in words))
print(f"  Q_8 parts alone whose 2-character agrees with the deck image's: {n_same_q8} of 24 (the Q_8 part is deck-symmetric up to conjugation, B1364)")

# ---------------------------------------------------------------- (F) the moduli tripod: the three deformation families through the Q_8 point
print("\n=== (F) the three flat directions of the (3,1) moduli: explicit families of SU(2)_beta-representations through the Q_8 line ===")
def qexp(axis, theta):
    """exp(theta * axis) for a unit imaginary quaternion axis"""
    return (math.cos(theta), math.sin(theta) * float(axis[1]), math.sin(theta) * float(axis[2]), math.sin(theta) * float(axis[3]))
def qmulf(p, q):
    a0,a1,a2,a3 = p; b0,b1,b2,b3 = q
    return (a0*b0-a1*b1-a2*b2-a3*b3, a0*b1+a1*b0+a2*b3-a3*b2, a0*b2-a1*b3+a2*b0+a3*b1, a0*b3+a1*b2-a2*b1+a3*b0)
def qinvf(q): return (q[0], -q[1], -q[2], -q[3])
def word_f(w, A, B):
    r = (1.0, 0.0, 0.0, 0.0)
    for (g, e) in w:
        x = A if g == 'a' else B
        if e < 0: x = qinvf(x)
        r = qmulf(r, x)
    return r
def relators_hold(A, B, tol=1e-9):
    return max(abs(u - v) for u, v in zip(word_f(phi3a, A, B), A)) < tol and max(abs(u - v) for u, v in zip(word_f(phi3b, A, B), B)) < tol
def axis_of(q):
    n = math.sqrt(sum(float(x) ** 2 for x in q[1:])); return (0, q[1] / n, q[2] / n, q[3] / n) if n > 1e-12 else None
fam_ok = Counter()
for L in lines:
    A, B = L; Af = tuple(float(x) for x in A); Bf = tuple(float(x) for x in B)
    thetas = [0.3, 0.9, 1.4, 2.5]
    # family along B's axis (A fixed), along A's axis (B fixed), and along the axis of AB (both moved: A -> A e^{t K}, B -> e^{-t K} B keeps AB fixed?)
    okB = all(relators_hold(Af, qexp(axis_of(B), t)) for t in thetas)
    okA = all(relators_hold(qexp(axis_of(A), t), Bf) for t in thetas)
    AB = qmulf(Af, Bf); ax = axis_of(AB)
    okAB = all(relators_hold(qmulf(Af, qexp(ax, t)), qmulf(qexp(ax, -t), Bf)) for t in thetas)
    fam_ok[(okA, okB, okAB)] += 1
print(f"  over the 24 lines, (family along a's axis, along b's axis, along ab's axis) hold for all test angles: {dict(fam_ok)}")
# the unbroken group along a family: the image stays non-abelian (centraliser in SU(2)_beta = +-1) except at the abelian end
A, B = lines[0]; Af = tuple(float(x) for x in A); Bf = tuple(float(x) for x in B)
def comm_norm(p, q):
    c = qmulf(qmulf(p, q), qmulf(qinvf(p), qinvf(q))); return abs(c[0] - 1)
print(f"  along b's family (a fixed at {tuple(round(float(x),3) for x in A)}): |[a, b_theta] - 1| at theta = pi/2 (the Q_8 point), 1.0, 0.1, 0.0: "
      f"{[round(comm_norm(Af, qexp(axis_of(B), t)), 4) for t in (math.pi/2, 1.0, 0.1, 0.0)]} -> non-abelian (SM x U(1)' unbroken) until the abelian end theta = 0, where U(1)_beta returns")

print("\nDONE")
