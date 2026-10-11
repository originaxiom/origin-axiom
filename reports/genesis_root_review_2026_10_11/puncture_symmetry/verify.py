#!/usr/bin/env python3
"""Exact safeguards; execute only after the preregistration and seal.

Scope: the W24/W28 local coefficient representation, a conditional doubled
Green-data model, and the conditional matrix-conjugation action. This does
not test a global PDE, the E8 embedding, the physical index dictionary,
or selection of a cusp sector.
"""
import json
import sympy as s


def clean(m):
    return m.applyfunc(s.simplify)


def same(a, b):
    return clean(a - b) == s.zeros(a.rows, a.cols)


def unit(n, i, j):
    m = s.zeros(n)
    m[i, j] = 1
    return m


def commutant(ops):
    n = ops[0].rows
    xs = s.symbols(f'c0:{n*n}')
    k = s.Matrix(n, n, xs)
    equations = [s.expand(e) for op in ops for e in k * op - op * k]
    matrix, rhs = s.linear_eq_to_matrix(equations, xs)
    assert rhs == s.zeros(rhs.rows, 1)
    return [s.Matrix(n, n, tuple(v)) for v in matrix.nullspace()]


def required_check_names():
    """Independent inventory: an omitted computation must not make a pass.

    Expected kernel basis counts are part of the preregistered predictions,
    not inferred from the number of checks that happened to execute.
    """
    names = {
        'L_square', 'R_square', 'quaternion_commutator', 'Phi_unitary',
        'Phi_untwists_a', 'Phi_untwists_b', 'move_commutant_dimension_two',
        'D_flat_flavour_map', 'D_involutive_unitary', 'D_special_unitary',
        'D_commutes_with_holonomies', 'D_mixes_puncture_pieces',
        'D_nonzero_commutator_block', 'enlarged_commutant_scalar',
        'scalar_phase_does_not_select', 'Green_form_nondegenerate',
        'imaginary_graph_Green_null', 'imaginary_graph_injective',
        'imaginary_graph_projection', 'graph_grading_commutator_block',
        'nonzero_graph_not_graded', 'real_graph_wrong_sign_detected',
        'cubic_nonzero', 'common_conjugation_preserves_cubic',
        'single_slot_sign_error_detected',
    }
    for name in ('L', 'R'):
        names.add(f'{name}_unitary')
        for g in (1, 2):
            names.add(f'{name}_intertwines_{g}')
    for label in ('P2', 'P4'):
        for suffix in ('projection', 'rank', 'move_invariance'):
            names.add(f'{label}_{suffix}')
    for k in (0, 1):
        names.add(f'move_commutant_basis_{k}')
    for label in ('V2', 'V4'):
        names.add(f'{label}_flat_stabilizer_dimension_one')
        names.add(f'{label}_flat_stabilizer_scalar_0')
    for name in ('L', 'R', 'D'):
        names.add(f'{name}_doubled_preserves_Green')
        names.add(f'{name}_doubled_preserves_graph')
    for name in ('plus', 'minus'):
        names.add(f'{name}_endpoint_graded')
        names.add(f'{name}_endpoint_Green_null')
    for a in range(36):
        names.add(f'dagger_{a}')
        for b in range(36):
            names.add(f'bracket_{a}_{b}')
            names.add(f'trace_metric_{a}_{b}')
    return names


def main():
    checks = {}

    def check(name, value):
        if name in checks:
            raise AssertionError(f'duplicate check name: {name}')
        if not any(value is literal for literal in (True, False, s.true, s.false)):
            raise TypeError(f'non-Boolean or unresolved result for {name}: {value!r}')
        checks[name] = bool(value)

    i2, i3, i6 = s.eye(2), s.eye(3), s.eye(6)
    z = s.diag(1, -1)
    y = s.Matrix([[0, -s.I], [s.I, 0]])
    qi, qj = s.I * z, s.I * y
    qk = qi * qj
    parities = [(2, 0), (0, 2), (2, 2)]
    automorphisms = {'L': {1: [1], 2: [1, 2]},
                     'R': {1: [1, 2], 2: [2]}}
    lifts = {'L': (i2 + qi) / s.sqrt(2),
             'R': (i2 - qj) / s.sqrt(2)}
    wa = s.diag(*[s.I**p[0] * qi for p in parities])
    wb = s.diag(*[s.I**p[1] * qj for p in parities])
    phi = s.diag(qj, qi, qk)

    def word(w):
        out = i6
        for letter in w:
            out = out * {1: wa, 2: wb}[letter]
        return out

    moves = {}
    for name, aut in automorphisms.items():
        permutation = s.zeros(3)
        for row, parity in enumerate(parities):
            target = tuple(sum(parity[a-1] for a in aut[g]) % 4
                           for g in (1, 2))
            permutation[row, parities.index(target)] = 1
        moves[name] = s.kronecker_product(permutation, lifts[name])
        check(f'{name}_unitary', same(moves[name].H*moves[name], i6))
        for g in (1, 2):
            check(f'{name}_intertwines_{g}', same(
                moves[name]*word([g])*moves[name].H, word(aut[g])))
    l, r = moves['L'], moves['R']
    check('L_square', same(l*l, s.kronecker_product(i3, qi)))
    check('R_square', same(r*r, s.kronecker_product(i3, -qj)))
    check('quaternion_commutator', same(wa*wb*wa.H*wb.H, -i6))
    check('Phi_unitary', same(phi.H*phi, i6))
    check('Phi_untwists_a', same(phi.H*wa*phi, s.kronecker_product(i3, qi)))
    check('Phi_untwists_b', same(phi.H*wb*phi, s.kronecker_product(i3, qj)))

    p2 = s.kronecker_product(s.ones(3)/3, i2)
    p4 = i6-p2
    for label, p, rank in [('P2', p2, 2), ('P4', p4, 4)]:
        check(label+'_projection', same(p*p, p) and same(p.H, p))
        check(label+'_rank', p.rank() == rank)
        check(label+'_move_invariance', same(p*l, l*p) and same(p*r, r*p))
    basis = commutant([s.sqrt(2)*l, s.sqrt(2)*r])
    check('move_commutant_dimension_two', len(basis) == 2)
    for k, b in enumerate(basis):
        reconstructed = s.trace(p2*b)/2*p2 + s.trace(p4*b)/4*p4
        check(f'move_commutant_basis_{k}', same(b, reconstructed))

    xs = s.symbols('x0:9')
    x = s.Matrix(3, 3, xs)
    fx = phi*s.kronecker_product(x, i2)*phi.H
    for label, forbidden in [('V2', p4*fx*p2), ('V4', p2*fx*p4)]:
        matrix, rhs = s.linear_eq_to_matrix(list(forbidden), xs)
        kernel = matrix.nullspace()
        check(label+'_flat_stabilizer_dimension_one', len(kernel) == 1)
        for k, v in enumerate(kernel):
            mat = s.Matrix(3, 3, tuple(v))
            check(f'{label}_flat_stabilizer_scalar_{k}', same(mat, mat[0, 0]*i3))

    dx = s.diag(1, -1, -1)
    d = s.kronecker_product(dx, i2)
    check('D_flat_flavour_map', same(phi*s.kronecker_product(dx, i2)*phi.H, d))
    check('D_involutive_unitary', same(d*d, i6) and same(d.H*d, i6))
    check('D_special_unitary', dx.det() == 1 and d.det() == 1)
    check('D_commutes_with_holonomies', same(d*wa, wa*d) and same(d*wb, wb*d))
    check('D_mixes_puncture_pieces', not same(d*p2, p2*d))
    check('D_nonzero_commutator_block', same((d*p2-p2*d)[0:2, 2:4], 2*i2/3))
    enlarged = commutant([s.sqrt(2)*l, s.sqrt(2)*r, d])
    check('enlarged_commutant_scalar', len(enlarged) == 1 and
          all(same(b, b[0, 0]*i6) for b in enlarged))
    check('scalar_phase_does_not_select', len(commutant([
        s.sqrt(2)*l, s.sqrt(2)*r, -i6])) == 2)

    # Local doubled Green-data control, not a global selfadjoint-extension
    # or ellipticity theorem. Source: physical branch weave_puncture_operator
    # PROOF section 2, pin 9e434bfaa63cff9450959d54384e1a6ad969546a.
    # ASSUMPTION here: both slots carry the same unitary coefficient action.
    # This is not an identification with the full parent reality/Lorentz data.
    # If End_G(E)=C, End_G(E+E)=M2(C). Its invariant six-dimensional
    # subspaces are ell tensor E. For J=[[0,I],[I,0]], null lines are
    # ell=span(1,it), t real, and span(0,1). Grading diag(I,-I)
    # preserves only the two endpoint lines. Naturality alone thus has
    # a continuous local coefficient family; grading selects endpoints.
    # This preserves the existing graded +/-3 statement. A physical use
    # must justify this grading and map it to the actual physical domain;
    # gauge covariance is not by itself that identification. The finite-cut
    # weave_boundary_lift packet already distinguishes Lorentz chirality,
    # internal slots, spin seams and reality. None is identified here merely
    # from a matching dimension. No new-absence or novelty claim is made.
    t = s.symbols('t', real=True)
    z6 = s.zeros(6)
    green = z6.row_join(i6).col_join(i6.row_join(z6))
    grading = s.diag(i6, -i6)
    graph = i6.col_join(s.I*t*i6)
    projector = clean(graph*graph.H/(1+t*t))
    check('Green_form_nondegenerate', green.det() != 0)
    check('imaginary_graph_Green_null', same(graph.H*green*graph, z6))
    check('imaginary_graph_injective', same(graph[:6, :], i6))
    check('imaginary_graph_projection', same(projector.H, projector) and
          same(projector*projector, projector))
    for name, op in [('L', l), ('R', r), ('D', d)]:
        doubled = s.diag(op, op)
        check(name+'_doubled_preserves_Green', same(doubled.H*green*doubled, green))
        check(name+'_doubled_preserves_graph', same(doubled*graph, graph*op))
    comm = clean(grading*projector-projector*grading)
    check('graph_grading_commutator_block', same(
        comm[:6, 6:], -2*s.I*t*i6/(1+t*t)))
    check('nonzero_graph_not_graded', not same(comm.subs(t, 1), s.zeros(12)))
    for name, endpoint in [('plus', s.diag(i6, z6)), ('minus', s.diag(z6, i6))]:
        check(name+'_endpoint_graded', same(endpoint*grading, grading*endpoint))
        check(name+'_endpoint_Green_null', same(endpoint*green*endpoint, s.zeros(12)))
    real_graph = i6.col_join(t*i6)
    check('real_graph_wrong_sign_detected', same(real_graph.H*green*real_graph, 2*t*i6)
          and not same((real_graph.H*green*real_graph).subs(t, 1), z6))

    # Finite matrix-algebra safeguards for the written conjugation proof.
    # These are not an E8 root construction or a global-domain computation.
    def conjugate(a):
        return d*a*d.H

    units = [unit(6, a, b) for a in range(6) for b in range(6)]
    for a, e in enumerate(units):
        check(f'dagger_{a}', same(conjugate(e.H), conjugate(e).H))
        for b, f in enumerate(units):
            check(f'bracket_{a}_{b}', same(conjugate(e*f-f*e),
                  conjugate(e)*conjugate(f)-conjugate(f)*conjugate(e)))
            check(f'trace_metric_{a}_{b}', s.trace(e.H*f) ==
                  s.trace(conjugate(e).H*conjugate(f)))
    a, q, v = unit(6, 0, 2), unit(6, 1, 0), unit(6, 2, 1)
    cubic = s.trace(q*(a*v-v*a))
    transformed = s.trace(conjugate(q)*(conjugate(a)*conjugate(v)
                                      - conjugate(v)*conjugate(a)))
    wrong = s.trace(q*(conjugate(a)*v-v*conjugate(a)))
    check('cubic_nonzero', cubic == 1)
    check('common_conjugation_preserves_cubic', transformed == cubic)
    check('single_slot_sign_error_detected', wrong != cubic)

    failed = [name for name, passed in checks.items() if not passed]
    required = required_check_names()
    missing = sorted(required-set(checks))
    unexpected = sorted(set(checks)-required)
    print(json.dumps({'checks': checks, 'passed': len(checks)-len(failed),
                      'failed': failed, 'required_checks': len(required),
                      'missing_checks': missing, 'unexpected_checks': unexpected,
                      'physical_index_derived': False,
                      'E8_embedding_reconstructed': False,
                      'global_PDE_certified': False,
                      'doubled_boundary_identified_with_full_parent': False,
                      'cusp_unit_selected': False}, indent=2))
    if failed or missing or unexpected:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
