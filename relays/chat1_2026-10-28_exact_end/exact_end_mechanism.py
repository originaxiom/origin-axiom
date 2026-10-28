"""chat1, 2026-10-28: THE EXACT END, the mechanism. Post hoc and labelled: written after the look and the family were read,
from a scratch check of the same computation. Data-free. Committed before its one run.

The small-cut form 2 pi L + c_s counts the whole of the regular part of K_s = P_s / R_s, inside the horoball too: c_s is
the norm with the pole's divergence subtracted as the cut shrinks. The exact norm removes the horoball. Writing
K_s = 1/z + a_0 + a_1 z + a_2 z^2 + ... near the puncture, a round disc of radius rho = e^(-L) holds
pi (|a_0|^2 rho^2 + |a_1|^2 rho^4 / 2 + |a_2|^2 rho^6 / 3 + ...) of the regular part's mass (the cross terms with the pole
average to zero on circles). This script reads the Laurent coefficients of the frame's twisted kernels at the four rows of
exact_end.py (an FFT on the circle |z| = 0.05, 256 points) and sets that estimate beside the stored gap, small-cut minus
exact, at L_max. The horoball is not round (its radius runs 0.50-0.55 against e^(-L_max) = 0.52), so the estimate is
rough by construction.
Run:  python3 -B exact_end_mechanism.py <main_checkout>"""
import sys, json, math, pathlib, importlib.util
from fractions import Fraction as Fr
import numpy as np
ROOT = pathlib.Path(sys.argv[1]).resolve(); HERE = pathlib.Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location("ee", HERE / "exact_end.py")
ee = importlib.util.module_from_spec(_spec); sys.argv = [sys.argv[0], str(ROOT)]; _spec.loader.exec_module(ee)
B, K = ee.B, ee.K
EPS_R, NPT = 0.05, 256


def main():
    d = json.loads((HERE / "exact_end.json").read_text()); out = []
    th = 2 * np.pi * np.arange(NPT) / NPT; z = EPS_R * np.exp(1j * th)
    for r in d["rows"]:
        tau = complex(*r["tau"]); b = Fr(r["line"][1]); w = float(Fr(2, 5)) * tau + float(b); rho = math.exp(-r["L_exact"]["L_max"])
        for sec in ("up", "down", "lep"):
            lf, rf = K.SECT[sec]; x, yy = B.sector_twists(w, tau, B.SIXY[lf], B.SIXY[rf]); R = B.residues(x, yy, tau)
            P = B.pairs(x, yy, z, tau); st = r["sectors"][sec]["L_max"]; row = {"row": r["row"], "line": r["line"], "sector": sec, "channels": {}}
            for s in B.UNITS:
                if abs(R[s]) < 1e-12:
                    row["channels"][s] = None; continue
                c = np.fft.fft(P[s] / R[s]) / NPT
                a = {"a_-1": c[-1] * EPS_R, "a_0": c[0], "a_1": c[1] / EPS_R, "a_2": c[2] / EPS_R ** 2}
                est = math.pi * (abs(a["a_0"]) ** 2 * rho ** 2 + abs(a["a_1"]) ** 2 * rho ** 4 / 2 + abs(a["a_2"]) ** 2 * rho ** 6 / 3)
                gap = st["small_cut"][s] - st["exact"][s]
                row["channels"][s] = {"|a_-1|": abs(a["a_-1"]), "|a_0|": abs(a["a_0"]), "|a_1|": abs(a["a_1"]), "|a_2|": abs(a["a_2"]),
                                      "round_disc_estimate": est, "stored_gap": gap, "small_cut": st["small_cut"][s], "exact": st["exact"][s]}
            out.append(row)
            print("%s %s %-4s rho %.4f | %s" % (r["row"], r["line"], sec, rho, " | ".join(
                "%s: zero channel" % s if v is None else "%s: |a_-1| %.3f |a_0| %.3f |a_1| %.3f |a_2| %.3f; estimate %.2f, gap %.2f (%.0f%% of the small-cut norm)"
                % (s, v["|a_-1|"], v["|a_0|"], v["|a_1|"], v["|a_2|"], v["round_disc_estimate"], v["stored_gap"], 100 * v["stored_gap"] / v["small_cut"])
                for s, v in row["channels"].items())))
    ok = [v for rw in out for v in rw["channels"].values() if v is not None]
    rel = [abs(v["round_disc_estimate"] / v["stored_gap"] - 1) for v in ok]
    print("the round-disc estimate against the stored gap: largest relative difference %.3f over %d channels" % (max(rel), len(ok)))
    for rw in out:
        if rw["sector"] == "down":
            ch = rw["channels"]
            print("%s split of the heavy pair, N_i - N_1: small-cut %.3f, exact %.3f; the |a_0|^2 difference times pi rho^2 accounts for %.3f"
                  % (rw["row"], ch["i"]["small_cut"] - ch["1"]["small_cut"], ch["i"]["exact"] - ch["1"]["exact"],
                     math.pi * (ch["i"]["|a_0|"] ** 2 - ch["1"]["|a_0|"] ** 2) * math.exp(-2 * [r for r in d["rows"] if r["row"] == rw["row"]][0]["L_exact"]["L_max"])))
    (HERE / "exact_end_mechanism.json").write_text(json.dumps(out, indent=1, default=str))
    print("exact_end_mechanism exit 0")


if __name__ == "__main__":
    main()
