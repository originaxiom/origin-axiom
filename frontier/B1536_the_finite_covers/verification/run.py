#!/usr/bin/env python3
"""B1536 -- THE RUN: the population of population.py read by one route (PREREGISTRATION section 6).

    python3 -u run.py --route N|R --state m004|m003 [--workers k] [--only COVER ...] --record
        -> run_<route>_<state>.jsonl (one row per (cover, character); resumable: a cover whose 'done' row is present is skipped)

Per cover and pulled-back character nu = (u, kappa):
  Part S   the supplies: h^1(V_eta) (membership), n(V_eta), b0, n(L), n((VL)*), and the caps capW = b0 + n(L), capL2 = n((VL)*);
  Part P   at a member whose class can be pulled back (kappa^5 = 1): the count at the pulled-back class c0 (the base's class);
  Part O   at a member with min(capW, capL2) >= 2: every cusp stratum (subsets S of the cusps where nu is trivial), two random
           classes of each, read in full (the count, k, the connecting ranks and the stratum bounds).
Each route reads every cover at every character, in full: the supplies everywhere, Part P and Part O wherever they apply, each
route deciding membership and the caps by its own cohomology (PREREGISTRATION section 5).
Every reading asserts nothing; it records its identities and Theorem C's checks, and the read-out counts failures."""
import json
import random
import sys
import time
import warnings
import zlib
from multiprocessing import Pool
from pathlib import Path

warnings.filterwarnings("ignore")
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import cover_lib as CL  # noqa: E402
import gf  # noqa: E402
import population as POP  # noqa: E402
import route_n as N  # noqa: E402
import route_r as R  # noqa: E402

CAP_O = 2              # Part O's threshold on min(capW, capL2)


def rd(r):
    """a reading, compacted"""
    return {"count": [r["I(W)"], r["I(L2W)"]], "k": r["k"], "b0": r["b0"], "n(L)": r["n(L)"], "n((VL)*)": r["n((VL)*)"],
            "n(V)": r["n(V)"], "rk d1": r["rk d1"], "bound W": r["rk d1(E*) bound"],
            "bound L2": r["rk d1"]["L2*"] - r["k"], "all": r["all"],
            "failed": [k for k, v in r["checks"].items() if not v]}


def read_cover(task):
    route, name, cid, perms = task
    st = CL.state(name)
    G = st["G"]
    cus, L, Nroot, chars = POP.characters(st, perms)
    d = len(perms["a"])
    if route == "N":
        p = gf.primes_1_mod(Nroot, N.P_BOUND, 1)[0]
    else:
        p = gf.primes_1_mod(Nroot, 1 << 31, 1)[0]
    F = gf.GF(p, Nroot)
    B = N.Base(st, F)                     # the base data mod p (the holonomy and the characters; shared input)
    rows = []
    t0 = time.time()
    P_ = CL.with_inverses(perms)
    abelian = all(P_[g][P_[h][x]] == P_[h][P_[g][x]] for g in G.gens for h in G.gens for x in range(len(perms["a"])))
    if route == "N":
        pa = N.perm_arrays(G, perms)
    else:
        cov = R.PCover(G, perms)
    rng = random.Random(zlib.crc32(f"{route}|{name}|{cid}".encode()))
    for (u, kap) in chars:
        pulled = (kap * 5).denominator == 1
        chi = B.character(u, kap)
        row = {"route": route, "state": name, "cover": cid, "degree": d, "cusps": len(cus), "L": L, "prime": p, "abelian": abelian,
               "u": [str(u[0]), str(u[1])], "kappa": str(kap)}
        if route == "N":
            sup = N.supplies(B, pa, chi)
        else:
            sup = R.supplies(cov, B.rho, chi, p)
        row["S"] = sup
        member = sup["h1(V_eta)"] >= 1
        row["member"] = member
        if member and pulled:
            # the pulled-back class: the base's class of V_eta = nu^5 rho (one-dimensional on m004 and m003)
            if route == "N":
                pa1 = N.perm_arrays(G, {"a": [0], "b": [0], "t": [0]})
                cls = N.base_classes(B, N.tensor(B, N.small_four(B, chi, 5), pa1))
                assert list(cls) == ["c1"], cls.keys()
                z = cls["c1"]
                cz = {g: z[gi * 4:(gi + 1) * 4] for gi, g in enumerate(B.gens)}
                row["P"] = rd(N.reading(B, pa, chi, {g: [cz[g]] * d for g in B.gens}))
            else:
                Veta = {g: B.rho[g] * pow(int(chi[g]), 5, p) % p for g in B.gens}
                c0 = R.base_cocycle(G, Veta, p)
                cv = R.cocycle_on_words(G, Veta, c0, cov.sword, p)
                row["P"] = rd(R.reading(cov, B.rho, chi, cv, p))
        if member and min(sup["capW"], sup["capL2"]) >= CAP_O:
            trivial = [(kap * c["j0"]).denominator == 1 for c in cus]
            if route == "N":
                cs = [dict(c, trivial=t) for c, t in zip(cus, trivial)]
                strata = N.strata_readings(B, pa, chi, cs, rng)
            else:
                strata = R.strata_readings(cov, B.rho, chi, p, trivial, rng)
            row["O"] = [{"S": S, "readings": [rd(x) for x in reads]} for S, reads in strata]
        rows.append(row)
    rows.append({"route": route, "state": name, "cover": cid, "done": True, "rows": len(rows),
                 "seconds": round(time.time() - t0, 1)})
    return rows


def main():
    args = sys.argv[1:]
    route = args[args.index("--route") + 1]
    name = args[args.index("--state") + 1]
    workers = int(args[args.index("--workers") + 1]) if "--workers" in args else 1
    only = None
    if "--only" in args:
        only = []
        for x in args[args.index("--only") + 1:]:
            if x.startswith("--"):
                break
            only.append(x)
    st = CL.state(name)
    cv = POP.covers(st)
    out = HERE / f"run_{route}_{name}.jsonl"
    done = set()
    if out.exists():
        for line in out.read_text().splitlines():
            r = json.loads(line)
            if r.get("done"):
                done.add(r["cover"])
    tasks = [(route, name, cid, p) for cid, p in cv if cid not in done and (only is None or cid in only)]
    # big covers first, so the pool's tail is short
    tasks.sort(key=lambda t: -len(t[3]["a"]))
    print(f"B1536 run, route {route}, {name}: {len(tasks)} covers to read ({len(done)} done)", flush=True)
    t0 = time.time()
    rec = "--record" in args
    with Pool(workers) as pool:
        for rows in pool.imap_unordered(read_cover, tasks):
            if rec:
                with open(out, "a") as f:
                    for r in rows:
                        f.write(json.dumps(r) + "\n")
            last = rows[-1]
            n_mem = sum(1 for r in rows[:-1] if r.get("member"))
            n_o = sum(1 for r in rows[:-1] if "O" in r)
            bad = sum(1 for r in rows[:-1] for part in ("P",) if part in r and not r[part]["all"])
            print(f"{last['cover']}: {last['rows'] - 1} characters, {n_mem} members, {n_o} with Part O, "
                  f"{bad} failed readings, {last['seconds']} s (total {time.time() - t0:.0f} s)", flush=True)


if __name__ == "__main__":
    main()
