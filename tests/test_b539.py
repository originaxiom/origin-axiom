"""Locks for B539 — the relations campaign."""
import numpy as np
import sympy as sp

t = sp.Symbol('t')
MIN = t**4 - t**2 - 1


def red(e):
    return sp.rem(sp.expand(e), MIN, t)


def test_catalog_witnesses_exact():
    x, y = sp.symbols('x y')
    tau, phi, beta = t, t**2, t**2 + t**3
    cases = [
        (y - x**2, tau, phi),
        (y**2 - y - 1, tau, phi),
        (x**4 - x**2 - 1, tau, phi),
        (y*(x - 1) - 1, tau, beta),
        (y - x**2 + 1, tau, t**2 - 1),
    ]
    for P, wx, wy in cases:
        assert red(P.subs([(x, wx), (y, wy)])) == 0


def test_positive_control_e8():
    E8 = [1, 1.6180340, 1.9890438, 2.4048672, 2.9562952, 3.2183405,
          3.8911568, 4.7833861]
    phi = (1 + np.sqrt(5)) / 2
    assert abs(E8[1] - phi) < 1.5e-2 * phi          # GOLD at Coldea tolerance
    for i, j in [(5, 2), (6, 3), (7, 4)]:
        assert abs(E8[i]/E8[j] - E8[1]) < 1e-6      # self-similarity


def test_sm_no_match_at_1e3():
    """The 19-parameter SM list has ZERO catalog hits at tol 1e-3."""
    m_e, m_mu, m_tau = 0.51099895e-3, 0.1056583755, 1.77686
    m_u, m_d, m_s, m_c, m_b, m_t = 2.16e-3, 4.67e-3, 93.4e-3, 1.27, 4.18, 172.69
    m_W, m_Z, m_H = 80.3692, 91.1876, 125.25
    SM = [137.035999084, 0.1180, 0.23122, m_mu/m_e, m_tau/m_e, m_tau/m_mu,
          m_u/m_d, m_s/m_d, m_c/m_s, m_b/m_s, m_t/m_b, m_c/m_u, m_t/m_u,
          m_W/m_Z, m_H/m_Z, m_H/m_W, 0.22500, 0.04182, 0.00365]
    rels = [
        lambda x, y: (y - x**2, max(abs(y), x*x)),
        lambda x, y: (y*y - y - 1, max(y*y, abs(y), 1)),
        lambda x, y: (x**4 - x**2 - 1, max(x**4, x*x, 1)),
        lambda x, y: (y - x**3, max(abs(y), abs(x)**3)),
        lambda x, y: (x*y - 1, max(abs(x*y), 1)),
        lambda x, y: (y*(x - 1) - 1, max(abs(y*(x-1)), 1)),
        lambda x, y: (y - x**2 + 1, max(abs(y), x*x, 1)),
    ]
    hits = 0
    for rel in rels:
        for i, x in enumerate(SM):
            for j, y in enumerate(SM):
                if i == j:
                    continue
                P, s = rel(x, y)
                if s > 0 and abs(P) / s < 1e-3:
                    hits += 1
    assert hits == 0
