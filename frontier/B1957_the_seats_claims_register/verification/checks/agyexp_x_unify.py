"""B1957: agy-exp's X-UNIFY campaign (four result notes, read in full through the mask): the exact facts under its
statements that main's other checks do not already hold.  Nothing of the seat's is run.  (The bijection x = 3u + 5v
and the factorised generators, the doubled shear, the anomaly sums and the one-loop relation with its Pati-Salam
term are in physical_state_orbit.py, physical_all_seats_refresh.py and the lock.)
 U1  tr (6Y)^2 = 30 and tr Y^2 = 5/6 on the five; the cubic anomaly 4 (3a + 2b)((3a + b)^2 + 4b^2) is -32 at
     (a, b) = (-1, 1), and its second factor vanishes only at a = b = 0.
 U2  frame C's whole-orbit least exponents from MAIN'S OWN rule (B1788's tropical rule), in both readings, at the
     points of exact order 5, 10 and 15: the note's table.
 U3  for Hermitian H_1, H_2 the traces of H_1, H_1^2 and H_1 H_2 are real, so Im tr(Y^-1 p(H_1, H_2) Y) = 0 for a
     real-coefficient combination of 1, H_1, H_2, H_1^2, H_2^2 and of H_1 H_2 with H_2 H_1."""
import functools, math, pathlib, sys
from fractions import Fraction as Fr
import numpy as np
import sympy as sp
print = functools.partial(print, flush=True)
SEC = {"sec1": (1, -4), "sec2": (1, 2), "sec3": (-3, 6)}
def prim(N): return [(a, b) for a in range(N) for b in range(N) if math.gcd(math.gcd(a, b), N) == 1]

if __name__ == "__main__":
    Y6 = sp.diag(-2, -2, -2, 3, 3); a, b = sp.symbols("a b", real=True); cub = 4 * (3 * a + 2 * b) * ((3 * a + b) ** 2 + 4 * b ** 2)
    print("U1: tr (6Y)^2 = %s, tr Y^2 = %s; the cubic at (-1, 1): %s; the second factor is zero only at %s" % ((Y6 ** 2).trace(), (Y6 ** 2).trace() / 36, cub.subs({a: -1, b: 1}), sp.solve([3 * a + b, b], [a, b])))
    ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
    sys.path.insert(0, str(next((ROOT / "frontier").glob("B1788_*")) / "verification")); import tropical as T
    out = []
    for rd in ("S", "St"):
        P = T.polys(rd)
        for N in (5, 10, 15):
            row = []
            for s in ("sec2", "sec3"):
                l, r = SEC[s]; ex = [T.predict(P, T.E(l * Fr(x, N), r * Fr(x, N))) for x, y in prim(N)]; row.append("%s [%s, %s]" % (s, min(e[0] for e in ex), min(e[1] for e in ex)))
            out.append("%s order %d: %s" % (rd, N, ", ".join(row)))
    print("U2: least exponents over the points of each order: " + "; ".join(out))
    rng = np.random.default_rng(7); worst = 0
    for _ in range(50):
        Y1, Y2 = (rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3)) for _ in range(2)); H1, H2 = Y1 @ Y1.conj().T, Y2 @ Y2.conj().T; c = rng.normal(size=6)
        p = c[0] * np.eye(3) + c[1] * H1 + c[2] * H2 + c[3] * H1 @ H1 + c[4] * H2 @ H2 + c[5] * (-0.25 * H1 @ H2 - H2 @ H1)
        worst = max(worst, abs(np.trace(np.linalg.inv(Y1) @ p @ Y1).imag) / abs(np.trace(p)))
    print("U3: over 50 random pairs the largest |Im tr(Y^-1 p Y)| / |tr p| is %.1e" % worst)
