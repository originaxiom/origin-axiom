# s14_ranks.py -- rank (number of orbits on ordered pairs) of the permutation action on the finite char-0 orbits and
# on the Cayley torsion orbit of order 12 / 14; compared with the splittings seen in s13 (orbit sizes / |O|).
from fractions import Fraction as Fr
import math
from common import QD, orbit, perms
from sage.all import libgap
def rank_and_suborbits(pL, pR):
    n = len(pL)
    G = libgap.Group([libgap.PermList([i+1 for i in pL]), libgap.PermList([i+1 for i in pR])])
    S = libgap.Stabilizer(G, 1)
    sub = sorted([int(libgap.Size(o)) for o in libgap.Orbits(S, libgap.eval("[1..%d]" % n))], reverse=True)
    return len(sub), sub
r2 = QD(0, 1, 2); phi = QD(Fr(1, 2), Fr(1, 2), 5); phii = QD(Fr(-1, 2), Fr(1, 2), 5)
starts = {"two-zero 6": (3, 0, 0), "16@k=2": (1, 1, 1), "36@k=3": (r2, QD(1, 0, 2), QD(0, 0, 2)),
          "72@k=3": (phi, phii, QD(0, 0, 5)), "40@k=(5-r5)/2": (QD(1, 0, 5), phii, QD(0, 0, 5))}
for name, p0 in starts.items():
    pts, idx = orbit(p0); pL, pR = perms(pts, idx)
    print(name, "rank, suborbit lengths:", rank_and_suborbits(pL, pR), flush=True)
for d in (12, 14):
    vs = sorted(set(min((a, b), ((-a) % d, (-b) % d)) for a in range(d) for b in range(d) if math.gcd(math.gcd(a, b), d) == 1))
    vi = {v: i for i, v in enumerate(vs)}; norm = lambda v: min(v, ((-v[0]) % d, (-v[1]) % d))
    pL = [vi[norm((a, (a+b) % d))] for (a, b) in vs]; pR = [vi[norm(((a+b) % d, b))] for (a, b) in vs]
    print("Cayley torsion d=%d (size %d)" % (d, len(vs)), "rank, suborbit lengths:", rank_and_suborbits(pL, pR), flush=True)
