#!/usr/bin/env python3
"""W166, POST HOC (labelled; written after part S was read, committed before its one run): at B1757's four points, is
the free fit's down (and lepton) coupling the inverse induced form's response with the source conjugated?

Part S found the rule's down and lepton couplings 88-90 degrees from B1757's fitted ones (the up within 3-8).  This
reads only angles between coupling matrices taken as vectors in C^9; it computes no chi2 and promotes nothing.

The down variants (each a coupling matrix, compared with B1757's Y_down = Y_of(S, H_d^fit) and B1762's L1 hd_1):
  D0  the rule's: Y_of(S, K_d^-1 DR)
  D1  the response conjugated: Y_of(S, conj(K_d^-1 DR))
  D2  the conjugate source: Y_of(S, K_d^-1 conj(DR))
  D3  the other reading: Y_of(S~, Kt_d^-1 DR), Kt_d the forms in the S~ reading (3 Kt_down + Kt_lep)
  D4, D5  the record's DR itself: Y_of(S, conj(DR)) and Y_of(S~, DR)
The same for the leptons (with H_d's variants).

    python3 -B docs/dossiers/the_weave_2026-10-07/the_higgs_from_the_action_posthoc.py
"""
import contextlib
import io
import json
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
with contextlib.redirect_stdout(io.StringIO()):
    import the_higgs_from_the_action as W66   # noqa: E402  (W166's producer and instrument)
W61, W58, T8 = W66.W61, W66.W58, W66.T8
OUT = HERE / "the_higgs_from_the_action_posthoc.json"


def main():
    root = T8.repo_root()
    col, _sha, W93, W89, L = W66.frame(root)
    k0 = L.index(W66.LINE0)
    b57 = T8.git_bytes(root, W61.AGY, W61.J57)
    d57 = [r for r in json.loads(b57.decode("utf-8")) if r["hor"] == "L_max"]
    out = {"arc": "W166", "status": "POST HOC (labelled), one run", "B1757 file sha256": T8.sha256(b57), "points": []}
    for (x, y) in W66.POINTS:
        B = W58.basis(W93, W89, col, L[k0], x, y, "L_max")
        tau = complex(x, y)
        DR = np.array(T8.higgs_DR(tau))
        Kd = W66.NC * W66.form(B, "down", "S") + W66.form(B, "lep", "S")
        Kt = W66.NC * W66.form(B, "down", "St") + W66.form(B, "lep", "St")
        h0 = np.linalg.solve(Kd, DR)
        var = {"D0 rule": ("S", h0), "D1 response conjugated": ("S", np.conj(h0)),
               "D2 conjugate source": ("S", np.linalg.solve(Kd, np.conj(DR))),
               "D3 other reading": ("St", np.linalg.solve(Kt, DR)),
               "D4 conj(DR) in S": ("S", np.conj(DR)), "D5 DR in S~": ("St", DR)}
        fit = next(q for q in d57 if abs(q["tau"][0] - x) < 1e-6 and abs(q["tau"][1] - y) < 1e-6)
        Hd = np.array([complex(a, b) for a, b in fit["H_d"]])
        _p, _i, hd1, _hp = W61.recipes(B, tau)
        rec = {"tau": [x, y]}
        for sec in ("down", "lep"):
            ref = W58.Y_of(B, sec, "S", Hd)
            ref62 = W58.Y_of(B, sec, "S", hd1)
            for name, (rd, h) in var.items():
                Y = W58.Y_of(B, sec, rd, h)
                rec[f"{sec}: {name} to B1757's fit (deg)"] = W66.mat_angle(Y, ref)
                rec[f"{sec}: {name} to B1762's hd_1 (deg)"] = W66.mat_angle(Y, ref62)
        out["points"].append(rec)
    OUT.write_text(json.dumps(out, indent=1, default=float) + "\n", encoding="utf-8")
    print("done", len(out["points"]))


if __name__ == "__main__":
    main()
