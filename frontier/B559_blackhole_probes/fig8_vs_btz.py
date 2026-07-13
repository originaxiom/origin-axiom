"""Figure-eight as a 3D-gravity saddle, compared to BTZ.

Dictionary (banked B520): a loxodromic element of trace x is a BTZ black hole with
entropy S = arccosh(x/2).  For a closed geodesic of complex length lambda,
x = 2 cosh(lambda/2)  ->  S = arccosh(x/2) = lambda/2  (Re = horizon/entropy,
Im = rotation/angular-momentum, i.e. a *rotating* BTZ).

BTZ            : H^3 / <one loxodromic> = solid torus. ONE geodesic (the horizon),
                 infinite volume, characterized by one complex trace (mass + i*spin).
Figure-eight   : H^3 / Gamma, Gamma non-abelian. FINITE volume, a DISCRETE SPECTRUM
                 of geodesics, CS = 0 (amphichiral -> real action).
"""
import cmath
import snappy

M = snappy.Manifold('4_1')
vol = M.volume()
cvol = M.complex_volume()
print(f"Vol = {vol:.10f}   complex Vol = {cvol}")
print(f"Chern-Simons = {float(M.chern_simons()):.3e}  -> CS = 0 (amphichiral: figure-eight is its own mirror)")
print(f"total 3d-gravity action of this saddle = Vol + i*CS = {vol:.7f} + 0 i   (REAL, no framing phase)\n")

print("=== the geodesic 'black-hole' spectrum (BTZ dictionary S = lambda/2) ===")
print(f"{'complex length lambda':>34} | {'trace x=2cosh(l/2)':>26} | {'|x|':>7} | {'entropy Re(S)=Re(l)/2':>20}")
seen = set()
for g in M.length_spectrum(2.4):
    lam = complex(g.length)
    key = round(lam.real, 6)
    if key in seen:
        continue
    seen.add(key)
    x = 2*cmath.cosh(lam/2)
    S = lam/2                      # = arccosh(x/2)
    print(f"{lam.real:>15.6f}{lam.imag:>+13.6f} i | "
          f"{x.real:>11.6f}{x.imag:>+11.6f} i | {abs(x):>7.4f} | {S.real:>20.6f}")

print("\n=== BTZ side: the banked formula S = arccosh(x/2) at the object's traces ===")
import math
for label, x in [("golden loxodromic x=5 (B520, 40a1 2-torsion)", 5.0),
                 ("figure-eight systole |x|=sqrt3", math.sqrt(3)),
                 ("trace x=3 (Markov seed / first rung)", 3.0)]:
    print(f"  {label:<44}: S = arccosh({x/2:.4f}) = {math.acosh(x/2):.6f}")

print("\n=== structural verdict ===")
print("  BTZ         : 1 geodesic,  infinite volume, action needs regularization.")
print(f"  figure-eight: infinitely many geodesics, FINITE action {vol:.6f}, CS=0.")
print("  -> the figure-eight is NOT one black hole; it is a complete finite-volume")
print("     3d-gravity instanton (a subleading saddle in the sum over geometries),")
print("     carrying a whole discrete spectrum of rotating-BTZ-like geodesics.")
