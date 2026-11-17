"""B1957: agy-002's note M33 (its second computation of the SM seat's SM-C13), on main's frame code (the coupling of
wb2_stage3_on_main.py, which is B1945's with the charges passed in; with the norms).  Data-free.
 M33.1  at the 24 points of order 5 the lepton coupling (-3, 6) is the transpose of the down coupling (1, 2) times one
        scalar, exp(-20 pi i w1 w2), a fifth root of unity, in both Higgs readings; so the singular-value ratios agree.
 M33.2  at the 72 points of exact order 10 (an order-5 point plus one of the three half-periods) it is not.
 M33.3  the mechanism's signs: each channel matrix E_s and each generation contraction is symmetric or antisymmetric,
        with signs (-1, +1, +1, +1) for both, so the product is + in every channel.
 M33.4  two of the seat's controls in kind: the lepton charge moved to (-2, 6) breaks the copy at order 5; with the
        charges unchanged the copy fails at orders 3 and 7."""
import sys, pathlib, functools, cmath, math
from fractions import Fraction as Fr
import numpy as np
print = functools.partial(print, flush=True)
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent)); sys.path.insert(0, str(next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file()) / "frontier/B1957_the_seats_claims_register/verification/checks"))
import wb2_stage3_on_main as W

if __name__ == "__main__":
    tx, ty = "0.13", 1.45; P5 = [(Fr(i, 5), Fr(j, 5)) for i in range(5) for j in range(5) if (i, j) != (0, 0)]
    w1 = w2 = w3 = 0.0
    for (a, b) in P5:
        Yl, Yd = W.coupling(tx, ty, a, b, -3, 6, False), W.coupling(tx, ty, a, b, 1, 2, False)
        for rd in ("S", "St"):
            c = np.vdot(Yd[rd].T, Yl[rd]) / np.vdot(Yd[rd].T, Yd[rd].T); w1 = max(w1, np.abs(Yl[rd] - c * Yd[rd].T).max() / np.abs(Yl[rd]).max())
            w2 = max(w2, abs(c - cmath.exp(-20j * math.pi * float(a) * float(b)))); w3 = max(w3, np.abs(W.sv(Yl[rd]) - W.sv(Yd[rd])).max())
    print("M33.1: order 5, 24 points, both readings, with the norms: Y_lepton - c Y_down^T: %.1e; c against exp(-20 pi i w1 w2): %.1e; singular-value ratios differ by %.1e" % (w1, w2, w3))
    dist, split = [], []
    for (a, b) in P5:
        for (ha, hb) in ((Fr(1, 2), Fr(0)), (Fr(0), Fr(1, 2)), (Fr(1, 2), Fr(1, 2))):
            Yl, Yd = W.coupling(tx, ty, a + ha, b + hb, -3, 6, False), W.coupling(tx, ty, a + ha, b + hb, 1, 2, False)
            for rd in ("S",):
                dist.append(W.upto(Yl[rd], Yd[rd].T)); split.append(np.abs(W.sv(Yl[rd]) - W.sv(Yd[rd])).max())
    print("M33.2: order 10, %d points (reading S): distance of Y_lepton from any multiple of Y_down^T: least %.4f; singular-value ratios differ by between %.4f and %.4f; points where they agree to 1e-6: %d" % (len(dist), min(dist), min(split), max(split), sum(s < 1e-6 for s in split)))
    FM = W.FM; mp = W.mp; mp.mp.dps = 30; I, QI, QJ, QK, EPS, U, ED, BLOCKS = FM.setup(); t = mp.mpc("0.13", "1.45"); c3 = [W.te.ev(cc, t) for cc in W.te.B[1]]; S = c3[0] * QI + c3[1] * QJ + c3[2] * QK
    conj = lambda A: mp.matrix([[mp.conj(A[i, j]) for j in range(A.cols)] for i in range(A.rows)]); sm, sg = [], {"S": [], "St": []}
    for s_ in FM.UNITS:
        E = ED[s_]; sm.append(+1 if mp.norm(E.T - E) < 1e-20 else (-1 if mp.norm(E.T + E) < 1e-20 else 0))
        for rn, Sr in (("S", S), ("St", EPS * conj(S) * EPS.T)):
            G = mp.matrix([[sum(((Ca.T * EPS * Sr * Cb)[m, n] * E[m, n] for m in range(2) for n in range(2)), mp.mpc(0)) for Cb in BLOCKS] for Ca in BLOCKS])
            sg[rn].append(+1 if mp.norm(G.T - G) < 1e-20 * (1 + mp.norm(G)) else (-1 if mp.norm(G.T + G) < 1e-20 * (1 + mp.norm(G)) else 0))
    print("M33.3: transpose signs of the four channel matrices %s; of the generation contractions: reading S %s, reading S~ %s; products %s" % (sm, sg["S"], sg["St"], [a * b for a, b in zip(sm, sg["S"])]))
    worst = min(np.abs(W.sv(W.coupling(tx, ty, a, b, -2, 6, False)["S"]) - W.sv(W.coupling(tx, ty, a, b, 1, 2, False)["S"])).max() for (a, b) in P5[:8])
    print("M33.4: lepton charge moved to (-2, 6), order 5, eight points: the singular-value ratios differ from the down quark's by at least %.4f" % worst)
    for N in (3, 7):
        pts = [(Fr(i, N), Fr(j, N)) for i in range(N) for j in range(N) if (i, j) != (0, 0)][:8]
        d = [np.abs(W.sv(W.coupling(tx, ty, a, b, -3, 6, False)["S"]) - W.sv(W.coupling(tx, ty, a, b, 1, 2, False)["S"])).max() for (a, b) in pts]
        print("M33.4: charges unchanged, order %d, eight points: the singular-value ratios differ by between %.4f and %.4f" % (N, min(d), max(d)))
