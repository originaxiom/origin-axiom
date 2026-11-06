"""Check of agy's Stage 29 geometry claims (commit 4bbaa659d, theorem154), data-free.

PRE-REGISTRATION (written before this script was run; its sha256 is recorded before the run)
Claims under test, with the pass rule for each:
  C1  z_3 = coth^2(L_tube/2): z_3 is the central tetrahedron's shape in SnapPy's own triangulation of the bundle
      b++ L^6 R (LR)^k, and L_tube is the complex length of its shortest closed geodesic from SnapPy's length spectrum
      (independent of the shapes as entered here). PASS if, for k = 1, 2 and 3, the smallest of |coth^2(L/2) - z| over
      the central tetrahedron's three edge parameters and over L and conj(L) is below 1e-9.
  C2  "the tunnel twists by exactly 45 degrees": PASS if | |Im L_tube| - pi/4 | < 1e-6 at k = 1.
  C3  "3.6518 / sqrt(2) = 2.5789": PASS if | (-Re z_2)/sqrt(2) - Im z_2 | < 1e-4, with z_2 = z_3 + 1 at k = 1.
  C4  the Teichmuller apex sqrt(40/3) "also equal to -Re(z_2)": PASS if | sqrt(40/3) - (-Re z_2) | < 1e-9 at k = 1.
  C5  a 45-degree tilt of z_2 (equal shadows): PASS if | |Re z_2| - |Im z_2| | < 1e-4 at k = 1.
Predicted before running: C1 PASS (B1846 § 3 reports the same k = 1 length as agy's table); C2-C5 FAIL.
Nothing here is a coupling, a scale ratio, an inter-sector value or a held-out quantity. No data is read.
"""
import cmath
import math

import snappy

print("snappy", snappy.__version__)


def central_shapes(M):
    """Return all tetrahedra shapes (z) as complex numbers."""
    return [complex(z) for z in M.tetrahedra_shapes("rect")]


def three_params(z):
    return [z, 1 / (1 - z), 1 - 1 / z]


def coth2(L):
    return (cmath.cosh(L / 2) / cmath.sinh(L / 2)) ** 2


rows = []
for k in (1, 2, 3):
    word = "LLLLLLR" + "LR" * k
    M = snappy.Manifold("b++" + word)
    sol = M.solution_type()
    ntet = M.num_tetrahedra()
    shapes = central_shapes(M)
    spec = M.length_spectrum(0.5)
    Ls = [complex(g.length) for g in spec]
    L = min(Ls, key=lambda c: c.real)
    best = None
    for i, z in enumerate(shapes):
        for w in three_params(z):
            for LL in (L, L.conjugate()):
                d = abs(coth2(LL) - w)
                if best is None or d < best[0]:
                    best = (d, i, w, LL)
    rows.append((k, word, sol, ntet, L, best))
    print(f"k={k} word={word} tets={ntet} solution={sol}")
    print(f"  shortest geodesic L = {L.real:.12f} {L.imag:+.12f}i  (|Im L| in degrees {abs(math.degrees(L.imag)):.6f})")
    print(f"  best |coth^2(L/2) - shape param| = {best[0]:.3e} at tet {best[1]}, param {best[2].real:.12f} {best[2].imag:+.12f}i")

k1 = rows[0]
z3 = k1[5][2]
z2 = z3 + 1
L1 = k1[4]
c1 = all(r[5][0] < 1e-9 for r in rows)
c2 = abs(abs(L1.imag) - math.pi / 4) < 1e-6
c3 = abs((-z2.real) / math.sqrt(2) - z2.imag) < 1e-4
c4 = abs(math.sqrt(40 / 3) - (-z2.real)) < 1e-9
c5 = abs(abs(z2.real) - abs(z2.imag)) < 1e-4
print()
print(f"z_2 (k=1) = {z2.real:.10f} {z2.imag:+.10f}i")
print(f"C1 coth^2 identity at k=1,2,3: {'PASS' if c1 else 'FAIL'}  (max residual {max(r[5][0] for r in rows):.3e})")
print(f"C2 exactly 45 degrees: {'PASS' if c2 else 'FAIL'}  (|Im L| = {abs(L1.imag):.9f} rad = {abs(math.degrees(L1.imag)):.6f} deg; pi/4 = {math.pi/4:.9f})")
print(f"C3 (-Re z_2)/sqrt2 = Im z_2: {'PASS' if c3 else 'FAIL'}  ({-z2.real/math.sqrt(2):.6f} vs {z2.imag:.6f}; 3.6518/sqrt2 = {3.6518/math.sqrt(2):.6f})")
print(f"C4 sqrt(40/3) = -Re z_2: {'PASS' if c4 else 'FAIL'}  ({math.sqrt(40/3):.9f} vs {-z2.real:.9f}; difference {math.sqrt(40/3)+z2.real:+.3e})")
print(f"C5 equal shadows (45-degree tilt of z_2): {'PASS' if c5 else 'FAIL'}  (angle of z_2 above the negative real axis {math.degrees(math.atan2(z2.imag, -z2.real)):.4f} deg)")
