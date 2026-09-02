#!/usr/bin/env python3
"""Fill/refresh the auto sections of synthesis/W-D_SYNTHESIS.md from coverage.md and SUMMARY.md (re-runnable)."""
import re
S = 'synthesis/'
cov = open(S + 'coverage.md').read(); summ = open(S + 'SUMMARY.md').read()
kinds = summ[summ.index('## red-flag kinds'):summ.index('## arcs with the most red flags')].strip()
top = summ[summ.index('## arcs with the most red flags'):summ.index('## load-bearing kinds')].strip()
first = summ.splitlines()[2] if len(summ.splitlines()) > 2 else ''
covblock = '\n'.join(l for l in cov.splitlines() if l.startswith('- '))
p = S + 'W-D_SYNTHESIS.md'; s = open(p).read()
s = re.sub(r'<!--COV-->.*?<!--/COV-->', '', s, flags=re.S)
s = s.replace('COVERAGE_PLACEHOLDER', '<!--COV-->\n' + covblock + '\n<!--/COV-->') if 'COVERAGE_PLACEHOLDER' in s else s.replace('Final coverage: see `coverage.md` (', 'Final coverage: see `coverage.md` (<!--COV-->\n' + covblock + '\n<!--/COV-->', 1) if '<!--COV-->' not in s else s
s = re.sub(r'<!--KINDS-->.*?<!--/KINDS-->', '', s, flags=re.S)
kblock = '<!--KINDS-->\n' + first + '\n\n' + kinds.replace('## red-flag kinds', '**Red-flag kinds:**') + '\n\n' + top.replace('## arcs with the most red flags', '**Arcs with the most flags (top 40):**') + '\n<!--/KINDS-->'
s = s.replace('KINDS_PLACEHOLDER', kblock) if 'KINDS_PLACEHOLDER' in s else s.replace('## 5. The reader red flags by kind (auto, `SUMMARY.md`)\n\n', '## 5. The reader red flags by kind (auto, `SUMMARY.md`)\n\n' + kblock + '\n\n', 1)
open(p, 'w').write(s); print('synthesis auto sections refreshed')
