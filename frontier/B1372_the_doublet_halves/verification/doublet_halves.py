#!/usr/bin/env python3
"""B1372 -- THE DOUBLET HALVES (door 2): can a Standard-Model generation be assembled from SL(2)_beta-DOUBLET sectors alone -- the 10
from the 78's (2,20) and the 5bar from the 27's (2,6bar) -- so that the non-abelian part of the flat E6(C) connection, and not a
character, carries the Higgs data on both halves?  B1368's spin split shows one half is spin 0 inside each of the 27 and the 78;
this arc closes the third reading, the mixed frame, by charge arithmetic at the cusp, and records the two lemmas on non-abelian
cusp holonomy (parabolic and central) that make the doublet sectors vector-like there.

Frame (B1351, B1368, B1369): the connection's image lies in c(SM) = SL(2)_beta x C*^2; a doublet sector is V_2 (x) chi_w with chi_w
the character on (Y, gamma) evaluated on the weight; on cusp c the peripheral holonomy rho(mu), rho(lambda) commutes and is either
parabolic (eigenvalues +-1, non-scalar), central (+-I) or diagonalisable with eigenvalues m^{+-1}, m != +-1.  The sector is cusp-fixed
iff some joint eigenvector has total holonomy 1: chi_w(p) = m_p^{-1} (e_1) or m_p (e_2) for p = mu, lambda.
  (A) the table: every Standard-Model weight of the 27 and the 78 with its SU(5) piece, its SL(2)_beta spin (beta.w) and gamma;
      the frame theorem (27: 10 spin 0, 5bar spin 1/2; 78: 10 spin 1/2, 5bar spin 0) and the unique both-doublet assignment.
  (B) non-unitary cusp eigenvalue (|m_p| != 1): the 10 (gamma = 1) forces Im s(p) = 0 and Im t(p) = +-L; the 5bar (gamma = 1/3)
      forces Im t(p) = +-3L: no simultaneous cusp-fixedness for L != 0.  Exact, all sign patterns.
  (C) unitary cusp eigenvalue m_p = e^{2 pi i theta}: the fifteen congruences Y(w) a + gamma(w) b + eps_w theta in Z force
      theta in (1/4) Z; at theta = +-1/4 the eigenvector choices eps_w are never uniform: either the 10 and the 5bar choose opposite
      eigenvectors, or Q and d^c choose one and u^c, e^c, L the other.  Exact, by solving the congruences symbolically.
  (D) m004: the order-4 points of the character variety (tr rho(mu) = 0 with rho(lambda) fixing a vector) are the four SU(2)
      dihedral representations: unitary, no Higgs field -- verified by an invariant positive Hermitian form.
Usage: python3 doublet_halves.py  (seconds)"""
import itertools, warnings
warnings.filterwarnings("ignore")
from fractions import Fraction as Fr
import sympy as sp

# ---------------------------------------------------------------- the E6 root system and the 27 in SO(10) x U(1) coordinates (B1364-B1369)
def roots_e6():
    R = []
    for i in range(5):
        for j in range(i + 1, 5):
            for si in (1, -1):
                for sj in (1, -1):
                    v = [Fr(0)] * 5; v[i] = Fr(si); v[j] = Fr(sj); R.append((tuple(v), Fr(0)))
    for signs in itertools.product((1, -1), repeat=5):
        if signs.count(-1) % 2 == 0:
            w = tuple(Fr(s, 2) for s in signs); R.append((w, Fr(1))); R.append((tuple(-x for x in w), Fr(-1)))
    return R
def weights_27():
    W = []
    for signs in itertools.product((1, -1), repeat=5):
        if signs.count(-1) % 2 == 1:
            W.append((tuple(Fr(s, 2) for s in signs), Fr(1, 3)))
    for k in range(5):
        for s in (1, -1):
            v = [Fr(0)] * 5; v[k] = Fr(s); W.append((tuple(v), Fr(-2, 3)))
    W.append(((Fr(0),) * 5, Fr(4, 3)))
    return W
def dot(a, b): return sum(x * y for x, y in zip(a[0], b[0])) + Fr(3, 4) * a[1] * b[1]
def vec(*xs): return (tuple(Fr(x) for x in xs[:5]), Fr(xs[5]))
R78 = roots_e6(); W27 = weights_27()
assert len(R78) == 72 and len(W27) == 27
Y = vec(Fr(-1, 3), Fr(-1, 3), Fr(-1, 3), Fr(1, 2), Fr(1, 2), 0)
beta = vec(Fr(1, 2), Fr(1, 2), Fr(1, 2), Fr(1, 2), Fr(1, 2), 1)
gamma = vec(Fr(1, 2), Fr(1, 2), Fr(1, 2), Fr(1, 2), Fr(1, 2), Fr(-5, 3))
assert dot(beta, gamma) == 0 and dot(beta, Y) == 0 and dot(gamma, Y) == 0
def sm_type(w):
    """(colour, weak, Y): colour from the SU(3) weight (w1, w2, w3) minus its mean, weak from w4 - w5"""
    c = [w[0][i] for i in range(3)]; m = sum(c) / 3; red = [x - m for x in c]
    if all(x == 0 for x in red): col = "1"
    elif any(x == Fr(2, 3) for x in red): col = "3"
    elif any(x == Fr(-2, 3) for x in red): col = "3b"
    else: col = "?"
    weak = "2" if w[0][3] != w[0][4] else "1"
    return (col, weak, dot(Y, w))
NAMES = {("3", "2", Fr(1, 6)): "Q", ("3b", "1", Fr(-2, 3)): "u^c", ("1", "1", Fr(1)): "e^c", ("3b", "1", Fr(1, 3)): "d^c/Dbar", ("1", "2", Fr(-1, 2)): "L/H_d",
         ("1", "1", Fr(0)): "nu^c/N", ("3", "1", Fr(-1, 3)): "D", ("1", "2", Fr(1, 2)): "H_u",
         ("3b", "2", Fr(-1, 6)): "Qbar", ("3", "1", Fr(2, 3)): "u", ("1", "1", Fr(-1)): "e", ("3", "1", Fr(1, 3)): "Dbar'", ("3b", "1", Fr(-1, 3)): "d"}
SU5 = {"Q": "10", "u^c": "10", "e^c": "10", "d^c/Dbar": "5b", "L/H_d": "5b", "nu^c/N": "1", "D": "5", "H_u": "5"}

print("=== (A) the Standard-Model weights of the 27 and of the 78: SU(5) piece, SL(2)_beta spin, gamma ===")
def table(weights, label):
    rows = {}
    for w in weights:
        t = sm_type(w); nm = NAMES.get(t, f"exotic {t}")
        b = dot(beta, w); g = dot(gamma, w)
        rows.setdefault((nm, b, g), 0); rows[(nm, b, g)] += 1
    print(f"  {label}:")
    for (nm, b, g), n in sorted(rows.items(), key=lambda kv: (str(kv[0][0]), kv[0][1], kv[0][2])):
        spin = 'spin 0' if b == 0 else ('doublet' if abs(b) == 1 else 'triplet: the SL(2)_beta adjoint')
        su5 = SU5.get(nm, '10b' if nm in ('Qbar', 'u', 'e') else ('24' if nm.startswith('exotic') else '-'))
        print(f"    {nm:12s} x{n:2d}   beta.w = {str(b):>4s} ({spin})   gamma = {str(g):>5s}   SU(5): {su5}")
    return rows
rows27 = table(W27, "the 27"); rows78 = table(R78, "the 78 (the roots; the Cartan is neutral)")
def spins(rows, nm): return sorted({b for (n, b, g) in rows if n == nm})
def gammas(rows, nm): return sorted({g for (n, b, g) in rows if n == nm})
ten27 = [spins(rows27, n) for n in ("Q", "u^c", "e^c")]; five27 = [spins(rows27, n) for n in ("d^c/Dbar", "L/H_d")]
ten78 = [spins(rows78, n) for n in ("Q", "u^c", "e^c")]; five78 = [spins(rows78, n) for n in ("d^c/Dbar", "L/H_d")]
print(f"  frame theorem: in the 27 the 10 has beta.w in {ten27} (spin 0) and the 5bar in {five27} (doublets); in the 78 the 10 has {ten78} (doublets) and the 5bar-type weights {five78}")
g10_78 = [g for (n, b, g) in rows78 if n in ("Q", "u^c", "e^c") and b != 0]
g5_27 = [g for (n, b, g) in rows27 if n in ("d^c/Dbar", "L/H_d") and b != 0]
print(f"  the only both-doublet assignment: the 10 from the 78's doublets, gamma = {sorted(set(g10_78))}; the 5bar from the 27's doublets, gamma = {sorted(set(g5_27))}")
assert set(g10_78) == {Fr(1)} and set(g5_27) == {Fr(1, 3)}
# the doublet weights of the 78's 10: Y-types; the 27's 5bar doublets: Y-types
types10 = sorted({(dot(Y, w), dot(gamma, w)) for w in R78 if NAMES.get(sm_type(w)) in ("Q", "u^c", "e^c") and dot(beta, w) != 0})
types5 = sorted({(dot(Y, w), dot(gamma, w)) for w in W27 if NAMES.get(sm_type(w)) in ("d^c/Dbar", "L/H_d") and dot(beta, w) != 0})
print(f"  (Y, gamma) types: the 10 in the 78 {[(str(a), str(b)) for a, b in types10]}; the 5bar in the 27 {[(str(a), str(b)) for a, b in types5]}")
TYPES = types10 + types5          # five (Y, gamma) types; every weight of a type carries the same character

# ---------------------------------------------------------------- (B) non-unitary cusp eigenvalue: no simultaneous cusp-fixedness
print("\n=== (B) a non-unitary peripheral eigenvalue m_p = e^{L} e^{i phase}, L != 0: the imaginary parts ===")
# chi_w(p) = exp(2 pi i (Y(w) s + gamma(w) t)) with s, t complex; |chi_w(p)| = exp(-2 pi (Y Im s + gamma Im t)) must equal |m_p|^{-+1} = e^{-+L}
sigma, tau, Lsym = sp.symbols('sigma tau L', real=True)
count_ok = 0; patterns = list(itertools.product((1, -1), repeat=5))
for eps in patterns:
    eqs = [sp.Eq(sp.Rational(Yw.numerator, Yw.denominator) * sigma + sp.Rational(gw.numerator, gw.denominator) * tau, e * Lsym) for (Yw, gw), e in zip(TYPES, eps)]
    sol = sp.solve(eqs, [sigma, tau], dict=True)
    if sol:
        s0 = sol[0]
        consistent = all(sp.simplify(eq.lhs.subs(s0) - eq.rhs) == 0 for eq in eqs)
        if consistent: count_ok += 1
print(f"  sign patterns (which eigenvector each of the five types fixes) admitting (Im s, Im t) with L != 0: {count_ok} of {len(patterns)}")
# the mechanism: the 10 alone forces Im s = 0, Im t = +-L; the 5bar alone forces Im t = +-3L
for name, tys in (("the 10 (three Y-types, gamma = 1)", types10), ("the 5bar (two Y-types, gamma = 1/3)", types5)):
    sols = set()
    for eps in itertools.product((1, -1), repeat=len(tys)):
        eqs = [sp.Eq(sp.Rational(Yw.numerator, Yw.denominator) * sigma + sp.Rational(gw.numerator, gw.denominator) * tau, e * Lsym) for (Yw, gw), e in zip(tys, eps)]
        sol = sp.solve(eqs, [sigma, tau], dict=True)
        if sol and all(sp.simplify(eq.lhs.subs(sol[0]) - eq.rhs) == 0 for eq in eqs):
            sols.add((str(sol[0][sigma]), str(sol[0][tau])))
    print(f"  {name}: consistent (Im s, Im t) = {sorted(sols)}")
print("  -> Theorem B: with a non-unitary eigenvalue on a peripheral element, the 10 of the 78 and the 5bar of the 27 are never cusp-fixed together.")

# ---------------------------------------------------------------- (C) unitary cusp eigenvalue: the congruences
print("\n=== (C) a unitary peripheral eigenvalue m_p = e^{2 pi i theta}: Y a + gamma b + eps theta in Z for the five types ===")
a, b, th = sp.symbols('a b theta', real=True)
n = sp.symbols('n1:6', integer=True)
theta_values = {}
Yg = [(sp.Rational(Yw.numerator, Yw.denominator), sp.Rational(gw.numerator, gw.denominator)) for (Yw, gw) in TYPES]
for eps in patterns:
    eqs = [Yg[i][0] * a + Yg[i][1] * b + e * th - n[i] for i, e in enumerate(eps)]
    found = False
    for trip in itertools.combinations(range(5), 3):
        sol = sp.solve([eqs[i] for i in trip], [a, b, th], dict=True)
        if not sol or len(sol[0]) < 3: continue
        s0 = sol[0]
        rest_idx = [i for i in range(5) if i not in trip]
        # linear forms in the triple's integers: theta = c0 + sum c_k n_k; each remaining equation gives r = d0 + sum d_k n_k - n_j
        def lin(expr):
            expr = sp.expand(expr)
            return (Fr(str(expr.subs({n[t]: 0 for t in trip}))), [Fr(str(expr.coeff(n[t]))) for t in trip])
        th_lin = lin(s0[th])
        rest_lin = [lin(sp.expand(Yg[i][0] * s0[a] + Yg[i][1] * s0[b] + eps[i] * s0[th])) for i in rest_idx]   # must be an integer
        found = True
        thetas = set()
        for vals in itertools.product(range(-6, 7), repeat=3):
            ok = all((c0 + sum(ck * v for ck, v in zip(cs, vals))).denominator == 1 for (c0, cs) in rest_lin)
            if ok:
                tv = th_lin[0] + sum(ck * v for ck, v in zip(th_lin[1], vals))
                thetas.add(sp.Rational(tv.numerator, tv.denominator) % 1)
        theta_values[eps] = thetas
        break
    if not found: theta_values[eps] = "singular"
all_thetas = set()
for eps, tv in theta_values.items():
    if tv != "singular": all_thetas |= tv
print(f"  theta mod 1 admitting a solution, over all 32 patterns: {sorted(all_thetas)}")
assert all_thetas <= {sp.Rational(0), sp.Rational(1, 4), sp.Rational(1, 2), sp.Rational(3, 4)}
print("  -> Theorem C: both halves cusp-fixed on the same cusp only when the peripheral eigenvalue is a fourth root of unity.")
# the sign structure at theta = +-1/4: which patterns admit a solution?
quarter = [eps for eps, tv in theta_values.items() if tv != "singular" and (sp.Rational(1, 4) in tv or sp.Rational(3, 4) in tv)]
labels = ["Q", "u^c", "e^c", "d^c", "L"]
print(f"  patterns with a solution at theta = +-1/4: {len(quarter)}:")
for eps in quarter:
    print(f"    {dict(zip(labels, eps))}  -> 10 uniform: {eps[0] == eps[1] == eps[2]}, 5bar uniform: {eps[3] == eps[4]}, all fifteen uniform: {len(set(eps)) == 1}")
uniform = [eps for eps in quarter if len(set(eps)) == 1]
print(f"  patterns with all fifteen weights on the same eigenvector: {len(uniform)}")
assert not uniform
print("  -> Theorem C': at the order-4 points the two halves (or the pieces of the 10) fix opposite eigenvectors, so their partitions by the")
print("     SL(2)_beta Higgs are complementary and their chiralities opposite: no generation from the doublet halves where the abelian Higgs vanishes.")
# an explicit solution for the record
for eps in quarter[:1]:
    eqs = [sp.Rational(Yw.numerator, Yw.denominator) * a + sp.Rational(gw.numerator, gw.denominator) * b + e * th - n[i] for i, ((Yw, gw), e) in enumerate(zip(TYPES, eps))]
    for vals in itertools.product(range(-3, 4), repeat=5):
        sol = sp.solve([eq.subs(dict(zip(n, vals))) for eq in eqs], [a, b, th], dict=True)
        if sol and len(sol[0]) == 3 and (sol[0][th] % 1) in (sp.Rational(1, 4), sp.Rational(3, 4)):
            print(f"  example: pattern {dict(zip(labels, eps))}, (a, b, theta) = ({sol[0][a]}, {sol[0][b]}, {sol[0][th]}) with integers {vals}")
            break

# ---------------------------------------------------------------- (D) m004's order-4 points are unitary
print("\n=== (D) m004: the order-4 points (tr rho(mu) = 0, rho(lambda) with a fixed vector) are the dihedral SU(2) representations ===")
# B1368's meridian presentation of the figure-eight knot group: <a, b | a w b^-1 w^-1>, w = b a^-1 b^-1 a; longitude w w*, w* = a b^-1 a^-1 b;
# Riley's normal form A = [[m, 1], [0, 1/m]], B = [[m, 0], [-y, 1/m]]  (a and b meridians)
m, y = sp.symbols('m y')
A = sp.Matrix([[m, 1], [0, 1 / m]]); B = sp.Matrix([[m, 0], [-y, 1 / m]])
W = [2, -1, -2, 1]; WSTAR = [1, -2, -1, 2]; REL = [1] + W + [-2] + [-x for x in reversed(W)]; LONG = W + WSTAR
def wmat(letters, Ma, Mb):
    out = sp.eye(2)
    for l in letters:
        X = Ma if abs(l) == 1 else Mb
        out = out * (X if l > 0 else X.inv())
    return sp.simplify(out)
Rm = wmat(REL, A, B) - sp.eye(2)
riley = sp.factor(sp.gcd(sp.numer(sp.together(Rm[0, 0])), sp.numer(sp.together(Rm[1, 0]))))
print(f"  relator a w b^-1 w^-1 (w = b a^-1 b^-1 a); Riley polynomial: {riley}")
Mlam = wmat(LONG, A, B)
pts = []
for mv in (sp.I, -sp.I):
    poly_y = sp.Poly(sp.expand(riley.subs(m, mv)), y)
    for yv in sp.roots(poly_y, multiple=True):
        Ma = A.subs({m: mv, y: yv}); Mb = B.subs({m: mv, y: yv})
        if sp.simplify(wmat(REL, Ma, Mb) - sp.eye(2)) != sp.zeros(2, 2):
            print(f"  m = {mv}, y = {sp.nsimplify(yv)}: not a representation (the factor y of the gcd is an artefact of the two entries used); dropped")
            continue
        Lm = sp.simplify(Mlam.subs({m: mv, y: yv}))
        trL = sp.nsimplify(sp.simplify(Lm.trace()))
        fixed = sp.simplify((Lm - sp.eye(2)).det()) == 0
        # unitarity: an invariant positive-definite Hermitian form H with X^dagger H X = H for X = rho(a), rho(b)
        h11, h22, r12, i12 = sp.symbols('h11 h22 r12 i12', real=True)
        H = sp.Matrix([[h11, r12 + sp.I * i12], [r12 - sp.I * i12, h22]])
        eqsH = []
        for X in (Ma, Mb):
            E = sp.expand(X.H * H * X - H)
            eqsH += [sp.re(E[0, 0]), sp.im(E[0, 0]), sp.re(E[0, 1]), sp.im(E[0, 1]), sp.re(E[1, 1]), sp.im(E[1, 1])]
        eqsH = [sp.nsimplify(sp.expand(e)) for e in eqsH]
        solH = sp.solve(eqsH, [h11, h22, r12, i12], dict=True)
        unitary = False
        if solH:
            Hs = H.subs(solH[0])
            free = sorted(Hs.free_symbols, key=str)
            if free: Hs = Hs.subs({fs: 1 for fs in free})
            dets = [sp.N(Hs[0, 0]), sp.N(Hs.det())]
            unitary = (dets[0] > 0 and dets[1] > 0) or (dets[0] < 0 and dets[1] > 0)
        pts.append((mv, yv, trL, fixed, unitary))
        print(f"  m = {mv}, y = {sp.nsimplify(yv)}: tr rho(lambda) = {trL}, rho(lambda) has eigenvalue 1: {fixed}, an invariant definite Hermitian form (conjugate into SU(2)): {unitary}")
n_fixed = sum(1 for p in pts if p[3]); n_unit = sum(1 for p in pts if p[3] and p[4])
print(f"  order-4 representations: {len(pts)}; with rho(lambda) fixing a vector (a cusp-fixed doublet sector possible): {n_fixed}; of them unitary: {n_unit} (B1368: the four SU(2) dihedral representations)")
assert n_fixed == n_unit == 4
print("DONE")
