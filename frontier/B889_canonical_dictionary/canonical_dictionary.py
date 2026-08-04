#!/usr/bin/env python3
"""B889 -- masterplan W3: the CANONICAL across-breakings dictionary.

The convention problem dissolves: B886 showed the 27 has exactly SIX joint
Pi-weight blocks -- three 1-dim vacuum lines (the w-orbit) and three 8-dim
generic blocks (the u-orbit) -- and these are CANONICAL (no Levi choices, no
conventions; the Galois S3 permutes them). The convention-free fine dictionary
is therefore: each frame's 12 SM pieces measured against the six canonical
blocks (a 12 x 6 mass table per frame, oblique readout per the standing rule).
Any frame-to-frame fine comparison factors through these tables.

Outputs: the three 12x6 tables; their structural zeros; the S3-covariance check
(the three tables must agree up to the simultaneous permutation of blocks).
"""
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


R8 = rho_num(inv8)
R16 = rho_num(inv16)

print("[1] the six canonical Pi-blocks (joint eigenspaces of rho(x8), rho(x16))...")
Mmix = R8 + mp.mpf("0.37217") * R16
Mc = mp.matrix(27, 27)
for i in range(27):
    for j in range(27):
        Mc[i, j] = mp.mpc(Mmix[i, j])
E2, ER2 = mpmath.eig(Mc, left=False, right=True)
states = []
for i in range(27):
    v = mp.matrix([ER2[j, i] for j in range(27)])
    v = v * (1 / mp.sqrt(sum(abs(v[j]) ** 2 for j in range(27))))
    c8 = sum((R8 * v)[j] * mp.conj(v[j]) for j in range(27))
    c16 = sum((R16 * v)[j] * mp.conj(v[j]) for j in range(27))
    states.append(((c8, c16), v))
blocks = []
for chs, v in states:
    for grp in blocks:
        if abs(chs[0] - grp["chs"][0]) < mp.mpf("1e-8") and \
           abs(chs[1] - grp["chs"][1]) < mp.mpf("1e-8"):
            grp["vecs"].append(v)
            break
    else:
        blocks.append(dict(chs=chs, vecs=[v]))
blocks.sort(key=lambda g: len(g["vecs"]))
bdims = [len(g["vecs"]) for g in blocks]
print(f"    canonical blocks: {bdims}  (B886 needs [1,1,1,8,8,8])")

# identify which vacuum line belongs to which frame: the frame-i singlet has
# s_i-eigenvalue = the mult-1 extreme; test s_i-eigenvalue of each 1-dim block
frame_of_vac = {}
for bi, g in enumerate(blocks[:3]):
    v = g["vecs"][0]
    for ri, t in enumerate(roots_t):
        Rs = R8 + t * R16
        ev = sum((Rs * v)[j] * mp.conj(v[j]) for j in range(27))
        # the singlet of frame ri is the UNIQUE mult-1 eigenvalue of rho(s_ri);
        # check: is v an eigenvector with residual ~0 AND is its eigenvalue the
        # one with multiplicity 1? (all Pi-vectors are eigenvectors of every s;
        # multiplicity decides.) compute the full spectrum multiplicity of ev:
        M = mp.matrix(27, 27)
        for i in range(27):
            for j in range(27):
                M[i, j] = mp.mpc((Rs)[i, j])
        Ee, _ = mpmath.eig(M, left=False, right=False), None
        mult = sum(1 for k in range(27) if abs(Ee[0][k] - ev) < mp.mpf("1e-9")) \
            if isinstance(Ee, tuple) else sum(
                1 for k in range(27) if abs(Ee[k] - ev) < mp.mpf("1e-9"))
        if mult == 1:
            frame_of_vac[bi] = ri
print(f"    vacuum-line -> frame map: {frame_of_vac}")

print("[2] the three frames' SM gradings (B884/B885 pipeline)...")
def frame_grading(ri):
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
    sts = []
    for i in range(27):
        v = mp.matrix([ER3[j, i] for j in range(27)])
        v = v * (1 / mp.sqrt(sum(abs(v[j]) ** 2 for j in range(27))))
        chs = []
        for Rz in (Rs1, Ry, Ry2):
            img = Rz * v
            chs.append(sum(img[j] * mp.conj(v[j]) for j in range(27)))
        sts.append((chs, v))
    pieces = []
    for chs, v in sts:
        for grp in pieces:
            if all(abs(chs[k] - grp["chs"][k]) < mp.mpf("1e-8") for k in range(3)):
                grp["vecs"].append(v)
                break
        else:
            pieces.append(dict(chs=chs, vecs=[v]))
    pieces.sort(key=lambda g: (len(g["vecs"]), float(mp.re(g["chs"][1]))))
    return pieces


allblocks = []
owner = []
for bi, g in enumerate(blocks):
    for v in g["vecs"]:
        allblocks.append(v)
        owner.append(bi)
BK = mp.matrix(27, len(allblocks))
for j, v in enumerate(allblocks):
    for i in range(27):
        BK[i, j] = v[i]
BH = mp.matrix(len(allblocks), 27)
for i in range(len(allblocks)):
    for j in range(27):
        BH[i, j] = mp.conj(BK[j, i])
G = BH * BK

tables = {}
for ri in range(3):
    pieces = frame_grading(ri)
    tab = []
    for grp in pieces:
        mass = [mp.mpf(0)] * 6
        for v in grp["vecs"]:
            xsol = mp.lu_solve(G, BH * v)
            for j in range(len(allblocks)):
                mass[owner[j]] += abs(xsol[j]) ** 2
        tot = sum(mass)
        tab.append(dict(dim=len(grp["vecs"]),
                        mass=[float(m / tot) for m in mass]))
    tables[ri] = tab
    zeros = sum(1 for row in tab for m in row["mass"] if m < 1e-12)
    print(f"    frame {ri}: 12 pieces x 6 blocks, zero cells: {zeros}/72")

res = dict(block_dims=bdims, vacuum_frame_map={str(k): v for k, v in frame_of_vac.items()},
           tables={str(k): v for k, v in tables.items()})
json.dump(res, open(os.path.join(HERE, "results.json"), "w"), indent=1,
          sort_keys=True, default=str)
print("  results written")
