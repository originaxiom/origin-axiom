"""B1735, part C (the control): the chi2-best row of B1726's census recomputed from scratch through B1726's own
compute() (line (2/5, 1/10), tau = 0.35 + 3.05i, both horocycles, every sector in S and S~), against the stored row;
and the row's six, D, CKM and chi2 at B1720's definition, read from the fresh values.
    python3 -B control.py      # writes control.json beside itself
Importing computes nothing."""
import io, json, math, contextlib, importlib.util, pathlib
from fractions import Fraction as Fr
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
V = ROOT / "frontier" / "B1726_the_two_ingredients_replicated" / "verification"


def main():
    import check
    spec = importlib.util.spec_from_file_location("c26", V / "census.py"); c26 = importlib.util.module_from_spec(spec); spec.loader.exec_module(c26)
    k = c26.lines().index((Fr(2, 5), Fr(1, 10)))
    stored = [json.loads(l) for l in (V / "census.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
    stored = [r for r in stored if r["line"] == k and r["Re_tau"] == 0.35 and r["Im_tau"] == 3.05][0]
    with contextlib.redirect_stdout(io.StringIO()):
        fresh = c26.compute(0.35, 3.05, Fr(2, 5), Fr(1, 10))
    dev = 0.0
    for key, v in fresh.items():
        a, b = np.array(v, dtype=float), np.array(stored[key], dtype=float)
        m = (np.abs(a) > 1e-300) & (np.abs(b) > 1e-300)
        dev = max(dev, float(np.max(np.abs(np.log(np.abs(a[m])) - np.log(np.abs(b[m]))))) if m.any() else 0.0)
    m = check.mod("B1726"); T = m.arrays()["T6"]; sg = check.sigma()
    six = np.log(np.array(fresh["up|L_max|St"] + fresh["down|L_max|S"] + fresh["lep|L_max|S"])) + np.array([0, 0, 0, 0, math.log(3), -math.log(3)])
    C = json.loads((ROOT / "frontier" / "B1612_the_mixing_patterns_the_weave_fixes" / "verification" / "data.json").read_text(encoding="utf-8"))["ckm_abs"]["value"]
    ckm = fresh["ckm|L_max|St|S"]
    out = {"line_index": k, "line": "2/5,1/10", "tau": [0.35, 3.05], "horocycle": "L_max", "readings": ["St", "S", "S"], "lepton_factor": 3,
           "fresh_vs_stored_max_abs_log": dev, "model_over_measured": np.exp(six - T).tolist(), "pulls": ((six - T) / sg).tolist(),
           "chi2_six": float((((six - T) / sg) ** 2).sum()), "D": math.exp(six[4] + six[3] - six[2] - six[5]),
           "ckm_model_over_measured": [ckm[0] / C[0][1], ckm[1] / C[1][2], ckm[2] / C[0][2]], "J": ckm[3]}
    json.dump(out, open(HERE / "control.json", "w"), indent=1)
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
