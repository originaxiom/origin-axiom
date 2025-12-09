"""
1D complex scalar on a ring with a single defect bond and a twist.

We construct a quadratic form matrix M such that the potential energy is

  V = 1/2 * phi^† M phi

for a complex field vector phi. The eigenvalues of M are ω^2, so that ω are
the normal-mode frequencies. The vacuum energy is then

  E0(θ*) = 1/2 Σ_j ω_j(θ*).

The defect is implemented as a modified coupling on the bond between site
N-1 and site 0. A twist θ* is applied on that same bond.
"""

import numpy as np


def make_defected_mass_matrix(
    N: int,
    c: float,
    m0: float,
    theta_star: float,
    defect_strength: float = 0.5,
) -> np.ndarray:
    """Return the N×N Hermitian mass matrix M for the defected chain.

    Parameters
    ----------
    N : int
        Number of sites.
    c : float
        Nearest-neighbour coupling (velocity scale).
    m0 : float
        Bare mass parameter.
    theta_star : float
        Twist angle applied on the defect bond between site N-1 and 0.
    defect_strength : float, optional
        Relative strength of the defect bond compared to bulk bonds.
        For defect_strength = 1.0 we recover a uniform ring.
    """
    # Start with diagonal contributions: m0^2 + 2 c^2 from two neighbours
    M = np.zeros((N, N), dtype=np.complex128)
    M += (m0**2 + 2.0 * c**2) * np.eye(N, dtype=np.complex128)

    # Bulk bonds between n and n+1 for n = 0,...,N-2 (uniform ring part)
    for n in range(N - 1):
        M[n, n + 1] += -c**2
        M[n + 1, n] += -c**2

    # Defect bond between site N-1 and 0 with twist θ* and strength factor
    c_def = defect_strength * c
    phase = np.exp(1j * theta_star)

    # Off-diagonal terms correspond to -c_def^2 ( e^{iθ} φ_0* φ_{N-1}
    #                                         + e^{-iθ} φ_{N-1}* φ_0 )
    # so that M is Hermitian.
    M[0, N - 1] += -c_def**2 * np.conjugate(phase)
    M[N - 1, 0] += -c_def**2 * phase

    return M


def defected_omegas(
    N: int,
    c: float,
    m0: float,
    theta_star: float,
    defect_strength: float = 0.5,
) -> np.ndarray:
    """Return normal-mode frequencies ω_j(θ*) for the defected chain."""
    M = make_defected_mass_matrix(N, c, m0, theta_star, defect_strength)
    evals = np.linalg.eigvalsh(M)

    # Numerical safety: clip tiny negative eigenvalues to zero
    evals = np.clip(evals.real, 0.0, None)
    omegas = np.sqrt(evals)
    return omegas


def defected_vacuum_energy(
    N: int,
    c: float,
    m0: float,
    theta_star: float,
    defect_strength: float = 0.5,
) -> float:
    """Return vacuum energy E0(θ*) = 1/2 Σ_j ω_j(θ*)."""
    omegas = defected_omegas(N, c, m0, theta_star, defect_strength)
    return 0.5 * float(np.sum(omegas))
