# s07_char0_orbit_invariants.py -- cusp/genus/congruence invariants of the characteristic-0 finite orbits
from fractions import Fraction as Fr
from common import QD, orbit, perms
from orbinv import invariants, gap_info
import cmath, math

r2 = QD(0, 1, 2); phi = QD(Fr(1, 2), Fr(1, 2), 5); phii = QD(Fr(-1, 2), Fr(1, 2), 5)
starts = {
    "two-zero (3,0,0) k=9": (3, 0, 0),
    "16 @ k=2  (1,1,1)": (1, 1, 1),
    "36 @ k=3  (sqrt2,1,0)": (r2, QD(1, 0, 2), QD(0, 0, 2)),
    "72 @ k=3  (phi,1/phi,0)": (phi, phii, QD(0, 0, 5)),
    "40 @ k=(5-sqrt5)/2 (1,1/phi,0)": (QD(1, 0, 5), phii, QD(0, 0, 5)),
}
for name, p0 in starts.items():
    pts, idx = orbit(p0)
    pL, pR = perms(pts, idx)
    print(name, invariants(pL, pR), gap_info(pL, pR), flush=True)

# Cayley leaf k=4: torsion points of order d, exact model on exponents (a,b) mod d up to sign;
# L:(a,b)->(a,a+b), R:(a,b)->(a+b,b)  [derived in report from x=lam+1/lam, y=mu+1/mu, z=lam*mu+1/(lam*mu)]
for d in range(2, 13):
    vs = set()
    for a in range(d):
        for b in range(d):
            if math.gcd(math.gcd(a, b), d) == 1:
                vs.add(min((a, b), ((-a) % d, (-b) % d)))
    vs = sorted(vs); vi = {v: i for i, v in enumerate(vs)}
    norm = lambda v: min(v, ((-v[0]) % d, (-v[1]) % d))
    pL = [vi[norm((a, (a+b) % d))] for (a, b) in vs]
    pR = [vi[norm(((a+b) % d, b))] for (a, b) in vs]
    print("Cayley torsion order d=%d" % d, invariants(pL, pR), gap_info(pL, pR), flush=True)
