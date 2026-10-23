#!/usr/bin/env python3
"""REVISION CHECKS for THE_NEXT_ATTACK.md, after its read-only referee (committed before its run; output committed
before it is read).  R1-R3, R5-R7 are data-free (the channel store, B1736's closed form, the stored Higgs directions);
R4 and R8 read the committed reconnaissance outputs (post hoc, labelled).
  R1  at the band, how good are the first-order formulas?  For DR, F_6 and F_22 (each oriented to be led by the null
      line n = (0, 1, i)/sqrt2) in every sector: |beta| from the first-order formula against the light left state's
      e1 component from the SVD; m2 m3 against |Delta| = |u.u + w^2|; medians of the relative error by Im tau band;
  R2  V_cb under the null Higgs n against |kappa_u - kappa_d| on every row: median and largest relative error;
  R3  V_cb under the null Higgs n by horocycle at each Im tau: the ranges on L_max and L_2 and the per-point ratio;
  R4  the mirror (2/5, b) at Re tau  <->  (2/5, 3/5 - b mod 1) at 1 - Re tau with h -> P conj(h), P = [[-1,0,0],[0,0,1],
      [0,1,0]]: the largest |delta ln| of the singular-value ratios and |V| over every mirror pair of stored points, random
      h; and the committed inverse_higgs minima of mirror pairs that disagree by more than 1%;
  R5  the up channel's idealisation u = a3 n, w = 0: m2 m3 = |a3|^2 |h.h| and m2/m3 >= |h.h|/4 for every unit h (random
      draws; the Frobenius identity); and how far the stored up channels are from it (|u.u|/|u|^2, |w|/|u|, |a2|/|u|,
      |a1|/|u| by line order and Im tau band);
  R6  the leptons' channels against the down quarks': on order-5 lines (w, u) -> (-w, u)?; on order-10 lines the best of
      the eight sign patterns on (w, u_i, u_j, u_k): the largest relative deviation;
  R7  channel_store's C2 extended to every point: TWO_HIGGS's stored rows for 'F_6 | F_22' and 'dR split (up S~)';
  R8  inverse_higgs's A2 optima split by horocycle: median delta_d / r^(1/2), eps_d / r and their ratio to DR's.
    python3 -B revision_checks.py      # writes revision_checks.json"""
import json, math, pathlib
from fractions import Fraction as Fr
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
st = np.load(HERE / "channel_store_two_higgs.npz"); U, H = st["U"], st["H"]
I = json.loads((HERE / "channel_store_two_higgs_index.json").read_text())
tasks, lines, hors, DIRS = I["tasks"], I["lines"], I["hors"], I["dirs"]
F1 = np.array([0, 1, -1j]) / math.sqrt(2); F2 = np.array([1, 0, 0], dtype=complex); F3 = np.array([0, 1, 1j]) / math.sqrt(2)
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


ims = np.array([t[2] for t in tasks])
# R1
acc = {}
for d in ("dR", "F_6", "F_22"):
    for i_s, sec in enumerate(("up", "down", "lep")):
        for p in range(len(tasks)):
            h = nled(H[p, DIRS.index(d)]); c3 = np.vdot(F3, h); hh = h / c3
            de, ep = np.vdot(F2, hh), np.vdot(F1, hh)
            for ih in range(2):
                u4 = U[p, i_s, ih]; w, u = u4[0], u4[1:]
                a1, a2, a3 = np.vdot(F1, u), np.vdot(F2, u), np.vdot(F3, u)
                Dl = u @ u + w * w
                beta = abs(np.conj(de + 2 * ep * a3 * (a2 - 1j * w) / Dl))
                Ul, s, _ = np.linalg.svd(closed(u4, hh))
                x = Ul[:, 2]; x = x / np.vdot(F1, x)
                bnum = abs(np.vdot(F2, x))
                key = f"{d} {sec} {band(tasks[p][2])}"
                acc.setdefault(key, {"beta": [], "m2m3": []})
                acc[key]["beta"].append(abs(beta - bnum) / max(bnum, 1e-30))
                acc[key]["m2m3"].append(abs(s[0] * s[1] - abs(Dl) * abs(c3) ** 0) / (s[0] * s[1]))
OUT["R1 median relative error of the first-order |beta| and of m2 m3 ~ |Delta| (h normalised to unit n-component)"] = {
    k: {"beta": round(float(np.median(v["beta"])), 4), "m2m3 vs |Delta|": round(float(np.median(v["m2m3"])), 4), "n": len(v["beta"])} for k, v in sorted(acc.items())}
# R2, R3
errs = []; vc = {}
for p in range(len(tasks)):
    for ih in range(2):
        kap = {}
        for i_s, sec in enumerate(("up", "down")):
            w, u = U[p, i_s, ih, 0], U[p, i_s, ih, 1:]
            a1, a2, a3 = np.vdot(F1, u), np.vdot(F2, u), np.vdot(F3, u)
            r2 = np.array([a2 - 1j * w, -a1]); r3 = np.array([2 * a3, a2 + 1j * w])
            kap[sec] = np.vdot(r3, r2) / np.vdot(r3, r3)
        Uu = np.linalg.svd(closed(U[p, 0, ih], F3))[0]; Ud = np.linalg.svd(closed(U[p, 1, ih], F3))[0]
        V = np.conj(Uu[:, ::-1].T) @ Ud[:, ::-1]
        vcb = abs(V[1, 2]); errs.append(abs(vcb - abs(kap["up"] - kap["down"])) / vcb)
        vc.setdefault(round(tasks[p][2], 1), {"L_max": {}, "L_2": {}})[hors[ih]][p] = vcb
OUT["R2 |V_cb - |kappa_u - kappa_d|| / V_cb over 2 560 rows: median, largest"] = [float(np.median(errs)), float(np.max(errs))]
R3 = {}
for y, dd in sorted(vc.items()):
    a = np.array([dd["L_max"][p] for p in dd["L_max"]]); b = np.array([dd["L_2"][p] for p in dd["L_max"]])
    R3[str(y)] = {"L_max range": [round(float(a.min()), 4), round(float(a.max()), 4)], "L_2 range": [round(float(b.min()), 4), round(float(b.max()), 4)],
                  "ratio L_max / L_2: median, min, max": [round(float(np.median(a / b)), 3), round(float((a / b).min()), 3), round(float((a / b).max()), 3)]}
OUT["R3 V_cb under the null Higgs by horocycle (data V_cb = 0.0418)"] = R3
# R4
Pm = np.array([[-1, 0, 0], [0, 0, 1], [0, 1, 0]], dtype=complex)
idx = {(t[0], round(t[1], 6), round(t[2], 6)): p for p, t in enumerate(tasks)}
lv = [(Fr(2, 5), Fr(k, 10)) for k in range(10)]
rng = np.random.default_rng(7); worst = 0.0; npairs = 0
for p, (k, re_t, im_t) in enumerate(tasks):
    a, b = lv[k]; bm = (Fr(3, 5) - b) % 1; km = lv.index((a, bm)); q = idx.get((km, round(1 - re_t, 6), round(im_t, 6)))
    if q is None or q < p:
        continue
    npairs += 1
    for _ in range(2):
        hu = rng.normal(size=3) + 1j * rng.normal(size=3); hd = rng.normal(size=3) + 1j * rng.normal(size=3)
        for ih in range(2):
            o = []
            for (pp, xu, xd) in ((p, hu, hd), (q, Pm @ np.conj(hu), Pm @ np.conj(hd))):
                Yu, Yd, Ye = closed(U[pp, 0, ih], xu), closed(U[pp, 1, ih], xd), closed(U[pp, 2, ih], xd)
                su = np.linalg.svd(Yu, compute_uv=False); sd = np.linalg.svd(Yd, compute_uv=False); se = np.linalg.svd(Ye, compute_uv=False)
                Uu = np.linalg.svd(Yu)[0][:, ::-1]; Ud = np.linalg.svd(Yd)[0][:, ::-1]; V = np.abs(np.conj(Uu.T) @ Ud)
                o.append(np.log(np.concatenate([su[1:] / su[0], sd[1:] / sd[0], se[1:] / se[0], [V[0, 1], V[1, 2], V[0, 2]]])))
            worst = max(worst, float(np.max(np.abs(o[0] - o[1]))))
D = json.loads((HERE / "inverse_higgs_two_higgs.json").read_text())
mins = {}
for r in D["rows"]:
    mins[(r["line"], round(r["point"][1], 6), round(r["point"][2], 6), r["hor"])] = r
dis = {"A2": [], "A1": [], "SM": []}; mp_pairs = 0
lab = {f"({a}, {b})": (a, b) for a, b in lv}
for key, r in mins.items():
    ln, re_t, im_t, hor = key; a, b = lab[ln]; bm = (Fr(3, 5) - b) % 1
    mkey = (f"({a}, {bm})", round(1 - re_t, 6), im_t, hor)
    if mkey in mins and key < mkey:
        mp_pairs += 1
        for s_ in ("A2", "A1", "SM"):
            x, y = r[s_]["min chi2_nine"], mins[mkey][s_]["min chi2_nine"]
            if abs(x - y) > 0.01 * min(x, y):
                dis[s_].append([ln, re_t, im_t, hor, x, y])
OUT["R4 mirror pairs of stored points; largest |delta ln| over the twelve outputs, random h, both horocycles"] = {"pairs": npairs, "largest": worst}
OUT["R4 inverse_higgs: mirror pairs among the 160 optimised rows; those whose minima differ by more than 1%"] = {
    "pairs": mp_pairs, **{k: {"count": len(v), "examples": v[:4]} for k, v in dis.items()}}
# R5
rng = np.random.default_rng(11); w1 = 0.0; w2 = 0.0; worst_ratio = 1e9
for _ in range(2000):
    a3 = complex(*rng.normal(size=2)); h = rng.normal(size=3) + 1j * rng.normal(size=3); h /= np.linalg.norm(h)
    Y = closed(np.concatenate([[0], a3 * F3]), h); s = np.linalg.svd(Y, compute_uv=False)
    w1 = max(w1, abs(s[0] * s[1] - abs(a3) ** 2 * abs(h @ h)) / (abs(a3) ** 2))
    fro = abs(a3) ** 2 * (4 * abs(np.vdot(F3, h)) ** 2 + 2 * abs(np.vdot(F2, h)) ** 2 + abs(np.vdot(F1, h)) ** 2)
    w2 = max(w2, abs(np.sum(np.abs(Y) ** 2) - fro) / abs(a3) ** 2)
    worst_ratio = min(worst_ratio, (s[1] / s[0]) / (abs(h @ h) / 4) if abs(h @ h) > 1e-12 else 1e9)
OUT["R5 idealised up channel (u = a3 n, w = 0), 2 000 random unit h: |m2 m3 - |a3|^2 |h.h|| / |a3|^2, Frobenius identity error, min of (m2/m3) / (|h.h|/4)"] = [w1, w2, worst_ratio]
dev = {}
for p, (k, re_t, im_t) in enumerate(tasks):
    order = 5 if k % 2 == 0 else 10
    for ih in range(2):
        w, u = U[p, 0, ih, 0], U[p, 0, ih, 1:]; nu = np.linalg.norm(u)
        key = f"order {order}, {band(im_t)}"
        dev.setdefault(key, []).append([abs(u @ u) / nu ** 2, abs(w) / nu, abs(np.vdot(F2, u)) / nu, abs(np.vdot(F1, u)) / nu])
OUT["R5 the stored up channels: medians (max) of |u.u|/|u|^2, |w|/|u|, |a2|/|u|, |a1|/|u|"] = {
    k: {"median": np.median(np.array(v), axis=0).round(4).tolist(), "max": np.max(np.array(v), axis=0).round(4).tolist()} for k, v in sorted(dev.items())}
# R6
signs = [np.array([s0, s1, s2, s3]) for s0 in (1, -1) for s1 in (1, -1) for s2 in (1, -1) for s3 in (1, -1)]
r6 = {"order 5": {}, "order 10": {}}
for p, (k, re_t, im_t) in enumerate(tasks):
    order = "order 5" if k % 2 == 0 else "order 10"
    for ih in range(2):
        dn, lp = U[p, 1, ih], U[p, 2, ih]
        for sg in signs:
            e = float(np.max(np.abs(lp - sg * dn)) / np.max(np.abs(dn)))
            key = str(sg.tolist()); r6[order][key] = max(r6[order].get(key, 0.0), e)
OUT["R6 max over rows of |lep - sign * down| / |down| for each sign pattern on (u_1, u_i, u_j, u_k); the best three"] = {
    o: sorted(v.items(), key=lambda kv: kv[1])[:3] for o, v in r6.items()}
# R7
th = HERE.parent / "chat1_2026-10-23_two_higgs"
X = np.load(th / "two_higgs.npz")["data"].astype(np.float64); TI = json.loads((th / "two_higgs_index.json").read_text())
mi = {m: i for i, m in enumerate(TI["models"])}
P_BLOCK = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
wr = wv = 0.0
for p in range(len(tasks)):
    f6, f22, dr = H[p, DIRS.index("F_6")], H[p, DIRS.index("F_22")], H[p, DIRS.index("dR")]
    for ih, hor in enumerate(hors):
        for model, (hu, hd) in (("F_6 | F_22", (f6, f22)), ("dR split (up S~)", (np.conj(dr), dr))):
            Yu, Yd, Ye = closed(U[p, 0, ih], hu), closed(U[p, 1, ih], hd), closed(U[p, 2, ih], hd)
            f = []
            for Y in (Yu, Yd, Ye):
                s = np.linalg.svd(Y, compute_uv=False); f += [math.log10(s[1] / s[0]), math.log10(s[2] / s[0])]
            Uu = np.linalg.svd(P_BLOCK @ Yu @ P_BLOCK.T)[0][:, ::-1]; Ud = np.linalg.svd(P_BLOCK @ Yd @ P_BLOCK.T)[0][:, ::-1]
            V = np.abs(np.conj(Uu.T) @ Ud)
            ref = X[p, TI["hors"].index(hor), mi[model]]
            wr = max(wr, float(np.max(np.abs(np.array(f) - ref[:6]))))
            for x, y in zip((V[0, 1], V[1, 2], V[0, 2]), ref[6:9]):
                if x > 1e-9 and y > 1e-9:
                    wv = max(wv, abs(math.log(x / y)))
OUT["R7 channel_store C2 on every point: max |delta log10 ratio|, max |delta ln |V||"] = [wr, wv]
# R8
r8 = {}
for r in D["rows"]:
    rr = r["r = exp(-pi Im tau)"]; a = r["A2"]
    if a["min chi2_nine"] >= 21.67:
        continue
    r8.setdefault(r["hor"], []).append([a["h_d"]["delta = e1 / leading"] / rr ** 0.5, a["h_d"]["epsilon = other null / leading"] / rr,
                                        a["h_u"]["delta = e1 / leading"] / rr ** 0.5, a["h_u"]["epsilon = other null / leading"] / rr, r["point"][2]])
OUT["R8 A2 optima below 21.67 by horocycle: count, Im tau range, medians of delta_d/r^.5, eps_d/r, delta_u/r^.5, eps_u/r (DR: 5.657, 20)"] = {
    h: {"rows": len(v), "Im tau": [min(x[4] for x in v), max(x[4] for x in v)], "medians": np.median(np.array(v)[:, :4], axis=0).round(2).tolist(),
        "delta_d over DR's": round(float(np.median(np.array(v)[:, 0])) / 5.657, 2)} for h, v in r8.items()}
(HERE / "revision_checks.json").write_text(json.dumps(OUT, indent=1, default=str) + "\n")
print("written")
