"""EXPLORATION (main, firewalled): D(tau) near omega by direction, and at the top of the root's geodesic.
Uses B1654's lock's cutoff-free route (polar Gauss-Legendre over the period parallelogram)."""
import sys, numpy as np, importlib.util
spec = importlib.util.spec_from_file_location("lk", "tests/test_b1654_the_norm_of_the_boundary_class.py")
lk = importlib.util.module_from_spec(spec); spec.loader.exec_module(lk)
w = np.exp(2j*np.pi/3)
print("D/|R|^2 at omega:", lk._D(complex(w)))
for d in (1e-2, 3e-3, 1e-3):
    row = []
    for phi in np.linspace(0, 2*np.pi, 7)[:-1]:
        t = complex(w + d*np.exp(1j*phi)); D = lk._D(t)
        row.append(f"{phi/np.pi:.2f}pi:{abs(D)/d:.4f}/arg{np.angle(D)/np.pi:+.3f}pi")
    print(f"d={d:g}: |D|/(|R|^2 d) by direction:", "  ".join(row))
ts = complex(0.5, np.sqrt(5)/2)
print("tau* = 1/2 + i sqrt5/2: D/|R|^2 =", lk._D(ts), "  rho = 1/2 + i sqrt3/2:", lk._D(complex(0.5, np.sqrt(3)/2)))
for y in (1.0, 1.05, 1.118034, 1.2):
    print(f"  on Re tau = 1/2, Im = {y}: D/|R|^2 = {lk._D(complex(0.5, y))}")
