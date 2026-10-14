"""W68: residual charges at omega. The parameter-free sections of rho_R at the weights -1/2, 3/2 and 7/2, the eigenline
of the stabiliser of omega that each takes there, every pair's Yukawa Y(a; c) at omega, and the powers of the
displacement delta = |tau - omega| with which m1/m3 and m2/m3 grow near omega. The rule (W68_RULE.md, with its
correction to G4 before any code) was committed before this script.

  G1  the sections: the one-dimensional placements at each weight, and the 40-digit solves
  G2  the eigenlines at omega: -1/2 on l_w, 3/2 on the real axis, 7/2 on l_w2
  G3  the pairs at omega: rank one, (0, 1, 1) or (1, 1, 1), by their two lines
  G4  the powers near omega
  plus the read-outs: the dimension table, every pair's powers and coefficients, the distinct patterns

Run: python3 the_residual_charges_at_omega.py  ->  the_residual_charges_at_omega.json beside it.
"""
import itertools
import json
import sys
from fractions import Fraction
from pathlib import Path

import mpmath as mp
import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_cusp_unit_as_a_vector as CU  # noqa: E402  (W64: the double-precision collocation)
import the_index_on_the_weaves_surface as IW  # noqa: E402  (W45: the chi formula)
import the_second_unit as SU  # noqa: E402  (W65: the 40-digit tools and the sample)

OUT = HERE / "the_residual_charges_at_omega.json"
mp.mp.dps = 40
I = mp.mpc(0, 1)
W3 = mp.exp(2 * mp.pi * I / 3)
OMEGA = SU.OMEGA
WEIGHTS = (Fraction(-1, 2), Fraction(3, 2), Fraction(7, 2))
LINES = SU.LINES
EIG = {"axis": [mp.mpf(1), mp.mpf(-1), mp.mpf(-1)], "l_w": [-W3, mp.mpf(1), W3 ** 2],
       "l_w2": [-W3 ** 2, mp.mpf(1), W3]}
EXPECT = {Fraction(-1, 2): "l_w", Fraction(3, 2): "axis", Fraction(7, 2): "l_w2"}
DELTAS = (mp.mpf("1e-4"), mp.mpf("1e-3"), mp.mpf("1e-2"))
ZERO = mp.mpf("1e-30")
PT = np.array([[1, 0, 0], [0, 0, 1], [0, -1, 0]])
PS = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 1]])


def solve(units, k, norm_line, N=30, M=120):
    """W65's collocation at weight k, with the lowest allowed coefficient on norm_line set to 1"""
    u = dict(zip(LINES, units))
    n0 = -u[norm_line]
    cols = [(l, n) for l in LINES for n in range(-u[l], N) if not (l == norm_line and n == n0)]
    thetas = [mp.pi / 3 + mp.mpf("0.02") + j * (mp.pi / 3 - mp.mpf("0.04")) / (M - 1) for j in range(M)]
    A = mp.matrix(3 * M, len(cols))
    b = mp.matrix(3 * M, 1)
    kk = mp.mpf(k.numerator) / k.denominator
    for r, th in enumerate(thetas):
        t = mp.exp(I * th)
        ts, tk = -1 / t, mp.power(t, kk)
        for c, (l, n) in enumerate(cols):
            e = n + SU.LAM[l]
            sc = mp.exp(2 * mp.pi * e * SU.H0)
            v2 = SU.matvec(SU.RS, SU.B[l])
            for q in range(3):
                A[3 * r + q, c] = (SU.B[l][q] * SU.qp(e, ts) - tk * v2[q] * SU.qp(e, t)) * sc
        e = n0 + SU.LAM[norm_line]
        v2 = SU.matvec(SU.RS, SU.B[norm_line])
        for q in range(3):
            b[3 * r + q] = -(SU.B[norm_line][q] * SU.qp(e, ts) - tk * v2[q] * SU.qp(e, t))
    Q, Rm = mp.qr(A, mode="skinny")
    x = mp.lu_solve(Rm, Q.H * b)
    res = mp.norm(A * x - b) / mp.norm(b)
    terms = [(norm_line, n0 + SU.LAM[norm_line], mp.mpf(1))] + [
        (l, n + SU.LAM[l], x[c] * mp.exp(2 * mp.pi * (n + SU.LAM[l]) * SU.H0)) for c, (l, n) in enumerate(cols)]
    return terms, float(res)


def dims():
    rS, rT = CU.reps(PT, PS)
    table = {}
    for k in WEIGHTS:
        for u in itertools.product((0, 1), repeat=3):
            d, gap, *_ = CU.collocate(rS, rT, k, u)
            chi = IW.chi(k, rS, rT)[0] + sum(u)
            table[(k, u)] = {"dimension": d, "chi + sum(u)": round(float(chi), 9), "gap": gap}
    return table


def parallel(f, g):
    return SU.sine(f, g) < mp.mpf("1e-25")


def main():
    table = dims()
    sections = []                              # (name, k, u, terms, residual)
    for k in WEIGHTS:
        for u in itertools.product((0, 1), repeat=3):
            if table[(k, u)]["dimension"] != 1:
                continue
            order = [l for l, on in zip(LINES, u) if on] + [l for l, on in zip(LINES, u) if not on]
            best = None
            for line in order:
                terms, res = solve(u, k, line)
                if best is None or res < best[1]:
                    best = (terms, res, line)
                if res < 1e-20:
                    break
            f = (lambda tm: (lambda t: SU.evaluate(tm, t)))(best[0])
            probe = [mp.mpc("0.13", "1.21"), mp.mpc("-0.31", "1.07")]
            dup = next((s for s in sections if s["k"] == k and all(parallel(f(t), s["f"](t)) for t in probe)), None)
            if dup is not None:
                dup["also the placements"].append(str(u))
                continue
            sections.append({"name": f"k = {k}, u = {u}", "k": k, "u": u, "f": f, "residual": best[1],
                             "normalized on": best[2], "also the placements": []})
    # G1
    one_dim = {str(k): [str(u) for u in itertools.product((0, 1), repeat=3) if table[(k, u)]["dimension"] == 1]
               for k in WEIGHTS}
    unit_ok = all(set(one_dim[str(k)]) == {"(1, 0, 0)", "(0, 1, 0)", "(0, 0, 1)"} for k in WEIGHTS[:2])
    g1 = {"one-dimensional placements per weight": one_dim,
          "the sections kept (distinct)": [s["name"] for s in sections],
          "residuals": {s["name"]: s["residual"] for s in sections},
          "holds": bool(unit_ok and len(one_dim[str(WEIGHTS[2])]) >= 1 and all(s["residual"] < 1e-20
                                                                               for s in sections))}
    # G2
    rows, ok2 = {}, True
    for s in sections:
        v = s["f"](OMEGA)
        scale = SU.norm(s["f"](OMEGA + I * mp.mpf("1e-3")))
        if SU.norm(v) < mp.mpf("1e-20") * scale:      # a section vanishing at omega has no direction there
            s["line"] = "vanishes at omega"
            s["isotropic everywhere"] = False
            rows[s["name"]] = {"vanishes at omega": True}
            ok2 = False
            continue
        sines = {name: float(SU.sine(v, line)) for name, line in EIG.items()}
        nearest = min(sines, key=sines.get)
        s["line"] = nearest
        s["isotropic everywhere"] = bool(max(abs(SU.dot(s["f"](t), s["f"](t))) / SU.norm(s["f"](t)) ** 2
                                             for t in SU.SAMPLE) < ZERO)
        rows[s["name"]] = {"sines to the axis, l_w, l_w2": sines, "nearest": nearest,
                           "isotropic at every tau": s["isotropic everywhere"]}
        ok2 &= nearest == EXPECT[s["k"]] and sines[nearest] < 1e-20
    g2 = {"per section": rows, "holds": bool(ok2)}
    # G3 and G4
    pairs, ok3, ok4 = {}, True, True
    for a, c in itertools.combinations_with_replacement(sections, 2):
        la, lc = a["line"], c["line"]
        S0 = mp.svd_c(SU.Yuk(a["f"](OMEGA), c["f"](OMEGA)), compute_uv=False)
        r1, r2 = (S0[2] / S0[0], S0[1] / S0[0]) if S0[0] > 0 else (mp.nan, mp.nan)
        if "vanishes at omega" in (la, lc):
            kind, good = "a member vanishes at omega", False
        elif la != "axis" and lc != "axis":
            kind, good = "two isotropic lines: rank one", r2 < 1e-20
        elif la == "axis" and lc == "axis":
            kind, good = "two on the axis: m1 = m2 = m3", abs(r1 - 1) < 1e-20 and abs(r2 - 1) < 1e-20
        else:
            kind, good = "isotropic with the axis: m1 = 0, m2 = m3", r1 < 1e-20 and abs(r2 - 1) < 1e-20
        ok3 &= bool(good)
        ms = []
        for d in DELTAS:
            t = OMEGA + I * d
            S = mp.svd_c(SU.Yuk(a["f"](t), c["f"](t)), compute_uv=False)
            ms.append((S[2] / S[0], S[1] / S[0]))

        def power(i):
            vals = [m[i] for m in ms]
            if all(v < ZERO for v in vals):
                return "identically zero", None
            if any(v < ZERO for v in vals):
                return "zero at some delta", None
            p01 = float(mp.log(vals[1] / vals[0]) / mp.log(10))
            p12 = float(mp.log(vals[2] / vals[1]) / mp.log(10))
            return p01, p12
        p1, p1b = power(0)
        p2, p2b = power(1)
        coef = {}
        if isinstance(p2, float):
            coef["m2/m3 / delta^p2 at 1e-4"] = float(ms[0][1] / DELTAS[0] ** round(p2))
        if isinstance(p1, float):
            coef["m1/m3 / delta^p1 at 1e-4"] = float(ms[0][0] / DELTAS[0] ** round(p1))
        key = f"{a['name']} | {c['name']}"
        pairs[key] = {"lines at omega": [la, lc], "kind": kind, "at omega: m1/m3, m2/m3": [float(r1), float(r2)],
                      "holds at omega": bool(good), "p1 (1e-4 to 1e-3), (1e-3 to 1e-2)": [p1, p1b],
                      "p2 (1e-4 to 1e-3), (1e-3 to 1e-2)": [p2, p2b], "coefficients": coef}
        # G4
        ks = {a["k"], c["k"]}
        if ks == {Fraction(-1, 2), Fraction(7, 2)}:
            lo, hi = (a, c) if a["k"] == Fraction(-1, 2) else (c, a)
            if not hi["isotropic everywhere"]:
                ok4 &= isinstance(p2, float) and abs(p2 - 1) < 0.05
                if lo["isotropic everywhere"]:
                    ok4 &= p1 == "identically zero"
                else:
                    ok4 &= isinstance(p1, float) and abs(p1 - 2) < 0.05
        if a["k"] == c["k"] == Fraction(-1, 2):
            n_iso = int(a["isotropic everywhere"]) + int(c["isotropic everywhere"])
            if n_iso == 1:
                ok4 &= p1 == "identically zero" and isinstance(p2, float) and abs(p2 - 2) < 0.05
            elif n_iso == 2:
                ok4 &= p2 == "identically zero"
    g3 = {"holds": bool(ok3)}
    g4 = {"holds": bool(ok4)}
    patterns = {}
    for key, row in pairs.items():
        p1, p2 = row["p1 (1e-4 to 1e-3), (1e-3 to 1e-2)"][0], row["p2 (1e-4 to 1e-3), (1e-3 to 1e-2)"][0]
        pat = (p1 if isinstance(p1, str) else round(p1, 2), p2 if isinstance(p2, str) else round(p2, 2))
        patterns.setdefault(str(pat), []).append(key)
    out = {"status": "W68: residual charges at omega (the rule W68_RULE.md first, corrected before any code; one run)",
           "G1": g1, "G2": g2, "G3": g3, "G4": g4}
    out["cells"] = {k: out[k]["holds"] for k in ("G1", "G2", "G3", "G4")}
    out["read-outs"] = {"the dimension table": {f"k = {k}, u = {u}": v for (k, u), v in table.items()},
                        "every pair": pairs, "the distinct patterns (p1, p2)": patterns,
                        "duplicates folded": {s["name"]: s["also the placements"] for s in sections}}
    OUT.write_text(json.dumps(out, indent=1, default=lambda x: float(x) if isinstance(x, (np.floating, mp.mpf))
                              else str(x)) + "\n", encoding="utf-8")
    print(json.dumps(out["cells"], indent=1))


if __name__ == "__main__":
    main()
