#!/usr/bin/env python3
"""Append seat verdicts: python3 verdict.py '<i>|<VERDICT>|<note>' ...   (VERDICT in NOISE, CONSISTENT, STANDS,
SUPERSEDED, CONTRADICTED, OPEN_LATER, GENERIC, REGISTRY_ECHO).  Writes/updates VERDICTS.tsv keyed by claim index."""
import sys, csv, json, os
import glob
recs = {}
for _f in sorted(glob.glob('absence_sweep_paths*.json')):
    for r in json.load(open(_f)): recs[r['i']] = r
_claims = list(csv.DictReader(open('../synthesis/absence_claims.tsv'), delimiter='\t'))
for _f in sorted(glob.glob('absence_sweep*.tsv')):
    if 'trial' in _f or 'v1' in _f: continue
    for _r in csv.DictReader(open(_f), delimiter='\t'):
        _i = int(_r.get('i', -1)) if _r.get('i') else None
        pass
_sweep = list(csv.DictReader(open('absence_sweep.tsv'), delimiter='\t'))
for _i, _r in enumerate(_sweep):
    if _i not in recs: recs[_i] = dict(i=_i, arc=_r['arc'], where=_r['where'], status=_r['status'])
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
