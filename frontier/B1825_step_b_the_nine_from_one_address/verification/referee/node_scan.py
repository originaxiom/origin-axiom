import sys, io, glob, gzip, json, math, contextlib
import numpy as np
sys.path.insert(0, "frontier/B1741_tau_from_the_thread_rule_the_line_free/verification")
with contextlib.redirect_stdout(io.StringIO()):
    import compare
    T9 = np.array(compare.arrays()["T9"], float)
t10 = np.concatenate([T9, [math.log(3.12e-5)]])
sig = np.array(json.load(open("scripts/stepb/sigma/SIGMA_ONLY.json"))["sigma_natural_log"])
tt = t10.copy(); tt[4] -= math.log(3); tt[5] += math.log(3)
def feats(rows):
    a = np.array([[r[3][1], r[3][0], r[4][1], r[4][0], r[5][1], r[5][0], r[6][0], r[6][1], r[6][2], abs(r[7])] for r in rows], float)
    with np.errstate(divide="ignore", invalid="ignore"):
        f = np.where(a > 0, np.log(np.where(a > 0, a, 1.0)), -np.inf)
    return f
THR = [23.209251158954356, 50, 100, 200, 300]
cnt = {str(t): 0 for t in THR}
best = {"ten": (1e99,), "nine": (1e99,), "six": (1e99,)}
total = 0; rows_n = 0
six_lim = 1.358 * 1.001 + 0.001 + 13.8629
clause_n = 0; clause_best = (1e99,); bound_n = 0; bound_bad = 0; bound_undef = 0; bound_zero = 0
lowcut = 1.358 * 1.001 + 0.001
for fn in sorted(glob.glob("audit/drafts/rigid_census/refined/*.jsonl.gz")):
    with gzip.open(fn, "rt") as fh:
        for ln in fh:
            rec = json.loads(ln)
            if "error" in rec or "rows" not in rec: continue
            rs = [r for r in rec["rows"] if r[0] != 6]
            if not rs: continue
            F = feats(rs); vd = np.array([bool(r[8]) for r in rs])
            with np.errstate(invalid="ignore"):
                z = ((F - tt) / sig) ** 2
            z = np.where(np.isnan(z), np.inf, z)
            c = z.sum(1); c9 = z[:, :9].sum(1); c6 = z[:, :6].sum(1); c4 = z[:, 6:].sum(1)
            cten = np.where(vd, c, np.inf)
            rows_n += len(rs)
            for t in THR: cnt[str(t)] += int((cten < t).sum())
            for k, arr, mask in (("ten", cten, None), ("nine", np.where(vd, c9, np.inf), None), ("six", c6, None)):
                i = int(np.argmin(arr))
                if arr[i] < best[k][0]:
                    r = rs[i]; best[k] = (float(arr[i]), fn.split("/")[-1], rec["tau"], rec["line"], r[0], r[1], r[2], bool(r[8]))
            m = c6 <= six_lim
            if m.any():
                bound_n += int(m.sum())
                a = np.array([[r[6][0], r[6][1], r[6][2], abs(r[7])] for r in rs])
                zero = (a < 1e-12).any(1)
                bound_undef += int((m & ~vd).sum()); bound_zero += int((m & zero).sum())
                mm = m & vd
                clause_n += int(mm.sum())
                if mm.any():
                    j = np.where(mm)[0][np.argmin(np.where(mm, c4, np.inf)[mm])] if False else None
                    c4m = np.where(mm, c4, np.inf); i = int(np.argmin(c4m))
                    if c4m[i] < clause_best[0]:
                        r = rs[i]; clause_best = (float(c4m[i]), fn.split("/")[-1], rec["tau"], rec["line"], r[0], r[1], r[2], float(c6[i]))
    print(fn, rows_n, best["ten"][0], file=sys.stderr, flush=True)
json.dump({"rows": rows_n, "count_below": cnt, "best": best, "clause": {"six_limit": six_lim, "rows_with_c6_in_bound": bound_n,
  "of_which_V_undefined": bound_undef, "of_which_structural_zero": bound_zero, "V_defined_rows": clause_n, "least_chi2_4": clause_best},
  "t10": t10.tolist(), "sigma": sig.tolist()}, open("frontier/B1825_step_b_the_nine_from_one_address/verification/referee/node_scan.json", "w"), indent=1)
