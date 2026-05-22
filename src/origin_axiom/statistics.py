"""
Classical statistical transfer-matrix realizations of the record system.

Locks claims P3, P4, P5 of ``CLAIMS.md``. These are *exact* identities between
the record matrices and known statistical-mechanics transfer matrices — they are
realizability statements, not empirical validation (see ``GOVERNANCE.md`` sec. 8).
"""

import sympy as sp

from .algebra import L, R

# Ising coupling at which the normalized transfer matrix equals L + R:
#   e^{2K} = 2  =>  K = (1/2) log 2
K_ISING = sp.log(2) / 2


def ising_transfer_matrix(K):
    """Normalized 1D zero-field Ising transfer matrix ``[[e^{2K}, 1], [1, e^{2K}]]``."""
    e2k = sp.exp(2 * K)
    return sp.Matrix([[e2k, 1], [1, e2k]])


def zimm_bragg_matrix(s, sigma):
    """Zimm-Bragg helix-coil transfer matrix ``[[s, 1], [sigma*s, 1]]``."""
    return sp.Matrix([[s, 1], [sigma * s, 1]])


def correlation_length(K):
    """1D Ising correlation length ``xi = -1 / log(tanh K)``."""
    return -1 / sp.log(sp.tanh(K))


def z_count(N):
    """Word-count partition: number of length-``N`` words over {L, R} = ``2**N``."""
    return 2 ** N


def z_trace(N):
    """
    Trace-weighted partition ``Z_N^trace = sum_{|w|=N} Tr(M_w) = Tr((L+R)**N)``.

    Equals ``3**N + 1`` because ``L + R`` has eigenvalues 3 and 1.
    """
    return sp.trace((L + R) ** N)
