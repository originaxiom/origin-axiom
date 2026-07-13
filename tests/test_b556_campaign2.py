"""Tower-probe campaign — the negatives + connections (B556/B540/S061), re-verified.

  P-A  : lambda1 = phi(1+sqrt phi) has non-abelian (D4) Galois closure => NOT a
         cyclotomic integer => NO fusion category of any rank (Calegari-Morrison-
         Snyder). The escalator exits the fusion-category world at rung 1.
  FL1  : the B540 NEW_2 <-> NEW_10 2-cycle is eigenvalue-universal (shared charpoly
         lambda^4-14lambda^3+7lambda^2-6lambda+1) but content-varying (matrices NOT
         permutation-conjugate).
  BKL  : golden Kasner + era-map fixed point u=phi (BKL "IS the trace map" downgraded
         to conjugate-on-locus; the golden-Kasner 3/2=1+p2 link survives).
  c_eff: method-validity control (V=0 free fermions -> c=1); the 7/10 lock-on is
         REFUTED (documented negative, noise-limited).
See frontier/B556_escalator_tower/FINDINGS.md and speculations/S061.
"""
import numpy as np
import sympy as sp


# ---------- P-A ----------
def test_pa_lambda1_non_cyclotomic_D4():
    x = sp.Symbol('x')
    p = sp.Poly(x**4 - 2 * x**3 - 5 * x**2 - 4 * x - 1, x)     # minpoly of lambda1 = phi(1+sqrt phi)
    assert p.is_irreducible
    G, _ = p.galois_group()
    assert G.order() == 8 and not G.is_abelian          # D4: non-abelian => non-cyclotomic
    # non-abelian Galois closure => not contained in any cyclotomic field (Kronecker-Weber)
    # => lambda1 is not a cyclotomic integer => no fusion category has an object of this dim (CMS).


# ---------- FL1 ----------
_NEW_2 = ((0, 1, 2, 1, 3),
          (0, 1, 2, 1, 3, 0, 2, 2, 0, 1, 2, 2, 1, 3),
          (0, 1, 2, 1, 3, 0, 2, 2, 0, 1, 2, 2, 1, 3, 0, 2, 1, 3),
          (0, 1, 2, 1, 3, 0, 1, 2, 2, 1, 3, 0, 2, 1, 3))
_NEW_10 = ((0, 0, 1, 2, 0, 1, 2, 3, 0, 1, 2, 0, 2, 3),
           (0, 0, 1, 2, 3, 0, 1, 2, 3),
           (0, 0, 1, 2, 0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 0, 2, 3),
           (0, 0, 1, 2, 3, 0, 1, 2, 0, 2, 3))


def _M_of(codes):
    M = sp.zeros(4, 4)
    for i, w in enumerate(codes):
        for j in w:
            M[j, i] += 1
    return M


def test_fl1_isospectral_nonconjugate():
    import itertools
    M2, M10 = _M_of(_NEW_2), _M_of(_NEW_10)
    lam = sp.Symbol('lambda')
    expected = lam**4 - 14 * lam**3 + 7 * lam**2 - 6 * lam + 1
    assert sp.expand(M2.charpoly().as_expr() - expected) == 0
    assert sp.expand(M10.charpoly().as_expr() - expected) == 0   # SHARED spectrum
    assert sp.Poly(expected, lam).is_irreducible
    # NOT permutation-conjugate: no relabeling P with P M2 P^-1 == M10
    A2, A10 = np.array(M2.tolist(), int), np.array(M10.tolist(), int)
    conj = False
    for perm in itertools.permutations(range(4)):
        P = np.eye(4, dtype=int)[list(perm)]
        if np.array_equal(P @ A2 @ P.T, A10):
            conj = True
            break
    assert not conj                                              # eigenvalue-universal, content-varies


# ---------- BKL ----------
def test_bkl_golden_kasner_and_era_fixed_point():
    phi = (1 + sp.sqrt(5)) / 2
    p = [-1 / (2 * phi), sp.Rational(1, 2), phi / 2]
    assert sp.simplify(sum(p)) == 1 and sp.simplify(sum(t**2 for t in p)) == 1
    assert 1 + p[1] == sp.Rational(3, 2)                         # 3/2 = 1 + p2
    assert sp.simplify(1 / (phi - 1) - phi) == 0                 # phi = fixed pt of era map u->1/(u-1)
    m = sp.symbols('m', positive=True)
    lam = (m + sp.sqrt(m**2 + 4)) / 2                            # metallic mean
    assert sp.simplify(1 / (lam - m) - lam) == 0                 # constant-era BKL cycle


# ---------- c_eff (method-validity control; the 7/10 lock-on is the documented negative) ----------
def test_ceff_method_control_v0_is_c1():
    """Uniform (V=0) free-fermion chain reproduces c=1 (validates the estimator);
    the Fibonacci c_eff(V) scan finds NO plateau at 7/10 (documented negative)."""
    N = 400
    H = np.diag(np.ones(N - 1), 1) + np.diag(np.ones(N - 1), -1)   # V=0 uniform hopping
    w, U = np.linalg.eigh(H)
    occ = U[:, :N // 2]
    C = occ @ occ.T
    Ls = [20, 40, 80, 160]
    S = []
    for L in Ls:
        a = N // 2 - L // 2
        pv = np.linalg.eigvalsh(C[a:a + L, a:a + L])
        pv = np.clip(pv, 1e-13, 1 - 1e-13)
        S.append(float(-np.sum(pv * np.log(pv) + (1 - pv) * np.log(1 - pv))))
    # bulk interval, two cuts: S = (c/3) log L + const ; slope*3 = c ~ 1
    c = 3 * np.polyfit(np.log(Ls), S, 1)[0]
    assert abs(c - 1.0) < 0.15                                     # method valid: c ~ 1
