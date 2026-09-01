#!/usr/bin/env python3
"""Exact choice-versus-observable quotient for a one-dimensional tail.

This is the finite linear-algebra lemma used to keep raw presentation choices
separate from physical/operator parameters.  It is dependency-free.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import product


Q = Fraction


def alternating_value(matrix, left, right):
    return sum(left[i] * matrix[i][j] * right[j]
               for i in range(len(left)) for j in range(len(right)))


def matrix_rank(rows):
    work = [[Q(value) for value in row] for row in rows]
    if not work:
        return 0
    rank = 0
    for column in range(len(work[0])):
        pivot = next((row for row in range(rank, len(work))
                      if work[row][column]), None)
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        scale = work[rank][column]
        work[rank] = [value / scale for value in work[rank]]
        for row in range(len(work)):
            if row == rank or not work[row][column]:
                continue
            scale = work[row][column]
            work[row] = [left - scale * right
                         for left, right in zip(work[row], work[rank])]
        rank += 1
        if rank == len(work):
            break
    return rank


def form_with_mixed_block(mixed):
    """Alternating form on V=C+<t>, zero on wedge^2 C."""

    assert len(mixed) == 3
    return tuple(tuple(
        Q(0) if i < 3 and j < 3 else
        Q(mixed[i]) if i < 3 and j == 3 else
        Q(-mixed[j]) if i == 3 and j < 3 else Q(0)
        for j in range(4)) for i in range(4))


def main():
    c_basis = (
        (Q(1), Q(0), Q(0), Q(0)),
        (Q(0), Q(1), Q(0), Q(0)),
        (Q(0), Q(0), Q(1), Q(0)),
    )
    tail_lift = (Q(0), Q(0), Q(0), Q(1))
    mixed = (Q(2), Q(-3), Q(5))
    form = form_with_mixed_block(mixed)

    # The premise beta|Lambda^2 C=0 is checked on a basis.
    assert all(alternating_value(form, left, right) == 0
               for left in c_basis for right in c_basis)

    # Every lift of the same quotient generator differs by an element of C.
    # The observable vector beta(C,lift) is exactly independent of all three
    # lift coordinates, while remaining nonzero.
    observed = tuple(alternating_value(form, c, tail_lift)
                     for c in c_basis)
    assert observed == mixed
    changes = tuple(product(range(-2, 3), repeat=3))
    for change in changes:
        changed_lift = tuple(Q(value) for value in change) + (Q(1),)
        assert tuple(alternating_value(form, c, changed_lift)
                     for c in c_basis) == observed
    assert any(observed)

    # On projective V, the open set with nonzero tail coordinate has one
    # observable projective value.  The boundary P(C) maps to zero and is a
    # separate stratum; the lemma does not silently erase that distinction.
    for tail_scale in (Q(-3), Q(-1), Q(1), Q(2), Q(5)):
        vector = (Q(7), Q(-11), Q(13), tail_scale)
        value = tuple(alternating_value(form, c, vector) for c in c_basis)
        assert tuple(entry / tail_scale for entry in value) == observed
    pure_connecting = (Q(7), Q(-11), Q(13), Q(0))
    assert all(alternating_value(form, c, pure_connecting) == 0
               for c in c_basis)

    # The derivative of the observable with respect to the three raw lift
    # coordinates is zero: raw affine dimension 3, observable-image dimension 0.
    variations = []
    for direction in c_basis:
        variations.append([
            alternating_value(form, c, direction) for c in c_basis
        ])
    assert matrix_rank(variations) == 0

    # Bite control: a nonzero C-C block makes a lift change observable.
    planted = [list(row) for row in form]
    planted[0][1] = Q(7)
    planted[1][0] = Q(-7)
    planted = tuple(tuple(row) for row in planted)
    changed_lift = (Q(0), Q(1), Q(0), Q(1))
    planted_base = tuple(alternating_value(planted, c, tail_lift)
                         for c in c_basis)
    planted_changed = tuple(alternating_value(planted, c, changed_lift)
                            for c in c_basis)
    assert planted_base != planted_changed

    print("PASS beta restricted to wedge^2(C) is zero")
    print("PASS induced C tensor (V/C) observable is well-defined")
    print("DATA nonzero induced mixed observable =", observed)
    print("PASS all", len(changes), "tested tail lifts give the same observable")
    print("RESULT raw lift-choice dimension = 3; observable variation rank = 0")
    print("RESULT projective nonzero-tail stratum has one observable point; pure-connecting boundary maps to zero")
    print("CONTROL a planted C-C term makes the lift choice observable")
    print("SCOPE exact quotient lemma; no R032 characteristic-zero vanishing or physical normalization is assumed")


if __name__ == "__main__":
    main()
