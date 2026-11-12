"""
REVIEW 80, the web seat, second addition (M12): every quotation and line number the addition relies on, checked in
its file at main 10fbbc1c2.  Computed once; extended after the referee's read, and run again.

Usage: r80_m12_quotes.py <checkout of main with 10fbbc1c2 fetched>
"""
import subprocess, sys
MAIN, NEW = sys.argv[1], '10fbbc1c2'
A = 'docs/handoffs/MAIN_TO_BUILDER_2026-11-12/review80/ANSWERS_the_first_43.md'
S = 'docs/handoffs/MAIN_TO_BUILDER_2026-11-12/review80/STATUS_OF_THE_57.md'
B = 'tests/test_b448.py'
Q = [(B, 52, 'assert sp.Integer(d).is_negative or abs(int(d)) % 5 != 0'),
     (B, 49, 'if sp.degree(f, t) == 2:'), (B, 55, 'if sp.degree(f, t) == 2:'), (B, 54, 'for f in f5:'),
     (B, 56, 'assert sp.discriminant(f, t) != 5'),
     (A, 12, 'With the constant taken out, five statements hold'), (A, 12, 'the nine registered as a debt'),
     (A, 3, 'Each row was reproduced by main before a word was changed'), (A, 10, "| main's reproduction |"),
     (A, 3, '(DRAFT: two of four files are in)'), (A, 18, "the foundation's seven are its version 1.67"),
     ('docs/RETRACTED_PHRASES.md', None, 'Main reproduced it: a planted row on a new page is reported'),
     ('frontier/B1892_review_79_read_by_those_who_did_not_build_it/ANSWERS.md', None,
      'the protocol\'s § 12 keeps "reproduced" for the same code run again on a clean checkout'),
     (S, None, '"reproduced" is § 12\'s word for the same code run again'), (S, None, 'Owed from the first 43'),
     (S, None, "Eighteen rows in the enforcement package's own files"),
     (S, None, 'checks/genesis_v1_67.py'), (S, 9, 'It is not the label'),
     (S, 21, "a line in the next log entry on main's own use of the word on 2026-11-12"),
     ('docs/RETRACTED_PHRASES.md', None, 'Its table holds the FILE for that phrase, every line of it'),
     ('frontier/B1896_the_third_enforcement_series_verified_and_landed/FINDINGS.md', 44,
      'the file is held for that phrase, every line of it, and not the line'),
     (S, 101, 'writes them; the')]
ok = 0
for f, n, q in Q:
    lines = subprocess.run(['git', '-C', MAIN, 'show', f'{NEW}:{f}'], capture_output=True, text=True).stdout.splitlines()
    hit = (q in lines[n - 1]) if n else any(q in l for l in lines)
    ok += hit
    print('%-5s %s%s :: %s' % (hit, f, (':%d' % n) if n else '', q))
subj = subprocess.run(['git', '-C', MAIN, 'log', '-1', '--format=%s', NEW], capture_output=True, text=True).stdout
h = "Review 80's four files are in" in subj
print('%-5s the subject of %s :: %s' % (h, NEW, "Review 80's four files are in"))
print('found: %d of %d' % (ok + h, len(Q) + 1))
w = subprocess.run(['git', '-C', MAIN, 'log', '-S', 'Main reproduced it', '--format=%h', '5c7abd72a..' + NEW, '--',
                    'docs/RETRACTED_PHRASES.md'], capture_output=True, text=True).stdout.split()
print('the commit that wrote "Main reproduced it":', w)
import re
reg = subprocess.run(['git', '-C', MAIN, 'show', f'{NEW}:docs/POINT_REGISTER.md'], capture_output=True, text=True).stdout
print('register lines naming `or True`, or_true, B1036 or B1103:',
      sum(bool(re.search(r'or True|or_true|B1036|B1103', l)) for l in reg.splitlines()))
