"""W73: the masses under the end's normalisation (H-end). W72's surface-frame Yukawa Y, rescaled by the cusp's pairing
of the modes' units, K = diag(1, 2, 2), read against W66's data under W66's predicate, with a look-elsewhere figure.
The rule (W73_RULE.md) was committed before this script; it discloses that H-end was chosen after W72's Y was read.

  Z1  the values: the two settings agree, and m2/m3 and m1/m3 under H-end
  Z2  the verdict on the data: W66's predicate on the three m2/m3 with one coupling, and the CKM matrix (V = 1)
  Z3  the down sector's z
  Z4  the look-elsewhere figure
  plus the read-outs: every ratio against every datum, and the singular vectors

Run: python3 the_end_normalisation.py  ->  the_end_normalisation.json beside it.
"""
import json
import math
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_parameter_free_census as PF  # noqa: E402  (W66: the data and the tolerance)

OUT = HERE / "the_end_normalisation.json"
A = 0.10
PASS = 7.81
KS = {"H-end, K = diag(1, 2, 2)": np.array([1.0, 2.0, 2.0]), "W72's basis, K = 1": np.array([1.0, 1.0, 1.0])}


def stored_Y():
    d = json.loads((HERE / "the_surface_yukawa.json").read_text(encoding="utf-8"))
    Y2 = np.array([[complex(*z) for z in row] for row in d["X4"]["Y (Y0 = 2.0)"]])
    parts = d["read-outs"]["the parts above and below Y0"]
    Y1 = np.zeros((3, 3), dtype=complex)
    for a in range(3):
        for b in range(a, 3):
            p = parts[f"1.25:{a}{b}"]
            Y1[a, b] = Y1[b, a] = complex(*p["above"]) + complex(*p["below"])
    return Y1, Y2


def ratios(Y, k):
    D = np.diag(1 / np.sqrt(k))
    Yh = D @ Y @ D
    U, s, Vh = np.linalg.svd(Yh)
    return s, U, Yh


def main():
    out = {"status": "W73: the masses under the end's normalisation (the rule W73_RULE.md first; one run)"}
    Y1, Y2 = stored_Y()
    hz = json.loads((HERE / "received" / "HZ2021_running_masses_MZ.json").read_text(encoding="utf-8"))
    mv, ms = hz["masses_GeV"]["value"], hz["masses_GeV"]["sigma"]
    data = {"up": ("u", "c", "t"), "down": ("d", "s", "b"), "lepton": ("e", "mu", "tau")}
    res = {}
    for name, k in KS.items():
        s1, _, _ = ratios(Y1, k)
        s2, U, Yh = ratios(Y2, k)
        agree = float(np.max(np.abs(s1 - s2)) / s2[0])
        r21, r31 = float(s2[1] / s2[0]), float(s2[2] / s2[0])
        rows = {}
        for sec, (one, two, three) in data.items():
            d21, d31 = mv[two] / mv[three], mv[one] / mv[three]
            e21 = float(np.hypot(ms[two] / mv[two], ms[three] / mv[three]))
            rows[sec] = {"m2/m3 datum": d21, "m1/m3 datum": d31,
                         "z (m2/m3)": (math.log(r21) - math.log(d21)) / math.hypot(e21, A),
                         "log ratio, m2/m3": math.log(r21 / d21), "log ratio, m1/m3": math.log(r31 / d31)}
        res[name] = {"singular values": s2.tolist(), "agreement of the two settings": agree, "m2/m3": r21,
                     "m1/m3": r31, "per sector": rows,
                     "singular vectors (|components| on F_i, F+, F-)": np.abs(U).T.tolist()}
    he = res["H-end, K = diag(1, 2, 2)"]
    out["Z1"] = {"agreement": he["agreement of the two settings"], "m2/m3": he["m2/m3"], "m1/m3": he["m1/m3"],
                 "holds": bool(he["agreement of the two settings"] < 1e-8 and 0.0185 <= he["m2/m3"] <= 0.0205
                               and 3e-4 <= he["m1/m3"] <= 5e-4)}
    z = {sec: v["z (m2/m3)"] for sec, v in he["per sector"].items()}
    chi2 = sum(v * v for v in z.values())
    out["Z2"] = {"z per sector": z, "chi2 (three m2/m3)": chi2, "CKM under one coupling": "V = 1: |V_us| = |V_cb| = 0",
                 "holds": bool(chi2 > PASS and abs(z["up"]) > 5 and abs(z["lepton"]) > 5)}
    out["Z3"] = {"z_down": z["down"], "holds": bool(abs(z["down"]) < 1)}
    deltas = [abs(v[key]) for r in res.values() for v in r["per sector"].values()
              for key in ("log ratio, m2/m3", "log ratio, m1/m3")]
    dmin = min(deltas)
    p = 1 - (1 - 2 * dmin / math.log(1e6)) ** 12
    out["Z4"] = {"comparisons": len(deltas), "smallest |log ratio|": dmin, "p": p, "holds": bool(p > 0.05)}
    out["cells"] = {k: out[k]["holds"] for k in ("Z1", "Z2", "Z3", "Z4")}
    out["read-outs"] = res
    OUT.write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
    print("written", OUT.name)


if __name__ == "__main__":
    main()
