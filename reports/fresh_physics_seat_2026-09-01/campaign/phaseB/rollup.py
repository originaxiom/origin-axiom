#!/usr/bin/env python3
"""Phase B W-D rollup (pure python, no agents): fold every landed digest into the synthesis tables.

  synthesis/coverage.md                 packets landed vs MANIFEST, arcs digested per source head
  synthesis/red_flags.tsv               arc, source, kind, detail                     (every reader red flag)
  synthesis/absence_claims.tsv          arc, source, where, quote                     (input to the W-E sweep executor)
  synthesis/log_discrepancies.md        arcs whose log_consistency is DRIFT / CONTRADICTION, with the reader's log_says
  synthesis/load_bearing.tsv            arc, source, kind, reproducible, what, where, why
  synthesis/load_bearing_unrecomputed.tsv   the subset not (COMPUTED, yes) — candidates for the next recompute cells
  synthesis/log_entries.tsv             date, log, title, arcs, status words, retractions, owner elections
  synthesis/tests.tsv                   (when the test digests land) file, arcs, what it locks, weakness
  synthesis/SUMMARY.md                  counts + the top red-flag kinds + the arcs with most flags

Re-runnable at any time; it only reads digests/ and MANIFEST.json.
"""
import json, glob, os, csv, collections, re

HERE = os.path.dirname(os.path.abspath(__file__))
D = os.path.join(HERE, 'digests')
S = os.path.join(HERE, 'synthesis')
os.makedirs(S, exist_ok=True)
man = json.load(open(os.path.join(HERE, 'MANIFEST.json')))

def js(x):
    return ' | '.join(json.dumps(i, ensure_ascii=False) if isinstance(i, (dict, list)) else str(i) for i in (x or []))

def tsv(name, header, rows):
    with open(os.path.join(S, name), 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f, delimiter='\t', lineterminator='\n')
        w.writerow(header)
        for r in rows:
            w.writerow([re.sub(r'\s+', ' ', str(x)) if x is not None else '' for x in r])

# ---------------- arcs ----------------
arc_files = sorted(glob.glob(os.path.join(D, 'arcs', 'arcs_*.json')))
arcs, batches = [], set()
for f in arc_files:
    d = json.load(open(f, encoding='utf-8'))
    recs = d['arcs'] if isinstance(d, dict) else d
    b = int(re.search(r'arcs_(\d+)', f).group(1)); batches.add(b)
    for a in recs:
        a['_batch'] = b
        arcs.append(a)
missing_batches = sorted(set(range(man['arc_batches'])) - batches)

red, absent, lb, lb_un, disc = [], [], [], [], []
per_arc_flags = collections.Counter()
kinds = collections.Counter()
lc = collections.Counter()
belts = collections.Counter()
for a in arcs:
    nm, src = a.get('arc'), a.get('source')
    _l = str(a.get('log_consistency') or '').strip().upper()
    _l = next((k for k in ('CONTRADICTION', 'DRIFT', 'NOT_IN_LOG', 'CONSISTENT') if _l.startswith(k)), _l or 'UNSTATED')
    a['_lc'] = _l; lc[_l] += 1
    _b = str(a.get('belt') or '').strip().upper(); _b = next((k for k in ('RECOMPUTES', 'RE-READS', 'NONE', 'UNCLEAR') if _b.startswith(k)), _b or 'UNSTATED'); belts[_b] += 1
    for r in a.get('red_flags', []) or []:
        k = r.get('kind') if isinstance(r, dict) else 'OTHER'
        det = r.get('detail') if isinstance(r, dict) else str(r)
        red.append((nm, src, k, det)); kinds[k] += 1; per_arc_flags[nm] += 1
    for c in a.get('absence_claims', []) or []:
        if isinstance(c, dict):
            absent.append((nm, src, c.get('where'), c.get('quote')))
        else:
            absent.append((nm, src, '', str(c)))
    for l in a.get('load_bearing', []) or []:
        if not isinstance(l, dict): continue
        row = (nm, src, l.get('kind'), l.get('reproducible_from_committed'), l.get('what'), l.get('where'), l.get('why'))
        lb.append(row)
        k = str(l.get('kind', '')).upper(); rep = str(l.get('reproducible_from_committed', '')).lower()
        if not (k.startswith('COMPUTED') and rep.startswith('yes') and 'numeric only' not in rep and 'not' not in rep.split('yes', 1)[1][:40]):
            lb_un.append(row)
    if a['_lc'] in ('DRIFT', 'CONTRADICTION'):
        disc.append(a)

tsv('red_flags.tsv', ['arc', 'source', 'kind', 'detail'], red)
tsv('absence_claims.tsv', ['arc', 'source', 'where', 'quote'], absent)
tsv('load_bearing.tsv', ['arc', 'source', 'kind', 'reproducible_from_committed', 'what', 'where', 'why'], lb)
tsv('load_bearing_unrecomputed.tsv', ['arc', 'source', 'kind', 'reproducible_from_committed', 'what', 'where', 'why'], lb_un)

with open(os.path.join(S, 'log_discrepancies.md'), 'w', encoding='utf-8') as f:
    f.write('# Arcs whose reader found the progress logs and the arc files in DRIFT or CONTRADICTION\n\n')
    f.write('(%d arcs of %d digested; NOT_IN_LOG = %d, CONSISTENT = %d)\n\n' % (len(disc), len(arcs), lc['NOT_IN_LOG'], lc['CONSISTENT']))
    for a in sorted(disc, key=lambda a: (a['_lc'] != 'CONTRADICTION', a.get('arc'))):
        f.write('## %s (%s) — %s\n\n' % (a.get('arc'), a.get('source'), a['_lc']))
        f.write('- **claim of record:** %s\n' % re.sub(r'\s+', ' ', str(a.get('claim_of_record'))))
        f.write('- **log says:** %s\n' % re.sub(r'\s+', ' ', str(a.get('log_says'))))
        if a.get('seat_note'): f.write('- **reader note:** %s\n' % re.sub(r'\s+', ' ', str(a.get('seat_note'))))
        f.write('\n')

# ---------------- logs ----------------
log_rows, log_files = [], sorted(glob.glob(os.path.join(D, 'log', '*.json')))
log_parts = collections.Counter()
elections = []
for f in log_files:
    d = json.load(open(f, encoding='utf-8'))
    log_parts[d.get('log')] += 1
    for e in d.get('entries', []):
        log_rows.append((e.get('date'), d.get('log'), e.get('title'), js(e.get('arcs')), js(e.get('status_words')),
                         js(e.get('retractions')), js(e.get('owner_elections_verbatim')), js(e.get('numbers_claimed'))))
        for o in e.get('owner_elections_verbatim', []) or []:
            elections.append((e.get('date'), d.get('log'), e.get('title'), js([o])))
        for r in e.get('red_flags', []) or []:
            red.append(('LOG:' + str(e.get('title'))[:60], d.get('log'), r.get('kind') if isinstance(r, dict) else 'OTHER', r.get('detail') if isinstance(r, dict) else str(r)))
tsv('log_entries.tsv', ['date', 'log', 'title', 'arcs', 'status_words', 'retractions', 'owner_elections_verbatim', 'numbers_claimed'], log_rows)
tsv('owner_elections.tsv', ['date', 'log', 'entry', 'election_verbatim'], elections)
tsv('red_flags.tsv', ['arc', 'source', 'kind', 'detail'], red)   # rewrite with the log flags appended

# ---------------- tests ----------------
test_rows, test_files = [], sorted(glob.glob(os.path.join(D, 'tests', '*.json')))
for f in test_files:
    d = json.load(open(f, encoding='utf-8'))
    recs = d.get('tests', d) if isinstance(d, dict) else d
    for t in recs if isinstance(recs, list) else []:
        if isinstance(t, dict):
            test_rows.append((t.get('file'), js(t.get('target_arcs')), t.get('what_it_locks'), t.get('lock_type'),
                              js(t.get('hardcoded_constants')), js(t.get('red_flags'))))
            for r in t.get('red_flags', []) or []:
                red.append(('TEST:' + str(t.get('file')), 'tests', r.get('kind') if isinstance(r, dict) else 'OTHER', r.get('detail') if isinstance(r, dict) else str(r)))
tsv('tests.tsv', ['file', 'target_arcs', 'what_it_locks', 'lock_type', 'hardcoded_constants', 'red_flags'], test_rows)
tsv('red_flags.tsv', ['arc', 'source', 'kind', 'detail'], red)   # rewrite with the test flags appended
lock_types = collections.Counter(r[3] for r in test_rows)

# ---------------- coverage + summary ----------------
by_src = collections.Counter(a.get('source') for a in arcs)
with open(os.path.join(S, 'coverage.md'), 'w', encoding='utf-8') as f:
    f.write('# Phase B coverage (auto)\n\n')
    f.write('- arc packets landed: **%d / %d**; missing: %s\n' % (len(batches), man['arc_batches'], missing_batches or 'none'))
    f.write('- arc records digested: **%d / %d** (%s)\n' % (len(arcs), man['arcs_total'], dict(by_src)))
    f.write('- log chunks landed: **%d / %d** (%s)\n' % (len(log_files), man['log_chunks'], dict(log_parts)))
    f.write('- test packets landed: **%d / %d**; test records: %d / %d\n' % (len(test_files), man['test_batches'], len(test_rows), man['tests_total']))
    f.write('- log consistency: %s\n' % dict(lc))
    f.write('- belts: %s\n' % dict(belts))
    f.write('- test lock types: %s\n' % dict(lock_types))

with open(os.path.join(S, 'SUMMARY.md'), 'w', encoding='utf-8') as f:
    f.write('# Phase B rollup summary (auto; re-run rollup.py after every landing)\n\n')
    f.write('arcs digested %d/%d, red flags %d, absence claims %d, load-bearing claims %d (of which not (COMPUTED, yes): %d), '
            'log entries %d, owner elections captured %d, tests %d.\n\n' % (len(arcs), man['arcs_total'], len(red), len(absent), len(lb), len(lb_un), len(log_rows), len(elections), len(test_rows)))
    f.write('## red-flag kinds\n\n')
    for k, n in kinds.most_common(): f.write('- %s: %d\n' % (k, n))
    f.write('\n## arcs with the most red flags\n\n')
    for nm, n in per_arc_flags.most_common(40): f.write('- %s: %d\n' % (nm, n))
    f.write('\n## load-bearing kinds\n\n')
    for k, n in collections.Counter((str(r[2]).split(' ')[0].split('(')[0], str(r[3]).split(' ')[0]) for r in lb).most_common(): f.write('- %s / %s: %d\n' % (k[0], k[1], n))
print('arcs %d/%d  batches %d/%d missing %s  red %d  absent %d  lb %d (un %d)  log chunks %d entries %d elections %d  tests %d' % (
    len(arcs), man['arcs_total'], len(batches), man['arc_batches'], missing_batches[:5], len(red), len(absent), len(lb), len(lb_un), len(log_files), len(log_rows), len(elections), len(test_rows)))
