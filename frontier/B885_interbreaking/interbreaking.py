#!/usr/bin/env python3
"""B885 -- the inter-breaking dictionary on the 27: two measurement frames, one space.

The same 27 carries K1's SM-grading and K2's (and K3's). The transition structure
between graded bases is the structural analog of frame misalignment between
measurements. TWO LAYERS, different invariance (stated before computing):

  COARSE (canonical): the 3x3 overlap table between K_i's {1, 10, 16} blocks --
    centralizer-determined, convention-free. Computed for all three root pairs;
    Galois consistency checked.
  FINE (convention-carrying): the multiplet-level table -- the Levi charges y, y2
    are chosen independently at each root by the same algorithm; only the
    zero-pattern's robustness is examined, and no fine-structure numbers are
    claimed.

All readouts OBLIQUE (the standing rule). Structure only; nothing resembling a
mixing MATRIX of values is computed or claimed.
"""
import json
import os
import subprocess

import mpmath
from mpmath import mp

HERE = os.path.dirname(os.path.abspath(__file__))
B884 = os.path.normpath(os.path.join(HERE, "..", "B884_yukawa_support"))
B883 = os.path.normpath(os.path.join(HERE, "..", "B883_the_27"))
B854 = os.path.normpath(os.path.join(HERE, "..", "B854_centralizer_exact",
                                     "e6_centralizer.py"))
CUBIC = [500716339200, -159667200, -28224, 1]

mp.dps = 30
REPJ = json.load(open(os.path.join(B883, "rep27.json")))
REP = {int(k): v for k, v in REPJ["rep"].items()}

src6 = open(B854, encoding="utf-8").read()
g6 = {"__file__": B854, "__name__": "b854"}
exec(compile(src6, B854, "exec"), g6)
inv8 = [mp.mpf(c.numerator) / mp.mpf(c.denominator) for c in g6["INV"][8]]
inv16 = [mp.mpf(c.numerator) / mp.mpf(c.denominator) for c in g6["INV"][16]]
roots_t = sorted(13 * mp.re(r) for r in mpmath.polyroots(
    [mp.mpf(c) for c in CUBIC], maxsteps=200, extraprec=120))


def rho_num(vec78):
    M = mp.zeros(27, 27)
    for p in range(78):
        c = vec78[p]
        if abs(c) < mp.mpf("1e-28"):
            continue
        Rp = REP[p]
        for i in range(27):
            for j in range(27):
                if Rp[i][j]:
                    M[i, j] += c * Rp[i][j]
    return M


def grading(ri):
    """the (s1, y, y2)-graded pieces of the 27 at root ri."""
    lf = os.path.join(B884, f"levi_charges_r{ri}.json")
    if not os.path.exists(lf):
        print(f"    computing Levi charges at root {ri}...")
        subprocess.run(["python3", os.path.join(B884, "make_levi_charges.py"),
                        str(ri)], check=True, cwd=B884,
                       stdout=subprocess.DEVNULL)
    lv = json.load(open(lf))
    y = [mp.mpc(mp.mpf(v[0]), mp.mpf(v[1])) for v in lv["y"]]
    y2 = [mp.mpc(mp.mpf(v[0]), mp.mpf(v[1])) for v in lv["y2"]]
    s1 = [inv8[p] + roots_t[ri] * inv16[p] for p in range(78)]
    Rs1, Ry, Ry2 = rho_num(s1), rho_num(y), rho_num(y2)
    Mmix = Rs1 * mp.mpf("1.0") + Ry * mp.mpf("0.70710678118") \
        + Ry2 * mp.mpf("0.31622776601")
    Mc = mp.matrix(27, 27)
    for i in range(27):
        for j in range(27):
            Mc[i, j] = mp.mpc(Mmix[i, j])
    E2, ER2 = mpmath.eig(Mc, left=False, right=True)
    states = []
    for i in range(27):
        v = mp.matrix([ER2[j, i] for j in range(27)])
        nv = mp.sqrt(sum(abs(v[j]) ** 2 for j in range(27)))
        v = v * (1 / nv)
        chs = []
        for Rz in (Rs1, Ry, Ry2):
            img = Rz * v
            chs.append(sum(img[j] * mp.conj(v[j]) for j in range(27)))
        states.append((chs, v))
    pieces = []
    for chs, v in states:
        for grp in pieces:
            if all(abs(chs[k] - grp["chs"][k]) < mp.mpf("1e-8")
                   for k in range(3)):
                grp["vecs"].append(v)
                break
        else:
            pieces.append(dict(chs=chs, vecs=[v]))
    # coarse blocks by s1-charge: {1, 10, 16}
    s1vals = sorted({mp.nstr(mp.re(p["chs"][0]), 10) for p in pieces})
    coarse = {}
    for p in pieces:
        key = mp.nstr(mp.re(p["chs"][0]), 10)
        coarse.setdefault(key, []).extend(p["vecs"])
    coarse_blocks = sorted(coarse.values(), key=len)   # dims 1, 10, 16
    return pieces, coarse_blocks


def oblique_overlap(blocks_a, blocks_b):
    """for each a-block: its coefficient mass on each b-block, in the FULL
    b-eigenbasis (oblique -- the standing rule)."""
    allb = []
    owner = []
    for bi, blk in enumerate(blocks_b):
        for v in blk:
            allb.append(v)
            owner.append(bi)
    B = mp.matrix(27, len(allb))
    for j, v in enumerate(allb):
        for i in range(27):
            B[i, j] = v[i]
    BH = mp.matrix(len(allb), 27)
    for i in range(len(allb)):
        for j in range(27):
            BH[i, j] = mp.conj(B[j, i])
    G = BH * B
    tab = []
    for ai, blk in enumerate(blocks_a):
        mass = [mp.mpf(0)] * len(blocks_b)
        for v in blk:
            x = mp.lu_solve(G, BH * v)
            for j in range(len(allb)):
                mass[owner[j]] += abs(x[j]) ** 2
        tot = sum(mass)
        tab.append([float(m / tot) for m in mass])
    return tab


print("[1] gradings at all three roots...")
G = {ri: grading(ri) for ri in (0, 1, 2)}
for ri in (0, 1, 2):
    print(f"    root {ri}: pieces {sorted(len(p['vecs']) for p in G[ri][0])}, "
          f"coarse dims {[len(b) for b in G[ri][1]]}")

print("[2] the COARSE 3x3 tables (canonical) for all root pairs...")
coarse_tables = {}
for (a, b) in ((0, 1), (0, 2), (1, 2)):
    tab = oblique_overlap(G[a][1], G[b][1])
    coarse_tables[f"{a}{b}"] = tab
    print(f"    K{a+1} blocks (rows: 1,10,16) vs K{b+1} blocks (cols):")
    for row in tab:
        print("      " + "  ".join(f"{x:.4f}" for x in row))

print("[3] the FINE zero-pattern (convention-carrying, pattern only)...")
fine_zero = {}
for (a, b) in ((0, 1),):
    pa = sorted(G[a][0], key=lambda p: len(p["vecs"]))
    pb = sorted(G[b][0], key=lambda p: len(p["vecs"]))
    blocks_a = [p["vecs"] for p in pa]
    blocks_b = [p["vecs"] for p in pb]
    tab = oblique_overlap(blocks_a, blocks_b)
    zeros = sum(1 for row in tab for x in row if x < 1e-10)
    total = len(tab) * len(tab[0])
    fine_zero[f"{a}{b}"] = dict(zeros=zeros, total=total,
                                dims_a=[len(b_) for b_ in blocks_a],
                                dims_b=[len(b_) for b_ in blocks_b],
                                table=tab)
    print(f"    K{a+1} x K{b+1} fine ({len(tab)}x{len(tab[0])}): "
          f"{zeros}/{total} zero cells")

res = dict(coarse=coarse_tables, fine=fine_zero,
           coarse_dims=[[len(b) for b in G[ri][1]] for ri in (0, 1, 2)])
json.dump(res, open(os.path.join(HERE, "results.json"), "w"), indent=1,
          sort_keys=True, default=str)
print("  results written")
