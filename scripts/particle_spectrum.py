"""B8: Particle spectrum around golden vacuum."""
import numpy as np
from scipy.constants import golden_ratio as phi

kappa = 2 * np.log(phi**2) / np.sqrt(5)
mass_sq = kappa * np.sqrt(5)
mass = np.sqrt(mass_sq)
coupling = kappa
ratio = mass / coupling

print(f"mass² = κ√5 = {mass_sq:.6f}")
print(f"mass = {mass:.6f}")
print(f"coupling = κ = {coupling:.6f}")
print(f"m/g = {ratio:.6f}")
print(f"φ = {phi:.6f}")
print(f"m/g ≠ φ (near-miss: {abs(ratio-phi):.6f})")
print(f"m/g = √(5/(4logφ)) = {np.sqrt(5/(4*np.log(phi))):.10f}")
