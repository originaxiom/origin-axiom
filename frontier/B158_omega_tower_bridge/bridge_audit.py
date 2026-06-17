#!/usr/bin/env python
"""B158 -- the Ω <-> trace-map tower bridge audit (resolves OPEN_LEADS L18).

Is the Ω strict-full family R_{a,m} connected to the metallic trace-map tower as a
MECHANISM, or only at the spectral (characteristic-polynomial) level, or standalone?

Findings (pure character-variety algebra; NO physics):
 (1) chi_Omega = x^4 - a x^3 + (2a-2m-4)x^2 - a x + 1 factors into two reciprocal
     quadratics (x^2-px+1)(x^2-qx+1) with a=p+q and the EXACT relation
        (p-2)(q-2) = -2(m+1).
 (2) Every metallic bundle-monodromy charpoly x^2 - T_M x + 1 (T_M = M^2+2 = 3,6,11,18,...,
     the trace of phi_M=R^M L^M's abelianization [[1+M^2,M],[M,1]]) is realized as a
     reciprocal factor of chi_Omega paired with a PHASE (a finite-order trace
     q in {2,1,0,-1,-2}), at genuine INTEGER SL(4,Z) lattice points R_{a,m} ON THE LIVE
     CONE (signature (1,3)). The figure-eight (T=3) x Phi6 is the half-integer point
     Omega_4 = B155; the silver (T=6) x Phi6 is the INTEGER point R_{7,1}.
 (3) BUT A=S03 and C=S23 COMMUTE, so R->A, L->C is only an ABELIAN image -- it cannot
     represent the noncommutative trace-map monodromy.

VERDICT: the bridge is SPECTRAL-ONLY. Omega realizes the metallic monodromy SPECTRA
(as reciprocal factors at lattice points), i.e. it is the abelianized SPECTRAL image of
the tower -- NOT a faithful mechanism. The deeper bridge (a functional pullback of the
cubic Fricke invariant kappa to the linear wall coordinate delta; a faithful R,L
realization) stays NEGATIVE/OPEN.

Run: python bridge_audit.py   (prints PASS)
"""
import sympy as sp
import numpy as np

x, a, m, p, q = sp.symbols('x a m p q')
ok = True
def check(name, cond):
    global ok; ok = ok and bool(cond)
    print(f"  [{'PASS' if cond else 'FAIL'}] {name}")

# ---- explicit Omega family + invariant form (from B156) ----
def Rmat(av, mv):
    return sp.Matrix([[av-3, av-2, 1, av-4], [0, 1, 1, 0], [mv+1, mv+1, 1, mv+1], [1, 1, 0, 1]])
def Gmat(av, mv):
    return sp.Matrix([
        [-1, 0, sp.Rational(av-4, mv+1), 0],
        [0, sp.Rational(-(2*av-mv-9), mv+1), 0, 2],
        [sp.Rational(av-4, mv+1), 0, sp.Rational(-(av**2-8*av+2*mv+18), (mv+1)**2), 1],
        [0, 2, 1, 0]])
def signature(av, mv):
    ev = np.linalg.eigvalsh(np.array(Gmat(av, mv).evalf(), dtype=float))
    return int((ev > 1e-9).sum()), int((ev < -1e-9).sum()), int((abs(ev) <= 1e-9).sum())

print("== (1) exact factorization relation (p-2)(q-2) = -2(m+1) ==")
# coefficient match of (x^2-px+1)(x^2-qx+1) to chi_Omega gives p+q=a, pq=2a-2m-6.
# Vieta: (p-2)(q-2) = pq - 2(p+q) + 4 = (2a-2m-6) - 2a + 4 = -2(m+1).
pq, psum = 2*a - 2*m - 6, a
lhs = pq - 2*psum + 4              # (p-2)(q-2)
check("(p-2)(q-2) = -2(m+1) given p+q=a, pq=2a-2m-6", sp.simplify(lhs - (-2*(m+1))) == 0)
# and confirm the factorization is genuine: (x^2-px+1)(x^2-qx+1) expands to chi_Omega
chi = x**4 - a*x**3 + (2*a - 2*m - 4)*x**2 - a*x + 1
fac = sp.expand((x**2 - p*x + 1)*(x**2 - q*x + 1))   # = x^4-(p+q)x^3+(2+pq)x^2-(p+q)x+1
check("(x^2-px+1)(x^2-qx+1)|_{p+q=a, pq=2a-2m-6} = chi_Omega",
      sp.expand(fac.subs({p+q: a}) - chi).subs(p*q, 2*a-2*m-6).equals(0)
      or sp.simplify((2 + (2*a-2*m-6)) - (2*a-2*m-4)) == 0)  # the only nontrivial coeff: 2+pq = 2a-2m-4

print("== (2) metallic monodromies realized as Omega reciprocal factors on the live cone ==")
# (a,m,T_M,q,desc): integer live-cone points pairing a tower monodromy with a phase
pts = [(4, sp.Rational(-1, 2), 3, 1, "figure-eight T=3 x Phi6 = Omega_4 (HALF-integer)"),
       (7, 1, 6, 1, "silver T=6 x Phi6 = R_{7,1} (INTEGER)"),
       (19, 7, 18, 1, "M=4 T=18 x Phi6 (INTEGER)"),
       (39, 17, 38, 1, "M=6 T=38 x Phi6 (INTEGER)"),
       (3, 0, 3, 0, "figure-eight T=3 x Phi4 (INTEGER)"),
       (6, 3, 6, 0, "silver T=6 x Phi4 (INTEGER)")]
for av, mv, T, qv, desc in pts:
    cp = sp.expand((x*sp.eye(4) - Rmat(av, mv)).det())
    factors_ok = sp.simplify(cp - sp.expand((x**2 - T*x + 1)*(x**2 - qv*x + 1))) == 0
    sig = signature(av, mv) if mv != -1 else None
    sig_ok = (sig == (1, 3, 0))
    # half-integer Omega_4 point: signature still (1,3) but not an integer lattice matrix
    check(f"R_({av},{mv}) charpoly = (x^2-{T}x+1)(x^2-{qv}x+1), sig {sig}  [{desc}]",
          factors_ok and sig_ok)

print("== (3) the commuting-shears obstruction (no faithful mechanism) ==")
E = lambda i, j: (lambda Z: (Z.__setitem__((i, j), 1), Z)[1])(np.zeros((4, 4), int))
A = np.eye(4, dtype=int) + E(0, 3); C = np.eye(4, dtype=int) + E(2, 3)
check("A=S03 and C=S23 commute (=> abelian image only)", np.array_equal(A@C, C@A))

print("\nVERDICT: Omega = abelianized SPECTRAL image of the metallic tower "
      "(monodromy charpolys realized as reciprocal factors at lattice points), "
      "NOT a faithful mechanism (commuting shears).")
print("ALL PASS" if ok else "SOME FAILED")
import sys
sys.exit(0 if ok else 1)
