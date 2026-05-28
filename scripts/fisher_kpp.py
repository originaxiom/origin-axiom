"""B7: Fisher-KPP creation wave. Gradient flow simulation."""
import numpy as np
from scipy.constants import golden_ratio as phi

N, L, D = 500, 60.0, 1.0
dx = L/N
dt = 0.2 * dx**2 / (2*D)
x = np.linspace(-L/2, L/2, N)
tau = 0.3 * np.exp(-x**2/2.0)  # seed at zero

for n in range(8000):
    reaction = 1 + tau - tau**2
    lap = np.zeros_like(tau)
    lap[1:-1] = (tau[2:] - 2*tau[1:-1] + tau[:-2]) / dx**2
    tau = tau + dt * (reaction + D * lap)

avg = np.mean(tau)
err = abs(avg - phi)
print(f"Final <τ> = {avg:.10f}, |<τ>-φ| = {err:.2e}")
print(f"Fisher-KPP speed = 2√D = {2*np.sqrt(D):.4f}")
assert err < 1e-6, f"Did not converge to φ: error {err}"
print("PASS: field converges to golden vacuum from seed at zero")
