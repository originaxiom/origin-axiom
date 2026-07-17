"""B662 CELL B — Q-BLOCK: (i1, i2) and (h0, h1) of the adjoint 78 on the fig-8.

Prereg (CAMPAIGN_PREREGISTRATION.md, CELL B): the banked adjoint blocks are
[23,17,15,11,9,3] (no Sym^0) => predict i1 = 0, i2 = 6 => (h0, h1) = (0, 6)
by the reduction (B656/G5 + one-per-block B657/W0b). Compute exactly on the
fig-8: the adjoint action of the holonomy on B575's e6 basis (78-dim rep),
joint fixed spaces, Fox h0/h1. Outcomes: the predicted (0,6) CONFIRMS the
reduction on a third module / deviation stated exactly (either banks).

Method:
  0. exec the B637 apparatus (which execs B575 stages 0-3): exact e6 in
     gl(27) over K = Q(sqrt(-3)) (Fraction pairs), E6_BASIS (78 matrices),
     E6_SOLVER (coordinates), BLOCKS (adjoint principal-sl2 isotypic blocks,
     dims 23,17,15,11,9,3), holonomy A27/B27 (exact nilpotent exponentials),
     REL (solo relator), LONG (longitude word), meridian mu = 'a'.
  1. Adjoint letters: Ad(g): X -> g X g^{-1} on E6_BASIS, expressed in basis
     coordinates via E6_SOLVER (78x78 exact over K).  Gates: Ad(g)Ad(g^{-1})
     = I for g in {A27, B27, rho(LONG)}; closure (coords never leaves span);
     peripheral commutation [A27, rho(LONG)] = 0 at 27 AND 78 level.
  2. i1 = dim ker{Ad(A)-I, Ad(B)-I} (joint holonomy fixed space);
     i2 = dim ker{Ad(rho(mu))-I, Ad(rho(LONG))-I} (peripheral Z^2 fixed).
  3. Fox h0/h1 of the solo relator with the 78-dim letters (the W0b
     2-generator Fox pattern at dV=78); relator gate Pw(REL) = I at 78;
     Euler check h0 - h1 + h2 = 0.
  4. Cross-check: the same numbers per principal-sl2 block (each block is
     Ad-invariant; block Solver coords gate the invariance exactly).

All decisive arithmetic exact over K = Q(sqrt(-3)) as Fraction pairs.
"""
import json
import os
import time

HERE = os.path.dirname(os.path.abspath(__file__))
B637 = os.path.join(HERE, "..", "..", "B637_corrected_cell3", "b637_threeform.py")
JSON_PATH = os.path.join(HERE, "qblock_78.json")

T0 = time.time()
def log(msg):
    print(f"[{time.time()-T0:7.1f}s] {msg}", flush=True)

log("executing the B637 apparatus (B575 stages 0-3 inside)...")
mod = {"__name__": "b637_module", "__file__": B637}
exec(compile(open(B637).read(), "b637_threeform.py", "exec"), mod)
log("B637 apparatus loaded")

ns = mod["ns"]
K, K0, K1 = ns["K"], ns["K0"], ns["K1"]
E6_BASIS, E6_SOLVER = ns["E6_BASIS"], ns["E6_SOLVER"]
BLOCKS = ns["BLOCKS"]
A27, B27, A27i, B27i = ns["A27"], ns["B27"], ns["A27i"], ns["B27i"]
REL = ns["REL"]
nullspace, rref, Solver = ns["nullspace"], ns["rref"], ns["Solver"]
flat, mmul, meye = ns["flat"], ns["mmul"], ns["meye"]
msub, mzero_p = ns["msub"], ns["mzero_p"]
LONG = mod["LONG"]
inv_word = mod["inv"]
MU = "a"                                    # meridian (b637 side-1 convention)
N78 = len(E6_BASIS)
assert N78 == 78, f"e6 basis dim {N78} != 78"
log(f"REL = {REL!r}  LONG = {LONG!r}  mu = {MU!r}  |E6_BASIS| = {N78}")

LET27 = {'a': A27, 'b': B27, 'A': A27i, 'B': B27i}

def word27(w):
    M = meye(27)
    for ch in w:
        M = mmul(M, LET27[ch])
    return M

def is_eye(M, n):
    return all((M[i][j] - (K1 if i == j else K0)).is_zero()
               for i in range(n) for j in range(n))

# ---------------------------------------------------------------- gate 0: 27-level
Rm = word27(REL)
assert is_eye(Rm, 27), "GATE FAIL: relator not identity at 27"
log("gate 0a PASS: relator = exact identity at 27")

ML = word27(LONG)
MLi = word27(inv_word(LONG))
assert is_eye(mmul(ML, MLi), 27), "GATE FAIL: rho(LONG) inverse"
comm = msub(mmul(A27, ML), mmul(ML, A27))
assert mzero_p(comm), "GATE FAIL: peripheral pair does not commute at 27"
log("gate 0b PASS: rho(LONG) exact-invertible; [rho(mu), rho(LONG)] = 0 at 27")

# ---------------------------------------------------------------- the adjoint letters
def ad_matrix(P, Pi, name):
    t0 = time.time()
    cols = []
    for X in E6_BASIS:
        img = mmul(mmul(P, X), Pi)
        cols.append(E6_SOLVER.coords(flat(img)))   # ValueError => closure fail
    M = [[cols[j][i] for j in range(N78)] for i in range(N78)]
    log(f"Ad({name}) built ({time.time()-t0:.0f}s)")
    return M

AdA = ad_matrix(A27, A27i, "a")
AdAi = ad_matrix(A27i, A27, "a^-1")
AdB = ad_matrix(B27, B27i, "b")
AdBi = ad_matrix(B27i, B27, "b^-1")
AdL = ad_matrix(ML, MLi, "LONG")
AdLi = ad_matrix(MLi, ML, "LONG^-1")

assert is_eye(mmul(AdA, AdAi), N78), "GATE FAIL: Ad(a) inverse"
assert is_eye(mmul(AdB, AdBi), N78), "GATE FAIL: Ad(b) inverse"
assert is_eye(mmul(AdL, AdLi), N78), "GATE FAIL: Ad(LONG) inverse"
log("gate 1a PASS: Ad(g) Ad(g^-1) = I exactly (g = a, b, LONG) at 78")

comm78 = msub(mmul(AdA, AdL), mmul(AdL, AdA))
assert mzero_p(comm78), "GATE FAIL: [Ad(mu), Ad(LONG)] != 0 at 78"
log("gate 1b PASS: [Ad(rho(mu)), Ad(rho(LONG))] = 0 exactly at 78")

# ---------------------------------------------------------------- i1, i2
def joint_fixed_dim(mats, n):
    rows = []
    for M in mats:
        rows += [[M[i][j] - (K1 if i == j else K0) for j in range(n)]
                 for i in range(n)]
    return len(nullspace(rows))

t0 = time.time()
i1 = joint_fixed_dim([AdA, AdB], N78)
log(f"i1 = dim (78)^holonomy = {i1}   ({time.time()-t0:.0f}s)")
t0 = time.time()
i2 = joint_fixed_dim([AdA, AdL], N78)
log(f"i2 = dim (78)^peripheral = {i2}   ({time.time()-t0:.0f}s)")

# ---------------------------------------------------------------- Fox h0/h1 (78-dim)
GENS2 = ['a', 'b']

def fox_matrices_2gen(word, acts_V, dV):
    """Fox derivatives D_a(word), D_b(word) as dV x dV matrices; returns
    (D, Pw) with Pw = the full word action (must be I for the relator)."""
    D_ = {g: [[K0] * dV for _ in range(dV)] for g in GENS2}
    Pw = meye(dV)
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
    return D_, Pw

def fox_h0_h1_h2(acts_V, dV, tag):
    t0 = time.time()
    Dw, Pw = fox_matrices_2gen(REL, acts_V, dV)
    assert is_eye(Pw, dV), f"GATE FAIL [{tag}]: adjoint relator != identity"
    big = [[Dw['a'][i][j] for j in range(dV)] +
           [Dw['b'][i][j] for j in range(dV)] for i in range(dV)]
    Z1 = nullspace(big)
    z1dim = len(Z1)
    cobs = []
    for j in range(dV):
        e = [K1 if i == j else K0 for i in range(dV)]
        row = []
        for g in GENS2:
            ge = [e[i] - sum((acts_V[g][i][kk] * e[kk] for kk in range(dV)
                              if not e[kk].is_zero()), K0) for i in range(dV)]
            row += ge
        cobs.append(row)
    _, pivc = rref(cobs)
    rank_cob = len(pivc)
    h0 = dV - rank_cob
    h1 = z1dim - rank_cob
    # h2 = coker of z -> z(r): dV - rank(big)
    _, pivb = rref(big)
    h2 = dV - len(pivb)
    log(f"Fox [{tag}]: Z1 = {z1dim}, rank B1 = {rank_cob}, rank L = {len(pivb)}"
        f" => h0 = {h0}, h1 = {h1}, h2 = {h2}   ({time.time()-t0:.0f}s)")
    return h0, h1, h2, z1dim, rank_cob, len(pivb)

acts78 = {'a': AdA, 'A': AdAi, 'b': AdB, 'B': AdBi}
h0, h1, h2, z1dim, rank_cob, rank_big = fox_h0_h1_h2(acts78, N78, "78-dim")
assert h0 - h1 + h2 == 0, "GATE FAIL: Euler characteristic != 0"
assert h0 == i1, "GATE FAIL: Fox h0 != joint holonomy fixed dim i1"
log("gate 2 PASS: adjoint relator = I at 78; Euler h0-h1+h2 = 0; h0 == i1")

# ---------------------------------------------------------------- per-block cross-check
log("cross-check: per principal-sl2 block (dims 23,17,15,11,9,3)...")
per_block = []
block_ok = True
for m in sorted(BLOCKS, reverse=True):
    vecs = BLOCKS[m]
    d = len(vecs)
    bsolver = Solver([flat(X) for X in vecs])
    def blk_act(P, Pi):
        cols = [bsolver.coords(flat(mmul(mmul(P, X), Pi))) for X in vecs]
        return [[cols[j][i] for j in range(d)] for i in range(d)]
    try:
        bA = blk_act(A27, A27i); bAi = blk_act(A27i, A27)
        bB = blk_act(B27, B27i); bBi = blk_act(B27i, B27)
        bL = blk_act(ML, MLi)
    except ValueError:
        log(f"  block m={m} (dim {d}): NOT Ad-invariant (coords left the span)")
        block_ok = False
        per_block.append({"exponent": m, "dim": d, "invariant": False})
        continue
    bi1 = joint_fixed_dim([bA, bB], d)
    bi2 = joint_fixed_dim([bA, bL], d)
    bacts = {'a': bA, 'A': bAi, 'b': bB, 'B': bBi}
    bh0, bh1, bh2, _, _, _ = fox_h0_h1_h2(bacts, d, f"block m={m} dim {d}")
    per_block.append({"exponent": m, "dim": d, "invariant": True,
                      "i1": bi1, "i2": bi2, "h0": bh0, "h1": bh1, "h2": bh2})
    log(f"  block m={m} (dim {d}): i1={bi1} i2={bi2} h0={bh0} h1={bh1} h2={bh2}")

if block_ok:
    s_i1 = sum(b["i1"] for b in per_block)
    s_i2 = sum(b["i2"] for b in per_block)
    s_h0 = sum(b["h0"] for b in per_block)
    s_h1 = sum(b["h1"] for b in per_block)
    log(f"block sums: i1 = {s_i1}, i2 = {s_i2}, h0 = {s_h0}, h1 = {s_h1}"
        f"  (must equal full-78: {i1}, {i2}, {h0}, {h1})")
    sums_match = (s_i1, s_i2, s_h0, s_h1) == (i1, i2, h0, h1)
else:
    sums_match = None

# ---------------------------------------------------------------- verdict
predicted = (i1, i2, h0, h1) == (0, 6, 0, 6)
verdict = ("CONFIRMED-(0,6)" if predicted
           else f"DEVIATION: (i1,i2,h0,h1) = ({i1},{i2},{h0},{h1})")
log(f"(i1, i2) = ({i1}, {i2})   (h0, h1) = ({h0}, {h1})   [predicted (0,6),(0,6)]")
log(f"VERDICT: {verdict}")
if sums_match is not None:
    log(f"per-block sums match full-78: {sums_match}")

result = {
    "cell": "B662-cellB Q-BLOCK adjoint 78",
    "REL": REL, "LONG": LONG, "mu": MU,
    "dim_module": N78,
    "adjoint_block_dims": sorted((len(v) for v in BLOCKS.values()), reverse=True),
    "i1_joint_holonomy_fixed": i1,
    "i2_joint_peripheral_fixed": i2,
    "fox": {"h0": h0, "h1": h1, "h2": h2, "Z1_dim": z1dim,
            "coboundary_rank": rank_cob, "jacobian_rank": rank_big},
    "gates": {"relator_identity_27": True, "relator_identity_78": True,
              "ad_inverses_exact": True, "peripheral_commute_27_and_78": True,
              "euler_zero": True, "h0_equals_i1": True},
    "per_block": per_block,
    "per_block_sums_match_full": sums_match,
    "predicted": {"i1": 0, "i2": 6, "h0": 0, "h1": 6},
    "verdict": verdict,
    "runtime_s": round(time.time() - T0, 1),
}
with open(JSON_PATH, "w") as f:
    json.dump(result, f, indent=2)
log(f"wrote {JSON_PATH}")
log(f"TOTAL runtime {time.time()-T0:.0f}s")
