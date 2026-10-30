"""The global-minimum re-search, redone with a cancellation-free F (the draft's double-precision F(u) returns exactly 0 for
u >~ 1e14 m0^2-scale masses -- u + m0^2 rounds to u -- instead of ~2 m0^2 u log u > 0; t_probe_cusp.py, and the table in
the report).  F(u) = (2 u m0^2 + m0^4)(log(u/mu^2) - 3/2) + (u + m0^2)^2 log1p(m0^2/u), algebraically identical.
For every configuration the draft or t_runaway.py flagged, and controls: (a) the draft's own 24 seeded starts (its seeds)
with the stable F; (b) 48 starts over Im tau in [0.9, 16]; the best point of each is then re-evaluated in mpmath at 30
digits with the referee's independent forms (ref_model.py) -- the arbiter.  -> t_runaway_stable.json"""
import sys, pathlib, json, time
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE)); sys.path.insert(1, str(HERE / "rerun"))
import numpy as np


def stable_F(u, mu2, m02):
    if u <= 0:
        return m02 ** 2 * (np.log(m02 / mu2) - 1.5)
    return (2 * u * m02 + m02 ** 2) * (np.log(u / mu2) - 1.5) + (u + m02) ** 2 * np.log1p(m02 / u)


def job(args):
    import numpy as np
    import model as M, search as Sr
    M.Ffun = stable_F; Sr.Ffun = stable_F                       # patch the draft's F everywhere it is looked up
    from search import Model, make_copies, local_min
    menu, n, mu2, m02, lv, tnorm, snorm, Vrep, seed_draft, seed_wide = args
    model = Model(make_copies(n, menu, tnorm, snorm), mu2, m02, lv)
    out = dict(menu=menu, n=n, mu2=mu2, m02=m02, lv=lv, tnorm=tnorm, V_reported=Vrep)
    t0 = time.time()
    for label, seed, nst, ymax, logy in (("draft_starts", seed_draft, 24, 3.5, False), ("wide_starts", seed_wide, 48, 16.0, True)):
        rng = np.random.default_rng(seed); found = []
        for _ in range(nst):
            x = rng.uniform(-0.5, 0.5)
            if logy:
                y = max(float(np.exp(rng.uniform(np.log(0.9), np.log(ymax)))), np.sqrt(1 - x * x) + 1e-3)
            else:
                y = rng.uniform(np.sqrt(1 - x * x), ymax)
            S = rng.normal(size=3) + 1j * rng.normal(size=3)
            try:
                tau, Sf, v, r = local_min(model, complex(x, y), S)
                if np.isfinite(v) and v < 1e29:
                    found.append((float(v), tau, Sf))
            except Exception:
                pass
        found.sort(key=lambda t: t[0])
        b = found[0] if found else None
        out[label] = dict(best_V=(b[0] if b else None), best_tau=([b[1].real, b[1].imag] if b else None),
                          best_S=([[c.real, c.imag] for c in b[2]] if b else None),
                          n_below_reported=sum(1 for f in found if f[0] < Vrep - 1e-9 * (1 + abs(Vrep))),
                          lowest_5=[[f[0], f[1].real, f[1].imag] for f in found[:5]])
    out["seconds"] = round(time.time() - t0, 1)
    return out


if __name__ == "__main__":
    workers = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else 1
    D = json.loads((HERE.parent / "step_a_v2.json").read_text())["D"]["configs"]
    first = json.loads((HERE / "t_runaway.json").read_text())["rows"]
    flagged = {(r["menu"], r["tnorm"], r["n"], r["mu2"], r["m02"], r["lv"]) for r in first}
    # the draft's own seeds (step_a_v2.grid_D order)
    seed = 100; seeds = {}
    for menu in ("Z", "H"):
        for n in range(1, 9):
            for mu2 in (0.3, 0.5, 0.8):
                for lv in (0.1, 0.3, 1.0):
                    seed += 1; seeds[(menu, "N", n, mu2, round(0.01 * mu2, 10), lv)] = seed
            seed += 1; seeds[(menu, "N", n, 0.5, 0.05, 0.3)] = seed
            seed += 1; seeds[(menu, "cusp", n, 0.5, 0.005, 0.3)] = seed
    jobs = []; s2 = 777
    for r in D:
        key = (r["menu"], r["tnorm"], r["n"], r["mu2"], r["m02"], r["lv"])
        kk = (r["menu"], r["tnorm"], r["n"], r["mu2"], round(r["m02"], 10), r["lv"])
        if key in flagged or "runaway" in r:
            Vrep = r["best"]["V"] if "best" in r else r["runaway"]["V"]
            s2 += 1; jobs.append((r["menu"], r["n"], r["mu2"], r["m02"], r["lv"], r["tnorm"], r["snorm"], Vrep, seeds[kk], s2))
    print("jobs", len(jobs), flush=True)
    res = []
    import multiprocessing as mpr
    with mpr.get_context("spawn").Pool(workers) as pool:
        for o in pool.imap_unordered(job, jobs):
            res.append(o)
            print(json.dumps({k: (o[k] if not isinstance(o[k], dict) else {kk: o[k][kk] for kk in ("best_V", "best_tau", "n_below_reported")})
                              for k in ("menu", "tnorm", "n", "mu2", "lv", "V_reported", "draft_starts", "wide_starts", "seconds")}), flush=True)
    # the arbiter: mpmath, independent forms, at the best point found (either start set)
    import mpmath as mp
    import ref_model as rm
    from ref_helpers import draft_norms
    mp.mp.dps = 30
    for o in res:
        best = min((o[k] for k in ("draft_starts", "wide_starts") if o[k]["best_V"] is not None), key=lambda d: d["best_V"])
        sc, tc = draft_norms(o["menu"], o["n"], o["tnorm"], "sup" if o["tnorm"] == "N" else "cusp")
        m = rm.RefModel(o["menu"], o["n"], o["mu2"], o["m02"], o["lv"], sc, tc)
        tau = mp.mpc(*best["best_tau"]); S = [mp.mpc(*c) for c in best["best_S"]]
        Vmp = m.V(tau, S)
        o["arbiter_mpmath_V_at_best"] = float(Vmp)
        o["arbiter_best_tau"] = best["best_tau"]
        o["undercut_confirmed_in_mpmath"] = bool(Vmp < o["V_reported"] - 1e-9 * (1 + abs(o["V_reported"])))
        print("ARBITER %s %s n=%d mu2=%.1f lv=%.1f: V_reported %.6g | best found %.6g at Im tau %.2f | mpmath there %.6g | undercut %s" % (
            o["menu"], o["tnorm"], o["n"], o["mu2"], o["lv"], o["V_reported"], best["best_V"], best["best_tau"][1], float(Vmp),
            o["undercut_confirmed_in_mpmath"]), flush=True)
    res.sort(key=lambda r: (r["menu"], r["tnorm"], r["n"], r["mu2"], r["lv"]))
    (HERE / "t_runaway_stable.json").write_text(json.dumps(dict(rows=res), indent=1))
