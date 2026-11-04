"""P-638's control repeated through the card's instrument (B1726's compute path): on the 24 order-5 lines (w = a tau + b),
Y_lep(S) = c Y_down(S)^T and U_lep^L = conj(U_down^R); the order-10 lines as negative control. Prints deviations only."""
import pathlib, sys
from fractions import Fraction as F
import numpy as np
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from card_instrument import yukawas, selfcheck
print("the wrapper against compute(): max |ratio difference| = %.1e" % selfcheck())
def dev(Ue, Wd): return float(max(1 - abs(np.vdot(Ue[:, k], Wd[:, k])) for k in range(3)))
lines5 = [(F(a, 5), F(b, 5)) for a in range(5) for b in range(5) if (a, b) != (0, 0)]
lines10 = [(F(2, 5), F(b, 10)) for b in (1, 3, 5, 7, 9)]
for (re_t, im_t) in ((0.31, 2.9), (0.12, 3.2)):
    for hor in ("L_max", "L_2"):
        wi = wu = 0.0; neg = []
        for ln in lines5 + lines10:
            Y = yukawas(re_t, im_t, float(ln[0]), float(ln[1]), hor, ("down", "lep"))
            Yd, Ye = Y[("down", "S")], Y[("lep", "S")]
            Ue = np.linalg.svd(Ye)[0]; Wd = np.linalg.svd(Yd)[2].conj().T
            if ln in lines5:
                c = np.vdot(Yd.T.ravel(), Ye.ravel()) / np.vdot(Yd.T.ravel(), Yd.T.ravel())
                wi = max(wi, float(np.max(np.abs(Ye - c * Yd.T)) / np.max(np.abs(Ye)))); wu = max(wu, dev(Ue, Wd.conj()))
            else:
                neg.append(dev(Ue, Wd.conj()))
        print("tau %.2f+%.2fi %s: order-5 max|Y_e - c Y_d^T| = %.1e, max(1 - |<U_e^L, conj U_d^R>|) = %.1e; order-10 control min = %.2f"
              % (re_t, im_t, hor, wi, wu, min(neg)))
