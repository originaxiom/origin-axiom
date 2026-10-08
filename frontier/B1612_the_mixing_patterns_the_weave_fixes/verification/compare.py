#!/usr/bin/env python3
"""B1612 -- THE COMPARISON (sealed with the instrument, before any data is read).  Reads mixing_on_the_weave.json (the
weave's patterns) and data.json (transcribed after the seal from the sources the preregistration names: NuFIT's 3-sigma
ranges of the moduli |U_ij| of the leptonic mixing matrix, both orderings; PDG's global-fit moduli |V_ij| of the CKM
matrix with their uncertainties).  Tests, exactly as sealed:
 D1  PMNS, full patterns: a pattern survives in an ordering if, for some of its 36 row and column permutations, every
     sqrt(P_ij) lies inside NuFIT's 3-sigma range for |U_ij|.
 D2  CKM, full patterns and the identity (the two quark sectors keeping one subgroup): a pattern survives if, for some
     permutation, every |sqrt(P_ij) - |V_ij|| <= 3 sigma_ij.
 D3  PMNS, one-column patterns: a column survives if, for some column k of U and some ordering of its three entries,
     every sqrt(c_i) lies inside NuFIT's 3-sigma range of |U_ik|.
 D4  the look-elsewhere statement: survivors out of the number of (pattern, permutation) trials.
Writes comparison.json."""
import json, pathlib, itertools
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent


def perms(P):
    for rp in itertools.permutations(range(3)):
        for cpm in itertools.permutations(range(3)):
            yield rp, cpm, P[np.ix_(rp, cpm)]


def main():
    pat = json.load(open(HERE / "mixing_on_the_weave.json")); data = json.load(open(HERE / "data.json"))
    full = [np.array(p["matrix"]) for p in pat["M3"]["patterns"]]
    cols = [np.array(c["column_sorted"]) for c in pat["M4"]["columns"]]
    out = {"sources": data.get("sources"), "D1": {}, "D3": {}}
    for order in ("NO", "IO"):
        lo, hi = np.array(data["pmns_abs_3sigma"][order]["lo"]), np.array(data["pmns_abs_3sigma"][order]["hi"])
        surv = []
        for n, P in enumerate(full):
            for rp, cpm, Q in perms(P):
                if np.all((np.sqrt(Q) >= lo - 1e-9) & (np.sqrt(Q) <= hi + 1e-9)):
                    surv.append({"pattern": n, "rows": rp, "cols": cpm}); break
        out["D1"][order] = {"survivors": surv, "trials": len(full) * 36}
        csurv = []
        for n, c in enumerate(cols):
            hit = None
            for k in range(3):
                for o in itertools.permutations(range(3)):
                    v = np.sqrt(c[list(o)])
                    if np.all((v >= lo[:, k] - 1e-9) & (v <= hi[:, k] + 1e-9)): hit = {"column": n, "U_column": k, "order": o}; break
                if hit: break
            if hit: csurv.append(hit)
        out["D3"][order] = {"survivors": csurv, "trials": len(cols) * 18,
                            "columns": [list(map(float, cols[s["column"]])) for s in csurv]}
    V, S = np.array(data["ckm_abs"]["value"]), np.array(data["ckm_abs"]["sigma"])
    ksurv = []; cands = [("identity", np.eye(3))] + [(f"pattern {n}", P) for n, P in enumerate(full)]
    best = None
    for name, P in cands:
        for rp, cpm, Q in perms(P):
            z = np.abs(np.sqrt(Q) - V) / S; m = float(np.max(z))
            if best is None or m < best[1]: best = (name, m)
            if m <= 3: ksurv.append({"pattern": name, "rows": rp, "cols": cpm, "max_pull": m}); break
    out["D2"] = {"survivors": ksurv, "trials": len(cands) * 36, "closest": {"pattern": best[0], "max_pull_sigma": best[1]}}
    out["D4"] = {"pmns_full_trials": len(full) * 36, "pmns_column_trials": len(cols) * 18, "ckm_trials": len(cands) * 36}
    json.dump(out, open(HERE / "comparison.json", "w"), indent=1, default=str); print(json.dumps(out, indent=1, default=str))


if __name__ == "__main__":
    main()
