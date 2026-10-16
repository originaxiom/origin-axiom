"""W95: the weave's traces by discriminant (the fresh look's N2), in the surface frame's neutral couplings.
The rule (W95_RULE.md, 6bae47053) was committed before this script.

  V1  the threads: each Zagier cycle's word has the cycle's discriminant and trace; the cycles with words of length
      <= 10 correspond one to one, by rotation, to the Lyndon words of length <= 10 with both letters and D <= 300
  V2  invariance: series values of K and Y at tau, tau + 1, tau - 1 and -1/tau on the unit arc, no reduction, 1e-30
  V3  rank one at a point: sigma2/sigma1 of Y below 1e-25 at every CM point and at six further points
  V4  the CM side: the rank law by the number n_D of reduced primitive forms
  V5  every thread has three masses: m1/m3 > 1e-30
  V6  convergence: ln(m1/m3), ln(m2/m3) between the two node counts below 1e-6, every class and every D-trace
  V7  precision: 80 against 100 digits on the root and on the class with the most nodes, 1e-10
  V8  the cusp carries the trace: each D-trace against the sum over its highest classes, 1e-3, D in [100, 300]
  read-outs: the record's places; the law in D; kappa(D); the thread masses; the data (seen, no claim)

The instrument:
  - W72's units (F_i, F+, F- at 3/2; R at -1/2; h5 at 5/2) from the_per_field_units.build_units; rounded to Gaussian
    integers if every line coefficient lies within 1e-30 of one, otherwise used as built;
  - no hypercharge line: K = sum_c F_i,c conj(F_k,c) y^(3/2), Y = dot(G'(F_i, F_k; R), conj(h5)) y^(5/2);
  - each point reduced to the standard fundamental domain, the units evaluated there by their series (the matrices
    are invariant, V2);
  - the cycle integral: trapezoid in arclength over one period of the word's own axis, centred on its apex, nodes at
    half steps, ceil(30 P (1 + H)) and ceil(37.5 P (1 + H)) with H = sqrt(D) / (2 a_min); 80 digits;
  - masses: singular values of T(K)^(-1/2) T(Y) (T(K)^(-1/2))^T, ascending.

Run: python3 the_traces_by_discriminant.py  ->  the_traces_by_discriminant.json beside it (4 processes).
"""
import json
import math
import multiprocessing as mpr
import sys
import time
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
OUT = HERE / "the_traces_by_discriminant.json"
HZ = HERE / "received" / "HZ2021_running_masses_MZ.json"
DPS, DPS_HI = 80, 100
DMAX = 300
SLOPE_MIN, V8_MIN = 200, 100
NAMES = ("F0", "F1", "F2", "R", "h5")
UNITS, LO, HI = None, 0, 0


# ------------------------------------------------------------------------------------------------ the threads
def mat(w):
    A, B, C, D = 1, 0, 0, 1
    for ch in w:
        if ch == "L":
            A, B, C, D = A + B, B, C + D, D
        else:
            A, B, C, D = A, A + B, C, C + D
    return A, B, C, D


def rot_min(w):
    return min(w[i:] + w[:i] for i in range(len(w)))


def lyndon_words(nmax):
    out = []
    for n in range(2, nmax + 1):
        for k in range(1 << n):
            w = "".join("R" if (k >> (n - 1 - i)) & 1 else "L" for i in range(n))
            if all(w < w[i:] + w[:i] for i in range(1, n)):
                out.append(w)
    return out


def word_disc(w):
    A, B, C, D = mat(w)
    g = math.gcd(math.gcd(C, D - A), B)
    t = A + D
    return (t * t - 4) // (g * g), t


def discriminants(sign):
    out = []
    for D in range(3, DMAX + 1):
        d = sign * D
        if d % 4 not in (0, 1):
            continue
        if sign > 0 and (D < 5 or math.isqrt(D) ** 2 == D):
            continue
        out.append(d)
    return out


def zagier_cycles(D):
    """the narrow classes of primitive forms of discriminant D > 0, as cycles of Zagier-reduced forms"""
    red = set()
    for b in range(math.isqrt(D) + 1, (D + 1) // 2 + 2):
        if (b * b - D) % 4:
            continue
        ac = (b * b - D) // 4
        for a in range(1, ac + 1):
            if ac % a == 0:
                c = ac // a
                if b > a + c and math.gcd(math.gcd(a, b), c) == 1:
                    red.add((a, b, c))
    r = math.isqrt(D)
    seen, cycles = set(), []
    for Q in sorted(red):
        if Q in seen:
            continue
        cyc, q = [], Q
        while q not in seen:
            seen.add(q)
            a, b, c = q
            n = (b + r) // (2 * c) + 1
            cyc.append((q, n))
            q = (c, -b + 2 * c * n, a - b * n + c * n * n)
            assert q in red, (D, q)
        assert q == Q
        cycles.append(cyc)
    return cycles


def class_record(D, cyc):
    digits = [n for _, n in cyc]
    word = "".join("L" + "R" * (n - 2) for n in digits)
    A, B, C, Dd = 1, 0, 0, 1
    for n in digits:                     # the automorph, the product of S R^n = [[0, -1], [1, n]]
        A, B, C, Dd = B, -A + n * B, Dd, -C + n * Dd
    amin = min(min(q[0], q[2]) for q, _ in cyc)
    return {"D": D, "form": list(cyc[0][0]), "digits": digits, "word": word, "length": len(word),
            "automorph trace": A + Dd, "a_min": amin}


# ------------------------------------------------------------------------------------------------ units and matrices
def build_units():
    import the_per_field_units as PF
    U = PF.build_units()
    src = {"F0": U["F32"][0], "F1": U["F32"][1], "F2": U["F32"][2], "R": U["FM12"][1], "h5": U["h5"]}
    mp.mp.dps = DPS_HI
    worst = mp.mpf(0)
    for ser in src.values():
        for a in ser.values():
            worst = max(worst, abs(mp.re(a) - mp.nint(mp.re(a))), abs(mp.im(a) - mp.nint(mp.im(a))))
    exact = bool(worst < mp.mpf(10) ** -30)
    units = {}
    for name, ser in src.items():
        comp = {}
        for (l, n8), a in ser.items():
            if exact:
                a = mp.mpc(mp.nint(mp.re(a)), mp.nint(mp.im(a)))
            v = comp.setdefault(int(n8), [mp.mpc(0)] * 3)
            for k in range(3):
                if PF.B[l][k] != 0:
                    v[k] += a * mp.mpc(PF.B[l][k])
        units[name] = comp
    info = {"integer coefficients": exact, "largest distance to a Gaussian integer": mp.nstr(worst, 5),
            "build residuals": {k: float(v) for k, v in U["resid"].items()}}
    return units, info


def reduce(t):
    for _ in range(200000):
        n = int(mp.nint(t.real))
        if n:
            t = t - n
        if abs(t) < 1:
            t = -1 / t
        else:
            return t
    raise RuntimeError("reduction did not end")


def series(t):
    z = mp.exp(2j * mp.pi * t / 8)
    zi = 1 / z
    zp = {0: mp.mpc(1)}
    for k in range(1, HI + 1):
        zp[k] = zp[k - 1] * z
    for k in range(1, -LO + 1):
        zp[-k] = zp[-k + 1] * zi
    return {n: [mp.fsum(v[c] * zp[e] for e, v in UNITS[n].items()) for c in range(3)] for n in NAMES}


def dot(X, Y):
    return X[0] * Y[0] + X[1] * Y[1] + X[2] * Y[2]


def Gp(X, Y, v):
    a, b, c = dot(v, Y), dot(v, X), dot(X, Y)
    return [a * X[i] + b * Y[i] - c * v[i] for i in range(3)]


def mats_at(u):
    """K and Y from the series at u itself (no reduction)"""
    V = series(u)
    y = u.imag
    F = [V["F0"], V["F1"], V["F2"]]
    v = V["R"]
    h = [mp.conj(x) for x in V["h5"]]
    y15, y25 = y ** mp.mpf(1.5), y ** mp.mpf(2.5)
    K, Y = mp.matrix(3, 3), mp.matrix(3, 3)
    for i in range(3):
        for k in range(3):
            K[i, k] = dot(F[i], [mp.conj(x) for x in F[k]]) * y15
            Y[i, k] = dot(Gp(F[i], F[k], v), h) * y25
    return K, Y


def mats(t):
    return mats_at(reduce(t))


def masses(K, Y):
    """(None, eigenvalues) when K is singular (an eigenvalue at most 1e-60 of the largest): the masses are undefined"""
    K = (K + K.H) / 2
    ev, Uh = mp.eighe(K)
    if min(ev) <= max(ev) * mp.mpf(10) ** -60:
        return None, ev
    Ih = Uh * mp.diag([1 / mp.sqrt(x) for x in ev]) * Uh.H
    sv = sorted(abs(x) for x in mp.svd_c(Ih * Y * Ih.T, compute_uv=False))
    return sv, min(ev)


def ratios(sv):
    return [mp.log(sv[0] / sv[2]), mp.log(sv[1] / sv[2])]


# ------------------------------------------------------------------------------------------------ cycle integrals
def cycle_integral(args):
    key, word, D, amin, dps, counts = args
    mp.mp.dps = dps
    t0 = time.time()
    A, B, C, Dd = mat(word)
    tr = A + Dd
    x0 = mp.mpf(A - Dd) / (2 * C)
    rho = mp.sqrt(mp.mpf(tr * tr - 4)) / (2 * abs(C))
    P = 2 * mp.acosh(mp.mpf(tr) / 2)
    H = mp.sqrt(D) / (2 * amin)
    out = {}
    for lab, n0 in counts:
        N = int(mp.ceil(n0 * P * (1 + H)))
        h = P / N
        K, Y = mp.zeros(3, 3), mp.zeros(3, 3)
        for j in range(N):
            s = -P / 2 + (j + mp.mpf(1) / 2) * h
            k, y = mats(x0 + rho * (mp.tanh(s) + 1j / mp.cosh(s)))
            K += k
            Y += y
        K, Y = K * h, Y * h
        out[lab] = {"N": N, "K": [[K[i, k] for k in range(3)] for i in range(3)],
                    "Y": [[Y[i, k] for k in range(3)] for i in range(3)]}
    return key, out, float(P), float(H), round(time.time() - t0, 1)


def worker_init(units, lo, hi):
    global UNITS, LO, HI
    UNITS, LO, HI = units, lo, hi


# ------------------------------------------------------------------------------------------------ the CM side
def cm_forms(D):
    """reduced primitive positive-definite forms of discriminant D < 0"""
    out = []
    a = 1
    while 3 * a * a <= -D:
        for b in range(-a + 1, a + 1):
            if (b * b - D) % (4 * a):
                continue
            c = (b * b - D) // (4 * a)
            if c < a or (b < 0 and a == c) or math.gcd(math.gcd(a, b), c) != 1:
                continue
            out.append((a, b, c))
        a += 1
    return out


def s(x, n=30):
    return mp.nstr(x, n)


def main():
    global UNITS, LO, HI
    t00 = time.time()
    out = {"rule": "W95_RULE.md (6bae47053)", "status": "one run", "dps": DPS, "D range": [-DMAX, DMAX]}
    units, info = build_units()
    UNITS = units
    LO = min(min(u) for u in units.values())
    HI = max(max(u) for u in units.values())
    info["exponents (eighths)"] = [LO, HI]
    info["build seconds"] = round(time.time() - t00, 1)
    out["units"] = info
    mp.mp.dps = DPS

    # V1: the threads
    classes, bad = [], []
    for D in discriminants(+1):
        for cyc in zagier_cycles(D):
            rec = class_record(D, cyc)
            wd, wt = word_disc(rec["word"])
            if wd != D or wt != rec["automorph trace"]:
                bad.append([D, rec["word"][:40], wd, wt, rec["automorph trace"]])
            classes.append(rec)
    short = sorted(rot_min(c["word"]) for c in classes if c["length"] <= 10)
    lyn = sorted(w for w in lyndon_words(10) if "L" in w and "R" in w and word_disc(w)[0] <= DMAX)
    out["V1"] = {"classes": len(classes), "discriminants": len(discriminants(+1)),
                 "word disc or trace mismatches": bad, "cycles with words of length <= 10": len(short),
                 "Lyndon words of length <= 10 with D <= 300": len(lyn), "duplicates": len(short) - len(set(short)),
                 "holds": bool(not bad and short == lyn)}
    print("V1", out["V1"]["holds"], len(classes), flush=True)

    # V2: invariance on the unit arc
    worst = mp.mpf(0)
    for th in (80, 95, 110):
        t = mp.expjpi(mp.mpf(th) / 180)
        K0, Y0 = mats_at(t)
        for g in (t + 1, t - 1, -1 / t):
            K1, Y1 = mats_at(g)
            worst = max(worst, mp.norm(K1 - K0) / mp.norm(K0), mp.norm(Y1 - Y0) / mp.norm(Y0))
    out["V2"] = {"largest relative difference": s(worst, 5), "holds": bool(worst < mp.mpf(10) ** -30)}
    print("V2", out["V2"], flush=True)

    # the CM side (V3 partly, V4)
    cm, v3 = {}, mp.mpf(0)
    v4ok = True
    for D in discriminants(-1):
        forms = cm_forms(D)
        K, Y = mp.zeros(3, 3), mp.zeros(3, 3)
        for (a, b, c) in forms:
            w = 3 if (a, b, c) == (1, 1, 1) else 2 if (a, b, c) == (1, 0, 1) else 1
            k, y = mats(mp.mpc(-b, mp.sqrt(-D)) / (2 * a))
            sy = mp.svd_c(y, compute_uv=False)
            v3 = max(v3, sorted(abs(x) for x in sy)[1] / max(abs(x) for x in sy))
            K += k / w
            Y += y / w
        sv, emin = masses(K, Y)
        n = len(forms)
        if sv is None:
            rank = sum(1 for x in emin if x > max(emin) * mp.mpf(10) ** -60)
            cm[str(D)] = {"n_D": n, "K rank": rank, "m1/m3": "undefined (K singular)",
                          "m2/m3": "undefined (K singular)", "as predicted": False}
            v4ok = False
            continue
        r1, r2 = sv[0] / sv[2], sv[1] / sv[2]
        tiny = mp.mpf(10) ** -20
        ok = (r1 < tiny and r2 < tiny) if n == 1 else (r1 < tiny < r2) if n == 2 else (r1 > tiny and r2 > tiny)
        v4ok = v4ok and ok
        cm[str(D)] = {"n_D": n, "m1/m3": s(r1, 8), "m2/m3": s(r2, 8), "as predicted": bool(ok)}
    extra = (mp.mpc("0.3", 1), mp.mpc("0.3", 2), mp.mpc("0.3", 3), mp.mpc("0.3", 5), mp.mpc("0.3", 8),
             mp.mpc("0.21", "1.37"))
    for t in extra:
        sy = sorted(abs(x) for x in mp.svd_c(mats(t)[1], compute_uv=False))
        v3 = max(v3, sy[1] / sy[2])
    out["V3"] = {"largest sigma2/sigma1": s(v3, 5), "holds": bool(v3 < mp.mpf(10) ** -25)}
    out["V4"] = {"holds": bool(v4ok), "by D": cm}
    print("V3", out["V3"], "V4", v4ok, flush=True)

    # the cycle integrals: every class at 80 digits (both counts); V7 at 100 digits on two classes
    tasks = []
    for i, c in enumerate(classes):
        tasks.append(((i, DPS), c["word"], c["D"], c["a_min"], DPS, (("n1", 30), ("n2", mp.mpf("37.5")))))
    tasks.sort(key=lambda a: -float(2 * mp.acosh(mp.mpf(word_disc(a[1])[1]) / 2) * (1 + math.sqrt(a[2]) / (2 * a[3]))))
    root = next(i for i, c in enumerate(classes) if c["D"] == 5)
    big = tasks[0][0][0]
    for i in sorted({root, big}):
        c = classes[i]
        tasks.append(((i, DPS_HI), c["word"], c["D"], c["a_min"], DPS_HI, (("n2", mp.mpf("37.5")),)))
    res = {}
    with mpr.get_context("fork").Pool(4, initializer=worker_init, initargs=(UNITS, LO, HI)) as pool:
        for key, r, P, H, sec in pool.imap_unordered(cycle_integral, tasks):
            for lab in r:
                r[lab]["K"], r[lab]["Y"] = mp.matrix(r[lab]["K"]), mp.matrix(r[lab]["Y"])
            res[key] = (r, P, H, sec)
            print("done", key, sec, flush=True)
    mp.mp.dps = DPS

    # per class: V5, V6
    v5, v6 = True, mp.mpf(0)
    for i, c in enumerate(classes):
        r, P, H, sec = res[(i, DPS)]
        m1, _ = masses(r["n1"]["K"], r["n1"]["Y"])
        m2, emin = masses(r["n2"]["K"], r["n2"]["Y"])
        if m1 is None or m2 is None:
            c.update({"P": P, "H": H, "npts": [r["n1"]["N"], r["n2"]["N"]], "K singular": True, "seconds": sec})
            v5, v6 = False, mp.inf
            continue
        l1, l2 = ratios(m1), ratios(m2)
        d = max(abs(l2[0] - l1[0]), abs(l2[1] - l1[1]))
        v6 = max(v6, d)
        v5 = v5 and bool(m2[0] / m2[2] > mp.mpf(10) ** -30)
        c.update({"P": P, "H": H, "npts": [r["n1"]["N"], r["n2"]["N"]], "ln m1/m3": s(l2[0]), "ln m2/m3": s(l2[1]),
                  "m1/m3": float(m2[0] / m2[2]), "m2/m3": float(m2[1] / m2[2]), "r_calc": float(d),
                  "K posdef": bool(emin > 0), "seconds": sec})
        if c["length"] > 200:
            c["word"] = c["word"][:200] + "..."
    out["V5"] = {"holds": bool(v5)}

    # the D-traces: V6 (traces), V8
    traces, v8, v8n = {}, True, 0
    for D in discriminants(+1):
        idx = [i for i, c in enumerate(classes) if c["D"] == D]
        tot = {lab: [sum((res[(i, DPS)][0][lab]["K"] for i in idx), mp.zeros(3, 3)),
                     sum((res[(i, DPS)][0][lab]["Y"] for i in idx), mp.zeros(3, 3))] for lab in ("n1", "n2")}
        m1, _ = masses(*tot["n1"])
        m2, _ = masses(*tot["n2"])
        if m1 is None or m2 is None:
            traces[str(D)] = {"classes": len(idx), "K singular": True}
            v6 = mp.inf
            continue
        l1, l2 = ratios(m1), ratios(m2)
        d = max(abs(l2[0] - l1[0]), abs(l2[1] - l1[1]))
        v6 = max(v6, d)
        row = {"classes": len(idx), "ln m1/m3": s(l2[0]), "ln m2/m3": s(l2[1]), "m1/m3": float(m2[0] / m2[2]),
               "m2/m3": float(m2[1] / m2[2]), "r_calc": float(d), "kappa": float(l2[0] / l2[1])}
        if V8_MIN <= D and len(idx) >= 2:
            hmax = max(classes[i]["H"] for i in idx)
            top = [i for i in idx if classes[i]["H"] == hmax]
            K = sum((res[(i, DPS)][0]["n2"]["K"] for i in top), mp.zeros(3, 3))
            Y = sum((res[(i, DPS)][0]["n2"]["Y"] for i in top), mp.zeros(3, 3))
            mt = masses(K, Y)[0]
            if mt is None:
                v8, v8n = False, v8n + 1
                row["highest classes"] = "K singular"
                traces[str(D)] = row
                continue
            lt = ratios(mt)
            dd = max(abs(lt[0] - l2[0]), abs(lt[1] - l2[1]))
            row["highest classes"] = len(top)
            row["|trace - highest|"] = float(dd)
            v8 = v8 and bool(dd < mp.mpf(10) ** -3)
            v8n += 1
        traces[str(D)] = row
    out["V6"] = {"largest change": s(v6, 5), "holds": bool(v6 < mp.mpf(10) ** -6)}
    out["V8"] = {"discriminants tested": v8n, "holds": bool(v8)}

    # V7: precision
    v7 = mp.mpf(0)
    for i in sorted({root, big}):
        ma = masses(res[(i, DPS)][0]["n2"]["K"], res[(i, DPS)][0]["n2"]["Y"])[0]
        mb = masses(res[(i, DPS_HI)][0]["n2"]["K"], res[(i, DPS_HI)][0]["n2"]["Y"])[0]
        if ma is None or mb is None:
            v7 = mp.inf
            continue
        lo_, hi_ = ratios(ma), ratios(mb)
        v7 = max(v7, abs(lo_[0] - hi_[0]), abs(lo_[1] - hi_[1]))
    out["V7"] = {"classes": [classes[i]["word"][:40] for i in sorted({root, big})], "largest difference": s(v7, 5),
                 "holds": bool(v7 < mp.mpf(10) ** -10)}

    # read-outs
    places = {str(D): (cm[str(D)] if D < 0 else traces[str(D)]) for D in (-3, -4, 5, 8, 12)}
    places["D = 12 threads"] = [{k: c[k] for k in ("word", "ln m1/m3", "ln m2/m3")} for c in classes if c["D"] == 12]
    fit = {}
    xs = [(math.sqrt(D), traces[str(D)]) for D in discriminants(+1) if SLOPE_MIN <= D and "ln m1/m3" in traces[str(D)]]
    for key in ("ln m1/m3", "ln m2/m3"):
        X = [x for x, _ in xs]
        Yv = [float(r[key]) for _, r in xs]
        mx, my = sum(X) / len(X), sum(Yv) / len(Yv)
        fit[key] = sum((a - mx) * (b - my) for a, b in zip(X, Yv)) / sum((a - mx) ** 2 for a in X)
    hz = json.loads(HZ.read_text(encoding="utf-8"))["masses_GeV"]
    v, sg = hz["value"], hz["sigma"]
    data = {}
    for sec, (f1, f2, f3) in {"up": ("u", "c", "t"), "down": ("d", "s", "b"), "lepton": ("e", "mu", "tau")}.items():
        r = [math.log(v[f1] / v[f3]), math.log(v[f2] / v[f3])]
        rd = [math.hypot(sg[f1] / v[f1], sg[f3] / v[f3]), math.hypot(sg[f2] / v[f2], sg[f3] / v[f3])]
        within = []
        for D, row in traces.items():
            if "ln m1/m3" not in row:
                continue
            z = [(float(row[k]) - r[j]) / math.sqrt(row["r_calc"] ** 2 + rd[j] ** 2 + 0.10 ** 2)
                 for j, k in enumerate(("ln m1/m3", "ln m2/m3"))]
            if z[0] ** 2 + z[1] ** 2 <= 5.991:
                within.append(int(D))
        data[sec] = {"ln m1/m3": r[0], "ln m2/m3": r[1], "kappa": r[0] / r[1], "D-traces within": within}
    out["read-outs"] = {"the record's places": places, "slopes against sqrt D, 200 <= D <= 300": fit,
                        "data (seen; sector-blind frame; no null; no claim)": data}
    out["D-traces"] = traces
    out["classes"] = classes
    out["cells"] = {k: out[k]["holds"] for k in ("V1", "V2", "V3", "V4", "V5", "V6", "V7", "V8")}
    out["seconds"] = round(time.time() - t00, 1)
    OUT.write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8")
    print(out["cells"], out["seconds"], "s")


if __name__ == "__main__":
    main()
