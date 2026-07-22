#!/usr/bin/env python3
"""N3 -- ONE ORGAN OR TWO. Fine-grid (step 0.05) resolution of R3's residual-hint: are the
kappa=1.1/1.4 local maxima on the box_dim(kappa) plateau (0.1-step grid, depth14) two genuinely
separated peaks, or one broad peak with sub-baseline wiggle?

Full design is PREREGISTERED and SEALED in PREREG_N3.md (sha256 09246f08284a0bcf08ac32b3c0cbcc
68b9257f8c08ff3fba7ce3e7153ecf7686) BEFORE any of this script's target grid points were
computed. This script implements that design mechanically; no criterion or grid choice here
was touched after seeing any target-grid number.

Reuses lib_banked.py VERBATIM (fresh byte-identical copy of veins/v11_kappa/lib_banked.py,
diffed identical, no edits). Adds ONE new, additive function (box_dim_offset, see PREREG) to
get seeded-replicate jitter sigma per point, since box_dim/spectrum/metallic_word are fully
deterministic (no RNG anywhere in lib_banked.py).
"""
import json
import time
import numpy as np
import lib_banked as L

np.seterr(over="ignore", invalid="ignore")

T_START = time.time()
WORKDIR = "<cc2-seat>/seat-work/next_queue/n3_fine_grid"
GRID_TABLE_PATH = f"{WORKDIR}/grid_table.txt"
OUT_JSON = f"{WORKDIR}/n3_results.json"

BANKED_GRID_PATH = "<cc2-seat>/seat-work/veins/v11_kappa/grid_results.json"
BANKED_DEPTH14_PATH = "<cc2-seat>/seat-work/veins/v11_kappa/depth14_results.json"
BANKED_R3_PATH = "<cc2-seat>/seat-work/residuals_loop/r3_peak/r3_results.json"

with open(BANKED_GRID_PATH) as fh:
    BANKED_GRID = {float(k): v for k, v in json.load(fh).items()}
with open(BANKED_DEPTH14_PATH) as fh:
    _d14 = json.load(fh)
BANKED_DEPTH14 = {row["kappa"]: row for row in _d14["rows"]}
with open(BANKED_R3_PATH) as fh:
    _r3 = json.load(fh)
BANKED_R3_FINE = {float(k): v for k, v in _r3["fine_rows"].items()}


def elapsed():
    return time.time() - T_START


def lam_of(kappa):
    mu = float(np.sqrt(2.0 - kappa)) if kappa < 2.0 else 0.0
    return mu, 1j * mu


print("=" * 100)
print("N3 -- ONE ORGAN OR TWO (fine-grid box_dim(kappa) peak-shape resolution)")
print(f"PREREG_N3.md sha256 = 09246f08284a0bcf08ac32b3c0cbcc68b9257f8c08ff3fba7ce3e7153ecf7686")
print("=" * 100, flush=True)

# ====================================================================================================
# ANCHOR GATE -- HARD STOP. Reproduce banked numbers with THIS work dir's fresh lib_banked.py
# copy before trusting anything new (per task instructions and PREREG_N3.md).
# ====================================================================================================
print("\n" + "-" * 100)
print("ANCHOR GATE (HARD STOP before any target grid point is computed)")
print("-" * 100)

GOLDEN13 = L.metallic_word(13, 1)
GOLDEN14 = L.metallic_word(14, 1)
print(f"word13 length = {len(GOLDEN13)}   word14 length = {len(GOLDEN14)}", flush=True)

gate_rows = []

# (1) kappa=1.0 depth13 vs grid_results.json
mu, lam = lam_of(1.0)
t0 = time.time()
d13_fresh = L.box_dim(L.spectrum(GOLDEN13, lam, periodic=True))
t1 = time.time() - t0
d13_banked = BANKED_GRID[1.0]["box_dim_golden_depth13"]
g1_diff = abs(d13_fresh - d13_banked)
g1_pass = g1_diff < 1e-9
gate_rows.append(("kappa=1.0 depth13 vs grid_results.json", d13_fresh, d13_banked, g1_diff, g1_pass))
print(f"(1) kappa=1.0 depth13: fresh={d13_fresh!r} banked={d13_banked!r} diff={g1_diff:.3e} "
      f"pass(<1e-9)={g1_pass}  [{t1:.2f}s]", flush=True)

# (2) kappa=1.0 depth14 vs depth14_results.json
t0 = time.time()
d14_fresh = L.box_dim(L.spectrum(GOLDEN14, lam, periodic=True))
t2 = time.time() - t0
d14_banked = BANKED_DEPTH14[1.0]["box_dim_depth14"]
g2_diff = abs(d14_fresh - d14_banked)
g2_pass = g2_diff < 1e-9
gate_rows.append(("kappa=1.0 depth14 vs depth14_results.json", d14_fresh, d14_banked, g2_diff, g2_pass))
print(f"(2) kappa=1.0 depth14: fresh={d14_fresh!r} banked={d14_banked!r} diff={g2_diff:.3e} "
      f"pass(<1e-9)={g2_pass}  [{t2:.2f}s]", flush=True)

# (3) kappa=1.1 depth14 vs r3_results.json (inside our own target grid)
mu11, lam11 = lam_of(1.1)
t0 = time.time()
d14_11_fresh = L.box_dim(L.spectrum(GOLDEN14, lam11, periodic=True))
t3 = time.time() - t0
d14_11_banked = BANKED_R3_FINE[1.1]["box_dim_depth14"]
g3_diff = abs(d14_11_fresh - d14_11_banked)
g3_pass = g3_diff < 1e-9
gate_rows.append(("kappa=1.1 depth14 vs r3_results.json", d14_11_fresh, d14_11_banked, g3_diff, g3_pass))
print(f"(3) kappa=1.1 depth14: fresh={d14_11_fresh!r} banked={d14_11_banked!r} diff={g3_diff:.3e} "
      f"pass(<1e-9)={g3_pass}  [{t3:.2f}s]", flush=True)


def box_dim_offset(ev, rng, scales=2.0 ** np.arange(-2, -8, -1)):
    """ADDITIVE (not a lib_banked.py edit): identical normalization + log-log slope fit as
    L.box_dim, each scale given an independent random ORIGIN offset in [0,s) (standard
    box-counting placement-jitter estimator; no wraparound -- see PREREG_N3.md)."""
    P = np.c_[ev.real, ev.imag]
    rng_range = np.ptp(P, axis=0)
    rng_range[rng_range == 0] = 1
    P = (P - P.min(0)) / rng_range
    Ns = []
    for s in scales:
        ox, oy = rng.uniform(0, s), rng.uniform(0, s)
        Px = P[:, 0] + ox
        Py = P[:, 1] + oy
        cells = set(zip(np.floor(Px / s).astype(int).tolist(), np.floor(Py / s).astype(int).tolist()))
        Ns.append(len(cells))
    return float(np.polyfit(np.log(1 / scales), np.log(np.array(Ns, float)), 1)[0])


class _ZeroRNG:
    def uniform(self, a, b):
        return 0.0


# (4) self-consistency: box_dim_offset at forced zero offset == L.box_dim, bit for bit
d_self_check = box_dim_offset(L.spectrum(GOLDEN14, lam, periodic=True), _ZeroRNG())
g4_diff = abs(d_self_check - d14_fresh)
g4_pass = g4_diff < 1e-12
gate_rows.append(("box_dim_offset(zero) self-consistency vs L.box_dim (kappa=1.0 depth14)",
                   d_self_check, d14_fresh, g4_diff, g4_pass))
print(f"(4) box_dim_offset(zero-offset) self-consistency: mine={d_self_check!r} "
      f"L.box_dim={d14_fresh!r} diff={g4_diff:.3e} pass(<1e-12)={g4_pass}", flush=True)

ALL_GATES_PASS = all(row[4] for row in gate_rows)
print(f"\nALL GATES PASS: {ALL_GATES_PASS}")
if not ALL_GATES_PASS:
    print("\n!!! ANCHOR GATE FAILED -- HARD STOP per task honesty rules. "
          "No target grid point will be computed or trusted.")
    with open(OUT_JSON, "w") as fh:
        json.dump({"gate_rows": gate_rows, "all_gates_pass": False}, fh, indent=2, default=str)
    raise SystemExit(1)
print("GATE PASSED -- proceeding to the sealed fine grid.", flush=True)

# ====================================================================================================
# FINE GRID: 16 points, kappa=0.80..1.55 step 0.05, depth14, point estimate + 10 seeded
# box_dim_offset replicates per point (seed = 1000*i + r).
# ====================================================================================================
print("\n" + "-" * 100)
print("FINE GRID: depth-14 box_dim, kappa in {0.80,...,1.55} step 0.05 (16 points), "
      "10 seeded jitter replicates per point")
print("-" * 100, flush=True)

FINE_GRID = [round(0.80 + 0.05 * i, 2) for i in range(16)]
N_REPLICATES = 10
print(f"FINE_GRID = {FINE_GRID}")
assert len(FINE_GRID) == 16

grid_rows = []
with open(GRID_TABLE_PATH, "w") as gt:
    gt.write("# N3 grid_table.txt -- written incrementally as computed (per task instructions)\n")
    gt.write("# kappa  mu  box_dim_depth14(point_estimate)  jitter_mean10  jitter_std10(ddof=1)  t_spectrum_s\n")
    gt.flush()

    for i, kappa in enumerate(FINE_GRID):
        mu, lam = lam_of(kappa)
        t0 = time.time()
        ev = L.spectrum(GOLDEN14, lam, periodic=True)
        t_spec = time.time() - t0
        d_point = L.box_dim(ev)

        reps = []
        for r in range(N_REPLICATES):
            rng = np.random.default_rng(seed=1000 * i + r)
            reps.append(box_dim_offset(ev, rng))
        reps = np.array(reps)
        jit_mean = float(reps.mean())
        jit_std = float(reps.std(ddof=1))

        row = {"i": i, "kappa": kappa, "mu": mu, "box_dim_depth14": d_point,
               "jitter_replicates": reps.tolist(), "jitter_mean10": jit_mean,
               "jitter_std10": jit_std, "t_spectrum_s": round(t_spec, 3)}
        grid_rows.append(row)

        line = (f"{kappa:.2f}  {mu:.6f}  {d_point:.6f}  {jit_mean:.6f}  {jit_std:.6f}  "
                f"{t_spec:.2f}")
        gt.write(line + "\n")
        gt.flush()
        print(f"  i={i:2d} kappa={kappa:.2f}  mu={mu:.4f}  box_dim={d_point:.6f}  "
              f"jitter(mean/std over {N_REPLICATES})={jit_mean:.6f}/{jit_std:.6f}  "
              f"[t_spectrum={t_spec:.2f}s]  (elapsed={elapsed():.0f}s)", flush=True)

total_grid_time = elapsed()
print(f"\nfine grid complete: {len(grid_rows)} points, total elapsed {total_grid_time:.1f}s", flush=True)

# ====================================================================================================
# POOLED JITTER SIGMA
# ====================================================================================================
per_point_std = np.array([row["jitter_std10"] for row in grid_rows])
pooled_var = float(np.mean(per_point_std ** 2))
POOLED_SIGMA_D14 = float(np.sqrt(pooled_var))
print(f"\nper-point jitter std (10 reps each): "
      f"{[round(s, 5) for s in per_point_std]}")
print(f"POOLED JITTER SIGMA (depth14) = sqrt(mean(s_i^2)) = {POOLED_SIGMA_D14:.6f}")
print(f"2 * pooled_sigma = {2*POOLED_SIGMA_D14:.6f}", flush=True)

# ====================================================================================================
# DECISION CRITERION (mechanical, verbatim from PREREG_N3.md)
# ====================================================================================================
print("\n" + "-" * 100)
print("DECISION CRITERION")
print("-" * 100)

vals = [row["box_dim_depth14"] for row in grid_rows]
N = len(vals)


def find_local_maxima(vals):
    idx = []
    for i in range(len(vals)):
        left_ok = (i == 0) or (vals[i] >= vals[i - 1])
        right_ok = (i == len(vals) - 1) or (vals[i] >= vals[i + 1])
        strict_left = (i > 0) and (vals[i] > vals[i - 1])
        strict_right = (i < len(vals) - 1) and (vals[i] > vals[i + 1])
        if left_ok and right_ok and (strict_left or strict_right or (i == 0 and len(vals) == 1)):
            idx.append(i)
    return idx


local_max_idx = find_local_maxima(vals)
print(f"raw local-maxima indices (grid-sense, see PREREG def): {local_max_idx}  "
      f"(kappas: {[FINE_GRID[i] for i in local_max_idx]})")

# merge contiguous indices into peak regions; representative = highest point in the run,
# ties broken toward the lower-kappa (smaller index) point
regions = []
for i in local_max_idx:
    if regions and i == regions[-1][-1] + 1:
        regions[-1].append(i)
    else:
        regions.append([i])

region_reps = []
for reg in regions:
    reg_vals = [vals[i] for i in reg]
    best_val = max(reg_vals)
    # tie-break toward lower-kappa (smallest index) among ties
    rep_i = next(i for i in reg if vals[i] == best_val)
    region_reps.append(rep_i)

print(f"peak regions (contiguous local-max runs): {regions}")
print(f"region representative indices: {region_reps}  "
      f"(kappas: {[FINE_GRID[i] for i in region_reps]}, values: {[round(vals[i],6) for i in region_reps]})")

n_regions = len(region_reps)
verdict_d14 = None
qualifying_pairs = []

if n_regions == 1:
    verdict_d14 = "ONE-ORGAN"
    print(f"\nExactly one peak region -> ONE-ORGAN (mechanically unimodal).")
else:
    print(f"\n{n_regions} peak regions found -- testing all index-gap>=2 pairs against "
          f"2*pooled_sigma={2*POOLED_SIGMA_D14:.6f}:")
    for a in range(len(region_reps)):
        for b in range(a + 1, len(region_reps)):
            ia, ib = region_reps[a], region_reps[b]
            if ib - ia < 2:
                print(f"  pair (kappa={FINE_GRID[ia]}, kappa={FINE_GRID[ib]}): index-gap={ib-ia} "
                      f"< 2, NOT eligible")
                continue
            intervening = list(range(ia + 1, ib))
            interv_min_val = min(vals[j] for j in intervening)
            interv_min_j = min(intervening, key=lambda j: vals[j])
            margin_a = vals[ia] - interv_min_val
            margin_b = vals[ib] - interv_min_val
            qualifies = (margin_a > 2 * POOLED_SIGMA_D14) and (margin_b > 2 * POOLED_SIGMA_D14)
            print(f"  pair (kappa={FINE_GRID[ia]}={vals[ia]:.6f}, kappa={FINE_GRID[ib]}={vals[ib]:.6f}): "
                  f"index-gap={ib-ia}  valley=kappa={FINE_GRID[interv_min_j]}({interv_min_val:.6f})  "
                  f"marginA={margin_a:.6f}  marginB={margin_b:.6f}  qualifies(TWO-ORGANS)={qualifies}")
            if qualifies:
                qualifying_pairs.append({"ia": ia, "ib": ib, "valley_j": interv_min_j,
                                          "margin_a": margin_a, "margin_b": margin_b,
                                          "combined_margin": margin_a + margin_b})
    if qualifying_pairs:
        verdict_d14 = "TWO-ORGANS"
    else:
        verdict_d14 = "UNRESOLVED"

print(f"\n>>> DEPTH-14 VERDICT: {verdict_d14}")

canonical_pair = None
if qualifying_pairs:
    qualifying_pairs.sort(key=lambda q: (-q["combined_margin"],))
    canonical_pair = qualifying_pairs[0]
    print(f"canonical TWO-ORGANS pair: kappa={FINE_GRID[canonical_pair['ia']]} / "
          f"kappa={FINE_GRID[canonical_pair['ib']]}  valley=kappa={FINE_GRID[canonical_pair['valley_j']]}")
elif n_regions >= 2:
    # UNRESOLVED-at-depth14: still identify the two globally-highest peak regions for the
    # transparency depth-15 run (final verdict stays UNRESOLVED regardless, per PREREG).
    top2_regions = sorted(region_reps, key=lambda i: -vals[i])[:2]
    ia, ib = sorted(top2_regions)
    intervening = list(range(ia + 1, ib)) if ib - ia >= 2 else []
    if intervening:
        interv_min_j = min(intervening, key=lambda j: vals[j])
    else:
        interv_min_j = None
    canonical_pair = {"ia": ia, "ib": ib, "valley_j": interv_min_j,
                       "margin_a": None, "margin_b": None, "combined_margin": None,
                       "note": "UNRESOLVED-at-depth14 transparency pair, does not itself set the verdict"}
    print(f"(UNRESOLVED) transparency pair for depth-15 run: kappa={FINE_GRID[ia]} / kappa={FINE_GRID[ib]}  "
          f"valley=kappa={FINE_GRID[interv_min_j] if interv_min_j is not None else 'N/A'}")

print(f"\ntotal elapsed after depth-14 stage: {elapsed():.1f}s", flush=True)

# ====================================================================================================
# DEPTH-15 CONFIRMATION (sealed branches, PREREG_N3.md; depth15 can only confirm-or-downgrade
# toward UNRESOLVED, never upgrade a depth-14 verdict)
# ====================================================================================================
print("\n" + "-" * 100)
print("DEPTH-15 CONFIRMATION")
print("-" * 100)

GOLDEN15 = L.metallic_word(15, 1)
print(f"word15 length = {len(GOLDEN15)}", flush=True)


def compute_point_d15(tag, kappa, seed_base):
    mu, lam = lam_of(kappa)
    t0 = time.time()
    ev15 = L.spectrum(GOLDEN15, lam, periodic=True)
    t_spec = time.time() - t0
    d_point = L.box_dim(ev15)
    reps = []
    for r in range(N_REPLICATES):
        rng = np.random.default_rng(seed=seed_base + r)
        reps.append(box_dim_offset(ev15, rng))
    reps = np.array(reps)
    return {"kappa": kappa, "box_dim_depth15": d_point, "jitter_mean10": float(reps.mean()),
            "jitter_std10": float(reps.std(ddof=1)), "t_spectrum_s": round(t_spec, 3),
            "jitter_replicates": reps.tolist()}


d15_rows = {}
depth15_confirmation_kind = None
final_verdict = None
survive = None

if verdict_d14 == "ONE-ORGAN":
    depth15_confirmation_kind = "ONE-ORGAN flank check"
    kstar_i = region_reps[0]
    kstar_kappa = FINE_GRID[kstar_i]
    non_peak_idx = [i for i in range(N) if i != kstar_i]
    flank_i = min(non_peak_idx, key=lambda i: (vals[i], -abs(i - kstar_i)))
    flank_kappa = FINE_GRID[flank_i]
    print(f"ONE-ORGAN confirmation set: kappa*={kstar_kappa}  flank={flank_kappa}")
    d15_rows["kstar"] = compute_point_d15("kstar", kstar_kappa, 100000 + 0)
    print(f"  kstar kappa={kstar_kappa}: d15={d15_rows['kstar']['box_dim_depth15']:.6f}  "
          f"jitter_std={d15_rows['kstar']['jitter_std10']:.6f}  [{d15_rows['kstar']['t_spectrum_s']:.1f}s]",
          flush=True)
    d15_rows["flank"] = compute_point_d15("flank", flank_kappa, 100000 + 1000)
    print(f"  flank kappa={flank_kappa}: d15={d15_rows['flank']['box_dim_depth15']:.6f}  "
          f"jitter_std={d15_rows['flank']['jitter_std10']:.6f}  [{d15_rows['flank']['t_spectrum_s']:.1f}s]",
          flush=True)
    sep15 = d15_rows["kstar"]["box_dim_depth15"] - d15_rows["flank"]["box_dim_depth15"]
    survive = sep15 > 2 * POOLED_SIGMA_D14
    print(f"  sep15 (kstar - flank) = {sep15:.6f}  > 2*pooled_sigma_d14({2*POOLED_SIGMA_D14:.6f}) = {survive}")
    final_verdict = "ONE-ORGAN" if survive else "UNRESOLVED"

elif verdict_d14 == "TWO-ORGANS":
    depth15_confirmation_kind = "TWO-ORGANS peakA/valley/peakB check"
    ia, ib, vj = canonical_pair["ia"], canonical_pair["ib"], canonical_pair["valley_j"]
    kA, kV, kB = FINE_GRID[ia], FINE_GRID[vj], FINE_GRID[ib]
    print(f"TWO-ORGANS confirmation set: peakA=kappa={kA}  valley=kappa={kV}  peakB=kappa={kB}")
    d15_rows["peakA"] = compute_point_d15("peakA", kA, 100000 + 0)
    d15_rows["valley"] = compute_point_d15("valley", kV, 100000 + 1000)
    d15_rows["peakB"] = compute_point_d15("peakB", kB, 100000 + 2000)
    for tag in ["peakA", "valley", "peakB"]:
        print(f"  {tag} kappa={d15_rows[tag]['kappa']}: d15={d15_rows[tag]['box_dim_depth15']:.6f}  "
              f"jitter_std={d15_rows[tag]['jitter_std10']:.6f}  [{d15_rows[tag]['t_spectrum_s']:.1f}s]",
              flush=True)
    sepA = d15_rows["peakA"]["box_dim_depth15"] - d15_rows["valley"]["box_dim_depth15"]
    sepB = d15_rows["peakB"]["box_dim_depth15"] - d15_rows["valley"]["box_dim_depth15"]
    survive = (sepA > 2 * POOLED_SIGMA_D14) and (sepB > 2 * POOLED_SIGMA_D14)
    print(f"  sepA={sepA:.6f}  sepB={sepB:.6f}  both > 2*pooled_sigma_d14({2*POOLED_SIGMA_D14:.6f}) = {survive}")
    final_verdict = "TWO-ORGANS" if survive else "UNRESOLVED"

else:  # UNRESOLVED at depth14
    depth15_confirmation_kind = "UNRESOLVED transparency check (does not set final verdict)"
    ia, ib, vj = canonical_pair["ia"], canonical_pair["ib"], canonical_pair["valley_j"]
    kA, kB = FINE_GRID[ia], FINE_GRID[ib]
    print(f"UNRESOLVED transparency confirmation set (2 globally-highest peak regions): "
          f"kappa={kA} / kappa={kB}" + (f"  valley=kappa={FINE_GRID[vj]}" if vj is not None else ""))
    d15_rows["peakA"] = compute_point_d15("peakA", kA, 100000 + 0)
    print(f"  peakA kappa={kA}: d15={d15_rows['peakA']['box_dim_depth15']:.6f}  "
          f"jitter_std={d15_rows['peakA']['jitter_std10']:.6f}  [{d15_rows['peakA']['t_spectrum_s']:.1f}s]",
          flush=True)
    d15_rows["peakB"] = compute_point_d15("peakB", kB, 100000 + 2000)
    print(f"  peakB kappa={kB}: d15={d15_rows['peakB']['box_dim_depth15']:.6f}  "
          f"jitter_std={d15_rows['peakB']['jitter_std10']:.6f}  [{d15_rows['peakB']['t_spectrum_s']:.1f}s]",
          flush=True)
    if vj is not None:
        d15_rows["valley"] = compute_point_d15("valley", FINE_GRID[vj], 100000 + 1000)
        print(f"  valley kappa={FINE_GRID[vj]}: d15={d15_rows['valley']['box_dim_depth15']:.6f}  "
              f"jitter_std={d15_rows['valley']['jitter_std10']:.6f}  [{d15_rows['valley']['t_spectrum_s']:.1f}s]",
              flush=True)
        sepA = d15_rows["peakA"]["box_dim_depth15"] - d15_rows["valley"]["box_dim_depth15"]
        sepB = d15_rows["peakB"]["box_dim_depth15"] - d15_rows["valley"]["box_dim_depth15"]
        print(f"  [transparency only] sepA={sepA:.6f}  sepB={sepB:.6f}  "
              f"(2*pooled_sigma_d14={2*POOLED_SIGMA_D14:.6f}) -- NOT used to set the verdict per PREREG "
              f"(UNRESOLVED-at-depth14 cannot be upgraded by depth15)")
    survive = None
    final_verdict = "UNRESOLVED"

print(f"\n>>> FINAL VERDICT (depth15-adjudicated per PREREG's asymmetric rule): {final_verdict}")
print(f"total elapsed: {elapsed():.1f}s ({elapsed()/60:.2f} min)", flush=True)

# ====================================================================================================
# WRITE JSON
# ====================================================================================================
OUT = {
    "prereg_sha256": "09246f08284a0bcf08ac32b3c0cbcc68b9257f8c08ff3fba7ce3e7153ecf7686",
    "gate_rows": [{"name": r[0], "fresh": r[1], "banked": r[2], "diff": r[3], "pass": r[4]} for r in gate_rows],
    "all_gates_pass": ALL_GATES_PASS,
    "fine_grid_kappas": FINE_GRID,
    "n_replicates": N_REPLICATES,
    "grid_rows": grid_rows,
    "per_point_jitter_std": per_point_std.tolist(),
    "pooled_sigma_d14": POOLED_SIGMA_D14,
    "local_max_idx": local_max_idx,
    "peak_regions": regions,
    "region_reps": region_reps,
    "verdict_d14": verdict_d14,
    "qualifying_pairs": qualifying_pairs,
    "canonical_pair": canonical_pair,
    "depth15_confirmation_kind": depth15_confirmation_kind,
    "d15_rows": d15_rows,
    "survive": survive,
    "final_verdict": final_verdict,
    "total_compute_time_s": elapsed(),
}
with open(OUT_JSON, "w") as fh:
    json.dump(OUT, fh, indent=2, default=lambda o: o.item() if hasattr(o, "item") else str(o))
print(f"\nwrote {OUT_JSON}")
print(f"wrote {GRID_TABLE_PATH}")
