#!/usr/bin/env python3
"""The rigid-direction census's smoothness in τ, as aggregates only (THE FINAL ATTACK, Step B's revision, P-521; data-free).

The census (B1810's thirteen directions on the 266-line menu over B1726's τ grid, 6 Re τ × 15 Im τ, both radii, the eight
readings) is unread before the seal: the pre-seal review allows it to be read only through a committed script that outputs
aggregates (STEP_B's review, fix 15). This is that script. It checks the census against the manifest whose hash is on
record (P-495, S266) before it reads a row, and it writes no value of any row, only distributions of differences:
  - for each output (the six ratios and the three CKM moduli, in log10), its first differences between neighbouring grid
    points along Im τ (step 0.1) and along Re τ, and its second differences along Im τ;
  - their quantiles, overall and by the line's order N;
  - the count of non-finite and of degenerate entries (a ratio below 1e-9, a massless state) and of degeneracy changes
    between neighbours (where no interpolant is smooth).
Nothing is compared with a measured value.
    python3 -I scripts/census/rigid_census_smoothness_map.py <census dir> <out.json>
<census dir> holds full_menu/ and full_menu_MANIFEST.json (the audit room's rigid_census folder)."""
import gzip, hashlib, json, math, pathlib, sys
from collections import defaultdict

RECORDED_MANIFEST_SHA256 = "4683a000bd09dda1cbf22dae68117530fb6c3f09691528347f55177b4a9804d1"     # on record: P-495, S266


def manifest_ok(d):
    man = json.loads((d / "full_menu_MANIFEST.json").read_text(encoding="utf-8"))
    per = man["per_file"]
    h = hashlib.sha256("".join("%s  %s\n" % (v, n) for n, v in sorted(per.items())).encode()).hexdigest()
    if h != man["sha256_of_the_manifest"]:
        return False, "the manifest does not hash to its own stated value"
    if h != RECORDED_MANIFEST_SHA256:
        return False, "the manifest is not the one on record (P-495)"
    for n, v in per.items():
        if hashlib.sha256((d / "full_menu" / n).read_bytes()).hexdigest() != v:
            return False, "%s does not match the manifest" % n
    return True, "%d files match the recorded manifest" % len(per)


def q(xs, ps=(0.5, 0.9, 0.99, 0.999, 1.0)):
    if not xs:
        return {}
    s = sorted(xs); n = len(s)
    return {("max" if p == 1.0 else "q%g" % (100 * p)): round(s[min(n - 1, int(p * (n - 1) + 0.5))], 4) for p in ps}


def main():
    d = pathlib.Path(sys.argv[1]); out = pathlib.Path(sys.argv[2])
    ok, why = manifest_ok(d)
    if not ok:
        print("REFUSED:", why); return 2
    RE = (0.05, 0.2, 0.35, 0.55, 0.7, 0.85); IM = tuple(round(2.05 + 0.1 * k, 2) for k in range(15))
    d1_im, d1_re, d2_im = defaultdict(list), defaultdict(list), defaultdict(list)
    counts = defaultdict(int)
    for f in sorted((d / "full_menu").glob("*.jsonl.gz")):
        grid = {}
        order = None
        for line in gzip.open(f, "rt", encoding="utf-8"):
            rec = json.loads(line); order = rec["order"]
            if "rows" not in rec:
                counts["error_configurations"] += 1; continue
            for r in rec["rows"]:
                vals = list(r[3]) + list(r[4]) + list(r[5]) + list(r[6])
                grid[(r[0], r[1], r[2], tuple(rec["tau"]))] = vals
        keys = {k[:3] for k in grid}
        for k in keys:
            for j in range(9):
                def lv(re, im):
                    v = grid.get(k + ((re, im),))
                    if v is None: return None
                    x = v[j]
                    if not isinstance(x, (int, float)) or not math.isfinite(x): counts["non_finite"] += 1; return None
                    if x <= 1e-9: counts["degenerate"] += 1; return None
                    return math.log10(x)
                L = {(re, im): lv(re, im) for re in RE for im in IM}
                for re in RE:
                    for a, b in zip(IM, IM[1:]):
                        x, y = L[(re, a)], L[(re, b)]
                        if (x is None) != (y is None): counts["degeneracy_changes_along_im"] += 1
                        elif x is not None: d1_im[order].append(abs(y - x))
                    for a, b, c in zip(IM, IM[1:], IM[2:]):
                        x, y, z = L[(re, a)], L[(re, b)], L[(re, c)]
                        if None not in (x, y, z): d2_im[order].append(abs(z - 2 * y + x))
                for im in IM:
                    for a, b in zip(RE, RE[1:]):
                        x, y = L[(a, im)], L[(b, im)]
                        if (x is None) != (y is None): counts["degeneracy_changes_along_re"] += 1
                        elif x is not None: d1_re[order].append(abs(y - x))
    allv = lambda D: [v for vs in D.values() for v in vs]
    res = {"input": why, "aggregates_only": True,
           "first_difference_log10_along_im_step_0.1": {"all": q(allv(d1_im)), "by_order": {N: q(v) for N, v in sorted(d1_im.items())}},
           "first_difference_log10_along_re": {"all": q(allv(d1_re))},
           "second_difference_log10_along_im": {"all": q(allv(d2_im)), "by_order": {N: q(v) for N, v in sorted(d2_im.items())},
                                                "fraction_above_0.08": round(sum(1 for v in allv(d2_im) if v > 0.08) / max(1, len(allv(d2_im))), 5)},
           "counts": dict(counts),
           "n_differences": {"im": len(allv(d1_im)), "re": len(allv(d1_re)), "second_im": len(allv(d2_im))}}
    out.write_text(json.dumps(res, indent=1), encoding="utf-8")
    print("smoothness map written:", res["input"], "| second differences along Im above 0.08:", res["second_difference_log10_along_im"]["fraction_above_0.08"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
