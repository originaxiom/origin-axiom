"""
REVIEW 80, M11's addendum, the web seat: the quotations of the dated addition, each an exact substring of its file at
0dda7b472 (the end of Review 79's window).  Computed once.

Usage: r80_m11_checks.py <the seat's checkout of main>
"""
import subprocess
import sys

MAIN, REV = sys.argv[1], '0dda7b472'
QUOTES = [
    ('frontier/B731_object_observer_noncongruence/FINDINGS.md', '(160 in 1920), and 6 at (2)'),
    ('frontier/B731_object_observer_noncongruence/FINDINGS.md', '(order 960 at (4))'),
    ('frontier/B731_object_observer_noncongruence/arc_verdict.json', 'the congruence level is (4)'),
    ('frontier/B732_conjugation_is_out_A5/FINDINGS.md', "m004's OWN level-(8) observer"),
    ('frontier/B733_observer_space/FINDINGS.md', 'the congruence level is (4)'),
    ('frontier/B942_l113_bc_falsifier/FINDINGS.md', "the image order it quotes is the image's at (8) and is not changed"),
    ('frontier/B942_l113_bc_falsifier/arc_verdict.json', "is the image's order in the quotient at ("),
    ('frontier/B942_l113_bc_falsifier/arc_verdict.json', 'by every central unit of square one'),
    ('frontier/B1030_price_lock_verification/FINDINGS.md', 'retroactive designer freedom stays 0.000'),
    ('frontier/B1030_price_lock_verification/FINDINGS.md', 'su(3) ⊕ su(2) ⊕ u(1)³, two abelian factors more than the Standard Model'),
    ('frontier/B1067_rayclass_harvest/FINDINGS.md', 'Baker and Reid 2018 state that the figure-eight complement is a congruence manifold'),
]
bad = 0
for path, q in QUOTES:
    ok = q in subprocess.run(['git', '-C', MAIN, 'show', '%s:%s' % (REV, path)], capture_output=True, text=True).stdout
    bad += not ok
    print('Q   %s: %s' % (path, 'found' if ok else 'NOT FOUND'))
print('Q   quotations checked: %d; not found: %d' % (len(QUOTES), bad))
