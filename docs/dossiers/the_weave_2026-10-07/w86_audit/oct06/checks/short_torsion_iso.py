"""Audit: long vs short presentation torsion compared as abstract groups (prime-power decomposition)."""
import sys, json
from sympy import factorint
sys.path.insert(0, sys.argv[1])
import first_background as F, short_cover
def inv(ts):
    out = []
    for t in ts:
        for p, e in factorint(t).items(): out.append(p ** e)
    return sorted(out)
cells = set()
for f in ('control.json', 'family.json', 'orbit_law.json', 'recheck_zeros.json'):
    for r in json.load(open(sys.argv[1] + '/' + f)): cells.add((F.ROOTS.get(r['root'], r['root']), r['n']))
cells |= {('LLRR', 4), ('LLLRRR', 3), ('ILLLRRR', 3)}
ok = 0
for w, n in sorted(cells):
    phi = F.mono(w); tl = F.torsion(phi, n)[0]
    keep = F.bundle_cover; F.bundle_cover = short_cover.short_cover; ts = F.torsion(phi, n)[0]; F.bundle_cover = keep
    ok += inv(tl) == inv(ts)
    if inv(tl) != inv(ts): print('NOT ISOMORPHIC', w, n, tl, ts)
print(f"cells {len(cells)}: fibre torsion of long and short presentations isomorphic on {ok}")
