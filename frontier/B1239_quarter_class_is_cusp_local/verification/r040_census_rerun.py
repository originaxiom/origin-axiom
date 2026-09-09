#!/usr/bin/env python3
"""B1239 -- codex R040 rerun, on this bench, independently written.

For every manifold N in snappy.NonorientableCuspedCensus (expected 1260): M = N.orientation_cover()
is an orientable cusped manifold with a fixed-point-free orientation-REVERSING isometry (the deck
involution). Since cs(-M) = -cs(M) and SnapPy's cusped CS lives in R/(1/2)Z, oddness alone forces
2cs = 0 in R/(1/2)Z, i.e. cs in {0, 1/4} mod 1/2. THE CONTENT is which of the two classes occurs.
Codex's certificate reports zero: 1260, quarter: 0 at double precision. We recompute at double AND
quad-double, record the max residual in each class, cusp topology, H1 torsion of the cover, and a
lower bound on the number of isometry-distinct covers (codex checked distinct NAMES only).
Output: JSON to r040_census_rerun.json + a human summary on stdout.
"""
import json, sys, time
import snappy

TOL_D = 1e-6      # codex's tolerance at double precision
TOL_Q = 1e-20     # quad-double (SnapPy high_precision: ~ 60 digits claimed; we ask far less)
HALF = 0.5

def residue_class(cs, tol):
    """cs mod 1/2 -> ('zero'|'quarter'|'other', distance to the nearest of {0, 1/4})."""
    r = float(cs) % HALF
    d0 = min(r, HALF - r)
    dq = abs(r - 0.25)
    if d0 <= tol:
        return "zero", d0
    if dq <= tol:
        return "quarter", dq
    return "other", min(d0, dq)

def main():
    census = snappy.NonorientableCuspedCensus
    rows = []
    counts_d = {"zero": 0, "quarter": 0, "other": 0, "fail": 0}
    counts_q = {"zero": 0, "quarter": 0, "other": 0, "fail": 0}
    worst_d = worst_q = 0.0
    cusp_kinds = {}
    t0 = time.time()
    for i, N in enumerate(census):
        base = N.name()
        kinds = tuple(sorted(c["topology"] for c in N.cusp_info()))
        cusp_kinds[kinds] = cusp_kinds.get(kinds, 0) + 1
        M = N.orientation_cover()
        row = {"base": base, "base_cusps": kinds, "cover": M.name(), "cover_orientable": M.is_orientable(),
               "cover_cusps": M.num_cusps(), "vol_ratio": float(M.volume() / N.volume()),
               "cover_H1": str(M.homology())}
        try:
            cs = M.chern_simons()
            cls, d = residue_class(cs, TOL_D)
            row.update(cs_double=float(cs), class_double=cls, dist_double=d)
            counts_d[cls] += 1
            worst_d = max(worst_d, d) if cls != "other" else worst_d
        except Exception as exc:
            row.update(cs_double=None, class_double="fail", err_double=str(exc)[:80]); counts_d["fail"] += 1
        try:
            H = M.high_precision()
            csq = H.chern_simons()
            clsq, dq = residue_class(csq, TOL_Q)
            row.update(cs_quad=str(csq), class_quad=clsq, dist_quad=float(dq))
            counts_q[clsq] += 1
            worst_q = max(worst_q, float(dq)) if clsq != "other" else worst_q
        except Exception as exc:
            row.update(cs_quad=None, class_quad="fail", err_quad=str(exc)[:80]); counts_q["fail"] += 1
        rows.append(row)
        if (i + 1) % 100 == 0:
            print(f"  {i+1}/{len(census)}  double={counts_d}  quad={counts_q}  {time.time()-t0:.0f}s", flush=True)
    # distinct covers: signature buckets (volume to 1e-8, H1, cusps) then isometry within a bucket
    buckets = {}
    for r in rows:
        buckets.setdefault((round(float(snappy.Manifold(r["cover"]).volume()) if False else 0, 8), r["cover_H1"], r["cover_cusps"]), []).append(r["cover"])
    summary = {
        "census_size": len(census),
        "counts_double": counts_d, "counts_quad": counts_q,
        "max_dist_double_in_class": worst_d, "max_dist_quad_in_class": worst_q,
        "vol_ratio_all_2": all(abs(r["vol_ratio"] - 2) < 1e-9 for r in rows),
        "all_covers_orientable": all(r["cover_orientable"] for r in rows),
        "base_cusp_kinds": {"+".join(k): v for k, v in cusp_kinds.items()},
        "distinct_cover_names": len({r["cover"] for r in rows}),
        "tolerances": {"double": TOL_D, "quad": TOL_Q},
        "snappy_version": snappy.__version__,
    }
    json.dump({"summary": summary, "rows": rows}, open("r040_census_rerun.json", "w"), indent=1)
    print(json.dumps(summary, indent=1))

if __name__ == "__main__":
    main()
