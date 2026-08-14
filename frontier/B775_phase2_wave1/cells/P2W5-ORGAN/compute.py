"""P2W5-ORGAN (OI-123 / L98) -- one-organ-or-two: a NEW discriminating statistic.

THE PROBLEM (banked).  N3 (B646, prereg 09246f08) left one-organ-or-two
UNRESOLVED: box_dim(kappa) on the plateau kappa in [0.80,1.55] showed candidate
peaks at 1.10 / 1.45 with margins ~1.27 sigma against a placement-jitter floor
sigma_pool = 0.014337 (2 sigma bar preregistered; depth-15 gaps SHRANK).  N3's
own banked recommendation: DESIGN a structurally different statistic; do not
push depth.  OI-123 repeats that recommendation.

WHAT THIS CELL DOES.

 (S1) Executes -- byte-verified against its sealed sha-256 -- the L98 falsifier
      sealed in B666 cell W3-4 (SEALS.txt, 2026-07-17), whose --unblind pass was
      explicitly reserved for "the next data pass".  This is that pass.  The
      statistic is g_d(kappa) = mst_max_edge/diam: an EXACT deterministic
      functional of the spectrum -- no box grid, no placement, no RNG -- so N3's
      failure channel (placement jitter comparable to the candidate gaps) is
      structurally absent.  Its decision function (peak_regions /
      consistent_organs / verdict) is IMPORTED VERBATIM from the sealed file and
      neither re-implemented nor re-tuned here.

 (S1x) The same sealed decision function on an EXTENDED window.  Declared rule
      (D3 lesson, applied symmetrically to positives and negatives): a peak
      region whose representative index sits at a scan bound is BOUND-HUGGING
      and therefore non-identifiable; the remedy is to widen the window until
      the peaks are interior, then re-apply the unchanged criterion.  The v1
      run of this cell showed g turning UP at the sealed window's right bound
      (kappa=1.55) -- the signature that the window, not the object, sets the
      peak count.  EXT_GRID = 0.55..1.90 step 0.05 (28 points) strictly contains
      the sealed 16-point window.

 (S2) The exact dominant-gap LABEL statistic l1 = n_small/L (cut the largest MST
      edge).  Discrete: phi-hierarchy labels are spaced >= 0.09, measured
      depth-scatter 1.7e-6.  Tests the STRONG (two-gap-regime) form.

 (S3) NEW THIS CELL -- the gap-HIERARCHY CO-LOCATION statistic.  Structurally
      different from every previous test including S1: instead of asking how
      many peaks ONE curve has (the jitter-bound question), it asks whether the
      WHOLE gap hierarchy G_k(kappa) = e_k/diam, k = 1..5 (e_k = k-th largest
      MST edge), peaks at ONE kappa or at SEVERAL.  One organ = one
      fragmentation structure => all five gap ranks co-vary and their
      depth-consistent peak regions co-locate.  Two organs = two independent
      fragmentation structures => the hierarchy splits, ranks peaking at
      kappa's separated by index-gap >= 2 (N3's own separation rule).  The
      read-out is an integer CLUSTER COUNT of depth-consistent peak regions,
      not a sub-sigma height comparison.

POWER is MEASURED in-cell, never asserted: the perturbation floor of every
functional (eigenvalues + N(0,1e-10), 5 seeds, 2 kappas, depths 14 and 15 =
>=2 sizes and >=2 seeds) divides every decision margin.  The decision-critical
margin is dm(v) = min_i |v_i - max(neighbours of i)| -- exactly the quantity the
peak rule compares, so margin/floor is the true equivalent-sigma of the
flag pattern.  The remaining systematic channel (finite-size / depth flapping)
is handled by an EXACT three-depth consistency requirement and its flap rate is
reported.

Gate 5/5-Q: structural only; no SM values; nothing to CLAIMS; one-number pin
untouched.  Env: pyenv python3 (NOT sage).  Re-runnable: `python3 compute.py`
(a grid cache speeds re-runs; delete grid_cache.json to recompute from scratch).
"""
import hashlib
import json
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
W34 = os.path.abspath(os.path.join(HERE, "..", "..", "..",
                                   "B666_leads_campaign", "cellW34"))
CACHE = os.path.join(HERE, "grid_cache.json")

# ---------------------------------------------------------------- sealed inputs
SEALED = {
    "L98_FALSIFIER_PREREG.md":
        "112345cb3bccccda6682864ac3b518cd4f24a1ef59c60770400455f61078df53",
    "l98_falsifier.py":
        "36d0157f265665df2acbb0865857076df0040aecd66ccae88200b8428f956b00",
    "l98_lib.py":
        "0904fb4a35cfc5551323ec0bbd3e961d5aca6e281d1fea579483b6f83c5586ca",
}


def seal_gate():
    out = {}
    for fn, want in SEALED.items():
        h = hashlib.sha256(open(os.path.join(W34, fn), "rb").read()).hexdigest()
        out[fn] = (h == want, h)
        assert h == want, f"SEAL BROKEN for {fn}: {h} != {want}"
    return out


SEAL_STATUS = seal_gate()
sys.path.insert(0, W34)
from l98_lib import provenance_gate, metallic_word, spectrum, mst_edges, cut_partition  # noqa: E402
from l98_falsifier import (verdict as sealed_verdict, peak_regions,  # noqa: E402
                           consistent_organs, GRID, DEPTHS)

provenance_gate()   # metallic_word/spectrum verbatim vs the banked packet lib

TOPK = 5
NOISE_SEEDS = 5
NOISE_SIGMA = 1e-10
NOISE_KAPPAS = [1.00, 1.30]
NOISE_DEPTHS = [14, 15]
EXT_GRID = [round(0.55 + 0.05 * i, 2) for i in range(28)]      # 0.55 .. 1.90
assert set(GRID) <= set(EXT_GRID)
SEALED_IDX = [EXT_GRID.index(k) for k in GRID]
POWER_BAR = 2.0     # N3's 2-sigma bar transposed: margin >= 2 x measured floor


# ---------------------------------------------------------------- functionals
def diam_bbox(ev):
    P = np.c_[ev.real, ev.imag]
    return float(np.hypot(P[:, 0].max() - P[:, 0].min(),
                          P[:, 1].max() - P[:, 1].min()))


def hierarchy(ev, top=TOPK):
    """Exact gap hierarchy: (G[1..top], labels[1..top], e2/e1) with
    G_k = e_k/diam (e_k = k-th LARGEST Euclidean-MST edge) and
    label_k = n_small/L from cutting that edge.  Deterministic: no grid, no RNG."""
    n = len(ev)
    edges = mst_edges(ev)
    order = sorted(range(len(edges)), key=lambda i: -edges[i][0])
    dm = diam_bbox(ev)
    G, labs, lens = [], [], []
    for i in order[:top]:
        ns, _ = cut_partition(edges, n, i)
        G.append(edges[i][0] / dm)
        labs.append(ns / n)
        lens.append(edges[i][0])
    return G, labs, (lens[1] / lens[0] if len(lens) > 1 else 0.0)


# ---------------------------------------------------------------- decision aux
def dec_margin(v):
    """Decision-critical margin of the peak rule: min_i |v_i - max(neighbours)|.
    This is exactly the comparison peak_regions() makes, so margin/floor is the
    equivalent-sigma of the whole flag pattern."""
    n, out = len(v), []
    for i in range(n):
        nb = [v[j] for j in (i - 1, i + 1) if 0 <= j < n]
        out.append(abs(v[i] - max(nb)))
    return min(out)


def bound_hugging(organ, n):
    """Declared D3 rule: an organ any of whose depth representatives sits at a
    scan bound is non-identifiable (the window, not the object, may set it)."""
    return any(i in (0, n - 1) for i in organ)


def organ_verdict(g_by_depth, n):
    """The SEALED criterion (imported peak_regions/consistent_organs), plus the
    declared identifiability filter.  Returns
    (raw_verdict, organs, verdict_identifiable, organs_identifiable, organs_bh)."""
    raw_v, organs, _ = sealed_verdict(g_by_depth)
    keep = [o for o in organs if not bound_hugging(o, n)]
    bh = [o for o in organs if bound_hugging(o, n)]
    if len(keep) == 0:
        v = "UNRESOLVED"
    elif len(keep) == 1:
        v = "ONE-ORGAN"
    else:
        reps = sorted(o[1] for o in keep)
        v = ("TWO-ORGANS" if any(b - a >= 2 for a, b in zip(reps, reps[1:]))
             else "UNRESOLVED")
    return raw_v, organs, v, keep, bh


def cell_decision(p_x, p3, v_x, s3, n_keep, ranks_with_organ):
    """The cell's sealed verdict logic, isolated so --selftest can prove every
    branch can FIRE and can FAIL (MB12; the B414 lesson).

    RESOLVED-A  : a structurally discriminating statistic was found AND run AND
                  met its stated power (both margins >= POWER_BAR x the MEASURED
                  floor), with no verdict-bearing organ at a scan bound, and the
                  two independent statistics concordant.
    RESOLVED-B  : the question is bound at achievable depth (EXTERNAL) -- either
                  the margins sit under the measured floor (N3's failure mode) or
                  the depth channel destroys every candidate organ everywhere.
    UNRESOLVED  : powered but discordant / partially identifiable.
    """
    powered = (p_x >= POWER_BAR) and (p3 >= POWER_BAR)
    ident = (n_keep > 0) and (ranks_with_organ >= TOPK - 1)
    resolved = v_x in ("ONE-ORGAN", "TWO-ORGANS") and s3 in ("ONE-ORGAN", "TWO-ORGANS")
    concordant = resolved and (v_x == s3)
    depth_defeated = (n_keep == 0) and (ranks_with_organ == 0)
    jitter_bound = (not powered) or depth_defeated
    if powered and ident and concordant:
        return "RESOLVED-A", v_x, powered, ident, concordant, depth_defeated, jitter_bound
    if jitter_bound:
        return ("RESOLVED-B", "BOUND AT ACHIEVABLE DEPTH (EXTERNAL)", powered,
                ident, concordant, depth_defeated, jitter_bound)
    return ("UNRESOLVED", f"S1x={v_x} / S3={s3} (discordant or unidentifiable)",
            powered, ident, concordant, depth_defeated, jitter_bound)


def selftest():
    """MB12: every branch of cell_decision FIRES, and every branch FAILS."""
    cases = [
        # (args, expected)
        ((1e8, 1e8, "ONE-ORGAN", "ONE-ORGAN", 1, 5), "RESOLVED-A"),
        ((1e8, 1e8, "TWO-ORGANS", "TWO-ORGANS", 2, 5), "RESOLVED-A"),
        ((0.5, 1e8, "ONE-ORGAN", "ONE-ORGAN", 1, 5), "RESOLVED-B"),   # under floor
        ((1e8, 0.9, "ONE-ORGAN", "ONE-ORGAN", 1, 5), "RESOLVED-B"),   # under floor
        ((1e8, 1e8, "UNRESOLVED", "UNRESOLVED", 0, 0), "RESOLVED-B"),  # depth-defeated
        ((1e8, 1e8, "ONE-ORGAN", "TWO-ORGANS", 1, 5), "UNRESOLVED"),  # discordant
        ((1e8, 1e8, "ONE-ORGAN", "UNRESOLVED", 1, 5), "UNRESOLVED"),  # partial
        ((1e8, 1e8, "TWO-ORGANS", "TWO-ORGANS", 2, 1), "UNRESOLVED"),  # unidentifiable
    ]
    print("== cell_decision selftest (MB12: each branch can FIRE and can FAIL) ==")
    ok = True
    for args, want in cases:
        got = cell_decision(*args)[0]
        flag = "OK" if got == want else "MISMATCH"
        ok &= got == want
        print(f"  {args} -> {got:11s} (expected {want:11s}) {flag}")
    fired = {cell_decision(*a)[0] for a, _ in cases}
    print(f"  branches fired: {sorted(fired)}  (all three reachable: "
          f"{fired == {'RESOLVED-A', 'RESOLVED-B', 'UNRESOLVED'}})")
    assert ok and fired == {"RESOLVED-A", "RESOLVED-B", "UNRESOLVED"}
    print("  selftest PASS")
    return True


def clusters_at_gap1(idxs):
    """Single-linkage clustering of integer indices at gap <= 1; two clusters
    are therefore always separated by index-gap >= 2 (N3's separation rule)."""
    s = sorted(set(idxs))
    if not s:
        return []
    out, cur = [], [s[0]]
    for a in s[1:]:
        if a - cur[-1] <= 1:
            cur.append(a)
        else:
            out.append(cur)
            cur = [a]
    out.append(cur)
    return out


# ---------------------------------------------------------------- the grid run
def load_cache():
    if os.path.exists(CACHE):
        try:
            return json.load(open(CACHE))
        except Exception:
            return {}
    return {}


def run_grid(grid, cache):
    """hierarchy at every (depth, kappa); cached across re-runs."""
    G_by_depth, lab_by_depth, rat_by_depth, rows = {}, {}, {}, []
    for d in DEPTHS:
        w = metallic_word(d, 1)
        Gs, labs, rats = [], [], []
        for kap in grid:
            key = f"{d}|{kap:.2f}"
            if key in cache:
                G, lb, rt = cache[key]["G"], cache[key]["labels"], cache[key]["ratio"]
                tag = "cache"
                t = 0.0
            else:
                t0 = time.time()
                mu = np.sqrt(2.0 - kap)
                ev = spectrum(w, 1j * mu, periodic=True)
                G, lb, rt = hierarchy(ev)
                cache[key] = dict(G=G, labels=lb, ratio=rt)
                tag, t = "computed", time.time() - t0
            Gs.append(G)
            labs.append(lb)
            rats.append(rt)
            rows.append(dict(kappa=kap, depth=d, g=round(G[0], 10),
                             G=[round(x, 10) for x in G],
                             labels=[round(x, 8) for x in lb],
                             e2_over_e1=round(rt, 6)))
            print(f"  d={d} L={len(w)} kappa={kap:.2f}: g={G[0]:.6f} "
                  f"l1={lb[0]:.5f} e2/e1={rt:.4f}  ({tag} {t:.1f}s)", flush=True)
        G_by_depth[d], lab_by_depth[d], rat_by_depth[d] = Gs, labs, rats
    json.dump(cache, open(CACHE, "w"), separators=(",", ":"))
    return rows, G_by_depth, lab_by_depth, rat_by_depth


def noise_floor():
    """Measured perturbation floor of g and of every G_k."""
    dg, dG, lab_ok = [], [], True
    for d in NOISE_DEPTHS:
        w = metallic_word(d, 1)
        for kap in NOISE_KAPPAS:
            ev = spectrum(w, 1j * np.sqrt(2.0 - kap), periodic=True)
            G0, lb0, _ = hierarchy(ev)
            for s in range(NOISE_SEEDS):
                rng = np.random.default_rng(7000 + 100 * d + int(100 * kap) + s)
                pert = ev + NOISE_SIGMA * (rng.normal(size=len(ev))
                                           + 1j * rng.normal(size=len(ev)))
                G1, lb1, _ = hierarchy(pert)
                dg.append(abs(G1[0] - G0[0]))
                dG.append(max(abs(a - b) for a, b in zip(G1, G0)))
                if lb1[0] != lb0[0]:
                    lab_ok = False
            print(f"  floor d={d} kappa={kap:.2f}: max|dg|={max(dg):.3e} "
                  f"max|dG|={max(dG):.3e} label-invariant={lab_ok}", flush=True)
    return max(dg), max(dG), lab_ok


# ================================================================ MAIN
def main():
    print("=" * 70)
    print("P2W5-ORGAN (OI-123 / L98) -- one-organ-or-two: a new statistic")
    print("=" * 70)
    print("\n-- seal gate on the B666 cellW34 sealed L98 falsifier --")
    for fn, (ok, h) in SEAL_STATUS.items():
        print(f"  {fn}: sha256 {h[:16]}...  MATCHES SEAL: {ok}")
    print("  provenance gate (metallic_word/spectrum vs banked packet lib): PASS")

    print()
    selftest()

    print("\n-- measured perturbation floor (5 seeds x 2 kappas x depths 14,15) --")
    floor_g, floor_G, lab_inv = noise_floor()
    floor = max(floor_g, floor_G, 1e-16)
    print(f"  floor used = {floor:.3e}   (N3's box_dim jitter floor was 1.4337e-2, "
          f"{0.014337/floor:.2e} times larger)")

    print(f"\n-- exact gap hierarchy on the EXTENDED grid "
          f"(kappa {EXT_GRID[0]}..{EXT_GRID[-1]} step 0.05, {len(EXT_GRID)} pts, "
          f"depths {DEPTHS}) --")
    rows, G_ext, lab_ext, rat_ext = run_grid(EXT_GRID, load_cache())
    N = len(EXT_GRID)
    g_ext = {d: [G_ext[d][i][0] for i in range(N)] for d in DEPTHS}
    g_seal = {d: [g_ext[d][i] for i in SEALED_IDX] for d in DEPTHS}

    # ---------------- S1: the sealed criterion on the sealed window (verbatim)
    raw_s, org_s, v_s, keep_s, bh_s = organ_verdict(g_seal, len(GRID))
    reps_s = {d: peak_regions(g_seal[d]) for d in DEPTHS}
    m_s = min(dec_margin(g_seal[d]) for d in DEPTHS)
    print("\n-- S1 (SEALED L98 falsifier, sealed 16-point window, verbatim) --")
    for d in DEPTHS:
        print(f"  depth {d}: peak regions at kappa {[GRID[i] for i in reps_s[d]]}")
    print(f"  sealed criterion, RAW verdict: {raw_s}   organs={org_s}   "
          f"N2={len(org_s)-1}")
    print(f"  bound-hugging organs (D3, non-identifiable): {bh_s}")
    print(f"  identifiable-filtered verdict on the sealed window: {v_s}")
    print(f"  decision margin {m_s:.3e} / floor {floor:.3e} = {m_s/floor:.2e} x floor")

    # ---------------- S1x: same criterion, extended (identifiable) window
    raw_x, org_x, v_x, keep_x, bh_x = organ_verdict(g_ext, N)
    reps_x = {d: peak_regions(g_ext[d]) for d in DEPTHS}
    m_x = min(dec_margin(g_ext[d]) for d in DEPTHS)
    p_x = m_x / floor
    flaps = sum(1 for i in range(N - 1)
                if len({int(np.sign(g_ext[d][i + 1] - g_ext[d][i])) for d in DEPTHS}) > 1)
    print("\n-- S1x (same sealed criterion, EXTENDED identifiable window) --")
    for d in DEPTHS:
        print(f"  depth {d}: peak regions at kappa {[EXT_GRID[i] for i in reps_x[d]]}"
              f"   argmax kappa={EXT_GRID[int(np.argmax(g_ext[d]))]}")
    print(f"  RAW verdict: {raw_x}   organs (kappa) = "
          f"{[[EXT_GRID[i] for i in o] for o in org_x]}")
    print(f"  bound-hugging (excluded): {[[EXT_GRID[i] for i in o] for o in bh_x]}")
    print(f"  IDENTIFIABLE organs: {[[EXT_GRID[i] for i in o] for o in keep_x]}")
    print(f"  S1x verdict = {v_x}")
    print(f"  decision margin {m_x:.3e} / floor {floor:.3e} = {p_x:.2e} x floor")
    print(f"  depth-flapping pairs (sign(dg) not depth-constant): {flaps}/{N-1}")

    # ---------------- S2: exact gap-label regime
    lab_sets = {d: sorted({round(lab_ext[d][i][0], 4) for i in range(N)}) for d in DEPTHS}
    spread = {d: max(lab_sets[d]) - min(lab_sets[d]) for d in DEPTHS}
    s2 = ("TWO GAP REGIMES" if all(spread[d] > 0.01 for d in DEPTHS)
          else "ONE GAP REGIME" if all(spread[d] <= 0.01 for d in DEPTHS)
          else "MIXED")
    print("\n-- S2 (exact dominant-gap label l1 = n_small/L) --")
    for d in DEPTHS:
        print(f"  depth {d}: distinct l1 = {lab_sets[d]}   spread = {spread[d]:.6f}")
    print(f"  S2 = {s2}   (label perturbation-invariant = {lab_inv}; "
          f"phi-hierarchy label spacing >= 0.09)")

    # ---------------- S3: NEW -- gap-hierarchy co-location
    print("\n-- S3 (NEW: gap-hierarchy co-location, ranks k=1..5, extended window) --")
    rank_organs, rank_bh, margins, detail = {}, {}, [], {}
    for k in range(TOPK):
        curves = {d: [G_ext[d][i][k] for i in range(N)] for d in DEPTHS}
        reps = {d: peak_regions(curves[d]) for d in DEPTHS}
        organs = consistent_organs(reps)
        keep = [o for o in organs if not bound_hugging(o, N)]
        rank_organs[k] = keep
        rank_bh[k] = [o for o in organs if bound_hugging(o, N)]
        margins.append(min(dec_margin(curves[d]) for d in DEPTHS))
        detail[k] = dict(
            peak_regions={str(d): [EXT_GRID[i] for i in reps[d]] for d in DEPTHS},
            identifiable_organs=[[EXT_GRID[i] for i in o] for o in keep],
            bound_hugging=[[EXT_GRID[i] for i in o] for o in organs
                           if bound_hugging(o, N)],
            dec_margin=margins[-1])
        print(f"  rank k={k+1}: identifiable depth-consistent organs at kappa "
              f"{[[EXT_GRID[i] for i in o] for o in keep]}"
              f"   (bound-hugging dropped: {len(rank_bh[k])})")
    all_reps = [o[1] for k in range(TOPK) for o in rank_organs[k]]   # depth-14 reps
    cl = clusters_at_gap1(all_reps)
    m3 = min(margins)
    p3 = m3 / floor
    ranks_with_organ = sum(1 for k in range(TOPK) if rank_organs[k])
    s3 = ("UNRESOLVED" if (not cl or ranks_with_organ < TOPK - 1)
          else "ONE-ORGAN" if len(cl) == 1
          else "TWO-ORGANS")
    print(f"  pooled depth-14 organ locations across ranks: "
          f"{sorted(EXT_GRID[i] for i in set(all_reps))}")
    print(f"  co-location clusters (single-linkage gap<=1, i.e. separation >=2): "
          f"{[[EXT_GRID[i] for i in g] for g in cl]}  -> {len(cl)} cluster(s)")
    print(f"  ranks contributing an identifiable organ: {ranks_with_organ}/{TOPK}")
    print(f"  worst decision margin over ranks {m3:.3e} / floor = {p3:.2e} x floor")
    print(f"  S3 = {s3}")

    # ---------------- the plateau sub-question (N3's actual window)
    plateau = [i for i in range(N) if 0.80 - 1e-9 <= EXT_GRID[i] <= 1.55 + 1e-9]
    org_plateau = [o for o in keep_x if o[1] in plateau]
    print("\n-- the N3 sub-question: identifiable organs INSIDE the plateau "
          "[0.80,1.55] --")
    print(f"  {[[EXT_GRID[i] for i in o] for o in org_plateau]}  -> "
          f"{len(org_plateau)} organ(s)")

    # ================================================================ VERDICT
    (cell, call, powered, ident, concordant, depth_defeated,
     jitter_bound) = cell_decision(p_x, p3, v_x, s3, len(keep_x), ranks_with_organ)

    print("\n" + "=" * 70)
    print("CELL VERDICT")
    print("=" * 70)
    print(f"  powered (both margins >= {POWER_BAR} x measured floor): {powered}"
          f"   [S1x {p_x:.2e}x, S3 {p3:.2e}x]")
    print(f"  identifiable (no verdict-bearing organ at a scan bound): {ident}")
    print(f"  concordant: {concordant}   [S1x={v_x}, S3={s3}, S2={s2}]")
    print(f"  CELL = {cell}    organ call = {call}")
    print("  SCOPE (verbatim from the sealed prereg): a ONE-ORGAN verdict falsifies")
    print("  the two-organ hypothesis in its GAP-MECHANISTIC form; a two-organ")
    print("  structure invisible to the gap functional and to the gap labels is NOT")
    print("  excluded by this test (box_dim cannot see it either -- N3's floor).")
    print("  Gate 5/5-Q: structural only; no SM values; nothing to CLAIMS.")

    res = dict(
        cell="P2W5-ORGAN", OI="OI-123", lead="L98",
        question="one organ or two on the kappa-plateau [0.80,1.55]",
        seal_gate={k: v[0] for k, v in SEAL_STATUS.items()},
        sealed_grid=GRID, ext_grid=EXT_GRID, depths=list(DEPTHS),
        floor=dict(g=floor_g, G=floor_G, used=floor, seeds=NOISE_SEEDS,
                   sigma=NOISE_SIGMA, kappas=NOISE_KAPPAS, depths=NOISE_DEPTHS,
                   label_invariant=lab_inv, n3_box_dim_jitter=0.014337,
                   n3_over_this=0.014337 / floor),
        S1_sealed_window=dict(
            statistic="sealed L98 falsifier g=mst_max_edge/diam, N3 peak rule, "
                      "3-depth consistency (imported verbatim)",
            raw_verdict=raw_s, organs_kappa=[[GRID[i] for i in o] for o in org_s],
            bound_hugging=[[GRID[i] for i in o] for o in bh_s],
            filtered_verdict=v_s, dec_margin=m_s, power_x_floor=m_s / floor,
            peak_regions={str(d): [GRID[i] for i in reps_s[d]] for d in DEPTHS}),
        S1x_extended=dict(
            raw_verdict=raw_x,
            organs_kappa=[[EXT_GRID[i] for i in o] for o in org_x],
            bound_hugging=[[EXT_GRID[i] for i in o] for o in bh_x],
            identifiable_organs=[[EXT_GRID[i] for i in o] for o in keep_x],
            verdict=v_x, dec_margin=m_x, power_x_floor=p_x,
            depth_flap_pairs=flaps, n_pairs=N - 1,
            peak_regions={str(d): [EXT_GRID[i] for i in reps_x[d]] for d in DEPTHS},
            argmax_kappa={str(d): EXT_GRID[int(np.argmax(g_ext[d]))] for d in DEPTHS}),
        S2=dict(statistic="exact dominant-gap label l1=n_small/L", verdict=s2,
                label_sets={str(d): lab_sets[d] for d in DEPTHS},
                spread={str(d): spread[d] for d in DEPTHS}),
        S3=dict(statistic="NEW: gap-hierarchy co-location -- cluster count of the "
                          "depth-consistent peak regions of G_k=e_k/diam, k=1..5",
                verdict=s3, clusters=[[EXT_GRID[i] for i in g] for g in cl],
                n_clusters=len(cl), ranks_with_organ=ranks_with_organ,
                per_rank={str(k + 1): detail[k] for k in range(TOPK)},
                dec_margin=m3, power_x_floor=p3),
        plateau_organs=[[EXT_GRID[i] for i in o] for o in org_plateau],
        verdict=cell, organ_call=call, powered=powered, identifiable=ident,
        concordant=concordant, power_bar_x_floor=POWER_BAR,
        depth_defeated=depth_defeated, jitter_bound=jitter_bound,
        scope="ONE-ORGAN falsifies the two-organ hypothesis in its gap-mechanistic "
              "form only; a same-gap higher-order two-organ structure is excluded by "
              "nothing banked (declared at seal).",
        rows=rows)
    json.dump(res, open(os.path.join(HERE, "results.json"), "w"),
              separators=(",", ":"))
    print("\nwritten: results.json")
    return cell


if __name__ == "__main__":
    main()
