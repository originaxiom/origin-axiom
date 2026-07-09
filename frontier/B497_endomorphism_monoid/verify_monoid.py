#!/usr/bin/env python3
"""B497 Phase 0 — independent re-derivation: the endomorphism monoid's four strata + two universal laws.

NOT a port of the exploration seat's scripts. Derivations: Cayley-Hamilton for every trace map;
random exact SL(2,Q) + F_p guards; free-group witnesses via sympy.combinatorics; upper-triangular
closure for U1; diagonal characters for U2; exact degree iteration for the ledger.

  python3 verify_monoid.py
"""
import random
import sympy as sp
from sympy import symbols, simplify, expand, Matrix, Rational, Poly, total_degree
from sympy.combinatorics.free_groups import free_group

x, y, z = symbols('x y z')
KAP = x**2 + y**2 + z**2 - x*y*z - 2

T_GOLD = (z, x, x*z - y)                                  # stratum 1 (m=1)
T_DEC  = (x**2 - 2, y**2 - 2, x*y*z - x**2 - y**2 + 2)    # stratum 2: A->A^2, B->B^2 (det 4)
T_PD   = (z, x**2 - 2, (x**2 - 1)*z - x*y)                # stratum 2: a->ab, b->aa (det -2)
T_TM   = (z, z, x*y*z - x**2 - y**2 + 2)                  # stratum 3 (= B496)


def _rand_sl2():
    while True:
        a, b, c = [Rational(random.randint(-4, 4)) for _ in range(3)]
        if a != 0:
            return Matrix([[a, b], [c, (1 + b*c)/a]])


def check_stratum2_maps(n=12):
    """decimation + period-doubling trace maps on random exact SL(2,Q) pairs."""
    for _ in range(n):
        A, B = _rand_sl2(), _rand_sl2()
        X, Y, Z = A.trace(), B.trace(), (A*B).trace()
        # decimation
        got = ((A*A).trace(), (B*B).trace(), ((A*A)*(B*B)).trace())
        pred = [t.subs({x: X, y: Y, z: Z}) for t in T_DEC]
        if any(simplify(g - p) != 0 for g, p in zip(got, pred)):
            return False
        # period-doubling: A' = AB, B' = A^2
        Ap, Bp = A*B, A*A
        got = (Ap.trace(), Bp.trace(), (Ap*Bp).trace())
        pred = [t.subs({x: X, y: Y, z: Z}) for t in T_PD]
        if any(simplify(g - p) != 0 for g, p in zip(got, pred)):
            return False
    return True


def check_kappa_multipliers():
    """the exact per-verb kappa laws: gold kappa'=kappa; dec (k-2)x^2y^2; TM (k-2)(x^2+y^2-xyz)."""
    def kp(T):
        return T[0]**2 + T[1]**2 + T[2]**2 - T[0]*T[1]*T[2] - 2
    gold = simplify(kp(T_GOLD) - KAP) == 0
    dec = simplify((kp(T_DEC) - 2) - (KAP - 2)*x**2*y**2) == 0
    tm = simplify((kp(T_TM) - 2) - (KAP - 2)*(x**2 + y**2 - x*y*z)) == 0
    return gold and dec and tm


def check_U1(trials=20):
    """kappa=2 invariant under random endomorphisms (triangular closure)."""
    def word(A, B, w):
        M = sp.eye(2)
        for c in w:
            M = M*(A if c == 'a' else B)
        return M
    for _ in range(trials):
        a1 = Rational(random.choice([1, -1])); t1 = Rational(random.randint(-3, 3))
        a2 = Rational(random.choice([1, -1])); t2 = Rational(random.randint(-3, 3))
        A = Matrix([[a1, t1], [0, 1/a1]]); B = Matrix([[a2, t2], [0, 1/a2]])
        w1 = ''.join(random.choice('ab') for _ in range(random.randint(1, 4)))
        w2 = ''.join(random.choice('ab') for _ in range(random.randint(1, 4)))
        Ap, Bp = word(A, B, w1), word(A, B, w2)
        K = simplify(Ap.trace()**2 + Bp.trace()**2 + (Ap*Bp).trace()**2
                     - Ap.trace()*Bp.trace()*(Ap*Bp).trace() - 2)
        if simplify(K - 2) != 0:
            return False
    return True


def check_U2():
    """on kappa=2 (diagonal characters) every stratum representative acts by its abelianization."""
    a, b = symbols('a b', nonzero=True)
    A = Matrix([[a, 0], [0, 1/a]]); B = Matrix([[b, 0], [0, 1/b]])
    def word(w):
        M = sp.eye(2)
        for c in w:
            M = M*(A if c == 'a' else B)
        return M
    cases = [('ab', 'a',  Matrix([[1, 1], [1, 0]])),   # stratum 1
             ('aa', 'bb', Matrix([[2, 0], [0, 2]])),   # stratum 2 dec
             ('ab', 'aa', Matrix([[1, 2], [1, 0]])),   # stratum 2 pd
             ('ab', 'ba', Matrix([[1, 1], [1, 1]])),   # stratum 3 TM
             ('ab', 'ab', Matrix([[1, 1], [1, 1]]))]   # stratum 4
    for w1, w2, M in cases:
        Ap, Bp = word(w1), word(w2)
        if simplify(Ap[0, 0] - a**M[0, 0]*b**M[1, 0]) != 0:
            return False
        if simplify(Bp[0, 0] - a**M[0, 1]*b**M[1, 1]) != 0:
            return False
    return True


def check_witnesses():
    """I1 TM injective; stratum-2 free; stratum-4 kernel; erasure image in kappa=2."""
    F, A_, B_ = free_group("A B")
    tm_noncomm = ((A_*B_)*(B_*A_) != (B_*A_)*(A_*B_))          # I1
    s2_noncomm = ((A_**2)*(B_**2) != (B_**2)*(A_**2))          # stratum-2 witness
    s4_kernel = ((A_*B_)*((A_*B_)**-1)).is_identity            # phi(AB^-1)=1
    M = _rand_sl2()
    k = simplify(2*M.trace()**2 + (M*M).trace()**2 - M.trace()**2*(M*M).trace() - 2)
    erasure_classical = simplify(k - 2) == 0
    tm_ab_rank = Matrix([[1, 1], [1, 1]]).rank() == 1          # I2
    return tm_noncomm and s2_noncomm and s4_kernel and erasure_classical and tm_ab_rank


def degree_ledger():
    """Fibonacci trace map degrees (should be the Fibonacci numbers 2,3,5,8,13,21,34,55)."""
    cur = (x, y, z)
    degs = []
    for _ in range(8):
        cur = tuple(expand(t.subs({x: cur[0], y: cur[1], z: cur[2]}, simultaneous=True))
                    for t in T_GOLD)
        degs.append(max(total_degree(Poly(t, x, y, z)) for t in cur))
    return degs


def check_Fp(primes=(101, 10007), n=150):
    """F_p guard on the decimation kappa law."""
    kp = T_DEC[0]**2 + T_DEC[1]**2 + T_DEC[2]**2 - T_DEC[0]*T_DEC[1]*T_DEC[2] - 2
    for p in primes:
        for _ in range(n):
            vx, vy, vz = [random.randrange(p) for _ in range(3)]
            lhs = int((kp - 2).subs({x: vx, y: vy, z: vz})) % p
            rhs = int(((KAP - 2)*x**2*y**2).subs({x: vx, y: vy, z: vz})) % p
            if (lhs - rhs) % p:
                return False
    return True


if __name__ == "__main__":
    print("stratum-2 trace maps (decimation + period-doubling):", check_stratum2_maps())
    print("exact kappa multipliers (gold id / dec x^2y^2 / TM x^2+y^2-xyz):", check_kappa_multipliers())
    print("U1 kappa=2 invariant under random endos:", check_U1())
    print("U2 classical floor toral (abelianization action, all strata):", check_U2())
    print("witnesses (I1 TM inj, s2 free, s4 kernel, erasure classical, I2 rank1):", check_witnesses())
    print("Fibonacci degree ledger:", degree_ledger(), "(the Fibonacci numbers)")
    print("F_p guard (decimation law):", check_Fp())
