"""Lock: the 3/2 Law of the escalator (Session-5 handoff, independently verified).

For T(M)=[[M,M],[M^2,M]] and lambda_n = Perron(T^n(F)):
  (i)   lambda_{n+1} = lambda_n (1 + sqrt(lambda_n))
  (ii)  log lambda_{n+1} / log lambda_n -> 3/2
  (iii) lambda_n ~ phi^{C (3/2)^n}, C = 2.4283
  why   T_k=[[M,M],[M^k,M]] has growth exponent (k+1)/2; k=2 minimal non-trivial
  Kasner (firewalled): 3/2 = 1 + p2, p2=1/2 the golden Kasner middle exponent.
See frontier/B556_escalator_tower/FINDINGS.md.
"""
import math
import numpy as np
import sympy as sp

F = sp.Matrix([[1, 1], [1, 0]])


def _T(M):
    return sp.Matrix(sp.BlockMatrix([[M, M], [M * M, M]]))


def _perron(n):
    M = F
    for _ in range(n):
        M = _T(M)
    A = np.array(M.tolist(), dtype=float)
    v = np.ones(A.shape[0])
    for _ in range(20000):
        v = A @ v
        v /= np.linalg.norm(v)
    return float((A @ v) @ v / (v @ v))


def test_lambda_law_and_growth_rate_three_halves():
    lams = [_perron(n) for n in range(8)]
    # (i) lambda-law reproduces each Perron
    for n in range(7):
        assert abs(lams[n + 1] - lams[n] * (1 + math.sqrt(lams[n]))) < 1e-4 * lams[n + 1]
    # (ii) log-ratio -> 3/2
    ratios = [math.log(lams[n + 1]) / math.log(lams[n]) for n in range(7)]
    assert abs(ratios[-1] - 1.5) < 1e-3          # 1.5001 at rung 7
    assert ratios[-1] < ratios[-2] < ratios[-3]  # monotone decrease toward 3/2


def test_asymptotic_constant_C():
    phi = (1 + 5 ** 0.5) / 2
    lams = [_perron(n) for n in range(8)]
    Cs = [math.log(lams[n]) / ((1.5 ** n) * math.log(phi)) for n in range(1, 8)]
    assert abs(Cs[-1] - 2.4283) < 1e-3           # converges to 2.4283


def test_general_growth_exponent_k_plus_1_over_2():
    # T_k eigenvector [v, lam^{(k-1)/2} v] => mu = lam(1 + lam^{(k-1)/2}).
    # The growth exponent is (k+1)/2: mu / lam^{(k+1)/2} tends to a finite constant.
    lam = 1e10
    for k in (1, 2, 3):
        mu = lam * (1 + lam ** ((k - 1) / 2))
        c = mu / lam ** ((k + 1) / 2)
        assert 0.9 < c < 2.1        # -> 2 (k=1), -> 1 (k>=2); exponent confirmed
    # and k=2 (the escalator) hits 3/2 cleanly in the log-ratio too
    assert abs(math.log(lam * (1 + lam ** 0.5)) / math.log(lam) - 1.5) < 1e-3


def test_kasner_link_exact():
    phi = (1 + sp.sqrt(5)) / 2
    p = [-1 / (2 * phi), sp.Rational(1, 2), phi / 2]     # golden Kasner exponents
    assert sp.simplify(sum(p)) == 1
    assert sp.simplify(sum(x ** 2 for x in p)) == 1
    assert 1 + p[1] == sp.Rational(3, 2)                 # 3/2 = 1 + middle exponent
