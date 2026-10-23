#!/usr/bin/env python3
"""CHANNEL STORE (data-free instrument; chat1's attack reconnaissance, 2026-10-23).
Main's fibre frame (B1720's instrument at 3412bf09d, unchanged, imported through the zero-free census code) evaluated
once per point: for each sector (up, down, lep) and horocycle (L_max, L_2) the four channel weights
u_s = sqrt(2 pi L + c_s) R_s, s in (1, i, j, k), are stored as complex numbers.  With B1736's closed form
    Y = u h^T + h u^T - (u.h) 1 + w [h]_x        (u = (u_i, u_j, u_k), w = u_1, unit order (i, j, k))
every Higgs direction h, reading and pairing then costs three 3 x 3 SVDs, so any Higgs hypothesis becomes a read-out.
Also stored: the record's Higgs directions at each tau (DR = main's census Higgs; the zero-free theta-power family F_a
for a in -10, -6, -2, 2, 6, 10, 14, 18, 22, 26; B1700's h2, h3), unit-normalised, unconjugated.
Nothing here reads a target.

Grids:
  two_higgs  TWO_HIGGS's 1 280 points (the ten alpha = 2/5 lines (2/5, k/10); Re tau 0.0625 .. 0.9375 step 0.125;
             Im tau 2.0 .. 3.5 step 0.1).  Already looked at against the data (TWO_HIGGS, sealed, and its post hoc
             read-outs), so anything compared with data on it is post hoc.
Controls (channel_store_<grid>_controls.json, written before the store):
  C1  at the first five points, every sector and horocycle, the closed form with the stored weights equals
      B.coupling(S_of(h), M) for h = F_6 and h = DR, up to the block order (j, i, k) of B1644's BLOCKS: max relative
      difference below 1e-12;
  C2  TWO_HIGGS's stored fields (two_higgs.npz, float32) for 'F_6 | F_22' and 'dR split (up S~)' at the first five
      points recomputed from the store: max |delta| below 1e-5 (log10 ratios) and relative 1e-4 (|V|).
Resumable in chunks of 64 points (chunks_<grid>/, git-ignored).
    python3 -B channel_store.py --grid two_higgs [--workers 2] [--max-seconds 6600]"""
import contextlib, importlib.util, io, json, math, sys, time, pathlib
from fractions import Fraction as Fr
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
R = HERE.parent
_argv = sys.argv; sys.argv = ["x"]
_spec = importlib.util.spec_from_file_location("zfc", R / "chat1_2026-10-23_zero_free_frame" / "zero_free_census.py")
zfc = importlib.util.module_from_spec(_spec)
with contextlib.redirect_stdout(io.StringIO()):
    _spec.loader.exec_module(zfc)
sys.argv = _argv
rbs, B, tic = zfc.rbs, zfc.B, zfc.tic
TC = tic.TC
SECTORS = ["up", "down", "lep"]
HORS = ["L_max", "L_2"]
CHANS = ["1", "i", "j", "k"]
AS = [-10, -6, -2, 2, 6, 10, 14, 18, 22, 26]
DIRS = ["dR"] + [f"F_{a}" for a in AS] + ["h2", "h3"]
CHUNK = 64


def grid(name):
    if name == "two_higgs":
        lines = [(Fr(2, 5), Fr(k, 10)) for k in range(10)]
        res = [0.0625 + 0.125 * i for i in range(8)]
        ims = [round(2.0 + 0.1 * j, 10) for j in range(16)]
        return lines, [(k, r, y) for k in range(len(lines)) for r in res for y in ims]
    raise SystemExit(f"unknown grid {name}")


def weights(re_t, im_t, a, b):
    t = complex(re_t, im_t); w = a * t + b
    out = np.zeros((3, 2, 4), dtype=complex)
    for i_s, sec in enumerate(SECTORS):
        lf, rf = TC.SECT[sec]
        x, yy = B.sector_twists(w, t, B.SIXY[lf], B.SIXY[rf]); Rr = B.residues(x, yy, t); c = B.cA(x, yy, t, Rr)
        for i_h, which in enumerate(HORS):
            L = TC.L_of(t.imag, which)
            for i_c, kk in enumerate(CHANS):
                out[i_s, i_h, i_c] = (math.sqrt(2 * math.pi * L + c[kk]) * Rr[kk]) if (c[kk] is not None and 2 * math.pi * L + c[kk] > 0) else 0
    return out


def directions(re_t, im_t):
    out = np.zeros((len(DIRS), 3), dtype=complex)
    for i, d in enumerate(DIRS):
        if d in ("h2", "h3"):
            v = rbs.at(rbs.H2 if d == "h2" else rbs.H3, re_t, im_t); v = v / np.linalg.norm(v)
        else:
            v = zfc.direction(d, re_t, im_t)
        out[i] = v
    return out


def cross(h):
    return np.array([[0, -h[2], h[1]], [h[2], 0, -h[0]], [-h[1], h[0], 0]])


def closed(u4, h):
    """B1736's closed form in the unit order (i, j, k); u4 = (u_1, u_i, u_j, u_k)."""
    w, u = u4[0], u4[1:]
    return np.outer(u, h) + np.outer(h, u) - (u @ h) * np.eye(3) + w * cross(h)


P_BLOCK = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 1]])        # B1644's BLOCKS order (j, i, k) from the unit order


def point(task, lines):
    k, re_t, im_t = task
    a, b = lines[k]
    return weights(re_t, im_t, float(a), float(b)), directions(re_t, im_t)


def controls(lines, tasks):
    out = {}
    worst = 0.0
    for task in tasks[:5]:
        k, re_t, im_t = task
        a, b = lines[k]
        U, H = point(task, lines)
        M = rbs.channels(re_t, im_t, float(a), float(b))
        for d in ("F_6", "dR"):
            h = H[DIRS.index(d)]
            for i_s, sec in enumerate(SECTORS):
                for i_h, hor in enumerate(HORS):
                    Yc = P_BLOCK @ closed(U[i_s, i_h], h) @ P_BLOCK.T
                    Yb = B.coupling(rbs.S_of(h), M[(sec, hor)])
                    worst = max(worst, float(np.max(np.abs(Yc - Yb)) / np.max(np.abs(Yb))))
    out["C1 max relative |closed - coupling|"] = worst
    out["C1 holds"] = worst < 1e-12
    th = R / "chat1_2026-10-23_two_higgs"
    X = np.load(th / "two_higgs.npz")["data"].astype(np.float64)
    I = json.loads((th / "two_higgs_index.json").read_text())
    mi = {m: i for i, m in enumerate(I["models"])}
    wr, wv = 0.0, 0.0
    for p, task in enumerate(tasks[:5]):
        assert list(task) == list(I["tasks"][p])
        U, H = point(task, lines)
        f6, f22, dr = H[DIRS.index("F_6")], H[DIRS.index("F_22")], H[DIRS.index("dR")]
        for i_h, hor in enumerate(HORS):
            for model, (hu, hd) in (("F_6 | F_22", (f6, f22)), ("dR split (up S~)", (np.conj(dr), dr))):
                Yu, Yd, Ye = (closed(U[0, i_h], hu), closed(U[1, i_h], hd), closed(U[2, i_h], hd))
                f = []
                for Y in (Yu, Yd, Ye):
                    s = np.linalg.svd(Y, compute_uv=False); f += [math.log10(s[1] / s[0]), math.log10(s[2] / s[0])]
                Yu_b, Yd_b = P_BLOCK @ Yu @ P_BLOCK.T, P_BLOCK @ Yd @ P_BLOCK.T
                ck = tic.ckm_left(Yu_b, Yd_b)
                ref = X[p, I["hors"].index(hor), mi[model]]
                wr = max(wr, float(np.max(np.abs(np.array(f) - ref[:6]))))
                wv = max(wv, max(abs(math.log(x / y)) for x, y in zip(ck[:3], ref[6:9]) if x > 1e-12 and y > 1e-12))
    out["C2 max |delta log10 ratio|, max |delta ln |V||"] = [wr, wv]
    out["C2 holds"] = (wr < 1e-5) and (wv < 1e-4)
    return out


def chunk(args):
    ci, gname = args
    lines, tasks = grid(gname)
    p = HERE / f"chunks_{gname}" / f"chunk_{ci:03d}.npz"
    if not p.exists():
        res = [point(t, lines) for t in tasks[ci * CHUNK:(ci + 1) * CHUNK]]
        np.savez(p, U=np.stack([r[0] for r in res]), H=np.stack([r[1] for r in res]))
    return ci


if __name__ == "__main__":
    from multiprocessing import Pool
    gname = sys.argv[sys.argv.index("--grid") + 1]
    nw = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else 2
    budget = float(sys.argv[sys.argv.index("--max-seconds") + 1]) if "--max-seconds" in sys.argv else 6600.0
    lines, tasks = grid(gname)
    (HERE / f"chunks_{gname}").mkdir(exist_ok=True)
    cpath = HERE / f"channel_store_{gname}_controls.json"
    if not cpath.exists():
        cpath.write_text(json.dumps(controls(lines, tasks), indent=1) + "\n")
        print("controls written", flush=True)
    nch = (len(tasks) + CHUNK - 1) // CHUNK
    todo = [ci for ci in range(nch) if not (HERE / f"chunks_{gname}" / f"chunk_{ci:03d}.npz").exists()]
    print(f"{len(tasks)} points in {nch} chunks; {len(todo)} to do", flush=True)
    t0 = time.time(); n = 0
    with Pool(nw) as P:
        for ci in P.imap_unordered(chunk, [(ci, gname) for ci in todo]):
            n += 1
            print(f"chunk {ci} done ({n} of {len(todo)}, {time.time() - t0:.0f} s)", flush=True)
            if time.time() - t0 > budget:
                print("budget reached; rerun to resume", flush=True); P.terminate(); break
    if all((HERE / f"chunks_{gname}" / f"chunk_{ci:03d}.npz").exists() for ci in range(nch)):
        parts = [np.load(HERE / f"chunks_{gname}" / f"chunk_{ci:03d}.npz") for ci in range(nch)]
        U = np.concatenate([q["U"] for q in parts]); H = np.concatenate([q["H"] for q in parts])
        np.savez_compressed(HERE / f"channel_store_{gname}.npz", U=U, H=H)
        (HERE / f"channel_store_{gname}_index.json").write_text(json.dumps(
            {"grid": gname, "tasks": [[k, r, y] for k, r, y in tasks], "lines": [f"({a}, {b})" for a, b in lines],
             "sectors": SECTORS, "hors": HORS, "channels (u_1, u_i, u_j, u_k)": CHANS, "dirs": DIRS,
             "U shape (point, sector, hor, channel)": list(U.shape), "H shape (point, dir, component i j k)": list(H.shape)}, indent=1) + "\n")
        print("combined", U.shape, H.shape, flush=True)
