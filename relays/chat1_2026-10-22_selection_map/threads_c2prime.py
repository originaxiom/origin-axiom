#!/usr/bin/env python3
"""THREADS_C2_AMENDMENT.md: the control C2' (added before the THREADS run, the sealed C2 kept and reported as written).
C2'(a): every value committed in B1720's rows, recomputed in threads_with_ingredients.jsonl, agrees with B1720's: where
either value is below 1e-8 (a numerical zero: a massless state, or a CKM modulus forbidden by the line's symmetry) to
1e-9 in absolute value, otherwise to 1e-6 in |ln|.  C2'(b) is the sealed C2(b), read from the sealed comparison output.
No data.
    python3 -B threads_c2prime.py      # after threads_with_ingredients.py --compare; writes threads_c2prime.json, _run.txt"""
import json, math, subprocess, pathlib

HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / ".git").exists())
G = json.loads(subprocess.run(["git", "show", "3412bf09d:frontier/B1720_the_thread_fixes_the_point/verification/the_thread_census.json"],
                              cwd=ROOT, capture_output=True, check=True).stdout)
rows = {}
for line in (HERE / "threads_with_ingredients.jsonl").read_text().splitlines():
    if line.strip():
        r = json.loads(line); rows[(r["class"], r["line"])] = r
assert len(rows) == 3249 == len(G["rows"])
worst_log, worst_abs, n_small, n_all = 0.0, 0.0, 0, 0
for p in G["rows"]:
    r = rows[(p["class"], p["line"])]
    for hor in ("L_max", "L_2"):
        pairs = [(p[f"up|{hor}|{rd}"], r[f"up|{hor}|{rd}"]) for rd in ("S", "St", "conjS")]
        pairs += [(p[f"down|{hor}|S"], r[f"down|{hor}|S"]), (p[f"lep|{hor}|S"], r[f"lep|{hor}|S"])]
        pairs += [(p[f"ckm|{hor}|{rd}"][:3], r[f"ckm|{hor}|{rd}|S"][:3]) for rd in ("S", "St", "conjS")]
        for x, y in pairs:
            for s, t in zip(x, y):
                n_all += 1
                if min(s, t) < 1e-8:
                    n_small += 1; worst_abs = max(worst_abs, abs(s - t))
                else:
                    worst_log = max(worst_log, abs(math.log(s / t)))
cmp = json.loads((HERE / "threads_with_ingredients_comparison.json").read_text())
b_ok = abs(math.log(cmp["C2_six_main_readings_no_clebsch"] / cmp["C2_B1720_committed_best"])) < 1e-6
out = {"values_compared": n_all, "values_below_1e-8": n_small, "max_abs_diff_below_1e-8": worst_abs,
       "max_abs_log_diff_otherwise": worst_log, "C2prime_a": worst_abs < 1e-9 and worst_log < 1e-6, "C2prime_b": b_ok,
       "C2prime_holds": worst_abs < 1e-9 and worst_log < 1e-6 and b_ok,
       "sealed_C2_as_reported": {"max_abs_log": cmp["C2_max_abs_log_against_B1720_rows"], "holds": cmp["C2_holds"]}}
s = (f"C2' (a): {n_all} values, {n_small} below 1e-8 (max |diff| {worst_abs:.1e}); the rest max |dln| {worst_log:.1e} -> "
     f"{out['C2prime_a']}; (b) -> {b_ok}; C2' holds: {out['C2prime_holds']}.  Sealed C2 as written: max |dln| "
     f"{cmp['C2_max_abs_log_against_B1720_rows']:.2e}, holds {cmp['C2_holds']}")
print(s)
(HERE / "threads_c2prime.json").write_text(json.dumps(out, indent=1) + "\n")
(HERE / "threads_c2prime_run.txt").write_text(s + "\n")
