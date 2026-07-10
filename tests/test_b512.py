"""B512 locks — the six-computation pass (verified items)."""
import mpmath as mp


def _tr2(A, B, Aimg, Bimg):
    rows = []
    for (Mat, N) in [(A, Aimg), (B, Bimg)]:
        for i in range(2):
            for j in range(2):
                r = [mp.mpc(0)]*4
                for k in range(2):
                    r[2*i + k] += Mat[k, j]; r[2*k + j] -= N[i, k]
                rows.append(r)
    U, S, V = mp.svd(mp.matrix(rows))
    t = [V[3, k].conjugate() for k in range(4)]
    T = mp.matrix([[t[0], t[1]], [t[2], t[3]]])
    Tn = T/mp.sqrt(T[0, 0]*T[1, 1] - T[0, 1]*T[1, 0])
    return (Tn[0, 0] + Tn[1, 1])**2


def test_C_mckay_golden_specific():
    mp.mp.dps = 25
    A = mp.matrix([[0, -1], [1, 0]]); B = mp.matrix([[0, 1j], [1j, 0]])
    golden = _tr2(A, B, A*B, A)            # phi: a->ab, b->a
    silver = _tr2(A, B, A*A*B, A)          # phi: a->a^2 b, b->a
    assert abs(golden - 1) < 1e-18         # order-6 -> 2T -> E6
    assert abs(silver - 2) < 1e-18         # order-8 -> 2-group, NOT 2T


def test_A_delta_square_at_eisenstein():
    mp.mp.dps = 25
    d = lambda s: (s*s + s - 1)/(s - 1)
    assert abs(d(mp.mpc(1.5, mp.sqrt(3)/2)) - 4) < 1e-18   # = 2^2, a square
