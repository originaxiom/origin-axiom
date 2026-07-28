"""B788 — the Maass Spectrum Programme: locks on what was actually computed.

Locks the EXACT structural facts only (Step 2 + L1/L2). The eigenvalue tests (1-3) were
VACUOUS = DATA-UNAVAILABLE and have nothing to lock -- that is the point, and the lock on
their status lives in FINDINGS.md, not here.

Every assertion recomputes its fact. The arithmetic locks are snappy-free; the length-spectrum
locks use snappy when available and skip cleanly otherwise.
"""
import mpmath as mp
import pytest
import sympy as sp

VOL_M004 = "2.029883212819307250042405108549"


def test_step2_bianchi_index_is_exactly_12():
    """Humbert: vol(PSL(2,O_d)\\H^3) = |d_K|^{3/2} zeta_K(2)/(4 pi^2); ratio to vol(m004) = 12."""
    mp.mp.dps = 40
    L2chi = (mp.zeta(2, mp.mpf(1) / 3) - mp.zeta(2, mp.mpf(2) / 3)) / 9   # L(2, chi_-3)
    zK2 = mp.zeta(2) * L2chi
    vol_bianchi = mp.mpf(3) ** mp.mpf(1.5) * zK2 / (4 * mp.pi ** 2)
    index = mp.mpf(VOL_M004) / vol_bianchi
    assert abs(index - 12) < mp.mpf("1e-24")
    # and the library ceiling the index forces (Weyl ~ volume)
    assert abs(1 / index - mp.mpf(1) / 12) < mp.mpf("1e-24")


def test_step2_gamma41_is_not_the_principal_congruence_subgroup():
    """Riley holonomy mod (sqrt-3) generates ALL of SL(2,F_3) => Gamma_41 is not in Gamma(sqrt-3)."""
    A = sp.Matrix([[1, 1], [0, 1]])
    wbar = int(sp.Rational(-1, 2) % 3)          # omega == -1/2 (mod sqrt-3)
    assert wbar == 2
    B = sp.Matrix([[1, 0], [-wbar, 1]])

    def key(m):
        return tuple(int(x) % 3 for x in m)

    seen, frontier = {key(sp.eye(2))}, [sp.eye(2)]
    while frontier:
        nxt = []
        for m in frontier:
            for g in (A % 3, B % 3):
                p = (m * g) % 3
                if key(p) not in seen:
                    seen.add(key(p))
                    nxt.append(p)
        frontier = nxt
    assert len(seen) == 24                       # |SL(2,F_3)| = 24, so the image is everything
    # index is 12 (previous lock) yet the reduction is onto => not the principal congruence subgroup


def test_L2_geodesic_traces_lie_in_Z_omega_exactly():
    """tr(gamma) = 2 cosh(l/2) must lie in Z[omega] for Gamma_41 < PSL(2,O_3).

    Uses the m004 complex lengths recorded in the arc (cutoff 2.0). N(a+b w) = a^2-ab+b^2.
    """
    mp.mp.dps = 30
    lengths = [                                  # (Re l, Im l) from frontier/B788.../output.txt
        ("1.087070144995739", "1.722768449870090"),
        ("1.662885891058621", "2.392123788172313"),
        ("1.725109255324122", "0.921838931481337"),
    ]
    expected_norms = {3, 4, 7}
    sqrt3 = mp.sqrt(3)
    got = set()
    for re, im in lengths:
        ell = mp.mpc(mp.mpf(re), mp.mpf(im))
        tr = 2 * mp.cosh(ell / 2)
        b = 2 * tr.imag / sqrt3
        a = tr.real + b / 2
        bi, ai = mp.nint(b), mp.nint(a)
        assert max(abs(b - bi), abs(a - ai)) < mp.mpf("1e-12")     # exactly in Z[omega]
        got.add(int(ai * ai - ai * bi + bi * bi))
    assert got == expected_norms
    assert 3 in got            # the systole trace has norm 3 = the ramified prime of Q(sqrt-3)


def test_L1_m004_and_m003_share_volume_but_are_not_isospectral():
    snappy = pytest.importorskip("snappy")
    m4, m3 = snappy.Manifold("m004"), snappy.Manifold("m003")
    assert abs(float(m4.volume()) - float(m3.volume())) < 1e-9      # equal volume
    assert str(m4.homology()) != str(m3.homology())                 # homology discriminates
    s4 = min(complex(g.length).real for g in m4.length_spectrum(1.5))
    s3 = min(complex(g.length).real for g in m3.length_spectrum(1.5))
    assert abs(s4 - 1.087070144995739) < 1e-9
    assert abs(s3 - 0.862554627662061) < 1e-9
    assert s3 < s4                                                  # NOT isospectral
