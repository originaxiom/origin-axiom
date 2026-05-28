"""B7 supplement: Coupled Möbius lattice convergence."""
import numpy as np
from scipy.constants import golden_ratio as phi

def mobius(tau): return (2*tau + 1) / (tau + 1)

N, eps = 200, 0.3
np.random.seed(42)
tau = 0.1 * np.random.randn(N) + 0.1

for step in range(100):
    new = np.zeros(N)
    for i in range(N):
        local = mobius(tau[i])
        nbr = 0.5 * (tau[(i+1)%N] + tau[(i-1)%N])
        new[i] = (1-eps)*local + eps*nbr
    tau = new

err = np.max(np.abs(tau - phi))
print(f"Max |τ-φ| after 100 steps = {err:.2e}")
assert err < 1e-10, f"Lattice did not converge: {err}"
print("PASS: all sites converge to φ from random initial conditions")
