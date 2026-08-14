#!/usr/bin/env python3
"""B891 -- the sealed matter-extension cell (prereg a08398c5...): are the two
foreign 16-subspaces' profiles equal or distinct within each frame?"""
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

def sixteen_of(ri):
    """the mult-16 eigenspace of rho(s_ri)."""
    Rs = R8 + roots_t[ri] * R16
    M = mp.matrix(27, 27)
    for i in range(27):
        for j in range(27):
            M[i, j] = mp.mpc(Rs[i, j])
    Ee, ERe = mpmath.eig(M, left=False, right=True)
    # cluster eigenvalues, find the multiplicity-16 one
    groups = {}
    for k in range(27):
        key = None
        for g in groups:
            if abs(Ee[k] - g) < mp.mpf("1e-9"):
                key = g
                break
        groups.setdefault(key if key is not None else Ee[k], []).append(k)
    m16 = [idx for g, idx in groups.items() if len(idx) == 16][0]
    vecs = []
    for k in m16:
        v = mp.matrix([ERe[j, k] for j in range(27)])
        v = v * (1 / mp.sqrt(sum(abs(v[j]) ** 2 for j in range(27))))
        vecs.append(v)
    return vecs


S16 = {ri: sixteen_of(ri) for ri in range(3)}
print("foreign 16s extracted:", [len(S16[r]) for r in range(3)])

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
    for rj in range(3):
        if rj == ri:
            continue
        mass = [mp.mpf(0)] * 12
        for v in S16[rj]:
            xsol = mp.lu_solve(G, BH * v)
            for j in range(len(allp)):
                mass[owner[j]] += abs(xsol[j]) ** 2
        tot = sum(mass)
        profs.append((rj, [m / tot for m in mass]))
    (fa, pa), (fb, pb) = profs
    devs = [abs(pa[k] - pb[k]) for k in range(12)]
    mx = max(devs)
    verdict = "EQUAL" if mx < mp.mpf("1e-9") else \
              ("UNSTABLE" if mx < mp.mpf("1e-6") else "DISTINCT")
    res["frames"][str(ri)] = dict(foreign=(fa, fb),
                                  profile_a=[mp.nstr(m, 8) for m in pa],
                                  profile_b=[mp.nstr(m, 8) for m in pb],
                                  max_dev=mp.nstr(mx, 4), verdict=verdict)
    print(f"frame {ri}: foreign 16s {fa},{fb}  max dev {mp.nstr(mx, 4)}  -> {verdict}")

vs = [res["frames"][str(ri)]["verdict"] for ri in range(3)]
res["overall"] = ("DISTINCT" if all(v == "DISTINCT" for v in vs)
                  else "EQUAL" if any(v == "EQUAL" for v in vs) else "UNSTABLE")
json.dump(res, open(os.path.join(HERE, "results.json"), "w"), indent=1,
          sort_keys=True, default=str)
print(f"OVERALL: {res['overall']}")
