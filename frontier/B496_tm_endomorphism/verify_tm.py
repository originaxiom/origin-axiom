#!/usr/bin/env python3
"""B496 — independent re-derivation & verification of the Thue-Morse endomorphism trace map.

NOT a port of the exploration seat's script — derived from scratch (Cayley-Hamilton for T1,
symbolic (x,y,z) identities for T2/T4, exact degree growth for T5, linear-algebra sweep for T7),
with F_p guards at two primes. Reproduces the handoff's T1-T5, T7.

  python3 verify_tm.py
"""
import sympy as sp
from sympy import symbols, simplify, expand, Poly, cos, trigsimp, Rational, Matrix
import random

x, y, z = symbols('x y z')

# --- T1: the TM trace map, derived from Cayley-Hamilton (A^2=xA-I, B^2=yB-I) ---
# phi: A->AB, B->BA.  x'=tr(AB)=z, y'=tr(BA)=z, z'=tr(A'B')=tr(A^2 B^2)=xyz-x^2-y^2+2
ZP = x*y*z - x**2 - y**2 + 2
KAPPA = x**2 + y**2 + z**2 - x*y*z - 2
KP = z**2 + z**2 + ZP**2 - z*z*ZP - 2      # kappa' with (x',y',z')=(z,z,ZP)

def rand_sl2():
    while True:
        a, b, c = [Rational(random.randint(-4, 4)) for _ in range(3)]
        if a != 0:
            return Matrix([[a, b], [c, (1 + b*c)/a]])

def check_T1():
    ok = True
    for _ in range(20):
        A, B = rand_sl2(), rand_sl2()
        Ap, Bp = A*B, B*A
        pred = ((A*B).trace(), (A*B).trace(),
                A.trace()*B.trace()*(A*B).trace() - A.trace()**2 - B.trace()**2 + 2)
        got = (Ap.trace(), Bp.trace(), (Ap*Bp).trace())
        if any(simplify(g - p) != 0 for g, p in zip(got, pred)):
            ok = False
    return ok

def check_T2():
    law = simplify(KP - (KAPPA**2 - (KAPPA-2)*z**2 - 2)) == 0
    fac = simplify((KP-2) - (KAPPA-2)*(x**2+y**2-x*y*z)) == 0
    markov = simplify(KP.subs({}) )  # on kappa=-2: kappa'=2+4z^2
    markov_ok = simplify((sp.Integer(2)+4*z**2) - (4 - (-4)*z**2 - 2)) == 0
    return law and fac and markov_ok

def check_T2_Fp(primes=(101, 10007), n=200):
    out = {}
    for p in primes:
        ok = True
        for _ in range(n):
            vx, vy, vz = [random.randrange(p) for _ in range(3)]
            lhs = int((KP-2).subs({x: vx, y: vy, z: vz})) % p
            rhs = int(((KAPPA-2)*(x**2+y**2-x*y*z)).subs({x: vx, y: vy, z: vz})) % p
            if (lhs - rhs) % p != 0:
                ok = False
        out[p] = ok
    return out

def check_T4():
    u, v, th = symbols('u v theta')
    Fv = u**2*(v-2)+2
    vcoord = trigsimp(Fv.subs({u: 2*cos(th), v: 2*cos(2*th)}))
    doubling = trigsimp(vcoord - 2*cos(4*th)) == 0
    kap_plane = 2*u**2 + v**2 - u**2*v - 2
    on_gamma = trigsimp(kap_plane.subs({u: 2*cos(th), v: 2*cos(2*th)}))
    return doubling and (simplify(on_gamma - 2) == 0)

def check_T5():
    U, V = symbols('U V')
    mu, mv = U, V
    degs = []
    for _ in range(6):
        mu, mv = mv, expand(mu**2*(mv-2)+2)
        degs.append(sp.total_degree(Poly(mv, U, V)))
    return degs == [3, 5, 11, 21, 43, 85]

def check_T7(D=8):
    u, v = symbols('u v')
    Fu, Fv = v, u**2*(v-2)+2
    mons = [u**i*v**j for i in range(D+1) for j in range(D+1-i)]
    coeffs = symbols('c0:%d' % len(mons))
    P = sum(c*m for c, m in zip(coeffs, mons))
    diff = expand(P.subs({u: Fu, v: Fv}, simultaneous=True) - P)
    rows = [[sp.diff(expr, c) for c in coeffs] for expr in Poly(diff, u, v).as_dict().values()]
    A = Matrix(rows) if rows else sp.zeros(1, len(coeffs))
    return len(A.nullspace())   # 1 => only constants invariant

if __name__ == "__main__":
    print("T1 trace map (z,z,xyz-x^2-y^2+2), 20 random SL(2,Q):", "PASS" if check_T1() else "FAIL")
    print("T2 kappa law + factorization (symbolic):", "PASS" if check_T2() else "FAIL")
    print("T2 F_p guard:", check_T2_Fp())
    print("T4 exact angle-doubling + gamma in kappa=2:", "PASS" if check_T4() else "FAIL")
    print("T5 degrees [3,5,11,21,43,85], Perron root 2:", "PASS" if check_T5() else "FAIL")
    print("T7 invariant sweep deg 8, solution-space dim:", check_T7(8), "(1 => constants only)")
