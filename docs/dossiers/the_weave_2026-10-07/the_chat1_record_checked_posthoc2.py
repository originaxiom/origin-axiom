"""W86, POST HOC 2 (labelled; written after the auditors' reports on chat1's selection and meditation folders, committed
before its one run). The two A-grade findings so far, re-checked on this seat's own code.

  A1  chat1's self-coupling scan (meditation, post_hoc_self_coupling.py) carries B517's coupling [[W, C], [D, W]] to a
      thread W with C = c0 I + c1 W, D = d0 I + d1 W and c0, c1, d0, d1 in {0..3}: nonnegative COEFFICIENTS in the basis
      {I, W}. Its docstring, and B517's theorem ("coupled by nonneg-integral F-equivariant maps"), say nonnegative
      ENTRIES. The meditation's fork (self-reference admits every thread to length 8 except the root) rests on the scan.
      Re-checked for F (control) and every Lyndon word of length 2..8 (70 matrices), C and D never 0 or I:
        A1a  chat1's convention: the irreducible Pisot hits per word;
        A1b  nonnegative entries, C = c0 I + c1 W with c0 in {-3..3}, c1 in {0..3} (D alike): the hits per word, and the
             hits that also meet B517's other conditions (T primitive: some power T^k, k <= 10, has every entry > 0;
             unimodular: det T = +-1);
        A1c  the root in B517's own basis {I, F'}, F' = LR - I (F'^2 = LR): C = a I + b F', D = c I + d F', a..d in
             {0..3}: the hits; and the coupling (F', F'^2) itself: its matrix, nonnegativity, primitivity, det,
             characteristic polynomial, irreducibility over Q, Pisot property and root moduli.
      'Pisot': exactly one root of modulus > 1, real and > 1, every other root of modulus < 1. The roots are taken in
      closed form at 50 digits (C, D and W commute, so on W's eigenline for lambda the roots are lambda +- sqrt(gamma
      delta), gamma and delta the eigenvalues of C and D there); for every hit they are checked against the exact
      characteristic polynomial's roots (mpmath polyroots), and irreducibility is decided exactly (sympy factor_list).
      A1a's counts are compared word by word with chat1's banked S3 counts (post_hoc_self_coupling.json at 9fbab9f5e).
      A1 holds (the auditor's A finding confirmed) if A1a reproduces chat1 (no hit at LR, a hit at every other word),
      every word including LR has an A1b hit, and (F', F'^2) meets all four of B517's conditions (nonnegative entries,
      primitive, unimodular, irreducible Pisot).
  A2  chat1's reading "the 2-3 hierarchy is carried by K, the normalisation, not by Y" (FINDINGS_THREAD_FRAME.md,
      corrections, item 1) rests on the hybrid: W72's Y, normalised by each thread's own K, gives the thread's m2/m3
      within x0.90 to x1.02. Re-checked on the 12 threads of chat1's sealed test (the Lyndon words of length 2..5), with
      W84's instrument (the_thread_frame_checked.py: Forms, cycle, masses; 60 digits; N = 256 nodes):
        A2a  the normalised residual of each thread's own Y against its best complex multiple of W72's Y
             (the_surface_yukawa.json, X4, "Y (Y0 = 2.0)"): min over lambda of |Y_w - lambda Y72| / |Y_w|, Frobenius;
        A2b  with the thread's own K fixed, 256 random complex symmetric Y (independent standard complex Gaussian
             entries on and above the diagonal; numpy default_rng(86); the same 256 at every thread): the median m2/m3
             against the thread's own; the same with 256 real symmetric Y (standard Gaussian);
        A2c  the trend: the decades by which m2/m3 falls from LR to LLLLR, own against the complex median;
        A2d  W72's six independent entries each scaled by exp(u), u uniform in [-ln 2, ln 2], 256 draws (the same
             generator, after A2b's draws): the least and greatest m2/m3 against the hybrid's, per thread;
        controls: the own ln m2/m3 and ln m1/m3 at N = 256 against W84's values at N = 512 (five threads; |d ln|
             below 1e-8), and against chat1's banked thread_frame.json (twelve threads; below 1e-5); this seat's hybrid
             against chat1's post_hoc_hybrid.json (twelve threads; below 1e-5). chat1's files are read at 9fbab9f5e.
      A2 holds (the auditor's A finding confirmed: the hybrid cannot detect a dependence on Y, and Y's shape sets the
      level) if A2a's residual is below 0.1 on all 12 threads and A2b's complex median lies outside [1/2, 2] times the
      thread's own m2/m3 on all 12. What survives of chat1's reading is read from A2c: K carries the trend if the
      complex median falls by at least half of the own decades.

Run: python3 the_chat1_record_checked_posthoc2.py  ->  the_chat1_record_checked_posthoc2.json beside it.
"""
import itertools
import json
import math
import subprocess
import sys
import time
from pathlib import Path

import mpmath as mp
import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_thread_frame_checked as TF  # noqa: E402  (Forms, cycle, masses)

OUT = HERE / "the_chat1_record_checked_posthoc2.json"
CHAT1 = "9fbab9f5e"
x = sp.symbols("x")
L = sp.Matrix([[1, 0], [1, 1]])
R = sp.Matrix([[1, 1], [0, 1]])
I2 = sp.eye(2)
Z2 = sp.zeros(2)


def lyndon(n, m=2):
    return [w for k in range(m, n + 1) for w in ("".join(p) for p in itertools.product("LR", repeat=k))
            if all(w < w[i:] + w[:i] for i in range(1, len(w)))]


def mat(w):
    M = sp.eye(2)
    for ch in w:
        M = M * (L if ch == "L" else R)
    return M


def chat1_json(folder, name):
    top = subprocess.run(["git", "rev-parse", "--show-toplevel"], cwd=HERE, capture_output=True, check=True,
                         text=True).stdout.strip()
    return json.loads(subprocess.run(["git", "show", f"{CHAT1}:relays/{folder}/{name}"], cwd=top,
                                     capture_output=True, check=True, text=True).stdout)


# ---------------------------------------------------------------- A1
def eig2(W):
    t, dt = int(W.trace()), int(W.det())
    s = mp.sqrt(mp.mpf(t * t - 4 * dt))
    return [(t + s) / 2, (t - s) / 2]


def closed_roots(lams, Cc, Dc):
    """Cc, Dc = (k0, k1, shift): the element k0 I + k1 (W - shift I); roots lambda +- sqrt(gamma delta)"""
    out = []
    for lam in lams:
        g = Cc[0] + Cc[1] * (lam - Cc[2])
        d = Dc[0] + Dc[1] * (lam - Dc[2])
        r = mp.sqrt(mp.mpc(g * d))
        out += [lam + r, lam - r]
    return out


def is_pisot(roots):
    big = [z for z in roots if abs(z) > 1]
    if len(big) != 1 or abs(mp.im(big[0])) > mp.mpf(10) ** -40 or mp.re(big[0]) <= 1:
        return False
    return all(abs(z) < 1 - mp.mpf(10) ** -40 for z in roots if z is not big[0])


def exact(W, C, D, roots):
    T = sp.Matrix(sp.BlockMatrix([[W, C], [D, W]]))
    p = sp.Poly(T.charpoly(x).as_expr(), x)
    fl = sp.factor_list(p.as_expr())[1]
    irr = len(fl) == 1 and fl[0][1] == 1 and sp.degree(fl[0][0], x) == 4
    dev = None                                            # roots compared only when p is irreducible (so separable)
    if irr:
        pr = mp.polyroots([int(c) for c in p.all_coeffs()], maxsteps=400, extraprec=200)
        dev = float(max(min(abs(z - q) for q in pr) for z in roots))
    nonneg = all(v >= 0 for v in T)
    P, prim = sp.eye(4), False
    for _ in range(10):
        P = P * T
        if all(v > 0 for v in P):
            prim = True
            break
    return {"irreducible": bool(irr), "det": int(T.det()), "nonnegative": bool(nonneg),
            "primitive": bool(prim and nonneg), "charpoly": str(p.as_expr()),
            "closed-form roots against polyroots": dev, "T": T}


def scan(W, box0, box1, shift, need_nonneg):
    lams = eig2(W)
    elems = []
    for k1 in box1:
        for k0 in box0:
            M = k0 * I2 + k1 * (W - shift * I2)
            if M in (Z2, I2) or (need_nonneg and min(M) < 0):
                continue
            elems.append(((k0, k1), M))
    hits = []
    for (cc, C), (dd, D) in itertools.product(elems, repeat=2):
        roots = closed_roots(lams, (cc[0], cc[1], shift), (dd[0], dd[1], shift))
        if not is_pisot(roots):
            continue
        e = exact(W, C, D, roots)
        if e["irreducible"]:
            hits.append({"C": list(cc), "D": list(dd), "unimodular": abs(e["det"]) == 1, "primitive": e["primitive"],
                         "all of B517's conditions": bool(abs(e["det"]) == 1 and e["primitive"] and e["nonnegative"]),
                         "charpoly": e["charpoly"], "dev": e["closed-form roots against polyroots"]})
    return len(elems), hits


def a1():
    mp.mp.dps = 50
    words = {"F (control)": sp.Matrix([[1, 1], [1, 0]])}
    for w in lyndon(8):
        words[w] = mat(w)
    rows, worst = {}, 0.0
    for name, W in words.items():
        n_a, h_a = scan(W, range(4), range(4), 0, False)
        n_b, h_b = scan(W, range(-3, 4), range(4), 0, True)
        worst = max([worst] + [h["dev"] for h in h_a + h_b])
        rows[name] = {"trace": int(W.trace()), "A1a hits (chat1's convention)": len(h_a),
                      "A1b elements with nonnegative entries": n_b, "A1b hits (nonnegative entries)": len(h_b),
                      "A1b hits meeting all of B517's conditions": sum(h["all of B517's conditions"] for h in h_b),
                      "A1b hits, first four": [[h["C"], h["D"], h["unimodular"], h["primitive"]] for h in h_b[:4]]}
    W = words["LR"]
    n_c, h_c = scan(W, range(4), range(4), 1, True)
    Fp = W - I2
    roots = closed_roots(eig2(W), (0, 1, 1), (1, 1, 1))
    e = exact(W, Fp, Fp * Fp, roots)
    worst = max([worst] + [h["dev"] for h in h_c]
                + ([e["closed-form roots against polyroots"]] if e["irreducible"] else []))
    other = [n for n in words if n != "LR"]
    s3 = chat1_json("chat1_2026-10-14_meditation", "post_hoc_self_coupling.json")["rows"]
    mism = [n for n in words if rows[n]["A1a hits (chat1's convention)"] != s3[n]["S3 scan hits"]]
    out = {"words": len(words),
           "A1a": {"hits at LR": rows["LR"]["A1a hits (chat1's convention)"],
                   "every other word has a hit": all(rows[n]["A1a hits (chat1's convention)"] > 0 for n in other),
                   "words with no hit": [n for n in words if rows[n]["A1a hits (chat1's convention)"] == 0],
                   "hit counts equal chat1's S3 counts on every word": not mism, "words where they differ": mism},
           "A1b": {"every word has a hit": all(r["A1b hits (nonnegative entries)"] > 0 for r in rows.values()),
                   "every word has a hit meeting all of B517's conditions":
                       all(r["A1b hits meeting all of B517's conditions"] > 0 for r in rows.values()),
                   "words with no hit": [n for n, r in rows.items() if r["A1b hits (nonnegative entries)"] == 0],
                   "hits at LR": rows["LR"]["A1b hits (nonnegative entries)"],
                   "hits at LR meeting all of B517's conditions":
                       rows["LR"]["A1b hits meeting all of B517's conditions"]},
           "A1c": {"F' squared is LR": bool(Fp * Fp == W), "F' squared is F' + I": bool(Fp * Fp == Fp + I2),
                   "elements": n_c, "hits": len(h_c),
                   "hits (a, b, c, d; unimodular; primitive)": [h["C"] + h["D"] + [h["unimodular"], h["primitive"]]
                                                                for h in h_c],
                   "(F', F'^2)": {"T": [[int(v) for v in e["T"].row(i)] for i in range(4)],
                                  "nonnegative": e["nonnegative"], "primitive": e["primitive"], "det": e["det"],
                                  "charpoly": e["charpoly"], "irreducible": e["irreducible"], "Pisot": is_pisot(roots),
                                  "root moduli": sorted((float(abs(z)) for z in roots), reverse=True)}},
           "closed-form roots against the characteristic polynomial's, worst over every hit": worst,
           "per word": rows}
    pc = out["A1c"]["(F', F'^2)"]
    out["A1 holds"] = bool(out["A1a"]["hits at LR"] == 0 and out["A1a"]["every other word has a hit"]
                           and out["A1b"]["every word has a hit"]
                           and pc["nonnegative"] and pc["primitive"] and abs(pc["det"]) == 1 and pc["irreducible"]
                           and pc["Pisot"])
    return out


# ---------------------------------------------------------------- A2


def frob(A):
    return mp.sqrt(sum(abs(A[i][j]) ** 2 for i in range(3) for j in range(3)))


def sym(v, cplx):
    """six independent entries (00, 01, 02, 11, 12, 22) -> a symmetric 3x3 of mp numbers"""
    idx = [(0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2)]
    Y = [[mp.mpc(0)] * 3 for _ in range(3)]
    for k, (i, j) in enumerate(idx):
        z = mp.mpc(float(v[k].real), float(v[k].imag)) if cplx else mp.mpc(float(v[k]), 0)
        Y[i][j] = z
        Y[j][i] = z
    return Y


def ratio(K, Y):
    return mp.e ** TF.masses(K, Y)["ln m2/m3"]


def a2(t0):
    forms = TF.Forms()                                    # sets mp.mp.dps = 60
    banked = json.loads((HERE / "the_surface_yukawa.json").read_text(encoding="utf-8"))["X4"]["Y (Y0 = 2.0)"]
    Y72 = [[mp.mpc(z[0], z[1]) for z in row] for row in banked]
    w84 = json.loads((HERE / "the_thread_frame_checked.json").read_text(encoding="utf-8"))["V1"]["threads"]
    c1_own = chat1_json("chat1_2026-10-14_selection", "thread_frame.json")["readouts"]["per thread"]
    c1_hyb = chat1_json("chat1_2026-10-14_selection", "post_hoc_hybrid.json")["per thread"]
    rng = np.random.default_rng(86)
    n = 256
    rc = [rng.standard_normal(6) + 1j * rng.standard_normal(6) for _ in range(n)]
    rr = [rng.standard_normal(6) for _ in range(n)]
    ru = [np.exp(rng.uniform(-math.log(2), math.log(2), 6)) for _ in range(n)]
    Yc = [sym(v, True) for v in rc]
    Yr = [sym(v, False) for v in rr]
    idx = [(0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2)]
    Yp = []
    for f in ru:
        Y = [[mp.mpc(0)] * 3 for _ in range(3)]
        for k, (i, j) in enumerate(idx):
            Y[i][j] = Y72[i][j] * mp.mpf(float(f[k]))
            Y[j][i] = Y[i][j]
        Yp.append(Y)
    per, ctl = {}, {"against W84 (N = 512)": 0.0, "against chat1's thread_frame": 0.0, "against chat1's hybrid": 0.0}
    for w in lyndon(5):
        r = TF.cycle(forms, w, 256)
        K, Y = r["K"], r["Y"]
        own = TF.masses(K, Y)
        o2, o1 = own["ln m2/m3"], own["ln m1/m3"]
        hyb = TF.masses(K, Y72)
        lam = sum(mp.conj(Y72[i][j]) * Y[i][j] for i in range(3) for j in range(3)) / frob(Y72) ** 2
        res = frob([[Y[i][j] - lam * Y72[i][j] for j in range(3)] for i in range(3)]) / frob(Y)
        qc = sorted(float(ratio(K, Z)) for Z in Yc)
        qr = sorted(float(ratio(K, Z)) for Z in Yr)
        qp = sorted(float(ratio(K, Z)) for Z in Yp)
        own2, hyb2 = float(mp.e ** o2), float(mp.e ** hyb["ln m2/m3"])
        med_c, med_r = float(np.median(qc)), float(np.median(qr))
        per[w] = {"sampled y_max": float(r["sampled y_max"]), "own m2/m3": own2, "own m1/m3": float(mp.e ** o1),
                  "hybrid m2/m3": hyb2, "hybrid / own": hyb2 / own2,
                  "A2a residual of Y against its best multiple of W72's Y": float(res), "|lambda|": float(abs(lam)),
                  "A2b complex: median m2/m3": med_c, "A2b complex: 5% and 95%": [qc[12], qc[243]],
                  "A2b complex: median / own": med_c / own2,
                  "A2b real: median m2/m3": med_r, "A2b real: median / own": med_r / own2,
                  "A2d W72 scaled: least and greatest m2/m3 / hybrid": [qp[0] / hyb2, qp[-1] / hyb2]}
        if w in w84:
            ctl["against W84 (N = 512)"] = max(ctl["against W84 (N = 512)"],
                                               abs(float(o2) - math.log(w84[w]["m2/m3"])),
                                               abs(float(o1) - math.log(w84[w]["m1/m3"])))
        ctl["against chat1's thread_frame"] = max(ctl["against chat1's thread_frame"],
                                                  abs(float(o2) - math.log(c1_own[w]["m2/m3"])),
                                                  abs(float(o1) - math.log(c1_own[w]["m1/m3"])))
        ctl["against chat1's hybrid"] = max(ctl["against chat1's hybrid"],
                                            abs(float(hyb["ln m2/m3"]) - math.log(c1_hyb[w]["hybrid m2/m3"])))
        print(w, {k: per[w][k] for k in ("own m2/m3", "hybrid / own",
                                         "A2a residual of Y against its best multiple of W72's Y",
                                         "A2b complex: median / own")}, round(time.time() - t0, 1), flush=True)
    res = [v["A2a residual of Y against its best multiple of W72's Y"] for v in per.values()]
    medc = [v["A2b complex: median / own"] for v in per.values()]
    medr = [v["A2b real: median / own"] for v in per.values()]
    hy = [v["hybrid / own"] for v in per.values()]
    pr = [q for v in per.values() for q in v["A2d W72 scaled: least and greatest m2/m3 / hybrid"]]
    own_dec = math.log10(per["LR"]["own m2/m3"] / per["LLLLR"]["own m2/m3"])
    med_dec = math.log10(per["LR"]["A2b complex: median m2/m3"] / per["LLLLR"]["A2b complex: median m2/m3"])
    out = {"per thread": per,
           "controls (largest |d ln|)": ctl,
           "controls hold": bool(ctl["against W84 (N = 512)"] < 1e-8 and ctl["against chat1's thread_frame"] < 1e-5
                                 and ctl["against chat1's hybrid"] < 1e-5),
           "hybrid / own, range": [min(hy), max(hy)],
           "A2a residual, range": [min(res), max(res)],
           "A2b complex median / own, range": [min(medc), max(medc)],
           "A2b real median / own, range": [min(medr), max(medr)],
           "A2c decades from LR to LLLLR": {"own": own_dec, "complex median": med_dec},
           "A2c K carries the trend (median falls by at least half the own decades)": bool(med_dec >= own_dec / 2),
           "A2d W72 scaled, range against the hybrid": [min(pr), max(pr)]}
    out["A2 holds"] = bool(max(res) < 0.1 and all(m < 0.5 or m > 2 for m in medc))
    return out


def main():
    t0 = time.time()
    out = {"status": "W86 post hoc 2 (labelled): the auditors' A-grade findings A1 (the self-coupling convention) and "
                     "A2 (the hierarchy 'carried by K, not by Y') re-checked on this seat's own code"}
    out["A1"] = a1()
    print("A1", {k: out["A1"][k] for k in ("A1a", "A1b", "A1 holds")}, round(time.time() - t0, 1), flush=True)
    out["A2"] = a2(t0)
    out["cells"] = {"A1": out["A1"]["A1 holds"], "A2": out["A2"]["A2 holds"]}
    out["seconds"] = round(time.time() - t0, 1)
    OUT.write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
    print("written", OUT.name, out["cells"], out["seconds"])


if __name__ == "__main__":
    main()
