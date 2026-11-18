"""B1957: agy-exp's X-CLOSURE campaign (four result notes, read in full through the mask): the exact facts under its
statements that main's other checks do not already hold.  Nothing of the seat's is run.  (The doubled shear, the
standard relation (S T)^3 = S^2, D(z) + D(conj z) = 0, the anomaly, and the algebra of the physical lane's P-C3b are
in physical_state_orbit.py and physical_all_seats_findings.py.)
 C1  SnapPy on main: m004 and m003 have the same volume; the Chern-Simons invariant is 0 for m004 and 1/4 for m003;
     their first homology is Z and Z/5 + Z; m015's value and its distance from the multiples of 1/12.
 C2  the Gauss sums with the half-shear: gamma_N(r) = N^(-1/2) sum_x exp(2 pi i (r/2) x^2/N) is i, 1, i at
     (N, r) = (15, 1), (5, 3), (3, 2), and gamma_15(1) = gamma_5(3) gamma_3(2).
 C3  for H = L = 1, B = i (2/5), C = i (3/7) on three dimensions the block matrix is not Hermitian and the Schur
     complement L - B H^-1 C is (41/35) times the identity, positive and real.
 C4  1/(8 ell^2) at ell = 3/2 is 1/18."""
import cmath, functools, math
from fractions import Fraction as Fr
import numpy as np
print = functools.partial(print, flush=True)

def gauss(N, r):
    h = (r * pow(2, -1, N)) % N; return sum(cmath.exp(2j * cmath.pi * h * x * x / N) for x in range(N)) / math.sqrt(N)

if __name__ == "__main__":
    try:
        import snappy
        v = {n: (float(snappy.Manifold(n).volume()), float(snappy.Manifold(n).chern_simons()), str(snappy.Manifold(n).homology())) for n in ("m004", "m003", "m015")}
        cs15 = v["m015"][1]; dist = min(abs(cs15 - k / 12) for k in range(-12, 13))
        print("C1: volumes m004 %.10f, m003 %.10f (difference %.1e); Chern-Simons m004 %.2e, m003 %.8f; homology %s and %s; m015: %.8f, at distance %.4f from the nearest multiple of 1/12"
              % (v["m004"][0], v["m003"][0], abs(v["m004"][0] - v["m003"][0]), v["m004"][1], v["m003"][1], v["m004"][2], v["m003"][2], cs15, dist))
    except ImportError:
        print("C1: SnapPy is not installed here; not checked")
    g = {k: gauss(*k) for k in ((15, 1), (5, 3), (3, 2))}
    print("C2: gamma_15(1) = %.6f%+.6fi, gamma_5(3) = %.6f%+.6fi, gamma_3(2) = %.6f%+.6fi; |gamma_15(1) - gamma_5(3) gamma_3(2)| = %.1e; their inverse squares: %s"
          % (g[(15, 1)].real, g[(15, 1)].imag, g[(5, 3)].real, g[(5, 3)].imag, g[(3, 2)].real, g[(3, 2)].imag, abs(g[(15, 1)] - g[(5, 3)] * g[(3, 2)]), [round((1 / x ** 2).real) for x in g.values()]))
    I3 = np.eye(3); Mb = np.block([[I3, 0.4j * I3], [(3j / 7) * I3, I3]]); schur = I3 - (0.4j * I3) @ np.linalg.inv(I3) @ ((3j / 7) * I3)
    print("C3: |M - M^dagger| = %.4f; the Schur complement is %.10f times the identity (41/35 = %.10f), imaginary part %.1e" % (np.linalg.norm(Mb - Mb.conj().T), schur[0, 0].real, 41 / 35, abs(schur[0, 0].imag)))
    print("C4: 1/(8 ell^2) at ell = 3/2: %s" % (1 / (8 * Fr(3, 2) ** 2)))
