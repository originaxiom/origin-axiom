"""
W-R79b: three constructed pages run through the tripwire of B1862's lock (its function _hits, imported from main's
checkout unchanged), in a scratch git repository.  Computed once.  Each page states an old form; none carries its
correction; the tripwire should report every one as not corrected.  What would show a fault: a page reported as
corrected because an unrelated word stands near the old form.
  P1  the old form of E3, with an unrelated "E = +I" followed by the common word "only" within 500 characters.
  P2  the old form of E3, with the word "parity" in an unrelated sentence before "E = +I".
  P3  the old form of E13 ("21 distinct eigenvalues"), with "at most 20" in an unrelated sentence nearby.
  K   control: the lock's own good fixture (a true correction) is reported as corrected.
Usage: tripwire_probe.py <the seat's checkout of main> <a scratch directory>
"""
import importlib.util
import pathlib
import subprocess
import sys

main, scratch = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
lock = next(main.glob('frontier/B1862_*/verification/test_b1862_the_audits_first_corrections.py'))
spec = importlib.util.spec_from_file_location('b1862_lock', lock)
L = importlib.util.module_from_spec(spec)
spec.loader.exec_module(L)
scratch.mkdir(parents=True, exist_ok=True)
(scratch / 'docs').mkdir(exist_ok=True)
(scratch / 'frontier').mkdir(exist_ok=True)


def git(*a):
    subprocess.run(['git', '-C', str(scratch), '-c', 'user.name=t', '-c', 'user.email=t@example.invalid', *a],
                   capture_output=True, text=True, check=True)


git('init', '-q')
pages = {
    'docs/p1.md': 'The charge is invisibility to every state). In another matter one has E = +I for the identity only.',
    'docs/p2.md': 'Parity is discussed elsewhere. The charge is invisibility to every state). One has E = +I for the identity.',
    'docs/p3.md': 'B567 finds 21 distinct eigenvalues at level 165. In another matter, a bound of at most 20 is used for the rank.',
    'docs/good.md': 'The charge is invisibility to every state) [corrected: that holds for E = +I only; E = −I is invisible only under parity].',
}
for rel, s in pages.items():
    (scratch / rel).write_text(s + '\n', encoding='utf-8')
git('add', '-A')
got = {rel: ok for rel, _, ok in L._hits(scratch)}
for rel in pages:
    print('%-14s reported as corrected: %s' % (rel, got.get(rel)))
