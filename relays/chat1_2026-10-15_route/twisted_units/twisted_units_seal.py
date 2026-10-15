"""THE TWISTED UNITS ON THE LOW THREADS (chat1; sealed with PREREGISTRATION_TWISTED_UNITS.md; run once).

Both readings of the hypercharge line's twist in the thread frame (the owner's ruling; the SM seat's §133):
  per-field (main's construction, S134): every field's units and the Higgs modes dressed by their own charge (W92), R neutral;
  minimal: W72's untwisted units and Higgs, B1656's twisted coupling vector (W91's object, chat1's convention).
On every T-low configuration at N = 9, 11, 12 (tlow_configurations.json: words to length 12 at height <= 3, lines of
exact order N fixed up to sign with N^2 | Q_gamma(w)), for the Standard Model's 6Y charges and the null's 199
gauge-invariant assignments (null_draws.json, |q| <= 18, eligible on the SM's terms, the first 199 in its fixed order), the cells' masses, the CKM moduli and
W66's predicate against HZ2021 (M_Z) and B1612's CKM, as fixed in the preregistration. The instrument is tlow2.py.

Usage: python3 -B twisted_units_seal.py <forms.pkl>   (writes twisted_units_seal_output.json beside itself;
progress lines carry no mass and no score)
"""
import hashlib, json, math, os, pickle, sys, time
from multiprocessing import Pool
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

M_NULL = 199
A_ALLOW = 0.10
CHI95 = {3: 7.815, 6: 12.592}
NPTS_PER_PERIOD, NPTS_CHECK = 30.0, 37.5
CLOSURE_MAX, RCALC_MAX = 1e-20, 1e-6
SEC_DATA = {"up": ("u", "c", "t"), "down": ("d", "s", "b"), "lepton": ("e", "mu", "tau")}
SM = {"Q": 1, "u": -4, "d": 2, "L": -3, "e": 6, "H": 3}
FORMS = sys.argv[1] if len(sys.argv) > 1 else None


def sha(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


def assignments():
    draws = json.load(open(os.path.join(HERE, "null_draws.json")))["draws_in_order"][:M_NULL]
    out = {"SM": SM}
    out.update({f"null{i:03d}": {k: int(v) for k, v in d.items()} for i, d in enumerate(draws)})
    return out


def masses_summary(m, N):
    """per (assignment, reading, sector, cell): ln R2, ln R1 and the left vectors (for the CKM), as floats"""
    out = {}
    for (name, reading, sec), cells in m.items():
        for cell, d in cells.items():
            if d is None:
                out[(name, reading, sec, cell)] = None; continue
            s = [float(x) for x in d["s"]]
            U = [[complex(x) for x in row] for row in d["U"]]
            out[(name, reading, sec, cell)] = {"s": s, "U": U}
    return out


def one_configuration(job):
    import flint, mpmath as mp
    import tlow2 as T2
    idx, N, word, line, P = job
    t0 = time.time()
    rot, M, rho, k, height = T2.thread_geometry(word)
    flint.ctx.prec = 800
    F = T2.Forms(P).prepare()
    F53 = T2.Forms(P, round53=True).prepare()
    flint.ctx.prec = T2.bits_for(height)
    a, b, c, d = M
    Pl = 2 * math.acosh((a + d) / 2)
    n1, n2 = int(round(Pl * NPTS_PER_PERIOD)), int(round(Pl * NPTS_CHECK))
    A = assignments()
    conf1 = T2.configuration(F, word, tuple(line), N, A, n1)
    conf2 = T2.configuration(F, word, tuple(line), N, A, n2)
    conf3 = T2.configuration(F53, word, tuple(line), N, {"SM": SM}, n1)
    m1 = masses_summary(T2.masses(conf1, F, A, N, mp), N)
    m2 = masses_summary(T2.masses(conf2, F, A, N, mp), N)
    m3 = masses_summary(T2.masses(conf3, F53, {"SM": SM}, N, mp), N)
    rec = {"index": idx, "N": N, "word": word, "line": list(line), "rotation": conf1["rot"],
           "line_in_rotation": list(conf1["line_in_rotation"]), "height": height, "bits": conf1["bits"],
           "Npts": [n1, n2], "closure": {f"{t}|{k_}": v for (t, k_), v in conf1["closure"].items()},
           "plan": {f"{a_}|{s_}": [list(v[0]), list(v[1])] for (a_, s_), v in conf1["plan"].items()},
           "cells": {}}
    for key, v in m1.items():
        name, reading, sec, cell = key
        v2 = m2.get(key)
        entry = None
        if v is not None and v2 is not None and min(v["s"]) > 0 and min(v2["s"]) > 0:
            rc = max(abs(math.log(v["s"][i] / v2["s"][i])) for i in range(3))
            if name == "SM":
                v3 = m3.get(key)
                rc53 = max(abs(math.log(v["s"][i] / v3["s"][i])) for i in range(3)) if v3 and min(v3["s"]) > 0 else None
            else:
                rc53 = None
            entry = {"s": v["s"], "U": [[[z.real, z.imag] for z in row] for row in v["U"]], "r_calc": rc,
                     "r_calc_53": rc53}
        rec["cells"]["|".join(key)] = entry
    rec["seconds"] = round(time.time() - t0, 1)
    return rec


def one_configuration_safe(job):
    try:
        return one_configuration(job)
    except Exception as e:                                  # recorded, never dropped: it counts as no pass for anyone
        idx, N, word, line, P = job
        return {"index": idx, "N": N, "word": word, "line": list(line), "error": repr(e), "cells": {}, "closure": {},
                "plan": {}, "Npts": None, "bits": None, "seconds": None}


# ------------------------------------------------------------------ scoring (W66's predicate as W88 used it)
def data():
    hz = json.load(open(os.path.join(HERE, "received_HZ2021_running_masses_MZ.json")))
    ckm = json.load(open(os.path.join(HERE, "received_B1612_data.json")))["ckm_abs"]
    return hz["masses_GeV"]["value"], hz["masses_GeV"]["sigma"], ckm["value"], ckm["sigma"]


def score(records):
    MV, MS, VV, VS = data()
    ratio = lambda a, b: (MV[a] / MV[b], math.hypot(MS[a] / MV[a], MS[b] / MV[b]))
    target = {}
    for sec, (f1, f2, f3) in SEC_DATA.items():
        (x1, r1), (x2, r2) = ratio(f1, f3), ratio(f2, f3)
        l1, l2 = math.log(x1), math.log(x2)
        target[sec] = {"R1": (x1, r1), "R2": (x2, r2), "rho": (l1 / l2, math.hypot(r1 / l1, r2 / l2))}
    ckm_t = {"Vus": (VV[0][1], VS[0][1] / VV[0][1]), "Vcb": (VV[1][2], VS[1][2] / VV[1][2]),
             "Vub": (VV[0][2], VS[0][2] / VV[0][2])}
    z = lambda x, rx, y, ry: (math.log(x) - math.log(y)) / math.sqrt(rx * rx + ry * ry + A_ALLOW * A_ALLOW)
    names = list(assignments())
    counts = {}                                     # (statistic, reading, N or 'all', name) -> passes
    detail_sm = []
    accept_fail = {}
    w94 = []
    errors = [r["index"] for r in records if r.get("error")]
    for rec in records:
        if rec.get("error"):
            continue
        N = rec["N"]
        clos = rec["closure"]
        cells_seen = sorted(set(k.split("|")[3] for k in rec["cells"]))
        for reading in ("per-field", "minimal"):
            tag = "pf" if reading == "per-field" else "mn"
            for cell in cells_seen:
                for name in names:
                    rows = {sec: rec["cells"].get(f"{name}|{reading}|{sec}|{cell}") for sec in SEC_DATA}
                    if any(rw is None for rw in rows.values()) and all(f"{name}|{reading}|{s}|{cell}" not in rec["cells"] for s in SEC_DATA):
                        continue
                    plan = {sec: rec["plan"][f"{name}|{sec}"] for sec in SEC_DATA}
                    ok, why = True, None
                    for sec in SEC_DATA:
                        rw = rows[sec]
                        key = tuple(plan[sec][0]) if reading == "per-field" else tuple(plan[sec][1])
                        cval = clos.get(f"{tag}|{key}")
                        if rw is None:
                            ok, why = False, why or "no masses (a norm matrix not positive, or an exact zero mass)"
                        elif min(rw["s"]) <= 1e-30 * max(rw["s"]):
                            ok, why = False, why or "rank deficient (a zero singular value)"
                        elif not (rw["s"][0] < rw["s"][1] < rw["s"][2]):
                            ok, why = False, why or "degenerate singular values"
                        elif cval is None or cval > CLOSURE_MAX:
                            ok, why = False, why or "closure"
                        elif rw["r_calc"] > RCALC_MAX:
                            ok, why = False, why or "convergence"
                    if not ok:
                        kk_ = (name, reading, why)
                        accept_fail[kk_] = accept_fail.get(kk_, 0) + 1
                    passes = {"S-mass": False, "S-shape": False, "S-ckm": False}
                    zz = {}
                    if ok:
                        chi_m, chi_s = 0.0, 0.0
                        for sec in SEC_DATA:
                            s1, s2, s3 = rows[sec]["s"]
                            rc = rows[sec]["r_calc"]
                            R1, R2 = s1 / s3, s2 / s3
                            z1 = z(R1, rc, *target[sec]["R1"]); z2 = z(R2, rc, *target[sec]["R2"])
                            rho = math.log(R1) / math.log(R2)
                            zr = math.log(rho / target[sec]["rho"][0]) / math.sqrt(rc * rc + target[sec]["rho"][1] ** 2 + A_ALLOW ** 2)
                            chi_m += z1 * z1 + z2 * z2; chi_s += zr * zr
                            zz[sec] = {"R1": R1, "R2": R2, "rho": rho, "z1": z1, "z2": z2, "z_rho": zr}
                        Uu = [[complex(*x) for x in row] for row in rows["up"]["U"]]
                        Ud = [[complex(*x) for x in row] for row in rows["down"]["U"]]
                        V = [[sum(Uu[k][i].conjugate() * Ud[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
                        rc = max(rows["up"]["r_calc"], rows["down"]["r_calc"])
                        cv = {"Vus": abs(V[0][1]), "Vcb": abs(V[1][2]), "Vub": abs(V[0][2])}
                        chi_c = sum(z(max(cv[k_], 1e-300), rc, *ckm_t[k_]) ** 2 for k_ in cv)
                        passes = {"S-mass": chi_m <= CHI95[6], "S-shape": chi_s <= CHI95[3], "S-ckm": chi_c <= CHI95[3]}
                        zz.update({"chi_mass": chi_m, "chi_shape": chi_s, "chi_ckm": chi_c, "ckm": cv})
                        w94.append({"name": name, "reading": reading, "N": N, "word": rec["word"], "line": rec["line"],
                                    "cell": cell, "w94": zz["lepton"]["R2"] / zz["down"]["R2"]}) if name == "SM" else None
                    for st, val in passes.items():
                        for scope in ("all", N):
                            kk = (st, reading, scope, name)
                            counts[kk] = counts.get(kk, 0) + int(val)
                    if name == "SM":
                        detail_sm.append({"N": N, "word": rec["word"], "line": rec["line"], "cell": cell,
                                          "reading": reading, "accepted": ok, **({"z": zz} if ok else {}),
                                          "passes": passes})
    def p_value(st, reading, scope):
        sm = counts.get((st, reading, scope, "SM"), 0)
        nulls = [counts.get((st, reading, scope, n), 0) for n in names if n != "SM"]
        return sm, (1 + sum(1 for x in nulls if x >= sm)) / (len(nulls) + 1), sum(nulls) / len(nulls)
    claims = {}
    sm, p, mean_null = p_value("S-mass", "per-field", "all")
    claims["PRIMARY: S-mass, per-field, pooled over N = 9, 11, 12"] = {
        "SM passes": sm, "null mean passes": mean_null, "p": p, "earned": bool(sm >= 1 and p <= 0.05)}
    readouts = [("S-mass", "minimal", "all"), ("S-shape", "per-field", "all"), ("S-shape", "minimal", "all"),
                ("S-ckm", "per-field", "all"), ("S-ckm", "minimal", "all"),
                ("S-mass", "per-field", 9), ("S-mass", "per-field", 11), ("S-mass", "per-field", 12)]
    for st, reading, scope in readouts:
        sm, p, mean_null = p_value(st, reading, scope)
        claims[f"read-out: {st}, {reading}, N = {scope}"] = {
            "SM passes": sm, "null mean passes": mean_null, "p": p,
            "earned at Bonferroni 0.05/8": bool(sm >= 1 and p <= 0.05 / 8)}
    # N = 12, split by W92's odd-structure feature (a field with charge = 6 mod 12; the SM's e^c has it): report only
    feat = {n: any(v % 12 == 6 for v in a_.values()) for n, a_ in assignments().items()}
    split12 = {}
    for flag in (True, False):
        grp = [n for n in names if n != "SM" and feat[n] == flag]
        split12[f"nulls with a charge = 6 mod 12: {flag}"] = {
            "number": len(grp),
            "mean S-mass per-field passes at N = 12": (sum(counts.get(("S-mass", "per-field", 12, n), 0) for n in grp) / len(grp)) if grp else None}
    split12["SM (has the feature)"] = counts.get(("S-mass", "per-field", 12, "SM"), 0)
    return {"targets": {s: {k: list(v) for k, v in t.items()} for s, t in target.items()},
            "configurations with an error (no pass for anyone)": errors,
            "N = 12 split by the odd-structure feature (report only)": split12,
            "ckm targets": {k: list(v) for k, v in ckm_t.items()},
            "claims": claims, "SM per configuration-cell": detail_sm,
            "acceptance failures (configuration-cells, counted as not passing)": {f"{a}|{b}|{c}": v for (a, b, c), v in accept_fail.items()},
            "W94 read-out (SM)": w94}


def tower_law():
    """the T-tower read-out: the per-field cusp law's leading exponents (cusp_law.py's rule) on the least-volume closing
    lines at odd N (+ L R^{N^2}: lines (0, b); - L R^{N^2 - 4}: lines (-2b, b)); C1 and E4 cells; no score"""
    from fractions import Fraction as Fr
    PU = {"F_i": (Fr(-7, 8), Fr(7, 8), Fr(3, 8)), "F+": (Fr(1, 8), Fr(-1, 8), Fr(3, 8)), "F-": (Fr(1, 8), Fr(7, 8), Fr(-5, 8))}
    dist = lambda x: min(x % 1, 1 - x % 1)
    def g(u, al):
        pe, pp, pm = PU[u]; s2 = dist(al + Fr(1, 2)) ** 2 - Fr(1, 4); s34 = dist(al) ** 2
        return max(0, -(pe + s2), -(pp + s34), -(pm + s34))
    out = {}
    for N in (9, 11):
        for b in range(1, N // 2 + 1):
            row = {}
            for sec, (fl, fr) in {"up": ("Q", "u"), "down": ("Q", "d"), "lepton": ("L", "e")}.items():
                L = {u: g(u, Fr(SM[fl] * b, N)) for u in PU}; R = {u: g(u, Fr(SM[fr] * b, N)) for u in PU}
                m2 = (L["F-"] - L["F+"]) + (R["F-"] - R["F+"]); m1 = (L["F_i"] - L["F+"]) + (R["F_i"] - R["F+"])
                row[sec] = {"m2/m3 exponent": float(m2), "m1/m3 exponent": float(m1), "rho": float(m1 / m2)}
            out[f"N={N} lb={b}"] = row
    return out


def controls(P):
    """run before any N = 9, 11, 12 configuration; the run stops if one fails"""
    import flint, mpmath as mp
    import tlow2 as T2
    res = {}
    for word, line, N in (("LLRRRLRLRLRR", (6, 3), 10), ("LLLRLLLRLR", (1, 7), 8)):
        rot, M, rho, k, height = T2.thread_geometry(word)
        flint.ctx.prec = 800; F = T2.Forms(P).prepare(); flint.ctx.prec = T2.bits_for(height)
        a, b, c, d = M; Pl = 2 * math.acosh((a + d) / 2)
        c1 = T2.configuration(F, word, line, N, {"SM": SM}, int(round(Pl * NPTS_PER_PERIOD)))
        c2 = T2.configuration(F, word, line, N, {"SM": SM}, int(round(Pl * NPTS_CHECK)))
        m1 = T2.masses(c1, F, {"SM": SM}, N, mp); m2 = T2.masses(c2, F, {"SM": SM}, N, mp)
        def rank3(c):
            s_ = [float(x) for x in c["s"]]
            return min(s_) > 1e-30 * max(s_)
        rc = max(abs(math.log(float(m1[k_][cell]["s"][i]) / float(m2[k_][cell]["s"][i]))) for k_ in m1 for cell in m1[k_]
                 if m1[k_][cell] and rank3(m1[k_][cell]) for i in range(3))
        # rotation invariance: another rotation of the same word, the line carried into it, gives the same masses
        kalt = (k + 1) % len(word)
        c3 = T2.configuration(F, word, line, N, {"SM": SM}, int(round(Pl * NPTS_PER_PERIOD)), kforce=kalt)
        m3 = T2.masses(c3, F, {"SM": SM}, N, mp)
        rot_dev = max(abs(float(mp.log(m1[k_][cell]["s"][i] / m3[k_][cell]["s"][i]))) for k_ in m1 for cell in m1[k_]
                      if m1[k_][cell] and m3[k_][cell] and rank3(m1[k_][cell]) for i in range(3))
        # the negative control: on a rotation that moves the line, the line NOT carried into it must fail closure
        neg = None
        for kk in (k, kalt):
            mv = T2.line_in_rotation(word, kk, line, N)
            if mv not in (tuple(line), ((-line[0]) % N, (-line[1]) % N)):
                c4 = T2.configuration(F, word, line, N, {"SM": SM}, 60, kforce=kk, carry_line=False)
                neg = max(c4["closure"].values())
                break
        holds = (max(c1["closure"].values()) < CLOSURE_MAX and rc < RCALC_MAX and rot_dev < 1e-20
                 and (neg is None or neg > 1e-3))
        res[f"{word} N={N} line {line}"] = {"closure": max(c1["closure"].values()), "r_calc": rc,
                                            "rotation invariance (ln s)": rot_dev,
                                            "uncarried line's closure (must fail)": neg, "holds": bool(holds)}
    return res


if __name__ == "__main__":
    t0 = time.time()
    P = pickle.load(open(FORMS, "rb"))
    out = {"status": "THE TWISTED UNITS ON THE LOW THREADS; sealed (PREREGISTRATION_TWISTED_UNITS.md); one run",
           "inputs sha256": {f: sha(os.path.join(HERE, f)) for f in ("tlow2.py", "null_draws.json",
                             "tlow_configurations.json", "received_HZ2021_running_masses_MZ.json",
                             "received_B1612_data.json", "twisted_units_seal.py")},
           "forms.pkl sha256": sha(FORMS)}
    out["controls"] = controls(P)
    print("controls", {k: v["holds"] for k, v in out["controls"].items()}, round(time.time() - t0, 1), flush=True)
    if not all(v["holds"] for v in out["controls"].values()):
        out["stopped"] = "a control failed; no N = 9, 11 or 12 configuration was computed"
        json.dump(out, open(os.path.join(HERE, "twisted_units_seal_output.json"), "w"), indent=1)
        sys.exit(1)
    cfg = json.load(open(os.path.join(HERE, "tlow_configurations.json")))
    jobs = []
    for N in ("9", "11", "12"):
        for w, h, key, eps in cfg[N]:
            jobs.append((len(jobs), int(N), w, tuple(key), P))
    records = []
    with Pool(2) as pool:
        for rec in pool.imap_unordered(one_configuration_safe, jobs):
            records.append(rec)
            print(f"configuration {rec['index']:3d} done ({len(records)}/{len(jobs)}): N={rec['N']} {rec['word']} "
                  f"bits {rec['bits']} Npts {rec['Npts']} max closure {max(rec['closure'].values(), default=float('nan')):.0e} "
                  f"{'ERROR ' if rec.get('error') else ''}{rec['seconds']} s; elapsed {time.time() - t0:.0f} s", flush=True)
    records.sort(key=lambda r: r["index"])
    out["records"] = records
    json.dump(out, open(os.path.join(HERE, "twisted_units_seal_output.json"), "w"), indent=1, default=str)
    out["score"] = score(records)
    out["T-tower read-out (the per-field cusp law, leading order; no score)"] = tower_law()
    out["seconds"] = round(time.time() - t0, 1)
    json.dump(out, open(os.path.join(HERE, "twisted_units_seal_output.json"), "w"), indent=1, default=str)
    print("written twisted_units_seal_output.json; seconds", out["seconds"], flush=True)
