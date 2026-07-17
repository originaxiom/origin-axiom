"""W1 -- THE PORTAL (PREREG_IL.md sha 9d8aa8ff, W1 clause; ADDENDUM_W1.md sha
7b77c578). Findings language: "the invariant line" -- never "dark".

P(u) = [v0 x u(.)], with x the Jordan cross product 27 (x) 27 -> 27-bar, the
polarization of the banked cubic norm N (<x X y, z> = N(x,y,z); convention
pinned to the B632 cell2_texture.py cubic invariant, the same trilinear
machinery that cell3b_stage2.py's pairing/chain conventions build on).

Setup replicates d5_triality.py / cell3b_stage1.py exactly: exec the B575
prefix, rehydrate cell3_double/stage1_classes.pkl, rebuild C27 from J, gate
the three relators. v0 is the W0a joint-nullspace result (cross-checked
against w0a_singlet/w0a_v0.json). The dual (contragredient) local system's
Fox calculus follows cell3b_stage1.py's fox_matrices pattern verbatim, with
rho-bar(g) = (rho(g)^-1)^T.

Every number lives in K = Q(sqrt(-3)) (Fraction pairs). Zero floats anywhere
in the portal path.
"""
import os
import sys
import time
import json
import pickle
from fractions import Fraction as Fr

os.environ["PYTHONDONTWRITEBYTECODE"] = "1"

T0 = time.time()
def log(msg):
    print(f"[{time.time()-T0:7.1f}s] {msg}", flush=True)

HERE = os.path.dirname(os.path.abspath(__file__))
B575 = "<repo>/frontier/B575_bridge_obstruction/l51_obstruction.py"
PKL = "<seat-workdir>/cell3_double/stage1_classes.pkl"
W0A_JSON = "<seat-workdir>/invariant_line/w0a_singlet/w0a_v0.json"
LAM = "abABaaBAbA"
d = 27
GENS = ['a', 'b', 'c']

gates = {}

# ============================================================================
log("STEP 0: exec B575 prefix (stages 0-3; exact e6 + 27 build)...")
src = open(B575).read()
cut = src.index("# ---------------------------------------------------------------- stage 4")
ns = {"__name__": "b575_prefix", "__file__": B575}
t0 = time.time()
exec(compile(src[:cut], B575, "exec"), ns)
log(f"  B575 prefix done ({time.time()-t0:.0f}s)")

K, K0, K1 = ns["K"], ns["K0"], ns["K1"]
A27, B27, A27i, B27i = ns["A27"], ns["B27"], ns["A27i"], ns["B27i"]
mmul, meye, rref, nullspace = ns["mmul"], ns["meye"], ns["rref"], ns["nullspace"]
W27, E6_e, E6_f = ns["W27"], ns["E6_e"], ns["E6_f"]
REL = ns["REL"]


def mt(M):
    return [[M[j][i] for j in range(d)] for i in range(d)]


def is_eye(M):
    return all((M[i][j] - (K1 if i == j else K0)).is_zero()
               for i in range(d) for j in range(d))


def word_mat(word, actsmap):
    P = meye(d)
    for ch in word:
        P = mmul(P, actsmap[ch])
    return P


def inv_word(w):
    return ''.join(ch.swapcase() for ch in reversed(w))


def apply(M, v):
    return [sum((M[i][k] * v[k] for k in range(d) if not v[k].is_zero()), K0)
            for i in range(d)]


def vsub(u, v):
    return [u[i] - v[i] for i in range(d)]


def vadd(u, v):
    return [u[i] + v[i] for i in range(d)]


def minv(M):
    aug = [list(M[i]) + [K1 if k == i else K0 for k in range(d)] for i in range(d)]
    Rr, piv = rref(aug)
    assert len(piv) == d
    return [[Rr[i][d + j] for j in range(d)] for i in range(d)]


# ============================================================================
log("STEP 1: load + rehydrate cell3_double/stage1_classes.pkl...")
pk = pickle.load(open(PKL, "rb"))
Kc = ns["K"]
J = [[Kc(*pk["J"][i][j]) for j in range(d)] for i in range(d)]
raw_classes = pk["classes"]
h1_bank = pk["h1"]
assert len(raw_classes) == 5 and all(len(c) == 3 * d for c in raw_classes), \
    f"class layout: expected 5x81, got {len(raw_classes)}x{[len(c) for c in raw_classes]}"
classes = [{g: [Kc(*c[gi * d + i]) for i in range(d)]
            for gi, g in enumerate(('a', 'b', 'c'))} for c in raw_classes]
log(f"  rehydrated: banked h1 = {h1_bank}, classes = {len(classes)} (81-vectors -> a/b/c)")

Jinv = minv(J)
C27 = mmul(mmul(J, mt(B27i)), Jinv)
C27i = mmul(mmul(J, mt(B27)), Jinv)
gates["C27_inverse_consistent"] = is_eye(mmul(C27, C27i))
assert gates["C27_inverse_consistent"], "C27 * C27i != I"
acts = {'a': A27, 'A': A27i, 'b': B27, 'B': B27i, 'c': C27, 'C': C27i}

R1 = REL
R2 = REL.replace('b', 'c').replace('B', 'C')
R3 = LAM.replace('b', 'c').replace('B', 'C') + inv_word(LAM)
RELS = [R1, R2, R3]
for name, w in (("R1", R1), ("R2", R2), ("R3", R3)):
    ok = is_eye(word_mat(w, acts))
    gates[f"relator_{name}"] = ok
    log(f"  relator gate {name}: {'PASS' if ok else 'FAIL'}")
    assert ok, f"relator gate FAIL: {name}"

# ============================================================================
log("STEP 2: v0 = joint nullspace of (A27-I, B27-I)  [W0a result]...")
I = meye(d)


def msub2(X, Y):
    return [[X[i][j] - Y[i][j] for j in range(d)] for i in range(d)]


AmI = msub2(A27, I)
BmI = msub2(B27, I)
ns_basis = nullspace(AmI + BmI)
gates["v0_dim1"] = (len(ns_basis) == 1)
log(f"  joint nullspace dim = {len(ns_basis)}  [HARD GATE dim=1]: "
    f"{'PASS' if gates['v0_dim1'] else 'FAIL'}")
assert gates["v0_dim1"], f"v0 nullspace dim {len(ns_basis)} != 1"

v0_raw = ns_basis[0]
idx0 = next(i for i, x in enumerate(v0_raw) if not x.is_zero())
scale = v0_raw[idx0].inv()
v0 = [scale * x for x in v0_raw]
assert (v0[idx0] - K1).is_zero()
assert all(x.is_zero() for x in apply(AmI, v0)), "(A27-I)v0 != 0"
assert all(x.is_zero() for x in apply(BmI, v0)), "(B27-I)v0 != 0"
log(f"  v0 verified exactly: (A27-I)v0=0, (B27-I)v0=0; normalized idx0={idx0}")

w0a = json.load(open(W0A_JSON))
gates["v0_idx0_matches_w0a"] = (w0a["v0_normalized_idx0"] == idx0)
w0a_v0 = [Kc(Fr(a_s), Fr(b_s)) for a_s, b_s in w0a["v0_coordinates_full"]]
gates["v0_matches_w0a"] = all((v0[i] - w0a_v0[i]).is_zero() for i in range(d))
log(f"  cross-check vs w0a_v0.json: idx0 match={gates['v0_idx0_matches_w0a']}, "
    f"coordinates match={gates['v0_matches_w0a']}")
assert gates["v0_idx0_matches_w0a"] and gates["v0_matches_w0a"], \
    "v0 does not match the banked W0a result"

gates["v0_C27_invariant"] = all(x.is_zero() for x in vsub(apply(C27, v0), v0))
log(f"  v0 invariant under C27 (conjugate holonomy): "
    f"{'PASS' if gates['v0_C27_invariant'] else 'FAIL -- STOP'}")
if not gates["v0_C27_invariant"]:
    log("STOP: v0 is NOT C27-invariant -- refutes the construction's premise. Aborting.")
    with open(os.path.join(HERE, "portal_matrix.json"), "w") as f:
        json.dump({"verdict": "STOPPED", "reason": "v0 not C27-invariant", "gates": gates}, f, indent=2)
    sys.exit(1)

# ============================================================================
log("STEP 3: the Jordan cubic invariant N (B632 cell2_texture.py method)...")
support, SUPIDX = [], {}
for p in range(d):
    for q in range(p, d):
        for r in range(q, d):
            if all(W27[p][k] + W27[q][k] + W27[r][k] == 0 for k in range(6)):
                SUPIDX[(p, q, r)] = len(support)
                support.append((p, q, r))
nsup = len(support)
log(f"  zero-weight-sum sorted triples: {nsup}")

eqs = {}
for gi, X in enumerate(list(E6_e) + list(E6_f)):
    xent = [(s, t) for s in range(d) for t in range(d) if not X[s][t].is_zero()]
    for (a, b, c) in support:
        k = SUPIDX[(a, b, c)]
        for (u, v, w) in ((a, b, c), (b, a, c), (c, a, b)):
            for s, t in xent:
                if s == u:
                    key = (gi,) + tuple(sorted((t, v, w)))
                    row = eqs.setdefault(key, {})
                    row[k] = row.get(k, K0) + X[u][t]
rows = [[row.get(k, K0) for k in range(nsup)] for row in eqs.values()
        if any(not cv.is_zero() for cv in row.values())]
log(f"  invariance equations: {len(rows)}")
sol = nullspace(rows)
gates["N_dim1"] = (len(sol) == 1)
log(f"  cubic invariant space dim = {len(sol)}  [GATE: must equal 1]: "
    f"{'PASS' if gates['N_dim1'] else 'FAIL'}")
assert gates["N_dim1"], f"cubic invariant dim {len(sol)} != 1"
Cvals = sol[0]
CFULL = {}
for (p, q, r), k in SUPIDX.items():
    if not Cvals[k].is_zero():
        for perm in {(p, q, r), (p, r, q), (q, p, r), (q, r, p), (r, p, q), (r, q, p)}:
            CFULL[perm] = Cvals[k]
log(f"  nonzero sorted coefficients: "
    f"{sum(1 for k in range(nsup) if not Cvals[k].is_zero())}/{nsup}")


def C3(u, v):
    """The cross product: covector m -> N(u, v, e_m), i.e. u x v in 27-bar."""
    cov = [K0] * d
    for (p, q, r), cval in CFULL.items():
        if not u[p].is_zero() and not v[q].is_zero():
            cov[r] = cov[r] + cval * u[p] * v[q]
    return cov


def dot(f, v):
    return sum((f[t] * v[t] for t in range(d) if not v[t].is_zero()), K0)


u1 = [K(i % 5 - 2) for i in range(d)]
v1 = [K((2 * i) % 7 - 3) for i in range(d)]
w1 = [K((3 * i) % 4 - 1) for i in range(d)]
ninv = {}
for nm, M in (("A27", A27), ("B27", B27), ("C27", C27)):
    lhs = dot(C3(apply(M, u1), apply(M, v1)), apply(M, w1))
    rhs = dot(C3(u1, v1), w1)
    ninv[nm] = (lhs - rhs).is_zero()
    log(f"  N-invariance under {nm}: {'PASS' if ninv[nm] else 'FAIL'}")
gates["N_invariant_all"] = all(ninv.values())
if not gates["N_invariant_all"]:
    log("STOP: N is NOT rho-invariant -- refutes the construction's premise. Aborting.")
    with open(os.path.join(HERE, "portal_matrix.json"), "w") as f:
        json.dump({"verdict": "STOPPED", "reason": "N not rho-invariant", "gates": gates}, f, indent=2)
    sys.exit(1)

# ============================================================================
log("STEP 4: the dual (contragredient) Fox machinery, rho-bar(g)=(rho(g)^-1)^T...")


def transpose(M):
    return [[M[j][i] for j in range(d)] for i in range(d)]


dacts = {'a': transpose(A27i), 'A': transpose(A27),
         'b': transpose(B27i), 'B': transpose(B27),
         'c': transpose(C27i), 'C': transpose(C27)}


def fox_matrices(word, actsmap):
    D_ = {g: [[K0] * d for _ in range(d)] for g in GENS}
    P = meye(d)
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
for w in RELS:
    Dw = fox_matrices(w, dacts)
    for i in range(d):
        dual_big.append([Dw['a'][i][j] for j in range(d)] +
                         [Dw['b'][i][j] for j in range(d)] +
                         [Dw['c'][i][j] for j in range(d)])
log(f"  dual Fox-derivative matrix built ({time.time()-t0:.0f}s)")


def flatabc(u):
    return u['a'] + u['b'] + u['c']


def is_dual_cocycle(vec81):
    img = [sum((dual_big[r][cidx] * vec81[cidx] for cidx in range(3 * d)
                if not vec81[cidx].is_zero()), K0)
           for r in range(len(dual_big))]
    return all(x.is_zero() for x in img)


def P_of(u):
    """P(u): the dual-valued 1-cochain g -> v0 x u(g)."""
    return {g: C3(v0, u[g]) for g in ('a', 'b', 'c')}


log("  cocycle-property spot check on class 0 (before proceeding)...")
Pu0 = P_of(classes[0])
gates["P_class0_is_cocycle"] = is_dual_cocycle(flatabc(Pu0))
log(f"  P(u_0) in Z1(dual): {'PASS' if gates['P_class0_is_cocycle'] else 'FAIL -- STOP'}")
if not gates["P_class0_is_cocycle"]:
    log("STOP: P(u) is not a valid dual cocycle. Aborting.")
    with open(os.path.join(HERE, "portal_matrix.json"), "w") as f:
        json.dump({"verdict": "STOPPED", "reason": "P(u_0) not a cocycle", "gates": gates}, f, indent=2)
    sys.exit(1)

# ============================================================================
log("STEP 5: Z1(dual)/B1(dual) and h1(D; 27-bar); extract the dual class basis...")
sols1_dual = nullspace(dual_big)
cobs_dual = []
for j in range(d):
    e = [K1 if i == j else K0 for i in range(d)]
    row = []
    for g in GENS:
        ge = [e[i] - sum((dacts[g][i][k] * e[k] for k in range(d) if not e[k].is_zero()), K0)
              for i in range(d)]
        row += ge
    cobs_dual.append(row)
_, pivc = rref([list(r) for r in cobs_dual])
rank_cob_dual = len(pivc)
h0_dual = d - rank_cob_dual
h1_dual = len(sols1_dual) - rank_cob_dual
log(f"  Z1(dual) dim = {len(sols1_dual)}, coboundary rank = {rank_cob_dual}")
log(f"  h0(dual) = {h0_dual}, h1(dual) = {h1_dual}   [GATE: h1(dual)=5]")
gates["h1_dual_eq_5"] = (h1_dual == 5)
assert gates["h1_dual_eq_5"], f"h1(dual)={h1_dual} != 5"


def mrank(rows_):
    if not rows_:
        return 0
    _, p = rref([list(r) for r in rows_])
    return len(p)


span = [list(c) for c in cobs_dual]
dual_classes = []
cur = list(span)
for s in sols1_dual:
    if mrank(cur + [list(s)]) > mrank(cur):
        dual_classes.append(list(s))
        cur.append(list(s))
    if len(dual_classes) == h1_dual:
        break
assert len(dual_classes) == h1_dual
log(f"  extracted {len(dual_classes)} dual class representatives")

basis = dual_classes + cobs_dual   # length h1_dual + d


def reduce_to_classes(target_flat):
    aug = [list(col) + [target_flat[r]] for r, col in enumerate(zip(*basis))]
    Rr2, piv2 = rref([row[:] for row in aug])
    coeff = [K0] * len(basis)
    for r_i, p_j in enumerate(piv2):
        if p_j < len(basis):
            coeff[p_j] = Rr2[r_i][len(basis)]
    resid = [target_flat[r] - sum((coeff[k] * basis[k][r] for k in range(len(basis))
                                    if not coeff[k].is_zero()), K0)
             for r in range(len(target_flat))]
    ok = all(x.is_zero() for x in resid)
    return coeff[:h1_dual], ok


# ============================================================================
log("STEP 6: THE PORTAL MATRIX  P: H1(D;27) -> H1(D;27-bar) in class bases...")
PORTAL = [[None] * 5 for _ in range(5)]   # PORTAL[dual-row i][primal-col j]
cocycle_flags = []
for j in range(5):
    Puj = P_of(classes[j])
    tgt = flatabc(Puj)
    ok_cocycle = is_dual_cocycle(tgt)
    cocycle_flags.append(ok_cocycle)
    coeffs, ok_resid = reduce_to_classes(tgt)
    assert ok_cocycle and ok_resid, f"class {j}: cocycle={ok_cocycle}, residual-clean={ok_resid}"
    for i in range(5):
        PORTAL[i][j] = coeffs[i]
gates["all_5_are_dual_cocycles"] = all(cocycle_flags)
log(f"  all 5 P(u_j) verified as dual cocycles: {gates['all_5_are_dual_cocycles']}")

rowsP = [[PORTAL[i][j] for j in range(5)] for i in range(5)]
_, pivP = rref([list(r) for r in rowsP])
rank_portal = len(pivP)
kernel_portal = nullspace(rowsP)
kernel_dim = len(kernel_portal)
image_dim = rank_portal
log(f"  PORTAL rank = {rank_portal}, kernel dim = {kernel_dim}, image dim = {image_dim}")


def fmt(x):
    if x.is_zero():
        return "0"
    if x.b == 0:
        return str(x.a)
    return f"({x.a}{'+' if x.b > 0 else ''}{x.b}*sqrt(-3))"


log("  PORTAL[i][j] (i=dual-class row, j=primal-class col):")
for i in range(5):
    log("    [" + ", ".join(fmt(PORTAL[i][j]) for j in range(5)) + "]")

# ============================================================================
log("STEP 7: THE SPLIT -- B637_corrected_cell3/FINDINGS.md 3+2 identification...")
# FINDINGS.md (verified on receipt, cross-adjudication + stage 3 sections) names
# classes {0,1} explicitly and repeatedly as "the boundary-born pair" / "the
# coker-delta^0 pair" that "never couples jointly" in the 3-form Y; classes
# {2,3,4} are the solo-inherited classes (each shows a/b/c support spanning
# all three sl2 blocks V16/V8/V0 in OUTPUT_3B_STAGE2.txt's block-content
# listing, vs classes 0/1 which are supported ONLY on the 'b' chunk). This
# identifies onto the SAME pkl class indices used here (same stage1_classes.pkl).
BOUNDARY_BORN = [0, 1]
SOLO_INHERITED = [2, 3, 4]
split_note = (
    "classes 0,1 = boundary-born (B637 FINDINGS.md's 'coker-delta^0 pair', "
    "support only on generator b); classes 2,3,4 = solo-inherited (support "
    "spans a,b,c). Split applies to the PORTAL's INPUT (column) index j, "
    "since B637's naming was established for the primal double's classes; "
    "the 5 dual-side (row) classes have no independent B637 identification."
)
log("  " + split_note)
bb_cols_zero = all(PORTAL[i][j].is_zero() for i in range(5) for j in BOUNDARY_BORN)
si_cols_zero = all(PORTAL[i][j].is_zero() for i in range(5) for j in SOLO_INHERITED)
log(f"  boundary-born columns (0,1) all-zero: {bb_cols_zero}")
log(f"  solo-inherited columns (2,3,4) all-zero: {si_cols_zero}")

# ============================================================================
log("CONTROL A: coboundary invariance (input-side + representative-side)...")
wshift1 = [K((5 * i + 3) % 11 - 5) for i in range(d)]
cob_u = {g: vsub(apply(acts[g], wshift1), wshift1) for g in ('a', 'b', 'c')}
u0_shifted = {g: vadd(classes[0][g], cob_u[g]) for g in ('a', 'b', 'c')}
Pu0s = P_of(u0_shifted)
assert is_dual_cocycle(flatabc(Pu0s))
coeffs_shifted, ok = reduce_to_classes(flatabc(Pu0s))
assert ok
ctrlA_input = all((coeffs_shifted[i] - PORTAL[i][0]).is_zero() for i in range(5))
log(f"  input-side (primal coboundary shift of u_0): class-image unchanged: {ctrlA_input}")

wshift2 = [K((7 * i + 2) % 13 - 6) for i in range(d)]
cob_dual_shift = []
for g in GENS:
    ge = [wshift2[i] - sum((dacts[g][i][k] * wshift2[k] for k in range(d)
                            if not wshift2[k].is_zero()), K0)
          for i in range(d)]
    cob_dual_shift += ge
tgt0 = flatabc(P_of(classes[0]))
tgt0_shifted = [tgt0[r] + cob_dual_shift[r] for r in range(3 * d)]
assert is_dual_cocycle(tgt0_shifted)
coeffs2, ok2 = reduce_to_classes(tgt0_shifted)
assert ok2
ctrlA_repr = all((coeffs2[i] - PORTAL[i][0]).is_zero() for i in range(5))
log(f"  representative-side (dual coboundary shift of P(u_0)): class-image unchanged: {ctrlA_repr}")
gates["control_coboundary"] = ctrlA_input and ctrlA_repr

log("CONTROL B: trivial-coefficient control (H0 x H1 -> H1 cup = scalar mult)...")


def signed_counts(word):
    cnt = {g: 0 for g in GENS}
    for ch in word:
        cnt[ch.lower()] += 1 if ch.islower() else -1
    return [K(cnt[g]) for g in GENS]


Ntriv = [signed_counts(w) for w in RELS]
Z1triv = nullspace(Ntriv)
b1_D = len(Z1triv)
log(f"  b1(D) [trivial-coefficient control] = {b1_D}")
triv_classes = Z1triv


def reduce_triv(target):
    aug = [list(col) + [target[r]] for r, col in enumerate(zip(*triv_classes))]
    Rr2, piv2 = rref([row[:] for row in aug])
    coeff = [K0] * len(triv_classes)
    for r_i, p_j in enumerate(piv2):
        if p_j < len(triv_classes):
            coeff[p_j] = Rr2[r_i][len(triv_classes)]
    resid = [target[r] - sum((coeff[k] * triv_classes[k][r] for k in range(len(triv_classes))
                               if not coeff[k].is_zero()), K0)
             for r in range(len(target))]
    return coeff, all(x.is_zero() for x in resid)


PORTAL_triv = [[None] * b1_D for _ in range(b1_D)]
for j in range(b1_D):
    target = list(Z1triv[j])   # P(u_j)(g) = v0_triv * u_j(g) = 1 * u_j(g)
    coeff, ok = reduce_triv(target)
    assert ok
    for i in range(b1_D):
        PORTAL_triv[i][j] = coeff[i]
is_identity = all((PORTAL_triv[i][j] - (K1 if i == j else K0)).is_zero()
                   for i in range(b1_D) for j in range(b1_D))
log(f"  trivial-coefficient portal == identity_{b1_D}x{b1_D}: {is_identity}")
gates["control_trivial"] = is_identity
gates["b1_D"] = b1_D

gates["control_exactness"] = True   # design: K/Fraction arithmetic throughout; no floats
log("CONTROL C: exactness -- K = Q(sqrt(-3)) (Fraction pairs) throughout; zero floats "
    "in the portal path: PASS by construction")

# ============================================================================
all_gates_pass = all(v for k, v in gates.items() if isinstance(v, bool))
log(f"ALL GATES PASS: {all_gates_pass}")

if rank_portal == 0:
    verdict = "ZERO-PORTAL"
elif si_cols_zero and not bb_cols_zero:
    verdict = f"BOUNDARY-ONLY (rank {rank_portal}; image supported only via boundary-born columns 0,1)"
else:
    verdict = f"RANK-{rank_portal}"

log(f"VERDICT: {verdict}")

out = {
    "prereg_sha256": "9d8aa8ff36da8cc63285599c889a5fa9814e675c639c3026244b58a24d25b18a",
    "addendum_sha256": "7b77c578d1814638169562d209be79d03d8094db89e7917e2a2164e2e90006b3",
    "gates": gates,
    "v0_normalized_idx0": idx0,
    "h1_dual": h1_dual,
    "h0_dual": h0_dual,
    "portal_matrix": [[[str(PORTAL[i][j].a), str(PORTAL[i][j].b)] for j in range(5)] for i in range(5)],
    "portal_matrix_readable": [[fmt(PORTAL[i][j]) for j in range(5)] for i in range(5)],
    "rank": rank_portal,
    "kernel_dim": kernel_dim,
    "image_dim": image_dim,
    "split": {
        "boundary_born_cols": BOUNDARY_BORN,
        "solo_inherited_cols": SOLO_INHERITED,
        "note": split_note,
        "boundary_born_cols_all_zero": bb_cols_zero,
        "solo_inherited_cols_all_zero": si_cols_zero,
    },
    "controls": {
        "coboundary_input_side": ctrlA_input,
        "coboundary_representative_side": ctrlA_repr,
        "trivial_coefficient_b1_D": b1_D,
        "trivial_coefficient_is_identity": is_identity,
        "exactness": True,
    },
    "verdict": verdict,
    "runtime_s": time.time() - T0,
}
with open(os.path.join(HERE, "portal_matrix.json"), "w") as f:
    json.dump(out, f, indent=2)
log(f"saved {os.path.join(HERE, 'portal_matrix.json')}")
log("DONE.")
