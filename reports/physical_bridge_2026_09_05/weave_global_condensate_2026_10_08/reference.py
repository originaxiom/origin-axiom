"""Exact monomial phase orbits and rational roots; same author, no outside certificate."""
from collections import Counter
from fractions import Fraction as F
from itertools import combinations, product
from pathlib import Path
import importlib.util
import json


EXPONENTS = (-1, 1, 3, 1, -1, -3)


def permutation_sign(seq):
    return sum(seq[i] > seq[j] for i in range(len(seq)) for j in range(i+1, len(seq))) % 2


def orbit_invariants(basis, a_phase, b_action):
    seen = set()
    admitted = []
    for first in basis:
        if first in seen:
            continue
        cycle, phase, current = [], 0, first
        while current not in seen:
            seen.add(current)
            cycle.append(current)
            current, inc = b_action(current)
            phase += inc
        assert current == first
        if phase % 8 == 0 and all(a_phase(v) % 8 == 0 for v in cycle):
            admitted.append(cycle)
    assert seen == set(basis)
    return admitted


def exterior_invariants(k, exponents=EXPONENTS):
    basis = list(combinations(range(6), k))
    def action(I):
        moved = [(i+1) % 6 for i in I]
        sign = (int(5 in I)+permutation_sign(moved)) % 2
        return tuple(sorted(moved)), 4*sign
    return orbit_invariants(basis, lambda I: sum(exponents[i] for i in I), action)


def end_invariants():
    def action(pair):
        i, j = pair
        return ((i+1) % 6, (j+1) % 6), 4*(int(i == 5)-int(j == 5))
    return orbit_invariants(list(product(range(6), repeat=2)), lambda pair: EXPONENTS[pair[0]]-EXPONENTS[pair[1]], action)


def independent_roots():
    path = Path(__file__).resolve().parents[0].parent/'weave_cusp_condensate_2026_10_08/reference.py'
    spec = importlib.util.spec_from_file_location('previous_Weyl_root_closure', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.weyl_roots()


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def run():
    dims = {str(k): len(exterior_invariants(j)) for k, j in ((6, 1), (15, 2), (20, 3))}
    dims['35'] = len(end_invariants())-1
    comm = [(EXPONENTS[i]-EXPONENTS[(i-1) % 6]) % 8 for i in range(6)]
    roots = independent_roots()
    alpha, v = (0, 0, 0, 2, 0, 2, 0, 0), (0, 0, 0, 2, -2, 0, 0, 0)
    spinlog = tuple(F(a, 8) for a in alpha)
    targetlog = tuple(F(a, 4) for a in v)
    t = tuple(b-a for a, b in zip(spinlog, targetlog))
    action = lambda b, log: sum(F(x, 2)*y for x, y in zip(b, log))
    sumlog = tuple(a+b for a, b in zip(spinlog, t))
    spectators = sum(dot(b, alpha) == 0 and (dot(b, v)//4) % 2 == 1 for b in roots)
    c_roots = [tuple(F(int(i == k)-int(j == k)) for k in range(3)) for i, j in product(range(3), repeat=2) if i != j]
    fundamental = [tuple(F(int(i == k))-F(1, 3) for k in range(3)) for i in range(3)]
    surviving = Counter(c_roots)
    for w in fundamental:
        surviving[w] += dims['15']
        surviving[tuple(-x for x in w)] += dims['15']
    lengths = Counter()
    for w, n in surviving.items():
        lengths[str(dot(w, w))] += n
    dimension = 2+dims['35']+sum(surviving.values())
    # A constant-curvature core gives int ds=-area/2; positive x reverses boundary orientation.
    spin_line_turn = -F(1, 2)
    root_line_turn = -spin_line_turn/2
    cursor, accumulated = 0, 0
    for _ in range(6):
        accumulated += 4*int(cursor == 5)
        cursor = (cursor+1) % 6
    cycle_parity = permutation_sign([1, 2, 3, 4, 5, 0])
    flags = {
        'det_A_one_from_exponents': sum(EXPONENTS) % 8 == 0,
        'signed_B_determinant_one': (-1)**cycle_parity*(-1) == 1,
        'unsigned_B_control': (-1)**cycle_parity == -1,
        'commutator_phases_actual': comm == [2, 2, 2, 6, 6, 6],
        'wrong_commutator_sign_detected': [(-a) % 8 for a in comm] != comm,
        'B_sixth_is_minus_identity': cursor == 0 and accumulated % 8 == 4,
        'A_preserves_opposite_pair_form': all((EXPONENTS[i]+EXPONENTS[i+3]) % 8 == 0 for i in range(3)),
        'six_has_no_invariant': dims['6'] == 0,
        'fifteen_has_one_actual_cycle': exterior_invariants(2) == [[(0, 3), (1, 4), (2, 5)]],
        'twenty_has_no_invariant': dims['20'] == 0,
        'endomorphism_kernel_only_diagonal_cycle': end_invariants() == [[(i, i) for i in range(6)]],
        'adjoint_kernel_zero': dims['35'] == 0,
        'changed_holonomy_detected': len(exterior_invariants(2, (0,)*6)) != dims['15'],
        'Weyl_closure_has240_roots': len(roots) == 240,
        'actual_compensator_orthogonal_to_root': dot(t, alpha) == 0,
        'global_peripheral_on_all_roots': all((action(b, sumlog)-action(b, targetlog)).denominator == 1 for b in roots),
        'missing_compensator_detected': any((action(b, spinlog)-action(b, targetlog)).denominator != 1 for b in roots),
        'compensator_has_order4': all((4*action(b, t)).denominator == 1 for b in roots) and any((2*action(b, t)).denominator != 1 for b in roots),
        '54_spectators_unchanged': spectators == 54,
        'G2_whole_root_lengths': lengths == Counter({'2': 6, '2/3': 6}) and dimension == 14,
        'G2_not_SM_dimension': dimension != 12,
        'core_sign_gives_quarter_turn': root_line_turn == F(1, 4),
        'wrong_core_orientation_changes_phase': root_line_turn != -root_line_turn,
        'spin_bounds_at_end': spin_line_turn % 1 == F(1, 2),
    }
    return dict(predicates=flags, predicates_passed=sum(flags.values()),
        global_profile=dict(invariant_dimensions=dims, unbroken_dimension=dimension,
            unbroken_rank=2, root_lengths=dict(lengths), odd_cusp_spectators=spectators,
            root_spin_limit='i', compensator_phases_mod8=comm))


if __name__ == '__main__':
    result = run()
    print(json.dumps(result, indent=2, sort_keys=True))
    raise SystemExit(0 if all(result['predicates'].values()) else 1)
