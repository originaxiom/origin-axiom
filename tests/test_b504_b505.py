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


def test_b507_beta_gates_and_zero():
    import numpy as np
    rng = np.random.default_rng(41)
    N = 400_000
    q = rng.normal(size=(N, 4)); q /= np.linalg.norm(q, axis=1, keepdims=True)
    q2 = rng.normal(size=(N, 4)); q2 /= np.linalg.norm(q2, axis=1, keepdims=True)
    x = 2*q[:, 0]; y = 2*q2[:, 0]
    z = 2*(q[:, 0]*q2[:, 0] - np.sum(q[:, 1:]*q2[:, 1:], axis=1))
    kap = x*x + y*y + z*z - x*y*z - 2
    gM = np.log(np.maximum(np.abs(x*x + y*y - x*y*z), 1e-300))
    gD = np.log(np.maximum(np.abs(x*x*y*y), 1e-300))
    assert abs(gM.mean()) < 0.01 and abs(gD.mean() + 2) < 0.01      # proved gates
    lo = gM[(kap > -0.3) & (kap < -0.1)].mean()
    hi = gM[(kap > 0.1) & (kap < 0.3)].mean()
    assert lo < 0 < hi                                               # the zero sits at ~0
