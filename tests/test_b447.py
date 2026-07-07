"""Locks for B447 (Thermodynamic Campaign D2) — the m-scan harness + the laundered flag.

Fast subset (~60 s): module arithmetic, three-regime transport at small N, criticality,
and the burden-inversion surrogate reproducing the measured peak at m=1.
"""
import math
import os
import sys

import numpy as np

HERE = os.path.join(os.path.dirname(__file__), "..", "frontier", "B447_thermo_d2_mscan")
sys.path.insert(0, HERE)
import harness as H  # noqa: E402


def test_theta_module_is_letter_frequency():
    # theta_m = b-letter frequency = 1/(1+lam_m); NOT (sqrt(m^2+4)-m)/2 for m >= 2
    for m in (1, 2, 3):
        w = H.metallic_word(m, 4000)
        freq_b = float(np.mean(w == 1))
        assert abs(freq_b - H.theta(m)) < 2e-3
    assert abs(H.theta(2) - (math.sqrt(8) - 2) / 2) > 0.01   # the trap, kept visible


def test_three_regime_transport_small():
    per = np.tile([0, 1], 300)
    rnd = np.random.default_rng(7).integers(0, 2, 600)
    gold = H.metallic_word(1, 600)
    b_per, _ = H.transport_beta(per, 1.0)
    b_rnd, _ = H.transport_beta(rnd, 1.0)
    b_gold, _ = H.transport_beta(gold, 1.0)
    assert b_per > 0.9
    assert b_rnd < 0.35
    assert 0.4 < b_gold < 0.9
    assert b_rnd < b_gold < b_per


def test_permanent_criticality_classwide():
    for m in (1, 4, 6):
        w = H.metallic_word(m, 1000)
        E = H.spectrum(H.metallic_word(m, 600), 1.0)
        Eon = E[np.linspace(10, len(E) - 10, 8).astype(int)]
        g = H.lyapunov(w, 1.0, Eon)
        assert abs(g.mean()) < 0.01          # ~0 on-spectrum
    # off-spectrum control: in the biggest gap gamma is far from 0
    E = np.sort(H.spectrum(H.metallic_word(1, 600), 1.0))
    d = np.diff(E)
    i = int(np.argmax(d))
    goff = H.lyapunov(H.metallic_word(1, 1000), 1.0, np.array([E[i] + d[i] / 2]))
    assert goff[0] > 0.1


def test_burden_inversion_surrogate_matches_measured_peak():
    # the exhibited F: K=4 Gauss-quadrature surrogate reproduces m=1's measured
    # high-T peak at V=2 to < 0.2% (parameter-free)
    sys.path.insert(0, HERE)
    from burden_inversion import high_peak_of, gauss_quadrature_dos  # noqa: E402
    E = H.spectrum(H.metallic_word(1, 1500), 2.0)
    meas = high_peak_of(E)
    nd, wt = gauss_quadrature_dos(E, 4)
    surr = high_peak_of(nd, wt)
    assert abs(meas - 1.8026) < 0.01
    assert abs(surr - meas) / meas < 0.002


def test_gap_labels_on_theta_module():
    E = H.spectrum(H.metallic_word(2, 1200), 1.0)
    labs = H.gap_labels(E, H.theta(2), n_top=6)
    assert max(g['resid'] for g in labs) < 1e-3
