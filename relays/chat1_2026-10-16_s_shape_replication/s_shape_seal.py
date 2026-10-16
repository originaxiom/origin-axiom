"""THE S-SHAPE REPLICATION ON FRESH THREADS (chat1; sealed with PREREGISTRATION_S_SHAPE_REPLICATION.md; run once).

The low-thread seal (0d83e6981) left one nominal read-out: S-shape, per-field, pooled, p = 0.03, not earned at 0.05/8.
This run asks whether the SM's excess persists on configurations that seal never saw, with its duplicates removed:
  - the configurations: Lyndon words of length 13 and 14 at height <= 3 with a closing line of exact order N = 9, 11,
    12 (fresh_configurations.json), one representative per class of word reversal with the L <-> R mirror;
  - the null: the 224 eligible draws of null_draws.json, one per pair under q -> -q (the first in the fixed order),
    112 assignments, distinct jointly over the three orders (per order they fall into 15, 39 and 49 orbits under
    q -> k.q mod N, which leaves an order's counts unchanged: reported, not claimed).
One claim, the pooled count, at 0.025: the SM and the nulls are the first run's, so this is not an independent test of
whether the SM is special, and it must clear a stricter bar than the first run's nominal 0.03.
The reading is per-field only, the statistic S-shape only (W66's predicate as W88 used it, a = 0.10, on the ratio of
log-ratios rho = ln(m1/m3) / ln(m2/m3) per sector, Sigma z^2 <= 7.815 over the three sectors), the instrument
tlow2.py unchanged (its sha256 is recorded).

Usage: python3 -B s_shape_seal.py <forms.pkl>   (writes s_shape_seal_output.json beside itself; progress lines carry
no mass and no score)
"""
import hashlib, json, math, os, pickle, sys, time
from multiprocessing import Pool

HERE = os.path.dirname(os.path.abspath(__file__))
TU = os.path.normpath(os.path.join(HERE, "..", "chat1_2026-10-15_route", "twisted_units"))
sys.path.insert(0, TU)

A_ALLOW = 0.10
CHI95_3 = 7.815
ALPHA = 0.025                      # the one claim; stricter than 0.05, since the SM and the nulls are those of the first run
NPTS_PER_PERIOD, NPTS_CHECK = 30.0, 37.5
CLOSURE_MAX, RCALC_MAX = 1e-20, 1e-6
SYMMETRY_TOL = 1e-30              # |difference| / the cell's largest singular value (an exact zero sits below it)
SEC_DATA = {"up": ("u", "c", "t"), "down": ("d", "s", "b"), "lepton": ("e", "mu", "tau")}
SM = {"Q": 1, "u": -4, "d": 2, "L": -3, "e": 6, "H": 3}
FIELDS = ("Q", "u", "d", "L", "e", "H")
FORMS = sys.argv[1] if len(sys.argv) > 1 else None


def sha(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


def distinct_nulls():
    """one per pair under q -> -q: the first in null_draws.json's fixed order"""
    draws = json.load(open(os.path.join(TU, "null_draws.json")))["draws_in_order"]
    seen, out = set(), []
    for d in draws:
        key = tuple(sorted(d.items()))
        neg = tuple(sorted((k, -v) for k, v in d.items()))
        if key in seen or neg in seen:
            continue
        seen.add(key)
        out.append({k: int(v) for k, v in d.items()})
    return out


def unit_orbit(q, N):
    """the orbit of q's residues under multiplication by a unit mod N (the per-field reading's symmetry)"""
    r = [q[f] % N for f in FIELDS]
    return min(tuple((k * x) % N for x in r) for k in range(1, N) if math.gcd(k, N) == 1)


def assignments():
    out = {"SM": SM}
    out.update({f"null{i:03d}": d for i, d in enumerate(distinct_nulls())})
    return out


def sign_controls():
    """the negatives of the first three distinct nulls (for the sign-flip control only; never scored)"""
    return {f"neg{i:03d}": {k: -v for k, v in d.items()} for i, d in enumerate(distinct_nulls()[:3])}


def jobs_list():
    cfg = json.load(open(os.path.join(HERE, "fresh_configurations.json")))
    jobs = []
    for N in ("9", "11", "12"):
        for ci, cls in enumerate(cfg[N]):
            w, h, line = cls["representative"]
            jobs.append({"kind": "class", "N": int(N), "class": ci, "word": w, "line": tuple(line)})
    # symmetry controls, one class per order: the first class with four members; each of its other three members
    # (the mirror, the reversal and both), and the representative again with the sign-flipped nulls added
    for N in ("9", "11", "12"):
        for ci, cls in enumerate(cfg[N]):
            if len(cls["members"]) == 4:
                for mi, (w2, l2) in enumerate(cls["members"][1:], start=1):
                    jobs.append({"kind": "class-control", "N": int(N), "class": ci, "member": mi, "word": w2,
                                 "line": tuple(l2)})
                w, h, line = cls["representative"]
                jobs.append({"kind": "sign-control", "N": int(N), "class": ci, "member": 0, "word": w,
                             "line": tuple(line)})
                break
    for i, j in enumerate(jobs):
        j["index"] = i
    return jobs


def one_configuration(job, P):
    import flint, mpmath as mp
    import tlow2 as T2
    t0 = time.time()
    N, word, line = job["N"], job["word"], job["line"]
    rot, M, rho, k, height = T2.thread_geometry(word)
    flint.ctx.prec = 800
    F = T2.Forms(P).prepare()
    flint.ctx.prec = T2.bits_for(height)
    a, b, c, d = M
    Pl = 2 * math.acosh((a + d) / 2)
    n1, n2 = int(round(Pl * NPTS_PER_PERIOD)), int(round(Pl * NPTS_CHECK))
    A = assignments()
    if job["kind"] == "sign-control":
        A = {k_: v for k_, v in A.items() if k_ in ("null000", "null001", "null002")}
        A.update(sign_controls())
    conf1 = T2.configuration(F, word, tuple(line), N, A, n1, readings=("per-field",))
    conf2 = T2.configuration(F, word, tuple(line), N, A, n2, readings=("per-field",))
    m1 = T2.masses(conf1, F, A, N, mp)
    m2 = T2.masses(conf2, F, A, N, mp)
    rec = {**{k_: (list(v) if isinstance(v, tuple) else v) for k_, v in job.items()}, "rotation": conf1["rot"],
           "line_in_rotation": list(conf1["line_in_rotation"]), "height": height, "bits": conf1["bits"],
           "Npts": [n1, n2], "closure": {f"{t}|{k_}": v for (t, k_), v in conf1["closure"].items()},
           "plan": {f"{a_}|{s_}": [list(v[0]), list(v[1])] for (a_, s_), v in conf1["plan"].items()}, "cells": {}}
    for (name, reading, sec), cells in m1.items():
        for cell, dd in cells.items():
            d2 = m2.get((name, reading, sec), {}).get(cell)
            entry = None
            if dd is not None:
                s = [float(x) for x in dd["s"]]
                s_str = [mp.nstr(x, 40) for x in dd["s"]]
                rc = None
                if d2 is not None and min(s) > 0 and min(float(x) for x in d2["s"]) > 0:
                    rc = max(abs(math.log(s[i] / float(d2["s"][i]))) for i in range(3))
                entry = {"s": s, "s40": s_str, "r_calc": rc}
            rec["cells"][f"{name}|{sec}|{cell}"] = entry
    rec["seconds"] = round(time.time() - t0, 1)
    return rec


def one_configuration_safe(args):
    job, P = args
    try:
        return one_configuration(job, P)
    except Exception as e:                       # recorded, never dropped: it counts as no pass for anyone
        return {**{k_: (list(v) if isinstance(v, tuple) else v) for k_, v in job.items()}, "error": repr(e),
                "cells": {}, "closure": {}, "plan": {}, "Npts": None, "bits": None, "seconds": None}


# ------------------------------------------------------------------ the symmetry controls
def symmetry_controls(records):
    import mpmath
    mpmath.mp.dps = 50
    by = {(r["kind"], r["N"], r["class"], r.get("member", 0)): r for r in records}
    out, ok = {}, True
    for (kind, N, ci, mi), r in by.items():
        if kind == "class":
            continue
        rep = by.get(("class", N, ci, 0))
        worst, compared = 0.0, 0
        if r.get("error") or rep is None or rep.get("error"):
            ok = False
            out[f"{kind} N={N} class {ci} member {mi}"] = {"holds": False, "why": "an error"}
            continue
        for key, c in r["cells"].items():
            name, rest = key.split("|", 1)
            if kind == "class-control":
                c0 = rep["cells"].get(key)
            else:
                if not name.startswith("neg"):
                    continue
                c0 = r["cells"].get("null" + name[3:] + "|" + rest)
            if (c is None) != (c0 is None):
                worst = float("inf"); continue
            if c is None:
                continue
            smax = max(mpmath.mpf(c["s40"][2]), mpmath.mpf(c0["s40"][2]))
            for x, y in zip(c["s40"], c0["s40"]):           # scale-aware: |dX| relative to the cell's largest value
                worst = max(worst, float(abs(mpmath.mpf(x) - mpmath.mpf(y)) / smax))
                compared += 1
        holds = worst <= SYMMETRY_TOL and compared > 0
        ok &= holds
        out[f"{kind} N={N} class {ci} member {mi}"] = {"compared singular values": compared,
                                                        "worst difference relative to the cell's largest": worst,
                                                        "holds": bool(holds)}
    return ok, out


# ------------------------------------------------------------------ scoring (S-shape, per-field)
def data():
    hz = json.load(open(os.path.join(TU, "received_HZ2021_running_masses_MZ.json")))
    return hz["masses_GeV"]["value"], hz["masses_GeV"]["sigma"]


def score(records):
    MV, MS = data()
    target = {}
    for sec, (f1, f2, f3) in SEC_DATA.items():
        x1, x2 = MV[f1] / MV[f3], MV[f2] / MV[f3]
        r1 = math.hypot(MS[f1] / MV[f1], MS[f3] / MV[f3]); r2 = math.hypot(MS[f2] / MV[f2], MS[f3] / MV[f3])
        l1, l2 = math.log(x1), math.log(x2)
        target[sec] = (l1 / l2, math.hypot(r1 / l1, r2 / l2))
    names = list(assignments())
    counts, detail_sm, accept_fail, errors = {}, [], {}, []
    for rec in records:
        if rec["kind"] != "class":
            continue
        if rec.get("error"):
            errors.append(rec["index"]); continue
        N = rec["N"]
        cells_seen = sorted({k.split("|")[2] for k in rec["cells"]})
        for cell in cells_seen:
            for name in names:
                ok, why, chi, zz = True, None, 0.0, {}
                for sec in SEC_DATA:
                    rw = rec["cells"].get(f"{name}|{sec}|{cell}")
                    key = tuple(rec["plan"][f"{name}|{sec}"][0])
                    cval = rec["closure"].get(f"pf|{key}")
                    if rw is None:
                        ok, why = False, why or "no masses"
                    elif min(rw["s"]) <= 1e-30 * max(rw["s"]):
                        ok, why = False, why or "rank deficient"
                    elif not (rw["s"][0] < rw["s"][1] < rw["s"][2]):
                        ok, why = False, why or "degenerate singular values"
                    elif cval is None or cval > CLOSURE_MAX:
                        ok, why = False, why or "closure"
                    elif rw["r_calc"] is None or rw["r_calc"] > RCALC_MAX:
                        ok, why = False, why or "convergence"
                    if ok:
                        s1, s2, s3 = rw["s"]
                        rho = math.log(s1 / s3) / math.log(s2 / s3)
                        z = math.log(rho / target[sec][0]) / math.sqrt(rw["r_calc"] ** 2 + target[sec][1] ** 2 + A_ALLOW ** 2)
                        chi += z * z
                        zz[sec] = {"rho": rho, "z_rho": z}
                passed = bool(ok and chi <= CHI95_3)
                if not ok:
                    accept_fail[f"{name}|{why}"] = accept_fail.get(f"{name}|{why}", 0) + 1
                for scope in ("all", N):
                    counts[(scope, name)] = counts.get((scope, name), 0) + int(passed)
                if name == "SM":
                    detail_sm.append({"N": N, "class": rec["class"], "word": rec["word"], "line": rec["line"],
                                      "cell": cell, "accepted": ok, "chi_shape": chi if ok else None, "z": zz,
                                      "pass": passed})
    def p_value(scope):
        sm = counts.get((scope, "SM"), 0)
        nulls = [counts.get((scope, n), 0) for n in names if n != "SM"]
        return sm, (1 + sum(1 for x in nulls if x >= sm)) / (len(nulls) + 1), sum(nulls) / len(nulls), sorted(nulls)
    claims = {}
    sm, p, mean_null, dist = p_value("all")
    claims["PRIMARY: S-shape, per-field, pooled over N = 9, 11, 12"] = {
        "SM passes": sm, "null mean passes": mean_null, "p": p, "earned at 0.025": bool(sm >= 1 and p <= ALPHA),
        "null distribution": dist}
    # report only: each order on its own, at the level of assignments and of unit orbits (q -> k.q mod N leaves an
    # order's counts unchanged in the per-field reading); the orbit-level count is checked to be constant on each orbit
    Q = assignments()
    report = {}
    for N in (9, 11, 12):
        sm_n, p_n, mean_n, dist_n = p_value(N)
        orbits = {}
        for n in names:
            if n != "SM":
                orbits.setdefault(unit_orbit(Q[n], N), []).append(counts.get((N, n), 0))
        spread = max(max(v) - min(v) for v in orbits.values())
        oc = [v[0] for v in orbits.values()]
        report[f"S-shape, per-field, N = {N}"] = {
            "SM passes": sm_n, "null mean passes": mean_n, "p over assignments": p_n,
            "unit orbits among the nulls": len(orbits),
            "largest count spread within an orbit (must be 0)": spread,
            "p over orbits": (1 + sum(1 for x in oc if x >= sm_n)) / (len(oc) + 1)}
    # report only: calibration of the pooled claim; each null in turn as "the SM", against the nulls that share none of
    # its unit orbits (as no null shares the SM's)
    hits = 0
    for n in names:
        if n == "SM":
            continue
        own = {N: unit_orbit(Q[n], N) for N in (9, 11, 12)}
        others = [m for m in names if m not in ("SM", n) and all(unit_orbit(Q[m], N) != own[N] for N in (9, 11, 12))]
        c0 = counts.get(("all", n), 0)
        pp = (1 + sum(1 for m in others if counts.get(("all", m), 0) >= c0)) / (len(others) + 1)
        hits += int(c0 >= 1 and pp <= ALPHA)
    report["calibration: nulls that would earn the pooled claim against the rest"] = {
        "earned": hits, "of": len(names) - 1, "fraction": hits / (len(names) - 1)}
    return {"targets (rho, r_rho)": target, "class-cells per assignment": sum(
                len({k.split("|")[2] for k in r["cells"]}) for r in records if r["kind"] == "class" and not r.get("error")),
            "configurations with an error (no pass for anyone)": errors, "claims": claims, "report only": report,
            "acceptance failures (class-cells, counted as not passing)": accept_fail, "SM per class-cell": detail_sm}


# ------------------------------------------------------------------ the excluded-order controls (as in 0d83e6981)
def controls(P):
    import flint, mpmath as mp
    import tlow2 as T2
    res = {}
    for word, line, N in (("LLRRRLRLRLRR", (6, 3), 10), ("LLLRLLLRLR", (1, 7), 8)):
        rot, M, rho, k, height = T2.thread_geometry(word)
        flint.ctx.prec = 800; F = T2.Forms(P).prepare(); flint.ctx.prec = T2.bits_for(height)
        a, b, c, d = M; Pl = 2 * math.acosh((a + d) / 2)
        A = {"SM": SM}
        c1 = T2.configuration(F, word, line, N, A, int(round(Pl * NPTS_PER_PERIOD)), readings=("per-field",))
        c2 = T2.configuration(F, word, line, N, A, int(round(Pl * NPTS_CHECK)), readings=("per-field",))
        m1 = T2.masses(c1, F, A, N, mp); m2 = T2.masses(c2, F, A, N, mp)
        def rank3(cc):
            s_ = [float(x) for x in cc["s"]]
            return min(s_) > 1e-30 * max(s_)
        rc = max(abs(math.log(float(m1[k_][cell]["s"][i]) / float(m2[k_][cell]["s"][i]))) for k_ in m1 for cell in m1[k_]
                 if m1[k_][cell] and rank3(m1[k_][cell]) for i in range(3))
        kalt = (k + 1) % len(word)
        c3 = T2.configuration(F, word, line, N, A, int(round(Pl * NPTS_PER_PERIOD)), readings=("per-field",), kforce=kalt)
        m3 = T2.masses(c3, F, A, N, mp)
        rot_dev = max(abs(float(mp.log(m1[k_][cell]["s"][i] / m3[k_][cell]["s"][i]))) for k_ in m1 for cell in m1[k_]
                      if m1[k_][cell] and m3[k_][cell] and rank3(m1[k_][cell]) for i in range(3))
        neg = None
        for kk in (k, kalt):
            mv = T2.line_in_rotation(word, kk, line, N)
            if mv not in (tuple(line), ((-line[0]) % N, (-line[1]) % N)):
                c4 = T2.configuration(F, word, line, N, A, 60, readings=("per-field",), kforce=kk, carry_line=False)
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
    OUT = os.path.join(HERE, "s_shape_seal_output.json")
    out = {"status": "THE S-SHAPE REPLICATION ON FRESH THREADS; sealed (PREREGISTRATION_S_SHAPE_REPLICATION.md); one run",
           "inputs sha256": {os.path.relpath(f, HERE): sha(f) for f in (
               os.path.join(TU, "tlow2.py"), os.path.join(TU, "null_draws.json"),
               os.path.join(TU, "received_HZ2021_running_masses_MZ.json"),
               os.path.join(HERE, "fresh_configurations.json"), os.path.join(HERE, "classes.py"),
               os.path.join(HERE, "PREREGISTRATION_S_SHAPE_REPLICATION.md"), os.path.join(HERE, "s_shape_seal.py"))},
           "forms.pkl sha256": sha(FORMS), "distinct nulls": len(distinct_nulls())}
    out["controls"] = controls(P)
    print("controls", {k: v["holds"] for k, v in out["controls"].items()}, round(time.time() - t0, 1), flush=True)
    if not all(v["holds"] for v in out["controls"].values()):
        out["stopped"] = "an excluded-order control failed; no N = 9, 11 or 12 configuration was computed"
        json.dump(out, open(OUT, "w"), indent=1)
        sys.exit(1)
    jobs = jobs_list()
    records = []
    with Pool(2) as pool:
        for rec in pool.imap_unordered(one_configuration_safe, [(j, P) for j in jobs]):
            records.append(rec)
            print(f"job {rec['index']:3d} done ({len(records)}/{len(jobs)}): {rec['kind']} N={rec['N']} class {rec['class']} "
                  f"{rec['word']} bits {rec['bits']} {'ERROR ' if rec.get('error') else ''}{rec['seconds']} s; "
                  f"elapsed {time.time() - t0:.0f} s", flush=True)
    records.sort(key=lambda r: r["index"])
    out["records"] = records
    json.dump(out, open(OUT, "w"), indent=1, default=str)
    ok, sym = symmetry_controls(records)
    out["symmetry controls"] = sym
    if not ok:
        out["stopped"] = "a symmetry control failed; nothing is scored"
        json.dump(out, open(OUT, "w"), indent=1, default=str)
        print("written s_shape_seal_output.json (stopped at the symmetry controls)", flush=True)
        sys.exit(2)
    out["score"] = score(records)
    out["seconds"] = round(time.time() - t0, 1)
    json.dump(out, open(OUT, "w"), indent=1, default=str)
    print("written s_shape_seal_output.json; seconds", out["seconds"], flush=True)
