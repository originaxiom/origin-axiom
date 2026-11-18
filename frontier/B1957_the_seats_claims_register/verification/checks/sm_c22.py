"""B1957: the SM seat's card SM-C22 (its branch at e7bf7bfca: SM_C22_EVERY_HIGGS_VECTOR_IN_D1.md, its card, its script read as
text and not run), on main's own closed form (cim_closed.Y_mp, 60 digits) with SM-C22's definitions as its script states them:
the top-aligned share (|<u_1(up), u_1(down)>| > 0.99 at height 10, over the 24 points of order 5, lift (0, 0), Re tau = 0.13)
and the median over the 24 points of the down sector's exponent E(s3/s1) between heights 8 and 10.
 S1  T1: Z^3 and X^3 on the six modes anticommute (main's level6_higgs.py).
 S2  the six single modes: the seat's figures (median E 0.93 to 1.07; at the mark (8/15, 4/5) or (2/15, 6/5); share <= 0.38).
 S3  MAIN'S COHERENT VECTOR h* (register row P-873), outside the seat's scan: its share and median E.  The seat's statement is
     that no vector has both a share >= 0.5 and a median E >= 0.1; h* has a hierarchy on three modes and no alignment.
NOT done: the seat's 5,000 random vectors and the pair vectors (its own run)."""

import sys, math, pathlib, itertools
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent; sys.path.insert(0, str(HERE))
sys.dont_write_bytecode = True
import cim_closed as CC, level6_higgs as L6
print("S1: ||Z^3 X^3 + X^3 Z^3|| = %.1e and ||Z^3 X^3 - X^3 Z^3|| = %.1f on the six modes: they anticommute" % (np.abs(L6.Z3 @ L6.X3 + L6.X3 @ L6.Z3).max(), np.abs(L6.Z3 @ L6.X3 - L6.X3 @ L6.Z3).max()), flush=True)
from fractions import Fraction as Fr
P5 = [(Fr(a, 5), Fr(b, 5)) for a in range(5) for b in range(5) if math.gcd(math.gcd(a, b), 5) == 1]; MARK = P5.index((Fr(2, 5), Fr(4, 5)))
def Ymp(tau, xi):
    d = CC.Y_mp(tau, xi, dps=60); T = np.zeros((3, 3, 6), complex)
    for (i, j, k), v in d.items(): T[i, j, k] = complex(v)
    return T
T = {}
for hy in (8, 10):
    tau = complex(0.13, hy)
    for idx, (a, b) in enumerate(P5):
        wv = float(a) * tau + float(b); T[(hy, idx, "up")] = Ymp(tau, 2.5 * wv); T[(hy, idx, "down")] = Ymp(tau, -0.5 * wv)
def stats(v, sec_e="down"):
    top = 0; E3 = {"up": [], "down": []}; Em = {}
    for idx in range(24):
        M = {(hy, s): np.einsum("ijk,k->ij", T[(hy, idx, s)], v) for hy in (8, 10) for s in ("up", "down")}
        Uu = np.linalg.svd(M[(10, "up")])[0]; Ud = np.linalg.svd(M[(10, "down")])[0]
        top += abs(np.vdot(Uu[:, 0], Ud[:, 0])) > 0.99
        for s in ("up", "down"):
            s8 = np.linalg.svd(M[(8, s)], compute_uv=False); s10 = np.linalg.svd(M[(10, s)], compute_uv=False)
            e = lambda q, r: math.log(max(q[r] / q[0], 1e-300)); E = [-(e(s10, r) - e(s8, r)) / (2 * math.pi) for r in (1, 2)]
            E3[s].append(E[1])
            if idx == MARK: Em[s] = [round(x, 4) for x in E]
    return top / 24, float(np.median(E3["down"])), float(np.median(E3["up"])), Em
hs = np.array([1 / math.sqrt(2), np.exp(1j * math.pi / 12) / 2, 0, 0, 0, np.exp(1j * math.pi / 12) / 2])
vecs = {"h*": hs}
for k in range(6):
    e = np.zeros(6, complex); e[k] = 1; vecs["mode %d" % k] = e
for name, v in vecs.items():
    s = stats(v / np.linalg.norm(v)); print(("S3: " if name == "h*" else "S2: ") + "%-7s top-aligned share %.3f; median E(s3/s1) down %.4f, up %.4f; at the mark (E2, E3): %s" % (name, s[0], s[1], s[2], s[3]), flush=True)
