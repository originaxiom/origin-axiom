#!/usr/bin/env python3
"""Aggregate the Phase E journal: results/flags_verified.tsv (all rows) + results/UNCAUGHT.md (the rows the seat judges).
Usage: aggregate.py <journal.jsonl>"""
import json, sys, csv, collections
rows = {}
for line in open(sys.argv[1]):
    e = json.loads(line); r = e.get('result') or e.get('value') or {}
    if isinstance(r, dict) and 'results' in r:
        for x in r['results']: x = dict(x); x['packet'] = r['packet']; rows.setdefault(x['i'], x)
rows = [rows[k] for k in sorted(rows)]
with open('results/flags_verified.tsv', 'w', newline='') as f:
    w = csv.writer(f, delimiter='\t', lineterminator='\n'); w.writerow(['i', 'packet', 'arc', 'kind', 'premise', 'classification', 'note', 'quoted', 'files_read'])
    for x in rows: w.writerow([x['i'], x['packet'], x['arc'], x['kind'], x['premise'], x['classification'], x['note'].replace('\n', ' '), x['quoted'].replace('\n', ' / '), ';'.join(x.get('files_read') or [])])
cc = collections.Counter(x['classification'] for x in rows); kk = collections.Counter((x['kind'], x['classification']) for x in rows)
with open('results/UNCAUGHT.md', 'w') as f:
    f.write('# Phase E — UNCAUGHT flags (auto; the seat judges these in IDENTIFICATION_LEDGER.md)\n\nflags verified %d: %s\n\n' % (len(rows), ', '.join('%s %d' % kv for kv in cc.most_common())))
    f.write('by kind × class: ' + ', '.join('%s/%s %d' % (k[0][:10], k[1], v) for k, v in sorted(kk.items())) + '\n\n')
    for kind in ('IDENTIFICATION_BY_TYPE', 'CLAIM_EXCEEDS_COMPUTATION', 'FITTED_VALUE', 'SELF_REFERENTIAL_LOCK'):
        f.write('## %s\n\n' % kind)
        for x in rows:
            if x['classification'] == 'UNCAUGHT' and x['kind'] == kind: f.write('- **#%d %s** — %s\n  - quoted: %s\n' % (x['i'], x['arc'], x['note'].replace('\n', ' '), x['quoted'].replace('\n', ' / ')[:500]))
        f.write('\n')
print(len(rows), dict(cc))
