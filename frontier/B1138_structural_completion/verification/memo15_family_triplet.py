#!/usr/bin/env python3
"""INDEPENDENT VERIFICATION -- golden_gate memo 15 "THE FAMILY TRIPLET" (session_handoff
commit 577712f). Own-authored code throughout. certificates/family_triplet.py read for
SPEC ONLY (never imported/copied) -- and its own E8 Cartan matrix was found to be
ASYMMETRIC as transcribed (row2 has a -1 at col7 but row7 has 0 at col2; row7 has a -1 at
col1 but row1 has 0 at col7), which cannot be a genuine simply-laced Cartan matrix, so it
is NOT reused; a fresh, independently-verified, symmetric Bourbaki E8 Cartan matrix is
built here instead (self-checked: symmetric by construction, and produces exactly 240
roots, which only the E8 root system among rank-8 simple systems has -- a strong
correctness signal in itself).

Reuses: frontier/B1102_exact_hypercharge_solve/e6_bracket_vendored.py for the E6 part
(Part 2, the D5xu1 grading of the 27) -- same module memo 13's verification used.
The E8 part (Part 1) needs no Chevalley bracket/structure constants at all -- only the
root system and inner products -- so nothing beyond a Cartan matrix is required there.
"""
import importlib.util, itertools, os, time, json
from collections import Counter
import sympy as sp

T0 = time.time()
def log(m): print(f"[{time.time()-T0:7.2f}s] {m}", flush=True)

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

# ============================================================ PART 1: E8, own build
log("PART 1: E8 root system, own Bourbaki Cartan matrix (chain 0-2-3-4-5-6-7, node1@node3)")
N8 = 8
EDGES8 = [(0, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (1, 3)]
A8 = [[2 if i == j else 0 for j in range(N8)] for i in range(N8)]
for i, j in EDGES8:
    A8[i][j] = A8[j][i] = -1
# symmetry self-check
assert all(A8[i][j] == A8[j][i] for i in range(N8) for j in range(N8)), "Cartan matrix not symmetric!"
log(f"  Cartan matrix built, symmetry self-check PASSED")

def ip8(a, b):
    return sum(a[i] * A8[i][j] * b[j] for i in range(N8) for j in range(N8))

def build_roots8():
    simples = [tuple(1 if i == j else 0 for i in range(N8)) for j in range(N8)]
    roots = set(simples)
    frontier = list(simples)
    while frontier:
        nxt = []
        for r in frontier:
            for j in range(N8):
                pair = sum(r[i] * A8[i][j] for i in range(N8))
                s = tuple(r[i] - pair * (1 if i == j else 0) for i in range(N8))
                if any(s) and s not in roots:
                    roots.add(s)
                    nxt.append(s)
        frontier = nxt
    return sorted(roots)

ROOTS8 = build_roots8()
log(f"  roots built by reflection closure: {len(ROOTS8)}  (ONLY E8 among rank-8 simple "
    f"systems has exactly 240 -- self-verifying)")
assert len(ROOTS8) == 240, f"expected 240 (E8), got {len(ROOTS8)} -- Cartan matrix is wrong type/rank"
IDX8 = {r: k for k, r in enumerate(ROOTS8)}
DIM8 = N8 + len(ROOTS8)
assert DIM8 == 248
log(f"  dim e8 = {N8} + {len(ROOTS8)} = {DIM8}")
SIMPLE8 = [tuple(1 if k == i else 0 for k in range(N8)) for i in range(N8)]

# highest root (own check: unique dominant root)
dominant = [r for r in ROOTS8 if all(ip8(r, SIMPLE8[i]) >= 0 for i in range(N8))]
assert len(dominant) == 1, f"expected a UNIQUE highest root, got {len(dominant)}"
theta = dominant[0]
log(f"  unique highest root theta found: {theta}")

# ------------------------------------------------------ find the family A2 (S_fam)
log("PART 1b: searching for an A2 (family slot) whose FULL orthogonal complement in the "
    "240 roots is exactly 72 (an E6) -- own bounded search, starting from theta")

def orth_complement(pair_roots):
    r1, r2 = pair_roots
    return [r for r in ROOTS8 if ip8(r, r1) == 0 and ip8(r, r2) == 0]

def is_a2_pair(r1, r2):
    if ip8(r1, r2) != -1:
        return False
    s = tuple(r1[i] + r2[i] for i in range(N8))
    return s in IDX8

S_fam = None
_t = time.time()
for r1 in [theta] + ROOTS8:
    for r2 in ROOTS8:
        if r2 == r1:
            continue
        if is_a2_pair(r1, r2):
            comp = orth_complement((r1, r2))
            if len(comp) == 72:
                S_fam_pair = (r1, r2)
                S_fam = {r1, r2, tuple(-x for x in r1), tuple(-x for x in r2),
                          tuple(r1[i] + r2[i] for i in range(N8)),
                          tuple(-r1[i] - r2[i] for i in range(N8))}
                break
    if S_fam is not None:
        break
assert S_fam is not None and len(S_fam) == 6
log(f"  family A2 found in {time.time()-_t:.2f}s: simple pair {S_fam_pair}; |S_fam|=6")
E6_1 = set(orth_complement(S_fam_pair))
assert len(E6_1) == 72
log(f"  its orthogonal complement: {len(E6_1)} roots (E6, checked)")

# ------------------------------------------------ decompose E6_1 into 3 orthogonal A2's
log("PART 1c: decomposing E6_1 into its own 3 orthogonal A2's (same method as memo 13 / "
    "B1135, applied within this 72-root sub-system)")

def find_adjacent_pair_in(pool):
    for r1 in pool:
        for r2 in pool:
            if r2 == r1:
                continue
            if is_a2_pair(r1, r2):
                return r1, r2
    raise RuntimeError("no adjacent pair found")

b0a, b0b = find_adjacent_pair_in(E6_1)
S0e = set()
for c1 in (-1, 0, 1):
    for c2 in (-1, 0, 1):
        r = tuple(c1 * b0a[k] + c2 * b0b[k] for k in range(N8))
        if r in IDX8:
            S0e.add(r)
assert len(S0e) == 6

Rperp_e6 = [r for r in E6_1 if ip8(r, b0a) == 0 and ip8(r, b0b) == 0]
assert len(Rperp_e6) == 12

def connected_components8(roots_list):
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
                    if ip8(u, v) != 0:
                        comp.add(v)
                        remaining.discard(v)
                        nf.append(v)
            frontier = nf
        comps.append(comp)
    return comps

comps_e6 = connected_components8(Rperp_e6)
assert len(comps_e6) == 2 and all(len(c) == 6 for c in comps_e6)
S1e, S2e = comps_e6
log(f"  E6_1 decomposed: S0e={len(S0e)} S1e={len(S1e)} S2e={len(S2e)}")

def simple_pair_of(comp):
    for r1, r2 in itertools.permutations(comp, 2):
        if is_a2_pair(r1, r2):
            return r1, r2
    raise RuntimeError("no simple pair")

SLOT_PAIRS8 = [S_fam_pair, (b0a, b0b), simple_pair_of(S1e), simple_pair_of(S2e)]
SLOTS8 = [S_fam, S0e, S1e, S2e]
names = ["S_fam (family A2)", "S0 (E6-internal)", "S1 (E6-internal)", "S2 (E6-internal)"]

# ============================================================ PART 1d: the family triplet check
log("PART 1d: for EACH of the 4 orthogonal A2 slots -- complement=72(E6), crossing=162, "
    "projecting onto exactly 6 weights x 27 each")
all_pass = True
for nm, S, (r1, r2) in zip(names, SLOTS8, SLOT_PAIRS8):
    comp = orth_complement((r1, r2))
    crossing = [r for r in ROOTS8 if r not in S and any(ip8(r, s) != 0 for s in S)]
    proj = Counter((ip8(r, r1), ip8(r, r2)) for r in crossing)
    ok = (len(comp) == 72 and len(crossing) == 162 and len(proj) == 6
          and all(v == 27 for v in proj.values()))
    log(f"  {nm}: |slot|={len(S)} |complement|={len(comp)} (want 72) "
        f"|crossing|={len(crossing)} (want 162) weights={dict(proj)}  {'PASS' if ok else 'FAIL'}")
    all_pass = all_pass and ok
assert all_pass, "not every slot gave the (8,1)+(1,78)+(3,27)+(3bar,27bar) decomposition"
log("  EVERY ONE of the 4 slots: complement=e6(72), crossing=162=6x27 -- CONFIRMED")
log("  => 248 = (8,1) + (1,78) + (3,27) + (3bar,27bar); dim check 8+78+81+81 = "
    f"{8+78+81+81}")
assert 8 + 78 + 81 + 81 == 248
log("  THE 27 ENTERS E8 EXACTLY THREE TIMES, indexed by the A2-triplet of ANY of the "
    "4 slots -- CONFIRMED (own E8 construction, independent of the cloud seat's script)")

# ============================================================ PART 2: E6's 27, D5 x u(1)
log("\nPART 2: the E6 27's D5xu(1) grading (charge multiset) -- reusing the SAME banked "
    "e6_bracket_vendored.py module and the SAME own minuscule-orbit 27 construction "
    "already independently verified in the memo-13 script (Part 1 of that verification)")
VEND = os.path.join(REPO, "frontier/B1102_exact_hypercharge_solve/e6_bracket_vendored.py")
spec = importlib.util.spec_from_file_location("e6_trusted_bank_m15", VEND)
E6M = importlib.util.module_from_spec(spec)
spec.loader.exec_module(E6M)
ROOTS6, IDX6, N6 = E6M.ROOTS, E6M.IDX, E6M.N
CARTAN6 = E6M.A
assert len(ROOTS6) == 72
SIMPLE6 = [tuple(1 if k == i else 0 for k in range(N6)) for i in range(N6)]
CartM6 = sp.Matrix(N6, N6, lambda i, j: CARTAN6[i][j])

def fundamental6(k):
    b = sp.Matrix([1 if j == k else 0 for j in range(N6)])
    return tuple(CartM6.solve(b))

def wtip6(lam, r):
    return sum(lam[i] * CARTAN6[i][j] * r[j] for i in range(N6) for j in range(N6))

weights6 = None
minus_node6 = None
for k in range(N6):
    lam0 = fundamental6(k)
    orb = {lam0}
    frontier = [lam0]
    while frontier and len(orb) <= 27:
        nf = []
        for lam in frontier:
            for i in range(N6):
                c = wtip6(lam, SIMPLE6[i])
                if c > 0:
                    nl = tuple(lam[j] - c * sp.Rational(SIMPLE6[i][j]) for j in range(N6))
                    if nl not in orb:
                        orb.add(nl)
                        nf.append(nl)
        frontier = nf
    if len(orb) == 27:
        weights6 = sorted(orb)
        minus_node6 = k
        break
assert weights6 is not None and len(weights6) == 27
log(f"  27 weights rebuilt (own code, node {minus_node6}): {len(weights6)} distinct")

charges6 = Counter()
for lam in weights6:
    charges6[sp.nsimplify(3 * lam[minus_node6])] += 1
log(f"  charge multiset (3*alpha_{minus_node6} coefficient): {dict(charges6)}")
mults6 = sorted(charges6.values(), reverse=True)
log(f"  multiplicities: {mults6}  (expect [16,10,1] = 16-spinor family + 10-vector + "
    f"1-singlet)")
assert mults6 == [16, 10, 1]
log("  CONFIRMED: 27 = 16 (+) 10 (+) 1 under E6 grading by a minuscule-node u(1) "
    "(matches memo 15's charge multiset {4:1,-2:10,1:16} up to overall normalization "
    "of the u(1) generator -- the PARTITION [16,10,1] is what's asserted and it matches "
    "exactly; also cross-checked against B883's independently-derived (via the E7 cubic "
    "invariant, an entirely different route) s1_multiplicities=[1,10,16] in memo 13's "
    "Part 1 run)")

# ============================================================ fence check
log("\nFENCE CHECK: is the claim 'the object forces E8/3-generations', or merely "
    "'IF E8 is reached, the algebra affords 3x27'? -- this script computes ONLY the "
    "algebra fact (E8 root combinatorics + E6 branching); it makes and can make NO "
    "claim about whether the programme's own object reaches or forces E8. That question "
    "is explicitly marked EXHIBITS-NOT-FORCES per B1033/the banking seat's prior fence, "
    "and nothing computed here bears on it either way.")

RESULT = dict(
    e8_roots=len(ROOTS8), e8_dim=DIM8,
    family_triplet_all_slots_pass=all_pass,
    dim_check=8 + 78 + 81 + 81,
    e6_27_mults=mults6,
    e6_charge_multiset={str(k): v for k, v in charges6.items()},
)
HERE = os.path.dirname(os.path.abspath(__file__))
json.dump(RESULT, open(os.path.join(HERE, "memo15_result.json"), "w"), indent=2)
log(f"\nresult summary dumped to {os.path.join(HERE, 'memo15_result.json')}")
log("MEMO 15 VERIFICATION DONE")
