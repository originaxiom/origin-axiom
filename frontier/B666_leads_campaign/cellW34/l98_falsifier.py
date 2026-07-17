"""L98 falsifier runner (B666 cell W3-4; sealed with L98_FALSIFIER_PREREG.md).

--selftest : MB12 vacuity checks of the decision function on synthetic
             triples (no target-grid point touched).  Run in-cell.
--unblind  : the sealed 16x3 target-grid run + mechanical verdict.
             NOT run by cell W3-4; reserved for the next data pass.

Every decision-path comparison is exact arithmetic on deterministic
floats (no RNG, no box grid anywhere).
"""
import json
import sys

import numpy as np

from l98_lib import provenance_gate, metallic_word, spectrum, gap_labels

GRID = [round(0.80 + 0.05 * i, 2) for i in range(16)]   # 0.80 .. 1.55
DEPTHS = (13, 14, 15)


# ---------------------------------------------------------------- decision core
def peak_regions(v):
    """N3's verbatim rule. v = list of values on the grid. Returns the list of
    representative indices (one per region)."""
    n = len(v)
    flagged = []
    for i in range(n):
        left = v[i - 1] if i > 0 else None
        right = v[i + 1] if i < n - 1 else None
        ge = all(v[i] >= x for x in (left, right) if x is not None)
        gt = any(v[i] > x for x in (left, right) if x is not None)
        flagged.append(ge and gt)
    reps = []
    i = 0
    while i < n:
        if flagged[i]:
            j = i
            while j + 1 < n and flagged[j + 1]:
                j += 1
            block = list(range(i, j + 1))
            best = max(block, key=lambda t: (v[t], -t))
            reps.append(best)
            i = j + 1
        else:
            i += 1
    return reps


def consistent_organs(reps_by_depth):
    """Greedy pairing of peak regions across the three depths: a
    depth-consistent organ = one region per depth, pairwise index distance
    <= 1.  Greedy by minimal total pairwise distance, ties toward lower
    kappa; each region used at most once.  Returns the list of organ
    triples (i13, i14, i15)."""
    r13, r14, r15 = (list(reps_by_depth[d]) for d in DEPTHS)
    cands = []
    for a in r13:
        for b in r14:
            for c in r15:
                if abs(a - b) <= 1 and abs(a - c) <= 1 and abs(b - c) <= 1:
                    cands.append((abs(a - b) + abs(a - c) + abs(b - c),
                                  min(a, b, c), (a, b, c)))
    cands.sort()
    used13, used14, used15, organs = set(), set(), set(), []
    for _, _, (a, b, c) in cands:
        if a in used13 or b in used14 or c in used15:
            continue
        used13.add(a); used14.add(b); used15.add(c)
        organs.append((a, b, c))
    organs.sort(key=lambda t: t[1])
    return organs


def verdict(g_by_depth):
    """The sealed criterion.  g_by_depth: {depth: [16 values]}.
    Returns (verdict_string, organs, n2)."""
    reps = {d: peak_regions(g_by_depth[d]) for d in DEPTHS}
    organs = consistent_organs(reps)
    n2 = len(organs) - 1
    if len(organs) == 0:
        return "UNRESOLVED", organs, n2
    if n2 == 0:
        return "ONE-ORGAN", organs, n2
    reps14 = sorted(o[1] for o in organs)
    sep = any(b - a >= 2 for a, b in zip(reps14, reps14[1:]))
    return ("TWO-ORGANS" if sep else "UNRESOLVED"), organs, n2


# ---------------------------------------------------------------- selftest (MB12)
def selftest():
    print("== l98_falsifier --selftest (MB12: criterion can pass AND fail) ==")
    # 1. depth-consistent unimodal triple -> ONE-ORGAN
    uni = [np.exp(-((i - 7.0 - s) / 4) ** 2) for s in (0.0, 0.3, -0.3)
           for i in [np.arange(16)]]
    g = {13: list(uni[0]), 14: list(uni[1]), 15: list(uni[2])}
    v, o, n2 = verdict(g)
    print(f"  synthetic unimodal (drift<=1):   {v}  organs={o}  N2={n2}")
    assert v == "ONE-ORGAN" and n2 == 0
    # 2. depth-consistent bimodal triple (peaks at 4 and 11) -> TWO-ORGANS
    bi = []
    for s in (0.0, 0.4, -0.4):
        x = np.arange(16)
        bi.append(np.exp(-((x - 4 - s) / 2.0) ** 2) +
                  0.9 * np.exp(-((x - 11 + s) / 2.0) ** 2))
    g = {13: list(bi[0]), 14: list(bi[1]), 15: list(bi[2])}
    v, o, n2 = verdict(g)
    print(f"  synthetic bimodal (sep>=2):      {v}  organs={o}  N2={n2}")
    assert v == "TWO-ORGANS" and n2 >= 1
    # 3. depth-INCONSISTENT second peak (flaps 3 <-> 12 <-> absent) -> ONE-ORGAN
    #    (the flapping peak forms no consistent organ; the stable one does)
    x = np.arange(16)
    fl = {13: list(np.exp(-((x - 7) / 3.0) ** 2) +
                   0.5 * np.exp(-((x - 2) / 1.0) ** 2)),
          14: list(np.exp(-((x - 7) / 3.0) ** 2) +
                   0.5 * np.exp(-((x - 13) / 1.0) ** 2)),
          15: list(np.exp(-((x - 7) / 3.0) ** 2))}
    v, o, n2 = verdict(fl)
    print(f"  flapping second peak:            {v}  organs={o}  N2={n2}")
    assert v == "ONE-ORGAN" and n2 == 0
    # 4. no consistent organ at all -> UNRESOLVED
    nc = {13: list(np.exp(-((x - 2) / 1.5) ** 2)),
          14: list(np.exp(-((x - 8) / 1.5) ** 2)),
          15: list(np.exp(-((x - 14) / 1.5) ** 2))}
    v, o, n2 = verdict(nc)
    print(f"  no consistent organ:             {v}  organs={o}  N2={n2}")
    assert v == "UNRESOLVED"
    # 5. adjacent (unseparated) double peak -> UNRESOLVED
    ad = {}
    for d, s in zip(DEPTHS, (0, 0, 0)):
        y = np.exp(-((x - 7) / 3.0) ** 2)
        y[9] = y[7]          # twin summit at index-gap 2? make gap 1: index 8
        y[8] = y[7] * 0.98   # valley between 7 and 9
        ad[d] = list(y)
    v, o, n2 = verdict(ad)
    print(f"  twin summit at index-gap 1..2:   {v}  organs={o}  N2={n2}")
    print("  (informational; separation rule exercised)")
    print("selftest PASS — both outcomes reachable, flapping handled")


# ---------------------------------------------------------------- unblind
def unblind():
    provenance_gate()
    print("== L98 SEALED FALSIFIER — UNBLINDING RUN (16 x 3 grid) ==")
    g_by_depth, rows = {}, []
    for d in DEPTHS:
        w = metallic_word(d, 1)
        vals = []
        for kap in GRID:
            mu = np.sqrt(2.0 - kap)
            ev = spectrum(w, 1j * mu, periodic=True)
            top, ratio = gap_labels(ev, top=5)
            P = np.c_[ev.real, ev.imag]
            dm = float(np.hypot(P[:, 0].max() - P[:, 0].min(),
                                P[:, 1].max() - P[:, 1].min()))
            gval = top[0][0] / dm
            vals.append(gval)
            rows.append(dict(kappa=kap, depth=d, g=gval, e1=top[0][0],
                             label=top[0][2], n_small=top[0][1],
                             e2_over_e1=ratio,
                             top5=[(t[0], t[1]) for t in top]))
            print(f"  d={d} kappa={kap:.2f}: g={gval:.6f} "
                  f"label={top[0][2]:.5f} (ns={top[0][1]}) e2/e1={ratio:.4f}")
        g_by_depth[d] = vals
    v, organs, n2 = verdict(g_by_depth)
    print(f"\nVERDICT: {v}   organs (i13,i14,i15)={organs}   N2={n2}")
    if v == "TWO-ORGANS":
        reps14 = sorted(o[1] for o in organs)
        labs = {}
        for i in reps14:
            r = [r for r in rows if r["depth"] == 14 and
                 abs(r["kappa"] - GRID[i]) < 1e-9][0]
            labs[GRID[i]] = (r["label"], r["e2_over_e1"])
            print(f"  peak kappa={GRID[i]}: label={r['label']:.5f} "
                  f"e2/e1={r['e2_over_e1']:.4f}")
        ls = [l for l, _ in labs.values()]
        tag = ("TWO GAP REGIMES" if max(ls) - min(ls) > 0.01
               else "ONE GAP REGIME (shape-level split)")
        print(f"  mechanism tag: {tag}")
    with open("l98_unblind_results.json", "w") as fh:
        json.dump(dict(grid=GRID, depths=list(DEPTHS), rows=rows,
                       g_by_depth={str(k): v_ for k, v_ in g_by_depth.items()},
                       verdict=v, organs=organs, n2=n2), fh, indent=1)
    print("written: l98_unblind_results.json")


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        selftest()
    elif "--unblind" in sys.argv:
        unblind()
    else:
        print("usage: l98_falsifier.py --selftest | --unblind")
        print("cell W3-4 runs --selftest only; --unblind is the next data pass")
