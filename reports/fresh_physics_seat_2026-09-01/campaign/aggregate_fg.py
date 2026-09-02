#!/usr/bin/env python3
"""Aggregate Phase F (chirality) and Phase G (tracker) workflow journals into TSVs + digests.
Usage: aggregate_fg.py <journal.jsonl> [<journal2.jsonl> ...]"""
import json, sys, csv, collections, os
F, G = {}, {}
for path in sys.argv[1:]:
    for line in open(path):
        try: e = json.loads(line)
        except Exception: continue
        r = e.get('result') or e.get('value') or {}
        if not (isinstance(r, dict) and 'results' in r): continue
        pk = r.get('packet', '')
        tgt = F if pk.startswith('F') else G if pk.startswith('G') else None
        if tgt is None: continue
        for k, x in enumerate(r['results']):
            x = dict(x); x['packet'] = pk; tgt[(pk, k, x.get('arc'))] = x
def dump(rows, path, cols):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', newline='') as f:
        w = csv.writer(f, delimiter='\t', lineterminator='\n'); w.writerow(cols)
        for x in rows: w.writerow([str(x.get(c, '')).replace('\n', ' / ') if not isinstance(x.get(c), list) else ';'.join(x.get(c)) for c in cols])
Fr = [F[k] for k in sorted(F)]; Gr = [G[k] for k in sorted(G)]
dump(Fr, 'phaseF/results/chirality_sweep.tsv', ['packet', 'arc', 'orientation_source', 'status', 'evidence', 'amphichirality_test', 'headline', 'mechanism', 'note', 'quoted', 'files_read'])
dump(Gr, 'phaseG/results/tracker_sweep.tsv', ['packet', 'arc', 'is_choice_declared', 'status', 'evidence', 'headline', 'tracker_definition', 'inputs', 'outputs', 'symmetry_statements', 'note', 'quoted', 'files_read'])
cF = collections.Counter(x['orientation_source'] for x in Fr); sF = collections.Counter((x['orientation_source'], x['status']) for x in Fr)
cG = collections.Counter(x['is_choice_declared'] for x in Gr)
with open('phaseF/results/DIGEST.md', 'w') as f:
    f.write('# Phase F digest (auto)\n\nrows %d: %s\n\nsource × status: %s\n\n' % (len(Fr), ', '.join('%s %d' % kv for kv in cF.most_common()), ', '.join('%s/%s %d' % (k[0], k[1], v) for k, v in sorted(sF.items()))))
    for src in ['RULE_INTRINSIC', 'OBSERVER_CHOICE', 'ARITHMETIC_GALOIS', 'GEOMETRY_CS_OR_TORSION', 'FILLING_SLOPE', 'NONE_OBJECT_AMPHICHIRAL', 'UNSTATED']:
        f.write('## %s\n\n' % src)
        for x in Fr:
            if x['orientation_source'] == src:
                f.write('- **%s** [%s, %s; test: %s] %s\n  - mechanism: %s\n  - note: %s\n  - quoted: %s\n' % (x['arc'], x['status'], x['evidence'], x.get('amphichirality_test', ''), x['headline'], x['mechanism'], x['note'], str(x['quoted']).replace('\n', ' / ')[:600]))
        f.write('\n')
with open('phaseG/results/DIGEST.md', 'w') as f:
    f.write('# Phase G digest (auto)\n\nrows %d: %s\n\n' % (len(Gr), ', '.join('%s %d' % kv for kv in cG.most_common())))
    for x in Gr:
        f.write('- **%s** [%s, %s, %s] %s\n  - tracker: %s\n  - in: %s → out: %s\n  - symmetry: %s\n  - note: %s\n  - quoted: %s\n' % (x['arc'], x['is_choice_declared'], x['status'], x['evidence'], x['headline'], x['tracker_definition'], x['inputs'], x['outputs'], x['symmetry_statements'], x['note'], str(x['quoted']).replace('\n', ' / ')[:500]))
print('F rows', len(Fr), dict(cF)); print('G rows', len(Gr), dict(cG))
