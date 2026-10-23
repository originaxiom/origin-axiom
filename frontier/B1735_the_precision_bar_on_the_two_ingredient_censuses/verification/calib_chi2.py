"""B1735, part B (post hoc, labelled): the calibration of the chi-square cell on B1726's and B1734's committed censuses.  For each seed of
the arc's own list, B1695's random six-targets (the arc's draws()); for each target the minimum chi2_six over the same
rows and the same menu, sigma as B1720 compare.py (the data's errors with 0.10 in quadrature); the fraction of targets at
least as good as the data.  chi2 = |X - t|^2 per row is expanded as |X|^2 - 2 X.t + |t|^2, so a block of targets is one
matrix product.  Also the minimum chi2_nine (the six and |V_us|, |V_cb|, |V_ub|, the CKM's sigma as B1720: 0.10 with
PDG's errors; the seat's menu, CKM from the up and down readings).
    python3 -B calib_chi2.py [--workers 4]
Importing computes nothing."""
import sys, json, math, pathlib
import numpy as np
import check
ROOT = check.ROOT
MENUS = ("seat", "cov", "free", "covfree")


def features(m, menu):
    """per configuration: (row features X / sigma_eff, the map of a six-target to the same coordinates)"""
    A = m.arrays(); sg = check.sigma(); out = []
    cfgs = m.SEAT if menu in ("seat", "free") else m.COV
    for (a, b, l) in cfgs:
        base = np.concatenate([A["U"][:, a], A["Dn"][:, b]], axis=1) / sg[0:4]
        if menu in ("seat", "cov"):
            for k in (0.0, math.log(3)):
                X = np.concatenate([base, ((A["E"][:, l, 0] + k) / sg[4])[:, None], ((A["E"][:, l, 1] - k) / sg[5])[:, None]], axis=1)
                out.append((X, lambda T: np.concatenate([T[:, 0:4] / sg[0:4], T[:, 4:5] / sg[4], T[:, 5:6] / sg[5]], axis=1)))
        else:
            s45 = math.sqrt(sg[4] ** 2 + sg[5] ** 2)
            X = np.concatenate([base, ((A["E"][:, l, 0] + A["E"][:, l, 1]) / s45)[:, None]], axis=1)
            out.append((X, lambda T, s45=s45: np.concatenate([T[:, 0:4] / sg[0:4], ((T[:, 4] + T[:, 5]) / s45)[:, None]], axis=1)))
    return out


def min_chi2(F, T, block=400):
    """the minimum over rows and configurations of chi2_six for each target row of T (log six)"""
    best = np.full(len(T), np.inf)
    for X, tmap in F:
        x2 = (X ** 2).sum(1)
        for s in range(0, len(T), block):
            t = tmap(T[s:s + block]); c = x2[:, None] - 2 * X @ t.T + (t ** 2).sum(1)[None, :]
            best[s:s + block] = np.minimum(best[s:s + block], c.min(0))
    return best


def one(arg):
    name, seed = arg; m = check.mod(name); A = m.arrays(); d6, _ = m.draws(seed); T = np.array(d6)
    res = {}
    for menu in MENUS:
        F = features(m, menu); obs = float(min_chi2(F, A["T6"][None, :])[0])
        res[menu] = (obs, float(np.mean(min_chi2(F, T) <= obs + 1e-9)))
    return name, seed, res


def chi2_nine(m):
    A = m.arrays(); sg = check.sigma()
    C = json.loads((ROOT / "frontier" / "B1612_the_mixing_patterns_the_weave_fixes" / "verification" / "data.json").read_text(encoding="utf-8"))
    cv, cs = C["ckm_abs"]["value"], C["ckm_abs"]["sigma"] if "sigma" in C["ckm_abs"] else None
    vals = [cv[0][1], cv[1][2], cv[0][2]]
    errs = [cs[0][1] / cv[0][1], cs[1][2] / cv[1][2], cs[0][2] / cv[0][2]] if cs else [0, 0, 0]
    s9 = np.concatenate([sg, np.sqrt(np.array(errs) ** 2 + 0.10 ** 2)]); T9 = A["T9"]; best = (math.inf, None)
    for (a, b, l) in m.SEAT:
        for k in (0.0, math.log(3)):
            X = np.concatenate([A["U"][:, a], A["Dn"][:, b], (A["E"][:, l, 0] + k)[:, None], (A["E"][:, l, 1] - k)[:, None], A["K"][:, a, b]], axis=1)
            c = (((X - T9) / s9) ** 2).sum(1); i = int(np.argmin(c))
            if c[i] < best[0]: best = (float(c[i]), dict(row=list(A["lab"][i]), readings=[m.RD[a], m.RD[b], m.RD[l]], lepton_factor=math.exp(k)))
    return dict(chi2_nine_min=best[0], ckm_sigma_from_data=bool(cs), **best[1])


def main():
    from multiprocessing import Pool
    nw = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else 1
    jobs = [(n, s) for n in check.ARCS for s in check.mod(n).SEEDS]
    with Pool(nw) as P:
        res = P.map(one, jobs)
    out = {"definition": "post hoc, labelled: chi2_six at B1720 compare.py's definition; fraction of the arc's own random six-targets whose minimum over the same rows and menu is at most the data's"}
    for n in check.ARCS:
        per = {str(s): r for nn, s, r in res if nn == n}
        out[n] = {"chi2_nine_seat": chi2_nine(check.mod(n))}
        for menu in MENUS:
            fr = [per[s][menu][1] for s in per]
            out[n][menu] = {"chi2_six_min": per[next(iter(per))][menu][0], "fraction_mean": float(np.mean(fr)), "fraction_max": float(np.max(fr)),
                            "per_seed": {s: per[s][menu][1] for s in per}}
        print(n, {menu: (round(out[n][menu]["chi2_six_min"], 2), round(out[n][menu]["fraction_mean"], 4), round(out[n][menu]["fraction_max"], 4)) for menu in MENUS},
              "chi2_nine(seat) %.1f" % out[n]["chi2_nine_seat"]["chi2_nine_min"])
    json.dump(out, open(pathlib.Path(__file__).with_name("calib_chi2.json"), "w"), indent=1)


if __name__ == "__main__":
    main()
