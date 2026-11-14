#!/usr/bin/env python3
"""Standalone zero-trust verifier for Card X-C9 (agy-exp).

Recomputes from scratch (zero imports from main or any other seat, zero reads of
SM-C7 or SM-C9 .py or .json files):
  1. Bohn's U(1) rho invariant rho_A(T^2_M) from Chapter IV, Section 4, Theorem 20
     and Equation (4.67), plus untwisted eta(T^2_M) (Theorem 4.4.12), verified on
     Bohn's worked examples, Corollary 4.4.21, orientation reversal, and SL(2, Z)
     conjugation invariance.
  2. Independent two-route recomputation of Z(0, chi_c) (Shintani half-open cone
     parallelogram sum with second-generator control, and geodesic period integral
     of G^(Jc)*) across all 16 levels / 601 characters of B1737, plus the per-level
     affine fit test of rho_A against sqrt(D) * Z(0, chi_c).
  3. Independent two-route recomputation of L_odd(1, chi_c) (Gauss-Legendre geodesic
     quadrature of G_c and holomorphic Siegel-theta logarithm increment) and test of
     eta_A(T^2_M) = rho_A(T^2_M) + eta(T^2_M) = -L_odd(1, chi_c) / pi^2 on all 601
     in-sample characters and 531 fresh out-of-sample characters across 10 unseen
     hyperbolic matrices, plus the 2D symplectic DFT bridge on principal congruence
     levels (+LR 3 and +LR 5) and 5 planted controls (P1-P5).
"""

from __future__ import annotations

import cmath
from fractions import Fraction
import json
import math
from pathlib import Path
import time
from typing import Dict, List, Sequence, Tuple

Mat2 = Tuple[Tuple[int, int], Tuple[int, int]]
Frac2 = Tuple[Fraction, Fraction]

L_MAT: Mat2 = ((1, 1), (0, 1))
R_MAT: Mat2 = ((1, 0), (1, 1))


def mat_mul(A: Mat2, B: Mat2) -> Mat2:
    return (
        (A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]),
        (A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]),
    )


def mat_pow(A: Mat2, k: int) -> Mat2:
    res: Mat2 = ((1, 0), (0, 1))
    base = A
    n = k
    while n > 0:
        if n & 1:
            res = mat_mul(res, base)
        base = mat_mul(base, base)
        n >>= 1
    return res


def mat_neg(A: Mat2) -> Mat2:
    return ((-A[0][0], -A[0][1]), (-A[1][0], -A[1][1]))


def mat_inv_sl2(A: Mat2) -> Mat2:
    a, b = A[0]
    c, d = A[1]
    assert a * d - b * c == 1
    return ((d, -b), (-c, a))


def word_level_matrix(sign_word: str, level: int) -> Tuple[Mat2, int]:
    """Return (M, num_neg_I) for a signed word level such as '+LR', 2 or '-LLRLR', 1."""
    sign_ch = sign_word[0]
    letters = sign_word[1:]
    assert sign_ch in ("+", "-") and len(letters) >= 2
    W: Mat2 = ((1, 0), (0, 1))
    for ch in letters:
        if ch == "L":
            W = mat_mul(W, L_MAT)
        elif ch == "R":
            W = mat_mul(W, R_MAT)
        else:
            raise ValueError(f"Unknown letter: {ch}")
    if sign_ch == "-":
        W = mat_neg(W)
        num_neg_i = level
    else:
        num_neg_i = 0
    return mat_pow(W, level), num_neg_i


# ---------------------------------------------------------------------------
# Section 1: Exact rational Bernoulli / sawtooth / Bohn rho & untwisted eta
# ---------------------------------------------------------------------------


def sgn_int(n: int) -> int:
    return 1 if n > 0 else (-1 if n < 0 else 0)


def frac_part(x: Fraction) -> Fraction:
    _, rem = divmod(x.numerator, x.denominator)
    return Fraction(rem, x.denominator)


def delta_nonint(x: Fraction) -> int:
    return 0 if x.denominator == 1 else 1


def P1_frac(x: Fraction) -> Fraction:
    if x.denominator == 1:
        return Fraction(0)
    return frac_part(x) - Fraction(1, 2)


def P2_frac(x: Fraction) -> Fraction:
    f = frac_part(x)
    return f * f - f + Fraction(1, 6)


def bohn_m_vec(M: Mat2, nu: Frac2) -> Tuple[int, int]:
    a, b = M[0]
    c, d = M[1]
    nu1, nu2 = nu
    m1_f = (1 - a) * nu1 - c * nu2
    m2_f = -b * nu1 + (1 - d) * nu2
    assert m1_f.denominator == 1 and m2_f.denominator == 1, f"Not fixed: M={M}, nu={nu}"
    return m1_f.numerator, m2_f.numerator


def rho_bohn_thm420(M: Mat2, nu: Frac2, bracket_mode: str = "R1") -> Fraction:
    """Bohn Chapter IV, Section 4, Theorem 20 in exact rationals.

    bracket_mode:
      - 'R1': ((2(a+d) - 4) / c) * (P_2(nu_1) - 1/6)  [exact TeX: \\lfrac{2(a+d)-4}{c}]
      - 'R2': (2(a+d)/c - 4) * (P_2(nu_1) - 1/6)      [planted misreading]
      - 'R3': (2(a+d) - 4/c) * (P_2(nu_1) - 1/6)      [planted misreading P5]
    """
    a, b = M[0]
    c, d = M[1]
    assert a * d - b * c == 1 and abs(a + d) > 2 and c != 0
    nu1, nu2 = nu
    assert not (nu1.denominator == 1 and nu2.denominator == 1)
    m1, _ = bohn_m_vec(M, nu)
    ac = abs(c)
    r = m1 % ac
    p2_shift = P2_frac(nu1) - Fraction(1, 6)
    if bracket_mode == "R1":
        pref = Fraction(2 * (a + d) - 4, c)
    elif bracket_mode == "R2":
        pref = Fraction(2 * (a + d), c) - Fraction(4)
    elif bracket_mode == "R3":
        pref = Fraction(2 * (a + d)) - Fraction(4, c)
    else:
        raise ValueError(bracket_mode)

    term1 = pref * p2_shift
    term2 = -4 * sum((P1_frac(Fraction(d * k, c)) for k in range(1, ac - r + 1)), Fraction(0))
    term3 = Fraction(sgn_int(c * (a + d)))
    d_nu1 = delta_nonint(nu1)
    m1_over_c = Fraction(m1, c)
    dm1_over_c = Fraction(d * m1, c)
    term4 = Fraction(-sgn_int(c) * d_nu1 * (1 - delta_nonint(m1_over_c)))
    term5 = -2 * P1_frac(dm1_over_c)
    term6 = -2 * d_nu1 * (P1_frac(m1_over_c) - P1_frac(dm1_over_c))
    return term1 + term2 + term3 + term4 + term5 + term6


def gen_dedekind_sum(a: int, c: int, nu1: Fraction, nu2: Fraction) -> Fraction:
    ac = abs(c)
    total = Fraction(0)
    for k in range(ac):
        arg1 = (Fraction(k) + nu1) / c
        arg2 = a * arg1 + nu2
        total += P1_frac(arg1) * P1_frac(arg2)
    return total


def rho_bohn_eq467(M: Mat2, nu: Frac2) -> Fraction:
    """Bohn Equation (4.67) in exact rationals."""
    a, b = M[0]
    c, d = M[1]
    assert a * d - b * c == 1 and abs(a + d) > 2 and c != 0
    nu1, nu2 = nu
    _ = bohn_m_vec(M, nu)
    s_nu = gen_dedekind_sum(a, c, nu1, nu2)
    s_0 = gen_dedekind_sum(a, c, Fraction(0), Fraction(0))
    return (
        Fraction(2 * (a + d), c) * (P2_frac(nu1) - Fraction(1, 6))
        - 4 * sgn_int(c) * (s_nu - s_0)
        + Fraction(sgn_int(c * (a + d)))
    )


def eta_untwisted(M: Mat2) -> Fraction:
    """Bohn Theorem 4.4.12 (Atiyah-Hirzebruch-Meyer untwisted eta(T^2_M) = Psi(M)/3)."""
    a, b = M[0]
    c, d = M[1]
    assert a * d - b * c == 1 and abs(a + d) > 2 and c != 0
    s_0 = gen_dedekind_sum(a, c, Fraction(0), Fraction(0))
    return Fraction(a + d, 3 * c) - 4 * sgn_int(c) * s_0 - Fraction(sgn_int(c * (a + d)))


def enumerate_fixed_characters(M: Mat2) -> Tuple[int, List[Frac2]]:
    """Return (exponent_N, sorted list of non-trivial c = (i/N, j/N) fixed by M)."""
    a, b = M[0]
    c, d = M[1]
    k00, k01 = 1 - a, -c
    k10, k11 = -b, 1 - d
    det_k = abs(k00 * k11 - k01 * k10)
    assert det_k == abs(2 - (a + d)) and det_k > 0
    g = math.gcd(math.gcd(abs(k00), abs(k01)), math.gcd(abs(k10), abs(k11)))
    N = det_k // g
    chars: List[Frac2] = []
    for i in range(N):
        for j in range(N):
            if i == 0 and j == 0:
                continue
            if (i * a + j * c - i) % N == 0 and (i * b + j * d - j) % N == 0:
                chars.append((Fraction(i, N), Fraction(j, N)))
    assert len(chars) == det_k - 1, f"Expected {det_k - 1} chars, got {len(chars)} for M={M}"
    return N, chars


# ---------------------------------------------------------------------------
# Section 2: Independent Z(0, chi_c) — Route A (Shintani cone) & Route B (G^(Jc)*)
# ---------------------------------------------------------------------------


def gamma_fixed_points(M: Mat2) -> Tuple[float, float]:
    """Fixed points beta > beta_p of gamma = M^T: z -> (a z + c) / (b z + d)."""
    a, b = M[0]
    c, d = M[1]
    assert b != 0
    disc = float((a + d) * (a + d) - 4)
    mid = (a - d) / (2.0 * b)
    rad = math.sqrt(disc) / (2.0 * abs(b))
    beta = mid + rad
    beta_p = mid - rad
    assert beta > beta_p
    assert abs(b * beta * beta + (d - a) * beta - c) < 1e-9 * max(1.0, abs(b) * beta * beta)
    return beta, beta_p


def find_cone_generators(M: Mat2, c_char: Frac2, count: int = 2) -> List[Tuple[int, int]]:
    """Find `count` primitive lattice vectors w in C_+ with chi_c(w) != 1."""
    beta, beta_p = gamma_fixed_points(M)
    c1, c2 = c_char
    found: List[Tuple[int, int]] = []
    for radius in range(1, 80):
        for w0 in range(-radius, radius + 1):
            for w1 in (-radius, radius) if abs(w0) < radius else range(-radius, radius + 1):
                if math.gcd(abs(w0), abs(w1)) != 1:
                    continue
                if w0 * beta + w1 <= 1e-11 or w0 * beta_p + w1 <= 1e-11:
                    continue
                phase_frac = frac_part(c1 * w0 + c2 * w1)
                if phase_frac == 0:
                    continue
                # Ensure not collinear with already chosen generators
                if any(w0 * u1 - w1 * u0 == 0 for (u0, u1) in found):
                    continue
                found.append((w0, w1))
                if len(found) == count:
                    return found
    raise RuntimeError(f"Could not find {count} cone generators for M={M}, c={c_char}")


def parallelogram_points(w: Tuple[int, int], wp: Tuple[int, int]) -> List[Tuple[int, int]]:
    """Exact integer points p in {t1*w + t2*wp : 0 < t1 <= 1, 0 <= t2 < 1}."""
    w0, w1 = w
    wp0, wp1 = wp
    raw_det = w0 * wp1 - w1 * wp0
    assert raw_det != 0
    delta = abs(raw_det)
    s = 1 if raw_det > 0 else -1

    # Tight p1 range from vertices 0, w, wp, w + wp
    p1_min = min(0, w1, wp1, w1 + wp1)
    p1_max = max(0, w1, wp1, w1 + wp1)

    pts: List[Tuple[int, int]] = []
    for p1 in range(p1_min, p1_max + 1):
        # Inequalities on p0:
        #   1 <= s*(wp1*p0 - wp0*p1) <= delta
        #   0 <= s*(-w1*p0 + w0*p1) < delta
        lo = -10**18
        hi = 10**18
        # Condition 1: A1 * p0 in [1 - B1, delta - B1] where A1 = s*wp1, B1 = -s*wp0*p1
        A1 = s * wp1
        B1 = -s * wp0 * p1
        if A1 > 0:
            lo = max(lo, math.ceil((1 - B1) / A1))
            hi = min(hi, math.floor((delta - B1) / A1))
        elif A1 < 0:
            lo = max(lo, math.ceil((delta - B1) / A1))
            hi = min(hi, math.floor((1 - B1) / A1))
        else:
            if not (1 <= B1 <= delta):
                continue

        # Condition 2: A2 * p0 in [-B2, delta - 1 - B2] where A2 = -s*w1, B2 = s*w0*p1
        A2 = -s * w1
        B2 = s * w0 * p1
        if A2 > 0:
            lo = max(lo, math.ceil((-B2) / A2))
            hi = min(hi, math.floor((delta - 1 - B2) / A2))
        elif A2 < 0:
            lo = max(lo, math.ceil((delta - 1 - B2) / A2))
            hi = min(hi, math.floor((-B2) / A2))
        else:
            if not (0 <= B2 < delta):
                continue

        for p0 in range(lo, hi + 1):
            u1 = s * (wp1 * p0 - wp0 * p1)
            u2 = s * (-w1 * p0 + w0 * p1)
            if 1 <= u1 <= delta and 0 <= u2 < delta:
                pts.append((p0, p1))

    assert len(pts) == delta, f"Count mismatch: got {len(pts)}, expected {delta}"
    return pts


def z0_shintani(M: Mat2, c_char: Frac2, w: Tuple[int, int]) -> complex:
    tr = M[0][0] + M[1][1]
    if tr > 0:
        gen = M
        scale = 1.0
    else:
        gen = mat_mul(M, M)
        scale = 0.5
    wp = (gen[0][0] * w[0] + gen[0][1] * w[1], gen[1][0] * w[0] + gen[1][1] * w[1])
    pts = parallelogram_points(w, wp)
    c1 = float(c_char[0])
    c2 = float(c_char[1])
    two_pi = 2.0 * math.pi
    chi_w = cmath.exp(1j * two_pi * (c1 * w[0] + c2 * w[1]))
    denom = (1.0 - chi_w) ** 2
    num = sum(cmath.exp(1j * two_pi * (c1 * p0 + c2 * p1)) for (p0, p1) in pts)
    return scale * (num / denom)


def b1438_letter_slope(sign_word: str, level: int, c_char: Frac2) -> Tuple[bool, float]:
    """B1438 Theorem D letter-by-letter slope where the sigma(x)=0 gauge is non-singular."""
    sign_ch = sign_word[0]
    letters = sign_word[1:]
    c1, c2 = frac_part(c_char[0]), frac_part(c_char[1])
    two_pi = 2.0 * math.pi
    total = 0j
    for _ in range(level):
        seq = (["-"] if sign_ch == "-" else []) + list(letters)
        for tok in seq:
            X = cmath.exp(1j * two_pi * float(c1))
            Y = cmath.exp(1j * two_pi * float(c2))
            if tok == "-":
                if c1 == 0:
                    return False, 0.0
                total += 1.0 / (1.0 - X)
                c1, c2 = frac_part(-c1), frac_part(-c2)
            elif tok == "L":
                c1, c2 = c1, frac_part(c1 + c2)
            elif tok == "R":
                c1_next = frac_part(c1 + c2)
                if c1 == 0 or c1_next == 0:
                    return False, 0.0
                XY = cmath.exp(1j * two_pi * float(c1_next))
                total += X / ((X - 1.0) * (XY - 1.0))
                c1 = c1_next
    return True, -total.real


# ---------------------------------------------------------------------------
# Gauss-Legendre nodes & closed-form Lipschitz q-series for G^(u)* and G_c
# ---------------------------------------------------------------------------


def gauss_legendre_nodes(n: int) -> List[Tuple[float, float]]:
    """Compute Gauss-Legendre nodes and weights on [-1, 1] by Newton iteration."""
    nodes_weights: List[Tuple[float, float]] = []
    m = (n + 1) // 2
    for i in range(1, m + 1):
        x = math.cos(math.pi * (i - 0.25) / (n + 0.5))
        for _ in range(30):
            p0 = 1.0
            p1 = x
            for k in range(2, n + 1):
                p2 = ((2 * k - 1) * x * p1 - (k - 1) * p0) / k
                p0, p1 = p1, p2
            dp = n * (x * p1 - p0) / (x * x - 1.0)
            dx = p1 / dp
            x -= dx
            if abs(dx) < 1e-16:
                break
        w = 2.0 / ((1.0 - x * x) * dp * dp)
        if 2 * i - 1 == n and n % 2 == 1:
            nodes_weights.append((0.0, w))
        else:
            nodes_weights.append((-x, w))
            nodes_weights.append((x, w))
    nodes_weights.sort(key=lambda t: t[0])
    return nodes_weights


GL_48 = gauss_legendre_nodes(48)
GL_96 = gauss_legendre_nodes(96)


def eval_G_shifted_star(z: complex, u: Frac2) -> complex:
    """Hecke-regularized shifted weight-2 series G^(u)*(z) for u in (Q/Z)^2 \\ {(0,0)}."""
    u1_f = frac_part(u[0])
    u2_f = frac_part(u[1])
    assert not (u1_f == 0 and u2_f == 0)
    u1 = float(u1_f)
    u2 = float(u2_f)
    y = z.imag
    assert y > 0.0
    two_pi_i = 2j * math.pi
    q = cmath.exp(two_pi_i * z)
    four_pi_sq = 4.0 * math.pi * math.pi

    if u1_f == 0:
        s_u = math.sin(math.pi * u2)
        const_term = (math.pi * math.pi) / (s_u * s_u)
        acc = 0j
        qr = q
        r = 1
        while True:
            term = (2.0 * r * math.cos(2.0 * math.pi * r * u2)) * (qr / (1.0 - qr))
            acc += term
            if abs(qr) * r < 1e-17 and r > 6:
                break
            qr *= q
            r += 1
        return const_term - four_pi_sq * acc - (math.pi / y)
    else:
        u1_tilde = 1.0 - u1
        q_u1 = cmath.exp(two_pi_i * u1 * z)
        q_u1t = cmath.exp(two_pi_i * u1_tilde * z)
        e_u2 = cmath.exp(two_pi_i * u2)
        e_u2_inv = e_u2.conjugate()
        p1 = q_u1
        p2 = q_u1t
        e1 = e_u2
        e2 = e_u2_inv
        qr = q
        acc = 0j
        r = 1
        while True:
            denom = 1.0 - qr
            term = r * (e1 * p1 + e2 * p2) / denom
            acc += term
            if r * max(abs(p1), abs(p2)) < 1e-17 and r > 6:
                break
            p1 *= q_u1
            p2 *= q_u1t
            e1 *= e_u2
            e2 *= e_u2_inv
            qr *= q
            r += 1
        return -four_pi_sq * acc - (math.pi / y)


def eval_G_twisted(z: complex, c_char: Frac2) -> complex:
    """Character-twisted holomorphic weight-2 series G_c(z) for c != (0,0)."""
    c1_f = frac_part(c_char[0])
    c2_f = frac_part(c_char[1])
    assert not (c1_f == 0 and c2_f == 0)
    c1 = float(c1_f)
    c2 = float(c2_f)
    c2_tilde = float(frac_part(-c2_f))
    two_pi_i = 2j * math.pi
    q = cmath.exp(two_pi_i * z)
    e_c1 = cmath.exp(two_pi_i * c1)
    e_c1_inv = e_c1.conjugate()

    const_term = 2.0 * math.pi * math.pi * float(P2_frac(c2_f))
    four_pi_sq = 4.0 * math.pi * math.pi

    w1 = e_c1 * cmath.exp(two_pi_i * (1.0 - c2) * z)
    w2 = e_c1_inv * cmath.exp(two_pi_i * (1.0 - c2_tilde) * z)
    acc = 0j
    r = 1
    while True:
        a1 = r - c2
        a2 = r - c2_tilde
        t1 = a1 * w1 / (1.0 - w1)
        t2 = a2 * w2 / (1.0 - w2)
        acc += t1 + t2
        if max(a1 * abs(w1), a2 * abs(w2)) < 1e-17 and r > 6:
            break
        w1 *= q
        w2 *= q
        r += 1
    return const_term - four_pi_sq * acc


def eval_log_siegel(z: complex, a_pt: Frac2) -> complex:
    """Canonical branch-cut-free holomorphic logarithm of Siegel's g_a(z) on H."""
    a1_f = frac_part(a_pt[0])
    a2_f = frac_part(a_pt[1])
    assert not (a1_f == 0 and a2_f == 0)
    a1 = float(a1_f)
    a2 = float(a2_f)
    two_pi_i = 2j * math.pi
    q = cmath.exp(two_pi_i * z)
    e_a2 = cmath.exp(two_pi_i * a2)
    e_a2_inv = e_a2.conjugate()

    res = 1j * math.pi * float(P2_frac(a1_f)) * z
    if a1_f != 0:
        w0 = cmath.exp(two_pi_i * a1 * z) * e_a2
        res += cmath.log(1.0 - w0)
    else:
        res += cmath.log(1.0 - e_a2)

    w_pos = cmath.exp(two_pi_i * (1.0 + a1) * z) * e_a2
    w_neg = cmath.exp(two_pi_i * (1.0 - a1) * z) * e_a2_inv
    n = 1
    while True:
        res += cmath.log(1.0 - w_pos) + cmath.log(1.0 - w_neg)
        if max(abs(w_pos), abs(w_neg)) < 1e-17 and n > 6:
            break
        w_pos *= q
        w_neg *= q
        n += 1
    return res


def geodesic_arc_params(M: Mat2) -> Tuple[float, float, float, float]:
    """Return (beta, beta_p, t_start, t_end) on z(t) = (beta*i*e^t + beta_p)/(i*e^t + 1)
    such that gamma = M^T maps z(t_start) -> z(t_end)."""
    a, b = M[0]
    c, d = M[1]
    beta, beta_p = gamma_fixed_points(M)
    tr_abs = abs(a + d)
    lam = 0.5 * (tr_abs + math.sqrt(tr_abs * tr_abs - 4.0))
    ell = 2.0 * math.log(lam)

    def z_of_t(t: float) -> complex:
        iet = 1j * math.exp(t)
        return (beta * iet + beta_p) / (iet + 1.0)

    def gamma_act(z: complex) -> complex:
        return (a * z + c) / (b * z + d)

    z_minus = z_of_t(-0.5 * ell)
    z_plus = z_of_t(0.5 * ell)
    if abs(gamma_act(z_minus) - z_plus) < 1e-9 * max(1.0, abs(z_plus)):
        return beta, beta_p, -0.5 * ell, 0.5 * ell
    elif abs(gamma_act(z_plus) - z_minus) < 1e-9 * max(1.0, abs(z_minus)):
        return beta, beta_p, 0.5 * ell, -0.5 * ell
    else:
        raise RuntimeError(f"Geodesic period mismatch for M={M}")


def geodesic_quadrature(
    M: Mat2,
    integrand_fn,
    gl_nodes: Sequence[Tuple[float, float]],
) -> complex:
    beta, beta_p, t0, t1 = geodesic_arc_params(M)
    mid = 0.5 * (t0 + t1)
    half = 0.5 * (t1 - t0)
    span = beta - beta_p
    acc = 0j
    for xi, wi in gl_nodes:
        t = mid + half * xi
        et = math.exp(t)
        iet = 1j * et
        denom = iet + 1.0
        z = (beta * iet + beta_p) / denom
        dz_dt = (1j * et * span) / (denom * denom)
        acc += wi * integrand_fn(z) * dz_dt
    return half * acc


def dual_point_Jc(c_char: Frac2) -> Frac2:
    return (frac_part(-c_char[1]), frac_part(c_char[0]))


def z0_geodesic(M: Mat2, c_char: Frac2, gl_nodes: Sequence[Tuple[float, float]]) -> complex:
    jc = dual_point_Jc(c_char)
    period = geodesic_quadrature(M, lambda z: eval_G_shifted_star(z, jc), gl_nodes)
    return period / (4.0 * math.pi * math.pi)


def l_odd_quadrature(M: Mat2, c_char: Frac2, gl_nodes: Sequence[Tuple[float, float]]) -> complex:
    return geodesic_quadrature(M, lambda z: eval_G_twisted(z, c_char), gl_nodes)


def l_odd_siegel(M: Mat2, c_char: Frac2, z0: complex) -> complex:
    a, b = M[0]
    c, d = M[1]
    gz0 = (a * z0 + c) / (b * z0 + d)
    jc = dual_point_Jc(c_char)
    return -2j * math.pi * (eval_log_siegel(gz0, jc) - eval_log_siegel(z0, jc))


# ---------------------------------------------------------------------------
# Affine least-squares fit helper
# ---------------------------------------------------------------------------


def affine_fit(xs: Sequence[float], ys: Sequence[float]) -> Tuple[float, float, float, int]:
    """Fit y ~ slope * x + intercept. Returns (slope, intercept, max_abs_resid, n_distinct_x)."""
    assert len(xs) == len(ys) and len(xs) > 0
    # Count distinct x up to 1e-9
    sorted_x = sorted(xs)
    distinct_x = 1
    for k in range(1, len(sorted_x)):
        if abs(sorted_x[k] - sorted_x[k - 1]) > 1e-9:
            distinct_x += 1

    n = float(len(xs))
    mx = sum(xs) / n
    my = sum(ys) / n
    sxx = sum((x - mx) ** 2 for x in xs)
    sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    if sxx < 1e-24:
        slope = 0.0
        intercept = my
    else:
        slope = sxy / sxx
        intercept = my - slope * mx
    max_resid = max(abs(y - (slope * x + intercept)) for x, y in zip(xs, ys))
    return slope, intercept, max_resid, distinct_x


# ---------------------------------------------------------------------------
# Main execution
# ---------------------------------------------------------------------------


def main() -> None:
    t_start_wall = time.time()

    # 1. Literature benchmark gates G1, G2, G3
    M_bohn1: Mat2 = ((-2, 1), (1, -1))
    bohn1_inputs = [
        (Fraction(1, 5), Fraction(3, 5)),
        (Fraction(2, 5), Fraction(1, 5)),
        (Fraction(3, 5), Fraction(4, 5)),
        (Fraction(4, 5), Fraction(2, 5)),
    ]
    bohn1_expected = [Fraction(8, 5), Fraction(12, 5), Fraction(12, 5), Fraction(8, 5)]
    bohn1_thm = [rho_bohn_thm420(M_bohn1, nu) for nu in bohn1_inputs]
    bohn1_eq = [rho_bohn_eq467(M_bohn1, nu) for nu in bohn1_inputs]
    assert bohn1_thm == bohn1_expected and bohn1_eq == bohn1_expected

    M_bohn2: Mat2 = ((3, 2), (4, 3))
    bohn2_inputs = [
        (Fraction(0, 1), Fraction(1, 2)),
        (Fraction(1, 2), Fraction(0, 1)),
        (Fraction(1, 2), Fraction(1, 2)),
    ]
    bohn2_expected = [Fraction(0), Fraction(0), Fraction(1)]
    bohn2_thm = [rho_bohn_thm420(M_bohn2, nu) for nu in bohn2_inputs]
    bohn2_eq = [rho_bohn_eq467(M_bohn2, nu) for nu in bohn2_inputs]
    assert bohn2_thm == bohn2_expected and bohn2_eq == bohn2_expected

    in_sample_specs: List[Tuple[str, int, Fraction]] = [
        ("+LR", 2, Fraction(0)),
        ("+LR", 3, Fraction(0)),
        ("+LR", 4, Fraction(0)),
        ("+LR", 5, Fraction(0)),
        ("+LLR", 3, Fraction(1)),
        ("+LLLR", 3, Fraction(2)),
        ("+LLRLR", 2, Fraction(2, 3)),
        ("-LR", 1, Fraction(0)),
        ("-LR", 2, Fraction(0)),
        ("-LR", 3, Fraction(0)),
        ("-LR", 4, Fraction(0)),
        ("-LLRLR", 1, Fraction(1, 3)),
        ("-LLLRLR", 1, Fraction(2, 3)),
        ("-LLR", 2, Fraction(2, 3)),
        ("-LLR", 3, Fraction(1)),
        ("-LLRR", 1, Fraction(0)),
    ]

    conjugators: List[Mat2] = [((1, 1), (0, 1)), ((2, 1), (1, 1))]

    level_summaries = []
    total_chars = 0
    t1_pass = 0
    t2_pass = 0
    t3_pass = 0
    t4_pass = 0
    t4_tested = 0
    r2_fail_count = 0
    r3_fail_count = 0

    max_z0_w1_w2_diff = 0.0
    max_z0_shintani_geod_diff = 0.0
    max_z0_quad48_96_diff = 0.0
    letter_slope_checked = 0
    max_letter_slope_diff = 0.0

    max_lodd_quad48_96_diff = 0.0
    max_lodd_quad_siegel_diff = 0.0
    max_lodd_basepoint_diff = 0.0
    max_eta_identity_resid = 0.0
    exact_eta_identity_matches = 0

    # Planted controls counters on the 601 population
    p1_eta_flipped_breaks = 0
    p1_eta_zero_count = 0
    p2_permuted_breaks_levels = 0
    p3_no_untwisted_eta_breaks_levels = 0
    p3_no_untwisted_eta_breaks_chars = 0
    p4_jc_swap_breaks_chars = 0
    p4_jc_equal_chars = 0

    levels_ge3_distinct = 0
    levels_ge3_affine_pass = 0
    levels_ge3_affine_fail = 0

    dft_checks = []

    for sw, lv, expected_eta in in_sample_specs:
        label = f"{sw} {lv}"
        M, num_neg_i = word_level_matrix(sw, lv)
        M_inv = mat_inv_sl2(M)
        eta_M = eta_untwisted(M)
        assert eta_M == expected_eta, f"G3 failed on {label}: got {eta_M}, expected {expected_eta}"

        N, chars = enumerate_fixed_characters(M)
        tr = M[0][0] + M[1][1]
        disc = tr * tr - 4
        sqrt_D = math.sqrt(float(disc))

        xs_scaled: List[float] = []
        z0_vals: Dict[Frac2, float] = {}
        ys_rho: List[float] = []
        rho_fracs: List[Fraction] = []
        eta_A_map: Dict[Frac2, Fraction] = {}
        lodd_over_pi2_map: Dict[Frac2, float] = {}

        beta, beta_p, ts0, _ = geodesic_arc_params(M)
        iet0 = 1j * math.exp(ts0)
        z_base1 = (beta * iet0 + beta_p) / (iet0 + 1.0)
        z_base2 = (-M[1][1] + 0.13) / M[0][1] + 1j * (1.25 / abs(M[0][1]))

        lv_max_eta_resid = 0.0
        lv_max_z0_diff = 0.0
        denom_set = set()

        for c_char in chars:
            total_chars += 1
            nu: Frac2 = (-c_char[0], -c_char[1])
            rho_thm = rho_bohn_thm420(M, nu, "R1")
            rho_eq = rho_bohn_eq467(M, nu)
            if rho_thm == rho_eq:
                t1_pass += 1
            if rho_bohn_thm420(M, nu, "R2") != rho_eq:
                r2_fail_count += 1
            if rho_bohn_thm420(M, nu, "R3") != rho_eq:
                r3_fail_count += 1

            m1, m2 = bohn_m_vec(M, nu)
            cs_diff = rho_thm - 2 * (nu[1] * m1 - nu[0] * m2)
            if cs_diff.denominator == 1:
                t2_pass += 1

            rho_inv = rho_bohn_thm420(M_inv, nu, "R1")
            if rho_inv == -rho_thm:
                t3_pass += 1

            for P in conjugators:
                P_inv = mat_inv_sl2(P)
                M_conj = mat_mul(mat_mul(P, M), P_inv)
                if M_conj[1][0] != 0:
                    t4_tested += 1
                    # P^{-T} nu: P^{-1} = [[P11, -P01], [-P10, P00]], transpose = [[P11, -P10], [-P01, P00]]
                    nu_conj: Frac2 = (
                        P_inv[0][0] * nu[0] + P_inv[1][0] * nu[1],
                        P_inv[0][1] * nu[0] + P_inv[1][1] * nu[1],
                    )
                    if rho_bohn_thm420(M_conj, nu_conj, "R1") == rho_thm:
                        t4_pass += 1

            # Z(0, chi_c): Route A (two cone generators) & Route B (geodesic G^(Jc)*)
            w1, w2 = find_cone_generators(M, c_char, count=2)
            z0_a1 = z0_shintani(M, c_char, w1)
            z0_a2 = z0_shintani(M, c_char, w2)
            assert abs(z0_a1.imag) < 1e-11
            diff_w = abs(z0_a1 - z0_a2)
            max_z0_w1_w2_diff = max(max_z0_w1_w2_diff, diff_w)

            z0_b48 = z0_geodesic(M, c_char, GL_48)
            z0_b96 = z0_geodesic(M, c_char, GL_96)
            max_z0_quad48_96_diff = max(max_z0_quad48_96_diff, abs(z0_b48 - z0_b96))
            diff_ab = abs(z0_a1.real - z0_b96.real)
            max_z0_shintani_geod_diff = max(max_z0_shintani_geod_diff, diff_ab)
            lv_max_z0_diff = max(lv_max_z0_diff, diff_ab)

            ok_let, s_let = b1438_letter_slope(sw, lv, c_char)
            if ok_let:
                letter_slope_checked += 1
                max_letter_slope_diff = max(
                    max_letter_slope_diff, abs((s_let + 0.5 * num_neg_i) - z0_a1.real)
                )

            z0_val = z0_a1.real
            z0_vals[c_char] = z0_val
            xs_scaled.append(sqrt_D * z0_val)
            ys_rho.append(float(rho_thm))
            rho_fracs.append(rho_thm)

            # L_odd(1, chi_c): Route 1 (quadrature) & Route 2 (Siegel log increment)
            lodd_48 = l_odd_quadrature(M, c_char, GL_48)
            lodd_96 = l_odd_quadrature(M, c_char, GL_96)
            lodd_s1 = l_odd_siegel(M, c_char, z_base1)
            lodd_s2 = l_odd_siegel(M, c_char, z_base2)

            max_lodd_quad48_96_diff = max(max_lodd_quad48_96_diff, abs(lodd_48 - lodd_96))
            max_lodd_quad_siegel_diff = max(max_lodd_quad_siegel_diff, abs(lodd_96 - lodd_s1))
            max_lodd_basepoint_diff = max(max_lodd_basepoint_diff, abs(lodd_s1 - lodd_s2))

            eta_A = rho_thm + eta_M
            eta_A_map[c_char] = eta_A
            lodd_div_pi2 = (lodd_s1 / (math.pi * math.pi)).real
            assert abs(lodd_s1.imag) < 1e-11
            lodd_over_pi2_map[c_char] = lodd_div_pi2

            resid_eta = abs(float(eta_A) + lodd_div_pi2)
            max_eta_identity_resid = max(max_eta_identity_resid, resid_eta)
            lv_max_eta_resid = max(lv_max_eta_resid, resid_eta)

            approx_neg_lodd = Fraction(-lodd_div_pi2).limit_denominator(100000)
            if approx_neg_lodd == eta_A:
                exact_eta_identity_matches += 1
            denom_set.add((eta_A / 4).denominator)

            # Plant P1: orientation flip M -> M^{-1}
            eta_A_flipped = rho_inv + eta_untwisted(M_inv)
            assert eta_A_flipped == -eta_A
            if eta_A == 0:
                p1_eta_zero_count += 1
            else:
                if abs(float(eta_A_flipped) + lodd_div_pi2) > 1e-6:
                    p1_eta_flipped_breaks += 1

            # Plant P3: omitting untwisted eta(T^2_M)
            if abs(float(rho_thm) + lodd_div_pi2) > 1e-6:
                p3_no_untwisted_eta_breaks_chars += 1

        if eta_M != 0:
            p3_no_untwisted_eta_breaks_levels += 1

        # Plant P4: evaluate L_odd at Jc instead of c
        for c_char in chars:
            jc = dual_point_Jc(c_char)
            lodd_jc_div_pi2 = (l_odd_siegel(M, jc, z_base2) / (math.pi * math.pi)).real
            # Note: jc need not be fixed by M! Even stronger test; also compare with eta_A(-c)
            if abs(float(eta_A_map[c_char]) + lodd_jc_div_pi2) > 1e-6:
                p4_jc_swap_breaks_chars += 1
            else:
                p4_jc_equal_chars += 1

        slope_fit, intercept_fit, max_aff_resid, n_distinct_z0 = affine_fit(xs_scaled, ys_rho)
        if n_distinct_z0 >= 3:
            levels_ge3_distinct += 1
            if max_aff_resid <= 1e-9:
                levels_ge3_affine_pass += 1
            else:
                levels_ge3_affine_fail += 1

            # Plant P2: deterministic cyclic shift (by 1, or first shift not preserving x)
            n_c = len(xs_scaled)
            perm_broken = False
            for shift in range(1, n_c):
                xs_perm = xs_scaled[shift:] + xs_scaled[:shift]
                _, _, perm_resid, _ = affine_fit(xs_perm, ys_rho)
                if perm_resid > 1e-3:
                    perm_broken = True
                    break
            if perm_broken:
                p2_permuted_breaks_levels += 1

        # Symplectic 2D DFT check on principal congruence levels (M == I mod N, i.e. len(chars) == N^2 - 1)
        if len(chars) == N * N - 1:
            psi_over_12 = 0.25 * float(eta_M)  # since eta = Psi/3 => -Psi/12 = -eta/4
            z_triv = -psi_over_12
            max_dft_diff = 0.0
            two_pi_N = 2.0 * math.pi * N
            for c_char in chars:
                c1_f, c2_f = float(c_char[0]), float(c_char[1])
                acc_dft = z_triv
                for cp in chars:
                    cp1_f, cp2_f = float(cp[0]), float(cp[1])
                    # u = J(cp) = (-cp2, cp1), phase = exp(2*pi*i*N*(c1*u1 + c2*u2)) = exp(2*pi*i*N*(c2*cp1 - c1*cp2))
                    angle = two_pi_N * (c2_f * cp1_f - c1_f * cp2_f)
                    acc_dft += math.cos(angle) * z0_vals[cp]
                lhs = -0.25 * float(eta_A_map[c_char])
                rhs = acc_dft / float(N * N)
                max_dft_diff = max(max_dft_diff, abs(lhs - rhs))
            dft_checks.append(
                {
                    "level": label,
                    "N": N,
                    "num_chars": len(chars),
                    "max_symplectic_dft_diff": max_dft_diff,
                }
            )

        level_summaries.append(
            {
                "level": label,
                "M": [list(M[0]), list(M[1])],
                "N": N,
                "num_chars": len(chars),
                "eta_untwisted": f"{eta_M.numerator}/{eta_M.denominator}" if eta_M.denominator != 1 else str(eta_M.numerator),
                "distinct_z0_count": n_distinct_z0,
                "affine_slope_vs_sqrtD_z0": slope_fit,
                "affine_intercept": intercept_fit,
                "affine_max_resid": max_aff_resid,
                "affine_holds_1e9": max_aff_resid <= 1e-9,
                "max_z0_shintani_vs_geod_diff": lv_max_z0_diff,
                "max_eta_plus_lodd_pi2_resid": lv_max_eta_resid,
                "lodd_over_4pi2_denominators": sorted(denom_set),
            }
        )

    # 3. Fresh out-of-sample test suite (10 unseen matrices, 531 characters)
    fresh_specs: List[Tuple[str, Mat2]] = [
        ("+LR 6", word_level_matrix("+LR", 6)[0]),
        ("-LR 5", word_level_matrix("-LR", 5)[0]),
        ("+LLR 2", word_level_matrix("+LLR", 2)[0]),
        ("+LLLR 2", word_level_matrix("+LLLR", 2)[0]),
        ("+LLRR 2", word_level_matrix("+LLRR", 2)[0]),
        ("+LLLRLR 1", word_level_matrix("+LLLRLR", 1)[0]),
        ("-LLLR 1", word_level_matrix("-LLLR", 1)[0]),
        ("+LLLLR 1", word_level_matrix("+LLLLR", 1)[0]),
        ("Bohn_Ex1", M_bohn1),
        ("Bohn_Ex2", M_bohn2),
    ]

    fresh_total_chars = 0
    fresh_t1_pass = 0
    fresh_t2_pass = 0
    fresh_t3_pass = 0
    fresh_exact_eta_matches = 0
    fresh_max_eta_resid = 0.0
    fresh_max_quad_siegel_diff = 0.0
    fresh_p1_zero_count = 0
    fresh_p1_breaks = 0
    fresh_summaries = []

    for flabel, Mf in fresh_specs:
        Mf_inv = mat_inv_sl2(Mf)
        eta_Mf = eta_untwisted(Mf)
        Nf, fchars = enumerate_fixed_characters(Mf)
        z_fbase = (-Mf[1][1] + 0.11) / Mf[0][1] + 1j * (1.25 / abs(Mf[0][1]))
        lv_f_max_resid = 0.0
        lv_f_exact = 0
        for c_char in fchars:
            fresh_total_chars += 1
            nu = (-c_char[0], -c_char[1])
            r_thm = rho_bohn_thm420(Mf, nu, "R1")
            r_eq = rho_bohn_eq467(Mf, nu)
            if r_thm == r_eq:
                fresh_t1_pass += 1
            m1, m2 = bohn_m_vec(Mf, nu)
            if (r_thm - 2 * (nu[1] * m1 - nu[0] * m2)).denominator == 1:
                fresh_t2_pass += 1
            r_inv = rho_bohn_thm420(Mf_inv, nu, "R1")
            if r_inv == -r_thm:
                fresh_t3_pass += 1

            lodd_s = l_odd_siegel(Mf, c_char, z_fbase)
            lodd_q = l_odd_quadrature(Mf, c_char, GL_96)
            fresh_max_quad_siegel_diff = max(fresh_max_quad_siegel_diff, abs(lodd_s - lodd_q))

            eta_Af = r_thm + eta_Mf
            lodd_div_pi2 = (lodd_s / (math.pi * math.pi)).real
            resid = abs(float(eta_Af) + lodd_div_pi2)
            fresh_max_eta_resid = max(fresh_max_eta_resid, resid)
            lv_f_max_resid = max(lv_f_max_resid, resid)

            if Fraction(-lodd_div_pi2).limit_denominator(100000) == eta_Af:
                fresh_exact_eta_matches += 1
                lv_f_exact += 1

            if eta_Af == 0:
                fresh_p1_zero_count += 1
            else:
                if abs(float(-eta_Af) + lodd_div_pi2) > 1e-6:
                    fresh_p1_breaks += 1

        fresh_summaries.append(
            {
                "level": flabel,
                "M": [list(Mf[0]), list(Mf[1])],
                "N": Nf,
                "num_chars": len(fchars),
                "eta_untwisted": f"{eta_Mf.numerator}/{eta_Mf.denominator}" if eta_Mf.denominator != 1 else str(eta_Mf.numerator),
                "exact_eta_matches": lv_f_exact,
                "max_eta_plus_lodd_pi2_resid": lv_f_max_resid,
            }
        )

    out = {
        "card": "X-C9",
        "seat": "agy-exp",
        "elapsed_seconds": round(time.time() - t_start_wall, 3),
        "benchmark_gates": {
            "G1_bohn_example1_exact": [f"{x.numerator}/{x.denominator}" for x in bohn1_thm],
            "G2_bohn_example2_exact": [str(x.numerator) for x in bohn2_thm],
            "G3_untwisted_eta_all_16_levels_match": True,
        },
        "in_sample_601": {
            "num_levels": len(in_sample_specs),
            "total_characters": total_chars,
            "T1_thm420_equals_eq467": t1_pass,
            "T2_corollary421_mod_Z": t2_pass,
            "T3_orientation_oddness": t3_pass,
            "T4_sl2z_conjugation_pass": t4_pass,
            "T4_sl2z_conjugation_tested": t4_tested,
            "bracket_misreading_R2_failures": r2_fail_count,
            "bracket_misreading_R3_P5_failures": r3_fail_count,
            "z0_cross_checks": {
                "max_w1_vs_w2_cone_diff": max_z0_w1_w2_diff,
                "max_shintani_vs_geodesic_diff": max_z0_shintani_geod_diff,
                "max_geodesic_gl48_vs_gl96_diff": max_z0_quad48_96_diff,
                "b1438_letter_slope_checked": letter_slope_checked,
                "max_b1438_letter_slope_diff": max_letter_slope_diff,
            },
            "affine_fit_test_vs_sqrtD_z0": {
                "levels_with_ge3_distinct_z0": levels_ge3_distinct,
                "levels_affine_pass": levels_ge3_affine_pass,
                "levels_affine_fail": levels_ge3_affine_fail,
            },
            "twisted_eta_identity": {
                "exact_rational_matches": exact_eta_identity_matches,
                "max_abs_residual": max_eta_identity_resid,
                "max_lodd_gl48_vs_gl96_diff": max_lodd_quad48_96_diff,
                "max_lodd_quad_vs_siegel_diff": max_lodd_quad_siegel_diff,
                "max_lodd_siegel_basepoint_diff": max_lodd_basepoint_diff,
            },
            "symplectic_2d_dft_congruence_levels": dft_checks,
            "planted_controls": {
                "P1_orientation_flip_breaks": p1_eta_flipped_breaks,
                "P1_vanishing_eta_A_chars": p1_eta_zero_count,
                "P2_permuted_z0_breaks_levels": p2_permuted_breaks_levels,
                "P3_omit_untwisted_eta_breaks_levels": p3_no_untwisted_eta_breaks_levels,
                "P3_omit_untwisted_eta_breaks_chars": p3_no_untwisted_eta_breaks_chars,
                "P4_swap_c_with_Jc_breaks_chars": p4_jc_swap_breaks_chars,
                "P4_swap_c_with_Jc_equal_chars": p4_jc_equal_chars,
                "P5_bracket_misreading_R3_breaks_chars": r3_fail_count,
            },
            "levels": level_summaries,
        },
        "fresh_out_of_sample_531": {
            "num_levels": len(fresh_specs),
            "total_characters": fresh_total_chars,
            "T1_thm420_equals_eq467": fresh_t1_pass,
            "T2_corollary421_mod_Z": fresh_t2_pass,
            "T3_orientation_oddness": fresh_t3_pass,
            "exact_rational_eta_matches": fresh_exact_eta_matches,
            "max_abs_residual": fresh_max_eta_resid,
            "max_lodd_quad_vs_siegel_diff": fresh_max_quad_siegel_diff,
            "P1_orientation_flip_breaks": fresh_p1_breaks,
            "P1_vanishing_eta_A_chars": fresh_p1_zero_count,
            "levels": fresh_summaries,
        },
    }

    out_path = Path(__file__).resolve().parent / "verify_x_c9_out.json"
    out_path.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
