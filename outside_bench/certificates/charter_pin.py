#!/usr/bin/env python3
"""THE GRAVITY CHARTER's drift guard: assert, from the lane's own banked
outputs, the four bench anchors the charter leans on (E2, E3, E6, E7 of
THE_GRAVITY_CHARTER.md).  A future re-run that silently changed any of
them must break here loudly.  No new mathematics; a pin, not a cell.
"""
import os
HERE=os.path.dirname(os.path.abspath(__file__))
OUT=os.path.join(HERE,'..','outputs')
def has(fn, needle):
    txt=open(os.path.join(OUT,fn)).read()
    assert needle in txt, f"CHARTER DRIFT: {fn} no longer contains: {needle!r}"
    return True

# E2 (memo 78): gravity load-bearing, cubic redundant in-frame
has('grav_ablation_out.txt', 'BRANCH LB: GRAVITY IS LOAD-BEARING')
has('grav_ablation_out.txt', "V2 NO-CUBIC: {'q-zero-line': 9, 'line-solutions': 36, 'only-zero': 36}")
print("E2 pinned: grav^2 Y load-bearing; cubic redundant (memo 78)")

# E3 (memo 81): spectrum exact; mirror preserves lengths, negates torsions
has('geodesic_tongue_out.txt', 'every class trace lies in Z[w]')
has('geodesic_tongue_out.txt', 'EVERY inner-ball class has a mirror partner')
has('geodesic_tongue_out.txt', 'tr = 2-1w   [AB]')
print("E3 pinned: exact spectrum, mirror-symmetric, systole 2-w (memo 81)")

# E6 (memo 77): surviving torus = SM torus exactly; vev pair the closing
has('psi_survival_out.txt', 'the surviving torus IS the SM torus EXACTLY')
has('psi_survival_out.txt', 'gcd(|1|,|-2|) = 1')
print("E6 pinned: SM torus exact; family charge dies gcd-1 (memo 77)")

# E7 (memo 79): orientation charged, chirality free
has('one_bit_out.txt', 'words with chi(w) != chi(w^-1): 0')
has('one_bit_out.txt', 'chi^gal(w) != chi(w): 396 of 484')
print("E7 pinned: chirality character-invisible, orientation visible (memo 79)")

print("\nCHARTER PIN GREEN: the four bench anchors of THE_GRAVITY_CHARTER.md")
print("stand as banked.  (cc's anchors E1/E4/E5/E8 are cited to main commits")
print("e3149e10/3e0028c9/294cb57e and are theirs to guard.)")
