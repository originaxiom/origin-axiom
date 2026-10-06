#!/usr/bin/env python3
"""B1544 -- controls K1-K6, before the seal (no count at a class of K0 is read here, except at the interior classes of the
degree-60 covers, whose counts are banked: sm:B1542).

  K1  structure, in both routes on all five covers: h^1(rho), n(rho), h^1(C), n(1), the dimension of K0, its meeting with the
      interior part, its split over the deck group's eigenspaces, the cusp labels, the deck group's action on the cusps and the
      closed supports of K0 with dim K0(S).  The routes must agree, and the values must be the sealed ones (run.STRUCTURE).
  K2  the cochain formula for the cup map against the long exact sequence: at three random classes of H^1(N; rho) per cover and
      route, rk delta1_W by the cochain formula equals h1(V) + h1(L) - h1(W) - 1; and at a random class of K0, both are 0.
  K3  the positive control: a generic interior class reads the banked count in both routes -- (4, -10) on N_45 (sm:B1541),
      (-1, -3) on d10.13's and d10.36's covers and (0, -5) on d10.16's and d10.40's (sm:B1542).
  K4  the read-out on synthetic rows (read_out.evaluate is pure).
  K5  the cusps: route F's and route R's cusps (orbits of the base cusp group) coincide as point sets, and the two routes'
      deck transformations are the same permutation of the points.
  K6  Lemma F's ingredients at a generic class of H^1(N; rho) and at K3's interior class, in both routes: h0(dN; W*) = 2m,
      h1(dN; W) = 4m - k, r1(W) <= 3m - k, I(W) = -1 + h0(dN; W*) - r1(W) >= k - m - 1, with k the size of the class's support
      (all cusps, and none); and the generic class reads the banked count of the full cusp stratum: (5, -5) on N_45, (2, -3)
      on d10.13's and d10.36's covers, (3, -4) on d10.16's and d10.40's.

    python3 controls.py [--record]   ->  controls.json"""
import importlib.util
import json
import random
import sys
import time
import zlib
from pathlib import Path

HERE = Path(__file__).resolve().parent


def load(name, path):
    """a module of this arc, by path under its own name (E12)"""
    if name not in sys.modules:
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        sys.modules[name] = mod
        spec.loader.exec_module(mod)
    return sys.modules[name]


FL = load("b1544_floor_lib", HERE / "floor_lib.py")
RUN = load("b1544_run", HERE / "run.py")

EXPECTED = {
    "N45": {"h1(rho)": 23, "n(rho)": 18, "h1(C)": 9, "n(1)": 4, "dim K0": 5, "K0 meets the interior in": 0,
            "K0 by eigenspace": [1, 1, 1, 1, 1]},
    "d10.13": {"h1(rho)": 9, "n(rho)": 3, "h1(C)": 9, "n(1)": 3, "dim K0": 6, "K0 meets the interior in": 3,
               "K0 by eigenspace": [4, 0, 0, 2, 0, 0]},
    "d10.16": {"h1(rho)": 11, "n(rho)": 7, "h1(C)": 7, "n(1)": 3, "dim K0": 3, "K0 meets the interior in": 2,
               "K0 by eigenspace": [3, 0, 0, 0, 0, 0]},
}
EXPECTED["d10.36"] = dict(EXPECTED["d10.13"])
EXPECTED["d10.40"] = dict(EXPECTED["d10.16"])
for _cid, _st in RUN.STRUCTURE.items():
    EXPECTED[_cid] = dict(EXPECTED[_cid], **{"cusp labels": sorted(_st["tau"]), "tau on the cusps": dict(_st["tau"]),
                                             "closed supports of K0 [S, dim K0(S)]": _st["closed"]})
BANKED_INTERIOR = {"N45": [4, -10], "d10.13": [-1, -3], "d10.36": [-1, -3], "d10.16": [0, -5], "d10.40": [0, -5]}
BANKED_GENERIC = {"N45": [5, -5], "d10.13": [2, -3], "d10.36": [2, -3], "d10.16": [3, -4], "d10.40": [3, -4]}


def lemma_f_ok(x):
    lf, k = x["lemma F"], len(x["support"])
    m = lf["m"]
    return (lf["h0(dN;W*)"] == 2 * m and lf["h1(dN;W)"] == 4 * m - k and lf["r1(W)"] <= 3 * m - k
            and x["count"][0] == -1 + lf["h0(dN;W*)"] - lf["r1(W)"] and x["count"][0] >= k - m - 1)


def main():
    t0 = time.time()
    rep = {}
    pF = FL.F().primes(1)[0]
    rep["prime (route F)"] = pF
    k1, k2, k3, k5, k6 = {}, {}, {}, {}, {}
    for cid in FL.COVERS:
        fc = FL.FCover(cid, pF)
        rc = FL.RCover(cid)
        sF, sR = FL.structure(fc), FL.structure(rc)
        sF["tau on the cusps"] = {int(a): int(b) for a, b in sF["tau on the cusps"].items()}
        sR["tau on the cusps"] = {int(a): int(b) for a, b in sR["tau on the cusps"].items()}
        k1[cid] = {"route F": sF, "route R": sR, "prime (route R)": rc.p, "holds": sF == sR == EXPECTED[cid]}
        rows = []
        for name, Cv in (("F", fc), ("R", rc)):
            rng = random.Random(zlib.crc32(f"B1544|K2|{cid}|{name}".encode()))
            B = Cv.Call if name == "F" else Cv.Cs
            for _ in range(3):
                c = Cv.draw(B, rng)
                rows.append([name, "generic", Cv.rk_cup(c), Cv.rk_les(c)])
            c = Cv.draw(Cv.K0(), rng)
            rows.append([name, "K0", Cv.rk_cup(c), Cv.rk_les(c)])
        k2[cid] = {"readings (route, class, cochain rank, LES rank)": rows,
                   "holds": all(r[2] == r[3] for r in rows) and all(r[2] == 0 for r in rows if r[1] == "K0")}
        cnt, lf = {}, {}
        for name, Cv in (("F", fc), ("R", rc)):
            rng = random.Random(zlib.crc32(f"B1544|K3|{cid}|{name}".encode()))
            x = Cv.reading(Cv.draw(Cv.Cint, rng))
            cnt[name] = x["count"]
            rng = random.Random(zlib.crc32(f"B1544|K6|{cid}|{name}".encode()))
            g = Cv.reading(Cv.draw(Cv.Call if name == "F" else Cv.Cs, rng))
            lf[name] = {"interior": {"count": x["count"], "support": x["support"], "lemma F": x["lemma F"],
                                     "holds": lemma_f_ok(x) and x["support"] == []},
                        "generic": {"count": g["count"], "support": g["support"], "lemma F": g["lemma F"],
                                    "holds": lemma_f_ok(g) and g["support"] == sorted(fc.labels)
                                    and g["count"] == BANKED_GENERIC[cid]}}
        k3[cid] = {"interior count (route F, route R)": [cnt["F"], cnt["R"]], "banked": BANKED_INTERIOR[cid],
                   "holds": cnt["F"] == cnt["R"] == BANKED_INTERIOR[cid]}
        k6[cid] = dict(lf, holds=all(v["holds"] for d in lf.values() for v in d.values()))
        fo = sorted(sorted(T["orbit"]) for T in fc.cov.cusps)
        ro = sorted(sorted(T["orbit"]) for T in rc.cov.cusp_list)
        k5[cid] = {"cusps (orbit sizes)": sorted(len(o) for o in fo), "holds": fo == ro and list(fc.tau) == list(rc.tau)}
        print(cid, json.dumps(k1[cid]), json.dumps(k2[cid]), json.dumps(k3[cid]), json.dumps(k5[cid]), json.dumps(k6[cid]),
              round(time.time() - t0, 1), "s", flush=True)
    rep["K1"] = dict(k1, holds=all(v["holds"] for v in k1.values()))
    rep["K2"] = dict(k2, holds=all(v["holds"] for v in k2.values()))
    rep["K3"] = dict(k3, holds=all(v["holds"] for v in k3.values()))
    RO = load("b1544_read_out", HERE / "read_out.py")    # by path: sm:B1536's population.py puts its own read_out first (E12)
    rep["K4"] = RO.selftest()
    rep["K5"] = dict(k5, holds=all(v["holds"] for v in k5.values()))
    rep["K6"] = dict(k6, holds=all(v["holds"] for v in k6.values()))
    rep["all hold"] = all(rep[k]["holds"] for k in ("K1", "K2", "K3", "K4", "K5", "K6"))
    rep["seconds"] = round(time.time() - t0, 1)
    print(json.dumps({k: (v["holds"] if isinstance(v, dict) and "holds" in v else v) for k, v in rep.items()}), flush=True)
    if "--record" in sys.argv:
        (HERE / "controls.json").write_text(json.dumps(rep, indent=1) + "\n")
    return rep


if __name__ == "__main__":
    sys.exit(0 if main()["all hold"] else 1)
