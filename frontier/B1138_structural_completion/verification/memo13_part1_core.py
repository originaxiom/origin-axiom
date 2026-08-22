#!/usr/bin/env python3
"""INDEPENDENT VERIFICATION -- golden_gate memo 13 "THE Y-SELECTION" (session_handoff
commit 577712f), PART 1: the 18 hypercharge directions + the W(S1)xW(S2) 9+9 orbit
split. Own-authored code. certificates/g1_yselect.py etc. read for SPEC ONLY, not
imported. REUSES ONLY the banked+locked Chevalley e6 module
(frontier/B1102_exact_hypercharge_solve/e6_bracket_vendored.py). The 27's weights are
built here fresh (own minuscule-orbit code), cross-checked against B1102's own banked
FINDINGS.md target multiset and weight-class-size table, and against B883's build_27.py
saved data (read-only, frontier/B883_the_27/results.json).
"""
import importlib.util, itertools, os, time, json
from fractions import Fraction as Q
from collections import Counter
import sympy as sp

T0 = time.time()
def log(m): print(f"[{time.time()-T0:7.2f}s] {m}", flush=True)

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
VEND = os.path.join(REPO, "frontier/B1102_exact_hypercharge_solve/e6_bracket_vendored.py")

spec = importlib.util.spec_from_file_location("e6_trusted_bank_m13", VEND)
E6 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(E6)
ROOTS, IDX, N, DIM = E6.ROOTS, E6.IDX, E6.N, E6.DIM
BR, EVEC, HVEC, IP, EPS, CARTAN = E6.br, E6.evec, E6.hvec, E6.ip, E6.eps, E6.A
NR = len(ROOTS)
assert NR == 72 and DIM == 78, "trusted module shape unexpected -- stop"
SIMPLE = [tuple(1 if k == i else 0 for k in range(N)) for i in range(N)]
log(f"trusted e6 loaded (vendored, B1102 bank, sha in its header): {NR} roots, dim {DIM}")

# ============================================================ the 27's weights
# Own code: the minuscule orbit of a fundamental weight under simple reflections.
# (same *standard* technique as both cloud-seat certs use; written independently here)
CartM = sp.Matrix(N, N, lambda i, j: CARTAN[i][j])

def fundamental(k):
    b = sp.Matrix([1 if j == k else 0 for j in range(N)])
    return tuple(CartM.solve(b))

def wtip(lam, r):
    return sum(lam[i] * CARTAN[i][j] * r[j] for i in range(N) for j in range(N))

weights = None
minus_node = None
for k in range(N):
    lam0 = fundamental(k)
    orb = {lam0}
    frontier = [lam0]
    while frontier and len(orb) <= 27:
        nf = []
        for lam in frontier:
            for i in range(N):
                c = wtip(lam, SIMPLE[i])
                if c > 0:
                    nl = tuple(lam[j] - c * sp.Rational(SIMPLE[i][j]) for j in range(N))
                    if nl not in orb:
                        orb.add(nl)
                        nf.append(nl)
        frontier = nf
    if len(orb) == 27:
        weights = sorted(orb)
        minus_node = k
        break
assert weights is not None and len(weights) == 27
log(f"27 minuscule weights built (own code, node {minus_node}): {len(weights)} distinct")

# cross-check vs B883's build_27.py banked validation (read-only, not re-run)
B883_RESULTS = os.path.join(REPO, "frontier/B883_the_27/results.json")
b883 = json.load(open(B883_RESULTS))
log(f"B883 (banked, read-only) s1_multiplicities={b883['s1_multiplicities']} "
    f"validated={b883['validated']}  (cross-check target for the D5xu1 grading below)")

# D5 x u(1) grading cross-check (also memo 15's claim -- shared machinery)
charges = Counter()
for lam in weights:
    charges[sp.nsimplify(3 * lam[minus_node])] += 1
mults = sorted(charges.values(), reverse=True)
log(f"own D5xu1-style grading (3*alpha_{minus_node} coeff) multiset: {dict(charges)}  "
    f"mults={mults}  (expect [16,10,1], cross-checks B883's [1,10,16] up to labeling)")
assert mults == [16, 10, 1]

# ============================================================ the three A2 slots
log("building S0 (a0,a2 span), S1, S2 (orthogonal complement components) -- own code, "
    "same convention as B1102/B1135 (a0=simple[0], a2=simple[2])")
a0, a2 = SIMPLE[0], SIMPLE[2]
assert IP(a0, a2) == -1, "nodes 0,2 must be adjacent"

def iprr(a, b):
    return sum(a[i] * CARTAN[i][j] * b[j] for i in range(N) for j in range(N))

S0 = set()
for c1 in (-1, 0, 1):
    for c2 in (-1, 0, 1):
        r = tuple(c1 * a0[k] + c2 * a2[k] for k in range(N))
        if r in IDX:
            S0.add(r)
assert len(S0) == 6

Rperp = [r for r in ROOTS if iprr(r, a0) == 0 and iprr(r, a2) == 0]
assert len(Rperp) == 12

def connected_components(roots_list):
    remaining = set(roots_list)
    comps = []
    while remaining:
        start = next(iter(remaining))
        comp = {start}
        frontier = [start]
        remaining.discard(start)
        while frontier:
            nf = []
            for u in frontier:
                for v in list(remaining):
                    if iprr(u, v) != 0:
                        comp.add(v)
                        remaining.discard(v)
                        nf.append(v)
            frontier = nf
        comps.append(comp)
    return comps

comps = connected_components(Rperp)
assert len(comps) == 2 and all(len(c) == 6 for c in comps)
S1, S2 = comps
cross_bad = sum(1 for r in S1 for s in S2 if iprr(r, s) != 0)
assert cross_bad == 0
log(f"  S0={len(S0)} S1={len(S1)} S2={len(S2)}, mutually orthogonal confirmed")

def find_simple_pair(comp):
    for r, s in itertools.permutations(comp, 2):
        t = tuple(r[k] + s[k] for k in range(N))
        if iprr(r, s) == -1 and t in comp:
            return r, s
    raise RuntimeError("no simple pair found")

p1 = find_simple_pair(S1)
p2 = find_simple_pair(S2)
cor = [p1[0], p1[1], p2[0], p2[1]]
log(f"  cor basis fixed: p1={p1}  p2={p2}")

# ============================================================ the 18 hypercharge directions
log("projecting the 27 weights onto cor-coordinates, grouping into classes")

def wt4(lam):
    return tuple(int(wtip(lam, r)) for r in cor)

W4 = [wt4(w) for w in weights]
classes = Counter(W4)
class_sizes = sorted(classes.values(), reverse=True)
log(f"  weight-class sizes: {class_sizes}  (B1102 banked weight_class_sizes: "
    f"[3,3,3,3,3,3,1,1,1,1,1,1,1,1,1] -- cross-check)")
assert class_sizes == [3] * 6 + [1] * 9, "MISMATCH vs B1102 weight-class structure"

# B1102's own banked target multiset (FINDINGS.md, the banked 6Y multiset), scaled x6
# to clear denominators for exact integer pairing (same convenience the cloud cert uses)
B1102_TARGET_FRAC = {Q(1,6): 6, Q(1,3): 6, Q(-1,2): 4, Q(-2,3): 3,
                      Q(-1,3): 3, Q(0): 2, Q(1,2): 2, Q(1): 1}
assert sum(B1102_TARGET_FRAC.values()) == 27
target = {int(v * 6): m for v, m in B1102_TARGET_FRAC.items()}
log(f"  B1102 target (x6, exact): {target}")

cls = list(classes.items())
big = [c for c in cls if c[1] == 3]
vals3 = [v for v, m in target.items() if m >= 3]
sols = set()
for assign in itertools.product(vals3, repeat=6):
    used = Counter()
    for v in assign:
        used[v] += 3
    if any(used[v] > target.get(v, 0) for v in used):
        continue
    Am = sp.Matrix([list(w) for w, _ in big])
    bvec = sp.Matrix(list(assign))
    if Am.rank() != Am.row_join(bvec).rank() or Am.rank() < 4:
        continue
    y = (Am.T * Am).solve(Am.T * bvec)
    got = Counter()
    ok = True
    for w, sz in cls:
        val = sum(y[i] * w[i] for i in range(4))
        if val != int(val):
            ok = False
            break
        got[int(val)] += sz
    if ok and dict(got) == target:
        sols.add(tuple(Q(sp.Rational(y[i]).p, sp.Rational(y[i]).q) for i in range(4)))

sols = sorted(sols)
log(f"  hypercharge directions solved (own code): {len(sols)}  (B1102/B1118 banked: 18)")
assert len(sols) == 18, f"expected 18, got {len(sols)}"

# every one of the 18, divided by 6, must reproduce B1102's EXACT fractional target
for y in sols:
    got = Counter()
    for w, sz in cls:
        val = Q(sum(y[i] * w[i] for i in range(4)), 6)
        got[val] += sz
    assert dict(got) == dict(B1102_TARGET_FRAC), f"y={y} fails exact B1102 multiset match: {dict(got)}"
log("  ALL 18 directions reproduce B1102's EXACT banked fractional multiset "
    "{1/6x6,1/3x6,-1/2x4,-2/3x3,-1/3x3,0x2,1/2x2,1x1} -- CONFIRMED")

# ============================================================ W(S1) x W(S2), order 36
log("building W(S1) x W(S2) (order 36) acting on cor-coords, checking 9+9 orbit split")

def refl_matrix(ridx):
    Mm = sp.eye(4)
    for j in range(4):
        Mm[ridx, j] = Mm[ridx, j] - iprr(cor[ridx], cor[j])
    return Mm

gensW = [refl_matrix(k) for k in range(4)]
seenW = {tuple(sp.eye(4)): sp.eye(4)}
frontier = [sp.eye(4)]
while frontier:
    nf = []
    for X in frontier:
        for g in gensW:
            Y = g * X
            k2 = tuple(Y)
            if k2 not in seenW:
                seenW[k2] = Y
                nf.append(Y)
    frontier = nf
log(f"  |W(S1) x W(S2)| = {len(seenW)}  (expect 36 = 6x6)")
assert len(seenW) == 36

def act(Mm, y):
    ysp = [sp.Rational(v.numerator, v.denominator) for v in y]
    out = tuple(sum(Mm[i, j] * ysp[j] for j in range(4)) for i in range(4))
    return tuple(Q(sp.Rational(v).p, sp.Rational(v).q) for v in out)

solset = set(sols)
orbits = []
left = set(sols)
while left:
    y0 = next(iter(left))
    orb = {act(Mm, y0) for Mm in seenW.values()} & solset
    orbits.append(orb)
    left -= orb
orbit_sizes = sorted(len(o) for o in orbits)
log(f"  orbits of the 18 under W(S1)xW(S2): sizes {orbit_sizes}  (expect [9,9])")
assert orbit_sizes == [9, 9]
O1, O2 = orbits
log("  9+9 ORBIT SPLIT CONFIRMED (own recomputation)")

# ---------------------------------------------------------------- save state for part 2
STATE = dict(
    sols=[[str(x) for x in y] for y in sols],
    O1=[[str(x) for x in y] for y in O1],
    O2=[[str(x) for x in y] for y in O2],
    S0=[list(r) for r in sorted(S0)],
    S1=[list(r) for r in sorted(S1)],
    S2=[list(r) for r in sorted(S2)],
    p1=[list(p1[0]), list(p1[1])],
    p2=[list(p2[0]), list(p2[1])],
    cor=[list(c) for c in cor],
    weights=[[str(x) for x in w] for w in weights],
    class_sizes=class_sizes,
)
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "part1_state.json")
json.dump(STATE, open(OUT, "w"))
log(f"state saved to {OUT}")
log("PART 1 DONE -- core hypercharge computation confirmed")
