"""
REVIEW 80, the web seat: main's retraction sweep (scripts/checks/retraction_sweep.py at c40446392) on constructed
pages, in a scratch clone of main.  Computed once; nothing here was sealed in advance.  Main's files are never changed:
each case writes or appends one page in the scratch clone, stages it (the sweep reads `git ls-files`), runs the sweep's
own `sweep_all()` there, and resets the clone.

Two registered phrases are used, both named in the sweep's own table STANDS_AS_FOUND:
  P = "the sense of the root's 3-cycle as the chirality bit"   (held in one relay only)
  Q = "the only lifts that agree with the ruled moves"         (held, among others, in docs/POINT_REGISTER.md)

  B   the clone as it is: the sweep's violations (the gate passes at c40446392, so none is expected).
  C0  a new page, docs/PROBE_NOTE.md, stating P as a live claim on one line            (a control: one violation)
  R1  the same sentence, with a line break inside P                                    (a live claim)
  R2  the same sentence on one line, with an unrelated "corrected" later on the line   (a live claim)
  C1  a new page stating Q as a live claim in a register-like row                      (a control: one violation)
  R3  the same row appended to docs/POINT_REGISTER.md, as a new row                    (a live claim)

Usage: sweep_probe.py <the seat's checkout of main, at c40446392> <scratch directory>
"""
import importlib.util
import os
import pathlib
import shutil
import subprocess
import sys

MAIN, SCRATCH = pathlib.Path(sys.argv[1]).resolve(), pathlib.Path(sys.argv[2]).resolve() / 'sweep_clone'
P = "the sense of the root's 3-cycle as the chirality bit"
Q = 'the only lifts that agree with the ruled moves'
CASES = [
    ('B', None, None, False),
    ('C0', 'docs/PROBE_NOTE.md', 'The record says that %s decides the hand.\n' % P, False),
    ('R1', 'docs/PROBE_NOTE.md', 'The record says that %s decides the hand.\n' % P.replace(' 3-cycle ', ' 3-cycle\n'), False),
    ('R2', 'docs/PROBE_NOTE.md', 'The record says that %s decides the hand; a typo in section 2 is corrected below.\n' % P,
     False),
    ('C1', 'docs/PROBE_NOTE.md', '| P-999 | %s are the two of the record | OPEN |\n' % Q, False),
    ('R3', 'docs/POINT_REGISTER.md', '| P-999 | %s are the two of the record | OPEN |\n' % Q, True),
]


def git(*a):
    return subprocess.run(['git', '-C', str(SCRATCH), *a], capture_output=True, text=True, check=True).stdout


if SCRATCH.exists():
    shutil.rmtree(SCRATCH)
subprocess.run(['git', 'clone', '-q', '--shared', '--no-checkout', str(MAIN), str(SCRATCH)], check=True)
git('checkout', '-q', '--detach', 'c40446392')
print('scratch clone at', git('rev-parse', '--short', 'HEAD').strip())
for i, (key, rel, text, append) in enumerate(CASES):
    git('reset', '-q', '--hard', 'c40446392')
    git('clean', '-q', '-fd')
    if rel:
        path = SCRATCH / rel
        with open(path, 'a' if append else 'w', encoding='utf-8') as fh:
            fh.write(('\n' if append else '') + text)
        git('add', rel)
    spec = importlib.util.spec_from_file_location('rs_%d' % i, str(SCRATCH / 'scripts/checks/retraction_sweep.py'))
    rs = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(rs)
    if key == 'B':
        ph = rs._phrases()
        print('B   P is a swept phrase: %s; Q is a swept phrase: %s' % (P in ph, Q in ph))
    v, met = rs.sweep_all()
    mine = [x for x in v if x[0] == rel] if rel else v
    print('%-3s violations: %d in all, %d on the page of the case%s' % (key, len(v), len(mine),
          ('; ' + '; '.join('%s:%d' % (r, n) for r, n, _p in mine)) if mine else ''))
git('reset', '-q', '--hard', 'c40446392')
git('clean', '-q', '-fd')
