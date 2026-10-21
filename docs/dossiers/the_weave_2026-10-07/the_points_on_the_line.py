#!/usr/bin/env python3
"""W117 -- a point on the line: do the weave's canonical functionals, extremized on each thread's closed geodesic, mark
a point where the zero-dof quark assignments fit with two degrees of freedom, and is the tick's line special?  The
rule is W117_RULE.md, committed and pushed before this script.  One run; its output (the_points_on_the_line.json,
the_points_on_the_line_run.txt) is committed before it is read.

The order: the rule was committed (19a6e1994) before this script was begun; its push waited on the pre-push suite and
came before this script's commit.

Pre-run disclosure: while this script was written, its parts were run in scratch only on code paths that touch no
cell: the functionals and the marks on three lines of length 9, outside the census (LLRLRRLRR, LLLRLRLRR, and the
self-mirror LLLLLLLLR, whose one mark is CP-fixed: there the snapping and J = 0 were checked); the fit at one mark
against a synthetic target drawn there; and the worker pool on LLRLRRLRR's line with the data replaced by that
synthetic target, with small budgets.  No line of the census was evaluated, no functional was evaluated on any
census line, no fit to the quark data was run, and no cell was computed.

It reuses W113's, W114's and W116's code (the_strong_angle.py, the_tuned_fit.py and the_seed_geodesics.py,
imported): W114's sectors replayed exactly (seed 114, in its order), W115's solutions replayed exactly and closed
under the CP mirror, and W116's census, lines and distances.

Conventions fixed here, within the rule:
- the functionals are evaluated at the image of each point in F; e1, e2, N_T and P_T are minimized along the line and
  D is maximized (W51's direction); a local extremum is kept only if it is strict (the functional at +-10^-3 in s on
  either side is worse), and a functional whose spread along the line is below 10^-10 of its mean marks nothing there;
- a mark within 10^-6 of its CP mirror is CP-fixed; by symmetry the critical point lies exactly on a reflection line,
  so the mark is placed at the point of the nearest reflection line (Re tau = 0, Re tau = +-1/2 or |tau| = 1) closest to
  the refined point (the shift is recorded; it is of the order of the refinement's precision);
- the marks of a class are ordered by s; within a self-mirror line, a mark whose CP mirror is an earlier mark is not
  fitted again (its fits are equal by CP), and the mirror line of a class takes the class's values;
- the tick's larger read-out uses seed 127 000 + 10 (mark index) + j; assignment 16 at the tick's marks uses j = 3 in
  the census seed; R1's control draws its line, mark, coupling and search from seed 1171; R2's couplings come from
  seed 1172.
"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import json  # noqa: E402
import math  # noqa: E402
import multiprocessing  # noqa: E402
import sys  # noqa: E402
import time  # noqa: E402
from pathlib import Path  # noqa: E402

import numpy as np  # noqa: E402
from scipy.optimize import minimize_scalar  # noqa: E402
from scipy.special import gamma  # noqa: E402

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_seed_geodesics as SG  # noqa: E402

SA, TF = SG.SA, SG.TF
T0 = time.time()
FAM = (11, 13, 14)
JIDX = {11: 0, 13: 1, 14: 2, 16: 3}
PASS2 = 5.99
FUNCS = ("e1", "e2", "N_T", "P_T", "D")
SIGN = {"e1": 1.0, "e2": 1.0, "N_T": 1.0, "P_T": 1.0, "D": -1.0}
NS = 8000
CENSUS = dict(n_rand=3000, n_best=8)
TICK = dict(n_rand=12000, n_best=32)
MAXFEV = 4000
NWORK = 4
TICK_TOP = complex(0.5, math.sqrt(5) / 2)

MARKS = {}  # class index -> list of fitted marks (dicts)
SOLS = {}


def log(*a):
    print(f"[{time.time() - T0:9.1f}s]", *a, flush=True)


# ------------------------------------------------------------------------------------------- the functionals
def fvals(T):
    """W51's functionals at points T of F"""
    T = np.asarray(T, dtype=complex).reshape(-1)
    U, E = SA.u_eta_np(T)
    ae2 = np.abs(E) ** 2
    au = np.abs(U)
    x = au / ae2[:, None]
    y = T.imag
    return {"e1": x.sum(1), "e2": x[:, 0] * x[:, 1] + x[:, 0] * x[:, 2] + x[:, 1] * x[:, 2], "e3": x.prod(1),
            "D": y * ae2 ** 2, "N_T": y ** -0.5 * (au ** 2).sum(1) / ae2 ** 3,
            "P_T": y ** -1.5 * np.prod(au ** 2, 1) / ae2 ** 9, "F": (x ** 2).sum(1)}


def f_at(line, s, name):
    return SIGN[name] * float(fvals([SA.to_fd(complex(line.tau(s)))])[name][0])


def cp_mirror(t):
    return complex(-t.real, t.imag)


def snap(t):
    """the point of the nearest reflection line (Re tau = 0, Re tau = +-1/2, |tau| = 1) closest to t"""
    cands = [complex(0.0, t.imag), complex(math.copysign(0.5, t.real), t.imag), t / abs(t)]
    return min(cands, key=lambda c: abs(c - t))


def same(a, b, tol=1e-6):
    return float(SG.surface_dist([a], b)[0]) < tol


def marks_of(line):
    S = np.linspace(-line.ell / 2, line.ell / 2, NS, endpoint=False)
    dS = line.ell / NS
    V = fvals(line.tf(S))
    raw, flat, dropped = [], [], 0
    for name in FUNCS:
        g = SIGN[name] * V[name]
        if np.ptp(g) <= 1e-10 * np.mean(np.abs(g)):
            flat.append(name)
            continue
        for k in range(NS):
            if g[k] < g[k - 1] and g[k] <= g[(k + 1) % NS]:
                r = minimize_scalar(lambda s, name=name: f_at(line, s, name), bounds=(S[k] - dS, S[k] + dS),
                                    method="bounded", options={"xatol": 1e-12})
                s0, g0 = float(r.x), float(r.fun)
                if not (g0 < f_at(line, s0 - 1e-3, name) and g0 < f_at(line, s0 + 1e-3, name)):
                    dropped += 1
                    continue
                raw.append((name, float(line.wrap(s0)), g0, SA.to_fd(complex(line.tau(s0)))))
    gmin = {}
    for name, _, g0, _ in raw:
        gmin[name] = min(gmin.get(name, np.inf), g0)
    marks = []
    for name, s0, g0, t in sorted(raw, key=lambda r: r[1]):
        glob = bool(g0 <= gmin[name] + 1e-9 * abs(gmin[name]))
        for m in marks:
            if same(t, m["tau"]):
                m["by"].append({"functional": name, "s": s0, "global": glob})
                break
        else:
            marks.append({"tau": t, "s": s0, "by": [{"functional": name, "s": s0, "global": glob}]})
    for i, m in enumerate(marks):
        m["cp_fixed"] = same(m["tau"], cp_mirror(m["tau"]))
        m["mirror of"] = None
        m["snapped by"] = 0.0
        if m["cp_fixed"]:
            sn = snap(m["tau"])
            m["snapped by"], m["tau"] = abs(sn - m["tau"]), sn
        if not m["cp_fixed"]:
            for j in range(i):
                if marks[j]["mirror of"] is None and same(cp_mirror(m["tau"]), marks[j]["tau"]):
                    m["mirror of"] = j
                    break
    return marks, flat, dropped


# ------------------------------------------------------------------------------------------- the fit at a mark
def fit_at(model, t, logd, rng, n_rand, n_best, warm, maxfev=MAXFEV, n_pol=2, a=0.10):
    nu, nd = model.up.nfree, model.dn.nfree
    VU = rng.normal(size=(n_rand, nu)) if nu else np.zeros((n_rand, 0))
    VD = rng.normal(size=(n_rand, nd)) if nd else np.zeros((n_rand, 0))
    P1 = np.concatenate([np.full((n_rand, 1), t.real), np.full((n_rand, 1), t.imag), VU, VD], 1)
    v1 = TF.stage1(model, P1, logd, a)
    order = np.argsort(v1)
    starts = [np.concatenate([VU[i], VD[i]]) for i in order[:n_best]] + [np.array(vec) for vec, _, _ in warm]

    def g(v):
        return model.chi2(np.concatenate([[t.real, t.imag], v]), logd, a)

    ends = sorted((TF.nm(g, v0, maxfev) for v0 in starts), key=lambda e: e[1])
    pol = sorted((TF.nm(g, v, maxfev) for v, _ in ends[:n_pol]), key=lambda e: e[1])
    best = min([ends[0]] + pol, key=lambda e: e[1])
    return best, float(v1[order[0]])


def info_at(model, t, v, logd):
    r = model.evaluate(np.concatenate([[t.real, t.imag], v]), ycap=1e9)
    if r is None:
        return {}
    _, _, _, (obs, J, _, _, _) = r
    o = obs[0]
    with np.errstate(divide="ignore", invalid="ignore"):
        z = (np.log(np.where(o > 0, o, 1.0)) - logd) / np.hypot(SA.REL, 0.10)
    return {"J": float(np.ravel(J)[0]), "observables": dict(zip(SA.LABELS, map(float, o))),
            "pulls": dict(zip(SA.LABELS, map(float, z)))}


def task_mark(args):
    kind, ci, mi, num = args
    t0 = time.time()
    t = MARKS[ci][mi]["tau"]
    model = SG.MODELS[num]
    if kind == "census":
        rng, bud = np.random.default_rng(117000 + 1000 * ci + 10 * mi + JIDX[num]), CENSUS
    else:
        rng, bud = np.random.default_rng(127000 + 10 * mi + JIDX[num]), TICK
    (v, c), s1 = fit_at(model, t, SA.LOGD, rng, bud["n_rand"], bud["n_best"], SOLS[num])
    rec = {"chi2_min": float(c), "stage-1 best": s1, "seconds": time.time() - t0}
    rec.update(info_at(model, t, v, SA.LOGD))
    return (kind, ci, mi, num), rec


def task_control(_):
    t0 = time.time()
    rc = np.random.default_rng(1171)
    others = [ci for ci, (rep, _) in enumerate(SG.CLASSES) if rep != "LR" and MARKS[ci]]
    ci = others[int(rc.integers(len(others)))]
    mi = int(rc.integers(len(MARKS[ci])))
    t = MARKS[ci][mi]["tau"]
    model = SG.MODELS[14]
    ostar = None
    for _ in range(5000):
        p, r = SG.draw_valid(model, rc, t)
        o = r[3][0][0]
        if np.all((o > 1e-6) & (o < 0.9)):
            ostar = o
            break
    (v, c), s1 = fit_at(model, t, np.log(ostar), rc, CENSUS["n_rand"], CENSUS["n_best"], SOLS[14])
    return "control", {"class": ci, "line": SG.CLASSES[ci][0], "mark": mi, "tau": [t.real, t.imag],
                       "synthetic observables": ostar.tolist(), "chi2_min": float(c), "stage-1 best": s1,
                       "holds": bool(c <= 0.01), "seconds": time.time() - t0}


def dispatch(t):
    if t[0] == "control":
        return task_control(None)
    if t[0] == "replay":
        return SG.task_replay(t[1])
    return task_mark(t)


# ------------------------------------------------------------------------------------------- the run
def main():
    out = {"rule": "W117_RULE.md", "script": "the_points_on_the_line.py", "status": "one run",
           "pass mark (2 dof)": PASS2, "budgets": {"census": CENSUS, "tick": TICK, "maxfev": MAXFEV, "grid": NS}}
    SG.build()
    W, lines, classes = SG.census(8)
    for k in lines:
        SG.LINES[k] = SG.Line(k)
    SG.CLASSES.extend(classes)
    tick_ci = next(i for i, (rep, _) in enumerate(SG.CLASSES) if rep == "LR")
    tick = SG.LINES["LR"]
    log("census", len(W), "words,", len(lines), "lines,", len(SG.CLASSES), "classes")

    # ---------------- R0's closed forms and the marks
    eta_i = gamma(0.25) / (2 * math.pi ** 0.75)
    eta_w = 3 ** 0.125 * gamma(1 / 3) ** 1.5 / (2 * math.pi)
    Di, Dw = eta_i ** 4, (math.sqrt(3) / 2) * eta_w ** 4
    closed = {"e1": (2 + 2 * math.sqrt(2), 3 * 2 ** (2 / 3)), "e2": (2 + 4 * math.sqrt(2), 3 * 2 ** (4 / 3)),
              "D": (Di, Dw), "N_T": (8 / math.sqrt(Di), 3 * 2 ** (4 / 3) / math.sqrt(Dw)),
              "P_T": (16 / Di ** 1.5, 16 / Dw ** 1.5)}
    vi = fvals([1j])
    vw = fvals([complex(-0.5, math.sqrt(3) / 2)])
    worst_closed = max(max(abs(float(vi[n][0]) / closed[n][0] - 1), abs(float(vw[n][0]) / closed[n][1] - 1))
                       for n in closed)
    T64 = tick.tf(np.linspace(-tick.ell / 2, tick.ell / 2, 64, endpoint=False))
    worst_F = float(np.max(np.abs(fvals(T64)["F"] - 8)))

    per_class = {}
    worst_e3, worst_crit = 0.0, 0.0
    for ci, (rep, ls) in enumerate(SG.CLASSES):
        L = SG.LINES[rep]
        marks, flat, dropped = marks_of(L)
        for m in marks:
            worst_e3 = max(worst_e3, abs(float(fvals([m["tau"]])["e3"][0]) - 4))
            for b in m["by"]:
                h = 1e-5
                fp, fm = f_at(L, b["s"] + h, b["functional"]), f_at(L, b["s"] - h, b["functional"])
                f0 = f_at(L, b["s"], b["functional"])
                worst_crit = max(worst_crit, abs(fp - fm) / (2 * h) / abs(f0))
        MARKS[ci] = marks
        per_class[ci] = {"rep": rep, "lines": ls, "flat functionals": flat, "dropped as not strict": dropped,
                         "marks": [{"tau": [m["tau"].real, m["tau"].imag], "s": m["s"], "by": m["by"],
                                    "cp_fixed": m["cp_fixed"], "snapped by": m["snapped by"],
                                    "mirror of": m["mirror of"]} for m in marks]}
        log("marks", ci, rep, len(marks), "marks,", sum(m["cp_fixed"] for m in marks), "CP-fixed,",
            sum(m["mirror of"] is not None for m in marks), "mirror copies; flat", flat, "dropped", dropped)
    out["classes"] = per_class
    tick_marks = MARKS[tick_ci]
    r3 = bool(tick_marks) and all(same(m["tau"], 1j) or same(m["tau"], TICK_TOP) for m in tick_marks)
    out["R0"] = {"census as in W116": bool(len(W) == 69 and len(lines) == 40 and len(SG.CLASSES) == 34),
                 "W51's closed forms: worst relative deviation": worst_closed,
                 "e3 = 4 at every mark: worst": worst_e3, "F = 8 on the tick's line: worst": worst_F,
                 "every mark critical: worst relative derivative": worst_crit,
                 "number of marks (fitted classes)": sum(len(v) for v in MARKS.values())}
    out["R0"]["holds"] = bool(out["R0"]["census as in W116"] and worst_closed <= 1e-8 and worst_e3 <= 1e-10
                              and worst_F <= 1e-10 and worst_crit <= 1e-6)
    log("R0", out["R0"])
    out["R3"] = {"the tick's marks": per_class[tick_ci]["marks"], "holds": r3}
    log("R3", r3, [(round(m["tau"].real, 4), round(m["tau"].imag, 4)) for m in tick_marks])

    # ---------------- R2, J at the CP-fixed marks
    r2rng = np.random.default_rng(1172)
    worstJ, nJ = 0.0, 0
    for ci in range(len(SG.CLASSES)):
        for m in MARKS[ci]:
            if not m["cp_fixed"]:
                continue
            for num in FAM:
                for _ in range(20):
                    Jv = SG.draw_valid(SG.MODELS[num], r2rng, m["tau"])[1][3][1]
                    worstJ = max(worstJ, abs(float(np.ravel(Jv)[0])))
                    nJ += 1
    out["R2"] = {"worst |J| at the CP-fixed marks": worstJ, "evaluations": nJ, "holds": bool(worstJ <= 1e-14)}
    log("R2", out["R2"])

    ctx = multiprocessing.get_context("fork")
    # ---------------- the replay of W115's solutions
    with ctx.Pool(NWORK) as pool:
        rep = dict(pool.map(dispatch, [("replay", (n, 20000, 50, 5, 60000, 120, 8000)) for n in FAM]))
    w115 = json.loads((HERE / "the_shared_tau.json").read_text(encoding="utf-8"))["V2"]
    replay = {}
    for num in FAM:
        found = rep[num]["found"]
        SOLS[num] = SG.mirror_closed([(np.array(p[2:]), complex(*t), v) for p, v, t in found])
        rec_ts = [complex(*x["tau"]) for x in w115[str(num)]["solutions"]]
        ok = len(rec_ts) == len(found) and all(abs(complex(*f[2]) - r) < 1e-6 for f, r in zip(found, rec_ts))
        replay[str(num)] = {"reproduced": bool(ok), "solutions": len(found), "with mirrors": len(SOLS[num])}
    SOLS[16] = []
    log("replay", replay)

    # ---------------- the fits
    tasks = [("tick", tick_ci, mi, n) for mi in range(len(tick_marks)) for n in FAM]
    tasks += [("census", tick_ci, mi, 16) for mi in range(len(tick_marks))]
    tasks += [("control",)]
    tasks += [("census", ci, mi, n) for ci in range(len(SG.CLASSES)) for mi, m in enumerate(MARKS[ci])
              if m["mirror of"] is None for n in FAM]
    log("tasks", len(tasks))
    res = {}
    with ctx.Pool(NWORK) as pool:
        for key, rec in pool.imap_unordered(dispatch, tasks):
            res[key] = rec
            if key != "control":
                log("fit", key, f"chi2_min {rec['chi2_min']:.4g}")
    ctl = res.pop("control")
    out["R1"] = {"replay": replay, "control": ctl,
                 "holds": bool(all(r["reproduced"] for r in replay.values()) and ctl["holds"])}
    log("R1", out["R1"]["holds"], "control", ctl["chi2_min"])

    # ---------------- assemble: every mark's fits (mirror copies take their partner's), every line's statistic
    fits = {}
    for (kind, ci, mi, num), rec in res.items():
        fits.setdefault(kind, {}).setdefault(str(ci), {}).setdefault(str(mi), {})[str(num)] = rec
    out["fits"] = fits

    def mark_chi2(ci, mi, num):
        m = MARKS[ci][mi]
        j = mi if m["mirror of"] is None else m["mirror of"]
        return fits["census"][str(ci)][str(j)][str(num)]["chi2_min"]

    per_line, passing = {}, []
    for ci, (repw, ls) in enumerate(SG.CLASSES):
        vals = [(mark_chi2(ci, mi, n), mi, n) for mi in range(len(MARKS[ci])) for n in FAM]
        best = min(vals) if vals else (float("inf"), None, None)
        for mi in range(len(MARKS[ci])):
            for n in FAM:
                c = mark_chi2(ci, mi, n)
                if c <= PASS2:
                    m = MARKS[ci][mi]
                    j = mi if m["mirror of"] is None else m["mirror of"]
                    passing.append({"class": ci, "line": repw, "mark": mi, "assignment": n, "chi2_min": c,
                                    "tau": [m["tau"].real, m["tau"].imag], "by": m["by"], "cp_fixed": m["cp_fixed"],
                                    "J": fits["census"][str(ci)][str(j)][str(n)].get("J"),
                                    "distance to the nearest W115 solution": float(min(
                                        SG.surface_dist([m["tau"]], u)[0] for _, u, _ in SOLS[n]))})
        for k in ls:
            per_line[k] = {"class": ci, "fitted on": repw, "marks": len(MARKS[ci]), "chi2_line": best[0],
                           "at mark": best[1], "assignment": best[2]}
    out["lines"] = per_line
    out["passing marks"] = passing
    tick_line = per_line["LR"]["chi2_line"]
    tk = {}
    for mi in range(len(tick_marks)):
        for n in FAM:
            tk[f"{mi}/{n}"] = {"census budget": mark_chi2(tick_ci, mi, n),
                               "tick budget": fits["tick"][str(tick_ci)][str(mi)][str(n)]["chi2_min"]}
    out["R4"] = {"the tick's marks": tk, "holds": bool(all(min(v.values()) > PASS2 for v in tk.values()))}
    npass = sum(1 for r in per_line.values() if r["chi2_line"] <= PASS2)
    out["R5"] = {"lines that pass": sorted(k for k, r in per_line.items() if r["chi2_line"] <= PASS2),
                 "number": npass, "of": len(per_line), "passing marks (fitted classes)": len(passing),
                 "marks fitted": sum(1 for v in MARKS.values() for m in v if m["mirror of"] is None),
                 "holds": bool(npass >= 1)}
    p = sum(1 for r in per_line.values() if r["chi2_line"] <= tick_line) / len(per_line)
    out["R6"] = {"the tick's chi2_line": tick_line, "p": p, "holds": bool(p >= 0.05)}
    out["R7"] = {f"{mi}": fits["census"][str(tick_ci)][str(mi)]["16"]["chi2_min"] for mi in range(len(tick_marks))}
    out["cells"] = {c: out[c]["holds"] for c in ("R0", "R1", "R2", "R3", "R4", "R5", "R6")}
    out["seconds"] = time.time() - T0
    (HERE / "the_points_on_the_line.json").write_text(json.dumps(out, indent=1, default=str) + "\n",
                                                      encoding="utf-8")
    log("R4", out["R4"]["holds"], "R5", npass, "R6 p", p, "R7", out["R7"])
    log("cells", out["cells"])
    log("written the_points_on_the_line.json")


if __name__ == "__main__":
    main()
