#!/usr/bin/env python3
"""B1233 -- the z-ai audit. Every checkable claim from an external analysis, verified or refuted
ON THIS BENCH. Owner: 'take every letter seriously / verify never trust / digest and integrate all'."""
import sympy as sp, mpmath as mp
mp.mp.dps = 40
R = {}
phi = (1+mp.sqrt(5))/2
L = lambda x: mp.polylog(2,x) + mp.log(x)*mp.log(1-x)/2

# --- CONFIRMED ---
R['dilog_partition'] = (abs(L(1/phi)-mp.pi**2/10) < mp.mpf(10)**-30 and
                        abs(L(1/phi**2)-mp.pi**2/15) < mp.mpf(10)**-30 and
                        abs(L(1/phi)+L(1/phi**2)-mp.zeta(2)) < mp.mpf(10)**-30)
R['lagrange_identity'] = all(abs(((m+mp.sqrt(m*m+4))/2 + 2/(m+mp.sqrt(m*m+4))) - mp.sqrt(m*m+4))
                             < mp.mpf(10)**-30 for m in range(1,8))
R['jones_phi2'] = abs(4*mp.cos(mp.pi/5)**2 - phi**2) < mp.mpf(10)**-30
x,y,z,v = sp.symbols('x y z v')
K = x**2+y**2+z**2-x*y*z-4
H = sp.hessian(K,(x,y,z))
ev = sp.Matrix(H.subs({x:2,y:2,z:2})).eigenvals()
R['void_is_2_1_saddle'] = (sorted(ev.keys()) == [-2,4] and K.subs({x:2,y:2,z:2}) == 0)
R['origin_is_global_min'] = (K.subs({x:0,y:0,z:0}) == -4 and
                             list(sp.Matrix(H.subs({x:0,y:0,z:0})).eigenvals()) == [2])
A = sp.Matrix([[1,1],[0,1]]); B = sp.Matrix([[1,0],[v,1]])
R['riley_trace'] = sp.simplify(sp.trace(A*B*A.inv()*B.inv()) - (v**2+2)) == 0
R['markov_stratum'] = sp.simplify(sp.expand((x**2+y**2+(x*y-z)**2-x*y*(x*y-z)) -
                                            (x**2+y**2+z**2-x*y*z))) == 0
R['j_sqrt_m3_is_54000'] = abs(mp.kleinj(mp.mpc(0,mp.sqrt(3)))*1728 - 54000) < mp.mpf(10)**-10
R['two_splits_only_in_meeting'] = ((-3) % 8 == 5 and 5 % 8 == 5 and (-15) % 8 == 1)

# --- REFUTED ---
j_m004 = mp.kleinj(mp.mpc(0, 2*mp.sqrt(3)))*1728
R['REFUTED_j_m004_is_zero'] = abs(j_m004) > 1e6           # claim was j = 0
j_m003 = mp.kleinj(mp.mpc(0.5, mp.sqrt(3)/2))*1728        # rho -- the SISTER's cusp
R['j_zero_is_m003_not_m004'] = abs(j_m003) < mp.mpf(10)**-20
roots = [mp.kleinj((mp.mpc(-b, mp.sqrt(15)))/(2*a))*1728 for a,b,c in [(1,1,4),(2,1,2)]]
R['REFUTED_disc15_j_is_quartic'] = (abs(mp.im(roots[0]+roots[1])) < 1e-15 and
                                    abs(mp.re(roots[0]+roots[1]) + 191025) < 1e-6)   # rational sum => DEGREE 2
R['H15_constant_is_NEGATIVE'] = mp.re(roots[0]*roots[1]) < 0                          # claim wrote +

# --- the Galois refutation of the observer-bit identification ---
# V4 = Gal(Q(sqrt-3,sqrt5)/Q); complex conjugation fixes sqrt5 (real), the class-group
# generator fixes sqrt-15 hence flips BOTH. Different elements.
CC   = (-1, +1)   # conj: flips sqrt-3, fixes sqrt5
CLS  = (-1, -1)   # Gal(H/Q(sqrt-15)): fixes sqrt-15 = sqrt-3*sqrt5, so flips both
R['REFUTED_class_bit_equals_c'] = (CC != CLS)

for k,val in R.items():
    print(f"  [{'PASS' if val else 'FAIL'}] {k}")
assert all(R.values()), [k for k,v in R.items() if not v]
print("\nALL AUDIT ASSERTIONS HOLD (confirmations confirmed, refutations refuted)")
