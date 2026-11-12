"""
REVIEW 79b, the web seat's reading of main's answers (M6): the checks its review file relies on, run once and committed
before the file.  Computed once; nothing here was sealed in advance.  Main at 896cae025; the window is 0dda7b472..896cae025.

  Q   every quotation in the findings table of the review file, as an exact substring of its file at 896cae025 (git show).
  L   the further strings the review names, each in its file at 896cae025, with the line it is said to stand on.
  P   B1882's page: each of the three corrected sentences stands once, after the first dated correction (booleans only).
  D   arc numbers that more than one folder under frontier/ carries, and how many of those folders have a verdict file.
  V   main's vendor pattern (imported from scripts/gates/gates.py, _VENDOR_RE; the names are not spelled here) and the
      co-author trailer (a line that begins "Co-Authored-By:"): hits in the messages of the window's commits and in the
      window's added lines; and the vendor pattern alone in this seat's review file and scripts.  Counts and paths only.

Usage: r79b_checks.py <the seat's checkout of main> <the review file>
"""
import collections
import importlib.util
import os
import re
import subprocess
import sys

MAIN, REVIEW = sys.argv[1], sys.argv[2]
REV, BASE = '896cae025', '0dda7b472'
HERE = os.path.dirname(os.path.abspath(__file__))


def git(*a):
    return subprocess.run(['git', '-C', MAIN, *a], capture_output=True, text=True).stdout


def show(path):
    return git('show', '%s:%s' % (REV, path))


def q():
    text = open(REVIEW, encoding='utf-8').read()
    bad = total = 0
    for m in re.finditer(r'^\| (B\d{3,4}) \| `([^`]+)`[^|]*\| "(.+?)" \|', text, re.M):
        arc, path, quote = m.groups()
        total += 1
        ok = quote in show(path)
        bad += not ok
        print('Q   %s %s: %s' % (arc, path, 'found' if ok else 'NOT FOUND'))
    print('Q   quotations checked: %d; not found: %d' % (total, bad))


PS = 'frontier/B1861_the_closure_programme/verification/programme_source.py'
PM = 'frontier/B1861_the_closure_programme/PROGRAMME.md'
L82 = 'frontier/B1882_the_v1_card_run_on_main/verification/test_b1882_the_v1_card_run_on_main.py'
L62 = 'frontier/B1862_the_audits_first_corrections/verification/test_b1862_the_audits_first_corrections.py'
L79 = 'frontier/B1879_the_weaves_theorems_with_the_exchange/verification/test_b1879_the_weaves_theorems_with_the_exchange.py'
GF = 'frontier/B862_global_form/global_form.py'
QY = 'scripts/atlas/query.py'
STRINGS = [
    (PS, 701, 'U("V'), (PS, 701, 'the audit\'s figure is reproduced'), (PS, 701, 'belongs to targets that fit nothing'),
    (PS, 701, 'below its neighbour'), (PS, 701, 'almost nothing at the bottom'),
    (PM, 954, 'below its neighbour'), (PM, 954, 'almost nothing at the bottom'), (PM, 954, 'belongs to targets that fit nothing'),
    (L82, 222, 'page.index(old) or old == "was reproduced on main in B1870"'),
    (L62, 189, 'the correction must name the split, not the sign alone'),
    (L62, 194, '_SPLIT = r"(?:only|'), (L62, 194, '|parity)"'),
    (L62, 203, '21 distinct eigenvalues'), (L62, 203, 'at most 20'),
    (L62, None, 'BEFORE, AFTER = 400, 900'), (L62, None, '".{0,500}?"'),
    (L62, None, 'put("docs/unrelated.md", "The charge is invisibility to every state). Elsewhere, in another matter, one has '
                'E = +I for the identity.")'),
    (L62, None, '"docs/unrelated.md": False'),
    (L79, None, '"is not among the\\n  thirteen"'),
    (GF, None, 'the grid of sixths is complete'), (GF, None, 'assert grid % 6 == 0'), (GF, None, 'charges[0] * q'),
    (QY, None, 'for h in hits[:1]:'), (QY, None, 'return dict(probe=arc_id, status=p["status"]'),
]


def l():
    bad = 0
    for path, line, s in STRINGS:
        src = show(path)
        lines = src.splitlines()
        if line is None:
            ok = src.count(s) >= 1
            where = 'in the file (%d times)' % src.count(s)
        else:
            ok = line <= len(lines) and s in lines[line - 1]
            where = 'on line %d' % line
        bad += not ok
        print('L   %s %s: %s' % (os.path.basename(path), where, 'found' if ok else 'NOT FOUND'))
    print('L   strings checked: %d; not found: %d' % (len(STRINGS), bad))


def p():
    page = show('frontier/B1882_the_v1_card_run_on_main/FINDINGS.md')
    c = page.find('CORRECTED 2026-11-12 (Review 79')
    for i, old in enumerate(('Those are targets that fit nothing.', 'At the bottom end, at less than a tenth of it.',
                             'was reproduced on main in B1870'), 1):
        print('P   B1882 page, sentence %d: stands %d time(s); after the first dated correction: %s'
              % (i, page.count(old), page.find(old) > c >= 0))


def d():
    dirs = [x[len('frontier/'):] for x in git('ls-tree', '-d', '--name-only', REV, 'frontier/').split('\n') if x]
    num = collections.Counter(m.group(1) for x in dirs for m in [re.match(r'(B\d+[a-z]?)_', x)] if m)
    files = set(git('ls-tree', '-r', '--name-only', REV, 'frontier/').split('\n'))
    for n, k in sorted(num.items()):
        if k > 1:
            with_v = sum(1 for x in dirs if x.startswith(n + '_') and 'frontier/%s/arc_verdict.json' % x in files)
            print('D   %s: %d folders, %d with a verdict file' % (n, k, with_v))
    print('D   arc numbers carried by more than one folder: %d' % sum(1 for k in num.values() if k > 1))


def v():
    spec = importlib.util.spec_from_file_location('gates_for_r79b', MAIN + '/scripts/gates/gates.py')
    g = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(g)
    trailer = re.compile(r'^\+?\s*co-authored-by:', re.I | re.M)
    hit = lambda s: bool(trailer.search(s) or g._VENDOR_RE.search(s))
    msgs = [m for m in git('log', '--format=%B%x00', BASE + '..' + REV).split('\x00') if m.strip()]
    print('V   commits in the window: %d; messages with a trailer or a vendor\'s name: %d' % (len(msgs), sum(map(hit, msgs))))
    diff = git('diff', BASE, REV)
    per = collections.Counter()
    cur = None
    for line in diff.splitlines():
        if line.startswith('+++ '):
            cur = line[6:] if line.startswith('+++ b/') else None
        elif line.startswith('+') and cur and hit(line):
            per[cur] += 1
    print('V   added lines in the window with a trailer or a vendor\'s name: %d, in %s' % (sum(per.values()), sorted(per) or 'no file'))
    mine = [REVIEW] + [os.path.join(HERE, f) for f in sorted(os.listdir(HERE)) if f.endswith('.py')]
    print('V   this seat\'s files with a vendor\'s name: %s'
          % ([os.path.basename(f) for f in mine if g._VENDOR_RE.search(open(f, encoding='utf-8').read())] or 'none'))


if __name__ == '__main__':
    print('r79b_checks at main %s (window %s..%s)' % (REV, BASE, REV))
    q()
    l()
    p()
    d()
    v()
