#!/usr/bin/env python3
"""Builds fd_rank.py, the sealed and dependency-free script of the claim card for P-596 and P-568's first half.

    python3 build_fd_rank.py <a checkout of main> <commit of main>

It copies main's frame code verbatim, by line ranges, from the named commit (git show), and adds the rank computation
of this seat's relations_check.py version 2 (796f02e2b, part 1). Everything copied is marked with its file and lines.
The built file imports only the standard library, numpy and mpmath, and reads no file.
"""
import json
import pathlib
import subprocess
import sys

ROOT, REV = pathlib.Path(sys.argv[1]).resolve(), sys.argv[2]
HERE = pathlib.Path(__file__).resolve().parent
QS = "frontier/B1691_the_exponents_at_the_two_fixed_points/verification/qseries.py"
TE = "frontier/B1691_the_exponents_at_the_two_fixed_points/verification/the_exponents.py"
BF = "frontier/B1691_the_exponents_at_the_two_fixed_points/verification/correction/b1656_funcs.py"
CZ = "frontier/B1821_the_frames_mirror_symmetry_in_re_tau/verification/cm_zero_line.py"
CC = "frontier/B1667_the_canonical_cusp/verification/the_canonical_cusp.json"


def src(path):
    return subprocess.run(["git", "-C", str(ROOT), "show", "%s:%s" % (REV, path)], check=True, capture_output=True,
                          text=True).stdout


def lines(path, a, b):
    L = src(path).splitlines()
    return "# ---- verbatim: %s, lines %d-%d (main at %s)\n" % (path, a, b, REV) + "\n".join(L[a - 1:b]) + "\n"


col = sorted((p["tau"][1], p["L_max"], p["L_2"]) for p in json.loads(src(CC))["points"] if abs(p["tau"][0] - 0.25) < 1e-9)

HEAD = '''#!/usr/bin/env python3
"""CLAIM CARD script for P-596 and P-568's first half: f(d), the rank of FR-FIB's ten outputs in tau, per branch.
Sealed and dependency-free: it imports only the standard library, numpy and mpmath, and reads no file. Data-free: no
measured value is used, and no inter-sector value is printed.

    python3 -I fd_rank.py

Built by build_fd_rank.py from main at %(rev)s. It copies main's frame code verbatim (marked below):
  - qseries.py and the Higgs directions' series from the_exponents.py (B1691);
  - route A and the coupling of b1656_funcs.py (B1691's correction folder);
  - DIRS, SECTORS, direction, radii and rows_at of cm_zero_line.py (B1821), with mods() returning the embedded objects;
  - the column Re tau = 1/4 of B1667's the_canonical_cusp.json (%(n)d points), for the radii.
The rank computation is part (1) of this seat's relations_check.py version 2 (796f02e2b).

The count. On a branch (line, direction, radius rule, reading; c by hand, H = I) the frame's only continuous input is
tau, so its outputs there form at most a two-parameter family. For each branch with the CKM defined and positive
ratios, the gradients in (Re tau, Im tau) of the ten outputs (logs of the six mass ratios and of |V_us|, |V_cb|, |V_ub|;
J itself) by central differences at step 1e-5. An output below 1e-6, or a gradient below 1e-8, is dropped from that
branch's gradients. The branch has rank 2 when two kept gradients are not parallel; printed are the largest |sin| of
the angle between two kept gradients, its distribution over the branches, and the counts below 0.1 and 1e-3.
"""
import contextlib
import io
import itertools
import math
import types
from fractions import Fraction
from fractions import Fraction as Fr

import mpmath as mp
import numpy as np
from numpy.polynomial.legendre import leggauss

''' % {"rev": REV, "n": len(col)}

parts = [HEAD]
parts.append(lines(QS, 1, 88))
parts.append("F = Fraction\n")
parts.append(lines(TE, 24, 29))
parts.append(lines(TE, 102, 104))
parts.append(lines(BF, 19, 69))
parts.append(lines(BF, 86, 86))
parts.append(lines(BF, 119, 126))
parts.append('''
# ---- the embedded objects that cm_zero_line's mods() loads from main's files
mp.mp.dps = 30
_te = types.SimpleNamespace(S=S, e4=e4, B=B, ev=ev)
_b = types.SimpleNamespace(QI=QI, QJ=QJ, QK=QK, EPS=EPS, UNITS=UNITS, line_w=line_w, sector_twists=sector_twists,
                           residues=residues, cA=cA, coupling=coupling, weighted_M=weighted_M)
_COL = %r
_S_ = _te.S
_Q = {"DR": _te.B[1], "a0": [_te.B[2][j] + _S_.c(F(-1, 48)) * _te.e4 * _te.B[0][j] for j in range(3)], "R": _te.B[0],
      "t=-5/288": [_te.B[2][j] + _S_.c(F(-5, 288)) * _te.e4 * _te.B[0][j] for j in range(3)]}
_M = dict(te=_te, B=_b, col=_COL, Q=_Q)


def mods():
    return _M


''' % (col,))
parts.append(lines(CZ, 37, 82))
parts.append('''

# ---- the rank, as in relations_check.py version 2, part (1)
def outs(tau, line):
    with contextlib.redirect_stdout(io.StringIO()):
        rows = rows_at(tau, line)
    res = {}
    for r in rows:
        a = [r["up"][1], r["up"][0], r["down"][1], r["down"][0], r["lepton"][1], r["lepton"][0], *r["V"]]
        if not r["V defined"] or min(a) <= 1e-300:
            continue
        res[(r["direction"], r["radius"], r["reading"])] = (np.array([math.log(v) for v in a] + [r["J"]]), np.array(a))
    return res


def main():
    print("(1) the rank of the ten in (Re tau, Im tau), per branch")
    h = 1e-5
    LINES1 = [(Fr(1, 7), Fr(2, 7)), (Fr(3, 8), Fr(3, 8)), (Fr(4, 9), Fr(1, 3)), (Fr(2, 5), Fr(1, 10)),
              (Fr(3, 11), Fr(5, 11)), (Fr(1, 12), Fr(0)), (Fr(5, 12), Fr(1, 4)), (Fr(1, 4), Fr(1, 8))]
    allmax = []
    dropped = 0
    for line in LINES1:
        for tau in (complex(0.13, 2.2), complex(0.31, 3.1)):
            o0 = outs(tau, line)
            ox = (outs(tau + h, line), outs(tau - h, line))
            oy = (outs(tau + 1j * h, line), outs(tau - 1j * h, line))
            mx = []
            for k in o0:
                if not all(k in d for d in (*ox, *oy)):
                    continue
                keep = np.array([v > 1e-6 for v in o0[k][1]] + [True])
                dropped += int(not keep.all())
                G = np.stack([(ox[0][k][0] - ox[1][k][0]) / (2 * h), (oy[0][k][0] - oy[1][k][0]) / (2 * h)], 1)[keep]
                n = np.linalg.norm(G, axis=1)
                G = G[n > 1e-8] / n[n > 1e-8][:, None]
                s = max(abs(G[i, 0] * G[j, 1] - G[i, 1] * G[j, 0]) for i in range(len(G)) for j in range(i + 1, len(G)))
                mx.append(s)
            mx = np.array(mx)
            allmax.extend(mx.tolist())
            print("    line (%s, %s), tau %.2f%+.2fi: %3d branches; max |sin| between two kept gradients: median %.3f, "
                  "minimum %.3f, below 0.1: %d" % (line[0], line[1], tau.real, tau.imag, len(mx), np.median(mx), mx.min(),
                                                   int(np.sum(mx < 0.1))))
    allmax = np.array(allmax)
    print("    all: %d branches (%d with an output below 1e-6 dropped); minimum %.3f; below 0.1: %d; below 1e-3: %d"
          % (len(allmax), dropped, allmax.min(), int(np.sum(allmax < 0.1)), int(np.sum(allmax < 1e-3))))
    print("    f(d) = 2 on every branch above:", bool(allmax.min() > 1e-3))


if __name__ == "__main__":
    main()
''')
text = "".join(parts)
(HERE / "fd_rank.py").write_text(text)
print("wrote fd_rank.py, %d lines" % text.count("\n"))
