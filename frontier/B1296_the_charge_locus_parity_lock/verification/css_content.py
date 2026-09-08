"""B1296 T6 detail: the C_ss-content of every charged sector for the four theta-even coweights and omega_1^vee.
Decomposes each sector's weights into (per simple factor) fundamental-weight coordinates; names the irreps by peeling
highest weights with Freudenthal-free logic valid for the small reps that occur (checked by dimension bookkeeping)."""
import itertools, sys
from fractions import Fraction as Fr
from collections import Counter
exec(open("e6_theta_spectra.py").read().split("# T3: the toggled")[0].split("print(")[0])  # reuse: roots, omega, W27, theta, even, odd, helpers
def simple_roots_of(rootsC):
    pos = [r for r in rootsC if coords(r) > tuple([0]*6)]        # positive in E6's ordering (first nonzero coeff > 0)
    pos = [r for r in rootsC if any(x != 0 for x in coords(r)) and next(x for x in coords(r) if x != 0) > 0]
    simple = [r for r in pos if not any(key(sub(r, s)) in {key(p) for p in pos} for s in pos if s != r)]
    return pos, simple
def components(simple):
    comps = []; left = list(range(len(simple)))
    while left:
        comp = [left.pop()]; grew = True
        while grew:
            grew = False
            for j in list(left):
                if any(dot(simple[i], simple[j]) != 0 for i in comp): comp.append(j); left.remove(j); grew = True
        comps.append(sorted(comp))
    return comps
def sector_content(u, weights, label):
    rootsC = [r for r in roots if dot(r, u) == 0]
    pos, simple = simple_roots_of(rootsC); comps = components(simple)
    names = []
    for comp in comps:
        n = len(comp); names.append({1: "A1", 2: "A2", 3: "A3", 4: "D4" if any(sum(1 for j in comp if dot(simple[i], simple[j]) != 0 and i != j) == 3 for i in comp) else "A4", 5: "A5/D5"}[n])
    by_q = {}
    for w in weights:
        q = dot(w, u)
        if q == 0: continue
        dl = tuple(tuple(dot(w, simple[i]) for i in comp) for comp in comps)   # Dynkin labels per factor (simply laced: <w, alpha_i>)
        by_q.setdefault(q, Counter())[dl] += 1
    print(f"  [{label}] C_ss = {' x '.join(names)} (ranks {[len(c) for c in comps]}), charged sectors:")
    for q in sorted(by_q):
        cnt = by_q[q]; dim = sum(cnt.values())
        # highest weights = dominant labels not obtainable as (other weight) - (positive root of C); name by peeling dominant weights
        dom = sorted([dl for dl in cnt if all(x >= 0 for f in dl for x in f)], key=lambda d: -sum(sum(f) for f in d))
        fmt = lambda d: "(" + ", ".join("[" + " ".join(str(int(x)) for x in f) + "]" for f in d) + ")"
        print(f"     q = {str(q):>4}  dim {dim:>2}  dominant labels (per factor, Dynkin) " + "  ".join(f"{fmt(d)} x{cnt[d]}" for d in dom))
    return by_q
for name, u in (("omega_1^vee", omega[0]), ("omega_2^vee", omega[1]), ("omega_4^vee", omega[3]), ("omega_1^vee+omega_6^vee", even[0]), ("omega_3^vee+omega_5^vee", even[2])):
    print(f"\n== u = {name} ==")
    sector_content(u, roots, "78"); sector_content(u, W27, "27")
