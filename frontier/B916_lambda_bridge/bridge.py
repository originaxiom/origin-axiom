#!/usr/bin/env python3
"""B916 -- THE LAMBDA BRIDGE: is 2304/953 vs 1 a realization convention?

Two seats computed "the same" colorless coupling invariant
    lambda = |c| / sqrt(|h_i h_j h_k|)
on the nine colorless atom lines and got different constants:
  cc   (B914, banked, B883 27):      lambda = 1 EXACTLY
  solo (handoff 7, their 27bar rep): lambda = 2304/953 (85-digit belt)

This cell builds the explicit realization bridge and decides where the
factor lives.

PHASE A (exact, Q): the intertwiner S with
      rho_handoff(x_k) = - S rho_B883(x_k)^T S^{-1}   (all 78 generators)
  solved as a linear system (Schur: unique up to scale), then the handoff
  cubic and H are transported through S and compared entry-by-entry with
  the banked B883 cubic (B914) and H+ (B912):  c' = t*cub_B883,
  H' = s*H_B883.  The scale-covariant bridge constant |t|/|s|^{3/2} is
  computed exactly and compared with 2304/953.

  EARLY STRUCTURAL FACT (checked here): BOTH reps have all entries in
  {-1,0,+1}, so every two-term intertwiner equation forces x-ratios of
  +-1 and the primitive S is a SIGNED PERMUTATION.  Then |t| = |s| = 1
  and the bridge factor is 1, NOT 2304/953 -- i.e. "primitive +-1 in its
  own basis" is NOT basis-dependent between these two realizations; the
  factor must live elsewhere.  Phase B/C locate it.

PHASE B (numeric, dps 60-80): lambda_handoff recomputed INDEPENDENTLY
  from the handoff files in their own realization (their rep -> charge
  matrices -> eigen-atoms -> their cubic + their H convention); the
  handoff atom lines transported back through S^{-1} and identified
  against H_B883 * (banked exact atoms) -- the left-eigenline twist.

PHASE C (exact, Mbar): the B914 exact atom machinery is re-run (same
  tower K -> N -> Mbar), the DUAL atom lines v_i = H u_i are formed
  exactly, and both lambdas are computed exactly on them.

WHAT THE COMPUTATION FOUND (all exact unless noted):
  * S is a signed permutation, unique up to scale; det S = 1.
  * the primitive cubic transports IDENTICALLY: t = 1.  "primitive +-1
    in its own basis" IS canonical across the mirror.
  * the H's do NOT transport into each other: H'(solo) = H+(B912) *
    diag(D2), D2 = +-1 with 11 flips; no scalar s exists.  The solo M
    is the tau-twisted dual intertwiner M = P D_chi with
    P rho(tau X) = -rho(X)^T P (Cartan permutation (5,1,4,3,2,0)),
    NOT charge-equivariant (verified: no sign works for any charge).
  * lambda with the banked H+ is 1 EXACTLY on the primal nine AND on
    the mirror nine: the canonical lambda is realization-independent.
  * lambda with the solo H' is 2304/953 EXACTLY on the mirror nine AND
    on the primal nine: the tau-twisted lambda is ALSO
    realization-independent, and the solo 85-digit belt is exactified.
  * the factor lives in the per-line norm ratios d_i = q^{H'}/q^{H+}:
    each d_i is a K-cubic irrationality with minimal polynomial of
    shape 2304^2 x^3 + ... +- 953^2 (A-family linear coefficient even
    equals -2304*953); every coupling triple is a Galois norm:
    prod d_i = -(953/2304)^2 = N_{K/Q}(d).  953 is the norm-arithmetic
    of the H-twist, not a normalization.

Env: HANDOFF7 = dir containing the solo seat's rep27.pkl, H27.pkl,
cubic27.json (required).  SESSION_SCRATCH optional (cache + isolated-exec
cwd for e6_centralizer.py).  Repo paths relative to this file.
Output: results.json.  Exact arithmetic for every verdict-bearing claim.
"""
import io, os, json, math, time, pickle, tempfile, contextlib, itertools
from fractions import Fraction as Fr
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.normpath(os.path.join(HERE, "..", ".."))
SCRATCH = os.environ.get("SESSION_SCRATCH") or tempfile.mkdtemp(prefix="b916_")
os.makedirs(SCRATCH, exist_ok=True)
HANDOFF7 = os.environ.get("HANDOFF7")
if not HANDOFF7 or not os.path.isdir(HANDOFF7):
    raise SystemExit("HANDOFF7 env var must point at the handoff-7 scripts dir "
                     "(rep27.pkl, H27.pkl, cubic27.json)")
T00 = time.time()
RES = {"cell": "B916 lambda bridge", "checks": {}, "notes": []}


def log(*a):
    print(f"[{time.time()-T00:7.1f}s]", *a, flush=True)


def CHK(name, ok, detail=""):
    RES["checks"][name] = {"pass": bool(ok), "detail": str(detail)}
    log(f"  [{'PASS' if ok else 'FAIL'}] {name} {detail}")
    if not ok:
        RES["verdict"] = "UNSTABLE"
        json.dump(RES, open(os.path.join(HERE, "results.json"), "w"), indent=1)
        raise SystemExit(f"UNSTABLE at {name}")


def REC(name, value, detail=""):
    """verdict-bearing comparison recorded as data (never aborts)."""
    RES["checks"][name] = {"value": value, "detail": str(detail)}
    log(f"  [DATA] {name} = {value} {detail}")


# ================================================================ [A1] inputs
log("[A1] load B883 rep (banked) + handoff rep/H/cubic ...")
REPJ = json.load(open(os.path.join(REPO, "frontier", "B883_the_27", "rep27.json")))
REP_B = [[[int(x) for x in row] for row in REPJ["rep"][str(k)]] for k in range(78)]
WT_B = [tuple(REP_B[i][a][a] for i in range(6)) for a in range(27)]
CHK("B883_cartan_diagonal_27_distinct_weights",
    all(all(REP_B[i][a][b] == 0 for a in range(27) for b in range(27) if a != b)
        for i in range(6)) and len(set(WT_B)) == 27)

DH = pickle.load(open(os.path.join(HANDOFF7, "rep27.pkl"), "rb"))
REP_H = [[[Fr(x) for x in row] for row in M] for M in DH["REP"]]
CHK("handoff_rep_78_generators", len(REP_H) == 78, f"variant {DH.get('variant')}")
WT_H = [tuple(REP_H[i][a][a] for i in range(6)) for a in range(27)]
CHK("handoff_cartan_diagonal_27_distinct_weights",
    all(all(REP_H[i][a][b] == 0 for a in range(27) for b in range(27) if a != b)
        for i in range(6)) and len(set(WT_H)) == 27)
CHK("weight_multisets_are_exact_negatives_27bar",
    sorted(WT_H) == sorted(tuple(-x for x in w) for w in WT_B),
    "re-verifies the B914/B912 mirror fact")

entsB = set(); entsH = set()
for k in range(78):
    for a in range(27):
        for b in range(27):
            if REP_B[k][a][b]:
                entsB.add(Fr(REP_B[k][a][b]))
            if REP_H[k][a][b]:
                entsH.add(REP_H[k][a][b])
CHK("both_reps_all_entries_pm1",
    entsB <= {Fr(1), Fr(-1)} and entsH <= {Fr(1), Fr(-1)},
    "=> every intertwiner ratio equation is +-1 => primitive S is a signed permutation")

MH_raw = pickle.load(open(os.path.join(HANDOFF7, "H27.pkl"), "rb"))
Mh = [[Fr(x) for x in row] for row in MH_raw["M"]]
CHK("handoff_H_symmetric_signed_permutation",
    all(Mh[i][j] == Mh[j][i] for i in range(27) for j in range(27))
    and sorted(j for i in range(27) for j in range(27) if Mh[i][j]) == list(range(27))
    and all(abs(Mh[i][j]) == 1 for i in range(27) for j in range(27) if Mh[i][j]))

CBH = json.load(open(os.path.join(HANDOFF7, "cubic27.json")))
TRIP_H = [tuple(t) for t in CBH["triples"]]
COEF_H = [int(Fr(c)) for c in CBH["coeffs"]]
CHK("handoff_cubic_45_triples_pm1_28_17",
    len(TRIP_H) == 45 and all(a < b < c for a, b, c in TRIP_H)
    and Counter(COEF_H) == Counter({1: 28, -1: 17}))
CHK("handoff_cubic_support_weight_zero",
    all(all(WT_H[a][i] + WT_H[b][i] + WT_H[c][i] == 0 for i in range(6))
        for a, b, c in TRIP_H))

B914 = json.load(open(os.path.join(REPO, "frontier", "B914_ratio_table",
                                   "results.json")))
TRIP_C = [tuple(t) for t in B914["cubic_B883"]["triples"]]
COEF_C = [int(c) for c in B914["cubic_B883"]["coeffs"]]
CHK("B883_cubic_45_triples_pm1",
    len(TRIP_C) == 45 and all(a < b < c for a, b, c in TRIP_C)
    and all(abs(c) == 1 for c in COEF_C),
    f"split {Counter(COEF_C)}")
B912 = json.load(open(os.path.join(REPO, "frontier", "B912_norm_cell",
                                   "results.json")))
piW = B912["H_plus_support_pi"]
cbP = B912["H_plus_entries_c_b"]
cbM = B912["H_minus_entries_c_b"]
Dd = B912["D_diag"]

# ---------------------------------------------------------------- sparse forms
nzH = [[[(j, M[i][j]) for j in range(27) if M[i][j]] for i in range(27)]
       for M in REP_H]
nzB = [[[(j, M[i][j]) for j in range(27) if M[i][j]] for i in range(27)]
       for M in REP_B]

# ---------------------------------------------------------------- B854 invariants
# (cached; isolated exec with scratch cwd -- house rule)
cache = os.path.join(SCRATCH, "b914_base_cache.pkl")
if os.path.exists(cache):
    INV, ns = pickle.load(open(cache, "rb"))
else:
    cwd = os.getcwd()
    g6 = {"__file__": os.path.join(SCRATCH, "e6_centralizer.py"),
          "__name__": "b854_frame"}
    src = open(os.path.join(REPO, "frontier", "B854_centralizer_exact",
                            "e6_centralizer.py")).read()
    try:
        os.chdir(SCRATCH)
        with contextlib.redirect_stdout(io.StringIO()):
            exec(compile(src, "b854", "exec"), g6)
    finally:
        os.chdir(cwd)
    ns = g6["ns"]
    INV = {n: [Fr(c.numerator, c.denominator) for c in g6["INV"][n]] for n in ns}
    pickle.dump((INV, ns), open(cache, "wb"))
CHK("base_ns_8_14_16_22", sorted(ns) == [8, 14, 16, 22])
INV_EARLY = INV

# ================================================================ [A2] solve S
log("[A2] the intertwiner S: rho_h(x) S + S rho_B(x)^T = 0 ...")
negW = {tuple(-x for x in WT_B[b]): b for b in range(27)}
pB2H = [None] * 27            # B883 index b -> handoff index a with W_H[a] = -W_B[b]
for a in range(27):
    b = negW.get(WT_H[a])
    assert b is not None
    pB2H[b] = a
H2B = [None] * 27
for b in range(27):
    H2B[pB2H[b]] = b
CHK("weight_matching_permutation_bijective",
    sorted(pB2H) == list(range(27)) and pB2H != list(range(27)),
    "nontrivial permutation")

# two-term equations: for generator k, entry (a,b):
#   REP_H[k][a][pB2H[b]] * x_b  +  REP_B[k][b][H2B[a]] * x_{H2B[a]}  =  0
eqs = set()
for k in range(6, 78):
    for a in range(27):
        for (ap, v) in nzH[k][a]:
            eqs.add((k, a, H2B[ap]))          # column b with pB2H[b] = ap
    for b in range(27):
        for (c, v) in nzB[k][b]:
            eqs.add((k, pB2H[c], b))
eqlist = []
for (k, a, b) in eqs:
    c1 = REP_H[k][a][pB2H[b]]
    c2 = Fr(REP_B[k][b][H2B[a]])
    eqlist.append((b, H2B[a], c1, c2))        # c1*x_b + c2*x_{b2} = 0
CHK("no_single_sided_equations_would_force_zero",
    all((c1 != 0) == (c2 != 0) or (c1 != 0 and c2 != 0) for b, b2, c1, c2 in eqlist)
    and all(not ((c1 != 0) ^ (c2 != 0)) for b, b2, c1, c2 in eqlist),
    f"{len(eqlist)} two-term equations")

xv = [None] * 27
xv[0] = Fr(1)
changed = True
while changed:
    changed = False
    for b, b2, c1, c2 in eqlist:
        if xv[b] is not None and xv[b2] is None:
            xv[b2] = -c1 * xv[b] / c2
            changed = True
        elif xv[b2] is not None and xv[b] is None:
            xv[b] = -c2 * xv[b2] / c1
            changed = True
CHK("propagation_graph_connected_schur_unique_up_to_scale",
    all(v is not None for v in xv),
    "the two-term system alone pins S up to one overall scale")
CHK("propagation_consistent_all_equations",
    all(c1 * xv[b] + c2 * xv[b2] == 0 for b, b2, c1, c2 in eqlist))

L = 1
for v in xv:
    L = L * v.denominator // math.gcd(L, v.denominator)
xi = [v * L for v in xv]
g = 0
for v in xi:
    g = math.gcd(g, abs(v.numerator))
xi = [v / g for v in xi]
if xi[0] < 0:
    xi = [-v for v in xi]
CHK("primitive_S_is_signed_permutation_all_x_pm1",
    all(abs(v) == 1 for v in xi), f"x values {sorted(set(xi))}")
X = [int(v) for v in xi]                      # S[pB2H[b]][b] = X[b]
RES["S_permutation_pB2H"] = pB2H
RES["S_signs_X"] = X

# full exact verification, ALL 78 generators
ok = True
for k in range(78):
    bad = []
    for a in range(27):
        for b in range(27):
            v = REP_H[k][a][pB2H[b]] * X[b] + REP_B[k][b][H2B[a]] * X[H2B[a]]
            if v != 0:
                ok = False
CHK("intertwiner_identity_all_78_generators_EXACT", ok,
    "rho_h(x) = -S rho_B(x)^T S^{-1} verified entrywise")
# det S = sign(perm) * prod X
sgn = 1
seen = [False] * 27
for b in range(27):
    if not seen[b]:
        l = 0; j = b
        while not seen[j]:
            seen[j] = True; j = pB2H[j]; l += 1
        if l % 2 == 0:
            sgn = -sgn
detS = sgn
for v in X:
    detS *= v
RES["det_S"] = detS
CHK("det_S_pm1_no_953_anywhere_in_S", abs(detS) == 1, f"det S = {detS}")

# ================================================================ [A3] cubics verified
log("[A3] exact invariance of BOTH cubics in their own realizations ...")


def full_sym(triples, coeffs):
    T3 = {}
    for t, cf in zip(triples, coeffs):
        for perm in set(itertools.permutations(t)):
            T3[perm] = Fr(cf)
    return T3


def cubic_invariant_all78(T3, nz):
    for k in range(78):
        rownz = nz[k]
        acc = {}
        for (x, y, z), v in T3.items():
            for (i, w) in rownz[x]:
                acc[(i, y, z)] = acc.get((i, y, z), Fr(0)) + w * v
            for (i, w) in rownz[y]:
                acc[(x, i, z)] = acc.get((x, i, z), Fr(0)) + w * v
            for (i, w) in rownz[z]:
                acc[(x, y, i)] = acc.get((x, y, i), Fr(0)) + w * v
        if any(v != 0 for v in acc.values()):
            return False
    return True


# nz by ROW index for the derivation contraction: entry (l -> i) means
# generator maps e_l component into e_i; the B914 loop used rownz[l] = row l.
nzrowH = [[[(i, REP_H[k][l][i]) for i in range(27) if REP_H[k][l][i]]
           for l in range(27)] for k in range(78)]
nzrowB = [[[(i, Fr(REP_B[k][l][i])) for i in range(27) if REP_B[k][l][i]]
           for l in range(27)] for k in range(78)]
T3H = full_sym(TRIP_H, COEF_H)
T3C = full_sym(TRIP_C, COEF_C)
CHK("handoff_cubic_exact_derivation_identity_all_78", cubic_invariant_all78(T3H, nzrowH))
CHK("B883_cubic_exact_derivation_identity_all_78", cubic_invariant_all78(T3C, nzrowB))


def qkernel(M):
    m, n = len(M), len(M[0])
    A = [row[:] for row in M]
    piv = []; rr = 0
    for c in range(n):
        pr = next((r for r in range(rr, m) if A[r][c] != 0), None)
        if pr is None:
            continue
        A[rr], A[pr] = A[pr], A[rr]
        iv = A[rr][c]
        A[rr] = [e / iv for e in A[rr]]
        for r in range(m):
            if r != rr and A[r][c]:
                f = A[r][c]
                A[r] = [A[r][j] - f * A[rr][j] for j in range(n)]
        piv.append(c); rr += 1
    ker = []
    for fc in [c for c in range(n) if c not in piv]:
        v = [Fr(0)] * n
        v[fc] = Fr(1)
        for i, c in enumerate(piv):
            v[c] = -A[i][fc]
        ker.append(v)
    return ker


# uniqueness of the handoff cubic in ITS OWN realization (kernel dim 1)
wzH = [t for t in itertools.combinations_with_replacement(range(27), 3)
       if all(WT_H[t[0]][i] + WT_H[t[1]][i] + WT_H[t[2]][i] == 0 for i in range(6))]
CHK("handoff_weight_zero_triples_45", len(wzH) == 45 and set(wzH) == set(TRIP_H))
tidxH = {t: i for i, t in enumerate(wzH)}
rows_eq = {}
for k in range(78):
    rownz = nzrowH[k]
    for t in wzH:
        for perm in set(itertools.permutations(t)):
            x, y, z = perm
            for (i, v) in rownz[x]:
                key = (k, tuple(sorted((i, y, z))))
                rows_eq.setdefault(key, [Fr(0)] * 45)[tidxH[t]] += v
            for (i, v) in rownz[y]:
                key = (k, tuple(sorted((x, i, z))))
                rows_eq.setdefault(key, [Fr(0)] * 45)[tidxH[t]] += v
            for (i, v) in rownz[z]:
                key = (k, tuple(sorted((x, y, i))))
                rows_eq.setdefault(key, [Fr(0)] * 45)[tidxH[t]] += v
eqm = [r for r in rows_eq.values() if any(r)]
kerH = qkernel(eqm)
CHK("handoff_cubic_kernel_dim_1_their_cubic_is_THE_cubic", len(kerH) == 1)
kv = kerH[0]
r0 = next((Fr(COEF_H[TRIP_H.index(t)]) / kv[tidxH[t]] for t in TRIP_H
           if kv[tidxH[t]] != 0), None)
CHK("handoff_cubic_spans_the_kernel",
    r0 is not None and all(Fr(COEF_H[TRIP_H.index(t)]) == r0 * kv[tidxH[t]]
                           for t in TRIP_H))

# ================================================================ [A4] transport cubic
log("[A4] transport the handoff cubic through S: c'(u,v,w) = c_h(Su,Sv,Sw) ...")
image_supp = {tuple(sorted((pB2H[a], pB2H[b], pB2H[c]))) for a, b, c in TRIP_C}
CHK("cubic_supports_correspond_under_S", image_supp == set(TRIP_H))
coefH_by_trip = {t: c for t, c in zip(TRIP_H, COEF_H)}
coefC_by_trip = {t: c for t, c in zip(TRIP_C, COEF_C)}
cprime = {}
for (a, b, c) in TRIP_C:
    th = tuple(sorted((pB2H[a], pB2H[b], pB2H[c])))
    cprime[(a, b, c)] = coefH_by_trip[th] * X[a] * X[b] * X[c]
ratios = [Fr(cprime[t], coefC_by_trip[t]) for t in TRIP_C]
prop_cubic = len(set(ratios)) == 1
if prop_cubic:
    t_scalar = ratios[0]
    REC("cubic_transport_proportional_t", str(t_scalar),
        "c' = t * cub_B883 entry-by-entry on all 45 triples")
else:
    t_scalar = None
    REC("cubic_transport_proportional_t", None,
        f"NOT proportional: ratio distribution {Counter(str(r) for r in ratios)}")
RES["cubic_transport"] = {
    "proportional": prop_cubic,
    "t": str(t_scalar) if prop_cubic else None,
    "ratio_distribution": {str(k): v for k, v in
                           Counter(str(r) for r in ratios).items()},
    "abs_t_forced": str(abs(ratios[0])) if len(set(map(abs, ratios))) == 1 else None,
    "cprime_coeffs_pm1": all(abs(v) == 1 for v in cprime.values()),
}
CHK("transported_cubic_has_pm1_coefficients",
    all(abs(v) == 1 for v in cprime.values()),
    "|t| would be 1 whenever proportionality holds")

# ================================================================ [A5] transport H
log("[A5] transport the handoff H through S: H' = S^T M_h S ...")
# H'[a][b] = X[a] X[b] Mh[pB2H[a]][pB2H[b]]
Hp = [[X[a] * X[b] * Mh[pB2H[a]][pB2H[b]] for b in range(27)] for a in range(27)]
CHK("H_transport_support_equals_H_plus_support",
    all((Hp[a][b] != 0) == (piW[b] == a) for a in range(27) for b in range(27)),
    "H' lives on the SAME signed-permutation support pi as the banked H+")
res_H = {"support_matches_H_plus": True}
s_scalar = None
sr = {Fr(Hp[piW[b]][b], cbP[b]) for b in range(27)}
srm = {Fr(Hp[piW[b]][b], cbM[b]) for b in range(27)}
if len(sr) == 1:
    s_scalar = sr.pop()
    res_H["proportional_to"] = "H_plus"
    res_H["s"] = str(s_scalar)
elif len(srm) == 1:
    s_scalar = srm.pop()
    res_H["proportional_to"] = "H_minus"
    res_H["s"] = str(s_scalar)
else:
    res_H["proportional_to"] = None
    res_H["ratio_distribution_vs_H_plus"] = {
        str(k): v for k, v in
        Counter(str(Fr(Hp[piW[b]][b], cbP[b])) for b in range(27)).items()}
RES["H_transport"] = res_H
REC("H_transport_proportional_s",
    str(s_scalar) if s_scalar is not None else None,
    f"target {res_H.get('proportional_to')}")

# the diagonal discrepancy: H' = H+ * D2, D2 diagonal +-1
D2 = [int(Fr(Hp[piW[b]][b], cbP[b])) for b in range(27)]
CHK("H_prime_equals_H_plus_times_diag_pm1",
    all(abs(d) == 1 for d in D2)
    and all(D2[piW[b]] == D2[b] for b in range(27))
    and all(Hp[piW[b]][b] == cbP[b] * D2[b] for b in range(27)),
    f"D2 signs: {Counter(D2)} (pi-symmetric, consistent with H' symmetric)")
RES["H_prime_diag_vs_H_plus"] = {
    "D2": D2,
    "flip_count": D2.count(-1),
    "flipped_coordinates_weights": [list(WT_B[b]) for b in range(27) if D2[b] == -1],
    "same_as_B912_D_diag": D2 == list(Dd)}

# is the handoff H charge-equivariant in ITS OWN realization?  (both signs)
RnHex = {}
for n in ns:
    M = [[Fr(0)] * 27 for _ in range(27)]
    for k, c in enumerate(INV_EARLY[n]):
        if c:
            Rk = REP_H[k]
            for a in range(27):
                for b in range(27):
                    if Rk[a][b]:
                        M[a][b] += c * Rk[a][b]
    RnHex[n] = M


def eqv_sign(R, M, eps):
    for a in range(27):
        for b in range(27):
            v = (sum(R[c][a] * M[c][b] for c in range(27) if R[c][a])
                 + eps * sum(M[a][c] * R[c][b] for c in range(27) if R[c][b]))
            if v != 0:
                return False
    return True


eqv_table = {n: {"+1": eqv_sign(RnHex[n], Mh, 1), "-1": eqv_sign(RnHex[n], Mh, -1)}
             for n in ns}
CHK("handoff_H_is_NOT_charge_equivariant_either_sign_any_charge",
    all(not eqv_table[n]["+1"] and not eqv_table[n]["-1"] for n in ns),
    "their M is the tau-twisted dual intertwiner (P rho(tau X) = -rho(X)^T P), "
    "NOT the charge-family form: the two seats used DIFFERENT H-objects")
RES["handoff_H_charge_equivariance"] = eqv_table

# their own decomposition M = P * D_chi (tau-intertwiner times a diagonal)
tauP_path = os.path.join(HANDOFF7, "tauP.pkl")
if os.path.exists(tauP_path):
    TP = pickle.load(open(tauP_path, "rb"))
    Pm = [[Fr(x) for x in row] for row in TP["P"]]
    # D_chi = P^{-1} M ; P is a signed permutation here
    psupp = {}
    okP = True
    for j in range(27):
        col = [i for i in range(27) if Pm[i][j]]
        if len(col) != 1 or abs(Pm[col[0]][j]) != 1:
            okP = False
            break
        psupp[j] = col[0]
    if okP:
        Dchi = [Pm[psupp[j]][j] * Mh[psupp[j]][j] for j in range(27)]
        diag_ok = all(Mh[psupp[j]][jj] == 0 for j in range(27)
                      for jj in range(27) if jj != j)
        RES["handoff_M_eq_P_Dchi"] = {
            "P_signed_permutation": True, "M_eq_P_diag": diag_ok,
            "D_chi": [str(d) for d in Dchi]}
        REC("handoff_M_decomposes_as_P_times_diag", diag_ok,
            f"D_chi signs {Counter(str(d) for d in Dchi)}")

# ================================================================ [A6] bridge factor
log("[A6] the exact bridge factor |t|/|s|^{3/2} vs 2304/953 ...")
if t_scalar is not None and s_scalar is not None:
    bridge2 = abs(t_scalar) ** 2 / abs(s_scalar) ** 3      # (|t|/|s|^{3/2})^2
    is_2304_953 = (bridge2 * Fr(953) ** 2 == Fr(2304) ** 2)
    RES["bridge_factor"] = {
        "abs_t": str(abs(t_scalar)), "abs_s": str(abs(s_scalar)),
        "bridge_squared": str(bridge2),
        "equals_2304_over_953": is_2304_953,
        "equals_one": bridge2 == 1}
    REC("bridge_factor_squared_exact", str(bridge2),
        "scale-covariant invariant |t|^2/|s|^3")
    REC("bridge_reproduces_2304_over_953", is_2304_953)
else:
    RES["bridge_factor"] = {
        "abs_t": None if t_scalar is None else str(abs(t_scalar)),
        "abs_s": None,
        "equals_2304_over_953": False,
        "note": "NO scalar bridge exists: the cubic transports with t = 1 but the "
                "two H's are NOT proportional (H' = H+ D2, 11 sign flips) -- "
                "the 2304/953-vs-1 factor is NOT a realization convention"}
    REC("bridge_reproduces_2304_over_953", False,
        "hypothesis refuted at the H leg: no scalar s exists")

# ================================================================ [A7] lambda_B883 = 1
log("[A7] lambda_B883 = 1 EXACT re-verified from B914 banked exact data ...")
MU = [500716339200, -2075673600, -4769856, 2197]
A_, B_, C_, D_ = MU
R3K = [Fr(-D_, A_), Fr(-C_, A_), Fr(-B_, A_)]
R4K = [R3K[2] * R3K[0], R3K[0] + R3K[2] * R3K[1], R3K[1] + R3K[2] * R3K[2]]
KZERO = (Fr(0), Fr(0), Fr(0))
KONE = (Fr(1), Fr(0), Fr(0))


def kmul(x, y):
    c0 = x[0] * y[0]
    c1 = x[0] * y[1] + x[1] * y[0]
    c2 = x[0] * y[2] + x[1] * y[1] + x[2] * y[0]
    c3 = x[1] * y[2] + x[2] * y[1]
    c4 = x[2] * y[2]
    if c4:
        c0 += c4 * R4K[0]; c1 += c4 * R4K[1]; c2 += c4 * R4K[2]
    if c3:
        c0 += c3 * R3K[0]; c1 += c3 * R3K[1]; c2 += c3 * R3K[2]
    return (c0, c1, c2)


def kadd(x, y): return (x[0] + y[0], x[1] + y[1], x[2] + y[2])
def ksub(x, y): return (x[0] - y[0], x[1] - y[1], x[2] - y[2])
def kscale(x, s): return (x[0] * s, x[1] * s, x[2] * s)
def kis0(x): return not (x[0] or x[1] or x[2])


def kinv(x):
    cols = [kmul(x, KONE), kmul(x, (Fr(0), Fr(1), Fr(0))),
            kmul(x, (Fr(0), Fr(0), Fr(1)))]
    Aug = [[cols[j][i] for j in range(3)] + [Fr(1) if i == 0 else Fr(0)]
           for i in range(3)]
    for c in range(3):
        pr = next(r for r in range(c, 3) if Aug[r][c] != 0)
        Aug[c], Aug[pr] = Aug[pr], Aug[c]
        iv = Aug[c][c]
        Aug[c] = [e / iv for e in Aug[c]]
        for r in range(3):
            if r != c and Aug[r][c]:
                f = Aug[r][c]
                Aug[r] = [Aug[r][j] - f * Aug[c][j] for j in range(4)]
    return (Aug[0][3], Aug[1][3], Aug[2][3])


b_mu = Fr(MU[1], MU[0]); c_mu = Fr(MU[2], MU[0])
P_N = (b_mu, Fr(1), Fr(0))
Q_N = (c_mu, b_mu, Fr(1))
NZERO = (KZERO, KZERO)
NONE_ = (KONE, KZERO)


def nmul(a, b):
    a0, a1 = a; b0, b1 = b
    x00 = kmul(a0, b0); x11 = kmul(a1, b1)
    x01 = kadd(kmul(a0, b1), kmul(a1, b0))
    return (ksub(x00, kmul(x11, Q_N)), ksub(x01, kmul(x11, P_N)))


def nadd(a, b): return (kadd(a[0], b[0]), kadd(a[1], b[1]))
def nsub(a, b): return (ksub(a[0], b[0]), ksub(a[1], b[1]))
def nscale(a, s): return (kscale(a[0], s), kscale(a[1], s))
def nis0(a): return kis0(a[0]) and kis0(a[1])


def ninv(a):
    x, y = a
    det = kadd(ksub(kmul(x, x), kmul(kmul(P_N, x), y)), kmul(Q_N, kmul(y, y)))
    di = kinv(det)
    return (kmul(ksub(x, kmul(P_N, y)), di), kscale(kmul(y, di), Fr(-1)))


def parseN(coords):
    f = [Fr(c) for c in coords]
    return ((f[0], f[1], f[2]), (f[3], f[4], f[5]))


qB = {nm: parseN(v) for nm, v in B914["q_exact_ncoords"].items()}
cS = Fr(B914["c_S"]); crow = Fr(B914["c_row_nonS"])
couplB = [(("S0", "S1", "S2"), ((cS, Fr(0), Fr(0)), KZERO)),
          (("A0p", "A1p", "A2p"), ((crow, Fr(0), Fr(0)), KZERO)),
          (("A0m", "A1m", "A2m"), ((crow, Fr(0), Fr(0)), KZERO))]
for key, v in B914["c_cols_ncoords"].items():
    couplB.append((tuple(key.split("+")), parseN(v)))
sgns = []
for names, c in couplB:
    c2 = nmul(c, c)                          # c tau-free -> |c|^2 = c^2
    pq = NONE_
    for nm in names:
        pq = nmul(pq, qB[nm])
    if nis0(nsub(c2, pq)):
        sgns.append("+")
    elif nis0(nadd(c2, pq)):
        sgns.append("-")
    else:
        sgns.append("X")
CHK("lambda_B883_equals_1_EXACT_all_six_couplings",
    all(s in "+-" for s in sgns),
    f"c^2 = sign*prod(q) with signs {sgns} (all -1: the q-product is negative)")
RES["lambda_B883"] = {"value": "1 (exact)", "c2_vs_prodq_signs": sgns}

# ================================================================ [B] numeric belts
log("[B] numeric belts (mpmath) ...")
import numpy as np
import sympy as sp
import mpmath
from mpmath import mp

mp.dps = 60


def charge_num(REP, coefs):
    M = mp.matrix(27, 27)
    for k, c in enumerate(coefs):
        if c:
            cv = mp.mpf(c.numerator) / c.denominator
            for a in range(27):
                for (b, v) in [(j, REP[k][a][j]) for j in range(27) if REP[k][a][j]]:
                    M[a, b] += cv * (mp.mpf(v.numerator) / v.denominator
                                     if isinstance(v, Fr) else mp.mpf(v))
    return M


def eigen_lines(Z):
    """dim-1 clusters (colorless lines) of a 27x27 complex matrix."""
    Zc = mp.matrix(27, 27)
    for i in range(27):
        for j in range(27):
            Zc[i, j] = mp.mpc(Z[i, j])
    E, ER = mp.eig(Zc, left=False, right=True)
    order = sorted(range(27), key=lambda k: (mp.re(E[k]), mp.im(E[k])))
    clusters = []
    for k in order:
        for cl in clusters:
            if abs(E[k] - cl["ev"]) < mp.mpf("1e-20"):
                cl["ks"].append(k)
                break
        else:
            clusters.append({"ev": E[k], "ks": [k]})
    lines = []
    for cl in clusters:
        if len(cl["ks"]) == 1:
            k = cl["ks"][0]
            v = mp.matrix([ER[j, k] for j in range(27)])
            v = v / mp.sqrt(sum(abs(v[j]) ** 2 for j in range(27)))
            lines.append(v)
    return lines


# ---- [B1] independent lambda_handoff in THEIR realization
log("[B1] independent lambda_handoff from the handoff files (dps 60) ...")
RnH = {n: charge_num(REP_H, INV[n]) for n in ns}
ZH = 3 * RnH[8] + 17 * RnH[14] + 5 * RnH[16] + 7 * RnH[22]
linesH = eigen_lines(ZH)
CHK("handoff_realization_nine_colorless_lines", len(linesH) == 9, f"{len(linesH)}")
MhN = mp.matrix(27, 27)
for i in range(27):
    for j in range(27):
        if Mh[i][j]:
            MhN[i, j] = mp.mpf(int(Mh[i][j]))


def hval_handoff(u, v):
    # the solo seat's convention: sum_a u[a] sum_b M[a,b] conj(v[b])
    return sum(u[a] * sum(MhN[a, b] * mp.conj(v[b]) for b in range(27))
               for a in range(27))


T3H_num = {k: int(v) for k, v in T3H.items()}
T3C_num = {k: int(v) for k, v in T3C.items()}


def cub_num(T3, u, v, w):
    s = mp.mpc(0)
    for (a, b, c), cf in T3.items():
        s += cf * u[a] * v[b] * w[c]
    return s


hH = [mp.re(hval_handoff(v, v)) for v in linesH]
lamsH = []
for i in range(9):
    for j in range(i + 1, 9):
        for k in range(j + 1, 9):
            c = cub_num(T3H_num, linesH[i], linesH[j], linesH[k])
            if abs(c) > mp.mpf("1e-18"):
                lam = abs(c) / mp.sqrt(abs(hH[i] * hH[j] * hH[k]))
                lamsH.append(((i, j, k), lam))
CHK("handoff_lambda_support_six_couplings", len(lamsH) == 6, f"{len(lamsH)}")
lamvals = [l for _, l in lamsH]
spreadH = max(lamvals) / min(lamvals) - 1
target = mp.mpf(2304) / 953
worstH = max(abs(l - target) for l in lamvals)
CHK("handoff_lambda_recomputed_equals_2304_over_953",
    spreadH < mp.mpf("1e-40") and worstH < mp.mpf("1e-40"),
    f"spread {mp.nstr(spreadH, 3)}, |lam - 2304/953| worst {mp.nstr(worstH, 3)}")
RES["lambda_handoff_independent"] = {
    "value_50d": mp.nstr(lamvals[0], 50),
    "spread": mp.nstr(spreadH, 4),
    "residual_953lam_minus_2304": mp.nstr(953 * lamvals[0] - 2304, 4)}

# ---- [B2] transported handoff lines vs H_B * (B883 primal lines)
log("[B2] S^-1-transported handoff lines vs H*(primal lines) (dps 60) ...")
RnB = {n: charge_num(REP_B, INV[n]) for n in ns}
ZB = 3 * RnB[8] + 17 * RnB[14] + 5 * RnB[16] + 7 * RnB[22]
linesB = eigen_lines(ZB)
CHK("B883_realization_nine_colorless_lines", len(linesB) == 9, f"{len(linesB)}")
HB = mp.matrix(27, 27)
for b in range(27):
    HB[piW[b], b] = mp.mpf(cbP[b])
# transported handoff lines: v[b] = w[pB2H[b]] / X[b]
transported = []
for w in linesH:
    v = mp.matrix([w[pB2H[b]] / X[b] for b in range(27)])
    v = v / mp.sqrt(sum(abs(v[j]) ** 2 for j in range(27)))
    transported.append(v)
Hu = []
for u in linesB:
    v = HB * u
    v = v / mp.sqrt(sum(abs(v[j]) ** 2 for j in range(27)))
    Hu.append(v)


def line_dist(u, v):
    ip = sum(mp.conj(u[j]) * v[j] for j in range(27))
    d = v - u * ip
    return mp.sqrt(sum(abs(d[j]) ** 2 for j in range(27)))


pairing = {}
worst_pair = mp.mpf(0)
for i, v in enumerate(transported):
    ds = [(line_dist(h, v), j) for j, h in enumerate(Hu)]
    d, j = min(ds)
    pairing[i] = j
    worst_pair = max(worst_pair, d)
CHK("transported_handoff_lines_ARE_H_times_primal_lines",
    sorted(pairing.values()) == list(range(9)) and worst_pair < mp.mpf("1e-40"),
    f"bijective, worst line distance {mp.nstr(worst_pair, 3)}")
RES["dual_lines_identification"] = {
    "statement": "S^-1 (handoff atom lines) = H_B883 * (B883 primal atom lines), "
                 "line for line",
    "worst_line_distance": mp.nstr(worst_pair, 4)}

# lambda with the BANKED instruments (cub_B883, H_plus) on the DUAL lines
hD = []
for v in transported:
    hv = HB * v
    hD.append(mp.re(sum(mp.conj(v[j]) * hv[j] for j in range(27))))
lamsD = []
for i in range(9):
    for j in range(i + 1, 9):
        for k in range(j + 1, 9):
            c = cub_num(T3C_num, transported[i], transported[j], transported[k])
            if abs(c) > mp.mpf("1e-18"):
                lam = abs(c) / mp.sqrt(abs(hD[i] * hD[j] * hD[k]))
                lamsD.append(((i, j, k), lam))
CHK("dual_lines_banked_instruments_six_couplings", len(lamsD) == 6, f"{len(lamsD)}")
lamDv = [l for _, l in lamsD]
spreadD = max(lamDv) / min(lamDv) - 1
worstD = max(abs(l - target) for l in lamDv)
REC("lambda_dual_numeric_equals_2304_over_953",
    bool(spreadD < mp.mpf("1e-40") and worstD < mp.mpf("1e-40")),
    f"lambda(cub_B883, H+, dual lines) = {mp.nstr(lamDv[0], 30)}, "
    f"spread {mp.nstr(spreadD, 3)}")
RES["lambda_dual_numeric"] = {"value_50d": mp.nstr(lamDv[0], 50),
                              "spread": mp.nstr(spreadD, 4),
                              "residual_953lam_minus_2304":
                                  mp.nstr(953 * lamDv[0] - 2304, 4)}

# lambda with the banked instruments on the PRIMAL lines (must be 1; belt of [A7])
hP = []
for u in linesB:
    hu = HB * u
    hP.append(mp.re(sum(mp.conj(u[j]) * hu[j] for j in range(27))))
lamsP = []
for i in range(9):
    for j in range(i + 1, 9):
        for k in range(j + 1, 9):
            c = cub_num(T3C_num, linesB[i], linesB[j], linesB[k])
            if abs(c) > mp.mpf("1e-18"):
                lamsP.append(abs(c) / mp.sqrt(abs(hP[i] * hP[j] * hP[k])))
CHK("primal_lines_lambda_1_numeric_belt",
    len(lamsP) == 6 and max(abs(l - 1) for l in lamsP) < mp.mpf("1e-40"),
    f"worst |lam-1| {mp.nstr(max(abs(l-1) for l in lamsP), 3)}")

# lambda with the TRANSPORTED handoff H' = H+ D2 on primal and dual lines
HPn = mp.matrix(27, 27)
for b in range(27):
    HPn[piW[b], b] = mp.mpf(cbP[b] * D2[b])


def lam_set(lines, Hm, T3):
    hs = []
    for u in lines:
        hu = Hm * u
        hs.append(mp.re(sum(mp.conj(u[j]) * hu[j] for j in range(27))))
    out = []
    for i in range(9):
        for j in range(i + 1, 9):
            for k in range(j + 1, 9):
                c = cub_num(T3, lines[i], lines[j], lines[k])
                if abs(c) > mp.mpf("1e-18"):
                    out.append(abs(c) / mp.sqrt(abs(hs[i] * hs[j] * hs[k])))
    return out


lamHp_dual = lam_set(transported, HPn, T3C_num)
lamHp_primal = lam_set(linesB, HPn, T3C_num)
CHK("dual_lines_with_transported_Hprime_equal_2304_953_numeric",
    len(lamHp_dual) == 6 and max(abs(l - target) for l in lamHp_dual)
    < mp.mpf("1e-40"),
    f"lambda(cub, H', dual) = {mp.nstr(lamHp_dual[0], 30)}")
REC("primal_lines_with_transported_Hprime_lambda",
    mp.nstr(lamHp_primal[0], 30) if len(lamHp_primal) == 6 else None,
    f"spread {mp.nstr(max(lamHp_primal)/min(lamHp_primal)-1, 3) if lamHp_primal else 'NA'}; "
    f"residual vs 2304/953 {mp.nstr(max(abs(l-target) for l in lamHp_primal), 3) if lamHp_primal else 'NA'}")
RES["lambda_Hprime"] = {
    "dual_lines_value_50d": mp.nstr(lamHp_dual[0], 50),
    "primal_lines_value_50d": (mp.nstr(lamHp_primal[0], 50)
                               if len(lamHp_primal) == 6 else None)}

# ================================================================ [C] exact lambda_dual
log("[C] EXACT lambda_dual on v = H u (B914 exact atoms re-built) ...")
# --- charges over Q on the B883 27
Rex = {}
for n in ns:
    M = [[Fr(0)] * 27 for _ in range(27)]
    for k, c in enumerate(INV[n]):
        if c:
            Rk = REP_B[k]
            for a in range(27):
                ra = Rk[a]
                for b in range(27):
                    if ra[b]:
                        M[a][b] += c * ra[b]
    Rex[n] = M
EPS = {8: -1, 14: 1, 16: -1, 22: 1}
ok = True
pinv = [0] * 27
for b in range(27):
    pinv[piW[b]] = b
for n in ns:
    R = Rex[n]
    for a in range(27):
        for b in range(27):
            v = R[piW[b]][a] * cbP[b] + EPS[n] * cbP[pinv[a]] * R[pinv[a]][b]
            if v != 0:
                ok = False
CHK("H_plus_charge_equivariance_reverified_EXACT", ok, "eps = (-1,+1,-1,+1)")


def matmulQ(Xm, Ym):
    n = len(Xm); m = len(Ym[0]); kk = len(Ym)
    return [[sum(Xm[i][t2] * Ym[t2][j] for t2 in range(kk) if Xm[i][t2])
             for j in range(m)] for i in range(n)]


def qsolve_span(basis, vec):
    k, n = len(basis), len(basis[0])
    Aug = [[basis[j][i] for j in range(k)] + [vec[i]] for i in range(n)]
    piv = []; rr = 0
    for c in range(k):
        pr = next((r for r in range(rr, n) if Aug[r][c] != 0), None)
        if pr is None:
            continue
        Aug[rr], Aug[pr] = Aug[pr], Aug[rr]
        iv = Aug[rr][c]
        Aug[rr] = [e / iv for e in Aug[rr]]
        for r in range(n):
            if r != rr and Aug[r][c]:
                f = Aug[r][c]
                Aug[r] = [Aug[r][j] - f * Aug[rr][j] for j in range(k + 1)]
        piv.append(c); rr += 1
    sol = [Fr(0)] * k
    for i, c in enumerate(piv):
        sol[c] = Aug[i][k]
    for i in range(n):
        if sum(sol[j] * basis[j][i] for j in range(k)) != vec[i]:
            return None
    return sol


def _ratrec_real(x, maxden):
    f = mp.mpf(x)
    p0, q0, p1, q1 = mp.mpf(0), mp.mpf(1), mp.mpf(1), mp.mpf(0)
    r = f
    for _ in range(4000):
        a = mp.floor(r)
        p0, q0, p1, q1 = p1, q1, a * p1 + p0, a * q1 + q0
        if q1 > maxden or r == a:
            break
        den = r - a
        if den == 0:
            break
        r = 1 / den
    if q1 > maxden:
        p1, q1 = p0, q0
    if q1 == 0:
        return None
    num, den = int(mp.nint(p1)), int(mp.nint(q1))
    if den < 0:
        num, den = -num, -den
    return Fr(num, den) if den else None


def _mu_roots_numeric(dps=400):
    mp.dps = dps
    rts = mp.polyroots([mp.mpf(c) for c in MU], maxsteps=300, extraprec=400)
    return [mp.re(r) for r in rts]


def _kev_num(x, r):
    return (mp.mpf(x[0].numerator) / mp.mpf(x[0].denominator)
            + (mp.mpf(x[1].numerator) / mp.mpf(x[1].denominator)) * r
            + (mp.mpf(x[2].numerator) / mp.mpf(x[2].denominator)) * r * r)


def _interp_K(vals, mu_roots, maxden, hmax):
    M3 = mp.matrix(3, 3)
    for i in range(3):
        M3[i, 0] = 1; M3[i, 1] = mu_roots[i]; M3[i, 2] = mu_roots[i] ** 2
    try:
        sol = mp.lu_solve(M3, mp.matrix(vals))
    except Exception:
        return None
    cand = []
    for v in sol:
        r = _ratrec_real(v, maxden)
        if r is None or max(abs(r.numerator), r.denominator) > hmax:
            return None
        cand.append(r)
    return tuple(cand)


def root_in_K(h_coeffs, dps=400, hmax=10 ** 120):
    mu_roots = _mu_roots_numeric(dps)
    hh = [mp.mpf(sp.Rational(c).p) / mp.mpf(sp.Rational(c).q) for c in h_coeffs]
    h_roots = mp.polyroots(hh, maxsteps=400, extraprec=400)
    reals = [mp.re(r) for r in h_roots if abs(mp.im(r)) < mp.mpf(10) ** (-dps // 2)]
    maxden = mp.mpf(10) ** (dps // 3)
    for pick in itertools.permutations(range(len(reals)), 3):
        cand = _interp_K([reals[pick[j]] for j in range(3)], mu_roots, maxden, hmax)
        if cand is None:
            continue
        acc = (Fr(sp.Rational(h_coeffs[0]).p, sp.Rational(h_coeffs[0]).q),
               Fr(0), Fr(0))
        for c in h_coeffs[1:]:
            acc = kmul(acc, cand)
            acc = (acc[0] + Fr(sp.Rational(c).p, sp.Rational(c).q), acc[1], acc[2])
        if kis0(acc):
            return cand
    return None


def sqrt_in_K(targetk, dps=400, hmax=10 ** 120):
    mu_roots = _mu_roots_numeric(dps)
    tv = [_kev_num(targetk, r) for r in mu_roots]
    if any(t < 0 for t in tv):
        return None
    sq = [mp.sqrt(t) for t in tv]
    maxden = mp.mpf(10) ** (dps // 3)
    for signs in itertools.product((1, -1), repeat=2):
        vals = [sq[0], signs[0] * sq[1], signs[1] * sq[2]]
        cand = _interp_K(vals, mu_roots, maxden, hmax)
        if cand is None:
            continue
        if kis0(ksub(kmul(cand, cand), targetk)):
            return cand
    return None


def sigma(j, x):
    c0, c1, c2 = x
    if j == 0:
        return ((c0, c1, c2), KZERO)
    if j == 1:
        return (ksub((c0, Fr(0), Fr(0)), kscale(Q_N, c2)),
                ksub((c1, Fr(0), Fr(0)), kscale(P_N, c2)))
    R3N = ((-b_mu, Fr(-1), Fr(0)), (Fr(-1), Fr(0), Fr(0)))
    acc = ((Fr(c0), Fr(0), Fr(0)), KZERO)
    acc = nadd(acc, nscale(R3N, c1))
    acc = nadd(acc, nscale(nmul(R3N, R3N), c2))
    return acc


class TR:
    def mul(self, a, b):
        Xv = nsub(nmul(a[0], b[0]), nscale(nmul(a[1], b[1]), Fr(3)))
        Yv = nadd(nmul(a[0], b[1]), nmul(a[1], b[0]))
        return (Xv, Yv)
    def add(self, a, b): return (nadd(a[0], b[0]), nadd(a[1], b[1]))
    def sub(self, a, b): return (nsub(a[0], b[0]), nsub(a[1], b[1]))
    def scale(self, a, s): return (nscale(a[0], s), nscale(a[1], s))
    def is0(self, a): return nis0(a[0]) and nis0(a[1])
    def conj(self, a): return (a[0], nscale(a[1], Fr(-1)))
    def inv(self, a):
        nrm = nadd(nmul(a[0], a[0]), nscale(nmul(a[1], a[1]), Fr(3)))
        ni = ninv(nrm)
        return (nmul(a[0], ni), nscale(nmul(a[1], ni), Fr(-1)))


T = TR()
TZERO = (NZERO, NZERO)
TONE = (NONE_, NZERO)

CO = {8: 3, 14: 7, 16: 13, 22: 17}
Mc = [[sum(Fr(CO[n]) * Rex[n][i][j] for n in ns) for j in range(27)]
      for i in range(27)]
x = sp.Symbol("x")
cp = sp.Matrix(27, 27, lambda i, j: sp.Rational(Mc[i][j].numerator,
                                                Mc[i][j].denominator)).charpoly(x)
fl = sp.factor_list(cp.as_expr())
facs = sorted([(sp.degree(f, x), m, sp.Poly(f, x)) for f, m in fl[1]])
CHK("charpoly_Mc_factors_3_1__6_1__6_3",
    [(d, m) for d, m, _ in facs] == [(3, 1), (6, 1), (6, 3)])
h_S = [int(c) for c in facs[0][2].all_coeffs()]
h_A = [int(c) for c in facs[1][2].all_coeffs()]


def poly_mat(coeffs):
    Acc = [[Fr(coeffs[0]) if i == j else Fr(0) for j in range(27)]
           for i in range(27)]
    for c in coeffs[1:]:
        Acc = matmulQ(Acc, Mc)
        for i in range(27):
            Acc[i][i] += Fr(c)
    return Acc


W3 = qkernel(poly_mat(h_S))
W6 = qkernel(poly_mat(h_A))
CHK("rational_blocks_dim_3_and_6", len(W3) == 3 and len(W6) == 6)
Me = [[Fr(3) * Rex[8][i][j] + Fr(13) * Rex[16][i][j] for j in range(27)]
      for i in range(27)]
Mo = [[Fr(7) * Rex[14][i][j] + Fr(17) * Rex[22][i][j] for j in range(27)]
      for i in range(27)]


def restrict(Mbig, W):
    Crows = []
    for w in W:
        img = [sum(Mbig[i][j] * w[j] for j in range(27) if w[j]) for i in range(27)]
        sol = qsolve_span(W, img)
        assert sol is not None
        Crows.append(sol)
    return [[Crows[b][a] for b in range(len(W))] for a in range(len(W))]


C_S = restrict(Mc, W3)
C_E = restrict(Me, W6)
C_O = restrict(Mo, W6)
cpE = sp.Matrix(6, 6, lambda i, j: sp.Rational(C_E[i][j].numerator,
                                               C_E[i][j].denominator)).charpoly(x)
flE = sp.factor_list(cpE.as_expr())
gs = [(f, m) for f, m in flE[1] if sp.degree(f, x) > 0]
CHK("char_Me_W6_is_g_squared_cubic", len(gs) == 1 and gs[0][1] == 2
    and sp.degree(gs[0][0], x) == 3)
g_even = sp.Poly(gs[0][0], x).all_coeffs()
g_even = [sp.Rational(c, g_even[0]) for c in g_even]
cpO = sp.Matrix(6, 6, lambda i, j: sp.Rational(C_O[i][j].numerator,
                                               C_O[i][j].denominator)).charpoly(x)
co = sp.Poly(cpO.as_expr(), x).all_coeffs()
CHK("char_Mo_W6_even", co[1] == 0 and co[3] == 0 and co[5] == 0)
h_B = [co[0], co[2], co[4], co[6]]

xS = root_in_K([sp.Rational(c) for c in h_S])
alph = root_in_K(g_even)
Bk = root_in_K(h_B)
CHK("K_roots_xS_alpha_B_found", None not in (xS, alph, Bk))
wK = sqrt_in_K(kscale(Bk, Fr(-1, 3)))
CHK("B_equals_minus_3_w_squared", wK is not None
    and kis0(ksub(kmul(wK, wK), kscale(Bk, Fr(-1, 3)))))


def kkernel(M):
    m, n = len(M), len(M[0])
    A = [row[:] for row in M]
    piv = []; rr = 0
    for c in range(n):
        pr = next((r for r in range(rr, m) if not kis0(A[r][c])), None)
        if pr is None:
            continue
        A[rr], A[pr] = A[pr], A[rr]
        iv = kinv(A[rr][c])
        A[rr] = [kmul(iv, e) for e in A[rr]]
        for r in range(m):
            if r != rr and not kis0(A[r][c]):
                f = A[r][c]
                A[r] = [ksub(A[r][j], kmul(f, A[rr][j])) for j in range(n)]
        piv.append(c); rr += 1
    ker = []
    for fc in [c for c in range(n) if c not in piv]:
        v = [KZERO] * n
        v[fc] = KONE
        for i, c in enumerate(piv):
            v[c] = kscale(A[i][fc], Fr(-1))
        ker.append(v)
    return ker


CmK = [[ksub((Fr(C_S[i][j]), Fr(0), Fr(0)), xS if i == j else KZERO)
        for j in range(3)] for i in range(3)]
kerS = kkernel(CmK)
CHK("kernel_S_dim_1", len(kerS) == 1)
vS3 = kerS[0]


def fmul(a, b):
    return (kadd(kmul(a[0], b[0]), kmul(Bk, kmul(a[1], b[1]))),
            kadd(kmul(a[0], b[1]), kmul(a[1], b[0])))


def fsub(a, b): return (ksub(a[0], b[0]), ksub(a[1], b[1]))
def fis0(a): return kis0(a[0]) and kis0(a[1])


def finv(a):
    den = ksub(kmul(a[0], a[0]), kmul(Bk, kmul(a[1], a[1])))
    di = kinv(den)
    return (kmul(a[0], di), kscale(kmul(a[1], di), Fr(-1)))


rowsF = []
for i in range(6):
    rowsF.append([(ksub((Fr(C_E[i][j]), Fr(0), Fr(0)),
                        alph if i == j else KZERO), KZERO) for j in range(6)])
for i in range(6):
    rowsF.append([((Fr(C_O[i][j]), Fr(0), Fr(0)),
                   (Fr(-1), Fr(0), Fr(0)) if i == j else KZERO) for j in range(6)])
A2m = [row[:] for row in rowsF]
piv = []; rr = 0
for c in range(6):
    pr = next((r for r in range(rr, 12) if not fis0(A2m[r][c])), None)
    if pr is None:
        continue
    A2m[rr], A2m[pr] = A2m[pr], A2m[rr]
    iv = finv(A2m[rr][c])
    A2m[rr] = [fmul(iv, e) for e in A2m[rr]]
    for r in range(12):
        if r != rr and not fis0(A2m[r][c]):
            f = A2m[r][c]
            A2m[r] = [fsub(A2m[r][j], fmul(f, A2m[rr][j])) for j in range(6)]
    piv.append(c); rr += 1
FZ = (KZERO, KZERO)
kerA = []
for fc in [c for c in range(6) if c not in piv]:
    v = [FZ] * 6
    v[fc] = (KONE, KZERO)
    for i, c in enumerate(piv):
        v[c] = fsub(FZ, A2m[i][fc])
    kerA.append(v)
CHK("kernel_nonS_dim_1_over_K_beta", len(kerA) == 1)
vA6 = kerA[0]


def lift(coords, W):
    out = []
    for i in range(27):
        acc = KZERO
        for a, cf in enumerate(coords):
            if W[a][i]:
                acc = kadd(acc, kscale(cf, W[a][i]))
        out.append(acc)
    return out


def normalize27(vec):
    L2 = 1
    for kt in vec:
        for x2 in kt:
            if x2:
                d = x2.denominator
                L2 = L2 * d // math.gcd(L2, d)
    vec2 = [kscale(kt, Fr(L2)) for kt in vec]
    G = 0
    for kt in vec2:
        for x2 in kt:
            G = math.gcd(G, abs(x2.numerator))
    if G > 1:
        vec2 = [kscale(kt, Fr(1, G)) for kt in vec2]
    return vec2


vS27 = normalize27(lift(vS3, W3))
u27 = lift([f[0] for f in vA6], W6)
wt27 = lift([f[1] for f in vA6], W6)
wodd27 = [kmul(wK, kt) for kt in wt27]
uw = normalize27(u27 + wodd27)
u27, wodd27 = uw[:27], uw[27:]
atoms_ex = {}
for j in range(3):
    atoms_ex[f"S{j}"] = [(sigma(j, kt), NZERO) for kt in vS27]
    for sgn2, tag in ((1, "p"), (-1, "m")):
        atoms_ex[f"A{j}{tag}"] = [(sigma(j, u27[i]),
                                   nscale(sigma(j, wodd27[i]), Fr(sgn2)))
                                  for i in range(27)]
NAMES = sorted(atoms_ex)

# joint-eigenline certificate (all 4 charges, exact)
ok = True
for name in NAMES:
    vec = atoms_ex[name]
    k0 = next(i for i in range(27) if not T.is0(vec[i]))
    for n in ns:
        R = Rex[n]
        w = []
        for i in range(27):
            acc = TZERO
            for jj in range(27):
                if R[i][jj] and not T.is0(vec[jj]):
                    acc = T.add(acc, T.scale(vec[jj], R[i][jj]))
            w.append(acc)
        for i in range(27):
            for k in range(i + 1, 27):
                if not T.is0(T.sub(T.mul(w[i], vec[k]), T.mul(w[k], vec[i]))):
                    ok = False
CHK("nine_primal_atoms_exact_joint_eigenlines", ok)

# ---- the DUAL lines exactly: v = H u  (coordinate signed permutation)
dual_ex = {}
for name in NAMES:
    u = atoms_ex[name]
    v = [TZERO] * 27
    for b in range(27):
        v[piW[b]] = T.scale(u[b], Fr(cbP[b]))
    dual_ex[name] = v
# certificate: v is a joint LEFT eigenline: R_n^T v = (-eps_n mu_n) v.
ok = True
for name in NAMES:
    vec = dual_ex[name]
    for n in ns:
        R = Rex[n]
        w = []
        for i in range(27):
            acc = TZERO
            for jj in range(27):
                if R[jj][i] and not T.is0(vec[jj]):        # R^T action
                    acc = T.add(acc, T.scale(vec[jj], R[jj][i]))
            w.append(acc)
        for i in range(27):
            for k in range(i + 1, 27):
                if not T.is0(T.sub(T.mul(w[i], vec[k]), T.mul(w[k], vec[i]))):
                    ok = False
CHK("nine_dual_lines_exact_joint_LEFT_eigenlines", ok,
    "v = H u is a joint eigenline of the transposed charge family")


def hpairP(u, v):
    acc = TZERO
    for b in range(27):
        a = piW[b]
        if not (T.is0(u[a]) or T.is0(v[b])):
            acc = T.add(acc, T.scale(T.mul(T.conj(u[a]), v[b]), Fr(cbP[b])))
    return acc


def cubT(T3, u, v, w):
    s = TZERO
    for (a, b, c), cf in T3.items():
        if not (T.is0(u[a]) or T.is0(v[b]) or T.is0(w[c])):
            s = T.add(s, T.scale(T.mul(T.mul(u[a], v[b]), w[c]), cf))
    return s


qD = {}
ok_real = True; ok_nz = True
for name in NAMES:
    v = dual_ex[name]
    qv = hpairP(v, v)
    if not nis0(qv[1]):
        ok_real = False
    if T.is0(qv):
        ok_nz = False
    qD[name] = qv[0]
CHK("dual_q_tau_free_and_nonzero", ok_real and ok_nz)

log("    exact couplings on the dual lines (all 165 multisets) ...")
supportD = []
valsD = {}
for i1 in range(9):
    for i2 in range(i1, 9):
        for i3 in range(i2, 9):
            val = cubT(T3C, dual_ex[NAMES[i1]], dual_ex[NAMES[i2]],
                       dual_ex[NAMES[i3]])
            if not T.is0(val):
                supportD.append((i1, i2, i3))
                valsD[(i1, i2, i3)] = val
CHK("dual_support_exactly_6_of_165", len(supportD) == 6,
    f"{[[NAMES[i] for i in t] for t in supportD]}")

# --- the CANONICAL lambda (banked H+) on the mirror lines: 1 EXACTLY
lam_ok = []
for t in supportD:
    c = valsD[t]
    c2 = T.mul(c, T.conj(c))
    assert nis0(c2[1])
    pq = NONE_
    for i in t:
        pq = nmul(pq, qD[NAMES[i]])
    plus = nis0(nsub(c2[0], pq))
    minus = nis0(nadd(c2[0], pq))
    lam_ok.append("+" if plus else ("-" if minus else "X"))
CHK("lambda_dual_with_banked_Hplus_EQUALS_1_EXACT_all_six",
    all(s in "+-" for s in lam_ok),
    f"|c|^2 = sign*prod(q) with signs {lam_ok}: the canonical lambda is "
    "REALIZATION-INDEPENDENT (1 on the 27 lines AND on the mirror lines)")
RES["lambda_dual_exact_Hplus"] = {
    "value": "1 (exact)",
    "statement": "same primitive cubic, banked H+, MIRROR (left-eigen) lines",
    "support": [[NAMES[i] for i in t] for t in supportD],
    "c2_vs_prodq_signs": lam_ok}

# --- lambda with the transported handoff H' = H+ D2 on the mirror lines:
#     2304/953 EXACTLY (the exactification of the solo seat's number)
def hpairD2(u, v):
    acc = TZERO
    for b in range(27):
        a = piW[b]
        if not (T.is0(u[a]) or T.is0(v[b])):
            acc = T.add(acc, T.scale(T.mul(T.conj(u[a]), v[b]),
                                     Fr(cbP[b] * D2[b])))
    return acc


qDp = {}
ok_real = True; ok_nz = True
for name in NAMES:
    v = dual_ex[name]
    qv = hpairD2(v, v)
    if not nis0(qv[1]):
        ok_real = False
    if T.is0(qv):
        ok_nz = False
    qDp[name] = qv[0]
CHK("dual_qprime_tau_free_and_nonzero", ok_real and ok_nz)
lam2_target = Fr(2304, 953) ** 2
lam2_ok = []
for t in supportD:
    c = valsD[t]
    c2 = T.mul(c, T.conj(c))
    pq = NONE_
    for i in t:
        pq = nmul(pq, qDp[NAMES[i]])
    plus = nis0(nsub(c2[0], nscale(pq, lam2_target)))
    minus = nis0(nadd(c2[0], nscale(pq, lam2_target)))
    lam2_ok.append("+" if plus else ("-" if minus else "X"))
CHK("lambda_dual_with_Hprime_EQUALS_2304_953_EXACT_all_six",
    all(s in "+-" for s in lam2_ok),
    f"|c|^2 = (2304/953)^2 * sign*prod(q') with signs {lam2_ok}: the solo "
    "seat's 85-digit number is EXACT -- and it is the tau-twisted-H lambda")
RES["lambda_dual_exact_Hprime"] = {
    "value": "2304/953 (exact)",
    "statement": "same primitive cubic, transported handoff H' = H+ D2, "
                 "mirror lines: the solo lambda exactified",
    "c2_vs_prodq_signs": lam2_ok}

# --- lambda with H' on the PRIMAL lines (symmetry check, exact)
qPp = {}
prim_ok = True
for name in NAMES:
    u = atoms_ex[name]
    qv = hpairD2(u, u)
    if not nis0(qv[1]) or T.is0(qv):
        prim_ok = False
    qPp[name] = qv[0]
lam2P_ok = []
if prim_ok:
    # primal support = banked six couplings (B914); reuse the exact banked c's
    for names, c in couplB:
        c2 = nmul(c, c)
        pq = NONE_
        for nm in names:
            pq = nmul(pq, qPp[nm])
        pq_s = nscale(pq, lam2_target)
        hit_2304 = nis0(nsub(c2, pq_s)) or nis0(nadd(c2, pq_s))
        hit_1 = nis0(nsub(c2, pq)) or nis0(nadd(c2, pq))
        lam2P_ok.append("2304/953" if hit_2304 else ("1" if hit_1 else "other"))
REC("lambda_primal_with_Hprime", str(lam2P_ok),
    "the tau-twisted lambda evaluated on the PRIMAL nine lines")
RES["lambda_primal_Hprime"] = {"per_coupling": lam2P_ok}

# --- the per-line discrepancy d_i = q'^{H'}_i / q^{H+}_i and where 953 lives
def ncoords(z):
    return [z[0][0], z[0][1], z[0][2], z[1][0], z[1][1], z[1][2]]


def minpoly_N(z):
    pows = [NONE_]
    for _ in range(6):
        pows.append(nmul(pows[-1], z))
    for d in range(1, 7):
        M = [[ncoords(pows[k])[i] for k in range(d + 1)] for i in range(6)]
        kv2 = qkernel(M)
        if kv2:
            cvec = kv2[0]
            if cvec[d] == 0:
                continue
            mon = [c / cvec[d] for c in cvec]
            acc = NZERO
            for k in range(d + 1):
                acc = nadd(acc, nscale(pows[k], mon[k]))
            assert nis0(acc)
            den = 1
            for c in mon:
                den = den * c.denominator // math.gcd(den, c.denominator)
            ints = [int(c * den) for c in mon]
            g2 = 0
            for v in ints:
                g2 = math.gcd(g2, abs(v))
            ints = [v // g2 for v in ints]
            if ints[-1] < 0:
                ints = [-v for v in ints]
            return ints[::-1]
    return None


# d_i = q'^{H'}_i / q^{H+}_i per line, exact in N; the 953-carrier hunt
import sympy.ntheory as nt
d_ex = {nm: nmul(qDp[nm], ninv(qD[nm])) for nm in NAMES}
d_min = {nm: minpoly_N(d_ex[nm]) for nm in NAMES}
RES["d_ratio_minpolys_desc"] = {nm: [str(c) for c in (d_min[nm] or [])]
                                for nm in NAMES}
fac_d = {}
for nm in NAMES:
    mpoly = d_min[nm]
    if mpoly:
        fac_d[nm] = {
            "deg": len(mpoly) - 1,
            "is_rational": len(mpoly) == 2,
            "value_if_rational": (str(Fr(-mpoly[1], mpoly[0]))
                                  if len(mpoly) == 2 else None),
            "lead_factor": {str(p): e for p, e in
                            nt.factorint(abs(mpoly[0])).items()} if mpoly[0] else {},
            "const_factor": {str(p): e for p, e in
                             nt.factorint(abs(mpoly[-1])).items()} if mpoly[-1] else {}}
RES["d_ratio_arithmetic"] = fac_d
# per-coupling products of d: must equal (953/2304)^2 exactly (both lambdas exact)
dprod_ok = []
inv_target = Fr(953, 2304) ** 2
for t in supportD:
    dp = NONE_
    for i in t:
        dp = nmul(dp, d_ex[NAMES[i]])
    plus = nis0(nsub(dp, nscale(NONE_, inv_target)))
    minus = nis0(nadd(dp, nscale(NONE_, inv_target)))
    dprod_ok.append("+" if plus else ("-" if minus else "X"))
CHK("d_products_per_coupling_equal_953_2304_squared_EXACT",
    all(s in "+-" for s in dprod_ok),
    f"prod_t d_i = sign*(953/2304)^2 with signs {dprod_ok}: THE structural "
    "home of 953 -- the per-line H'/H+ norm ratios")
RES["d_products_signs"] = dprod_ok
has953 = {nm: ("953" in fac_d[nm]["lead_factor"]
               or "953" in fac_d[nm]["const_factor"]) for nm in fac_d}
REC("where_953_lives", str(has953),
    "953 in the minimal polynomials of the per-line ratios d = q^{H'}/q^{H+}")

# ================================================================ verdict
bridge_ok = (prop_cubic and abs(t_scalar) == 1 and s_scalar is None)
RES["verdict"] = (
    "BRIDGE COMPUTED -- THE CONVENTION HYPOTHESIS IS REFUTED AND THE "
    "DISCREPANCY IS RESOLVED: S is unique up to scale and primitive S is a "
    "SIGNED PERMUTATION (both realizations have all entries +-1); the "
    "primitive cubic transports IDENTICALLY (t = 1: 'primitive +-1 in its own "
    "basis' IS canonical across the mirror); but the two H's are DIFFERENT "
    "INVARIANT OBJECTS: H'(solo, transported) = H+(B912) * diag(D2) with 11 "
    "sign flips -- the solo M is the tau-twisted dual intertwiner, not the "
    "charge-equivariant form, so NO scalar s exists and the factor 2304/953 "
    "is NOT a normalization convention.  Both pipelines are arithmetically "
    "RIGHT: with the banked H+ the lambda is 1 EXACTLY on the primal nine "
    "AND on the mirror nine (realization-independent); with the solo H' the "
    "lambda is 2304/953 EXACTLY (exactified here from their 85-digit belt) "
    "on the mirror lines.  953 enters through the per-line norm ratios "
    "d_i = q^{H'}/q^{H+} whose per-coupling products are (953/2304)^2."
    if bridge_ok else
    "BRIDGE ANOMALY: an unexpected branch -- see cubic_transport / "
    "H_transport / the lambda checks.")
RES["runtime_s"] = round(time.time() - T00, 1)
json.dump(RES, open(os.path.join(HERE, "results.json"), "w"), indent=1)
log("results.json written")
log("VERDICT:", RES["verdict"])
