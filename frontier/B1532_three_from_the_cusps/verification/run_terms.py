#!/usr/bin/env python3
"""B1532 -- THE SEALED RUN: every twisted term of every lam = 1 member on M2-M6, by one route.

    python3 -u run_terms.py --route T --workers 3          (route T at sm:B1515's first route-T prime of each level)
    python3 -u run_terms.py --route L --workers 3          (route L at sm:B1515's first route-L prime of each level)
    python3 -u run_terms.py --route T --part0              (Part 0 only)

Part 0  the banked identity, read first and stopping the run if it fails: every chi = 1 term against sm:B1515's census rows
        (census_t_run.txt for route T, census_l_run.txt for route L) at the same prime -- the one-class members' c1 rows, and
        the two-class members' generic class against the banked "generic" row (I and the B1297 dimensions of W1 and Lambda^2 W1).
Part A  the terms: for every level n = 2..6, every member nu and every chi in T_n^: a one-class member's term; a two-class
        member's interior, generic and special terms with the four pencils (gen2, a second generic class, on the members whose
        hash puts them in the one-in-eight sample).  One JSON row per (n, nu, chi) in terms_<route>.jsonl; a member is
        complete when its "done" row is written, and a restart skips complete members (resume-safe).
Nothing is summed here; read_out.py reads both routes' files."""
import argparse
import json
import multiprocessing as mp_
import os
import sys
import time
from fractions import Fraction as Fr
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
ROOT = Path(os.environ.get("ORIGIN_AXIOM_ROOT", HERE.parents[2]))
B1515 = ROOT / "frontier/B1515_the_hyperbolic_point/verification"
LEVELS = (2, 3, 4, 5, 6)
_CTX = {}


def banked(route):
    rec = json.loads((B1515 / ("census_t_run.txt" if route == "T" else "census_l_run.txt")).read_text(encoding="utf-8"))
    return rec


def primes(route):
    rec = banked(route)
    return {n: rec["primes"][f"M{n}"][0] for n in LEVELS}


def gen2_sample(n, label):
    import hashlib
    return int(hashlib.sha256(f"B1532 gen2:{n}:{label}".encode()).hexdigest(), 16) % 8 == 0


# ============================================================================================ the per-route adapters
def level(route, n, p):
    if route == "T":
        import cover_lib_t as C
        L = C.LevelT(n, p)
        return L, list(L.chars), (lambda ab: C.MemberT(L, ab)), (0, 0)
    import cover_lib_l as C
    L = C.LevelL(n, p)
    return L, list(L.chars), (lambda ab: C.MemberL(L, ab)), (Fr(0), Fr(0))


def norm_label(route, L, ab):
    """the shared label: (a, b) as reduced fractions of the fibre character's exponents"""
    return L.label(ab)


def read_member(route, n, p, ab):
    key = (route, n, p)
    if key not in _CTX:
        _CTX.clear()
        _CTX[key] = level(route, n, p)
    L, chars, make, one = _CTX[key]
    m = make(ab)
    lab = norm_label(route, L, ab)
    rows = []
    g2 = gen2_sample(n, lab)
    for chi in chars:
        row = {"route": route, "p": p, "n": n, "nu": lab, "chi": norm_label(route, L, chi), "kind": m.kind}
        if m.kind == "one":
            row.update(m.read_one(chi))
        else:
            row.update(m.read_two(chi, gen2=g2))
        rows.append(row)
    return n, lab, rows


# ============================================================================================ Part 0
def part0(route, log):
    rec = banked(route)
    ps = primes(route)
    bad, n_ok = [], 0
    for n in LEVELS:
        L, chars, make, one = level(route, n, ps[n])
        field = f"GF({ps[n]})"
        rows = {",".join(r["char"]): r["row"] for r in rec["A"] if r["level"] == n and r["field"] == field and r["lam"] == "1"}
        assert len(rows) == len(chars), ("banked rows", n, len(rows), len(chars))
        for ab in chars:
            lab = L.label(ab)
            b = rows[lab]
            m = make(ab)
            if m.kind == "one":
                t = m.read_one(one)["c"]
                bw = b["W1"]["c1"]
            else:
                t = m.term(m.cls_at(m.s_gen[0]), (L.exponents(one) if route == "T" else one))
                bw = b["W1"]["generic"]
            if route == "T":
                want = [[bw["W1"]["I"]] + bw["W1"]["E(a0,a1,t0,r1)"] + bw["W1"]["E*(b0,b1,s0,q1)"],
                        [bw["L2W1"]["I"]] + bw["L2W1"]["E(a0,a1,t0,r1)"] + bw["L2W1"]["E*(b0,b1,s0,q1)"]]
            else:
                want = [[bw["W1"]["I"]] + bw["W1"]["E(a0,h1,t0,n)"] + bw["W1"]["E*(b0,h1,s0,n)"],
                        [bw["L2W1"]["I"]] + bw["L2W1"]["E(a0,h1,t0,n)"] + bw["L2W1"]["E*(b0,h1,s0,n)"]]
            if t != want or b["h1(V_eta)"] != m.h1:
                bad.append((n, lab, t, want))
            else:
                n_ok += 1
        log(f"Part 0 route {route}: M{n} read ({len(chars)} members)")
    passed = not bad
    log(f"Part 0 route {route}: {n_ok} chi = 1 terms equal sm:B1515's banked rows, {len(bad)} differ; passed = {passed}")
    return {"agree": n_ok, "differ": bad[:20], "passed": passed}


# ============================================================================================ Part A
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--route", choices=("T", "L"), required=True)
    ap.add_argument("--workers", type=int, default=3)
    ap.add_argument("--part0", action="store_true")
    ap.add_argument("--levels", default=",".join(map(str, LEVELS)))
    a = ap.parse_args()
    out = HERE / f"terms_{a.route}.jsonl"
    logf = HERE / f"terms_{a.route}_log.txt"
    t0 = time.time()

    def log(msg):
        line = f"[{time.time() - t0:9.1f}s] {msg}"
        print(line, flush=True)
        with open(logf, "a", encoding="utf-8") as fh:
            fh.write(line + "\n")
    p0 = part0(a.route, log)
    (HERE / f"part0_{a.route}.json").write_text(json.dumps(p0, indent=1, default=str) + "\n", encoding="utf-8")
    if not p0["passed"] or a.part0:
        log("stopping after Part 0" + ("" if p0["passed"] else ": the banked identity FAILED, nothing of the census is read"))
        return
    ps = primes(a.route)
    done = set()
    if out.exists():
        for line in out.read_text(encoding="utf-8").splitlines():
            r = json.loads(line)
            if r.get("done"):
                done.add((r["n"], r["nu"]))
    tasks = []
    for n in map(int, a.levels.split(",")):
        L, chars, make, one = level(a.route, n, ps[n])
        for ab in chars:
            if (n, L.label(ab)) not in done:
                tasks.append((a.route, n, ps[n], ab))
    log(f"Part A route {a.route}: {len(tasks)} members to read ({len(done)} complete before this start)")
    with mp_.get_context("fork").Pool(a.workers) as pool, open(out, "a", encoding="utf-8") as fh:
        for k, (n, lab, rows) in enumerate(pool.imap_unordered(_task, tasks, chunksize=1), start=1):
            for r in rows:
                fh.write(json.dumps(r, separators=(",", ":")) + "\n")
            fh.write(json.dumps({"done": True, "route": a.route, "n": n, "nu": lab, "rows": len(rows)}) + "\n")
            fh.flush()
            if k % 10 == 0 or k == len(tasks):
                log(f"M{n} {lab}: {k}/{len(tasks)} members read")
    log(f"Part A route {a.route}: complete")


def _task(t):
    return read_member(*t)


if __name__ == "__main__":
    main()
