#!/usr/bin/env python3
"""Regenerate VERDICTS.md from VERDICTS.tsv + every absence_sweep*.tsv part (excluding trial/v1 files)."""
import csv, glob, collections
rows = list(csv.DictReader(open('VERDICTS.tsv'), delimiter='\t'))
sweep = []
for f in sorted(glob.glob('absence_sweep*.tsv')):
    if 'trial' in f or 'v1' in f: continue
    sweep += list(csv.DictReader(open(f), delimiter='\t'))
vc = collections.Counter(r['verdict'] for r in rows); sc = collections.Counter(r['status'] for r in sweep)
with open('VERDICTS.md', 'w') as f:
    f.write('# W-E absence sweep — the seat\'s verdicts\n\n')
    f.write('Claims swept: %d (%s). Verdicts written: %d — %s.\n\n' % (len(sweep), ', '.join('%s %d' % kv for kv in sorted(sc.items())), len(rows), ', '.join('%s %d' % kv for kv in vc.most_common())))
    f.write('Verdict key: CONTRADICTED = the repo already holds what the claim says is absent (the claim is wrong as written); SUPERSEDED = a later arc supplied it (the claim was true when written, stale now); OPEN_LATER = supplied only on an unmerged head, or the later work is unverified; STANDS / CONSISTENT = the sweep found nothing that supplies it (STANDS when the seat also checked directly); NOISE = co-occurrence only; GENERIC = terms too common for the sweep to say anything; REGISTRY_ECHO = only index/ledger files echo the claim. DOC_ECHO / NO_HIT rows (%d) carry no verdict: the sweep found no text outside catch-all files, so the claim stands as far as the repository text goes.\n\n' % (sc['DOC_ECHO'] + sc['NO_HIT']))
    for v in ['CONTRADICTED', 'SUPERSEDED', 'OPEN_LATER', 'STANDS']:
        f.write('## %s (%d)\n\n' % (v, vc[v]))
        for r in rows:
            if r['verdict'] == v: f.write('- **#%s %s** (%s): %s\n' % (r['i'], r['arc'], r['where'][-40:], r['note']))
        f.write('\n')
    f.write('## CONSISTENT / NOISE / GENERIC / REGISTRY_ECHO\n\nIn `VERDICTS.tsv` (one row per claim).\n')
print(len(sweep), dict(vc))
