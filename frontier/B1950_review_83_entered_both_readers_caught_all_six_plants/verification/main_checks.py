"""Review 83: main's own checks of the readers' findings that bear on the mathematics (main, 2026-11-17; data-free).
C1 (R83-20, F-R83-05): which order-5 line LR and RL fix up to sign.
C2 (F-R83-07): the torsion of H1 for the monodromies LR, -LR and LP (abs(2 - tr), abs(tr) for det -1).
C3 (F-R83-11): the complex channel residues under T, (tau, a, b) -> (tau + 1, a, b - a), in the down sector, divided by
    channel 1: a signed swap, not a plain one?
C4 (R83-19): B1940's own run files at height 12: do the double frame and the extended frame agree on W-'s mixing?"""
import sys, re, pathlib
from fractions import Fraction as Fr
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
sys.path.insert(0, str(next((ROOT / "frontier").glob("B1945_*")) / "verification"))
import determinant_law as DL
mp = DL.mp
# C1
for name, M in (("LR", ((2, 1), (1, 1))), ("RL", ((1, 1), (1, 2)))):
    fixed = sorted((i, j) for i in range(5) for j in range(5) if (i, j) != (0, 0)
                   and ((M[0][0] * i + M[0][1] * j + i) % 5, (M[1][0] * i + M[1][1] * j + j) % 5) == (0, 0))
    print("C1: %s sends to its negative the order-5 points (i, j)/5 with (i, j) in %s" % (name, fixed))
# C2
for name, M, det in (("LR (m004)", ((2, 1), (1, 1)), 1), ("-LR (m003)", ((-2, -1), (-1, -1)), 1), ("LP (m000)", ((1, 1), (1, 0)), -1)):
    tr = M[0][0] + M[1][1]
    print("C2: %s: trace %d, order of H1's torsion %d" % (name, tr, abs(2 - tr) if det == 1 else abs(tr)))
# C3
a, b = Fr(1, 5), Fr(2, 5)
_, _, _, u0, *_ = DL.parts("0.13", 1.7, a, b, "down"); _, _, _, u1, *_ = DL.parts("1.13", 1.7, a, (b - a) % 1, "down")
r0 = {s: u0[s] / u0["1"] for s in "ijk"}; r1 = {s: u1[s] / u1["1"] for s in "ijk"}
fmt = lambda z: "%.4f%+.4fi" % (float(mp.re(z)), float(mp.im(z)))
print("C3: at (tau, w):    i %s  j %s  k %s" % tuple(fmt(r0[s]) for s in "ijk"))
print("C3: at (tau+1, Tw): i %s  j %s  k %s" % tuple(fmt(r1[s]) for s in "ijk"))
print("C3: i' / i = %s ; j' / k = %s ; k' / j = %s" % (fmt(r1["i"] / r0["i"]), fmt(r1["j"] / r0["k"]), fmt(r1["k"] / r0["j"])))
# C4
V = next((ROOT / "frontier").glob("B1940_*")) / "verification"
for f in ("double_precision_fails_run.txt", "validate_frame_mp_run.txt"):
    for l in (V / f).read_text().split("\n"):
        if re.search(r"\b12(\.0)?\b", l[:40]): print("C4: %s: %s" % (f, l[:230]))
