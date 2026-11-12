"""
REVIEW 80, the web seat, second addition (M12): main's answers to the seat's seven, and main's mends for W1, W3, W6, W7.
Computed once; nothing here was sealed in advance.  Main's files are never changed: plants are made in a scratch
worktree of main at 10fbbc1c2 and reset after each case.  Nothing behind the firewall is read or printed: pytest is run
with --tb=no, and only pass/fail lines and counts are printed.

  S   asserts whose test is an `or` with a truthy constant among its terms, by the syntax tree, at 5c7abd72a and 10fbbc1c2
  T   the seven mended tests, run at 10fbbc1c2
  N   each mended assert of W1 that remains, its test negated in place: the test must then fail (the assert is reached
      and its statement is what decides it)
  K   B1891's lock: K0 the first old form appended (control: fails); K1 the fourth old form appended (main's plant);
      K2 the fourth old form put directly after its corrected sentence
  Q   the quotations the addition relies on, each found in its file at 10fbbc1c2
  G   GENESIS.md's version line names 1.67 (W7)

Usage: r80_m12_checks.py <checkout of main with 10fbbc1c2 fetched> <scratch worktree of main at 10fbbc1c2>
"""
import ast, pathlib, re, subprocess, sys

MAIN, WT = pathlib.Path(sys.argv[1]).resolve(), pathlib.Path(sys.argv[2]).resolve()
NEW, OLD = '10fbbc1c2', '5c7abd72a'


def git(repo, *a):
    return subprocess.run(['git', '-C', str(repo), *a], capture_output=True, text=True).stdout


def pytest(*ids):
    r = subprocess.run([sys.executable, '-m', 'pytest', '-q', '--tb=no', '-p', 'no:cacheprovider', *ids], cwd=WT,
                       capture_output=True, text=True)
    last = [l for l in r.stdout.splitlines() if l.strip()][-1:]
    return last[0] if last else '(no output)'


# S
for rev in (OLD, NEW):
    hits = []
    for f in git(MAIN, 'ls-tree', '-r', '--name-only', rev).split():
        if not f.endswith('.py'):
            continue
        try:
            tree = ast.parse(git(MAIN, 'show', f'{rev}:{f}'))
        except Exception:
            continue
        for n in ast.walk(tree):
            if isinstance(n, ast.Assert) and isinstance(n.test, ast.BoolOp) and isinstance(n.test.op, ast.Or) and \
                    any(isinstance(v, ast.Constant) and v.value for v in n.test.values):
                hits.append(f)
    print('S  %s: %d asserts, %d in tests/' % (rev, len(hits), sum(h.startswith('tests/') for h in hits)))

# T
MENDED = {
    'tests/test_b1011_mckay_tensor.py': 'test_the_forced_counts_and_the_value_sets',
    'tests/test_b355_weil_layer_independent.py': 'test_weil_divisibility_operator_level',
    'tests/test_b448.py': 'test_orbit_tower_fields',
    'tests/test_b674_route1.py': 'test_trace_silence_and_golden_rotation',
    'tests/test_b799_doors.py': 'test_b332_deck_element_is_hyperbolic_and_det_A_minus_I_is_minus_one',
    'tests/test_r28_10_stabilizations.py': 'TestTombL255::test_golden_seed_eigenvalues_rank1',
    'tests/test_w2_molien_cell.py': 'test_decisive_identities_exact',
}
git(WT, 'checkout', '-q', '--detach', NEW)
print('T  the seven at %s: %s' % (NEW, pytest(*[f'{f}::{t}' for f, t in MENDED.items()])))

# N
for f, t in MENDED.items():
    p = WT / f
    src = p.read_text(encoding='utf-8')
    lines = src.splitlines(keepends=True)
    mark = [i + 1 for i, l in enumerate(lines) if "the web seat's finding 1" in l and 'CORRECTED' in l]
    if not mark:
        print('N  %s: no CORRECTED mark (the line was removed)' % f)
        continue
    asserts = sorted((n for n in ast.walk(ast.parse(src)) if isinstance(n, ast.Assert) and n.lineno > mark[0]),
                     key=lambda n: n.lineno)
    a = asserts[0]
    seg = ast.get_source_segment(src, a.test)
    off = sum(len(l) for l in lines[:a.test.lineno - 1]) + len(lines[a.test.lineno - 1].encode('utf-8')[:a.test.col_offset].decode('utf-8'))
    assert src[off:off + len(seg)] == seg
    p.write_text(src[:off] + 'not (' + seg + ')' + src[off + len(seg):], encoding='utf-8')
    print('N  %s line %d negated: %s' % (f, a.lineno, pytest(f'{f}::{t}')))
    git(WT, 'checkout', '-q', '--', f)

# K
TEST = ('frontier/B1891_the_foundation_at_version_1_66/verification/test_b1891_the_foundation_at_version_1_66.py'
        '::test_the_four_sentences_stand_corrected_and_the_old_forms_only_where_they_are_quoted')
G = WT / 'GENESIS.md'
base = G.read_text(encoding='utf-8')
NEWFORM = 'it is the only one that does'
k = base.find(NEWFORM)
cases = [('base', base),
         ('K0', base + "\nEleven entries of the record came as suppositions on a seat's word.\n"),
         ('K1', base + '\nThe tick is the only history of at most five letters that does.\n'),
         ('K2', base[:k + len(NEWFORM)] + '; the tick is the only history of at most five letters that does'
          + base[k + len(NEWFORM):])]
print('K  the corrected sentence found in GENESIS.md: %s (occurrences: %d)' % (k >= 0, base.count(NEWFORM)))
for key, text in cases:
    G.write_text(text, encoding='utf-8')
    print('K  %-4s %s' % (key, pytest(TEST)))
git(WT, 'checkout', '-q', '--', 'GENESIS.md')

# Q
Q = [
    ('docs/handoffs/MAIN_TO_BUILDER_2026-11-12/review80/ANSWERS_the_first_43.md',
     'Each row was reproduced by main before a word was changed'),
    ('docs/handoffs/MAIN_TO_BUILDER_2026-11-12/review80/ANSWERS_the_first_43.md', "| main's reproduction |"),
    ('docs/handoffs/MAIN_TO_BUILDER_2026-11-12/review80/ANSWERS_the_first_43.md', '(DRAFT: two of four files are in)'),
    ('docs/RETRACTED_PHRASES.md', 'Main reproduced it: a planted row on a new page is reported'),
    ('frontier/B1892_review_79_read_by_those_who_did_not_build_it/ANSWERS.md',
     'the protocol\'s § 12 keeps "reproduced" for the same code run again on a clean checkout'),
    ('docs/handoffs/MAIN_TO_BUILDER_2026-11-12/review80/STATUS_OF_THE_57.md',
     '"reproduced" is § 12\'s word for the same code run again'),
]
for f, q in Q:
    print('Q  %-5s %s :: %s' % (q in git(MAIN, 'show', f'{NEW}:{f}'), f, q))
subj = git(MAIN, 'log', '-1', '--format=%s', NEW)
print('Q  %-5s the subject of %s :: %s' % ("Review 80's four files are in" in subj, NEW, "Review 80's four files are in"))
n = sum(1 for l in git(MAIN, 'diff', '-U0', OLD, NEW).splitlines()
        if l.startswith('+') and not l.startswith('+++') and 'reproduced by main' in l)
print('Q  added lines in %s..%s that hold "reproduced by main": %d' % (OLD, NEW, n))

# G
gl = [l for l in git(MAIN, 'show', f'{NEW}:GENESIS.md').splitlines() if re.search(r'\bv?1\.67\b', l)]
print('G  lines of GENESIS.md naming 1.67: %d' % len(gl))
