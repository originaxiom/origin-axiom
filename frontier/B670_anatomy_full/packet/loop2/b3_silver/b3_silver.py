"""B3 -- THE SILVER TRICHOTOMY (PREREG_L2.md sha f9ae4a9e, B3 clause).

  "v0_silver's Jordan invariants on the banked B649 letters (cross-square
  support/values, N(v0), the sharp-fixedness) -- is unit-direction-ness
  metallic-universal? (K020: expect same FORM -- sharp-fixed invertible --
  different values.)"

Machinery reused, all read-only, all from this seat's already-verified
constructions:
  - origin-axiom/frontier/B649_silver_holonomy/letters27_L.json,
    entries_L.json, e6_principal_rational.json, cubic_rational.json
    (the banked exact silver 27-letters + Jordan cubic over
    L = Q(s,i), s^4 = 8 s^2 + 16).
  - origin-axiom/frontier/B649_silver_holonomy/b649_stage3a.py: the L-field
    exact arithmetic, the S1 = {a,b,c,A,B,C} letter-matrix loader, and the
    SL2(L) weld-solve (EXEC'd as source, read-only). We deliberately
    truncate the exec at the SAME cut point W2a used (right before the
    weld-solution-space print), i.e. BEFORE the expensive 6-generator
    silver DOUBLE Fox/Z1 computation (~200s, confirmed by
    b649_stage3a_output.txt: "dim Z1 = 31 (200.6s)") -- B3 only needs the
    SOLO 3-generator letters {a,b,c,A,B,C} and the weld U27 (itself cheap:
    "U27 lifted (3.9s)" per the same banked log), NOT the DOUBLE's H1.
  - seat-work/invariant_line/w2_silver/w2a_silver.py: REUSED verbatim for
    (a) v0_silver's construction as the joint nullspace of {A-I,B-I,C-I}
    (banked support {12,13,14}, coefficients (1,-1,1)), and (b) the
    N_silver cubic contraction C3(u,v)[r] = sum_{p,q} CUB[p,q,r] u_p v_q,
    with N_silver(u,v,w) = dotL(C3(u,v), w) -- the exact same test vectors
    u1,v1,w1 are reused for the invariance gate, so this literally reruns
    W2a's gates["v0_dim1"] and gates["N_invariant_all"].

THE NEW COMPUTATION (not in W2a): the cross-square s(z) = N_silver(v0,v0,z)
for all 27 basis z (== the vector C3(v0,v0) itself, since
dotL(C3(v0,v0), e_i) = C3(v0,v0)[i]); its support/values; the
sharp-fixedness proportionality constant; N_silver(v0,v0,v0); and the
rank/trichotomy classification compared to golden's banked form
(sharp-fixed factor -2, N=-6, rank 3 invertible).

Every number lives in L = Q(s,i) (Fraction-pairs on a 4x4 basis
{1,s,s^2,s^3} each for the real/imaginary parts). Zero floats anywhere.
"""
import os
import sys
import time
import json
from fractions import Fraction as Fr

os.environ["PYTHONDONTWRITEBYTECODE"] = "1"

T0 = time.time()


def log(msg):
    print(f"[{time.time()-T0:7.1f}s] {msg}", flush=True)


HERE = os.path.dirname(os.path.abspath(__file__))
B649 = "<repo>/frontier/B649_silver_holonomy"
STAGE3A = os.path.join(B649, "b649_stage3a.py")

d = 27
gates = {}

# ============================================================================
log("STEP 0: exec b649_stage3a.py prefix (L-arith + S1 letters + weld-solve "
    "nullspace)")
log("        source READ only -- no writes to origin-axiom. Truncated BEFORE "
    "the")
log("        expensive 6-gen silver DOUBLE Fox/Z1 computation (not needed "
    "for B3;")
log("        banked timing for that skipped part: rows 46.5s + Z1 200.6s, "
    "see")
log("        b649_stage3a_output.txt -- confirms this is a deliberate, "
    "justified skip)")
src = open(STAGE3A).read()
cut = src.index('print(f"  weld solution space')
ns = {"__name__": "b649_stage3a_head", "__file__": STAGE3A}
t0 = time.time()
exec(compile(src[:cut], STAGE3A, "exec"), ns)
log(f"  prefix exec complete ({time.time()-t0:.1f}s)")

L, Lc, L0, L1 = ns["L"], ns["Lc"], ns["L0"], ns["L1"]
meye, mmul, mscale, madd = ns["meye"], ns["mmul"], ns["mscale"], ns["madd"]
mconj27 = ns["mconj27"]
lift_sl2 = ns["lift_sl2"]
adj2 = ns["adj2"]
S1 = ns["S1"]
null = ns["null"]
log(f"  S1 letters loaded: {sorted(S1.keys())}   weld rational nullspace "
    f"dim = {len(null)}")

# ============================================================================
log("STEP 0b: reconstruct weld U27 (verbatim adaptation of "
    "b649_stage3b_swap.py L32-50)")
t0 = time.time()
u = None
for v in null:
    cand = [[L(list(map(Fr, v[8 * (2 * i + j): 8 * (2 * i + j) + 4])),
               list(map(Fr, v[8 * (2 * i + j) + 4: 8 * (2 * i + j) + 8])))
             for j in range(2)] for i in range(2)]
    det = cand[0][0] * cand[1][1] - cand[0][1] * cand[1][0]
    if not det.is_zero():
        u = cand
        break
assert u is not None, "no invertible weld intertwiner found in rational " \
    "nullspace"
U27 = lift_sl2(u)
U27i = lift_sl2(adj2(u))
log(f"  U27 lifted ({time.time()-t0:.1f}s)")

S2 = {nm: mmul(mmul(U27, mconj27(S1[nm])), U27i) for nm in "abcABC"}
LETS = {"a": S1["a"], "b": S1["b"], "c": S1["c"],
        "A": S1["A"], "B": S1["B"], "C": S1["C"],
        "d": S2["a"], "e": S2["b"], "f": S2["c"],
        "D": S2["A"], "E": S2["B"], "F": S2["C"]}
log("  LETS built: 12 letters (a..f, A..F) -- full silver holonomy "
    "generating set available")

# ============================================================================
# generic exact linear algebra over L (verbatim pattern from w2a_silver.py)


def is_zero_vec(v):
    return all(x.is_zero() for x in v)


def matvec(M, v):
    n = len(v)
    return [sum((M[i][k] * v[k] for k in range(n) if not v[k].is_zero()), L0)
            for i in range(n)]


def msub(X, Y, n):
    return [[X[i][j] - Y[i][j] for j in range(n)] for i in range(n)]


def dotL(f, v):
    return sum((f[t] * v[t] for t in range(d) if not v[t].is_zero()), L0)


def L_nullspace_basis(rows, ncols):
    A = [r[:] for r in rows]
    m = len(A)
    r = 0
    pivs = []
    for c in range(ncols):
        piv = next((k for k in range(r, m) if not A[k][c].is_zero()), None)
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        pv_inv = A[r][c].inv()
        A[r] = [x * pv_inv for x in A[r]]
        for k in range(m):
            if k != r and not A[k][c].is_zero():
                f = A[k][c]
                A[k] = [x - f * y for x, y in zip(A[k], A[r])]
        pivs.append(c)
        r += 1
        if r == m:
            break
    free = [c for c in range(ncols) if c not in pivs]
    basis = []
    for fc in free:
        v = [L0] * ncols
        v[fc] = L1
        for rr, pc in enumerate(pivs):
            v[pc] = L0 - A[rr][fc]
        basis.append(v)
    return basis


def fmtL(x):
    if x.is_zero():
        return "0"

    def poly_str(coeffs, varname):
        terms = []
        for k, c in enumerate(coeffs):
            if c == 0:
                continue
            if k == 0:
                terms.append(f"{c}")
            elif k == 1:
                terms.append(f"{c}*{varname}")
            else:
                terms.append(f"{c}*{varname}^{k}")
        return "+".join(terms) if terms else "0"

    re_s = poly_str(x.re, "s")
    im_s = poly_str(x.im, "s")
    if im_s == "0":
        return re_s
    return f"({re_s}) + i*({im_s})"


# ============================================================================
log("=== GATE 1: v0_silver = joint nullspace of {A-I,B-I,C-I}  [rerun of "
    "W2a's gates['v0_dim1']] ===")
AmI = msub(S1['a'], meye(d), d)
BmI = msub(S1['b'], meye(d), d)
CmI = msub(S1['c'], meye(d), d)
stacked = AmI + BmI + CmI
v0_basis = L_nullspace_basis(stacked, d)
gates["v0_dim1"] = (len(v0_basis) == 1)
log(f"  joint nullspace dim = {len(v0_basis)}  [HARD GATE dim=1]: "
    f"{'PASS' if gates['v0_dim1'] else 'FAIL'}")
assert gates["v0_dim1"], f"v0_silver nullspace dim {len(v0_basis)} != 1"

v0_raw = v0_basis[0]
idx0 = next(i for i, x in enumerate(v0_raw) if not x.is_zero())
scale = v0_raw[idx0].inv()
v0 = [scale * x for x in v0_raw]
assert (v0[idx0] - L1).is_zero()
for M, nm in ((AmI, "A"), (BmI, "B"), (CmI, "C")):
    assert is_zero_vec(matvec(M, v0)), f"v0_silver fails ({nm}-I)v0=0 exactly"
support_v0 = [i for i, x in enumerate(v0) if not x.is_zero()]
log(f"  v0_silver verified exactly: (A-I)v0=(B-I)v0=(C-I)v0=0; normalized "
    f"idx0={idx0}")
log(f"  support size = {len(support_v0)}  indices = {support_v0}")
for i in support_v0:
    log(f"    idx {i:2d}  coeff = {fmtL(v0[i])}")
banked_match = (support_v0 == [12, 13, 14]
                and fmtL(v0[12]) == "1" and fmtL(v0[13]) == "-1"
                and fmtL(v0[14]) == "1")
log(f"  matches W2a-banked v0_silver (support {{12,13,14}}, coeffs "
    f"(1,-1,1)): {banked_match}")
gates["v0_matches_banked"] = banked_match

# invariance under d,e,f too (full 6-generator solo+weld group, sanity check)
log("checking v0_silver invariance under the weld-derived d,e,f as well "
    "(sanity; not a hard gate)...")
inv_def = {}
for g in ('d', 'e', 'f'):
    diff = [matvec(LETS[g], v0)[i] - v0[i] for i in range(d)]
    inv_def[g] = is_zero_vec(diff)
    log(f"  v0_silver invariant under {g}: {inv_def[g]}")
gates["v0_invariant_under_def"] = all(inv_def.values())

# ============================================================================
log("=== GATE 2: N_silver invariance under all 6 letters a,b,c,d,e,f  "
    "[rerun of W2a's gates['N_invariant_all']] ===")
CUB = {tuple(map(int, k.split(","))): Fr(v)
       for k, v in json.load(open(os.path.join(B649,
                                                 "cubic_rational.json"))).items()}
log(f"  cubic_rational.json entries: {len(CUB)}")


def C3(u, v):
    cov = [L0] * d
    for (p, q, r_), cval in CUB.items():
        if not u[p].is_zero() and not v[q].is_zero():
            cov[r_] = cov[r_] + Lc(cval) * u[p] * v[q]
    return cov


# EXACT SAME test vectors as W2a (reproducing its gate literally)
u1 = [Lc(Fr(i % 5 - 2)) for i in range(d)]
v1_ = [Lc(Fr((2 * i) % 7 - 3)) for i in range(d)]
w1 = [Lc(Fr((3 * i) % 4 - 1)) for i in range(d)]
ninv = {}
for nm in ('a', 'b', 'c', 'd', 'e', 'f'):
    M = LETS[nm]
    lhs = dotL(C3(matvec(M, u1), matvec(M, v1_)), matvec(M, w1))
    rhs = dotL(C3(u1, v1_), w1)
    ninv[nm] = (lhs - rhs).is_zero()
    log(f"  N_silver-invariance under {nm}: {'PASS' if ninv[nm] else 'FAIL'}")
gates["N_invariant_all"] = all(ninv.values())
log(f"  GATE N_invariant_all: {'PASS' if gates['N_invariant_all'] else 'FAIL'}")
assert gates["N_invariant_all"], "N_silver is NOT rho-invariant"

# ============================================================================
log("=== STEP 3: THE CROSS-SQUARE  s(z) = N_silver(v0,v0,z) for all 27 "
    "basis z ===")
log("  (s(z) = dotL(C3(v0,v0), e_z) == C3(v0,v0)[z] -- computed once as a "
    "27-vector)")
s_vec = C3(v0, v0)
support_s = [i for i, x in enumerate(s_vec) if not x.is_zero()]
log(f"  cross-square support size = {len(support_s)}  indices = "
    f"{support_s}")
for i in support_s:
    log(f"    idx {i:2d}  s(e_{i}) = {fmtL(s_vec[i])}")

log("  sharp-fixedness check: is s proportional to v0's own pattern "
    "(same support, ratio constant)?")
sharp_fixed = (support_s == support_v0)
lam = None
if sharp_fixed:
    lam = s_vec[idx0] * v0[idx0].inv()  # v0[idx0] == L1 so lam == s_vec[idx0]
    for i in support_v0:
        if (s_vec[i] - lam * v0[i]).is_zero() is False:
            sharp_fixed = False
            break
    if sharp_fixed:
        for i in range(d):
            if i not in support_v0 and not s_vec[i].is_zero():
                sharp_fixed = False
                break
gates["sharp_fixed"] = sharp_fixed
log(f"  SHARP-FIXED (s = lambda * v0 exactly): {sharp_fixed}")
if sharp_fixed:
    log(f"  proportionality constant lambda = {fmtL(lam)}")

# ============================================================================
log("=== STEP 4: N_silver(v0,v0,v0) exactly ===")
N_v0 = dotL(s_vec, v0)
log(f"  N_silver(v0,v0,v0) = {fmtL(N_v0)}")
if sharp_fixed:
    sumsq = dotL(v0, v0)
    log(f"  cross-check: lambda * dotL(v0,v0) = {fmtL(lam)} * "
        f"{fmtL(sumsq)} = {fmtL(lam*sumsq)}  (should equal N(v0,v0,v0))")
    gates["N_crosscheck"] = (lam * sumsq - N_v0).is_zero()
    log(f"  cross-check PASS: {gates['N_crosscheck']}")

# ============================================================================
log("=== STEP 5: THE TRICHOTOMY + K020 VERDICT ===")
N_nonzero = not N_v0.is_zero()
s_nonzero = any(not x.is_zero() for x in s_vec)

if not s_nonzero:
    rank = 1
    rank_desc = "rank 1 (v0^# = 0, v0 != 0)"
elif not N_nonzero:
    rank = 2
    rank_desc = "rank 2 (v0^# != 0 but N(v0)=0)"
else:
    rank = 3
    rank_desc = "rank 3 (N(v0) != 0 -- INVERTIBLE)"
log(f"  rank classification: {rank}  -- {rank_desc}")

golden = {"sharp_fixed": True, "factor": Fr(-2), "N": Fr(-6), "rank": 3,
          "invertible": True}
form_match = (sharp_fixed and rank == 3 and golden["sharp_fixed"]
              and golden["rank"] == 3)
log(f"  golden form (banked): sharp-fixed factor -2, N=-6, rank 3 "
    f"invertible")
log(f"  silver form (this run): sharp-fixed={sharp_fixed}, "
    f"lambda={fmtL(lam) if lam is not None else 'n/a'}, "
    f"N={fmtL(N_v0)}, rank={rank}")

if form_match:
    k020 = ("FORM-MATCH: silver reproduces golden's sharp-fixed / rank-3 "
            "/ invertible FORM with different exact values "
            "(unit-direction-ness IS metallic-universal)")
else:
    k020 = (f"FORM-MISMATCH: silver's (sharp_fixed={sharp_fixed}, rank="
             f"{rank}) differs from golden's (sharp_fixed=True, rank=3) "
             "(golden-specific -- either banks)")
log(f"*** THE K020 VERDICT: {k020} ***")
gates["form_match"] = form_match

# ============================================================================
all_gates_pass = all(v for k, v in gates.items() if isinstance(v, bool))
log(f"ALL HARD GATES PASS: {all_gates_pass}")

out = {
    "prereg_sha256": "f9ae4a9e",
    "prereg_clause": "B3 (THE SILVER TRICHOTOMY)",
    "object": "m136 (B649 silver holonomy, L=Q(s,i), s^4=8s^2+16)",
    "gates": gates,
    "v0_silver": {
        "normalized_idx0": idx0,
        "support_indices": support_v0,
        "support_size": len(support_v0),
        "coefficients_readable": {str(i): fmtL(v0[i]) for i in support_v0},
        "coordinates_full": [[str(x.re), str(x.im)] for x in v0],
        "matches_banked_w2a": banked_match,
        "invariant_under_def": gates["v0_invariant_under_def"],
    },
    "N_silver_invariance": ninv,
    "cross_square": {
        "support_indices": support_s,
        "support_size": len(support_s),
        "values_readable": {str(i): fmtL(s_vec[i]) for i in support_s},
        "coordinates_full": [[str(x.re), str(x.im)] for x in s_vec],
        "sharp_fixed": sharp_fixed,
        "proportionality_constant_readable": (fmtL(lam)
                                               if lam is not None else None),
        "proportionality_constant_full": ([str(lam.re), str(lam.im)]
                                           if lam is not None else None),
    },
    "N_v0_v0_v0": {
        "readable": fmtL(N_v0),
        "full": [str(N_v0.re), str(N_v0.im)],
        "is_zero": N_v0.is_zero(),
    },
    "trichotomy": {
        "rank": rank,
        "description": rank_desc,
        "s_nonzero": s_nonzero,
        "N_nonzero": N_nonzero,
    },
    "golden_reference_form": {
        "sharp_fixed": True, "factor": "-2", "N": "-6", "rank": 3,
        "invertible": True,
    },
    "k020_verdict": k020,
    "form_match": form_match,
    "runtime_s": time.time() - T0,
}
with open(os.path.join(HERE, "b3_results.json"), "w") as f:
    json.dump(out, f, indent=2)
log(f"saved {os.path.join(HERE, 'b3_results.json')}")
log("DONE.")
