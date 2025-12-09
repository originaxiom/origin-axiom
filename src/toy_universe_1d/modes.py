import numpy as np

def compute_modes_1d(N, c, m0, theta_star):
    """
    Compute normal mode momenta k_m and frequencies ω_m for a 1D chain
    of length N with twisted boundary condition Φ_{n+N} = exp(i θ*) Φ_n.

    Parameters
    ----------
    N : int
        Number of lattice sites.
    c : float
        Wave speed parameter.
    m0 : float
        Mass parameter (like m in Klein–Gordon).
    theta_star : float
        Twist angle θ* (in radians).

    Returns
    -------
    k : np.ndarray
        Array of shape (N,) of mode momenta k_m(θ*).
    omega : np.ndarray
        Array of shape (N,) of mode frequencies ω_m(θ*).
    """
    # Mode index m = 0,...,N-1
    m = np.arange(N, dtype=float)

    # Twisted momenta k_m(θ*) = (θ* + 2π m) / N
    k = (theta_star + 2.0 * np.pi * m) / float(N)

    # Discrete Laplacian eigenvalues: λ(k) = -4 sin^2(k/2)
    # Equation of motion: d2Φ/dt2 = c^2 ΔΦ - m0^2 Φ
    # => ω^2 = m0^2 + 4 c^2 sin^2(k/2)
    sin_half = np.sin(0.5 * k)
    omega_sq = m0**2 + 4.0 * (c**2) * (sin_half**2)
    omega = np.sqrt(omega_sq)

    return k, omega


def vacuum_energy_1d(N, c, m0, theta_star):
    """
    Compute the (unregularized) vacuum energy for the 1D twisted model:

        E0(θ*) = 1/2 Σ_m ω_m(θ*)

    For a finite N this is a finite sum. For physical interpretations we will
    mostly look at energy differences relative to θ* = 0.
    """
    _, omega = compute_modes_1d(N, c, m0, theta_star)
    return 0.5 * omega.sum()
