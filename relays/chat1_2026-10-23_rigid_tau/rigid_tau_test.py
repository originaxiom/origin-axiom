#!/usr/bin/env python3
"""RIGID_TAU_HOLOMORPHIC (sealed: RIGID_TAU_HOLOMORPHIC_RULE.md, 51b05f7c7, committed and pushed before this script).
Main's frame (B1720's instrument at 3412bf09d, through the zero-free census's code) at the record's rigid tau candidates,
for the menu F_6, F_-2, F_22 and the reference DR:
  family A: B1720's apex rule, unchanged: its 121 classes (thread_geometry.census(2, 9, 4.0), as main's
            the_thread_census.py builds CENSUS), tau = each class's stored apex, every line the class fixes as stored;
  family B: tau = 2 sqrt3 i and 1/2 + sqrt3 i on the tick's eight lines (B1698's S1 and S2).
Per point and horocycle the census's 28 fields (log10 m2/m3 and m1/m3 for (up, down, lep) x (S, S~); |V_us|, |V_cb|,
|V_ub|, J for the four (up, down) readings).
Controls first (rigid_tau_controls.json): C1 (DR with S against main's TC.ratios_at at 1/2 + 3.08i on (2/5, 1/10)); C2
(F_6's T-covariance at the first family-A point; ratios and |V| above 1e-12); C3 (DR at B1720's best point against the
six ratios main stored in the_thread_census.json, up reading S~, L_max).
Resumable in chunks of 200 points (chunks_rigid/, git-ignored); when all exist they are combined into rigid_tau.npz and
its index.  Nothing here reads a target.
    python3 -B rigid_tau_test.py [--workers 2] [--max-seconds 6600]"""
import contextlib, importlib.util, io, json, math, subprocess, sys, time, pathlib
from fractions import Fraction as Fr
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / ".git").exists())
ZF = HERE.parent / "chat1_2026-10-23_zero_free_frame"
_argv = sys.argv; sys.argv = ["x"]
_spec = importlib.util.spec_from_file_location("zfc", ZF / "zero_free_census.py")
zfc = importlib.util.module_from_spec(_spec)
with contextlib.redirect_stdout(io.StringIO()):
    _spec.loader.exec_module(zfc)
sys.argv = _argv
rbs, tic = zfc.rbs, zfc.tic
TC = tic.TC
CH = HERE / "chunks_rigid"
CH.mkdir(exist_ok=True)
DIRS = ["F_6", "F_-2", "F_22", "dR"]

Lm = np.array([[1, 0], [-1, 1]]); Rm = np.array([[1, -1], [0, 1]])              # B1698's moves on (alpha, b)


def sign_fixed(M):
    return sorted({(Fr(i, 5), Fr(j, 5)) for i in range(5) for j in range(5)
                   if (i, j) != (0, 0) and all(v % 5 == 0 for v in (M + np.eye(2, dtype=int)) @ [i, j])})


TICK = sign_fixed(Lm @ Rm) + sign_fixed(Rm @ Lm)
POINTS = []                                    # (family, label, re, im, alpha, b)
for k, r in enumerate(TC.CENSUS):
    for j, (a, b) in enumerate(r["lines"]):
        POINTS.append(("A", f"{r['word']} #{k} line {j} ({a}, {b})", float(r["tau"][0]), float(r["tau"][1]), Fr(a), Fr(b)))
for name, re_t, im_t in (("2 sqrt3 i", 0.0, 2 * math.sqrt(3)), ("1/2 + sqrt3 i", 0.5, math.sqrt(3))):
    for a, b in TICK:
        POINTS.append(("B", f"{name} on ({a}, {b})", re_t, im_t, a, b))
CHUNK = 200


def point(pt):
    _f, _l, re_t, im_t, a, b = pt
    M = rbs.channels(re_t, im_t, float(a), float(b))
    return np.stack([zfc.rows_at(M, zfc.direction(d, re_t, im_t)) for d in DIRS]).astype(np.float32)


def chunk(ci):
    p = CH / f"chunk_{ci:03d}.npy"
    if not p.exists():
        np.save(p, np.stack([point(t) for t in POINTS[ci * CHUNK:(ci + 1) * CHUNK]]))
    return ci


def controls():
    out = {}
    t, a, b = complex(0.5, 3.08), 2 / 5, 1 / 10
    x = zfc.rows_at(rbs.channels(t.real, t.imag, a, b), zfc.direction("dR", t.real, t.imag))
    ours = [10 ** x[0, j] for j in (0, 1, 4, 5, 8, 9)]
    out["C1 max |delta ln| against TC.ratios_at"] = max(abs(math.log(p / q)) for p, q in zip(ours, TC.ratios_at(t, a, b)))
    _f, lab, re0, im0, a0, b0 = POINTS[0]
    x0 = zfc.rows_at(rbs.channels(re0, im0, float(a0), float(b0)), zfc.direction("F_6", re0, im0))
    x1 = zfc.rows_at(rbs.channels(re0 + 1, im0, float(a0), float(b0 - a0)), zfc.direction("F_6", re0 + 1, im0))
    keep = (x0[:, :12] > -12) & (x1[:, :12] > -12)
    dr = float(np.max(np.abs(x0[:, :12] - x1[:, :12])[keep])) * math.log(10)
    sel_v = [12 + 4 * p + q for p in range(4) for q in range(3)]
    v0, v1 = x0[:, sel_v], x1[:, sel_v]
    keepv = (v0 > 1e-12) & (v1 > 1e-12)
    dv = float(np.max(np.abs(np.log(v0 / v1))[keepv]))
    out["C2 point"] = lab
    out["C2 max |delta ln| under T (ratios, |V| above 1e-12), F_6"] = [dr, dv]
    out["C2 entries kept (ratios, |V|)"] = [int(keep.sum()), int(keepv.sum())]
    stored = json.loads(subprocess.run(["git", "show", "3412bf09d:frontier/B1720_the_thread_fixes_the_point/verification/the_thread_census.json"],
                                       cwd=ROOT, capture_output=True, check=True).stdout)
    k = next(i for i, r in enumerate(TC.CENSUS) if r["word"] == "LLLLLRLRR")
    j = next(i for i, l in enumerate(TC.CENSUS[k]["lines"]) if (Fr(l[0]), Fr(l[1])) == (Fr(11, 28), Fr(2, 7)))
    row = next(r for r in stored["rows"] if r["class"] == k and r["line"] == j)
    r = TC.CENSUS[k]; a3, b3 = TC.CENSUS[k]["lines"][j]
    x3 = zfc.rows_at(rbs.channels(float(r["tau"][0]), float(r["tau"][1]), float(Fr(a3)), float(Fr(b3))),
                     zfc.direction("dR", float(r["tau"][0]), float(r["tau"][1])))[0]          # L_max
    ours3 = [10 ** x3[2], 10 ** x3[3], 10 ** x3[4], 10 ** x3[5], 10 ** x3[8], 10 ** x3[9]]       # up S~, down S, lep S
    main3 = row["up|L_max|St"] + row["down|L_max|S"] + row["lep|L_max|S"]
    out["C3 class, line"] = [r["word"], k, j, f"({a3}, {b3})", list(r["tau"])]
    out["C3 max |delta ln| against B1720's stored six"] = max(abs(math.log(p / q)) for p, q in zip(ours3, main3))
    out["C1 holds"] = out["C1 max |delta ln| against TC.ratios_at"] < 1e-9
    out["C2 holds"] = max(dr, dv) < 1e-9
    out["C3 holds"] = out["C3 max |delta ln| against B1720's stored six"] < 1e-6
    return out


if __name__ == "__main__":
    from multiprocessing import Pool
    nw = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else 2
    budget = float(sys.argv[sys.argv.index("--max-seconds") + 1]) if "--max-seconds" in sys.argv else 6600.0
    if not (HERE / "rigid_tau_controls.json").exists():
        (HERE / "rigid_tau_controls.json").write_text(json.dumps(controls(), indent=1, default=str) + "\n")
        print("controls written", flush=True)
    nch = (len(POINTS) + CHUNK - 1) // CHUNK
    todo = [ci for ci in range(nch) if not (CH / f"chunk_{ci:03d}.npy").exists()]
    print(f"{len(POINTS)} points in {nch} chunks; {nch - len(todo)} done; {len(todo)} to do", flush=True)
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
        np.savez_compressed(HERE / "rigid_tau.npz", data=data)
        (HERE / "rigid_tau_index.json").write_text(json.dumps(
            {"points": [[f, l, re_t, im_t, str(a), str(b)] for f, l, re_t, im_t, a, b in POINTS], "dirs": DIRS,
             "hors": rbs.HORS, "fields": zfc.FIELDS, "shape": list(data.shape)}, indent=1) + "\n")
        print("combined", data.shape, flush=True)
