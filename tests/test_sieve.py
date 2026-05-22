"""P10 — the trace-3 algebraic sieve, one of five filters selecting 4_1."""

from origin_axiom.topology import (
    is_torsion_free_hyperbolic,
    SELECTION_FILTERS,
    unique_trace_three,
)


def test_trace_three_passes_the_sieve():
    assert is_torsion_free_hyperbolic(3)


def test_trace_three_is_the_unique_integer_trace_passing_the_sieve():
    assert unique_trace_three() == [3]


def test_neighbouring_traces_fail():
    assert not is_torsion_free_hyperbolic(2)  # parabolic, not hyperbolic
    assert not is_torsion_free_hyperbolic(4)  # hyperbolic but has torsion
    assert not is_torsion_free_hyperbolic(1)  # torsion-free but not hyperbolic


def test_five_independent_filters_are_documented():
    assert len(SELECTION_FILTERS) == 5
