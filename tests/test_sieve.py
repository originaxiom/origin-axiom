"""P10 — the trace-3 algebraic sieve, one of five filters selecting 4_1.

Hardened 2026-07-01 (audit): of the five documented filters, only the trace-3
sieve was computational; three of the other four (minimum volume, amphichirality,
Eisenstein triangulation) now get live SnapPy cross-checks when SnapPy is
installed. Rank-2 categorifiability (Ostrik) remains a literature fact carried
as a named string — P10's claim text already records that the four auxiliary
filters are "documented, not proven to uniquely select" 4_1.
"""

import cmath

import pytest

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


def test_snappy_minimum_volume_filter_if_available():
    # Filter 2 (Cao-Meyerhoff): 4_1 (= m004) realizes the minimal volume of
    # orientable cusped hyperbolic 3-manifolds, tied only with its sister
    # m003 (which the trace-3 sieve's torsion-free clause then excludes:
    # m003 carries Z/5 torsion, cf. P9/B197).
    snappy = pytest.importorskip("snappy")
    census = snappy.OrientableCuspedCensus  # volume-ordered
    first, second, third = (census[i] for i in range(3))
    assert {first.name(), second.name()} == {"m003", "m004"}
    v_min = snappy.Manifold("4_1").volume()
    assert abs(first.volume() - v_min) < 1e-9
    assert abs(second.volume() - v_min) < 1e-9
    assert third.volume() > v_min + 0.5   # the tie is exactly {m003, m004}


def test_snappy_eisenstein_triangulation_filter_if_available():
    # Filter 5: 4_1 decomposes into two regular ideal tetrahedra, both of
    # shape e^{i pi/3} — the Eisenstein point (cf. P12's disc -3 factor).
    snappy = pytest.importorskip("snappy")
    shapes = [complex(z) for z in snappy.Manifold("4_1").tetrahedra_shapes("rect")]
    assert len(shapes) == 2
    eisenstein = cmath.exp(1j * cmath.pi / 3)
    assert all(abs(z - eisenstein) < 1e-9 for z in shapes)


def test_snappy_amphichirality_filter_if_available():
    # Filter 3: 4_1 is amphichiral — symmetry_group().is_amphicheiral()
    # gated on is_full_group(), per the MB guard in REPRODUCIBILITY.md.
    snappy = pytest.importorskip("snappy")
    sg = snappy.Manifold("4_1").symmetry_group()
    assert sg.is_full_group()
    assert sg.is_amphicheiral()
