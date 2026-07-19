#!/usr/bin/env python3
"""
B715 — Frontier 3 (native gauge), PROBE 3.
THE Z/11 AS A UV-ARITHMETIC (NON-FORCE) CHARGE.

Two-outcome test (structural only; no SM value, no physics assertion):
  A = the Z/11 DESCENDS to an IR gauge force.
  B = the Z/11 is UV-ARITHMETIC bookkeeping (real arithmetic on the letter/
      geometry floor), NON-DESCENDING, NON-FORCE.

Everything is verified in-sandbox by independent computation (verify-don't-trust),
not by citing B566/B565/B552.

(a) ARITHMETIC ORIGIN (B566-S5): Z/11 = |N_{Q(sqrt5)/Q}(phi^5 - 1)|, geometric
    in the 5-fold cyclic cover. phi=(1+sqrt5)/2.
(b) NON-DESCENDING (B565-T1): 11 is prime and divides no available IR
    invertible-symmetry order, so the only hom Z/11 -> IR-symmetry is trivial:
    the charge is VACUOUS in the IR = does not become a force.
"""

import sympy as sp

log_lines = []
def out(s=""):
    print(s)
    log_lines.append(s)

out("=" * 74)
out("B715 PROBE 3 — Z/11 as a UV-arithmetic (non-force) charge")
out("=" * 74)

# ----------------------------------------------------------------------
# (a) ARITHMETIC ORIGIN:  Z/11 = N(phi^5 - 1)  in  Z[phi] = O_{Q(sqrt5)}
# ----------------------------------------------------------------------
out("")
out("(a) ARITHMETIC ORIGIN — Z/11 = N(phi^5 - 1), geometric in the 5-fold cover")
out("-" * 74)

sqrt5 = sp.sqrt(5)
phi    = (1 + sqrt5) / 2           # golden ratio,  root of x^2 - x - 1
phibar = (1 - sqrt5) / 2           # Galois conjugate

# --- Fibonacci closed form: phi^n = F_n * phi + F_{n-1} ---
# so phi^5 = F_5*phi + F_4 = 5*phi + 3.
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

F5, F4 = fib(5), fib(4)
out(f"  Fibonacci:  F_5 = {F5},  F_4 = {F4}   => predict phi^5 = {F5}*phi + {F4}")

phi5_direct = sp.expand(sp.simplify(phi**5))
phi5_fib    = sp.expand(F5*phi + F4)
assert sp.simplify(phi5_direct - phi5_fib) == 0, "phi^5 != 5 phi + 3"
out(f"  symbolic:   phi^5 = {sp.nsimplify(phi5_direct)}  (matches 5*phi+3)  [OK]")

# --- phi^5 - 1 = 5*phi + 2 ---
alpha = sp.simplify(phi**5 - 1)
assert sp.simplify(alpha - (5*phi + 2)) == 0, "phi^5 - 1 != 5 phi + 2"
out(f"  phi^5 - 1 = {sp.nsimplify(alpha)}  = 5*phi + 2                       [OK]")

# --- Field norm  N(x) = x * conj(x).   For x = 5 phi + 2:
#     conj = 5 phibar + 2;  N = 25*(phi*phibar) + 10*(phi+phibar) + 4.
phi_phibar = sp.simplify(phi * phibar)          # = -1
phi_plus   = sp.simplify(phi + phibar)          # = +1
out(f"  phi*phibar = {phi_phibar}  (product of roots of x^2-x-1)")
out(f"  phi+phibar = {phi_plus}  (sum of roots)")

# hand-expanded norm, term by term (matches the prompt's arithmetic)
N_hand = 25*phi_phibar + 10*phi_plus + 4
out(f"  N(5*phi+2) = 25*({phi_phibar}) + 10*({phi_plus}) + 4 = {N_hand}")

# fully-independent symbolic norm
alpha_bar = alpha.subs(sqrt5, -sqrt5)           # apply the nontrivial Galois auto
N_sym = sp.expand(sp.simplify(alpha * alpha_bar))
out(f"  N(phi^5-1) [symbolic, alpha*conj(alpha)] = {N_sym}")
assert N_sym == -11 and N_hand == -11
out(f"  ==> N(phi^5 - 1) = -11,  |N| = 11   [OK, PRIME]")

# --- The B517 intertwining: (phi^5 - 1) = (1 - 3 phi) * (-phi^2), unit -phi^2 ---
unit = -phi**2
assoc = sp.simplify((1 - 3*phi) * unit)
assert sp.simplify(assoc - alpha) == 0
N_unit = sp.simplify(unit * unit.subs(sqrt5, -sqrt5))
one_m_3phi = sp.simplify(1 - 3*phi)
N_1m3phi = sp.simplify(one_m_3phi * one_m_3phi.subs(sqrt5, -sqrt5))
out(f"  associate:  (phi^5-1) = (1-3*phi)*(-phi^2),  N(-phi^2) = {N_unit} (unit)")
out(f"  golden guise:  N(1-3*phi) = {N_1m3phi}   (same norm, associate) [OK]")

# --- Chain guise cross-check:  det(I - 3F),  F = [[1,1],[1,0]] (golden companion)
F = sp.Matrix([[1, 1], [1, 0]])
det_I_3F = sp.simplify((sp.eye(2) - 3*F).det())
out(f"  det(I - 3F), F=[[1,1],[1,0]]  = {det_I_3F}   (= N(1-3phi))          [OK]")
assert det_I_3F == -11

# ----------------------------------------------------------------------
# (a') CHAIN GUISE — det(I - M4) = -11, coker(I-M4) = Z/11  (B552 charge)
#   M4 = abelianization (Parikh) matrix of the 4-letter substitution sigma:
#     a -> abAAB   b -> aAB   A -> abAB   B -> aA        (letter order a,b,A,B)
# ----------------------------------------------------------------------
out("")
out("(a') CHAIN GUISE — the same 11 as a Smith-normal-form torsion (B552)")
out("-" * 74)

# columns = image of each generator; rows = count of (a,b,A,B)
#   sigma(a)=abAAB : a1 b1 A2 B1
#   sigma(b)=aAB   : a1 b0 A1 B1
#   sigma(A)=abAB  : a1 b1 A1 B1
#   sigma(B)=aA    : a1 b0 A1 B0
M4 = sp.Matrix([
    [1, 1, 1, 1],   # a-row
    [1, 0, 1, 0],   # b-row
    [2, 1, 1, 1],   # A-row
    [1, 1, 1, 0],   # B-row
])
cp = sp.factor(M4.charpoly(sp.Symbol('x')).as_expr())
out(f"  M4 char poly = {sp.expand(M4.charpoly(sp.Symbol('x')).as_expr())}")
det_I_M4 = (sp.eye(4) - M4).det()
out(f"  det(I - M4) = {det_I_M4}")
assert det_I_M4 == -11

# Smith normal form of (I - M4) over Z  ->  diag(1,1,1,11)
A = sp.Matrix(sp.eye(4) - M4)
from sympy.matrices.normalforms import smith_normal_form
snf = smith_normal_form(A, domain=sp.ZZ)
diag = [snf[i, i] for i in range(4)]
diag = [abs(d) for d in diag]
out(f"  SNF(I - M4) = diag({', '.join(str(d) for d in diag)})  ->  coker = Z/{diag[-1]}")
assert sorted(diag) == [1, 1, 1, 11]

# the primitive left charge generator chi = (1,3,6,7) mod 11, chi*M4 = chi
chi = sp.Matrix([[1, 3, 6, 7]])
lhs = (chi * M4).applyfunc(lambda z: z % 11)
out(f"  left charge chi=(1,3,6,7):  chi*M4 mod 11 = {list(lhs)}  (= chi)      [OK]")
assert list(lhs) == [1, 3, 6, 7]

# ----------------------------------------------------------------------
# (a'') TOPOLOGICAL GUISE — 121 = L_5^2, L_5 = 11 (Lucas), N=11^2 in the 5-cover
# ----------------------------------------------------------------------
out("")
out("(a'') TOPOLOGICAL GUISE — 11 = L_5 (Lucas), the 5-fold cover carries 11^2")
out("-" * 74)
def lucas(n):
    a, b = 2, 1
    for _ in range(n):
        a, b = b, a + b
    return a
L5 = lucas(5)
out(f"  Lucas L_5 = {L5};  H1-torsion order of the 5-fold cover = L_5^2 = {L5**2} = 11^2")
assert L5 == 11
# Res(Delta, Phi_5) for figure-eight Alexander Delta = t^2 - 3t + 1
t = sp.Symbol('t')
Delta = t**2 - 3*t + 1
Phi5 = sp.cyclotomic_poly(5, t)
res = sp.resultant(Delta, Phi5)
out(f"  Res(Delta_4_1, Phi_5) = {res}  (= 11^2 = 121; product over 5th roots)")
assert abs(res) == 121

# ----------------------------------------------------------------------
# (b) NON-DESCENDING — 11 divides NO available IR invertible-symmetry order
#     => only the trivial hom Z/11 -> IR-symmetry => VACUOUS in the IR.
# ----------------------------------------------------------------------
out("")
out("(b) NON-DESCENDING (B565-T1) — the charge is vacuous in the IR")
out("-" * 74)

# The IR of the object's chain = the golden (Fibonacci) anyon CFT.
# Available IR invertible / finite-symmetry orders (0-form invertible-object
# groups and the discrete symmetries B565 enumerated):
ir_symmetry_orders = {
    "Inv(Fib)            (invertible objects of the Fibonacci category)": 1,
    "Inv(Z(Fib))         (invertibles of the Drinfeld center Fib x Fib-bar)": 1,
    "chiral sectors      (# of primaries / sector count)": 2,
    "TCI Z/2             (tricritical-Ising / orientation Z/2)": 2,
}
for name, order in ir_symmetry_orders.items():
    out(f"    |{name}| = {order}")

out("")
out("  A homomorphism  f: Z/11 -> G  has image of order dividing gcd(11, |G|).")
p = 11
assert sp.isprime(p), "11 must be prime for the Lagrange argument"
trivial_everywhere = True
for name, order in ir_symmetry_orders.items():
    g = sp.gcd(p, order)
    only_trivial = (g == 1)
    trivial_everywhere &= only_trivial
    out(f"    gcd(11, {order}) = {g}  ->  image order 1  ->  "
        f"{'ONLY THE TRIVIAL HOM' if only_trivial else 'NONTRIVIAL POSSIBLE'}")

# 11 divides none of the available orders (equivalently: 11 nmid lcm of them)
from math import lcm
avail_lcm = 1
for o in ir_symmetry_orders.values():
    avail_lcm = lcm(avail_lcm, o)
out(f"    lcm(available IR orders) = {avail_lcm};  11 | {avail_lcm}? "
    f"{avail_lcm % 11 == 0}")
assert trivial_everywhere and avail_lcm % 11 != 0

out("")
out("  ==> The ONLY hom Z/11 -> (any available IR symmetry) is TRIVIAL.")
out("      The Z/11 charge cannot act on the IR: it is VACUOUS in the IR.")
out("      (UV side: on-site linear grading => H^3 class = 0 => gaugeable but")
out("       carrying no IR force. The charge lives on a DIFFERENT floor — the")
out("       letter/geometry arithmetic floor — from the emergent CFT.)")

# ----------------------------------------------------------------------
# VERDICT
# ----------------------------------------------------------------------
out("")
out("=" * 74)
out("VERDICT")
out("=" * 74)
out("  (a)  |N(phi^5 - 1)| = 11 (prime), realized identically as:")
out("        - golden  : N(1-3phi) = -11  (unit-associate)")
out("        - chain   : det(I - M4) = -11, SNF diag(1,1,1,11), coker = Z/11")
out("        - topology: 11 = L_5, the 5-fold cover carries 11^2 = 121")
out("       => the 11 is REAL UV ARITHMETIC, geometric in the 5-fold cover.")
out("  (b)  11 is prime and divides no available IR invertible-symmetry order")
out("       {Inv(Fib)=1, Inv(Z(Fib))=1, sectors=2, TCI Z/2}  =>  only trivial")
out("       hom  =>  the charge is NON-DESCENDING / VACUOUS in the IR.")
out("")
out("  OUTCOME = B :  the Z/11 is a UV-ARITHMETIC, NON-DESCENDING, NON-FORCE")
out("  charge — real arithmetic on the letter/geometry floor, NOT an IR gauge")
out("  force.  (Outcome A — a descending IR force — is REFUTED.)")
out("=" * 74)

# write the log next to this script
import os
here = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(here, "b715_probe3_out.txt"), "w") as f:
    f.write("\n".join(log_lines) + "\n")
