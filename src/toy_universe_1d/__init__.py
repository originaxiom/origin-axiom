"""
1D twisted toy universe: normal modes and vacuum energy
for a complex scalar field on a discrete ring with twisted boundary condition.

Boundary condition:
    Φ_{n+N} = exp(i θ*) Φ_n

This gives mode momenta:
    k_m(θ*) = (θ* + 2π m) / N,  m = 0,...,N-1

and frequencies:
    ω_m(θ*) = sqrt( m0^2 + 4 c^2 sin^2(k_m/2) )
"""

from .modes import compute_modes_1d, vacuum_energy_1d
