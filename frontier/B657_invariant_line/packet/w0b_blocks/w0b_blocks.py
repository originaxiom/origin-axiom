"""W0b — chat-1's unbanked one-per-block assertion (prereg 9d8aa8ff, W0b clause).

Setup: exec the B575 prefix (stages 0-3, ~95s) to get the exact e6 + 27 build:
A27, B27, A27i, B27i (rho(a), rho(b) and inverses on the 27), REL (the solo
relator word), h_pr/e_pr/f_pr (principal sl2 in gl(27)), meye/mmul/nullspace/rref
(exact linear algebra over K = Q(sqrt(-3))).

Principal-block decomposition: REPRODUCE the chain/eigvecs construction from
cell3_double/cell3b_stage1.py lines 50-92 (chain basis P/Pinv, block_slices)
that organizes the 27 into principal-SL(2) blocks.

Then, for the SOLO manifold M = <a, b | REL> (matrices A27, B27 -- NOT the
double, no c generator):
  1. Conjugate A27, B27 into the chain basis; verify exact block-diagonality.
  2. Per block V: h0 = dim nullspace{A_V - I, B_V - I}; h1 via Fox calculus for
     the 2-generator 1-relator group (adapting cell3b_stage1.py's fox_matrices,
     lines ~157+, from 3 generators a,b,c down to 2, a,b).
  3. GATES: sum h0 = 1, sum h1 = 3 (banked); the dim-1 block gives (h0,h1)=(1,1).
  4. Bank the per-block table; verdict ONE-PER-BLOCK or the actual distribution.
"""
import json
import os
import time

HERE = os.path.dirname(os.path.abspath(__file__))
B575 = "<repo>/frontier/B575_bridge_obstruction/l51_obstruction.py"
LOG_PATH = os.path.join(HERE, "w0b_run.log")
JSON_PATH = os.path.join(HERE, "w0b_blocks.json")

T0 = time.time()
_log_lines = []
def log(msg):
    line = f"[{time.time()-T0:7.1f}s] {msg}"
    print(line, flush=True)
    _log_lines.append(line)

# ---------------------------------------------------------------- B575 prefix
src = open(B575).read()
cut = src.index("# ---------------------------------------------------------------- stage 4")
ns = {"__name__": "b575_prefix", "__file__": B575}
log("executing B575 stages 0-3 (exact e6 + 27 build)...")
exec(compile(src[:cut], B575, "exec"), ns)
log(f"B575 prefix done in {time.time()-T0:.0f}s")

K0, K1, K = ns["K0"], ns["K1"], ns["K"]
A27, B27, A27i, B27i = ns["A27"], ns["B27"], ns["A27i"], ns["B27i"]
REL = ns["REL"]
meye, mmul = ns["meye"], ns["mmul"]
nullspace, rref = ns["nullspace"], ns["rref"]
e_pr, f_pr, h_pr = ns["e_pr"], ns["f_pr"], ns["h_pr"]
d = 27

log(f"REL (solo relator) = {REL!r}")

def mt(M):
    return [[M[j][i] for j in range(d)] for i in range(d)]

def is_eye(M):
    return all((M[i][j] - (K1 if i == j else K0)).is_zero() for i in range(d) for j in range(d))

def matvec(M, v):
    return [sum((M[i][k] * v[k] for k in range(d) if not v[k].is_zero()), K0)
            for i in range(d)]

def abs_K(x):
    # |a + b*sqrt(-3)|^2 = a^2 + 3 b^2 ; used only for reporting magnitudes.
    return float(x.a) ** 2 + 3.0 * float(x.b) ** 2

# ---------------------------------------------------------------- chain basis
# REPRODUCED verbatim (adapted var names) from cell3_double/cell3b_stage1.py
# lines 50-92: h_pr eigenvectors per eigenvalue via nullspace(h_pr - t I), the
# principal-sl2 chain basis, and block_slices.
log("building principal-sl2 chain basis (cell3b_stage1.py lines 50-92 pattern)...")
t0 = time.time()

def eigvecs(t):
    rows = [[h_pr[i][j] - (K(t) if i == j else K0) for j in range(d)] for i in range(d)]
    return nullspace(rows)

chains = []                                   # list of lists of vectors (chain basis)
for s in (8, 4, 0):                           # V(16), V(8), V(0)
    top = eigvecs(2 * s)
    cols = [matvec(e_pr, list(v)) for v in top]
    rows = [[cols[c][i] for c in range(len(top))] for i in range(d)]
    ker = nullspace(rows)
    assert len(ker) == 1, f"HW combo at 2s={2*s}: got {len(ker)} (eigdim {len(top)})"
    v = [sum((ker[0][c] * top[c][i] for c in range(len(top))
              if not ker[0][c].is_zero()), K0) for i in range(d)]
    chain = [v]
    for k in range(2 * s):
        v = matvec(f_pr, v)
        chain.append(v)
    assert not all(x.is_zero() for x in chain[-1])
    assert all(x.is_zero() for x in matvec(f_pr, chain[-1]))
    chains.append(chain)

P = [[K0] * d for _ in range(d)]             # columns = chain vectors
col = 0
block_slices = []
for chain in chains:
    block_slices.append((col, col + len(chain)))
    for v in chain:
        for i in range(d):
            P[i][col] = v[i]
        col += 1
assert col == d
aug = [list(P[i]) + [K1 if k == i else K0 for k in range(d)] for i in range(d)]
Rr, piv = rref(aug)
assert len(piv) == d, "chain basis singular"
Pinv = [[Rr[i][d + j] for j in range(d)] for i in range(d)]

block_dims = [hi - lo for (lo, hi) in block_slices]
log(f"chain basis built in {time.time()-t0:.0f}s")
log(f"block_slices = {block_slices}")
log(f"BLOCK DIMS FOUND = {block_dims}  (sum = {sum(block_dims)}; expected [17, 9, 1])")

# ---------------------------------------------------------------- conjugate into chain basis
log("conjugating A27, B27 into the chain basis...")
t0 = time.time()
A_chain = mmul(mmul(Pinv, A27), P)
B_chain = mmul(mmul(Pinv, B27), P)
Ai_chain = mmul(mmul(Pinv, A27i), P)
Bi_chain = mmul(mmul(Pinv, B27i), P)
log(f"conjugation done in {time.time()-t0:.0f}s")

# block-diagonality check: exact zero off-block entries required.
max_off = 0.0
max_off_entry = None
off_block_exact = True
for M_, nm in ((A_chain, "A"), (B_chain, "B")):
    for (lo_p, hi_p) in block_slices:
        for (lo_q, hi_q) in block_slices:
            if (lo_p, hi_p) == (lo_q, hi_q):
                continue
            for i in range(lo_p, hi_p):
                Mi = M_[i]
                for j in range(lo_q, hi_q):
                    if not Mi[j].is_zero():
                        off_block_exact = False
                        mag = abs_K(Mi[j])
                        if mag > max_off:
                            max_off = mag
                            max_off_entry = (nm, i, j, (Mi[j].a, Mi[j].b))

log(f"block-diagonality exact (off-block == 0 everywhere): {off_block_exact}")
if not off_block_exact:
    log(f"STOP: max off-block entry magnitude^2={max_off} at {max_off_entry} "
        f"-- block-decomposition premise REFUTED")
    result = {
        "prereg_sha256": "9d8aa8ff36da8cc63285599c889a5fa9814e675c639c3026244b58a24d25b18a",
        "REL": REL,
        "block_dims": block_dims,
        "block_slices": block_slices,
        "block_diagonal_exact": False,
        "max_off_block_entry": {
            "matrix": max_off_entry[0], "row": max_off_entry[1], "col": max_off_entry[2],
            "value_a_b": max_off_entry[3], "magnitude_sq": max_off,
        },
        "verdict": "BLOCK-DECOMPOSITION-REFUTED",
    }
    with open(JSON_PATH, "w") as f:
        json.dump(result, f, indent=2)
    with open(LOG_PATH, "w") as f:
        f.write("\n".join(_log_lines) + "\n")
    log(f"wrote {JSON_PATH} and {LOG_PATH}; STOPPING per gate protocol.")
    raise SystemExit(0)

# ---------------------------------------------------------------- per-block Fox h0/h1
# Adapted from cell3b_stage1.py fox_matrices (lines ~157+), 3 generators a,b,c ->
# here 2 generators a, b (the solo relator REL only; no c, no double).
GENS2 = ['a', 'b']

def fox_matrices_2gen(word, acts_V, dV):
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
    return D_

def block_h0(A_V, B_V, dV):
    """h0 = dim nullspace{A_V - I, B_V - I} (joint fixed space)."""
    AmI = [[A_V[i][j] - (K1 if i == j else K0) for j in range(dV)] for i in range(dV)]
    BmI = [[B_V[i][j] - (K1 if i == j else K0) for j in range(dV)] for i in range(dV)]
    rows = AmI + BmI
    return len(nullspace(rows))

log("computing per-block Fox h0/h1 for the solo relator REL...")
per_block = []
for bi, (lo, hi) in enumerate(block_slices):
    dV = hi - lo
    A_V = [row[lo:hi] for row in A_chain[lo:hi]]
    B_V = [row[lo:hi] for row in B_chain[lo:hi]]
    Ai_V = [row[lo:hi] for row in Ai_chain[lo:hi]]
    Bi_V = [row[lo:hi] for row in Bi_chain[lo:hi]]
    acts_V = {'a': A_V, 'A': Ai_V, 'b': B_V, 'B': Bi_V}

    # sanity: A_V A_V^-1 = I, B_V B_V^-1 = I within the block
    assert all((sum((A_V[i][k] * Ai_V[k][j] for k in range(dV)), K0) - (K1 if i == j else K0)).is_zero()
               for i in range(dV) for j in range(dV)), f"block {bi}: A_V not invertible via Ai_V"
    assert all((sum((B_V[i][k] * Bi_V[k][j] for k in range(dV)), K0) - (K1 if i == j else K0)).is_zero()
               for i in range(dV) for j in range(dV)), f"block {bi}: B_V not invertible via Bi_V"

    h0 = block_h0(A_V, B_V, dV)

    Dw = fox_matrices_2gen(REL, acts_V, dV)
    big = []
    for i in range(dV):
        big.append([Dw['a'][i][j] for j in range(dV)] + [Dw['b'][i][j] for j in range(dV)])
    sols1 = nullspace(big)
    z1dim = len(sols1)

    cobs = []
    for j in range(dV):
        e = [K1 if i == j else K0 for i in range(dV)]
        row = []
        for g in GENS2:
            ge = [e[i] - sum((acts_V[g][i][k] * e[k] for k in range(dV) if not e[k].is_zero()), K0)
                  for i in range(dV)]
            row += ge
        cobs.append(row)
    _, pivc = rref([list(r) for r in cobs]) if cobs else ([], [])
    rank_cob = len(pivc)
    h1 = z1dim - rank_cob

    consistent = (h0 == dV - rank_cob)
    per_block.append({
        "block": bi, "dim": dV, "slice": [lo, hi],
        "h0": h0, "h1": h1,
        "z1_dim": z1dim, "coboundary_rank": rank_cob,
        "h0_eq_dim_minus_cobrank": consistent,
    })
    log(f"block {bi} (dim {dV}, slice [{lo},{hi})): h0={h0}  h1={h1}  "
        f"(Z1={z1dim}, B1={rank_cob}, h0==dim-B1: {consistent})")

sum_h0 = sum(b["h0"] for b in per_block)
sum_h1 = sum(b["h1"] for b in per_block)
gate_h0 = (sum_h0 == 1)
gate_h1 = (sum_h1 == 3)
v1_blocks = [b for b in per_block if b["dim"] == 1]
gate_v1 = all(b["h0"] == 1 and b["h1"] == 1 for b in v1_blocks) if v1_blocks else None
one_per_block = all(b["h1"] == 1 for b in per_block)

log(f"SUM h0 = {sum_h0}  (gate: == 1 banked -> {gate_h0})")
log(f"SUM h1 = {sum_h1}  (gate: == 3 banked -> {gate_h1})")
log(f"dim-1 block(s) (h0,h1) = {[(b['h0'], b['h1']) for b in v1_blocks]}  "
    f"(gate: == (1,1) -> {gate_v1})")
log(f"ONE-PER-BLOCK (every block h1==1): {one_per_block}")

all_gates_pass = gate_h0 and gate_h1 and (gate_v1 is True)
verdict = "ONE-PER-BLOCK" if (all_gates_pass and one_per_block) else "ACTUAL-DISTRIBUTION"
if not all_gates_pass:
    verdict = "GATE-FAILED: " + verdict
log(f"VERDICT: {verdict}")

result = {
    "prereg_sha256": "9d8aa8ff36da8cc63285599c889a5fa9814e675c639c3026244b58a24d25b18a",
    "REL": REL,
    "block_dims": block_dims,
    "block_slices": block_slices,
    "block_diagonal_exact": True,
    "per_block": per_block,
    "sum_h0": sum_h0,
    "sum_h1": sum_h1,
    "gate_sum_h0_eq_1": gate_h0,
    "gate_sum_h1_eq_3": gate_h1,
    "gate_v1_block_eq_1_1": gate_v1,
    "one_per_block": one_per_block,
    "all_gates_pass": all_gates_pass,
    "verdict": verdict,
    "runtime_s": time.time() - T0,
}
with open(JSON_PATH, "w") as f:
    json.dump(result, f, indent=2)
with open(LOG_PATH, "w") as f:
    f.write("\n".join(_log_lines) + "\n")
log(f"wrote {JSON_PATH} and {LOG_PATH}")
log(f"TOTAL runtime {time.time()-T0:.0f}s")
