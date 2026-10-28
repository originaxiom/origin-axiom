"""Referee check 1: is K_s = P_s/R_s the same function for down and leptons (same sum twist 3w)?  Is |P_s| E_t-periodic?"""
import sys, pathlib, numpy as np
from fractions import Fraction as Fr
sys.path.insert(0, str(next(q for q in __import__("pathlib").Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file()) / "frontier/B1723_the_golden_valley/verification"))
_argv = sys.argv; sys.argv = ["x"]; import b1656_funcs as B; sys.argv = _argv
rng = np.random.default_rng(7)
for (a, b) in ((Fr(2,5), Fr(1,10)), (Fr(2,5), Fr(23,30)), (Fr(2,5), Fr(1,5)), (Fr(1,9), Fr(1,9))):
    for t in (complex(0.3, 3.0), complex(0.3, 1.2)):
        w = float(a)*t + float(b)
        K = {}
        z = (rng.uniform(-.5,.5,40) + rng.uniform(-.5,.5,40)*t)
        for sec, (lf, rf) in B.SECTORS.items():
            ql, qr = B.SIXY[lf], B.SIXY[rf]
            x, y = B.sector_twists(w, t, ql, qr); R = B.residues(x, y, t); P = B.pairs(x, y, z, t); Pt = B.pairs(x, y, z + t, t); P1 = B.pairs(x, y, z + 1, t)
            K[sec] = {s: P[s]/R[s] for s in B.UNITS if abs(R[s]) > 1e-12}
            per = max(np.max(np.abs(np.abs(Pt[s]) - np.abs(P[s]))/np.abs(P[s])) for s in B.UNITS)
            per1 = max(np.max(np.abs(np.abs(P1[s]) - np.abs(P[s]))/np.abs(P[s])) for s in B.UNITS)
            print("(%s,%s) t=%s %-4s |R| %s  E_t-periodicity of |P_s|: tau-shift %.1e  1-shift %.1e" % (a, b, t, sec, np.round([abs(R[s]) for s in B.UNITS], 4), per, per1))
        d = max(np.max(np.abs(K["down"][s] - K["lep"][s])/np.abs(K["down"][s])) for s in K["down"] if s in K["lep"])
        print("   max |K_s(down) - K_s(lep)|/|K_s(down)| over 40 random z, all channels: %.2e" % d)
        dm = max(np.max(np.abs(np.abs(K["down"][s]) - np.abs(K["lep"][s]))/np.abs(K["down"][s])) for s in K["down"] if s in K["lep"])
        print("   max ||K_s(down)| - |K_s(lep)||/|K_s(down)|: %.2e" % dm)
