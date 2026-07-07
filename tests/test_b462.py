"""B462 (Relation R3) — locks: the phi-scan gate, the forced structures, the
Masbaum gates, and the kappa-diagonal's banked-size gate + parabolic law."""
import os
import sys

import mpmath as mp
import pytest
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "frontier", "B462_relation_r3_double"))
sys.path.insert(0, os.path.join(HERE, "..", "frontier", "B441_child_wrt"))

import wrt as B441
from phi_scan import qd, tau_from_vector, pairing
from masbaum import masbaum_cj, masbaum_poly
import kappa_diagonal as KD


def test_engine_gate_reproduces_b441():
    mp.mp.dps = 40
    for r in (5, 7, 9, 11):
        mine = complex(tau_from_vector(r, 5))
        theirs = complex(B441.wrt(B441.cj_fig8, 5, r))
        assert abs(mine - theirs) < 1e-12


def test_tt_pairing_zero_is_km_forced():
    """T^2 pairing = 0 at odd r, forced by J_{r-n}=J_n + tw^2 antisymmetry."""
    mp.mp.dps = 30
    for r in (5, 7, 9):
        q = mp.e**(2j * mp.pi / r)
        assert max(abs(B441.cj_fig8(r - n, q) - B441.cj_fig8(n, q))
                   for n in range(1, r)) < 1e-20
        assert abs(pairing(r, 'TT')) < 1e-18


def test_masbaum_p_minus1_is_fig8():
    mp.mp.dps = 30
    cj = masbaum_cj(-1)
    for r in (5, 7):
        q = mp.e**(2j * mp.pi / r)
        for n in range(1, r):
            assert abs(cj(n, q) - B441.cj_fig8(n, q)) < 1e-18


def test_masbaum_j2_is_jones_52_mirror():
    Q = sp.Symbol('q')
    j2 = sp.expand(masbaum_poly(2, 2))
    # Knot-Atlas V(5_2) with q -> 1/q (this convention's K_2 is the mirror)
    assert sp.simplify(j2 - sp.expand(-Q**6 + Q**5 - Q**4 + 2*Q**3 - Q**2 + Q)) == 0


def test_kappa_fork_sizes_match_b174():
    for word, size in KD.BANKED_SIZES.items():
        fp = KD.fork_poly(word)
        assert sp.Poly(sp.expand(fp), KD.p).degree() == size


def test_parabolic_law_kappa_minus2_in_every_fork():
    x = KD.x
    for word in KD.BANKED_SIZES:
        fp = KD.fork_poly(word)
        kappa_polys = set()
        for g, _ in sp.factor_list(fp)[1]:
            kp = sp.factor(sp.resultant(sp.Poly(g, KD.p), sp.Poly(x - KD.f(KD.p), KD.p), KD.p))
            for kg, _ in sp.factor_list(kp)[1]:
                kappa_polys.add(sp.expand(kg))
        assert sp.expand(x + 2) in kappa_polys


def test_sesquilinear_equals_bilinear_for_amphichiral():
    """4_1's Z-vector is real (amphichirality) => H = B — the CUT-by-theorem."""
    mp.mp.dps = 30
    for r in (5, 7, 9):
        q = mp.e**(2j * mp.pi / r)
        assert max(abs(mp.im(B441.cj_fig8(n, q))) for n in range(1, r)) < 1e-20
