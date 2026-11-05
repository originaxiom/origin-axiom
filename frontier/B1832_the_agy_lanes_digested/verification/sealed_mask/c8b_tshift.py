"""SEALED-DIGEST CHECK c8b (value-free; main's residues): which integer shifts tau -> tau + m map the strip's order-10 lines
(2/5, (2j+1)/10) onto each other with |R_s| preserved in every sector and channel (Theorem 23 Step 3 claims one T-orbit)."""
import math, pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "frontier/B1821_the_frames_mirror_symmetry_in_re_tau/verification"))
import cm_zero_line as Z
B = Z.mods()["B"]
for odd in (True, False):
    for m in range(1, 11):
        worst = 0.0
        for tau in (0.21 + 1.8j, 0.37 + 2.5j):
            for j in range(5):
                p2 = (2 * j + 1) / 10 if odd else j / 5; p2s = (p2 - 0.4 * m) % 1
                for sn, ql, qr in Z.SECTORS:
                    R1 = B.residues(*B.sector_twists(B.line_w(0.4, p2, tau + m), tau + m, ql, qr), tau + m)
                    R0 = B.residues(*B.sector_twists(B.line_w(0.4, p2s, tau), tau, ql, qr), tau)
                    mx = max(abs(v) for v in R0.values())
                    worst = max(worst, max(abs(abs(R1[s]) - abs(R0[s])) / mx for s in B.UNITS))
        print("%s lines, shift m = %2d: max relative |R| mismatch %.1e" % ("order-10" if odd else "order-5 ", m, worst))
