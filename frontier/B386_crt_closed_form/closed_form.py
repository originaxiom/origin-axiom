"""B386 L2b -- THE CLOSED FORM: partial(K) as a two-branch product of local constants.

Window characters split exactly: zeta20 = zeta4*zeta5^{-1}, zeta12 = zeta4^{-1}*zeta3.
For each of the 4 slot window terms (a1,a2) in {6,14}x{2,10} with sign s = (+1,-1,-1,+1):
  3-side cell:  f(j4,l4) = zeta4^{-a1 j} * zeta4^{+a2 l} * C3(j,l) * ind3(j,l)   [period 4,4]
  5-side j-branch: G(p)  = sum_{j5} zeta5^{+a1 j} * [C5*ind5 j-part]  at j%2 = p
  5-side l-branch: H(q)  = sum_{l3} zeta3^{-a2 l} * [C5*ind5 l-part]  at l%2 = q
Assembly (exact identity to verify):
  partial(K) = (1/240) * sum_terms s * sum_{j4 in Z4, l4 in Z4}
                  f_K(j4,l4) * GH_K(j4%2, l4%2)
where GH_K(p,q) = sum over the 5-side lattice (j5,l3) of the 5-side factor at parities (p,q)
-- computed as one object since C5 couples (j,l) jointly (period 10x6).
All sums exact; every constant printed in H-components for recognition."""
import json, os, sys
from fractions import Fraction as Fr
from math import gcd
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "B358_seam_certification"))
sys.path.insert(0, os.path.join(HERE, "..", "B367_value_map"))
import cyclo_engine as E
import seam_certification as SC
from tensor_gate import local_partrace_table

o1, o2 = 20, 12
T3 = local_partrace_table(3, 2, 1, 2, o1, o2)
T5 = local_partrace_table(5, 2, 1, 2, o1, o2)
def A(m, n): return [[(1+m*m) % n, m % n], [m % n, 1 % n]]
def mm(a, b, n): return [[(a[0][0]*b[0][0]+a[0][1]*b[1][0]) % n, (a[0][0]*b[0][1]+a[0][1]*b[1][1]) % n],
                         [(a[1][0]*b[0][0]+a[1][1]*b[1][0]) % n, (a[1][0]*b[0][1]+a[1][1]*b[1][1]) % n]]
def ind_table(n):
    g1, g2 = A(1, n), A(2, n)
    G1 = [[[1 % n, 0], [0, 1 % n]]]
    for _ in range(o1-1): G1.append(mm(G1[-1], g1, n))
    G2 = [[[1 % n, 0], [0, 1 % n]]]
    for _ in range(o2-1): G2.append(mm(G2[-1], g2, n))
    return {(j, l): (gcd((( -mm(G1[j],G2[l],n)[0][0]-1)*(-mm(G1[j],G2[l],n)[1][1]-1)
                          - mm(G1[j],G2[l],n)[0][1]*mm(G1[j],G2[l],n)[1][0]) % n, n) == 1)
            for j in range(o1) for l in range(o2)}
I3, I5 = ind_table(3), ind_table(5)
def hs(t):
    s = SC.solve_H(SC.H_avg(t))
    return [str(x) for x in s] if s else None

TERMS = [(6, 2, 1), (6, 10, -1), (14, 2, -1), (14, 10, 1)]
def K_split(K): return {1: (True, True), 5: (True, False)}[K]

results = {}
for K in (1, 5):
    need3, need5 = K_split(K)
    total = E.ZERO
    factors = {}
    for (a1, a2, s) in TERMS:
        # GH_K(p,q): the 5-side lattice sum at parities (p,q). Representatives: j runs over
        # a full period-10 transversal with j%2 = p -- as j4 varies, j%2 = j4%2; we need the
        # 5-side sum with j5 free and the j%2-branch fixed: pick j in {p, p+2, ..., p+8}
        # (5 values, all j5 residues, fixed parity) -- likewise l in {q, q+2, q+4} mod 6.
        GH = {}
        for p in (0, 1):
            for q in (0, 1):
                t = E.ZERO
                for j in range(p, p+10, 2):
                    for l in range(q, q+6, 2):
                        if I5[(j % o1, l % o2)] != need5: continue
                        w5 = E.mul(E.zeta((12*a1*j) % 60), E.zeta((-20*a2*l) % 60))
                        t = E.add(t, E.mul(w5, T5[(j % o1, l % o2)]))
                GH[(p, q)] = t
        # 3-side: f(j4,l4) over Z4 x Z4 with ind3, zeta4 characters
        term = E.ZERO
        for j4 in range(4):
            for l4 in range(4):
                if I3[(j4, l4)] != need3: continue
                w4 = E.mul(E.zeta((-15*a1*j4) % 60), E.zeta((15*a2*l4) % 60))
                f = E.mul(w4, T3[(j4, l4)])
                term = E.add(term, E.mul(f, GH[(j4 % 2, l4 % 2)]))
        factors[f"term({a1},{a2})"] = dict(GH={f"{p}{q}": hs(GH[(p, q)]) for p in (0, 1) for q in (0, 1)})
        total = E.add(total, E.scal(Fr(s), term))
    total = E.scal(Fr(1, 240), total)
    got = hs(total)
    tgt = ["0", "0", "-1/16", "-1/16"] if K == 1 else ["0", "0", "-1/48", "-1/48"]
    print(f"class-{K} closed-form assembly: {got}  target {tgt}  MATCH: {got == tgt}")
    results[f"class{K}"] = dict(assembled=got, target=tgt, match=(got == tgt), factors=factors)

json.dump(results, open(os.path.join(HERE, "closed_form.json"), "w"), indent=1)
# print the recognizable constants for the FINDINGS
for K in (1, 5):
    print(f"-- class-{K} branch constants (term (6,2)):")
    for pq, v in results[f"class{K}"]["factors"]["term(6,2)"]["GH"].items():
        print(f"   GH[{pq}] =", v)
print("DONE")
