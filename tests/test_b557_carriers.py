"""Tower-probe campaign — the rung-2 carriers (B557), re-verified in-sandbox.

  E1  : an explicit primitive 8-letter substitution sigma8 whose incidence matrix
        is T(M4); the quine seed-invariant lifts (letter 1 once, at position 0).
  T-1 : the rung-2 gap-label module from T(M4) (irreducible octic, Perron = lambda-law,
        golden tower Q(sqrt5) c Q(sqrt5,sqrt phi) c Q(lambda_2), freq_0 = 1/lambda_2).
See frontier/B557_escalator_campaign/CARRIERS_FINDINGS.md.
"""
import numpy as np
import sympy as sp

M4 = sp.Matrix([[1, 1, 1, 1], [1, 0, 1, 0], [2, 1, 1, 1], [1, 1, 1, 0]])


def _T(M):
    return sp.Matrix(sp.BlockMatrix([[M, M], [M * M, M]]))


def test_e1_sigma8_incidence_and_seed_invariant():
    """T(M4) is realized by an explicit primitive 8-letter substitution; seed lifts."""
    TM4 = _T(M4)
    images = {}
    for j in range(8):
        col = [int(TM4[i, j]) for i in range(8)]
        assert col[0] == 1                      # row 1 all-ones => letter 1 once per image
        word = [1] + [li + 1 for li in range(1, 8) for _ in range(col[li])]
        images[j + 1] = word
    inc = sp.zeros(8, 8)
    for j in range(1, 9):
        for L in images[j]:
            inc[L - 1, j - 1] += 1
    assert inc == TM4                            # incidence(sigma8) == T(M4)
    An = np.array(inc.tolist(), dtype=np.int64)
    assert np.all((An @ An) > 0)                 # primitive at k=2
    assert all(img[0] == 1 and img.count(1) == 1 for img in images.values())   # seed-invariant


def test_t1_rung2_gap_label_module():
    x = sp.Symbol('x')
    R2 = _T(M4)
    cp = sp.Poly(R2.charpoly(x).as_expr(), x)
    expected = sp.Poly(x**8 - 4 * x**7 - 56 * x**6 - 152 * x**5 - 205 * x**4
                       - 192 * x**3 - 134 * x**2 - 56 * x - 11, x)
    assert cp == expected and cp.is_irreducible
    roots = np.roots([1, -4, -56, -152, -205, -192, -134, -56, -11])
    assert int(np.sum(np.abs(roots.imag) < 1e-9)) == 2       # signature (2 real, 3 cplx pairs)
    lam2 = float(max(roots, key=lambda z: z.real).real)
    assert abs(lam2 - 10.724751771861389) < 1e-9
    lam1 = float(max(np.roots([1, -2, -5, -4, -1]), key=lambda z: z.real).real)
    assert abs(lam1 * (1 + np.sqrt(lam1)) - lam2) < 1e-9      # lambda-law lambda_2=lambda_1(1+sqrt lambda_1)
    # freq_0 = 1/lambda_2 (normalized right Perron eigenvector, comp0=1, entry-sum=lambda_2)
    A = np.array(R2.tolist(), dtype=float)
    w, V = np.linalg.eig(A)
    v = V[:, int(np.argmax(w.real))].real
    v = v / v[0]
    assert abs(v.sum() - lam2) < 1e-6
    assert abs((1.0 / v.sum()) - 1.0 / lam2) < 1e-9          # freq_0 = 1/lambda_2
