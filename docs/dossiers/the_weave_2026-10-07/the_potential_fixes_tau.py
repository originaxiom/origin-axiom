"""W67: what fixes tau. The weave's O-invariant quartic V^ = lambda2 q2 + c qA (q2 = |a.a|^2/|a|^4, qA = sum_u |a_u|^4
/ |a|^4) evaluated on the parameter-free Higgs sections E, R and R' (H-sec), as a function on the modular curve. The
rule (W67_RULE.md) was committed before this script.

  F1  R and R': q2 = 0; qA = 1/3 at omega, 3/8 at i, toward 1/2 at the cusp; its only local minima at omega
  F2  E: q2 vanishes at omega and at tau_0 and its mirror only; qA(E(omega)) = 1/3; both toward 1 at the cusp
  F3  what fixes tau: with c > 0 the minimum of V^ is at omega; with c < 0, R and R' run to the cusp
  plus the read-outs: E's landscape, the points where all |E_u| are equal, every refined local minimum, the masses

Run: python3 the_potential_fixes_tau.py  ->  the_potential_fixes_tau.json beside it.
"""
import json
import sys
from pathlib import Path

import mpmath as mp
import numpy as np
from scipy.optimize import minimize

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_second_unit as SU  # noqa: E402  (W65: the collocation and the sample)
import the_parameter_free_census as PF  # noqa: E402  (W66: the double-precision sections and the domain map)

OUT = HERE / "the_potential_fixes_tau.json"
mp.mp.dps = 40
OMEGA = complex(-0.5, np.sqrt(3) / 2)
SPECIAL = {"omega": OMEGA, "omega + 1": OMEGA + 1, "i": 1j}
YCAP = 8.0
LAMBDAS = (0.0, 0.1, 1.0, 10.0)
CS = (-1.0, -0.1, 0.1, 1.0)
NM = {"xatol": 1e-11, "fatol": 1e-15, "maxiter": 6000}


def q2(a):
    return float(abs(a @ a) ** 2 / np.vdot(a, a).real ** 2)


def qA(a):
    return float(np.sum(np.abs(a) ** 4) / np.vdot(a, a).real ** 2)


def equal_moduli(a):
    w = np.abs(a) ** 2 / np.vdot(a, a).real
    return float(np.sum((w - 1 / 3) ** 2))


def near(t, pts, r):
    return min(abs(t - p) for p in pts) < r


def grid():
    xs = np.linspace(-0.5, 0.5, 81)
    ys = np.geomspace(0.866, YCAP, 80)
    G = np.full((len(xs), len(ys)), np.nan, dtype=complex)
    for i, x in enumerate(xs):
        for j, y in enumerate(ys):
            if abs(complex(x, y)) >= 1:
                G[i, j] = complex(x, y)
    return G


def objective(S, f):
    def g(xy):
        t = PF.to_fd(complex(xy[0], xy[1]))
        if t.imag > YCAP:
            return 1e3
        return f(PF.ev_np(S, t))
    return g


def landscape(S, f, G):
    vals = np.full(G.shape, np.nan)
    for idx in np.ndindex(G.shape):
        if not np.isnan(G[idx].real):
            vals[idx] = f(PF.ev_np(S, G[idx]))
    mins = []
    nx, ny = G.shape
    for i in range(nx):
        for j in range(ny):
            v = vals[i, j]
            if np.isnan(v):
                continue
            nb = [vals[i + a, j + b] for a in (-1, 0, 1) for b in (-1, 0, 1) if (a or b)
                  and 0 <= i + a < nx and 0 <= j + b < ny and not np.isnan(vals[i + a, j + b])]
            if nb and all(v < w for w in nb):
                mins.append(G[i, j])
    refined = []
    for t in mins:
        r = minimize(objective(S, f), [t.real, t.imag], method="Nelder-Mead", options=NM)
        tt = PF.to_fd(complex(*r.x))
        refined.append({"tau": [tt.real, tt.imag], "value": float(r.fun)})
    return vals, refined


def global_min(S, f, G, vals=None):
    if vals is None:
        vals = np.full(G.shape, np.nan)
        for idx in np.ndindex(G.shape):
            if not np.isnan(G[idx].real):
                vals[idx] = f(PF.ev_np(S, G[idx]))
    flat = [(vals[idx], G[idx]) for idx in np.ndindex(G.shape) if not np.isnan(vals[idx])]
    flat.sort(key=lambda z: z[0])
    best = None
    for v, t in flat[:10]:
        r = minimize(objective(S, f), [t.real, t.imag], method="Nelder-Mead", options=NM)
        if best is None or r.fun < best[0]:
            best = (float(r.fun), PF.to_fd(complex(*r.x)))
    for name, t in SPECIAL.items():                     # the special points themselves, exactly
        v = f(PF.ev_np(S, t))
        if v < best[0]:
            best = (float(v), t)
    return best


def where(t, tau0):
    if t.imag > 7:
        return "runs to the cusp"
    if near(t, [OMEGA, OMEGA + 1], 1e-4):
        return "omega"
    if near(t, [tau0, complex(-tau0.real, tau0.imag)], 1e-3):
        return "tau_0"
    if near(t, [1j], 1e-4):
        return "i"
    return "elsewhere"


def main():
    w65 = json.loads((HERE / "the_second_unit.json").read_text(encoding="utf-8"))
    tau0 = complex(*w65["read-outs"]["tau_0 (E on the cone)"])
    S = {}
    for name, units, lead in (("E", (1, 0, 0), "e_i"), ("R'", (0, 0, 1), "v-"), ("R", (0, 1, 0), "v+")):
        terms, _ = SU.solve_section(units, lead)
        S[name] = PF.to_numpy(terms)
    G = grid()
    pts = [G[idx] for idx in np.ndindex(G.shape) if not np.isnan(G[idx].real)]

    # F1
    f1, ok1 = {}, True
    for name in ("R", "R'"):
        vals_A, ref_A = landscape(S[name], qA, G)
        q2max = max(q2(PF.ev_np(S[name], t)) for t in pts)
        at = {k: qA(PF.ev_np(S[name], t)) for k, t in SPECIAL.items()}
        far = [vals_A[idx] for idx in np.ndindex(G.shape)
               if not np.isnan(vals_A[idx]) and not near(G[idx], [OMEGA, OMEGA + 1], 1e-3)]
        a8 = qA(PF.ev_np(S[name], 8j))
        mins_ok = all(near(complex(*m["tau"]), [OMEGA, OMEGA + 1], 1e-4) for m in ref_A)
        row = {"largest q2 on the grid": q2max, "qA at omega, omega + 1, i": at,
               "qA - 1/3, smallest away from omega": float(min(far) - 1 / 3),
               "1/2 - qA, smallest on the grid": float(0.5 - max(far)), "qA at 8i": a8,
               "refined local minima of qA": ref_A, "all at omega": bool(mins_ok)}
        ok1 &= (q2max < 1e-12 and abs(at["omega"] - 1 / 3) < 1e-12 and abs(at["i"] - 3 / 8) < 1e-12
                and min(far) > 1 / 3 and max(far) < 0.5 and a8 > 0.499 and mins_ok and len(ref_A) > 0)
        f1[name] = row
    f1["holds"] = bool(ok1)

    # F2
    zeros = [OMEGA, OMEGA + 1, tau0, complex(-tau0.real, tau0.imag)]
    E = S["E"]
    at_zero = {k: q2(PF.ev_np(E, t)) for k, t in (("omega", OMEGA), ("tau_0", tau0),
                                                   ("mirror of tau_0", complex(-tau0.real, tau0.imag)))}
    far2 = [q2(PF.ev_np(E, t)) for t in pts if not near(t, zeros, 0.02)]
    qAw = qA(PF.ev_np(E, OMEGA))
    e8 = PF.ev_np(E, 8j)
    vals_2E, ref_2E = landscape(E, q2, G)
    vals_AE, ref_AE = landscape(E, qA, G)
    f2 = {"q2 at omega, tau_0 and its mirror": at_zero, "smallest q2 at least 0.02 from them": float(min(far2)),
          "qA(E(omega))": qAw, "q2 and qA at 8i": [q2(e8), qA(e8)],
          "refined local minima of q2(E)": ref_2E, "refined local minima of qA(E)": ref_AE}
    f2["holds"] = bool(max(at_zero.values()) < 1e-12 and min(far2) > 1e-10 and abs(qAw - 1 / 3) < 1e-12
                       and q2(e8) > 0.99 and qA(e8) > 0.99)

    # F3
    census, ok3 = {}, True
    for name in ("E", "R", "R'"):
        for l2 in LAMBDAS:
            for c in CS:
                f = (lambda l2, c: (lambda a: l2 * q2(a) + c * qA(a)))(l2, c)
                v, t = global_min(S[name], f, G)
                w = where(t, tau0)
                census[f"{name}, lambda2 = {l2}, c = {c}"] = {"min": v, "tau": [t.real, t.imag], "where": w}
                if c > 0 and (name != "E" or l2 > 0):
                    ok3 &= w == "omega"
                if c < 0 and name in ("R", "R'"):
                    ok3 &= w == "runs to the cusp"
    f3 = {"census": census, "holds": bool(ok3)}

    # read-outs
    ro = {}
    ro["E with c < 0, and with lambda2 = 0 and c > 0"] = {
        k: v["where"] for k, v in census.items() if k.startswith("E,") and (", c = -" in k or "lambda2 = 0.0" in k)}
    ro["qA(E(tau_0))"] = qA(PF.ev_np(E, tau0))
    ys = np.linspace(1, 8, 29)
    ro["E along tau = iy (y = 1 to 8 by 0.25): q2, qA"] = [[q2(PF.ev_np(E, 1j * y)), qA(PF.ev_np(E, 1j * y))]
                                                          for y in ys]
    ths = np.pi / 2 + np.arange(41) * (np.pi / 6) / 40
    ro["E along the arc from i to omega: q2, qA"] = [
        [q2(PF.ev_np(E, np.exp(1j * th))), qA(PF.ev_np(E, np.exp(1j * th)))] for th in ths]
    for name in ("R", "R'"):
        ro[f"qA({name}) along tau = iy"] = [qA(PF.ev_np(S[name], 1j * y)) for y in ys]
        ro[f"qA({name}) along the arc from i to omega"] = [qA(PF.ev_np(S[name], np.exp(1j * th))) for th in ths]
    vals_eq, ref_eq = landscape(E, equal_moduli, G)
    ro["points where all |E_u| are equal (refined minima of the spread, value below 1e-12)"] = [
        dict(m, q2=q2(PF.ev_np(E, complex(*m["tau"])))) for m in ref_eq if m["value"] < 1e-12]
    masses = {}
    for label, t in (("omega", OMEGA), ("8i", 8j)):
        v = {k: PF.ev_np(S[k], t) for k in S}
        row = {}
        for pair, (a, c) in PF.PAIRS.items():
            Y = np.outer(v[a], v[c]) + np.outer(v[c], v[a]) - (v[a] @ v[c]) * np.eye(3)
            s = np.linalg.svd(Y, compute_uv=False)
            row[pair] = float(s[1] / s[0])
        masses[label] = row
    ro["m2/m3 for every pair at the fixed points (omega, and the cusp at 8i)"] = masses
    ro["grid points"] = len(pts)

    out = {"status": "W67: what fixes tau (the rule W67_RULE.md first; one run)",
           "F1": f1, "F2": f2, "F3": f3}
    out["cells"] = {k: out[k]["holds"] for k in ("F1", "F2", "F3")}
    out["read-outs"] = ro
    OUT.write_text(json.dumps(out, indent=1, default=lambda x: float(x) if isinstance(x, (np.floating, mp.mpf))
                              else [x.real, x.imag] if isinstance(x, complex) else str(x)) + "\n", encoding="utf-8")
    print(json.dumps(out["cells"], indent=1))


if __name__ == "__main__":
    main()
