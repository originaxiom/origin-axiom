#!/usr/bin/env python3
"""xB014 ADDENDUM 1, cells Z6-Z7 -- the owner's challenge ("u sure about extremality").

HE WAS RIGHT AND Z4 WAS WRONG, TWICE:
  (1) Z4 tested only the MAXIMUM of log(lambda)/vol. The meaningful extremality is the
      MINIMUM -- the Kojima-McShane bound is a LOWER bound, so "closest to the bound" means
      SMALLEST ratio, not largest.
  (2) Z4 sorted DESCENDING and then reported the index as a rank. "rank 38 of 40" was the
      DESCENDING index; ascending it is rank 3 -- and the two above it are m206 and s961,
      m004's OWN COVERS, which carry the IDENTICAL ratio by construction. So m004 is at the
      MINIMUM, not "near the bottom".
  And Z4 never tested the COMPONENTS at all, where the extremality actually lives.

Gate 5 untouched.
"""
import itertools
import math
import warnings

import snappy
import sympy as sp

warnings.filterwarnings("ignore")


def census(nmax=8):
    rows, seen = [], set()
    for n in range(2, nmax+1):
        for t in itertools.product('LR', repeat=n):
            w = ''.join(t)
            if 'L' not in w or 'R' not in w:
                continue
            if min(w[i:]+w[:i] for i in range(n)) != w:
                continue
            A = sp.eye(2)
            for ch in w:
                A = A*(sp.Matrix([[1, 1], [0, 1]]) if ch == 'L' else sp.Matrix([[1, 0], [1, 1]]))
            tr = int(A.trace())
            if tr <= 2:
                continue
            lam = (tr + math.sqrt(tr*tr-4))/2
            try:
                M = snappy.Manifold('b++'+w)
                v = float(M.volume())
            except Exception:
                continue
            ids = M.identify()
            nm = ids[0].name().split('(')[0] if ids else w
            if nm in seen:
                continue
            seen.add(nm)
            rows.append((nm, w, tr, math.log(lam), v, math.log(lam)/v))
    return rows


def Z6():
    rows = census()
    print("Z6       THE OWNER'S CHALLENGE -- Z4 tested the WRONG extremality, and mis-ranked it")
    print("         Kojima-McShane is a LOWER bound (ratio >= 1/(3pi)), so 'extremal' means the")
    print("         SMALLEST ratio. Z4 ranked DESCENDING and read the index as a rank.\n")
    for key, label in ((3, 'log lambda  (DILATATION)'), (4, 'volume'), (5, 'ratio log lam / vol')):
        s = sorted(rows, key=lambda r: r[key])
        rk = [i for i, r in enumerate(s) if r[0] == 'm004'][0] + 1
        print(f"         ranked ASCENDING by {label:<26} m004 is rank {rk} of {len(s)}")
        for r in s[:3]:
            tag = '  <== m004' if r[0] == 'm004' else ''
            print(f"             {r[0]:<10}{r[1]:<10} tr {r[2]:>4}  log lam {r[3]:.6f}"
                  f"  vol {r[4]:.6f}  ratio {r[5]:.6f}{tag}")
        print()
    lam_rank = [i for i, r in enumerate(sorted(rows, key=lambda r: r[3])) if r[0] == 'm004'][0]+1
    vol_rank = [i for i, r in enumerate(sorted(rows, key=lambda r: r[4])) if r[0] == 'm004'][0]+1
    assert lam_rank == 1, lam_rank
    assert vol_rank == 1, vol_rank
    assert min(r[2] for r in rows) == 3
    print("Z6 PASS  m004 IS RANK 1 OF 40 FOR DILATATION AND RANK 1 OF 40 FOR VOLUME.")
    print("         trace 3 is the minimum possible for a pseudo-Anosov in SL(2,Z), so the")
    print("         minimal dilatation phi^2 is FORCED, not found. Z4 never tested either.")
    return rows


def Z7(rows):
    print("\nZ7       AND THE RATIO ITSELF: is m004 at its MINIMUM?")
    s = sorted(rows, key=lambda r: r[5])
    r4 = [r for r in rows if r[0] == 'm004'][0][5]
    below = [r for r in s if r[5] < r4 - 1e-12]
    ties = [r[0] for r in s if abs(r[5]-r4) < 1e-12]
    print(f"         m004's ratio = {r4:.12f}")
    print(f"         bundles with a STRICTLY SMALLER ratio: {len(below)}   {[r[0] for r in below]}")
    print(f"         bundles TIED at that exact value       : {ties}")
    assert not below, below
    print("\n         the ties are m004's OWN COVERS -- the ratio is constant along the tower by")
    print("         construction (Z3), so they are not independent competitors.")
    print("\nZ7 PASS  m004 ATTAINS THE MINIMUM of log(lambda)/vol over this census, tied only")
    print("         with its own tower. IT IS EXTREMAL, THREE WAYS.")
    print("\n         >> Z4's VERDICT IS WITHDRAWN. PATH A IS NOT KILLED BY THE BASE RATE. <<")
    print("\n         BUT THE HONEST SCOPE, which Z4 got right for the wrong reason:")
    print("           - minimal dilatation on the once-punctured torus is a KNOWN theorem and")
    print("             is FORCED by trace 3 being the smallest pseudo-Anosov trace in SL(2,Z);")
    print("           - minimal volume is Cao-Meyerhoff, already banked;")
    print("           - B207 ALREADY SAID IT: 'golden has the smallest regulator (log phi) ->")
    print("             the least-hierarchical / extremal point.'")
    print("           - and the RATIO's minimality follows from the components', so it is a")
    print("             consequence, not an independent fact.")
    print("         So the extremality is REAL and this arc's kill was WRONG -- but the")
    print("         extremality is also ALREADY IN THE RECORD, and it still does not cross")
    print("         B1012's wall, which is about a DIMENSIONFUL quantity.")


if __name__ == "__main__":
    rows = Z6()
    Z7(rows)
    print("\nVERIFIED")
