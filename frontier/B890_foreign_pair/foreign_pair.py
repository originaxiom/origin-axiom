#!/usr/bin/env python3
"""B890 -- the sealed cell: are the two foreign vacuum lines' profiles equal or distinct?
Method fixed by the sealed prereg (ea66fc34...)."""
import json
import os

import mpmath
from mpmath import mp

HERE = os.path.dirname(os.path.abspath(__file__))
B883 = os.path.normpath(os.path.join(HERE, "..", "B883_the_27"))
B884 = os.path.normpath(os.path.join(HERE, "..", "B884_yukawa_support"))
B854 = os.path.normpath(os.path.join(HERE, "..", "B854_centralizer_exact",
                                     "e6_centralizer.py"))
CUBIC = [500716339200, -159667200, -28224, 1]
mp.dps = 30
REPJ = json.load(open(os.path.join(B883, "rep27.json")))
REP = {int(k): v for k, v in REPJ["rep"].items()}
g6 = {"__file__": B854, "__name__": "b854"}
exec(compile(open(B854).read(), B854, "exec"), g6)
inv8 = [mp.mpf(c.numerator) / mp.mpf(c.denominator) for c in g6["INV"][8]]
inv16 = [mp.mpf(c.numerator) / mp.mpf(c.denominator) for c in g6["INV"][16]]
roots_t = sorted(13 * mp.re(r) for r in mpmath.polyroots(
    [mp.mpf(c) for c in CUBIC], maxsteps=200, extraprec=120))


def rho_num(vec):
    M = mp.zeros(27, 27)
    for p in range(78):
        c = vec[p]
        if abs(c) < mp.mpf("1e-28"):
            continue
        Rp = REP[p]
        for i in range(27):
            for j in range(27):
                if Rp[i][j]:
                    M[i, j] += c * Rp[i][j]
    return M


R8, R16 = rho_num(inv8), rho_num(inv16)
# canonical vacuum lines: 1-dim joint eigenspaces (as in B889)
Mmix = R8 + mp.mpf("0.37217") * R16
Mc = mp.matrix(27, 27)
for i in range(27):
    for j in range(27):
        Mc[i, j] = mp.mpc(Mmix[i, j])
E2, ER2 = mpmath.eig(Mc, left=False, right=True)
sts = []
for i in range(27):
    v = mp.matrix([ER2[j, i] for j in range(27)])
    v = v * (1 / mp.sqrt(sum(abs(v[j]) ** 2 for j in range(27))))
    c8 = sum((R8 * v)[j] * mp.conj(v[j]) for j in range(27))
    c16 = sum((R16 * v)[j] * mp.conj(v[j]) for j in range(27))
    sts.append(((c8, c16), v))
blocks = []
for chs, v in sts:
    for grp in blocks:
        if abs(chs[0] - grp["chs"][0]) < mp.mpf("1e-8") and \
           abs(chs[1] - grp["chs"][1]) < mp.mpf("1e-8"):
            grp["vecs"].append(v)
            break
    else:
        blocks.append(dict(chs=chs, vecs=[v]))
vlines = [g for g in blocks if len(g["vecs"]) == 1]
assert len(vlines) == 3
# frame of each line: mult-1 eigenvalue of rho(s_i)
def frame_of(v):
    for ri, t in enumerate(roots_t):
        Rs = R8 + t * R16
        ev = sum((Rs * v)[j] * mp.conj(v[j]) for j in range(27))
        M = mp.matrix(27, 27)
        for i in range(27):
            for j in range(27):
                M[i, j] = mp.mpc(Rs[i, j])
        Ee = mpmath.eig(M, left=False, right=False)
        if sum(1 for k in range(27) if abs(Ee[k] - ev) < mp.mpf("1e-9")) == 1:
            return ri
    return None
vf = [frame_of(g["vecs"][0]) for g in vlines]
print(f"vacuum lines -> frames: {vf}")

res = dict(frames={})
for ri in range(3):
    lv = json.load(open(os.path.join(B884, f"levi_charges_r{ri}.json")))
    y = [mp.mpc(mp.mpf(v[0]), mp.mpf(v[1])) for v in lv["y"]]
    y2 = [mp.mpc(mp.mpf(v[0]), mp.mpf(v[1])) for v in lv["y2"]]
    s1 = [inv8[p] + roots_t[ri] * inv16[p] for p in range(78)]
    Rs1, Ry, Ry2 = rho_num(s1), rho_num(y), rho_num(y2)
    Mx = Rs1 + Ry * mp.mpf("0.70710678118") + Ry2 * mp.mpf("0.31622776601")
    Mc2 = mp.matrix(27, 27)
    for i in range(27):
        for j in range(27):
            Mc2[i, j] = mp.mpc(Mx[i, j])
    E3, ER3 = mpmath.eig(Mc2, left=False, right=True)
    sts2 = []
    for i in range(27):
        v = mp.matrix([ER3[j, i] for j in range(27)])
        v = v * (1 / mp.sqrt(sum(abs(v[j]) ** 2 for j in range(27))))
        chs = []
        for Rz in (Rs1, Ry, Ry2):
            img = Rz * v
            chs.append(sum(img[j] * mp.conj(v[j]) for j in range(27)))
        sts2.append((chs, v))
    pieces = []
    for chs, v in sts2:
        for grp in pieces:
            if all(abs(chs[k] - grp["chs"][k]) < mp.mpf("1e-8") for k in range(3)):
                grp["vecs"].append(v)
                break
        else:
            pieces.append(dict(chs=chs, vecs=[v]))
    # canonical piece order per the prereg: (dim, Re y-charge)
    pieces.sort(key=lambda g: (len(g["vecs"]), float(mp.re(g["chs"][1]))))
    allp, owner = [], []
    for pi, g in enumerate(pieces):
        for v in g["vecs"]:
            allp.append(v)
            owner.append(pi)
    B = mp.matrix(27, len(allp))
    for j, v in enumerate(allp):
        for i in range(27):
            B[i, j] = v[i]
    BH = mp.matrix(len(allp), 27)
    for i in range(len(allp)):
        for j in range(27):
            BH[i, j] = mp.conj(B[j, i])
    G = BH * B
    profs = []
    for li, g in enumerate(vlines):
        if vf[li] == ri:
            continue
        v = g["vecs"][0]
        xsol = mp.lu_solve(G, BH * v)
        mass = [mp.mpf(0)] * 12
        for j in range(len(allp)):
            mass[owner[j]] += abs(xsol[j]) ** 2
        tot = sum(mass)
        profs.append((vf[li], [m / tot for m in mass]))
    (fa, pa), (fb, pb) = profs
    devs = [abs(pa[k] - pb[k]) for k in range(12)]
    mx = max(devs)
    verdict = "EQUAL" if mx < mp.mpf("1e-9") else \
              ("UNSTABLE" if mx < mp.mpf("1e-6") else "DISTINCT")
    res["frames"][str(ri)] = dict(
        foreign=(fa, fb),
        profile_a=[mp.nstr(m, 8) for m in pa],
        profile_b=[mp.nstr(m, 8) for m in pb],
        max_dev=mp.nstr(mx, 4), verdict=verdict)
    print(f"frame {ri}: foreign pair {fa},{fb}  max profile deviation {mp.nstr(mx, 4)}  -> {verdict}")

vs = [res["frames"][str(ri)]["verdict"] for ri in range(3)]
res["overall"] = ("EQUAL" if all(v == "EQUAL" for v in vs)
                  else "DISTINCT" if any(v == "DISTINCT" for v in vs)
                  else "UNSTABLE")
json.dump(res, open(os.path.join(HERE, "results.json"), "w"), indent=1,
          sort_keys=True, default=str)
print(f"OVERALL: {res['overall']}")
