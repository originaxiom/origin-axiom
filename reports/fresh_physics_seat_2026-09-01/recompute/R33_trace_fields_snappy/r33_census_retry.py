#!/usr/bin/env python3
"""R33c — retry the census rows that returned no field at (800 bits, maxdeg 16): 2400 bits, maxdeg 48."""
import json, collections, time
import snappy
from r33_lib import shape_field, shape_field_oneshot
res = json.load(open('r33_census.json'))
t0 = time.time(); degs = collections.Counter(); still = []
for i, row in enumerate(res['rows']):
    if row[1] is not None: degs[row[1]] += 1; continue
    if i % 20 == 0: print(i, dict(degs), '%.0fs' % (time.time()-t0), flush=True)
    M = snappy.Manifold(row[0])
    try: f = shape_field_oneshot(M, bits=2000, deg=40)
    except Exception as e: f = None
    if f is None: degs['UNDETERMINED(>40 or non-geometric)'] += 1; still.append(row[0]); res['rows'][i] = (row[0], None, 'undetermined', None)
    else: degs[f['degree']] += 1; res['rows'][i] = (row[0], f['degree'], f['poly'], f['signature'])
res['degree_counts_after_retry'] = {str(k): v for k, v in degs.items()}; res['undetermined'] = still
json.dump(res, open('r33_census.json', 'w'), indent=1, default=str)
cub = [r for r in res['rows'] if r[1] == 3]
open('r33_census_out.txt', 'a').write('after retry (2000 bits, one-shot algdep 40): %s\nundetermined: %s\ncubic rows: %s\n' % (dict(degs), still, [r[0] for r in cub]))
print('done', dict(degs), 'undetermined', len(still), '%.0fs' % (time.time() - t0))
