#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
W-C1: PLANTED CASES AGAINST MAIN'S TWO LOCKS, IN A SCRATCH CLONE.   The web seat (chat1), 2026-11-11.

Each case starts from a clean checkout of main at 2f3984d27 in a scratch clone, makes one change, runs one lock with
pytest, and records CAUGHT (the lock fails) or PASSES (the lock passes).  Main's files are never touched: the clone is
made from the seat's checkout of main and thrown away.  Each case's expected outcome is written here before any case
has run.  A PASSES that was expected is a gap the seat names; a CAUGHT that was expected is the lock working.  The two
baselines must PASS, or the harness is broken.

The seat wrote these after reading both locks, so the expectations test its reading of them as much as the locks.

Usage: planted.py <path to the seat's checkout of main> <scratch directory>
"""
import json
import pathlib
import shutil
import subprocess
import sys

COMMIT = '2f3984d27'
E2_TEST = 'tests/test_b734_m004_congruence.py'
E7_TEST = 'tests/test_b1028_freedom_ledger.py'


def append(rel, text):
    def f(root):
        p = root / rel
        p.write_text(p.read_text(encoding='utf-8') + text, encoding='utf-8')
    return f


def write(rel, text):
    def f(root):
        p = root / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding='utf-8')
    return f


def edit_json(rel, fn):
    def f(root):
        p = root / rel
        v = json.loads(p.read_text(encoding='utf-8'))
        fn(v)
        p.write_text(json.dumps(v, ensure_ascii=False, indent=1), encoding='utf-8')
    return f


def replace(rel, old, new):
    def f(root):
        p = root / rel
        t = p.read_text(encoding='utf-8')
        assert t.count(old) >= 1, (rel, old[:40])
        p.write_text(t.replace(old, new, 1), encoding='utf-8')
    return f


def nothing(root):
    pass


B734V = 'frontier/B734_m004_is_congruence/arc_verdict.json'
B1028V = 'frontier/B1028_freedom_ledger/arc_verdict.json'


def strip_b734_lead(v):
    lead = "CORRECTED 2026-11-11 (the audit's finding E2): THE FIGURE-EIGHT KNOT GROUP IS A CONGRUENCE SUBGROUP OF LEVEL (4), not (8) as first asserted. "
    assert v['claim_one_line'].startswith(lead)
    v['claim_one_line'] = v['claim_one_line'][len(lead):]


def strip_b1028_lead(v):
    lead = "CORRECTED 2026-11-11 (the audit's finding E7; main): "
    assert v['claim_one_line'].startswith(lead)
    v['claim_one_line'] = v['claim_one_line'][len(lead):]


def set_proved(v):
    v['verdict'] = 'PROVED'


CASES = [
    # (name, lock, change, expected, why)
    ('E2-0 baseline', E2_TEST, nothing, 'PASSES', 'the harness: nothing planted'),
    ('E2-1 the arc\'s line no longer leads with the correction', E2_TEST, edit_json(B734V, strip_b734_lead), 'CAUGHT', 'the lead is tested'),
    ('E2-2 the ambient order at (4) typed as the quotient\'s', E2_TEST, replace(E2_TEST, '_SL = {2: 60, 4: 3840, 8: 245760}', '_SL = {2: 60, 4: 1920, 8: 245760}'), 'CAUGHT', 'the typed order is pinned by a count'),
    ('E2-3 a new page under docs/ states level (8)', E2_TEST, write('docs/PLANTED_NOTE.md', 'The figure-eight knot group m004 is congruence at level (8).\n'), 'CAUGHT', 'docs/ is swept'),
    ('E2-4 the foundation states level (8)', E2_TEST, append('GENESIS.md', '\n| PLANT | the figure-eight knot group m004 is congruence at level (8) |\n'), 'PASSES', 'root pages other than README are not swept'),
    ('E2-5 the claims ledger states level (8)', E2_TEST, append('CLAIMS.md', '\n| PLANT | the figure-eight knot group m004 is congruence at level (8) |\n'), 'PASSES', 'root pages other than README are not swept'),
    ('E2-6 the knot named 4_1', E2_TEST, write('docs/PLANTED_NOTE.md', 'The knot 4₁ is congruence at level (8).\n'), 'PASSES', 'the subject pattern does not know the name 4_1'),
    ('E2-7 "contains Gamma(8) and not Gamma(4)"', E2_TEST, write('docs/PLANTED_NOTE.md', 'The figure-eight knot group m004 is congruence: it contains Γ(8) and not Γ(4).\n'), 'PASSES', 'only the doubled bracket is a spelling'),
    ('E2-8 "level 2 cubed"', E2_TEST, write('docs/PLANTED_NOTE.md', 'm004 is a congruence subgroup of level 2³.\n'), 'PASSES', 'the cube is a spelling only inside brackets'),
    ('E2-9 the programme page states level (8)', E2_TEST, append('frontier/B1861_the_closure_programme/PROGRAMME.md', '\nThe figure-eight knot group m004 is congruence at level (8).\n'), 'PASSES', 'the programme is listed as history'),
    ('E2-10 a page that carries the correction states level (8) again', E2_TEST, append('docs/LAW_MAP.md', '\nm004 is congruence at level (8).\n'), 'PASSES', 'the stated rule: a page with the correction is not read further'),
    ('E2-11 another arc\'s verdict line states level (8)', E2_TEST, write('frontier/B9999_planted/arc_verdict.json', json.dumps({'id': 'B9999', 'verdict': 'PROVED', 'claim_one_line': 'm004 is congruence at level (8).'})), 'CAUGHT', 'verdict lines are swept'),
    ('E2-12 a .tex source states level (8)', E2_TEST, write('papers/PLANTED.tex', 'The figure-eight knot group is congruence at level $(8)$.\n'), 'CAUGHT', '.tex under papers/ is swept'),
    ('E7-0 baseline', E7_TEST, nothing, 'PASSES', 'the harness: nothing planted'),
    ('E7-1 the verdict back to PROVED', E7_TEST, edit_json(B1028V, set_proved), 'CAUGHT', 'the verdict is tested'),
    ('E7-2 the line no longer leads with the correction', E7_TEST, edit_json(B1028V, strip_b1028_lead), 'CAUGHT', 'the lead is tested'),
    ('E7-3 a new page under docs/ states the zero', E7_TEST, write('docs/PLANTED_NOTE.md', 'The freedom ledger (B1028) shows 0.000 bits of designer freedom.\n'), 'CAUGHT', 'docs/ is swept'),
    ('E7-4 the foundation states the zero', E7_TEST, append('GENESIS.md', '\nB1028: 0.000 bits of designer freedom.\n'), 'CAUGHT', 'five root pages are swept'),
    ('E7-5 the zero in other words', E7_TEST, write('docs/PLANTED_NOTE.md', 'The freedom ledger (B1028) found no designer freedom at all in the chain.\n'), 'PASSES', 'only three spellings'),
    ('E7-6 "0 bits"', E7_TEST, write('docs/PLANTED_NOTE.md', 'The freedom ledger (B1028) shows 0 bits of designer freedom.\n'), 'PASSES', 'only three spellings'),
    ('E7-7 a .tex source states the zero', E7_TEST, write('papers/PLANTED.tex', 'The freedom ledger (B1028) shows 0.000 bits of designer freedom.\n'), 'PASSES', 'only .md files are swept'),
    ('E7-8 another arc\'s verdict line states the zero', E7_TEST, write('frontier/B9999_planted/arc_verdict.json', json.dumps({'id': 'B9999', 'verdict': 'PROVED', 'claim_one_line': "B1028's freedom ledger: 0.000 bits of designer freedom."})), 'PASSES', 'verdict lines are not swept'),
    ('E7-9 one price changed in the walk', E7_TEST, replace('frontier/B1028_freedom_ledger/b1028_walk.py', 'link="faces", price=0.0', 'link="faces", price=0.5'), 'CAUGHT', 'the typed zeros are pinned'),
    ('E7-10 the programme page states the zero', E7_TEST, append('frontier/B1861_the_closure_programme/PROGRAMME.md', '\nB1028: 0.000 bits of designer freedom.\n'), 'PASSES', 'the programme is listed as history'),
    ('E7-11 a page that carries the correction states the zero again', E7_TEST, append('docs/THE_CLAIM.md', '\nB1028: 0.000 bits of designer freedom.\n'), 'PASSES', 'the stated rule: a page with the correction is not read further'),
]


def run_case(src, scratch, case):
    name, test, change, expected, why = case
    if scratch.exists():
        shutil.rmtree(scratch)
    subprocess.run(['git', 'clone', '-q', '--no-checkout', '--no-hardlinks', str(src), str(scratch)], check=True)
    subprocess.run(['git', '-C', str(scratch), '-c', 'advice.detachedHead=false', 'checkout', '-q', COMMIT], check=True)
    change(scratch)
    r = subprocess.run([sys.executable, '-m', 'pytest', '-q', '-p', 'no:cacheprovider', test], cwd=str(scratch), capture_output=True, text=True)
    got = 'PASSES' if r.returncode == 0 else 'CAUGHT'
    failing = [l.split('::')[-1].split(' ')[0] for l in r.stdout.splitlines() if l.startswith('FAILED')]
    return got, failing


def main():
    src = pathlib.Path(sys.argv[1]).resolve()
    scratch = pathlib.Path(sys.argv[2]).resolve() / 'clone'
    print('W-C1: planted cases against the locks of B734 and B1028 (main at %s; a scratch clone per case)' % COMMIT)
    agree = 0
    for case in CASES:
        got, failing = run_case(src, scratch, case)
        ok = got == case[3]
        agree += ok
        print('  %-62s expected %-6s got %-6s %s  %s' % (case[0], case[3], got, 'as expected' if ok else 'NOT AS EXPECTED', ('[' + ', '.join(failing) + ']') if failing else ''))
    shutil.rmtree(scratch, ignore_errors=True)
    base = [c for c in CASES if c[0].endswith('baseline')]
    print()
    print('as expected: %d of %d' % (agree, len(CASES)))
    return 0


if __name__ == '__main__':
    sys.exit(main())
