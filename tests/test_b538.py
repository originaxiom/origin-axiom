"""Locks for B538 — the reframe test cycle's EXACT prediction tables."""
import numpy as np


def test_e8_ladder_exact():
    C = np.array([
        [2, -1, 0, 0, 0, 0, 0, 0], [-1, 2, -1, 0, 0, 0, 0, 0],
        [0, -1, 2, -1, 0, 0, 0, 0], [0, 0, -1, 2, -1, 0, 0, 0],
        [0, 0, 0, -1, 2, -1, 0, -1], [0, 0, 0, 0, -1, 2, -1, 0],
        [0, 0, 0, 0, 0, -1, 2, 0], [0, 0, 0, 0, -1, 0, 0, 2]])
    w, v = np.linalg.eigh(C)
    pf = np.abs(v[:, np.argmin(w)])
    m = np.sort(pf / pf.min())
    claim = [1, 1.6180340, 1.9890438, 2.4048672, 2.9562952,
             3.2183405, 3.8911568, 4.7833861]
    assert np.allclose(m, claim, atol=2e-6)
    phi = (1 + np.sqrt(5)) / 2
    for (i, j) in [(5, 2), (6, 3), (7, 4)]:
        assert abs(m[i] / m[j] - phi) < 1e-9


def test_controls_discriminate():
    phi = (1 + np.sqrt(5)) / 2
    silver = 1 + np.sqrt(2)
    e7 = 2 * np.cos(np.pi / 18)
    assert abs(silver - 2.4142136) < 1e-6
    assert abs(e7 - 1.9696155) < 1e-6
    assert min(abs(silver - phi), abs(e7 - phi)) > 0.35


def test_jarlskog():
    s12, s13, s23, d = 0.2250, 0.00369, 0.04182, 1.144
    c12, c13, c23 = (np.sqrt(1 - s**2) for s in (s12, s13, s23))
    J = c12 * c23 * c13**2 * s12 * s23 * s13 * np.sin(d)
    assert abs(J - 3.08e-5) < 5e-7
    assert J != 0


def test_gap_label_sets_disjoint():
    phi = (1 + np.sqrt(5)) / 2
    golden = {round((n / phi) % 1, 6) for n in range(1, 7)}
    silver = {round((n / (1 + np.sqrt(2))) % 1, 6) for n in range(1, 7)}
    assert not golden & silver
