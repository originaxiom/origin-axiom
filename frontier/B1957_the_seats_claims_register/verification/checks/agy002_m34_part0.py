"""B1957: agy-002's note M34, Part 0: the phases of frame C's coupling under tau -> tau + 5, which fixes every point of
order 5, on main's frame code (the coupling of wb2_stage3_on_main.py).  Data-free.
The note: Y_f(tau + 5, w) = phi_f(w) U_L Y_f(tau, w) U_R^dagger with unitaries the same at every w; phi is trivial for
down (1^2 + 2^2 = 5) and takes three values {1, e^{+4 pi i/5}, e^{-4 pi i/5}} on the strata |5 w1| = 0, 1, 2 for up
(1^2 + 4^2 = 17).  It prints the closed form exp(-85 pi i w1^2) = exp(+(4 pi i/5)(5 w1)^2); the two sides of that are
compared here as numbers, and both with the phases main measures."""
import sys, pathlib, functools, cmath, math
from fractions import Fraction as Fr
import numpy as np
print = functools.partial(print, flush=True)
sys.path.insert(0, str(next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file()) / "frontier/B1957_the_seats_claims_register/verification/checks"))
import wb2_stage3_on_main as W
P5 = [(Fr(i, 5), Fr(j, 5)) for i in range(5) for j in range(5) if (i, j) != (0, 0)]

if __name__ == "__main__":
    for name, (ql, qr) in (("down", (1, 2)), ("up", (1, -4))):
        Y0, Y5 = {}, {}
        for (a, b) in P5:
            Y0[(a, b)] = W.coupling("0.13", 1.70, a, b, ql, qr, False)["S"]; Y5[(a, b)] = W.coupling("5.13", 1.70, a, b, ql, qr, False)["S"]
        w0 = (Fr(0), Fr(1, 5)); i0, i5 = np.linalg.inv(Y0[w0]), np.linalg.inv(Y5[w0]); strata = {0: set(), 1: set(), 2: set()}; unit = eig = 0.0
        for w in P5:
            A0, A5 = Y0[w] @ i0, Y5[w] @ i5; ph = np.trace(A5) / np.trace(A0); unit = max(unit, abs(abs(ph) - 1))
            e0, e5 = np.sort_complex(np.linalg.eigvals(A0) * ph), np.sort_complex(np.linalg.eigvals(A5)); eig = max(eig, np.abs(e0 - e5).max() / np.abs(e5).max())
            k = int(w[0] * 5); strata[min(k, 5 - k)].add(round((cmath.phase(ph) / (2 * math.pi) + 0.5) % 1.0 - 0.5, 6) + 0.0)
        print("%s: Y(tau + 5, w) Y(tau + 5, w0)^-1 against Y(tau, w) Y(tau, w0)^-1, w0 = (0, 1/5): the eigenvalues are the same up to one scalar (to %.1e) of modulus 1 (to %.1e); its phase/2 pi on the strata |5 w1| = 0, 1, 2: %s" % (name, eig, unit, {k: sorted(v) for k, v in strata.items()}))
    for k in (1, 2):
        lhs = cmath.exp(-85j * math.pi * (k / 5) ** 2); rhs = cmath.exp(4j * math.pi / 5 * k * k); f = lambda z: (cmath.phase(z) / (2 * math.pi) + 0.5) % 1 - 0.5
        print("the note's printed closed form at 5 w1 = %d: exp(-85 pi i w1^2) has phase/2 pi = %+.4f; exp((4 pi i/5)(5 w1)^2) has %+.4f: the two sides %s" % (k, f(lhs), f(rhs), "agree" if abs(lhs - rhs) < 1e-12 else "DIFFER"))
