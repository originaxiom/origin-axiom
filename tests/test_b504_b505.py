"""Locks for the two verified-on-arrival claims (B504 delta_M=2; B505 kappa-2=4lambda^2)."""
import sympy as sp
import mpmath as mp


def test_b505_kappa_is_squared_coupling():
    E, lam = sp.symbols('E lambda')
    TA = sp.Matrix([[E - lam, -1], [1, 0]]); TB = sp.Matrix([[E + lam, -1], [1, 0]])
    x, y, z = TA.trace(), TB.trace(), (TB*TA).trace()
    assert sp.simplify(x**2 + y**2 + z**2 - x*y*z - 2 - 2 - 4*lam**2) == 0


def test_b504_delta_M_is_two():
    mp.mp.dps = 25
    zz = mp.mpc(0.5, mp.sqrt(3)/2)
    A = mp.matrix([[1, -1], [1, 0]]); B = mp.matrix([[0, zz], [-1/zz, 1]])
    AB, BA = A*B, B*A
    rows = []
    for (Mat, N) in [(A, AB), (B, BA)]:
        for i in range(2):
            for j in range(2):
                r = [mp.mpc(0)]*4
                for k in range(2):
                    r[2*i + k] += Mat[k, j]
                    r[2*k + j] -= N[i, k]
                rows.append(r)
    U, S, V = mp.svd(mp.matrix(rows))
    t = [V[3, k].conjugate() for k in range(4)]
    T = mp.matrix([[t[0], t[1]], [t[2], t[3]]])
    Tn = T/mp.sqrt(T[0, 0]*T[1, 1] - T[0, 1]*T[1, 0])
    assert abs((Tn[0, 0] + Tn[1, 1])**2 - 2) < mp.mpf('1e-18')
