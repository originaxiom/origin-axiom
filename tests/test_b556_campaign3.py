"""Tower-probe campaign — the two re-run cells (P-E, E4), computed in-sandbox.

  P-E : the tower's Galois structure is NOT (Z/2)^{n+1}. Rung 0 = Z/2 (order 2),
        but rung 1 = D4 (order 8, non-abelian) -- refutes the elementary-abelian
        claim. e_n stays Galois-invariant (rational). The non-abelian D4 (complex
        embeddings) is why P-C sees complex-conjugate magnitude-degenerate pairs.
  E4  : covering functors are NON-escalating. A finite cover / higher-block
        presentation preserves topological entropy = log(Perron); the 2-block cover
        of the Fibonacci SFT has Perron = phi (unchanged), while the (M,M^2)
        escalator T(F) raises it to 3.676. Only the coupling escalates.
See frontier/B556_escalator_tower/FINDINGS.md.
"""
import sympy as sp

x = sp.Symbol('x')
F = sp.Matrix([[1, 1], [1, 0]])


def _T(M):
    return sp.Matrix(sp.BlockMatrix([[M, M], [M * M, M]]))


def test_pe_galois_not_elementary_abelian():
    """rung 0 = Z/2 (abelian); rung 1 = D4 (order 8, non-abelian) -> (Z/2)^{n+1} refuted."""
    cp0 = sp.Poly(F.charpoly(x).as_expr(), x)
    G0, _ = cp0.galois_group()
    assert G0.order() == 2 and G0.is_abelian                 # rung 0: Z/2 (matches (Z/2)^1)
    M1 = _T(F)
    cp1 = sp.Poly(M1.charpoly(x).as_expr(), x)
    G1, _ = cp1.galois_group()
    assert G1.order() == 8 and not G1.is_abelian             # rung 1: D4, NOT (Z/2)^2 (order 4)
    # e_n stays Galois-invariant (rational integer)
    assert (sp.eye(M1.shape[0]) - M1).det() == -11


def test_e4_covering_preserves_perron_only_coupling_escalates():
    phi = (1 + sp.sqrt(5)) / 2
    # 2-block (higher-block) presentation of the golden-mean SFT (no 'bb'): states aa,ab,ba
    states = ['aa', 'ab', 'ba']
    A = sp.zeros(3, 3)
    for i, s in enumerate(states):
        for j, t in enumerate(states):
            if s[1] == t[0]:                                 # overlap; bb already excluded from states
                A[i, j] = 1
    per_cover = max((sp.re(sp.N(r)) for r in A.eigenvals()))
    assert abs(sp.N(per_cover - phi)) < 1e-9                 # cover Perron unchanged = phi
    # the escalator raises the Perron
    T_F = _T(F)
    per_esc = max((sp.re(sp.N(r)) for r in T_F.eigenvals()))
    assert abs(sp.N(per_esc)) > 3.6                          # escalates to ~3.676
    assert abs(sp.N(per_esc - phi)) > 2.0                    # NOT phi -- coupling escalates
