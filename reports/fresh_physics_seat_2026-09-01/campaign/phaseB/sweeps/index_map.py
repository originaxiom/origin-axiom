#!/usr/bin/env python3
"""Map every sweep index (the key of VERDICTS.tsv) to its row in the CURRENT synthesis/absence_claims.tsv.
Why: rollup.py regenerates absence_claims.tsv with packets in sorted order, so the row index shifted between sweep
parts (p1 rows 249-544 -> +441, p2 -> +179, p3 -> +54, p4/p5 -> 0).  Sweep tsvs carry the true quote, so the
(arc, quote) key is stable.  Writes sweep_index_map.tsv: i, part, claim_index, dup_of (first sweep index with the same key)."""
import csv, os
OFFS = [('absence_sweep.tsv', 'p1', 0), ('absence_sweep_p2.tsv', 'p2', 545), ('absence_sweep_p3.tsv', 'p3', 1068), ('absence_sweep_p4.tsv', 'p4', 1374), ('absence_sweep_p5.tsv', 'p5', 1535)]
cur = list(csv.DictReader(open('../synthesis/absence_claims.tsv'), delimiter='\t'))
idx = {}
for i, c in enumerate(cur): idx.setdefault((c['arc'], c['quote'].strip()), i)
first, out = {}, []
for f, part, off in OFFS:
    if not os.path.exists(f): continue
    for k, r in enumerate(csv.DictReader(open(f), delimiter='\t')):
        i = off + k; key = (r['arc'], r['quote'].strip())
        out.append((i, part, idx.get(key, -1), first.get(key, '')))
        first.setdefault(key, i)
with open('sweep_index_map.tsv', 'w') as fh:
    fh.write('i\tpart\tclaim_index\tdup_of\n')
    for row in out: fh.write('\t'.join(map(str, row)) + '\n')
covered = {r[2] for r in out if r[2] >= 0}
print('sweep rows', len(out), 'distinct claims covered', len(covered), 'of', len(cur), 'duplicates', sum(1 for r in out if r[3] != ''), 'unmatched', sum(1 for r in out if r[2] < 0))
print('UNCOVERED claim rows:', [i for i in range(len(cur)) if i not in covered][:20], '...')
