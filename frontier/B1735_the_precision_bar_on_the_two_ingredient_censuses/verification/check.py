"""B1735, part A (post hoc, labelled). Main's own check of W138 (the SM seat's third opinion on B1726, its labelled A3: every covariant reading with the
lepton factor free) and of the web seat's PRECISION_BAR (chi-square cells at main's definition, B1720 compare.py) on
B1726's and B1734's committed censuses.  Read-only on both arcs; writes check.json beside itself.  Importing computes nothing.
    python3 -B check.py [--workers 8]"""
import sys, json, math, importlib.util, pathlib
import numpy as np
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
ARCS = {"B1726": ROOT / "frontier" / "B1726_the_two_ingredients_replicated" / "verification" / "compare.py",
        "B1734": ROOT / "frontier" / "B1734_the_thread_rule_with_the_two_ingredients" / "verification" / "compare.py"}
ALLOW = 0.10
_M = {}


def mod(name):
    if name not in _M:
        spec = importlib.util.spec_from_file_location("cmp_" + name, ARCS[name]); m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m); _M[name] = m
    return _M[name]


def best_covfree(m, t, E=None):
    eu, ed, el, _ = E if E is not None else m.errs(t)
    best = math.inf
    for (a, b, l) in m.COV:
        w = np.maximum(np.maximum(eu[:, a], ed[:, b]), el["free"][:, l]); best = min(best, float(w.min()))
    return best


def sigma():
    d = json.loads((ROOT / "frontier" / "B1637_fits_on_the_ruled_branch" / "received" / "HZ2021_running_masses_MZ.json").read_text(encoding="utf-8"))
    v, s = d["masses_GeV"]["value"], d["masses_GeV"]["sigma"]
    pr = [("c", "t"), ("u", "t"), ("s", "b"), ("d", "b"), ("mu", "tau"), ("e", "tau")]
    return np.array([math.sqrt((s[a] / v[a]) ** 2 + (s[b] / v[b]) ** 2 + ALLOW ** 2) for a, b in pr])


def chi2(m):
    """minimum chi2_six over the rows, per menu (seat, cov with c in {1,3}; free and covfree with c chosen to minimise)"""
    A = m.arrays(); T = A["T6"]; sg = sigma(); out = {}
    for menu, cfgs in (("seat", m.SEAT), ("cov", m.COV), ("free", m.SEAT), ("covfree", m.COV)):
        best = (math.inf, None)
        for (a, b, l) in cfgs:
            du = (A["U"][:, a] - T[0:2]) / sg[0:2]; dd = (A["Dn"][:, b] - T[2:4]) / sg[2:4]
            dm, de = A["E"][:, l, 0] - T[4], A["E"][:, l, 1] - T[5]
            base = (du ** 2).sum(1) + (dd ** 2).sum(1)
            if menu in ("seat", "cov"):
                cands = [(base + ((dm + k) / sg[4]) ** 2 + ((de - k) / sg[5]) ** 2, k) for k in (0.0, math.log(3))]
            else:
                w4, w5 = 1 / sg[4] ** 2, 1 / sg[5] ** 2; k = (-dm * w4 + de * w5) / (w4 + w5)
                cands = [(base + ((dm + k) / sg[4]) ** 2 + ((de - k) / sg[5]) ** 2, k)]
            for c2, k in cands:
                i = int(np.argmin(c2))
                if c2[i] < best[0]:
                    kk = float(k if np.isscalar(k) else k[i])
                    best = (float(c2[i]), dict(row=list(A["lab"][i]), readings=[m.RD[a], m.RD[b], m.RD[l]], lepton_factor=math.exp(kk)))
        out[menu] = dict(chi2_six_min=best[0], **best[1])
    return out


def one(arg):
    name, seed = arg; m = mod(name); A = m.arrays(); d6, _ = m.draws(seed)
    obs = best_covfree(m, A["T6"]); hits = sum(best_covfree(m, t) <= obs + 1e-12 for t in d6)
    return name, seed, hits / len(d6), obs


def main():
    from multiprocessing import Pool
    nw = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else 1
    out = {"definition": "chi2_six as B1720 compare.py: sigma^2 = rel_a^2 + rel_b^2 + 0.10^2; bar 16.75 (the web seat's PRECISION_BAR)"}
    for name in ARCS: out[name] = {"chi2": chi2(mod(name))}
    jobs = [(name, s) for name in ARCS for s in mod(name).SEEDS]
    with Pool(nw) as P:
        res = P.map(one, jobs)
    for name in ARCS:
        per = {str(s): f for n, s, f, _ in res if n == name}
        obs = [o for n, s, f, o in res if n == name][0]
        out[name]["covfree_six"] = {"best_factor": math.exp(obs), "per_seed": per, "mean": float(np.mean(list(per.values())))}
    json.dump(out, open(pathlib.Path(__file__).with_name("check.json"), "w"), indent=1)
    for name in ARCS:
        print(name, "covfree six: best %.4f mean %.4f" % (out[name]["covfree_six"]["best_factor"], out[name]["covfree_six"]["mean"]),
              "| chi2_six min:", {k: round(v["chi2_six_min"], 2) for k, v in out[name]["chi2"].items()})


if __name__ == "__main__":
    main()
