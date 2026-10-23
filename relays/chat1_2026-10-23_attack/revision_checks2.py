#!/usr/bin/env python3
"""REVISION CHECKS 2 for THE_NEXT_ATTACK.md, after its second read-only referee pass (committed before its run; output
committed before it is read).  Data-free unless marked; the channel store's ten (2/5, k/10) lines throughout.
  S1  the down quarks' m2/m3 and V_cb spread over the eight null-led record forms (DR, F_2, F_6, F_10, F_14, F_18, F_22,
      F_26, each oriented n-led, the same direction in both sectors): max/min, median and 90th percentile by Im tau band;
  S2  |V_us| against |beta_u - beta_d| for aligned pairs of those forms, with beta from the SVD (the light left state's
      e1 component at unit n-bar component) and from the first-order formula: median relative errors by band;
  S3  (pinned data) sqrt(m_d/m_s) against |V_us| and the uncertainty of sqrt(m_d/m_s);
  S4  (post hoc, the committed inverse_higgs output) the A2 optima's |delta_d|^2 / (2 |eps_d|): median over all 160
      rows, over the 150 below 21.67, and by horocycle; and their V_cb against the null Higgs's at the same row;
  S5  the Standard Model's reading (up sees conj h, down and leptons h) with the record's forms in both orientations
      (DR, F_6, F_22, F_14, F_10, R): medians of up m2/m3, |V_ud|, |V_cb| by orientation class (h led by n or by n-bar);
      and 40 random nearly null directions per row and orientation (numpy default_rng(1723); h = lead + d e1 + e other,
      |d| <= 0.25, |e| <= 0.03): the number with an up hierarchy (m_c/m_t < 7.4e-3, m_u/m_t < 1e-4), of those the number
      with |V_ud| > 0.9, and of those the number with |V_cb| < 0.2;
  S6  the idealised lemma against the stored up channels: (m2/m3) / (|h.h|/4) for 40 random unit h per row: quantiles;
  S7  the leptons' light singular value against the down quarks' on the order-10 lines, at leading order
      |u_d.h| / |u_d.P h| (P = diag(-1, 1, 1)), for DR in both orientations: median relative error by band.
    python3 -B revision_checks2.py      # writes revision_checks2.json"""
import hashlib, json, math, subprocess, pathlib
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / ".git").exists())
st = np.load(HERE / "channel_store_two_higgs.npz"); U, H = st["U"], st["H"]
I = json.loads((HERE / "channel_store_two_higgs_index.json").read_text())
tasks, hors, DIRS = I["tasks"], I["hors"], I["dirs"]
F1 = np.array([0, 1, -1j]) / math.sqrt(2); F2 = np.array([1, 0, 0], dtype=complex); F3 = np.array([0, 1, 1j]) / math.sqrt(2)
P = np.diag([-1.0, 1.0, 1.0]).astype(complex)
OUT = {}


def cross(h):
    return np.array([[0, -h[2], h[1]], [h[2], 0, -h[0]], [-h[1], h[0], 0]])


def closed(u4, h):
    w, u = u4[0], u4[1:]
    return np.outer(u, h) + np.outer(h, u) - (u @ h) * np.eye(3) + w * cross(h)


def nled(v):
    return v if abs(np.vdot(F3, v)) >= abs(np.vdot(F1, v)) else np.conj(v)


def band(y):
    return "2.0-2.5" if y < 2.5 else ("2.5-3.0" if y < 3.0 else "3.0-3.5")


def lstate(Y):
    Ul = np.linalg.svd(Y)[0]
    return Ul[:, ::-1]                                      # columns light, middle, heavy


NULLED = ["dR", "F_2", "F_6", "F_10", "F_14", "F_18", "F_22", "F_26"]
# S1
s1 = {}
for p, t in enumerate(tasks):
    hs = [nled(H[p, DIRS.index(d)]) for d in NULLED]
    for ih in range(2):
        m23, vcb = [], []
        for h in hs:
            Yu, Yd = closed(U[p, 0, ih], h), closed(U[p, 1, ih], h)
            sd = np.linalg.svd(Yd, compute_uv=False); m23.append(sd[1] / sd[0])
            V = np.conj(lstate(Yu).T) @ lstate(Yd); vcb.append(abs(V[1, 2]))
        s1.setdefault(band(t[2]), {"down m2/m3": [], "V_cb": []})
        s1[band(t[2])]["down m2/m3"].append(max(m23) / min(m23)); s1[band(t[2])]["V_cb"].append(max(vcb) / min(vcb))
OUT["S1 max/min over the eight null-led forms: median, 90th percentile"] = {
    b: {k: [round(float(np.median(v)), 3), round(float(np.quantile(v, 0.9)), 3)] for k, v in d.items()} for b, d in sorted(s1.items())}
# S2
s2 = {}
pairs = [("F_6", "F_22"), ("dR", "dR"), ("F_6", "dR"), ("F_14", "F_22"), ("F_6", "F_6")]
for p, t in enumerate(tasks):
    for ih in range(2):
        for du, dd in pairs:
            hu, hd = nled(H[p, DIRS.index(du)]), nled(H[p, DIRS.index(dd)])
            bs, bf = [], []
            for i_s, h in ((0, hu), (1, hd)):
                hh = h / np.vdot(F3, h)
                Y = closed(U[p, i_s, ih], hh); x = lstate(Y)[:, 0]; x = x / np.vdot(F1, x); bs.append(np.vdot(F2, x))
                w, u = U[p, i_s, ih, 0], U[p, i_s, ih, 1:]
                a1, a2, a3 = np.vdot(F1, u), np.vdot(F2, u), np.vdot(F3, u); Dl = u @ u + w * w
                de, ep = np.vdot(F2, hh), np.vdot(F1, hh)
                bf.append(np.conj(de + 2 * ep * a3 * (a2 - 1j * w) / Dl))
            V = np.conj(lstate(closed(U[p, 0, ih], hu)).T) @ lstate(closed(U[p, 1, ih], hd))
            vus = abs(V[0, 1])
            key = f"{du} | {dd}, {band(t[2])}"
            s2.setdefault(key, {"SVD beta": [], "first-order beta": []})
            s2[key]["SVD beta"].append(abs(abs(bs[0] - bs[1]) - vus) / vus); s2[key]["first-order beta"].append(abs(abs(bf[0] - bf[1]) - vus) / vus)
OUT["S2 median relative error of |beta_u - beta_d| as |V_us|"] = {k: {kk: round(float(np.median(vv)), 4) for kk, vv in v.items()} for k, v in sorted(s2.items())}
# S3
def git(path):
    return subprocess.run(["git", "show", f"3412bf09d:{path}"], cwd=ROOT, capture_output=True, check=True).stdout
bd = git("frontier/B1637_fits_on_the_ruled_branch/received/HZ2021_running_masses_MZ.json")
bc = git("frontier/B1612_the_mixing_patterns_the_weave_fixes/verification/data.json")
assert hashlib.sha256(bd).hexdigest() == "63450365401c149c726e928f842bc7810086ad4d897a62f51217e3c12189880f"
assert hashlib.sha256(bc).hexdigest() == "61ea1565a2a8b4e053c33cc3b29e37484f6c9c2aeca54f9b6a83c89137e0d606"
m = json.loads(bd)["masses_GeV"]; v, s = m["value"], m["sigma"]; C = json.loads(bc)["ckm_abs"]["value"]
g = math.sqrt(v["d"] / v["s"])
OUT["S3 sqrt(m_d/m_s), |V_us|, relative difference, relative uncertainty of sqrt(m_d/m_s)"] = [g, C[0][1], abs(g - C[0][1]) / C[0][1], 0.5 * math.hypot(s["d"] / v["d"], s["s"] / v["s"])]
# S4
D = json.loads((HERE / "inverse_higgs_two_higgs.json").read_text())
gd = {"all 160": [], "below 21.67": [], "L_max": [], "L_2": []}; vr = {"L_max": [], "L_2": []}
idx = {(round(t[1], 6), round(t[2], 6), I["lines"][t[0]]): p for p, t in enumerate(tasks)}
for r in D["rows"]:
    a = r["A2"]; x = a["h_d"]["delta = e1 / leading"] ** 2 / (2 * a["h_d"]["epsilon = other null / leading"])
    gd["all 160"].append(x); gd[r["hor"]].append(x)
    if a["min chi2_nine"] < 21.67:
        gd["below 21.67"].append(x)
    p = idx[(round(r["point"][1], 6), round(r["point"][2], 6), r["line"])]; ih = hors.index(r["hor"])
    V0 = np.conj(lstate(closed(U[p, 0, ih], F3)).T) @ lstate(closed(U[p, 1, ih], F3))
    vr[r["hor"]].append(a["model/data"][7] * C[1][2] / abs(V0[1, 2]))
OUT["S4 A2 optima: median |delta_d|^2/(2|eps_d|)"] = {k: round(float(np.median(v_)), 3) for k, v_ in gd.items()}
OUT["S4 A2 optima: V_cb over the null Higgs's at the same row, median and range"] = {k: [round(float(np.median(v_)), 3), round(float(min(v_)), 3), round(float(max(v_)), 3)] for k, v_ in vr.items()}
# S5
s5 = {}
rng = np.random.default_rng(1723)
cnt = {"n-led": [0, 0, 0, 0], "n-bar-led": [0, 0, 0, 0]}
for p, t in enumerate(tasks):
    for d in ("dR", "F_6", "F_22", "F_14", "F_10", "F_2"):
        z = H[p, DIRS.index(d)]
        for h in (z, np.conj(z)):
            cls = "n-led" if abs(np.vdot(F3, h)) >= abs(np.vdot(F1, h)) else "n-bar-led"
            for ih in range(2):
                Yu, Yd = closed(U[p, 0, ih], np.conj(h)), closed(U[p, 1, ih], h)
                su = np.linalg.svd(Yu, compute_uv=False); V = np.conj(lstate(Yu).T) @ lstate(Yd)
                key = f"{cls}, {band(t[2])}"
                s5.setdefault(key, {"up m2/m3": [], "|V_ud|": [], "|V_cb|": []})
                s5[key]["up m2/m3"].append(su[1] / su[0]); s5[key]["|V_ud|"].append(abs(V[0, 0])); s5[key]["|V_cb|"].append(abs(V[1, 2]))
    for ih in range(2):
        for cls, (lead, other) in (("n-led", (F3, F1)), ("n-bar-led", (F1, F3))):
            for _ in range(40):
                dd = 0.25 * math.sqrt(rng.uniform()) * np.exp(2j * math.pi * rng.uniform())
                ee = 0.03 * math.sqrt(rng.uniform()) * np.exp(2j * math.pi * rng.uniform())
                h = lead + dd * F2 + ee * other; h = h / np.linalg.norm(h)
                Yu, Yd = closed(U[p, 0, ih], np.conj(h)), closed(U[p, 1, ih], h)
                su = np.linalg.svd(Yu, compute_uv=False)
                cnt[cls][0] += 1
                if su[1] / su[0] < 7.4e-3 and su[2] / su[0] < 1e-4:
                    cnt[cls][1] += 1
                    V = np.conj(lstate(Yu).T) @ lstate(Yd)
                    if abs(V[0, 0]) > 0.9:
                        cnt[cls][2] += 1
                        if abs(V[1, 2]) < 0.2:
                            cnt[cls][3] += 1
OUT["S5 the Standard Model's reading with the record's forms: medians"] = {k: {kk: round(float(np.median(vv)), 4) for kk, vv in v_.items()} for k, v_ in sorted(s5.items())}
OUT["S5 random nearly null directions: drawn, with an up hierarchy, of those |V_ud| > 0.9, of those |V_cb| < 0.2"] = cnt
# S6
rat = {}
rng = np.random.default_rng(1724)
for p, t in enumerate(tasks):
    for ih in range(2):
        for _ in range(40):
            h = rng.normal(size=3) + 1j * rng.normal(size=3); h /= np.linalg.norm(h)
            su = np.linalg.svd(closed(U[p, 0, ih], h), compute_uv=False)
            rat.setdefault(band(t[2]), []).append((su[1] / su[0]) / (abs(h @ h) / 4))
OUT["S6 (m2/m3) / (|h.h|/4) for the stored up channels, random unit h: minimum, 1st, 10th, 50th percentile"] = {
    b: [round(float(np.min(v_)), 3)] + [round(float(np.quantile(v_, q)), 3) for q in (0.01, 0.1, 0.5)] for b, v_ in sorted(rat.items())}
# S7
s7 = {}
for p, t in enumerate(tasks):
    if t[0] % 2 == 0:
        continue
    for h in (H[p, DIRS.index("dR")], np.conj(H[p, DIRS.index("dR")])):
        for ih in range(2):
            sd = np.linalg.svd(closed(U[p, 1, ih], h), compute_uv=False); se = np.linalg.svd(closed(U[p, 2, ih], h), compute_uv=False)
            u = U[p, 1, ih, 1:]
            pred = abs(u @ h) / abs(u @ (P @ h))
            s7.setdefault(band(t[2]), []).append(abs((sd[2] / se[2]) / pred - 1))
OUT["S7 order-10 lines, DR both orientations: median relative error of m_d/m_e against |u_d.h|/|u_d.Ph|"] = {b: round(float(np.median(v_)), 4) for b, v_ in sorted(s7.items())}
(HERE / "revision_checks2.json").write_text(json.dumps(OUT, indent=1) + "\n")
print("written")
