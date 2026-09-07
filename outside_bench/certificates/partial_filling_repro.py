#!/usr/bin/env python3
"""REPRODUCTION TABLE for the partial-filling result -- canonical identifiers, no `break`.

Two defects in the first pass (certificates/partial_filling_joint.py) are fixed here:
  * it broke after the FIRST working slope per cover, so its "22" counted
    (cover, first-working-slope) pairs, not a census;
  * it identified covers by SnapPy's enumeration-order names (m004~irr~3), which are
    NOT stable across runs or versions.
Covers are identified here by triangulation_isosig(), which is canonical, plus volume
and homology so a reader can cross-check without trusting the isosig alone.

PREDICATE (from B1227): M amphichiral => 2*CS = 0 in R/(1/2)Z => CS in {0, 1/4}.
Contrapositive, which is what is being tested: CS NOT in {0,1/4} mod 1/2 => NOT amphichiral.
"""
import snappy

def dist_to_amphi(c):
    c = float(c) % 0.5
    return min(abs(c-0.0), abs(c-0.25), abs(c-0.5))

base = snappy.Manifold('m004')
SLOPES = [(1,0),(1,1),(2,1),(3,1),(1,2),(3,2)]
rows = []
for deg in range(4, 9):
    for C in base.covers(deg):
        if C.num_cusps() < 2:
            continue
        try: iso = C.triangulation_isosig()
        except Exception: iso = "?"
        try: hom = str(C.homology())
        except Exception: hom = "?"
        cvol = float(C.volume())
        for ci in range(C.num_cusps()):
            for sl in SLOPES:
                N = C.copy()
                try: N.dehn_fill(sl, ci)
                except Exception: continue
                st = str(N.solution_type())
                try:
                    cs = float(N.chern_simons()); vol = float(N.volume())
                except Exception:
                    continue
                left = sum(1 for x in N.cusp_info('is_complete') if x)
                if left < 1: continue
                pos = (st == 'all tetrahedra positively oriented')
                rows.append(dict(deg=deg, iso=iso, cvol=cvol, hom=hom, ncusp=C.num_cusps(),
                                 cusp=ci, slope=sl, left=left, st=st, cs=cs, vol=vol,
                                 d=dist_to_amphi(cs), pos=pos))

strict = [r for r in rows if r['pos'] and r['d'] > 1e-6]
print(f"total (cover, cusp, slope) attempts returning a CS : {len(rows)}")
print(f"STRICT survivors (positively oriented AND CS not in {{0,1/4}}): {len(strict)}")
print(f"distinct covers among strict survivors: {len({r['iso'] for r in strict})}\n")

print("STRICT SURVIVORS -- canonical identifiers")
print(f"{'deg':>3} {'cusps':>5} {'cusp':>4} {'slope':>7} {'left':>4} {'CS':>13} {'dist':>9}  isosig")
seen = set()
for r in sorted(strict, key=lambda r: (r['deg'], r['iso'], r['cusp'], r['slope'])):
    k = (r['iso'], r['cusp'], r['slope'])
    if k in seen: continue
    seen.add(k)
    print(f"{r['deg']:>3} {r['ncusp']:>5} {r['cusp']:>4} {str(r['slope']):>7} {r['left']:>4} "
          f"{r['cs']:>+13.9f} {r['d']:>9.6f}  {r['iso']}")

print("\n--- THE WITHDRAWN +-1/24 CASE, located so it can be checked and rejected ---")
cands = [r for r in rows if abs(abs(r['cs']) - 1/24) < 1e-6]
if not cands:
    print("  no CS within 1e-6 of +-1/24 in this run")
for r in cands:
    print(f"  deg {r['deg']} cover, {r['ncusp']} cusps, isosig {r['iso']}")
    print(f"    homology {r['hom']}, cover volume {r['cvol']:.9f}")
    print(f"    fill cusp {r['cusp']} slope {r['slope']} -> {r['left']} cusp(s) left, filled vol {r['vol']:.9f}")
    print(f"    CS = {r['cs']:+.9f}   solution_type = '{r['st']}'")
    print(f"    positively oriented? {r['pos']}   -> {'COUNTS' if r['pos'] else 'REJECTED: not a verified geometric solution'}")
