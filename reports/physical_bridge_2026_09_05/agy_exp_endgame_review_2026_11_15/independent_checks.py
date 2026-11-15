"""Bounded mathematical checks, implemented independently of the reviewed code.

Source definitions are pinned by CARD.md and SOURCE_RECEIPT.json. This file
imports no OA modules and computes no comparison with physical target data.
"""

import argparse
from collections import Counter
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path
import signal
import sys
import time
import traceback

import mpmath as mp


M = ((2, 1), (1, 1))
J = ((1, 1), (1, 0))
IDENTITY = ((1, 0), (0, 1))
NEGATIVE_IDENTITY = ((-1, 0), (0, -1))


def multiply(a, b):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(2))
                       for j in range(2)) for i in range(2))


def power(a, n):
    result = IDENTITY
    for _ in range(n):
        result = multiply(result, a)
    return result


def determinant(a):
    return a[0][0] * a[1][1] - a[0][1] * a[1][0]


def rational_rank(rows):
    work = [[Fraction(x) for x in row] for row in rows]
    pivot_row = 0
    for column in range(len(work[0])):
        pivot = next((i for i in range(pivot_row, len(work)) if work[i][column]), None)
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        scale = work[pivot_row][column]
        work[pivot_row] = [x / scale for x in work[pivot_row]]
        for i in range(len(work)):
            if i != pivot_row:
                coefficient = work[i][column]
                work[i] = [a - coefficient * b
                           for a, b in zip(work[i], work[pivot_row])]
        pivot_row += 1
        if pivot_row == len(work):
            break
    return pivot_row


def matrix_order(a, modulus):
    for n in range(1, 100):
        p = power(a, n)
        if all((p[i][j] - IDENTITY[i][j]) % modulus == 0
               for i in range(2) for j in range(2)):
            return n
    raise AssertionError("Matrix order exceeded the declared bound")


def act(point, a, denominator):
    return tuple(sum(point[k] * a[k][j] for k in range(2)) % denominator
                 for j in range(2))


def orbit_count(points, generators, denominator):
    remaining = set(points)
    sizes = []
    while remaining:
        first = min(remaining)
        orbit, stack = {first}, [first]
        while stack:
            point = stack.pop()
            for generator in generators:
                nxt = act(point, generator, denominator)
                if nxt not in orbit:
                    orbit.add(nxt)
                    stack.append(nxt)
        assert orbit <= set(points)
        remaining -= orbit
        sizes.append(len(orbit))
    return sorted(sizes)


def exact_topology_and_orbits():
    # The graph spine of a punctured torus has two 1-cells and no 2-cell.
    # Its mapping-torus boundary C2 -> C1 is (M-I) with a zero base row.
    boundary = tuple(tuple(M[i][j] - IDENTITY[i][j] for j in range(2))
                     for i in range(2))
    det_boundary = determinant(boundary)
    assert det_boundary == -1
    assert math.gcd(*(abs(x) for row in boundary for x in row)) == 1
    # A unimodular boundary is injective and its image is the fibre Z^2.
    punctured_d2 = [list(row) for row in boundary] + [[0, 0]]
    rank_d2 = rational_rank(punctured_d2)
    punctured_h2_rank = 2 - rank_d2
    punctured_h1_free_rank = 3 - rank_d2
    punctured_h1_torsion_order = abs(det_boundary)
    # Closing the fibre adds its invariant 2-cell and one mapping-torus 3-cell.
    closed_d2 = [row + [0] for row in punctured_d2]
    closed_d3 = [[0], [0], [determinant(M) - 1]]
    closed_fibre_h2_rank = 3 - rational_rank(closed_d2) - rational_rank(closed_d3)
    singular_control = tuple(tuple(IDENTITY[i][j] - IDENTITY[i][j]
                                  for j in range(2)) for i in range(2))
    assert determinant(singular_control) == 0
    control_d2 = [list(row) for row in singular_control] + [[0, 0]]
    assert 2 - rational_rank(control_d2) == 2
    assert punctured_h2_rank == 0 and closed_fibre_h2_rank == 1

    pts3 = {(a, b) for a in range(3) for b in range(3)} - {(0, 0)}
    m_orbits3 = orbit_count(pts3, [M], 3)
    j_orbits3 = orbit_count(pts3, [J], 3)
    assert matrix_order(M, 3) == 4 and matrix_order(J, 3) == 8
    assert m_orbits3 == [4, 4] and j_orbits3 == [8]

    denominator = 45
    fixed4 = {(a, b) for a in range(denominator) for b in range(denominator)
              if act((a, b), power(M, 4), denominator) == (a, b)}

    def point_order(p):
        return math.lcm(*(denominator // math.gcd(x, denominator) for x in p))

    counts = Counter(point_order(p) for p in fixed4)
    assert counts == {1: 1, 3: 8, 5: 4, 15: 32}
    o32 = {p for p in fixed4 if point_order(p) == 15}
    groups = [[M], [J], [M, NEGATIVE_IDENTITY],
              [J, NEGATIVE_IDENTITY], [NEGATIVE_IDENTITY]]
    counts32 = [len(orbit_count(o32, generators, denominator))
                for generators in groups]
    assert counts32 == [8, 4, 4, 2, 16]
    fixed2 = {p for p in fixed4 if act(p, power(M, 2), denominator) == p}
    assert len(fixed2) == 5
    return {
        "punctured_mapping_torus_boundary": boundary,
        "boundary_determinant": det_boundary,
        "punctured_H2_rank": punctured_h2_rank,
        "punctured_H1_free_rank": punctured_h1_free_rank,
        "punctured_H1_torsion_order": punctured_h1_torsion_order,
        "ordinary_H2_cohomology_rank_by_UCT": punctured_h2_rank,
        "closed_fibre_H2_rank": closed_fibre_h2_rank,
        "mod3_orders_M_J": [matrix_order(M, 3), matrix_order(J, 3)],
        "mod3_M_orbit_sizes": m_orbits3,
        "mod3_J_orbit_sizes": j_orbits3,
        "fixed4_orders": dict(counts),
        "O32_orbit_counts": counts32,
        "degree2_fixed_point_count": len(fixed2),
    }


def frac(n, d=1):
    return mp.mpf(n) / d


def norm(a):
    return mp.sqrt(sum(abs(x) ** 2 for x in a))


def trace(a):
    return sum(a[i, i] for i in range(a.rows))


def weil_order():
    t = mp.diag([mp.exp(mp.pi * mp.j * frac((2 * r + 1) ** 2, 12))
                 for r in range(3)])
    omega = mp.exp(2 * mp.pi * mp.j / 3)
    s = mp.matrix(3)
    for r in range(3):
        for c in range(3):
            s[r, c] = mp.exp(-mp.pi * mp.j / 6) * omega ** (-(r + 1) * c) / mp.sqrt(3)
    u = t * s.H * t.H * s
    errors = [norm(u ** 4 - mp.eye(3)), abs(mp.det(u) - 1),
              abs(trace(u) - 1), abs(trace(u ** 2) + 1)]
    assert max(errors) < mp.mpf('1e-65')
    assert norm(u ** 2 - mp.eye(3)) > 2
    return {"unitary_order_four_residual": errors[0],
            "determinant_residual": errors[1],
            "trace_residual": errors[2],
            "square_trace_residual": errors[3]}


def eisenstein(tau):
    q = mp.exp(2 * mp.pi * mp.j * tau)
    # Divisor-sum q-series, distinct from the reviewed Lambert-sum route.
    sums = []
    for weight in (1, 3, 5):
        sums.append(mp.fsum(sum(d ** weight for d in range(1, n + 1) if n % d == 0)
                            * q ** n for n in range(1, 181)))
    return 1 - 24 * sums[0], 1 + 240 * sums[1], 1 - 504 * sums[2]


def majorana_terms(tau):
    e2, e4, e6 = eisenstein(tau)
    y = mp.im(tau)
    v, w, u = mp.matrix(3, 1), mp.matrix(3, 1), mp.matrix(3, 1)
    for j in range(3):
        terms = []
        for n in range(-20, 21):
            a = frac(6 * n + 2 * j + 1, 6)
            theta_term = mp.exp(3 * mp.pi * mp.j * (tau * a * a + a))
            derivative_term = 3 * mp.j * a * theta_term
            terms.append((theta_term, derivative_term,
                          (frac(3, 2) * a * a - e2 / 8) * derivative_term))
        v[j] = y ** frac(1, 4) * mp.conj(mp.fsum(t[0] for t in terms))
        w[j] = y ** frac(3, 4) * mp.conj(mp.fsum(t[1] for t in terms))
        u[j] = y ** frac(7, 4) * mp.conj(mp.fsum(t[2] for t in terms))
    return [y ** 3 * mp.conj(e6) * (v * v.T),
            y ** 2 * mp.conj(e4) * (w * w.T), u * u.T]


def singular_ratios(a):
    values = sorted(max(mp.mpf(0), x) for x in mp.eighe(a * a.H, eigvals_only=True))
    return [mp.sqrt(values[0] / values[2]), mp.sqrt(values[1] / values[2])]


def majorana_coefficient_freedom():
    tau = frac(17, 100) + mp.j * frac(143, 100)
    variants = [(1, 1, 1), (2, 1, 1), (1, 2, 1), (1, 1, 2)]
    t = mp.diag([mp.exp(mp.pi * mp.j * frac((2 * r + 1) ** 2, 12))
                 for r in range(3)])
    omega = mp.exp(2 * mp.pi * mp.j / 3)
    s = mp.matrix([[omega ** ((r - 1) * (c - 1)) / mp.sqrt(3)
                    for c in range(3)] for r in range(3)])
    terms = majorana_terms(tau)
    terms_t = majorana_terms(tau + 1)
    terms_s = majorana_terms(-1 / tau)
    scalar = -mp.j * (mp.conj(tau) / abs(tau)) ** 7
    results = []
    for weights in variants:
        a = sum((w * component for w, component in zip(weights, terms)), mp.zeros(3))
        at = sum((w * component for w, component in zip(weights, terms_t)), mp.zeros(3))
        ass = sum((w * component for w, component in zip(weights, terms_s)), mp.zeros(3))
        err_t = norm(at - t.conjugate() * a * t.H) / norm(a)
        err_s = norm(ass - scalar * s.conjugate() * a * s.H) / norm(a)
        assert max(err_t, err_s) < mp.mpf('1e-60')
        assert norm(a - a.T) < mp.mpf('1e-65')
        results.append({"coefficients": weights, "T_error": err_t,
                        "S_error": err_s, "singular_ratios": singular_ratios(a)})
    ratio_shift = max(abs(x - y) for result in results[1:]
                      for x, y in zip(result['singular_ratios'], results[0]['singular_ratios']))
    assert ratio_shift > mp.mpf('1e-4')
    star_terms = majorana_terms(2 * mp.sqrt(3) * mp.j)
    rank2 = star_terms[0] + star_terms[1]
    full = rank2 + star_terms[2]
    rank2_ratio = singular_ratios(rank2)[0]
    assert rank2_ratio < mp.mpf('1e-30')
    return {"variants": results, "max_ratio_shift": ratio_shift,
            "cusp_baseline_ratios": singular_ratios(full),
            "rank_two_control_smallest_ratio": rank2_ratio}


def ordered_yukawa_products():
    yu = mp.diag([frac(1, 5), frac(2, 5), frac(4, 5)])
    rotation = mp.matrix([[1, 0, 0], [0, frac(3, 5), 4 * mp.j / 5],
                          [0, 4 * mp.j / 5, frac(3, 5)]])
    yd = rotation * mp.diag([frac(1, 7), frac(1, 3), frac(2, 3)])
    hu, hd = yu * yu.H, yd * yd.H
    comm = hu * hd - hd * hu
    # Luo-Xiao beta_H = H*A. The left convention is Y=H^dagger.
    right_u = yu.H * (-hu * hd - hd * hu / 4)
    right_d = yd.H * (-hd * hu - hu * hd / 4)
    correct_u, correct_d = right_u.H, right_d.H
    agy_u = (-hu * hd - hd * hu / 4) * yu
    agy_d = (-hd * hu - hu * hd / 4) * yd
    delta_u, delta_d = correct_u - agy_u, correct_d - agy_d
    assert norm(delta_u - frac(3, 4) * comm * yu) < mp.mpf('1e-70')
    assert norm(delta_d + frac(3, 4) * comm * yd) < mp.mpf('1e-70')
    du_h = delta_u * yu.H + yu * delta_u.H
    dd_h = delta_d * yd.H + yd * delta_d.H
    mixed_shift = trace(du_h * hd + hu * dd_h)
    exact_mixed_shift = frac(3, 2) * trace(comm * comm)
    assert abs(mixed_shift - exact_mixed_shift) < mp.mpf('1e-70')
    assert abs(mixed_shift) > mp.mpf('1e-4')
    commuting_hd = mp.diag([frac(1, 49), frac(1, 9), frac(4, 9)])
    assert norm(hu * commuting_hd - commuting_hd * hu) == 0
    return {"commutator_norm": norm(comm),
            "up_order_error_norm": norm(delta_u),
            "down_order_error_norm": norm(delta_d),
            "mixed_invariant_derivative_shift_without_loop_factor": mixed_shift,
            "exact_shift_residual": abs(mixed_shift - exact_mixed_shift),
            "diagonal_control_hides_error": True}


def rank_one_two_loop_mixing():
    yt, yb, ye = frac(9, 10), frac(1, 2), frac(3, 10)
    g1, g2, g3 = frac(45, 100), frac(65, 100), frac(115, 100)
    theta = frac(1, 4)
    c, s = mp.cos(theta), mp.sin(theta)
    yu = mp.diag([0, yt])
    rotation = mp.matrix([[c, s], [-s, c]])
    yd = rotation * mp.diag([0, yb])
    hu, hd = yu * yu.H, yd * yd.H
    common = frac(5, 4) * (3 * yt ** 2 + 3 * yb ** 2 + ye ** 2)
    bu = common - frac(43, 80) * g1 ** 2 + frac(9, 16) * g2 ** 2 - 16 * g3 ** 2
    bd = common - frac(79, 80) * g1 ** 2 + frac(9, 16) * g2 ** 2 - 16 * g3 ** 2

    def dlog(correct):
        d, e = (frac(-1, 4), -1) if correct else (-1, frac(-1, 4))
        du = (d * hu * hd + e * hd * hu + frac(11, 4) * hd ** 2 + bu * hd) * yu
        dd = (d * hd * hu + e * hu * hd + frac(11, 4) * hu ** 2 + bd * hu) * yd
        dhu = du * yu.H + yu * du.H
        dhd = dd * yd.H + yd * dd.H
        alpha_u = dhu[0, 1] / yt ** 2
        alpha_d = (rotation.H * dhd * rotation)[0, 1] / yb ** 2
        return (c / s) * (alpha_d - alpha_u)

    def analytic(mixed_coefficient):
        b = (frac(13, 2) * (yt ** 4 + yb ** 4)
             + mixed_coefficient * yt ** 2 * yb ** 2
             + frac(5, 4) * ye ** 2 * (yt ** 2 + yb ** 2)
             - 16 * g3 ** 2 * (yt ** 2 + yb ** 2)
             + frac(9, 16) * g2 ** 2 * (yt ** 2 + yb ** 2)
             - frac(79, 80) * g1 ** 2 * yt ** 2
             - frac(43, 80) * g1 ** 2 * yb ** 2)
        return -c ** 2 * b

    actual_correct, actual_agy = dlog(True), dlog(False)
    residuals = [abs(actual_correct - analytic(frac(11, 2))),
                 abs(actual_agy - analytic(7)),
                 abs(actual_correct - actual_agy - frac(3, 2) * c ** 2 * yt ** 2 * yb ** 2)]
    assert max(residuals) < mp.mpf('1e-65')
    return {"primary_converted_mixed_coefficient": '11/2',
            "campaign_mixed_coefficient": 7,
            "correct_pure_two_loop_dlog_without_loop_factor": actual_correct,
            "campaign_pure_two_loop_dlog_without_loop_factor": actual_agy,
            "difference_after_two_loop_factor": (actual_correct - actual_agy) / (16 * mp.pi ** 2) ** 2,
            "identity_residuals": residuals}


def gluing_area_and_collar():
    # Independent root and tangent equations. No imported geometry producer.
    z = mp.findroot(lambda v: v * v - v + 1, (frac(1, 3) + mp.j,
                                             frac(2, 3) + mp.j))

    def second_shape(first):
        roots = [(1 + sign * mp.sqrt(1 + 4 / (first * (first - 1)))) / 2
                 for sign in (-1, 1)]
        return max(roots, key=mp.im)

    def volume(x, y):
        first = mp.mpc(x, y)
        return sum(mp.im(mp.polylog(2, v)) + mp.arg(1 - v) * mp.log(abs(v))
                   for v in (first, second_shape(first)))

    other = second_shape(z)
    tangent = -(2 * z - 1) * other * (other - 1) / (z * (z - 1) * (2 * other - 1))
    du = tangent / other - 1 / (1 - z)
    dv = 2 / z - 2 / (1 - z)
    tau = dv / du
    gradient = [mp.diff(lambda x: volume(x, mp.im(z)), mp.re(z)),
                mp.diff(lambda y: volume(mp.re(z), y), mp.im(z))]
    hxx = -mp.diff(lambda x: volume(x, mp.im(z)), mp.re(z), 2)
    hyy = -mp.diff(lambda y: volume(mp.re(z), y), mp.im(z), 2)
    assert abs(z * (z - 1) * other * (other - 1) - 1) < mp.mpf('1e-65')
    assert max(abs(x) for x in gradient) < mp.mpf('1e-60')
    assert max(abs(hxx - mp.sqrt(3)), abs(hyy - mp.sqrt(3))) < mp.mpf('1e-60')
    assert abs(tau - 2 * mp.sqrt(3) * mp.j) < mp.mpf('1e-65')
    area_values = {}
    for coefficient in (Fraction(1, 4), Fraction(1, 2), Fraction(1)):
        cv = frac(coefficient.numerator, coefficient.denominator)
        area = mp.sqrt(2 * mp.pi ** 2 * 9 / cv)
        derivative = cv - 2 * mp.pi ** 2 * 9 / area ** 2
        assert abs(derivative) < mp.mpf('1e-70')
        area_values[str(coefficient)] = area
    length = mp.im(tau)

    def boundary_amplitude(kappa):
        integral = mp.quad(lambda t: mp.exp(2 * kappa * t), [0, length])
        return mp.exp(kappa * length) / mp.sqrt(integral)

    collar_ratio = boundary_amplitude(1) / boundary_amplitude(-1)
    assert abs(collar_ratio / mp.exp(length) - 1) < mp.mpf('1e-65')
    return {"tetrahedron_shape": z, "volume": volume(mp.re(z), mp.im(z)),
            "cusp_derivative": tau, "gradient": gradient,
            "negative_volume_Hessian_diagonal": [hxx, hyy],
            "classical_area_by_coefficient": area_values,
            "collar_plus_to_minus_ratio": collar_ratio,
            "collar_identity_residual": abs(collar_ratio / mp.exp(length) - 1)}


def serializable(value):
    if isinstance(value, dict):
        return {str(k): serializable(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [serializable(v) for v in value]
    if isinstance(value, (str, bool, int)) or value is None:
        return value
    if isinstance(value, mp.mpc):
        return {"real": mp.nstr(mp.re(value), 45), "imag": mp.nstr(mp.im(value), 45)}
    return mp.nstr(value, 45)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    output = Path(args.output)
    if output.exists():
        raise RuntimeError('Refusing to overwrite a previous output')
    mp.mp.dps = 80
    def timed_out(signum, frame):
        raise TimeoutError('Independent checks exceeded two minutes')

    signal.signal(signal.SIGALRM, timed_out)
    signal.alarm(120)
    result = {'state': 'PRELIMINARY_INDEPENDENT_MATHEMATICAL_CHECKS_UNBANKED',
              'python': sys.version, 'mpmath': mp.__version__, 'working_digits': mp.mp.dps,
              'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'checks': {}}
    started = time.monotonic()
    checks = [exact_topology_and_orbits, weil_order, majorana_coefficient_freedom,
              ordered_yukawa_products, rank_one_two_loop_mixing, gluing_area_and_collar]
    try:
        for check in checks:
            result['checks'][check.__name__] = serializable(check())
            output.write_text(json.dumps(result, indent=2) + '\n')
        result['completed'] = True
    except BaseException:
        result['completed'] = False
        result['first_exception'] = traceback.format_exc()
        raise
    finally:
        result['seconds'] = time.monotonic() - started
        output.write_text(json.dumps(result, indent=2) + '\n')


if __name__ == '__main__':
    main()
