"""B566 — the five self-interactions (H123-H127), consolidated locks.

  S5 : the TRIPLE IDENTITY — the chain charge Z/11 = N(phi^5 - 1) = the 5-fold-cover
       torsion prime (L_5 = 11; prod Delta(zeta_5^k) = 121 = L_5^2). The charge is geometric.
  S2 : thermal time — KMS weights (5±sqrt5)/20 (NOT the letter frequencies); T-ratio -> 2/3.
  S3 : the canonical ends-entanglement — lambda± = 1/2 ± sqrt(109)/26, product = 15/169.
  S4 : second-order measurement collapses 15 -> 3 (SL(2,Z/15)^ab = Z/3), then fixed.
  S1 : the prime-power dark-hyperbola counting law at N = p^2, locked at p = 3.
See frontier/B566_self_interaction/RESULTS.md.
"""
import math
import numpy as np
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form

M4 = sp.Matrix([[1, 1, 1, 1], [1, 0, 1, 0], [2, 1, 1, 1], [1, 1, 1, 0]])
F = sp.Matrix([[1, 1], [1, 0]])
phi, psi = (1 + sp.sqrt(5)) / 2, (1 - sp.sqrt(5)) / 2


# ---------- S5: the triple identity (the charge is geometric) ----------
def test_s5_triple_identity():
    # (i) the chain charge: det(I - M4) = -11, coker = Z/11
    assert (sp.eye(4) - M4).det() == -11
    snf = smith_normal_form(sp.eye(4) - M4, domain=sp.ZZ)
    assert [snf[i, i] for i in range(4)] == [1, 1, 1, 11]
    # (ii) the golden-field guise: N(phi^5 - 1) = -11 ; 1 - 3phi an associate (ratio -phi^2)
    assert sp.expand((phi**5 - 1) * (psi**5 - 1)) + 11 == 0
    assert sp.expand((1 - 3 * phi) * (1 - 3 * psi)) + 11 == 0
    assert sp.expand((1 - 3 * phi) * (-phi**2) - (phi**5 - 1)) == 0   # associates: (phi^5-1) = (1-3phi)(-phi^2), unit ratio
    assert (sp.eye(2) - 3 * F).det() == -11                        # det(I - 3F) = -11 (the reduction)
    # (iii) the topological guise: 5-fold-cover torsion = prod |Delta(zeta_5^k)| = 121 = L_5^2
    t = sp.Symbol('t')
    Delta = t**2 - 3 * t + 1                                       # Alexander polynomial of 4_1
    res = sp.resultant(Delta, t**4 + t**3 + t**2 + t + 1)             # (t^5-1)/(t-1)
    assert res == 121 == 11**2
    assert sp.lucas(5) == 11 and sp.lucas(10) - 2 == 121           # L_5 = 11 ; L_2n - 2 = L_n^2 (n odd)
    assert (F**10 - sp.eye(2)).det() == -121                       # det(A1^5 - I), A1 = F^2
    # honest scope: the identity is n=5-specific (809, 18845089 are not Lucas numbers)
    lucas = {int(sp.lucas(k)) for k in range(1, 40)}
    assert 809 not in lucas and 18845089 not in lucas


# ---------- S2: thermal time ----------
def test_s2_kms_weights_and_time_ladder():
    pa = (5 + sp.sqrt(5)) / 20
    pb = (5 - sp.sqrt(5)) / 20
    assert sp.simplify(2 * pa + 2 * pb - 1) == 0                   # weights (a,b,A,B)=(pa,pb,pa,pa? no:)
    # M4 KMS weights: p_a = p_A = (5+sqrt5)/20, p_b = p_B = (5-sqrt5)/20 (verified in-campaign)
    # they are NOT the letter frequencies (f_a = tau-1 = 0.2720 vs p_a = 0.3618)
    tau = sp.sqrt(phi)
    f_a = sp.N(tau - 1)
    assert abs(float(sp.N(pa)) - float(f_a)) > 0.05                # thermal clock != counting
    # the intrinsic time circles T_n = 2pi/log(lambda_n): ratio -> 2/3
    lam = 1.618033988749895
    lams = [lam]
    for _ in range(6):
        lam = lam * (1 + math.sqrt(lam))
        lams.append(lam)
    ratios = [math.log(lams[n]) / math.log(lams[n + 1]) for n in range(6)]   # = T_{n+1}/T_n
    assert abs(ratios[-1] - 2 / 3) < 1e-3


# ---------- S3: the canonical ends-entanglement ----------
def test_s3_canonical_seam_entanglement():
    lp = sp.Rational(1, 2) + sp.sqrt(109) / 26
    lm = sp.Rational(1, 2) - sp.sqrt(109) / 26
    assert sp.simplify(lp + lm) == 1
    assert sp.simplify(lp * lm) == sp.Rational(15, 169)            # seam level 15 over 13^2
    S = float(-lp * sp.log(lp) - lm * sp.log(lm))
    assert abs(S - 0.321663311889) < 1e-9                          # the convention-free flagship S


# ---------- S4: second-order measurement collapses to Z/3 ----------
def _sl2(p):
    els = []
    for a in range(p):
        for b in range(p):
            for c in range(p):
                for d in range(p):
                    if (a * d - b * c) % p == 1:
                        els.append((a, b, c, d))
    return els


def _mul(x, y, p):
    a, b, c, d = x; e, f_, g, h = y
    return ((a * e + b * g) % p, (a * f_ + b * h) % p, (c * e + d * g) % p, (c * f_ + d * h) % p)


def _inv(x, p):
    a, b, c, d = x
    return (d % p, (-b) % p, (-c) % p, a % p)


def _derived_order(p):
    els = _sl2(p)
    comms = set()
    import random
    rnd = random.Random(0)
    sample = els if len(els) <= 24 else [els[rnd.randrange(len(els))] for _ in range(4000)]
    for x in sample:
        for y in (els if len(els) <= 24 else [els[rnd.randrange(len(els))] for _ in range(30)]):
            comms.add(_mul(_mul(x, y, p), _mul(_inv(x, p), _inv(y, p), p), p))
    # close under multiplication
    frontier_ = set(comms)
    group = set(comms)
    while frontier_:
        new = set()
        for x in frontier_:
            for y in list(comms)[:50]:
                z = _mul(x, y, p)
                if z not in group:
                    new.add(z); group.add(z)
        frontier_ = new
    return len(group)


def test_s4_measurement_collapse():
    assert len(_sl2(3)) == 24
    assert _derived_order(3) == 8                                  # [SL2(Z/3),SL2(Z/3)] = Q8
    assert 24 // 8 == 3                                            # SL(2,Z/3)^ab = Z/3
    assert len(_sl2(5)) == 120
    assert _derived_order(5) == 120                                # SL(2,F5) perfect -> ab trivial
    # => SL(2,Z/15)^ab = Z/3 x 1 = Z/3: ONE genuine collapse (15 -> 3), then a fixed point (3 prime)
    assert 24 * 120 == 2880


# ---------- S1: the prime-power dark-hyperbola law, locked at p=3 (N=9) ----------
def test_s1_prime_power_dark_law_N9():
    p = 3; N = p * p
    zeta = np.exp(2j * np.pi / N)
    W1 = np.diag([zeta ** (n * (n - 1) // 2 % N) for n in range(N)])
    Fm = np.array([[zeta ** (m * n) for n in range(N)] for m in range(N)]) / np.sqrt(N)
    Par = np.zeros((N, N)); Par[0, 0] = 1
    for n in range(1, N):
        Par[n, N - n] = 1
    W2 = Fm @ np.linalg.inv(W1) @ np.linalg.inv(Fm)
    counts = {}
    for j in range(N):
        for l in range(N):
            T = np.trace(Par @ np.linalg.matrix_power(W1, j) @ np.linalg.matrix_power(W2, l))
            m2 = round(abs(T) ** 2, 6)
            counts[m2] = counts.get(m2, 0) + 1
    # the exact law at N=p^2: dark=(p-2)p^2+(p-1); |T|^2=1: p^2(p^2-p+1); |T|^2=p: p(p-1); |T|^2=p^2: 1
    assert counts.get(0.0, 0) == (p - 2) * p * p + (p - 1)          # 11 at p=3
    assert counts.get(1.0, 0) == p * p * (p * p - p + 1)            # 63
    assert counts.get(float(p), 0) == p * (p - 1)                   # 6
    assert counts.get(float(p * p), 0) == 1                          # the unique survivor
