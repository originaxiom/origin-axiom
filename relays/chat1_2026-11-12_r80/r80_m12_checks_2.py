"""
REVIEW 80, the web seat, second addition (M12), a further check after r80_m12_checks.py: its case N found that
tests/test_b448.py, line 52 at 10fbbc1c2, passes with its test negated.  Here the mended assert itself is replaced by
`assert False` in the scratch worktree; if the test still passes, the line is never reached.  Computed once; main's
files are never changed; the worktree is reset after the case.

Usage: r80_m12_checks_2.py <scratch worktree of main at 10fbbc1c2>
"""
import pathlib, subprocess, sys
WT = pathlib.Path(sys.argv[1]).resolve()
F, T = 'tests/test_b448.py', 'test_orbit_tower_fields'
p = WT / F
src = p.read_text(encoding='utf-8')
lines = src.splitlines(keepends=True)
i = [k for k, l in enumerate(lines) if "the web seat's finding 1" in l and 'CORRECTED' in l][0]
nxt = lines[i + 1]
print('the line after the mark, number %d, begins with "assert": %s' % (i + 2, nxt.lstrip().startswith('assert ')))
lines[i + 1] = nxt[:len(nxt) - len(nxt.lstrip())] + 'assert False\n'
p.write_text(''.join(lines), encoding='utf-8')
r = subprocess.run([sys.executable, '-m', 'pytest', '-q', '--tb=no', '-p', 'no:cacheprovider', f'{F}::{T}'], cwd=WT,
                   capture_output=True, text=True)
print('with `assert False` in its place:', [l for l in r.stdout.splitlines() if l.strip()][-1])
subprocess.run(['git', '-C', str(WT), 'checkout', '-q', '--', F], check=True)
