"""P-283 exploration (data-free; not sealed): the Majorana self-pairings at B1667's canonical end in B1656's frame --
nu^c nu^c (charges 0, 0; line-free) and the Weinberg-type L L (-3, -3) -- against the Dirac L nu^c (-3, 0).  det M via
D = sum c_s R_s^2 (B1716), Dn as B1716's Z6; the generation matrix's symmetry; on a few lines at B1716's two tau."""
import sys, math, importlib.util, pathlib
from fractions import Fraction as Fr
import numpy as np
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
spec = importlib.util.spec_from_file_location("split", ROOT / "frontier/B1795_the_doublet_triplet_split_at_the_canonical_end/verification/split.py")
sp_ = importlib.util.module_from_spec(spec); spec.loader.exec_module(sp_)
B = sp_._modules()["B"]
for (re_t, im_t) in ((0.37, 2.2), (0.11, 1.7)):
    t = complex(re_t, im_t); S = sp_.higgs(t); Ls = sp_.Ls_at(im_t)
    for (a, b) in ((Fr(0), Fr(0)), (Fr(2, 5), Fr(1, 10)), (Fr(1, 3), Fr(1, 2)), (Fr(2, 5), Fr(49, 60))):
        w = float(a) * t + float(b)
        for name, (ql, qr) in (("nuc nuc", (0, 0)), ("L L", (-3, -3)), ("L nuc", (-3, 0))):
            r = sp_.sector(t, w, ql, qr, S, Ls)
            x, y = B.sector_twists(w, t, ql, qr); R = B.residues(x, y, t); c = B.cA(x, y, t, R)
            u = {s: (math.sqrt(2 * math.pi * Ls["L_max"] + c[s]) * R[s] if c[s] is not None and 2 * math.pi * Ls["L_max"] + c[s] > 0 else 0) for s in B.UNITS}
            Y = B.coupling(S["S"], B.weighted_M(u)); asym = np.linalg.norm(Y - Y.T) / np.linalg.norm(Y)
            sv = r["sv|L_max|S"]
            print("tau %s line (%s, %s) %-8s R1_rel %.1e Dn %.2e  sv3/sv1 %.2e  |Y - Y^T|/|Y| %.2e" % (t, a, b, name, r["R1_rel"], r["Dn"], sv[2] / sv[0], asym))
