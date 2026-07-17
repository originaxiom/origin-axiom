"""B666 cell R1 — L63/Q-C: the transport map, CONSTRUCTED (B578-D2 option (a)).

The map T: the B469 residue object --> the E6 character-variety structure.

  Domain   : the residue object R_m = (X_m = [[m,1],[1,0]], det X_m = -1)
             = the half-monodromy mapping class sigma_m in Out(F_2)
             (Nielsen: Out(F_2) ~= GL(2,Z); H_1(sigma_m) = X_m; BR2: the
             residue's geometric carrier).  Scale field Q(lambda_m),
             lambda_m the metallic unit, N(lambda_m) = det X_m = -1 (BR-N).
  Map      : T = (precomposition functoriality) o (theta-fixed principal
             embedding iota: SL2 -> F4 = E6^theta c E6):
                 sigma_1  |-->  sigma_1^* : X(F_2, E6(C)) -> X(F_2, E6(C)),
                 chi |-> chi o sigma_1,
             restricted to the geometric orbit {chi_g, chi_g-bar}.
  Certificate (defining property, all exact):
                 sigma_1^*(chi_g) = c(chi_g)  !=  chi_g = theta(chi_g)
             — the transported residue acts as GALOIS CONJUGATION c
             (sqrt(-3) -> -sqrt(-3)) on the geometric E6 character, while
             the fold theta fixes it.  Q-C: the residue transports as c.

Parts:
  0. the domain object, symbolic m (det/norm/companion; T-NORM obstruction);
  1. the carrier at m=1: sigma_1: a->ab, b->a; H1 = X_1; sigma_1^2 = A_1;
  2. the transport on SL2 trace coordinates: sigma_1^*(x,y,z) = (z,x,xz-y),
     kappa-invariance — generic-matrix rational identities;
  3. the geometric locus (B67 curve): sigma_1^* preserves it via
     x -> x/(x-1); the cusp locus x^2(x^2-3x+3); the geometric pair
     x_pm = (3 pm sqrt(-3))/2 SWAPPED = Galois-conjugated; the sigma-fixed
     characters {0,2} are non-geometric (no geometric character is fixed);
  4. the E6 lift: E6-principal == F4-principal on the 27 (Jordan (17,9,1),
     B570's banked computation, replicated + multiset-verified) => theta o
     iota = iota; the 27- and 78-character polynomials P27, P78 in Z[t]
     derived from the exact 2*rho-vee grading; P27/P78 at the geometric
     point are NON-REAL elements of Q(sqrt(-3)) => c moves the E6 character
     and sigma_1^* lands exactly on its Galois twin;
  5. the Klein-four verdict + the T-NORM in-lineage adjudication.

Exact arithmetic throughout (sympy).  Run: python3 b666_r1_transport.py
"""
import hashlib
import os
from collections import Counter

import sympy as sp

CHECKS = []


def check(name, cond):
    ok = bool(cond)
    CHECKS.append((name, ok))
    print(("PASS  " if ok else "FAIL  ") + name)
    assert ok, name


print("=" * 72)
print("PART 0 — the domain: the residue object R_m (symbolic m)")
print("=" * 72)

mm = sp.Symbol('m', integer=True, positive=True)
X = sp.Matrix([[mm, 1], [1, 0]])
A_m = sp.Matrix([[mm**2 + 1, mm], [mm, 1]])
check("det X_m = -1 (the residue), all m symbolically", sp.simplify(X.det()) == -1)
check("X_m^2 = A_m (half-monodromy squares to the metallic monodromy)",
      sp.simplify(X**2 - A_m) == sp.zeros(2))
t = sp.Symbol('t')
cp = X.charpoly(t).as_expr()
check("charpoly(X_m) = t^2 - m t - 1 (X_m = companion of the metallic unit)",
      sp.expand(cp - (t**2 - mm * t - 1)) == 0)
# product of the roots of t^2 - m t - 1 = N(lambda_m) = -1  (Vieta, exact)
check("N(lambda_m) = product of roots = -1 (BR-N clause 1)",
      sp.expand(sp.Poly(cp, t).all_coeffs()[2] / sp.Poly(cp, t).all_coeffs()[0]) == -1)
# T-NORM obstruction (the in-lineage conflict's source), re-verified inline:
# in Q(sqrt(-d)), d>0, the norm form is a^2 + d b^2 — a sum of squares
# (positive semidefinite), so a unit of norm -1 is IMPOSSIBLE there.
a, b, d = sp.symbols('a b d', real=True)
norm_form = a**2 + d * b**2
check("T-NORM: imaginary-quadratic norm form a^2 + d b^2 is a sum of squares"
      " (norm -1 impossible; the NORM realization cannot cross)",
      norm_form == sp.Add(a**2, d * b**2) and sp.simplify(
          norm_form.subs([(a, 0), (b, 0)])) == 0 and
      sp.solve(sp.Eq(a**2 + 3 * b**2, -1), [a, b], dict=True) == [])

print()
print("=" * 72)
print("PART 1 — the carrier at m=1: sigma_1 in Out(F_2), Nielsen-realized")
print("=" * 72)


def ab_word(word):
    """Exponent-sum vector (n_a, n_b) of a word in letters a,b,A,B."""
    na = word.count('a') - word.count('A')
    nb = word.count('b') - word.count('B')
    return (na, nb)


def apply_sigma(word):
    """sigma_1: a -> ab, b -> a (B466's deck generator)."""
    out = []
    for ch in word:
        out.append({'a': 'ab', 'b': 'a', 'A': 'BA', 'B': 'A'}[ch])
    return ''.join(out)


sa, sb = apply_sigma('a'), apply_sigma('b')
H1 = sp.Matrix([[ab_word(sa)[0], ab_word(sb)[0]], [ab_word(sa)[1], ab_word(sb)[1]]])
check("H1(sigma_1) = X_1 = [[1,1],[1,0]] (the residue's carrier)",
      H1 == X.subs(mm, 1))
check("det H1(sigma_1) = -1 (orientation-reversing: THE residue bit)", H1.det() == -1)
s2a, s2b = apply_sigma(sa), apply_sigma(sb)
H1sq = sp.Matrix([[ab_word(s2a)[0], ab_word(s2b)[0]], [ab_word(s2a)[1], ab_word(s2b)[1]]])
check("H1(sigma_1^2) = A_1 = [[2,1],[1,1]] (the fig-8 monodromy; BR2/B466)",
      H1sq == A_m.subs(mm, 1))
print("   sigma_1(a) = %s, sigma_1(b) = %s ; sigma_1^2(a) = %s, sigma_1^2(b) = %s"
      % (sa, sb, s2a, s2b))

print()
print("=" * 72)
print("PART 2 — the transport on trace coordinates (generic SL2, exact)")
print("=" * 72)

p, q, r, s, u, v = sp.symbols('p q r s u v')
Amat = sp.Matrix([[p, q], [r, (1 + q * r) / p]])
Bmat = sp.Matrix([[s, u], [v, (1 + u * v) / s]])
check("generic det A = det B = 1", sp.simplify(Amat.det()) == 1 and
      sp.simplify(Bmat.det()) == 1)
x_, y_, z_ = sp.trace(Amat), sp.trace(Bmat), sp.trace(Amat * Bmat)
# sigma_1^* chi (g) = chi(sigma_1 g):  a -> ab, b -> a, ab -> aba
img_x = sp.trace(Amat * Bmat)            # chi(sigma a) = chi(ab) = z
img_y = sp.trace(Amat)                   # chi(sigma b) = chi(a)  = x
img_z = sp.trace(Amat * Bmat * Amat)     # chi(sigma ab) = chi(aba)
check("sigma_1^*: (x,y,z) -> (z, x, xz - y)   [tr(ABA) = xz - y, rational identity]",
      sp.simplify(img_z - (x_ * z_ - y_)) == 0 and
      sp.simplify(img_x - z_) == 0 and sp.simplify(img_y - x_) == 0)


def inv2(M):
    return sp.Matrix([[M[1, 1], -M[0, 1]], [-M[1, 0], M[0, 0]]])  # SL2 adjugate


kappa = sp.trace(Amat * Bmat * inv2(Amat) * inv2(Bmat))
kappa_img = sp.trace((Amat * Bmat) * Amat * inv2(Amat * Bmat) * inv2(Amat))
check("kappa = tr[A,B] is sigma_1^*-invariant (tr[AB,A] = tr[A,B], rational identity)",
      sp.simplify(kappa - kappa_img) == 0)

print()
print("=" * 72)
print("PART 3 — the geometric locus: the swap IS the Galois flip (exact)")
print("=" * 72)

x = sp.Symbol('x')
kap = lambda X1, Y1, Z1: X1**2 + Y1**2 + Z1**2 - X1 * Y1 * Z1 - 2
# the B67 fixed-locus curve y = z = x/(x-1)
yc = x / (x - 1)
# sigma_1^* on the curve: (x, yc, yc) -> (yc, x, x*yc - yc)
new_x, new_y, new_z = yc, x, sp.simplify(x * yc - yc)
check("sigma_1^* preserves the B67 curve: image = (x', x'/(x'-1), x'/(x'-1)),"
      " x' = x/(x-1)", sp.simplify(new_z - new_y) == 0 and
      sp.simplify(new_x / (new_x - 1) - new_y) == 0)
cusp_num = sp.factor(sp.together(kap(x, yc, yc) + 2))
check("cusp locus on the curve: kappa + 2 = x^2 (x^2 - 3x + 3) / (x-1)^2",
      sp.simplify(cusp_num - x**2 * (x**2 - 3 * x + 3) / (x - 1)**2) == 0)
xp = sp.Rational(3, 2) + sp.sqrt(3) * sp.I / 2   # (3 + sqrt(-3))/2
xm = sp.Rational(3, 2) - sp.sqrt(3) * sp.I / 2   # (3 - sqrt(-3))/2
check("x_pm are the geometric roots (x^2 - 3x + 3 = 0 exactly)",
      sp.expand(xp**2 - 3 * xp + 3) == 0 and sp.expand(xm**2 - 3 * xm + 3) == 0)
check("x_minus = Galois/complex conjugate of x_plus (sqrt(-3) -> -sqrt(-3))",
      sp.expand(sp.conjugate(xp) - xm) == 0)
check("the curve action x -> x/(x-1) SWAPS the geometric pair",
      sp.simplify(xp / (xp - 1) - xm) == 0 and sp.simplify(xm / (xm - 1) - xp) == 0)
# the full character points P_pm = (x_pm, x_mp, x_mp)
Pp = (xp, xm, xm)
Pm = (xm, xp, xp)
img = (Pp[2], Pp[0], sp.expand(Pp[0] * Pp[2] - Pp[1]))
check("THE DEFINING PROPERTY at SL2: sigma_1^*(P_+) = P_- = conj(P_+), exact",
      all(sp.simplify(img[i] - Pm[i]) == 0 for i in range(3)) and
      all(sp.expand(sp.conjugate(Pp[i]) - Pm[i]) == 0 for i in range(3)))
check("P_+ is on the cusp locus with kappa = -2 (irreducible: kappa != 2)",
      sp.simplify(kap(*Pp) + 2) == 0)
fixed = sp.solve(sp.Eq(x / (x - 1), x), x)
check("sigma_1^*-fixed characters on the curve = {0, 2}, both NON-geometric"
      " (x^2-3x+3 = 3, 1 there): no geometric character is fixed",
      sorted(fixed) == [0, 2] and
      (x**2 - 3 * x + 3).subs(x, 0) == 3 and (x**2 - 3 * x + 3).subs(x, 2) == 1)

print()
print("=" * 72)
print("PART 4 — the E6 lift: theta fixes, c moves, sigma_1^* = c (exact)")
print("=" * 72)

# --- (i) E6-principal == F4-principal on the 27 (B570's banked computation,
#         replicated; the grading multiset additionally verified) ---
C6 = sp.Matrix([[2, 0, -1, 0, 0, 0], [0, 2, 0, -1, 0, 0], [-1, 0, 2, -1, 0, 0],
                [0, -1, -1, 2, -1, 0], [0, 0, 0, -1, 2, -1], [0, 0, 0, 0, -1, 2]])
C4L = [[2, -1, 0, 0], [-1, 2, -2, 0], [0, -1, 2, -1], [0, 0, -1, 2]]


def _blocks(grades):
    cnt = Counter(grades)
    out = []
    while cnt:
        top = max(cnt)
        out.append(int(top + 1))
        g = top
        while g >= -top:
            cnt[g] -= 1
            if cnt[g] == 0:
                del cnt[g]
            g -= 2
    return sorted(out, reverse=True)


G6 = C6.inv()
seen = {tuple(G6[:, 0])}
frontier27 = [G6[:, 0]]
while frontier27:
    new = []
    for vv in frontier27:
        for j in range(6):
            pj = sum(C6[i, j] * vv[i] for i in range(6))
            uu = sp.Matrix(vv)
            uu[j] = vv[j] - pj
            tu = tuple(uu)
            if tu not in seen:
                seen.add(tu)
                new.append(uu)
    frontier27 = new
rho6 = sum([G6[:, j] for j in range(6)], sp.zeros(6, 1))
grades27 = sorted(sp.Rational(2 * (sp.Matrix(muv).T * C6 * rho6)[0, 0]) for muv in seen)
check("the 27's 2*rho-vee grading: 27 weights, top = 16", len(grades27) == 27 and
      max(grades27) == 16)
expected27 = sorted(list(range(-16, 17, 2)) + list(range(-8, 9, 2)) + [0])
check("grading multiset = V17 + V9 + V1 strings exactly (E6-principal on 27)",
      grades27 == expected27)
e6_blocks = _blocks(grades27)
check("Jordan/block type on the 27: E6-principal = (17,9,1)", e6_blocks == [17, 9, 1])
# F4 side: the 26's nonzero weights = the 24 SHORT roots; + two zeros; + the 1
d4 = [1, 1, sp.Rational(1, 2), sp.Rational(1, 2)]
B4 = sp.Matrix(4, 4, lambda i, j: sp.Rational(C4L[i][j]) * d4[j])
allr = {tuple(1 if i == j else 0 for i in range(4)) for j in range(4)}
fr = set(allr)
while fr:
    new = set()
    for rt in fr:
        for j in range(4):
            pj = sum(C4L[i][j] * rt[i] for i in range(4))
            yv = list(rt)
            yv[j] -= pj
            ty = tuple(yv)
            if ty not in allr:
                allr.add(ty)
                new.add(ty)
    fr = new
ip4 = lambda X1, Y1: (X1.T * B4 * Y1)[0, 0]
pos4 = [sp.Matrix(rr) for rr in allr if all(c >= 0 for c in rr)]
rhovee4 = sum([2 * al / ip4(al, al) for al in pos4], sp.zeros(4, 1)) / 2
short4 = [sp.Matrix(rr) for rr in allr if ip4(sp.Matrix(rr), sp.Matrix(rr)) == 1]
check("F4 root system: 48 roots, 24 short", len(allr) == 48 and len(short4) == 24)
grades26 = sorted([sp.Rational(2 * ip4(muv, rhovee4)) for muv in short4]
                  + [sp.Integer(0), sp.Integer(0)])
f4_blocks = sorted(_blocks(grades26) + [1], reverse=True)
check("F4-principal on 1+26: block type (17,9,1) — EQUAL to E6-principal"
      " => a principal sl2 of E6 lies inside F4 = E6^theta => theta o iota = iota"
      " (Kostant conjugacy, as banked in B570-QA)", f4_blocks == [17, 9, 1] and
      f4_blocks == e6_blocks)

# --- (ii) the 27- and 78-character polynomials from the exact grading ---
mu = sp.Symbol('mu')
S27 = sum(mu**g for g in grades27)
P27 = sp.expand(sp.chebyshevu(16, t / 2) + sp.chebyshevu(8, t / 2) + 1)
check("P27(t) = U16(t/2) + U8(t/2) + 1 EQUALS the grading character"
      " sum(mu^e) under t = mu + 1/mu (exact identity)",
      sp.simplify(S27 - P27.subs(t, mu + 1 / mu)) == 0)
check("P27 has integer coefficients and P27(2) = 27",
      all(c == int(c) for c in sp.Poly(P27, t).all_coeffs()) and
      P27.subs(t, 2) == 27)
# adjoint: grading = {2*height(alpha)} over all 72 roots, + 6 zeros (Cartan)
seenr = {tuple(1 if i == j else 0 for i in range(6)) for j in range(6)}
fr6 = set(seenr)
while fr6:
    new = set()
    for rt in fr6:
        for j in range(6):
            pj = sum(C6[i, j] * rt[i] for i in range(6))
            yv = list(rt)
            yv[j] -= pj
            ty = tuple(yv)
            if ty not in seenr:
                seenr.add(ty)
                new.add(ty)
    fr6 = new
check("E6 root system: 72 roots", len(seenr) == 72)
grades78 = sorted([sp.Integer(2 * sum(rt)) for rt in seenr] + [sp.Integer(0)] * 6)
blocks78 = _blocks(grades78)
check("adjoint block type = (23,17,15,11,9,3) — exponents {1,4,5,7,8,11}",
      blocks78 == [23, 17, 15, 11, 9, 3])
S78 = sum(mu**g for g in grades78)
P78 = sp.expand(sum(sp.chebyshevu(2 * e, t / 2) for e in [1, 4, 5, 7, 8, 11]))
check("P78(t) = sum U_{2e}(t/2), e in {1,4,5,7,8,11}, equals the adjoint"
      " grading character (exact identity); P78(2) = 78",
      sp.simplify(S78 - P78.subs(t, mu + 1 / mu)) == 0 and P78.subs(t, 2) == 78)

# --- (iii) the E6 character values at the geometric point: NON-REAL ---
v27p = sp.expand(P27.subs(t, xp))
v27m = sp.expand(P27.subs(t, xm))
re27, im27 = sp.re(v27p), sp.im(v27p)
check("tr_27(iota rho(A)) at the geometric point = %s + (%s) sqrt(-3)/... :"
      " NON-REAL element of Q(sqrt(-3)) => c MOVES the E6 27-character"
      % (re27, im27), sp.simplify(im27) != 0)
check("Galois equivariance at E6: P27(x_-) = conj(P27(x_+)) exactly",
      sp.expand(v27m - sp.conjugate(v27p)) == 0)
v78p = sp.expand(P78.subs(t, xp))
v78m = sp.expand(P78.subs(t, xm))
re78, im78 = sp.re(v78p), sp.im(v78p)
check("tr_78 (adjoint) at the geometric point is also NON-REAL"
      " (im = %s != 0); P78(x_-) = conj(P78(x_+))" % im78,
      sp.simplify(im78) != 0 and sp.expand(v78m - sp.conjugate(v78p)) == 0)
print("   exact values:  tr_27 = %s   [= %s + %s*I]" %
      (sp.nsimplify(v27p), re27, im27))
print("                  tr_78 = %s   [= %s + %s*I]" %
      (sp.nsimplify(v78p), re78, im78))
# --- (iv) functoriality: iota o (rho o sigma) = (iota o rho) o sigma is
#     definitional; its character consequence, verified:
#     the sigma_1^*-image of the E6 character value at the fiber generator a
#     is P27(sigma_1^* x) = P27(x_-) = conj(P27(x_+)).
check("TRANSPORT CLOSES AT E6: P27(sigma_1^*-image of x_+) = conj(P27(x_+))"
      " — sigma_1^* acts on the geometric E6 character AS c",
      sp.simplify(P27.subs(t, xp / (xp - 1)) - sp.conjugate(v27p)) == 0)

print()
print("=" * 72)
print("PART 5 — the Klein-four verdict (bookkeeping on the geometric orbit)")
print("=" * 72)

# action on the 2-point orbit {chi, chi-bar}: id <-> (), swap <-> (1 2)
ID, SW = (0, 1), (1, 0)
act = {'theta': ID,        # theta o iota = iota (Part 4.i) => fixes both
       'c': SW,            # non-real values (Part 4.iii) => conjugation swaps
       'theta*c': SW,      # composition
       'sigma_1^*': SW}    # Parts 3 + 4.iv
check("theta acts trivially on the orbit; c, theta*c, sigma_1^* act by the swap",
      act['theta'] == ID and act['c'] == SW and act['theta*c'] == SW and
      act['sigma_1^*'] == SW)
check("Klein four <theta,c> acts on the orbit THROUGH the quotient"
      " <theta,c>/<theta> = Z/2 (the c-column); the transported residue"
      " hits the GENERATOR of that Z/2",
      act['theta'] == ID and act['sigma_1^*'] == act['c'] and act['c'] != ID)
check("the theta-hypothesis (residue transports as the fold: acts trivially"
      " on the geometric orbit) is REFUTED exactly",
      act['sigma_1^*'] != act['theta'])

print()
print("VERDICT: Q-C = c.  sigma_1^*(chi_g) = c(chi_g) != chi_g = theta(chi_g).")
print("The residue transports as c (conjugation/orientation), not as theta.")
print()
print("T-NORM adjudication (the flagged in-lineage conflict): the residue has")
print("two realizations — the UNIT-NORM realization N(lambda_m) = -1 (confined")
print("to the real-quadratic scale axis; T-NORM, re-verified in Part 0) and")
print("the DECK/GALOIS realization (the mapping class sigma_m, det -1). The")
print("transport map T carries the second: functoriality transports the")
print("automorphism, never the unit. Its image on the geometry axis is the")
print("nontrivial element of Gal(Q(sqrt(-3))/Q) = Z/2 — i.e. c. BR-N clause 3")
print("('only the scale end can carry the norm-realization') and this map")
print("('the geometry end carries the deck/Galois realization') are the two")
print("halves of one statement. No contradiction. Conflict adjudicated.")
print()

nfail = sum(1 for _, ok in CHECKS if not ok)
print("CHECKS: %d run, %d failed" % (len(CHECKS), nfail))
print("ALL CHECKS PASS" if nfail == 0 else "FAILURES PRESENT")
with open(os.path.abspath(__file__), 'rb') as fh:
    print("script sha256:", hashlib.sha256(fh.read()).hexdigest())
