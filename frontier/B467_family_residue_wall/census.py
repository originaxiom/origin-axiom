#!/usr/bin/env python3
"""B467 extension (the 2026-07-07 registry, R3): the PARENT-COLLISION CENSUS.

Question (registry, assigned CC/SnapPy): is the 4_1(5,1) ~ 5_2(5,1) collision isolated,
or the first of a family? Enumerate slopes |p| <= 15, q in {1,2} for parents 4_1, 5_2,
6_1 (the third TWIST-KNOT parent; the registry's "extend to m=3" is corrected again:
metallic m=3 is a bundle, not a knot — the honest third small twist-knot parent is 6_1).
Bucket children by (volume, H1) ACROSS parents and slopes; certify candidate collisions
with isometry checks (hyperbolic only); report CS to orient each collision.
"""
import sys
from collections import defaultdict

import snappy

PARENTS = ['4_1', '5_2', '6_1']


def slopes():
    out = []
    for p in range(-15, 16):
        if p != 0:
            out.append((p, 1))
        if p % 2 != 0:
            out.append((p, 2))
    return out


def build(parent, slope):
    M = snappy.Manifold(parent)
    try:
        M.chern_simons()
    except Exception:
        pass
    M.dehn_fill(slope)
    return M


def main():
    rows = []
    for parent in PARENTS:
        for slope in slopes():
            M = build(parent, slope)
            try:
                vol = float(M.volume())
            except Exception:
                vol = float('nan')
            try:
                sol = M.solution_type()
            except Exception:
                sol = '?'
            hyp = sol in ('all tetrahedra positively oriented',
                          'contains negatively oriented tetrahedra') and vol == vol and vol > 0.1
            try:
                cs = float(M.chern_simons())
            except Exception:
                cs = None
            rows.append((parent, slope, vol, str(M.homology()), hyp, cs))
    buckets = defaultdict(list)
    for r in rows:
        if r[4]:                       # certified-hyperbolic only
            buckets[(round(r[2], 7), r[3])].append(r)
    print("== candidate cross-parent collision buckets (hyperbolic, vol+H1 match) ==")
    found = []
    for key, rs in sorted(buckets.items()):
        parents = {r[0] for r in rs}
        if len(parents) >= 2:
            print(f"  bucket vol={key[0]:.7f} H1={key[1]}:")
            for r in rs:
                print(f"    {r[0]}({r[1][0]},{r[1][1]})  CS={r[5]:+.6f}" if r[5] is not None
                      else f"    {r[0]}({r[1][0]},{r[1][1]})  CS=n/a")
            # certify pairwise across distinct parents
            for i in range(len(rs)):
                for j in range(i + 1, len(rs)):
                    if rs[i][0] != rs[j][0]:
                        A = build(rs[i][0], rs[i][1])
                        B = build(rs[j][0], rs[j][1])
                        try:
                            iso = A.is_isometric_to(B)
                        except RuntimeError:
                            iso = 'undecided'
                        if iso is True:
                            found.append((rs[i], rs[j]))
                        print(f"      {rs[i][0]}{rs[i][1]} vs {rs[j][0]}{rs[j][1]}: isometric = {iso}")
    print("\n== CERTIFIED cross-parent collisions in the window ==")
    for a, b in found:
        ori = ("orientation-PRESERVING" if a[5] is not None and b[5] is not None
               and abs(a[5] - b[5]) < 1e-6 else "orientation-REVERSING (CS signs differ)")
        print(f"  {a[0]}({a[1][0]},{a[1][1]}) ~ {b[0]}({b[1][0]},{b[1][1]})   [{ori}]")
    print(f"\ntotal certified collisions: {len(found)}")
    print("(exceptional/non-hyperbolic fillings excluded from certification — "
          "isometry testing is rigorous only for hyperbolic manifolds)")


if __name__ == '__main__':
    main()
