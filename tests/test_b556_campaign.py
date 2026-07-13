"""Tower-probe campaign — charge-arithmetic locks (B556), all re-verified in-sandbox.

  P-F  : exact factorization of e_4, e_5; "one prime per rung" breaks at n=4;
         period-3 divisibility 11|e_n <=> n=1 mod 3 through n=7; no 5/7 factors.
  P-C  : magnitude-degenerate eigenvalue pairs = 2^n - 1 (all complex-conjugate);
         charpoly irreducible at every rung.
  P-B  : free energy f_n = log|e_n|/2^{n+1} diverges (f_{n+1}/f_n -> 3/2).
  FL2  : golden-norm doubling transfer D(G)=Res_t(t^2-2yt+y^2-y^3, G); e_n=N(g_n(phi)).
See frontier/B556_escalator_tower/FINDINGS.md.
"""
import math
import numpy as np
import sympy as sp

F = sp.Matrix([[1, 1], [1, 0]])


def _T(M):
    return M.row_join(M).col_join((M * M).row_join(M))


def _rung(n):
    M = F
    for _ in range(n):
        M = _T(M)
    return M


E = {0: -1, 1: -11, 2: -809, 3: -18845089,
     4: -228654672055316545291,
     5: -14551745085338356602787456737044854593029948485574326872937769}


# ---------- P-F ----------
def test_pf_factorization_and_one_prime_per_rung_breaks():
    assert sp.factorint(abs(E[4])) == {11: 2, 1459: 1, 597049: 1, 2169349081: 1}
    f5 = sp.factorint(abs(E[5]))
    assert all(sp.isprime(p) for p in f5) and sum(f5.values()) == 3   # 3 distinct new primes
    # e1,e2,e3 prime; e4,e5 composite -> "one new prime per rung" refuted at n=4
    assert all(sp.isprime(abs(E[n])) for n in (1, 2, 3))
    assert not sp.isprime(abs(E[4])) and not sp.isprime(abs(E[5]))
    assert E[4] % 11 == 0 and E[5] % 11 != 0                          # 11 repeats at n=4 only


def _det_mod_p(M, p):
    A = (M % p).astype(np.int64); n = A.shape[0]; det = 1
    for i in range(n):
        nz = np.nonzero(A[i:, i] % p)[0]
        if len(nz) == 0:
            return 0
        piv = i + int(nz[0])
        if piv != i:
            A[[i, piv]] = A[[piv, i]]; det = (-det) % p
        det = (det * int(A[i, i])) % p
        inv = pow(int(A[i, i]), p - 2, p)
        rows = np.arange(i + 1, n)
        if len(rows):
            A[rows] = (A[rows] - ((A[rows, i] * inv) % p)[:, None] * A[i]) % p
    return int(det % p)


def test_pf_period_three_through_n7():
    """11 | e_n  <=>  n = 1 (mod 3), verified to n=7 via modular determinant."""
    def Tmod(M, p):
        n = M.shape[0]; M2 = (M @ M) % p
        return np.vstack([np.hstack([M, M]), np.hstack([M2, M])]) % p
    Ff = np.array([[1, 1], [1, 0]], dtype=np.int64)
    zeros = []
    M = Ff
    for n in range(8):
        I = np.eye(M.shape[0], dtype=np.int64)
        if _det_mod_p(I - M, 11) == 0:
            zeros.append(n)
        M = Tmod(M, 11)
    assert zeros == [1, 4, 7]
    for n in range(6):                                   # no factor of 5 or 7 up to n=5
        assert E[n] % 5 != 0 and E[n] % 7 != 0


# ---------- P-C ----------
def test_pc_magnitude_degeneracy_law():
    """distinct-eigenvalue pairs sharing |lambda| = 2^n - 1 (all complex-conjugate)."""
    for n in range(5):
        A = np.array(_rung(n).tolist(), dtype=float)
        eig = np.linalg.eigvals(A)
        mags = np.sort(np.abs(eig))
        pairs = sum(1 for i in range(len(mags) - 1)
                    if abs(mags[i] - mags[i + 1]) < 1e-9 * max(1.0, mags[i]))
        assert pairs == 2 ** n - 1, (n, pairs)
        assert sum(abs(z.imag) < 1e-9 for z in eig) == 2          # exactly 2 real eigenvalues
    # charpoly irreducible at every rung
    x = sp.Symbol('x')
    for n in range(4):
        assert sp.Poly(_rung(n).charpoly(x).as_expr(), x).is_irreducible


# ---------- P-B ----------
def test_pb_free_energy_diverges():
    f = {n: math.log(abs(E[n])) / 2 ** (n + 1) for n in range(1, 6)}
    assert all(f[n] < f[n + 1] for n in range(1, 5))              # strictly increasing
    assert abs(f[5] / f[4] - 1.5) < 0.05                          # ratio -> 3/2


# ---------- FL2 ----------
def _D(Gt, t, y):
    return sp.expand(sp.resultant(t ** 2 - 2 * y * t + y ** 2 - y ** 3, Gt, t))


def test_fl2_golden_norm_transfer():
    t, y = sp.symbols("t y")
    phi, psi = (1 + sp.sqrt(5)) / 2, (1 - sp.sqrt(5)) / 2
    g2 = _D(t ** 3 - t ** 2 + 2 * t - 1, t, y)                    # g2 = D(g1), degree 9
    assert sp.Poly(g2, y).degree() == 9
    N2 = sp.nsimplify(sp.expand(g2.subs(y, phi) * g2.subs(y, psi)))
    assert N2 == -809 == E[2]
    g3 = _D(g2.subs(y, t), t, y)                                  # g3 = D(g2), degree 27
    N3 = sp.nsimplify(sp.expand(g3.subs(y, phi) * g3.subs(y, psi)))
    assert N3 == -18845089 == E[3]
