#!/usr/bin/env python3
"""sm:B1551 -- the sealed run. Every member of population.json (every character of every member orbit of the spin cover),
in route P~ and route S~: the structure of nu (x) rho, then generic interior classes -- three at members whose interior
has dimension two or more, one where it is one-dimensional (a generic class is then the class up to scale) -- each with
its count (I(W1), I(Lambda^2 W1)) and the four module readings. Seeds: crc32 of "B1551|route|character|draw". One JSON
line per task, resumable (a task with its line is not read again).

    python3 run.py WORKERS   ->  run.jsonl beside this file"""
import json
import multiprocessing as mpc
import random
import sys
import time
import zlib

import spin_lib as S

T = S.T
HERE = S.HERE
M_ORDER = 4
_G = {}


def _sc():
    if "SC" not in _G:
        _G["SC"] = S.SpinCover()
    return _G["SC"]


def tasks():
    pop = json.loads((HERE / "population.json").read_text())
    out = []
    for oi, orb in enumerate(pop["member orbits"]):
        draws = 3 if orb["P"]["n"] >= 2 else 1
        for ch in orb["orbit"]:
            for route in ("P", "S"):
                out.append({"route": route, "character": ch, "orbit index": oi, "size": orb["size"],
                            "order": orb["order"], "m_A": orb["m_A"], "pulled back": orb["pulled back"],
                            "draws wanted": draws})
    return out


def key(t):
    return "|".join(["B1551", t["route"], ",".join(map(str, t["character"]))])


def seed(t, draw):
    return zlib.crc32((key(t) + "|" + str(draw)).encode())


def run_task(t):
    t0 = time.time()
    SC = _sc()
    c = tuple(t["character"])
    rngs = [random.Random(seed(t, k)) for k in range(t["draws wanted"])]
    if t["route"] == "P":
        r = T.read_P(SC.level3, SC, c, 0, M_ORDER, rngs)
    else:
        r = S.read_SN(SC, c, M_ORDER, rngs)
    row = dict(t)
    row.update({"key": key(t), "m_A (this character)": len(SC.trivial_cusps(c, 0, M_ORDER)), "b0": 1,
                "structure": r["structure"], "interior dimension": r.get("interior dimension"),
                "draws": r.get("draws", []), "seconds": round(time.time() - t0, 1)})
    return row


def main(workers):
    path = HERE / "run.jsonl"
    done = set()
    if path.exists():
        done = {json.loads(x)["key"] for x in path.read_text().splitlines() if x.strip()}
    todo = [t for t in tasks() if key(t) not in done]
    print(f"{len(todo)} tasks to read ({len(done)} done)", flush=True)
    with open(path, "a") as f, mpc.Pool(workers) as pool:
        for row in pool.imap_unordered(run_task, todo):
            f.write(json.dumps(row) + "\n")
            f.flush()
    print("rc 0", flush=True)


if __name__ == "__main__":
    main(int(sys.argv[1]))
