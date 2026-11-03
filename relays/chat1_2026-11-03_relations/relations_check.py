"""The web seat's check for its note on the relations FR-FIB forces (P-568's first half; data-free; no measured value is
read, and no inter-sector value is printed off the lines where B1728's law makes it 1).

(1) The count. On a branch (line, direction, radius rule, reading; c by hand, H = I) the frame's only continuous input is
    tau, so its outputs there form at most a two-parameter family. For each branch with the CKM defined and positive
    ratios, the gradients in (Re tau, Im tau) of the ten outputs (logs of the six mass ratios and of |V_us|, |V_cb|,
    |V_ub|; J itself) by central differences; the branch has rank 2 when two gradients are not parallel. An output
    below 1e-6 (an exact zero such as B1716's, or a value whose logarithm is too noisy to differentiate at step 1e-5)
    is dropped from that branch's gradients, as is a gradient below 1e-8. Printed: the largest |sin| of the angle
    between two kept gradients, its distribution over the branches, the counts below 0.1 and below 1e-3, and how many
    branches had an output dropped. (Version 2: version 1, at 5aecc2bce, kept the exact zeros, whose noisy gradients
    inflated the measure.)
(2) The exact relations by line class (B1728's law, read as relations among the outputs). On one line of each exact
    order 2-12 (two lines for orders 4, 5 and 7), at tau = 0.13 + 2.2i, direction DR, radius L_2, the same reading in all
    sectors (S, then S~), for each pair of sectors (up-down, down-lepton, up-lepton): the two mass ratios compared to
    1e-8 relative, a ratio below 1e-12 in both sectors counted as an exact zero (B1716's zeros); the |log| of the ratio
    of the two sectors' largest singular values (below 1e-8: "equal"); and whether the off-diagonal |V| all lie below
    1e-8. Each is printed only as "equal" or "apart", with no value.

Usage: python3 relations_check.py <main checkout>   (main at 354a4ea4d; the frame's files unchanged since B1821)
"""
import contextlib
import io
import math
import os
import pathlib
import sys
from fractions import Fraction as Fr

import numpy as np

sys.dont_write_bytecode = True
ROOT = pathlib.Path(sys.argv[1]).resolve()
sys.path.insert(0, str(ROOT / "frontier" / "B1821_the_frames_mirror_symmetry_in_re_tau" / "verification"))
os.chdir(ROOT)
with contextlib.redirect_stdout(io.StringIO()):
    import cm_zero_line as Z
    B = Z.mods()["B"]


def outs(tau, line):
    with contextlib.redirect_stdout(io.StringIO()):
        rows = Z.rows_at(tau, line)
    res = {}
    for r in rows:
        a = [r["up"][1], r["up"][0], r["down"][1], r["down"][0], r["lepton"][1], r["lepton"][0], *r["V"]]
        if not r["V defined"] or min(a) <= 1e-300:
            continue
        res[(r["direction"], r["radius"], r["reading"])] = (np.array([math.log(v) for v in a] + [r["J"]]), np.array(a))
    return res


print("(1) the rank of the ten in (Re tau, Im tau), per branch")
h = 1e-5
LINES1 = [(Fr(1, 7), Fr(2, 7)), (Fr(3, 8), Fr(3, 8)), (Fr(4, 9), Fr(1, 3)), (Fr(2, 5), Fr(1, 10)), (Fr(3, 11), Fr(5, 11)),
          (Fr(1, 12), Fr(0)), (Fr(5, 12), Fr(1, 4)), (Fr(1, 4), Fr(1, 8))]
allmax = []; dropped = 0
for line in LINES1:
    for tau in (complex(0.13, 2.2), complex(0.31, 3.1)):
        o0 = outs(tau, line); ox = (outs(tau + h, line), outs(tau - h, line)); oy = (outs(tau + 1j * h, line), outs(tau - 1j * h, line))
        mx = []
        for k in o0:
            if not all(k in d for d in (*ox, *oy)):
                continue
            keep = np.array([v > 1e-6 for v in o0[k][1]] + [True])
            dropped += int(not keep.all())
            G = np.stack([(ox[0][k][0] - ox[1][k][0]) / (2 * h), (oy[0][k][0] - oy[1][k][0]) / (2 * h)], 1)[keep]
            n = np.linalg.norm(G, axis=1); G = G[n > 1e-8] / n[n > 1e-8][:, None]
            s = max(abs(G[i, 0] * G[j, 1] - G[i, 1] * G[j, 0]) for i in range(len(G)) for j in range(i + 1, len(G)))
            mx.append(s)
        mx = np.array(mx); allmax.extend(mx.tolist())
        print("    line (%s, %s), tau %.2f%+.2fi: %3d branches; max |sin| between two kept gradients: median %.3f, "
              "minimum %.3f, below 0.1: %d" % (line[0], line[1], tau.real, tau.imag, len(mx), np.median(mx), mx.min(), int(np.sum(mx < 0.1))))
allmax = np.array(allmax)
print("    all: %d branches (%d with an output below 1e-6 dropped); minimum %.3f; below 0.1: %d; below 1e-3: %d"
      % (len(allmax), dropped, allmax.min(), int(np.sum(allmax < 0.1)), int(np.sum(allmax < 1e-3))))

print("(2) the exact relations by line class, tau = 0.13 + 2.2i, DR, L_2, one reading in all sectors")
CH = {sn: (ql, qr) for sn, ql, qr in Z.SECTORS}


def Ys(tau, line, reading):
    with contextlib.redirect_stdout(io.StringIO()):
        L = Z.radii(tau)[1]; a = Z.direction("DR", tau)
    out = {}
    for sn, (ql, qr) in CH.items():
        w = B.line_w(line[0], line[1], tau); x, y = B.sector_twists(w, tau, ql, qr)
        R = B.residues(x, y, tau); c = B.cA(x, y, tau, R)
        u = {k: (math.sqrt(2 * math.pi * L + c[k]) * R[k] if c[k] is not None and 2 * math.pi * L + c[k] > 0 else 0) for k in B.UNITS}
        Sm = a[0] * B.QI + a[1] * B.QJ + a[2] * B.QK
        if reading:
            Sm = B.EPS @ Sm.conj() @ B.EPS.T
        out[sn] = B.coupling(Sm, B.weighted_M(u))
    return out


def tag(v, tol=1e-8):
    return "equal" if v < tol else "apart"


tau = complex(0.13, 2.2)
LINES2 = [(Fr(1, 2), Fr(0)), (Fr(1, 3), Fr(0)), (Fr(1, 4), Fr(0)), (Fr(1, 2), Fr(1, 4)), (Fr(2, 5), Fr(0)), (Fr(1, 5), Fr(3, 5)), (Fr(1, 6), Fr(1, 3)),
          (Fr(1, 7), Fr(0)), (Fr(2, 7), Fr(3, 7)), (Fr(3, 8), Fr(1, 8)), (Fr(2, 9), Fr(1, 3)), (Fr(3, 10), Fr(1, 5)),
          (Fr(2, 11), Fr(5, 11)), (Fr(5, 12), Fr(1, 6))]
for line in LINES2:
    N = int(np.lcm(line[0].denominator, line[1].denominator))
    for reading in (0, 1):
        Y = Ys(tau, line, reading)
        sv, U = {}, {}
        for sn, M in Y.items():
            u_, s, _ = np.linalg.svd(M); o = np.argsort(s); sv[sn] = s[o]; U[sn] = u_[:, o]
        rat = {sn: sv[sn][:2] / sv[sn][2] for sn in sv}
        V = np.abs(U["up"].conj().T @ U["down"])
        cells = []
        for a, b in (("up", "down"), ("down", "lepton"), ("up", "lepton")):
            ok = True; zero = False
            for i in (0, 1):
                ra, rb = rat[a][i], rat[b][i]
                if max(ra, rb) < 1e-12:
                    zero = True
                elif abs(ra - rb) > 1e-8 * max(ra, rb):
                    ok = False
            word = ("equal (m1 = 0 in both)" if zero else "equal") if ok else "apart"
            cells.append("%s=%s ratios %s, largest %s" % (a, b, word, tag(abs(math.log(sv[a][2] / sv[b][2])))))
        cells.append("V %s" % ("= 1" if max(V[0, 1], V[1, 2], V[0, 2]) < 1e-8 else "not 1"))
        print("    order %2d line (%s, %s) reading %s: %s" % (N, line[0], line[1], "S~" if reading else "S ", "; ".join(cells)))
