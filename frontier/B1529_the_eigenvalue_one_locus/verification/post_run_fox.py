#!/usr/bin/env python3
"""B1529 post-run check (written after the census reported its first base-condition failure; disclosed in FINDINGS).

Where the census finds the four's base condition failing on a word state (h1 > t0 at a base point: an interior class of the
twisted geometric four at the hyperbolic point), this re-reads every such base point by the two banked routes of sm:B1527, which
share no linear algebra with route T.  The census's other failures are on the level M_6, where they reproduce sm:B1515's banked
classes (P3; read there by three methods) and are not re-read here.  The routes:
  - route Fox (cusp_lib.class_index): (a0, h1, t0, r1, n) for V and V*, the index, B1297's identity, the annihilator identity
    and Lemma E;
  - route W (wang_lib.index_wang): h1 by the Wang sequence on the fibre with the full module (its own ranks).
It also reads, for contrast, the base condition by both routes at every other character of the same states.
The module is nu (x) rho_hyp with nu = (zeta^i, zeta^j, lambda_c(u)) as sm:B1527's run.py builds it (lambda_c makes nu trivial on
the cusp).  Writes post_run_fox.json and prints one line per state."""
import json
import sys
import time
import warnings
from fractions import Fraction
from pathlib import Path

warnings.filterwarnings("ignore")
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import mpmath as mp  # noqa: E402

import fibre_lib as T  # noqa: E402

mp.mp.dps = 60
FL = T.load_b1527("family_lib")
L = T.load_b1527("cusp_lib")
R = T.load_b1527("run")
WL = T.load_b1527("wang_lib")


def failing_states():
    out = {}
    for line in (HERE / "census.jsonl").read_text().splitlines():
        r = json.loads(line)
        if "error" in r or r.get("level"):
            continue
        fails = r["4"]["base condition fails at"]
        if fails:
            out[r["state"]] = {"read as": r["read as"], "level": r.get("level"), "points": fails}
    return out


def read_state(read_as):
    sign, word = read_as[0], read_as[1:]
    G, img = FL.word_group(sign, word)
    mats = T.hyperbolic_mats(sign, word)
    chars, D = FL.torsion_characters(img)
    rows = []
    for u in chars:
        lc = R.lambda_c(sign, u)
        nu = R.nu_of(u, lc)
        m = R.twisted(mats, nu, wedge=False)
        fox = L.class_index(G, L.Module(m))
        w = WL.index_wang(img, G.cusp, m)
        rows.append({"u": [str(u[0]), str(u[1])],
                     "Fox (h1, h1*, t0, s0)": [fox["V"]["h1"], fox["V*"]["h1"], fox["V"]["t0"], fox["V*"]["t0"]],
                     "Fox n(V), n(V*)": [fox["V"]["n"], fox["V*"]["n"]], "Fox I": fox["I"],
                     "Fox identities": all(fox["checks"].values()), "Fox margins": fox["margins"],
                     "W (h1, h1*, t0, s0)": [w["h1(V)"], w["h1(V*)"], w["t0"], w["s0"]], "W I": w["I"],
                     "W margins": w["margins"]})
    return rows, D


def main():
    t0 = time.time()
    states = failing_states()
    out = {"states": {}, "seconds": None}
    for st, rec in states.items():
        rows, D = read_state(rec["read as"])
        bad = {tuple(p["u"]) for p in rec["points"]}
        census_fail = {tuple(p["u"]): p["(h1, h1*, t0, s0)"] for p in rec["points"]}
        fox_fail = {tuple(r["u"]): r["Fox (h1, h1*, t0, s0)"] for r in rows if r["Fox (h1, h1*, t0, s0)"] != [1, 1, 1, 1]}
        w_fail = {tuple(r["u"]): r["W (h1, h1*, t0, s0)"] for r in rows if r["W (h1, h1*, t0, s0)"] != [1, 1, 1, 1]}
        out["states"][st] = {
            "read as": rec["read as"], "level": rec["level"], "D": D,
            "census failures": {"/".join(k): v for k, v in census_fail.items()},
            "Fox failures": {"/".join(k): v for k, v in fox_fail.items()},
            "W failures": {"/".join(k): v for k, v in w_fail.items()},
            "the three routes agree": census_fail == fox_fail == w_fail,
            "every Fox identity holds": all(r["Fox identities"] for r in rows),
            "I = 0 on every row (both routes)": all(r["Fox I"] == 0 and r["W I"] == 0 for r in rows),
            "interior classes n(V) at the failures": {"/".join(r["u"]): r["Fox n(V), n(V*)"] for r in rows
                                                      if tuple(r["u"]) in bad},
            "rows": rows}
        o = out["states"][st]
        print(f"{st} ({rec['read as']}): census {len(census_fail)}, Fox {len(fox_fail)}, W {len(w_fail)} failures; "
              f"agree {o['the three routes agree']}; identities {o['every Fox identity holds']}; I = 0 {o['I = 0 on every row (both routes)']}",
              flush=True)
    out["seconds"] = round(time.time() - t0)
    (HERE / "post_run_fox.json").write_text(json.dumps(out, indent=1, default=str))


if __name__ == "__main__":
    main()
