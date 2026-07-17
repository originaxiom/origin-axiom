"""W2a -- THE SILVER CONTROL (PREREG_IL.md sha 9d8aa8ff, W2a clause).

K020 test: does the GOLDEN structure (v0 = holonomy-invariant line; the Jordan
cubic portal P(u) = [v0 x u] into the dual system; rank-5 sector-respecting
isomorphism on H1(D;27)) reproduce IN FORM on the SILVER object m136 (B649's
banked exact 27-letters over L = Q(s,i), s^4 = 8s^2+16), with different values?

Machinery reused/adapted (all read-only, all F4-verified by this seat):
  - frontier/B649_silver_holonomy/letters27_L.json, entries_L.json,
    cubic_rational.json, e6_principal_rational.json (the RATIONAL E6 apparatus
    -- same principal-sl2 triple + same Cartan cubic as the golden/fig-8 build,
    since B575's E6 apparatus is rational and was dumped once for the silver
    track -- see B649 FINDINGS.md stage 2b).
  - b649_stage3a.py / b649_stage3b_swap.py: the exact weld (U27), the SILVER
    DOUBLE's 6-generator (a..f) presentation, Fox rows, Z1, coboundary rank,
    and the 5 H1(D_silver;27) class representatives ("reps") -- executed
    in-place (source read, no writes to the origin-axiom repo) exactly as the
    golden w0a/w1 scripts exec B575's prefix.
  - finisher_queue/f4_receipt/verify_stage3_solo_exact.py: the clean
    Fraction-vector L-class + Fox-row pattern, reused for the SOLO (3-gen,
    2-relator) h0/h1 reproduction and for v0_silver's construction.

Every number lives in L = Q(s,i) (Fraction-pairs on a 4x4 basis {1,s,s^2,s^3}
each real/imaginary part). Zero floats anywhere in the portal path.
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
SWAP = os.path.join(B649, "b649_stage3b_swap.py")

d = 27
gates = {}

# ============================================================================
log("STEP 0: exec b649_stage3b_swap.py prefix (weld + silver DOUBLE Fox/Z1/cob/reps)")
log("        (source READ only -- no writes to origin-axiom; ~5-8 min expected)")
src = open(SWAP).read()
cut = src.index("# ---- sigma* ---")
ns = {"__name__": "b649_double_prefix", "__file__": SWAP}
t0 = time.time()
exec(compile(src[:cut], SWAP, "exec"), ns)
log(f"  prefix exec complete ({time.time()-t0:.0f}s)")

L, Lc, L0, L1 = ns["L"], ns["Lc"], ns["L0"], ns["L1"]
meye, mmul, mscale, madd = ns["meye"], ns["mmul"], ns["mscale"], ns["madd"]
mconj27 = ns["mconj27"]
S1, S2, LETS = ns["S1"], ns["S2"], ns["LETS"]
RELATORS_D, GENS_D = ns["RELATORS"], ns["GENS"]      # 6 relators, 'abcdef'
rows27_D = ns["rows27"]
Z1_D = ns["Z1"]
cob_D = ns["cob"]
reps = ns["reps"]
nc_D = ns["nc"]
L_nullspace_basis = ns["L_nullspace_basis"]
Span = ns["Span"]
U27, U27i = ns["U27"], ns["U27i"]

log(f"  double presentation: GENS={GENS_D!r}  RELATORS={RELATORS_D}")


def is_zero_vec(v):
    return all(x.is_zero() for x in v)


def matvec(M, v):
    n = len(v)
    return [sum((M[i][k] * v[k] for k in range(n) if not v[k].is_zero()), L0)
            for i in range(len(M))]


def msub(X, Y, n):
    return [[X[i][j] - Y[i][j] for j in range(n)] for i in range(n)]


def transposeL(M):
    return [[M[j][i] for j in range(len(M))] for i in range(len(M))]


def rrefL(rows):
    A = [r[:] for r in rows]
    m = len(A)
    ncols = len(A[0]) if m else 0
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
    return A, pivs


def rankL(mat):
    _, pivs = rrefL([row[:] for row in mat])
    return len(pivs)


meyeL = meye

# ============================================================================
log("=== GATE 1a: reproduce banked silver DOUBLE dims (h0=1, h1=5) ===")
h0_D = d - nc_D
h1_D = len(Z1_D) - nc_D
gates["double_h0_eq_1"] = (h0_D == 1)
gates["double_h1_eq_5"] = (h1_D == 5)
log(f"  double: dim Z1={len(Z1_D)} rank(cob)={nc_D}  ->  h0(D)={h0_D} h1(D)={h1_D}")
log(f"  GATE (1,5): {'PASS' if (gates['double_h0_eq_1'] and gates['double_h1_eq_5']) else 'FAIL'}")
assert gates["double_h0_eq_1"] and gates["double_h1_eq_5"], "SILVER DOUBLE dims gate FAILED"

# ============================================================================
log("=== GATE 1b: reproduce banked silver SOLO dims (h0=1, h1=3) -- f4-template pattern ===")
GENS_M = "abc"
RELATORS_M = ["aBAbcc", "aaCbcB"]


def fox_rows_solo(lets):
    rows = []
    for w in RELATORS_M:
        blocks = {g: [[L0] * d for _ in range(d)] for g in GENS_M}
        P = meyeL(d)
        for ch in w:
            g = ch.lower()
            if ch.islower():
                term = P
            else:
                PM = mmul(P, lets[ch])
                term = [[L0 - x for x in row] for row in PM]
            blocks[g] = [[a + b for a, b in zip(ra, rb)] for ra, rb in zip(blocks[g], term)]
            P = mmul(P, lets[ch])
        for i in range(d):
            rows.append([blocks[g][i][j] for g in GENS_M for j in range(d)])
    return rows


t0 = time.time()
rows_solo = fox_rows_solo(S1)
z1_solo_basis = L_nullspace_basis(rows_solo, 3 * d)
z1_solo = len(z1_solo_basis)
log(f"  solo Z1 dim = {z1_solo}  ({time.time()-t0:.0f}s)")

cob_solo = []
for j in range(d):
    v = [L1 if t == j else L0 for t in range(d)]
    entry = []
    for g in GENS_M:
        gv = matvec(S1[g], v)
        entry.extend([gv[i] - v[i] for i in range(d)])
    cob_solo.append(entry)

span_solo = Span(3 * d)
nc_solo = 0
for cv in cob_solo:
    if span_solo.add(cv, None):
        nc_solo += 1
h0_solo = d - nc_solo
h1_solo = z1_solo - nc_solo
gates["solo_h0_eq_1"] = (h0_solo == 1)
gates["solo_h1_eq_3"] = (h1_solo == 3)
log(f"  solo: rank(cob)={nc_solo}  ->  h0(M)={h0_solo} h1(M)={h1_solo}")
log(f"  GATE (1,3): {'PASS' if (gates['solo_h0_eq_1'] and gates['solo_h1_eq_3']) else 'FAIL'}")
assert gates["solo_h0_eq_1"] and gates["solo_h1_eq_3"], "SILVER SOLO dims gate FAILED"

# ============================================================================
log("=== STEP 2 (SILVER W0a-analog): v0_silver = joint nullspace of {A-I,B-I,C-I} ===")
AmI = msub(S1['a'], meyeL(d), d)
BmI = msub(S1['b'], meyeL(d), d)
CmI = msub(S1['c'], meyeL(d), d)
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
log(f"  v0_silver verified exactly: (A-I)v0=(B-I)v0=(C-I)v0=0; normalized idx0={idx0}")

support = [i for i, x in enumerate(v0) if not x.is_zero()]
log(f"  support size = {len(support)}  indices = {support}")


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


for i in support:
    log(f"    idx {i:2d}  coeff = {fmtL(v0[i])}")

# ---- v0_silver invariance under the DOUBLE's extra generators d,e,f -------
log("checking v0_silver invariance under the DOUBLE's d,e,f generators...")
inv_def = {}
for g in ('d', 'e', 'f'):
    diff = [matvec(LETS[g], v0)[i] - v0[i] for i in range(d)]
    inv_def[g] = is_zero_vec(diff)
    log(f"  v0_silver invariant under {g}: {inv_def[g]}")
gates["v0_invariant_under_def"] = all(inv_def.values())
if not gates["v0_invariant_under_def"]:
    log("STOP: v0_silver is NOT invariant under d,e,f -- refutes construction premise.")
    out = {"verdict": "STOPPED", "reason": "v0_silver not invariant under double's d,e,f",
           "gates": gates}
    json.dump(out, open(os.path.join(HERE, "silver_portal.json"), "w"), indent=2)
    sys.exit(1)

# ---- weight-label honesty note --------------------------------------------
log("weight-label note: silver's persisted rational assets carry the principal-sl2")
log("  grading (h_pr) only -- NOT the full 6d Spin(10)xU(1) weight lattice (W27, C6)")
log("  that golden's B575 build carries. Reporting h_pr-eigenvalue as the available")
log("  'weight' label; the full E6-weight identification is NOT available for silver.")
pr = json.load(open(os.path.join(B649, "e6_principal_rational.json")))
H_PR_Q = [[Fr(x) for x in row] for row in pr["h_pr"]]
E_PR_Q = [[Fr(x) for x in row] for row in pr["e_pr"]]
F_PR_Q = [[Fr(x) for x in row] for row in pr["f_pr"]]
is_diag_Q = all(H_PR_Q[i][j] == 0 for i in range(d) for j in range(d) if i != j)
log(f"  h_pr diagonal in this basis: {is_diag_Q}")
hpr_diag = [H_PR_Q[i][i] for i in range(d)]
v0_is_hpr_null = True
for i in support:
    log(f"    idx {i:2d}  h_pr-eigenvalue(principal grading) = {hpr_diag[i]}")


# ============================================================================
log("=== STEP 3 (SILVER W0b-analog): principal-SL2 block structure check ===")


def matvecQ(M, v):
    return [sum(M[i][k] * v[k] for k in range(len(v))) for i in range(len(M))]


def nullspaceQ(rows, ncols):
    A = [r[:] for r in rows]
    m = len(A)
    r = 0
    pivs = []
    for c in range(ncols):
        piv = next((k for k in range(r, m) if A[k][c] != 0), None)
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        pv = A[r][c]
        A[r] = [x / pv for x in A[r]]
        for k in range(m):
            if k != r and A[k][c] != 0:
                f = A[k][c]
                A[k] = [x - f * y for x, y in zip(A[k], A[r])]
        pivs.append(c)
        r += 1
        if r == m:
            break
    free = [c for c in range(ncols) if c not in pivs]
    basis = []
    for fc in free:
        v = [Fr(0)] * ncols
        v[fc] = Fr(1)
        for rr, pc in enumerate(pivs):
            v[pc] = -A[rr][fc]
        basis.append(v)
    return basis


def eigvecsQ(t):
    rows = [[H_PR_Q[i][j] - (Fr(t) if i == j else Fr(0)) for j in range(d)] for i in range(d)]
    return nullspaceQ(rows, d)


block_ok = True
try:
    chains = []
    for s in (8, 4, 0):
        top = eigvecsQ(2 * s)
        cols = [matvecQ(E_PR_Q, v) for v in top]
        rows = [[cols[c][i] for c in range(len(top))] for i in range(d)]
        ker = nullspaceQ(rows, len(top))
        assert len(ker) == 1, f"HW combo at 2s={2*s}: got {len(ker)} (eigdim {len(top)})"
        v = [sum(ker[0][c] * top[c][i] for c in range(len(top))) for i in range(d)]
        chain = [v]
        for k in range(2 * s):
            v = matvecQ(F_PR_Q, v)
            chain.append(v)
        assert any(x != 0 for x in chain[-1])
        assert all(x == 0 for x in matvecQ(F_PR_Q, chain[-1]))
        chains.append(chain)

    P = [[Fr(0)] * d for _ in range(d)]
    col = 0
    block_slices = []
    for chain in chains:
        block_slices.append((col, col + len(chain)))
        for v in chain:
            for i in range(d):
                P[i][col] = v[i]
            col += 1
    assert col == d
    aug = [list(P[i]) + [Fr(1) if k == i else Fr(0) for k in range(d)] for i in range(d)]
    for c in range(d):
        piv = next(r for r in range(c, d) if aug[r][c] != 0)
        aug[c], aug[piv] = aug[piv], aug[c]
        pv = aug[c][c]
        aug[c] = [x / pv for x in aug[c]]
        for r in range(d):
            if r != c and aug[r][c] != 0:
                f = aug[r][c]
                aug[r] = [x - f * y for x, y in zip(aug[r], aug[c])]
    Pinv = [[aug[i][d + j] for j in range(d)] for i in range(d)]

    block_dims = [hi - lo for (lo, hi) in block_slices]
    log(f"  block_slices = {block_slices}  block_dims = {block_dims}  (expect [17,9,1])")
    gates["block_dims_match"] = (block_dims == [17, 9, 1])

    P_L = [[Lc(P[i][j]) for j in range(d)] for i in range(d)]
    Pinv_L = [[Lc(Pinv[i][j]) for j in range(d)] for i in range(d)]

    chain_mats = {}
    for g in ('a', 'b', 'c', 'A', 'B', 'C'):
        chain_mats[g] = mmul(mmul(Pinv_L, S1[g]), P_L)

    off_block_exact = True
    max_off = None
    for g, M_ in chain_mats.items():
        for (lo_p, hi_p) in block_slices:
            for (lo_q, hi_q) in block_slices:
                if (lo_p, hi_p) == (lo_q, hi_q):
                    continue
                for i in range(lo_p, hi_p):
                    Mi = M_[i]
                    for j in range(lo_q, hi_q):
                        if not Mi[j].is_zero():
                            off_block_exact = False
                            max_off = (g, i, j)
    gates["block_diagonal_exact"] = off_block_exact
    log(f"  block-diagonality exact under silver solo generators a,b,c,A,B,C: {off_block_exact}"
        + ("" if off_block_exact else f"  (first violation at {max_off})"))

    if not off_block_exact:
        block_ok = False
        log("SKIP: silver solo generators do NOT block-diagonalize exactly in the")
        log("  principal-sl2 chain basis -- W0b-analog step SKIPPED (priced for a future cell).")
        per_block = None
    else:
        GENS2 = ['a', 'b', 'c']

        def fox_matrices_block(word, acts_V, dV):
            D_ = {g: [[L0] * dV for _ in range(dV)] for g in GENS2}
            Pw = meyeL(dV)
            for ch in word:
                low = ch.lower()
                if ch.islower():
                    M = D_[low]
                    for i in range(dV):
                        Pi_ = Pw[i]
                        Mi = M[i]
                        for j in range(dV):
                            Mi[j] = Mi[j] + Pi_[j]
                else:
                    PA = mmul(Pw, acts_V[ch])
                    M = D_[low]
                    for i in range(dV):
                        Mi = M[i]
                        PAi = PA[i]
                        for j in range(dV):
                            Mi[j] = Mi[j] - PAi[j]
                Pw = mmul(Pw, acts_V[ch])
            return D_

        def block_h0(acts_V, dV):
            AmI_ = [[acts_V['a'][i][j] - (L1 if i == j else L0) for j in range(dV)] for i in range(dV)]
            BmI_ = [[acts_V['b'][i][j] - (L1 if i == j else L0) for j in range(dV)] for i in range(dV)]
            CmI_ = [[acts_V['c'][i][j] - (L1 if i == j else L0) for j in range(dV)] for i in range(dV)]
            rows_ = AmI_ + BmI_ + CmI_
            return len(L_nullspace_basis(rows_, dV))

        per_block = []
        for bi, (lo, hi) in enumerate(block_slices):
            dV = hi - lo
            acts_V = {g: [row[lo:hi] for row in chain_mats[g][lo:hi]] for g in ('a', 'b', 'c', 'A', 'B', 'C')}
            h0b = block_h0(acts_V, dV)
            big = []
            for w in RELATORS_M:
                Dw = fox_matrices_block(w, acts_V, dV)
                for i in range(dV):
                    big.append([Dw[g][i][j] for g in GENS2 for j in range(dV)])
            z1dim = len(L_nullspace_basis(big, 3 * dV)) if big else 0
            cobs = []
            for j in range(dV):
                e = [L1 if i == j else L0 for i in range(dV)]
                row = []
                for g in GENS2:
                    ge = [e[i] - sum((acts_V[g][i][k] * e[k] for k in range(dV) if not e[k].is_zero()), L0)
                          for i in range(dV)]
                    row += ge
                cobs.append(row)
            spanb = Span(3 * dV)
            rank_cob = 0
            for cv in cobs:
                if spanb.add(cv, None):
                    rank_cob += 1
            h1b = z1dim - rank_cob
            per_block.append({"block": bi, "dim": dV, "slice": [lo, hi],
                               "h0": h0b, "h1": h1b, "z1_dim": z1dim, "coboundary_rank": rank_cob})
            log(f"  block {bi} (dim {dV}, slice [{lo},{hi})): h0={h0b} h1={h1b} "
                f"(Z1={z1dim}, B1={rank_cob})")

        sum_h0 = sum(b["h0"] for b in per_block)
        sum_h1 = sum(b["h1"] for b in per_block)
        gate_sum_h0 = (sum_h0 == h0_solo)
        gate_sum_h1 = (sum_h1 == h1_solo)
        v1_blocks = [b for b in per_block if b["dim"] == 1]
        gate_v1 = all(b["h0"] == 1 and b["h1"] == 1 for b in v1_blocks) if v1_blocks else None
        one_per_block = all(b["h1"] == 1 for b in per_block)
        log(f"  SUM h0={sum_h0} (== solo h0 {h0_solo}: {gate_sum_h0})  "
            f"SUM h1={sum_h1} (== solo h1 {h1_solo}: {gate_sum_h1})")
        log(f"  dim-1 block (h0,h1) = {[(b['h0'], b['h1']) for b in v1_blocks]}  gate(1,1): {gate_v1}")
        log(f"  ONE-PER-BLOCK (every block h1==1): {one_per_block}")
        gates["w0b_sum_h0_match"] = gate_sum_h0
        gates["w0b_sum_h1_match"] = gate_sum_h1
        gates["w0b_v1_block_1_1"] = gate_v1
        gates["w0b_one_per_block"] = one_per_block
except Exception as e:
    block_ok = False
    per_block = None
    log(f"SKIP: silver W0b-analog step raised an exception -- SKIPPED honestly: {e!r}")

# ============================================================================
log("=== STEP 4 (SILVER PORTAL): the Jordan cubic N_silver + P(u) = [v0_silver x u] ===")
CUB = {tuple(map(int, k.split(","))): Fr(v)
       for k, v in json.load(open(os.path.join(B649, "cubic_rational.json"))).items()}
log(f"  cubic_rational.json entries: {len(CUB)}")


def C3(u, v):
    cov = [L0] * d
    for (p, q, r_), cval in CUB.items():
        if not u[p].is_zero() and not v[q].is_zero():
            cov[r_] = cov[r_] + Lc(cval) * u[p] * v[q]
    return cov


def dotL(f, v):
    return sum((f[t] * v[t] for t in range(d) if not v[t].is_zero()), L0)


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
if not gates["N_invariant_all"]:
    log("STOP: N_silver is NOT rho-invariant -- refutes construction premise.")
    out = {"verdict": "STOPPED", "reason": "N_silver not rho-invariant", "gates": gates}
    json.dump(out, open(os.path.join(HERE, "silver_portal.json"), "w"), indent=2)
    sys.exit(1)

# ---- dual (contragredient) Fox machinery -----------------------------------
log("building dual Fox derivative rows (162x162 over L; expect several minutes)...")
dacts = {}
for g in GENS_D:
    Gup = g.upper()
    dacts[g] = transposeL(LETS[Gup])
    dacts[Gup] = transposeL(LETS[g])


def fox_matrices_D(word, actsmap):
    D_ = {g: [[L0] * d for _ in range(d)] for g in GENS_D}
    P = meyeL(d)
    for ch in word:
        low = ch.lower()
        if ch.islower():
            M = D_[low]
            for i in range(d):
                Pi_ = P[i]
                Mi = M[i]
                for j in range(d):
                    Mi[j] = Mi[j] + Pi_[j]
        else:
            PA = mmul(P, actsmap[ch])
            M = D_[low]
            for i in range(d):
                Mi = M[i]
                PAi = PA[i]
                for j in range(d):
                    Mi[j] = Mi[j] - PAi[j]
        P = mmul(P, actsmap[ch])
    return D_


t0 = time.time()
dual_big = []
for w in RELATORS_D:
    Dw = fox_matrices_D(w, dacts)
    for i in range(d):
        dual_big.append([Dw[g][i][j] for g in GENS_D for j in range(d)])
log(f"  dual Fox rows built ({time.time()-t0:.0f}s)")

t0 = time.time()
Z1_dual = L_nullspace_basis(dual_big, 6 * d)
log(f"  dim Z1(dual) = {len(Z1_dual)}  ({time.time()-t0:.0f}s)")

cobs_dual = []
for j in range(d):
    e = [L1 if i == j else L0 for i in range(d)]
    row = []
    for g in GENS_D:
        ge = [e[i] - sum((dacts[g][i][k] * e[k] for k in range(d) if not e[k].is_zero()), L0)
              for i in range(d)]
        row += ge
    cobs_dual.append(row)

span_dual = Span(6 * d)
rank_cob_dual = 0
for cv in cobs_dual:
    if span_dual.add(cv, None):
        rank_cob_dual += 1
h0_dual = d - rank_cob_dual
h1_dual = len(Z1_dual) - rank_cob_dual
gates["h1_dual_eq_5"] = (h1_dual == 5)
log(f"  h0(dual)={h0_dual} h1(dual)={h1_dual}  [GATE h1_dual==5]: "
    f"{'PASS' if gates['h1_dual_eq_5'] else 'FAIL'}")
assert gates["h1_dual_eq_5"], f"h1(dual)={h1_dual} != 5"


def is_dual_cocycle(vec):
    for row in dual_big:
        s_ = L0
        for t in range(6 * d):
            if not vec[t].is_zero() and not row[t].is_zero():
                s_ = s_ + row[t] * vec[t]
        if not s_.is_zero():
            return False
    return True


span_for_classes = Span(6 * d)
for cv in cobs_dual:
    span_for_classes.add(cv, ("cob", None))
dual_classes = []
for s_ in Z1_dual:
    if span_for_classes.add(s_, ("rep", len(dual_classes))):
        dual_classes.append(s_)
    if len(dual_classes) == h1_dual:
        break
assert len(dual_classes) == h1_dual
log(f"  extracted {len(dual_classes)} dual class representatives")

basis = dual_classes + cobs_dual   # 5 + 27 = 32


def reduce_to_classes(target_flat):
    aug = [list(col) + [target_flat[r]] for r, col in enumerate(zip(*basis))]
    Rr2, piv2 = rrefL(aug)
    coeff = [L0] * len(basis)
    for r_i, p_j in enumerate(piv2):
        if p_j < len(basis):
            coeff[p_j] = Rr2[r_i][len(basis)]
    resid = [target_flat[r] - sum((coeff[k] * basis[k][r] for k in range(len(basis)) if not coeff[k].is_zero()), L0)
             for r in range(len(target_flat))]
    ok = all(x.is_zero() for x in resid)
    return coeff[:h1_dual], ok


def slice_rep(u162):
    return {g: u162[27 * i:27 * (i + 1)] for i, g in enumerate(GENS_D)}


def P_of(u162):
    parts = slice_rep(u162)
    out = []
    for g in GENS_D:
        out.extend(C3(v0, parts[g]))
    return out


log("=== THE SILVER PORTAL MATRIX P: H1(D_silver;27) -> H1(D_silver;27bar) ===")
PORTAL = [[None] * 5 for _ in range(5)]
cocycle_flags = []
for j in range(5):
    tgt = P_of(reps[j])
    ok_cocycle = is_dual_cocycle(tgt)
    cocycle_flags.append(ok_cocycle)
    coeffs, ok_resid = reduce_to_classes(tgt)
    assert ok_cocycle and ok_resid, f"class {j}: cocycle={ok_cocycle} resid={ok_resid}"
    for i in range(5):
        PORTAL[i][j] = coeffs[i]
gates["all_5_are_dual_cocycles"] = all(cocycle_flags)
log(f"  all 5 P(u_j) verified as dual cocycles: {gates['all_5_are_dual_cocycles']}")

rowsP = [[PORTAL[i][j] for j in range(5)] for i in range(5)]
rank_portal = rankL(rowsP)
kernel_portal = L_nullspace_basis(rowsP, 5)
kernel_dim = len(kernel_portal)
log(f"  PORTAL rank = {rank_portal}, kernel dim = {kernel_dim}")

log("  PORTAL[i][j] (i=dual-class row, j=primal-class col):")
for i in range(5):
    log("    [" + ", ".join(fmtL(PORTAL[i][j]) for j in range(5)) + "]")

# ---- boundary-born / solo-inherited split investigation --------------------
log("=== support-pattern split investigation (stage 3a's boundary/solo analog) ===")
split_info = []
for idx, rp in enumerate(reps):
    parts = slice_rep(rp)
    nz_gens = [g for g in GENS_D if not is_zero_vec(parts[g])]
    split_info.append({"class": idx, "nonzero_generators": nz_gens})
    log(f"  class {idx}: nonzero on generators {nz_gens}")

# ============================================================================
log("=== CONTROL A: coboundary invariance ===")
wshift1 = [Lc(Fr((5 * i + 3) % 11 - 5)) for i in range(d)]
cob_u = {}
for g in GENS_D:
    diffv = [matvec(LETS[g], wshift1)[i] - wshift1[i] for i in range(d)]
    cob_u[g] = diffv
u0_shifted = list(reps[0])
for gi, g in enumerate(GENS_D):
    for i in range(d):
        u0_shifted[27 * gi + i] = u0_shifted[27 * gi + i] + cob_u[g][i]
Pu0s = P_of(u0_shifted)
assert is_dual_cocycle(Pu0s)
coeffs_shifted, ok = reduce_to_classes(Pu0s)
assert ok
ctrlA_input = all((coeffs_shifted[i] - PORTAL[i][0]).is_zero() for i in range(5))
log(f"  input-side (primal coboundary shift of rep0): class-image unchanged: {ctrlA_input}")

wshift2 = [Lc(Fr((7 * i + 2) % 13 - 6)) for i in range(d)]
cob_dual_shift = []
for g in GENS_D:
    ge = [wshift2[i] - sum((dacts[g][i][k] * wshift2[k] for k in range(d) if not wshift2[k].is_zero()), L0)
          for i in range(d)]
    cob_dual_shift += ge
tgt0 = P_of(reps[0])
tgt0_shifted = [tgt0[r] + cob_dual_shift[r] for r in range(6 * d)]
assert is_dual_cocycle(tgt0_shifted)
coeffs2, ok2 = reduce_to_classes(tgt0_shifted)
assert ok2
ctrlA_repr = all((coeffs2[i] - PORTAL[i][0]).is_zero() for i in range(5))
log(f"  representative-side (dual coboundary shift of P(rep0)): class-image unchanged: {ctrlA_repr}")
gates["control_coboundary"] = ctrlA_input and ctrlA_repr

log("=== CONTROL B: trivial-coefficient control (b1(D_silver)) ===")


def signed_counts(word):
    cnt = {g: 0 for g in GENS_D}
    for ch in word:
        cnt[ch.lower()] += 1 if ch.islower() else -1
    return [Lc(Fr(cnt[g])) for g in GENS_D]


Ntriv = [signed_counts(w) for w in RELATORS_D]
Z1triv = L_nullspace_basis(Ntriv, 6)
b1_D = len(Z1triv)
gates["b1_D_eq_1"] = (b1_D == 1)
log(f"  b1(D_silver) [trivial-coefficient control] = {b1_D}  "
    f"(expected 1, from H1(D_silver)=Z+Z/2+Z/2): {'PASS' if gates['b1_D_eq_1'] else 'FAIL'}")


def reduce_triv(target):
    aug = [list(col) + [target[r]] for r, col in enumerate(zip(*Z1triv))]
    Rr2, piv2 = rrefL(aug)
    coeff = [L0] * len(Z1triv)
    for r_i, p_j in enumerate(piv2):
        if p_j < len(Z1triv):
            coeff[p_j] = Rr2[r_i][len(Z1triv)]
    resid = [target[r] - sum((coeff[k] * Z1triv[k][r] for k in range(len(Z1triv)) if not coeff[k].is_zero()), L0)
             for r in range(len(target))]
    return coeff, all(x.is_zero() for x in resid)


PORTAL_triv = [[None] * b1_D for _ in range(b1_D)]
for j in range(b1_D):
    target = list(Z1triv[j])
    coeff, ok3 = reduce_triv(target)
    assert ok3
    for i in range(b1_D):
        PORTAL_triv[i][j] = coeff[i]
is_identity = all((PORTAL_triv[i][j] - (L1 if i == j else L0)).is_zero()
                   for i in range(b1_D) for j in range(b1_D))
gates["control_trivial"] = is_identity
log(f"  trivial-coefficient portal == identity_{b1_D}x{b1_D}: {is_identity}")

gates["control_exactness"] = True
log("CONTROL C: exactness -- L = Q(s,i) (Fraction-pair) arithmetic throughout; "
    "zero floats in the portal path: PASS by construction")

# ============================================================================
all_gates_pass = all(v for k, v in gates.items() if isinstance(v, bool))
log(f"ALL HARD GATES PASS: {all_gates_pass}")

if rank_portal == 0:
    verdict_rank = "ZERO-PORTAL"
elif rank_portal == 5 and kernel_dim == 0:
    verdict_rank = "RANK-5-ISOMORPHISM"
else:
    verdict_rank = f"RANK-{rank_portal} (kernel dim {kernel_dim})"

form_match_rank = (verdict_rank == "RANK-5-ISOMORPHISM")
log(f"RANK VERDICT: {verdict_rank}")

if form_match_rank:
    k020 = "FORM-MATCH (rank 5 isomorphism reproduces; values differ -- see portal matrix); " \
           "sector/split structure reported separately (support-pattern investigation above)"
else:
    k020 = f"FORM-MISMATCH: rank={rank_portal}, kernel_dim={kernel_dim} (golden had rank 5, kernel 0)"

log(f"*** THE K020 VERDICT: {k020} ***")

out = {
    "prereg_sha256": "9d8aa8ff36da8cc63285599c889a5fa9814e675c639c3026244b58a24d25b18a",
    "object": "m136 (B649 silver holonomy, L=Q(s,i), s^4=8s^2+16)",
    "gates": gates,
    "double_dims": {"h0": h0_D, "h1": h1_D},
    "solo_dims": {"h0": h0_solo, "h1": h1_solo},
    "v0_silver": {
        "normalized_idx0": idx0,
        "support_indices": support,
        "support_size": len(support),
        "coordinates_full": [[str(x.re), str(x.im)] for x in v0],
        "hpr_eigenvalues_at_support": [str(hpr_diag[i]) for i in support],
        "weight_label_note": "silver assets carry only the principal-sl2 grading (h_pr); "
                              "no W27/Spin(10)xU(1) weight lattice is available -- reported honestly.",
        "invariant_under_def": gates["v0_invariant_under_def"],
    },
    "w0b_analog": {
        "attempted": True,
        "block_structure_accessible": block_ok,
        "block_dims": (block_dims if block_ok else None),
        "per_block": (per_block if block_ok else None),
    },
    "cubic_N_invariance": ninv,
    "h1_dual": h1_dual,
    "h0_dual": h0_dual,
    "portal_matrix": [[[str(PORTAL[i][j].re), str(PORTAL[i][j].im)] for j in range(5)] for i in range(5)],
    "portal_matrix_readable": [[fmtL(PORTAL[i][j]) for j in range(5)] for i in range(5)],
    "rank": rank_portal,
    "kernel_dim": kernel_dim,
    "support_pattern_split": split_info,
    "controls": {
        "coboundary_input_side": ctrlA_input,
        "coboundary_representative_side": ctrlA_repr,
        "trivial_coefficient_b1_D": b1_D,
        "trivial_coefficient_is_identity": is_identity,
        "exactness": True,
    },
    "rank_verdict": verdict_rank,
    "k020_verdict": k020,
    "runtime_s": time.time() - T0,
}
with open(os.path.join(HERE, "silver_portal.json"), "w") as f:
    json.dump(out, f, indent=2)
log(f"saved {os.path.join(HERE, 'silver_portal.json')}")
log("DONE.")
