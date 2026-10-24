#!/usr/bin/env python3
"""HOLOMORPHIC TEST, POST HOC 2 (labelled; written after reading main's P-357 (S204: on the look's two lines the A1
optimum's invariant |h.h|/|h|^2 stays 0.017-0.020 and its e1 admixture tracks a fixed multiple of theta2(tau)/theta3(tau))
and before THE HOLOMORPHIC READING TEST's rows exist; committed before its run, which follows the cells).
On the rows holo_posthoc.py uses (chi2_nine below 100, or the 100 lowest), for the fitted direction h written on
(e1, n, n-bar) by the bilinear dot (a = h.e1, b = h.n-bar, c = h.n, so h = a e1 + b n + c n-bar):
  (a) the invariant |h.h| = |a^2 + 2bc| (h normalised): quantiles, and per Im tau;
  (b) the e1 admixture mu = a / (sqrt2 x the larger of b, c) against theta2(tau)/theta3(tau) and against
      Theta2(2 tau)/Theta3(2 tau) (R's own law, R_IS_THE_S4PRIME_TRIPLET.md): the ratio's modulus and phase - median,
      spread (median absolute deviation of ln|ratio| and of the phase) over all rows and per line with three rows or more;
  (c) the same two numbers for R itself at the rows' tau (a reference: its ratio to Theta2(2 tau)/Theta3(2 tau) is 1).
    python3 -B holo_posthoc2.py      # writes holo_posthoc2.json"""
import json, math, pathlib
import numpy as np
import mpmath as mp

HERE = pathlib.Path(__file__).resolve().parent
d = json.loads((HERE / "holo_rows.json").read_text()); tasks, rows = d["tasks"], d["rows"]
RE_MIRROR = 0.725
main = [r for r in rows if not r.get("degenerate") and tasks[r["p"]][1] != RE_MIRROR and np.isfinite(r["chi2_nine"])]
good = [r for r in main if r["chi2_nine"] < 100]
if len(good) < 100:
    good = sorted(main, key=lambda r: r["chi2_nine"])[:100]
F1 = np.array([0, 1, -1j]) / math.sqrt(2); F2 = np.array([1, 0, 0], dtype=complex); F3 = np.array([0, 1, 1j]) / math.sqrt(2)
mp.mp.dps = 25


def thetas(t):
    """theta2(tau)/theta3(tau) and Theta2(2tau)/Theta3(2tau), with the analytic q^(1/8) and q^(1/4)."""
    q1 = mp.exp(1j * mp.pi * t)
    th2 = 2 * mp.exp(1j * mp.pi * t / 4) * mp.fsum(q1 ** (n * n + n) for n in range(0, 30))
    th3 = 1 + 2 * mp.fsum(q1 ** (n * n) for n in range(1, 30))
    q2 = q1 * q1
    T2 = 2 * mp.exp(1j * mp.pi * t / 2) * mp.fsum(q2 ** (n * n + n) for n in range(0, 30))
    T3 = 1 + 2 * mp.fsum(q2 ** (n * n) for n in range(1, 30))
    return complex(th2 / th3), complex(T2 / T3)


def decomp(h):
    h = h / np.linalg.norm(h)
    a, b, c = h @ F2, h @ F1, h @ F3
    lead = b if abs(b) >= abs(c) else c
    return abs(a * a + 2 * b * c), a / (math.sqrt(2) * lead)


def spread(z):
    z = np.array(z)
    lm, ph = np.log(np.abs(z)), np.angle(z)
    return {"median |ratio|": float(np.exp(np.median(lm))), "MAD of ln|ratio|": float(np.median(np.abs(lm - np.median(lm)))),
            "median phase": float(np.median(ph)), "MAD of phase": float(np.median(np.abs(ph - np.median(ph))))}


cache, inv, r1, r2, byline, byim = {}, [], [], [], {}, {}
for r in good:
    k, re_t, im_t = tasks[r["p"]]
    key = (re_t, im_t)
    if key not in cache:
        cache[key] = thetas(mp.mpc(re_t, im_t))
    t1, t2 = cache[key]
    h = np.array([complex(x, y) for x, y in r["h"]])
    I, mu = decomp(h)
    inv.append(I); r1.append(mu / t1); r2.append(mu / t2)
    byline.setdefault((k, r["hor"]), []).append(mu / t1)
    byim.setdefault(im_t, []).append(I)
out = {"rows used": len(good),
       "(a) |h.h| quantiles 10/50/90%": [float(np.quantile(inv, q)) for q in (0.1, 0.5, 0.9)],
       "(a) |h.h| median per Im tau": {str(y): float(np.median(v)) for y, v in sorted(byim.items())},
       "(b) mu / (theta2/theta3)(tau)": spread(r1),
       "(b) mu / (Theta2/Theta3)(2 tau)": spread(r2),
       "(b) per (line, horocycle) with three rows or more: MAD of ln|mu / (theta2/theta3)|, median over such lines":
           (float(np.median([spread(v)["MAD of ln|ratio|"] for v in byline.values() if len(v) >= 3]))
            if any(len(v) >= 3 for v in byline.values()) else None)}
out["(c) R's own mu against (Theta2/Theta3)(2 tau) at the rows' tau (should be 1 up to sign)"] = "see R_IS_THE_S4PRIME_TRIPLET.md (exact)"
(HERE / "holo_posthoc2.json").write_text(json.dumps(out, indent=1) + "\n")
print("written")
