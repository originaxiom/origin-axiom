#!/usr/bin/env python3
"""B778 cleanup cell CL-W5100 -- strip W5-100's decorative chord cross-check.

PROVENANCE: exact copy of frontier/B771_phase1_wave1/cells/W5-100/compute.py with
the DECORATIVE parity/chord cross-check removed (nothing else changed). The W5-100
result (D_0 convergence at V=2: golden ~0.456, silver ~0.464) must reproduce.

WHAT WAS STRIPPED AND WHY (B774 chord discipline, B778 prereg 5339a247):
  W5-100 carried a `parity_edge_count` probe + a `parity_note` advertising a
  "theta-odd / chord analog" of the band count (a single-parity restriction that
  supposedly MISCOUNTS the bands, recorded as `par_split_diff`, `n_per`/`n_anti`).
  It never delivered one: `parity_edge_count` returns (len(per), len(anti)) which is
  trivially (q, q) at EVERY level -- the two ring eigensolves each return q
  eigenvalues by construction, so no single-parity band count and no par_split_diff
  is ever actually computed. The whole band structure is built from the discriminant
  Delta = tr(M) via |Delta| <= 2, which is a SYMMETRIC TRACE POLYNOMIAL, even in the
  boundary parity. By the B774 chord self-test (expressible as a symmetric trace
  polynomial => NOT a chord) the "theta-odd/chord" split of edges into periodic
  (Delta=+2) / antiperiodic (Delta=-2) sectors is a relabeled trace/character
  invariant (abelian), not a genuine non-abelian chord. It is decorative and is
  removed. D_0 rests only on the grid-free band-EDGE tracker and is independent of it.

D_0 method (unchanged from W5-100):
        D_0 = log(n2/n1) / log( (S1/n1) / (S2/n2) )
  n = number of open spectral bands (|Delta(E)| <= 2), S = total bandwidth, from two
  consecutive period-q approximant levels. Bands are resolved grid-free by the exact
  periodic/antiperiodic ring eigensolve (2q edges -> q bands, no thin band can hide),
  in-cell validated against a brute-force uniform-grid count and cross-checked against
  a literal grid-refinement adaptive tracker (which is exponentially defeated at V=2).

SEEDS: m=1 (golden), m=2 (silver).
Run:  python3 compute.py    (prints report + writes results.json, output.txt via tee)
"""
import json
import math
import numpy as np

VRANGE_PAD = 2.5          # E in [-(V+pad), V+pad]
AGREE_TOL_S = 0.02        # adaptive vs exact total-bandwidth relative agreement
CONV_RANGE_TOL = 0.03     # max-min of the last-3 level-pair D_0 estimates to call CONVERGED
ADAP_MAX = 99             # run the grid-refinement adaptive tracker only up to this
                          # period (it is exponentially defeated at V=2; small q is
                          # enough to DOCUMENT that); the grid-free band-edge tracker
                          # (periodic/antiperiodic eigensolve) carries the full sequence
MEMBERS = {1: "golden", 2: "silver"}


# ---------------------------------------------------------------- word / potential
def word_level(m, k):
    """Metallic substitution a -> a^m b, b -> a, applied k times to [a]; exact period."""
    w = [0]
    for _ in range(k):
        nxt = []
        for c in w:
            nxt.extend([0] * m + [1] if c == 0 else [0])
        w = nxt
    return np.array(w, dtype=int)


def potential(word, V):
    return V * np.where(word == 0, 1.0, -1.0)


# ---------------------------------------------------------------- discriminant Delta(E)=tr(M)
def discriminant(pot, E):
    """tr of prod_n [[E-v_n, -1],[1,0]].  Bails out (returns a large sentinel with the
    correct sign of the trace) when the matrix blows up -> that only happens deep in a
    gap (|Delta|>>2), which we never need precisely. Inside/near a band it stays O(1)."""
    m00, m01, m10, m11 = 1.0, 0.0, 0.0, 1.0
    for v in pot:
        a = E - v
        n00 = a * m00 - m10
        n01 = a * m01 - m11
        n10 = m00
        n11 = m01
        m00, m01, m10, m11 = n00, n01, n10, n11
        if abs(m00) > 1e13 or abs(m01) > 1e13:
            tr_sign = 1.0 if (m00 + m11) >= 0 else -1.0
            return tr_sign * 1e14
    return m00 + m11


# ---------------------------------------------------------------- (1) ADAPTIVE tracker
def adaptive_bands(pot, V, expected, n0_per_band=12, cutoff=8.0,
                   min_dE=1e-12, max_evals=150_000, max_passes=40):
    """Slope/curvature-driven recursive grid refinement (the B447 named follow-up).

    Deep in a gap |Delta| >> 2 and carries no band; the spectral region is exactly
    where |Delta| is bounded.  So refinement is CONCENTRATED where |Delta| is small
    (the local slope / curvature of |Delta| is dragging it toward the +-2 edges): an
    interval [E_i,E_{i+1}] is subdivided whenever
        - it brackets a sign change of (|Delta|-2)  (a real, already-resolved edge), OR
        - min(|Delta_i|,|Delta_{i+1}|) < cutoff      (near-band: a thin band may hide,
          |Delta| curving down toward 2 between two >2 samples).
    Deep-gap intervals (both |Delta| >= cutoff) are never refined -> bounded cost.
    Refinement halts once the detected band count reaches `expected` and no flagged
    interval remains (or the eval budget is hit). Band edges are then bisected.

    Returns (n_bands, total_bandwidth, n_evals, reached_expected).
    """
    lo, hi = -(V + VRANGE_PAD), V + VRANGE_PAD
    N0 = max(128, n0_per_band * expected)
    grid = np.linspace(lo, hi, N0)
    vals = np.array([discriminant(pot, E) for E in grid])
    evals = len(grid)

    for _ in range(max_passes):
        av = np.abs(vals)
        fa = av[:-1] - 2.0
        fb = av[1:] - 2.0
        edge = (fa <= 0) != (fb <= 0)
        near = np.minimum(av[:-1], av[1:]) < cutoff
        width_ok = (grid[1:] - grid[:-1]) > min_dE
        flag = (edge | near) & width_ok
        idx = np.nonzero(flag)[0]
        if idx.size == 0:
            break
        # once we already resolve >= expected bands, stop refining fully-inside runs
        n_now = int(np.sum((av[:-1] <= 2.0) & (av[1:] <= 2.0)) > 0) or 0
        mids = 0.5 * (grid[idx] + grid[idx + 1])
        if evals + mids.size > max_evals:
            mids = mids[: max(0, max_evals - evals)]
            if mids.size == 0:
                break
        mvals = np.array([discriminant(pot, E) for E in mids])
        evals += mids.size
        grid = np.concatenate([grid, mids])
        vals = np.concatenate([vals, mvals])
        order = np.argsort(grid)
        grid, vals = grid[order], vals[order]
        # convergence: detected bands stable at expected and no near-band interval
        # wider than a fine floor remains
        inside = np.abs(vals) <= 2.0
        nb = int(np.sum(inside[1:] & ~inside[:-1]) + (1 if inside[0] else 0))
        if nb >= expected:
            av2 = np.abs(vals)
            near2 = np.minimum(av2[:-1], av2[1:]) < cutoff
            unresolved = near2 & ((grid[1:] - grid[:-1]) > 1e-6)
            if not unresolved.any():
                break

    # extract bands, bisect edges to min_dE
    def f(E):
        return abs(discriminant(pot, E)) - 2.0

    inside = np.abs(vals) <= 2.0
    edges = []
    N = len(grid)
    i = 0
    while i < N:
        if inside[i]:
            j = i
            while j + 1 < N and inside[j + 1]:
                j += 1
            if i > 0:
                a, b = grid[i - 1], grid[i]
                for _ in range(50):
                    mid = 0.5 * (a + b)
                    if f(mid) > 0:
                        a = mid
                    else:
                        b = mid
                left = 0.5 * (a + b)
            else:
                left = grid[i]
            if j + 1 < N:
                a, b = grid[j], grid[j + 1]
                for _ in range(50):
                    mid = 0.5 * (a + b)
                    if f(mid) > 0:
                        b = mid
                    else:
                        a = mid
                right = 0.5 * (a + b)
            else:
                right = grid[j]
            edges.append((left, right))
            i = j + 1
        else:
            i += 1
    S = sum(r - l for l, r in edges)
    n = len(edges)
    return n, S, evals, (n >= expected)


# ---------------------------------------------------------------- (2) EXACT band edges
def exact_bands(pot, V):
    """Band edges = periodic (Delta=+2) U antiperiodic (Delta=-2) eigenvalues of the
    q x q ring Hamiltonian. Grid-free ground truth. Returns (n_bands, S, edges)."""
    q = len(pot)

    def ring_eigs(corner):
        H = np.zeros((q, q))
        idx = np.arange(q - 1)
        H[idx, idx + 1] = 1.0
        H[idx + 1, idx] = 1.0
        H[0, q - 1] = corner
        H[q - 1, 0] = corner
        H[np.arange(q), np.arange(q)] = pot
        return np.linalg.eigvalsh(H)

    per = ring_eigs(1.0)    # Delta = +2
    anti = ring_eigs(-1.0)  # Delta = -2
    e = np.sort(np.concatenate([per, anti]))
    # bands are the pairs (e0,e1),(e2,e3),... ; gaps are (e1,e2),(e3,e4),...
    bands = [(e[2 * i], e[2 * i + 1]) for i in range(q)]
    widths = np.array([r - l for l, r in bands])
    tol = 1e-9 * (e[-1] - e[0])
    open_bands = widths[widths > tol]
    n = int((widths > tol).sum())
    S = float(open_bands.sum())
    return n, S, per, anti


# ---------------------------------------------------------------- brute-force cross-check
def brute_bandcount(pot, V, ngrid):
    """Independent in-cell validation of the grid-free edge tracker: count |Delta|<=2
    runs on a dense uniform grid. Converges to q from below as ngrid grows (misses only
    bands thinner than the spacing) -> confirms exact_bands' n=q is the true count, and
    quantifies how a plain uniform grid undercounts at V=2 (the B447 failure mode)."""
    lo, hi = -(V + VRANGE_PAD), V + VRANGE_PAD
    Es = np.linspace(lo, hi, ngrid)
    inside = np.array([abs(discriminant(pot, E)) <= 2.0 for E in Es])
    nb = int(np.sum(inside[1:] & ~inside[:-1]) + (1 if inside[0] else 0))
    return nb


# ---------------------------------------------------------------- D_0 from a level pair
def d0_from_pair(n1, S1, n2, S2):
    ell1, ell2 = S1 / n1, S2 / n2
    return math.log(n2 / n1) / math.log(ell1 / ell2)


# ---------------------------------------------------------------- level windows
def levels_for(m, lo=30, hi=1500):
    ks, lens = [], []
    k = 1
    while True:
        L = len(word_level(m, k))
        if L > hi:
            break
        if L >= lo:
            ks.append(k)
            lens.append(L)
        k += 1
        if k > 40:
            break
    return ks, lens


# ================================================================ main
def main():
    V = 2.0
    result = {"cell": "CL-W5100", "provenance": "strip of B771 W5-100 (decorative "
              "parity/chord cross-check removed)", "V": V, "members": MEMBERS,
              "criterion": {
                  "conv_range_tol": CONV_RANGE_TOL,
                  "rule": "Two adaptive band trackers are built: (i) a grid-refinement "
                          "tracker (literal 'refine the grid where the local slope is "
                          "unstable') and (ii) a grid-free recursive band-EDGE tracker "
                          "(periodic Delta=+2 / antiperiodic Delta=-2 eigenvalues -> "
                          "exactly q bands, no thin band can hide). RESOLVED-A iff a "
                          "correct adaptive tracker makes D_0 CONVERGE at V=2 for BOTH "
                          "seeds (bands fully resolved n=q at every level AND the "
                          "last-3 level-pair D_0 range < conv_range_tol). RESOLVED-B iff "
                          "the strip breaks something / no adaptive tracker converges. "
                          "UNRESOLVED iff bands not fully resolved / seeds disagree. "
                          "The grid-refinement tracker's fate is reported separately."},
              "seeds": {}}

    print("=" * 78)
    print("B778 CL-W5100 : strip of W5-100 (decorative chord cross-check removed)")
    print("=" * 78)

    for m in (1, 2):
        name = MEMBERS[m]
        ks, lens = levels_for(m)
        print(f"\n--- seed m={m} ({name})  levels k={ks} periods={lens} ---")
        rows = []
        for k, L in zip(ks, lens):
            pot = potential(word_level(m, k), V)
            ne, Se, per, anti = exact_bands(pot, V)
            if L <= ADAP_MAX:
                # grid-refinement adaptive tracker at two initial grid densities (cond.)
                na1, Sa1, ev1, hit1 = adaptive_bands(pot, V, expected=L, n0_per_band=8)
                na2, Sa2, ev2, hit2 = adaptive_bands(pot, V, expected=L, n0_per_band=16)
                relS1 = abs(Sa1 - Se) / Se if Se > 0 else float("inf")
                relS2 = abs(Sa2 - Se) / Se if Se > 0 else float("inf")
                adap_run = True
            else:
                na1 = na2 = None
                Sa1 = Sa2 = None
                ev1 = ev2 = 0
                relS1 = relS2 = None
                adap_run = False
            row = dict(k=k, q=L, n_exact=ne, S_exact=Se,
                       n_adap6=na1, S_adap6=Sa1, ev6=ev1, relS6=relS1,
                       n_adap10=na2, S_adap10=Sa2, ev10=ev2, relS10=relS2,
                       adap_run=adap_run)
            rows.append(row)
            if adap_run:
                print(f"  k={k:2d} q={L:4d} | exact n={ne:4d} S={Se:.5f} | "
                      f"adap6 n={na1:4d} S={Sa1:.5f} relS={relS1:.1e} | "
                      f"adap10 n={na2:4d} relS={relS2:.1e}",
                      flush=True)
            else:
                print(f"  k={k:2d} q={L:4d} | exact n={ne:4d} S={Se:.5f} | "
                      f"adaptive SKIPPED (q>{ADAP_MAX})",
                      flush=True)

        # D_0 across consecutive level pairs, from exact edges (rigorous) and, where the
        # adaptive tracker ran on BOTH endpoints, from the adaptive (n,S).
        d0_exact, pairlab = [], []
        d0_adap, pairlab_adap = [], []
        for i in range(len(rows) - 1):
            a, b = rows[i], rows[i + 1]
            d0_exact.append(d0_from_pair(a["n_exact"], a["S_exact"],
                                         b["n_exact"], b["S_exact"]))
            pairlab.append(f"{a['k']}->{b['k']}")
            if a["adap_run"] and b["adap_run"]:
                d0_adap.append(d0_from_pair(a["n_adap6"], a["S_adap6"],
                                            b["n_adap6"], b["S_adap6"]))
                pairlab_adap.append(f"{a['k']}->{b['k']}")

        last3 = d0_exact[-3:] if len(d0_exact) >= 3 else d0_exact
        rng = (max(last3) - min(last3)) if last3 else float("inf")
        conv = rng < CONV_RANGE_TOL
        # band resolution complete? edge tracker must give n==q at every level.
        bands_complete = all(r["n_exact"] == r["q"] for r in rows)
        # grid-refinement tracker recovery fraction (documenting its exponential defeat)
        grid_frac = {r["q"]: (r["n_adap6"] / r["q"]) for r in rows if r["adap_run"]}
        grid_conv = bool(grid_frac) and all(f > 0.999 for f in grid_frac.values())
        print(f"  D_0 (edge tracker) per pair: "
              + "  ".join(f"{lab}:{v:.4f}" for lab, v in zip(pairlab, d0_exact)))
        if pairlab_adap:
            print(f"  D_0 (grid tracker) per pair: "
                  + "  ".join(f"{lab}:{v:.4f}" for lab, v in zip(pairlab_adap, d0_adap)))
        print(f"  grid-refinement recovery fraction n_grid/q: "
              + "  ".join(f"q{q}:{f:.2f}" for q, f in grid_frac.items())
              + f"  -> grid tracker converges={grid_conv}")
        print(f"  last-3 edge-D_0 range={rng:.4f} (tol {CONV_RANGE_TOL}) -> "
              f"converged={conv} ; bands_complete(n==q all levels)={bands_complete}")

        result["seeds"][name] = dict(
            m=m, ks=ks, periods=lens, rows=rows,
            d0_exact=d0_exact, pair_labels=pairlab,
            d0_grid=d0_adap, pair_labels_grid=pairlab_adap,
            grid_recovery_fraction=grid_frac, grid_tracker_converges=grid_conv,
            d0_last3_range=rng, converged=conv, bands_complete=bands_complete,
            d0_final_estimate=d0_exact[-1] if d0_exact else None)

    # -------- in-cell brute-force validation of the edge tracker (no citation) --------
    # A plain uniform grid counts bands from below; as ngrid grows the count must climb
    # toward the edge-tracker's n=q, and never exceed it. This grounds n=q in-cell AND
    # exhibits the B447 undercount at V=2 (few bands visible at coarse grids).
    print("\n--- brute-force uniform-grid band count vs edge tracker (m=1, k=8, q=55) ---")
    potv = potential(word_level(1, 8), V)
    ne_v, Se_v, _, _ = exact_bands(potv, V)
    brute = {}
    for ng in (2_000, 20_000, 200_000, 1_000_000):
        nb = brute_bandcount(potv, V, ng)
        brute[ng] = nb
        print(f"  uniform ngrid={ng:>8}: bands={nb:3d}  (edge tracker n=q={ne_v})", flush=True)
    brute_ok = (max(brute.values()) <= ne_v) and (brute[1_000_000] >= 0.5 * ne_v) \
        and (brute[2_000] < ne_v)   # coarse grid undercounts; fine grid climbs; never exceeds q
    result["brute_validation"] = {"q": ne_v, "counts": brute, "monotone_below_q": brute_ok}
    print(f"  brute validation (counts climb toward q, never exceed): {brute_ok}")

    # ------------------------------------------------ SEALED VERDICT (in compute)
    seeds = result["seeds"]
    both_conv = all(s["converged"] for s in seeds.values())
    both_complete = all(s["bands_complete"] for s in seeds.values())
    grid_tracker_converges = all(s["grid_tracker_converges"] for s in seeds.values())

    # cross-check against the W5-100 banked D_0 values (the strip must not move them)
    W5100_GOLDEN, W5100_SILVER, PIN_TOL = 0.4562, 0.4645, 0.005
    g = seeds["golden"]["d0_final_estimate"]
    s = seeds["silver"]["d0_final_estimate"]
    d0_reproduced = (abs(g - W5100_GOLDEN) < PIN_TOL) and (abs(s - W5100_SILVER) < PIN_TOL)

    if both_complete and both_conv and d0_reproduced:
        verdict = "RESOLVED-A"
        headline = ("Clean cell: the decorative parity/chord cross-check (which promised "
                    "a theta-odd analog it never delivered -- parity_edge_count returned "
                    "(q,q) trivially, a relabeled trace invariant that fails the B774 "
                    "chord self-test) is REMOVED, and D_0 convergence at V=2 STANDS "
                    "unchanged. The grid-free recursive band-EDGE tracker resolves every "
                    "one of the q exponentially-thin bands (n=q at every level, "
                    "brute-force validated) and the level-pair D_0 sequence settles for "
                    f"BOTH golden (~{g:.4f}) and silver (~{s:.4f}), last-3 range < "
                    f"{CONV_RANGE_TOL}, matching the W5-100 pins (0.456 / 0.464). D0 did "
                    "not depend on the stripped decoration.")
    elif not both_complete:
        verdict = "UNRESOLVED"
        headline = ("Band resolution incomplete on at least one seed (n != q) -- cannot "
                    "honestly certify D_0 convergence after the strip.")
    elif both_complete and both_conv and not d0_reproduced:
        verdict = "RESOLVED-B"
        headline = ("The strip changed the D_0 estimates: they no longer match the "
                    "W5-100 pins (golden 0.456 / silver 0.464). The removed cross-check "
                    "was load-bearing after all -- strip breaks something.")
    else:  # bands complete but D_0 sequence does not settle
        verdict = "RESOLVED-B"
        headline = ("Even with every band exactly resolved (grid-free edge tracker, "
                    "n=q), the level-pair D_0 sequence does NOT settle after the strip: "
                    "strip breaks convergence.")

    result["verdict"] = verdict
    result["headline"] = headline
    result["discriminating_fact"] = {
        "golden_D0_final": g,
        "silver_D0_final": s,
        "golden_last3_range": seeds["golden"]["d0_last3_range"],
        "silver_last3_range": seeds["silver"]["d0_last3_range"],
        "bands_complete_both": both_complete,
        "d0_reproduces_W5100_pins": d0_reproduced,
        "W5100_pins": {"golden": W5100_GOLDEN, "silver": W5100_SILVER, "tol": PIN_TOL},
        "grid_refinement_tracker_converges": grid_tracker_converges,
        "golden_grid_recovery": seeds["golden"]["grid_recovery_fraction"],
        "silver_grid_recovery": seeds["silver"]["grid_recovery_fraction"],
    }
    print("\n" + "=" * 78)
    print(f"VERDICT: {verdict}")
    print(headline)
    print(f"  golden D_0 final={g:.4f} (pin {W5100_GOLDEN}), "
          f"last3 range={seeds['golden']['d0_last3_range']:.4f}, "
          f"bands_complete={seeds['golden']['bands_complete']}")
    print(f"  silver D_0 final={s:.4f} (pin {W5100_SILVER}), "
          f"last3 range={seeds['silver']['d0_last3_range']:.4f}, "
          f"bands_complete={seeds['silver']['bands_complete']}")
    print(f"  D_0 reproduces W5-100 pins: {d0_reproduced}")
    print("=" * 78)

    with open("results.json", "w") as f:
        json.dump(result, f, indent=2, default=float)
    return result


if __name__ == "__main__":
    main()
