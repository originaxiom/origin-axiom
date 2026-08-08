r"""Generate `docs/REVIVABLE.md` — the revivable-kill frontier.

THE PROBLEM THIS SOLVES
-----------------------
`frontier/B738_pathfinder_compiler/kill_graph.json` records, for many killed
claims, an explicit route back: a `hatch` (the named escape) and a
`revival_score` (0-6, how promising that route is). That is a lead structure —
each entry is a relation between a dead claim and a live method.

No register indexes it. `OPEN_LEADS.md` indexes leads; the forcing graph indexes
arcs; the kill graph indexes kills. A revival hatch belongs to none of them, so
the question "what are the most revivable kills?" cannot be asked of any ledger
and its top items surface only by accident. This script makes that question
answerable by generating the index.

DESIGN
------
* **Generated, never hand-edited.** Re-run it; diff the result. A hand-maintained
  index is a second thing to go stale, which is the disease, not the cure.
* **Deterministic.** Same input -> byte-identical output. No timestamps, no
  ordering that depends on dict iteration. So a diff means the graph changed,
  not that the script ran again.
* **Sealed on its INPUT.** The header records sha256 of `kill_graph.json` and
  names the algorithm. It does NOT hash its own output (a file cannot contain
  its own hash), per the repo's seal convention.
* **Honest about the `id` field.** The graph's `id` is not uniformly an arc id
  (`P21 — the framework search`, `W10-B660/B666`). Non-arc ids are kept and
  flagged rather than dropped or coerced.
* **Explicit about WHICH graph it read.** `--ref` reads the source via
  `git show <ref>:<path>` instead of the working tree, and the ref is recorded
  in the output. This matters: a branch can carry a stale `kill_graph.json`
  (an audit branch here held the original 217-entry graph while `main` had 741),
  and an index generated from it would be confidently wrong. The script warns
  when the working tree and `origin/main` disagree.

Usage:  python3 scripts/revivable/build_revivable.py [--check] [--ref origin/main]
        --check exits nonzero if docs/REVIVABLE.md is stale (for CI).
"""
import subprocess
import argparse
import hashlib
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
GRAPH = os.path.join(ROOT, 'frontier', 'B738_pathfinder_compiler', 'kill_graph.json')
OUT = os.path.join(ROOT, 'docs', 'REVIVABLE.md')

REGISTERS = ['docs/OPEN_LEADS.md', 'docs/OPEN_PROBLEMS.md', 'docs/HINT_LEDGER.md',
             'docs/LEAD_REGISTER.md', 'docs/CAMPAIGN_STATUS.md', 'docs/ROADMAP.md']

ARC_ID = re.compile(r'^B\d+$')


def _read(path):
    with open(path, encoding='utf-8') as fh:
        return fh.read()


def _graph_bytes(ref):
    """Raw graph bytes from a git ref, or the working tree when ref is None."""
    rel = os.path.relpath(GRAPH, ROOT)
    if ref:
        r = subprocess.run(['git', '-C', ROOT, 'show', f'{ref}:{rel}'],
                           capture_output=True)
        if r.returncode:
            raise SystemExit(f'cannot read {rel} at {ref}: '
                             f'{r.stderr.decode().strip()}')
        return r.stdout
    return open(GRAPH, 'rb').read()


def _staleness_warning(ref):
    """Warn if the working tree's graph differs from origin/main's."""
    try:
        wt = _graph_bytes(None)
        om = _graph_bytes('origin/main')
    except SystemExit:
        return None
    if wt == om:
        return None
    return (f'working tree graph has {len(json.loads(wt))} entries; '
            f'origin/main has {len(json.loads(om))}. '
            f'Generated from: {ref or "working tree"}.')


def registrations(entry_id, reg_text):
    """Which registers name this id. Exact-token match, so B50 != B500."""
    if not ARC_ID.match(entry_id):
        return None                       # non-arc id: not answerable this way
    return [os.path.basename(f)[:-3] for f, t in reg_text.items()
            if re.search(rf'\b{entry_id}\b', t)]


def clean(s, n):
    if s is None:
        return ''
    s = re.sub(r'\s+', ' ', str(s)).strip()
    return (s[:n - 1] + '…') if len(s) > n else s


def build(ref=None):
    raw = _graph_bytes(ref)
    digest = hashlib.sha256(raw).hexdigest()
    warn = _staleness_warning(ref)
    graph = json.loads(raw.decode('utf-8'))

    # registers MUST be read from the same ref as the graph, or the
    # registration column reports one snapshot against another
    reg_text = {}
    for f in REGISTERS:
        if ref:
            r = subprocess.run(['git', '-C', ROOT, 'show', f'{ref}:{f}'],
                               capture_output=True, text=True)
            if r.returncode == 0:
                reg_text[f] = r.stdout
        else:
            p = os.path.join(ROOT, f)
            if os.path.isfile(p):
                reg_text[f] = _read(p)
    missing_regs = [f for f in REGISTERS if f not in reg_text]

    scored, untriaged, prose_hatch = [], [], []
    for e in graph:
        eid = str(e.get('id'))
        score = e.get('revival_score')
        hatch = e.get('hatch')
        if str(e.get('priority')) == 'UNTRIAGED':
            untriaged.append(eid)
        if score is None or not hatch or hatch == 'none-apparent':
            continue
        rec = {'id': eid, 'score': int(score), 'hatch': str(hatch),
               'priority': str(e.get('priority')),
               'killed': clean(e.get('claim_killed'), 300),
               'note': clean(e.get('note'), 300),
               'regs': registrations(eid, reg_text),
               'is_arc': bool(ARC_ID.match(eid))}
        # a hatch given as a full paragraph is a different animal from a route name
        (prose_hatch if len(rec['hatch']) > 40 else scored).append(rec)

    # deterministic: score desc, then unregistered first, then id
    def key(r):
        return (-r['score'], 0 if r['regs'] == [] else 1, r['id'])
    scored.sort(key=key)
    prose_hatch.sort(key=key)

    L = []
    A = L.append
    A('# REVIVABLE — the revivable-kill frontier')
    A('')
    A('> **GENERATED FILE — do not hand-edit.** Regenerate with')
    A('> `python3 scripts/revivable/build_revivable.py`; verify with `--check`.')
    A('> Source: `frontier/B738_pathfinder_compiler/kill_graph.json`,')
    A(f'> **sha256 `{digest}`** (algorithm: SHA-256 over the raw file bytes),')
    A(f'> read from **{ref or "the working tree"}**.')
    A('')
    if warn:
        A(f'> ⚠︎ **Source versions disagree.** {warn}')
        A('> An index built from a stale graph is confidently wrong, which is the')
        A('> failure this file exists to prevent — so the discrepancy is printed')
        A('> rather than resolved silently.')
        A('')
    A('**What this is.** The kill graph records, for many killed claims, an')
    A('explicit route back — a `hatch` naming the escape and a `revival_score`')
    A('(0–6) rating it. That is a lead structure, and no register indexed it, so')
    A('"what are the most revivable kills?" could not be asked of any ledger.')
    A('This file is that index. It asserts nothing new: every row is the kill')
    A("graph's own annotation, re-presented so it can be queried and ranked.")
    A('')
    A('**How to read a row.** `killed` is what was refuted. `hatch` is the route')
    A('the graph says could still work. `score` is the graph\'s own rating of that')
    A('route. `registers` is which ledgers name the id at all — **blank means the')
    A('item is invisible to every register**, which is the reason this file exists.')
    A('')

    tot = len(scored) + len(prose_hatch)
    unreg = sum(1 for r in scored + prose_hatch if r['regs'] == [])
    A('## Summary')
    A('')
    A('| | count |')
    A('|---|---|')
    A(f'| entries in the kill graph | {len(graph)} |')
    A(f'| with a named hatch **and** a revival score | **{tot}** |')
    A(f'| — of those, hatch is a short route name | {len(scored)} |')
    A(f'| — of those, hatch is a full prose paragraph | {len(prose_hatch)} |')
    A(f'| scoring ≥ 4 | {sum(1 for r in scored + prose_hatch if r["score"] >= 4)} |')
    A(f'| **named in no register** | **{unreg}** |')
    A(f'| `UNTRIAGED` (no hatch, no score, never assessed) | **{len(untriaged)}** |')
    A('')
    if missing_regs:
        A(f'> Registers consulted but **absent from the tree**: '
          f'{", ".join("`" + m + "`" for m in missing_regs)}. '
          f'Registration columns below are blank-by-absence for these.')
        A('')
    A(f'The `UNTRIAGED` {len(untriaged)} are the honest limit of this index: they')
    A('carry no hatch and no score, so they are not ranked here. Until they are')
    A('triaged, this file describes the assessed portion of the graph, not the graph.')
    A('')

    def table(rows, title, note):
        A(f'## {title}')
        A('')
        A(note)
        A('')
        A('| id | score | hatch | registers | claim killed |')
        A('|---|---|---|---|---|')
        for r in rows:
            regs = ('—' if r['regs'] == [] else
                    ('n/a' if r['regs'] is None else ', '.join(r['regs'])))
            flag = '' if r['is_arc'] else ' ⚠︎'
            A(f'| **{r["id"]}**{flag} | {r["score"]} | `{r["hatch"]}` | {regs} | '
              f'{r["killed"]} |')
        A('')

    hi = [r for r in scored if r['score'] >= 4]
    lo = [r for r in scored if r['score'] < 4]
    table(hi, 'Score ≥ 4 — the front of the queue',
          'Ranked by score, then by whether any register names them '
          '(unregistered first — those are the ones nothing else will surface).')
    table(lo, 'Score ≤ 3', 'Same ordering. Lower-rated routes, kept for completeness.')

    if prose_hatch:
        A('## Hatches written as prose, not as a route name')
        A('')
        A('These entries state their escape as a full paragraph rather than one of')
        A('the seven short route names. They are not lesser — several are the most')
        A('carefully reasoned in the graph — but they cannot be grouped by route,')
        A('so they are listed separately and the hatch text is given in full.')
        A('')
        for r in prose_hatch:
            regs = ('—' if r['regs'] == [] else
                    ('n/a' if r['regs'] is None else ', '.join(r['regs'])))
            A(f'**{r["id"]}** — score {r["score"]} — registers: {regs}')
            A('')
            A(f'- *killed:* {r["killed"]}')
            A(f'- *hatch:* {r["hatch"]}')
            A('')

    nonarc = [r['id'] for r in scored + prose_hatch if not r['is_arc']]
    if nonarc:
        A('## ⚠︎ Ids that are not arc ids')
        A('')
        A('The graph\'s `id` field is not uniformly an arc id. These entries are')
        A('kept and flagged rather than dropped or coerced; their `registers` column')
        A('reads `n/a` because register lookup is arc-keyed and cannot answer for')
        A('them. **Anything else keyed on `id` will mis-handle these silently.**')
        A('')
        for i in sorted(nonarc):
            A(f'- `{i}`')
        A('')

    A('## Verifying this file')
    A('')
    A('1. `python3 scripts/revivable/build_revivable.py --check` — exits nonzero')
    A('   if this file does not match the current graph.')
    A('2. Re-run without `--check` twice; the output is byte-identical (no')
    A('   timestamps, deterministic ordering), so any diff is a real graph change.')
    A('3. Spot-check a row against its source: every field is copied from the')
    A('   graph entry of the same `id`; nothing is inferred or summarised.')
    A('4. The graph **and** the registers are read from the same ref, so the')
    A('   `registers` column compares one snapshot against itself. Mixing refs')
    A('   there would silently misreport what is registered.')
    A('')
    return '\n'.join(L) + '\n'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true',
                    help='exit nonzero if docs/REVIVABLE.md is stale')
    ap.add_argument('--ref', default=None,
                    help='read the graph from a git ref (e.g. origin/main) '
                         'instead of the working tree')
    args = ap.parse_args()
    text = build(args.ref)
    if args.check:
        cur = _read(OUT) if os.path.isfile(OUT) else ''
        if cur != text:
            print('STALE: docs/REVIVABLE.md does not match kill_graph.json')
            return 1
        print('OK: docs/REVIVABLE.md is current')
        return 0
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, 'w', encoding='utf-8') as fh:
        fh.write(text)
    print(f'wrote {OUT} ({len(text):,} bytes)')
    return 0


if __name__ == '__main__':
    sys.exit(main())
