#!/usr/bin/env python3
"""
CELL T3 — amphichirality at theorem strength: the 2-torsion sweep + bite control.

Part A (sweep): first 40 manifolds of snappy.NonorientableCuspedCensus.
  For each base N: M = N.orientation_cover().
    - verify M orientable, vol(M) ~ 2 vol(N)
    - verify amphichirality via M.symmetry_group().is_amphicheiral()
      (SnapPy: True iff the symmetry group contains an orientation-reversing
       element; by Mostow this is the full isometry group when
       sg.is_full_group() is True — we record that flag too)
    - CS(M) in SnapPy's normalization (defined mod 1/2), at quad-double
      precision via Manifold.high_precision() when possible.
    - test: distance of CS to the 2-torsion set {0, 1/4} of R/(1/2)Z,
      i.e. to the nearest multiple of 1/4, must be < 1e-9.

Part B (bite control, MB12): first 15 manifolds of OrientableCuspedCensus
  whose symmetry group is full and has NO orientation-reversing element
  (chiral). Their CS must be generically OFF {0,1/4}: report each distance
  and the minimum. If chiral controls also cluster on {0,1/4}, the sweep
  is uninformative -> DEGRADED.

Conventions (E23 discipline):
  - CS normalization: SnapPy's Manifold.chern_simons(), real, defined
    modulo 1/2 for orientable cusped census manifolds; mirror-odd
    (CS(-M) = -CS(M)). Sanity anchors checked in-script:
    CS(m004) ≡ 0 and CS(m003) ≡ 1/4 (mod 1/2).
  - "amphichiral" = admits an orientation-reversing self-isometry.
  - distance measured mod 1/2 to nearest element of {0, 1/4} mod 1/2,
    equivalently to nearest integer multiple of 1/4; max possible = 1/8.

No Standard Model value appears anywhere in this computation (Gate 5).
"""
import json, os, sys, traceback
import snappy

CELL = os.path.dirname(os.path.abspath(__file__))
TOL = 1e-9

def dist_to_quarter_lattice(x):
    """distance from x to nearest integer multiple of 1/4 (the 2-torsion
    set {0,1/4} of R/(1/2)Z, unrolled)."""
    r = x % 0.25
    return min(r, 0.25 - r)

def nearest_torsion_label(x):
    """which 2-torsion element of R/(1/2)Z is nearest: '0' or '1/4'."""
    r = x % 0.5
    # representatives 0, 0.25, 0.5(=0)
    d0 = min(r, 0.5 - r)          # distance to 0 mod 1/2
    d4 = abs(r - 0.25)            # distance to 1/4 mod 1/2
    return "0" if d0 <= d4 else "1/4"

def get_cs(M):
    """CS at best available precision; returns (float, method)."""
    try:
        cs = float(M.high_precision().chern_simons())
        return cs, "high_precision"
    except Exception:
        cs = float(M.chern_simons())
        return cs, "double"

def main():
    out = {"tolerance": TOL, "anchors": {}, "sweep": [], "control": []}

    # ---- sanity anchors for the CS normalization -------------------------
    for name, expect in [("m004", "0"), ("m003", "1/4")]:
        M = snappy.Manifold(name)
        cs, meth = get_cs(M)
        lab = nearest_torsion_label(cs)
        out["anchors"][name] = {"cs": cs, "nearest": lab, "expected": expect,
                                "ok": lab == expect and
                                      dist_to_quarter_lattice(cs) < TOL}
    if not all(a["ok"] for a in out["anchors"].values()):
        print("ANCHOR FAILURE — normalization not as assumed", out["anchors"])
        # continue anyway; recorded

    # ---- Part A: the sweep ----------------------------------------------
    NC = snappy.NonorientableCuspedCensus
    n_sweep = 40
    for i in range(n_sweep):
        N = NC[i]
        rec = {"base": N.name(), "index": i}
        try:
            M = N.orientation_cover()
            rec["cover"] = M.name()
            rec["cover_orientable"] = bool(M.is_orientable())
            rec["vol_base"] = float(N.volume())
            rec["vol_cover"] = float(M.volume())
            try:
                sg = M.symmetry_group()
                rec["sym_group"] = str(sg)
                rec["sym_full"] = bool(sg.is_full_group())
                rec["amphichiral"] = bool(sg.is_amphicheiral())
            except Exception as e:
                rec["sym_error"] = repr(e)
            try:
                cs, meth = get_cs(M)
                rec["cs"] = cs
                rec["cs_method"] = meth
                d = dist_to_quarter_lattice(cs)
                rec["dist_to_2torsion"] = d
                rec["in_2torsion"] = d < TOL
                rec["torsion_value"] = nearest_torsion_label(cs)
            except Exception as e:
                rec["cs_error"] = repr(e)
        except Exception as e:
            rec["error"] = repr(e)
            rec["traceback"] = traceback.format_exc()
        out["sweep"].append(rec)
        print("SWEEP", rec.get("base"), "->", rec.get("cover"),
              "amph:", rec.get("amphichiral"), "cs:", rec.get("cs"),
              "d:", rec.get("dist_to_2torsion"), "val:",
              rec.get("torsion_value"), rec.get("cs_error", ""))

    # ---- Part B: chiral bite control ------------------------------------
    OC = snappy.OrientableCuspedCensus
    want = 15
    i = 0
    while len(out["control"]) < want and i < 500:
        M = OC[i]
        i += 1
        try:
            sg = M.symmetry_group()
            if not sg.is_full_group():
                continue  # need a PROVEN full group to certify chirality
            if sg.is_amphicheiral():
                continue  # amphichiral -> not a chiral control
        except Exception:
            continue
        rec = {"name": M.name(), "sym_group": str(sg), "chiral": True}
        try:
            cs, meth = get_cs(M)
            rec["cs"] = cs
            rec["cs_method"] = meth
            rec["dist_to_2torsion"] = dist_to_quarter_lattice(cs)
            rec["on_2torsion_at_tol"] = rec["dist_to_2torsion"] < TOL
        except Exception as e:
            rec["cs_error"] = repr(e)
        out["control"].append(rec)
        print("CTRL", rec["name"], "cs:", rec.get("cs"),
              "d:", rec.get("dist_to_2torsion"), rec.get("cs_error", ""))

    # ---- summary ---------------------------------------------------------
    sw_ok = [r for r in out["sweep"] if r.get("in_2torsion")]
    sw_cs = [r for r in out["sweep"] if "cs" in r]
    sw_amph = [r for r in out["sweep"] if r.get("amphichiral")]
    ctl_d = [r["dist_to_2torsion"] for r in out["control"]
             if "dist_to_2torsion" in r]
    ctl_on = [r for r in out["control"] if r.get("on_2torsion_at_tol")]
    dist0 = sum(1 for r in sw_ok if r["torsion_value"] == "0")
    dist4 = sum(1 for r in sw_ok if r["torsion_value"] == "1/4")
    out["summary"] = {
        "sweep_total": len(out["sweep"]),
        "sweep_with_cs": len(sw_cs),
        "sweep_amphichiral": len(sw_amph),
        "sweep_in_2torsion": len(sw_ok),
        "sweep_max_dist": max((r["dist_to_2torsion"] for r in sw_cs),
                              default=None),
        "value_distribution": {"0": dist0, "1/4": dist4},
        "control_total": len(out["control"]),
        "control_min_dist": min(ctl_d, default=None),
        "control_median_dist": sorted(ctl_d)[len(ctl_d)//2] if ctl_d else None,
        "control_on_2torsion": len(ctl_on),
    }
    print(json.dumps(out["summary"], indent=2))
    with open(os.path.join(CELL, "results.json"), "w") as f:
        json.dump(out, f, indent=1)

if __name__ == "__main__":
    main()
