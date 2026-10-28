"""Main's check of the census extension's tail file: 20 rows drawn with main's RNG, recomputed with B1753's point()."""
import sys, json, random, pathlib
D = pathlib.Path(__file__).resolve().parents[1]; sys.path.insert(0, str(D))
import census_ext as CE
rows = [json.loads(l) for l in (D / "b1753_all266" / "census_ext_tail.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
worst = 0.0; n = 0
for r in random.Random(20261029).sample(rows, 20):
    m = CE.point((r["apex"], r["Re_tau"], r["Im_tau"], r["line"]))
    for k, v in r.items():
        if k.startswith(("up|", "down|", "lep|", "ckm|")):
            n += 1
            for x, y in zip(v, m[k]): worst = max(worst, abs(x - y))
print("tail: 20 rows recomputed (%d keyed entries): max |stored - recomputed| = %.3e" % (n, worst)); print("tail_check exit 0")
