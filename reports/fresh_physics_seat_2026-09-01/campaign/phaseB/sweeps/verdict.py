#!/usr/bin/env python3
"""Append seat verdicts: python3 verdict.py '<i>|<VERDICT>|<note>' ...   (VERDICT in NOISE, CONSISTENT, STANDS,
SUPERSEDED, CONTRADICTED, OPEN_LATER, GENERIC, REGISTRY_ECHO).  Writes/updates VERDICTS.tsv keyed by claim index."""
import sys, csv, json, os
recs = {r['i']: r for r in json.load(open('absence_sweep_paths.json'))}
rows = {}
if os.path.exists('VERDICTS.tsv'):
    for r in csv.DictReader(open('VERDICTS.tsv'), delimiter='\t'): rows[int(r['i'])] = r
for a in sys.argv[1:]:
    i, v, note = a.split('|', 2); i = int(i)
    rows[i] = dict(i=i, arc=recs[i]['arc'], where=recs[i]['where'], status=recs[i]['status'], verdict=v.strip(), note=note.strip())
with open('VERDICTS.tsv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=['i', 'arc', 'where', 'status', 'verdict', 'note'], delimiter='\t', lineterminator='\n'); w.writeheader()
    for i in sorted(rows): w.writerow(rows[i])
print('verdicts', len(rows))
