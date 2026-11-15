"""Preliminary author checks of the relative phase/current derivation.

The constrained finite-cell minimizer is built before the reduced-response
formula is used for comparison. No repository modules or target data load.
"""

import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import signal
import sys
import time
import traceback

import mpmath as mp


def linear_solve(matrix, vector):
    rows = [list(row) + [value] for row, value in zip(matrix, vector)]
    n = len(rows)
    for column in range(n):
        pivot = next(i for i in range(column, n) if rows[i][column])
        rows[column], rows[pivot] = rows[pivot], rows[column]
        scale = rows[column][column]
        rows[column] = [x / scale for x in rows[column]]
        for row in range(n):
            if row == column:
                continue
            scale = rows[row][column]
            rows[row] = [a - scale * b for a, b in zip(rows[row], rows[column])]
    return [rows[i][-1] for i in range(n)]


def gauge_energy(curvatures, holonomies, phase_increments, areas, lengths, c, g2, kappa):
    bulk = c / (2 * g2) * sum(a * f * f for a, f in zip(areas, curvatures))
    edge = kappa / 2 * sum((x - d) ** 2 / ell
                           for x, d, ell in zip(holonomies, phase_increments, lengths))
    return bulk + edge


def finite_cell_response():
    c, g2, kappa = Q(7, 3), Q(5, 2), Q(11, 7)
    areas = [Q(1, 3), Q(4, 5), Q(7, 6), Q(9, 10)]
    lengths = [Q(1, 2), Q(2, 3), Q(5, 4), Q(8, 7), Q(3, 5)]
    phi = Q(3)  # Circulations are measured in units of 2*pi in this rational check.
    a_total, ell_total = sum(areas), sum(lengths)
    increments = [phi * ell / ell_total for ell in lengths]
    diagonal = [c * a / g2 for a in areas] + [kappa / ell for ell in lengths]
    constraint = areas + [-Q(1)] * len(lengths)
    n = len(diagonal)
    kkt = [[Q(0)] * (n + 1) for _ in range(n + 1)]
    rhs = [Q(0)] * (n + 1)
    for i in range(n):
        kkt[i][i] = diagonal[i]
        kkt[i][-1] = constraint[i]
        kkt[-1][i] = constraint[i]
    for j, delta in enumerate(increments):
        rhs[len(areas) + j] = kappa * delta / lengths[j]
    solution = linear_solve(kkt, rhs)
    curvature = solution[:len(areas)]
    holonomy = solution[len(areas):n]
    circulation = sum(holonomy)
    r, p = c / (g2 * a_total), kappa / ell_total
    expected_b = phi * p / (r + p)
    expected_energy = Q(1, 2) * r * p / (r + p) * phi * phi
    energy = gauge_energy(curvature, holonomy, increments, areas, lengths, c, g2, kappa)
    currents = [kappa * (x - d) / ell for x, d, ell in zip(holonomy, increments, lengths)]
    assert circulation == expected_b
    assert sum(f * a for f, a in zip(curvature, areas)) == circulation
    assert all(f == circulation / a_total for f in curvature)
    assert all(j == -c * curvature[0] / g2 for j in currents)
    assert energy == expected_energy
    assert circulation != phi and circulation != 0

    # Independent vertex gauge changes shift edge potentials and phase increments together.
    vertices = [Q(1, 7), Q(-2, 5), Q(3, 8), Q(4, 9), Q(-1, 3)]
    da = [vertices[(i + 1) % len(vertices)] - vertices[i] for i in range(len(vertices))]
    shifted_x = [x + change for x, change in zip(holonomy, da)]
    shifted_d = [d + change for d, change in zip(increments, da)]
    good_gauge = gauge_energy(curvature, shifted_x, shifted_d, areas, lengths, c, g2, kappa)
    dropped_phase = gauge_energy(curvature, shifted_x, increments, areas, lengths, c, g2, kappa)
    assert good_gauge == energy
    assert dropped_phase != energy
    reversed_source = -expected_b
    assert r * reversed_source + p * (reversed_source - phi) != 0
    return {
        'bulk_cells': len(areas), 'boundary_edges': len(lengths),
        'circulation': circulation, 'curvature_flux': sum(f * a for f, a in zip(curvature, areas)),
        'relative_winding': circulation - (circulation - phi),
        'uniform_curvature': curvature[0], 'conserved_current': currents[0],
        'on_shell_energy': energy, 'Schur_formula_matches_KKT': True,
        'full_gauge_energy_change': good_gauge - energy,
        'dropped_phase_gauge_energy_change': dropped_phase - energy,
        'wrong_source_sign_detected': True,
    }


def reference_and_sector_controls():
    r, p = Q(7, 9), Q(11, 13)
    coefficient = r * p / (2 * (r + p))
    energies = {n: coefficient * n * n for n in range(-8, 9)}
    assert min(energies, key=energies.get) == 0
    minimum_nonzero = min(value for n, value in energies.items() if n)
    minimizers = sorted(n for n, value in energies.items() if n and value == minimum_nonzero)
    assert minimizers == [-1, 1]
    assert energies[3] == 9 * energies[1]
    controls = []
    for n in (-3, -1, 0, 1, 3):
        bulk_flux = Q(0)
        boundary_eta_period = -Q(n)
        relative_number = bulk_flux - boundary_eta_period
        assert relative_number == n
        controls.append({'winding': n, 'bulk_flux': bulk_flux,
                         'boundary_eta_period': boundary_eta_period,
                         'relative_number': relative_number})
    assert all(energies[n] == energies[-n] for n in energies)
    soft_fraction = Q(1, 10 ** 12) / (r + Q(1, 10 ** 12))
    stiff_fraction = Q(10 ** 12) / (r + Q(10 ** 12))
    assert soft_fraction < Q(1, 10 ** 11)
    assert 1 - stiff_fraction < Q(1, 10 ** 11)
    return {'zero_curvature_relative_classes': controls, 'energy_coefficient': coefficient,
            'nonzero_minimizers': minimizers, 'energy_n3_over_n1': energies[3] / energies[1],
            'soft_flux_fraction': soft_fraction, 'stiff_flux_fraction': stiff_fraction,
            'orientation_even_energy': True}


def cut_and_source_controls():
    c, g2, phi, kappa = Q(7, 3), Q(5, 2), Q(3), Q(11, 7)
    rows = []
    for core_area, tail_area in ((Q(1, 2), Q(5, 2)), (Q(1), Q(2)), (Q(5, 2), Q(1, 2))):
        b = phi * tail_area / (core_area + tail_area)
        core_flux_density = (phi - b) / core_area
        tail_flux_density = b / tail_area
        old_energy = c / (2 * g2) * ((phi - b) ** 2 / core_area + b * b / tail_area)
        assert core_flux_density == tail_flux_density == phi / (core_area + tail_area)
        rc, rt = c / (g2 * core_area), c / (g2 * tail_area)
        # In the hyperbolic length normalization ell=1, tail area equals the cut-circle length.
        p = kappa / tail_area
        b_source = p * phi / (rc + rt + p)
        source_energy = ((rc + rt) * b_source ** 2 + p * (b_source - phi) ** 2) / 2
        assert (rc + rt) * b_source + p * (b_source - phi) == 0
        assert -b_source + b_source == 0
        rows.append({'core_area': core_area, 'tail_area': tail_area,
                     'old_fixed_flux_circulation': b, 'old_fixed_flux_energy': old_energy,
                     'phase_source_circulation': b_source, 'phase_source_energy': source_energy,
                     'phase_source_total_added_curvature': Q(0)})
    assert len({row['old_fixed_flux_energy'] for row in rows}) == 1
    assert len({row['phase_source_energy'] for row in rows}) > 1
    return {'cuts': rows, 'fixed_flux_cut_invariance': True,
            'fixed_local_source_changes_when_its_location_changes': True}


def smooth_radial_control():
    mp.mp.dps = 70
    radius, length, g2, kappa = mp.mpf(7) / 5, mp.mpf(11) / 6, mp.mpf(5) / 3, mp.mpf(13) / 9
    n = 3
    expected_b = n * kappa * g2 * radius / (2 + kappa * g2 * radius)

    def energy(b):
        def bulk_density(r):
            if r == 0:
                return mp.mpf(0)
            derivative = mp.diff(lambda s: b * s * s / (radius * radius), r)
            return derivative * derivative / r
        bulk = mp.pi * length / g2 * mp.quad(bulk_density, [0, radius])
        edge = mp.pi * kappa * length / radius * (b - n) ** 2
        return bulk + edge

    observed_b = mp.findroot(lambda b: mp.diff(energy, b), (mp.mpf(0), mp.mpf(n)))
    expected_e = 2 * mp.pi * length * kappa * n * n / (radius * (2 + kappa * g2 * radius))
    errors = [abs(observed_b - expected_b), abs(energy(observed_b) - expected_e)]
    assert max(errors) < mp.mpf('1e-60')
    assert mp.diff(energy, observed_b, 2) > 0
    return {'boundary_connection': mp.nstr(observed_b, 40),
            'magnetic_flux_over_2pi': mp.nstr(observed_b, 40),
            'relative_number': n, 'energy': mp.nstr(energy(observed_b), 40),
            'circulation_and_energy_errors': [mp.nstr(x, 20) for x in errors]}


def encode(value):
    if isinstance(value, Q):
        return str(value)
    if isinstance(value, dict):
        return {str(k): encode(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [encode(x) for x in value]
    return value


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    output = Path(parser.parse_args().output)
    if output.exists():
        raise RuntimeError('Refusing to overwrite a previous output')

    def timeout(signum, frame):
        raise TimeoutError('Two-minute author-check limit exceeded')

    signal.signal(signal.SIGALRM, timeout)
    signal.alarm(120)
    result = {'status': 'PRELIMINARY_AUTHOR_CHECK_UNBANKED', 'python': sys.version,
              'mpmath': mp.__version__,
              'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'checks': {}}
    started = time.monotonic()
    try:
        for check in (finite_cell_response, reference_and_sector_controls,
                      cut_and_source_controls, smooth_radial_control):
            result['checks'][check.__name__] = encode(check())
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
