#!/usr/bin/env python3
"""B1539 -- THE RUN (PREREGISTRATION.md section 5): routes R' and P' at every Galois orbit of the population's own characters,
then route N on the abelian covers the sealed rule selects.

    python3 -u run.py --route R [--workers k] --record    ->  run_R.jsonl
    python3 -u run.py --route P [--workers k] --record    ->  run_P.jsonl
    python3 -u run.py --route N [--workers k] --record    ->  run_N.jsonl   (only once run_R.jsonl and run_P.jsonl are complete)

Routes R' (own_chars.frame_own) and P' (own_chars.frame_own_p) read, at each orbit's representative c and at every member of a
sampled orbit, the frame at nu = c (h1(V_eta), n(V_eta), b0, n(L), n((VL)*), capW, capL2) and the two supplies the abelian
covers need, n(c) and n(rho c), with h1 of each; route R' at the prime route_primes(m)["R"], route P' at route_primes(m)["P"].
One row per reading; one 'done' row per (cover, chunk); resumable by (cover, chunk).
Route N (sm:B1536's route_n, by path, unchanged) reads n(1) and n(rho) at the trivial character of every abelian cover
read_out.selection() names: the outcome-blind ones (read_out.blind_selection) and each member's witness (read_out.witness)
within read_out.N_CAP.  Every reading records; nothing is asserted on outcomes."""
import json
import os
import sys
import time
from fractions import Fraction as Fr
from multiprocessing import get_context
from pathlib import Path

HERE = Path(__file__).resolve().parent
CHUNK = 1500

def _sib(alias, name):
    """this arc's own modules, by path under unique names (E12: sm:B1536's route_r puts sm:B1535's folder, with its own
    read_out.py and controls.py, first on sys.path, and sm:B1536's has its own population.py and run.py)"""
    import importlib.util
    if alias not in sys.modules:
        spec = importlib.util.spec_from_file_location(alias, HERE / name)
        mod = importlib.util.module_from_spec(spec)
        sys.modules[alias] = mod
        spec.loader.exec_module(mod)
    return sys.modules[alias]


def lib():
    return (_sib("b1539_own_chars", "own_chars.py"), _sib("b1539_population", "population.py"),
            _sib("b1539_read_out", "read_out.py"))


def tasks_RP():
    """[(state, cover, chunk, chunks)] in a fixed order: the members as population.members() lists them"""
    O, PO, RO = lib()
    out = []
    for st, cid, deg, *_ in PO.members():
        S, perms, cov, ab = PO.cover(st, cid)
        n = len(O.orbit_reps(ab, PO.modulus(deg)))
        k = (n + CHUNK - 1) // CHUNK
        out += [(st, cid, j, k) for j in range(k)]
    return out


def read_chunk(task):
    route, st, cid, j, k = task
    O, PO, RO = lib()
    import numpy as np
    t0 = time.time()
    deg = dict((c, d) for s, c, d, *_ in PO.members() if s == st)[cid]
    m = PO.modulus(deg)
    S, perms, cov, ab = PO.cover(st, cid)
    G = S["G"]
    reps = O.orbit_reps(ab, m)[j::k]
    p = O.route_primes(m)[route]
    B = O.RN.Base(S, O.GF.GF(p, O.root_order(m)))
    rho_np = {g: np.asarray(B.rho[g], dtype=np.int64) % p for g in B.gens}
    Pr = O.punct_present().Presentation(O.Shim(G, perms)) if route == "P" else None

    def one(c):
        exps = ab.exponents(c, m)
        if route == "R":
            return O.frame_own(cov, rho_np, exps, m, p)
        return O.frame_own_p(G, perms, cov, rho_np, exps, m, p, Pr)
    rows = []
    for c, size, order in reps:
        base = {"route": route, "state": st, "cover": cid, "chunk": j, "m": m, "prime": p}
        rows.append(dict(base, c=list(c), orbit=size, order=order, S=one(c)))
        if PO.sampled(st, cid, c):
            for c2 in O.galois_orbit(c, m):
                if c2 != c:
                    rows.append(dict(base, c=list(c2), orbit=size, order=order, S=one(c2), **{"sample of": list(c)}))
    rows.append({"route": route, "state": st, "cover": cid, "chunk": j, "chunks": k, "done": True,
                 "readings": len(rows), "representatives": len(reps), "seconds": round(time.time() - t0, 1)})
    return rows


def read_N(task):
    st, cid, gens, reason = task
    O, PO, RO = lib()
    POP = PO.POP
    t0 = time.time()
    deg = dict((c, d) for s, c, d, *_ in PO.members() if s == st)[cid]
    m = PO.modulus(deg)
    S, perms, cov, ab = PO.cover(st, cid)
    G = S["G"]
    pe, nA = O.abelian_cover(cov, ab, [tuple(g) for g in gens], m)
    assert O.CL.check_cover(G, pe)
    cus, L, Nroot, _ = POP.characters(S, pe)
    p = O.GF.primes_1_mod(Nroot, O.RN.P_BOUND, 1)[0]
    B = O.RN.Base(S, O.GF.GF(p, Nroot))
    sN = O.RN.supplies(B, O.RN.perm_arrays(G, pe), B.character((Fr(0), Fr(0)), Fr(0)))
    return {"route": "N", "state": st, "cover": cid, "generators": [list(g) for g in gens], "reason": reason, "m": m,
            "|A|": nA, "degree": len(pe[G.gens[0]]), "cusps": len(cus), "prime": p, "n(1)": sN["n(L)"],
            "n(rho)": sN["n((VL)*)"], "S": sN, "seconds": round(time.time() - t0, 1)}


def write(out, rows):
    with open(out, "a") as f:
        for r in rows:
            f.write(json.dumps(r) + "\n")
        f.flush()
        os.fsync(f.fileno())


def main():
    args = sys.argv[1:]
    route = args[args.index("--route") + 1]
    workers = int(args[args.index("--workers") + 1]) if "--workers" in args else 1
    rec = "--record" in args
    O, PO, RO = lib()
    out = HERE / f"run_{route}.jsonl"
    rows = RO.load_rows(out.name)
    if route in ("R", "P"):
        done = {(r["state"], r["cover"], r["chunk"]) for r in rows if r.get("done")}
        todo = [(route,) + t for t in tasks_RP() if t[:3] not in done]
        print(f"B1539 run, route {route}: {len(todo)} chunks to read ({len(done)} done)", flush=True)
        work = read_chunk
    else:
        structure = RO.structure_now()
        ev = RO.evaluate({"identity holds": True}, RO.load_rows("run_R.jsonl"), RO.load_rows("run_P.jsonl"), [],
                         structure, say=lambda s: None)
        assert ev["routes R' and P' complete"], "route N waits for complete records in routes R' and P'"
        sel = RO.selection(ev["witnesses"], structure)
        have = {(f"{r['state']}:{r['cover']}", tuple(map(tuple, r["generators"]))) for r in rows}
        todo = [(k[0].split(":")[0], k[0].split(":")[1], [list(g) for g in k[1]], why) for k, why in sorted(sel.items())
                if k not in have]
        print(f"B1539 run, route N: {len(todo)} covers to read ({len(have)} done)", flush=True)
        work = read_N
    with get_context("spawn").Pool(workers) as pool:
        for res in pool.imap_unordered(work, todo):
            rs = res if isinstance(res, list) else [res]
            if rec:
                write(out, rs)
            last = rs[-1]
            print(f"{last['state']} {last['cover']} {last.get('chunk', last.get('generators'))}: "
                  f"{last.get('readings', 1)} readings, {last['seconds']} s", flush=True)


if __name__ == "__main__":
    main()
