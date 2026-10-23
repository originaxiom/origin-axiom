#!/usr/bin/env python3
"""INVERSE HIGGS (POST HOC reconnaissance, labelled; not a test, no cell).  Committed before its run; its output is
committed before it is read.  On a stored channel grid (channel_store.py) it asks: if the Higgs direction were free,
how close could main's frame come to the nine?  It separates what the channels (line, tau, horocycle, the sectors'
twists) can carry from what a Higgs must supply.

Structures (c = 3 on the leptons throughout, as every value test since B1726; leptons use the down Higgs):
  A2  aligned two-Higgs: up sees h_u, down and leptons see h_d, both free in CP^2 (a reading is absorbed: S~ with h is
      S with conj h);
  A1  one Higgs in every sector: h_u = h_d = h free;
  SM  the Standard Model's reading of one Higgs: up sees conj h, down and leptons see h, h free.
Each free direction is six real numbers (x + iy, normalised; the phase and the norm drop out of every ratio and |V|).
The objective is B1720 compare.py's chi2_nine (sigma^2 = the pinned relative error^2 + 0.10^2) over the six ratios and
|V_us|, |V_cb|, |V_ub|; the chi2_six is reported at the same optimum and separately minimised.
Minimiser: scipy least_squares (trf, at most 400 evaluations) on the nine residuals from fixed starts: A1 and SM from
the record's directions at tau (DR, F_6, F_22, F_-2, h2, h3, each also conjugated) and four random directions (numpy
default_rng(1720)); A2 from ten record pairs (up, down) of h0-led forms, (F_6, F_22), (F_6, DR), (DR, DR), (F_22, F_22),
(F_6, F_6), (F_10, F_14), (F_14, F_22), (DR, F_22), (F_2, F_2), (F_2, DR), and two random pairs.  The six-only minimum
is sought from the nine's optimum and the same starts' best two.

Points: every point and horocycle of the grid is screened by the null-Higgs read-out (h = h0 = (0, 1, i)/sqrt2 in both
sectors: V_cb and the three m2/m3, which the Higgs moves least); the 160 best (point, horocycle) by that screen's chi2
are optimised (all three structures; two worker processes); the screen's numbers are reported for all.
Per optimised row: the minimum chi2_nine and chi2_six of each structure, the model/data ratios, J, D, and each optimal
direction's components on rho(T)'s eigenlines (e1, h0, conj h0) with its departures delta (e1) and epsilon (the other
null line) relative to the leading null component, beside the record forms' values at the same tau.
    python3 -B inverse_higgs.py --grid two_higgs      # writes inverse_higgs_<grid>.json"""
import hashlib, json, math, subprocess, sys, time, pathlib
import numpy as np
from scipy.optimize import least_squares

HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / ".git").exists())


def git(path):
    return subprocess.run(["git", "show", f"3412bf09d:{path}"], cwd=ROOT, capture_output=True, check=True).stdout


bd = git("frontier/B1637_fits_on_the_ruled_branch/received/HZ2021_running_masses_MZ.json")
bc = git("frontier/B1612_the_mixing_patterns_the_weave_fixes/verification/data.json")
assert hashlib.sha256(bd).hexdigest() == "63450365401c149c726e928f842bc7810086ad4d897a62f51217e3c12189880f"
assert hashlib.sha256(bc).hexdigest() == "61ea1565a2a8b4e053c33cc3b29e37484f6c9c2aeca54f9b6a83c89137e0d606"
m = json.loads(bd)["masses_GeV"]; v, s = m["value"], m["sigma"]; ck = json.loads(bc)["ckm_abs"]; C, CS = ck["value"], ck["sigma"]
PAIRS = [("c", "t"), ("u", "t"), ("s", "b"), ("d", "b"), ("mu", "tau"), ("e", "tau")]
T6 = np.log(np.array([v[a] / v[b] for a, b in PAIRS]))
T9 = np.concatenate([T6, np.log(np.array([C[0][1], C[1][2], C[0][2]]))])
REL = np.array([math.hypot(s[a] / v[a], s[b] / v[b]) for a, b in PAIRS] + [CS[0][1] / C[0][1], CS[1][2] / C[1][2], CS[0][2] / C[0][2]])
SIG = np.sqrt(REL ** 2 + 0.10 ** 2)
LC = math.log(3.0)
F1 = np.array([0, 1, -1j]) / math.sqrt(2); F2 = np.array([1, 0, 0], dtype=complex); F3 = np.array([0, 1, 1j]) / math.sqrt(2)


def cross(h):
    return np.array([[0, -h[2], h[1]], [h[2], 0, -h[0]], [-h[1], h[0], 0]])


def closed(u4, h):
    w, u = u4[0], u4[1:]
    return np.outer(u, h) + np.outer(h, u) - (u @ h) * np.eye(3) + w * cross(h)


def nine(Uh, hu, hd):
    """Uh: (sector, channel) weights at one point and horocycle; returns the nine logs, J and D (c = 3)."""
    Yu, Yd, Ye = closed(Uh[0], hu), closed(Uh[1], hd), closed(Uh[2], hd)
    L = np.zeros(9)
    Uu, su, _ = np.linalg.svd(Yu); Ud, sd, _ = np.linalg.svd(Yd); se = np.linalg.svd(Ye, compute_uv=False)
    for j, sv in enumerate((su, sd, se)):
        L[2 * j] = math.log(max(sv[1] / sv[0], 1e-300)); L[2 * j + 1] = math.log(max(sv[2] / sv[0], 1e-300))
    L[4] += LC; L[5] -= LC
    V = np.conj(Uu[:, ::-1].T) @ Ud[:, ::-1]
    L[6] = math.log(max(abs(V[0, 1]), 1e-300)); L[7] = math.log(max(abs(V[1, 2]), 1e-300)); L[8] = math.log(max(abs(V[0, 2]), 1e-300))
    J = float(np.imag(V[0, 1] * V[1, 2] * np.conj(V[0, 2]) * np.conj(V[1, 1])))
    D = math.exp((L[4] - L[2]) + (L[3] - L[5]))
    return L, J, D


def vec(x):
    z = x[:3] + 1j * x[3:]
    n = np.linalg.norm(z)
    return z / n if n > 0 else F3


def unvec(z):
    return np.concatenate([z.real, z.imag])


def make(structure, Uh):
    if structure == "A2":
        def res(x):
            L, _, _ = nine(Uh, vec(x[:6]), vec(x[6:])); return (L - T9) / SIG
        def dirs(x):
            return vec(x[:6]), vec(x[6:])
    elif structure == "A1":
        def res(x):
            h = vec(x); L, _, _ = nine(Uh, h, h); return (L - T9) / SIG
        def dirs(x):
            return vec(x), vec(x)
    else:                                                         # SM
        def res(x):
            h = vec(x); L, _, _ = nine(Uh, np.conj(h), h); return (L - T9) / SIG
        def dirs(x):
            h = vec(x); return np.conj(h), h
    return res, dirs


def decomp(h):
    c = np.array([np.vdot(F2, h), np.vdot(F3, h), np.vdot(F1, h)])
    lead = int(np.argmax(np.abs(c[1:]))) + 1
    other = 3 - lead
    return {"|e1|, |h0|, |conj h0|": [round(float(abs(q)), 5) for q in c], "leading null": ["h0", "conj h0"][lead - 1],
            "delta = e1 / leading": round(float(abs(c[0] / c[lead])), 5) if abs(c[lead]) > 0 else None,
            "epsilon = other null / leading": round(float(abs(c[other] / c[lead])), 5) if abs(c[lead]) > 0 else None}


def solve(structure, Uh, starts, six_only=False):
    res, dirs = make(structure, Uh)
    f = (lambda x: res(x)[:6]) if six_only else res
    best = None
    for x0 in starts:
        try:
            r = least_squares(f, x0, method="trf", max_nfev=400, xtol=1e-10, ftol=1e-10)
        except Exception:
            continue
        val = float(np.sum(r.fun ** 2))
        if best is None or val < best[0]:
            best = (val, r.x)
    return best, dirs


NULLED = ["dR", "F_2", "F_6", "F_10", "F_14", "F_18", "F_22", "F_26"]
A2_PAIRS = [("F_6", "F_22"), ("F_6", "dR"), ("dR", "dR"), ("F_22", "F_22"), ("F_6", "F_6"), ("F_10", "F_14"),
            ("F_14", "F_22"), ("dR", "F_22"), ("F_2", "F_2"), ("F_2", "dR")]
ONE = ["dR", "F_6", "F_22", "F_-2", "h2", "h3"]
G = {}


def init(gname):
    st = np.load(HERE / f"channel_store_{gname}.npz")
    G["U"], G["H"] = st["U"], st["H"]
    G["I"] = json.loads((HERE / f"channel_store_{gname}_index.json").read_text())
    rng = np.random.default_rng(1720)
    G["rnd"] = [unvec(z / np.linalg.norm(z)) for z in (rng.normal(size=(8, 3)) + 1j * rng.normal(size=(8, 3)))]


def one_row(args):
    p, ih, screen = args
    U, H, I, rnd = G["U"], G["H"], G["I"], G["rnd"]
    DIRS = I["dirs"]; tasks = I["tasks"]; lines = I["lines"]; hors = I["hors"]
    Uh = U[p, :, ih]; Hp = H[p]
    led = {}
    for d in NULLED:
        z = Hp[DIRS.index(d)]
        led[d] = z if abs(np.vdot(F3, z)) >= abs(np.vdot(F1, z)) else np.conj(z)
    pair_starts = [np.concatenate([unvec(led[a]), unvec(led[b])]) for a, b in A2_PAIRS]
    pair_starts += [np.concatenate([rnd[0], rnd[1]]), np.concatenate([rnd[2], rnd[3]])]
    one_starts = [unvec(Hp[DIRS.index(d)]) for d in ONE] + [unvec(np.conj(Hp[DIRS.index(d)])) for d in ONE] + rnd[4:8]
    row = {"point": tasks[p], "line": lines[tasks[p][0]], "hor": hors[ih], "screen chi2": round(float(screen), 3),
           "r = exp(-pi Im tau)": math.exp(-math.pi * tasks[p][2]),
           "record forms at tau (h0-led): delta, epsilon": {d: [decomp(led[d])["delta = e1 / leading"], decomp(led[d])["epsilon = other null / leading"]] for d in ("dR", "F_6", "F_22")}}
    for stt, starts in (("A2", pair_starts), ("A1", one_starts), ("SM", one_starts)):
        best, dirs = solve(stt, Uh, starts)
        hu, hd = dirs(best[1])
        L, J, D = nine(Uh, hu, hd)
        res, _ = make(stt, Uh)
        ranked = sorted(starts, key=lambda x0: float(np.sum(res(x0)[:6] ** 2)))[:2]
        best6, _ = solve(stt, Uh, [best[1]] + ranked, six_only=True)
        row[stt] = {"min chi2_nine": round(best[0], 3), "chi2_six there": round(float(np.sum(((L[:6] - T6) / SIG[:6]) ** 2)), 3),
                    "model/data": [round(float(q), 4) for q in np.exp(L - T9)], "J": J, "D": round(D, 4),
                    "h_u": decomp(hu), "h_d": decomp(hd), "min chi2_six (separately)": round(best6[0], 3)}
    return row


def main():
    from multiprocessing import Pool
    gname = sys.argv[sys.argv.index("--grid") + 1]
    init(gname)
    U, I = G["U"], G["I"]
    tasks, hors = I["tasks"], I["hors"]
    scr = np.zeros((len(tasks), len(hors)))
    for p in range(len(tasks)):
        for ih in range(len(hors)):
            L, _, _ = nine(U[p, :, ih], F3, F3)
            sel = [0, 2, 4, 7]
            scr[p, ih] = float(np.sum(((L[sel] - T9[sel]) / SIG[sel]) ** 2))
    order = np.argsort(scr, axis=None)[:160]
    jobs = []
    for k in order:
        p, ih = np.unravel_index(int(k), scr.shape); jobs.append((int(p), int(ih), float(scr[p, ih])))
    out = {"grid": gname, "screen": "null Higgs h0 in both sectors: chi2 over (m_c/m_t, m_s/m_b, m_mu/m_tau with c = 3, V_cb)",
           "screen minimum and median over all (point, horocycle)": [float(scr.min()), float(np.median(scr))], "rows": []}
    t0 = time.time()
    with Pool(2, initializer=init, initargs=(gname,)) as P:
        for n, row in enumerate(P.imap(one_row, jobs)):
            out["rows"].append(row)
            if n % 10 == 0:
                print(f"{n + 1} of {len(jobs)} rows, {time.time() - t0:.0f} s", flush=True)
    rows = out["rows"]
    out["summary"] = {stt: {"lowest min chi2_nine": min(rw[stt]["min chi2_nine"] for rw in rows),
                            "rows with min chi2_nine below 21.67": sum(rw[stt]["min chi2_nine"] < 21.67 for rw in rows),
                            "lowest min chi2_six": min(rw[stt]["min chi2_six (separately)"] for rw in rows)} for stt in ("A2", "A1", "SM")}
    (HERE / f"inverse_higgs_{gname}.json").write_text(json.dumps(out, indent=1, default=float) + "\n")
    print("written", flush=True)


if __name__ == "__main__":
    main()
