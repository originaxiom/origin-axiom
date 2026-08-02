#!/usr/bin/env python3
"""B856 -- the hearing coupling obeys a period-5 law across the metallic family.

B593 computed the coupling number h = u+ M_odd(RL) u at the golden weld ONLY (m=1). The metallic
family's bundle monodromy is the word R^m L^m (SL(2,Z) trace m^2+2: 3 golden, 6 silver, 11, 18...),
so the family law was one loop away from a banked arc and had never been run.

h is a COUPLING quantity in the strict sense: M_odd is the object's monodromy weld, u is the
listener's direction, and neither determines h alone.

Mathematics scope. Nothing reaches CLAIMS.md; Gate 5 untouched.
"""
import cmath
import importlib.util
import json
import math
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))


def _load(rel, name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, rel))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def setup():
    """SU(3)_2 modular data, the conjugation weld C, and the two theta-odd directions."""
    b238 = _load("../B238_su32_levelrank/su32_wrt.py", "b238_856")
    w, S, T, _cc = b238.su3_data(2)
    n = len(w)
    C = np.zeros((n, n))
    for i, wt in enumerate(w):
        C[w.index((wt[1], wt[0])), i] = 1.0
    Si, Ti = np.linalg.inv(S), np.linalg.inv(T)
    R, L = T, Si @ Ti @ S
    pairs = [(w.index((1, 0)), w.index((0, 1))), (w.index((2, 0)), w.index((0, 2)))]
    U = np.zeros((n, 2))
    for j, (a, b) in enumerate(pairs):
        U[a, j], U[b, j] = 1 / np.sqrt(2), -1 / np.sqrt(2)
    return n, C, R, L, U


N, C, R, L, U = setup()
U3, U6 = U[:, 0].astype(complex), U[:, 1].astype(complex)


def weld(m):
    """The metallic word R^m L^m, welded by charge conjugation."""
    P = np.eye(N, dtype=complex)
    for _ in range(m):
        P = P @ R
    for _ in range(m):
        P = P @ L
    return C @ P


def h(m, u=None):
    u = U3 if u is None else u
    return complex(np.conj(u) @ weld(m) @ u)


def matrix_order(M, cap=200):
    P = np.eye(N, dtype=complex)
    for k in range(1, cap + 1):
        P = P @ M
        if np.allclose(P, np.eye(N), atol=1e-9):
            return k
    return None


def period_of(f, cap=60, span=12, tol=1e-9):
    for p in range(1, cap + 1):
        if all(abs(f(m) - f(m + p)) < tol for m in range(1, span)):
            return p
    return None


def matrix_period(cap=60, span=8, tol=1e-9):
    for p in range(1, cap + 1):
        if all(np.allclose(weld(m), weld(m + p), atol=tol) for m in range(1, span)):
            return p
    return None


def main():
    phi = (1 + math.sqrt(5)) / 2
    rows = []
    for m in range(1, 21):
        a, b = h(m, U3), h(m, U6)
        rows.append(dict(m=m, sl2_trace=m * m + 2, re=a.real, im=a.imag,
                         abs2=abs(a) ** 2, arg_over_pi=cmath.phase(a) / math.pi,
                         conj_of_u6=bool(abs(a - np.conj(b)) < 1e-9)))

    ordR, ordL = matrix_order(R), matrix_order(L)
    pM, pH = matrix_period(), period_of(lambda m: h(m))

    # exact targets
    tgt = {"1/(2phi)": 1 / (2 * phi), "1/(phi sqrt5)": 1 / (phi * math.sqrt(5)),
           "phi/sqrt5": phi / math.sqrt(5)}
    res = dict(
        rows=rows, order_R=ordR, order_L=ordL,
        matrix_period=pM, form_period=pH,
        period_collapse_factor=(pM // pH if pM and pH else None),
        collapse_is_nontrivial=bool(pM and pH and pM != pH),
        h_at_5_is_minus_one=bool(abs(h(5) + 1) < 1e-12),
        b593_m1_reproduced=bool(abs(h(1) - (1 / (2 * phi)
                                            + 1j * math.sin(2 * math.pi / 5) / math.sqrt(5)))
                                < 1e-12),
        abs2_values=sorted({round(r["abs2"], 12) for r in rows}),
        golden_pair_sums_to_one=bool(abs(tgt["1/(phi sqrt5)"] + tgt["phi/sqrt5"] - 1) < 1e-12),
        targets=tgt)

    # Re h is invariant across listener directions -- the observer does not move it
    mixes = []
    for t in np.linspace(0, 1, 11):
        u = (t * U3 + (1 - t) * U6)
        nrm = np.sqrt(abs(np.conj(u) @ u))
        if nrm > 1e-12:
            mixes.append(h(1, u / nrm).real)
    res["Re_h_spread_over_listener_directions"] = float(max(mixes) - min(mixes))

    json.dump(res, open(os.path.join(HERE, "results.json"), "w"), indent=1, sort_keys=True)

    print("=" * 78)
    print("B856 -- the hearing coupling across the metallic family")
    print("=" * 78)
    print(f"\n  {'m':>2} {'SL2 tr':>7} {'h(m)':>34} {'|h|^2':>13} {'arg/pi':>8}")
    for r in rows[:10]:
        print(f"  {r['m']:>2} {r['sl2_trace']:>7} {r['re']:+.12f}{r['im']:+.12f}j "
              f"{r['abs2']:>13.9f} {r['arg_over_pi']:>8.3f}")
    print(f"\n  B593's m=1 value reproduced : {res['b593_m1_reproduced']}")
    print(f"  order(R) = order(L)          : {ordR}, {ordL}")
    print(f"  period of the MATRIX R^m L^m : {pM}")
    print(f"  period of the FORM h(m)      : {pH}")
    print(f"  => collapse {pM} -> {pH}, factor {res['period_collapse_factor']} "
          f"(nontrivial: {res['collapse_is_nontrivial']})")
    print(f"  h(5) = -1 exactly            : {res['h_at_5_is_minus_one']}")
    print(f"  |h|^2 values                 : {res['abs2_values']}")
    print(f"  golden pair sums to 1        : {res['golden_pair_sums_to_one']}")
    print(f"  Re h spread over listeners   : {res['Re_h_spread_over_listener_directions']:.2e}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
