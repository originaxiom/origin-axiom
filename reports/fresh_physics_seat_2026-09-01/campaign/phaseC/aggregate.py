#!/usr/bin/env python3
"""Aggregate the Phase C rerun and Phase D certificate workflow journals into TSVs + a digest of everything that is not
REPRODUCES/PASS.  Usage: aggregate.py <journalC> <journalD>"""
import json, sys, csv, collections
def load(j):
    out = []
    for line in open(j):
        e = json.loads(line); r = e.get('result') or e.get('value') or {}
        if isinstance(r, dict) and 'results' in r:
            for x in r['results']: x = dict(x); x['packet'] = r['packet']; out.append(x)
    return out
C = load(sys.argv[1]) if len(sys.argv) > 1 else []; D = load(sys.argv[2]) if len(sys.argv) > 2 else []
with open('phaseC/results/rerun_results.tsv', 'w', newline='') as f:
    w = csv.writer(f, delimiter='\t', lineterminator='\n'); w.writerow(['packet', 'i', 'arc', 'outcome', 'script', 'runtime_s', 'reason', 'evidence'])
    for x in sorted(C, key=lambda x: x['i']): w.writerow([x['packet'], x['i'], x['arc'], x['outcome'], x.get('script', ''), x.get('runtime_s', ''), (x.get('reason') or '').replace('\n', ' '), x['evidence'].replace('\n', ' ')])
with open('phaseD/results/certificate_results.tsv', 'w', newline='') as f:
    w = csv.writer(f, delimiter='\t', lineterminator='\n'); w.writerow(['packet', 'path', 'outcome', 'certifies', 'depends_on', 'runtime_s', 'reason', 'evidence'])
    for x in sorted(D, key=lambda x: x['path']): w.writerow([x['packet'], x['path'], x['outcome'], x['certifies'].replace('\n', ' '), (x.get('depends_on') or '').replace('\n', ' '), x.get('runtime_s', ''), (x.get('reason') or '').replace('\n', ' '), x['evidence'].replace('\n', ' ')])
cc = collections.Counter(x['outcome'] for x in C); cd = collections.Counter(x['outcome'] for x in D)
with open('phaseC/results/DIGEST.md', 'w') as f:
    f.write('# Phase C rerun digest (auto)\n\nclaims reported %d: %s\n\n' % (len(C), ', '.join('%s %d' % kv for kv in cc.most_common())))
    for k in ('DIFFERS', 'PARTIAL', 'CANNOT_RUN', 'NOT_A_COMPUTATION'):
        f.write('## %s (%d)\n\n' % (k, cc[k]))
        for x in sorted(C, key=lambda x: x['i']):
            if x['outcome'] == k: f.write('- **#%s %s** (%s): %s — %s\n' % (x['i'], x['arc'], x.get('script', ''), (x.get('reason') or '').replace('\n', ' ')[:300], x['evidence'].replace('\n', ' ')[:400]))
        f.write('\n')
with open('phaseD/results/DIGEST.md', 'w') as f:
    f.write('# Phase D certificate digest (auto)\n\ncertificates reported %d: %s\n\n' % (len(D), ', '.join('%s %d' % kv for kv in cd.most_common())))
    for k in ('FAIL', 'TIMEOUT', 'CANNOT_RUN', 'NOT_A_CERTIFICATE', 'PASS'):
        f.write('## %s (%d)\n\n' % (k, cd[k]))
        for x in sorted(D, key=lambda x: x['path']):
            if x['outcome'] == k: f.write('- **%s**: %s — deps: %s%s\n' % (x['path'], x['certifies'].replace('\n', ' ')[:400], (x.get('depends_on') or '')[:200], (' — ' + (x.get('reason') or '')[:200]) if k != 'PASS' else ''))
        f.write('\n')
print('C', len(C), dict(cc), '| D', len(D), dict(cd))
