#!/usr/bin/env python3
"""(the golden covers dossier, section 6: a draft for the next arc; not sealed, not run) the next arc's run: routes R' and P' at every own character of the population, then route N on the cyclic
covers the sealed rule selects.

    python3 -u run.py --route R|P [--workers k] --record      ->  run_<route>.jsonl  (one row per (cover, character); resumable)
    python3 -u run.py --route N [--workers k] --record        ->  run_N.jsonl        (one row per selected cyclic subgroup)

Route R' and route P' each read, at every own character c of order dividing m(cover): the frame at nu = c (h1(V_eta), n(V_eta),
b0, n(L), n((VL)*), capW, capL2) and the two supplies the cyclic covers need, n(c) and n(rho c), with h1 of each.
Route N (sm:B1536's route_n, by path) reads n(1) and n(rho) at the trivial character of N_e for the selected cyclic subgroups:
  - every cyclic subgroup of order <= 3 on the covers of degree 5 and 9;
  - every cyclic subgroup whose Lemma A sums, in route R' or route P', give room >= 3 at the trivial character of N_e;
  - a fixed sample: crc32 of (cover, generator) = 0 mod 25.
Every reading records; nothing is asserted on outcomes."""
import json
import sys
import time
import zlib
from fractions import Fraction as Fr
from multiprocessing import get_context
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
SAMPLE = 25


def lib():
    import gc_own_chars as O
    import gc_draft_population as PD
    return O, PD


def read_cover(task):
    route, st, cid, m = task
    O, PD = lib()
    import numpy as np
    POP = PD.POP
    N = O._load("b1536_route_n_run", O.B1536V / "route_n.py")
    gf = O._load("b1536_gf_run", O.B1536V / "gf.py")
    S = O.CL.state(st)
    G = S["G"]
    perms = dict(POP.covers(S))[cid]
    cov = O.R.PCover(G, perms)
    ab = O.Ab(cov)
    L = 12
    p = gf.primes_1_mod(L * m, 1 << 31, 1)[0]
    B = N.Base(S, gf.GF(p, L * m))
    rho_np = {g: np.asarray(B.rho[g], dtype=np.int64) % p for g in B.gens}
    Pr = O.punct_present().Presentation(O.Shim(G, perms)) if route == "P" else None
    rows = []
    t0 = time.time()
    for c in ab.characters(m):
        exps = ab.exponents(c, m)
        if route == "R":
            s = O.frame_own(cov, rho_np, exps, m, p)
        else:
            s = O.frame_own_p(G, perms, cov, rho_np, exps, m, p, Pr)
        rows.append({"route": route, "state": st, "cover": cid, "m": m, "c": list(c), "prime": p, "S": s})
    rows.append({"route": route, "state": st, "cover": cid, "done": True, "rows": len(rows),
                 "seconds": round(time.time() - t0, 1)})
    return rows


def main():
    args = sys.argv[1:]
    route = args[args.index("--route") + 1]
    workers = int(args[args.index("--workers") + 1]) if "--workers" in args else 1
    rec = "--record" in args
    O, PD = lib()
    out = HERE / f"run_{route}.jsonl"
    done = set()
    if out.exists():
        done = {(r["state"], r["cover"]) for r in map(json.loads, out.read_text().splitlines()) if r.get("done")}
    tasks = [(route, st, cid, PD.modulus(deg)) for st, cid, deg, *_ in PD.members() if (st, cid) not in done]
    print(f"run, route {route}: {len(tasks)} covers to read ({len(done)} done)", flush=True)
    with get_context("spawn").Pool(workers) as pool:
        for rows in pool.imap_unordered(read_cover, tasks):
            if rec:
                with open(out, "a") as f:
                    for r in rows:
                        f.write(json.dumps(r) + "\n")
            print(f"{rows[-1]['state']} {rows[-1]['cover']}: {rows[-1]['rows']} characters, {rows[-1]['seconds']} s",
                  flush=True)


if __name__ == "__main__":
    main()
