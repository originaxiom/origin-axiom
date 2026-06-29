"""B290 -- the core-geodesic SCALE LADDER and the n-vs-k question. Run with sage-python (SnapPy).
Phase III of the seam arc (wall #5, scale).

B286 found scale generated at the seam: the core geodesic of the (1,n) filling has length ~ 2*pi/n -> 0. B290 makes
the asymptotic precise and asks: does the filling integer n equal the program's WRT level k (B204)?

  1. THE LADDER (POSITIVE, math). The COMPLEX core length of the (1,n) filling is
        ell_C(1,n) = 2*pi*i/n + (pi/sqrt(3))/n^2 + O(1/n^3),
     so |ell_C| ~ 2*pi/n (confirming B286). The 1/n^2 correction coefficient is pi/sqrt(3) = 2*pi/|tau_cusp|, with
     tau_cusp = 2*sqrt(3)*i the cusp shape -- i.e. the ladder is the Neumann-Zagier core-geodesic ladder, controlled
     by the cusp shape. TWO methods: SnapPy core_length, and the correction coefficient PREDICTED independently from
     the (separately computed) cusp shape.

  2. n =/= k (NEGATIVE). The filling coefficient n is a TOPOLOGICAL surgery integer; the WRT level k (B204) is a
     QUANTUM root-of-unity parameter q = e^{2*pi*i/(k+2)} (B204's own shifted level is n_B204 = k+2, a DIFFERENT
     integer). They are INDEPENDENT axes: one can evaluate the WRT invariant at any level k of the (1,n)-surgered
     manifold. So 'filling n = level k' is a formal substitution, not an identity. The scale ladder does NOT identify
     the filling with the level.

  3. HELD coincidence (firewalled). Under the formal substitution k=n, the (firewalled) relation G*Lambda = 6*pi/k
     (S043/B259) gives core = 2*pi/n = (G*Lambda)/3 -- a numerical coincidence with the 122-ORDER GAP, NOT banked.
"""
import snappy
from math import pi, sqrt


def cusp_shape():
    return complex(snappy.Manifold('m004').cusp_info(0)['shape'])      # ~ 2*sqrt(3)*i


def core_length_complex(n):
    M = snappy.Manifold('m004'); M.dehn_fill((1, n))
    return complex(M.cusp_info(0)['core_length'])


def ladder(ns=(50, 100, 200, 400)):
    tau = cusp_shape()
    pred_coeff = 2 * pi / abs(tau)                       # = pi/sqrt(3), predicted from the cusp shape alone
    rows = []
    for n in ns:
        cl = core_length_complex(n)
        rows.append((n, abs(cl), cl.real * n**2, 2 * pi / n))   # |ell|, measured 1/n^2 coeff, leading 2pi/n
    return tau, pred_coeff, rows


if __name__ == "__main__":
    tau, pred, rows = ladder()
    print(f"cusp shape tau = {tau:.6f}  (= 2*sqrt(3)*i);  predicted 1/n^2 coeff 2pi/|tau| = {pred:.8f} (= pi/sqrt3)")
    print("\n n  : |ell_C|      vs 2pi/n      | measured Re(ell)*n^2 (-> 2pi/|tau|)")
    for n, mag, coeff, lead in rows:
        print(f" {n:4d}: {mag:.8f}  {lead:.8f} | {coeff:.6f}")
    # leading 2pi/n confirmed + correction coeff matches the cusp-shape prediction:
    assert abs(rows[-1][1] - rows[-1][3]) < 1e-4
    assert abs(rows[-1][2] - pred) < 1e-3
    print("\nVERDICT: scale ladder ell_C(1,n) = 2pi*i/n + (pi/sqrt3)/n^2 + ... (NZ, cusp-shape-controlled).")
    print("filling n =/= WRT level k (independent axes: topological surgery vs quantum root of unity). HELD: core")
    print("= (G*Lambda)/3 under k=n is a firewalled coincidence (122-order gap), not banked.")
