#!/usr/bin/env python3
"""Where the refined census's a0 and F_-2 rows disagree (THE FINAL ATTACK, Step B; data-free; aggregate-only; refused
unless the census manifest is committed and pushed).  B1824 proved a0 = eta^4 F_-2 / 6 identically, so the two directions
are proportional and every output (ratios of singular values, the CKM's moduli and J) must agree to roundoff.  The loader
found a largest |log10 difference| of 18.4.  This counts the disagreements (|log10 difference| above 1e-6) by class:
  - both values above the roundoff floor 1e-12 (a genuine disagreement);
  - one above and one below the floor;
  - both below (two roundoff values: structural zeros cannot agree in log);
and, for each class, by output, by Im tau band, by line order, and (the CKM's four) whether both rows define the mixing;
and the floor-side values' log10 bins.  Prints and writes counts and bin edges only, never a row's value.
    python3 -I scripts/census/a0_fm2_duplicate_diagnostic.py <refined dir> <manifest.json> <manifest sha256> <out.json>"""
import gzip, json, math, pathlib, sys
from collections import Counter

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts" / "stepb"))
from guard import require_pushed_manifest

A0, FM2 = 1, 6
FLOOR = 1e-12
NAMES = ["up m1/m3", "up m2/m3", "down m1/m3", "down m2/m3", "lepton m1/m3", "lepton m2/m3", "|V_us|", "|V_cb|", "|V_ub|", "|J|"]
BINS = [-math.inf, -30, -20, -16, -14, -12, -10, -6, -3, 0.5]


def outs(x):
    return list(x[3]) + list(x[4]) + list(x[5]) + list(x[6]) + [abs(x[7])]


def band(im):
    return "Im %.1f-%.1f" % (math.floor(im * 2) / 2, math.floor(im * 2) / 2 + 0.5)


def binof(v):
    lv = math.log10(v)
    for lo, hi in zip(BINS[:-1], BINS[1:]):
        if lo <= lv < hi:
            return "[%s, %s)" % (lo, hi)
    return "out"


def main(d, man, expected, out):
    g = require_pushed_manifest(man, expected)
    d = pathlib.Path(d)
    pairs = 0; cls = Counter(); by_out = {c: Counter() for c in ("both_above", "one_below", "both_below")}
    by_band = {c: Counter() for c in by_out}; by_order = {c: Counter() for c in by_out}; vdef = {c: Counter() for c in by_out}
    floor_bins = Counter(); worst = {c: 0.0 for c in by_out}; zero_pairs = 0
    for name in sorted(g["per_file"]):
        with gzip.open(d / name, "rt", encoding="utf-8") as fh:
            for line in fh:
                rec = json.loads(line)
                if "error" in rec: continue
                by = {(x[0], x[1], x[2]): x for x in rec["rows"]}
                for (dd, rr, lab), x in by.items():
                    if dd != FM2: continue
                    y = by[(A0, rr, lab)]
                    both_v = bool(x[8]) and bool(y[8])
                    for k, (p, q) in enumerate(zip(outs(x), outs(y))):
                        if k >= 6 and not both_v: continue
                        if not (p > 0 and q > 0):
                            zero_pairs += (p > 0) != (q > 0); continue
                        pairs += 1
                        dl = abs(math.log10(p) - math.log10(q))
                        if dl <= 1e-6: continue
                        c = "both_above" if (p >= FLOOR and q >= FLOOR) else ("both_below" if (p < FLOOR and q < FLOOR) else "one_below")
                        cls[c] += 1; worst[c] = max(worst[c], dl); by_out[c][NAMES[k]] += 1
                        by_band[c][band(rec["tau"][1])] += 1; by_order[c]["N%02d" % rec["order"]] += 1
                        if k >= 6: vdef[c]["both_define"] += 1
                        for v in (p, q):
                            if v < FLOOR: floor_bins[binof(v)] += 1
    rep = {"pairs_compared": pairs, "pairs_one_exact_zero": zero_pairs, "disagreements_above_1e-6": dict(cls),
           "largest_log10_difference_by_class": worst, "by_output": {c: dict(v) for c, v in by_out.items()},
           "by_Im_band": {c: dict(v) for c, v in by_band.items()}, "by_order": {c: dict(v) for c, v in by_order.items()},
           "ckm_both_define": {c: dict(v) for c, v in vdef.items()}, "floor_side_log10_bins": dict(floor_bins), "floor": FLOOR}
    pathlib.Path(out).write_text(json.dumps(rep, indent=1) + "\n", encoding="utf-8")
    print(json.dumps(rep, indent=1))


if __name__ == "__main__":
    if len(sys.argv) != 5: sys.exit(__doc__)
    main(*sys.argv[1:])
