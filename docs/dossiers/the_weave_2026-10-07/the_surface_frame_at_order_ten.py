#!/usr/bin/env python3
"""W171 — W73 per sector at N = 10, the counted line's order, in the weave reading (the rule: W171_RULE.md, committed
and pushed before this script). In the surface frame each sector's Yukawa integrand returns around a line's
stabiliser with its closure character; the weave reading's Yukawa is the character-invariant part. Both readings of
the twist: the minimal (W91's coupling vector V_s, W72's untwisted units) and the per field (W92's dressed units).

  K0  the instrument: W91's generator against direct theta evaluation (six lines, three tau, 1e-40); W92's dressing
      series against direct evaluation at N = 10 (three lines, every SM charge, two points, 1e-40)
  K1  the stabilisers, exact: g^-1 T^10 g keeps each of the 36 lines with c = +-1 mod 10; no character trivial; the
      [-30, 30] search finds an element with c prime to 10 on every line
  K2  the minimal law at N = 10: T^10 on the 20 lines with a prime to 10, the searched element on the other 16; the
      triplet's cycle products (W91 post hoc 2's method) and the identity channel against the reference pair (2, 4)
  K3  the per-field law at N = 10: W92's integrands on T^10 at the 20 lines, and W92's V3 at N = 10 (three threads)
  K4  the T^10 orbit sum at the line (1, 0) vanishes in every sector, both readings; controls give ten times the value
  R   the census over N = 2..16; the counted line (4, 5); the measured phases

Conventions: W91's integer lines (a, b), w = (a tau + b)/10, psi = (a/10, -b/10); chat1's (l_a, l_b) = (b, a).

    python3 -B docs/dossiers/the_weave_2026-10-07/the_surface_frame_at_order_ten.py
"""
import contextlib
import io
import json
import platform
import sys
import time
import traceback
import warnings
from fractions import Fraction as Fr
from math import gcd
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
with contextlib.redirect_stdout(io.StringIO()):
    import the_twisted_coupling_vector as W91          # noqa: E402  (W91: the generator, direct evaluation)
    import the_per_field_units as PF                   # noqa: E402  (W92: the dressing, the units, the integrands)
    import the_per_field_units_posthoc as PFH          # noqa: E402  (W92 post hoc: the analytic neutral R)

OUT = HERE / "the_surface_frame_at_order_ten.json"
N = 10
T10 = (1, 10, 0, 1)
UNITS = ("1", "i", "j", "k")
REF = (2, 4)                                           # (k_u, k_d); q_L^2 + q_R^2 = 10, the trivial character
BOX = 30
QMIN = {"up": 17, "down": 5, "leptons": 45}           # q_L^2 + q_R^2
QPF = {"up": 8, "down": -4, "lepton": 36}             # q_L^2 + q_R^2 - q_H^2
COUNTED = (4, 5)
_ROOT = {}


def sanitize(text):
    for k, v in _ROOT.items():
        text = text.replace(v, k)
    return text


# ----------------------------------------------------------------------------------------------- lines and elements
def lines_of(n):
    """lines of exact order n up to sign, as (a, b) with the lexicographically least representative"""
    seen, out = set(), []
    for a in range(n):
        for b in range(n):
            if gcd(gcd(a, b), n) != 1 or (a, b) in seen:
                continue
            seen.add((a, b)); seen.add(((-a) % n, (-b) % n))
            out.append((a, b))
    return out


def mul(x, y):
    return (x[0] * y[0] + x[1] * y[2], x[0] * y[1] + x[1] * y[3], x[2] * y[0] + x[3] * y[2], x[2] * y[1] + x[3] * y[3])


def keeps(w, g, n):
    """(eps, c) if w g = eps w mod n, else None; c = <w, w g>/n mod n (W91 post hoc 2's formula)"""
    a, b = w
    A, B, C, D = g
    wg = ((a * A + b * C) % n, (a * B + b * D) % n)
    if wg == (a % n, b % n):
        eps = 1
    elif wg == ((-a) % n, (-b) % n):
        eps = -1
    else:
        return None
    pair = a * (a * B + b * D) - b * (a * A + b * C)
    assert pair % n == 0
    return eps, (pair // n) % n


def conj_T(w, n):
    """g^-1 T^n g with g in SL(2, Z) whose first row is = w mod n (least |a'| + |b'| lift, then extended Euclid)"""
    a, b = w
    best = None
    for i in range(-3, 4):
        for j in range(-3, 4):
            x, y = a + n * i, b + n * j
            if gcd(x, y) == 1 and (best is None or (abs(x) + abs(y), x, y) < best[0]):
                best = ((abs(x) + abs(y), x, y), x, y)
    _, x, y = best

    def egcd(p, q):
        if q == 0:
            return (p, 1, 0)
        g_, s, t = egcd(q, p % q)
        return (g_, t, s - (p // q) * t)
    g_, s, t = egcd(x, y)                               # s x + t y = g_ = +-1
    s, t = s * g_, t * g_
    g = (x, y, -t, s)                                    # det = x s + y t = 1
    assert g[0] * g[3] - g[1] * g[2] == 1
    ginv = (g[3], -g[1], -g[2], g[0])
    return mul(mul(ginv, (1, n, 0, 1)), g), g


def sl2_box(R=BOX):
    out = []
    for A in range(-R, R + 1):
        for B in range(-R, R + 1):
            for C in range(-R, R + 1):
                if A != 0:
                    num = 1 + B * C
                    if num % A == 0 and -R <= num // A <= R:
                        out.append((A, B, C, num // A))
                elif B * C == -1:
                    out.extend((0, B, C, D) for D in range(-R, R + 1))
    out.sort(key=lambda g: (abs(g[2]), sum(abs(x) for x in g), g))
    return out


# ----------------------------------------------------------------------------------------------- K0
def part_K0():
    mp.mp.dps = 60
    lines6 = [(1, 0), (3, 7), (4, 5), (5, 2), (2, 1), (0, 1)]
    taus = [mp.mpc("0.11", "0.9"), mp.mpc("-0.23", "1.2"), mp.mpc("0.31", "0.7")]
    worst_g = mp.mpf(0)
    for (a, b) in lines6:
        psi = (Fr(a, N), Fr(-b, N))
        for qL, qR in W91.SECTORS.values():
            for t in taus:
                g = W91.ev_generator(qL + qR, qL - qR, psi, t, Fr(40))
                d = W91.V_direct(qL + qR, qL - qR, psi, t)
                sc = max(abs(x) for x in d.values())
                worst_g = max(worst_g, max(abs(g[u] - d[u]) for u in UNITS) / sc)
    charges = sorted({1, -4, 2, -3, 6, 3, -3})
    pts = (mp.mpc("0.1", "1.1"), mp.mpc("-0.3", "0.8"))
    worst_d, zeros, cases = mp.mpf(0), 0, 0
    for (a, b) in [(1, 0), (4, 5), (3, 7)]:
        line = (b, a)
        for q in charges:
            for c in range(3):
                if PF.is_odd(c, q, line, N):
                    zeros += 1
                    continue
                ser = PF.dressing_series(c, q, line, N, PF.EMAX)
                for t in pts:
                    d = PF.dressing_direct(c, q, line, N, t)
                    worst_d = max(worst_d, abs(PF.ev_scalar(ser, t) - d) / abs(d))
                    cases += 1
    return {"generator against direct, worst relative": float(worst_g),
            "dressing against direct, worst relative": float(worst_d), "dressing cases": cases,
            "odd components skipped": zeros,
            "holds": bool(worst_g < 1e-40 and worst_d < 1e-40)}


# ----------------------------------------------------------------------------------------------- K1
def part_K1():
    L = lines_of(N)
    box = sl2_box()
    rows, conj_ok, found_all, no_trivial = [], True, True, True
    chosen = {}
    for w in L:
        gam, g = conj_T(w, N)
        kc = keeps(w, gam, N)
        ok = kc is not None and kc[1] in (1, N - 1)
        conj_ok &= ok
        pick = None
        for h in box:
            k = keeps(w, h, N)
            if k is not None and gcd(k[1], N) == 1:
                pick = (h, k)
                break
        found_all &= pick is not None
        chosen[w] = pick
        chars = {}
        if kc is not None:
            for s, Q in QMIN.items():
                chars[f"minimal {s}"] = (-kc[1] * Q) % N              # the law exp(-2 pi i c Q / N), in tenths
                no_trivial &= (kc[1] * Q) % N != 0
            for s, Q in QPF.items():
                chars[f"per field {s}"] = (kc[0] * kc[1] * Q) % N     # exp(2 pi i eps c Q / N), in tenths
                no_trivial &= (kc[1] * Q) % N != 0
        rows.append({"line (a, b)": list(w), "g": list(g), "g^-1 T^10 g": list(gam),
                     "eps, c (conjugate)": list(kc) if kc else None, "characters (tenths)": chars,
                     "searched element": list(pick[0]) if pick else None,
                     "eps, c (searched)": list(pick[1]) if pick else None})
    return {"lines": len(L), "box size": len(box), "rows": rows,
            "conjugate c = +-1 on every line": bool(conj_ok), "searched element found on every line": bool(found_all),
            "no character trivial": bool(no_trivial),
            "holds": bool(len(L) == 36 and conj_ok and found_all and no_trivial)}, chosen


# ----------------------------------------------------------------------------------------------- K2
def zero_channels(Vs):
    """channels identically zero on every evaluation (as W91's U4 counts them): below 1e-40 of the largest channel"""
    return {u for u in ("i", "j", "k")
            if all(abs(V[u]) < mp.mpf(10) ** -40 * max(abs(V[x]) for x in UNITS) for V in Vs)}


def law_min(c, Q):
    return mp.exp(-2j * mp.pi * c * Q / N)


def part_K2(chosen):
    mp.mp.dps = 60
    rows, worst, worst_t, any_one = [], mp.mpf(0), mp.mpf(0), False
    for w, pick in chosen.items():
        a, b = w
        if gcd(a, N) == 1:
            g, (eps, c) = T10, keeps(w, T10, N)
        elif pick is None:
            rows.append({"line (a, b)": list(w), "element": None})
            worst = mp.mpf(1)
            continue
        else:
            g, (eps, c) = pick
        A, B, C, D = g
        if C == 0:
            taus = [mp.mpc("0.1", "1.1"), mp.mpc("0.3", "0.9")]
        else:
            base = mp.mpf(-D) / C
            taus = [base + 1j / mp.mpf(abs(C)), base + (mp.mpf("0.3") + 1.2j) / mp.mpf(abs(C))]
        gt = [(A * t + B) / (C * t + D) for t in taus]
        need = Fr(int(45 * mp.log(10) / (2 * mp.pi * min(mp.im(x) for x in taus + gt) / 1.6)) + 1)
        V0 = [W91.ev_generator(0, 0, (Fr(0), Fr(0)), t, need) for t in taus]
        V0g = [W91.ev_generator(0, 0, (Fr(0), Fr(0)), x, need) for x in gt]
        pi = {}
        for u in ("i", "j", "k"):
            best = None
            for u2 in ("i", "j", "k"):
                r = [V0g[n][u] * mp.sqrt(C * taus[n] + D) / V0[n][u2] for n in range(2)]
                if best is None or abs(r[0] - r[1]) < best[0]:
                    best = (abs(r[0] - r[1]), u2)
            pi[u] = best[1]
        psi = (Fr(a, N), Fr(-b, N))
        Rt = [W91.ev_generator(REF[0], REF[1], psi, t, need) for t in taus]
        Rg = [W91.ev_generator(REF[0], REF[1], psi, x, need) for x in gt]
        for name, (qL, qR) in W91.SECTORS.items():
            Q = qL * qL + qR * qR
            Vt = [W91.ev_generator(qL + qR, qL - qR, psi, t, need) for t in taus]
            Vg = [W91.ev_generator(qL + qR, qL - qR, psi, x, need) for x in gt]
            zero = set().union(*(zero_channels([V]) for V in Vt + Vg))
            chi = {u: [Vg[n][u] / Vt[n][pi[u]] / (V0g[n][u] / V0[n][pi[u]]) for n in range(2)]
                   for u in ("i", "j", "k") if u not in zero and pi[u] not in zero}
            tdep = max((abs(v[0] - v[1]) for v in chi.values()), default=mp.mpf(0))
            seen, err, cyc = set(), mp.mpf(0), []
            for u in ("i", "j", "k"):
                if u in seen:
                    continue
                x, ln, p, ok = u, 0, mp.mpc(1), True
                while x not in seen:
                    seen.add(x)
                    if x in chi:
                        p *= chi[x][0]
                    else:
                        ok = False
                    x = pi[x]
                    ln += 1
                if not ok:
                    cyc.append({"length": ln, "untested: an identically zero channel": True})
                    continue
                err = max(err, abs(p - law_min(c, Q) ** ln))
                cyc.append({"length": ln, "turns": float(mp.arg(p) / (2 * mp.pi) % 1)})
                any_one |= abs(p - 1) < 1e-3
            chi1 = [(Vg[n]["1"] / Vt[n]["1"]) / (Rg[n]["1"] / Rt[n]["1"]) for n in range(2)]
            tdep = max(tdep, abs(chi1[0] - chi1[1]))
            err = max(err, abs(chi1[0] - law_min(c, Q)))
            any_one |= abs(chi1[0] - 1) < 1e-3
            worst, worst_t = max(worst, err), max(worst_t, tdep)
            rows.append({"line (a, b)": list(w), "element": list(g), "eps": eps, "c": c, "sector": name,
                         "identically zero channels": sorted(zero), "cycles": cyc,
                         "identity channel turns": float(mp.arg(chi1[0]) / (2 * mp.pi) % 1),
                         "law turns": float((-c * Q / N) % 1), "law error": float(err), "tau-dependence": float(tdep)})
    return {"rows": rows, "worst law error": float(worst), "worst tau-dependence": float(worst_t),
            "some phase equal to 1": bool(any_one),
            "holds": bool(worst < 1e-30 and worst_t < 1e-30 and not any_one)}


# ----------------------------------------------------------------------------------------------- K3
def build():
    PF.neutral_R = PFH.neutral_R_analytic
    with contextlib.redirect_stdout(io.StringIO()):
        U = PF.build_units()
    U.update({"F32c": [PF.to_comp(s) for s in U["F32"]], "FM12c": [PF.to_comp(s) for s in U["FM12"]],
              "E4Fc": [PF.to_comp(s) for s in U["E4F"]], "fc": PF.to_comp(U["fser"]), "h5c": PF.to_comp(U["h5"]),
              "h9c": PF.to_comp(U["h9"])})
    return U


def sector_charges(sec):
    fl, fr, hh = PF.SECTORS[sec]
    return PF.SM[fl], PF.SM[fr], (PF.SM["H"] if hh == "H" else -PF.SM["H"])


def part_K3(U):
    mp.mp.dps = 50
    t0 = mp.mpc("0.1", "1.1")
    rows, worst_law, worst_K, any_one = [], mp.mpf(0), mp.mpf(0), False
    for (a, b) in lines_of(N):
        if gcd(a, N) != 1:
            continue
        eps, c = keeps((a, b), T10, N)
        line = (b, a)
        for sec in PF.SECTORS:
            qs = sector_charges(sec)
            Qp = qs[0] ** 2 + qs[1] ** 2 - qs[2] ** 2
            I0 = PF.integrands(U, t0, qs, line, N)
            I1 = PF.integrands(U, t0 + 10, qs, line, N)
            chi = mp.expjpi(2 * mp.mpf(eps * c * Qp) / N)
            row = {"line (a, b)": [a, b], "eps": eps, "c": c, "sector": sec, "law turns": float((eps * c * Qp / N) % 1)}
            for key in I0:
                A0, A1 = I0[key], I1[key]
                den = max(abs(x) for r in A0 for x in r)
                if den == 0:
                    row[key] = None
                    continue
                target = 1 if key.startswith("K") else chi
                err = max(abs(A1[i][k] - target * A0[i][k]) for i in range(len(A0)) for k in range(len(A0[0]))) / den
                row[key] = float(err)
                if key.startswith("K"):
                    worst_K = max(worst_K, err)
                else:
                    worst_law = max(worst_law, err)
            any_one |= gcd(c, N) == 1 and abs(chi - 1) < 1e-3
            rows.append(row)
    PF.NS = (N,)
    v3 = PF.V3(U)
    v3_one = any(gcd(r["c"], N) == 1 and (r["eps"] * r["c"] * QPF[r["sector"]]) % N == 0 for r in v3["rows"])
    holds = bool(worst_law < 1e-25 and worst_K < 1e-25 and not any_one and v3["holds"] and not v3_one)
    return {"T^10 rows": rows, "T^10 worst Y law error": float(worst_law), "T^10 worst K": float(worst_K),
            "T^10 some phase equal to 1 where c is prime to 10": bool(any_one),
            "W92's V3 at N = 10": v3, "V3: the law's phase equal to 1 where c is prime to 10": bool(v3_one),
            "holds": holds}


# ----------------------------------------------------------------------------------------------- K4
def part_K4(U):
    mp.mp.dps = 60
    t0 = mp.mpc("0.1", "1.1")
    pts = [t0 + 10 * j for j in range(10)]
    psi = (Fr(1, N), Fr(0))
    out = {"minimal": {}, "per field": {}}
    V0 = [W91.ev_generator(0, 0, (Fr(0), Fr(0)), t, Fr(40)) for t in pts]
    VR = [W91.ev_generator(REF[0], REF[1], psi, t, Fr(40)) for t in pts]
    d = {u: V0[1][u] / V0[0][u] for u in ("i", "j", "k")}
    d["1"] = VR[1]["1"] / VR[0]["1"]
    worst_tw, ctrl = mp.mpf(0), []
    for u in ("i", "j", "k"):
        S = mp.fsum(V0[j][u] / d[u] ** j for j in range(10))
        ctrl.append(float(abs(S) / mp.fsum(abs(V0[j][u]) for j in range(10))))
    S = mp.fsum(VR[j]["1"] / d["1"] ** j for j in range(10))
    ctrl.append(float(abs(S) / mp.fsum(abs(VR[j]["1"]) for j in range(10))))
    for name, (qL, qR) in W91.SECTORS.items():
        V = [W91.ev_generator(qL + qR, qL - qR, psi, t, Fr(40)) for t in pts]
        rel = {}
        zero = set().union(*(zero_channels([v]) for v in V))
        for u in UNITS:
            if u in zero:
                rel[u] = "identically zero, not tested"
                continue
            S = mp.fsum(V[j][u] / d[u] ** j for j in range(10))
            rel[u] = float(abs(S) / mp.fsum(abs(V[j][u]) for j in range(10)))
            worst_tw = max(worst_tw, rel[u])
        out["minimal"][name] = rel
    out["minimal"]["controls (untwisted i, j, k; reference 1)"] = ctrl
    mp.mp.dps = 50
    line = (0, 1)
    worst_pf, ctrl_pf = mp.mpf(0), {}
    for sec in list(PF.SECTORS) + ["control (all charges zero)"]:
        qs = (0, 0, 0) if sec.startswith("control") else sector_charges(sec)
        Is = [PF.integrands(U, t, qs, line, N) for t in pts]
        rel = {}
        for key in Is[0]:
            if key.startswith("K"):
                continue
            nr, nc = len(Is[0][key]), len(Is[0][key][0])
            num = max(abs(mp.fsum(Is[j][key][i][k] for j in range(10))) for i in range(nr) for k in range(nc))
            den = max(mp.fsum(abs(Is[j][key][i][k]) for j in range(10)) for i in range(nr) for k in range(nc))
            rel[key] = float(num / den) if den else None
            if not sec.startswith("control") and den:
                worst_pf = max(worst_pf, num / den)
        if sec.startswith("control"):
            ctrl_pf = rel
        else:
            out["per field"][sec] = rel
    out["per field"]["control (all charges zero)"] = ctrl_pf
    ctrl_ok = all(abs(x - 1) < 1e-20 for x in ctrl) and all(v is not None and abs(v - 1) < 1e-20
                                                            for v in ctrl_pf.values())
    out["worst twisted sum, minimal"] = float(worst_tw)
    out["worst twisted sum, per field"] = float(worst_pf)
    out["controls give ten times the value"] = bool(ctrl_ok)
    out["holds"] = bool(worst_tw < 1e-25 and worst_pf < 1e-25 and ctrl_ok)
    return out


# ----------------------------------------------------------------------------------------------- R
def part_R(K1, K2):
    census = {}
    for n in range(2, 17):
        L = lines_of(n)
        cs = []
        for w in L:
            gam, _ = conj_T(w, n)
            kc = keeps(w, gam, n)
            cs.append(kc[1] if kc else None)
        c_one = all(c in (1, n - 1) for c in cs)
        surv = {f"minimal {s}": Q % n == 0 for s, Q in QMIN.items()}
        surv.update({f"per field {s}": Q % n == 0 for s, Q in QPF.items()})
        census[str(n)] = {"lines": len(L), "c = +-1 on every line": c_one,
                          "survivors": sorted(k for k, v in surv.items() if v),
                          "all three survive, minimal": all(surv[f"minimal {s}"] for s in QMIN),
                          "all three survive, per field": all(surv[f"per field {s}"] for s in QPF)}
    counted = [r for r in K1["rows"] if tuple(r["line (a, b)"]) == COUNTED]
    phases = [{"line (a, b)": r["line (a, b)"], "sector": r["sector"], "c": r["c"],
               "cycles": r["cycles"], "identity channel turns": r["identity channel turns"]} for r in K2["rows"]
              if r.get("element")]
    return {"census over N = 2..16": census, "the counted line (4, 5)": counted,
            "the measured phases (minimal)": phases}


def run(out):
    t0 = time.time()
    out["K0"] = part_K0()
    print(f"K0 at {time.time() - t0:.0f} s", flush=True)
    out["K1"], chosen = part_K1()
    print(f"K1 at {time.time() - t0:.0f} s", flush=True)
    out["K2"] = part_K2(chosen)
    print(f"K2 at {time.time() - t0:.0f} s", flush=True)
    U = build()
    out["unit residuals"] = {k: float(v) for k, v in U["resid"].items()}
    print(f"units at {time.time() - t0:.0f} s", flush=True)
    out["K3"] = part_K3(U)
    print(f"K3 at {time.time() - t0:.0f} s", flush=True)
    out["K4"] = part_K4(U)
    print(f"K4 at {time.time() - t0:.0f} s", flush=True)
    out["R"] = part_R(out["K1"], out["K2"])
    out["cells"] = {k: out[k]["holds"] for k in ("K0", "K1", "K2", "K3", "K4")}


def main():
    root = HERE.parents[2]
    _ROOT["<repo>"] = str(root)
    _ROOT["<home>"] = str(Path.home())
    t0 = time.time()
    out = {"arc": "W171", "rule": "W171_RULE.md", "status": "one run", "python": sys.version.split()[0],
           "mpmath": mp.__version__, "machine": platform.machine()}
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        try:
            run(out)
        except Exception:  # noqa: BLE001  (a failed run is a failed launch, disclosed as such)
            out["run_failed"] = sanitize(traceback.format_exc()[-4000:])
    out["warnings"] = sorted({sanitize(f"{w.category.__name__}: {w.message}") for w in caught})
    out["seconds"] = round(time.time() - t0, 1)
    OUT.write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
    print(json.dumps(out.get("cells"), indent=1))
    if "run_failed" in out:
        print("run failed")


if __name__ == "__main__":
    main()
