#!/usr/bin/env python3
"""Phase B (owner rule 2, 2026-09-01: "read all the arcs, belts and tests ... through the progresslog,
both the one in main and in docs").  Mechanical preparation for the full-read workflow:

  1. log_index/<arc>.txt  — every progress-log / review entry (root PROGRESS_LOG.md,
     docs/progress/PROGRESS_2026-Q2.md, docs/progress/REVIEWS.md) that mentions the arc, with the
     sentences naming it.  Arc readers check the arc AGAINST what the log says it established.
  2. packets/arcs_NNN.json — batches of arcs with per-file read instructions (FULL / SAMPLE),
     packed by effective size.  Branch-only arcs (audit/b775, new-session-qor5up, paper branch)
     are included from read-only worktrees so no arc on any remote head is skipped.
  3. packets/tests_NN.json — batches of test files.
  4. packets/log_NN.json — chunks of the three logs for the W1 log digesters.
  5. MANIFEST.json — counts, so "all" is a checked number, not a word.

Nothing here is banked; this is seat instrumentation under reports/.
"""
import json, os, re, subprocess, sys
from collections import defaultdict

ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
HERE = os.path.dirname(os.path.abspath(__file__))
SCRATCH = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, 'scratch')
os.makedirs(os.path.join(SCRATCH, 'log_index'), exist_ok=True)
os.makedirs(os.path.join(HERE, 'packets'), exist_ok=True)
os.makedirs(os.path.join(HERE, 'digests', 'arcs'), exist_ok=True)
os.makedirs(os.path.join(HERE, 'digests', 'tests'), exist_ok=True)
os.makedirs(os.path.join(HERE, 'digests', 'log'), exist_ok=True)

READABLE = ('.md', '.py', '.json', '.txt', '.sh', '.sage', '.csv', '.tsv', '.jsonl', '.orig_claim', '.magma_out', '.patch')
MD_CAP, CODE_FULL, CODE_SAMPLE, DATA_FULL, DATA_SAMPLE = 120_000, 15_000, 6_000, 30_000, 2_500
BATCH_EFF, BATCH_MAX_ARCS = 260_000, 28

# ---------- 1. log index ----------
LOGS = [('PROGRESS_LOG.md', os.path.join(ROOT, 'PROGRESS_LOG.md')),
        ('docs/progress/PROGRESS_2026-Q2.md', os.path.join(ROOT, 'docs/progress/PROGRESS_2026-Q2.md')),
        ('docs/progress/REVIEWS.md', os.path.join(ROOT, 'docs/progress/REVIEWS.md'))]
ARC_RE = re.compile(r'\bB\d{3,4}\b')
entries = []  # (log, title, text)
for name, path in LOGS:
    txt = open(path, encoding='utf-8').read()
    parts = re.split(r'\n(?=## )', txt)
    for p in parts:
        title = p.splitlines()[0].strip() if p.strip() else ''
        if title.startswith('## '):
            entries.append((name, title[3:], p))
index = defaultdict(list)
for name, title, text in entries:
    for arc in set(ARC_RE.findall(text)):
        sents = [s.strip() for s in re.split(r'(?<=[.!?])\s+', text) if arc in s]
        index[arc].append((name, title, sents[:12]))
for arc, hits in index.items():
    with open(os.path.join(SCRATCH, 'log_index', f'{arc}.txt'), 'w', encoding='utf-8') as f:
        f.write(f'# log mentions of {arc}: {len(hits)} entries\n')
        for name, title, sents in hits:
            f.write(f'\n## [{name}] {title}\n')
            for s in sents:
                f.write('  - ' + re.sub(r'\s+', ' ', s)[:700] + '\n')

# ---------- log chunks for W1 ----------
log_chunks = []
def chunk(name, path, target=230_000):
    txt = open(path, encoding='utf-8').read()
    parts = re.split(r'\n(?=## )', txt)
    cur, size, i = [], 0, 0
    for p in parts:
        cur.append(p); size += len(p)
        if size >= target:
            log_chunks.append({'log': name, 'part': i, 'n_entries': len(cur), 'bytes': size,
                               'first_title': cur[0].splitlines()[0][:120], 'last_title': cur[-1].splitlines()[0][:120],
                               'path': path, 'text_file': None}); i += 1; cur, size = [], 0
    if cur:
        log_chunks.append({'log': name, 'part': i, 'n_entries': len(cur), 'bytes': size,
                           'first_title': cur[0].splitlines()[0][:120], 'last_title': cur[-1].splitlines()[0][:120],
                           'path': path, 'text_file': None})
    # materialize chunk text files
    parts_iter = iter(parts); k = 0
    for c in [c for c in log_chunks if c['log'] == name]:
        body = '\n'.join(next(parts_iter) for _ in range(c['n_entries']))
        fn = os.path.join(SCRATCH, f"logchunk_{name.replace('/', '_')}_{c['part']:02d}.md")
        open(fn, 'w', encoding='utf-8').write(body); c['text_file'] = fn
for name, path in LOGS:
    chunk(name, path)
for i, c in enumerate(log_chunks):
    json.dump(c, open(os.path.join(HERE, 'packets', f'log_{i:02d}.json'), 'w'), indent=1)

# ---------- 2. arcs (main tree + branch-only worktrees) ----------
heads = [l.split() for l in subprocess.check_output(['git', 'ls-remote', '--heads', 'origin'], text=True).splitlines()]
main_sha = [h for h, n in heads if n == 'refs/heads/main'][0]
def tree_arcs(sha):
    out = subprocess.check_output(['git', 'ls-tree', '-r', '--name-only', sha], text=True, cwd=ROOT).splitlines()
    return {p.split('/')[1] for p in out if p.startswith('frontier/') and p.count('/') >= 2}
main_arcs = tree_arcs(main_sha)
sources = [('main', os.path.join(ROOT, 'frontier'), sorted(main_arcs))]
for sha, ref in heads:
    n = ref.replace('refs/heads/', '')
    if n == 'main': continue
    only = sorted(tree_arcs(sha) - main_arcs)
    if not only: continue
    wt = os.path.join(SCRATCH, 'worktrees', n.replace('/', '_'))
    if not os.path.isdir(wt):
        subprocess.run(['git', 'worktree', 'add', '--detach', wt, sha], check=True, capture_output=True, cwd=ROOT)
    sources.append((n, os.path.join(wt, 'frontier'), only))

def classify(path, size):
    ext = os.path.splitext(path)[1]
    base = os.path.basename(path)
    if ext == '.md' or base in ('arc_verdict.json',):
        return ('FULL', min(size, MD_CAP)) if size <= MD_CAP else ('FULL_HEAD', MD_CAP)
    if ext in ('.py', '.sage', '.sh'):
        return ('FULL', size) if size <= CODE_FULL else ('SAMPLE_CODE', CODE_SAMPLE)
    if ext in READABLE:
        return ('FULL', size) if size <= DATA_FULL else ('SAMPLE_DATA', DATA_SAMPLE)
    return ('LIST_ONLY', 0)

arc_records = []
for src, fdir, arcs in sources:
    for arc in arcs:
        p = os.path.join(fdir, arc)
        files, eff = [], 0
        for r, ds, fs in os.walk(p):
            ds[:] = [d for d in ds if d != '__pycache__']
            for f in sorted(fs):
                fp = os.path.join(r, f); sz = os.path.getsize(fp)
                mode, e = classify(fp, sz); eff += e
                files.append({'path': fp, 'bytes': sz, 'mode': mode})
        has = {os.path.basename(f['path']) for f in files}
        arc_records.append({'arc': arc, 'source': src, 'dir': p, 'n_files': len(files), 'eff_bytes': eff,
                            'has_findings': 'FINDINGS.md' in has, 'has_verdict': 'arc_verdict.json' in has,
                            'has_verification_dir': any('/verification/' in f['path'] for f in files),
                            'log_index': os.path.join(SCRATCH, 'log_index', f'{arc.split("_")[0]}.txt')
                                         if os.path.exists(os.path.join(SCRATCH, 'log_index', f'{arc.split("_")[0]}.txt')) else None,
                            'files': files})
# frontier root files as one pseudo-arc
rootfiles = [{'path': os.path.join(ROOT, 'frontier', f), 'bytes': os.path.getsize(os.path.join(ROOT, 'frontier', f)),
              'mode': classify(f, os.path.getsize(os.path.join(ROOT, 'frontier', f)))[0]}
             for f in sorted(os.listdir(os.path.join(ROOT, 'frontier'))) if os.path.isfile(os.path.join(ROOT, 'frontier', f))]
arc_records.append({'arc': '_frontier_root_files', 'source': 'main', 'dir': os.path.join(ROOT, 'frontier'),
                    'n_files': len(rootfiles), 'eff_bytes': sum(f['bytes'] for f in rootfiles), 'has_findings': False,
                    'has_verdict': False, 'has_verification_dir': False, 'log_index': None, 'files': rootfiles})

def keyf(rec):
    m = re.match(r'B(\d+)', rec['arc']); return (0, int(m.group(1))) if m else (1, rec['arc'])
arc_records.sort(key=keyf)
batches, cur, cur_eff = [], [], 0
for rec in arc_records:
    if cur and (cur_eff + rec['eff_bytes'] > BATCH_EFF or len(cur) >= BATCH_MAX_ARCS):
        batches.append(cur); cur, cur_eff = [], 0
    cur.append(rec); cur_eff += rec['eff_bytes']
if cur: batches.append(cur)
for i, b in enumerate(batches):
    json.dump({'batch': f'arcs_{i:03d}', 'n_arcs': len(b), 'eff_bytes': sum(r['eff_bytes'] for r in b),
               'arcs': b}, open(os.path.join(HERE, 'packets', f'arcs_{i:03d}.json'), 'w'), indent=1)

# ---------- 3. tests ----------
tests = []
for r, ds, fs in os.walk(os.path.join(ROOT, 'tests')):
    ds[:] = [d for d in ds if d != '__pycache__']
    for f in sorted(fs):
        fp = os.path.join(r, f); tests.append({'path': fp, 'bytes': os.path.getsize(fp),
                                               'arcs': sorted(set(re.findall(r'\bb(\d{3,4})\b', f.lower())))})
tests.sort(key=lambda t: t['path'])
tb, cur, cur_b = [], [], 0
for t in tests:
    if cur and (cur_b + t['bytes'] > 220_000 or len(cur) >= 90):
        tb.append(cur); cur, cur_b = [], 0
    cur.append(t); cur_b += t['bytes']
if cur: tb.append(cur)
for i, b in enumerate(tb):
    json.dump({'batch': f'tests_{i:02d}', 'n_files': len(b), 'bytes': sum(t['bytes'] for t in b), 'files': b},
              open(os.path.join(HERE, 'packets', f'tests_{i:02d}.json'), 'w'), indent=1)

man = {'built_from_main': main_sha, 'heads': {n.replace('refs/heads/', ''): s for s, n in heads},
       'log_entries': {n: sum(1 for e in entries if e[0] == n) for n, _ in LOGS},
       'arcs_with_log_mentions': len(index), 'log_chunks': len(log_chunks),
       'arcs_total': len(arc_records), 'arcs_by_source': {s: len(a) for s, _, a in sources},
       'arc_files_total': sum(r['n_files'] for r in arc_records), 'arc_batches': len(batches),
       'arc_eff_bytes_total': sum(r['eff_bytes'] for r in arc_records),
       'arcs_without_findings': [r['arc'] for r in arc_records if not r['has_findings'] and r['arc'] != '_frontier_root_files'],
       'arcs_without_verdict': sum(1 for r in arc_records if not r['has_verdict']),
       'arcs_with_verification_dir': sum(1 for r in arc_records if r['has_verification_dir']),
       'tests_total': len(tests), 'test_batches': len(tb), 'test_bytes': sum(t['bytes'] for t in tests),
       'scratch': SCRATCH}
json.dump(man, open(os.path.join(HERE, 'MANIFEST.json'), 'w'), indent=1)
print(json.dumps({k: v for k, v in man.items() if k != 'arcs_without_findings'}, indent=1))
print('arcs without FINDINGS.md:', len(man['arcs_without_findings']))
