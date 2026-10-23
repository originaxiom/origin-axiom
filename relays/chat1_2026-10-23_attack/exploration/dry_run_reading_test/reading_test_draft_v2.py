#!/usr/bin/env python3
"""THE READING TEST (sealed by READING_TEST_RULE.md, committed and pushed before this script is committed; this script
is committed before its run on the test grid, its outputs before they are read).  Can any Higgs direction let the
Standard Model's one-Higgs reading (up sees conj h, down and leptons see h, c = 3 on the leptons) carry the nine on any
of B1713's 266 lines?

Instrument: main's fibre frame (B1720's instrument at 3412bf09d, unchanged, through chat1's channel_store.py wrappers)
and B1736's closed form on the stored channel weights; the search is sm_search.py's at 4370b2e95 with n_extra = 4; the
objective is PRECISION_BAR's chi2_nine with the pinned targets, as in inverse_higgs.py.

Modes, in this order:
  --c0       data-free: Lemma A's identity (Y h = Y^T h = (h.h) u) symbolically; Lemma A' (the symmetric part's norm
             identity and |u| <= sqrt3 m3) on 20 000 random draws; sm_search's vectorised model against inverse_higgs.nine
             on 1 000 directions at ten stored rows of TWO_HIGGS's grid (logs only; no chi2 against the data).
  --store    C1 at the first five points, then the channel weights and the record's directions on the test grid and the
             mirror set (resumable chunks of 64 points in chunks_reading_test/, git-ignored).
  --c2       the power control: 36 rows of the grid (seed 1741), a planted direction each (12 near the conic outside
             Lemma A's tube, 12 near n or n-bar, 12 uniform), targets the model's nine there plus Gaussian noise of the
             chi2's sigma; also the noiseless recovery on the same directions (a read-out).
  --scan     every row: sm_search.search with the pinned targets; writes reading_test_rows.json; prints only counts.
  --cells    S1, S1', S4, S5, C3 and the read-outs from the committed rows; writes reading_test_cells.json.
    python3 -B reading_test.py --c0 | --store [--workers 2] | --c2 | --scan [--workers 2] | --cells"""
import contextlib, importlib.util, io, json, math, sys, time, pathlib
from fractions import Fraction as Fr
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent


def _load(name, file):
    argv = sys.argv; sys.argv = ["x"]
    spec = importlib.util.spec_from_file_location(name, HERE / file); mod = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(mod)
    sys.argv = argv
    return mod


cs = _load("cs", "channel_store.py")
ih = _load("ih", "inverse_higgs.py")
sms = _load("sms", "sm_search.py")
T9, SIG = ih.T9, ih.SIG
LINES = [(tag, Fr(a), Fr(b)) for (tag, a, b) in cs.tic.LINES]
DIRS = cs.DIRS
RE = [0.1146, 0.6354]
IM = [2.1146, 2.5271, 2.9396, 3.3521]
RE_MIRROR = 0.8854
CHUNK = 64
BAR9 = 21.67
VUD_MIN, VTB_MIN, HH_TUBE = 0.933519, 0.997723, 1.112e-3
RAND = sms.HS[-4000:]                                    # sm_search's 4 000 random directions (uniform on CP^2)


def grid():
    pts = [(k, r, y) for k in range(len(LINES)) for r in RE for y in IM]
    a25 = [k for k, (_, a, _) in enumerate(LINES) if a == Fr(2, 5)]
    return pts + [(k, RE_MIRROR, y) for k in a25 for y in IM]


def bounds(Uh, H):
    """Lemma A's |V_ud| bound and Lemma B's |V_tb| bound for unit directions H (N, 3) under the Standard Model's
    reading, from one SVD per sector; also |V| from the same SVDs."""
    Uu, su, _ = np.linalg.svd(sms.Ybatch(Uh[0], np.conj(H))); Ud, sd, _ = np.linalg.svd(sms.Ybatch(Uh[1], H))
    hh = np.abs(np.einsum("ni,ni->n", H, H))
    with np.errstate(divide="ignore", invalid="ignore"):
        xu = np.where(su[:, 1] > 0, hh * np.linalg.norm(Uh[0, 1:]) / su[:, 1], np.inf)
        xd = np.where(sd[:, 1] > 0, hh * np.linalg.norm(Uh[1, 1:]) / sd[:, 1], np.inf)
    arg = np.arccos(np.minimum(1.0, hh)) - np.arcsin(np.minimum(1.0, xu)) - np.arcsin(np.minimum(1.0, xd))
    ba = np.where(arg > 0, np.cos(np.clip(arg, 0, None)), 1.0)
    au = 0.5 * np.arccos(np.minimum(1.0, np.abs(np.einsum("ni,ni->n", Uu[:, :, 0], Uu[:, :, 0]))))
    ad = 0.5 * np.arccos(np.minimum(1.0, np.abs(np.einsum("ni,ni->n", Ud[:, :, 0], Ud[:, :, 0]))))
    bb = np.cos(au - ad)
    V = np.abs(np.einsum("nji,njk->nik", np.conj(Uu[:, :, ::-1]), Ud[:, :, ::-1]))
    return {"hh": hh, "xu": xu, "xd": xd, "A": ba, "au": au, "ad": ad, "B": bb, "V": V}


# ---------------------------------------------------------------- C0
def c0():
    import sympy as sp
    u1, u2, u3, h1, h2, h3, w = sp.symbols("u1 u2 u3 h1 h2 h3 w")
    u, h = sp.Matrix([u1, u2, u3]), sp.Matrix([h1, h2, h3])
    cr = sp.Matrix([[0, -h[2], h[1]], [h[2], 0, -h[0]], [-h[1], h[0], 0]])
    Y = u * h.T + h * u.T - (u.T * h)[0] * sp.eye(3) + w * cr
    hh = (h.T * h)[0]
    ok_a = sp.expand(Y * h - hh * u) == sp.zeros(3, 1) and sp.expand(Y.T * h - hh * u) == sp.zeros(3, 1)
    rng = np.random.default_rng(31); idw, mx = 0.0, 0.0
    for _ in range(20000):
        uu = rng.normal(size=3) + 1j * rng.normal(size=3); hv = rng.normal(size=3) + 1j * rng.normal(size=3); hv /= np.linalg.norm(hv)
        ww = complex(*rng.normal(size=2)) * rng.uniform(0, 3)
        Yn = cs.closed(np.concatenate([[ww], uu]), hv); S = (Yn + Yn.T) / 2
        lhs = np.linalg.norm(S) ** 2; rhs = 2 * np.linalg.norm(uu) ** 2 + 2 * abs(np.vdot(uu, hv)) ** 2 - abs(uu @ hv) ** 2
        idw = max(idw, abs(lhs - rhs) / lhs); mx = max(mx, np.linalg.norm(uu) / np.linalg.svd(Yn, compute_uv=False)[0])
    U = np.load(HERE / "channel_store_two_higgs.npz")["U"]
    rng = np.random.default_rng(7); worst = 0.0
    for p in (0, 333, 777, 1111, 1279):
        for hr in range(2):
            Uh = U[p, :, hr]
            H = rng.normal(size=(100, 3)) + 1j * rng.normal(size=(100, 3)); H /= np.linalg.norm(H, axis=1)[:, None]
            Lb = sms.nine_batch(Uh, H, np.zeros(9), np.ones(9))[0]
            for n in range(100):
                L, _, _ = ih.nine(Uh, np.conj(H[n]), H[n])
                worst = max(worst, float(np.max(np.abs(L - Lb[n]))))
    out = {"C0a Y h = Y^T h = (h.h) u, symbolically": bool(ok_a),
           "C0b Lemma A': largest relative error of |S|_F^2 = 2|u|^2 + 2|<u,h>|^2 - |u.h|^2 (20 000 draws)": idw,
           "C0b Lemma A': largest |u| / m3 (must not exceed sqrt 3)": mx,
           "C0c largest |delta ln| between sm_search.nine_batch and inverse_higgs.nine (1 000 directions, 10 rows)": worst,
           "C0 holds": bool(ok_a and idw < 1e-10 and mx <= math.sqrt(3) and worst < 1e-10)}
    (HERE / "reading_test_c0.json").write_text(json.dumps(out, indent=1) + "\n")
    print("C0 written")


# ---------------------------------------------------------------- the store
def store_point(task):
    k, re_t, im_t = task
    _, a, b = LINES[k]
    return cs.weights(re_t, im_t, float(a), float(b)), cs.directions(re_t, im_t)


def store(nw):
    tasks = grid()
    worst = 0.0
    for task in tasks[:5]:
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
    ctl = {"C1 largest relative |closed - coupling| at the first five points (F_6 and dR, every sector and horocycle)": worst,
           "C1 holds": worst < 1e-12}
    (HERE / "reading_test_c1.json").write_text(json.dumps(ctl, indent=1) + "\n")
    if not ctl["C1 holds"]:
        raise SystemExit("C1 fails: the store is not written")
    cdir = HERE / "chunks_reading_test"; cdir.mkdir(exist_ok=True)
    from multiprocessing import Pool
    t0 = time.time(); nch = (len(tasks) + CHUNK - 1) // CHUNK
    with Pool(nw) as P:
        for c in range(nch):
            f = cdir / f"chunk_{c:04d}.npz"
            if f.exists():
                continue
            res = P.map(store_point, tasks[c * CHUNK:(c + 1) * CHUNK])
            np.savez(f, U=np.array([r[0] for r in res]), H=np.array([r[1] for r in res]))
            print(f"chunk {c + 1}/{nch} ({time.time() - t0:.0f} s)", flush=True)
    U = np.concatenate([np.load(cdir / f"chunk_{c:04d}.npz")["U"] for c in range(nch)])
    H = np.concatenate([np.load(cdir / f"chunk_{c:04d}.npz")["H"] for c in range(nch)])
    np.savez_compressed(HERE / "reading_test_store.npz", U=U, H=H)
    (HERE / "reading_test_store_index.json").write_text(json.dumps({"tasks": tasks, "lines": [[t, str(a), str(b)] for t, a, b in LINES],
                                                                   "sectors": cs.SECTORS, "hors": cs.HORS, "dirs": DIRS}) + "\n")
    print(f"store written ({time.time() - t0:.0f} s)")


# ---------------------------------------------------------------- the scan
G = {}


def _init():
    st = np.load(HERE / "reading_test_store.npz"); G["U"], G["H"] = st["U"], st["H"]


def scan_row(job):
    p, hr = job
    Uh = G["U"][p, :, hr]
    if any(np.allclose(Uh[s], 0) for s in range(3)):
        return {"p": p, "hor": cs.HORS[hr], "degenerate": True}
    gmin, (chi, x) = sms.search(Uh, G["H"][p], T9, SIG, n_extra=4)
    h = sms.vec(x)
    L, c9, _ = sms.nine_batch(Uh, h[None], T9, SIG)
    b = bounds(Uh, h[None])
    rb = bounds(Uh, RAND); rc = sms.nine_batch(Uh, RAND, T9, SIG)[1]
    exa, exb = rb["A"] < VUD_MIN, rb["B"] < VTB_MIN; ex = exa | exb
    c = [np.vdot(sms.F2, h), np.vdot(sms.F3, h), np.vdot(sms.F1, h)]
    return {"p": p, "hor": cs.HORS[hr], "degenerate": False, "grid min chi2_nine": gmin, "chi2_nine": float(c9[0]),
            "chi2_six there": float(np.sum(((L[0, :6] - T9[:6]) / SIG[:6]) ** 2)),
            "chi2 CKM share there": float(np.sum(((L[0, 6:] - T9[6:]) / SIG[6:]) ** 2)),
            "model/data": [float(q) for q in np.exp(L[0] - T9)], "|V|": b["V"][0].round(6).tolist(), "|h.h|": float(b["hh"][0]),
            "|e1|, |n|, |n-bar|": [float(abs(q)) for q in c], "x_u, x_d": [float(b["xu"][0]), float(b["xd"][0])],
            "Lemma A |V_ud| bound": float(b["A"][0]), "alpha_u3, alpha_d3": [float(b["au"][0]), float(b["ad"][0])],
            "Lemma B |V_tb| bound": float(b["B"][0]),
            "random directions excluded by A, by B, by either": [float(exa.mean()), float(exb.mean()), float(ex.mean())],
            "lowest chi2_nine among random directions neither excludes": float(rc[~ex].min()) if (~ex).any() else None,
            "lowest chi2_nine among the random directions": float(rc.min()),
            "h": [[float(q.real), float(q.imag)] for q in h]}


def scan(nw):
    tasks = json.loads((HERE / "reading_test_store_index.json").read_text())["tasks"]
    jobs = [(p, hr) for p in range(len(tasks)) for hr in range(2)]
    from multiprocessing import Pool
    t0 = time.time(); rows = []
    part = HERE / "chunks_reading_test" / "rows_partial.json"
    with Pool(nw, initializer=_init) as P:
        for i, r in enumerate(P.imap(scan_row, jobs, chunksize=4)):
            rows.append(r)
            if (i + 1) % 400 == 0:
                part.write_text(json.dumps({"tasks": tasks, "rows": rows}) + "\n")
                print(f"{i + 1}/{len(jobs)} rows ({time.time() - t0:.0f} s)", flush=True)
    (HERE / "reading_test_rows.json").write_text(json.dumps({"tasks": tasks, "rows": rows}) + "\n")
    print(f"rows written ({time.time() - t0:.0f} s)")


# ---------------------------------------------------------------- C2
def c2():
    _init()
    n_main = len(LINES) * len(RE) * len(IM)
    rng = np.random.default_rng(1741)
    out = []
    t0 = time.time()
    for n in range(36):
        p = int(rng.integers(0, n_main)); hr = int(rng.integers(0, 2))
        Uh = G["U"][p, :, hr]
        while True:
            if n < 12:
                kind = "near the conic"
                t = complex(*rng.normal(size=2)); r = 10 ** rng.uniform(math.log10(5.56e-4), -1); ph = rng.uniform(0, 2 * math.pi)
                h0 = np.array([2 * t, 1 - t * t, 1j * (1 + t * t)]); h0 /= np.linalg.norm(h0)
                hp = h0 + r * np.exp(1j * ph) * np.conj(h0)
            elif n < 24:
                kind = "near n" if n < 18 else "near n-bar"
                lead, other = (sms.F3, sms.F1) if n < 18 else (sms.F1, sms.F3)
                de = 0.25 * math.sqrt(rng.uniform()) * np.exp(2j * math.pi * rng.uniform())
                ep = 0.03 * math.sqrt(rng.uniform()) * np.exp(2j * math.pi * rng.uniform())
                hp = lead + de * sms.F2 + ep * other
            else:
                kind = "uniform"
                z = rng.normal(size=6); hp = z[:3] + 1j * z[3:]
            hp = hp / np.linalg.norm(hp)
            if abs(hp @ hp) >= HH_TUBE:
                break
        T0 = sms.nine_batch(Uh, hp[None], T9, SIG)[0][0]
        Tp = T0 + rng.normal(size=9) * SIG
        cp = float(sms.nine_batch(Uh, hp[None], Tp, SIG)[1][0])
        _, (chi, _) = sms.search(Uh, G["H"][p], Tp, SIG, n_extra=4)
        _, (chi0, _) = sms.search(Uh, G["H"][p], T0, SIG, n_extra=4)
        out.append({"p": p, "hor": cs.HORS[hr], "kind": kind, "|h.h| planted": float(abs(hp @ hp)),
                    "planted direction's chi2 (noisy targets)": cp, "found (noisy)": chi, "met": bool(chi <= cp + 1e-9),
                    "found (noiseless)": chi0})
    ok = sum(o["met"] for o in out)
    res = {"C2 rows": out, "C2 met (the search's minimum at or below the planted direction's chi2)": ok, "C2 holds": ok >= 34,
           "read-out: noiseless recovered to chi2 <= 0.1, <= 2.167": [sum(o["found (noiseless)"] <= 0.1 for o in out),
                                                                      sum(o["found (noiseless)"] <= 2.167 for o in out)],
           "seconds per planted row (both searches)": (time.time() - t0) / 36}
    (HERE / "reading_test_c2.json").write_text(json.dumps(res, indent=1) + "\n")
    print("C2 written")


# ---------------------------------------------------------------- the cells
def cells():
    d = json.loads((HERE / "reading_test_rows.json").read_text()); tasks, rows = d["tasks"], d["rows"]
    lines = [(t, Fr(a), Fr(b)) for t, a, b in json.loads((HERE / "reading_test_store_index.json").read_text())["lines"]]
    deg = [r for r in rows if r.get("degenerate")]
    good = [r for r in rows if not r.get("degenerate") and np.isfinite(r["chi2_nine"])]
    bad = [r for r in rows if not r.get("degenerate") and not np.isfinite(r["chi2_nine"])]
    main = [r for r in good if tasks[r["p"]][1] != RE_MIRROR]; mir = [r for r in good if tasks[r["p"]][1] == RE_MIRROR]
    chis = np.array([r["chi2_nine"] for r in main])

    def lab(r):
        k = tasks[r["p"]][0]
        return {"line": f"({lines[k][1]}, {lines[k][2]})", "order": lines[k][0], "tau": tasks[r["p"]][1:], "hor": r["hor"]}
    out = {"rows": len(main), "degenerate rows (a sector's weights vanish)": [lab(r) for r in deg],
           "rows with a non-finite minimum": [lab(r) for r in bad],
           "S1 no row below 21.67": bool(np.nanmin(chis) >= BAR9), "S1' no row below 100": bool(np.nanmin(chis) >= 100),
           "lowest chi2_nine": float(np.nanmin(chis)), "quantiles 1%, 5%, 50%": [float(np.quantile(chis, q)) for q in (0.01, 0.05, 0.5)],
           "rows below 21.67, 100, 500": [int((chis < c).sum()) for c in (BAR9, 100, 500)],
           "every row below 100": [{**lab(r), "chi2_nine": r["chi2_nine"], "model/data": [round(q, 3) for q in r["model/data"]]}
                                   for r in sorted(main, key=lambda r: r["chi2_nine"]) if r["chi2_nine"] < 100],
           "rows where the refinement lowered the grid minimum": int(sum(r["chi2_nine"] < r["grid min chi2_nine"] - 1e-9 for r in main))}
    br = [(r["|V|"][0][0] < 0.5) or (r["|V|"][1][2] > 0.5) for r in main]
    out["S4 every optimum in a failure branch (|V_ud| < 0.5 or |V_cb| > 0.5)"] = bool(all(br))
    out["S4 rows outside both branches"] = int(len(br) - sum(br))
    A = [r["Lemma A |V_ud| bound"] < VUD_MIN for r in main]; B = [r["Lemma B |V_tb| bound"] < VTB_MIN for r in main]
    out["S5 every optimum excluded by Lemma A or Lemma B"] = bool(all(a or b for a, b in zip(A, B)))
    out["S5 rows: by A only, by B only, by both, by neither"] = [int(sum(a and not b for a, b in zip(A, B))), int(sum(b and not a for a, b in zip(A, B))),
                                                                int(sum(a and b for a, b in zip(A, B))), int(sum(not a and not b for a, b in zip(A, B)))]
    ck = np.array([r["chi2 CKM share there"] for r in main])
    out["rows whose optimum's CKM share alone is above 21.67"] = int((ck >= BAR9).sum())
    fr = np.array([r["random directions excluded by A, by B, by either"] for r in main])
    out["random directions excluded by A, by B, by either: medians over rows"] = [float(np.median(fr[:, i])) for i in range(3)]
    out["random directions excluded by either: smallest fraction over rows"] = float(fr[:, 2].min())
    ne = [r["lowest chi2_nine among random directions neither excludes"] for r in main if r["lowest chi2_nine among random directions neither excludes"] is not None]
    out["lowest chi2_nine among random directions neither bound excludes, over all rows"] = float(min(ne)) if ne else None
    by = {}
    for r in main:
        by.setdefault(lines[tasks[r["p"]][0]][0], []).append(r["chi2_nine"])
    out["lowest chi2_nine by order"] = {o: float(min(v)) for o, v in sorted(by.items(), key=lambda kv: int(kv[0][2:]))}
    out["the twenty lowest rows"] = [{**lab(r), "chi2_nine": r["chi2_nine"], "chi2_six there": r["chi2_six there"],
                                      "chi2 CKM share there": r["chi2 CKM share there"], "model/data": [round(q, 3) for q in r["model/data"]],
                                      "|V_ud|": r["|V|"][0][0], "|h.h|": r["|h.h|"], "x_u, x_d": r["x_u, x_d"],
                                      "Lemma A |V_ud| bound": r["Lemma A |V_ud| bound"], "Lemma B |V_tb| bound": r["Lemma B |V_tb| bound"]}
                                     for r in sorted(main, key=lambda r: r["chi2_nine"])[:20]]
    idx = {(t[0], round(t[1], 6), round(t[2], 6)): i for i, t in enumerate(tasks)}
    rmap = {(r["p"], r["hor"]): r["chi2_nine"] for r in good}
    agree, low_bad, pairs = 0, 0, 0
    for r in mir:
        k, re_t, im_t = tasks[r["p"]]; _, a, b = lines[k]
        km = next(i for i, l in enumerate(lines) if l[1] == a and l[2] == (Fr(3, 5) - b) % 1)
        q = idx[(km, round(1 - re_t, 6), round(im_t, 6))]
        if (q, r["hor"]) not in rmap:
            continue
        x1, x2 = r["chi2_nine"], rmap[(q, r["hor"])]
        ok = abs(x1 - x2) <= 0.01 * min(x1, x2)
        pairs += 1; agree += ok; low_bad += (not ok) and min(x1, x2) < 100
    out["C3 mirror pairs agreeing within 1%"] = [agree, pairs]
    out["C3 pairs below 100 that disagree"] = low_bad
    out["C3 holds"] = bool(pairs == 80 and agree >= 72 and low_bad == 0)
    (HERE / "reading_test_cells.json").write_text(json.dumps(out, indent=1, default=float) + "\n")
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
    elif "--cells" in sys.argv:
        cells()
