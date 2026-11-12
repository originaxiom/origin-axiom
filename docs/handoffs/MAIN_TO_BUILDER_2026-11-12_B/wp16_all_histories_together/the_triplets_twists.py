#!/usr/bin/env python3
"""WP-1.6: the record's triplet among its 24 twists, under the two moves.

The twist by the character chi_m sends L to zeta^m L and R to zeta^-m R (zeta a primitive 24th root of unity; these are
the characters of the three-strand braid group that B1866 uses).  For each m: the central scalar c = S^2, the group the
two matrices generate (its order, by closure), the eigenvalues of the averaged move and the rate.  The record's triplet
is m = 0; B1866 found its twists of order 96 to be m = 0, 6, 12, 18.  Nothing is compared with a measured number."""
import cmath, importlib.util, json, math, pathlib
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent; ROOT = HERE.parents[1]
spec = importlib.util.spec_from_file_location("hands", ROOT / "frontier/B1610_the_hands_on_the_founding_torsor/verification/hands_on_the_torsor.py")
H = importlib.util.module_from_spec(spec); spec.loader.exec_module(H)
TB = H.PIECES["T"]; TL, TR = TB.conj().T @ H.W.ML @ TB, TB.conj().T @ H.W.MR @ TB
z = cmath.exp(2j * math.pi / 24); I3 = np.eye(3)
def order(gens, cap=3000):
    key = lambda M: tuple(np.round(M.flatten(), 6).view(float)); seen = {key(I3): I3}; fr = [I3]
    while fr and len(seen) <= cap:
        nxt = []
        for g in fr:
            for h in gens:
                x = g @ h; k = key(x)
                if k not in seen: seen[k] = x; nxt.append(x)
        fr = nxt
    return len(seen) if len(seen) <= cap else None
rows = []
for m in range(24):
    L, R = z ** m * TL, z ** (-m) * TR
    S = L @ np.linalg.inv(R) @ L; c = (S @ S)[0, 0]
    ev = np.linalg.eigvals((L + R) / 2); rate = float(max(abs(ev)))
    rows.append({"m": m, "c = S^2": [round(float(c.real), 6), round(float(c.imag), 6)], "order of the group": order([L, R]), "rate": round(rate, 9),
                 "moduli": sorted((round(float(abs(x)), 9) for x in ev), reverse=True), "real eigenvalues": sum(1 for x in ev if abs(x.imag) < 1e-9)})
    print("m = %2d  c = %-16s group of order %-5s rate %.9f  moduli %s  real eigenvalues: %d" % (m, np.round(c, 3), rows[-1]["order of the group"], rate, rows[-1]["moduli"], rows[-1]["real eigenvalues"]))
import collections
print("the rates that occur:", sorted(collections.Counter(r["rate"] for r in rows).items(), reverse=True))
json.dump(rows, open(HERE / "the_triplets_twists.json", "w"), indent=1)
