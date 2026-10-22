#!/usr/bin/env python3
"""W123, post hoc (labelled so; after the one run's read-out). Y2 failed as worded: in 9 of 64 end data for rho and
10 of 64 for rho_T-bar, d - h1 != sum m, every failure where some line carries a double pole, and every failing count
having singular values near the run's fixed threshold 1e-9. This check recounts all 128 end data with the threshold
placed in the singular-value gap, and reports the gap itself: the largest value counted as null and the smallest
kept, over every case.

    python3 -B the_higgs_route_posthoc.py      # writes the_higgs_route_posthoc.json beside itself
"""
import contextlib
import io
import itertools
import json
import sys
from fractions import Fraction as Fr
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
with contextlib.redirect_stdout(io.StringIO()):
    import the_higgs_route as HR  # noqa: E402
    import the_index_on_the_weaves_surface as W45  # noqa: E402


def singular_values(rS, rT, k, lower, N=30, M=160):
    """the run's collocation matrix (the_higgs_route.dims_lower), returning its normalized singular values"""
    rS, rT = np.array(rS, dtype=complex), np.array(rT, dtype=complex)
    d = rS.shape[0]
    w, P = np.linalg.eig(rT)
    P = np.linalg.qr(P)[0] if np.allclose(rT @ rT.conj().T, np.eye(d)) else P
    lam = [Fr(float(np.angle(z) / (2 * np.pi)) % 1.0).limit_denominator(48) for z in w]
    lows = [lower(x) for x in lam]
    cols = [(j, n) for j in range(d) for n in range(N)]
    h0 = np.sqrt(3) / 2
    rows = []
    for th in np.linspace(np.pi / 3 + 0.02, 2 * np.pi / 3 - 0.02, M):
        t = np.exp(1j * th)
        ts, tk = -1 / t, np.exp(float(k) * np.log(t))
        block = np.zeros((d, len(cols)), dtype=complex)
        for c, (j, n) in enumerate(cols):
            e = float(lows[j]) + n
            block[:, c] = (P[:, j] * np.exp(2j * np.pi * e * ts) - tk * (rS @ P[:, j]) * np.exp(2j * np.pi * e * t)) \
                * np.exp(2 * np.pi * e * h0)
        rows.append(block)
    s = np.linalg.svd(np.vstack(rows), compute_uv=False)
    return s / s[0]


def census(rS, rT, k, exps, tol):
    dual = (np.conj(rS), np.conj(rT))
    table, worst_null, least_kept, law = {}, 0.0, 1.0, True
    for m in itertools.product((-1, 0, 1, 2), repeat=3):
        mm = dict(zip(exps, m))
        s1 = singular_values(rS, rT, k, lambda x: x - mm[x])
        s2 = singular_values(*dual, 2 - k, lambda y: y + mm[(1 - y) % 1])
        d, h = int((s1 < tol).sum()), int((s2 < tol).sum())
        for s in (s1, s2):
            if (s < tol).any():
                worst_null = max(worst_null, float(s[s < tol].max()))
            least_kept = min(least_kept, float(s[s >= tol].min()))
        table[str(m)] = [d, h]
        law &= (d - h == sum(m))
    return table, worst_null, least_kept, law


def main():
    out = {"arc": "W123", "status": "post hoc, labelled; after the one run's read-out", "threshold": 1e-12}
    with contextlib.redirect_stdout(io.StringIO()):
        _, kept = W45.E3()
    bS, bT = (np.array(x, dtype=complex) for x in kept["S <-> S~^-1, T <-> L"])
    bexps = sorted(Fr(float(np.angle(z) / (2 * np.pi)) % 1.0).limit_denominator(48) for z in np.linalg.eigvals(bT))
    for name, (rS, rT, k, exps) in {"rho": (HR.rS, HR.rT, Fr(3, 2), HR.EXPS),
                                    "rho_T-bar": (bS, bT, Fr(1, 2), bexps)}.items():
        table, wn, lk, law = census(rS, rT, k, exps, 1e-12)
        run = json.loads((HERE / "the_higgs_route.json").read_text())["census " + name]
        changed = {m: [run[m]["d"], run[m]["h1"], v[0], v[1]] for m, v in table.items()
                   if [run[m]["d"], run[m]["h1"]] != v}
        out[name] = {"d - h1 = sum m for all 64 at 1e-12": bool(law), "largest value counted null": wn,
                     "smallest value kept": lk, "cases changed from the run [d, h1 -> d, h1]": changed,
                     "table": table}
        print(name, "| law at 1e-12:", law, "| largest null %.1e | smallest kept %.1e" % (wn, lk),
              "| changed:", changed)
    (HERE / "the_higgs_route_posthoc.json").write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
