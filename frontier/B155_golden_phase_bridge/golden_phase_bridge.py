#!/usr/bin/env python
"""
B155 — the 'golden x phase' spectral bridge (Result C).

A single integer 4x4 matrix M_g whose characteristic polynomial factors as
the figure-eight monodromy trace polynomial (the 'golden' factor x^2-3x+1,
discriminant 5, real/Anosov) TIMES the order-6 cyclotomic Phi_6 (the 'phase'
factor x^2-x+1, discriminant -3, |root|=1, finite order). It carries an
invariant symmetric form of signature (1,3) with discriminant -15 =
disc(Q(sqrt5)) * disc(Q(sqrt-3)), and glues the two invariant 2-planes over
Z with cokernel (Z/2)^2.

This is the n=4 'canonical object' at which the trace-map side (this repo's
metallic/figure-eight tower) and the Omega history-enumeration side
(R_{a,m} positive-shear family) meet: SAME charpoly x^4-4x^3+5x^2-4x+1, SAME
signature (1,3). The integer Omega lattice reaches this charpoly only at the
half-integer point a=4, m=-1/2 — so the bridge lives at the level of the
shared canonical object (Q-conjugacy class + signature), NOT at an integer
Omega point.

FIREWALL: signature (1,3) is ALGEBRAIC inertia of a bilinear form, NOT
spacetime. No physical claim. Standalone linear algebra / arithmetic.

Run: python golden_phase_bridge.py   (all checks must print PASS)
"""
import sympy as sp

x = sp.symbols('x')

ok_all = True
def check(name, cond):
    global ok_all
    if not cond:
        ok_all = False
    print(f"  [{'PASS' if cond else 'FAIL'}] {name}")
    return cond

def hr(s):
    print("\n==== " + s + " " + "=" * max(0, 56 - len(s)))

# The canonical matrix.
Mg = sp.Matrix([
    [1, 1, 0, 0],
    [0, 1, 1, 0],
    [1, 1, 1, 1],
    [1, 1, 0, 1],
])

golden = x**2 - 3*x + 1   # figure-eight monodromy: trace 3, disc 5, real (Anosov)
phase  = x**2 - x + 1     # Phi_6: trace 1, disc -3, primitive 6th roots of unity

# ---------------------------------------------------------------- spectrum
hr("spectrum: golden x phase")
chi = sp.expand(Mg.charpoly(x).as_expr())
print("    charpoly(M_g) =", chi)
check("charpoly = (x^2-3x+1)(x^2-x+1)", sp.expand(chi - golden*phase) == 0)
check("charpoly = x^4-4x^3+5x^2-4x+1",
      sp.expand(chi - (x**4 - 4*x**3 + 5*x**2 - 4*x + 1)) == 0)
check("golden disc = 5  (real, Q(sqrt5))", sp.discriminant(golden, x) == 5)
check("phase disc = -3  (Q(sqrt-3))", sp.discriminant(phase, x) == -3)
check("phase = cyclotomic Phi_6", sp.expand(phase - sp.cyclotomic_poly(6, x)) == 0)
check("det M_g = 1", Mg.det() == 1)
check("disc product 5*(-3) = -15", 5 * (-3) == -15)

# ---------------------------------------------------- rational block form
hr("rational block decomposition")
B_golden = sp.Matrix([[2, 1], [1, 1]])    # x^2-3x+1
B_phase  = sp.Matrix([[0, 1], [-1, 1]])   # x^2-x+1
Bdiag = sp.Matrix(sp.BlockDiagMatrix(B_golden, B_phase))

from sympy.matrices.normalforms import smith_normal_form
def invariant_factors(M):
    xm = x * sp.eye(M.shape[0]) - M
    snf = smith_normal_form(xm, domain=sp.QQ[x])
    return [sp.expand(sp.factor(snf[i, i])) for i in range(M.shape[0])]

inv_Mg = invariant_factors(Mg)
inv_Bd = invariant_factors(Bdiag)
print("    invariant factors M_g :", inv_Mg)
check("block A charpoly = golden", sp.expand(B_golden.charpoly(x).as_expr() - golden) == 0)
check("block B charpoly = phase",  sp.expand(B_phase.charpoly(x).as_expr() - phase) == 0)
check("M_g ~_Q  golden-block (+) phase-block", inv_Mg == inv_Bd)
check("M_g nonderogatory (min poly = char poly)", sp.expand(inv_Mg[-1] - chi) == 0)

# ---------------------------------------------------- glue group (Z/2)^2
hr("glue group: golden-plane (+) phase-plane in Z^4")
def primitive_int_basis(Msub):
    cols = []
    for v in Msub.nullspace():
        v = sp.Matrix(v)
        dens = [sp.Rational(c).q for c in v]
        v = v * sp.ilcm(*dens) if len(dens) > 1 else v * dens[0]
        ints = [int(c) for c in v]
        g = sp.igcd(*ints) if len(ints) > 1 else abs(ints[0])
        if g:
            v = sp.Matrix([c // g for c in ints])
        cols.append(v)
    return cols

Lp = primitive_int_basis(Mg**2 - 3*Mg + sp.eye(4))   # golden(M)=0 -> phase 2-plane
Lg = primitive_int_basis(Mg**2 - Mg + sp.eye(4))     # phase(M)=0  -> golden 2-plane
P = sp.Matrix.hstack(*(Lp + Lg))
diag = [smith_normal_form(P, domain=sp.ZZ)[i, i] for i in range(4)]
print("    det P =", P.det(), "  SNF diag =", diag)
check("glue order |det P| = 4", abs(P.det()) == 4)
check("glue group = (Z/2)^2 (SNF 1,1,2,2)",
      sorted(abs(d) for d in diag if abs(d) != 1) == [2, 2])
# representative-specific: the BLOCK-DIAGONAL matrix with the same charpoly has
# TRIVIAL glue (its invariant planes are the coordinate planes) -> the (Z/2)^2 is
# a GL(4,Z)-class invariant of M_g, NOT forced by the spectral type.
Lp0 = primitive_int_basis(Bdiag**2 - 3*Bdiag + sp.eye(4))
Lg0 = primitive_int_basis(Bdiag**2 - Bdiag + sp.eye(4))
P0 = sp.Matrix.hstack(*(Lp0 + Lg0))
check("block-diagonal form has TRIVIAL glue (index 1) -> glue is class-specific",
      abs(P0.det()) == 1)

# ------------------------------------------- invariant form, signature (1,3)
hr("invariant symmetric form: signature (1,3), disc -15")
g = sp.symbols('g0:16')
G = sp.Matrix(4, 4, lambda i, j: g[4*i + j])
cons = [G[i, j] - G[j, i] for i in range(4) for j in range(i+1, 4)]
cons += list(Mg.T * G * Mg - G)
sol = sp.solve(cons, list(g), dict=True)[0]
free = sorted({str(s) for v in sol.values() for s in v.free_symbols}, key=str)
import itertools
formG = None
for vals in itertools.product([1, -1, 2, -2, 3, 0], repeat=min(len(free), 3)):
    Gc = G.subs(sol).subs({sp.Symbol(s): v for s, v in zip(free, vals)})
    Gc = sp.Matrix(Gc.subs({r: 1 for r in Gc.free_symbols}))
    if Gc == Gc.T and Gc.det() != 0:
        formG = Gc
        break
ev = formG.eigenvals()
pos = sum(m for e, m in ev.items() if e.is_real and e > 0)
neg = sum(m for e, m in ev.items() if e.is_real and e < 0)
print("    G =", formG.tolist())
print(f"    signature = ({pos},{neg})   det = {formG.det()}")
check("signature (1,3) [or (3,1)]", {pos, neg} == {1, 3})
ratio = sp.nsimplify(formG.det() / sp.Integer(-15))
check("discriminant (det mod squares) = -15",
      sp.sqrt(ratio).is_rational is True)

# --------------------------------------------------- B206 = Omega_4 bridge
hr("B206 = Omega_4: the canonical-object unification")
a, m = sp.symbols('a m')
chi_omega = x**4 - a*x**3 + (2*a - 2*m - 4)*x**2 - a*x + 1   # Omega reciprocal charpoly
am = sp.solve([sp.Eq(a, 4), sp.Eq(2*a - 2*m - 4, 5)], [a, m], dict=True)[0]
print("    Omega charpoly = M_g charpoly at:", am)
check("Omega reaches it at a=4 (m = -1/2, half-integer)",
      am[a] == 4 and am[m] == sp.Rational(-1, 2))
print("    => bridge is the SHARED canonical object (Q-conjugacy class + signature),")
print("       NOT an integer Omega lattice point. M_g nonderogatory => any matrix")
print("       with this charpoly is Q-conjugate to M_g.")

hr("SUMMARY")
print("  ALL CHECKS PASS" if ok_all else "  *** SOME CHECKS FAILED ***")
import sys
sys.exit(0 if ok_all else 1)
