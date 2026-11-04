"""P-638's control (data-free): B1728's order-5 law Y_e = Y_d^T (FR-FIB's reading for down and lepton, a0 = 0) implies
U_e^L = conj(U_d^R) up to a phase per column, on every order-5 line. Checked on main's frame code at two tau, two seeds,
random complex Higgs h, both an arbitrary radius and a second one. Negative control: order-10 lines (2/5, odd/10), where
Y_e = Y_d^T is not claimed. Prints only deviations (no physical value)."""
import itertools, pathlib, sys
from fractions import Fraction as F
import numpy as np
ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "frontier/B1827_the_framing_ledger/verification/recheck"))
from identities_and_order5 import M_of, S_of, B

def Y(sector, tau, line, L, h):
    M, _ = M_of(tau, line, L, sector)
    return B.coupling(S_of(0, h), M)

def left_right(Yx):
    U, s, Vh = np.linalg.svd(Yx)            # Y = U diag(s) Vh, s descending
    return U, s, Vh.conj().T

def dev(Ue, Wd):
    """max over columns of 1 - |<ue_k, wd_k>|: 0 iff equal up to a phase per column"""
    return float(max(1 - abs(np.vdot(Ue[:, k], Wd[:, k])) for k in range(3)))

lines5 = [(F(a, 5), F(b, 5)) for a in range(5) for b in range(5) if (a, b) != (0, 0)]
lines10 = [(F(2, 5), F(b, 10)) for b in (1, 3, 5, 7, 9)]
for seed in (638, 6380):
    rng = np.random.default_rng(seed)
    for tau in (complex(0.31, 2.9), complex(0.12, 3.2)):
        for L in (2.37, 3.1):
            worst_id = worst5 = 0.0; neg = []
            for ln in lines5:
                h = rng.normal(size=3) + 1j * rng.normal(size=3)
                Yd = Y("down", tau, (float(ln[0]), float(ln[1])), L, h); Ye = Y("lepton", tau, (float(ln[0]), float(ln[1])), L, h)
                c = np.vdot(Yd.T.ravel(), Ye.ravel()) / np.vdot(Yd.T.ravel(), Yd.T.ravel())
                worst_id = max(worst_id, float(np.max(np.abs(Ye - c * Yd.T)) / np.max(np.abs(Ye))))
                Ue, se, _ = left_right(Ye); _, sd, Wd = left_right(Yd)
                if min(np.min(np.diff(-se)), np.min(np.diff(-sd))) > 1e-9 * se[0]:   # non-degenerate spectra only
                    worst5 = max(worst5, dev(Ue, Wd.conj()))
            for ln in lines10:
                h = rng.normal(size=3) + 1j * rng.normal(size=3)
                Yd = Y("down", tau, (float(ln[0]), float(ln[1])), L, h); Ye = Y("lepton", tau, (float(ln[0]), float(ln[1])), L, h)
                Ue, _, _ = left_right(Ye); _, _, Wd = left_right(Yd); neg.append(dev(Ue, Wd.conj()))
            print("seed %d tau %s L %.2f: order-5 (24 lines) max|Y_e - c Y_d^T|/|Y_e| = %.1e ; max(1 - |<U_e^L, conj U_d^R>|) = %.1e ; order-10 control min = %.2e"
                  % (seed, tau, L, worst_id, worst5, min(neg)))
