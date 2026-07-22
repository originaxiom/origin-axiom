"""
R4 -- the resonance order-prediction hypothesis: promoting or KILLING V2b's post-hoc lead.
SEALED preregistered design (this cell's whole point is that it is sealed, unlike V2b's
own B7 which was explicitly flagged post-hoc/exploratory).

Reuses <cc2-seat>/seat-work/veins/v2_resonance/lib.py VERBATIM for all core
machinery: fp, U, ph, cost (the nesting-cost statistic), Cga (the coin), incidence_matrix,
is_primitive, best_matched_consecutive_level, word_len_series, null_stats_uniform. No
re-implementation of anything the bank already has.

BACKGROUND (banked, V2b, mechanism.py/FINDINGS_CC2.md): across the 6 GOLD-family
assignments {GOLD, GOLDMIRROR, ASSIGN2a/2b, ASSIGN3a/3b} (all built from the SAME 4 fixed
literal image strings {abAAB, aAB, abAB, aA}, just permuted across letters), density-
normalized nesting cost correlated POSITIVELY with:
    rotating-pair image-length sum  len(sub['a'])+len(sub['A'])   rho=+0.9276  p=0.0077
    Perron root of the incidence matrix                           rho=+0.8857  p=0.0188
Both flagged explicitly as POST-HOC (found only after looking at the 6-point result), on a
small n=6 in-sample set built entirely from one fixed kit of 4 blocks. This cell tests both
predictors OUT OF SAMPLE, on 8 FRESH substitutions built from a different generative
principle (not permutations of the old 4 blocks), with the predictions written and hashed
BEFORE any nesting cost is computed.

Execution order in this file (the order IS the honesty mechanism -- do not reorder):
  PART A: construct the 8 fresh substitutions, check primitivity, check distinctness from
          every named prior substitution, compute Perron root + rotating-pair length sum,
          derive the two predicted cost orderings, WRITE r4_predictions_SEALED.txt, hash it.
  --- SEAL BARRIER (printed explicitly) ---
  PART B: growth-scan for matched levels (hi length nearest 243), compute raw nesting cost,
          uniform-phase null (500 trials), normalized cost = raw/null.
  PART C: Spearman rho per predictor vs the measured order; apply the sealed promotion
          threshold (|rho|>=0.8 AND p<0.05); report plainly, including disagreement if any.
"""
import hashlib
import json
import os
import sys
import time

import numpy as np
from scipy.stats import spearmanr

sys.path.insert(0, '<cc2-seat>/seat-work/veins/v2_resonance')
import lib as L

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(HERE, 'outputs')
os.makedirs(OUT_DIR, exist_ok=True)
SEALED_PATH = os.path.join(HERE, 'r4_predictions_SEALED.txt')

T_START = time.time()

def hdr(s):
    print("\n" + "=" * 100)
    print(s)
    print("=" * 100)
    sys.stdout.flush()

def sub_(s):
    print("\n" + "-" * 90)
    print(s)
    print("-" * 90)
    sys.stdout.flush()


# ======================================================================================
hdr("PART A -- CONSTRUCTION (no cost computation anywhere in this Part)")
# ======================================================================================

sub_("A0. The generative family, stated exactly")
print("""
FAMILY (\"R4 coupled-Fibonacci-type\"): four integer parameters (i_a, j_a, i_A, j_A) >= 0,
with i_a+j_a >= 1 and i_A+j_A >= 1 (so a's and A's images have content beyond the bare
coupling suffix), plus two short fixed coupling strings bimg (must contain >=1 'A') and
Bimg (must contain >=1 'a'):
    image(a) = 'a'*i_a + 'A'*j_a + 'b'
    image(A) = 'A'*i_A + 'a'*j_A + 'B'
    image(b) = bimg
    image(B) = Bimg
Why this is primitive for ANY valid parameter choice: the fixed trailing 'b'/'B' suffixes
plus bimg containing 'A' and Bimg containing 'a' give the backbone 4-cycle
    a -> b -> A -> B -> a
so the incidence matrix is irreducible regardless of (i_a,j_a,i_A,j_A). Self-loops at a
(if i_a>=1) or A (if i_A>=1), or the 3-cycles created by j_a>=1 (a->A->B->a) or j_A>=1
(A->a->b->A), break the pure period-4 case -- so the matrix is primitive (checked below,
not just argued) for every parameter combination used here.

Parameter selection (design-stage tooling, NOT itself sealed/scientific content -- only the
final 8 image strings below are): searched (scratch scripts explore_family.py/2/3.py in
this directory, fixed search seed 44) for 8 tuples whose Perron roots land close to 8
targets evenly spaced across [1.8, 4.2], while also reducing the incidental collinearity
between Perron root and rotating-pair length sum that a naive single-knob sweep of this
family produces (an unconstrained search gave within-set rho=0.96 between the two
predictors -- nearly degenerate as a two-predictor test; varying bimg/Bimg content, which
moves Perron root without moving len(a)+len(A) at all, brought this down to rho=0.52,
p=0.19, i.e. the two predictors are NOT forced to agree in this design, so the 8-point test
below can actually distinguish them.
""")

# --- The 8 substitutions, hardcoded (parameters found by the search above) ---
def make_sub(ia, ja, iA, jA, bimg, Bimg):
    return {'a': 'a' * ia + 'A' * ja + 'b',
            'A': 'A' * iA + 'a' * jA + 'B',
            'b': bimg, 'B': Bimg}

R4_PARAMS = [
    ('R4_1', dict(ia=1, ja=0, iA=1, jA=1, bimg='A',   Bimg='a')),
    ('R4_2', dict(ia=1, ja=0, iA=0, jA=1, bimg='ABB', Bimg='aB')),
    ('R4_3', dict(ia=0, ja=1, iA=0, jA=1, bimg='AbB', Bimg='aaB')),
    ('R4_4', dict(ia=2, ja=3, iA=1, jA=0, bimg='AAB', Bimg='a')),
    ('R4_5', dict(ia=2, ja=2, iA=2, jA=0, bimg='AbB', Bimg='aB')),
    ('R4_6', dict(ia=3, ja=0, iA=2, jA=1, bimg='ABB', Bimg='ab')),
    ('R4_7', dict(ia=3, ja=1, iA=0, jA=1, bimg='AAB', Bimg='aaB')),
    ('R4_8', dict(ia=4, ja=0, iA=0, jA=1, bimg='AbB', Bimg='abb')),
]
R4 = {name: make_sub(**p) for name, p in R4_PARAMS}
R4_names = [name for name, _ in R4_PARAMS]

print("The 8 fresh substitutions (exact image strings):")
for name, p in R4_PARAMS:
    print(f"  {name}: params={p}  sub={R4[name]}")

sub_("A1. Primitivity check (Perron-Frobenius; some matrix power strictly positive)")
primitivity = {}
for name in R4_names:
    M = L.incidence_matrix(R4[name])
    prim, k = L.is_primitive(M)
    primitivity[name] = dict(primitive=bool(prim), k=k, incidence=M.astype(int).tolist())
    print(f"  {name}: incidence=\n{M.astype(int)}\n    primitive={prim} (k={k})")
    assert prim, f"{name} is NOT primitive -- construction invalid, must fix before proceeding"
print("All 8 confirmed primitive.")

sub_("A2. Distinctness from every named prior substitution")
named_existing = dict(GOLD=L.GOLD, GOLDMIRROR=L.GOLDMIRROR, SYMMETRIC=L.SYMMETRIC,
                       UNCOUPLED=L.UNCOUPLED)
S5, S3, S4, S2 = 'abAAB', 'aAB', 'abAB', 'aA'
ASSIGN2b = {'a': S4, 'A': S2, 'b': S5, 'B': S3}
named_existing['ASSIGN2b'] = ASSIGN2b
length_map = {'a': 5, 'b': 3, 'A': 4, 'B': 2}
rand_subs = {}
for seed in [1, 2, 3]:
    rsub, attempts, draw_seed, k = L.make_random_control(seed, length_map)
    rand_subs[f'RAND{seed}'] = rsub
    named_existing[f'RAND{seed}'] = rsub
print("Named prior substitutions (regenerated/reused exactly, for byte-level comparison):")
for k, v in named_existing.items():
    print(f"  {k:10s} = {v}")

all_distinct = True
for name in R4_names:
    for oname, osub in named_existing.items():
        if R4[name] == osub:
            print(f"  COLLISION: {name} == {oname} !!")
            all_distinct = False
for i in range(len(R4_names)):
    for j in range(i + 1, len(R4_names)):
        if R4[R4_names[i]] == R4[R4_names[j]]:
            print(f"  COLLISION within R4 set: {R4_names[i]} == {R4_names[j]} !!")
            all_distinct = False
print(f"\nAll 8 x (5 named + 3 random) + all pairwise-within-8 comparisons distinct? {all_distinct}")
assert all_distinct, "distinctness check failed -- must fix before proceeding"

sub_("A3. Perron root and rotating-pair image-length sum (EXACT, per substitution)")
perron_vals = {}
rotsum_vals = {}
for name in R4_names:
    M = L.incidence_matrix(R4[name])
    ev = np.linalg.eigvals(M)
    perron = float(ev[np.argmax(np.abs(ev))].real)
    rotsum = len(R4[name]['a']) + len(R4[name]['A'])
    perron_vals[name] = perron
    rotsum_vals[name] = rotsum
    print(f"  {name}: Perron={perron:.6f}   rotating-pair length sum (len(a)+len(A))={rotsum}")

within_set_rho, within_set_p = spearmanr([perron_vals[n] for n in R4_names],
                                          [rotsum_vals[n] for n in R4_names])
print(f"\n(Diagnostic) Spearman(Perron, rotating-sum) WITHIN this 8-point design: "
      f"rho={within_set_rho:.4f} p={within_set_p:.4f} "
      f"-- the two predictors are NOT forced to agree by construction.")

sub_("A4. THE PREREGISTERED PREDICTIONS (direction fixed from the banked V2b sign, not re-derived)")
print("V2b (banked, mechanism.py B7, n=6, post-hoc): both correlations were POSITIVE --")
print("  Spearman(rotating-pair length sum, headline cost): rho=+0.9276  p=0.0077")
print("  Spearman(Perron root,             headline cost): rho=+0.8857  p=0.0188")
print("i.e. LARGER predictor value -> LARGER (worse) normalized nesting cost. This cell")
print("adopts that direction as the prediction to be tested -- it is not re-derived here,")
print("exactly as instructed (the direction is banked; only the fit on FRESH data is new).")

predicted_order_perron = sorted(R4_names, key=lambda n: perron_vals[n])
predicted_order_rotsum = sorted(R4_names, key=lambda n: rotsum_vals[n])
print(f"\nPREDICTED cost order from Perron root (ascending Perron = ascending/best-first predicted cost):")
print("    " + "  <  ".join(predicted_order_perron))
print(f"\nPREDICTED cost order from rotating-pair length sum (ascending sum = ascending/best-first predicted cost):")
print("    " + "  <  ".join(predicted_order_rotsum))
print(f"\nThe two predicted orders identical? {predicted_order_perron == predicted_order_rotsum}")

sub_("A5. WRITING THE SEALED PREDICTIONS FILE (before any nesting-cost computation)")
sealed_lines = []
sealed_lines.append("R4 -- SEALED PREREGISTERED PREDICTIONS")
sealed_lines.append("Written BEFORE any density-normalized nesting cost is computed for these substitutions.")
sealed_lines.append("This file contains ONLY: construction, primitivity, Perron root, rotating-pair length")
sealed_lines.append("sum, and the two predicted cost orderings. No cost values appear anywhere below.")
sealed_lines.append("")
sealed_lines.append(f"Timestamp (local, at write time): {time.strftime('%Y-%m-%d %H:%M:%S')}")
sealed_lines.append("")
sealed_lines.append("--- The 8 fresh substitutions (alphabet a,b,A,B; coins Cga: a,A rotate, b,B identity) ---")
for name, p in R4_PARAMS:
    sealed_lines.append(f"{name}: params={p}")
    sealed_lines.append(f"    sub = {R4[name]}")
    sealed_lines.append(f"    primitive = {primitivity[name]['primitive']}  (k={primitivity[name]['k']})")
sealed_lines.append("")
sealed_lines.append("--- Distinctness from GOLD/GOLDMIRROR/SYMMETRIC/UNCOUPLED/ASSIGN2b/V2-randoms ---")
sealed_lines.append(f"All distinct (pairwise dict equality checked): {all_distinct}")
for k, v in named_existing.items():
    sealed_lines.append(f"    {k:10s} = {v}")
sealed_lines.append("")
sealed_lines.append("--- Perron root and rotating-pair image-length sum (EXACT) ---")
for name in R4_names:
    sealed_lines.append(f"    {name}: Perron={perron_vals[name]:.6f}   rotating_sum={rotsum_vals[name]}")
sealed_lines.append(f"    (diagnostic) within-set Spearman(Perron,rotating_sum) = {within_set_rho:.4f} (p={within_set_p:.4f})")
sealed_lines.append("")
sealed_lines.append("--- Predicted direction (inherited from banked V2b sign, NOT re-derived here) ---")
sealed_lines.append("V2b banked (n=6, post-hoc): rho(rotating_sum,cost)=+0.9276 p=0.0077; rho(Perron,cost)=+0.8857 p=0.0188.")
sealed_lines.append("Direction adopted: LARGER predictor value -> predicted LARGER (worse) normalized nesting cost.")
sealed_lines.append("")
sealed_lines.append("--- PREDICTED COST ORDER #1 (from Perron root, ascending = best/lowest cost first) ---")
sealed_lines.append("    " + "  <  ".join(predicted_order_perron))
sealed_lines.append("")
sealed_lines.append("--- PREDICTED COST ORDER #2 (from rotating-pair length sum, ascending = best/lowest cost first) ---")
sealed_lines.append("    " + "  <  ".join(predicted_order_rotsum))
sealed_lines.append("")
sealed_lines.append(f"The two predicted orders identical? {predicted_order_perron == predicted_order_rotsum}")
sealed_lines.append("")
sealed_lines.append("--- SEALED PROMOTION THRESHOLD (decided now, applied later without modification) ---")
sealed_lines.append("For each predictor independently: PROMOTE to registered law-candidate iff")
sealed_lines.append("    |Spearman rho (predictor, measured normalized cost across these 8 points)| >= 0.8")
sealed_lines.append("    AND p < 0.05")
sealed_lines.append("Otherwise: that predictor's V2b lead DIES (banked kill). Both rho's reported regardless")
sealed_lines.append("of outcome; any sign or significance disagreement between the two predictors will be")
sealed_lines.append("stated plainly.")
sealed_lines.append("")
sealed_lines.append("--- Cost computation plan (to be executed AFTER this file is written and hashed) ---")
sealed_lines.append("Matched level pair per substitution: consecutive levels (lo,hi) whose hi word length is")
sealed_lines.append("nearest (log-ratio) to 243, via lib.best_matched_consecutive_level -- same convention as")
sealed_lines.append("GOLD(3,4)'s own hi length in V2/V2b. Null: uniform-phase, 500 trials (lib.null_stats_uniform).")
sealed_lines.append("Normalized cost = raw_cost / mean(null). No Haar null this time (not part of this cell's")
sealed_lines.append("sealed design, unlike V2/V2b).")
sealed_lines.append("")
sealed_lines.append("NO COST VALUE OF ANY KIND APPEARS ABOVE THIS LINE. End of sealed predictions.")

sealed_content = "\n".join(sealed_lines) + "\n"
with open(SEALED_PATH, 'w') as f:
    f.write(sealed_content)

sha256 = hashlib.sha256(sealed_content.encode('utf-8')).hexdigest()
print(f"Wrote {SEALED_PATH}  ({len(sealed_content)} bytes)")
print(f"SHA256({os.path.basename(SEALED_PATH)}) = {sha256}")
with open(os.path.join(HERE, 'r4_predictions_SEALED.sha256'), 'w') as f:
    f.write(f"{sha256}  {os.path.basename(SEALED_PATH)}\n")

print("\n" + "#" * 100)
print("### SEAL BARRIER -- everything above this line was computed/written with ZERO nesting-cost")
print("### values in scope. Everything below now proceeds to compute actual costs.")
print("#" * 100)
sys.stdout.flush()


# ======================================================================================
hdr("PART B -- COST COMPUTATION (only now; predictions above are frozen)")
# ======================================================================================

sub_("B0. Growth scan + matched levels (target hi word length = 243, consecutive levels)")
TARGET_HI = 243
matched_levels = {}
growth_tables = {}
for name in R4_names:
    series = L.word_len_series(R4[name], max_level=20, max_len=1000)
    growth_tables[name] = series
    lo_lvl, hi_lvl, lo_len, hi_len = L.best_matched_consecutive_level(R4[name], TARGET_HI, max_level=20, max_len=1000)
    matched_levels[name] = (lo_lvl, hi_lvl, lo_len, hi_len)
    print(f"  {name}: growth={series}")
    print(f"          matched levels ({lo_lvl},{hi_lvl})  lengths {lo_len}->{hi_len}  dims {2*lo_len}->{2*hi_len}")

max_dim = max(2 * hi_len for (_, _, _, hi_len) in matched_levels.values())
print(f"\nMax hi-dimension across all 8: {max_dim}  (runtime guard: dims <= 1000)")
assert max_dim <= 1000, "runtime guard exceeded -- a substitution grows too fast for the 20-min budget"

sub_("B1. Raw nesting cost + uniform-phase null (500 trials) + normalized cost")
SEED_BASE_R4_NULL = 45   # distinct from the design-search seed (44, non-scientific); arbitrary, fixed, stated
UNIFORM_TRIALS = 500
results = {}
for i, name in enumerate(R4_names):
    t0 = time.time()
    lo_lvl, hi_lvl, lo_len, hi_len = matched_levels[name]
    wlo = L.fp(R4[name], lo_lvl)
    whi = L.fp(R4[name], hi_lvl)
    dim_lo, dim_hi = 2 * len(wlo), 2 * len(whi)
    raw_cost = L.cost(L.ph(L.U(wlo, L.Cga)), L.ph(L.U(whi, L.Cga)))
    rng = np.random.default_rng(SEED_BASE_R4_NULL * 1000 + i)
    null_vals = L.null_stats_uniform(dim_lo, dim_hi, rng, UNIFORM_TRIALS)
    null_mean, null_std = float(null_vals.mean()), float(null_vals.std(ddof=1))
    normalized = raw_cost / null_mean
    results[name] = dict(lo=lo_lvl, hi=hi_lvl, word_lo=len(wlo), word_hi=len(whi),
                          dim_lo=dim_lo, dim_hi=dim_hi, raw_cost=raw_cost,
                          null_mean=null_mean, null_std=null_std, normalized_cost=normalized,
                          elapsed_s=time.time() - t0)
    print(f"  [{name}] word {len(wlo)}->{len(whi)}  dim {dim_lo}->{dim_hi}  raw={raw_cost:.6e}  "
          f"null_mean={null_mean:.6e}(+/-{null_std:.2e},n={UNIFORM_TRIALS})  "
          f"normalized={normalized:.6e}  [{time.time()-t0:.2f}s]")
    sys.stdout.flush()

total_elapsed = time.time() - T_START
print(f"\nTotal elapsed so far: {total_elapsed:.1f}s (guard: ~20 min = 1200s)")


# ======================================================================================
hdr("PART C -- SPEARMAN ANALYSIS + SEALED PROMOTION VERDICT")
# ======================================================================================

measured_order = sorted(R4_names, key=lambda n: results[n]['normalized_cost'])
print("MEASURED order (ascending normalized cost, i.e. best/lowest cost first):")
print("    " + "  <  ".join(measured_order))
print("\nPREDICTED order (Perron root, from the sealed file):")
print("    " + "  <  ".join(predicted_order_perron))
print("\nPREDICTED order (rotating-pair length sum, from the sealed file):")
print("    " + "  <  ".join(predicted_order_rotsum))

perron_arr = [perron_vals[n] for n in R4_names]
rotsum_arr = [rotsum_vals[n] for n in R4_names]
cost_arr = [results[n]['normalized_cost'] for n in R4_names]

rho_perron, p_perron = spearmanr(perron_arr, cost_arr)
rho_rotsum, p_rotsum = spearmanr(rotsum_arr, cost_arr)

THRESH_RHO = 0.8
THRESH_P = 0.05
promoted_perron = (abs(rho_perron) >= THRESH_RHO) and (p_perron < THRESH_P)
promoted_rotsum = (abs(rho_rotsum) >= THRESH_RHO) and (p_rotsum < THRESH_P)

print(f"\nSpearman(Perron root, measured normalized cost)          across these 8 fresh points: "
      f"rho={rho_perron:.4f}  p={p_perron:.4f}   PROMOTED={promoted_perron}")
print(f"Spearman(rotating-pair length sum, measured normalized cost) across these 8 fresh points: "
      f"rho={rho_rotsum:.4f}  p={p_rotsum:.4f}   PROMOTED={promoted_rotsum}")
print(f"\nSealed threshold: |rho| >= {THRESH_RHO} AND p < {THRESH_P}")

sub_("C1. Do the two predictors agree?")
sign_agree = np.sign(rho_perron) == np.sign(rho_rotsum)
both_sig = (p_perron < THRESH_P) and (p_rotsum < THRESH_P)
sig_agree = ((p_perron < THRESH_P) == (p_rotsum < THRESH_P))
print(f"Same sign? {sign_agree}  (rho_perron={rho_perron:+.4f}, rho_rotsum={rho_rotsum:+.4f})")
print(f"Same significance-at-0.05 status? {sig_agree}  (p_perron={p_perron:.4f}, p_rotsum={p_rotsum:.4f})")
if not sign_agree:
    print("*** THE TWO PREDICTORS DISAGREE IN SIGN on this fresh 8-point set. Stated plainly. ***")
if not sig_agree:
    print("*** THE TWO PREDICTORS DISAGREE IN SIGNIFICANCE (one crosses p<0.05, the other does not). "
          "Stated plainly. ***")
if sign_agree and sig_agree:
    print("The two predictors agree in both sign and significance status on this fresh set.")

sub_("C2. FINAL VERDICT")
if promoted_perron and promoted_rotsum:
    verdict = "BOTH predictors PROMOTED to registered law-candidate status."
elif promoted_perron or promoted_rotsum:
    winner = 'Perron root' if promoted_perron else 'rotating-pair length sum'
    loser = 'rotating-pair length sum' if promoted_perron else 'Perron root'
    verdict = f"ONLY {winner} PROMOTED; {loser} DIES (banked kill) on this fresh test."
else:
    verdict = "NEITHER predictor reaches the sealed threshold on fresh data -- V2b's post-hoc lead DIES (banked kill)."
print(verdict)

# ------------------------------------------------------------------
# Save everything
# ------------------------------------------------------------------
out = dict(
    sealed_file=SEALED_PATH, sealed_sha256=sha256,
    substitutions={name: R4[name] for name in R4_names},
    params={name: p for name, p in R4_PARAMS},
    primitivity=primitivity,
    distinctness_all_ok=all_distinct,
    named_existing_for_comparison={k: v for k, v in named_existing.items()},
    perron=perron_vals, rotating_sum=rotsum_vals,
    within_set_rho=float(within_set_rho), within_set_p=float(within_set_p),
    predicted_order_perron=predicted_order_perron,
    predicted_order_rotsum=predicted_order_rotsum,
    growth_tables=growth_tables,
    matched_levels={k: list(v) for k, v in matched_levels.items()},
    seed_null=SEED_BASE_R4_NULL, uniform_trials=UNIFORM_TRIALS,
    results=results,
    measured_order=measured_order,
    spearman_perron=dict(rho=float(rho_perron), p=float(p_perron), promoted=bool(promoted_perron)),
    spearman_rotsum=dict(rho=float(rho_rotsum), p=float(p_rotsum), promoted=bool(promoted_rotsum)),
    threshold=dict(rho=THRESH_RHO, p=THRESH_P),
    sign_agree=bool(sign_agree), sig_agree=bool(sig_agree),
    verdict=verdict,
    total_elapsed_s=time.time() - T_START,
)
with open(os.path.join(OUT_DIR, 'r4_results.json'), 'w') as f:
    json.dump(out, f, indent=2)
print(f"\nWrote {os.path.join(OUT_DIR, 'r4_results.json')}")
print(f"\nTOTAL ELAPSED: {time.time() - T_START:.1f}s")
