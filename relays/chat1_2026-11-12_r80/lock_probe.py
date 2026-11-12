"""
REVIEW 80, the web seat: B1891's lock (at c40446392) on a constructed change to GENESIS.md, in a scratch clone of main.
Computed once; nothing here was sealed in advance.  Main's files are never changed: each case appends one sentence to the
clone's GENESIS.md, runs the lock's test of the four corrected sentences there with pytest, and resets the clone.

The lock's header says it fails on "one of the four corrected sentences standing in its old form outside the bracket that
quotes it".  B1891's table gives the four old forms.
  K0  the first old form, "Eleven entries of the record came as suppositions", appended as a sentence   (a control: fails)
  K1  the fourth old form, the tick "is the only history of at most five letters that does", appended as a sentence

Usage: lock_probe.py <the seat's checkout of main, at c40446392> <scratch directory>
"""
import pathlib
import shutil
import subprocess
import sys

MAIN, SCRATCH = pathlib.Path(sys.argv[1]).resolve(), pathlib.Path(sys.argv[2]).resolve() / 'lock_clone'
TEST = ('frontier/B1891_the_foundation_at_version_1_66/verification/test_b1891_the_foundation_at_version_1_66.py'
        '::test_the_four_sentences_stand_corrected_and_the_old_forms_only_where_they_are_quoted')
CASES = [('K0', '\nEleven entries of the record came as suppositions on a seat\'s word.\n'),
         ('K1', '\nThe tick is the only history of at most five letters that does.\n')]


def git(*a):
    return subprocess.run(['git', '-C', str(SCRATCH), *a], capture_output=True, text=True, check=True).stdout


if SCRATCH.exists():
    shutil.rmtree(SCRATCH)
subprocess.run(['git', 'clone', '-q', '--shared', '--no-checkout', str(MAIN), str(SCRATCH)], check=True)
git('checkout', '-q', '--detach', 'c40446392')
print('scratch clone at', git('rev-parse', '--short', 'HEAD').strip())
for key, text in [('base', '')] + CASES:
    git('reset', '-q', '--hard', 'c40446392')
    if text:
        with open(SCRATCH / 'GENESIS.md', 'a', encoding='utf-8') as fh:
            fh.write(text)
    r = subprocess.run([sys.executable, '-m', 'pytest', '-q', '-p', 'no:cacheprovider', TEST], cwd=SCRATCH,
                       capture_output=True, text=True)
    last = [l for l in r.stdout.splitlines() if l.strip()][-1:]
    print('%-4s the lock: %s' % (key, last[0] if last else '(no output)'))
git('reset', '-q', '--hard', 'c40446392')
