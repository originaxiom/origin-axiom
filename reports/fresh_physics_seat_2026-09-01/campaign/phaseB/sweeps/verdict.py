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
OFFS = [('absence_sweep.tsv', 0), ('absence_sweep_p2.tsv', 545), ('absence_sweep_p3.tsv', 1068), ('absence_sweep_p4.tsv', 1374), ('absence_sweep_p5.tsv', 1535)]
for _f, _off in OFFS:   # fallback rows (UNSWEEPABLE claims are not in the paths json)
    if os.path.exists(_f):
        for _k, _r in enumerate(csv.DictReader(open(_f), delimiter='\t')):
            _i = _off + _k
            if _i not in recs: recs[_i] = dict(i=_i, arc=_r['arc'], where=_r['where'], status=_r['status'])
rows = {}
if os.path.exists('VERDICTS.tsv'):
    for r in csv.DictReader(open('VERDICTS.tsv'), delimiter='\t'): rows[int(r['i'])] = r
for a in sys.argv[1:]:
    i, v, note = a.split('|', 2); i = int(i)
    rows[i] = dict(i=i, arc=recs[i]['arc'], where=recs[i]['where'], status=recs[i]['status'], verdict=v.strip(), note=note.strip())
_q = {}
for _f, _off in OFFS:
    if os.path.exists(_f):
        for _k, _r in enumerate(csv.DictReader(open(_f), delimiter='\t')): _q[_off + _k] = _r['quote']
for _i in rows: rows[_i]['quote'] = rows[_i].get('quote') or _q.get(_i, '')
with open('VERDICTS.tsv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=['i', 'arc', 'where', 'status', 'verdict', 'note', 'quote'], delimiter='\t', lineterminator='\n'); w.writeheader()
    for i in sorted(rows): w.writerow(rows[i])
print('verdicts', len(rows))
