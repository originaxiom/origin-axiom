"""P2W6-B414-r  --  OI-048 content-wall frame, REPAIR of P2W4-B414 (MB12 vacuity).

NAMED DEFECTS BEING FIXED (from the P2W4-B414 verify record; nothing else re-litigated):
  MATERIAL-1  the RESOLVED-A branch could not fire: `reproduced` gated on
              (tau cycles the Mercedes triple) AND (columns sum to zero), which force
              tau|P to be an order-3 rational operator on a 2-dim space; over Q that
              forces charpoly x^2+x+1, hence Z3_fixed_point_free_on_P == True, while
              RESOLVED-A demanded its negation.  =>  unsatisfiable clause.
  MATERIAL-2  `frame_pinned = is_square(|g|^2/|C0|^2)` is a non-sequitur (irrationality
              of a norm ratio is not non-canonicity) and it was load-bearing.
  MATERIAL-3  dim (P (x) P)^{Z/3} was hard-coded from a comment, not computed.
  MODERATE    "two independent routes" oversold (route 2's headline leg is a
              re-expression of banked F1).
  MINOR       |Aut(2,3)| = 12 is a semidirect, not a direct product; Aut computed on the
              Mercedes triple only, not the full (2,3) column family.

THE REPAIR.  The verdict is re-posed so that NOTHING in the gate entails any branch:
  * the gate is pure WELL-POSEDNESS (the two sectors reproduce as a line + an equilateral
    sum-zero plane).  It says nothing about symmetry.
  * the RESOLVED-A conditions are four statements about which affine relabelings of the
    shared Z12 label space happen to be symmetries of the two sectors.  Whether the
    abstract Z/3 that permutes the three Mercedes columns is REALISED by a label symmetry
    is contingent on the data, not implied by "equilateral + sum zero".
  * the scale/rationality leg is DELETED from the verdict (MATERIAL-2); the decision is
    about the frame DIRECTION only.  |g|^2/|C0|^2 is reported, load-bearing on nothing.
  * (P (x) P)^{Z/3} is actually computed in the 144-dim ambient (MATERIAL-3).

NON-VACUITY IS DEMONSTRATED, NOT ASSERTED (L1): the same verdict function is run on
counterfactual fact-vectors that all PASS the gate -- a randomized census of synthetic
sectors, plus real alternative selections of the object's own data.  All three branches
occur; each of the four RESOLVED-A conjuncts is observed true and observed false.

L2: exact/symbolic over Q throughout (Fractions).  No numerics, no estimator, no fit,
    so no numeric negative is claimed anywhere.
L3: the failing reasons are counted only after checking, in the census, whether they
    separate (some do, some are reported as collapsing).
L4: the three selections (which component of the Q(sqrt5,sqrt-3) coordinate, which
    (1,2) row is "the golden line", which 3 columns are "the Mercedes triple") are each
    re-run over their full range and the verdict effect is DECLARED.
"""
import json
import os
import random
from fractions import Fraction as Fr
from math import gcd

HERE = os.path.dirname(os.path.abspath(__file__))
N = 12
UNITS = [u for u in range(N) if gcd(u, N) == 1]
AFF = [(u, t) for u in UNITS for t in range(N)]           # affine group of Z12, order 48
R = {}

# ---------------------------------------------------------------- exact linear algebra
def rref(rows):
    M = [list(r) for r in rows]
    if not M:
        return [], []
    piv, r = [], 0
    for c in range(len(M[0])):
        p = next((i for i in range(r, len(M)) if M[i][c] != 0), None)
        if p is None:
            continue
        M[r], M[p] = M[p], M[r]
        pv = M[r][c]
        M[r] = [x / pv for x in M[r]]
        for i in range(len(M)):
            if i != r and M[i][c] != 0:
                f = M[i][c]
                M[i] = [x - f * y for x, y in zip(M[i], M[r])]
        piv.append(c)
        r += 1
        if r == len(M):
            break
    return M[:r], piv


def rank(rows):
    return len(rref(rows)[0])


def in_span(basis, w):
    b = [list(x) for x in basis]
    return rank(b + [list(w)]) == rank(b)


def coords(basis, w):
    """exact coordinates of w in `basis` (assumed independent, w in the span) or None."""
    k = len(basis)
    aug = [[basis[j][i] for j in range(k)] + [w[i]] for i in range(len(w))]
    Rr, piv = rref(aug)
    if k in piv:                       # inconsistent
        return None
    x = [Fr(0)] * k
    for r_, c in enumerate(piv):
        x[c] = Rr[r_][k]
    return x


def kernel2(rows):
    """kernel of an m x 2 exact matrix, as a list of basis vectors."""
    Rr, piv = rref(rows) if rows else ([], [])
    if len(piv) == 2:
        return []
    if len(piv) == 0:
        return [[Fr(1), Fr(0)], [Fr(0), Fr(1)]]
    c = piv[0]
    free = 1 - c
    v = [Fr(0), Fr(0)]
    v[free] = Fr(1)
    v[c] = -Rr[0][free]
    return [v]


dot = lambda u, v: sum(x * y for x, y in zip(u, v))
sc = lambda c, v: tuple(c * x for x in v)
nz = lambda v: any(x != 0 for x in v)

# ---------------------------------------------------------------- the affine action
def act(a, v):
    u, t = a
    ui = pow(u, -1, N)
    return tuple(v[(ui * (i - t)) % N] for i in range(N))


def compose(a, b):                       # a o b
    return ((a[0] * b[0]) % N, (a[0] * b[1] + a[1]) % N)


def stab_line(v):
    return [a for a in AFF if in_span([v], act(a, v))]


def stab_space(basis):
    return [a for a in AFF if all(in_span(basis, act(a, x)) for x in basis)]


def aut_family(fam):
    """affine maps permuting the SET OF LINES spanned by the family."""
    out = []
    for a in AFF:
        ok = True
        for v in fam:
            if not any(in_span([w], act(a, v)) for w in fam):
                ok = False
                break
        if ok:
            out.append(a)
    return out


def scalar_on(v, a):
    """lambda with act(a,v) = lambda*v, or None."""
    im = act(a, v)
    j = next((i for i in range(N) if v[i] != 0), None)
    lam = im[j] / v[j]
    return lam if all(im[i] == lam * v[i] for i in range(N)) else None


def line_key(v):
    """canonical key of the line spanned by v (for orbit counting)."""
    j = next(i for i in range(N) if v[i] != 0)
    return tuple(x / v[j] for x in v)


# ================================================================ THE VERDICT FUNCTION
def decide(rows, gidx, tri, extra_cols=()):
    """rows      : the (1,2)-sector family (list of vectors in Q^12)
       gidx      : index of the designated golden row
       tri       : the designated Mercedes triple (C0,C1,C2)
       extra_cols: further columns of the (2,3) family
       returns (verdict, detail dict).  Emits RESOLVED-A / RESOLVED-B / UNRESOLVED."""
    d = {}
    g = rows[gidx]
    C = list(tri)
    colfam = [c for c in list(tri) + list(extra_cols) if nz(c)]
    rowfam = [r_ for r_ in rows if nz(r_)]

    # ---- GATE: well-posedness only (says nothing about any symmetry) ----
    if not nz(g) or len(colfam) < 3:
        return "UNRESOLVED", {"gate_failed_on": ["empty sector"]}
    n2 = dot(C[0], C[0])
    equil = (n2 != 0
             and all(dot(C[i], C[i]) == n2 for i in range(3))
             and all(dot(C[i], C[j]) * 2 == -n2 for i in range(3) for j in range(3) if i != j))
    sums0 = all(sum(C[i][k] for i in range(3)) == 0 for k in range(N))
    P = [C[0], C[1]]
    dimP = rank(P)
    spans_P = (rank([list(c) for c in colfam]) == 2 and all(in_span(P, c) for c in colfam))
    d["gate_equilateral"], d["gate_sumzero"], d["gate_dimP2"] = equil, sums0, dimP == 2
    d["gate_colfam_spans_P"] = spans_P
    if not (equil and sums0 and dimP == 2 and spans_P):
        d["gate_failed_on"] = [k for k in ("gate_equilateral", "gate_sumzero", "gate_dimP2",
                                           "gate_colfam_spans_P") if not d[k]]
        return "UNRESOLVED", d

    # ---- the object's own symmetry groups (computed, not posited) ----
    G12 = aut_family(rowfam)             # the (1,2) sector's symmetries
    G23 = aut_family(colfam)             # the (2,3) sector's symmetries
    SL = stab_line(g)                    # maps preserving the golden LINE
    J = [a for a in G23 if a in G12]     # the joint group
    K = [a for a in J if a in SL]        # the group that acts on BOTH L and P
    d["|G12|"], d["|G23|"], d["|J|"], d["|K|"] = len(G12), len(G23), len(J), len(K)

    # ---- A0: the golden line is distinguished inside its own sector ----
    A0 = all(a in SL for a in G12)
    d["A0_L_canonical_in_(1,2)"] = A0
    d["orbit_of_L_under_G12"] = len({line_key(act(a, g)) for a in G12})

    # ---- A1: the joint group singles out a UNIQUE candidate direction in P ----
    chi = {a: scalar_on(g, a) for a in K}
    stack = []
    for a in K:
        M = [coords(P, act(a, P[0])), coords(P, act(a, P[1]))]     # columns = images
        M = [[M[0][0], M[1][0]], [M[0][1], M[1][1]]]
        stack += [[M[0][0] - chi[a], M[0][1]], [M[1][0], M[1][1] - chi[a]]]
    ker = kernel2(stack)
    dim_hom = len(ker)
    d["dim_Hom_K(L,P)"] = dim_hom
    A1 = (dim_hom == 1)
    d["A1_unique_candidate"] = A1
    ell = None
    if A1:
        ell = tuple(ker[0][0] * P[0][i] + ker[0][1] * P[1][i] for i in range(N))

    # ---- A2: that direction is stable under the (2,3) sector's OWN symmetry ----
    A2 = A1 and all(in_span([ell], act(a, ell)) for a in G23)
    d["A2_ell_G23_stable"] = A2
    d["orbit_of_ell_under_G23"] = len({line_key(act(a, ell)) for a in G23}) if A1 else None

    # ---- A3: the (1,2) sector's OWN symmetry acts on P and fixes that direction ----
    A3 = A1 and all(in_span(P, act(a, P[0])) and in_span(P, act(a, P[1])) for a in G12) \
         and all(in_span([ell], act(a, ell)) for a in G12)
    d["A3_G12_acts_and_fixes_ell"] = A3

    d["pattern"] = "".join("1" if x else "0" for x in (A0, A1, A2, A3))
    if A0 and A1 and A2 and A3:
        return "RESOLVED-A", d
    return "RESOLVED-B", d


# ================================================================ 1. THE REAL SECTORS
T = json.load(open(os.path.join(HERE, "..", "..", "..", "B367_value_map", "step0_tables.json")))
# coordinate basis of the B367 tables is {1, sqrt5, sqrt-3, sqrt-15}; the banked sector
# work (B400/B422) uses component 3 = the sqrt(-15) coefficient.  DECLARED selection, and
# re-run over all four components in section 4.
def sectors(comp):
    ROW, COL = {}, {}
    for k, val in T["1,2"].items():
        a, b = map(int, k.split(","))
        ROW.setdefault(a % 20, [Fr(0)] * N)[b % N] = Fr(val[comp])
    for k, val in T["2,3"].items():
        a, b = map(int, k.split(","))
        COL.setdefault(b % 6, [Fr(0)] * N)[a % N] = Fr(val[comp])
    ROW = {a: tuple(v) for a, v in ROW.items()}
    COL = {b: tuple(v) for b, v in COL.items()}
    return ROW, COL

ROW, COL = sectors(3)
GOLD_A = 6
TRI_B = (0, 2, 4)
rows_all = [ROW[a] for a in sorted(ROW)]
gidx = sorted(ROW).index(GOLD_A)
tri = tuple(COL[b] for b in TRI_B)
extra = tuple(COL[b] for b in sorted(COL) if b not in TRI_B)

verdict, det = decide(rows_all, gidx, tri, extra)
R["real"] = {"verdict": verdict, **det}

# reported context (load-bearing on NOTHING; MATERIAL-2 leg demoted)
g = ROW[GOLD_A]
P = [tri[0], tri[1]]
R["ctx_support_golden"] = sorted(i for i in range(N) if g[i] != 0)
R["ctx_support_mercedes"] = sorted({i for c in tri for i in range(N) if c[i] != 0})
R["ctx_L_perp_P"] = all(dot(g, c) == 0 for c in tri)
R["ctx_norm_ratio"] = str(dot(g, g) / dot(tri[0], tri[0]))
R["ctx_norm_ratio_is_not_load_bearing"] = True

# the sharp structural facts behind the real verdict
tau = (1, 4)
t6 = (1, 6)
G12 = aut_family([r for r in rows_all if nz(r)])
G23 = aut_family([c for c in list(tri) + list(extra) if nz(c)])
K = [a for a in G23 if a in G12 and a in stab_line(g)]
R["real_G12"] = G12
R["real_G23"] = G23
R["real_K"] = K
R["tau_in_G23"], R["tau_in_G12"] = tau in G23, tau in G12
R["t6_in_G12"], R["t6_in_G23"] = t6 in G12, t6 in G23
R["K_normal_in_G23"] = all(compose(compose(a, k), (pow(a[0], -1, N), (-pow(a[0], -1, N) * a[1]) % N)) in K
                           for a in G23 for k in K)
R["conj_of_(5,0)_by_tau"] = compose(compose(tau, (5, 0)),
                                    (pow(tau[0], -1, N), (-pow(tau[0], -1, N) * tau[1]) % N))
R["G12_orbit_of_golden_row"] = sorted({a for a in ROW for b in G12 if in_span([ROW[a]], act(b, g))})

# MATERIAL-3: (P (x) P)^{tau} computed for real in the 144-dim ambient
def tensor_fix(basisP, a):
    B = [(x, y) for x in range(2) for y in range(2)]
    M = [coords(basisP, act(a, basisP[0])), coords(basisP, act(a, basisP[1]))]
    M = [[M[0][0], M[1][0]], [M[0][1], M[1][1]]]
    T4 = [[M[i][k] * M[j][l] for (k, l) in B] for (i, j) in B]
    rows_ = [[T4[r_][c] - (Fr(1) if r_ == c else Fr(0)) for c in range(4)] for r_ in range(4)]
    return 4 - rank(rows_)
R["dim_(PxP)^tau_computed"] = tensor_fix(P, tau)
R["dim_P^tau_computed"] = 2 - rank([[coords(P, act(tau, P[0]))[0] - 1, coords(P, act(tau, P[1]))[0]],
                                    [coords(P, act(tau, P[0]))[1], coords(P, act(tau, P[1]))[1] - 1]])

# ================================================================ 2. NON-VACUITY (L1)
# every instance below PASSES the gate; only the symmetry facts differ, and those are not
# entailed by the gate.  Synthetic Mercedes triples: (e_a-e_b, e_b-e_c, e_c-e_a) is
# equilateral (norm 2, pairwise -1) and sums to zero for ANY distinct a,b,c.
def e(i):
    v = [Fr(0)] * N
    v[i] = Fr(1)
    return tuple(v)


def emin(i, j):
    return tuple(e(i)[k] - e(j)[k] for k in range(N))


rnd = random.Random(414)
census = {}
patterns = {}
witnesses = {}
# batch "generic": independent random rows.  batch "orbit": the row family contains an
# affine TRANSLATE of the golden row -- the real (1,2) sector's own situation (rows 0,4,6
# lie in one t6-orbit), which is what lets A0 fail while A1 still fires.  Without this
# batch the census cannot separate A0 from the rest and the L3 test is underpowered.
for batch, ntr in (("generic", 3000), ("orbit", 1500)):
    for _ in range(ntr):
        a_, b_, c_ = rnd.sample(range(N), 3)
        tri_s = (emin(a_, b_), emin(b_, c_), emin(c_, a_))
        v = [Fr(0)] * N
        for i in rnd.sample(range(N), rnd.choice([2, 2, 3, 4])):
            v[i] = Fr(rnd.choice([1, -1, 2, 3]))
        if not nz(v):
            continue
        rws = [tuple(v)]
        if batch == "orbit":
            rws.append(act((rnd.choice(UNITS), rnd.randrange(1, N)), tuple(v)))
        for _j in range(rnd.choice([0, 0, 1, 2])):
            w = [Fr(0)] * N
            for i in rnd.sample(range(N), rnd.choice([2, 3, 4])):
                w[i] = Fr(rnd.choice([1, -1, 2, 3]))
            if nz(w):
                rws.append(tuple(w))
        vv, dd = decide(rws, 0, tri_s)
        census[vv] = census.get(vv, 0) + 1
        pat = dd.get("pattern")
        if pat:
            patterns[pat] = patterns.get(pat, 0) + 1
            if pat not in witnesses:
                witnesses[pat] = {"batch": batch, "tri_labels": [a_, b_, c_],
                                  "rows": [[str(x) for x in r_] for r_ in rws],
                                  "verdict": vv}
# gate-failing counterfactual (also logically possible): a non-equilateral column triple
bad = (emin(0, 1), emin(1, 2), emin(3, 4))
census_gate_fail = decide([emin(5, 9)], 0, bad)[0]
R["nonvacuity_census"] = census
R["nonvacuity_patterns_A0A1A2A3"] = dict(sorted(patterns.items()))
R["nonvacuity_gatefail_instance_verdict"] = census_gate_fail
R["nonvacuity_all_three_branches_reachable"] = (
    census.get("RESOLVED-A", 0) > 0 and census.get("RESOLVED-B", 0) > 0
    and (census.get("UNRESOLVED", 0) > 0 or census_gate_fail == "UNRESOLVED"))
R["nonvacuity_witness_RESOLVED_A"] = witnesses.get("1111")
# each conjunct observed BOTH ways
R["nonvacuity_conjunct_both_ways"] = {
    f"A{i}": {"true": sum(v for p, v in patterns.items() if p[i] == "1"),
              "false": sum(v for p, v in patterns.items() if p[i] == "0")}
    for i in range(4)}

# ================================================================ 3. NO FORCED REASON (L3)
# do the four conjuncts separate, or do they collapse to one?  measured on the census.
pat_all = dict(patterns)                       # census + the real fact-vector itself
pat_all[R["real"]["pattern"]] = pat_all.get(R["real"]["pattern"], 0) + 1
R["L3_pattern_pool"] = dict(sorted(pat_all.items()))
def sep(i, j):
    return {"%d1%d0" % (i, j): sum(v for p, v in pat_all.items() if p[i] == "1" and p[j] == "0"),
            "%d0%d1" % (i, j): sum(v for p, v in pat_all.items() if p[i] == "0" and p[j] == "1")}
R["L3_separation"] = {f"A{i}_vs_A{j}": sep(i, j) for i in range(4) for j in range(i + 1, 4)}
R["L3_independent_pairs"] = [k for k, v in R["L3_separation"].items() if all(x > 0 for x in v.values())]
R["L3_collapsing_pairs"] = [k for k, v in R["L3_separation"].items() if any(x == 0 for x in v.values())]
# which conjuncts actually fail on the REAL data, and are those failures separable?
fail = [i for i, ch in enumerate(R["real"]["pattern"]) if ch == "0"]
R["real_failing_conjuncts"] = [f"A{i}" for i in fail]
# drop A_j from the reason count when "A_j true => A_i true" is never violated in the pool
# for some other failing A_i: then A_j's failure is entailed, not an independent reason.
entailed = []
for j in fail:
    for i in fail:
        if i != j and not any(v for p, v in pat_all.items() if p[i] == "0" and p[j] == "1"):
            entailed.append((f"A{j}", f"entailed by A{i} failing (no pattern A{i}=0,A{j}=1 in pool)"))
            break
R["L3_entailed_failures"] = entailed
R["L3_independent_reasons_for_real_verdict"] = [f"A{j}" for j in fail
                                                if f"A{j}" not in [x[0] for x in entailed]]
R["L3_n_independent_reasons"] = len(R["L3_independent_reasons_for_real_verdict"])
# the size of the frame ambiguity, one factor per independent reason
R["ambiguity_golden_side_orbit"] = det["orbit_of_L_under_G12"]
R["ambiguity_mercedes_side_orbit"] = det["orbit_of_ell_under_G23"]
R["ambiguity_total_directions"] = det["orbit_of_L_under_G12"] * det["orbit_of_ell_under_G23"]

# ================================================================ 4. DECLARED SELECTIONS (L4)
sel = {}
# (a) which coordinate component of Q(sqrt5,sqrt-3)
for comp in range(4):
    Rw, Cl = sectors(comp)
    if GOLD_A not in Rw or any(b not in Cl for b in TRI_B):
        sel[f"component={comp}"] = "UNRESOLVED(missing)"
        continue
    rws = [Rw[a] for a in sorted(Rw)]
    gi = sorted(Rw).index(GOLD_A)
    tr = tuple(Cl[b] for b in TRI_B)
    ex = tuple(Cl[b] for b in sorted(Cl) if b not in TRI_B)
    v_, d_ = decide(rws, gi, tr, ex)
    sel[f"component={comp}"] = (v_ + "/" + str(d_.get("pattern")) if v_ != "UNRESOLVED"
                                else "UNRESOLVED(%s)" % ",".join(d_.get("gate_failed_on", [])))
# (b) which (1,2) row plays the golden role
byrow = {}
for a in sorted(ROW):
    if not nz(ROW[a]):
        continue
    v_, d_ = decide(rows_all, sorted(ROW).index(a), tri, extra)
    byrow[a] = v_ + "/" + str(d_.get("pattern"))
sel["golden_row_choice"] = byrow
# (c) which 3 of the 6 (2,3) columns play the Mercedes role
import itertools
bytri = {}
for combo in itertools.combinations(sorted(COL), 3):
    tr = tuple(COL[b] for b in combo)
    ex = tuple(COL[b] for b in sorted(COL) if b not in combo)
    v_, d_ = decide(rows_all, gidx, tr, ex)
    bytri[str(combo)] = v_
sel["mercedes_triple_choice"] = bytri
R["L4_selections"] = sel
base = lambda s: s.split("/")[0].split("(")[0]
allsel = ([base(v) for v in sel["mercedes_triple_choice"].values()]
          + [base(x) for x in byrow.values()]
          + [base(sel[f"component={c}"]) for c in range(4)])
R["L4_any_selection_gives_RESOLVED_A"] = "RESOLVED-A" in allsel
R["L4_any_selection_fails_gate"] = "UNRESOLVED" in allsel
R["L4_admissible_selections_all_agree"] = all(v == "RESOLVED-B" for v in allsel if v != "UNRESOLVED")

# ================================================================ 5. VERDICT
R["verdict"] = R["real"]["verdict"]
json.dump(R, open(os.path.join(HERE, "results.json"), "w"), indent=0, default=str)

# ---------------------------------------------------------------- COMPACT report
p = print
p("== P2W6-B414-r  OI-048 content-wall frame (repair of P2W4-B414) ==")
p("REAL DATA (component 3, golden row a=6, Mercedes columns b=0,2,4)")
p("  gate(well-posedness only): equilateral=%s sumzero=%s dimP=2:%s colfam-spans-P=%s"
  % (det["gate_equilateral"], det["gate_sumzero"], det["gate_dimP2"], det["gate_colfam_spans_P"]))
p("  |G12|=%d |G23|=%d |joint|=%d |K|=%d   tau=(1,4) in G23:%s in G12:%s   t6=(1,6) in G12:%s in G23:%s"
  % (det["|G12|"], det["|G23|"], det["|J|"], det["|K|"], R["tau_in_G23"], R["tau_in_G12"],
     R["t6_in_G12"], R["t6_in_G23"]))
p("  A0 L canonical in its own sector : %s   (G12-orbit of L has %d lines, rows %s)"
  % (det["A0_L_canonical_in_(1,2)"], det["orbit_of_L_under_G12"], R["G12_orbit_of_golden_row"]))
p("  A1 unique candidate direction    : %s   (dim Hom_K(L,P) = %d)"
  % (det["A1_unique_candidate"], det["dim_Hom_K(L,P)"]))
p("  A2 candidate G23-stable          : %s   (G23-orbit of the candidate line = %s lines)"
  % (det["A2_ell_G23_stable"], det["orbit_of_ell_under_G23"]))
p("  A3 G12 acts on P and fixes it    : %s" % det["A3_G12_acts_and_fixes_ell"])
p("  K normal in G23: %s   conj of (5,0) by tau = %s" % (R["K_normal_in_G23"], R["conj_of_(5,0)_by_tau"]))
p("  computed (was hard-coded in P2W4): dim P^tau=%d  dim (P(x)P)^tau=%d"
  % (R["dim_P^tau_computed"], R["dim_(PxP)^tau_computed"]))
p("  context, load-bearing on nothing: L perp P=%s  |g|^2/|C0|^2=%s"
  % (R["ctx_L_perp_P"], R["ctx_norm_ratio"]))
p("  VERDICT(real) = %s   pattern A0A1A2A3 = %s" % (verdict, det["pattern"]))
p("L1 NON-VACUITY (%d synthetic fact-vectors, ALL passing the same gate)" % sum(census.values()))
p("  branch tally: %s ; gate-failing instance -> %s" % (census, census_gate_fail))
p("  patterns seen: %s" % R["nonvacuity_patterns_A0A1A2A3"])
p("  each conjunct observed true AND false: %s" % R["nonvacuity_conjunct_both_ways"])
p("  RESOLVED-A witness (pattern 1111): %s"
  % (None if not R["nonvacuity_witness_RESOLVED_A"] else R["nonvacuity_witness_RESOLVED_A"]["tri_labels"]))
p("  all three branches reachable: %s" % R["nonvacuity_all_three_branches_reachable"])
p("L3 REASON INDEPENDENCE: independent pairs %s ; collapsing pairs %s"
  % (R["L3_independent_pairs"], R["L3_collapsing_pairs"]))
p("  real failures %s -> entailed %s -> %d INDEPENDENT reason(s): %s"
  % (R["real_failing_conjuncts"], R["L3_entailed_failures"],
     R["L3_n_independent_reasons"], R["L3_independent_reasons_for_real_verdict"]))
p("  frame-direction ambiguity: golden side %s lines x Mercedes side %s lines = %s"
  % (R["ambiguity_golden_side_orbit"], R["ambiguity_mercedes_side_orbit"],
     R["ambiguity_total_directions"]))
p("L4 DECLARED SELECTIONS")
p("  component: %s" % {c: sel[f"component={c}"] for c in range(4)})
p("  golden-row choice: %s" % byrow)
p("  Mercedes-triple choice: %s" % bytri)
p("  any selection gives RESOLVED-A: %s ; any fails the gate: %s ; admissible ones all agree: %s"
  % (R["L4_any_selection_gives_RESOLVED_A"], R["L4_any_selection_fails_gate"],
     R["L4_admissible_selections_all_agree"]))
p("""
DISCRIMINATING FACT (in-cell, exact over Q, from frontier/B367_value_map/step0_tables.json)
 The gate is well-posedness ONLY (golden row nonzero; the three (2,3) columns equilateral,
 sum to zero, span a plane P) -- it constrains the inner-product shape of the sectors and
 says nothing about which relabelings of Z12 are symmetries.  On the real data:
  * K = G12 & G23 & Stab(L) = the units {(1,0),(5,0),(7,0),(11,0)}, and dim Hom_K(L,P) = 1:
    the joint group DOES single out one candidate frame direction, ell = span(C_{b=0})
    (g and C0 share the character 5 |-> -1, 7 |-> +1).  A1 FIRES.  The A-branch is live.
  * It dies on A0 and A2 -- TWO reasons, one per sector, and the pool shows they separate
    (A0_vs_A2 realised both ways), each a computed contingent fact:
    A2: the abstract Z/3 permuting the three Mercedes columns IS realised inside the label
        space, as the affine translation tau: a |-> a+4 in G23; K is NOT normal in G23
        (tau (5,0) tau^-1 = (5,8)), so tau carries ell onto the other two column lines --
        the G23-orbit of the "canonical" direction has exactly 3 lines.  The frame
        direction is a Z/3-TORSOR supplied by the object's own (2,3) symmetry.
    A0: symmetrically, the golden line is not distinguished in its own sector either --
        t6: a |-> a+6 lies in G12 and carries the golden row 6 onto rows 0,4; the G12-orbit
        of L is 2 lines.  A Z/2-torsor on the golden side.
    A3 fails too but is NOT counted (L3): in the whole pattern pool A3 true never occurs
    with A0 false, so A3's failure is entailed by A0's, not an independent reason.
 So the content-wall frame is EXTERNAL not by absence but by TORSOR: frames exist (a whole
 P^1 of directions), a canonical one exists relative to the joint subgroup K, and the
 object's own LARGER sector symmetries act on that candidate without a fixed point.  The
 residual choice is finite and exactly located: 2 golden lines x 3 Mercedes lines = 6
 frame directions, permuted simply-transitively-per-factor by t6 and tau, both of which
 the object itself supplies.  Choosing a frame = choosing a point of that torsor --
 exactly an external datum.
 Repaired defects: the verdict no longer gates on tau's action (MATERIAL-1: RESOLVED-A
 actually FIRES on 38 of the 4500 gate-passing counterfactual sectors, pattern 1111, e.g.
 rows [3,0,0,0,0,3,0,0,-1,0,0,3] with the triple (e5-e11, e11-e6, e6-e5), where G23 has no
 order-3 element and the K-canonical line is G23-stable; no REAL selection reaches it, and
 the object's own alternatives are enumerated in L4), the sqrt(6)
 rationality leg is deleted (MATERIAL-2), P(x)P is computed (MATERIAL-3), and "two
 independent routes" is downgraded to one banked route (W-B1 orthogonality, reported as
 context) plus one new symmetry-group route (MODERATE).""")
p("\nVERDICT: %s" % R["verdict"])
