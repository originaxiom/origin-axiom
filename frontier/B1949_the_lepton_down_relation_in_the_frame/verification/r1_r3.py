"""B1949, R1 to R3 (main, 2026-11-15; data-free; card ddee39436).
R1: frame C's coupling (B1940's frame_mp, via B1945's determinant_law.parts) for the leptons at w equals that of the
    charges (-1, 2) at 3w, entry by entry, both readings, w not reduced.
R2: B1788's tropical rule gives e_lep(alpha) = e_down(3 alpha) for both generations, every alpha of denominator <= 30.
R3: over the points of exact order N, the multisets of lepton and down exponents (B1788's rule) coincide when 3 does
    not divide N, and the leptons' equal the down's of order N/3 when it does."""
import sys, pathlib
from fractions import Fraction as Fr
from math import gcd
from collections import Counter
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
sys.path.insert(0, str(next((ROOT / "frontier").glob("B1945_*")) / "verification"))
sys.path.insert(0, str(next((ROOT / "frontier").glob("B1788_*")) / "verification"))
import determinant_law as DL
import tropical as T
mp = DL.mp; B = DL.B
B.SIXY["X"] = -1; B.SECTORS["dneg"] = ("X", "d")          # the down sector with the doublet's sign negated
# R1
worst = 0
for tx, ty in (("0.13", 1.7), ("-0.31", 2.9), ("0.4", 6.0)):
    for a, b in ((Fr(1, 5), Fr(2, 5)), (Fr(2, 5), Fr(4, 5)), (Fr(0), Fr(3, 5)), (Fr(1, 10), Fr(3, 10)), (Fr(2, 15), Fr(1, 15)), (Fr(3, 10), Fr(1, 2))):
        _, _, Yl, *_ = DL.parts(tx, ty, a, b, "lep"); _, _, Yx, *_ = DL.parts(tx, ty, 3 * a, 3 * b, "dneg")
        for r in ("S", "St"):
            scale = max(abs(Yl[r][i, j]) for i in range(3) for j in range(3))
            worst = max(worst, max(abs(Yl[r][i, j] - Yx[r][i, j]) for i in range(3) for j in range(3)) / scale)
print("R1: Y_lep(tau, w) against Y_(-1,2)(tau, 3w), 36 cases: worst relative difference %.1e" % worst)
# R2
P = {rd: T.polys(rd) for rd in ("S", "St")}
SIX = {"Q": 1, "u": -4, "d": 2, "L": -3, "e": 6}
def ex(ql, qr, a, rd): return T.predict(P[rd], T.E(ql * a, qr * a))
bad = 0; n = 0
for den in range(1, 31):
    for num in range(den):
        if gcd(num, den) != 1: continue
        a = Fr(num, den)
        for rd in ("S", "St"):
            n += 1
            if ex(-3, 6, a, rd) != ex(1, 2, 3 * a, rd): bad += 1
print("R2: e_lep(alpha) = e_down(3 alpha), both generations and readings: %d of %d slopes agree exactly" % (n - bad, n))
# R3
def spectrum(ql, qr, N, rd):
    pts = [Fr(i, N) for i in range(N) if gcd(i, N) == 1 or True]
    pts = [Fr(i, N) for i in range(N) for j in range(N) if N // gcd(gcd(i, j), N) == N]
    return Counter(ex(ql, qr, a, rd) for a in pts)
for N in (5, 10, 15, 20, 30):
    for rd in ("S", "St"):
        lep = spectrum(-3, 6, N, rd)
        same = lep == spectrum(1, 2, N, rd)
        coarse = None
        if N % 3 == 0:
            ptsN = [Fr(i, N) for i in range(N) for j in range(N) if N // gcd(gcd(i, j), N) == N]
            coarse = Counter(ex(1, 2, (3 * a) % 1, rd) for a in ptsN) == lep
        print("R3: N = %2d, reading %-2s: lepton multiset = down multiset at N: %s%s" % (N, rd, same, "" if coarse is None else "; = down at the points 3w (order N/3): %s" % coarse))
