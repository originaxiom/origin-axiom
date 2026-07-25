"""
B784 A4 (part 4): Fix the SymPy substitution bug and produce final verification.
"""
from sympy import (
    Matrix, sqrt, Rational, I, simplify, expand, Symbol, N, eye, pprint,
    symbols, Dummy
)

x, y, z = symbols('x y z')
omega = Rational(-1, 2) + I * sqrt(3) / 2

# T_sigma(x,y,z) = (z, x, xz-y)
# T_{CsC}(x,y,z) = (y, z, yz-x)

# Step 1: Verify T_{CsC} = P * T_sigma(Pv) directly
P = Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
T_sigma_vec = Matrix([z, x, x*z - y])
T_CsC_vec = Matrix([y, z, y*z - x])

# P*v = (y,x,z), so T_sigma(P*v) = T_sigma(y,x,z)
# Use simultaneous substitution via a dummy
_x = Dummy('x')
T_sigma_at_Pv = T_sigma_vec.subs(x, _x).subs(y, x).subs(_x, y)
# This gives T_sigma(y, x, z)
print("T_sigma(y, x, z) =", T_sigma_at_Pv.T)

P_times_T_sigma_at_Pv = P * T_sigma_at_Pv
print("P * T_sigma(Pv) =", simplify(P_times_T_sigma_at_Pv).T)
print("T_{CsC}(v)      =", T_CsC_vec.T)
diff_T = simplify(P_times_T_sigma_at_Pv - T_CsC_vec)
print("Difference:", diff_T.T)
assert diff_T == Matrix.zeros(3, 1), "T_{CsC} = P * T_sigma(Pv) FAILED"
print("CONFIRMED: T_{CsC}(v) = P * T_sigma(Pv) for all v.")
print()

# Step 2: Jacobian intertwining via chain rule (using dummy for simultaneous sub)
J_sigma_sym = T_sigma_vec.jacobian([x, y, z])
J_CsC_sym = T_CsC_vec.jacobian([x, y, z])

# J_sigma at (y,x,z): swap x<->y simultaneously
J_sigma_at_Pv = J_sigma_sym.subs(x, _x).subs(y, x).subs(_x, y)
print("J_sigma(y, x, z) =")
pprint(J_sigma_at_Pv)
print()

conj_correct = P * J_sigma_at_Pv * P
print("P * J_sigma(y,x,z) * P =")
pprint(simplify(conj_correct))
print()

print("J_{CsC}(x,y,z) =")
pprint(J_CsC_sym)
print()

diff_correct = simplify(conj_correct - J_CsC_sym)
print("P * J_sigma(Pv) * P - J_{CsC}(v) =")
pprint(diff_correct)
if diff_correct == Matrix.zeros(3, 3):
    print("CONFIRMED: Chain-rule intertwining holds IDENTICALLY for all (x,y,z).")
else:
    print("UNEXPECTED: residual found.")
    for i in range(3):
        for j in range(3):
            e = simplify(diff_correct[i,j])
            if e != 0:
                print(f"  Entry ({i},{j}) = {e}")
print()

# Step 3: At geometric point (where x=y=2, so the naive conjugation also works)
x0, y0, z0 = 2, 2, 2 - omega
subs_geo = {x: x0, y: y0, z: z0}

J_sigma_geo = J_sigma_sym.subs(subs_geo)
J_CsC_geo = J_CsC_sym.subs(subs_geo)

print("At geometric point (2, 2, 5/2 - I*sqrt(3)/2):")
print("J_sigma|geo =")
pprint(J_sigma_geo)
print()

conj_geo = P * J_sigma_geo * P
diff_geo = simplify(conj_geo - J_CsC_geo)
print("P * J_sigma|geo * P = J_{CsC}|geo?", diff_geo == Matrix.zeros(3, 3))
print()

# Step 4: Determinant
det_sigma = J_sigma_geo.det()
det_CsC = J_CsC_geo.det()
print(f"det(J_sigma|geo) = {simplify(det_sigma)}")
print(f"det(J_{'{CsC}'}|geo) = {simplify(det_CsC)}")
print()

# Step 5: Char poly
lam = Symbol('lambda')
cp = J_sigma_geo.charpoly(lam).as_expr()
print(f"Characteristic polynomial: {expand(cp)}")
print()

# Step 6: C-eigenbasis decomposition (the core result)
print("=" * 60)
print("C-EIGENBASIS BLOCK STRUCTURE")
print("=" * 60)

Q = Matrix([[1, 0, 1], [1, 0, -1], [0, 1, 0]])  # columns: e_even1, e_even2, e_odd
Q_inv = Q.inv()

J_C_basis = simplify(Q_inv * J_sigma_geo * Q)
print("J_sigma|geo in C-eigenbasis {(1,1,0), (0,0,1), (1,-1,0)}:")
pprint(J_C_basis)
print()

# Verify P in this basis
P_C_basis = Q_inv * P * Q
print("P in C-eigenbasis (should be diag(1,1,-1)):")
pprint(P_C_basis)
print()

# The diagonal block structure:
print("Even-even block (2x2):")
pprint(J_C_basis[:2, :2])
print()
print("Odd-odd entry (1x1):", simplify(J_C_basis[2, 2]))
print()
print("Even-to-odd coupling (row 3 of even cols):")
print(f"  [{simplify(J_C_basis[2,0])}, {simplify(J_C_basis[2,1])}]")
print()
print("Odd-to-even coupling (col 3 of even rows):")
print(f"  [{simplify(J_C_basis[0,2])}]")
print(f"  [{simplify(J_C_basis[1,2])}]")
print()

# Under C-conjugation diag(1,1,-1) * J * diag(1,1,-1):
# even-even block: unchanged
# odd-odd entry: unchanged
# even-odd couplings: SIGN FLIPPED
D = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, -1]])
J_CsC_C_basis = simplify(Q_inv * J_CsC_geo * Q)
conj_check = simplify(D * J_C_basis * D - J_CsC_C_basis)
print("D * J_sigma_basis * D - J_{CsC}_basis:")
pprint(conj_check)
assert conj_check == Matrix.zeros(3, 3)
print("CONFIRMED: C-conjugation flips even-odd couplings, preserves blocks.")
print()

# Step 7: Numerical eigenvalues for display
import cmath
evals_num = [complex(N(ev, 30)) for ev in J_sigma_geo.eigenvals().keys()]
evals_num.sort(key=lambda z: -abs(z))

print("=" * 60)
print("EIGENVALUE TABLE")
print("=" * 60)
print(f"{'eigenvalue':>35s}  {'|lam|':>10s}  {'arg (deg)':>10s}")
for ev in evals_num:
    r, theta = cmath.polar(ev)
    print(f"  {ev.real:+.8f}{ev.imag:+.8f}i  {r:10.8f}  {theta*180/cmath.pi:+10.4f}")
print()
print(f"Product = {evals_num[0]*evals_num[1]*evals_num[2].real:+.8f} (det = -1)")
print(f"Sum     = {sum(evals_num).real:+.8f} (trace = 2)")
print()

# Golden ratio comparison
phi_n = (1 + 5**0.5) / 2
print(f"phi^2 = {phi_n**2:.8f} vs |lam_0| = {abs(evals_num[0]):.8f}")
print(f"1/phi^2 = {1/phi_n**2:.8f} vs |lam_2| = {abs(evals_num[2]):.8f}")
print("Eigenvalue magnitudes do NOT match phi^2, 1/phi^2.")
print("Reason: geometric point is complex and not a fixed point.")
print()

# Step 8: Even block eigenvalues
even_block = J_C_basis[:2, :2]
ev_even = even_block.eigenvals()
print("Even-block eigenvalues:")
for ev, mult in ev_even.items():
    ev_n = complex(N(ev, 20))
    print(f"  {ev_n.real:+.8f}{ev_n.imag:+.8f}i  (mult {mult})")
print()
print(f"Odd-block eigenvalue: {complex(N(J_C_basis[2,2], 20))}")
print()
print("The even block governs dynamics ON the C-even locus (x=y).")
print("The odd entry governs transverse drift off the C-even locus.")
print("C-conjugation preserves both blocks but flips their coupling.")
