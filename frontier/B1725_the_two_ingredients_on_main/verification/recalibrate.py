"""B1725 (P-293), part B: the web seat's TWO_INGREDIENTS result recalibrated with the choice of ingredients counted.
The seat's sealed calibration fits each random target with the one configuration chosen after seeing the data (S~ in
every sector, lepton factor 3).  Here every random target gets the same freedom the choice had, on the seat's census
(no new model computation), its draws (r_masses, r_ckm; 4 000 six-targets, then 4 000 nine-targets) and four menus:
    sealed     (S~, S~, S~) with the factor 3                      -- reproduces the seat's sealed numbers at seed 1720
    seat_menu  {(S~, S, S), (S~, S~, S~)} x {1, 3}                  -- the four configurations the seat compared
    c_free     the seat's two reading rules, the lepton factor c continuous (only m_mu m_e / m_tau^2 constrained)
    all_read   every (up, down, lepton) reading (27) x {1, 3}; the CKM from the up and down readings
    cov_read   the same over the covariant readings S and S~ only (8 x {1, 3}); B1724: S* is covariant only under Gamma(2)
For a menu the statistic is the best worst factor over rows and configurations; a random target fits as well if its
own best over the same menu is at most the data's.  Seed 1720 (the seal's) and seeds 100-119.
    python3 -B recalibrate.py [--workers 8]      # writes recalibrate.json beside itself
Importing computes nothing."""
import sys, json, math, random, hashlib, pathlib
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
CENSUS = HERE.parent / "received" / "two_ingredients_census.jsonl"
CENSUS_SHA = "f379a4b8cfe2966d9d067abff323f6f654560d589c1d55f55320d816d59c5c4b"
DATA = ROOT / "frontier" / "B1637_fits_on_the_ruled_branch" / "received" / "HZ2021_running_masses_MZ.json"
DATA_SHA = "63450365401c149c726e928f842bc7810086ad4d897a62f51217e3c12189880f"
CKMDATA = ROOT / "frontier" / "B1612_the_mixing_patterns_the_weave_fixes" / "verification" / "data.json"
CKM_SHA = "61ea1565a2a8b4e053c33cc3b29e37484f6c9c2aeca54f9b6a83c89137e0d606"
RD = ("S", "St", "conjS")
LC3 = math.log(3)
SEEDS = [1720] + list(range(100, 120))
N = 4000
_A = {}


def arrays():
    """per row (8 512 points x 2 horocycles): U, Dn, E [row, reading, 2] and K [row, up reading, down reading, 3] (logs);
    the targets T6, T9.  Loaded once per process."""
    if not _A:
        assert hashlib.sha256(CENSUS.read_bytes()).hexdigest() == CENSUS_SHA
        assert hashlib.sha256(DATA.read_bytes()).hexdigest() == DATA_SHA and hashlib.sha256(CKMDATA.read_bytes()).hexdigest() == CKM_SHA
        v = json.loads(DATA.read_text(encoding="utf-8"))["masses_GeV"]["value"]; C = json.loads(CKMDATA.read_text(encoding="utf-8"))["ckm_abs"]["value"]
        T6 = np.log(np.array([v["c"] / v["t"], v["u"] / v["t"], v["s"] / v["b"], v["d"] / v["b"], v["mu"] / v["tau"], v["e"] / v["tau"]]))
        rows = [json.loads(l) for l in CENSUS.read_text(encoding="utf-8").splitlines() if l.strip()]
        assert len(rows) == 8512 == len({(r["line"], r["Re_tau"], r["Im_tau"]) for r in rows})
        lg = lambda x: np.log(np.maximum(np.array(x, dtype=float), 1e-300))
        U, Dn, E, K = [], [], [], []
        for r in rows:
            for h in ("L_max", "L_2"):
                U.append([lg(r[f"up|{h}|{a}"]) for a in RD]); Dn.append([lg(r[f"down|{h}|{a}"]) for a in RD])
                E.append([lg(r[f"lep|{h}|{a}"]) for a in RD]); K.append([[lg(r[f"ckm|{h}|{a}|{b}"][:3]) for b in RD] for a in RD])
        _A.update(U=np.array(U), Dn=np.array(Dn), E=np.array(E), K=np.array(K), T6=T6,
                  T9=np.concatenate([T6, np.log(np.array([C[0][1], C[1][2], C[0][2]]))]))
    return _A


def menus(t):
    """the best worst factor (a log) over each menu for the target t (six or nine logs)"""
    A = arrays(); U, Dn, E, K = A["U"], A["Dn"], A["E"], A["K"]
    eu = np.max(np.abs(U - t[0:2]), axis=2); ed = np.max(np.abs(Dn - t[2:4]), axis=2)
    dm, de = E[:, :, 0] - t[4], E[:, :, 1] - t[5]
    el = np.stack([np.maximum(np.abs(dm), np.abs(de)), np.maximum(np.abs(dm + LC3), np.abs(de - LC3))], axis=2)
    el_free = np.abs(dm + de) / 2                                    # min over c of max(|dm + ln c|, |de - ln c|)
    nine = len(t) == 9
    ek = np.max(np.abs(K - t[6:9]), axis=3) if nine else None
    iS, iSt = RD.index("S"), RD.index("St")
    def cfg(a, b, c, ci=None, free=False):
        w = np.maximum(np.maximum(eu[:, a], ed[:, b]), el_free[:, c] if free else el[:, c, ci])
        return np.maximum(w, ek[:, a, b]) if nine else w
    seat = ((iSt, iS, iS), (iSt, iSt, iSt))
    out = {"sealed": cfg(iSt, iSt, iSt, 1).min(),
           "seat_menu": min(cfg(*r, ci).min() for r in seat for ci in (0, 1)),
           "c_free": min(cfg(*r, free=True).min() for r in seat)}
    q = (np.maximum(np.maximum(eu[:, :, None], ed[:, None, :]), ek).min(axis=(1, 2)) if nine else np.maximum(eu.min(axis=1), ed.min(axis=1)))
    out["all_read"] = np.maximum(q, el.min(axis=(1, 2))).min()
    cv = [iS, iSt]                                                   # the covariant readings only (B1724: S* is not)
    qc = (np.maximum(np.maximum(eu[:, cv][:, :, None], ed[:, cv][:, None, :]), ek[:, cv][:, :, cv]).min(axis=(1, 2)) if nine
          else np.maximum(eu[:, cv].min(axis=1), ed[:, cv].min(axis=1)))
    out["cov_read"] = np.maximum(qc, el[:, cv, :].min(axis=(1, 2))).min()
    return out


def draws(seed):
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
    d6 = [np.log(np.array(r_masses())) for _ in range(N)]
    d9 = [np.log(np.array(r_masses() + r_ckm())) for _ in range(N)]
    return d6, d9


def one(seed):
    A = arrays(); d6, d9 = draws(seed); out = {}
    for name, T, ds in (("six", A["T6"], d6), ("nine", A["T9"], d9)):
        data = menus(T); rand = [menus(t) for t in ds]
        out[name] = {m: {"data_best_factor": float(math.exp(data[m])), "random_as_good": float(np.mean([r[m] <= data[m] + 1e-12 for r in rand]))} for m in data}
    return seed, out


def main():
    from multiprocessing import Pool
    nw = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else 1
    with Pool(nw) as P:
        res = dict(P.map(one, SEEDS))
    summary = {}
    for name in ("six", "nine"):
        for m in ("sealed", "seat_menu", "c_free", "all_read", "cov_read"):
            a = np.array([res[s][name][m]["random_as_good"] for s in SEEDS[1:]])
            summary["%s|%s" % (name, m)] = {"data_best_factor": res[1720][name][m]["data_best_factor"], "seed_1720": res[1720][name][m]["random_as_good"],
                                            "mean_100_119": float(a.mean()), "sem": float(a.std(ddof=1) / math.sqrt(len(a))), "min": float(a.min()), "max": float(a.max()),
                                            "seeds_at_or_below_1pct": int((a <= 0.01).sum())}
            s = summary["%s|%s" % (name, m)]
            print("%-4s %-10s data %.3f  seed 1720 %.4f  seeds 100-119 %.4f +- %.4f (%d of 20 at or below 1%%)" % (name, m, s["data_best_factor"], s["seed_1720"], s["mean_100_119"], s["sem"], s["seeds_at_or_below_1pct"]))
    json.dump({"census_sha256": CENSUS_SHA, "N": N, "seeds": SEEDS, "per_seed": {str(k): v for k, v in res.items()}, "summary": summary},
              open(HERE / "recalibrate.json", "w"), indent=1)


if __name__ == "__main__":
    main()
