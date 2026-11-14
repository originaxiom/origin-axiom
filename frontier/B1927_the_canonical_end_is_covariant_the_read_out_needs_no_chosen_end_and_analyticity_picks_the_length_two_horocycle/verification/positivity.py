"""Which end convention? The first test the mathematics can decide (written before the run).

The frame weights each channel by u_s = sqrt(2 pi L + c_s) when 2 pi L + c_s > 0, and sets it to 0 otherwise (B1724's
frame): a channel whose weight is cut makes the frame non-analytic there. With the canonical end read point by point
(B1667; `grid.json`), count, along the threads of the read-out (60 allowed words at n = 16, the mark's line carried by
B1724's transport), the share of nodes at which any channel with a non-zero residue is cut, for each convention
(maximal horoball, L_max; horocycle of length 2, L_2). EXPECTATION: none (the record's frame was built with these ends);
a convention that cuts a channel on a set of positive measure is the one the mathematics rejects. Printed: shares
only."""
import math, random, sys, pathlib
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import canon_readout as CR
T, C = CR.T, CR.C
Bm = C._modules()["B"]

if __name__ == "__main__":
    rng = random.Random(9161); words = []
    while len(words) < 60:
        w = "".join(rng.choice("LR") for _ in range(16))
        if "L" in w and "R" in w and T.keeps_mark(w):
            words.append(w)
    nodes = 0; cut = {"L_max": 0, "L_2": 0}; margin = {"L_max": np.inf, "L_2": np.inf}
    for w in words:
        beta, betap, ell, g = T.geodesic(w)
        zt = lambda s: complex((beta * 1j * math.exp(s) + betap) / (1j * math.exp(s) + 1))
        n_nodes = max(64, int(30 * abs(ell))); s0 = -ell / 2
        for j in range(n_nodes):
            tr, a, b, _ = T.reduce(zt(s0 + ell * j / n_nodes), 0.4, 0.8, {"x": 0.0})
            L = CR.canon(tr); L.pop("_extrapolated")
            wpt = float(a) * tr + float(b)
            nodes += 1
            any_cut = {h: False for h in L}
            for sec, (lf, rf) in C.SECT.items():
                x, yy = Bm.sector_twists(wpt, tr, Bm.SIXY[lf], Bm.SIXY[rf]); R = Bm.residues(x, yy, tr); c = Bm.cA(x, yy, tr, R)
                for h in L:
                    for s in Bm.UNITS:
                        if c[s] is not None and abs(R[s]) > 1e-12:
                            v = 2 * math.pi * L[h] + c[s]
                            margin[h] = min(margin[h], v)
                            if v <= 0:
                                any_cut[h] = True
            for h in L:
                cut[h] += any_cut[h]
    for h in ("L_max", "L_2"):
        print("%s: share of nodes with a channel cut %.4f (%d of %d); smallest 2 pi L + c_s over all nodes and channels: %s"
              % (h, cut[h] / nodes, cut[h], nodes, "positive" if margin[h] > 0 else "zero or negative"), flush=True)
