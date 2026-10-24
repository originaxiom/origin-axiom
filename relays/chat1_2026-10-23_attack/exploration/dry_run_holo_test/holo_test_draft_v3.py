#!/usr/bin/env python3
"""THE HOLOMORPHIC READING TEST (sealed by HOLO_TEST_RULE.md, committed and pushed before this script is committed;
this script is committed before its run on the test grid, its outputs before they are read).  Does one Higgs direction,
read S (holomorphically) in every sector - THE_NEXT_ATTACK's A1 - carry the nine on any of B1713's 266 lines, and is a
fit as good as the data's rare for random hierarchies through the same search?

Instrument: main's fibre frame (B1720's instrument at 3412bf09d, unchanged, through chat1's channel_store.py wrappers)
and B1736's closed form on stored channel weights; the search is one_higgs_search.py's (up_conj = False, n_extra = 4)
on sm_search's direction grid; PRECISION_BAR's chi2 with the pinned targets as in inverse_higgs.py; c = 3 on the leptons.

Modes, in this order:
  --c0       data-free: the A1 model against inverse_higgs.nine(h, h) on 1 000 directions at ten stored rows of
             TWO_HIGGS's grid (logs only); one_higgs_search's Standard-Model path against sm_search (logs); chi2_many
             against a direct computation (40 targets at two stored rows).
  --store    C1 at five points on lines of orders 1, 7, 9, 11 and 12, then the channel weights and the record's directions
             on the test grid and the
             mirror set (resumable chunks of 64 points in chunks_holo/, git-ignored).
  --c2       the power control: 36 rows (seed 1744), a planted direction each (12 near the null conic with |s| log-uniform
             in 1e-4 .. 1e-1, 12 near n or n-bar, 12 uniform), targets the A1 model's nine there plus Gaussian noise of
             the chi2's sigma; also the noiseless recovery on the same directions (a read-out).
  --scan     every row: the A1 nine on the direction grid once; the data's search (refinement) on it; on the calibration
             grid (every fourth direction of the grid) the minimum of the data's target and of every random target (300
             from main's generator, seed 1743; 1 200 lepton-tied, seed 1743); chunks of 200 rows in chunks_holo/,
             written atomically, resumable only with the same script; then holo_rows.json and holo_calib_gridmin.npz.
  --calib    for each target (the data's, the 300 and the 1 200) its single best test row on the 264 lines other than
             (2/5, 0) and (2/5, 3/5) by calibration-grid minimum, refined by the same search; random as good per target
             set, with the upper end of the exact two-sided 95% interval; holo_calib.json.
  --cells    H1, H1', H2, H2', H3, H3', H3'_BAR, H4, C3 and the read-outs from the committed outputs; holo_cells.json.
    python3 -B holo_test.py --c0 | --store [--workers 2] | --c2 | --scan [--workers 2] | --calib [--workers 2] | --cells"""
import contextlib, hashlib, importlib.util, io, json, math, os, random, sys, time, pathlib
from fractions import Fraction as Fr
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent


def _load(name, file):
    argv = sys.argv; sys.argv = ["x"]
    spec = importlib.util.spec_from_file_location(name, HERE / file); mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(mod)
    sys.argv = argv
    return mod


cs = _load("cs", "channel_store.py")
ih = _load("ih", "inverse_higgs.py")
oh = _load("oh", "one_higgs_search.py")
T9, SIG = ih.T9, ih.SIG
LINES = [(tag, Fr(a), Fr(b)) for (tag, a, b) in cs.tic.LINES]
DIRS = cs.DIRS
RE = [0.275, 0.775]
IM = [2.075, 2.375, 2.675, 2.975, 3.275]
RE_MIRROR = 0.725                                        # = 1 - 0.275, the ten alpha = 2/5 lines only (control C3)
LOOK_LINES = [(Fr(2, 5), Fr(0)), (Fr(2, 5), Fr(3, 5))]   # the reconnaissance's below-bar rows (H1', H2' leave them out)
CHUNK, ROWCHUNK = 64, 200
BAR9, BAR6 = 21.67, 16.75
K1, K2 = 300, 1200
CD = HERE / "chunks_holo"
SHA = hashlib.sha256((HERE / "holo_test.py").read_bytes()).hexdigest() if (HERE / "holo_test.py").exists() else None


def grid():
    pts = [(k, r, y) for k in range(len(LINES)) for r in RE for y in IM]
    a25 = [k for k, (_, a, _) in enumerate(LINES) if a == Fr(2, 5)]
    return pts + [(k, RE_MIRROR, y) for k in a25 for y in IM]


def r_masses(rng):
    tg = []
    for _s in range(3):
        while True:
            r2 = 10 ** rng.uniform(-3, -1); r1 = 10 ** rng.uniform(-6, -2.5)
            if r1 < r2:
                break
        tg += [r2, r1]
    return tg


def r_ckm(rng):
    while True:
        a, b, c = 10 ** rng.uniform(-1.5, -0.2), 10 ** rng.uniform(-2.5, -0.7), 10 ** rng.uniform(-3.5, -1.5)
        if c < b < a:
            return [a, b, c]


def random_targets(n):
    rng = random.Random(1743)
    return np.log(np.array([r_masses(rng) + r_ckm(rng) for _ in range(n)]))


RT = random_targets(K1)                                   # main's generator (the first 300 draws)
RT2 = random_targets(K2)                                  # the first 1 200 draws, leptons tied to their own down ratios
RT2[:, 4] = RT2[:, 2] + (T9[4] - T9[2])                   # m_mu/m_tau = 3.144 m_s/m_b, the data's factor
RT2[:, 5] = RT2[:, 3] + (T9[5] - T9[3])                   # m_e/m_tau = 0.2972 m_d/m_b
TALL = np.concatenate([T9[None], RT, RT2])                # column 0 is the data's target
SUB = 4                                                   # the calibration grid: every fourth direction of the grid


# ---------------------------------------------------------------- C0
def c0():
    U = np.load(HERE / "channel_store_two_higgs.npz")["U"]
    sms = _load("sms_c0", "sm_search.py")
    rng = np.random.default_rng(8); w_a1, w_sm = 0.0, 0.0
    for p in (0, 333, 777, 1111, 1279):
        for hr in range(2):
            Uh = U[p, :, hr]
            H = rng.normal(size=(100, 3)) + 1j * rng.normal(size=(100, 3)); H /= np.linalg.norm(H, axis=1)[:, None]
            La = oh.model_logs(Uh, H, False)[0]; Ls = oh.model_logs(Uh, H, True)[0]
            w_sm = max(w_sm, float(np.max(np.abs(Ls - sms.nine_batch(Uh, H, np.zeros(9), np.ones(9))[0]))))
            for n in range(100):
                L, _, _ = ih.nine(Uh, H[n], H[n])
                w_a1 = max(w_a1, float(np.max(np.abs(L - La[n]))))
    wc = 0.0
    for p in (5, 900):
        L = oh.grid_logs(U[p, :, 0], False)
        nk = min(40, len(RT))
        b, _ = oh.chi2_many(L, RT[:nk], SIG)
        d = np.array([np.min(np.sum(((L - RT[k]) / SIG) ** 2, axis=1)) for k in range(nk)])
        wc = max(wc, float(np.max(np.abs(b - d) / np.maximum(d, 1e-9))))
    out = {"C0a A1 model against inverse_higgs.nine(h, h): largest |delta ln| (1 000 directions, 10 rows)": w_a1,
           "C0b the Standard-Model path against sm_search: largest |delta ln|": w_sm,
           "C0c chi2_many against a direct computation: largest relative difference (40 targets, 2 rows)": wc,
           "C0 holds": bool(w_a1 < 1e-10 and w_sm < 1e-10 and wc < 1e-8)}
    (HERE / "holo_c0.json").write_text(json.dumps(out, indent=1) + "\n")
    print("C0 written")


# ---------------------------------------------------------------- the store
def store_point(task):
    k, re_t, im_t = task
    _, a, b = LINES[k]
    return cs.weights(re_t, im_t, float(a), float(b)), cs.directions(re_t, im_t)


def store(nw):
    tasks = grid()
    worst = 0.0
    for task in [tasks[10 * k] for k in (0, 40, 100, 180, 260)]:   # five lines of different orders
        k, re_t, im_t = task; _, a, b = LINES[k]
        U, H = store_point(task)
        M = cs.rbs.channels(re_t, im_t, float(a), float(b))
        for d in ("F_6", "dR"):
            h = H[DIRS.index(d)]
            for i_s, sec in enumerate(cs.SECTORS):
                for i_h, hor in enumerate(cs.HORS):
                    Yc = cs.P_BLOCK @ cs.closed(U[i_s, i_h], h) @ cs.P_BLOCK.T
                    Yb = cs.B.coupling(cs.rbs.S_of(h), M[(sec, hor)])
                    worst = max(worst, float(np.max(np.abs(Yc - Yb)) / np.max(np.abs(Yb))))
    ctl = {"C1 largest relative |closed - coupling| at five points on lines 0, 40, 100, 180, 260 (F_6 and dR, every sector and horocycle)": worst,
           "C1 holds": worst < 1e-12}
    (HERE / "holo_c1.json").write_text(json.dumps(ctl, indent=1) + "\n")
    if not ctl["C1 holds"]:
        raise SystemExit("C1 fails: the store is not written")
    CD.mkdir(exist_ok=True)
    from multiprocessing import Pool
    t0 = time.time(); nch = (len(tasks) + CHUNK - 1) // CHUNK
    with Pool(nw) as P:
        for c in range(nch):
            f = CD / f"store_{c:04d}.npz"
            if f.exists():
                continue
            res = P.map(store_point, tasks[c * CHUNK:(c + 1) * CHUNK])
            np.savez(f, U=np.array([r[0] for r in res]), H=np.array([r[1] for r in res]))
            print(f"store chunk {c + 1}/{nch} ({time.time() - t0:.0f} s)", flush=True)
    U = np.concatenate([np.load(CD / f"store_{c:04d}.npz")["U"] for c in range(nch)])
    H = np.concatenate([np.load(CD / f"store_{c:04d}.npz")["H"] for c in range(nch)])
    np.savez_compressed(HERE / "holo_store.npz", U=U, H=H)
    (HERE / "holo_store_index.json").write_text(json.dumps({"tasks": tasks, "lines": [[t, str(a), str(b)] for t, a, b in LINES],
                                                           "sectors": cs.SECTORS, "hors": cs.HORS, "dirs": DIRS}) + "\n")
    print(f"store written ({time.time() - t0:.0f} s)")


G = {}


def _init():
    st = np.load(HERE / "holo_store.npz"); G["U"], G["H"] = st["U"], st["H"]


def n_main():
    return len(LINES) * len(RE) * len(IM)


# ---------------------------------------------------------------- C2
def c2():
    _init()
    rng = np.random.default_rng(1744)
    out = []
    t0 = time.time()
    for n in range(36):
        p = int(rng.integers(0, n_main())); hr = int(rng.integers(0, 2))
        Uh = G["U"][p, :, hr]
        if n < 12:
            kind = "near the conic"
            t = complex(*rng.normal(size=2)); r = 10 ** rng.uniform(-4, -1); ph = rng.uniform(0, 2 * math.pi)
            h0 = np.array([2 * t, 1 - t * t, 1j * (1 + t * t)]); h0 /= np.linalg.norm(h0)
            hp = h0 + r * np.exp(1j * ph) * np.conj(h0)
        elif n < 24:
            kind = "near n" if n < 18 else "near n-bar"
            lead, other = (oh.F3, oh.F1) if n < 18 else (oh.F1, oh.F3)
            de = 0.25 * math.sqrt(rng.uniform()) * np.exp(2j * math.pi * rng.uniform())
            ep = 0.03 * math.sqrt(rng.uniform()) * np.exp(2j * math.pi * rng.uniform())
            hp = lead + de * oh.F2 + ep * other
        else:
            kind = "uniform"
            z = rng.normal(size=6); hp = z[:3] + 1j * z[3:]
        hp = hp / np.linalg.norm(hp)
        T0 = oh.nine_batch(Uh, hp[None], T9, SIG, False)[0][0]
        Tp = T0 + rng.normal(size=9) * SIG
        cp = float(oh.nine_batch(Uh, hp[None], Tp, SIG, False)[1][0])
        _, (chi, _) = oh.search(Uh, G["H"][p], Tp, SIG, False, n_extra=4)
        _, (chi0, _) = oh.search(Uh, G["H"][p], T0, SIG, False, n_extra=4)
        out.append({"p": p, "hor": cs.HORS[hr], "kind": kind, "|h.h| planted": float(abs(hp @ hp)),
                    "planted direction's chi2 (noisy targets)": cp, "found (noisy)": chi, "met": bool(chi <= cp + 1e-9),
                    "found (noiseless)": chi0})
    ok = sum(o["met"] for o in out)
    res = {"C2 rows": out, "C2 met (the search's minimum at or below the planted direction's chi2)": ok, "C2 holds": ok >= 34,
           "read-out: noiseless recovered to chi2 <= 0.1, <= 2.167": [sum(o["found (noiseless)"] <= 0.1 for o in out),
                                                                      sum(o["found (noiseless)"] <= 2.167 for o in out)],
           "seconds per planted row (both searches)": (time.time() - t0) / 36}
    (HERE / "holo_c2.json").write_text(json.dumps(res, indent=1) + "\n")
    print("C2 written")


# ---------------------------------------------------------------- the scan
def scan_row(job):
    p, hr = job
    Uh = G["U"][p, :, hr]
    if any(np.allclose(Uh[s], 0) for s in range(3)):
        return {"p": p, "hor": cs.HORS[hr], "degenerate": True}, np.full(len(TALL), np.nan, dtype=np.float32)
    L = oh.grid_logs(Uh, False)
    chis = np.sum(((L - T9) / SIG) ** 2, axis=1)
    gmin, (chi, x) = oh.search(Uh, G["H"][p], T9, SIG, False, n_extra=4, chis=chis)
    h = oh.vec(x)
    Lh, c9, V = oh.nine_batch(Uh, h[None], T9, SIG, False)
    rb, _ = oh.chi2_many(L[::SUB], TALL, SIG)
    Vc = V[0]
    c = [np.vdot(oh.F2, h), np.vdot(oh.F3, h), np.vdot(oh.F1, h)]
    row = {"p": p, "hor": cs.HORS[hr], "degenerate": False, "grid min chi2_nine": gmin, "chi2_nine": float(c9[0]),
           "chi2_six there": float(np.sum(((Lh[0, :6] - T9[:6]) / SIG[:6]) ** 2)),
           "chi2 CKM share there": float(np.sum(((Lh[0, 6:] - T9[6:]) / SIG[6:]) ** 2)),
           "model/data": [float(q) for q in np.exp(Lh[0] - T9)], "|V|": Vc.round(6).tolist(),
           "D": float(math.exp((Lh[0, 4] - Lh[0, 2]) + (Lh[0, 3] - Lh[0, 5]))), "|h.h|": float(abs(h @ h)),
           "|e1|, |n|, |n-bar|": [float(abs(q)) for q in c], "h": [[float(q.real), float(q.imag)] for q in h]}
    return row, rb.astype(np.float32)


def scan(nw):
    tasks = json.loads((HERE / "holo_store_index.json").read_text())["tasks"]
    jobs = [(p, hr) for p in range(len(tasks)) for hr in range(2)]
    CD.mkdir(exist_ok=True)
    man = CD / "manifest.json"
    if man.exists():
        assert json.loads(man.read_text())["sha256"] == SHA, "chunks from another script: clear chunks_holo/ first"
    else:
        man.write_text(json.dumps({"sha256": SHA}) + "\n")
    from multiprocessing import Pool
    t0 = time.time(); nch = (len(jobs) + ROWCHUNK - 1) // ROWCHUNK
    with Pool(nw, initializer=_init) as P:
        for c in range(nch):
            f = CD / f"rows_{c:04d}.json"
            if f.exists():
                continue
            res = P.map(scan_row, jobs[c * ROWCHUNK:(c + 1) * ROWCHUNK], chunksize=4)
            np.save(CD / f"tmp_cal_{c:04d}.npy", np.array([r[1] for r in res])); os.replace(CD / f"tmp_cal_{c:04d}.npy", CD / f"cal_{c:04d}.npy")
            (CD / f"tmp_rows_{c:04d}.json").write_text(json.dumps([r[0] for r in res]) + "\n"); os.replace(CD / f"tmp_rows_{c:04d}.json", f)
            print(f"row chunk {c + 1}/{nch} ({time.time() - t0:.0f} s)", flush=True)
    rows = sum((json.loads((CD / f"rows_{c:04d}.json").read_text()) for c in range(nch)), [])
    R = np.concatenate([np.load(CD / f"cal_{c:04d}.npy") for c in range(nch)])
    assert [(r["p"], cs.HORS.index(r["hor"])) for r in rows] == jobs and R.shape == (len(jobs), len(TALL))
    (HERE / "holo_rows.json").write_text(json.dumps({"tasks": tasks, "rows": rows}) + "\n")
    np.savez_compressed(HERE / "holo_calib_gridmin.npz", gridmin=R)
    print(f"rows written ({time.time() - t0:.0f} s)")


# ---------------------------------------------------------------- the calibration
def calib_job(job):
    p, hr, k = job
    Uh = G["U"][p, :, hr]
    _, (chi, _) = oh.search(Uh, G["H"][p], TALL[k], SIG, False, n_extra=4)
    return chi


def cp_upper(k, n):
    """The upper end of the exact (Clopper-Pearson) two-sided 95% interval for k hits in n (as THE_BAR reads it)."""
    from scipy.stats import beta
    return 1.0 if k >= n else float(beta.ppf(0.975, k + 1, n - k))


def calib(nw):
    d = json.loads((HERE / "holo_rows.json").read_text()); tasks, rows = d["tasks"], d["rows"]
    R = np.load(HERE / "holo_calib_gridmin.npz")["gridmin"].astype(np.float64)
    assert R.shape == (len(rows), len(TALL))
    LN = [(Fr(a), Fr(b)) for _t, a, b in json.loads((HERE / "holo_store_index.json").read_text())["lines"]]
    ok = [i for i, r in enumerate(rows) if tasks[r["p"]][1] != RE_MIRROR and not r.get("degenerate")
          and LN[tasks[r["p"]][0]] not in LOOK_LINES and np.all(np.isfinite(R[i]))]
    jobs = []
    for k in range(len(TALL)):
        i = ok[int(np.argmin(R[ok, k]))]
        jobs.append((rows[i]["p"], cs.HORS.index(rows[i]["hor"]), k))
    from multiprocessing import Pool
    t0 = time.time()
    with Pool(nw, initializer=_init) as P:
        stat = np.array(P.map(calib_job, jobs, chunksize=2))
    data = float(stat[0]); s1, s2 = stat[1:1 + K1], stat[1 + K1:]
    h1, h2 = int(np.sum(s1 <= data)), int(np.sum(s2 <= data))
    out = {"the data's statistic (its best test row on the 264 lines by calibration-grid minimum, refined)": data,
           "the data's row": {"p": jobs[0][0], "hor": cs.HORS[jobs[0][1]]},
           "main's generator (300): hits at or below the data's, fraction, upper end of the exact 95% interval": [h1, h1 / K1, cp_upper(h1, K1)],
           "lepton-tied (1 200): hits at or below the data's, fraction, upper end of the exact 95% interval": [h2, h2 / K2, cp_upper(h2, K2)],
           "THE_BAR: 3 x the lepton-tied upper end": 3 * cp_upper(h2, K2),
           "statistics, main's generator": s1.tolist(), "statistics, lepton-tied": s2.tolist(),
           "grid level: the data's best calibration-grid minimum": float(R[ok, 0].min()),
           "grid level: fraction of main's generator, of lepton-tied at or below it": [float(np.mean(R[ok, 1:1 + K1].min(axis=0) <= R[ok, 0].min())),
                                                                                    float(np.mean(R[ok, 1 + K1:].min(axis=0) <= R[ok, 0].min()))],
           "seconds": time.time() - t0}
    (HERE / "holo_calib.json").write_text(json.dumps(out, indent=1, default=float) + "\n")
    print("calibration written")


# ---------------------------------------------------------------- the cells
def cells():
    d = json.loads((HERE / "holo_rows.json").read_text()); tasks, rows = d["tasks"], d["rows"]
    lines = [(t, Fr(a), Fr(b)) for t, a, b in json.loads((HERE / "holo_store_index.json").read_text())["lines"]]
    cal = json.loads((HERE / "holo_calib.json").read_text())
    deg = [r for r in rows if r.get("degenerate")]
    good = [r for r in rows if not r.get("degenerate") and np.isfinite(r["chi2_nine"])]
    main = [r for r in good if tasks[r["p"]][1] != RE_MIRROR]; mir = [r for r in good if tasks[r["p"]][1] == RE_MIRROR]
    away = [r for r in main if (lines[tasks[r["p"]][0]][1], lines[tasks[r["p"]][0]][2]) not in LOOK_LINES]

    def lab(r):
        k = tasks[r["p"]][0]
        return {"line": f"({lines[k][1]}, {lines[k][2]})", "order": lines[k][0], "tau": tasks[r["p"]][1:], "hor": r["hor"]}

    def below_both(rs):
        return [r for r in rs if r["chi2_nine"] < BAR9 and r["chi2_six there"] < BAR6]
    chis = np.array([r["chi2_nine"] for r in main]); chis_away = np.array([r["chi2_nine"] for r in away])
    both = below_both(main)
    h1row = min(main, key=lambda r: r["chi2_nine"])
    grank = 1 + sum(r["grid min chi2_nine"] < h1row["grid min chi2_nine"] for r in main)
    m1, m2 = cal["main's generator (300): hits at or below the data's, fraction, upper end of the exact 95% interval"], cal["lepton-tied (1 200): hits at or below the data's, fraction, upper end of the exact 95% interval"]
    drow = cal["the data's row"]; drow_r = next(r for r in away if r["p"] == drow["p"] and r["hor"] == drow["hor"])
    out = {"rows": len(main), "degenerate rows": [lab(r) for r in deg],
           "H1 some test row below 21.67": bool(chis.min() < BAR9),
           "H1' the same on the 264 lines other than (2/5, 0) and (2/5, 3/5)": bool(chis_away.min() < BAR9),
           "H2 some test row's optimum below both bars": bool(len(both) > 0),
           "H2' the same on the 264 lines": bool(len(below_both(away)) > 0),
           "H3 main's generator: fewer than 1% at or below the data's statistic (at most 2 of 300)": bool(m1[0] <= 2),
           "H3' lepton-tied: fewer than 1% (at most 11 of 1 200)": bool(m2[0] <= 11),
           "H3'_BAR 3 x the upper end of the lepton-tied exact 95% interval below 1%": bool(cal["THE_BAR: 3 x the lepton-tied upper end"] < 0.01),
           "H4 some row below both bars with D within 10.58 +- 0.33": bool(any(abs(r["D"] - 10.58) <= 0.33 for r in both)),
           "the calibration (hits, fraction, bound): main's generator, lepton-tied": [m1, m2],
           "the data's calibration statistic and its row's chi2_six; below both bars?": [cal["the data's statistic (its best test row on the 264 lines by calibration-grid minimum, refined)"],
                                                                                         drow_r["chi2_six there"],
                                                                                         bool(cal["the data's statistic (its best test row on the 264 lines by calibration-grid minimum, refined)"] < BAR9 and drow_r["chi2_six there"] < BAR6)],
           "H1's row: its rank by grid minimum among the test rows": grank,
           "lowest chi2_nine; on the 264 lines": [float(chis.min()), float(chis_away.min())],
           "quantiles 1%, 5%, 50%": [float(np.quantile(chis, q)) for q in (0.01, 0.05, 0.5)],
           "rows below 21.67, 50, 100": [int((chis < c).sum()) for c in (BAR9, 50, 100)],
           "every row below 21.67": [{**lab(r), "chi2_nine": r["chi2_nine"], "chi2_six there": r["chi2_six there"],
                                      "model/data": [round(q, 3) for q in r["model/data"]], "D": r["D"]}
                                     for r in sorted(main, key=lambda r: r["chi2_nine"]) if r["chi2_nine"] < BAR9],
           "D at the rows below both bars": [round(r["D"], 3) for r in both],
           "rows with chi2_nine above 1e7 (outputs identically zero on their line)": len([r for r in main if r["chi2_nine"] > 1e7])}
    by = {}
    for r in main:
        by.setdefault(lines[tasks[r["p"]][0]][0], []).append(r["chi2_nine"])
    out["lowest chi2_nine by order"] = {o: float(min(v)) for o, v in sorted(by.items(), key=lambda kv: int(kv[0][2:]))}
    out["the twenty lowest rows"] = [{**lab(r), "chi2_nine": r["chi2_nine"], "chi2_six there": r["chi2_six there"],
                                      "model/data": [round(q, 3) for q in r["model/data"]], "|V|": r["|V|"], "D": r["D"],
                                      "|h.h|": r["|h.h|"], "|e1|, |n|, |n-bar|": r["|e1|, |n|, |n-bar|"]}
                                     for r in sorted(main, key=lambda r: r["chi2_nine"])[:20]]
    idx = {(t[0], round(t[1], 6), round(t[2], 6)): i for i, t in enumerate(tasks)}
    rmap = {(r["p"], r["hor"]): r["chi2_nine"] for r in good}
    agree, bad_low, pairs = 0, 0, 0
    for r in mir:
        k, re_t, im_t = tasks[r["p"]]; _, a, b = lines[k]
        km = next(i for i, l in enumerate(lines) if l[1] == a and l[2] == (Fr(3, 5) - b) % 1)
        q = idx[(km, round(1 - re_t, 6), round(im_t, 6))]
        if (q, r["hor"]) not in rmap:
            continue
        x1, x2 = r["chi2_nine"], rmap[(q, r["hor"])]
        ok = abs(x1 - x2) <= 0.01 * min(x1, x2)
        pairs += 1; agree += ok; bad_low += (not ok) and min(x1, x2) < BAR9
    out["C3 mirror pairs agreeing within 1%"] = [agree, pairs]
    out["C3 pairs below 21.67 that disagree"] = bad_low
    out["C3 holds"] = bool(pairs == 100 and agree >= 90 and bad_low == 0)
    (HERE / "holo_cells.json").write_text(json.dumps(out, indent=1, default=float) + "\n")
    print("cells written")


if __name__ == "__main__":
    nw = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else 2
    if "--c0" in sys.argv:
        c0()
    elif "--store" in sys.argv:
        store(nw)
    elif "--c2" in sys.argv:
        c2()
    elif "--scan" in sys.argv:
        scan(nw)
    elif "--calib" in sys.argv:
        calib(nw)
    elif "--cells" in sys.argv:
        cells()
