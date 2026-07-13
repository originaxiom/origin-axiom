"""D6-s031m3 -- lock for the RETRACTION: K_3 (bronze, m=3, invariant trace field of the
once-punctured-torus bundle b++RRRLLL) is degree 6, NOT quadratic. Refutes the B571/OPEN_LEADS-L68
premise "K_3 = Q(sqrt(13)) IS quadratic". Reproduces (does not merely cite) B125's banked verdict
via a fresh SnapPy + cypari computation, at two independent precisions.

SnapPy/cypari-guarded: skips cleanly (record stands) when unavailable. Run:
  python3 -m pytest test_d6_s031m3_retraction.py -q
(3 passed, 1.3s, verified in-sandbox.)
"""
import pytest


def _degree6_check(bits_prec, thresh):
    cypari = pytest.importorskip("cypari")
    snappy = pytest.importorskip("snappy")
    pari = cypari.pari

    def hp(z):
        return pari(str(z.real())) + pari(str(z.imag())) * pari("I")

    M = snappy.Manifold("b++RRRLLL")  # m=3 bronze: M_3^2 = R^3 L^3 (B125 spine)
    assert abs(float(M.volume()) - 4.813819186) < 1e-6  # sanity: correct manifold

    sh = M.tetrahedra_shapes(part="rect", bits_prec=bits_prec)
    alpha = sum((7 * i + 3) * hp(z) for i, z in enumerate(sh))  # B125's primitive-element recipe
    for d in range(2, 11):
        p = alpha.algdep(d)
        val = abs(complex(p.subst("x", alpha)))
        if val < thresh and pari.polisirreducible(p):
            return d
    return None


def test_K3_is_degree_6_not_quadratic_bits400():
    d = _degree6_check(bits_prec=400, thresh=1e-70)
    assert d == 6, f"expected degree 6 (B125 record), got {d}"
    assert d != 2, "would confirm the Q(sqrt(13)) premise -- it does not"


def test_K3_is_degree_6_not_quadratic_bits800_independent_precision():
    # Second, independent precision/threshold -- exploratory-numerics-rigor: >=2 settings.
    d = _degree6_check(bits_prec=800, thresh=1e-140)
    assert d == 6, f"expected degree 6 (B125 record), got {d}"


def test_13_is_squarefree_but_irrelevant_field():
    # The one true fact in the B571/L68 note: 13 = 3^2+4 IS squarefree (so Q(sqrt13) is a genuine
    # quadratic field) -- but it is the metallic-mean/fusion field (B127 M-4), not K_3.
    import sympy as sp
    assert sp.factorint(13) == {13: 1}


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-q"]))
