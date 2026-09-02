#!/usr/bin/env python3
"""Review pass: print each verdict row with its TRUE quote (from the sweep tsv, stable) and the hits.
Usage: review_verdicts.py start count [verdicts-to-include e.g. NOISE,CONSISTENT]"""
import csv, sys, json, glob
start, count = int(sys.argv[1]), int(sys.argv[2]); inc = set(sys.argv[3].split(',')) if len(sys.argv) > 3 else None
recs = {}
for f in sorted(glob.glob('absence_sweep_paths*.json')):
    for r in json.load(open(f)): recs[r['i']] = r
rows = [r for r in csv.DictReader(open('VERDICTS.tsv'), delimiter='\t') if start <= int(r['i']) < start + count and (inc is None or r['verdict'] in inc)]
for r in rows:
    rr = recs.get(int(r['i']), {})
    print('#%s [%s] %s\n   Q: %s\n   V: %s — %s\n   hits: %s' % (r['i'], r['arc'], r['where'][-40:], r['quote'][:230].replace('\n', ' '), r['verdict'], r['note'][:150],
          ' ; '.join(p.replace('frontier/', 'f/') for p in rr.get('content', [])[:6]) or '(none)'))
