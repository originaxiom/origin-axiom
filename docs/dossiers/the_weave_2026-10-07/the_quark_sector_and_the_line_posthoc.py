"""W60, POST HOC (written after W60's one run and its read-out; labelled; W60's JSON is unchanged). Two things to trace:
P1 failed as worded only at (1/2, 0), where the control and its reference (1/2, 1/2) are both 2-torsion points, which
the order-3 rotation makes equivalent at omega, so both values are 0 and a relative error is undefined. And the
read-out's net term showed the Higgs's term outweighing the quarks' at the Higgs's own lines, against the rule's
predicted reading; but it compared four lines only and left out the leptons.

  PH1  P1 re-scored with absolute errors, from the stored numbers
  PH2  the matter's Delta V6 on the N = 96 grid, fitted by a cosine series of period 1/2 (|m|, |n| <= 5); the fit's
       residual, and its values against the N = 192 points
  PH3  the net six-dimensional term over all lines w in [0, 1)^2 (a 216 x 216 grid, then a local refinement), for
       stated contents (6d Casimir weights in heat-trace units; fermions -2 per state, a complex doublet +2):
       (i) the rule's: the quarks (Q 18, u^c 9, d^c 9) and the Higgs in the three parity sectors jointly;
       (ii) (i) with the leptons (L 6, e^c 3); (iii) (ii) with the Higgs in one parity sector, for each parity;
       (iv) the quarks and the leptons alone. For each: the global minimum, and the twists d^c and e^c see there

Run: python3 the_quark_sector_and_the_line_posthoc.py  ->  the_quark_sector_and_the_line_posthoc.json beside it.
"""
import json
import math
import sys
from pathlib import Path

import numpy as np
from scipy.optimize import minimize

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_one_loop_potential_on_the_fibre as OP  # noqa: E402  (W59: the parities, the charges)

OUT = HERE / "the_quark_sector_and_the_line_posthoc.json"
D = json.loads((HERE / "the_quark_sector_and_the_line.json").read_text(encoding="utf-8"))
AREA = math.sqrt(3) / 2
MODES = [(m, n) for m in range(-5, 6) for n in range(-5, 6) if (m, n) > (0, 0) or (m == 0 and n == 0)]


def ph1():
    out = {}
    for N in ("N = 96", "N = 192"):
        rows = D["P1"][N]["rows"]
        out[N] = {"largest |Delta V6 - exact|": max(abs(r["Delta V6"] - r["exact"]) for r in rows),
                  "largest relative error where the exact value is not 0":
                      max(r["relative diff"] for r in rows if abs(r["exact"]) > 1e-6),
                  "largest |Delta log det - Kronecker|": max(r["|diff|"] for r in rows)}
    scale = max(abs(r["exact"]) for r in D["P1"]["N = 192"]["rows"])
    out["holds with absolute errors (2e-3 log det; 3% of the largest |exact| for V6) at N = 192"] = bool(
        out["N = 192"]["largest |Delta log det - Kronecker|"] < 2e-3
        and out["N = 192"]["largest |Delta V6 - exact|"] < 0.03 * scale)
    return out


def basis(phi):
    phi = np.atleast_2d(phi)
    return np.stack([np.cos(4 * np.pi * (m * phi[:, 0] + n * phi[:, 1])) for m, n in MODES], axis=1)


def ph2():
    grid = D["the matter's values"]["the grid (N = 96)"]
    P = np.array([g["phi"] for g in grid])
    v = np.array([g["Delta V6"] for g in grid])
    coef, *_ = np.linalg.lstsq(basis(P), v, rcond=None)
    resid = float(np.max(np.abs(basis(P) @ coef - v)))
    pts = D["the matter's values"]["N = 192"]["points"]
    named = {"(1/4, 0)": (0.25, 0.0), "(1/6, 1/6)": (1 / 6, 1 / 6), "(1/9, 1/9)": (1 / 9, 1 / 9),
             "(2/9, 2/9)": (2 / 9, 2 / 9), "(1/18, 1/18)": (1 / 18, 1 / 18)}
    check = {k: {"fit (N = 96)": float(basis(p) @ coef), "N = 192": pts[k]["Delta V6"]} for k, p in named.items()}
    return coef, {"the fit's largest residual on the grid": resid, "against the N = 192 points": check}


def matter_v6(coef, phi):
    return basis(phi) @ coef


def higgs_v6(psi, parities, M=40):
    """a complex scalar of charge 1 in the given parity sectors, at phases psi (heat-trace units, against 0)"""
    m, n = np.meshgrid(np.arange(-M, M + 1), np.arange(-M, M + 1), indexing="ij")
    m, n = m.ravel(), n.ravel()
    keep = (m != 0) | (n != 0)
    m, n = m[keep], n[keep]
    w = 1.0 / np.abs(m + n * OP.OMEGA) ** 6
    c = sum(np.cos(2 * np.pi * (m * u + n * v)) for u, v in parities)
    psi = np.atleast_2d(psi)
    out = np.empty(len(psi))
    for s in range(0, len(psi), 2000):
        ph = np.cos(2 * np.pi * (np.outer(psi[s:s + 2000, 0], m) + np.outer(psi[s:s + 2000, 1], n)))
        out[s:s + 2000] = -(AREA / (4 * np.pi)) * 128 * ((ph - 1) @ (c * w))
    return out


CONTENTS = {
    "(i) the rule's: quarks, Higgs jointly": ({"Q": 18, "u^c": 9, "d^c": 9}, OP.PARITIES),
    "(ii) quarks, leptons, Higgs jointly": ({"Q": 18, "u^c": 9, "d^c": 9, "L": 6, "e^c": 3}, OP.PARITIES),
    "(iii) quarks, leptons, Higgs in (1/2, 0)": ({"Q": 18, "u^c": 9, "d^c": 9, "L": 6, "e^c": 3}, [OP.PARITIES[0]]),
    "(iii) quarks, leptons, Higgs in (0, 1/2)": ({"Q": 18, "u^c": 9, "d^c": 9, "L": 6, "e^c": 3}, [OP.PARITIES[1]]),
    "(iii) quarks, leptons, Higgs in (1/2, 1/2)": ({"Q": 18, "u^c": 9, "d^c": 9, "L": 6, "e^c": 3}, [OP.PARITIES[2]]),
    "(iv) quarks and leptons alone": ({"Q": 18, "u^c": 9, "d^c": 9, "L": 6, "e^c": 3}, None),
}


def net(coef, states, parities, w):
    w = np.atleast_2d(w)
    total = np.zeros(len(w))
    for f, k in states.items():
        total += -2 * k * matter_v6(coef, (OP.CHARGES[f] * w) % 1.0)
    if parities is not None:
        total += 2 * higgs_v6((3 * w) % 1.0, parities)
    return total


def ph3(coef):
    g = 216
    W = np.array([(a / g, b / g) for a in range(g) for b in range(g)])
    out = {}
    for name, (states, parities) in CONTENTS.items():
        vals = net(coef, states, parities, W)
        i = int(np.argmin(vals))
        res = minimize(lambda x: float(net(coef, states, parities, x)[0]), W[i], method="Nelder-Mead",
                       options={"xatol": 1e-10, "fatol": 1e-12})
        w = res.x % 1.0
        tw = {f: [float((OP.CHARGES[f] * c) % 1.0) for c in w] for f in ("Q", "u^c", "d^c", "L", "e^c", "H")}
        nearest_ninth = [round(c * 9) / 9 for c in w]
        out[name] = {"the global minimum w": w.tolist(), "its value": float(res.fun),
                     "the value at w = 0": float(net(coef, states, parities, (0.0, 0.0))[0]),
                     "the grid points within 1e-6 of the minimum value": int(np.sum(vals < vals[i] + 1e-6)),
                     "w on the ninths (largest distance)": float(max(abs(c - r) for c, r in zip(w, nearest_ninth))),
                     "the twists there (q w mod 1)": tw,
                     "d^c and e^c see different twists": bool(max(abs(a - b) for a, b in zip(tw["d^c"], tw["e^c"]))
                                                             > 1e-6)}
    return out


def main():
    coef, p2 = ph2()
    out = {"status": "W60 post hoc: P1 re-scored; the matter's potential fitted; the net term minimized over every "
                     "line (labelled; W60's JSON unchanged)",
           "PH1": ph1(), "PH2": p2, "PH3": ph3(coef)}
    OUT.write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8")
    for k, v in out["PH3"].items():
        print(k, [round(c, 4) for c in v["the global minimum w"]], round(v["its value"], 3),
              v["d^c and e^c see different twists"])


if __name__ == "__main__":
    main()
