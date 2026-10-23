#!/usr/bin/env python3
"""RECORD PAIRS (POST HOC reconnaissance, labelled; committed before its run, its output committed before it is read).
On the stored channel grid, every ordered pair (H_u, H_d) of the record's Higgs directions in both orientations
(each direction or its conjugate; for the null-led forms the two orientations are 'h0-led' and 'conj h0-led'), the
leptons with H_d and c = 3: the nine at every point and horocycle, B1720's chi2 (sigma^2 = rel^2 + 0.10^2).
The record's directions: DR, R = F_2 (exactly null: m1 = 0, kept as a reference), the zero-free F_a for
a = -10, -6, -2, 6, 10, 14, 18, 22, 26, B1700's h2 and h3.  Pairs whose two directions share the leading null line are
'aligned'; the others are reported apart.  The multiplier exponent r = 2a mod 24 of each F_a is carried so that a
pairing rule (r_u + r_d = 0 mod 24) can be read off; it selects nothing here.
Output: per pair the lowest chi2_nine and chi2_six (and where), the overall best rows, and the best aligned rows with
their parts.
    python3 -B record_pairs.py --grid two_higgs      # writes record_pairs_<grid>.json"""
import hashlib, json, math, subprocess, sys, pathlib
import numpy as np

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
F1 = np.array([0, 1, -1j]) / math.sqrt(2); F3 = np.array([0, 1, 1j]) / math.sqrt(2)


def cross(h):
    return np.array([[0, -h[2], h[1]], [h[2], 0, -h[0]], [-h[1], h[0], 0]])


def closed(u4, h):
    w, u = u4[0], u4[1:]
    return np.outer(u, h) + np.outer(h, u) - (u @ h) * np.eye(3) + w * cross(h)


def nine(Uh, hu, hd):
    Yu, Yd, Ye = closed(Uh[0], hu), closed(Uh[1], hd), closed(Uh[2], hd)
    L = np.zeros(9)
    Uu, su, _ = np.linalg.svd(Yu); Ud, sd, _ = np.linalg.svd(Yd); se = np.linalg.svd(Ye, compute_uv=False)
    for j, sv in enumerate((su, sd, se)):
        L[2 * j] = math.log(max(sv[1] / sv[0], 1e-300)); L[2 * j + 1] = math.log(max(sv[2] / sv[0], 1e-300))
    L[4] += math.log(3); L[5] -= math.log(3)
    V = np.conj(Uu[:, ::-1].T) @ Ud[:, ::-1]
    L[6] = math.log(max(abs(V[0, 1]), 1e-300)); L[7] = math.log(max(abs(V[1, 2]), 1e-300)); L[8] = math.log(max(abs(V[0, 2]), 1e-300))
    J = float(np.imag(V[0, 1] * V[1, 2] * np.conj(V[0, 2]) * np.conj(V[1, 1])))
    return L, J


def lead(h):
    a, b = abs(np.vdot(F3, h)), abs(np.vdot(F1, h))
    return "h0" if a >= b else "conj h0"


def main():
    gname = sys.argv[sys.argv.index("--grid") + 1]
    st = np.load(HERE / f"channel_store_{gname}.npz"); U, H = st["U"], st["H"]
    I = json.loads((HERE / f"channel_store_{gname}_index.json").read_text())
    DIRS = I["dirs"]; tasks = I["tasks"]; lines = I["lines"]; hors = I["hors"]
    names = [d for d in DIRS]
    rexp = {d: (2 * int(d[2:])) % 24 for d in DIRS if d.startswith("F_")}
    best = {}
    allrows = []
    for p in range(len(tasks)):
        Hp = H[p]
        opts = []
        for d in names:
            z = Hp[DIRS.index(d)]
            opts.append((d, "as is", z)); opts.append((d, "conj", np.conj(z)))
        for ih in range(len(hors)):
            Uh = U[p, :, ih]
            for (du, ou, hu) in opts:
                for (dd, od, hd) in opts:
                    L, J = nine(Uh, hu, hd)
                    chi9 = float(np.sum(((L - T9) / SIG) ** 2)); chi6 = float(np.sum(((L[:6] - T6) / SIG[:6]) ** 2))
                    key = (du, ou, dd, od)
                    aligned = lead(hu) == lead(hd)
                    b = best.get(key)
                    if b is None or chi9 < b["min chi2_nine"]:
                        best[key] = {"up": f"{du} ({ou})", "down": f"{dd} ({od})", "aligned": aligned, "min chi2_nine": chi9,
                                     "chi2_six there": chi6, "at": [lines[tasks[p][0]], tasks[p][1], tasks[p][2], hors[ih]],
                                     "model/data": [round(float(q), 3) for q in np.exp(L - T9)], "J": J,
                                     "D": math.exp((L[4] - L[2]) + (L[3] - L[5])), "min chi2_six": best.get(key, {}).get("min chi2_six", 1e99)}
                    best[key]["min chi2_six"] = min(best[key]["min chi2_six"], chi6)
                    if chi9 < 60:
                        allrows.append({"up": f"{du} ({ou})", "down": f"{dd} ({od})", "aligned": aligned, "chi2_nine": chi9, "chi2_six": chi6,
                                        "at": [lines[tasks[p][0]], tasks[p][1], tasks[p][2], hors[ih]],
                                        "model/data": [round(float(q), 3) for q in np.exp(L - T9)], "J": J})
        if p % 128 == 0:
            print(f"point {p} of {len(tasks)}", flush=True)
    vals = sorted(best.values(), key=lambda b: b["min chi2_nine"])
    out = {"grid": gname, "multiplier exponent r = 2a mod 24": rexp,
           "pairs evaluated": len(best), "the 25 best pairs by their lowest chi2_nine": vals[:25],
           "the 10 best aligned pairs": [b for b in vals if b["aligned"]][:10],
           "rows below chi2_nine 60 (all pairs), the 40 lowest": sorted(allrows, key=lambda r: r["chi2_nine"])[:40],
           "pairs with a row below 21.67": sum(b["min chi2_nine"] < 21.67 for b in vals),
           "pairs with a row below chi2_six 16.75": sum(b["min chi2_six"] < 16.75 for b in vals)}
    (HERE / f"record_pairs_{gname}.json").write_text(json.dumps(out, indent=1, default=float) + "\n")
    print("written", flush=True)


if __name__ == "__main__":
    main()
