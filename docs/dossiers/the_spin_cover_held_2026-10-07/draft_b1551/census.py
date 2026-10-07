#!/usr/bin/env python3
"""sm:B1551 -- the design-time structure census (no count): on the root's spin cover S, every orbit of its deck group 2T
(= SL(2, F_3)) on the characters of order dividing 4. Route P~ (S's own presentation) reads every orbit's representative;
route S~ (Shapiro on N) reads every orbit with a member in route P~, and the first 100 orbits without one in the census's
own order (the named sample). h0, h1, r1, n of nu (x) rho with the gaps; m_A; the orbit's size; whether the character is
pulled back from N (fixed by the deck involution of S over N). One JSON line per orbit.

    python3 census.py WORKERS        ->  census.jsonl beside this file
    python3 census.py collect        ->  population.json (it reads the banked census.jsonl.gz when the raw record is absent)"""
import json
import multiprocessing as mpc
import sys
import time

import numpy as np

import spin_lib as S

T = S.T
HERE = S.HERE
M_ORDER = 4
SAMPLE = 100

_G = {}


def _setup():
    if not _G:
        SC = S.SpinCover()
        Pr, P = S.presentation_S(SC)
        _G.update(SC=SC, Pr=Pr)
    return _G["SC"], _G["Pr"]


def orbits():
    """the 2T orbits on S's characters of order dividing 4, each as a sorted list of characters (edge labellings)"""
    SC, Pr = _setup()
    chars = SC.characters(M_ORDER)
    K = np.array([S.key(SC, Pr, c, M_ORDER) for c in chars], dtype=np.int64)
    idx = {tuple(r): i for i, r in enumerate(K)}
    assert len(idx) == len(chars)
    mats = [np.array(M, dtype=np.int64) for M in S.action_matrices(SC, Pr)]
    parent = list(range(len(chars)))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for M in mats:
        for i, r in enumerate((K @ M.T) % M_ORDER):
            a, b = find(i), find(idx[tuple(r)])
            if a != b:
                parent[a] = b
    groups = {}
    for i in range(len(chars)):
        groups.setdefault(find(i), []).append(i)
    out = [sorted(chars[i] for i in g) for g in groups.values()]
    out.sort(key=lambda o: o[0])
    return out


def pulled_back(SC, Pr, c):
    """fixed by S's deck involution over N (conjugation by the sheet-changing coset representative)"""
    h = SC.u[SC.lab(0, 1)]
    vals = SC.rs_values(c, 0, M_ORDER)
    for (_, _, w) in Pr.gens:
        if SC.chi_exp(w, vals, M_ORDER) != SC.chi_exp(h + w + S.PC.inv_word(h), vals, M_ORDER):
            return False
    return True


def read_P(task):
    k, c, size = task
    SC, Pr = _setup()
    t0 = time.time()
    s = T.read_P(SC.level3, SC, c, 0, M_ORDER)["structure"]
    return {"orbit index": k, "rep": list(c), "size": size, "order": T.char_order((tuple(c), 0), M_ORDER),
            "m_A": len(SC.trivial_cusps(c, 0, M_ORDER)), "pulled back": pulled_back(SC, Pr, c), "P": s,
            "s P": round(time.time() - t0, 1)}


def read_S(row):
    SC, Pr = _setup()
    t0 = time.time()
    s = S.read_SN(SC, tuple(row["rep"]), M_ORDER)["structure"]
    row = dict(row)
    row["S"] = s
    row["s S"] = round(time.time() - t0, 1)
    return row


def run(workers):
    orbs = orbits()
    tasks = [(k, o[0], len(o)) for k, o in enumerate(orbs)]
    print(f"{len(tasks)} orbits", flush=True)
    with mpc.Pool(workers) as pool:
        rows = sorted(pool.imap_unordered(read_P, tasks, chunksize=8), key=lambda r: r["orbit index"])
        members = [r for r in rows if r["P"]["n"] > 0]
        sample = [r for r in rows if r["P"]["n"] == 0][:SAMPLE]
        both = {r["orbit index"]: r for r in pool.imap_unordered(read_S, members + sample)}
    with open(HERE / "census.jsonl", "w") as f:
        for r in rows:
            r = both.get(r["orbit index"], r)
            f.write(json.dumps(r) + "\n")
    print("rc 0", flush=True)


def _lines(path):
    import gzip
    if path.exists():
        return path.read_text().splitlines()
    return gzip.open(str(path) + ".gz", "rt").read().splitlines()


def collect():
    rows = [json.loads(x) for x in _lines(HERE / "census.jsonl") if x.strip()]
    orbs = orbits()
    assert len(rows) == len(orbs)
    st = lambda r, k: (r[k]["h1"], r[k]["r1"], r[k]["n"])
    read_both = [r for r in rows if "S" in r]
    members = [r for r in rows if r["P"]["n"] > 0 or ("S" in r and r["S"]["n"] > 0)]
    out = {"orbits read in route P~": len(rows), "orbits read in route S~": len(read_both),
           "routes agree wherever both read": all(st(r, "P") == st(r, "S") for r in read_both),
           "characters by (h1, r1, n), route P~": {str(list(k)): v for k, v in sorted(
               __import__("collections").Counter((r["P"]["h1"], r["P"]["r1"], r["P"]["n"]) for r in rows
                                                 for _ in range(r["size"])).items())},
           "member orbits": [{"orbit index": r["orbit index"], "orbit": [list(c) for c in orbs[r["orbit index"]]],
                              "size": r["size"], "order": r["order"], "m_A": r["m_A"], "pulled back": r["pulled back"],
                              "P": r["P"], "S": r["S"]} for r in members],
           "members": sum(r["size"] for r in members)}
    (HERE / "population.json").write_text(json.dumps(out, indent=1) + "\n")
    return out


if __name__ == "__main__":
    if sys.argv[1] == "collect":
        o = collect()
        print("orbits", o["orbits read in route P~"], "both routes", o["orbits read in route S~"], "member orbits",
              len(o["member orbits"]), "members", o["members"], "routes agree", o["routes agree wherever both read"])
    else:
        run(int(sys.argv[1]))
