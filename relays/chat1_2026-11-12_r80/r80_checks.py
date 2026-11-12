"""
REVIEW 80, the web seat's reading: the checks its review file relies on, run once and committed before the file.
Computed once; nothing here was sealed in advance.  Main at c40446392; the window is 0dda7b472..c40446392.

  Q   every quotation in the findings table of the review file, as an exact substring of its file at c40446392.
  L   the further strings the review names, each in its file at c40446392, with the line it is said to stand on.
  C   counts the review states: the tables held by name in gates.py and retraction_sweep.py; the gates that read git; the
      rows of B1894's table by reader; Review 79's distinct faults from B1892's groups.
  R   the seven asserts of the form `... or True` (code_probe.py, S): whether any register row or the error ledger names
      their files; and the 53 controls of tests/GATE_CONTROLS.json: how many sit in a module that may skip itself at import
      under an `if`, a `try` or a `with`.
  W   Review 79's window by git: commits, arcs added, arcs whose verdict or findings changed, and those on no reader's
      card; and the arcs added in this window.
  V   main's vendor pattern (imported from scripts/gates/gates.py, _VENDOR_RE; the names are not spelled here) and the
      co-author trailer: hits in the messages of the window's commits and in its added lines; the pattern alone in this
      seat's review file and scripts.  Counts and paths only.

Usage: r80_checks.py <the seat's checkout of main, at c40446392> <the review file>
"""
import ast
import collections
import importlib.util
import json
import os
import re
import subprocess
import sys

MAIN, REVIEW = sys.argv[1], sys.argv[2]
REV, BASE = 'c40446392', '0dda7b472'
HERE = os.path.dirname(os.path.abspath(__file__))


def git(*a):
    return subprocess.run(['git', '-C', MAIN, *a], capture_output=True, text=True).stdout


def show(path):
    return git('show', '%s:%s' % (REV, path))


def q():
    text = open(REVIEW, encoding='utf-8').read()
    bad = total = 0
    for m in re.finditer(r'^\| (\d+) \| `([^`]+)`[^|]*\| "(.+?)" \|', text, re.M):
        n, path, quote = m.groups()
        total += 1
        ok = quote in show(path)
        bad += not ok
        print('Q   %s %s: %s' % (n, path, 'found' if ok else 'NOT FOUND'))
    print('Q   quotations checked: %d; not found: %d' % (total, bad))


GT = 'scripts/gates/gates.py'
RS = 'scripts/checks/retraction_sweep.py'
CV = 'scripts/checks/check_test_vacuity.py'
RP = 'docs/RETRACTED_PHRASES.md'
F91 = 'frontier/B1891_the_foundation_at_version_1_66/FINDINGS.md'
L91 = 'frontier/B1891_the_foundation_at_version_1_66/verification/test_b1891_the_foundation_at_version_1_66.py'
F94 = 'frontier/B1894_review_79_the_second_round/FINDINGS.md'
F96 = 'frontier/B1896_the_third_enforcement_series_verified_and_landed/FINDINGS.md'
F84 = 'frontier/B1884_what_level_a_ground_names_verified/arc_verdict.json'
PR = 'docs/POINT_REGISTER.md'
EL = 'docs/ERROR_LEDGER.md'
STRINGS = [
    (CV, 2, 'Find test functions that pass unconditionally -- locks that cannot fail.'),
    (RS, 56, 'A line is a MENTION (allowed) if it carries any of these near the phrase.'),
    (RS, 279, 'mention = MENTION_CUES.search(line) or MENTION_CUES.search(flat)'),
    (RS, 284, 'if (rel, phrase) in STANDS_AS_FOUND:'),
    (RP, 222, "that line is held by name in the sweep's own table, by its file and its phrase"),
    (F96, 44, 'where a newly read phrase already stood, the line is held by name'),
    (GT, 2742, '(1) the control is not skipped: no skip or xfail mark on it or on its module, and no call that skips in its body;'),
    (GT, 2763, "# the module's own mark, or a skip at import"),
    (GT, 1133, 'healed = len(CANNOT_FAIL_AS_FOUND) - len(held) if held else 0'),
    (GT, 1105, 'Only the two hard classes gate.'),
    (L91, 3, 'one of the four corrected sentences standing in its old'),
    (L91, 48, 'for old in ("Eleven entries", "every statement the record holds about the weave is unchanged except the hand"):'),
    (F91, 20, 'is the only history of at most five letters that does'),
    (F94, 94, 'is a living page and quotes nothing he said'),
    (F91, 32, 'The foundation still quotes the owner elsewhere.'),
    (PR, 1014, 'they are counted and left, the ruling leaving what was written before it'),
    (PR, 1018, 'any marker word near the old form counted as its correction'),
    (EL, 236, 'an assertion ending in "or True"'),
    (F96, 160, 'the vacuity class is decided by working the assert out and stops at a call'),
    (PR, 1021, 'a retracted phrase with a line break in its middle'),
    (PR, 1021, 'a second instance of a held phrase in the file that holds it'),
    (PR, 1021, 'a control skipped at run time by a helper or a fixture'),
    (PR, 1021, 'a clause that is not a literal and is always true'),
    (EL, 182, "B1604's lock ended its assertion `\u2026 or True`"),
    (F84, None, "THE WEB SEAT'S SEALED CARD ON WHAT LEVEL A GROUND NAMES, VERIFIED ON MAIN"),
    ('tests/test_r28_10_stabilizations.py', 104, ') or True  # eigenvalues are in Q(sqrt5)'),
    ('frontier/B862_global_form/global_form.py', None, 'need = math.gcd(3 * abs(c1), 2 * abs(c2))'),
    ('docs/RETRACTIONS.md', None, '## Currency read 2026-11-12 (window B1837'),
]


def l():
    bad = 0
    for path, line, s in STRINGS:
        src = show(path)
        lines = src.splitlines()
        ok = (s in src) if line is None else (line <= len(lines) and s in lines[line - 1])
        bad += not ok
        print('L   %s %s: %s' % (os.path.basename(path), 'in the file' if line is None else 'line %d' % line,
                                  'found' if ok else 'NOT FOUND'))
    print('L   strings checked: %d; not found: %d' % (len(STRINGS), bad))


def c():
    spec = importlib.util.spec_from_file_location('gates_r80c', os.path.join(MAIN, GT))
    g = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(g)
    spec = importlib.util.spec_from_file_location('rs_r80c', os.path.join(MAIN, RS))
    rs = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(rs)
    print('C   held by name: FRAMING_EXEMPT %d (one added in the window), CITES_NO_LOCK_AS_FOUND %d, CANNOT_FAIL_AS_FOUND %d, '
          'NOT_SWEPT_BY_NAME %d, STANDS_AS_FOUND %d' % (len(g.FRAMING_EXEMPT), len(g.CITES_NO_LOCK_AS_FOUND),
                                                       len(g.CANNOT_FAIL_AS_FOUND), len(rs.NOT_SWEPT_BY_NAME), len(rs.STANDS_AS_FOUND)))
    print('C   gates that read git: %d (%d tracked, %d history); controls registered: %d'
          % (len(g.READS_GIT), len(g.READS_TRACKED), len(g.READS_HISTORY), len(json.loads(show('tests/GATE_CONTROLS.json')))))
    a = show('frontier/B1894_review_79_the_second_round/ANSWERS.md')
    ids = re.findall(r'(?m)^\| (2(?:W|SM-|A|X)\d+) \|', a)
    by = collections.Counter(re.match(r'2(W|SM-|A|X)', i).group(1) for i in ids)
    print('C   B1894 rows: %d; by reader %s' % (len(ids), dict(by)))
    A = json.loads(show('frontier/B1892_review_79_read_by_those_who_did_not_build_it/verification/answers.json'))
    print('C   B1892: findings %d; groups %d; distinct by the groups %d; stated %d'
          % (A['findings'], len(A['reported by two readers']),
             A['findings'] - sum(len(x) - 1 for x in A['reported by two readers']) + 1, A['distinct faults']))


def r():
    files = ['tests/test_b1011_mckay_tensor.py', 'tests/test_b355_weil_layer_independent.py', 'tests/test_b448.py',
             'tests/test_b674_route1.py', 'tests/test_b799_doors.py', 'tests/test_r28_10_stabilizations.py',
             'tests/test_w2_molien_cell.py']
    named = {f: [p for p in (PR, EL) if os.path.basename(f)[:-3] in show(p)] for f in files}
    print('R   the seven files named in the register or the error ledger: %s' % ({k: v for k, v in named.items() if v} or 'none'))
    reg = json.loads(show('tests/GATE_CONTROLS.json'))
    sk = re.compile(r'\b(skip|skipif|xfail|importorskip)\b')
    n = 0
    for ref in reg.values():
        tree = ast.parse(show(ref.split('::')[0]))
        for node in tree.body:
            if isinstance(node, (ast.If, ast.Try, ast.With)) and any(
                    isinstance(x, ast.Call) and sk.search(ast.unparse(x.func)) for x in ast.walk(node)):
                n += 1
                break
    print('R   controls in a module that may skip itself at import under an if, a try or a with: %d of %d' % (n, len(reg)))


def w():
    st = git('diff', '--name-status', '38d2a36dc', BASE, '--', 'frontier/')
    added, ver, fin = set(), set(), set()
    for line in st.splitlines():
        kind, path = line.split('\t')[0], line.split('\t')[-1]
        m = re.match(r'frontier/(B\d+)_[^/]*/(arc_verdict\.json|FINDINGS\.md)$', path)
        if not m:
            continue
        arc, f = m.groups()
        if kind == 'A' and f == 'arc_verdict.json':
            added.add(arc)
        elif kind == 'M':
            (ver if f == 'arc_verdict.json' else fin).add(arc)
    ver, fin = ver - added, fin - added
    cards = {'B874', 'B892', 'B1221', 'B1486', 'B1494', 'B1499', 'B1641', 'B1675', 'B1726', 'B1753', 'B1853', 'B1861',
             'B1872', 'B1874', 'B1877'}
    key = lambda x: int(x[1:])
    print('W   Review 79 window: commits %s; added arcs %d; verdict changed %d; findings changed %d (%d of them alone); '
          'changed arcs in all %d; on no card\'s list: %s'
          % (git('rev-list', '--count', '38d2a36dc..' + BASE).strip(), len(added), len(ver), len(fin), len(fin - ver),
             len(ver | fin), sorted((ver | fin) - cards, key=key)))
    print('W   this window: arcs added %s' % sorted(x for x in re.findall(r'frontier/(B\d+)_[^/]*/arc_verdict\.json',
          '\n'.join(l.split('\t')[-1] for l in git('diff', '--name-status', BASE, REV, '--', 'frontier/').splitlines()
                     if l.startswith('A')))))


def v():
    spec = importlib.util.spec_from_file_location('gates_r80v', os.path.join(MAIN, GT))
    g = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(g)
    trailer = re.compile(r'^\+?\s*co-authored-by:', re.I | re.M)
    hit = lambda s: bool(trailer.search(s) or g._VENDOR_RE.search(s))
    msgs = [m for m in git('log', '--format=%B%x00', BASE + '..' + REV).split('\x00') if m.strip()]
    print('V   commits in the window: %d; messages with a trailer or a vendor\'s name: %d' % (len(msgs), sum(map(hit, msgs))))
    per = collections.Counter()
    cur = None
    for line in git('diff', BASE, REV).splitlines():
        if line.startswith('+++ '):
            cur = line[6:] if line.startswith('+++ b/') else None
        elif line.startswith('+') and cur and hit(line):
            per[cur] += 1
    print('V   added lines in the window with a trailer or a vendor\'s name: %d, in %s' % (sum(per.values()), sorted(per) or 'no file'))
    mine = [REVIEW] + [os.path.join(HERE, f) for f in sorted(os.listdir(HERE)) if f.endswith('.py')]
    print('V   this seat\'s files with a vendor\'s name: %s'
          % ([os.path.basename(f) for f in mine if g._VENDOR_RE.search(open(f, encoding='utf-8').read())] or 'none'))


if __name__ == '__main__':
    print('r80_checks at main %s (window %s..%s)' % (REV, BASE, REV))
    q()
    l()
    c()
    r()
    w()
    v()
