"""B1957: the web seat's W-C5 (B1914's eight classes, B1915's orbits, the cusp statement), on main.  Data-free; exact.
 C1  the eight classes +-J^n K^e of the normaliser of <LR>: orientation sign det X * e (e = +1 if X commutes with the
     act, -1 if it inverts it); the keeping classes act on the line of (1, 2) mod 5 by +-1 and the reversing by +-2.
 C2  the labelling of the second side's line: main's B1915 uses D(1, 2) = (1, 3) mod 5, the seat's basis; in main's
     own run an orientation-keeping map between the sides swaps the twin's label, as the seat found.
 C3  the cusp statement: for integers a, n the tail integral of exp(-(a - 2n) t) t^(a - 2) over (T, oo) is finite
     exactly when a - 2n > 0, or a = 2n and a <= 0 (by hand: the exponential decides unless its rate is 0, and then
     the power t^(a - 2) is integrable exactly when a - 2 < -1).  That condition is n <= b(a), b(a) = (a - 1)//2 for
     a >= 1 and a//2 for a <= 0, on the grid -40 <= a, n <= 40; the control b'(a) = a//2 differs exactly at even a >= 2.
     Numerically (mpmath, 40 digits) at the boundary 2n = a: the partial integrals to 10^3, 10^6, 10^9 converge for
     a <= 0 and grow for a >= 1."""
import json, pathlib
import mpmath as mp
import numpy as np
mp.mp.dps = 40
HERE = pathlib.Path(__file__).resolve().parent
if __name__ == "__main__":
    J = np.array([[1, 1], [1, 0]], dtype=object); K = np.array([[0, 1], [-1, 0]], dtype=object); A = np.array([[2, 1], [1, 1]], dtype=object); Ai = np.array([[1, -1], [-1, 2]], dtype=object)
    rows = []
    for sg in (1, -1):
        for n in (0, 1):
            for e in (0, 1):
                X = sg * np.linalg.matrix_power(J, n).dot(np.linalg.matrix_power(K, e)); d = int(X[0, 0] * X[1, 1] - X[0, 1] * X[1, 0]); Xi = np.array([[X[1, 1], -X[0, 1]], [-X[1, 0], X[0, 0]]], dtype=object) * d
                C = X.dot(A).dot(Xi); ex = 1 if (C == A).all() else (-1 if (C == Ai).all() else None); v = (int(X[0, 0] + 2 * X[0, 1]) % 5, int(X[1, 0] + 2 * X[1, 1]) % 5); sc = next(s for s in range(1, 5) if v == (s % 5, (2 * s) % 5))
                rows.append((sg, n, e, d * ex, sc))
    print("C1: (sign, n, e): orientation sign, scalar on the line of (1, 2) mod 5: %s" % {r[:3]: r[3:] for r in rows})
    print("C1: every keeping class acts by 1 or 4 and every reversing class by 2 or 3: %s; the opposite statement: %s" % (all((r[4] in (1, 4)) == (r[3] == 1) for r in rows), all((r[4] in (2, 3)) == (r[3] == 1) for r in rows)))
    root = HERE.parents[2]; run = next(root.glob("B1915_*/verification/the_hand_rows.json")); res = json.loads(run.read_text())
    keep = res["orbits_under_orientation_keeping_maps"]
    print("C2: main's B1915 labels the second side's line by D(1, 2) = (1, -2) = (1, 3) mod 5 (its BASE); its run: %d orbits under every map, %d under the orientation-keeping ones; each of those holds one placement of each side with the twin's label swapped: %s" % (
        len(res["orbits_under_every_map"]), len(keep), all(len(o) == 2 and {p.split(",")[0] for p in o} == {"+ side", "- side"} and {p.split(", ")[2] for p in o} == {"v", "2v"} and len({p.split(", ")[1] for p in o}) == 1 for o in keep)))
    b = lambda a: (a - 1) // 2 if a >= 1 else a // 2; fin = lambda a, n: (a - 2 * n > 0) or (a == 2 * n and a <= 0); G = range(-40, 41)
    diff = sorted({a for a in G for n in G if fin(a, n) != (n <= a // 2)})
    print("C3: on the grid -40..40: [finite] = [n <= b(a)] at every point: %s; the control b'(a) = a//2 differs exactly at the even a >= 2: %s" % (all(fin(a, n) == (n <= b(a)) for a in G for n in G), diff == [a for a in G if a >= 2 and a % 2 == 0]))
    out = {}
    for a in (-4, -2, 0, 2, 4):
        part = [mp.quad(lambda t: t ** (a - 2), [1, T]) for T in (mp.mpf(10) ** 3, mp.mpf(10) ** 6, mp.mpf(10) ** 9)]; out[a] = [mp.nstr(x, 8) for x in part]
    print("C3: at the boundary 2n = a, the partial integrals of t^(a - 2) from 1 to 10^3, 10^6, 10^9: %s" % out)
