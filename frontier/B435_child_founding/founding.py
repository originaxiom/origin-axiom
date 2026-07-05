"""B435 -- THE CHILD PROGRAM founding bud (C0). The child = the Meyerhoff manifold = 4_1(5,1)
(B434: the FORCED minimal filling of the parent). First invariants, exact:

1. H1(child) = Z/5 -- (p,q)=(5,1) surgery on a knot gives H1 = Z/p. THE GOLDEN PRIME RETURNS:
   the child's trace field exits Q(sqrt-15) (disc -283, B434) but its torsion homology
   remembers the parent's 5.
2. The abelian E6 vacuum count (the Z/5 floor of T[child, E6]):
   Hom(Z/5, E6)/conj = Kac coordinates (a0..a6) >= 0, gcd 1, sum(ai*mi) = 5 with affine-E6
   marks (1,1,2,2,3,2,1), MODULO Omega = Z(E6) = Z/3 (the cyclic leg-rotation of the affine
   diagram) -- Kac's theorem for the simply-connected group.
   DERIVED: 75 raw solutions; a rotation-fixed solution would need 3 | 5 (sum = 3*(...)) --
   impossible -- so all orbits are free: 75/3 = **25 = 5^2 abelian vacua.**
   (Up to the outer flip as well -- S3 on legs -- the count is 17; recorded as the refinement.)

Weil rigidity note: the child is closed hyperbolic => H^1(child, ad) = 0 -- NO moduli. The
child's content is its flat-connection SPECTRUM with torsion weights (waves C2-C5).

Firewall: homology + Kac combinatorics; "vacua" is the 3d-3d label for flat connections --
mathematics. Nothing here licenses a physics claim.
"""
import os, json
from math import gcd
from itertools import product, permutations

MARKS = [1, 1, 2, 2, 3, 2, 1]          # affine E6: tips at 0,1,6 (mark 1), mids 2,3,5, center 4
LEGS = [(0, 2), (1, 3), (6, 5)]         # (tip, mid) pairs

def kac_solutions(N=5):
    out = []
    for a in product(range(N + 1), repeat=7):
        if sum(x*m for x, m in zip(a, MARKS)) == N and gcd(*a) == 1:
            out.append(a)
    return out

def rotate(a):
    """the Omega = Z/3 cyclic rotation of the three legs (center fixed)."""
    b = [0]*7; b[4] = a[4]
    for i in range(3):
        t, m = LEGS[i]; t2, m2 = LEGS[(i + 1) % 3]
        b[t2], b[m2] = a[t], a[m]
    return tuple(b)

def orbits_mod_rotation(sols):
    seen = set(); orbits = 0; fixed = 0
    for a in sols:
        if a in seen: continue
        orb = {a, rotate(a), rotate(rotate(a))}
        if len(orb) == 1: fixed += 1
        seen |= orb; orbits += 1
    return orbits, fixed

def orbits_mod_S3(sols):
    def canon(a):
        best = None
        for perm in permutations(range(3)):
            b = [0]*7; b[4] = a[4]
            for i in range(3):
                t, m = LEGS[i]; t2, m2 = LEGS[perm[i]]
                b[t2], b[m2] = a[t], a[m]
            tb = tuple(b)
            if best is None or tb < best: best = tb
        return best
    return len({canon(a) for a in sols})

if __name__ == "__main__":
    sols = kac_solutions(5)
    n_orb, n_fix = orbits_mod_rotation(sols)
    n_s3 = orbits_mod_S3(sols)
    print("H1(child) = Z/5  (5,1)-surgery => Z/p; the golden prime returns in torsion")
    print(f"Kac solutions (order|5 in E6): {len(sols)}")
    print(f"rotation-fixed solutions: {n_fix}  (must be 0: fixed => 3 | 5, impossible)")
    print(f"ABELIAN E6 VACUA of the child: {n_orb} = 5^2 nontrivial (26 incl. trivial vacuum)   (Hom(Z/5,E6)/conj)")
    print(f"refinement mod outer flip (S3): {n_s3}")
    json.dump(dict(H1="Z/5", kac_solutions=len(sols), rotation_fixed=n_fix,
                   abelian_vacua=n_orb, mod_S3=n_s3),
              open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "founding.json"), "w"),
              indent=1)
    print("[written] founding.json")
