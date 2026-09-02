#!/usr/bin/env python3
"""Phase B W-E — absence-claim sweep executor (owner rule 1: before you conclude we don't have
something, sweep the repo first — every remote head's tree AND every file ever deleted).

Input : synthesis/absence_claims.tsv   (arc, source, where, quote) — one row per "no X / not derived /
        never computed" sentence a reader extracted from an arc.
Output: sweeps/absence_sweep.tsv        one row per claim: search terms used, per-head file-hit counts
                                        (excluding the claiming arc's own directory and this seat's
                                        reports/), deleted-history hits, and the top 5 hit paths.
        sweeps/absence_sweep_hits.md    the claims whose sweep found something OUTSIDE the claiming arc,
                                        with the hit paths — the seat writes a verdict on each of these
                                        by hand (verdicts are never delegated).
        sweeps/deleted_corpus/          the content of every path ever deleted on any head (materialised
                                        once from the parent commit so the sweep can grep it like a tree).

Term extraction is mechanical (distinctive tokens of the quote, stop-listed) and deliberately loose: a
hit means "these words co-occur in some other file", i.e. a LEAD, not a refutation.  The verdict layer
is human.  A claim whose quote yields < 2 usable terms is marked UNSWEEPABLE (seat reads it directly).
"""
import csv, os, re, subprocess, sys, json, collections

ROOT = '/home/user/origin-axiom'
HERE = os.path.dirname(os.path.abspath(__file__))
SYN = os.path.join(HERE, '..', 'synthesis')
DEL = os.path.join(HERE, 'deleted_corpus')
SEAT = 'reports/fresh_physics_seat_2026-09-01'
# catch-all files: they echo every claim ever made (a hit there means "the claim was logged", never "the thing exists")
CATCHALL_EXACT = {'CHANGELOG.md', 'PROGRESS_LOG.md', 'CLAIMS.md', 'ROADMAP.md', 'GOVERNANCE.md', 'README.md', 'TERMINOLOGY.md',
                  'REPRODUCIBILITY.md', 'AUDIT_REPORT.md', 'ARCHITECTURE.md', 'PROVENANCE.md', 'METHOD.md', 'WORKING_RULES.md',
                  'docs/PROGRESS_LOG.md', 'docs/REVIEWS.md'}
CATCHALL_PREFIX = ('docs/progress/', 'docs/reviews', 'documents/', 'legacy/', 'CC_TO_', 'CC3_TO_', 'outside_bench/')
def is_catchall(p):
    return p in CATCHALL_EXACT or p.startswith(CATCHALL_PREFIX) or p.endswith(('PROGRESS_LOG.md', 'REVIEWS.md', 'CHANGELOG.md'))

ENV = dict(os.environ, LC_ALL='C', LANG='C')   # byte-wise case folding: git grep -i is many times faster than under UTF-8
def git(*a, check=True):
    r = subprocess.run(['git', '-C', ROOT] + list(a), capture_output=True, text=True, env=ENV)
    if check and r.returncode not in (0, 1): raise RuntimeError(r.stderr[:300])
    return r.stdout

HEADS = [h.strip() for h in git('branch', '-r').splitlines() if 'HEAD' not in h and 'physics-seat-evaluation' not in h]
# the seat's own head is main + reports/fresh_physics_seat_2026-09-01/ (excluded from every hit anyway); grepping it only
# re-scans main plus this seat's multi-MB sweep/digest files — dropped from the head list (its tree is not evidence)

# ---------------- deleted corpus (materialise once) ----------------
def build_deleted_corpus():
    if os.path.isdir(DEL) and os.listdir(DEL): return
    os.makedirs(DEL, exist_ok=True)
    seen = set()
    log = git('log', '--all', '--diff-filter=D', '--name-only', '--format=%H')
    commit = None
    for line in log.splitlines():
        if re.fullmatch(r'[0-9a-f]{40}', line): commit = line; continue
        p = line.strip()
        if not p or p in seen or 'zcache' in p or p.endswith(('.pdf', '.png', '.npz', '.pkl')): continue
        seen.add(p)
        content = git('show', '%s^:%s' % (commit, p), check=False)
        if content:
            dst = os.path.join(DEL, p.replace('/', '__'))
            open(dst, 'w', encoding='utf-8').write(content)
    open(os.path.join(DEL, '_INDEX.txt'), 'w').write('\n'.join(sorted(seen)) + '\n')

# ---------------- term extraction ----------------
STOP = set('''the this that these those there here from with into onto upon about above below between within without
does doesnt does not do did done been being have having has had were was are is be will would could should shall
may might must can cannot not never none nothing nowhere only just also even still yet than then thus hence
therefore however whereas whether which what when where while who whom whose why how any some such other another
each every either neither both all more most much many few less least own same very via per and but for nor
or so if as at by in of on to up its it he she they them their our your his her we you one two three four
derived derive derives deriving derivation derivable defined define defines definition construction constructed
construct claimed claim claims claiming currently current present presented provide provided provides supply supplied
supplies supplying produce produced produces resolve resolved resolves restate restates restated give gives given
name names named exist exists existing exhibited exhibit shown show shows showed proved prove proves proven theorem
result results obtained obtain obtains attempted attempt computed compute computes computation performed perform
established establish independent independently explicit explicitly directly direct physical physically physics
substrate repo repository file files arc arcs cell cells bank banked seat seats reader readers finding findings
findings.md readme.md readme note notes section sections table row rows line lines does.not is.not are.not
step steps case cases sense mean means meaning content contents level levels part parts rule rules'''.split())

def terms(quote):
    q = quote.lower()
    q = re.sub(r'[`"“”\'’*_]', ' ', q)
    toks = re.findall(r'[a-z][a-z0-9\-\+]{3,}', q)
    out, seen = [], set()
    for t in toks:
        t = t.strip('-+')
        if len(t) < 4 or t in STOP or t in seen: continue
        seen.add(t); out.append(t)
    # prefer rarer-looking tokens: longer, with digits/hyphens, or capitalised-ish domain words
    out.sort(key=lambda t: (-(any(c.isdigit() for c in t) or '-' in t), -len(t)))
    return out[:4]

def arc_dir(where, arc):
    m = re.match(r'([^:]+?)/[^/]+$', where or '')
    return m.group(1) if m else ('frontier/' + arc if arc else '')

def sweep_head(head, ts, exclude_dir):
    args = ['grep', '-i', '-l', '--all-match']
    for t in ts: args += ['-e', t]
    args += [head, '--']
    out = git(*args, check=False)
    paths = []
    for line in out.splitlines():
        p = line.split(':', 1)[1] if ':' in line else line
        if p.startswith(SEAT): continue
        if exclude_dir and p.startswith(exclude_dir.rstrip('/') + '/'): continue
        paths.append(p)
    return paths

def sweep_deleted(ts):
    hits = []
    for fn in os.listdir(DEL):
        if fn.startswith('_'): continue
        txt = open(os.path.join(DEL, fn), encoding='utf-8', errors='replace').read().lower()
        if all(t in txt for t in ts): hits.append(fn.replace('__', '/'))
    return hits

def main():
    build_deleted_corpus()
    rows = list(csv.DictReader(open(os.path.join(SYN, 'absence_claims.tsv'), encoding='utf-8'), delimiter='\t'))
    # usage: sweep_batch.py [start] [end] [suffix]  -> sweeps rows[start:end], writes absence_sweep<suffix>.tsv etc.
    start = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    end = int(sys.argv[2]) if len(sys.argv) > 2 else len(rows)
    SUF = sys.argv[3] if len(sys.argv) > 3 else ''
    rows = [dict(r, _i=i) for i, r in enumerate(rows)][start:end]
    out_rows, leads, allrec = [], [], []
    for i, r in enumerate(rows):
        i = r['_i']
        ts = terms(r['quote'])
        exclude = arc_dir(r['where'], r['arc'])
        if len(ts) < 2:
            out_rows.append((r['arc'], r['source'], r['where'], ' '.join(ts), 'UNSWEEPABLE', '', '', r['quote'])); continue
        per_head, allpaths = {}, collections.Counter()
        for h in HEADS:
            ps = sweep_head(h, ts, exclude)
            per_head[h.replace('origin/', '')] = len(ps)
            for p in ps: allpaths[p] += 1
        dl = [d for d in sweep_deleted(ts) if not is_catchall(d)]
        subst = collections.Counter({p: n for p, n in allpaths.items() if not is_catchall(p)})
        echo = len(allpaths) - len(subst)
        top = [p for p, _ in subst.most_common(8)]
        if not (allpaths or dl): status = 'NO_HIT'
        elif not (subst or dl): status = 'DOC_ECHO'
        elif len(subst) > 40 and not dl: status = 'GENERIC'
        else: status = 'LEAD'
        allrec.append(dict(i=i, arc=r['arc'], where=r['where'], terms=ts, status=status, substantive=sorted(subst), catchall_hits=echo, deleted=dl))
        out_rows.append((r['arc'], r['source'], r['where'], ' '.join(ts), status,
                         json.dumps(per_head, separators=(',', ':')), ' | '.join(top + ['DELETED:' + d for d in dl]) + (' | +%d catch-all' % echo if echo else ''), r['quote']))
        if status == 'LEAD':
            leads.append((r, ts, per_head, top, dl, len(subst)))
        if i % 25 == 0: print('%d/%d  leads so far %d' % (i, end, len(leads)), flush=True)
    json.dump(allrec, open(os.path.join(HERE, 'absence_sweep_paths%s.json' % SUF), 'w'), indent=0)
    with open(os.path.join(HERE, 'absence_sweep%s.tsv' % SUF), 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f, delimiter='\t', lineterminator='\n')
        w.writerow(['arc', 'source', 'where', 'terms', 'status', 'hits_per_head', 'top_paths', 'quote'])
        for row in out_rows: w.writerow([re.sub(r'\s+', ' ', str(x)) for x in row])
    with open(os.path.join(HERE, 'absence_sweep_hits%s.md' % SUF), 'w', encoding='utf-8') as f:
        f.write('# W-E absence sweep — LEADS (co-occurrence hits outside the claiming arc; verdicts are the seat\'s, below each)\n\n')
        f.write('claims swept %d, leads %d, doc-echo (hits only in changelog/progress-log/claims-type catch-all files) %d, generic (>40 substantive files) %d, no-hit %d, unsweepable %d. Heads: %s. Deleted corpus: %s files.\n\n' % (
            len(rows), len(leads), sum(1 for r in out_rows if r[4] == 'DOC_ECHO'), sum(1 for r in out_rows if r[4] == 'GENERIC'), sum(1 for r in out_rows if r[4] == 'NO_HIT'), sum(1 for r in out_rows if r[4] == 'UNSWEEPABLE'),
            ', '.join(h.replace('origin/', '') for h in HEADS), len([x for x in os.listdir(DEL) if not x.startswith('_')])))
        for r, ts, ph, top, dl, n in sorted(leads, key=lambda x: -x[5]):
            f.write('## %s (%s) — %s\n' % (r['arc'], r['source'], r['where']))
            f.write('> %s\n\n' % re.sub(r'\s+', ' ', r['quote']))
            f.write('- terms: `%s`; distinct substantive hit files across heads: %d; per head (all hits): %s%s\n' % (' '.join(ts), n, ph, ('; DELETED: ' + ', '.join(dl)) if dl else ''))
            f.write('- top: %s\n' % ', '.join('`%s`' % p for p in top))
            f.write('- **verdict:** _(seat)_\n\n')
    print('done: %d claims, %d leads' % (len(rows), len(leads)))

if __name__ == '__main__':
    main()
