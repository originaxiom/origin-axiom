"""B393 M1 session 2 -- THE GALOIS WHY: classify the X3 spectra under Gal(Q(zeta60)/H).

For each pair, the 3-side spectrum X3 has exactly 3 nonzero elements. For each element x
and each c in {19,31,49}: test sigma_c(x) = zeta60^k * x (proportionality by a root of
unity; exact). The eigen-pattern per pair is the candidate discriminator dark-vs-bright."""
import json, os, sys
from fractions import Fraction as Fr
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "B358_seam_certification"))
sys.path.insert(0, os.path.join(HERE, "..", "B367_value_map"))
sys.path.insert(0, os.path.join(HERE, "..", "B386_crt_closed_form"))
import cyclo_engine as E
import seam_certification as SC
from step0_exact_matrices import build_theta_W, matrix_order
from tensor_gate import local_partrace_table

def x3_spectrum(m1, m2):
    o1,_ = matrix_order(build_theta_W(m1))
    o2,_ = matrix_order(build_theta_W(m2))
    T3 = local_partrace_table(3, 2, m1, m2, o1, o2)
    z1, z2 = 60//o1, 60//o2
    out = {}
    for a in range(o1):
        for b in range(o2):
            t = E.ZERO
            for j in range(o1):
                za = E.zeta((-z1*j*a) % 60)
                for l in range(o2):
                    t = E.add(t, E.mul(E.mul(za, E.zeta((-z2*l*b) % 60)), T3[(j,l)]))
            if any(x != 0 for x in t):
                out[(a,b)] = E.scal(Fr(1, o1*o2), t)
    return out

def eig_pattern(x):
    pat = {}
    for c in (19, 31, 49):
        sx = SC.sigma(x, c)
        hit = None
        for k in range(60):
            if sx == E.mul(E.zeta(k), x): hit = k; break
        pat[c] = hit          # None = not an eigenvector of sigma_c
    return pat

PAIRS = [((1,3),"dark"),((1,4),"dark"),((3,5),"dark"),((3,4),"bright"),((2,3),"bright")]
res = {}
for (m1,m2), st in PAIRS:
    X3 = x3_spectrum(m1, m2)
    pats = []
    for (a,b), x in sorted(X3.items()):
        p = eig_pattern(x)
        pats.append(dict(cell=[a,b], sigma19=p[19], sigma31=p[31], sigma49=p[49]))
    res[f"{m1},{m2}"] = dict(status=st, n=len(X3), patterns=pats)
    print(f"({m1},{m2}) {st:7s}:", [(t['cell'], t['sigma19'], t['sigma31'], t['sigma49']) for t in pats])
json.dump(res, open(os.path.join(HERE, "galois_why.json"), "w"), indent=1)
print("DONE")
