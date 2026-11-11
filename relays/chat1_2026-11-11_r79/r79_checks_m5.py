"""
REVIEW 79, M5's additions: every quotation of the review file's § 4 table, checked as an exact substring of its file at
0dda7b472 (git show).  Computed once.  Usage: r79_checks_m5.py <the seat's checkout of main> <the review file>
"""
import re
import subprocess
import sys

MAIN, REVIEW, REV = sys.argv[1], sys.argv[2], '0dda7b472'
text = open(REVIEW, encoding='utf-8').read()
sec = text[text.index('## 4. '):]
total = bad = 0
for m in re.finditer(r'^\| (B\d{4}) \| `([^`]+)`[^|]*\| "(.+?)" \|', sec, re.M):
    arc, path, quote = m.groups()
    src = subprocess.run(['git', '-C', MAIN, 'show', '%s:%s' % (REV, path)], capture_output=True, text=True).stdout
    ok = quote in src
    total += 1
    bad += (not ok)
    print('Q   %s %s: %s' % (arc, path, 'found' if ok else 'NOT FOUND'))
roadmap = subprocess.run(['git', '-C', MAIN, 'show', REV + ':ROADMAP.md'], capture_output=True, text=True).stdout
print('Q   the heading "VIEW REFRESH — 2026-11-11 (Review 78)" in ROADMAP.md: %s'
      % ('found' if 'VIEW REFRESH — 2026-11-11 (Review 78)' in roadmap else 'NOT FOUND'))
print('Q   quotations checked: %d; not found: %d' % (total, bad))
