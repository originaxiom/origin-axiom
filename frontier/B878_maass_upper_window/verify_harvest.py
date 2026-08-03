#!/usr/bin/env python3
"""B878 -- the cc3 Wave-1 harvest: the upper-window Maass dataset, verified.

Provenance: branch audit/b775-braver-questions @ cd1447b6 (cc3 seat; NEVER merged --
integrate-don't-merge). Files harvested as branch_* siblings; relay preserved verbatim.
This script re-runs the banking seat's verification legs and writes results.json.
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    up = json.load(open(os.path.join(HERE, "branch_scanE_refined.json")))
    win, entries = up["window"], up["eigenvalues"]
    mn = json.load(open(os.path.join(
        HERE, "..", "B797_maass_spectrum_harvest", "eigenvalues_final.json")))
    mne = mn["eigenvalues"]
    mnv = [float(e["r"]) if isinstance(e, dict) else float(e) for e in mne]
    mnmult = sum(int(e.get("multiplicity", 1)) for e in mne
                 if isinstance(e, dict)) or len(mnv)

    vals = [float(e["r"]) for e in entries]
    upmult = sum(int(e.get("multiplicity", 1)) for e in entries)
    stab = sum(1 for e in entries
               if e.get("stable", False)
               and abs(float(e["r"]) - float(e["r_Y2"]))
               <= 100 * max(float(e["sigma_Y1"]), float(e["sigma_Y2"]), 1e-12))
    parents = [7.072004187, 11.008113359, 12.500100167, 13.293162714]
    pdel = [min(min(abs(p - v) for v in vals), min(abs(p - v) for v in mnv))
            for p in parents]
    noted = sorted(e["note"] for e in entries if e.get("note"))
    sdevs = sorted(abs(float(e.get("S_invariance_dev", 0))) for e in entries)

    res = dict(
        window=win, upper_distinct=len(entries), upper_mult=upmult,
        lower_distinct=len(mnv), lower_mult=mnmult,
        combined_distinct=len(mnv) + len(entries),
        combined_mult=mnmult + upmult,
        two_Y_stable=stab,
        parent_deltas=[f"{d:.2e}" for d in pdel],
        parents_all_present=max(pdel) < 1e-8,
        noted_entries=noted,
        s_invariance_dev_range=[f"{sdevs[0]:.2e}", f"{sdevs[-1]:.2e}"],
        provenance="audit/b775-braver-questions @ cd1447b6 (cc3; never merged)",
        claims_check=dict(claim_43=len(mnv) + len(entries) == 43,
                          claim_72=mnmult + upmult == 72,
                          stability_26_26=stab == len(entries) == 26),
    )
    json.dump(res, open(os.path.join(HERE, "results.json"), "w"), indent=1,
              sort_keys=True)
    for k, v in res["claims_check"].items():
        print(f"  {k}: {v}")
    print(f"  parents: {res['parent_deltas']}  noted: {len(noted)}")
    print(f"  S-dev range: {res['s_invariance_dev_range']} (reported, not interpreted)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
