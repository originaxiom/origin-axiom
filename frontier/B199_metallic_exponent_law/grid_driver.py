"""B199 grid driver (Goal A, P1): compute the geometric-stratum exponent for every admissible cell.

Runs geom_grid.geom_exponent_cell over the manifest, skips det(A)!=1 cells (ill-posed: the bundle
relation forces det A=1; full regular spectra at EVEN rank have det -1 and are inadmissible), and
dumps a structured JSON table. Reuses the B198 numeric engine + the order(mu)=inf geometric filter.

Usage:  python grid_driver.py [out.json] [validation|new|controls|all]
pyenv. Standalone character-variety math; nothing to CLAIMS.md.
"""
import sys, json, time
import numpy as np
from geom_grid import geom_exponent_cell, make_A

# (m, o, n, exps, status, expected_k)   exps = eigenvalue exponents of A=diag(zeta_o^exps)
MANIFEST = [
    # validation anchors (re-derive known geometric k)
    (1, 3, 4, [0, 0, 1, 2], "validation", 4),
    (1, 4, 3, [0, 1, 3],    "validation", 3),
    (1, 5, 5, [0, 1, 2, 3, 4], "validation", 2),
    (1, 8, 4, [1, 3, 5, 7], "validation", 3),
    (2, 3, 4, [0, 0, 1, 2], "validation", 4),
    (2, 4, 3, [0, 1, 3],    "validation", 2),
    (3, 4, 3, [0, 1, 3],    "validation", 3),
    # NEW (the yield surface)
    (3, 3, 4, [0, 0, 1, 2], "new", None),
    (4, 3, 4, [0, 0, 1, 2], "new", None),
    (5, 3, 4, [0, 0, 1, 2], "new", None),
    (4, 4, 3, [0, 1, 3],    "new", None),    # held-out for Judge-Predict
    (5, 4, 3, [0, 1, 3],    "new", None),
    (3, 5, 5, [0, 1, 2, 3, 4], "new", None),
    (4, 5, 5, [0, 1, 2, 3, 4], "new", None),
    (2, 8, 4, [1, 3, 5, 7], "new", None),
    (1, 6, 6, [0, 0, 1, 2, 4, 5], "new", None),   # o=6 at n=6 (det-1 fix: drop zeta6^3, double 1)
    # controls (expected empty: no irreducible reps)
    (2, 5, 5, [0, 1, 2, 3, 4], "control", None),
    (1, 5, 3, [0, 1, 4],    "control", None),
    (1, 6, 3, [0, 1, 5],    "control", None),
    (1, 3, 5, [0, 0, 1, 1, 2], "control", None),
]


def detA(o, exps, n):
    A = make_A(o, exps)[0]
    return complex(np.prod([A[i, i] for i in range(n)]))


def main():
    out = sys.argv[1] if len(sys.argv) > 1 else "grid_results.json"
    which = sys.argv[2] if len(sys.argv) > 2 else "all"
    cells = [c for c in MANIFEST if which == "all" or c[4] == which]
    results = []
    t0 = time.time()
    for (m, o, n, exps, status, exp_k) in cells:
        d = detA(o, exps, n)
        if abs(d - 1) > 1e-9:
            r = {"id": "m%d_o%d_n%d" % (m, o, n), "m": m, "o": o, "n": n, "exps": exps,
                 "status": status, "skipped": "det(A)=%s != 1 (inadmissible)" % round(d.real, 4)}
            print("SKIP %-14s det(A)=%s" % (r["id"], round(abs(d), 4)), flush=True)
            results.append(r); continue
        seeds = 250 if n <= 4 else 700           # SL5 reps are rare (~1/130)
        rngs = (0, 1, 7) if n <= 4 else (0, 1, 7, 13, 23)
        res = geom_exponent_cell(m, o, n, exps, seeds=seeds, rng_seeds=rngs)
        res["status"] = status
        res["expected_k"] = exp_k
        res["match"] = (exp_k is None) or (res["geometric_k"] == exp_k)
        results.append(res)
        gk = res["geometric_k"]
        tag = "EMPTY" if res["empty"] else ("k=%s%s" % (gk, "" if res["geometric"]["unique"] else " (NON-UNIQUE)"))
        chk = "" if exp_k is None else ("  [%s]" % ("OK" if res["match"] else "MISMATCH exp %s" % exp_k))
        print("%-14s %-10s %-8s reps(geo)=%d lox=%s (t=%.0fs)%s" % (
            res["id"], status, tag, res["geometric"]["reps"], bool(res["loxodromic_sample"]),
            time.time() - t0, chk), flush=True)
    json.dump(results, open(out, "w"), indent=1)
    # summary
    val = [r for r in results if r.get("status") == "validation" and "skipped" not in r]
    mism = [r for r in val if not r.get("match")]
    print("\nwrote %s  (%d cells, %.0fs)" % (out, len(results), time.time() - t0))
    print("validation: %d/%d match" % (len(val) - len(mism), len(val)),
          "" if not mism else "MISMATCHES: " + ",".join(r["id"] for r in mism))
    print("ALL CHECKS PASS" if not mism else "VALIDATION MISMATCH")


if __name__ == "__main__":
    main()
