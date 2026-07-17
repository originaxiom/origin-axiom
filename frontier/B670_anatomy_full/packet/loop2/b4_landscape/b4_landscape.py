"""B4 -- THE CROSS-LANDSCAPE (PREREG_L2.md sha c6d4fabd, B4 clause / ADDENDUM).

  "the matrix |tr_odd(word, stage)| for words = the single-L family R^{n-2}L
  (tr = 3..15) PLUS the multi-block controls RRLL, RLRL, RRLRL (the H3
  counterexample set), stages kappa = 4..15 (SU(3) levels 1..12)."

Machinery (all read-only reuse, per task spec):
  - engine_v7.An_Level(n=3, k) -- the V7 conduit SU(3)_k build pattern, same
    exact code path as
      <seat-workdir>/veins/v7_conduit/chat2_hearing_group_verify.py
    (theta = conjugation; theta-odd (e_a-e_b)/sqrt2 orthonormal block).
  - The H3 word-mapping (h3_resolution.py, PREREG_HA.md sha 77c72b58, H3
    clause): R -> T, L -> S T^-1 S^-1, left-to-right product, dps 40.
  - kappa = K = k + hvee(A2) = k + 3, so kappa=4..15 <-> k=1..12.

Entry = tr of the theta-odd 2x2 block of rho(word), exact-quantized at
dps 40 (quantization grid 10^20, matching h3_resolution.py's qkey()).

Row = 13 single-L words R^{n-2}L for n=3..15 (exact SL(2,Z) trace = n, a
one-line identity: R^m L = [[1+m,m],[1,1]], trace = m+2 = n) + the 3
H3 multi-block controls RRLL, RLRL, RRLRL. 16 rows x 12 columns.

GATES (per task spec -- STOP on any mismatch):
  G1: (RL, kappa=5) == -1/phi (banked, H3 W1 @ SU(3)_2).
  G2: kappa=5 column, single-L family n=3..15: |value| in {0, 1/phi, 1}.
  G3: kappa=5 column, multi-block: RRLL==1.0, RLRL==-phi, RRLRL~=0
      (banked H3 W3/W6/W7 @ SU(3)_2 -- cross-checked against
      h3_resolution/h3_table.json before writing this script).

ANALYSIS (sealed hypotheses, read off honestly, not forced):
  (i)   per-column distinct |value| set (shadow-class law candidate).
  (ii)  the diagonal hypothesis: row-minima (minimal nonzero |value| per
        word) vs. conductor (tr^2-4) divisibility/gcd with kappa.
  (iii) the realness catalog: exact-real entries vs. det(A-I) unit-ness.
"""
import os
import sys
import time
import json
import hashlib
from math import gcd

os.environ["PYTHONDONTWRITEBYTECODE"] = "1"

T0 = time.time()


def log(msg):
    print(f"[{time.time()-T0:7.1f}s] {msg}", flush=True)


HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, "<seat-workdir>/veins/v7_conduit")
import mpmath as mp
from engine_v7 import An_Level

PREREG = "<seat-workdir>/anatomy/loop2/PREREG_L2.md"
SEALED_SHA = "c6d4fabdd8eabc6a777d9fc462a404c50511c1cea9abc429d77b2f54a9768926"

# ============================================================================
log("STEP 0: seal check")
with open(PREREG, "rb") as f:
    actual_sha = hashlib.sha256(f.read()).hexdigest()
log(f"  PREREG_L2.md sha256 = {actual_sha}")
log(f"  sealed (task spec)  = {SEALED_SHA}")
seal_match = (actual_sha == SEALED_SHA)
log(f"  MATCH: {seal_match}")
assert seal_match, "PREREG SEAL BROKEN -- refusing to proceed"

mp.mp.dps = 40
phi = (1 + mp.sqrt(5)) / 2
log(f"  mp.mp.dps = {mp.mp.dps}, phi = {mp.nstr(phi, 25)}")

# ============================================================================
log("STEP 1: exact SL(2,Z) integer words -- trace, conductor, det(A-I)")
R_INT = ((1, 1), (0, 1))
L_INT = ((1, 0), (1, 1))
I_INT = ((1, 0), (0, 1))


def imatmul(A, B):
    return (
        (A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]),
        (A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]),
    )


def iword(w):
    """w: string of 'R'/'L' -> exact integer SL(2,Z) matrix, left-to-right product."""
    M = I_INT
    for ch in w:
        M = imatmul(M, R_INT if ch == "R" else L_INT)
    return M


def itrace(M):
    return M[0][0] + M[1][1]


def idet(M):
    return M[0][0] * M[1][1] - M[0][1] * M[1][0]


ROWS = []  # (label, word)
for n in range(3, 16):
    ROWS.append((f"n={n}", "R" * (n - 2) + "L"))
for w in ("RRLL", "RLRL", "RRLRL"):
    ROWS.append((w, w))
assert len(ROWS) == 16

row_meta = {}
for label, w in ROWS:
    M = iword(w)
    tr = itrace(M)
    detM = idet(M)
    AmI = ((M[0][0] - 1, M[0][1]), (M[1][0], M[1][1] - 1))
    det_AmI = idet(AmI)
    cond = tr * tr - 4
    row_meta[label] = dict(word=w, trace=tr, det=detM, det_AmI=det_AmI, conductor=cond,
                            hyperbolic=(tr > 2))
    log(f"  {label:8s} word={w:16s} trace={tr:4d} det={detM:2d} "
        f"det(A-I)={det_AmI:5d} conductor(tr^2-4)={cond:6d} hyperbolic={tr>2}")
assert all(v["hyperbolic"] for v in row_meta.values()), "not all words hyperbolic"
assert all(v["det"] == 1 for v in row_meta.values()), "not all words in SL(2,Z)"

# ============================================================================
log("STEP 2: build stages SU(3)_k, k=1..12 (kappa = k+3 = 4..15), ONCE each")


def odd_even_basis(L, S):
    """Orthonormal basis for the theta-odd subspace ((e_a-e_b)/sqrt2 per pair)
    and the theta-even subspace, as N x N unitary change-of-basis [odd|even]."""
    fixed_idx, pairs = L.theta_split()
    N = S.rows
    n_odd = len(pairs)
    n_even = len(fixed_idx) + len(pairs)
    odd = mp.matrix(N, n_odd)
    even = mp.matrix(N, n_even)
    s2 = 1 / mp.sqrt(2)
    for jj, (a, b) in enumerate(pairs):
        odd[a, jj], odd[b, jj] = s2, -s2
        even[a, jj], even[b, jj] = s2, s2
    for jj, i in enumerate(fixed_idx):
        even[i, len(pairs) + jj] = 1
    return odd, even


def block(basis, M):
    return basis.T * M * basis


def trace_of(M):
    return sum(M[i, i] for i in range(M.rows))


log("  NOTE: the theta-odd subspace is NOT fixed at dim 2 for general k -- that")
log("  was specific to SU(3)_2 (k=2). dim(odd) = #conjugate-pairs, which grows")
log("  with k (H3's 'hearing plane' is the k=2 special case). 'tr of the")
log("  theta-odd block' generalizes naturally as: sum of diagonal entries of")
log("  rho(word) restricted to whatever theta-odd subspace THAT level has --")
log("  legitimate because S,T are theta-equivariant (charge-conjugation is a")
log("  symmetry of the modular data at every level), verified below per stage.")

STAGES = {}
theta_gates = {}
for k in range(1, 13):
    kappa = k + 3
    t0 = time.time()
    Lk = An_Level(n=3, k=k, name=f"SU(3)_{k}")
    Sk, Tk = Lk.build(verbose=False)
    fixed_idx, pairs = Lk.theta_split()
    N = Sk.rows
    assert len(fixed_idx) + 2 * len(pairs) == N, f"theta-split does not partition N at k={k}"

    # legitimacy gate: theta (conjugation permutation) must commute with S,T,
    # i.e. S and T must be block-diagonal in the odd|even basis -- otherwise
    # "the theta-odd block" is not a well-defined restriction.
    Theta = mp.zeros(N, N)
    for i in fixed_idx:
        Theta[i, i] = 1
    for a, b in pairs:
        Theta[a, b] = 1
        Theta[b, a] = 1
    comm_S = Theta * Sk - Sk * Theta
    comm_T = Theta * Tk - Tk * Theta
    dev_S = max(abs(comm_S[i, j]) for i in range(N) for j in range(N))
    dev_T = max(abs(comm_T[i, j]) for i in range(N) for j in range(N))
    theta_equivariant = bool(dev_S < mp.mpf('1e-30') and dev_T < mp.mpf('1e-30'))
    theta_gates[kappa] = dict(dev_S=mp.nstr(dev_S, 6), dev_T=mp.nstr(dev_T, 6),
                               theta_equivariant=theta_equivariant)

    odd, even = odd_even_basis(Lk, Sk)
    Tm, Sm = block(odd, Tk), block(odd, Sk)
    Rop = Tm
    Lop = Sm * (Tm ** -1) * (Sm ** -1)
    STAGES[kappa] = dict(k=k, N=N, n_odd=len(pairs), Rop=Rop, Lop=Lop)
    log(f"  kappa={kappa:2d} (k={k:2d}): built, N={N:3d}, odd-dim={len(pairs):2d}, "
        f"theta-equivariant(S,T)={theta_equivariant} "
        f"(dev_S={mp.nstr(dev_S,3)}, dev_T={mp.nstr(dev_T,3)})  ({time.time()-t0:.2f}s)")

ALL_THETA_EQUIVARIANT = all(v["theta_equivariant"] for v in theta_gates.values())
log(f"  ALL STAGES THETA-EQUIVARIANT (block-diagonal decomposition legitimate): "
    f"{ALL_THETA_EQUIVARIANT}")
assert ALL_THETA_EQUIVARIANT, "theta-odd block is not well-defined at some stage -- STOP"

# ============================================================================
log("STEP 3: evaluate all 16 words x 12 stages -- theta-odd block traces")


def word_op(w, Rop, Lop):
    M = mp.eye(Rop.rows)
    for ch in w:
        M = M * (Rop if ch == "R" else Lop)
    return M


def q(x, grid=mp.mpf(10) ** 20):
    return int(mp.floor(x * grid + mp.mpf('0.5')))


MATRIX = {}  # MATRIX[label][kappa] = dict(re,im,modulus,re_q,im_q,mod_q,is_real)
for label, w in ROWS:
    MATRIX[label] = {}
    for kappa in range(4, 16):
        st = STAGES[kappa]
        Mop = word_op(w, st["Rop"], st["Lop"])
        tr = trace_of(Mop)
        re, im = mp.re(tr), mp.im(tr)
        modv = mp.sqrt(re * re + im * im)
        MATRIX[label][kappa] = dict(
            re=mp.nstr(re, 35), im=mp.nstr(im, 35), modulus=mp.nstr(modv, 35),
            re_val=re, im_val=im, mod_val=modv,
            re_q=q(re), im_q=q(im), mod_q=q(modv),
            is_real=bool(abs(im) < mp.mpf('1e-30')),
        )
    vals = " ".join(f"{mp.nstr(MATRIX[label][kk]['mod_val'],6):>9s}" for kk in range(4, 16))
    log(f"  {label:8s} |tr_odd| @ kappa=4..15: {vals}")

# ============================================================================
log("STEP 4: GATES")
gates = {}

g1_val = MATRIX["n=3"][5]
g1 = (abs(g1_val["re_val"] - (-1 / phi)) < mp.mpf('1e-30') and abs(g1_val["im_val"]) < mp.mpf('1e-30'))
gates["G1_RL_kappa5_eq_minus_1_over_phi"] = g1
log(f"  G1: (RL='n=3', kappa=5) = {g1_val['re']} + {g1_val['im']}i  "
    f"vs -1/phi = {mp.nstr(-1/phi,25)}   PASS={g1}")

golden_set = [mp.mpf(0), 1 / phi, mp.mpf(1)]


def near_any(x, vals, tol=mp.mpf('1e-25')):
    return any(abs(x - v) < tol for v in vals)


g2_rows = {}
g2 = True
for n in range(3, 16):
    mv = MATRIX[f"n={n}"][5]["mod_val"]
    ok = near_any(mv, golden_set)
    g2_rows[f"n={n}"] = dict(modulus=mp.nstr(mv, 20), ok=ok)
    g2 = g2 and ok
gates["G2_kappa5_singleL_values_in_0_1overphi_1"] = g2
log("  G2: kappa=5 column, single-L family, |value| in {0, 1/phi, 1}:")
for n in range(3, 16):
    r = g2_rows[f"n={n}"]
    log(f"      n={n:2d}: |value|={r['modulus']:>10s}  ok={r['ok']}")
log(f"  G2 PASS={g2}")

rl_g = MATRIX["RRLL"][5]
rlrl_g = MATRIX["RLRL"][5]
rrlrl_g = MATRIX["RRLRL"][5]
g3a = abs(rl_g["mod_val"] - 1) < mp.mpf('1e-25') and abs(rl_g["im_val"]) < mp.mpf('1e-25')
g3b = abs(rlrl_g["re_val"] - (-phi)) < mp.mpf('1e-25') and abs(rlrl_g["im_val"]) < mp.mpf('1e-25')
g3c = abs(rrlrl_g["mod_val"]) < mp.mpf('1e-30')
gates["G3a_RRLL_kappa5_eq_1"] = g3a
gates["G3b_RLRL_kappa5_eq_minus_phi"] = g3b
gates["G3c_RRLRL_kappa5_approx_0"] = g3c
log(f"  G3a: RRLL @ kappa=5 = {rl_g['re']} + {rl_g['im']}i  (want 1.0)        PASS={g3a}")
log(f"  G3b: RLRL @ kappa=5 = {rlrl_g['re']} + {rlrl_g['im']}i  (want -phi)   PASS={g3b}")
log(f"  G3c: RRLRL @ kappa=5 = {rrlrl_g['re']} + {rrlrl_g['im']}i  (want ~0)  PASS={g3c}")

GATES_PASS = all(gates.values())
log(f"  ALL GATES PASS: {GATES_PASS}")
assert GATES_PASS, "B4 GATE FAILURE -- STOP, per task spec"

# ============================================================================
log("STEP 5: ANALYSIS (i) -- per-column distinct |value| sets")


def cluster_moduli(vals, tol=mp.mpf('1e-15')):
    """vals: list of mp values. Returns sorted list of representative distinct values."""
    reps = []
    for v in sorted(vals):
        if not any(abs(v - r) < tol for r in reps):
            reps.append(v)
    return reps


column_value_sets = {}
for kappa in range(4, 16):
    mods = [MATRIX[label][kappa]["mod_val"] for label, _ in ROWS]
    reps = cluster_moduli(mods)
    column_value_sets[kappa] = [mp.nstr(r, 20) for r in reps]
    log(f"  kappa={kappa:2d}: {len(reps)} distinct |value|(s): "
        f"{[mp.nstr(r,10) for r in reps]}")

# ============================================================================
log("STEP 6: ANALYSIS (ii) -- the diagonal hypothesis (row minima vs conductor)")

log("  divisibility test (BOTH directions, since conductor can be << or >> kappa):")
log("    (a) kappa % conductor == 0  (conductor divides kappa -- relevant when cond<=15)")
log("    (b) conductor % kappa == 0  (kappa divides conductor -- relevant when cond>15)")

# background-value diagnostic: which |value| appears in the most (row,stage)
# cells overall -- ties at this generic value are a weaker signal than a
# distinctive, rare minimum.
from collections import Counter
bg_counter = Counter()
for label, _ in ROWS:
    for kappa in range(4, 16):
        bg_counter[q(MATRIX[label][kappa]["mod_val"], grid=mp.mpf(10) ** 8)] += 1
bg_key, bg_count = bg_counter.most_common(1)[0]
bg_value = mp.mpf(bg_key) / mp.mpf(10) ** 8
log(f"  most common |value| across the whole 16x12 matrix: {mp.nstr(bg_value,10)} "
    f"({bg_count}/{16*12} cells) -- ties at this value are the weak/generic signal")

row_minima = {}
for label, w in ROWS:
    entries = [(kappa, MATRIX[label][kappa]["mod_val"]) for kappa in range(4, 16)]
    nonzero = [(kk, v) for kk, v in entries if v > mp.mpf('1e-20')]
    if not nonzero:
        row_minima[label] = dict(min_stages=[], min_value=None, note="all entries ~0")
        continue
    minval = min(v for _, v in nonzero)
    tol = mp.mpf('1e-10')
    min_stages = [kk for kk, v in nonzero if abs(v - minval) < tol]
    cond = row_meta[label]["conductor"]
    divisors_of_cond_in_range = [kk for kk in range(4, 16) if cond % kk == 0]
    multiples_of_cond_in_range = [kk for kk in range(4, 16) if kk % cond == 0]
    gcds = {kk: gcd(cond, kk) for kk in range(4, 16)}
    dir_a = [kk for kk in min_stages if kk % cond == 0]        # cond | kappa
    dir_b = [kk for kk in min_stages if cond % kk == 0]        # kappa | cond
    either = sorted(set(dir_a) | set(dir_b))
    is_generic_bg = bool(abs(minval - bg_value) < mp.mpf('1e-6'))
    row_minima[label] = dict(
        conductor=cond, min_value=mp.nstr(minval, 20), min_stages=min_stages,
        is_generic_background_value=is_generic_bg,
        divisors_of_conductor_in_4_15=divisors_of_cond_in_range,
        multiples_of_conductor_in_4_15=multiples_of_cond_in_range,
        gcd_at_min_stage={kk: gcds[kk] for kk in min_stages},
        min_stages_matching_cond_divides_kappa=dir_a,
        min_stages_matching_kappa_divides_cond=dir_b,
        min_stages_matching_either_direction=either,
        all_min_stages_on_conductor=bool(len(either) == len(min_stages) and len(min_stages) > 0),
        frac_min_stages_on_conductor=(len(either) / len(min_stages)) if min_stages else 0.0,
    )
    log(f"  {label:8s} cond={cond:6d}  min|value|={mp.nstr(minval,10):>10s}"
        f"{'(*generic bg*)' if is_generic_bg else '':16s} @ kappa={min_stages}  "
        f"on-conductor(either dir)={either}  "
        f"frac={row_minima[label]['frac_min_stages_on_conductor']:.2f}")

n_rows_all_on_conductor = sum(1 for v in row_minima.values() if v.get("all_min_stages_on_conductor"))
n_rows_generic_bg = sum(1 for v in row_minima.values() if v.get("is_generic_background_value"))
log(f"  rows whose minimum sits ENTIRELY on conductor-divisibility stage(s) "
    f"(either direction): {n_rows_all_on_conductor}/{len(ROWS)}")
log(f"  rows whose minimum IS the generic background value ({mp.nstr(bg_value,6)}): "
    f"{n_rows_generic_bg}/{len(ROWS)} (weak signal: minimum ties a common value, "
    f"not a distinctive quiet spot)")

# specific checks called out by the sealed hypothesis
tr4_label = "n=4"  # R^2 L, trace 4, conductor 12
tr4_at_12 = MATRIX[tr4_label][12]
guess_val = 2 - mp.sqrt(3)
tr4_check = dict(
    conductor=row_meta[tr4_label]["conductor"],
    value_at_kappa12=mp.nstr(tr4_at_12["mod_val"], 25),
    is_row_minimum_at_12=(12 in row_minima[tr4_label]["min_stages"]),
    matches_2_minus_sqrt3=bool(abs(tr4_at_12["mod_val"] - guess_val) < mp.mpf('1e-25')),
)
log(f"  SPECIAL CHECK tr-4 word ({tr4_label}, conductor=12) @ kappa=12: "
    f"|value|={tr4_check['value_at_kappa12']}  "
    f"is-row-min-at-12={tr4_check['is_row_minimum_at_12']}  "
    f"== 2-sqrt3={mp.nstr(guess_val,20)}: {tr4_check['matches_2_minus_sqrt3']}")

golden_check = dict(
    conductor=row_meta["n=3"]["conductor"],
    min_stages=row_minima["n=3"]["min_stages"],
    min_value=row_minima["n=3"]["min_value"],
)
log(f"  SPECIAL CHECK golden row (n=3, conductor=5): min @ kappa="
    f"{golden_check['min_stages']}  value={golden_check['min_value']} "
    f"(banked 1/phi = {mp.nstr(1/phi,20)})")

# ============================================================================
log("STEP 7: ANALYSIS (iii) -- the realness catalog")

realness_catalog = {}
for label, w in ROWS:
    flags = {kappa: MATRIX[label][kappa]["is_real"] for kappa in range(4, 16)}
    realness_catalog[label] = flags
    n_real = sum(flags.values())
    log(f"  {label:8s} real at {n_real:2d}/12 stages: "
        f"{[kk for kk in range(4,16) if flags[kk]]}")

# test: "det(A-I) unit => real" -- per row (word-level property, det(A-I) is
# stage-independent since it's the exact SL(2,Z) integer word matrix)
det_unit_test = {}
for label, w in ROWS:
    det_AmI = row_meta[label]["det_AmI"]
    is_unit = abs(det_AmI) == 1
    always_real = all(realness_catalog[label].values())
    never_real = not any(realness_catalog[label].values())
    det_unit_test[label] = dict(
        det_AmI=det_AmI, is_unit=is_unit,
        always_real=always_real, never_real=never_real,
        n_real_stages=sum(realness_catalog[label].values()),
    )
    log(f"  {label:8s} det(A-I)={det_AmI:5d} unit={is_unit!s:5s}  "
        f"always_real={always_real!s:5s}  never_real={never_real!s:5s}  "
        f"(real at {det_unit_test[label]['n_real_stages']}/12)")

counterexamples = [lbl for lbl, d in det_unit_test.items()
                    if d["always_real"] and not d["is_unit"]]
false_negatives = [lbl for lbl, d in det_unit_test.items()
                    if d["is_unit"] and not d["always_real"]]
log(f"  counterexamples to 'det(A-I) unit => real' (real but non-unit det(A-I)): "
    f"{counterexamples}")
log(f"  words with unit det(A-I) that are NOT always real: {false_negatives}")

# ============================================================================
log("STEP 8: save b4_matrix.json")

out = {
    "prereg_sha256": actual_sha,
    "prereg_clause": "B4 (THE CROSS-LANDSCAPE)",
    "seal_match": seal_match,
    "dps": mp.mp.dps,
    "rows": [label for label, _ in ROWS],
    "row_meta": row_meta,
    "stages": {str(kk): {"k": STAGES[kk]["k"], "N": STAGES[kk]["N"], "n_odd": STAGES[kk]["n_odd"],
                         "theta_gate": theta_gates[kk]} for kk in range(4, 16)},
    "matrix": {
        label: {
            str(kappa): {
                "re": MATRIX[label][kappa]["re"],
                "im": MATRIX[label][kappa]["im"],
                "modulus": MATRIX[label][kappa]["modulus"],
                "is_real": MATRIX[label][kappa]["is_real"],
            }
            for kappa in range(4, 16)
        }
        for label, _ in ROWS
    },
    "gates": gates,
    "gates_pass": GATES_PASS,
    "analysis_i_column_value_sets": column_value_sets,
    "analysis_ii_diagonal": {
        "row_minima": row_minima,
        "n_rows_all_min_stages_on_conductor": n_rows_all_on_conductor,
        "n_rows_min_is_generic_background": n_rows_generic_bg,
        "background_value": mp.nstr(bg_value, 10),
        "n_rows_total": len(ROWS),
        "tr4_special_check": tr4_check,
        "golden_special_check": golden_check,
    },
    "analysis_iii_realness": {
        "realness_flags": {lbl: {str(k): v for k, v in flags.items()}
                            for lbl, flags in realness_catalog.items()},
        "det_AmI_unit_test": det_unit_test,
        "counterexamples_real_without_unit_det": counterexamples,
        "unit_det_but_not_always_real": false_negatives,
    },
    "runtime_s": time.time() - T0,
}

json_path = os.path.join(HERE, "b4_matrix.json")
with open(json_path, "w") as f:
    json.dump(out, f, indent=2)
log(f"saved: {json_path}")
log("B4 RUN COMPLETE")
