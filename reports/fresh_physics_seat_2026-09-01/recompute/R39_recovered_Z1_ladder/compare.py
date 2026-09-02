#!/usr/bin/env python3
"""R39 — compare the recovered (deleted) cell's partial.json against this bench's rerun of the same script."""
import json, sys
orig = {x['k']: x for x in json.load(open('partial_original.json'))}
new = {x['k']: x for x in json.load(open('partial_rerun.json'))}
rows = []
for k in sorted(set(orig) | set(new)):
    o, n = orig.get(k), new.get(k)
    rows.append((k, o and o['Z'], n and n['Z'], o and o.get('cert'), n and n.get('cert'), (o and n and o['Z'] == n['Z'])))
    print('k=%2d  original Z=%-12s rerun Z=%-12s cert %s/%s  agree %s' % rows[-1])
print('agree on %d of %d shared k' % (sum(1 for r in rows if r[5]), sum(1 for r in rows if r[1] is not None and r[2] is not None)))
