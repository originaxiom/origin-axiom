#!/usr/bin/env python3
"""INDEPENDENT VERIFICATION of golden_gate memo 24 (SM_TABLE.md / certificates/sm_table.py)
and memo 23 (WEINBERG_POINT.md / certificates/weinberg.py), ref 577712f.

VERIFY-DON'T-TRUST discipline (own-code, per the assignment):
  - The two cloud certificates were read ONLY to understand the SPEC (what is claimed,
    what the closing assignment structurally is: color via wt4-classes, T3L the kept
    su(2), T3R the OTHER annihilated su(2), Y_phys, Q=T3L+Y, candidate B-L=2(Y-T3R)).
    Neither certificate's code is imported or copied anywhere below.
  - REUSED (per the task's explicit instruction): the banked, already-certified Chevalley
    e6 module frontier/B1102_exact_hypercharge_solve/e6_bracket_vendored.py (loaded fresh
    below, its ROOTS/Cartan-matrix/ip() reused directly -- these are the "trusted" e6
    primitives, re-certified in B1102's own arc by the full Jacobi/antisymmetry check).
  - The 27 representation: built HERE by the standard crystal-of-omega_1 BFS descent
    (a textbook construction for E6's minuscule 27; mathematically the SAME object
    frontier/B883_the_27/build_27.py and B1102's build_27() construct via different
    routes -- written fresh here, in e6_bracket_vendored's OWN coordinate frame
    throughout, to avoid cross-module basis-alignment risk). frontier/B883_the_27/
    build_27.py is separately EXECUTED unmodified below (own subprocess) as a genuine
    reuse + cross-check that "the 27" both scripts work with is the same object (same
    weight count, same dominant weight, same validated 1+10+16 branching).
  - The trinification decomposition e6 = su(3)_c(S0) + su(3)_L(S1) + su(3)_R(S2): this is
    the SAME standard maximal-rank subalgebra frontier/B1134 and frontier/B1135 build (own
    scripts, already twice-banked locally) -- re-derived FRESH here (own code, not
    imported) using the identical, mechanically-checkable recipe (S0 = the A2 spanned by
    two non-adjacent-to-each-other, mutually-adjacent simple roots; S1,S2 = the two
    connected components of the roots orthogonal to S0), with every structural property
    (orthogonality, A2-closure, sizes) independently re-verified below, not assumed.
  - The physical (Y, beta_L, beta_R) closing assignment: memo 13's own selection search
    (g1_yselect.py) was NOT fetched or reproduced (out of this task's scope -- the task
    directs "the closing assignment is memo 23's"). Instead this script performs ITS OWN
    small, exhaustive, well-posed search for a physical assignment (any (beta_L in S1,
    beta_R in S2, Y in the S1+S2 Cartan neutral on both) reproducing the exact physical
    charge multiset) -- independent discovery of *a* valid physical point, not a bit-match
    of the cloud's specific numbers. The cloud's OWN concrete numbers (fetched from
    session_handoff/outputs/{weinberg,sm_table}_out.txt at the same ref, read as
    reference data only) are used purely as a cross-check target for the CLAIMS (the
    table shape, the anomaly zeros, the naive-B-L unphysical values), never executed.

Run: python3 verify_sm_table.py
"""
import importlib.util
import itertools
import os
import subprocess
import sys
from collections import Counter, deque
from fractions import Fraction as F

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
VENDORED = os.path.join(REPO, "frontier/B1102_exact_hypercharge_solve/e6_bracket_vendored.py")
BUILD27 = os.path.join(REPO, "frontier/B883_the_27/build_27.py")


def log(msg):
    print(msg, flush=True)


# ============================================================ PART 0 -- trusted e6 (REUSED)
def load_trusted_e6():
    spec = importlib.util.spec_from_file_location("e6_trusted_bank", VENDORED)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


log("=" * 78)
log("PART 0: loading the banked, certified Chevalley e6 (frontier/B1102 vendored module)")
E6 = load_trusted_e6()
ROOTS, IDX, N, DIM = E6.ROOTS, E6.IDX, E6.N, E6.DIM
A, ip = E6.A, E6.ip
assert len(ROOTS) == 72 and DIM == 78 and N == 6, "trusted e6 module shape unexpected"
SIMPLE = [tuple(1 if k == i else 0 for k in range(N)) for i in range(N)]
log(f"  e6 loaded: {len(ROOTS)} roots, dim {DIM}, rank {N} -- REUSED, not rebuilt")

# ================================================ PART 0b -- cross-check: run build_27.py
log("\nPART 0b: cross-check by ACTUALLY RUNNING frontier/B883_the_27/build_27.py (REUSED,")
log("  unmodified, own subprocess -- writes only inside its own arc dir as it always does;")
log("  used here purely as an independent confirmation that 'the 27' is the same object)")
res = subprocess.run([sys.executable, BUILD27], cwd=os.path.dirname(BUILD27),
                      capture_output=True, text=True, timeout=300)
b883_tail = "\n".join(res.stdout.strip().splitlines()[-4:])
log(f"  build_27.py exit={res.returncode}; tail of its own output:\n    " +
    b883_tail.replace("\n", "\n    "))
assert res.returncode == 0
assert "VALIDATED: True" in res.stdout, "B883's own 1+10+16 validation did not pass"
log("  CONFIRMED: B883's independently-routed 27 (via the e7 3-grading) validates itself")
log("  (27 distinct weights, dominant = omega_1, branching 1+10+16 at the enhancement point)")

# ============================================== PART 1 -- the 27's weights, OWN crystal BFS
log("\n" + "=" * 78)
log("PART 1: the 27 = crystal of omega_1, built FRESH here (own code) directly in")
log("  e6_bracket_vendored's own coordinate frame (simple-root basis throughout)")


def ipr(a, b):
    return sum(sp.Rational(a[i]) * A[i][j] * sp.Rational(b[j]) for i in range(N) for j in range(N))


Msys = sp.Matrix(N, N, lambda i, j: ip(SIMPLE[i], SIMPLE[j]))
rhs = sp.Matrix([1] + [0] * (N - 1))
w1 = Msys.solve(rhs)
omega1 = tuple(sp.nsimplify(w1[k]) for k in range(N))


def tsub(a, b):
    return tuple(sp.nsimplify(x - y) for x, y in zip(a, b))


weights = [omega1]
seen = {omega1}
queue = [omega1]
while queue:
    lam = queue.pop()
    for al in SIMPLE:
        if ipr(lam, al) == 1:
            mu = tsub(lam, al)
            if mu not in seen:
                seen.add(mu)
                weights.append(mu)
                queue.append(mu)
assert len(weights) == 27, f"expected 27 weights, got {len(weights)}"
log(f"  crystal BFS from omega_1 = {omega1}: {len(weights)} distinct weights (own re-derivation)")

# sanity: all weights are minuscule (every simple-root pairing in {-1,0,1})
minuscule_ok = all(ipr(lam, al) in (-1, 0, 1) for lam in weights for al in SIMPLE)
assert minuscule_ok
log("  minuscule check (all simple-root pairings in {-1,0,1}): PASS")

# ============================================== PART 2 -- the trinification slots S0,S1,S2
log("\n" + "=" * 78)
log("PART 2: e6 = su(3)_c(S0) + su(3)_L(S1) + su(3)_R(S2), re-derived fresh (own code,")
log("  same standard recipe as frontier/B1134/B1135's own independently-verified scripts)")

a0, a2 = SIMPLE[0], SIMPLE[2]
assert ip(a0, a2) == -1, "nodes 0,2 must be adjacent (Cartan integer -1)"
S0 = set()
for c1 in (-1, 0, 1):
    for c2 in (-1, 0, 1):
        r = tuple(c1 * a0[k] + c2 * a2[k] for k in range(N))
        if r in IDX:
            S0.add(r)
assert len(S0) == 6, f"S0 (color A2) should have 6 roots, got {len(S0)}"

Rperp = [r for r in ROOTS if ip(r, a0) == 0 and ip(r, a2) == 0]
assert len(Rperp) == 12


def connected_components(roots_list):
    remaining = set(roots_list)
    comps = []
    while remaining:
        start = next(iter(remaining))
        comp = {start}
        q = deque([start])
        remaining.discard(start)
        while q:
            u = q.popleft()
            for v in list(remaining):
                if ip(u, v) != 0:
                    comp.add(v)
                    remaining.discard(v)
                    q.append(v)
        comps.append(comp)
    return comps


comps = connected_components(Rperp)
assert len(comps) == 2 and all(len(c) == 6 for c in comps), "expected 2 components of size 6"
S1, S2 = comps
cross_bad = sum(1 for r in S1 for s in S2 if ip(r, s) != 0)
assert cross_bad == 0, "S1, S2 must be mutually orthogonal"
log(f"  S0(color)={len(S0)} S1={len(S1)} S2={len(S2)} roots; S0 perp {{S1,S2}}, S1 perp S2 (own check)")


def find_simple_pair(comp):
    for r, s in itertools.permutations(comp, 2):
        t = tuple(r[k] + s[k] for k in range(N))
        if ip(r, s) == -1 and t in comp:
            return r, s
    raise RuntimeError("no simple pair found in component")


p0 = find_simple_pair(S0)
p1 = find_simple_pair(S1)
p2 = find_simple_pair(S2)
log(f"  each slot independently confirmed to be a genuine A2 (su(3)) root system")
log(f"  slot simple pairs: S0={p0}  S1={p1}  S2={p2}")

# ============================================== PART 3 -- color via wt4 classes (own code)
log("\n" + "=" * 78)
log("PART 3: color content of the 27 via the wt4-classes (own re-derivation of the")
log("  B1102-style rule: joint weight under the NON-color Cartan (S1+S2, 4-dim) --")
log("  states sharing a non-color weight are color-partners; class size 3 = triplet)")

cor = [p1[0], p1[1], p2[0], p2[1]]  # coroots spanning the non-color (S1+S2) Cartan


def wt4(lam):
    return tuple(ipr(lam, c) for c in cor)


W4 = [wt4(lam) for lam in weights]
cls = Counter(W4)
class_sizes = sorted(cls.values(), reverse=True)
log(f"  wt4-class sizes: {class_sizes}")
assert class_sizes == [3] * 6 + [1] * 9, "expected 6 triplet classes + 9 singlet classes"
colored = [i for i, lam in enumerate(weights) if cls[W4[i]] == 3]
assert len(colored) == 18 and (27 - len(colored)) == 9
log(f"  colored states: {len(colored)} (6 classes x3);  color-singlet states: "
    f"{27 - len(colored)} (9 classes x1) -- CONFIRMED, matches memo 24's 'banked wt4 classes'")
log("  ALSO matches B1102's independently-found class-size pattern [3^6, 1^9] in ITS OWN,")
log("  completely different (centralizer-adapted) basis -- a structural cross-anchor.")

# ============================================== PART 4 -- own search: a physical closing
log("\n" + "=" * 78)
log("PART 4: OWN search for a physical assignment -- beta_L in S1, beta_R in S2 (or the")
log("  L<->R relabeling), Y confined to the S1+S2 Cartan and neutral on both, such that")
log("  Q = T3L + Y_phys reproduces the EXACT physical charge multiset {+-1:2,+-2/3:3,")
log("  -+1/3:6, 0:5}. Exhaustive over the small combinatorial space (S1,S2 root choices x")
log("  a 2x2 linear solve per candidate pair of classes/targets) -- not a hand guess.")

PHYS_TARGET = Counter({sp.Rational(0): 5, sp.Rational(1): 2, sp.Rational(-1): 2,
                        sp.Rational(1, 3): 6, sp.Rational(-1, 3): 6,
                        sp.Rational(2, 3): 3, sp.Rational(-2, 3): 3})
assert sum(PHYS_TARGET.values()) == 27
PHYS_SET = sorted(PHYS_TARGET, key=str)  # sorted (not a raw set) -- deterministic search order

# ADDITIONAL, non-circular target: B1102's own independently-banked "6Y" hypercharge
# multiset (frontier/B1102_exact_hypercharge_solve/FINDINGS.md, Side 1: "the banked 6Y
# hypercharge multiset {1/6x6, 1/3x6, -1/2x4, -2/3x3, -1/3x3, 0x2, 1/2x2, 1x1}") -- an arc
# banked long before memo 23/24 existed, on a totally different (centralizer-adapted)
# landing. Used here ONLY to disambiguate ties in the Q-multiset search below (the Q-only
# criterion under-determines (s,t): a Q-physical solution exists whose Y-values do NOT
# match the standard embedding at all -- e.g. Q_L getting Y=-1/6 instead of +1/6 -- so this
# second, independent target is required to pick out the STANDARD embedding, not merely
# "a" charge-consistent relabeling. Matching it is itself a strong cross-check, not an
# assumption: B1102's multiset was derived with no reference to the trinification frame.
B1102_Y_TARGET = Counter({sp.Rational(1, 6): 6, sp.Rational(1, 3): 6, sp.Rational(-1, 2): 4,
                           sp.Rational(-2, 3): 3, sp.Rational(-1, 3): 3, sp.Rational(0): 2,
                           sp.Rational(1, 2): 2, sp.Rational(1): 1})
assert sum(B1102_Y_TARGET.values()) == 27


def slot_roots_pos(slot_pair, slot_set):
    # the 3 "positive" roots of the A2: the two simple ones + their sum
    r, s = slot_pair
    t = tuple(r[k] + s[k] for k in range(N))
    assert t in slot_set
    return [r, s, t]


def try_assignment(betaL_slot_idx):
    """betaL_slot_idx: 0 -> beta_L drawn from S1, T3R from S2 ; 1 -> swapped."""
    slots = [(S1, p1), (S2, p2)]
    (SL, pL), (SR, pR) = (slots[0], slots[1]) if betaL_slot_idx == 0 else (slots[1], slots[0])
    L_candidates = slot_roots_pos(pL, SL)
    L_candidates = L_candidates + [tuple(-x for x in r) for r in L_candidates]
    R_candidates = slot_roots_pos(pR, SR)
    R_candidates = R_candidates + [tuple(-x for x in r) for r in R_candidates]

    # coroots spanning the L-slot and R-slot Cartans (2 each)
    corL = list(pL)
    corR = list(pR)

    for beta_L in L_candidates:
        for beta_R in R_candidates:
            # Y confined to span(corL) + span(corR), neutral on beta_L and beta_R:
            #   y0*ip(beta_L,corL0) + y1*ip(beta_L,corL1) = 0  -> a 1-dim line (yL0,yL1)=s*dirL
            #   y2*ip(beta_R,corR0) + y3*ip(beta_R,corR1) = 0  -> (yR0,yR1)=t*dirR
            cL0, cL1 = ip(beta_L, corL[0]), ip(beta_L, corL[1])
            if cL1 != 0:
                dirL = (sp.Integer(1), sp.Rational(-cL0, cL1))
            elif cL0 != 0:
                dirL = (sp.Integer(0), sp.Integer(1))
            else:
                continue
            cR0, cR1 = ip(beta_R, corR[0]), ip(beta_R, corR[1])
            if cR1 != 0:
                dirR = (sp.Integer(1), sp.Rational(-cR0, cR1))
            elif cR0 != 0:
                dirR = (sp.Integer(0), sp.Integer(1))
            else:
                continue

            def T3L_of(lam):
                return sp.Rational(ipr(lam, beta_L), 2)

            def T3R_of(lam):
                return sp.Rational(ipr(lam, beta_R), 2)

            def fL(lam):
                return ipr(lam, corL[0]) * dirL[0] + ipr(lam, corL[1]) * dirL[1]

            def fR(lam):
                return ipr(lam, corR[0]) * dirR[0] + ipr(lam, corR[1]) * dirR[1]

            # per-class data (one representative weight per wt4-class)
            class_reps = {}
            for i, lam in enumerate(weights):
                class_reps.setdefault(W4[i], (lam, cls[W4[i]]))
            reps = list(class_reps.values())  # [(lam, class_size), ...] 15 entries

            coeffs = [(T3L_of(lam), fL(lam), fR(lam), csize) for lam, csize in reps]
            # try all pairs of classes with independent (fL,fR) to solve for (s,t)
            idxs = list(range(len(coeffs)))
            PHYS_SET_SET = set(PHYS_SET)
            for i, j in itertools.combinations(idxs, 2):
                T3Li, fLi, fRi, _ = coeffs[i]
                T3Lj, fLj, fRj, _ = coeffs[j]
                det = fLi * fRj - fLj * fRi
                if det == 0:
                    continue
                for qi in PHYS_SET:
                    for qj in PHYS_SET:
                        # solve  T3Li + s*fLi + t*fRi = qi ;  T3Lj + s*fLj + t*fRj = qj
                        rhs_i, rhs_j = qi - T3Li, qj - T3Lj
                        s_val = (rhs_i * fRj - rhs_j * fRi) / det
                        t_val = (fLi * rhs_j - fLj * rhs_i) / det
                        # evaluate all 15 classes
                        Qs = [T3l + s_val * fl + t_val * fr for T3l, fl, fr, _ in coeffs]
                        if not all(q in PHYS_SET_SET for q in Qs):
                            continue
                        Q_mult = Counter()
                        Y_mult = Counter()
                        for (T3l, fl, fr, csize), q in zip(coeffs, Qs):
                            Q_mult[q] += csize
                        Ys = [s_val * fl + t_val * fr for _, fl, fr, _ in coeffs]
                        for (_, _, _, csize), y in zip(coeffs, Ys):
                            Y_mult[y] += csize
                        if Q_mult == PHYS_TARGET and Y_mult == B1102_Y_TARGET:
                            return dict(beta_L=beta_L, beta_R=beta_R, s=s_val, t=t_val,
                                        dirL=dirL, dirR=dirR, corL=corL, corR=corR,
                                        L_slot="S1" if betaL_slot_idx == 0 else "S2",
                                        R_slot="S2" if betaL_slot_idx == 0 else "S1")
    return None


found = try_assignment(0) or try_assignment(1)
assert found is not None, "NO physical assignment found by the own search"
log(f"  FOUND a physical assignment: beta_L={found['beta_L']} (slot {found['L_slot']}), "
    f"beta_R={found['beta_R']} (slot {found['R_slot']})")
log(f"  Y = {found['s']} * (dir in {found['L_slot']}'s Cartan) + {found['t']} * "
    f"(dir in {found['R_slot']}'s Cartan)  [own coordinates -- not the cloud's basis]")

# ============================================== PART 5 -- build the full 27-state table
log("\n" + "=" * 78)
log("PART 5: THE FULL TABLE, own numbers")

beta_L, beta_R = found["beta_L"], found["beta_R"]
s_val, t_val = found["s"], found["t"]
corL, corR = found["corL"], found["corR"]
dirL, dirR = found["dirL"], found["dirR"]


def T3L_of(lam):
    return sp.Rational(ipr(lam, beta_L), 2)


def T3R_of(lam):
    return sp.Rational(ipr(lam, beta_R), 2)


def Yphys_of(lam):
    fL = ipr(lam, corL[0]) * dirL[0] + ipr(lam, corL[1]) * dirL[1]
    fR = ipr(lam, corR[0]) * dirR[0] + ipr(lam, corR[1]) * dirR[1]
    return s_val * fL + t_val * fR


rows = []
for i, lam in enumerate(weights):
    t3l, t3r, y = T3L_of(lam), T3R_of(lam), Yphys_of(lam)
    q = t3l + y
    bl_naive = 2 * (y - t3r)
    is_colored = (i in colored)
    rows.append(dict(colored=is_colored, T3L=t3l, T3R=t3r, Y=y, Q=q, BL=bl_naive))

# 1. the table, grouped by class (matches the cert's "colored?, T3L, T3R, Y, Q, B-L : count")
mult = Counter((r["colored"], str(r["T3L"]), str(r["T3R"]), str(r["Y"]), str(r["Q"]), str(r["BL"]))
               for r in rows)
log("  THE TABLE (color?, T3L, T3R, Y, Q, B-L) : count  [own numbers]")
for k, v in sorted(mult.items(), key=lambda kv: (not kv[0][0], kv[0])):
    log(f"    colored={str(k[0]):5s} T3L={k[1]:>4s} T3R={k[2]:>4s} Y={k[3]:>5s} "
        f"Q={k[4]:>5s} B-L={k[5]:>5s}  x{v}")
assert len(mult) == 15, f"expected 15 distinct rows, got {len(mult)}"

Q_multiset = Counter(r["Q"] for r in rows)
log(f"\n  Q multiset: { {str(k): v for k, v in sorted(Q_multiset.items())} }")
assert Q_multiset == PHYS_TARGET, "Q multiset is NOT the physical target"
log("  CLAIM 1 CHECK: Q multiset EXACTLY matches the physical SM-generation-plus-exotics "
    "target {0:5, +-1:2, +-1/3:6, +-2/3:3} -- CONFIRMED")

# cross-check vs the physical multiplet ROLE assignment memo 24 makes (by (T3L,T3R,Y) shape)
QL_up = [r for r in rows if r["colored"] and r["T3L"] == sp.Rational(1, 2) and r["Y"] == sp.Rational(1, 6)]
QL_dn = [r for r in rows if r["colored"] and r["T3L"] == sp.Rational(-1, 2) and r["Y"] == sp.Rational(1, 6)]
Dexotic = [r for r in rows if r["colored"] and r["T3L"] == 0 and r["T3R"] == 0 and r["Y"] == sp.Rational(-1, 3)]
log(f"\n  role cross-check: Q_L up-type (T3L=1/2,Y=1/6) Q={ {str(r['Q']) for r in QL_up} } "
    f"x{len(QL_up)}")
log(f"                     Q_L down-type (T3L=-1/2,Y=1/6) Q={ {str(r['Q']) for r in QL_dn} } "
    f"x{len(QL_dn)}")
log(f"                     exotic D-quark (T3L=T3R=0,Y=-1/3) Q={ {str(r['Q']) for r in Dexotic} } "
    f"x{len(Dexotic)}")
assert len(QL_up) == 3 and all(r["Q"] == sp.Rational(2, 3) for r in QL_up)
assert len(QL_dn) == 3 and all(r["Q"] == sp.Rational(-1, 3) for r in QL_dn)
assert len(Dexotic) == 3 and all(r["Q"] == sp.Rational(-1, 3) for r in Dexotic)
log("  CONFIRMED: quark doublet Q_L (Y=1/6, Q=2/3 & -1/3 x3 each) and the exotic vector-like")
log("  D-quark (Y=-1/3, Q=-1/3 x3) land exactly as memo 24 §1 describes.")

leptons = [r for r in rows if not r["colored"]]
lepton_Q = Counter(r["Q"] for r in leptons)
ec = [r for r in leptons if r["T3L"] == 0 and r["Q"] == 1]
log(f"\n  lepton/Higgs nonet (9 color singlets) Q multiset: "
    f"{ {str(k): v for k, v in sorted(lepton_Q.items())} }")
assert sum(lepton_Q.values()) == 9
assert len(ec) >= 1, "expected at least one T3L=0, Q=+1 state (e^c)"
log(f"  CONFIRMED: 9 color singlets forming the T3L x T3R grid; a T3L=0,Q=+1 state present "
    f"(the e^c role memo 24 names) x{len(ec)}")

# ============================================== PART 6 -- the anomaly traces (own, exact)
log("\n" + "=" * 78)
log("PART 6: THE EIGHT ANOMALY TRACES (own, exact sympy Rational arithmetic)")


def tr(f):
    return sp.nsimplify(sum(f(r) for r in rows))


traces = {
    "Tr Y": tr(lambda r: r["Y"]),
    "Tr Y^3": tr(lambda r: r["Y"] ** 3),
    "Tr(T3L^2 Y)": tr(lambda r: r["T3L"] ** 2 * r["Y"]),
    "Tr Q": tr(lambda r: r["Q"]),
    "Tr Q^3": tr(lambda r: r["Q"] ** 3),
    "Tr(B-L)": tr(lambda r: r["BL"]),
    "Tr(B-L)^3": tr(lambda r: r["BL"] ** 3),
    "Tr(T3R^2 Y)": tr(lambda r: r["T3R"] ** 2 * r["Y"]),
}
for name, val in traces.items():
    log(f"    {name:14s} = {val}")
all_zero = all(v == 0 for v in traces.values())
assert all_zero, f"NOT all anomaly traces vanished: {traces}"
log("  CLAIM 2 CHECK: all eight traces = 0 exactly -- CONFIRMED")

# ================================================== PART 7 -- the honest negative: naive B-L
log("\n" + "=" * 78)
log("PART 7: THE NAIVE B-L = 2(Y - T3R) -- physicality check (the honest negative)")
BL_physical_set = {sp.Rational(1, 3), sp.Rational(-1, 3), sp.Rational(2, 3), sp.Rational(-2, 3)}
BL_physical_singlet_set = {sp.Rational(1), sp.Rational(-1), sp.Rational(0)}

colored_BL = Counter(r["BL"] for r in rows if r["colored"])
singlet_BL = Counter(r["BL"] for r in rows if not r["colored"])
log(f"  colored states' naive B-L multiset: { {str(k): v for k, v in sorted(colored_BL.items())} }")
log(f"  singlet states' naive B-L multiset: { {str(k): v for k, v in sorted(singlet_BL.items())} }")

colored_ok = all(bl in BL_physical_set for bl in colored_BL)
singlet_ok = all(bl in BL_physical_singlet_set for bl in singlet_BL)
bl_is_physical = colored_ok and singlet_ok
log(f"  naive B-L physical for ALL colored states (in {{+-1/3,+-2/3}})? {colored_ok}")
log(f"  naive B-L physical for ALL singlet states (in {{+-1,0}})? {singlet_ok}")

unphysical_colored = sorted({str(bl) for bl in colored_BL if bl not in BL_physical_set})
unphysical_singlet = sorted({str(bl) for bl in singlet_BL if bl not in BL_physical_singlet_set})
log(f"  unphysical colored B-L values found: {unphysical_colored}")
log(f"  unphysical singlet B-L values found: {unphysical_singlet}")

assert not bl_is_physical, "the naive B-L unexpectedly came out physical -- claim would be REFUTED"
assert set(unphysical_colored) == {"5/3", "-4/3"}, \
    f"expected exactly {{5/3,-4/3}} unphysical colored values, got {unphysical_colored}"
assert set(unphysical_singlet) == {"2", "-2"}, \
    f"expected exactly {{2,-2}} unphysical singlet values, got {unphysical_singlet}"
log("  CLAIM 3 CHECK: naive B-L is UNPHYSICAL, with colored states at EXACTLY {5/3,-4/3}")
log("  and singlets at EXACTLY {+-2} -- CONFIRMED (matches memo 24 section 3 verbatim)")

# ============================================== SUMMARY
log("\n" + "=" * 78)
log("BONUS: cross-check vs memo 23 (WEINBERG_POINT.md) -- sin^2 theta_W = Tr(T3L^2)/Tr(Q^2)")
trT3L2 = sp.nsimplify(sum(r["T3L"] ** 2 for r in rows))
trQ2 = sp.nsimplify(sum(r["Q"] ** 2 for r in rows))
s2w = sp.Rational(trT3L2, trQ2)
log(f"  Tr T3L^2 = {trT3L2}   Tr Q^2 = {trQ2}   sin^2 theta_W = {s2w}")
assert s2w == sp.Rational(3, 8), "sin^2 theta_W did not come out 3/8 on this own assignment"
log("  CONFIRMED: 3/8, matching memo 23's closing-independent symmetry-point value on")
log("  this independently-found physical assignment too.")

log("\n" + "=" * 78)
log("SUMMARY -- all three claims independently re-derived and CONFIRMED:")
log("  1. one SM generation + exotics table:  CONFIRMED")
log("  2. eight anomaly traces = 0 exactly:    CONFIRMED")
log("  3. naive B-L unphysical {5/3,-4/3,+-2}: CONFIRMED")
log("  bonus: sin^2 theta_W = 3/8 (memo 23):    CONFIRMED")
log("=" * 78)
