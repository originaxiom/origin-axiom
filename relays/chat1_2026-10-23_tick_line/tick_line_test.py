#!/usr/bin/env python3
"""TICK_LINE_HIGGS (sealed: TICK_LINE_HIGGS_RULE.md, e0c16e1cd, committed and pushed before this script).
Computes, on the rule's unseen grid, main's frame (B1720's instrument at 3412bf09d, through the zero-free census's
code) on the tick's eight sign-fixed order-5 lines (B1698: the points fixed up to sign by L.R and by R.L, with
L: (alpha, b) -> (alpha, b - alpha) and R: (alpha, b) -> (alpha - b, b)) for four Higgs directions: the menu F_6, F_-2,
F_22 and the reference DR.  Per point and horocycle the census's 28 fields (log10 m2/m3 and m1/m3 for (up, down, lep)
x (S, S~); |V_us|, |V_cb|, |V_ub|, J for the four (up, down) readings).
Controls first (tick_line_controls.json): C1 (DR with S against main's TC.ratios_at at 1/2 + 3.08i on (2/5, 1/10)) and
C2 (F_6's T-covariance at the first grid point, every ratio and every |V| above 1e-12).
Resumable in chunks of 200 points (chunks_tick/, git-ignored); when all exist they are combined into tick_line.npz and
its index.  Nothing here reads a target.
    python3 -B tick_line_test.py [--workers 2] [--max-seconds 6600]"""
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
CH = HERE / "chunks_tick"
CH.mkdir(exist_ok=True)

Lm = np.array([[1, 0], [-1, 1]]); Rm = np.array([[1, -1], [0, 1]])              # on the column (alpha, b), as B1698


def sign_fixed(M):
    return sorted({(Fr(i, 5), Fr(j, 5)) for i in range(5) for j in range(5)
                   if (i, j) != (0, 0) and all(v % 5 == 0 for v in (M + np.eye(2, dtype=int)) @ [i, j])})


S1, S2 = sign_fixed(Lm @ Rm), sign_fixed(Rm @ Lm)
LINES = [("S1", a, b) for a, b in S1] + [("S2", a, b) for a, b in S2]
NAMES = [f"({a}, {b})" for _t, a, b in LINES]
DIRS = ["F_6", "F_-2", "F_22", "dR"]
RE = [round(0.025 + 0.05 * i, 3) for i in range(20)]
IM = [round(2.025 + 0.1 * j, 3) for j in range(15)]
TASKS = [(k, r, y) for k in range(len(LINES)) for r in RE for y in IM]
CHUNK = 200


def point(task):
    k, re_t, im_t = task
    _t, a, b = LINES[k]
    M = rbs.channels(re_t, im_t, float(a), float(b))
    return np.stack([zfc.rows_at(M, zfc.direction(d, re_t, im_t)) for d in DIRS]).astype(np.float32)


def chunk(ci):
    p = CH / f"chunk_{ci:03d}.npy"
    if not p.exists():
        np.save(p, np.stack([point(t) for t in TASKS[ci * CHUNK:(ci + 1) * CHUNK]]))
    return ci


def controls():
    out = {"S1": [str(x) for x in S1], "S2": [str(x) for x in S2]}
    t, a, b = complex(0.5, 3.08), 2 / 5, 1 / 10
    M = rbs.channels(t.real, t.imag, a, b)
    x = zfc.rows_at(M, zfc.direction("dR", t.real, t.imag))
    ours = [10 ** x[0, j] for j in (0, 1, 4, 5, 8, 9)]                    # L_max, reading S: up, down, lep (m2/m3, m1/m3)
    main = tic.TC.ratios_at(t, a, b)
    out["C1 max |delta ln| against TC.ratios_at"] = max(abs(math.log(p / q)) for p, q in zip(ours, main))
    k0, re0, im0 = TASKS[0]
    _t, a0, b0 = LINES[k0]
    x0 = zfc.rows_at(rbs.channels(re0, im0, float(a0), float(b0)), zfc.direction("F_6", re0, im0))
    x1 = zfc.rows_at(rbs.channels(re0 + 1, im0, float(a0), float(b0 - a0)), zfc.direction("F_6", re0 + 1, im0))
    r0, r1 = x0[:, :12], x1[:, :12]
    keep = (r0 > -12) & (r1 > -12)
    dr = float(np.max(np.abs(r0 - r1)[keep])) * math.log(10)
    sel_v = [12 + 4 * p + q for p in range(4) for q in range(3)]
    v0, v1 = x0[:, sel_v], x1[:, sel_v]
    keepv = (v0 > 1e-12) & (v1 > 1e-12)
    dv = float(np.max(np.abs(np.log(v0 / v1))[keepv]))
    out["C2 line, point"] = [NAMES[k0], re0, im0]
    out["C2 max |delta ln| under T (ratios, |V| above 1e-12), F_6 at the first grid point"] = [dr, dv]
    out["C2 entries kept (ratios, |V|)"] = [int(keep.sum()), int(keepv.sum())]
    out["C1 holds"] = out["C1 max |delta ln| against TC.ratios_at"] < 1e-9
    out["C2 holds"] = max(dr, dv) < 1e-9
    return out


if __name__ == "__main__":
    from multiprocessing import Pool
    nw = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else 2
    budget = float(sys.argv[sys.argv.index("--max-seconds") + 1]) if "--max-seconds" in sys.argv else 6600.0
    if not (HERE / "tick_line_controls.json").exists():
        (HERE / "tick_line_controls.json").write_text(json.dumps(controls(), indent=1) + "\n")
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
        np.savez_compressed(HERE / "tick_line.npz", data=data)
        (HERE / "tick_line_index.json").write_text(json.dumps(
            {"tasks": [[k, r, y] for k, r, y in TASKS], "lines": NAMES, "sets": [t for t, _a, _b in LINES],
             "dirs": DIRS, "hors": rbs.HORS, "fields": zfc.FIELDS, "shape": list(data.shape)}, indent=1) + "\n")
        print("combined", data.shape, flush=True)
