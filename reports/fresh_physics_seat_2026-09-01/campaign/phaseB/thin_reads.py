#!/usr/bin/env python3
"""Fold every reader's `thin_reads` (what was NOT read in full, and why) from the workflow journals into
synthesis/thin_reads.md — the honesty table behind 'every arc read'."""
import json, glob, os, re
J = '/root/.claude/projects/-home-user-origin-axiom/def55705-87fb-5c25-8c65-d57916765de8/subagents/workflows'
HERE = os.path.dirname(os.path.abspath(__file__))
rows = {}
for run in ('wf_28f4233f-0b3', 'wf_f5c14ccf-b9d', 'wf_640f00ee-2d9'):
    p = os.path.join(J, run, 'journal.jsonl')
    if not os.path.exists(p): continue
    for line in open(p, encoding='utf-8'):
        try: d = json.loads(line)
        except Exception: continue
        if d.get('type') != 'result': continue
        r = d.get('result') or d.get('value') or {}
        if isinstance(r, str):
            try: r = json.loads(r)
            except Exception: continue
        if not isinstance(r, dict) or 'batch' not in r: continue
        rows[r['batch']] = dict(n=r.get('n_items_digested'), failed=r.get('items_failed') or [], thin=r.get('thin_reads') or [])
with open(os.path.join(HERE, 'synthesis', 'thin_reads.md'), 'w', encoding='utf-8') as f:
    f.write('# Reader thin-reads (auto from workflow journals): what was not read in full, per packet\n\n')
    f.write('%d packets reported; %d with thin reads; %d with failed items.\n\n' % (len(rows), sum(1 for r in rows.values() if r['thin']), sum(1 for r in rows.values() if r['failed'])))
    for b in sorted(rows):
        r = rows[b]
        if not r['thin'] and not r['failed']: continue
        f.write('## %s (%s items)\n' % (b, r['n']))
        for t in r['failed']: f.write('- FAILED: %s\n' % t)
        for t in r['thin']: f.write('- %s\n' % re.sub(r'\s+', ' ', str(t)))
        f.write('\n')
print('packets', len(rows), 'thin', sum(1 for r in rows.values() if r['thin']), 'failed', sum(1 for r in rows.values() if r['failed']))
