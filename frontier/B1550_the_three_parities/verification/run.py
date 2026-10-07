#!/usr/bin/env python3
"""sm:B1550 -- the sealed run. Every member of population.json (every character of every member orbit), in route P and
route S: the structure of nu (x) rho, then three generic interior classes, each with its count (I(W1), I(Lambda^2 W1)) and
the four module readings. Seeds: crc32 of "B1550|route|state|character|draw". One JSON line per task, resumable (a task
with its line is not read again).

    python3 run.py WORKERS   ->  run.jsonl beside this file"""
import json
import multiprocessing as mpc
import random
import sys
import time
import zlib

import tetra_lib as L

T = L.T
HERE = L.HERE
M_ORDER = L.M_ORDER
DRAWS = 3


def tasks():
    pop = json.loads((HERE / "population.json").read_text())
    out = []
    for oi, orb in enumerate(pop["member orbits"]):
        for ch in orb["orbit"]:
            info = orb["members"][json.dumps(ch)]
            for route in ("P", "S"):
                out.append({"route": route, "state": orb["state"], "level 3": orb["level 3"], "wbar": orb["wbar"],
                            "character": ch, "orbit index": oi, "size": orb["size"], "order": orb["order"],
                            "m_A": info["m_A"], "label": info["label"], "puncture values": info["puncture values"]})
    return out


def key(t):
    return "|".join(["B1550", t["route"], t["state"], ",".join(map(str, t["character"]))])


def seed(t, draw):
    return zlib.crc32((key(t) + "|" + str(draw)).encode())


def run_task(t):
    t0 = time.time()
    wl, C = L.tetra_cover(t["state"])
    assert wl == t["wbar"]
    ez, es = tuple(t["character"][:-1]), t["character"][-1]
    rngs = [random.Random(seed(t, k)) for k in range(DRAWS)]
    reader = T.read_P if t["route"] == "P" else T.read_S
    r = reader(t["level 3"], C, ez, es, M_ORDER, rngs)
    row = dict(t)
    row.update({"key": key(t), "m_A (this character)": len(C.trivial_cusps(ez, es, M_ORDER)), "b0": 1,
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
