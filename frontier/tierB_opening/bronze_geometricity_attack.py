import sympy as sp

z1 = (1 + sp.sqrt(-7))/2
z2 = (1 - sp.sqrt(-7))/2

print("=== 1. Is (-1,-1,z) on the Markov surface x^2+y^2+z^2 = xyz  (<=> tr[a,b] = -2)? ===")
for z in (z1, z2):
    x, y = sp.Integer(-1), sp.Integer(-1)
    lhs = sp.simplify(x**2 + y**2 + z**2)
    rhs = sp.simplify(x*y*z)
    print(f"  z={sp.nsimplify(z)}:  lhs-rhs = {sp.simplify(lhs-rhs)}   on-surface={sp.simplify(lhs-rhs)==0}")

print("\n=== 2. tr[a,b] from the triple:  tr[a,b] = x^2+y^2+z^2-xyz-2 ===")
x, y = sp.Integer(-1), sp.Integer(-1)
comm = sp.simplify(x**2+y**2+z1**2 - x*y*z1 - 2)
print(f"  tr[a,b] = {comm}   (punctured torus needs EXACTLY -2, parabolic peripheral)")

print("\n=== 3. THE ATTACK: what is an element of trace -1 in SL(2,C)? ===")
lam = sp.symbols('lam')
for t in (sp.Integer(-1), sp.Integer(1)):
    roots = sp.solve(sp.Eq(lam + 1/lam, t), lam)
    print(f"  trace {t}: eigenvalues {[sp.nsimplify(r) for r in roots]}")
    for r in roots:
        # multiplicative order of the eigenvalue = order of the elliptic element
        n = 1
        while n <= 24 and sp.simplify(r**n - 1) != 0:
            n += 1
        print(f"     |lambda|={sp.simplify(sp.Abs(r))}, lambda^{n}=1  -> ELLIPTIC of order {n} in SL2 "
              f"(order {n//2 if n%2==0 else n} in PSL2)")
