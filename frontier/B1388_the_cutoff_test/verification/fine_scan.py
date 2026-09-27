#!/usr/bin/env python3
"""B1388, post-seal -- both counts at sixteen heights around the sealed grid's brackets at cusp 0 (K_n = 14, the sealed solve).

The sealed grid (40 heights, ratio 1.08) records the first change inside each bracket.  This lists every change: the relative index
chi(d+) (the sealed count, cutoff_test.chi_at) and Morse's boundary count Phi (the signed Higgs zeros, higgs_zeros.phi), side by side.
Usage: python3 fine_scan.py"""
import sys
import time
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import higgs_zeros as HZ

TAUS = (0.0967, 0.0980, 0.0990, 0.1000, 0.1020, 0.1030, 0.10335, 0.10355, 0.1040, 0.1044, 0.1050, 0.1056, 0.1100, 0.1128, 0.183,
        0.190)

if __name__ == "__main__":
    t0 = time.time()
    M = HZ.HF.member()
    S, x, st = HZ.HF.solve(M, 14, 0.10, 1, 1)
    print("B1388 post-seal fine scan, cusp 0, K_n 14 (fit residual %.1e)" % st["fit residual rms"], flush=True)
    for tau in TAUS:
        chi = HZ.CT.chi_at(S, x, 0, tau)
        phi = HZ.phi(S, x, 0, tau)
        print("tau %.5f  chi(d+) %+d (search complete: %s)  Phi %+d (complete: %s)" % (tau, chi[0], chi[1], phi[0], phi[1]), flush=True)
    print("(%.0fs)" % (time.time() - t0))
    print("DONE")
