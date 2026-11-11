"""
REVIEW 79, the web seat's reading: the computations its review file relies on, run once and committed before the file.
Computed once; nothing here was sealed in advance.  Main at 323f92327.

  K1  B1882: the exact (Clopper-Pearson) 95% intervals for the 13 counts its null run prints, out of 1000; and the
      thresholds for A, 2 x 1000 x r, with r = 1/15 and 0.0673.
  K2  B1886: the first status word of every row of GENESIS.md whose first cell is an identifier (T-ROOT included), at
      8f0b03814 (version 1.64) and at 323f92327; which changed, which are new.  A route of this seat's own, not the
      arc's lock.
  K2b B1886: every row of every table of GENESIS.md whose header has a cell "Status", keyed by its first cell, at the
      two commits: which status cells changed.  This reaches the rows the arc's lock does not read.
  K3  B1883: which packages each milestone of the closure programme (B1861's PROGRAMME.json) counts; which package is
      counted twice and which in none.  Only package identifiers, obligations and states are printed.
  K4  B1878: the number of first-parent commits after da25c4f49 up to B1878's landing, and how many of their messages
      carry a co-author trailer or a vendor's name.  Needs the history from 2026-09-10 in the checkout.  The names are
      not spelled here: the pattern is main's own, imported from its gate (scripts/gates/gates.py, _VENDOR_RE).
  K5  B1886: its lock run once in the checkout (pytest), the summary line only.
  Q   every quotation of the review file, checked as an exact substring of its file at 323f92327 (by `git show`).

Usage: r79_checks.py <the seat's checkout of main> <the review file>
"""
import collections
import json
import re
import subprocess
import sys

from scipy.stats import beta

MAIN = sys.argv[1]
REV = '323f92327'


def show(rev, path):
    return subprocess.run(['git', '-C', MAIN, 'show', '%s:%s' % (rev, path)], capture_output=True, text=True).stdout


def k1():
    print('K1  exact 95% intervals, k of 1000:')
    for k in (4, 109, 6, 134, 132, 12, 130, 3, 128, 140, 7, 143, 159):
        lo = beta.ppf(0.025, k, 1000 - k + 1) if k else 0.0
        hi = beta.ppf(0.975, k + 1, 1000 - k)
        print('    %4d  [%.4f, %.4f]' % (k, lo, hi))
    print('    thresholds for A: %.1f (r = 1/15) and %.1f (r = 0.0673)' % (2000 / 15, 2000 * 0.0673))


def k2():
    ident = re.compile(r'[A-Z]{1,4}(?:[:-][A-Z0-9]+)*\d*[a-z]?')

    def rows(rev):
        out = {}
        for line in show(rev, 'GENESIS.md').splitlines():
            if not line.startswith('|'):
                continue
            cells = [c.strip() for c in line.strip('|').split('|')]
            c0 = cells[0].replace('*', '').replace('`', '').strip() if cells else ''
            if not ident.fullmatch(c0) or not re.search(r'\d|-', c0):
                continue
            words = [w for c in cells[1:] for w in re.findall(
                r'\b(DERIVED|CONDITIONAL|OPEN|POSTULATED|CHOSEN|NEGATIVE|PROVED|RETRACTED)\b', c)]
            out.setdefault(c0, words[:1])
        return out
    a, b = rows('8f0b03814'), rows(REV)
    common = [k for k in a if k in b]
    print('K2  rows with no status word this route knows: %s' % sorted(k for k in a if not a[k]))

    def rows_prefix(rev):
        out = {}
        for line in show(rev, 'GENESIS.md').splitlines():
            if not line.startswith('|'):
                continue
            cells = [c.strip() for c in line.strip('|').split('|')]
            m = re.match(r'^\**`?([A-Z]{1,4}:?[A-Z0-9-]*\d+[a-z]?)`?\**', cells[0]) if cells else None
            if m:
                out.setdefault(m.group(1), True)
        return out
    print('K2  items whose row only begins with an identifier, new since v1.64: %s'
          % sorted(set(rows_prefix(REV)) - set(rows_prefix('8f0b03814'))))
    print('K2  identifiers at v1.64: %d (%d with a status word); at %s: %d; common: %d; first status word changed: %s; '
          'new: %s; T-ROOT matched: %s' % (len(a), sum(1 for k in a if a[k]), REV, len(b), len(common),
                                          [k for k in common if a[k] != b[k]], sorted(set(b) - set(a)), 'T-ROOT' in a))

    def status_tables(rev):
        out = {}
        header = None
        for line in show(rev, 'GENESIS.md').splitlines():
            if not line.startswith('|'):
                header = None
                continue
            cells = [c.strip() for c in line.strip('|').split('|')]
            if header is None:
                header = cells
                continue
            if set(cells) <= {'', '---', ':---', '---:'} or all(re.fullmatch(r':?-+:?', c or '-') for c in cells):
                continue
            if 'Status' in header:
                i = header.index('Status')
                if i < len(cells):
                    out[cells[0]] = cells[i]
        return out
    a, b = status_tables('8f0b03814'), status_tables(REV)
    common = [k for k in a if k in b]
    print('K2b rows of tables with a Status column: %d at v1.64, %d at %s; common %d; status changed: %d; '
          'rows gone: %d; rows new: %d' % (len(a), len(b), REV, len(common), sum(1 for k in common if a[k] != b[k]),
                                          len(set(a) - set(b)), len(set(b) - set(a))))


def k3():
    d = json.loads(show(REV, 'frontier/B1861_the_closure_programme/PROGRAMME.json'))
    pk = {p['id']: (p['obligation'], p['status'].split(' (')[0]) for p in d['packages']}
    obs = collections.defaultdict(list)
    for pid, (ob, st) in pk.items():
        obs[ob].append(pid)
    count = collections.Counter()
    for m in d['milestones']:
        members = m[3]
        ids = [x for x in members if x in pk] + [p for ob in members for p in obs.get(ob, [])]
        print('K3  %s: members %s -> %d packages' % (m[0], members, len(ids)))
        for x in ids:
            count[x] += 1
    print('K3  packages: %d; in no milestone: %s; in more than one: %s'
          % (len(pk), [(p, pk[p]) for p in pk if count[p] == 0], [(p, pk[p], count[p]) for p in pk if count[p] > 1]))


def k4():
    import importlib.util
    spec = importlib.util.spec_from_file_location('gates_for_r79', MAIN + '/scripts/gates/gates.py')
    g = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(g)
    land = '7480c2426'
    n = subprocess.run(['git', '-C', MAIN, 'rev-list', '--first-parent', '--count', 'da25c4f49..' + land],
                       capture_output=True, text=True).stdout.strip()
    msgs = subprocess.run(['git', '-C', MAIN, 'log', '--first-parent', '--format=%B%x00', 'da25c4f49..' + land],
                          capture_output=True, text=True).stdout.split('\x00')
    pat = re.compile(r'co-authored-by', re.I)
    hits = sum(1 for m in msgs if pat.search(m) or g._VENDOR_RE.search(m))
    print('K4  first-parent commits after da25c4f49 up to B1878\'s landing %s: %s; messages with a trailer or a vendor\'s '
          'name: %d' % (land, n, hits))


def k5():
    r = subprocess.run([sys.executable, '-m', 'pytest', '-q', '-p', 'no:cacheprovider',
                        'frontier/B1886_the_foundation_at_version_1_65/verification/'], cwd=MAIN, capture_output=True,
                       text=True)
    last = [l for l in r.stdout.splitlines() if l.strip()][-1:]
    print('K5  B1886\'s lock at %s: %s' % (REV, last[0] if last else '(no output)'))


def q(review):
    text = open(review, encoding='utf-8').read()
    bad = 0
    total = 0
    for m in re.finditer(r'^\| (B\d{4}) \| `([^`]+)`[^|]*\| "(.+?)" \|', text, re.M):
        arc, path, quote = m.group(1), m.group(2), m.group(3)
        quote = quote.replace('\\"', '"')
        total += 1
        src = show(REV, path)
        ok = quote in src
        bad += (not ok)
        print('Q   %s %s: %s' % (arc, path, 'found' if ok else 'NOT FOUND'))
    print('Q   quotations checked: %d; not found: %d' % (total, bad))


if __name__ == '__main__':
    k1()
    k2()
    k3()
    k4()
    k5()
    if len(sys.argv) > 2:
        q(sys.argv[2])
