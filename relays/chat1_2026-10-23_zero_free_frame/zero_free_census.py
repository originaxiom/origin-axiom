#!/usr/bin/env python3
"""EXPLORATORY, labelled (chat1's next step after route (b); no cell, no seal, no data in the design): main's frame
with the zero-free Higgs lines in place of DR.

The Higgs directions at tau:
  dR   main's Higgs (the reference);
  F_a  = eta^(3-a) (e th2^a, e th4^a, i th3^a), e = i^((a+2)/2), a = 2 mod 4: every zero-free weight-3/2 section of
       rho_T (x) chi_eta^r is one of these, with r = 2a mod 24 (chat1's W133 check, relays/CHAT1_TO_SM_AND_CC_
       2026-10-23_W133_CHECKED.md).  The ten with one unit of end data:
         r = 4: a = -10, 2, 14, 26;   r = 12: a = -6, 6, 18;   r = 20: a = -2, 10, 22   (r = 12, 20: W127's count three).
       The scalar eta^(3-a) drops out of every ratio; the direction is normalised to unit length.
The frame: main's B1720 instrument at 3412bf09d, unchanged, through route_b_scan.py (channels, S_of, St, outputs'
pieces).  A twist multiplies the coupling by a phase, which no ratio, |V| or J sees.
Readings: S(v) and S~ = S(conj v) in every sector; the four (up, down) pairings for the mixing.
Grid: Re tau in {0.1, 0.4}; Im tau = 1.0, 1.1, ..., 4.0 (the range of main's horocycle table, B1667); the sealed
census's 266 lines of order 1-12 (B1713's list): 16 492 points, both horocycles.
Stored per point, direction and horocycle (float32): log10 of m2/m3 and m1/m3 for (up, down, lep) x (S, S~) [12 fields],
then |V_us|, |V_cb|, |V_ub|, J for the (up, down) readings (S,S), (S,S~), (S~,S), (S~,S~) [16 fields].
Controls (zero_free_census_controls.json, written before the grid):
  C1  DR's values reproduce the sealed census's stored values at three census points (both horocycles, S and S~);
  C2  F_2's direction is R's (main's te.B[0]);
  C3  T-covariance with F_6 (r = 12) and F_-2 (r = 20): tau -> tau + 1, b -> b - a.
Resumable: chunks of 200 points in chunks/ (git-ignored); when every chunk exists, they are combined into
zero_free_census.npz and zero_free_census_index.json.
    python3 -B zero_free_census.py [--workers 2] [--max-seconds 6600]"""
import contextlib, importlib.util, io, json, math, sys, time, pathlib
from fractions import Fraction as Fr
import numpy as np
import mpmath as mp

HERE = pathlib.Path(__file__).resolve().parent
RB = HERE.parent / "chat1_2026-10-23_route_b"
_spec = importlib.util.spec_from_file_location("rbs", RB / "route_b_scan.py")
rbs = importlib.util.module_from_spec(_spec)
with contextlib.redirect_stdout(io.StringIO()):
    _spec.loader.exec_module(rbs)
B, tic = rbs.B, rbs.tic
mp.mp.dps = 30
CH = HERE / "chunks"
CH.mkdir(exist_ok=True)
AS = [-10, 2, 14, 26, -6, 6, 18, -2, 10, 22]
DIRS = ["dR"] + [f"F_{a}" for a in AS]
RE = [0.1, 0.4]
IM = [round(1.0 + 0.1 * j, 2) for j in range(31)]
LINES = [(float(Fr(a)), float(Fr(b)), f"({a}, {b})") for (_t, a, b) in tic.LINES]
TASKS = [(k, r, y) for k in range(len(LINES)) for r in RE for y in IM]
CHUNK = 200
FIELDS = [f"log10 {sec} {rat} {rd}" for sec in ("up", "down", "lep") for rd in ("S", "St") for rat in ("m2/m3", "m1/m3")] + \
         [f"{q} {ru}|{rd}" for ru, rd in (("S", "S"), ("S", "St"), ("St", "S"), ("St", "St")) for q in ("Vus", "Vcb", "Vub", "J")]


def th(t):                                                   # theta2, 3, 4 summed directly in tau
    t = mp.mpc(t)
    t2 = mp.fsum(mp.exp(1j * mp.pi * t * (n + mp.mpf(1) / 2) ** 2) for n in range(-30, 30))
    t3 = mp.fsum(mp.exp(1j * mp.pi * t * n * n) for n in range(-30, 31))
    t4 = mp.fsum((-1) ** n * mp.exp(1j * mp.pi * t * n * n) for n in range(-30, 31))
    return t2, t3, t4


def direction(d, re_t, im_t):
    if d == "dR":
        v = rbs.at(rbs.H1, re_t, im_t)
    else:
        a = int(d[2:]); e = 1 if ((a + 2) // 2) % 4 == 0 else -1
        t2, t3, t4 = th(complex(re_t, im_t))
        v = np.array([complex(e * t2 ** a), complex(e * t4 ** a), complex(1j * t3 ** a)])
    return v / np.linalg.norm(v)


def rows_at(M, v):
    out = np.zeros((2, 28), dtype=np.float64)
    S = rbs.S_of(v); St = rbs.St(S)
    for ih, hor in enumerate(rbs.HORS):
        Y = {}
        f = []
        for sec in ("up", "down", "lep"):
            for rd, SS in (("S", S), ("St", St)):
                Y[(sec, rd)] = B.coupling(SS, M[(sec, hor)])
                s = np.linalg.svd(Y[(sec, rd)], compute_uv=False)
                f += [math.log10(max(s[1] / s[0], 1e-300)), math.log10(max(s[2] / s[0], 1e-300))]
        for ru, rd in (("S", "S"), ("S", "St"), ("St", "S"), ("St", "St")):
            f += tic.ckm_left(Y[("up", ru)], Y[("down", rd)])
        out[ih] = f
    return out


def point(task):
    k, re_t, im_t = task
    a, b, _ = LINES[k]
    M = rbs.channels(re_t, im_t, a, b)
    return np.stack([rows_at(M, direction(d, re_t, im_t)) for d in DIRS]).astype(np.float32)


def chunk(ci):
    p = CH / f"chunk_{ci:03d}.npy"
    if not p.exists():
        arr = np.stack([point(t) for t in TASKS[ci * CHUNK:(ci + 1) * CHUNK]])
        np.save(p, arr)
    return ci


def controls():
    out = {}
    rows = {}
    for l in (RB.parent / "chat1_2026-10-22_selection_map" / "two_ingredients_census.jsonl").read_text().splitlines()[:3]:
        r = json.loads(l); rows[(r["line"], r["Re_tau"], r["Im_tau"])] = r
    dev = 0.0
    for (k, re_t, im_t), r in rows.items():
        a, b, _ = LINES[k]
        M = rbs.channels(re_t, im_t, a, b)
        x = rows_at(M, direction("dR", re_t, im_t))
        for ih, hor in enumerate(rbs.HORS):
            j = 0
            for sec in ("up", "down", "lep"):
                for rd in ("S", "St"):
                    for q in range(2):
                        dev = max(dev, abs(x[ih, j] - math.log10(r[f"{sec}|{hor}|{rd}"][q]))); j += 1
            for ru, rd in (("S", "S"), ("S", "St"), ("St", "S"), ("St", "St")):
                ref = r[f"ckm|{hor}|{ru}|{rd}"]
                dev = max(dev, max(abs(math.log10(x[ih, j + q] / ref[q])) for q in range(3))); j += 4
    out["C1 max |delta log10| against the census"] = dev
    t = complex(0.4, 2.7)
    v2 = direction("F_2", t.real, t.imag); vR = rbs.at(rbs.R, t.real, t.imag); vR = vR / np.linalg.norm(vR)
    out["C2 |F_2 direction wedge R direction|"] = float(abs(abs(np.vdot(vR, v2)) - 1))
    cov = {}
    for d in ("F_6", "F_-2", "dR"):
        re_t, im_t, a, b = 0.4, 2.7, 0.4, 0.1
        x0 = rows_at(rbs.channels(re_t, im_t, a, b), direction(d, re_t, im_t))
        x1 = rows_at(rbs.channels(re_t + 1, im_t, a, b - a), direction(d, re_t + 1, im_t))
        sel = list(range(12)) + [12 + 4 * p + q for p in range(4) for q in range(3)]
        cov[d] = float(np.max(np.abs(x0[:, sel[:12]] - x1[:, sel[:12]]))) , float(np.max(np.abs(np.log10(x0[:, sel[12:]] / x1[:, sel[12:]]))))
    out["C3 T-covariance, max |delta log10| (ratios, |V|)"] = cov
    return out


if __name__ == "__main__":
    from multiprocessing import Pool
    nw = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else 2
    budget = float(sys.argv[sys.argv.index("--max-seconds") + 1]) if "--max-seconds" in sys.argv else 6600.0
    if not (HERE / "zero_free_census_controls.json").exists():
        (HERE / "zero_free_census_controls.json").write_text(json.dumps(controls(), indent=1) + "\n")
        print("controls written", flush=True)
    nch = (len(TASKS) + CHUNK - 1) // CHUNK
    todo = [ci for ci in range(nch) if not (CH / f"chunk_{ci:03d}.npy").exists()]
    print(f"{len(TASKS)} points in {nch} chunks; {nch - len(todo)} done; {len(todo)} to do", flush=True)
    t0 = time.time(); n = 0
    with Pool(nw) as P:
        for ci in P.imap_unordered(chunk, todo):
            n += 1
            print(f"chunk {ci} done ({n} of {len(todo)} this run, {time.time() - t0:.0f} s)", flush=True)
            if time.time() - t0 > budget:
                print("budget reached; rerun to resume", flush=True)
                P.terminate(); break
    if all((CH / f"chunk_{ci:03d}.npy").exists() for ci in range(nch)):
        data = np.concatenate([np.load(CH / f"chunk_{ci:03d}.npy") for ci in range(nch)])
        np.savez_compressed(HERE / "zero_free_census.npz", data=data)
        (HERE / "zero_free_census_index.json").write_text(json.dumps(
            {"tasks": [[k, r, y] for k, r, y in TASKS], "lines": [l[2] for l in LINES], "dirs": DIRS, "a": AS,
             "twist_r": {f"F_{a}": (2 * a) % 24 for a in AS}, "hors": rbs.HORS, "fields": FIELDS,
             "shape": list(data.shape)}, indent=1) + "\n")
        print("combined", data.shape, flush=True)
