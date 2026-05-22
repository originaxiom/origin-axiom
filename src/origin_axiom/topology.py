"""
Mapping-torus torsion and the figure-eight selection sieve.

Locks claims P8 and P10 of ``CLAIMS.md``; provides verified data for P9.
"""

import sympy as sp

from .algebra import A


def torsion_order(n):
    """
    ``|det(A**n - I)|`` — the torsion order of ``H_1`` of the mapping torus of
    ``A**n`` (the finite part of ``coker(A**n - I)``).
    """
    return abs((A**n - sp.eye(2)).det())


def torsion_growth_rate(n):
    """``(1/n) * log|det(A**n - I)|`` — converges to ``log(phi**2)``."""
    return sp.log(torsion_order(n)) / n


def is_torsion_free_hyperbolic(trace):
    """
    Trace-3 sieve (claim C3 scope: once-punctured-torus bundles with SL(2,Z)
    monodromy ``B``). The mapping torus is hyperbolic and has torsion-free
    ``H_1`` iff::

        |2 - trace| == 1     (torsion-free: |det(B - I)| == 1)
        |trace|     >  2     (hyperbolic)

    Among integer traces only ``trace == 3`` satisfies both.
    """
    torsion_free = abs(2 - trace) == 1
    hyperbolic = abs(trace) > 2
    return torsion_free and hyperbolic


def unique_trace_three(trace_range=range(-20, 21)):
    """Return every integer trace in ``trace_range`` passing the sieve."""
    return [tr for tr in trace_range if is_torsion_free_hyperbolic(tr)]


# --- The five independent selection filters (claim P10) --------------------
# Documented here; only the trace-3 sieve is computational in this module.
# The others are literature results carried as named facts.
SELECTION_FILTERS = (
    "trace-3 algebraic sieve (torsion-free + hyperbolic)",
    "minimum hyperbolic volume (Cao-Meyerhoff)",
    "amphichirality (mirror-symmetric)",
    "rank-2 categorifiability (Ostrik classification)",
    "Eisenstein triangulation (regular ideal tetrahedra)",
)
