#!/usr/bin/env python3
"""TWO_HIGGS (sealed: TWO_HIGGS_RULE.md, 0b192e458, committed and pushed before this script).
Main's frame (B1720's instrument at 3412bf09d, through the zero-free census's code) with two Higgs directions: H_u for the
up quarks and H_d for the down quarks and the leptons, each from the menu F_6, F_-2, F_22, both read S.  Nine pairs (six
off-diagonal, three diagonal) and two references (main's DR in its split reading, and with S~ in every sector).
The grid: the ten alpha = 2/5 lines (2/5, k/10), Re tau in {0.0625, 0.1875, ..., 0.9375}, Im tau in {2.0, 2.1, ..., 3.5},
both horocycles: 1 280 points.
Per point, horocycle and model, 16 fields: log10 m2/m3 and m1/m3 for up, down, leptons; |V_us|, |V_cb|, |V_ub|, J (left
singular vectors, two_ingredients_census's ckm_left); the up and down sectors' heaviest left vector as weights on the
generation blocks (QJ, QI, QK).
Controls first (two_higgs_controls.json): C1 (each diagonal pair against the zero-free census code's rows_at, S fields, at
the first grid point); C2 (DR with S in every sector, through this script's own code path, against main's TC.ratios_at at
1/2 + 3.08i on (2/5, 1/10), L_max).  Resumable in chunks of 64 points (chunks_two_higgs/, git-ignored); when all exist they
are combined into two_higgs.npz and its index.  Nothing here reads a target.
    python3 -B two_higgs_test.py [--workers 2] [--max-seconds 6600]"""
import contextlib, importlib.util, io, json, math, sys, time, pathlib
from fractions import Fraction as Fr
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
ZF = HERE.parent / "chat1_2026-10-23_zero_free_frame"
_argv = sys.argv; sys.argv = ["x"]
_spec = importlib.util.spec_from_file_location("zfc", ZF / "zero_free_census.py")
zfc = importlib.util.module_from_spec(_spec)
with contextlib.redirect_stdout(io.StringIO()):
    _spec.loader.exec_module(zfc)
sys.argv = _argv
rbs, B, tic = zfc.rbs, zfc.B, zfc.tic
TC = tic.TC
CH = HERE / "chunks_two_higgs"
CH.mkdir(exist_ok=True)
MENU = ["F_6", "F_-2", "F_22"]
PAIRS = [(u, d) for u in MENU for d in MENU]
MODELS = [f"{u} | {d}" for u, d in PAIRS] + ["dR split (up S~)", "dR S~ in every sector"]
LINES = [(Fr(2, 5), Fr(k, 10)) for k in range(10)]
RES = [0.0625 + 0.125 * i for i in range(8)]
IMS = [round(2.0 + 0.1 * j, 10) for j in range(16)]
TASKS = [(k, re_t, im_t) for k in range(len(LINES)) for re_t in RES for im_t in IMS]
FIELDS = ["log10 up m2/m3", "log10 up m1/m3", "log10 down m2/m3", "log10 down m1/m3", "log10 lep m2/m3", "log10 lep m1/m3",
          "Vus", "Vcb", "Vub", "J", "up heaviest on QJ", "up heaviest on QI", "up heaviest on QK",
          "down heaviest on QJ", "down heaviest on QI", "down heaviest on QK"]
CHUNK = 64


def heavy(Y):
    U = np.linalg.svd(Y)[0]
    return list(np.abs(U[:, 0]) ** 2)


def row(M, hor, Su, Sd):
    Yu = B.coupling(Su, M[("up", hor)]); Yd = B.coupling(Sd, M[("down", hor)]); Ye = B.coupling(Sd, M[("lep", hor)])
    f = []
    for Y in (Yu, Yd, Ye):
        s = np.linalg.svd(Y, compute_uv=False)
        f += [math.log10(max(s[1] / s[0], 1e-300)), math.log10(max(s[2] / s[0], 1e-300))]
    f += tic.ckm_left(Yu, Yd)
    return f + heavy(Yu) + heavy(Yd)


def point(task):
    k, re_t, im_t = task
    a, b = LINES[k]
    M = rbs.channels(re_t, im_t, float(a), float(b))
    S = {d: rbs.S_of(zfc.direction(d, re_t, im_t)) for d in MENU}
    SR = rbs.S_of(zfc.direction("dR", re_t, im_t)); SRt = rbs.St(SR)
    out = np.zeros((2, len(MODELS), len(FIELDS)))
    for ih, hor in enumerate(rbs.HORS):
        for im_, (u, d) in enumerate(PAIRS):
            out[ih, im_] = row(M, hor, S[u], S[d])
        out[ih, 9] = row(M, hor, SRt, SR)
        out[ih, 10] = row(M, hor, SRt, SRt)
    return out.astype(np.float32)


def chunk(ci):
    p = CH / f"chunk_{ci:03d}.npy"
    if not p.exists():
        np.save(p, np.stack([point(t) for t in TASKS[ci * CHUNK:(ci + 1) * CHUNK]]))
    return ci


def controls():
    out = {}
    k, re_t, im_t = TASKS[0]
    a, b = LINES[k]
    M = rbs.channels(re_t, im_t, float(a), float(b))
    worst_r, worst_v = 0.0, 0.0
    for ih, hor in enumerate(rbs.HORS):
        for d in MENU:
            v = zfc.direction(d, re_t, im_t)
            x = zfc.rows_at(M, v)[ih]
            ours = row(M, hor, rbs.S_of(v), rbs.S_of(v))
            ref_r = [x[0], x[1], x[4], x[5], x[8], x[9]]
            worst_r = max(worst_r, max(abs(p - q) * math.log(10) for p, q in zip(ours[:6], ref_r) if p > -12 and q > -12))
            for p, q in zip(ours[6:9], x[12:15]):
                if p > 1e-12 and q > 1e-12:
                    worst_v = max(worst_v, abs(math.log(p / q)))
    out["C1 point"] = [f"({a}, {b})", re_t, im_t]
    out["C1 max |delta ln| (ratios, |V|)"] = [worst_r, worst_v]
    out["C1 holds"] = max(worst_r, worst_v) < 1e-9
    t, a2, b2 = complex(0.5, 3.08), 2 / 5, 1 / 10
    M2 = rbs.channels(t.real, t.imag, a2, b2)
    SR = rbs.S_of(zfc.direction("dR", t.real, t.imag))
    ours = row(M2, "L_max", SR, SR)
    mine = [10 ** ours[j] for j in range(6)]
    main = TC.ratios_at(t, a2, b2)
    out["C2 max |delta ln| against TC.ratios_at"] = max(abs(math.log(p / q)) for p, q in zip(mine, main))
    out["C2 holds"] = out["C2 max |delta ln| against TC.ratios_at"] < 1e-9
    return out


if __name__ == "__main__":
    from multiprocessing import Pool
    nw = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else 2
    budget = float(sys.argv[sys.argv.index("--max-seconds") + 1]) if "--max-seconds" in sys.argv else 6600.0
    if not (HERE / "two_higgs_controls.json").exists():
        (HERE / "two_higgs_controls.json").write_text(json.dumps(controls(), indent=1, default=str) + "\n")
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
        np.savez_compressed(HERE / "two_higgs.npz", data=data)
        (HERE / "two_higgs_index.json").write_text(json.dumps(
            {"tasks": [[k, re_t, im_t] for k, re_t, im_t in TASKS], "lines": [f"({a}, {b})" for a, b in LINES],
             "models": MODELS, "pairs": [list(p) for p in PAIRS], "hors": rbs.HORS, "fields": FIELDS,
             "shape": list(data.shape)}, indent=1) + "\n")
        print("combined", data.shape, flush=True)
