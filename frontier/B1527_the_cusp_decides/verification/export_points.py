#!/usr/bin/env python3
"""B1527: the type-one points for main's L242 (e), exported without any reading (written at banking; disclosed in FINDINGS).

Main's L242 (e) is a blind second-route run of main's class index on the projective family of the first mirror-broken word
states, after this seat's seal. This file gives main the representations and nothing read from them: for each manifold its
presentation (generators a, b, t; relators t g T = phi(g); the cusp words), and for each type-one point the matrices of a,
b and t at 60 digits, with the frame, the line and the residual. No index, cohomology, eigenvalue or margin is written.
- X1's points are rebuilt from their banked frames as X2 rebuilds them (post_run_x2.rebuild: X1's pinned solve, then the
  b = 0 system in float64) and polished at 60 digits with X1's polish_gn to |F| < 1e-48 (the type-one system: the bundle
  relations, the two cusp words in Ballas' slice at a = 1e-5 and b = 0, det = 1 for a and b).
- X1c's two new points on -L4RLR3LR2 start from their banked 60-digit solutions and are polished the same way.
- Each exported point's frame (the angle of l's translation) must agree with the banked one to 1e-3 degrees.
Words are read left to right, rho(w) = rho(w[0]) rho(w[1]) ...; an upper-case letter is the inverse.
Writes points_for_l242e.json. Usage: python3 export_points.py [--workers 4]"""
import json
import sys
import time
import warnings
from multiprocessing import Pool
from pathlib import Path

warnings.filterwarnings("ignore")
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

DPS = 60
TOL = 48


def one(job):
    sign, word = job
    import mpmath as mp
    import family_lib as FL
    import post_run_x1 as X1
    import post_run_x2 as X2
    import run as R
    t0 = time.time()
    name = R.name_of(sign, word)
    x1 = json.loads((HERE / ("x1_" + name + ".json")).read_text(encoding="utf-8"))
    work = [("X1", p["frame alpha0"], p["alpha"], p["beta"], None) for p in x1["points"] if p.get("point")]
    x1c_path = HERE / ("x1c_" + name + ".json")
    if x1c_path.exists():
        work += [("X1c", e["alpha"], e["alpha"], e["beta"], e["point (60 digits)"])
                 for e in json.loads(x1c_path.read_text(encoding="utf-8"))["new points"]]
    G, img = FL.word_group(sign, word)
    P = X1.Pinned(sign, word)
    out = {"manifold": sign + word, "generators": ["a", "b", "t"], "relators": G.rels,
           "relators read as": "t g T = phi(g) for g = a, b, phi(a) = " + img["a"] + ", phi(b) = " + img["b"],
           "cusp words": list(G.cusp), "slice scale a": X1.A, "digits": DPS, "points": []}
    for source, frame, alpha, beta, u60 in work:
        if source == "X1":
            u1, _, _, _ = X2.rebuild(P, frame)
            mp.mp.dps = DPS
            U = mp.matrix([mp.mpf(x) for x in u1])
        else:
            mp.mp.dps = DPS
            U = mp.matrix([mp.mpf(x) for x in u60])
        Up, fp, it, _ = X1.polish_gn(U, mp.mpf(X1.A), G, img, tol=mp.mpf(10) ** -TOL, maxit=40)
        mats, (Xl, Yl, _, _) = FL.unpack(Up)
        got = float(mp.degrees(mp.atan2(Yl, Xl))) % 360.0
        d = abs(got - alpha % 360.0)
        d = min(d, 360.0 - d)
        out["points"].append({
            "source": source, "frame alpha (deg)": got, "banked alpha (deg)": alpha, "frame agrees (1e-3 deg)": d < 1e-3,
            "line beta (deg)": beta, "polished |F|": mp.nstr(fp, 3), "polish iterations": it,
            "matrices": {g: [[mp.nstr(mats[g][i, j], DPS) for j in range(4)] for i in range(4)] for g in "abt"}})
    out["seconds"] = round(time.time() - t0)
    return out


def main():
    import run as R
    workers = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else 4
    print(f"start {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}", flush=True)
    res = {}
    with Pool(workers) as pool:
        for rec in pool.imap_unordered(one, list(R.MANIFOLDS)):
            res[rec["manifold"]] = rec
            ok = sum(p["frame agrees (1e-3 deg)"] for p in rec["points"])
            worst = max((float(p["polished |F|"]) for p in rec["points"]), default=None)
            print(f"{rec['manifold']}: {rec['seconds']} s; points {len(rec['points'])}; frames agreeing {ok}; "
                  f"largest polished |F| {worst:.2e}", flush=True)
    order = [s + w for s, w in R.MANIFOLDS]
    doc = {"for": "main's L242 (e): the type-one points of sm:B1527, without readings",
           "manifolds": {m: res[m] for m in order if m in res}}
    (HERE / "points_for_l242e.json").write_text(json.dumps(doc, indent=1) + "\n", encoding="utf-8")
    n = sum(len(r["points"]) for r in res.values())
    bad = sum(1 for r in res.values() for p in r["points"] if not p["frame agrees (1e-3 deg)"] or float(p["polished |F|"]) >= 1e-48)
    print(f"points {n}; failing (frame or |F|) {bad}", flush=True)
    print(f"end {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}", flush=True)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
