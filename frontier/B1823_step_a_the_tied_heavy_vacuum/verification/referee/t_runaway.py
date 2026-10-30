"""Is the reported interior vacuum the GLOBAL minimum?  For the 24 configurations whose interior V lies above the cusp's
asymptotic lower bound n (2 F(0) + F(u*)) (t_cusp_bound.json), and a control sample of others, search again with starts
spread over Im tau in [0.9, 16] (the draft's starts stop at 3.5), using the draft's own Model and local_min (copied in
rerun/).  A point below the reported V (any Im tau) means the reported 'vacuum' is not the global minimum.
    python3 -I t_runaway.py [--workers 3]  -> t_runaway.json"""
import sys, pathlib, json, time
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / "rerun"))
import numpy as np


def job(args):
    import numpy as np
    from search import Model, make_copies, local_min
    menu, n, mu2, m02, lv, tnorm, snorm, Vrep, seed, nstart = args
    model = Model(make_copies(n, menu, tnorm, snorm), mu2, m02, lv)
    rng = np.random.default_rng(seed)
    found = []
    t0 = time.time()
    for k in range(nstart):
        x = rng.uniform(-0.5, 0.5)
        y = float(np.exp(rng.uniform(np.log(0.9), np.log(16.0))))
        y = max(y, np.sqrt(1 - x * x) + 1e-3)
        S = rng.normal(size=3) + 1j * rng.normal(size=3)
        try:
            tau, Sf, v, r = local_min(model, complex(x, y), S)
            if np.isfinite(v) and v < 1e29:
                found.append((float(v), tau.real, tau.imag))
        except Exception:
            pass
    found.sort()
    best = found[0] if found else None
    below = [f for f in found if f[0] < Vrep - 1e-9 * (1 + abs(Vrep))]
    return dict(menu=menu, n=n, mu2=mu2, m02=m02, lv=lv, tnorm=tnorm, V_reported=Vrep, n_starts=nstart,
                best=best, n_below_reported=len(below), lowest_below=(below[0] if below else None),
                lowest_5=found[:5], seconds=round(time.time() - t0, 1))


if __name__ == "__main__":
    workers = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else 1
    cb = json.loads((HERE / "t_cusp_bound.json").read_text())
    D = json.loads((HERE.parent / "step_a_v2.json").read_text())["D"]["configs"]
    flagged = {(x["menu"], x["tnorm"], x["n"], x["mu2"], x["m02"], x["lv"]) for x in cb["not_below"]}
    jobs = []; seed = 4242
    for r in D:
        if "best" not in r:
            continue
        key = (r["menu"], r["tnorm"], r["n"], r["mu2"], r["m02"], r["lv"])
        control = (r["tnorm"] == "N" and r["lv"] == 0.3 and r["mu2"] == 0.5 and r["m02"] == 0.005)
        if key in flagged or control:
            seed += 1
            jobs.append((r["menu"], r["n"], r["mu2"], r["m02"], r["lv"], r["tnorm"], r["snorm"], r["best"]["V"], seed, 48))
    print("jobs", len(jobs), flush=True)
    res = []
    if workers > 1:
        import multiprocessing as mpr
        with mpr.get_context("spawn").Pool(workers) as pool:
            for out in pool.imap_unordered(job, jobs):
                res.append(out)
                print(json.dumps({k: out[k] for k in ("menu", "tnorm", "n", "mu2", "lv", "V_reported", "best", "n_below_reported", "seconds")}), flush=True)
    else:
        for j in jobs:
            out = job(j); res.append(out)
            print(json.dumps({k: out[k] for k in ("menu", "tnorm", "n", "mu2", "lv", "V_reported", "best", "n_below_reported", "seconds")}), flush=True)
    res.sort(key=lambda r: (r["menu"], r["tnorm"], r["n"], r["mu2"], r["lv"]))
    (HERE / "t_runaway.json").write_text(json.dumps(dict(rows=res, n_jobs=len(res),
                                                         n_reported_not_global=sum(1 for r in res if r["n_below_reported"] > 0)), indent=1))
    print("reported vacua undercut:", sum(1 for r in res if r["n_below_reported"] > 0), "of", len(res))
