#!/usr/bin/env python3
"""READING TEST, POST HOC (labelled; written after the cells were read, committed before its run, its output committed
before it is read).  Two checks of the sealed search's reach on the reading test's own store:
  P1  the two planted rows of C2 the search missed (rows 5 and 27 of reading_test_c2.json, regenerated from seed 1741):
      a denser search (t on 1 600 Fibonacci points, |s| as before, 32 phases, 16 000 random directions; refinement from
      the best eight grid directions and all 26 record starts) against the same noisy and noiseless targets.
  P2  the same denser search with the pinned targets on the 40 lowest rows of the scan and 40 further rows (seed 2024):
      its minimum against the scan's.
    python3 -B reading_test_posthoc.py [--workers 2]      # writes reading_test_posthoc.json"""
import contextlib, importlib.util, io, json, math, sys, time, pathlib
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
argv = sys.argv; sys.argv = ["x"]
spec = importlib.util.spec_from_file_location("rt", HERE / "reading_test.py"); rt = importlib.util.module_from_spec(spec)
sys.modules["rt"] = rt
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(rt)
sys.argv = argv
sms, T9, SIG = rt.sms, rt.T9, rt.SIG
HD = sms.tube(nt=1600, nr=17, nphi=32, nrand=16000, seed=2611)
G = {}


def _init():
    st = np.load(HERE / "reading_test_store.npz"); G["U"], G["H"] = st["U"], st["H"]


def dense(job):
    p, hr, T = job
    Uh = G["U"][p, :, hr]
    g, (c, x) = sms.search(Uh, G["H"][p], np.array(T), SIG, H=HD, n_extra=None)
    return {"p": p, "hr": hr, "dense grid min": g, "dense min": c}


def planted(n_want):
    """Regenerate C2's planted rows (same draws as reading_test.c2) and return those with indices in n_want."""
    n_main = len(rt.LINES) * len(rt.RE) * len(rt.IM)
    rng = np.random.default_rng(1741); out = {}
    for n in range(36):
        p = int(rng.integers(0, n_main)); hr = int(rng.integers(0, 2))
        Uh = G["U"][p, :, hr]
        while True:
            if n < 12:
                t = complex(*rng.normal(size=2)); r = 10 ** rng.uniform(math.log10(5.56e-4), -1); ph = rng.uniform(0, 2 * math.pi)
                h0 = np.array([2 * t, 1 - t * t, 1j * (1 + t * t)]); h0 /= np.linalg.norm(h0)
                hp = h0 + r * np.exp(1j * ph) * np.conj(h0)
            elif n < 24:
                lead, other = (sms.F3, sms.F1) if n < 18 else (sms.F1, sms.F3)
                de = 0.25 * math.sqrt(rng.uniform()) * np.exp(2j * math.pi * rng.uniform())
                ep = 0.03 * math.sqrt(rng.uniform()) * np.exp(2j * math.pi * rng.uniform())
                hp = lead + de * sms.F2 + ep * other
            else:
                z = rng.normal(size=6); hp = z[:3] + 1j * z[3:]
            hp = hp / np.linalg.norm(hp)
            if abs(hp @ hp) >= rt.HH_TUBE:
                break
        T0 = sms.nine_batch(Uh, hp[None], T9, SIG)[0][0]
        Tp = T0 + rng.normal(size=9) * SIG
        if n in n_want:
            out[n] = (p, hr, T0, Tp, float(sms.nine_batch(Uh, hp[None], Tp, SIG)[1][0]))
    return out


if __name__ == "__main__":
    from multiprocessing import Pool
    nw = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else 2
    _init()
    t0 = time.time()
    pl = planted({5, 27})
    d = json.loads((HERE / "reading_test_rows.json").read_text()); tasks, rows = d["tasks"], d["rows"]
    main = [r for r in rows if tasks[r["p"]][1] != rt.RE_MIRROR]
    low = sorted(main, key=lambda r: r["chi2_nine"])[:40]
    rng = np.random.default_rng(2024); rest = [r for r in main if r not in low]
    pick = low + [rest[i] for i in rng.choice(len(rest), 40, replace=False)]
    jobs = []
    for n, (p, hr, T0, Tp, cp) in sorted(pl.items()):
        jobs += [(p, hr, Tp.tolist()), (p, hr, T0.tolist())]
    jobs += [(r["p"], rt.cs.HORS.index(r["hor"]), T9.tolist()) for r in pick]
    with Pool(nw, initializer=_init) as P:
        res = P.map(dense, jobs, chunksize=1)
    out = {"P1 the two missed planted rows": [], "P2 rows": []}
    for i, (n, (p, hr, T0, Tp, cp)) in enumerate(sorted(pl.items())):
        out["P1 the two missed planted rows"].append({"C2 index": n, "p": p, "hor": rt.cs.HORS[hr], "planted direction's chi2 (noisy)": cp,
                                                       "dense min (noisy)": res[2 * i]["dense min"], "dense min (noiseless)": res[2 * i + 1]["dense min"]})
    for r, q in zip(pick, res[4:]):
        out["P2 rows"].append({"p": r["p"], "hor": r["hor"], "scan min": r["chi2_nine"], "dense min": q["dense min"],
                               "dense grid min": q["dense grid min"], "in the 40 lowest": r in low})
    rel = [(q["dense min"] - q["scan min"]) / q["scan min"] for q in out["P2 rows"]]
    out["P2 relative change of the minimum (dense - scan) / scan: min, median, max"] = [float(min(rel)), float(np.median(rel)), float(max(rel))]
    out["P2 lowest dense minimum"] = float(min(q["dense min"] for q in out["P2 rows"]))
    out["seconds"] = time.time() - t0
    (HERE / "reading_test_posthoc.json").write_text(json.dumps(out, indent=1, default=float) + "\n")
    print("written")
