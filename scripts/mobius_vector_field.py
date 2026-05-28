"""P15+P16: Möbius generating vector field and derived potential. Exact algebra."""
import numpy as np
from scipy.linalg import logm
from scipy.constants import golden_ratio as phi

A = np.array([[2.,1.],[1.,1.]])
logA = logm(A).real
kappa = 2 * np.log(phi**2) / np.sqrt(5)

# Vector field v(τ) = b + (a-d)τ - cτ² from log(A) entries
a, b, c, d = logA[0,0], logA[0,1], logA[1,0], logA[1,1]
# v(τ) = b + (a-d)τ - cτ²
# At fixed points: v(φ) = 0, v(-1/φ) = 0, v(0) = b = 2κ/2... 
# Actually v = b + (a-d)τ - cτ²
v_at_phi = b + (a-d)*phi - c*phi**2
v_at_neg = b + (a-d)*(-1/phi) - c*(-1/phi)**2
v_at_zero = b

print(f"v(φ) = {v_at_phi:.2e} (should be 0)")
print(f"v(-1/φ) = {v_at_neg:.2e} (should be 0)")
print(f"v(0) = {v_at_zero:.6f} (should be κ = {kappa:.6f})")

# Factor: v(τ) = -c(τ-φ)(τ+1/φ) = -c(τ²-τ-1)
factor_check = -c * (phi**2 - phi - 1)
print(f"-c(φ²-φ-1) = {factor_check:.2e} (should be 0)")
print(f"c = {c:.6f}, κ = {kappa:.6f}")
print(f"v(τ) = -{c:.6f}(τ²-τ-1)")

# Potential V'(τ) = κ(τ²-τ-1), V(τ) = κ(τ³/3-τ²/2-τ)
V_phi = kappa * (phi**3/3 - phi**2/2 - phi)
V_neg = kappa * ((-1/phi)**3/3 - (-1/phi)**2/2 - (-1/phi))
Vpp_phi = kappa * (2*phi - 1)  # = κ√5

print(f"\nV(φ) = {V_phi:.6f}")
print(f"V(-1/φ) = {V_neg:.6f}")
print(f"V''(φ) = κ(2φ-1) = κ√5 = {Vpp_phi:.6f} > 0 (minimum)")
print(f"V''(-1/φ) = κ(-2/φ-1) = -κ√5 = {kappa*(-2/phi-1):.6f} < 0 (maximum)")
print(f"V'(0) = κ(0-0-1) = -κ = {-kappa:.6f} ≠ 0 (zero is NOT a critical point)")
