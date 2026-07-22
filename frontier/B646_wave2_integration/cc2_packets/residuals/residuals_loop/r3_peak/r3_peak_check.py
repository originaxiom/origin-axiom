#!/usr/bin/env python3
"""R3 -- the middle-organ PEAK MECHANISM cell (residuals_loop/r3_peak).

Reuses lib_banked.py VERBATIM (fresh copy of veins/v11_kappa/lib_banked.py, byte-identical, no
edits) and the depth14_check.py conventions from v11_kappa: fresh-vs-banked anchor gate before
trusting any new number, per-step wall-clock printing with an edge-dropping fallback guard, and
the V11b top-2-stability + absolute-separation persistence criterion.

BANKED CONTEXT (from veins/v11_kappa, box_dim depth13/14 9-point grid {-1.9..1.9 step 0.5}):
  peak at kappa in {1.0, 1.5} (depth14 ~1.075/1.072 vs baseline ~0.99-1.03), cliff at kappa=1.9;
  gamma (escape_rate) monotone 0.08->0.41 over kappa in (-2,1.9); liftoff_ratio ~0.91 flat.

====================================================================================================
PREREGISTERED DESIGN (locked BEFORE any result below is inspected)
====================================================================================================
(a) FINE GRID kappa in {0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.8} (10 pts) at depth14 box_dim
    (metallic_word(14,1), periodic=True, B186-exact estimator): locate kappa* = argmax and
    classify the peak shape as single / plateau / double.
(b) MECHANISM COMPARISONS -- SEALED LIST, computed for ALL 10 grid points, no post-hoc additions,
    no correlations beyond these three:
      (i)   gamma via the banked escape_rate on the density-converged spectrum_window (calibrate.py
            found gamma stabilizes for N>=200x200; grid_map.py's own official setting
            re=[-4,4] im=[-3,3] n_re=n_im=400 Kmax=30 R=20 is reused verbatim here).
      (ii)  MST-gap/diam at F=1597 (fib_word(16), open BC via H_eig, B163-exact).
      (iii) liftoff ratio = max|Im eig|/mu via fib_word(15) (L=987) periodic diagonalization
            (B162-exact), same as grid_map.py's liftoff_ratio_vs_mu.
    Verdict per comparison: does kappa* sit AT or ADJACENT TO (one grid step; "within grid
    resolution") a local extremum or an inflection (sign change of the discrete 2nd difference)
    of that diagnostic over this SAME 10-point grid?
    SEALED SIGNIFICANCE FLOOR (locked after kernel-cost calibration, BEFORE any fine-grid
    diagnostic was computed; the only values seen so far are the already-banked coarse-grid
    numbers): these diagnostics are deterministic, so every fine-structure wiggle of a
    near-linear curve (banked liftoff spans only 0.907->0.915 over the FULL coarse grid) would
    otherwise register as an "inflection", making MECHANISM-CANDIDATE unfalsifiable. An
    inflection COUNTS only if both flanking |2nd differences| >= median(|2nd difference|) over
    the fine grid (scale-free, robust). Raw unfiltered inflections are still REPORTED for
    transparency but do not enter the verdict. Local extrema need no floor (rank-based).
(c) DEPTH-15 spot-check at {kappa*, the non-argmax partner of the banked (1.0,1.5) pair, 0.0, 1.9}
    (metallic_word(15,1), L=1597, periodic=True): does the peak's separation persist one level
    deeper? V11b criterion adapted to this restricted point set (top-2/pair ranking stability +
    absolute separation vs the 0.0/1.9 baseline pair, using part (a)'s own fine-grid baseline_std
    as the noise scale) -- documented inline below, since V11b's original criterion was defined
    over a full 9/10-point grid at both depths and here depth-15 is deliberately only spot-checked.

HONESTY RULES: anchor gate first (reproduce ONE banked grid point exactly, to float precision,
before trusting anything new); runtime guard ~25 min total wall-clock (if threatened, drop the
FINE_GRID edges first for the expensive part (b) diagnostics, stating so explicitly); no post-hoc
correlations beyond the three sealed comparisons in (b).
DISCLOSURE: the kernel-cost calibration (run after this design was locked, purely to size the
runtime budget) incidentally printed one depth-15 value (kappa=1.0: 1.14943) and re-printed four
already-banked kappa=1.0 diagnostics. No design element was changed in response; the only
subsequent edit was the part-(b) inflection significance floor above, which concerns a different
part of the design and was motivated by the BANKED coarse-grid liftoff range, not by any new number.

LOCKED VERDICTS: ARTIFACT-AT-DEPTH (depth-15 kills the peak) overrides the others; else
MECHANISM-CANDIDATE (>=1 sealed diagnostic aligns with kappa*) or ISOLATED-FEATURE (peak robust,
no diagnostic aligns).
"""
import json
import time
import numpy as np
import lib_banked as L

np.seterr(over="ignore", invalid="ignore")

T_START = time.time()
BUDGET_S = 25 * 60

WORKDIR = "<cc2-seat>/seat-work/residuals_loop/r3_peak"
BANKED_GRID_PATH = "<cc2-seat>/seat-work/veins/v11_kappa/grid_results.json"
BANKED_DEPTH14_PATH = "<cc2-seat>/seat-work/veins/v11_kappa/depth14_results.json"
OUT_JSON = f"{WORKDIR}/r3_results.json"

with open(BANKED_GRID_PATH) as fh:
    BANKED_GRID = {float(k): v for k, v in json.load(fh).items()}
with open(BANKED_DEPTH14_PATH) as fh:
    _d14 = json.load(fh)
BANKED_DEPTH14 = {row["kappa"]: row for row in _d14["rows"]}

FINE_GRID = [0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.8]
WINDOW = dict(re_lo=-4.0, re_hi=4.0, im_lo=-3.0, im_hi=3.0, n_re=400, n_im=400, Kmax=30, R=20.0)


def lam_of(kappa):
    mu = float(np.sqrt(2.0 - kappa)) if kappa < 2.0 else 0.0
    return mu, 1j * mu


def elapsed():
    return time.time() - T_START


print("=" * 100)
print("R3 -- middle-organ peak MECHANISM cell")
print("=" * 100, flush=True)

# ====================================================================================================
# ANCHOR GATE -- rerun ONE banked grid point exactly before trusting the copied machinery.
# (v11_kappa's calibrate.py already gated 4 anchors and depth14_check.py already gated depth13
#  fresh-vs-banked at all 9 grid points; this reruns exactly one of those -- kappa=1.0, depth13
#  golden box_dim -- with THIS work dir's fresh copy of lib_banked.py, to confirm the copy itself
#  reproduces a banked number bit-for-bit before any new r3-specific computation is trusted.)
# ====================================================================================================
print("\n" + "-" * 100)
print("ANCHOR GATE: reproduce one banked grid point exactly (kappa=1.0, box_dim golden depth13)")
print("-" * 100)

GATE_KAPPA = 1.0
mu_g, lam_g = lam_of(GATE_KAPPA)
GOLDEN13 = L.metallic_word(13, 1)
print(f"word13 (golden m=1, depth13) length = {len(GOLDEN13)}")

t0 = time.time()
d13_fresh = L.box_dim(L.spectrum(GOLDEN13, lam_g, periodic=True))
t_gate = time.time() - t0
d13_banked = BANKED_GRID[GATE_KAPPA]["box_dim_golden_depth13"]
gate_diff = abs(d13_fresh - d13_banked)
gate_pass = gate_diff < 1e-9

print(f"kappa={GATE_KAPPA}  box_dim_depth13: fresh={d13_fresh!r}  banked={d13_banked!r}  "
      f"|diff|={gate_diff:.3e}  match(<1e-9)={gate_pass}  [{t_gate:.2f}s]")

if not gate_pass:
    print("\n!!! GATE FAILED -- the copied lib_banked.py does NOT reproduce the banked anchor. "
          "STOPPING per honesty rules (no new results should be trusted).")
    raise SystemExit(1)
print("GATE PASSED -- proceeding.")

# ====================================================================================================
# (a) FINE GRID: depth-14 box_dim over the 10-point kappa grid
# ====================================================================================================
print("\n" + "-" * 100)
print(f"(a) FINE GRID: depth-14 box_dim over kappa in {FINE_GRID}")
print("-" * 100)

GOLDEN14 = L.metallic_word(14, 1)
print(f"word14 (golden m=1, depth14) length = {len(GOLDEN14)}", flush=True)

fine_rows = {}
for kappa in FINE_GRID:
    mu, lam = lam_of(kappa)
    t0 = time.time()
    d14 = L.box_dim(L.spectrum(GOLDEN14, lam, periodic=True))
    dt = time.time() - t0
    fine_rows[kappa] = {"kappa": kappa, "mu": mu, "box_dim_depth14": d14, "t_s": round(dt, 3)}
    print(f"  kappa={kappa:+.2f}  mu={mu:.4f}  box_dim_depth14={d14:.6f}  [{dt:.2f}s]  "
          f"(elapsed={elapsed():.0f}s)", flush=True)

vals_a = [fine_rows[k]["box_dim_depth14"] for k in FINE_GRID]
argmax_i = int(np.argmax(vals_a))
KSTAR = FINE_GRID[argmax_i]
order_desc = sorted(range(len(vals_a)), key=lambda i: -vals_a[i])
top_val = vals_a[order_desc[0]]
second_val = vals_a[order_desc[1]]
second_kappa = FINE_GRID[order_desc[1]]
gap_top2 = top_val - second_val
adjacent_top2 = abs(order_desc[1] - argmax_i) == 1

# noise scale for the peak-shape call: V11b's OWN measured depth14 baseline_std (0.01999,
# from the banked 9-point grid) -- reused here rather than invented fresh, for continuity.
NOISE_V11B = 0.01999203127607128


def find_local_maxima(vals):
    idx = []
    for i in range(len(vals)):
        left_ok = (i == 0) or (vals[i] >= vals[i - 1])
        right_ok = (i == len(vals) - 1) or (vals[i] >= vals[i + 1])
        strict = (i == 0 or vals[i] > vals[i - 1]) or (i == len(vals) - 1 or vals[i] > vals[i + 1])
        if left_ok and right_ok and strict:
            idx.append(i)
    return idx


local_max_idx = find_local_maxima(vals_a)
# group local maxima into peak "regions": consecutive/near indices within NOISE_V11B of the top
peak_region_idx = [i for i in range(len(vals_a)) if (top_val - vals_a[i]) < NOISE_V11B]
# split peak_region_idx into contiguous blocks
blocks = []
for i in sorted(peak_region_idx):
    if blocks and i == blocks[-1][-1] + 1:
        blocks[-1].append(i)
    else:
        blocks.append([i])

if len(blocks) == 1 and len(blocks[0]) == 1:
    shape = "single (clear unique maximum; no other grid point within V11b's baseline_std of the top)"
elif len(blocks) == 1 and len(blocks[0]) > 1:
    shape = (f"plateau ({len(blocks[0])} adjacent grid points "
              f"{[FINE_GRID[i] for i in blocks[0]]} within V11b's baseline_std of the top)")
else:
    shape = (f"double/multi-peak ({len(blocks)} separated regions within baseline_std of the top: "
              f"{[[FINE_GRID[i] for i in b] for b in blocks]})")

print(f"\nkappa* (argmax) = {KSTAR}   box_dim={top_val:.6f}")
print(f"second-highest  = kappa={second_kappa}  box_dim={second_val:.6f}  gap={gap_top2:.6f}  "
      f"adjacent_to_kappa*={adjacent_top2}")
print(f"local maxima (grid-sense) at: {[FINE_GRID[i] for i in local_max_idx]}")
print(f"PEAK SHAPE: {shape}")

# ====================================================================================================
# (b) MECHANISM COMPARISONS -- sealed list, same 10-point grid, processed center-outward so that
# any runtime-guard truncation drops the FINE_GRID edges first (0.8/1.8, then 0.9/1.6, ...).
# ====================================================================================================
print("\n" + "-" * 100)
print("(b) MECHANISM COMPARISONS (sealed: gamma, MST-gap/diam@F=1597, liftoff ratio)")
print("-" * 100)

WORD16 = L.fib_word(16)   # F=1597, open-BC MST-gap word (B163-exact)
FIB15 = L.fib_word(15)    # L=987, liftoff/area word, periodic (B162-exact)
print(f"fib_word(16) length (F for MST-gap) = {len(WORD16)}")
print(f"fib_word(15) length (liftoff word)  = {len(FIB15)}", flush=True)

CENTER = 1.25
order_center_out = sorted(FINE_GRID, key=lambda k: abs(k - CENTER))
print(f"processing order (center-out, for edge-first dropping if the runtime guard trips): "
      f"{order_center_out}")

mech_rows = {}
dropped_b = []
for kappa in order_center_out:
    if elapsed() > BUDGET_S * 0.85:
        dropped_b.append(kappa)
        continue
    mu, lam = lam_of(kappa)
    row = {"kappa": kappa}

    t0 = time.time()
    _, _, _, fcurve = L.spectrum_window(lam, **WINDOW)
    gamma = L.escape_rate(fcurve)
    t_gamma = time.time() - t0
    row["gamma_banked_window"] = gamma

    t0 = time.time()
    mst_gap = L.max_gap_over_diam(L.H_eig(WORD16, lam, periodic=False))
    t_mst = time.time() - t0
    row["mst_gap_over_diam_F1597"] = mst_gap

    t0 = time.time()
    ev15 = L.H_eig(FIB15, lam, periodic=True)
    max_im = float(np.max(np.abs(ev15.imag))) if len(ev15) else 0.0
    liftoff = (max_im / mu) if mu > 1e-9 else None
    t_lift = time.time() - t0
    row["liftoff_ratio_vs_mu"] = liftoff

    mech_rows[kappa] = row
    print(f"  kappa={kappa:+.2f}  gamma={gamma:.5f}[{t_gamma:.1f}s]  "
          f"MSTgap(F1597)={mst_gap:.5f}[{t_mst:.1f}s]  liftoff={liftoff:.5f}[{t_lift:.1f}s]  "
          f"(elapsed={elapsed():.0f}s)", flush=True)

if dropped_b:
    print(f"\n!!! RUNTIME GUARD: >85% of {BUDGET_S}s budget reached -- dropped fine-grid EDGE "
          f"points from part (b) mechanism comparisons: {sorted(dropped_b)}. Stating this plainly "
          f"per the honesty rules; (a)'s box_dim values for these points (already computed, cheap) "
          f"are unaffected.")

grid_b = sorted(mech_rows.keys())
kstar_idx_b = grid_b.index(KSTAR) if KSTAR in grid_b else None


def scan_diagnostic(label, field, kappas_sorted):
    vals = [mech_rows[k][field] for k in kappas_sorted]
    if any(v is None for v in vals):
        return None
    diffs = np.diff(vals)
    local_ext = []
    for i in range(1, len(vals) - 1):
        if (vals[i] - vals[i - 1]) * (vals[i + 1] - vals[i]) < 0:
            local_ext.append(kappas_sorted[i])
    d2 = np.diff(diffs)                      # d2[j] is centered at kappas_sorted[j+1]
    d2_signs = np.sign(d2)
    d2_floor = float(np.median(np.abs(d2)))  # sealed significance floor (see header)
    inflect_raw, inflect_sig = [], []
    for i in range(1, len(d2)):
        if d2_signs[i] != 0 and d2_signs[i - 1] != 0 and d2_signs[i] != d2_signs[i - 1]:
            loc = kappas_sorted[i + 1]
            inflect_raw.append(loc)
            if abs(d2[i]) >= d2_floor and abs(d2[i - 1]) >= d2_floor:
                inflect_sig.append(loc)
    monotonic = len(local_ext) == 0
    aligned = False
    aligned_how = []
    if kstar_idx_b is not None:
        for feat_list, tag in [(local_ext, "extremum"), (inflect_sig, "significant-inflection")]:
            for f in feat_list:
                fi = kappas_sorted.index(f)
                if abs(fi - kstar_idx_b) <= 1:
                    aligned = True
                    aligned_how.append(f"{tag}@{f}")
    print(f"  [{label}] values={[round(v, 5) for v in vals]}")
    print(f"    d2(x1e5)={[round(v * 1e5, 2) for v in d2]}  median|d2|floor(x1e5)={d2_floor*1e5:.2f}")
    print(f"    monotonic={monotonic}  local_extrema={local_ext}  "
          f"inflections_significant={inflect_sig}  inflections_raw_unfiltered={inflect_raw}")
    print(f"    kappa*={KSTAR} aligned(within 1 grid step, extrema+significant inflections only)="
          f"{aligned} {aligned_how if aligned_how else ''}")
    return {"field": field, "values": vals, "monotonic": monotonic, "local_extrema": local_ext,
            "d2": [float(v) for v in d2], "d2_median_floor": d2_floor,
            "inflections_significant": inflect_sig, "inflections_raw": inflect_raw,
            "aligned_with_kstar": aligned, "aligned_how": aligned_how}


print("\nMechanism-comparison scans (kappa* =", KSTAR, "):")
scan_gamma = scan_diagnostic("gamma (banked escape_rate, density-converged window)",
                              "gamma_banked_window", grid_b)
scan_mst = scan_diagnostic("MST-gap/diam @ F=1597", "mst_gap_over_diam_F1597", grid_b)
scan_lift = scan_diagnostic("liftoff ratio (max|Im eig|/mu)", "liftoff_ratio_vs_mu", grid_b)

any_aligned = any(s is not None and s["aligned_with_kstar"] for s in (scan_gamma, scan_mst, scan_lift))
aligned_names = [n for n, s in [("gamma", scan_gamma), ("MST-gap/diam@F1597", scan_mst),
                                 ("liftoff", scan_lift)] if s is not None and s["aligned_with_kstar"]]
print(f"\n(b) VERDICT: any sealed diagnostic aligned with kappa*={KSTAR}? {any_aligned}  "
      f"({aligned_names if aligned_names else 'none'})")

# ====================================================================================================
# (c) DEPTH-15 spot-check
# ====================================================================================================
print("\n" + "-" * 100)
print("(c) DEPTH-15 spot-check")
print("-" * 100)

if KSTAR == 1.0:
    partner = 1.5
elif KSTAR == 1.5:
    partner = 1.0
else:
    partner = None

if partner is not None:
    spot_kappas = sorted(set([KSTAR, partner, 0.0, 1.9]))
    dev_note = None
else:
    spot_kappas = sorted(set([KSTAR, 1.0, 1.5, 0.0, 1.9]))
    dev_note = (f"kappa*={KSTAR} is NOT one of the banked V11b pair {{1.0,1.5}} -- preregistration "
                f"anticipated kappa* in that pair. Deviation handled by keeping BOTH 1.0 and 1.5 "
                f"(the original pair) in addition to kappa*, giving {len(spot_kappas)} spot-check "
                f"points instead of 4. Stated plainly per the honesty rules; not a post-hoc "
                f"correlation, just an adapted point list since kappa* was unknown until part (a) ran.")

GOLDEN15 = L.metallic_word(15, 1)
print(f"word15 (golden m=1, depth15) length = {len(GOLDEN15)}")
print(f"spot-check kappas: {spot_kappas}")
if dev_note:
    print(f"NOTE: {dev_note}")

spot_rows = {}
for kappa in spot_kappas:
    mu, lam = lam_of(kappa)
    d13 = L.box_dim(L.spectrum(GOLDEN13, lam, periodic=True))

    if kappa in fine_rows:
        d14 = fine_rows[kappa]["box_dim_depth14"]
        d14_src = "fine-grid (this run, part a)"
    else:
        d14 = L.box_dim(L.spectrum(GOLDEN14, lam, periodic=True))
        d14_src = "fresh (not in fine grid)"

    t0 = time.time()
    d15 = L.box_dim(L.spectrum(GOLDEN15, lam, periodic=True))
    t15 = time.time() - t0

    spot_rows[kappa] = {"kappa": kappa, "box_dim_depth13": d13, "box_dim_depth14": d14,
                         "depth14_source": d14_src, "box_dim_depth15": d15, "t15_s": round(t15, 3)}

    banked_note = ""
    if kappa in BANKED_DEPTH14:
        bd14 = BANKED_DEPTH14[kappa]["box_dim_depth14"]
        bmatch = abs(d14 - bd14) < 1e-9
        banked_note = f"  banked_d14={bd14:.6f} match={bmatch}"

    print(f"  kappa={kappa:+.2f}  d13={d13:.6f}  d14={d14:.6f}({d14_src}){banked_note}  "
          f"d15={d15:.6f}  [{t15:.1f}s]  (elapsed={elapsed():.0f}s)", flush=True)

# --- V11b-style persistence criterion, adapted to this restricted spot-check point set ---
peak_pair = [k for k in [KSTAR, partner] if k is not None]
baseline_pair = [0.0, 1.9]

# noise scale: part (a)'s OWN fine-grid baseline (the 8 non-top-2 fine-grid points), analogous
# to V11b's baseline_std but computed fresh on THIS cell's fine grid rather than reused from V11b.
non_top2_vals = [vals_a[i] for i in range(len(vals_a)) if i not in order_desc[:2]]
NOISE_A = float(np.std(non_top2_vals))
print(f"\npart-(a) fine-grid baseline (non-top-2, n={len(non_top2_vals)}): "
      f"mean={np.mean(non_top2_vals):.5f}  std={NOISE_A:.5f}  (used as the noise scale below)")


def sep_at(depth_key):
    peak_vals = [spot_rows[k][depth_key] for k in peak_pair]
    base_vals = [spot_rows[k][depth_key] for k in baseline_pair]
    return min(peak_vals) - float(np.mean(base_vals)), peak_vals, base_vals


sep14, peakv14, basev14 = sep_at("box_dim_depth14")
sep15, peakv15, basev15 = sep_at("box_dim_depth15")

top2_stable = all(pv > bv for pv in peakv15 for bv in basev15) if len(peak_pair) == 2 else (peakv15[0] > max(basev15))
sep15_within_noise = abs(sep15) < 2 * NOISE_A
sep_shrunk_a_lot = sep15 < 0.3 * sep14 if sep14 != 0 else True
sep_grew_or_held = sep15 >= 0.7 * sep14 if sep14 != 0 else False

print(f"\npeak_pair={peak_pair}  baseline_pair={baseline_pair}")
print(f"depth14: peak_vals={[round(v,6) for v in peakv14]}  baseline_vals={[round(v,6) for v in basev14]}  "
      f"separation={sep14:+.6f}")
print(f"depth15: peak_vals={[round(v,6) for v in peakv15]}  baseline_vals={[round(v,6) for v in basev15]}  "
      f"separation={sep15:+.6f}")
print(f"top2_stable(peak_pair both > baseline_pair @depth15)={top2_stable}  "
      f"sep15_within_noise(<2*{NOISE_A:.5f})={sep15_within_noise}  "
      f"sep_shrunk_a_lot(<0.3*sep14)={sep_shrunk_a_lot}  sep_grew_or_held(>=0.7*sep14)={sep_grew_or_held}")

if top2_stable and sep_grew_or_held and not sep15_within_noise:
    depth15_verdict = "PEAK-ROBUST"
elif (not top2_stable) or sep15_within_noise or sep_shrunk_a_lot:
    depth15_verdict = "PEAK-ARTIFACT (finite-depth)"
else:
    depth15_verdict = "UNDECIDED"

print(f"\n(c) DEPTH-15 PERSISTENCE VERDICT: {depth15_verdict}")

# ====================================================================================================
# FINAL LOCKED VERDICT
# ====================================================================================================
print("\n" + "=" * 100)
print("FINAL LOCKED VERDICT")
print("=" * 100)

if depth15_verdict == "PEAK-ARTIFACT (finite-depth)":
    final_verdict = "ARTIFACT-AT-DEPTH"
    reason = "depth-15 spot-check kills the peak per the adapted V11b criterion."
elif depth15_verdict == "PEAK-ROBUST":
    if any_aligned:
        final_verdict = "MECHANISM-CANDIDATE"
        reason = f"peak survives depth-15 AND aligns with: {aligned_names}."
    else:
        final_verdict = "ISOLATED-FEATURE"
        reason = "peak survives depth-15 but none of the 3 sealed diagnostics align with kappa*."
else:
    final_verdict = "UNDECIDED-AT-DEPTH (closest locked bucket noted below)"
    reason = "depth-15 persistence itself was ambiguous by the adapted V11b criterion."

print(f"kappa* = {KSTAR}   peak shape = {shape}")
print(f"(b) mechanism alignment: {aligned_names if aligned_names else 'none'}")
print(f"(c) depth-15 persistence: {depth15_verdict}")
print(f"\n>>> VERDICT: {final_verdict}")
print(f">>> REASON: {reason}")

print(f"\ntotal wall-clock time: {elapsed():.1f}s ({elapsed()/60:.2f} min) of {BUDGET_S/60:.0f} min budget")

# ====================================================================================================
# write JSON
# ====================================================================================================
OUT = {
    "gate": {"kappa": GATE_KAPPA, "fresh": d13_fresh, "banked": d13_banked, "diff": gate_diff, "pass": gate_pass},
    "fine_grid_kappas": FINE_GRID,
    "fine_rows": fine_rows,
    "kstar": KSTAR,
    "second_highest_kappa": second_kappa,
    "gap_top2": gap_top2,
    "adjacent_top2": adjacent_top2,
    "local_maxima_kappas": [FINE_GRID[i] for i in local_max_idx],
    "peak_shape": shape,
    "mech_rows": mech_rows,
    "dropped_from_b": dropped_b,
    "scan_gamma": scan_gamma,
    "scan_mst_gap_F1597": scan_mst,
    "scan_liftoff": scan_lift,
    "any_mechanism_aligned": any_aligned,
    "aligned_names": aligned_names,
    "spot_kappas": spot_kappas,
    "spot_rows": spot_rows,
    "deviation_note_c": dev_note,
    "noise_scale_a_std": NOISE_A,
    "sep14": sep14, "sep15": sep15,
    "top2_stable": top2_stable, "sep15_within_noise": sep15_within_noise,
    "sep_shrunk_a_lot": sep_shrunk_a_lot, "sep_grew_or_held": sep_grew_or_held,
    "depth15_verdict": depth15_verdict,
    "final_verdict": final_verdict,
    "final_reason": reason,
    "total_compute_time_s": elapsed(),
}
with open(OUT_JSON, "w") as fh:
    json.dump(OUT, fh, indent=2, default=lambda o: o.item() if hasattr(o, "item") else str(o))
print(f"\nwrote {OUT_JSON}")
