"""B1304 Q1 -- R20's C3-compatible character locus and the algebraic twisted cohomology of m202, from main's own data (DESIGN sealed 866bd71e).
Inputs: B1302's census of m202's isometry action on H_1 = Z^2 (the order-3 matrices), and the one-relator presentation
pi_1(m202) = <a, b | aabbAbAABBaB> (fc R72b, used by the audit seat's R20; exponent sums zero, so H_1 = Z^2 with basis a, b).
Computed here: the characters chi: Z^2 -> U(1) fixed by the C3 action (kernel of M^T - I on the torus), the Fox Jacobian, the
Alexander polynomial Delta(t1, t2) (cross-checked against B1302: seven monomials, coefficients +-1), Delta at the fixed characters,
and the algebraic h^1(m202; chi) = dim ker d^1 - rank d^0 for the aspherical one-relator complex."""
import json, os, sys, itertools
import sympy as sp
fails = []
def check(label, ok):
    print(("  [PASS] " if ok else "  [FAIL] ") + label)
    if not ok: fails.append(label)
HERE = os.path.dirname(os.path.abspath(__file__))
census = json.load(open(os.path.join(HERE, "..", "..", "B1302_the_sibling_m202", "verification", "m202_census.json")))
ord3 = [a for a in census["actions"] if a["order"] == 3]
print(f"  order-3 H1 actions in B1302's census: {[a['action'] for a in ord3]}")
M = sp.Matrix(ord3[0]["action"])
check("(a) the order-3 action has characteristic polynomial t^2 + t + 1 and det(M - I) = 3", sp.expand(M.charpoly().as_expr()) == sp.expand(sp.Symbol('lambda')**2 + sp.Symbol('lambda') + 1) and (M - sp.eye(2)).det() == 3)
# fixed characters: v in (R/Z)^2 with (M^T - I) v in Z^2  <=>  v in (M^T - I)^{-1} Z^2 / Z^2, a group of order |det| = 3
A = (M.T - sp.eye(2)); Ainv = A.inv()
fixed = set()
for m in itertools.product(range(-3, 4), repeat=2):
    v = Ainv * sp.Matrix(m); v = sp.Matrix([sp.nsimplify(x % 1) for x in v]); fixed.add((v[0], v[1]))
fixed = sorted(fixed); print(f"  C3-fixed characters (as (theta_a, theta_b) in (Q/Z)^2): {fixed}")
check("(a) exactly three C3-fixed characters: the trivial one and a conjugate pair of order 3", len(fixed) == 3 and (sp.Integer(0), sp.Integer(0)) in fixed and all(all(3 * x % 1 == 0 for x in f) for f in fixed) and sorted(f for f in fixed if f != (0, 0)) == sorted([tuple(sp.nsimplify((-x) % 1) for x in f) for f in fixed if f != (0, 0)]))
# Fox calculus on the relator
rel = "aabbAbAABBaB"
t1, t2 = sp.symbols('t1 t2')
img = {'a': t1, 'A': 1 / t1, 'b': t2, 'B': 1 / t2}
def fox(word, gen):
    """Fox derivative d(word)/d(gen) under the abelianisation, gen in {'a','b'}"""
    out = 0; prefix = 1
    for ch in word:
        if ch == gen: out += prefix
        elif ch == gen.upper(): out += -prefix * img[ch]      # d(x^-1) = -x^-1
        prefix *= img[ch]
    return sp.simplify(out)
da, db = fox(rel, 'a'), fox(rel, 'b')
ex = {'a': rel.count('a') - rel.count('A'), 'b': rel.count('b') - rel.count('B')}
check("(b) the relator abelianises to zero (H_1 = Z^2 with basis a, b)", ex == {'a': 0, 'b': 0})
# Alexander polynomial = gcd of the Fox entries (Laurent polynomials): clear denominators, take polynomial gcd
num_a = sp.expand(sp.together(da) * t1**8 * t2**8); num_b = sp.expand(sp.together(db) * t1**8 * t2**8)
num_a = sp.Poly(sp.expand(sp.cancel(num_a)), t1, t2); num_b = sp.Poly(sp.expand(sp.cancel(num_b)), t1, t2)
Delta = sp.gcd(num_a, num_b).as_expr()
Delta = sp.factor(Delta)
# strip monomial units
D = sp.Poly(sp.expand(Delta), t1, t2); terms = D.terms()
mindeg = [min(t[0][i] for t in terms) for i in range(2)]
Dn = sp.expand(sum(c * t1**(e[0] - mindeg[0]) * t2**(e[1] - mindeg[1]) for e, c in terms))
print(f"  Delta_m202 (up to units) = {Dn}")
Dterms = sp.Poly(Dn, t1, t2).terms()
check("(b) Delta has seven monomials with coefficients +-1 (B1302's Fox result by another presentation)", len(Dterms) == 7 and all(abs(c) == 1 for e, c in Dterms))
# evaluate at the fixed characters; algebraic twisted h^1 for chi != 1: dim ker d1 - rank d0 = (2 - rank[da db](chi)) - 1
def at(expr, th):
    return sp.nsimplify(sp.simplify(expr.subs({t1: sp.exp(2 * sp.pi * sp.I * th[0]), t2: sp.exp(2 * sp.pi * sp.I * th[1])})))
rows = []
for f in fixed:
    if f == (0, 0):
        rows.append(dict(chi=str(f), Delta="1 (trivial character)", h1=2, note="b_1 = 2")); continue
    dv = at(Dn, f); ja, jb = at(da, f), at(db, f)
    rank = 0 if (ja == 0 and jb == 0) else 1
    h1 = (2 - rank) - 1
    rows.append(dict(chi=str(f), Delta=str(dv), fox=[str(ja), str(jb)], h1=h1))
    print(f"  chi = {f}: Delta(chi) = {dv}  |Delta| = {float(abs(sp.N(dv))):.6f};  Fox row = ({ja}, {jb});  algebraic h^1(m202; chi) = {h1}")
pair = [r for r in rows if r["chi"] != "(0, 0)"]
check("(c) Delta(chi) != 0 at both characters of the pair (they are OFF the Alexander zero locus)", all(sp.N(sp.Abs(sp.sympify(r["Delta"]))) > 1e-9 for r in pair))
check("(c') the algebraic twisted h^1 at the pair is 1 (the DESIGN's prediction)", all(r["h1"] == 1 for r in pair))
json.dump(dict(M=[list(map(int, r)) for r in M.tolist()], fixed=[[str(x) for x in f] for f in fixed], Delta=str(Dn), rows=rows, fails=fails), open("b1304_c3_locus.json", "w"), indent=1)
print("Q1:", "PASS" if not fails else f"FAIL ({len(fails)})"); sys.exit(0 if not fails else 1)
