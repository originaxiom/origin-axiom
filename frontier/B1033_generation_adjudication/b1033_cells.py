"""B1033 -- THE GENERATION ADJUDICATION (sealed 73eedc0b BEFORE these computations).

V1: the exact per-level content table -> FLAVOR vs CHIRAL.
V2: B299's triality transported to the banked frame -> the orbit-channel identity.
V3: the classification against the walls (B298/B280/B299).
All exact; the informing exercises are re-run here for the record (the seal discloses them)."""
import json
from collections import Counter
from itertools import permutations
import sympy as sp

R = json.load(open('frontier/B883_the_27/rep27.json'))
REP = {int(k): v for k, v in R['rep'].items()}
WTS = [tuple(w) for w in R['weights']]
A7 = [tuple(r) for r in R['plus_roots']]
lev = [r[3] for r in A7]                       # trinification u(1) level (branch node 3)
so10 = [{0: "10", 1: "16", 2: "1"}[r[0]] for r in A7]

# our Cartan (solved in the disclosed exercise; re-asserted here)
C_OURS = sp.Matrix([[2,0,-1,0,0,0],[0,2,0,-1,0,0],[-1,0,2,-1,0,0],
                    [0,-1,-1,2,-1,0],[0,0,0,-1,2,-1],[0,0,0,0,-1,2]])

# ---------------------------------------------------------------- the cubic (re-run)
triples = [(a,b,c) for a in range(27) for b in range(a,27) for c in range(b,27)
           if all(WTS[a][k]+WTS[b][k]+WTS[c][k]==0 for k in range(6))]
tidx = {t:i for i,t in enumerate(triples)}
rows = []
for gidx in range(6,78):
    Mg = REP[gidx]; eqs = {}
    for (a,b,c) in triples:
        coef = tidx[(a,b,c)]
        for (x,y,z) in ((a,b,c),(b,a,c),(c,a,b)):
            for k in range(27):
                if Mg[k][x]:
                    key = tuple(sorted((k,y,z)))
                    eqs.setdefault(key,{}); eqs[key][coef]=eqs[key].get(coef,0)+Mg[k][x]
    for key,terms in eqs.items():
        row=[0]*len(triples)
        for coef,val in terms.items(): row[coef]=val
        if any(row): rows.append(row)
ns = sp.Matrix(rows).nullspace(); assert len(ns) == 1
cub = [sp.Rational(x) for x in ns[0]]
den = sp.lcm([c.q for c in cub]); cub = [c*den for c in cub]
g0 = sp.gcd([c.p for c in cub if c != 0]); cub = [int(c/g0) for c in cub]
SUP = {t: c for t, c in zip(triples, cub) if c}
CH024 = {frozenset(t) for t in SUP
         if tuple(sorted((lev[t[0]], lev[t[1]], lev[t[2]]))) == (0, 2, 4)}
assert len(CH024) == 9


def v1_content_table():
    """The exact table + the FLAVOR/CHIRAL criterion + the singlet anomaly resolved."""
    a02 = lambda i: (WTS[i][0], WTS[i][2])
    a45 = lambda i: (WTS[i][4], WTS[i][5])
    a1 = lambda i: WTS[i][1]
    blocks = {"A(lv2)": [i for i in range(27) if lev[i] == 2],
              "B(lv01)": [i for i in range(27) if lev[i] in (0, 1)],
              "C(lv34)": [i for i in range(27) if lev[i] in (3, 4)]}
    table = {}
    for bn, idxs in blocks.items():
        # group by the arm02 "copy index": the arm02-weight ORBIT classes; a copy = one
        # arm02-weight value's fiber; content = multiset of (arm45 wt, arm1 wt, so10 origin)
        fibers = {}
        for i in idxs:
            fibers.setdefault(a02(i), []).append((a45(i), a1(i), so10[i]))
        table[bn] = {w: sorted(v) for w, v in fibers.items()}
    # the criterion: FLAVOR iff in every block whose arm02-weight set has exactly 3 values,
    # the three fibers carry IDENTICAL content multisets (ignoring the arm02 label itself)
    verdicts = {}
    for bn, fib in table.items():
        if len(fib) == 3:
            contents = [tuple(v) for v in fib.values()]
            verdicts[bn] = "identical-copies" if len(set(contents)) == 1 else "distinct-copies"
        else:
            verdicts[bn] = f"{len(fib)} arm02-classes (no 3-copy structure)"
    flavorish = [v for v in verdicts.values() if v == "identical-copies"]
    outcome = "FLAVOR" if flavorish and all(
        v in ("identical-copies",) or "no 3-copy" in v for v in verdicts.values()) else "CHIRAL"
    singlet = [i for i in range(27) if so10[i] == "1"][0]
    anomaly = dict(index=singlet, level=lev[singlet], arm02=a02(singlet),
                   arm45=a45(singlet), arm1=a1(singlet))
    return table, verdicts, outcome, anomaly


def v2_orbit_identity():
    """Transport B299's (theta,phi) to the banked frame; nine 3-orbits vs the 9-channel."""
    THETA = sp.Matrix([[0,-1,1,0,0,0],[1,-1,1,0,0,0],[0,0,1,0,0,0],
                       [0,0,1,0,-1,0],[0,0,0,1,-1,0],[0,0,0,0,0,1]])
    PHI = sp.Matrix([[1,0,0,0,0,-1],[0,1,0,0,0,-2],[0,0,1,0,0,-3],
                     [0,0,1,-1,1,-2],[0,0,1,-1,0,-1],[0,0,1,0,0,-2]])
    C299 = sp.Matrix([[2,-1,0,0,0,0],[-1,2,-1,0,0,0],[0,-1,2,-1,0,-1],
                      [0,0,-1,2,-1,0],[0,0,0,-1,2,0],[0,0,-1,0,0,2]])
    # node bijections ours->b299 (chain 0-2-3-4-5 with 1 on 3  ->  chain b0..b4 with b5 on b2)
    maps = [{0:0, 2:1, 3:2, 4:3, 5:4, 1:5},        # arm02 end first
            {5:0, 4:1, 3:2, 2:3, 0:4, 1:5}]        # the diagram-automorphism variant
    wtset = {WTS[i]: i for i in range(27)}
    results = {}
    for mi, m in enumerate(maps):
        P = sp.zeros(6, 6)
        for ours, b in m.items():
            P[b, ours] = 1
        if P.T * C299 * P != C_OURS:
            results[f"map{mi}"] = "cartan-mismatch (bijection invalid)"
            continue
        for name, G in (("theta", THETA), ("phi", PHI), ("theta*phi", THETA*PHI),
                        ("theta*phi^2", THETA*PHI*PHI)):
            W = C299 * G * C299.inv()             # action on Dynkin labels, b299 order
            act = {}
            ok = True
            for i in range(27):
                lam = P * sp.Matrix(WTS[i])       # ours -> b299 labels
                lam2 = W * lam
                back = tuple((P.T * lam2))        # b299 -> ours
                back = tuple(int(x) for x in back)
                if back not in wtset: ok = False; break
                act[i] = wtset[back]
            if not ok:
                results[f"map{mi}:{name}"] = "not-a-weight-permutation"
                continue
            # orbits
            seen, orbits = set(), []
            for i in range(27):
                if i in seen: continue
                o = {i, act[i], act[act[i]]}
                seen |= o; orbits.append(frozenset(o))
            sizes = Counter(len(o) for o in orbits)
            match = set(orbits) == CH024
            results[f"map{mi}:{name}"] = dict(orbit_sizes=dict(sizes),
                                              matches_9channel=match)
    return results


if __name__ == "__main__":
    table, verdicts, outcome, anomaly = v1_content_table()
    print("V1 -- per-block arm02-fiber structure:")
    for bn, v in verdicts.items():
        print(f"   {bn}: {v}")
    print(f"   singlet anomaly resolved: {anomaly}")
    print(f"   V1 OUTCOME: {outcome}")
    print()
    print("V2 -- orbit-channel identity:")
    r2 = v2_orbit_identity()
    hit = False
    for k, v in r2.items():
        print(f"   {k}: {v}")
        if isinstance(v, dict) and v.get("matches_9channel"): hit = True
    print(f"   V2 OUTCOME: {'IDENTICAL' if hit else 'DISTINCT'}")
    print()
    print("V3 assembles in FINDINGS from V1+V2 per the sealed branches.")
