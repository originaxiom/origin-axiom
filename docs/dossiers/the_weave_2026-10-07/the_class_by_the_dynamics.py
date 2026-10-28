#!/usr/bin/env python3
"""W176 — the web seat's question 3 as the weave sees it (the rule: W176_RULE.md, committed and pushed before this
script). A weave-forced condition on the line sees only its order N (W140), so within an order the class is the
dynamics' choice. Per N, the frame's own one-loop potential (W172's kernel and content) over every line of order N and
tau in the fundamental domain F: its least, the height it holds, whether that least is CP-fixed (exact test), and
whether it sits in the six's band.

  K0  transitivity of L, R on the points of exact order N (exact)
  K1  (0, 1/N) at Re tau = 0 is mirror-fixed (the exact test)
  K2  for every N >= 2 the least lies below Im tau = 3.9
  K3  for every N the least is CP-fixed (decisive)
  K4  for no N does the least lie at 2 <= Im tau <= 4
  R   per N: tau*, the line, V*, the CP status, J where defined, the refined candidates; the overall least

    python3 -B docs/dossiers/the_weave_2026-10-07/the_class_by_the_dynamics.py

Fixed for the second launch (2026-10-28; the_class_by_the_dynamics_first_launch_stopped.txt). The first launch was
stopped by the session's one-hour limit on a background task, refining order 30 after the grid and fifteen orders; it
writes only at its end, so nothing was written and only its progress lines were seen. Its refinement was Nelder-Mead,
unconstrained and then reduced into F, which is not the rule's wording ("L-BFGS-B, staying in F") and was slow. Now:
L-BFGS-B on a box around F, the result reduced into F with the line carried, repeated until it stays in F; and the
refinement is spread over the four workers. No cell, threshold, grid, order or line changed.
"""
import contextlib
import io
import itertools
import json
import math
import multiprocessing as mpc
import platform
import sys
import time
import traceback
import warnings
from fractions import Fraction as Fr
from pathlib import Path

import numpy as np
from scipy.optimize import minimize

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
with contextlib.redirect_stdout(io.StringIO()):
    import the_price_of_cp_at_the_counted_line as W72   # noqa: E402  (W172: the kernel at general s, the content)
    import the_higgs_from_the_action as W66             # noqa: E402  (W166: the frame for own_point)
W67, T8 = W72.W67, W72.T8
OUT = HERE / "the_class_by_the_dynamics.json"
ORDERS = tuple(range(1, 13)) + (15, 20, 25, 30)
S = 3
YTOP = 4.0
XS = [round(-0.5 + 0.05 * i, 4) for i in range(21)]
YS = [round(0.9 + 0.1 * i, 4) for i in range(32)]
ARC = [complex(math.cos(t), math.sin(t)) for t in np.linspace(math.pi / 3, 2 * math.pi / 3, 21)]
KEY = "ckm|L_max|St|S"
WORKERS = 4
LOCUS_TOL = 1e-5
_ROOT = {}
_G = {}


def sanitize(text):
    for k, v in _ROOT.items():
        text = text.replace(v, k)
    return text


# ============================================================================================ lines and the group
def lines_of_order(N):
    """every (a, b) in (Q/Z)^2 of exact order N, up to sign, as Fractions"""
    out, seen = [], set()
    for j in range(N):
        for k in range(N):
            if math.gcd(math.gcd(j, k), N) != 1:
                continue
            key = min((j, k), ((-j) % N, (-k) % N))
            if key not in seen:
                seen.add(key)
                out.append((Fr(key[0], N), Fr(key[1], N)))
    return out


def psi_of(line):
    return (-line[0], line[1])


def line_of(psi):
    return ((-psi[0]) % 1, psi[1] % 1)


def same_up_to_sign(p, q):
    return ((p[0] - q[0]) % 1 == 0 and (p[1] - q[1]) % 1 == 0) or ((p[0] + q[0]) % 1 == 0 and (p[1] + q[1]) % 1 == 0)


def act(g, tau):
    p, q, r, s = g
    return (p * tau + q) / (r * tau + s)


def carry(g, phi):
    """the configuration (tau, phi) equals (g tau, psi) with psi = phi M^-1, M = [[p, -q], [-r, s]]"""
    p, q, r, s = g
    return (s * phi[0] + r * phi[1], q * phi[0] + p * phi[1])


def mul(g, h):
    a, b, c, d = g
    e, f, k, l = h
    return (a * e + b * k, a * f + b * l, c * e + d * k, c * f + d * l)


SL_WORDS = []
_gens = {"S": (0, -1, 1, 0), "T": (1, 1, 0, 1), "t": (1, -1, 0, 1)}
for n in range(0, 5):
    for w in itertools.product("STt", repeat=n):
        g = (1, 0, 0, 1)
        for ch in w:
            g = mul(g, _gens[ch])
        if g not in SL_WORDS:
            SL_WORDS.append(g)


def cp_fixed(tau, psi):
    """exact: is the mirror image (-conj tau, (psi1, -psi2)) the same configuration up to SL(2,Z) and sign?"""
    mt = -tau.conjugate()
    mp = (psi[0], -psi[1])
    hits = []
    for g in SL_WORDS:
        if abs(act(g, mt) - tau) < LOCUS_TOL:
            if same_up_to_sign(carry(g, mp), psi):
                return True, g
            hits.append(g)
    return False, (hits[0] if hits else None)


def reduce_to_F(tau, psi):
    for _ in range(200):
        k = -math.floor(tau.real + 0.5)
        if k:
            g = (1, k, 0, 1)
            psi, tau = carry(g, psi), act(g, tau)
        if abs(tau) < 1 - 1e-12:
            g = (0, -1, 1, 0)
            psi, tau = carry(g, psi), act(g, tau)
            continue
        break
    return tau, psi


def k0(N):
    pts = {(j, k) for j in range(N) for k in range(N) if math.gcd(math.gcd(j, k), N) == 1}
    seen, todo = {(0, 1 % N)}, [(0, 1 % N)]
    while todo:
        j, k = todo.pop()
        for nj, nk in (((j + k) % N, k), (j, (j + k) % N), ((j - k) % N, k), (j, (k - j) % N)):
            if (nj, nk) not in seen:
                seen.add((nj, nk))
                todo.append((nj, nk))
    return seen == pts


# ============================================================================================ the potential
def V_one(tau, psi, wv):
    return float(W72.kq(tau.real, tau.imag, S, np.array([float(psi[0]), float(psi[1])])) @ wv)


def _init(payload):
    _G.update(payload)


def _grid_point(tau):
    """V at tau for every line of every order: one kernel, chunked phases"""
    K = W72.KernelS(tau, S)
    P = _G["P"]                 # (L, 2) float psi of every line
    wv, qs = _G["wv"], _G["QS"]
    out = np.zeros(len(P))
    for qi, q in enumerate(qs):
        if wv[qi] == 0:
            continue
        for lo in range(0, len(P), 400):
            ph = 2 * np.pi * (np.outer(K.m, q * P[lo:lo + 400, 0]) + np.outer(K.n, q * P[lo:lo + 400, 1]))
            out[lo:lo + 400] += wv[qi] * (-(K.cw @ np.cos(ph)))
    return tau, out


def _refine(task):
    """L-BFGS-B on a box around F for the candidate's line, then the result reduced into F with the line carried;
    repeated from the reduced configuration until it stays in F (at most four passes)"""
    tau, phi = task
    wv = _G["wv"]
    for _ in range(4):
        res = minimize(lambda z: V_one(complex(z[0], z[1]), phi, wv), x0=[tau.real, tau.imag], method="L-BFGS-B",
                       bounds=[(-0.6, 0.6), (0.8, YTOP)], options={"ftol": 1e-15, "gtol": 1e-10, "maxiter": 500})
        t2, p2 = reduce_to_F(complex(res.x[0], res.x[1]), phi)
        moved = abs(t2 - complex(res.x[0], res.x[1])) > 1e-12
        tau, phi = t2, p2
        if not moved:
            break
    return {"V": float(V_one(tau, phi, wv)), "tau": [tau.real, tau.imag], "line": [str(x) for x in line_of(phi)]}


def run(root, out, pool_ctx):
    out["K0"] = {"per order": {str(N): k0(N) for N in ORDERS}}
    out["K0"]["holds"] = all(out["K0"]["per order"].values())
    wv = W72.weights(1.0)
    # the transformation law, checked numerically (an instrument check)
    rng = np.random.default_rng(176)
    worst = 0.0
    for _ in range(6):
        tau = complex(rng.uniform(-0.5, 0.5), rng.uniform(1.0, 2.5))
        phi = (Fr(int(rng.integers(0, 30)), 30), Fr(int(rng.integers(0, 30)), 30))
        for g in ((0, -1, 1, 0), (1, 1, 0, 1), (2, 1, 1, 1)):
            a, b = V_one(tau, phi, wv), V_one(act(g, tau), carry(g, phi), wv)
            worst = max(worst, abs(a - b) / abs(a))
    out["instrument: V(g tau; carried line) = V(tau; line), worst relative"] = worst
    # K1 and the controls of the CP test
    k1 = {str(N): cp_fixed(complex(0, 1.3), psi_of((Fr(0), Fr(1, N))))[0] for N in ORDERS}
    out["K1"] = {"per order": k1, "holds": all(k1.values())}
    ctrl_free = cp_fixed(complex(0.3, 2.0), psi_of((Fr(2, 5), Fr(1, 30))))[0]
    out["instrument: a mirror-free slope-2/5 line at Re tau 0.3 tests fixed"] = ctrl_free
    # every line of every order
    lines, owner = [], []
    for N in ORDERS:
        for ln in lines_of_order(N):
            lines.append(ln)
            owner.append(N)
    P = np.array([[float(psi_of(l)[0]), float(psi_of(l)[1])] for l in lines])
    out["lines per order"] = {str(N): owner.count(N) for N in ORDERS}
    taus = [complex(x, y) for x in XS for y in YS if abs(complex(x, y)) >= 1 - 1e-12] + ARC
    out["grid points"] = len(taus)
    t0 = time.time()
    grid = {}
    owner = np.array(owner)
    with pool_ctx.Pool(WORKERS, initializer=_init, initargs=({"P": P, "wv": wv, "QS": W72.QS},)) as pool:
        for j, (tau, vals) in enumerate(pool.imap(_grid_point, taus, chunksize=4)):
            grid[tau] = vals
            if j % 100 == 0:
                print(f"grid {j + 1}/{len(taus)} at {time.time() - t0:.0f} s", flush=True)
        cands = {}
        for N in ORDERS:
            idx = np.where(owner == N)[0]
            cands[N] = sorted(((grid[t][i], t, i) for t in taus for i in idx), key=lambda v: v[0])[:5]
        tasks = [(t, psi_of(lines[i])) for N in ORDERS for (_v, t, i) in cands[N]]
        done = pool.map(_refine, tasks, chunksize=1)
        print(f"refined {len(done)} candidates at {time.time() - t0:.0f} s", flush=True)
    with contextlib.redirect_stdout(io.StringIO()):
        col, _sha, W93, W89, _L = W66.frame(root)
    per = {}
    k = 0
    for N in ORDERS:
        idx = np.where(owner == N)[0]
        refined = []
        for v0, t, i in cands[N]:
            r = dict(done[k])
            k += 1
            r["grid start"] = [t.real, t.imag, float(v0)]
            refined.append(r)
        refined.sort(key=lambda r: r["V"])
        best = refined[0]
        tau_b = complex(*best["tau"])
        psi_b = psi_of((Fr(best["line"][0]), Fr(best["line"][1])))
        fixed, g = cp_fixed(tau_b, psi_b)
        J = None
        if 1.0 <= tau_b.imag <= YTOP:
            o, _d = T8.own_point(W93, W89, col, (Fr(best["line"][0]), Fr(best["line"][1])), tau_b.real, tau_b.imag)
            J = float(o[KEY][3])
        per[str(N)] = {"lines": int(len(idx)), "least": best, "CP-fixed": fixed,
                       "the element tested": list(g) if g else None, "J at the least": J,
                       "refined candidates": refined,
                       "on a slope-2/5 line": Fr(best["line"][0]) in (Fr(2, 5), Fr(3, 5))}
        print(f"order {N} done", flush=True)
    out["per order"] = per
    ys = {N: per[str(N)]["least"]["tau"][1] for N in ORDERS}
    out["K2"] = {"Im tau at the least": {str(N): ys[N] for N in ORDERS},
                 "holds": all(ys[N] < 3.9 for N in ORDERS if N >= 2)}
    out["K3"] = {"CP-fixed per order": {str(N): per[str(N)]["CP-fixed"] for N in ORDERS},
                 "holds": all(per[str(N)]["CP-fixed"] for N in ORDERS)}
    out["K4"] = {"orders with the least in the band": [N for N in ORDERS if 2.0 <= ys[N] <= YTOP],
                 "holds": not any(2.0 <= ys[N] <= YTOP for N in ORDERS)}
    best_N = min(ORDERS, key=lambda N: per[str(N)]["least"]["V"])
    out["R"] = {"the order with the least V overall": best_N, "its least": per[str(best_N)]["least"]}
    out["cells"] = {k: out[k]["holds"] for k in ("K0", "K1", "K2", "K3", "K4")}


def main():
    root = T8.repo_root()
    _ROOT["<repo>"] = str(root)
    _ROOT["<home>"] = str(Path.home())
    t0 = time.time()
    out = {"arc": "W176", "rule": "W176_RULE.md", "status": "one run", "head": T8.resolve(root, "HEAD"),
           "python": sys.version.split()[0], "numpy": np.__version__, "machine": platform.machine(),
           "workers": WORKERS}
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        try:
            run(root, out, mpc.get_context("fork"))
        except Exception:  # noqa: BLE001  (a failed run is a failed launch, disclosed as such)
            out["run_failed"] = sanitize(traceback.format_exc()[-4000:])
    out["warnings"] = sorted({sanitize(f"{w.category.__name__}: {w.message}") for w in caught})
    out["seconds"] = round(time.time() - t0, 1)
    OUT.write_text(json.dumps(out, indent=1, default=float) + "\n", encoding="utf-8")
    print("done" if "run_failed" not in out else "run failed")


if __name__ == "__main__":
    main()
