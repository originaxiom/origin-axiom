#!/usr/bin/env python3
"""Render the substantive LEADs of the W-E sweep compactly for the seat's hand verdicts:
one block per lead with the claim quote, the terms, and the substantive hit paths (catch-all files removed).
Usage: python3 render_leads.py [start] [count]  -> prints leads[start:start+count]."""
import json, sys, csv
SUF = sys.argv[3] if len(sys.argv) > 3 else ''
recs = json.load(open('absence_sweep_paths%s.json' % SUF))
rows = {}
for _f, _off in [('absence_sweep.tsv', 0), ('absence_sweep_p2.tsv', 545), ('absence_sweep_p3.tsv', 1068), ('absence_sweep_p4.tsv', 1374), ('absence_sweep_p5.tsv', 1535)]:
    try:
        for _k, _r in enumerate(csv.DictReader(open(_f), delimiter='\t')): rows[_off + _k] = _r
    except FileNotFoundError: pass
leads = [r for r in recs if r['status'] == 'LEAD']
start = int(sys.argv[1]) if len(sys.argv) > 1 else 0; count = int(sys.argv[2]) if len(sys.argv) > 2 else 40
for r in leads[start:start + count]:
    q = rows[r['i']]['quote']
    print('#%d [%s] %s' % (r['i'], r['arc'], r['where'].split('/')[-1][:50]))
    print('   Q: %s' % q[:260].replace('\n', ' '))
    print('   terms: %s | content hits %d, registry %d, catch-all %d%s' % (' '.join(r['terms']), len(r.get('content', [])), len(r.get('registry', [])), r['catchall_hits'], (' | DELETED: ' + ', '.join(r['deleted'])) if r['deleted'] else ''))
    paths = r.get('content', r['substantive'])
    print('   hits: %s%s' % (' ; '.join(p.replace('frontier/', 'f/') for p in paths[:10]), ' ; ...' if len(paths) > 10 else ''))
