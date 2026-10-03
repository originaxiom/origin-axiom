#!/usr/bin/env python3
"""B1529 post-run check (written after the sealed crossing run had begun; disclosed in FINDINGS): the sealed bracket rule at
the poles of b, and the sealed run on +-LLLRLRR completed.

Why. crossings.brackets takes a sign change of a crossing function between adjacent converged frames of X1's grid, both with
|b| < 50 a, as a bracket.  Where b passes through a pole between two such frames, psi_b = b Y_l changes sign through infinity
and every crossing function whose psi_b coefficient is non-zero changes sign with it: such a bracket holds no crossing of its
kind unless it also holds a second sign change.  X1's own zero finder excludes these (a sign change of b is a zero only when
|b/a| < 10 at both frames); the sealed rule, like X1's crossing count, does not.  On +-LLLRLRR the poles (alpha_1 + 30 + 60 k,
alpha_1 = 8.2555 degrees) fall 3.3 and 1.7 degrees from the grid's frames, where b/a = -5.81 and 10.92: 22 of the 40 brackets
on each sign are sign changes through a pole.  On the other eight rings the frames next to the poles did not converge, and no
pole bracket was admitted.  The sealed run on +-LLLRLRR located its first bracket (E1, 25-30 degrees, both signs), then spent
2,024 and 1,928 seconds failing on its second (E1, 35-40, a pole bracket); it was stopped at 13:26:46Z.

What this does.  The sealed run_one on +-LLLRLRR, its loop body unchanged (crossings.locate, then crossings.read, on
crossings.brackets' own list), one process per bracket, the brackets with no pole first.  Each bracket's computation is
independent of the others: X1's pinned solver caches only the hyperbolic seeds, a deterministic function of the frame, and
X1c's solver takes its warm start as an argument.  So the record is the one run_one writes, the seconds aside, and it is written
where run_one writes it (crossings_<name>.json, with the key "written by").  Each bracket's entry is also appended, as it
finishes, to post_run_poles_<name>.jsonl, which makes the run resume-safe.  The pole test is X1's: b changes sign between the
two frames and |b/a| >= 10 at one of them.
Usage: python3 post_run_poles.py [--workers N]   (both signs of LLLRLRR)"""
import json
import sys
import time
import warnings
from multiprocessing import Pool
from pathlib import Path

warnings.filterwarnings("ignore")
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import mpmath as mp  # noqa: E402
import numpy as np  # noqa: E402

import crossings as C  # noqa: E402

STATES = [("+", "LLLRLRR"), ("-", "LLLRLRR")]
POLE_B = 10                          # X1's zero test: a sign change of b is a zero of b when |b/a| < 10 at both frames
_SETUP = {}


def brackets_with_poles(name):
    """crossings.brackets(name), each tagged with X1's pole test; the list is checked equal to the sealed one"""
    x1 = json.loads((C.B1527 / ("x1_" + name + ".json")).read_text())
    grid, a = x1["grid"], x1["a"]
    out = []
    for k in range(len(grid)):
        g, h = grid[k], grid[(k + 1) % len(grid)]
        if not (g["converged"] and h["converged"]) or abs(g["b"]) > C.GRID_B_MAX * a or abs(h["b"]) > C.GRID_B_MAX * a:
            continue
        pole = bool(np.sign(g["b"]) != np.sign(h["b"]) and not (abs(g["b"]) < POLE_B * a and abs(h["b"]) < POLE_B * a))
        for kind, f in C.FUNCS.items():
            if np.sign(f(g["psi_a(l)"], g["psi_b(l)"])) != np.sign(f(h["psi_a(l)"], h["psi_b(l)"])):
                hi = h["alpha0"] if h["alpha0"] > g["alpha0"] else h["alpha0"] + 360
                out.append({"kind": kind, "between": [g["alpha0"], hi], "pole": pole,
                            "b/a at the frames": [g["b"] / a, h["b"] / a]})
    sealed = C.brackets(name)
    assert [{"kind": b["kind"], "between": b["between"]} for b in out] == sealed, name
    return out


def setup(sign, word):
    """what run_one builds before its loop, once per worker and state"""
    if (sign, word) not in _SETUP:
        G, img = C.FL.word_group(sign, word)
        chars, D = C.FL.torsion_characters(img)
        P64 = C.X1.Pinned(sign, word)
        P60 = C.XC.Problem(sign, word)
        _SETUP[(sign, word)] = (G, img, chars, D, P64, P60)
    return _SETUP[(sign, word)]


def one(job):
    """run_one's loop body for one bracket, unchanged"""
    sign, word, k, br = job
    G, img, chars, D, P64, P60 = setup(sign, word)
    t1 = time.time()
    loc, V = C.locate(P64, P60, br, G, img)
    entry = {"kind": br["kind"], "bracket (deg)": br["between"], "locate": loc}
    if V is not None:
        Xl, Yl = V[48], V[49]
        entry["alpha (deg)"] = float(mp.degrees(mp.atan2(Yl, Xl)) % 360)
        entry["b/a"] = mp.nstr(V[52] / C.A, 12)
        entry["crossing function / a"] = mp.nstr(C.FUNCS[br["kind"]](C.A * Xl, V[52] * Yl) / C.A, 3)
        entry["read"] = C.read(sign, word, G, img, V, br["kind"], chars, D)
    entry["seconds"] = round(time.time() - t1)
    return sign, word, k, entry


def main():
    args = sys.argv[1:]
    workers = int(args[args.index("--workers") + 1]) if "--workers" in args else 4
    t0 = time.time()
    tagged, done, jobs_first, jobs_pole = {}, {}, [], []
    for sign, word in STATES:
        name = C.R.name_of(sign, word)
        tagged[name] = brackets_with_poles(name)
        f = HERE / ("post_run_poles_" + name + ".jsonl")
        done[name] = {}
        if f.exists():
            for line in f.read_text().splitlines():
                r = json.loads(line)
                done[name][r["index"]] = r["entry"]
        for k, b in enumerate(tagged[name]):
            if k in done[name]:
                continue
            job = (sign, word, k, {"kind": b["kind"], "between": b["between"]})
            (jobs_pole if b["pole"] else jobs_first).append(job)
        print(f"{sign}{word}: {len(tagged[name])} brackets, {sum(b['pole'] for b in tagged[name])} through a pole; "
              f"{len(done[name])} already done", flush=True)
    with Pool(workers) as pool:
        for sign, word, k, entry in pool.imap_unordered(one, jobs_first + jobs_pole, chunksize=1):
            name = C.R.name_of(sign, word)
            done[name][k] = entry
            with open(HERE / ("post_run_poles_" + name + ".jsonl"), "a") as fh:
                fh.write(json.dumps({"index": k, "entry": entry}, default=str) + "\n")
            br = tagged[name][k]
            print(f"{sign}{word} {br['kind']} {br['between']}: converged {entry['locate'].get('converged')}, "
                  f"alpha {entry.get('alpha (deg)')}, {entry['seconds']} s{'  (pole bracket)' if br['pole'] else ''}",
                  flush=True)
    for sign, word in STATES:
        name = C.R.name_of(sign, word)
        brs = tagged[name]
        G, img = C.FL.word_group(sign, word)
        chars, D = C.FL.torsion_characters(img)
        mp.mp.dps = C.XC.DPS                       # run_one writes "a" after XC.Problem has set the precision
        res = {"manifold": sign + word, "a": mp.nstr(C.A, 20), "D": D, "brackets": len(brs),
               "brackets by kind": {kd: sum(1 for b in brs if b["kind"] == kd) for kd in C.FUNCS},
               "crossings": [done[name][k] for k in range(len(brs))],
               "seconds": sum(done[name][k]["seconds"] for k in range(len(brs))),
               "written by": "post_run_poles.py: run_one's loop body unchanged, one process per bracket (disclosed in "
                             "FINDINGS); 'seconds' is the sum over brackets, not the wall time"}
        (HERE / ("crossings_" + name + ".json")).write_text(json.dumps(res, indent=1, default=str))
        print(f"wrote crossings_{name}.json: {len(brs)} brackets, "
              f"{sum(1 for e in res['crossings'] if 'read' in e)} located", flush=True)
    print(f"post_run_poles: {round(time.time() - t0)} s", flush=True)


if __name__ == "__main__":
    main()
