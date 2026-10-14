"""Audit: long (bundle of phi^n) vs short (cyclic cover) presentations give the same fibre torsion, on every cell of the record."""
import sys, json
sys.path.insert(0, sys.argv[1])
import first_background as F, short_cover
cells = set()
for f in ('control.json', 'family.json', 'orbit_law.json', 'recheck_zeros.json'):
    for r in json.load(open(sys.argv[1] + '/' + f)): cells.add((F.ROOTS.get(r['root'], r['root']), r['n']))
cells |= {('LLRR', 4), ('LLLRRR', 3), ('ILLLRRR', 3)}
ok = 0
for w, n in sorted(cells, key=lambda c: (len(c[0]), c)):
    phi = F.mono(w)
    tl = F.torsion(phi, n)[0]
    long_cover = F.bundle_cover; F.bundle_cover = short_cover.short_cover
    ts = F.torsion(phi, n)[0]
    F.bundle_cover = long_cover
    ok += (sorted(tl) == sorted(ts))
    if sorted(tl) != sorted(ts): print('MISMATCH', w, n, tl, ts)
print(f"cells {len(cells)}: torsion long == short on {ok}")
