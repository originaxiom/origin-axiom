#!/usr/bin/env python3
"""B1522 -- the read-out: P1-P9 decided mechanically from census.json against the sealed numbers (PREREGISTRATION section 5),
the outcome (A, B or C), and the golden reading in its sealed form. A last section holds observations made AFTER the run,
marked as such: they were not sealed and decide nothing.
Usage: python3 read_out.py   (writes read_out.json)"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import census as C  # noqa: E402
import route_fibre as RF  # noqa: E402

SEALED_F = {5: (11, 20, 0), 7: (29, 448, 392), 11: (199, 35244, 34848)}   # n: (p = L_n, generic, unitary), Lemma F
SPLIT_LEVELS = (5, 7, 9, 10, 11)
NO_SPLIT = (3, 4, 6, 8, 12)


def main():
    census = json.loads((HERE / "census.json").read_text(encoding="utf-8"))
    post = json.loads((HERE / "post_run_check.json").read_text(encoding="utf-8"))
    L = {r["n"]: r for r in census["levels"]}
    g = {n: L[n]["unfixed at generic lam"] for n in L}
    u = {n: L[n]["unfixed at unitary lam"] for n in L}
    out = {"predictions": {}}
    P = out["predictions"]

    P["P1"] = {"claim": "levels 1, 2: no unfixed vacuum at any lam", "held": all(g[n] == 0 and u[n] == 0 for n in (1, 2))}
    for name, n in (("P2", 5), ("P3", 7), ("P4", 11)):
        p, eg, eu = SEALED_F[n]
        # Lemma F's closed form, recomputed here, must equal the sealed numbers
        assert (p - 1) * (p + 1 - 2 * n) == eg and (p - 1) * (p - 1 - 2 * n) == eu
        P[name] = {"claim": f"n = {n}: {eg} unfixed at generic lam, {eu} at unitary lam (Lemma F)", "read": [g[n], u[n]],
                   "held": (g[n], u[n]) == (eg, eu)}
    # P5: no character with a nonzero single-eigenline component at a split prime is fixed at generic lam; lower bounds
    single = {}
    for n in SPLIT_LEVELS:
        d = L[n]["generic unfixed described"]["by golden type at split primes"]
        single[n] = sum(v for k, v in d.items() if "phi-line" in k or "phibar-line" in k)
    p5_bounds = g[9] >= 576 and g[10] >= 2500
    P["P5"] = {"claim": "single-eigenline components at split primes are never fixed at generic lam; n = 9: >= 576, n = 10: >= 2500",
               "X1 (direct, every level n <= 12)": post["X1"]["passed"], "read": {"n = 9": g[9], "n = 10": g[10]},
               "held": post["X1"]["passed"] and p5_bounds}
    P["P6"] = {"claim": "some level with no split prime (3, 4, 6, 8, 12) has unfixed vacua at generic lam",
               "read": {str(n): g[n] for n in NO_SPLIT}, "held": any(g[n] > 0 for n in NO_SPLIT)}
    P["P7"] = {"claim": "on M12 more than half the vacua are unfixed at generic lam", "read": [g[12], L[12]["order"]],
               "held": 2 * g[12] > L[12]["order"]}
    fire = census["firing"]
    P["P8"] = {"claim": "every one of the 196 firing members is fixed at its lam", "read": [fire["fixed"], fire["members"]],
               "X3 (direct)": [post["X3"]["fixed"], post["X3"]["members"]],
               "held": fire["members"] == 196 and fire["fixed"] == 196 and post["X3"]["passed"]}
    P["P9"] = {"claim": "the two routes agree on every character of every level",
               "held": all(L[n]["routes agree on every character"] for n in L)}
    out["held"] = sum(1 for v in P.values() if v["held"])
    out["expected from the priors"] = round(0.99 + 0.95 * 3 + 0.97 + 0.70 + 0.70 + 0.65 + 0.99, 2)
    any_unfixed = any(g[n] > 0 or u[n] > 0 for n in L)
    out["outcome"] = "A" if not any_unfixed else ("B" if fire["fixed"] == fire["members"] else "C")

    # the golden reading in its sealed form: at generic lam a vacuum is unfixed iff no golden Galois reflection fixes its twist
    # (Lemmas C and G, both routes); checked without the criterion by X2 on n <= 6. Its sheet gloss, level by level:
    gloss = {}
    for n in sorted(L):
        if g[n] == 0:
            continue
        d = L[n]["generic unfixed described"]["by golden type at split primes"]
        if n in SPLIT_LEVELS:
            mixed = sum(v for k, v in d.items() if "mixed" in k and "phi-line" not in k and "phibar-line" not in k)
            du = L[n]["unitary unfixed described"]["by golden type at split primes"]
            single_u = sum(v for k, v in du.items() if "phi-line" in k or "phibar-line" in k)
            gloss[str(n)] = {"unfixed": g[n], "with a single-sheet component": single[n], "mixed only": mixed,
                             "unfixed = single-sheet exactly": single[n] == g[n],
                             "at |lam| = 1: unfixed": u[n], "at |lam| = 1: single-sheet still unfixed": single_u}
        else:
            gloss[str(n)] = {"unfixed": g[n], "no split prime": True}
    out["golden reading"] = {
        "sealed form holds (criterion route F = route R on n <= 12; criterion bypassed by X2 on n <= 6)":
            all(L[n]["routes agree on every character"] for n in L) and post["X2"]["passed"],
        "per level": gloss,
        "unfixed exactly the single-sheet twists on": [int(n) for n, v in gloss.items() if v.get("unfixed = single-sheet exactly")],
    }

    # AFTER THE RUN (not sealed): where the firing members sit
    rows = fire["rows"]
    chars5, _, N5 = RF.characters(5)
    unfixed5 = {tuple(v) for v in L[5]["generic unfixed list"]}
    by_lam = {}
    for lam in ("1", "-1", "i", "-i"):
        mem = {tuple(r["char at level"]) for r in rows if r["level"] == 5 and r["lam"] == lam and r["source"].startswith("case (b)")}
        sheets = {"phi-line": 0, "phibar-line": 0, "other": 0}
        for v in mem:
            t = C.eigen_type(v, N5, 11)
            sheets[t if t in sheets else "other"] += 1
        by_lam[lam] = {"members": len(mem), "equal to the 20 vacua no reflection fixes": mem == unfixed5, "sheets": sheets,
                       "E": sum(1 for r in rows if r["level"] == 5 and r["lam"] == lam and r["source"].startswith("case (b)") and r["E"]),
                       "A": sum(1 for r in rows if r["level"] == 5 and r["lam"] == lam and r["source"].startswith("case (b)") and r["A"])}
    held_by = {}
    for r in rows:
        k = f"level {r['level']}"
        h = held_by.setdefault(k, {"members": 0, "by a reflection (E)": 0, "only by a rotation (A, not E)": 0})
        h["members"] += 1
        h["by a reflection (E)"] += r["E"]
        h["only by a rotation (A, not E)"] += (r["A"] and not r["E"])
    out["after the run (not sealed)"] = {
        "M5 case-(b) members by lam": by_lam,
        "how each level's members are held": held_by,
        "note": "M5's case-(b) members are B1511/B1512's eigenline characters. This read finds them equal, at every lam in mu_4, "
                "to the 20 vacua of M5 that no golden Galois reflection fixes, ten on each sheet, held at their unitary lam only "
                "by the golden rotations. Seen after the run; decides nothing; a sealed question for the levels with split primes "
                "is registered (OPEN_LEADS sL-10 item 7).",
    }
    (HERE / "read_out.json").write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")
    for k, v in P.items():
        print(k, "HELD" if v["held"] else "FAILED", "--", v["claim"])
    print("held", out["held"], "of 9; expected", out["expected from the priors"], "; outcome", out["outcome"])
    print("golden reading:", json.dumps(out["golden reading"], ensure_ascii=False))
    print("after the run:", json.dumps(out["after the run (not sealed)"]["M5 case-(b) members by lam"], ensure_ascii=False))
    print("held by:", json.dumps(held_by, ensure_ascii=False))


if __name__ == "__main__":
    main()
