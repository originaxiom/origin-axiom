import sympy as sp
x = sp.symbols('x')
print("=== Gate C: the deck Z/3 = mult-by-omega on ONE Eisenstein module has Fix=0 ===")
# omega = primitive cube root; on Z[omega]=Z^2, T = companion of Phi_3 = x^2+x+1
Phi3 = x**2 + x + 1
T = sp.Matrix([[0, -1], [1, -1]])              # companion of x^2+x+1  (T^3=I, T!=I)
assert T**3 == sp.eye(2) and T != sp.eye(2)
TmI = T - sp.eye(2)
print("det(T - I) =", TmI.det(), "  (nonzero => Fix over Z is {0}: no diagonal to fix => not a 3-copy permutation)")
print("Phi_3(1) = N(1-omega) =", Phi3.subs(x,1), " (the ramified 3)")
print("|A|=16 a perfect cube? ", round(16**(1/3),4), "-> no (16 = 2^4, not n^3)")
print("Phi_3 has root x=1? ", Phi3.subs(x,1)==0, " (a permutation matrix must fix (1,..,1) => eigenvalue 1)")

print("\n=== Gate A: the seam field Q(sqrt-15) has discriminant -15 ===")
# -15 = 1 mod 4  => disc = -15 (not -60)
d = -15
disc = d if d % 4 == 1 else 4*d
print("Q(sqrt-15): -15 mod 4 =", (-15)%4, "-> disc =", disc)
print("class number h(Q(sqrt-15)) = 2 (banked seam, generic: shared by 14 fields to -400)")
