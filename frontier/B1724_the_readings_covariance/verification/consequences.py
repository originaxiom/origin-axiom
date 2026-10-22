"""B1724 (P-297): what the readings' covariance changes in the sealed tests that used B1660's three up readings.
For B1712, B1713, B1720 and B1723 the rows are rebuilt from each arc's committed output exactly as its compare.py builds
them, and its calibration is re-run with its own seed and draw order: first with every reading (must reproduce the stored
numbers), then with the up reading S* removed, since S* is covariant only under Gamma(2) (covariance.py) and its rows
depend on the representative of tau.  The random targets are the same in both runs.  The verdicts stand as sealed; these
are labelled read-outs after the fact.
    python3 -B consequences.py [--workers 6]      # writes consequences.json beside itself
Importing computes nothing."""
import sys, json, math, random, hashlib, pathlib
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
F = ROOT / "frontier"
DATA = F / "B1637_fits_on_the_ruled_branch" / "received" / "HZ2021_running_masses_MZ.json"
CKMDATA = F / "B1612_the_mixing_patterns_the_weave_fixes" / "verification" / "data.json"
ARCS = {"B1712": ("B1712_the_weave_census_of_lines", "the_line_census_masses.json", 1712),
        "B1713": ("B1713_the_complement_and_the_mixing", "the_complement_and_mixing.json", 1713),
        "B1720": ("B1720_the_thread_fixes_the_point", "the_thread_census.json", 1720),
        "B1723": ("B1723_the_golden_valley", "the_golden_valley.json", 1723)}
N = 4000


def targets():
    assert hashlib.sha256(DATA.read_bytes()).hexdigest() == "63450365401c149c726e928f842bc7810086ad4d897a62f51217e3c12189880f"
    assert hashlib.sha256(CKMDATA.read_bytes()).hexdigest() == "61ea1565a2a8b4e053c33cc3b29e37484f6c9c2aeca54f9b6a83c89137e0d606"
    v = json.loads(DATA.read_text(encoding="utf-8"))["masses_GeV"]["value"]; C = json.loads(CKMDATA.read_text(encoding="utf-8"))["ckm_abs"]["value"]
    t6 = np.log(np.array([v["c"] / v["t"], v["u"] / v["t"], v["s"] / v["b"], v["d"] / v["b"], v["mu"] / v["tau"], v["e"] / v["tau"]]))
    return t6, np.log(np.array([C[0][1], C[1][2], C[0][2]]))


def logs(x): return [math.log(max(z, 1e-300)) for z in x]


def rows(arc):
    """(A, readA, MX, readB): the mass rows and the mixing rows (six + three logs) with each row's up reading, as the arc
    builds them (B1712: masses only, rows with a zero dropped; B1713: masses on the complement lines only)"""
    d, fn, _ = ARCS[arc]; G = json.loads((F / d / "verification" / fn).read_text(encoding="utf-8"))
    A, rA, MX, rB = [], [], [], []
    NC = G.get("n_complement")
    for p in G["rows"]:
        for hor in ("L_max", "L_2"):
            for rd in ("S", "St", "conjS"):
                vals = p["up|%s|%s" % (hor, rd)] + p["down|%s|S" % hor] + p["lep|%s|S" % hor]
                if arc == "B1712":
                    if all(x > 0 for x in vals): A.append([math.log(x) for x in vals]); rA.append(rd)
                    continue
                ck = p["ckm|%s|%s" % (hor, rd)]
                if arc != "B1713" or p["line"] < NC: A.append(logs(vals)); rA.append(rd)
                MX.append(logs(vals) + logs(ck[:3])); rB.append(rd)
    return np.array(A), np.array(rA), (np.array(MX) if MX else None), (np.array(rB) if rB else None)


def draws(seed, mixing):
    rng = random.Random(seed)
    def r_masses():
        tg = []
        for _s in range(3):
            while True:
                r2 = 10 ** rng.uniform(-3, -1); r1 = 10 ** rng.uniform(-6, -2.5)
                if r1 < r2: break
            tg += [r2, r1]
        return tg
    def r_ckm():
        while True:
            a, b, c = 10 ** rng.uniform(-1.5, -0.2), 10 ** rng.uniform(-2.5, -0.7), 10 ** rng.uniform(-3.5, -1.5)
            if c < b < a: return [a, b, c]
    dA = [np.log(np.array(r_masses())) for _ in range(N)]
    if not mixing: return dA, None, None
    dK = [np.log(np.array(r_ckm())) for _ in range(N)]
    dJ = [np.log(np.array(r_masses() + r_ckm())) for _ in range(N)]
    return dA, dK, dJ


def bestlog(M, t): return float(np.min(np.max(np.abs(M - t), axis=1)))


def calib(M, t, ds):
    obs = bestlog(M, t)
    hits = sum(bestlog(M, d) <= obs + 1e-12 for d in ds)
    return {"best_factor": math.exp(obs), "fraction_fit_as_well": hits / len(ds)}


def one(job):
    arc, which, version = job
    t6, t3 = targets(); A, rA, MX, rB = rows(arc); seed = ARCS[arc][2]
    dA, dK, dJ = draws(seed, MX is not None)
    keepA = np.ones(len(rA), bool) if version == "all" else (rA != "conjS")
    if which == "masses":
        return job, dict(calib(A[keepA], t6, dA), rows=int(keepA.sum()))
    keepB = np.ones(len(rB), bool) if version == "all" else (rB != "conjS")
    if which == "mixing":
        return job, dict(calib(MX[keepB][:, 6:], t3, dK), rows=int(keepB.sum()))
    return job, dict(calib(MX[keepB], np.concatenate([t6, t3]), dJ), rows=int(keepB.sum()))


STORED = {  # (arc, which): stored fraction and best factor, from each arc's committed comparison.json
}


def stored():
    out = {}
    c = json.loads((F / ARCS["B1712"][0] / "verification" / "comparison.json").read_text(encoding="utf-8"))
    out[("B1712", "masses")] = (c["calibration"]["fraction_fit_as_well"], c["best_by_worst_factor"]["worst_factor"])
    c = json.loads((F / ARCS["B1713"][0] / "verification" / "comparison.json").read_text(encoding="utf-8"))
    out[("B1713", "masses")] = (c["A"]["calibration"]["fraction_fit_as_well"], c["A"]["best_by_worst_factor"]["worst_factor"])
    out[("B1713", "mixing")] = (c["B"]["calibration_three"]["fraction_fit_as_well"], c["B"]["best_three"]["worst_factor"])
    out[("B1713", "nine")] = (c["B"]["calibration_nine"]["fraction_fit_as_well"], c["B"]["best_nine"]["worst_factor"])
    for arc in ("B1720", "B1723"):
        c = json.loads((F / ARCS[arc][0] / "verification" / "comparison.json").read_text(encoding="utf-8"))
        out[(arc, "masses")] = (c["calibration_masses"]["fraction_fit_as_well"], c["masses"]["worst_factor"])
        out[(arc, "mixing")] = (c["calibration_mixing"]["fraction_fit_as_well"], c["mixing"]["worst_factor"])
        out[(arc, "nine")] = (c["calibration_nine"]["fraction_fit_as_well"], c["nine"]["worst_factor"])
    return out


def main():
    from multiprocessing import Pool
    nw = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else 1
    S = stored()
    jobs = [(arc, which, ver) for (arc, which) in S for ver in ("all", "covariant")]
    with Pool(nw) as P:
        res = dict(P.map(one, jobs))
    out = {}
    for (arc, which), (frac, best) in S.items():
        a, c = res[(arc, which, "all")], res[(arc, which, "covariant")]
        rep = abs(a["fraction_fit_as_well"] - frac) < 1e-12 and abs(a["best_factor"] - best) < 1e-9 * best
        out["%s|%s" % (arc, which)] = {"stored": {"fraction": frac, "best": best}, "all_readings": a, "covariant_readings": c, "reproduced": rep}
        print("%s %-6s stored %.4f at %.3f | rebuilt %.4f at %.3f (%s) | without S*: %.4f at %.3f (%d rows of %d)" % (
            arc, which, frac, best, a["fraction_fit_as_well"], a["best_factor"], "reproduced" if rep else "NOT REPRODUCED",
            c["fraction_fit_as_well"], c["best_factor"], c["rows"], a["rows"]))
    json.dump(out, open(HERE / "consequences.json", "w"), indent=1)


if __name__ == "__main__":
    main()
