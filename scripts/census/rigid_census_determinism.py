#!/usr/bin/env python3
"""The refined census's determinism check, alone (THE FINAL ATTACK, Step B; data-free; aggregate-only; refused unless the
manifest is pushed).  The same nodes as the certification (per file, the first hash-chosen cell's node, re-evaluated at its
stored tau by B1821's evaluator); the census must equal the fresh values at its own precision (census_io.dup_disagreement:
within 1e-9 absolutely, both below the roundoff floor, or within 1e-6 in log10 -- the census stores 8 significant digits).
The certification's first run (S283) applied a 1e-9 log10 tolerance, which the 8-digit storage cannot meet: '%.8g' rounds
with a relative error of at most 5e-8 (a mantissa of 1.0000000), 2.171e-8 in log10, and the first run's largest difference
was 2.16e-8.  This recomputes the check under the census's precision, and counts the pairs (both values positive) whose
|log10 difference| exceeds that storage bound (none if the evaluator is deterministic).  Prints and writes counts and
maxima only.
    python3 -I scripts/census/rigid_census_determinism.py <refined dir> <manifest.json> <manifest sha256> <out.json> [workers]"""
import gzip, json, math, pathlib, sys
from fractions import Fraction as F
from multiprocessing import Pool

ROOT = pathlib.Path(__file__).resolve().parents[2]
GEN = ROOT / "scripts" / "stepb"
EVAL = ROOT / "frontier" / "B1821_the_frames_mirror_symmetry_in_re_tau" / "verification"
FM2 = 6
STORE = math.log10(1 + 5e-8)                      # '%.8g''s largest relative rounding error, in log10


def task(args):
    fname, d = args
    sys.path.insert(0, str(EVAL)); sys.path.insert(0, str(GEN)); sys.path.insert(0, str(ROOT / "scripts" / "census"))
    import cm_zero_line as Z
    from census_io import dup_disagreement
    from exact_tau import GridStencils
    import rigid_census_certification as CERT
    recs = []
    with gzip.open(pathlib.Path(d) / fname, "rt", encoding="utf-8") as fh:
        for line in fh:
            r = json.loads(line)
            if "error" not in r: recs.append(r)
    pts = [(round(r["tau"][0], 4), round(r["tau"][1], 4)) for r in recs]
    gs = GridStencils(pts)
    for node in gs.pts:                                    # the certification's selection: the first chosen cell's node
        if CERT.chosen("%s|%s|%s|%s" % (fname, node[0], node[1], "cell")):
            break
    else:
        return fname, 0.0, 0.0, 0, 0
    rec = recs[pts.index(node)]; a, b = F(rec["line"][0]), F(rec["line"][1])
    fr = {(Z.DIRS.index(r["direction"]), ("L_max", "L_2").index(r["radius"]), r["reading"]): r for r in Z.rows_at(complex(*rec["tau"]), (a, b))}
    det = raw = 0.0; n = over = 0
    for x in rec["rows"]:
        if x[0] == FM2: continue
        f_ = fr[(x[0], x[1], x[2])]
        js = [abs(x[7])] if abs(x[7]) > 1e-15 else []; jf = [abs(f_["J"])] if abs(x[7]) > 1e-15 else []
        for p_, q_ in zip(list(x[3]) + list(x[4]) + list(x[5]) + list(x[6]) + js,
                          list(f_["up"]) + list(f_["down"]) + list(f_["lepton"]) + list(f_["V"]) + jf):
            det = max(det, dup_disagreement(p_, q_)); n += 1
            if p_ > 0 and q_ > 0:
                dl = abs(math.log10(p_) - math.log10(q_)); raw = max(raw, dl); over += dl > STORE
    return fname, det, raw, n, over


def main(d, man, expected, out, workers="4"):
    sys.path.insert(0, str(GEN))
    from guard import require_pushed_manifest
    g = require_pushed_manifest(man, expected)
    names = sorted(g["per_file"])
    with Pool(int(workers)) as P:
        res = P.map(task, [(n, d) for n in names])
    rep = {"files": len(res), "values_compared": sum(r[3] for r in res), "determinism_max_disagreement": max(r[1] for r in res),
           "readout_raw_max_log10": max(r[2] for r in res), "storage_bound_log10": STORE,
           "pairs_above_storage_bound": sum(r[4] for r in res), "files_without_a_chosen_node": sum(r[3] == 0 for r in res),
           "rule": "census_io.dup_disagreement (the census's 8-digit precision)"}
    rep["gate"] = "PASS" if rep["determinism_max_disagreement"] <= 1e-6 else "FAIL"
    pathlib.Path(out).write_text(json.dumps(rep, indent=1) + "\n", encoding="utf-8"); print(json.dumps(rep, indent=1))


if __name__ == "__main__":
    if len(sys.argv) not in (5, 6): sys.exit(__doc__)
    main(*sys.argv[1:])
