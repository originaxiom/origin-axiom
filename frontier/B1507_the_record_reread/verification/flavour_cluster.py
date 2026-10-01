"""B1507 -- the July flavour cluster (B324, B325, B335, B343, B345) read against B1361/B1362: own code.
(a) A matrix commuting with the cyclic permutation of the generations is a circulant circ(c0, c1, c2), diagonal in the charge
    (Fourier) basis with eigenvalues c0 + c1 w^k + c2 w^2k.  Generic: three distinct singular values (B325's refutation of a
    'Z/3-protected' degeneracy).  Symmetric (c1 = c2, as E6's symmetric cubic gives): a degenerate pair (B1362).  All three equal
    only when c1 = c2 = 0, i.e. no coupling between generations -- which B335's 'the masses are exactly degenerate' needs and does
    not state.
(b) B345's anti-diagonal texture (charges 0,1,2; allowed (0,0), (1,2), (2,1)) for a symmetric bilinear coupling IS circ(x, y, y) in
    the charge basis: [[x+2y, 0, 0], [0, 0, x-y], [0, x-y, 0]], singular values |x+2y|, |x-y|, |x-y| -- B1362's pair, in July."""
import numpy as np
import sympy as sp

W = (-1 + sp.sqrt(3) * sp.I) / 2


def circulant_facts():
    P = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    c0, c1, c2 = sp.symbols('c0 c1 c2')
    M = sp.Matrix([[c0, c2, c1], [c1, c0, c2], [c2, c1, c0]])
    commutes = (P * M * P.T - M).applyfunc(sp.simplify) == sp.zeros(3)
    F = sp.Matrix(3, 3, lambda i, j: W**(i * j)) / sp.sqrt(3)
    D = (F.H * M * F).applyfunc(lambda e: sp.simplify(sp.expand(e)))
    diagonal = all(D[i, j] == 0 for i in range(3) for j in range(3) if i != j)
    eig = [D[k, k] for k in range(3)]
    sym = [sp.simplify(e.subs(c2, c1)) for e in eig]
    all_equal = sp.solve([sp.expand(eig[0] - eig[1]), sp.expand(eig[1] - eig[2])], [c1, c2], dict=True)
    rng = np.random.default_rng(1)
    generic_distinct, symmetric_pair = True, True
    for _ in range(50):
        cc = rng.normal(size=3) + 1j * rng.normal(size=3)
        Mn = np.array([[cc[0], cc[2], cc[1]], [cc[1], cc[0], cc[2]], [cc[2], cc[1], cc[0]]])
        s = np.linalg.svd(Mn, compute_uv=False)
        generic_distinct &= min(abs(s[0] - s[1]), abs(s[1] - s[2])) > 1e-9
        s2 = np.sort(np.linalg.svd(Mn + Mn.T, compute_uv=False))
        symmetric_pair &= min(abs(s2[0] - s2[1]), abs(s2[1] - s2[2])) < 1e-9
    return dict(commutes=commutes, diagonal_in_charge_basis=diagonal, symmetric_eigenvalues=[str(e) for e in sym],
                symmetric_pair_degenerate=sp.simplify(sym[1] - sym[2]) == 0, all_equal_only_if=[{str(k): str(v) for k, v in d.items()} for d in all_equal],
                generic_three_distinct_50_of_50=bool(generic_distinct), symmetric_pair_50_of_50=bool(symmetric_pair))


def b345_texture():
    q = [0, 1, 2]
    allowed = [(i, j) for i in range(3) for j in range(3) if (q[i] + q[j]) % 3 == 0]
    x, y = sp.symbols('x y')
    C = sp.Matrix([[x, y, y], [y, x, y], [y, y, x]])
    F = sp.Matrix(3, 3, lambda i, j: W**(i * j)) / sp.sqrt(3)
    B = (F.T * C * F).applyfunc(lambda e: sp.simplify(sp.expand(e)))     # a bilinear form transforms by F^T . F
    support = [(i, j) for i in range(3) for j in range(3) if B[i, j] != 0]
    return dict(allowed=allowed, circulant_in_charge_basis=[[str(B[i, j]) for j in range(3)] for i in range(3)],
                support_equals_allowed=sorted(support) == sorted(allowed))


if __name__ == "__main__":
    for k, v in circulant_facts().items():
        print("(a)", k, "=", v)
    for k, v in b345_texture().items():
        print("(b)", k, "=", v)
