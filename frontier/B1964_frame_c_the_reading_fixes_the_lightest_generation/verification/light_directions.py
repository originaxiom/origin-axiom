"""B1964, the cusp limit on frame C's code (main, 2026-11-19; data-free): the lemma's consequence checked at every point.

The lemma (lemma.py, exact): if the Higgs matrix is exactly E12 the coupling's left null vector is (-i, 0, 1)/sqrt 2 for
every Mw of rank 2, and for E21 it is (i, 0, 1)/sqrt 2; frame C's S tends to a multiple of E12 high in the cusp and its
conjugate reading to a multiple of E21.  So, where Mw has rank 2 and the cusp limit has set in, every sector's lightest
generation is (-i, 0, 1)/sqrt 2 under S and (i, 0, 1)/sqrt 2 under S~, orthogonal, whatever the point and the charges.

EXPECTATIONS, written before the run (main, 2026-11-19):
 K1  at height 30, at every point of orders 3 to 10 whose Mw has rank 2 in the sense below, in all three sectors, the
     lightest left vector matches the lemma's to 1e-10 under both readings; prior 0.8.
 K2  every point where K1's match fails has an ill-conditioned Mw (singular ratio below 1e-30) or is degenerate; prior 0.7.
 K3  the order-2 points fail K1 under S (their Mw is rank 1 at leading order); prior 0.8.
 K4  |S[1,0] / S[0,1]| is at most 1e-38 at every point at height 30; prior 0.9.
Mw has rank 2 when its singular ratio is at least 1e-30; a point is degenerate as in B1963.
    python3 -B light_directions.py > light_directions_run.txt"""
import sys, pathlib
from fractions import Fraction as Fr
from collections import Counter
ROOT = next((q for q in [*pathlib.Path(__file__).resolve().parents, pathlib.Path.cwd()] if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file()))
sys.path.insert(0, str(next((ROOT / "frontier").glob("B1945_*")) / "verification"))
import determinant_law as DL, cusp_mixing as CM
mp = DL.mp
uS = mp.matrix([-1j, 0, 1]) / mp.sqrt(2); uSt = mp.matrix([1j, 0, 1]) / mp.sqrt(2)
if __name__ == "__main__":
    tally = Counter(); fails = []; worst_nil = 0.0
    for n in (2, 3, 4, 5, 6, 7, 8, 10):
        for i in range(n):
            for j in range(n):
                if (i, j) == (0, 0): continue
                a, b = Fr(i, n), Fr(j, n)
                for sec in ("up", "down", "lep"):
                    RD, Mw, Ys, u, cs, ds = DL.parts("0.13", 30.0, a, b, sec)
                    sv = sorted(mp.svd_c(Mw, compute_uv=False), key=lambda v: float(v)); ratio = sv[0] / sv[1]
                    worst_nil = max(worst_nil, float(abs(RD["S"][1, 0] / RD["S"][0, 1])))
                    devS = 1 - float(abs((uS.H * CM.U_of(Ys["S"])[:, 0])[0])); devT = 1 - float(abs((uSt.H * CM.U_of(Ys["St"])[:, 0])[0]))
                    rank2 = ratio >= mp.mpf(10) ** -30
                    ok = devS < 1e-10 and devT < 1e-10
                    tally[(n, "rank 2" if rank2 else "Mw ill-conditioned", "match" if ok else "no match")] += 1
                    if not ok: fails.append((n, str(a), str(b), sec, "%.1e" % float(ratio), "%.1e" % devS, "%.1e" % devT))
    for k in sorted(tally): print("order %2d, %-19s %-8s: %d (point, sector) cases" % (k[0], k[1] + ",", k[2], tally[k]))
    print("largest |S[1,0]/S[0,1]| at height 30: %.2e" % worst_nil)
    print("cases without a match (order, point, sector, Mw ratio, 1 - |overlap| under S, under S~): %d" % len(fails))
    for f in fails[:40]: print("  ", f)
