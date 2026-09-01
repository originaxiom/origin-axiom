#!/usr/bin/env python3
"""R33b — B307: 'of 500 cusped manifolds, 32 have degree-3 trace fields, all signature (1,1), 0 cyclic'.
Recompute over OrientableCuspedCensus[:500]: shape-field (= invariant trace field) degree, signature for cubics."""
import json, os, time, collections
import snappy
from r33_lib import shape_field
HERE = os.path.dirname(os.path.abspath(__file__))
t0 = time.time(); rows = []; degs = collections.Counter(); cubic_sigs = collections.Counter(); fails = []
for i, M in enumerate(snappy.OrientableCuspedCensus[:500]):
    try:
        f = shape_field(M, bits=800, maxdeg=16)
    except Exception as e:
        f = None; fails.append((M.name(), repr(e)[:80]))
    if f is None: degs['FAIL'] += 1; rows.append((M.name(), None, None, None)); continue
    degs[f['degree']] += 1
    if f['degree'] == 3: cubic_sigs[tuple(f['signature'])] += 1
    rows.append((M.name(), f['degree'], f['poly'], f['signature']))
    if i % 50 == 0: print(i, dict(degs), '%.0fs' % (time.time() - t0), flush=True)
res = dict(n=500, degree_counts=dict(degs), cubic_signatures={str(k): v for k, v in cubic_sigs.items()}, fails=fails,
           bank=dict(cubic=32, signature='(1,1) all', cyclic=0), rows=rows)
json.dump(res, open(HERE + '/r33_census.json', 'w'), indent=1, default=str)
open(HERE + '/r33_census_out.txt', 'w').write('degree counts %s\ncubic signatures %s (cyclic cubics are totally real (3,0): count %d)\nfails %s\n' % (
    dict(degs), dict(cubic_sigs), cubic_sigs[(3, 0)], fails))
print('done', dict(degs), dict(cubic_sigs), '%.0fs' % (time.time() - t0))
