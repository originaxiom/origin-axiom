"""B1949, R5, found in R4's output and tested after it was read (not blind; main, 2026-11-17; data-free): at order 10,
are the leptons the down quarks with the Higgs reading swapped? Frame C's averages over the 72 points of exact order 10
of sigma2/sigma3 and sigma1/sigma3, leptons under S against down under S-tilde and the reverse, at bulk moduli and on
the mirror column; and the same at order 5 (where the leptons copy the down quarks in the same reading) as the control."""
import sys, pathlib
from fractions import Fraction as Fr
from math import gcd
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
sys.path.insert(0, str(next((ROOT / "frontier").glob("B1945_*")) / "verification"))
import determinant_law as DL
mp = DL.mp


def averages(N, tx, ty):
    pts = [(Fr(i, N), Fr(j, N)) for i in range(N) for j in range(N) if N // gcd(gcd(i, j), N) == N]
    acc = {}
    for a, b in pts:
        for sec in ("lep", "down"):
            _, _, Ys, *_ = DL.parts(tx, ty, a, b, sec)
            for rd in ("S", "St"):
                s = sorted((abs(v) for v in mp.svd_c(Ys[rd], compute_uv=False)), reverse=True)
                k = (sec, rd); acc[k] = [p + q for p, q in zip(acc.get(k, [0, 0]), (s[1] / s[0], s[2] / s[0]))]
    return {k: [float(v / len(pts)) for v in acc[k]] for k in acc}


if __name__ == "__main__":
    for N in (10, 5):
        for tx, ty in (("0.13", 1.7), ("-0.31", 2.9), ("0.4", 6.0)):
            A = averages(N, tx, ty)
            swap = max(abs(A[("lep", "S")][j] / A[("down", "St")][j] - 1) for j in range(2)), max(abs(A[("lep", "St")][j] / A[("down", "S")][j] - 1) for j in range(2))
            same = max(abs(A[("lep", "S")][j] / A[("down", "S")][j] - 1) for j in range(2))
            print("N = %2d, tau = %s + %si: lep(S) against down(S~) %.1e, lep(S~) against down(S) %.1e; lep(S) against down(S) %.1e" % (N, tx, ty, swap[0], swap[1], same), flush=True)
