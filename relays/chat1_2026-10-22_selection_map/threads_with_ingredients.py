#!/usr/bin/env python3
"""THREADS_WITH_INGREDIENTS_RULE.md: B1720's thread census (its 121 classes, each at its apex tau with the lines its
monodromy fixes, read from B1720's committed the_thread_census.json at main's 3412bf09d) re-evaluated with every Higgs
reading in every sector by two_ingredients_census.evaluate (main's B1720 instrument, unchanged).  Then the cells H1-H4
under the sealed rule (S~ for every sector, Clebsch 3 on the leptons) with main's measure and calibration, and the
control C2 against B1720's committed rows and its committed best.
    python3 -B threads_with_ingredients.py [--workers 2]   # the model, no data: writes threads_with_ingredients.jsonl
    python3 -B threads_with_ingredients.py --compare       # the cells: writes _comparison.json and _run.txt"""
import hashlib, json, math, random, subprocess, sys, time, pathlib, importlib.util
from fractions import Fraction as Fr
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / ".git").exists())
REV = "3412bf09d"
B1720 = "frontier/B1720_the_thread_fixes_the_point/verification/"
OUTL = HERE / "threads_with_ingredients.jsonl"


def git(path):
    return subprocess.run(["git", "show", f"{REV}:{path}"], cwd=ROOT, capture_output=True, check=True).stdout


G = json.loads(git(B1720 + "the_thread_census.json"))
TASKS = [(k, j) for k, c in enumerate(G["classes"]) for j in range(len(c["lines"]))]
_spec = importlib.util.spec_from_file_location("tic", HERE / "two_ingredients_census.py")
tic = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(tic)


def run(task):
    k, j = task
    c = G["classes"][k]; a, b = c["lines"][j]
    r = tic.evaluate(c["tau"][0], c["tau"][1], float(Fr(a)), float(Fr(b)))
    r.update({"class": k, "line": j})
    return r


LOG = []


def say(*a):
    s = " ".join(str(x) for x in a); LOG.append(s); print(s, flush=True)


def compare():
    bd = git("frontier/B1637_fits_on_the_ruled_branch/received/HZ2021_running_masses_MZ.json")
    bc = git("frontier/B1612_the_mixing_patterns_the_weave_fixes/verification/data.json")
    assert hashlib.sha256(bd).hexdigest() == "63450365401c149c726e928f842bc7810086ad4d897a62f51217e3c12189880f"
    assert hashlib.sha256(bc).hexdigest() == "61ea1565a2a8b4e053c33cc3b29e37484f6c9c2aeca54f9b6a83c89137e0d606"
    v = json.loads(bd)["masses_GeV"]["value"]; C = json.loads(bc)["ckm_abs"]["value"]
    T6 = np.log(np.array([v["c"] / v["t"], v["u"] / v["t"], v["s"] / v["b"], v["d"] / v["b"], v["mu"] / v["tau"], v["e"] / v["tau"]]))
    T9 = np.concatenate([T6, np.log(np.array([C[0][1], C[1][2], C[0][2]]))])
    rows = [json.loads(l) for l in OUTL.read_text().splitlines() if l.strip()]
    assert len({(r["class"], r["line"]) for r in rows}) == len(TASKS) == len(rows) == 3249, len(rows)
    rows.sort(key=lambda r: (r["class"], r["line"]))

    # C2 (a): every committed value of B1720's rows, recomputed
    mine = {(r["class"], r["line"]): r for r in rows}; dev = 0.0
    for p in G["rows"]:
        r = mine[(p["class"], p["line"])]
        for hor in ("L_max", "L_2"):
            pairs = [(p[f"up|{hor}|{rd}"], r[f"up|{hor}|{rd}"]) for rd in ("S", "St", "conjS")]
            pairs += [(p[f"down|{hor}|S"], r[f"down|{hor}|S"]), (p[f"lep|{hor}|S"], r[f"lep|{hor}|S"])]
            pairs += [(p[f"ckm|{hor}|{rd}"][:3], r[f"ckm|{hor}|{rd}|S"][:3]) for rd in ("S", "St", "conjS")]
            for x, y in pairs:
                for s, t in zip(x, y):
                    dev = max(dev, abs(math.log(max(s, 1e-300) / max(t, 1e-300))))

    def matrix(cu, cd, cl, c):
        M, lab = [], []
        for r in rows:
            for hor in ("L_max", "L_2"):
                vals = r[f"up|{hor}|{cu}"] + r[f"down|{hor}|{cd}"] + r[f"lep|{hor}|{cl}"] + r[f"ckm|{hor}|{cu}|{cd}"][:3]
                x = np.log(np.maximum(np.array(vals, dtype=float), 1e-300)); x[4] += math.log(c); x[5] -= math.log(c)
                M.append(x); lab.append((r["class"], r["line"], hor, r[f"ckm|{hor}|{cu}|{cd}"][3]))
        return np.array(M), lab

    def best(M, t):
        w = np.max(np.abs(M - t), axis=1); i = int(np.argmin(w)); return float(np.exp(w[i])), i

    rng = random.Random(1720)                         # as two_ingredients_compare.py: 4 000 six-target draws, then 4 000 nine

    def r_masses():
        tg = []
        for _s in range(3):
            while True:
                r2 = 10 ** rng.uniform(-3, -1); r1 = 10 ** rng.uniform(-6, -2.5)
                if r1 < r2:
                    break
            tg += [r2, r1]
        return tg

    def r_ckm():
        while True:
            a, b, c = 10 ** rng.uniform(-1.5, -0.2), 10 ** rng.uniform(-2.5, -0.7), 10 ** rng.uniform(-3.5, -1.5)
            if c < b < a:
                return [a, b, c]

    N = 4000
    d6 = [np.log(np.array(r_masses())) for _ in range(N)]
    d9 = [np.log(np.array(r_masses() + r_ckm())) for _ in range(N)]

    def describe(lab):
        k, j, hor, J = lab; c = G["classes"][k]
        return {"word": c["word"], "height": c["height"], "tau": c["tau"], "line": c["lines"][j], "horocycle": hor, "J": J}

    M, lab = matrix("St", "St", "St", 3)
    w6, i6 = best(M[:, :6], T6); w9, i9 = best(M, T9)
    f6 = float(np.mean([best(M[:, :6], d)[0] <= w6 + 1e-12 for d in d6]))
    f9 = float(np.mean([best(M, d)[0] <= w9 + 1e-12 for d in d9]))
    b1720_best = json.loads(git(B1720 + "comparison.json"))["masses"]["worst_factor"]
    Mc, _ = matrix("St", "S", "S", 1); wc, _ = best(Mc[:, :6], T6)
    Mr, labr = matrix("St", "S", "S", 3); wr6, ir6 = best(Mr[:, :6], T6); wr9, ir9 = best(Mr, T9)
    per = {}
    for i, l in enumerate(lab):
        wv = float(np.exp(np.max(np.abs(M[i, :6] - T6)))); word = G["classes"][l[0]]["word"]
        if word not in per or wv < per[word][0]:
            per[word] = (wv, describe(l))
    top = sorted(per.items(), key=lambda kv: kv[1][0])[:10]
    out = {"rows": len(M),
           "sealed_six": {"best": w6, "at": describe(lab[i6]), "model_over_measured": np.exp(M[i6, :6] - T6).tolist(), "random_as_good": f6},
           "sealed_nine": {"best": w9, "at": describe(lab[i9]), "model_over_measured": np.exp(M[i9] - T9).tolist(), "random_as_good": f9},
           "H1_six_within_2": w6 <= 2.0, "H2_six_specific": f6 <= 0.01, "H3_nine_within_2.5": w9 <= 2.5, "H4_nine_specific": f9 <= 0.01,
           "C2_max_abs_log_against_B1720_rows": dev, "C2_six_main_readings_no_clebsch": wc, "C2_B1720_committed_best": b1720_best,
           "C2_holds": dev < 1e-6 and abs(math.log(wc / b1720_best)) < 1e-6,
           "readout_main_readings_with_clebsch": {"six": wr6, "six_at": describe(labr[ir6]), "nine": wr9, "nine_at": describe(labr[ir9])},
           "readout_ten_best_classes_six": [[kv[1][0], kv[0], kv[1][1]] for kv in top]}
    say(f"sealed (S~ for every sector, Clebsch 3): six {w6:.3f} (random as good {f6:.4f}) at {describe(lab[i6])}")
    say(f"  nine {w9:.3f} (random as good {f9:.4f}) at {describe(lab[i9])}")
    say(f"H1 {out['H1_six_within_2']}  H2 {out['H2_six_specific']}  H3 {out['H3_nine_within_2.5']}  H4 {out['H4_nine_specific']}")
    say(f"C2: max |dlog| against B1720's rows {dev:.2e}; six under main's readings, no Clebsch {wc:.10f} (B1720 {b1720_best:.10f}) -> {out['C2_holds']}")
    say(f"read-out, main's readings with the Clebsch: six {wr6:.3f} at {describe(labr[ir6])}; nine {wr9:.3f}")
    say("read-out, ten best classes (six, sealed rule):", "; ".join(f"{kv[0]} {kv[1][0]:.3f}" for kv in top))
    (HERE / "threads_with_ingredients_comparison.json").write_text(json.dumps(out, indent=1, default=str) + "\n")
    (HERE / "threads_with_ingredients_run.txt").write_text("\n".join(LOG) + "\n")


if __name__ == "__main__":
    if "--compare" in sys.argv:
        compare(); sys.exit(0)
    from multiprocessing import Pool
    nw = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else 2
    done = set()
    if OUTL.exists():
        for line in OUTL.read_text().splitlines():
            if line.strip():
                r = json.loads(line); done.add((r["class"], r["line"]))
    todo = [t for t in TASKS if t not in done]
    print(f"{len(TASKS)} points; {len(done)} done; {len(todo)} to do", flush=True)
    t0 = time.time(); n = 0
    with Pool(nw) as P, open(OUTL, "a") as fh:
        for r in P.imap_unordered(run, todo, chunksize=2):
            fh.write(json.dumps(r) + "\n"); fh.flush(); n += 1
            if time.time() - t0 > 6600:
                print(f"budget reached after {n}; rerun to resume", flush=True); P.terminate(); break
    print(f"wrote {n} in {time.time() - t0:.0f} s; total {len(done) + n} of {len(TASKS)}", flush=True)
