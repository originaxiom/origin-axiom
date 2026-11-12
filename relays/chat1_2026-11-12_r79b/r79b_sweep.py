"""
REVIEW 79b: the sweep.  The old wording of each of the web seat's ten findings of Review 79 (W1 to W10), and of the
sentences B1882's correction of 2026-11-12 names, looked for in every tracked text file of main at 896cae025.
Computed once; nothing here was sealed in advance.

Each file's text is read with its line breaks and its quotation marks of block quotes ("> ") joined, so a phrase broken
across lines is found.  For each place the script prints the file and whether a dated correction stands near it: the
word "corrected" or "scoped" (any case) within 1,500 characters before the phrase or 600 after it.  That is a pointer for
reading, not a judgment: each place is then read through the mask.  Paths, counts and flags only; no text is printed.

Usage: r79b_sweep.py <the seat's checkout of main>
"""
import re
import subprocess
import sys

MAIN, REV = sys.argv[1], '896cae025'
PHRASES = [
    ('W1', 'at less than a tenth of it'),
    ('W1', '1.5 to 2 times'),
    ('W1/W7', 'bottom end would add almost none'),
    ('W1/W7', 'a lower bottom end almost none'),
    ('W1/W7', 'almost nothing at the bottom'),
    ('W2', "waits on a computation, at the owner's word"),
    ('W3', 'compares them all with the committed v1.64'),
    ('W4', 'this checkout does not hold the commit of version 1.64'),
    ('W5', 'longer than the true one and not shorter'),
    ('W6', 'never touches the measured values'),
    ('W7', 'would add almost none (0.06)'),
    ('W8', 'the last layer is below its neighbour'),
    ('W9', 'Eleven entries of the record came as suppositions'),
    ('W10', '16 statements of what he means, which are his to make; 11'),
    ('B1882 1', "the audit's figure is reproduced"),
    ('B1882 2', 'targets that fit nothing'),
]
NEAR = re.compile(r'corrected|scoped', re.I)


def git(*a):
    return subprocess.run(['git', '-C', MAIN, *a], capture_output=True, text=True).stdout


files = [f for f in git('ls-tree', '-r', '--name-only', REV).split('\n')
         if f.endswith(('.md', '.json', '.txt', '.tex', '.py', '.html', '.csv', '.yaml', '.yml'))]
texts = {}
for f in files:
    raw = subprocess.run(['git', '-C', MAIN, 'show', '%s:%s' % (REV, f)], capture_output=True).stdout
    try:
        t = raw.decode('utf-8')
    except UnicodeDecodeError:
        continue
    texts[f] = ' '.join(re.sub(r'(?m)^\s*>\s?', ' ', t).split())
print('sweep at main %s: %d tracked text files read' % (REV, len(texts)))
for key, ph in PHRASES:
    rows = []
    for f, t in texts.items():
        for m in re.finditer(re.escape(ph), t, re.I):
            near = bool(NEAR.search(t[max(0, m.start() - 1500):m.end() + 600]))
            rows.append((f, near))
    print('%-8s "%s": %d place(s) in %d file(s)' % (key, ph, len(rows), len({f for f, _ in rows})))
    for f, near in rows:
        print('           %s  correction near: %s' % (f, 'yes' if near else 'NO'))
