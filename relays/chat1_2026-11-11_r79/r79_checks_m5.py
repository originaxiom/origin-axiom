"""
REVIEW 79, M5's additions: every quotation of the review file's § 4, in its table and in its notes, checked as an exact
substring of its file at 0dda7b472 (git show).  Computed once.  Second version: the first checked only the table's
B-numbered rows and one heading.  Usage: r79_checks_m5.py <the seat's checkout of main> <the review file>
"""
import re
import subprocess
import sys

MAIN, REVIEW, REV = sys.argv[1], sys.argv[2], '0dda7b472'


def show(path, rev=REV):
    return subprocess.run(['git', '-C', MAIN, 'show', '%s:%s' % (rev, path)], capture_output=True, text=True).stdout


text = open(REVIEW, encoding='utf-8').read()
sec = text[text.index('## 4. '):]
total = bad = 0
for m in re.finditer(r'^\| ([^|]+?) \| `([^`]+)`[^|]*\| "(.+?)" \|', sec, re.M):
    arc, path, quote = m.groups()
    ok = quote in show(path)
    total += 1
    bad += (not ok)
    print('Q   table: %s %s: %s' % (arc, path, 'found' if ok else 'NOT FOUND'))
EXTRA = [
    ('frontier/B1726_the_two_ingredients_replicated/FINDINGS.md', '1.5 to 2'),
    ('ROADMAP.md', 'VIEW REFRESH — 2026-11-11 (Review 78)'),
    ('docs/seats/README.md', 'recomputed with separate code'),
    ('docs/seats/README.md', 'these words and no others'),
    ('docs/seats/README.md', 'recomputed independently'),
    ('docs/seats/README.md', 'REPRODUCED, DIFFERS, or CANNOT CHECK'),
    ('frontier/B892_second_measurement/FINDINGS.md', 'accepts this mend'),
    ('frontier/B1726_the_two_ingredients_replicated/FINDINGS.md', "decided by the advisor seat's sealed card"),
    ('frontier/B1753_the_six_on_the_five_ality_lines/FINDINGS.md', "decided by the advisor seat's sealed card"),
    ('frontier/B1882_the_v1_card_run_on_main/FINDINGS.md', 'in all three cells'),
]
for path, quote in EXTRA:
    ok = quote in show(path)
    total += 1
    bad += (not ok)
    print('Q   note: %s "%s": %s' % (path, quote, 'found' if ok else 'NOT FOUND'))
print('Q   quotations checked: %d; not found: %d' % (total, bad))
