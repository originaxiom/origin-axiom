#!/usr/bin/env python3
"""B1530 -- Parts B and C: the census over every word state to length 12 (sm:B1529's 536 manifolds, read as sm:B1529's census
read them) and m004's levels M2 .. M6, at the hyperbolic point (60 digits, sm:B1527's family_lib through sm:B1529's
fibre_lib.hyperbolic_mats).

Part B, population B (PREREGISTRATION section 3, Lemma 5 and section 6): at every torsion character u of F and every
kappa in {-1, i, -i, omega, omega^2}, is h^1(Gamma; nu (x) rho) >= 1 (nu|F = u, nu(t') = kappa)?  There the cusp is acyclic, so
every class is interior; B1515's members at such kappa are the nu with nu^5 among these characters.
  - route T (sm:B1529's fibre_lib): g(C; kappa) on C = H^1(F; nu0 (x) rho), at all five kappa;
  - route G (census_lib): h^1 on Gamma's own presentation, at kappa = -1 for every character (the one twist where a
    generation-shaped member can live, Lemma 5), and at the other kappa wherever route T reads h^1 >= 1, and at the first two
    characters of every state.
Part C, the mechanism at the simple members (Lemma 8 (ii), Remark 9): at chi = nu^2 for every nu at kappa = 1 (the base points
of 2u), dim(Lambda_A meet pi_A) for chi (x) Lambda^2 rho, read by rank and by the torus pairing (census_lib.lambda_meet_pi).

    python3 census_bc.py [--workers N] [--only STATE ...]   -> census_bc.jsonl (working file, resume-safe; *.jsonl is ignored by
                                                               git) and, with --summary, census_bc.json (tracked)
    python3 census_bc.py --dry-run                          -> the banked dry run on m004's levels M2 .. M6 only (sm:B1515:
                                                               population B empty on M1 .. M6; Lambda_A meets pi_A in 0 at
                                                               every simple member), written to dry_run_bc.json"""
import json
import sys
import time
import warnings
from multiprocessing import Pool
from pathlib import Path

warnings.filterwarnings("ignore")
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import mpmath as mp  # noqa: E402

import exact_states as S  # noqa: E402

FT = S.load(S.B1529, "fibre_lib", "b1529_fibre_lib")
import census_lib as CL  # noqa: E402

OUT = HERE / "census_bc.jsonl"
LEVELS = ["+" + "LR" * n for n in range(2, 7)]
KAPPAS = [("-1", (1, 2)), ("i", (1, 4)), ("-i", (3, 4)), ("omega", (1, 3)), ("omega^2", (2, 3))]


def kappa_acb(turn):
    k, n = turn
    return CL.unit(k, n)


def states():
    recs = json.loads((S.B1529 / "census_records.json").read_text())["records"]
    return [(r["state"], r["read as"], bool(r.get("level")), r["D"], r["trace"], r["golden"]) for r in recs]


def one(job):
    state, read_as, level, D_rec, trace, golden = job
    t0 = time.time()
    mp.mp.dps = 60
    try:
        sign, word = read_as[0], read_as[1:]
        mats = FT.hyperbolic_mats(sign, word)
        FL = S.family()
        G, img = FL.word_group(sign, word)
        chars, D = FL.torsion_characters(img)
        assert D == D_rec, (D, D_rec)
        rec = {"state": state, "read as": read_as, "level": level, "D": D, "trace": trace, "golden": golden}
        # ---------------------------------------------------------------- Part B
        fm = FT.FibreModule(sign, img, mats, D)
        gf = CL.GroupedFox(G, mats, D)
        B = {"route T: h1 >= 1 at": [], "route G at kappa = -1": {}, "route G checks": [], "disagreements": [],
             "H0(F) != 0 at": [], "margins": {"T kept": None, "T dropped": None, "G kept": None, "G dropped": None}}

        def note(key_k, key_d, kept, dropped):
            m = B["margins"]
            if kept is not None:
                m[key_k] = kept if m[key_k] is None else min(m[key_k], kept)
            if dropped is not None:
                m[key_d] = dropped if m[key_d] is None else max(m[key_d], dropped)
        for n_u, u in enumerate(chars):
            i, j = int(u[0] * D), int(u[1] * D)
            (TC, slot, cond) = fm.T_C(i, j)
            if fm.fibre_invariants(i, j) != 0:
                B["H0(F) != 0 at"].append([str(u[0]), str(u[1])])
            gT = {}
            for name, turn in KAPPAS:
                g, kept, dropped = FT.g_at(TC, kappa_acb(turn))
                note("T kept", "T dropped", kept, dropped)
                gT[name] = g
                if g >= 1:
                    B["route T: h1 >= 1 at"].append([str(u[0]), str(u[1]), name, g])
            for name, turn in KAPPAS:
                if name == "-1" or gT[name] >= 1 or n_u < 2:
                    lam = CL.lam_of(sign, i, j, D, kappa_acb(turn))
                    hG, t0G, mg = CL.h1(gf, i, j, lam)
                    note("G kept", "G dropped", mg.kept, mg.dropped)
                    if name == "-1":
                        B["route G at kappa = -1"][str(hG)] = B["route G at kappa = -1"].get(str(hG), 0) + 1
                    B["route G checks"].append(1)
                    if hG != gT[name] or t0G != 0:
                        B["disagreements"].append([str(u[0]), str(u[1]), name, "T", gT[name], "G", hG, "t0", t0G])
        B["route G checks"] = len(B["route G checks"])
        B["margins"] = {k: (mp.nstr(v, 3) if v is not None else None) for k, v in B["margins"].items()}
        rec["B"] = B
        # ---------------------------------------------------------------- Part C
        L = S.load(S.B1527, "cusp_lib", "cusp_lib")
        gf2 = CL.GroupedFox(G, {g: L.wedge2(mats[g]) for g in "abt"}, D)
        chis = sorted({((2 * int(u[0] * D)) % D, (2 * int(u[1] * D)) % D) for u in chars})
        Cc = {"characters": len(chis), "meet != 0 (rank)": [], "meet != 0 (pairing)": [], "dims not (2, 2)": [],
              "rank and pairing disagree": [], "isotropy worst": "0", "kept": None, "dropped": None}
        iso = mp.mpf(0)
        for (i, j) in chis:
            lam = CL.lam_of(sign, i, j, D, CL.unit(0, 1))
            r = CL.lambda_meet_pi(gf2, i, j, lam)
            key = [f"{i}/{D}", f"{j}/{D}"]
            if (r["dim Lambda_A"], r["dim pi_A"]) != (2, 2) or r["h1"] != 2:
                Cc["dims not (2, 2)"].append(key + [r["h1"], r["dim Lambda_A"], r["dim pi_A"]])
            if r["dim(Lambda_A meet pi_A) by rank"] != 0:
                Cc["meet != 0 (rank)"].append(key + [r["dim(Lambda_A meet pi_A) by rank"]])
            if r["dim(Lambda_A meet pi_A) by pairing"] != 0:
                Cc["meet != 0 (pairing)"].append(key + [r["dim(Lambda_A meet pi_A) by pairing"]])
            if r["dim(Lambda_A meet pi_A) by rank"] != r["dim(Lambda_A meet pi_A) by pairing"]:
                Cc["rank and pairing disagree"].append(key)
            iso = max(iso, mp.mpf(r["Lambda_A isotropic (rel)"]), mp.mpf(r["pi_A isotropic (rel)"]))
            k_, d_ = mp.mpf(r["margins"]["smallest kept"]), mp.mpf(r["margins"]["largest dropped"])
            Cc["kept"] = k_ if Cc["kept"] is None else min(Cc["kept"], k_)
            Cc["dropped"] = d_ if Cc["dropped"] is None else max(Cc["dropped"], d_)
        Cc["isotropy worst"] = mp.nstr(iso, 3)
        Cc["kept"] = mp.nstr(Cc["kept"], 3) if Cc["kept"] is not None else None
        Cc["dropped"] = mp.nstr(Cc["dropped"], 3) if Cc["dropped"] is not None else None
        rec["C"] = Cc
    except Exception as ex:                                          # recorded, never silent
        rec = {"state": state, "read as": read_as, "level": level, "error": repr(ex)}
    rec["seconds"] = round(time.time() - t0)
    return rec


def run(workers, only=None, out=OUT, jobs=None):
    jobs = jobs if jobs is not None else states()
    if only:
        jobs = [j for j in jobs if j[0] in only]
    done = set()
    if out.exists():
        for line in out.read_text().splitlines():
            done.add(json.loads(line)["state"])
    todo = [j for j in jobs if j[0] not in done]
    print(f"census_bc: {len(todo)} states to do, {len(done)} done", flush=True)
    with Pool(workers) as pool:
        for rec in pool.imap_unordered(one, todo, chunksize=1):
            with open(out, "a") as fh:
                fh.write(json.dumps(rec, default=str) + "\n")
            if "error" in rec:
                print(f"{rec['state']}: ERROR {rec['error']}", flush=True)
                continue
            b, c = rec["B"], rec["C"]
            print(f"{rec['state']}: D {rec['D']}; B: T h1>=1 {len(b['route T: h1 >= 1 at'])}, G(-1) {b['route G at kappa = -1']}, "
                  f"disagree {len(b['disagreements'])}; C: chars {c['characters']}, meet {len(c['meet != 0 (rank)'])}/"
                  f"{len(c['meet != 0 (pairing)'])}, dims {len(c['dims not (2, 2)'])}; {rec['seconds']} s", flush=True)


def summary(src=OUT, dst=HERE / "census_bc.json"):
    recs = [json.loads(line) for line in src.read_text().splitlines()]
    ok = [r for r in recs if "error" not in r]
    out = {"manifolds": len(recs), "errors": [r for r in recs if "error" in r],
           "B": {"route T: characters with h1 >= 1 at kappa != 1": [],
                 "route G at kappa = -1, all characters": {},
                 "disagreements": [], "H0(F) != 0": [], "route G checks": sum(r["B"]["route G checks"] for r in ok)},
           "C": {"characters": sum(r["C"]["characters"] for r in ok), "meet != 0 (rank)": [], "meet != 0 (pairing)": [],
                 "dims not (2, 2)": [], "rank and pairing disagree": []},
           "records": recs}
    for r in ok:
        for x in r["B"]["route T: h1 >= 1 at"]:
            out["B"]["route T: characters with h1 >= 1 at kappa != 1"].append([r["state"], r["golden"]] + x)
        for k, v in r["B"]["route G at kappa = -1"].items():
            out["B"]["route G at kappa = -1, all characters"][k] = out["B"]["route G at kappa = -1, all characters"].get(k, 0) + v
        for x in r["B"]["disagreements"]:
            out["B"]["disagreements"].append([r["state"]] + x)
        if r["B"]["H0(F) != 0 at"]:
            out["B"]["H0(F) != 0"].append([r["state"], r["B"]["H0(F) != 0 at"]])
        for key in ("meet != 0 (rank)", "meet != 0 (pairing)", "dims not (2, 2)", "rank and pairing disagree"):
            for x in r["C"][key]:
                out["C"][key].append([r["state"], r["golden"]] + x)
    dst.write_text(json.dumps(out, indent=1, default=str))
    print(json.dumps({k: (v if k != "records" else len(v)) for k, v in out.items()}, indent=1, default=str)[:3000])
    return out


def main():
    a = sys.argv[1:]
    workers = int(a[a.index("--workers") + 1]) if "--workers" in a else 4
    if "--dry-run" in a:
        out = HERE / "dry_run_bc.jsonl"
        if out.exists():
            out.unlink()
        jobs = [j for j in states() if j[2]]
        run(workers, out=out, jobs=jobs)
        summary(out, HERE / "dry_run_bc.json")
        out.unlink()
        return
    if "--summary" in a:
        summary()
        return
    only = a[a.index("--only") + 1:] if "--only" in a else None
    run(workers, only)


if __name__ == "__main__":
    main()
