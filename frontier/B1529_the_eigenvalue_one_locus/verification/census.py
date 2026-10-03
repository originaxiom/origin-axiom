#!/usr/bin/env python3
"""B1529 instrument (a): the base census.  Written and committed with PREREGISTRATION.md before it was run on any state.

On every word state to length 12 (sm:B1523's 536 manifolds, one state each, the state B1523's route F read; a cyclic rotation of
the word where B1523 read one), and on m004's levels M_2 .. M_6 (the bundles of (LR)^n), at the hyperbolic point (sm:B1527 family_lib: route F seeded, Ballas' paraboloid frame, 60
digits), for every torsion character u of F at its lambda_c (there nu(t') = 1 for both signs), for the four and Lambda^2:
  route T (fibre_lib): T_C on C = H^1(F; nu0 (x) W) and T_C' for the dual (nu0^-1 (x) W*), the cusp ends A = W^l, D = W_l;
    am(C; 1)   the order of vanishing of chi_C at 1 (Taylor coefficients, with margins),
    am(D; 1)   the same for chi_D (W(t')^-1 on D),
    e          dim W^l,
    g(C; 1) = h1(V),  g(C'; 1) = h1(V*),  g(A; 1) = t0,  g(D; 1) = s0,  I by Lemma F,
    chi_K(1)   (chi_C / chi_D)(1), relative, with the division's remainder,
    and route T's hypothesis H^0(F; V) = H^0(F; V*) = 0.
Sealed (PREREGISTRATION section 7): P1 SR for Lambda^2: am(C; 1) = am(C'; 1) = am(D; 1) = 2 at every base point (word states and
levels); P2 the four's base condition: h1 = h1* = t0 = s0 = 1 at every base point of every word state (on the levels it is banked:
it fails at 28 characters of M_6, sm:B1515); P3 the theorems' controls: Lambda^2's h1 = h1* = t0 = s0 = 2, I = 0 for both modules,
e = am(D; 1) = 2 for both modules, route T's hypothesis, everywhere.  Recorded, not predicted: the four's am(C; 1) and chi_K(1).
Writes census.jsonl (one line per manifold, appended as each finishes; a rerun skips manifolds already written) and, with
--summary, census.json.
Usage: python3 census.py [--workers 4] [--only STATE ...]   then   python3 census.py --summary"""
import json
import sys
import time
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import mpmath as mp  # noqa: E402

import fibre_lib as T  # noqa: E402

ROOT = HERE.parents[2]
B1523 = ROOT / "frontier" / "B1523_the_flexible_states" / "verification"
OUT = HERE / "census.jsonl"
LUCAS_EVEN = {3, 7, 18, 47, 123, 322}          # L_2k, k = 1..6: |trace| of a golden monodromy (eigenvalues phi^(+-2k))


LEVELS = ["+" + "LR" * n for n in range(2, 7)]  # m004's levels M_2 .. M_6 (M_1 = +LR is a word state)


def states():
    """sm:B1523's 536 states (route_f_seeded.jsonl, in its order), with the rotation B1523 read where it read one; then m004's
    levels M_2 .. M_6 (the bundles of (LR)^n, sm:B1506, sm:B1511, sm:B1515)"""
    out = []
    for line in (B1523 / "route_f_seeded.jsonl").read_text().splitlines():
        d = json.loads(line)
        out.append((d["state"], d.get("rotation read")))
    return out + [(lv, None) for lv in LEVELS]


def hyperbolic(state, rotation):
    FL = T.load_b1527("family_lib")
    tried = [state] + ([rotation] if rotation and rotation != state else [])
    last = None
    for st in tried:
        try:
            mats = T.hyperbolic_mats(st[0], st[1:])
            return st, mats
        except RuntimeError as exc:          # no seed reached a root with SnapPy's cusp shape
            last = exc
    raise last


def margin_min(cur, x):
    return x if cur is None or (x is not None and x < cur) else cur


def margin_max(cur, x):
    return x if cur is None or (x is not None and x > cur) else cur


def one(job):
    state, rotation = job
    mp.mp.dps = T.DPS
    t0 = time.time()
    FL = T.load_b1527("family_lib")
    L = T.load_b1527("cusp_lib")
    try:
        st, mats = hyperbolic(state, rotation)
    except Exception as exc:  # noqa: BLE001
        return {"state": state, "error": repr(exc), "seconds": round(time.time() - t0)}
    sign, word = st[0], st[1:]
    G, img = FL.word_group(sign, word)
    chars, D = FL.torsion_characters(img)
    M = FL.homology_matrix(img)
    trace = M[0][0] + M[1][1]
    rec = {"state": state, "read as": st, "level": state in LEVELS, "D": D, "trace": trace,
           "golden": abs(trace) in LUCAS_EVEN,
           "relator residual": mp.nstr(L.relator_residual(G, L.Module(mats)), 3)}
    SM = T.StateModules(sign, img, mats, D)
    one_ = mp.mpf(1)
    for name in ("4", "L2"):
        m = SM.mods[name]
        chiD = T.acb_of_mp(m["TD"]).charpoly() if m["e"] else T.acb_poly([T.acb(1)])
        amD = T.order_at(chiD, T.acb(1)) if m["e"] else (0, None, None)
        s = {"e": m["e"], "am(D; 1)": amD[0], "rows": 0, "am(C; 1) values": {}, "am(C'; 1) values": {},
             "(h1, h1*, t0, s0) values": {}, "I values": {}, "hypothesis fails": 0,
             "SR fails at": [], "base condition fails at": [],
             "margins": {"am: largest zero": None, "am: first non-zero": None, "g: smallest kept": None,
                         "g: largest dropped": None, "slot conditioning": None, "|chi_K(1)| rel, smallest": None,
                         "division remainder rel, largest": None}}
        want = 2 if name == "L2" else 1
        for u in chars:
            i, j = T.int_char(u, D)
            (TC, slot, cond), f0 = SM.TC(name, "V", i, j)
            (TCd, slotd, condd), f0d = SM.TC(name, "V*", -i, -j)
            pc, pcd = TC.charpoly(), TCd.charpoly()
            amC, amCd = T.order_at(pc, T.acb(1)), T.order_at(pcd, T.acb(1))
            rt = SM.row(name, i, j, one_)
            iv = T.interior_value(pc, m["TD"], one_)
            s["rows"] += 1
            for key, val in (("am(C; 1) values", amC[0]), ("am(C'; 1) values", amCd[0]),
                             ("(h1, h1*, t0, s0) values", (rt["h1"], rt["h1*"], rt["t0"], rt["s0"])),
                             ("I values", rt["I"])):
                s[key][str(val)] = s[key].get(str(val), 0) + 1
            if rt["H0(F; V), H0(F; V*)"] != [0, 0]:
                s["hypothesis fails"] += 1
            if not (amC[0] == amD[0] == amCd[0] == m["e"]):
                s["SR fails at"].append({"u": [str(u[0]), str(u[1])], "am(C)": amC[0], "am(C')": amCd[0],
                                         "chi_K(1) rel": mp.nstr(iv["chi_K(kappa) rel"], 3)})
            if (rt["h1"], rt["h1*"], rt["t0"], rt["s0"]) != (want, want, want, want):
                s["base condition fails at"].append({"u": [str(u[0]), str(u[1])],
                                                     "(h1, h1*, t0, s0)": [rt["h1"], rt["h1*"], rt["t0"], rt["s0"]]})
            mg = s["margins"]
            for a in (amC, amCd):
                mg["am: largest zero"] = margin_max(mg["am: largest zero"], a[1])
                mg["am: first non-zero"] = margin_min(mg["am: first non-zero"], a[2])
            mg["g: smallest kept"] = margin_min(mg["g: smallest kept"], rt["kept"])
            mg["g: largest dropped"] = margin_max(mg["g: largest dropped"], rt["dropped"])
            mg["slot conditioning"] = margin_min(mg["slot conditioning"], rt["slot conditioning"])
            mg["|chi_K(1)| rel, smallest"] = margin_min(mg["|chi_K(1)| rel, smallest"], iv["chi_K(kappa) rel"])
            mg["division remainder rel, largest"] = margin_max(mg["division remainder rel, largest"], iv["remainder rel"])
        s["margins"] = {k: (mp.nstr(v, 3) if v is not None else None) for k, v in s["margins"].items()}
        rec[name] = s
    rec["seconds"] = round(time.time() - t0)
    return rec


def run(workers, only=None):
    done = set()
    if OUT.exists():
        for line in OUT.read_text().splitlines():
            done.add(json.loads(line)["state"])
    todo = [s for s in states() if s[0] not in done and (only is None or s[0] in only)]
    print(f"census: {len(todo)} to do, {len(done)} done", flush=True)
    t0 = time.time()
    from multiprocessing import Pool
    with Pool(workers) as pool, OUT.open("a") as fh:
        for k, rec in enumerate(pool.imap_unordered(one, todo, chunksize=1), 1):
            fh.write(json.dumps(rec, default=str) + "\n")
            fh.flush()
            if k % 25 == 0 or k == len(todo):
                print(f"  {k}/{len(todo)} ({round(time.time() - t0)} s)", flush=True)


def summary():
    recs = [json.loads(line) for line in OUT.read_text().splitlines()]
    out = {"manifolds": len(recs), "word states": sum(1 for r in recs if not r.get("level")),
           "levels": sorted(r["state"] for r in recs if r.get("level")), "errors": [r for r in recs if "error" in r]}
    ok = [r for r in recs if "error" not in r]
    for name in ("4", "L2"):
        agg = {"base points": sum(r[name]["rows"] for r in ok), "e values": {}, "am(D; 1) values": {},
               "am(C; 1) values": {}, "(h1, h1*, t0, s0) values": {}, "I values": {}, "hypothesis fails": 0,
               "manifolds where SR fails": [], "manifolds where the base condition fails": []}
        for r in ok:
            s = r[name]
            for key in ("e", "am(D; 1)"):
                agg[key + " values"][str(s[key])] = agg[key + " values"].get(str(s[key]), 0) + 1
            for key in ("am(C; 1) values", "(h1, h1*, t0, s0) values", "I values"):
                for k, v in s[key].items():
                    agg[key][k] = agg[key].get(k, 0) + v
            agg["hypothesis fails"] += s["hypothesis fails"]
            if s["SR fails at"]:
                agg["manifolds where SR fails"].append({"state": r["state"], "level": r.get("level"), "golden": r["golden"],
                                                       "trace": r["trace"], "points": len(s["SR fails at"]),
                                                       "first": s["SR fails at"][:3]})
            if s["base condition fails at"]:
                agg["manifolds where the base condition fails"].append(
                    {"state": r["state"], "level": r.get("level"), "golden": r["golden"], "trace": r["trace"],
                     "points": len(s["base condition fails at"]), "first": s["base condition fails at"][:3]})
        out[name] = agg
    out["golden manifolds"] = sorted(r["state"] for r in ok if r["golden"])
    (HERE / "census.json").write_text(json.dumps(out, indent=1, default=str))
    print(json.dumps(out, indent=1, default=str)[:6000])


def main():
    args = sys.argv[1:]
    if "--summary" in args:
        summary()
        return
    workers = int(args[args.index("--workers") + 1]) if "--workers" in args else 4
    only = set(args[args.index("--only") + 1:]) if "--only" in args else None
    run(workers, only)


if __name__ == "__main__":
    main()
