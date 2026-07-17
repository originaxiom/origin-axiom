"""W0a -- the conflation, decided (PREREG_IL.md sha 9d8aa8ff).
Reconstruct v0 = the holonomy-invariant line of the 27; weight support; the
Spin(10)xU(1) branching 16(1)+10(-2)+1(4); THE DECISIVE NUMBER = h_pr-eigenvalue
of the GUT-singlet weight; the exact overlap <v0, w_singlet>.
Exec pattern for the B575 prefix follows d5_triality.py / cell3b_stage1.py exactly.
"""
import os, sys, time, json
from fractions import Fraction as Fr
from collections import Counter

os.environ["PYTHONDONTWRITEBYTECODE"] = "1"

T0 = time.time()
def log(msg):
    print(f"[{time.time()-T0:7.1f}s] {msg}", flush=True)

B575 = "<repo>/frontier/B575_bridge_obstruction/l51_obstruction.py"
OUT = "<seat-workdir>/invariant_line/w0a_singlet"

src = open(B575).read()
cut = src.index("# ---------------------------------------------------------------- stage 4")
ns = {"__name__": "b575_prefix", "__file__": B575}
log("exec B575 stages 0-3 (exact e6 + 27 build; gates G1-G3 print PASS below)...")
exec(compile(src[:cut], B575, "exec"), ns)
log("B575 prefix exec complete.")

K0, K1, K = ns["K0"], ns["K1"], ns["K"]
A27, B27, A27i, B27i = ns["A27"], ns["B27"], ns["A27i"], ns["B27i"]
mmul, meye, rref, nullspace = ns["mmul"], ns["meye"], ns["rref"], ns["nullspace"]
W27 = ns["W27"]
h_pr = ns["h_pr"]
C6 = ns["C6"]
d = 27

def msub2(X, Y):
    return [[X[i][j] - Y[i][j] for j in range(d)] for i in range(d)]

def matvec(M, v):
    return [sum((M[i][k] * v[k] for k in range(d) if not v[k].is_zero()), K0)
            for i in range(d)]

I = meye(d)

# ---------------------------------------------------------------------------
# Step 1: v0 = joint nullspace of (A27 - I), (B27 - I)
# ---------------------------------------------------------------------------
log("=== STEP 1: joint nullspace of (A27-I), (B27-I) ===")
AmI = msub2(A27, I)
BmI = msub2(B27, I)
stacked = AmI + BmI   # 54 x 27
ns_basis = nullspace(stacked)
log(f"joint nullspace dim = {len(ns_basis)}   [HARD GATE: must equal 1 = banked h0]")
gate_h0 = (len(ns_basis) == 1)
log(f"GATE h0=1: {'PASS' if gate_h0 else 'FAIL'}")
assert gate_h0, f"HARD GATE FAIL: nullspace dim {len(ns_basis)} != 1"

v0_raw = ns_basis[0]
idx0 = next(i for i, x in enumerate(v0_raw) if not x.is_zero())
scale = v0_raw[idx0].inv()
v0 = [scale * x for x in v0_raw]
assert (v0[idx0] - K1).is_zero()

chkA = matvec(AmI, v0)
chkB = matvec(BmI, v0)
assert all(x.is_zero() for x in chkA), "v0 fails (A27-I)v0=0 exactly"
assert all(x.is_zero() for x in chkB), "v0 fails (B27-I)v0=0 exactly"
log("v0 verified exactly: (A27-I)v0 = 0 and (B27-I)v0 = 0.")
log(f"v0 (normalized, first nonzero coord idx {idx0} -> 1):")
for i in range(d):
    if not v0[i].is_zero():
        log(f"    idx {i:2d}  weight {W27[i]}   coeff {v0[i]}")

# ---------------------------------------------------------------------------
# Step 2: weight support + h_pr-null check
# ---------------------------------------------------------------------------
log("=== STEP 2: v0 weight support + h_pr-null check ===")
support = [i for i, x in enumerate(v0) if not x.is_zero()]
log(f"support size = {len(support)}  indices = {support}")
log(f"support weights = {[W27[i] for i in support]}")

is_diag = all(h_pr[i][j].is_zero() for i in range(d) for j in range(d) if i != j)
log(f"h_pr is diagonal in the weight basis (as constructed): {is_diag}")
diag_vals = [h_pr[i][i] for i in range(d)]
log("h_pr eigenvalue at each support weight:")
for i in support:
    log(f"    idx {i:2d}  weight {W27[i]}   h_pr-eigenvalue = {diag_vals[i]}")

hv0 = matvec(h_pr, v0)
h_pr_null = all(x.is_zero() for x in hv0)
log(f"h_pr @ v0 == 0 exactly (v0 is h_pr-null)?  {h_pr_null}")

# ---------------------------------------------------------------------------
# Step 3: Spin(10) x U(1) branching search over the 6 fundamental coweights
# ---------------------------------------------------------------------------
log("=== STEP 3: Spin(10)xU(1) branching search (6 candidate coweights) ===")

def mat_inv_fr(M):
    n = len(M)
    aug = [[Fr(M[i][j]) for j in range(n)] + [Fr(1) if k == i else Fr(0) for k in range(n)]
           for i in range(n)]
    for col in range(n):
        piv = next(r for r in range(col, n) if aug[r][col] != 0)
        aug[col], aug[piv] = aug[piv], aug[col]
        pv = aug[col][col]
        aug[col] = [x / pv for x in aug[col]]
        for r in range(n):
            if r != col and aug[r][col] != 0:
                f = aug[r][col]
                aug[r] = [aug[r][j] - f * aug[col][j] for j in range(2 * n)]
    return [[aug[i][n + j] for j in range(n)] for i in range(n)]

Cinv = mat_inv_fr(C6)
log("E6 Cartan matrix C6:")
for row in C6:
    log(f"    {row}")
log("Cartan inverse C6^-1 (Q):")
for row in Cinv:
    log(f"    {[str(x) for x in row]}")

branchings = []
for j in range(6):
    c = [Cinv[i][j] for i in range(6)]        # column j = fundamental coweight j+1
    qs = [sum((c[k] * W27[i][k] for k in range(6)), Fr(0)) for i in range(27)]
    cnt = Counter(qs)
    mults = sorted(cnt.values())
    entry = {"node": j + 1, "coweight": [str(x) for x in c], "mult_pattern": mults}
    if mults == [1, 10, 16]:
        vm = {v: m for v, m in cnt.items()}
        v16 = next(v for v, m in vm.items() if m == 16)
        v10 = next(v for v, m in vm.items() if m == 10)
        v1 = next(v for v, m in vm.items() if m == 1)
        ratio_ok = (v16 != 0) and (v10 / v16 == -2) and (v1 / v16 == 4)
        w_s = next(i for i in range(27) if qs[i] == v1)
        entry.update({"is_16_10_1": True, "v16_charge": str(v16), "v10_charge": str(v10),
                      "v1_charge_singlet": str(v1), "ratio_1_neg2_4_ok": ratio_ok,
                      "w_singlet_idx": w_s, "w_singlet_weight": W27[w_s],
                      "qs": [str(x) for x in qs]})
        log(f"  node {j+1}: coweight {c} -> charges (16-mult)={v16}, (10-mult)={v10}, "
            f"(1-mult,singlet)={v1}   ratio(1:-2:4) OK = {ratio_ok}   "
            f"w_singlet = idx {w_s} weight {W27[w_s]}")
    else:
        entry["is_16_10_1"] = False
        log(f"  node {j+1}: coweight {c} -> multiplicity pattern {mults} (not 16/10/1, skip)")
    branchings.append(entry)

valid = [b for b in branchings if b.get("is_16_10_1") and b["ratio_1_neg2_4_ok"]]
log(f"VALID Spin(10)xU(1) branchings (16/10/1, ratio 1:-2:4): nodes "
    f"{[b['node'] for b in valid]}  (count={len(valid)})")

# ---------------------------------------------------------------------------
# Step 4: THE DECISIVE NUMBERS
# ---------------------------------------------------------------------------
log("=== STEP 4: THE DECISIVE NUMBERS ===")
decisive = []
all_nonzero = True
identified_any = False
for b in valid:
    w_s = b["w_singlet_idx"]
    h_eig = diag_vals[w_s]
    v0_coeff = v0[w_s]
    is_zero_eig = h_eig.is_zero()
    if not is_zero_eig:
        pass
    else:
        all_nonzero = False
    fully_supported_on_singlet = (support == [w_s]) or (len(support) == 1 and support[0] == w_s)
    if fully_supported_on_singlet:
        identified_any = True
    rec = {
        "node": b["node"], "w_singlet_idx": w_s, "w_singlet_weight": W27[w_s],
        "h_pr_eigenvalue_at_singlet": str(h_eig),
        "v0_coeff_at_singlet": str(v0_coeff),
        "v0_coeff_at_singlet_zero": v0_coeff.is_zero(),
    }
    decisive.append(rec)
    log(f"  node {b['node']}: w_singlet = idx {w_s} weight {W27[w_s]}   "
        f"h_pr-eigenvalue = {h_eig}   v0-coefficient there = {v0_coeff}")

if len(valid) == 0:
    verdict = "NO-VALID-BRANCHING (unable to evaluate)"
elif all_nonzero and h_pr_null:
    verdict = "CONFLATION-REFUTED"
elif identified_any:
    verdict = "IDENTIFIED"
else:
    verdict = f"PARTIAL (overlap: v0 support = {[W27[i] for i in support]}, " \
              f"singlet coeff(s) = {[r['v0_coeff_at_singlet'] for r in decisive]})"

log(f"*** VERDICT: {verdict} ***")

# ---------------------------------------------------------------------------
# Save outputs
# ---------------------------------------------------------------------------
def kser(x):
    return [str(x.a), str(x.b)]

out = {
    "prereg_sha256": "9d8aa8ff36da8cc63285599c889a5fa9814e675c639c3026244b58a24d25b18a",
    "gate_h0_dim1": gate_h0,
    "v0_normalized_idx0": idx0,
    "v0_coordinates_full": [kser(x) for x in v0],
    "v0_support_indices": support,
    "v0_support_weights": [W27[i] for i in support],
    "h_pr_is_diagonal": is_diag,
    "h_pr_diag_values_at_support": [str(diag_vals[i]) for i in support],
    "v0_is_h_pr_null": h_pr_null,
    "cartan_matrix_C6": C6,
    "cartan_inverse_C6inv": [[str(x) for x in row] for row in Cinv],
    "branchings_all_candidates": branchings,
    "branchings_valid_16_10_1_ratio": valid,
    "decisive_numbers": decisive,
    "verdict": verdict,
}
with open(os.path.join(OUT, "w0a_v0.json"), "w") as f:
    json.dump(out, f, indent=2)
log(f"saved {os.path.join(OUT, 'w0a_v0.json')}")
log("DONE.")
