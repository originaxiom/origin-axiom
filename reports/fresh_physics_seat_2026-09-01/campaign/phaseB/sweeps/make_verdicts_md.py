#!/usr/bin/env python3
"""Regenerate VERDICTS.md from VERDICTS.tsv + every absence_sweep*.tsv part (excluding trial/v1 files).
Counts are per DISTINCT claim (arc, quote): the sweep parts overlap because rollup.py re-sorted absence_claims.tsv
between parts (see index_map.py / sweep_index_map.tsv).  When duplicate sweep rows carry different verdicts the more
informative one wins: CONTRADICTED > SUPERSEDED > OPEN_LATER > STANDS > CONSISTENT > REGISTRY_ECHO > GENERIC > NOISE
(NOISE/GENERIC mean 'the sweep said nothing', so any substantive verdict dominates)."""
import csv, glob, collections, subprocess
subprocess.run(['python3', 'index_map.py'], check=True, capture_output=True)
RANK = {v: k for k, v in enumerate(['NOISE', 'GENERIC', 'REGISTRY_ECHO', 'CONSISTENT', 'STANDS', 'OPEN_LATER', 'SUPERSEDED', 'CONTRADICTED'])}
rows = {int(r['i']): r for r in csv.DictReader(open('VERDICTS.tsv'), delimiter='\t')}
imap = list(csv.DictReader(open('sweep_index_map.tsv'), delimiter='\t'))
sweep = []
for f in sorted(glob.glob('absence_sweep*.tsv')):
    if 'trial' in f or 'v1' in f: continue
    sweep += [dict(r, _f=f) for r in csv.DictReader(open(f), delimiter='\t')]
key_rows = collections.defaultdict(list)          # distinct-claim key -> sweep indices
for m in imap: key_rows[m['dup_of'] or m['i']].append(int(m['i']))
best = {}
for k, ids in key_rows.items():
    cands = [rows[i] for i in ids if i in rows and not rows[i]['note'].startswith('duplicate of')]
    if cands: best[k] = max(cands, key=lambda r: RANK.get(r['verdict'], -1))
# status per distinct claim from the sweep tsv row of its first sweep index
srow = {}
off = 0
for f in ['absence_sweep.tsv', 'absence_sweep_p2.tsv', 'absence_sweep_p3.tsv', 'absence_sweep_p4.tsv', 'absence_sweep_p5.tsv']:
    try: part = list(csv.DictReader(open(f), delimiter='\t'))
    except FileNotFoundError: continue
    for k, r in enumerate(part): srow[off + k] = r
    off += len(part)
sc = collections.Counter(srow[int(k)]['status'] for k in key_rows)
vc = collections.Counter(r['verdict'] for r in best.values())
claims_total = len(list(csv.DictReader(open('../synthesis/absence_claims.tsv'), delimiter='\t')))
with open('VERDICTS.md', 'w') as f:
    f.write('# W-E absence sweep — the seat\'s verdicts\n\n')
    f.write('Distinct claims swept: %d of %d in synthesis/absence_claims.tsv (sweep rows %d; %d rows are duplicates caused by the index shift, see `sweep_index_map.tsv`). Status by claim: %s.\n\n' % (len(key_rows), claims_total, len(imap), sum(1 for m in imap if m['dup_of']), ', '.join('%s %d' % kv for kv in sorted(sc.items()))))
    f.write('Verdicts (per distinct claim): %d — %s.\n\n' % (len(best), ', '.join('%s %d' % kv for kv in vc.most_common())))
    f.write('Verdict key: CONTRADICTED = the repo already holds what the claim says is absent (the claim is wrong as written); SUPERSEDED = a later arc supplied it (the claim was true when written, stale now); OPEN_LATER = supplied only on an unmerged head, or the later work is unverified; STANDS / CONSISTENT = the sweep found nothing that supplies it (STANDS when the seat also checked directly); NOISE = co-occurrence only; GENERIC = terms too common for the sweep to say anything; REGISTRY_ECHO = only index/ledger files echo the claim. DOC_ECHO / NO_HIT rows carry no verdict: the sweep found no text outside catch-all files, so the claim stands as far as the repository text goes.\n\n')
    f.write('Index note: `i` is the sweep index (VERDICTS.tsv key). `sweep_index_map.tsv` maps it to the row of the current absence_claims.tsv and marks duplicates; when duplicates disagree the more informative verdict is the claim\'s (order NOISE < GENERIC < REGISTRY_ECHO < CONSISTENT < STANDS < OPEN_LATER < SUPERSEDED < CONTRADICTED).\n\n')
    for v in ['CONTRADICTED', 'SUPERSEDED', 'OPEN_LATER', 'STANDS']:
        f.write('## %s (%d)\n\n' % (v, vc[v]))
        for r in sorted(best.values(), key=lambda r: int(r['i'])):
            if r['verdict'] == v: f.write('- **#%s %s** (%s): %s\n' % (r['i'], r['arc'], r['where'][-40:], r['note']))
        f.write('\n')
    f.write('## CONSISTENT / NOISE / GENERIC / REGISTRY_ECHO\n\nIn `VERDICTS.tsv` (one row per sweep index).\n')
print('distinct claims', len(key_rows), 'verdicts', len(best), dict(vc), dict(sc))
