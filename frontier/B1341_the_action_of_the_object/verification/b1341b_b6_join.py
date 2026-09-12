"""B1341 second addendum -- B6's field equation and B1341's obstruction are ONE NUMBER.

Found by applying the discipline this arc's FIRST addendum registered: main's newest commit (B1247,
"the index was keyed on NOUNS and every question asked of it was a VERB") names B6 as an arc
"holding the very kinetic term B1157 lists as missing, on ZERO surfaces since week one". B6 was
therefore read -- to its claim line, not its title.

B6 (OPEN, week one): the Euler-Lagrange equation of L = (1/2)(d tau)^2 - V(tau) with the DERIVED
potential V(tau) = kappa(tau^3/3 - tau^2/2 - tau) is  box tau + kappa(tau^2 - tau - 1) = 0, with
stationary points tau = phi (stable) and tau = -1/phi (unstable). B6's own fence: "the potential is
derived; the field theory is a natural but not unique extension ... the lift is a CHOICE."

THE QUESTION: is the polynomial tau^2 - tau - 1 in B6 the SAME object as the characteristic
polynomial of the half step in B1341, or a coincidence of the golden ratio appearing twice?

PRE-REGISTERED: J1 B6's stationary polynomial IS char(C) for C = L.P = B448's half-monodromy;
J2 the PRODUCT of B6's two stationary points is det(C) = -1, which is exactly B1341's obstruction;
J3 the monodromy C^2 has product +1 and so is NOT obstructed -- so B6's stationary points are the
eigenvalues of the map that has NO action, not of the one that has one; J4 a control -- the silver
morphism gives a DIFFERENT stationary polynomial and a DIFFERENT product, so the coincidence is
object-specific and the test could have failed.
"""
import sympy as sp

tau, lam = sp.symbols('tau lam')
fails = []
def check(tag, label, ok):
    print(f"   [{'PASS' if ok else 'FAIL'}] {tag}: {label}")
    if not ok: fails.append(tag)

L = sp.Matrix([[1, 1], [0, 1]]); R = sp.Matrix([[1, 0], [1, 1]]); P = sp.Matrix([[0, 1], [1, 0]])
C = L * P                                   # B448's half-monodromy = B1341's genesis morphism
MONO = C ** 2                               # the figure-eight monodromy = L o R (B448, verified)

print("J1 -- B6's stationary polynomial vs the half step's characteristic polynomial")
b6_stat = tau ** 2 - tau - 1                                   # V'(tau)/kappa, B6's own expression
charC = sp.expand(C.charpoly(lam).as_expr())
print(f"      B6:   V'(tau)/kappa = {b6_stat}")
print(f"      B1341: char(C) = char(L.P) = {charC},  C = {C.tolist()}")
check("J1", "they are the SAME polynomial -- B6's stationary points are the eigenvalues of the "
            "half step, not a second appearance of the golden ratio",
      sp.simplify(charC.subs(lam, tau) - b6_stat) == 0)

print("\nJ2 -- the product of B6's stationary points")
roots = sp.solve(b6_stat, tau)
phi = (1 + sp.sqrt(5)) / 2
prod = sp.simplify(roots[0] * roots[1])
rs = sorted([sp.simplify(r) for r in roots], key=lambda r: float(r))
same = sp.simplify(rs[0] - (-1 / phi)) == 0 and sp.simplify(rs[1] - phi) == 0
print(f"      B6's stationary points: {rs}   are exactly (-1/phi, phi): {same}")
check("J2a", "B6's stationary points are literally -1/phi and phi (the golden and its Galois "
             "conjugate), as B6 states", same)
print(f"      their PRODUCT = {prod}   and   det(C) = {C.det()}")
check("J2", "the product of B6's two stationary points IS det(L.P) = -1 -- the very determinant "
            "B1341 proves is the obstruction to the half step having any discrete Lagrangian",
      prod == -1 == C.det())

print("\nJ3 -- and it is the OBSTRUCTED map whose eigenvalues they are")
print(f"      half step C:   eigenvalues {sorted([sp.simplify(r) for r in roots], key=lambda r: float(r))}, "
      f"product {C.det()}  -> anti-variational (B1341 Q3)")
ev2 = sorted([sp.simplify(v) for v in MONO.eigenvals()], key=lambda r: float(r))
print(f"      monodromy C^2: eigenvalues {ev2}, product {MONO.det()}  -> variational (B1341 Q5)")
check("J3", "B6's field equation is stationary exactly at the eigenvalues of the map that has NO "
            "action; the map that HAS one (the monodromy) has eigenvalue product +1",
      C.det() == -1 and MONO.det() == 1 and sp.simplify(sp.prod(ev2) - 1) == 0)

print("\nJ4 -- CONTROL: the silver morphism must give a different answer, or nothing was tested")
S = L ** 2 * R ** 2                          # B448's silver monodromy S = L^2 R^2
Shalf = L ** 2 * P                           # the corresponding det -1 half
print(f"      silver S = L^2 R^2 = {S.tolist()}, char {sp.expand(S.charpoly(lam).as_expr())}, det {S.det()}")
print(f"      silver half L^2.P = {Shalf.tolist()}, char {sp.expand(Shalf.charpoly(lam).as_expr())}, det {Shalf.det()}")
check("J4", "the silver half's characteristic polynomial is NOT tau^2 - tau - 1, so J1 is "
            "object-specific and could have failed",
      sp.simplify(sp.expand(Shalf.charpoly(lam).as_expr()).subs(lam, tau) - b6_stat) != 0)

print("\nREAD-OUT")
print("  B6 fenced its own result: 'the potential is derived; the LIFT is a CHOICE', locating the")
print("  choice in the kinetic term. B1341 names what is underneath that choice: at the level the")
print("  object actually supplies -- a discrete map on a surface -- there is NO Lagrangian at the")
print("  half step to lift, and the number that forbids one is the PRODUCT OF B6'S OWN STATIONARY")
print("  POINTS. One number, -1, wearing three names in this record:")
print("    * 'the product of creation is inversion', lambda.sigma(lambda) = -1  (CRYSTALLIZATION)")
print("    * det(C) for B448's det-(-1) half-monodromy C = [[1,1],[1,0]]        (B448)")
print("    * the anti-symplectic obstruction to a discrete Lagrangian            (B1341)")
print("  and it is the product of phi and -1/phi                                 (B6).")
print("\nB1341b:", "PASS" if not fails else f"FAIL ({fails})")
raise SystemExit(0 if not fails else 1)
