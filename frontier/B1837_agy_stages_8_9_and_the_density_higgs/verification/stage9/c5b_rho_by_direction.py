"""S303 check c5b (value-free; Higgs-only): rho = |h.h|/||h||^2 per census direction at Re tau 0.25, Im tau 2.4 and 4.5."""
import pathlib, sys
import numpy as np
sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parents[4]) + "/frontier/B1827_the_framing_ledger/verification/recheck")
from identities_and_order5 import Z
for im in (2.4, 4.5):
    tau = complex(0.25, im)
    print("Im tau %.1f: " % im + "  ".join("%s %.1e" % (d, abs(np.array(Z.direction(d, tau)) @ np.array(Z.direction(d, tau))) / np.vdot(Z.direction(d, tau), Z.direction(d, tau)).real) for d in Z.DIRS))
