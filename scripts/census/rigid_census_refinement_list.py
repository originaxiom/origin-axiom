#!/usr/bin/env python3
"""The rigid census's refinement list and its curvature along Re τ (THE FINAL ATTACK, Step B's revision, P-521; aggregates
and cell indices only; data-free).  The companion of rigid_census_smoothness_map.py (B1819), whose manifest check it reuses:
it refuses a census that is not the one on record (P-495).  It writes no value of any row:
  - the curvature along Re τ on B1726's uneven grid (0.05, 0.2, 0.35, 0.55, 0.7, 0.85), as the second divided difference
    scaled to the mean step, in log10, as quantiles;
  - for every line, the grid intervals where any output needs refinement before an interpolant can be certified: a
    second difference above 0.08 decades (along Im τ or Re τ), or a change between degenerate (≤ 1e-9) and not;
  - the totals, so the refinement's cost is known before it is run.
Nothing is compared with a measured value.
    python3 -I scripts/census/rigid_census_refinement_list.py <census dir> <out.json>"""
import gzip, json, math, pathlib, sys
from collections import defaultdict
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from rigid_census_smoothness_map import manifest_ok, q

RE = (0.05, 0.2, 0.35, 0.55, 0.7, 0.85)
IM = tuple(round(2.05 + 0.1 * k, 2) for k in range(15))
THRESH = 0.08


def main():
    d = pathlib.Path(sys.argv[1]); out = pathlib.Path(sys.argv[2])
    ok, why = manifest_ok(d)
    if not ok:
        print("REFUSED:", why); return 2
    d2_re = []; flagged = {}; totals = defaultdict(int)
    for f in sorted((d / "full_menu").glob("*.jsonl.gz")):
        grid = {}
        for line in gzip.open(f, "rt", encoding="utf-8"):
            rec = json.loads(line)
            for r in rec.get("rows", []):
                grid[(r[0], r[1], r[2], tuple(rec["tau"]))] = list(r[3]) + list(r[4]) + list(r[5]) + list(r[6])
        cells = set()                                  # ("im", ire, iim) is the interval IM[iim]..IM[iim+1] at RE[ire]; ("re", ire, iim) likewise
        for k in {g[:3] for g in grid}:
            for j in range(9):
                def lv(re, im):
                    v = grid.get(k + ((re, im),))
                    if v is None or not isinstance(v[j], (int, float)) or not math.isfinite(v[j]) or v[j] <= 1e-9: return None
                    return math.log10(v[j])
                L = {(a, b): lv(a, b) for a in RE for b in IM}
                for ia, a in enumerate(RE):
                    for ib in range(len(IM) - 1):
                        x, y = L[(a, IM[ib])], L[(a, IM[ib + 1])]
                        if (x is None) != (y is None): cells.add(("im", ia, ib))
                    for ib in range(1, len(IM) - 1):
                        x, y, z = L[(a, IM[ib - 1])], L[(a, IM[ib])], L[(a, IM[ib + 1])]
                        if None not in (x, y, z) and abs(z - 2 * y + x) > THRESH:
                            cells.add(("im", ia, ib - 1)); cells.add(("im", ia, ib))
                for ib, b in enumerate(IM):
                    for ia in range(len(RE) - 1):
                        x, y = L[(RE[ia], b)], L[(RE[ia + 1], b)]
                        if (x is None) != (y is None): cells.add(("re", ia, ib))
                    for ia in range(1, len(RE) - 1):
                        x, y, z = L[(RE[ia - 1], b)], L[(RE[ia], b)], L[(RE[ia + 1], b)]
                        if None in (x, y, z): continue
                        h1, h2 = RE[ia] - RE[ia - 1], RE[ia + 1] - RE[ia]; hm = (h1 + h2) / 2
                        c = 2 * ((z - y) / h2 - (y - x) / h1) / (h1 + h2) * hm * hm     # curvature per mean step, comparable to Im's second difference
                        d2_re.append(abs(c))
                        if abs(c) > THRESH: cells.add(("re", ia - 1, ib)); cells.add(("re", ia, ib))
        flagged[f.name.split(".")[0]] = sorted(cells)
        totals["im_intervals"] += sum(1 for c in cells if c[0] == "im"); totals["re_intervals"] += sum(1 for c in cells if c[0] == "re")
    n_int_im = len(RE) * (len(IM) - 1); n_int_re = (len(RE) - 1) * len(IM)
    res = {"input": why, "aggregates_and_indices_only": True, "threshold_log10": THRESH,
           "second_difference_log10_along_re_per_mean_step": q(d2_re), "fraction_re_above_threshold": round(sum(1 for v in d2_re if v > THRESH) / max(1, len(d2_re)), 5),
           "totals": dict(totals), "per_line_interval_counts": {k: len(v) for k, v in flagged.items()},
           "fraction_of_intervals_flagged": {"im": round(totals["im_intervals"] / (n_int_im * len(flagged)), 5), "re": round(totals["re_intervals"] / (n_int_re * len(flagged)), 5)},
           "refinement_list": flagged}
    out.write_text(json.dumps(res, indent=1), encoding="utf-8")
    print("refinement list written:", why, "| flagged intervals", dict(totals), "| fractions", res["fraction_of_intervals_flagged"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
