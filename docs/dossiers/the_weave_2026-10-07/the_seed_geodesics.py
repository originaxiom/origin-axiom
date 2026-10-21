#!/usr/bin/env python3
"""W116 -- the seed's marks: does putting tau on a thread's closed geodesic leave a quark fit with a degree of freedom
to spare, and is the tick's geodesic special among the threads'?  The rule is W116_RULE.md, committed and pushed
before this script.  One run; its output (the_seed_geodesics.json, the_seed_geodesics_run.txt) is committed before it
is read.

The order: the rule was committed (e34f9f9d1) before this script was begun; its push waited on the pre-push suite and
came before this script's commit.

Pre-run disclosure: while this script was written, its parts were run in scratch only on code paths that touch no
cell: the line geometry and the search on the line of LLRLRRLRR (length 9, outside the census) against a synthetic
target drawn there, with small budgets; the worker pool on that line, with the data replaced by that synthetic
target; and the replay routine with small budgets (its numbers were not compared with W115's).  No line of the
census was evaluated, no fit to the quark data was run on any line, and no cell was computed.

It reuses W113's and W114's code (the_strong_angle.py and the_tuned_fit.py, imported).  W114's sectors are replayed
exactly (seed 114, in W114's order), and W115's quark solutions by replaying W114's searches (seeds 1150 + n) and
W115's (seeds 115 + n), as W115 ran them.  The searches run in four worker processes, each with its own fixed seed,
so the result does not depend on the order in which they finish.

Conventions fixed here, within the rule:
- the classes are ordered by the length of their representative word, then lexicographically with L < R; the class
  index in the seeds is the position in that order (the tick, LR, is class 0);
- s is wrapped into [-l/2, l/2), so the evaluated points stay near the top of the axis;
- the warm starts: CP in the law maps a solution (tau, coefficients) to (-conj(tau), the same coefficients), which
  is again a solution; the solutions are closed under that mirror before use, so that mirror lines get the same
  starts; for each solution and line, the start is the nearest of 4000 points of one period;
- distances on the modular surface are taken over the images of the solution under the words of length <= 3 in S,
  T and T^-1;
- the tick's larger read-out: 30 000 random points, Nelder-Mead from the best 60 and from every warm start, then
  again from the best 3 endpoints;
- S0's mirror check uses the first class (in the order) with two lines, at a coupling of assignment 14 drawn from
  seed 1160; S1's control draws its line, point, coupling and search from seed 1161; S2's couplings come from seed
  1163.
"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import itertools  # noqa: E402
import json  # noqa: E402
import math  # noqa: E402
import multiprocessing  # noqa: E402
import sys  # noqa: E402
import time  # noqa: E402
from pathlib import Path  # noqa: E402

import numpy as np  # noqa: E402
from scipy.stats import chi2 as CHI2  # noqa: E402

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_strong_angle as SA  # noqa: E402
import the_tuned_fit as TF  # noqa: E402

T0 = time.time()
FAM = (11, 13, 14)
ALL = (11, 13, 14, 16)
JIDX = {11: 0, 13: 1, 14: 2, 16: 3}
THRESH = {11: 1e-6, 13: 1e-6, 14: 3.84}
PASS = {k: round(float(CHI2.ppf(0.95, k)), 2) for k in range(1, 6)}
NWORK = 4
PHI = (1 + math.sqrt(5)) / 2
MAT = {"L": ((1, 0), (1, 1)), "R": ((1, 1), (0, 1))}
CENSUS = dict(n_rand=6000, n_best=15)
TICK = dict(n_rand=30000, n_best=60)
MAXFEV = 6000
NGRID = 4000


def log(*a):
    print(f"[{time.time() - T0:9.1f}s]", *a, flush=True)


# ------------------------------------------------------------------------------------------- the census of words
def rotations(w):
    return {w[i:] + w[:i] for i in range(len(w))}


def canon(w):
    return min(rotations(w))


def mirror(w):
    return w.translate(str.maketrans("LR", "RL"))


def primitive(w):
    n = len(w)
    return all(w != w[:d] * (n // d) for d in range(1, n) if n % d == 0)


def words(nmax):
    out = set()
    for n in range(2, nmax + 1):
        for t in itertools.product("LR", repeat=n):
            w = "".join(t)
            if "L" in w and "R" in w and primitive(w):
                out.add(canon(w))
    return sorted(out, key=lambda w: (len(w), w))


def line_key(w):
    """w and its reversed mirror trace the same line (M(w)^T = M(reversed mirror), and M^T ~ M^-1)"""
    return min(canon(w), canon(mirror(w)[::-1]))


def matmul(A, B):
    return ((A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]),
            (A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]))


def mat(w):
    M = ((1, 0), (0, 1))
    for ch in w:
        M = matmul(M, MAT[ch])
    return M


def transpose(M):
    return ((M[0][0], M[1][0]), (M[0][1], M[1][1]))


def census(nmax=8):
    W = words(nmax)
    lines = {}
    for w in W:
        lines.setdefault(line_key(w), []).append(w)
    classes = {}
    for k in lines:
        classes.setdefault(min(k, line_key(mirror(k))), set()).add(k)
    order = sorted(classes, key=lambda w: (len(w), w))
    return W, lines, [(rep, sorted(classes[rep], key=lambda w: (w != rep, w))) for rep in order]


# ------------------------------------------------------------------------------------------- a line and its points
class Line:
    def __init__(self, word):
        self.word = word
        (a, b), (c, d) = mat(word)
        self.M = ((a, b), (c, d))
        self.trace = a + d
        self.c0 = (a - d) / (2 * c)
        self.rho = math.sqrt(self.trace ** 2 - 4) / (2 * abs(c))
        self.ell = 2 * math.acosh(abs(self.trace) / 2)

    def wrap(self, s):
        return (np.asarray(s, dtype=float) + self.ell / 2) % self.ell - self.ell / 2

    def tau_raw(self, s):
        th = 2 * np.arctan(np.exp(-np.asarray(s, dtype=float)))
        return self.c0 + self.rho * np.exp(1j * th)

    def tau(self, s):
        return self.tau_raw(self.wrap(s))

    def arc(self, z):
        th = math.atan2(z.imag, z.real - self.c0)
        return -math.log(math.tan(th / 2))

    def moebius(self, z):
        (a, b), (c, d) = self.M
        return (a * z + b) / (c * z + d)

    def tf(self, s):
        return np.array([SA.to_fd(complex(t)) for t in np.atleast_1d(self.tau(s))])


def images(w, depth=3):
    """the images of w under the words of length <= depth in S, T, T^-1"""
    seen, front = {complex(w)}, [complex(w)]
    for _ in range(depth):
        new = []
        for z in front:
            for g in (z + 1, z - 1, -1 / z):
                if all(abs(g - x) > 1e-12 for x in seen):
                    seen.add(g)
                    new.append(g)
        front = new
    return np.array(sorted(seen, key=lambda z: (z.real, z.imag)))


def surface_dist(Z, w):
    """hyperbolic distance from the points Z (in F) to the point w on the modular surface"""
    Z = np.asarray(Z, dtype=complex).reshape(-1, 1)
    I = images(w)[None, :]
    ch = 1 + np.abs(Z - I) ** 2 / (2 * Z.imag * I.imag)
    return np.arccosh(np.maximum(ch.min(1), 1.0))


def line_grid(line):
    S = np.linspace(-line.ell / 2, line.ell / 2, NGRID, endpoint=False)
    return S, line.tf(S)


def nearest(grid, w):
    S, T = grid
    d = surface_dist(T, w)
    i = int(np.argmin(d))
    return float(S[i]), float(d[i])


def mirror_closed(sols):
    """(vector, tau in F, chi2) -> the same list closed under tau -> -conj(tau) with the same coefficients"""
    out = list(sols)
    for vec, t, v in sols:
        m = complex(-t.real, t.imag)
        if all(float(surface_dist([m], u)[0]) > 1e-6 for _, u, _ in out):
            out.append((vec, m, v))
    return out


# ------------------------------------------------------------------------------------------- the search on a line
def chi2_on_line(model, line, q, logd, a=0.10):
    t = SA.to_fd(complex(line.tau(q[0])))
    return model.chi2(np.concatenate([[t.real, t.imag], q[1:]]), logd, a)


def line_search(model, line, logd, rng, n_rand, n_best, warm, maxfev=MAXFEV, n_pol=3, a=0.10):
    nu, nd = model.up.nfree, model.dn.nfree
    S = rng.uniform(-line.ell / 2, line.ell / 2, n_rand)
    VU = rng.normal(size=(n_rand, nu)) if nu else np.zeros((n_rand, 0))
    VD = rng.normal(size=(n_rand, nd)) if nd else np.zeros((n_rand, 0))
    T = line.tf(S)
    P1 = np.concatenate([T.real[:, None], T.imag[:, None], VU, VD], 1)
    v1 = TF.stage1(model, P1, logd, a)
    order = np.argsort(v1)
    starts = [np.concatenate([[S[i]], VU[i], VD[i]]) for i in order[:n_best]]
    grid = line_grid(line) if warm else None
    for vec, t, _ in warm:
        s0, _ = nearest(grid, t)
        starts.append(np.concatenate([[s0], vec]))

    def g(q):
        return chi2_on_line(model, line, q, logd, a)

    ends = sorted((TF.nm(g, q0, maxfev) for q0 in starts), key=lambda e: e[1])
    pol = sorted((TF.nm(g, q, maxfev) for q, _ in ends[:n_pol]), key=lambda e: e[1])
    best = min([ends[0]] + pol, key=lambda e: e[1])
    return best, float(v1[order[0]]), [float(v) for _, v in ends[:5]]


def point_info(model, line, q, logd):
    t = SA.to_fd(complex(line.tau(q[0])))
    r = model.evaluate(np.concatenate([[t.real, t.imag], q[1:]]), ycap=1e9)
    if r is None:
        return {"tau_in_F": [t.real, t.imag], "s": float(line.wrap(q[0]))}
    tf, cu, cd, (obs, J, su, sd, V) = r
    o = obs[0]
    with np.errstate(divide="ignore", invalid="ignore"):
        z = (np.log(np.where(o > 0, o, 1.0)) - logd) / np.hypot(SA.REL, 0.10)
    return {"tau_in_F": [tf.real, tf.imag], "s": float(line.wrap(q[0])), "J": float(np.ravel(J)[0]),
            "observables": dict(zip(SA.LABELS, map(float, o))), "pulls": dict(zip(SA.LABELS, map(float, z)))}


# ------------------------------------------------------------------------------------------- worker state and tasks
SECS, MODELS, LINES, CLASSES, SOLS = {}, {}, {}, [], {}


def build():
    rng114 = np.random.default_rng(114)
    for _, _, up, dn in TF.ASSIGN:
        for typ, k in (up, dn):
            if (typ, k) not in SECS:
                SECS[(typ, k)] = TF.SectorParam(typ, k, rng114)
    for num, hand, up, dn in TF.ASSIGN:
        if num in ALL:
            MODELS[num] = TF.Model(SECS[up], SECS[dn])


def task_replay(args):
    num, n1, n2, n3, nr, nb, maxfev = args
    t0 = time.time()
    model = MODELS[num]

    def f(p, model=model):
        return model.chi2(p, SA.LOGD, 0.10)

    (p114, v114), _, _, _ = TF.search(model, SA.LOGD, np.random.default_rng(1150 + num), n1=n1, n2=n2, n3=n3,
                                      maxfev=maxfev)
    tf114 = SA.to_fd(complex(p114[0], p114[1]))
    rec = {"W114's point": [tf114.real, tf114.imag], "W114's chi2": float(v114)}
    if num == 16:
        rec["found"] = [(p114.tolist(), float(v114), [tf114.real, tf114.imag])]
        rec["seconds"] = time.time() - t0
        return num, rec
    rng = np.random.default_rng(115 + num)
    P1 = TF.random_starts(model, rng, nr)
    v1 = TF.stage1(model, P1, SA.LOGD, 0.10)
    order = np.argsort(v1)
    ends = [TF.nm(f, P1[i], maxfev) for i in order[:nb]]
    ends.append(TF.nm(f, p114, maxfev))
    found = []
    for p, v in sorted(ends, key=lambda e: e[1]):
        if v > THRESH[num]:
            continue
        tfp = SA.to_fd(complex(p[0], p[1]))
        if all(abs(tfp - complex(*q[2])) > 1e-3 for q in found):
            found.append((p.tolist(), float(v), [tfp.real, tfp.imag]))
    rec["found"] = found
    rec["seconds"] = time.time() - t0
    return num, rec


def task_fit(args):
    kind, ci, num = args
    t0 = time.time()
    rep = CLASSES[ci][0]
    line, model = LINES[rep], MODELS[num]
    if kind == "census":
        rng, bud = np.random.default_rng(116000 + 10 * ci + JIDX[num]), CENSUS
    else:
        rng, bud = np.random.default_rng(117000 + JIDX[num]), TICK
    (q, v), s1, top = line_search(model, line, SA.LOGD, rng, bud["n_rand"], bud["n_best"], SOLS[num])
    rec = {"chi2_min": float(v), "stage-1 best": s1, "best five endpoints": top}
    rec.update(point_info(model, line, q, SA.LOGD))
    rec["seconds"] = time.time() - t0
    return (kind, ci, num), rec


def draw_valid(model, rng, t):
    """a coupling drawn as W114 draws it, redrawn until it evaluates at t (a tuned root can fail)"""
    for _ in range(1000):
        p = np.concatenate([[t.real, t.imag], rng.normal(size=model.up.nfree), rng.normal(size=model.dn.nfree)])
        r = model.evaluate(p, ycap=1e9)
        if r is not None:
            return p, r
    raise RuntimeError("no valid coupling")


def task_control(_):
    """S1's second half: synthetic data from assignment 14 on a random line other than the tick's, fitted back"""
    t0 = time.time()
    rc = np.random.default_rng(1161)
    others = [i for i, (rep, _) in enumerate(CLASSES) if rep != "LR"]
    ci = others[int(rc.integers(len(others)))]
    rep = CLASSES[ci][0]
    line, model = LINES[rep], MODELS[14]
    ostar, qstar = None, None
    for _ in range(5000):
        s = float(rc.uniform(-line.ell / 2, line.ell / 2))
        q = np.concatenate([[s], rc.normal(size=model.up.nfree), rc.normal(size=model.dn.nfree)])
        t = SA.to_fd(complex(line.tau(s)))
        r = model.evaluate(np.concatenate([[t.real, t.imag], q[1:]]))
        if r is None:
            continue
        o = r[3][0][0]
        if np.all((o > 1e-6) & (o < 0.9)):
            ostar, qstar = o, q
            break
    (q, v), s1, top = line_search(model, line, np.log(ostar), rc, CENSUS["n_rand"], CENSUS["n_best"], SOLS[14])
    return "control", {"class": ci, "line": rep, "synthetic point": qstar.tolist(),
                       "synthetic observables": ostar.tolist(), "chi2_min": float(v), "stage-1 best": s1,
                       "holds": bool(v <= 0.01), "seconds": time.time() - t0}


# ------------------------------------------------------------------------------------------- the run
def main():
    out = {"rule": "W116_RULE.md", "script": "the_seed_geodesics.py", "status": "one run",
           "pass marks": PASS, "budgets": {"census": CENSUS, "tick": TICK, "maxfev": MAXFEV}}
    build()
    log("sectors", {s.label: s.dim for s in SECS.values()})

    # ---------------- the census
    W, lines, classes = census(8)
    for k in lines:
        LINES[k] = Line(k)
    CLASSES.extend(classes)
    tick_ci = next(i for i, (rep, _) in enumerate(CLASSES) if rep == "LR")
    per_len = {n: sum(1 for w in W if len(w) == n) for n in range(2, 9)}
    out["census"] = {
        "words": len(W), "words by length": per_len, "lines": len(lines), "classes": len(CLASSES),
        "self-mirror lines": sum(1 for _, ls in CLASSES if len(ls) == 1),
        "the tick's class index": tick_ci,
        "lines (key: words)": {k: v for k, v in lines.items()},
        "classes (index: lines)": {i: ls for i, (_, ls) in enumerate(CLASSES)},
        "line data": {k: {"trace": L.trace, "length": L.ell, "centre": L.c0, "radius": L.rho}
                      for k, L in LINES.items()}}
    log("census", len(W), "words,", len(lines), "lines,", len(CLASSES), "classes; tick class", tick_ci)

    # ---------------- S0, the structure
    s0 = {"counts as stated": bool(len(W) == 69 and len(lines) == 40 and len(CLASSES) == 34
                                   and per_len == {2: 1, 3: 2, 4: 3, 5: 6, 6: 9, 7: 18, 8: 30})}
    worst_circ, worst_shift = 0.0, 0.0
    for k, L in LINES.items():
        for w in lines[k]:
            Lw = Line(w)
            for s in np.linspace(-1.0, 1.0, 5):
                z = complex(Lw.tau_raw(s))
                mz = Lw.moebius(z)
                worst_circ = max(worst_circ, abs(abs(mz - Lw.c0) / Lw.rho - 1))
                worst_shift = max(worst_shift, abs(abs(Lw.arc(mz) - s) - Lw.ell))
    s0["axis invariance: worst |M tau - c|/rho - 1"] = worst_circ
    s0["axis invariance: worst | |s' - s| - l |"] = worst_shift
    s0["M(w)^T equals the reversed mirror's matrix, every word"] = bool(
        all(transpose(mat(w)) == mat(mirror(w)[::-1]) for w in W))
    basis, d = SA.space(1, 1, 1)
    _, rb = SA.real_basis(basis, d)
    sec1 = SA.Sector(rb, SA.M_ETA[(1, 1)], "T(x)T k=1")
    tick = LINES["LR"]
    T64 = tick.tf(np.linspace(-tick.ell / 2, tick.ell / 2, 64, endpoint=False))
    U, E = SA.u_eta_np(T64)
    _, sv = SA.svd_sorted(sec1.Y(U, E, np.array([1.0])))
    gold = np.array([PHI ** -2, PHI ** -1, 1.0])
    s0["golden: worst deviation on the tick's line (64 points)"] = float(np.max(np.abs(sv / sv[:, 2:3] - gold)))
    L3 = LINES["LLR"]
    U3, E3 = SA.u_eta_np(L3.tf(np.linspace(-L3.ell / 2, L3.ell / 2, 64, endpoint=False)))
    _, sv3 = SA.svd_sorted(sec1.Y(U3, E3, np.array([1.0])))
    s0["read-out: the middle mass's spread on LLR's line"] = float(np.ptp(sv3[:, 1] / sv3[:, 2]))
    ci_m = next(i for i, (_, ls) in enumerate(CLASSES) if len(ls) == 2)
    A, B = CLASSES[ci_m][1]
    LA, Lm = LINES[A], Line(mirror(A))
    rm = np.random.default_rng(1160)
    m14 = MODELS[14]
    t0a = SA.to_fd(complex(LA.tau(0.0)))
    vv = draw_valid(m14, rm, t0a)[0][2:]
    worst_on, worst_obs = 0.0, 0.0
    for s in np.linspace(-LA.ell / 2, LA.ell / 2, 50, endpoint=False):
        z = complex(LA.tau(s))
        zm = 1 / z.conjugate()
        worst_on = max(worst_on, abs(abs(zm - Lm.c0) / Lm.rho - 1))
        oa = m14.evaluate(np.concatenate([[SA.to_fd(z).real, SA.to_fd(z).imag], vv]), ycap=1e9)
        ob = m14.evaluate(np.concatenate([[SA.to_fd(zm).real, SA.to_fd(zm).imag], vv]), ycap=1e9)
        if oa is None or ob is None:
            worst_obs = float("inf")
            continue
        worst_obs = max(worst_obs, float(np.max(np.abs(ob[3][0][0] / oa[3][0][0] - 1))))
    s0["mirror pair"] = {"class": ci_m, "lines": [A, B], "the mirror word's line": line_key(mirror(A)),
                         "worst: mirror point off the mirror axis": worst_on,
                         "worst relative difference of the observables": worst_obs}
    s0["holds"] = bool(s0["counts as stated"] and worst_circ <= 1e-10 and worst_shift <= 1e-10
                       and s0["M(w)^T equals the reversed mirror's matrix, every word"]
                       and s0["golden: worst deviation on the tick's line (64 points)"] <= 1e-10
                       and line_key(mirror(A)) == B and worst_on <= 1e-10 and worst_obs <= 1e-9)
    out["S0"] = s0
    log("S0", s0["holds"])

    # ---------------- S2, the line's own points
    r2 = np.random.default_rng(1163)
    s2 = {}
    for num in FAM:
        m = MODELS[num]
        for name, z in (("i", 1j), ("1/2 + i sqrt5/2", complex(0.5, math.sqrt(5) / 2))):
            t = SA.to_fd(z)
            Js = [abs(float(np.ravel(draw_valid(m, r2, t)[1][3][1])[0])) for _ in range(20)]
            s2[f"{num} at {name}"] = max(Js)
        t = SA.to_fd(complex(tick.tau(0.3)))
        Jg = draw_valid(m, r2, t)[1][3][1]
        s2[f"{num}: read-out, |J| at s = 0.3 on the tick's line"] = abs(float(np.ravel(Jg)[0]))
    out["S2"] = {"max |J| over 20 couplings": s2,
                 "holds": bool(all(v <= 1e-14 for k, v in s2.items() if "read-out" not in k))}
    log("S2", out["S2"]["holds"])

    # ---------------- S3, the implication
    w114 = json.loads((HERE / "the_tuned_fit.json").read_text(encoding="utf-8"))["assignments"]
    w113 = json.loads((HERE / "the_strong_angle.json").read_text(encoding="utf-8"))
    s3 = {}
    for n, rec in w114.items():
        if int(n) in ALL:
            continue
        dof = rec["dof"] + 1
        s3[f"W114 {n}"] = {"chi2_min": rec["chi2_min (a = 0.10)"], "dof on a line": dof,
                           "pass mark": PASS[dof], "above": bool(rec["chi2_min (a = 0.10)"] > PASS[dof])}
    c6 = w113["C"]["(-1, -1, -1)"]["C6"]["chi2_min (a = 0.10)"]
    s3["W113 forced"] = {"chi2_min": c6, "dof on a line": 3, "pass mark": PASS[3], "above": bool(c6 > PASS[3])}
    out["S3"] = {"rows": s3, "holds": bool(all(r["above"] for r in s3.values()))}
    log("S3", out["S3"]["holds"])

    ctx = multiprocessing.get_context("fork")

    # ---------------- the replay of W115's solutions (and W114's point for 16)
    with ctx.Pool(NWORK) as pool:
        rep = dict(pool.map(task_replay, [(n, 20000, 50, 5, 60000, 120, 8000) for n in (11, 13, 14, 16)]))
    w115 = json.loads((HERE / "the_shared_tau.json").read_text(encoding="utf-8"))["V2"]
    s1 = {}
    for num in ALL:
        found = rep[num]["found"]
        SOLS[num] = mirror_closed([(np.array(p[2:]), complex(*t), v) for p, v, t in found])
        if num == 16:
            rec_t = complex(*w114["16"]["best point"]["tau_in_F"])
            ok = abs(complex(*found[0][2]) - rec_t) < 1e-6
        else:
            rec_ts = [complex(*x["tau"]) for x in w115[str(num)]["solutions"]]
            ok = len(rec_ts) == len(found) and all(abs(complex(*f[2]) - r) < 1e-6 for f, r in zip(found, rec_ts))
        s1[str(num)] = {"found": [{"tau": f[2], "chi2_q": f[1]} for f in found], "reproduced": bool(ok),
                        "warm starts after the mirror": [[t.real, t.imag] for _, t, _ in SOLS[num]],
                        "seconds": rep[num]["seconds"]}
        log("replay", num, "reproduced", ok, len(found), "found,", len(SOLS[num]), "with mirrors")

    # ---------------- the fits
    tasks = [("tick", tick_ci, n) for n in ALL] + [("control", None, None)]
    tasks += [("census", ci, n) for n in ALL for ci in range(len(CLASSES))]
    res = {}
    with ctx.Pool(NWORK) as pool:
        it = pool.imap_unordered(dispatch, tasks)
        for key, rec in it:
            res[key] = rec
            if key != "control":
                log("fit", key, CLASSES[key[1]][0], f"chi2_min {rec['chi2_min']:.4g}")
    ctl = res.pop("control")
    s1["control"] = ctl
    out["S1"] = {"replay": s1, "holds": bool(all(s1[str(n)]["reproduced"] for n in ALL) and ctl["holds"])}
    log("S1", out["S1"]["holds"], "control chi2", ctl["chi2_min"])

    fits = {}
    for (kind, ci, num), rec in sorted(res.items(), key=lambda kv: (kv[0][0], kv[0][1], kv[0][2])):
        fits.setdefault(kind, {}).setdefault(CLASSES[ci][0], {})[str(num)] = rec
    out["fits"] = fits

    # ---------------- the lines: every line takes its class's values (CP); distances to the solutions
    per_line = {}
    for ci, (repw, ls) in enumerate(CLASSES):
        cen = fits["census"][repw]
        for k in ls:
            L = LINES[k]
            dist = {}
            grid = np.linspace(-L.ell / 2, L.ell / 2, NGRID, endpoint=False)
            Tg = L.tf(grid)
            for num in ALL:
                dist[str(num)] = float(min(surface_dist(Tg, t).min() for _, t, _ in SOLS[num]))
            row = {"class": ci, "fitted on": repw, "words": lines[k], "length": L.ell,
                   "chi2_min": {str(n): cen[str(n)]["chi2_min"] for n in ALL},
                   "chi2_fam": min(cen[str(n)]["chi2_min"] for n in FAM),
                   "distance to the nearest solution": dist}
            per_line[k] = row
    out["lines"] = per_line
    fam = {k: r["chi2_fam"] for k, r in per_line.items()}
    tick_fam = fam["LR"]

    # ---------------- S4 .. S7
    tk = {str(n): {"census budget": fits["census"]["LR"][str(n)]["chi2_min"],
                   "tick budget": fits["tick"]["LR"][str(n)]["chi2_min"]} for n in ALL}
    out["S4"] = {"the tick": tk, "holds": bool(all(min(tk[str(n)].values()) > PASS[1] for n in FAM))}
    passing = sorted(k for k, v in fam.items() if v <= PASS[1])
    out["S5"] = {"lines that pass": passing, "number": len(passing), "of": len(fam), "holds": bool(len(passing) >= 1),
                 "read-out: the least chi2_fam over every line (the union)": min(fam.values()),
                 "on": min(fam, key=fam.get)}
    p = sum(1 for v in fam.values() if v <= tick_fam) / len(fam)
    out["S6"] = {"the tick's chi2_fam (census budget)": tick_fam, "p": p, "holds": bool(p >= 0.05)}
    ex16 = sorted(k for k, r in per_line.items() if r["chi2_min"]["16"] <= 1e-6)
    out["S7"] = {"lines with chi2_min <= 1e-6 for 16": ex16, "number": len(ex16)}
    out["cells"] = {c: out[c]["holds"] for c in ("S0", "S1", "S2", "S3", "S4", "S5", "S6")}
    out["seconds"] = time.time() - T0
    (HERE / "the_seed_geodesics.json").write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
    log("S4", out["S4"]["holds"], "S5", out["S5"]["number"], "S6 p", p, "S7", len(ex16))
    log("cells", out["cells"])
    log("written the_seed_geodesics.json")


def dispatch(t):
    if t[0] == "control":
        return task_control(None)
    return task_fit(t)


if __name__ == "__main__":
    main()
