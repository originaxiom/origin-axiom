"""The rerun of exit_law_check.py at p = 0.75 (seed 7531, 40 000 samples per arm), made because the first run's KS distance
there (0.0151) exceeded the 5% critical value (0.0136, two-sample, 20 000 each; p about 0.02).  Saved for provenance."""
import json, pathlib, random
src = (pathlib.Path(__file__).parent / "exit_law_check.py").read_text().split("rng = random.Random(1663)")[0]
ns = {}; exec(src, ns)
rng = random.Random(7531); N = 40000; p = 0.75
M = [ns["exit_point"](0.0, rng) for _ in range(N)]
walk = [ns["exit_point"](p, rng) for _ in range(N)]
mix = [(-m if rng.random() < p else m) for m in [ns["exit_point"](0.0, rng) for _ in range(N)]]
out = {"p": p, "N": N, "seed": 7531, "KS(walk, (1-p)M + p(-M))": round(ns["ks"](walk, mix), 4), "5% critical value 1.36 sqrt(2/N)": round(1.36 * (2 / N) ** 0.5, 4),
       "P(xi > 0)": round(sum(x > 0 for x in walk) / N, 4)}
print(json.dumps(out)); (pathlib.Path(__file__).with_suffix(".json")).write_text(json.dumps(out, indent=1))
