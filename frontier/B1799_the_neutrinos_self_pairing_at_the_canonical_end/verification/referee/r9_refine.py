"""Referee B1799: refine r5's LL winding cells at tau = 0.37 + 2.2i (B1716's / B1799's point g1) by Newton on the complex
D(a, b) = sum c_s R_s^2 (finite-difference Jacobian), then check the full spectrum of the LL coupling at the root through
B1795's sector() (S and S~, both horocycles).  A root at a non-torsion (a, b) is a point where the Weinberg pair's det M
vanishes at a generic tau, off the census.  Read-only."""
import pathlib as _pl; _ROOT = str(next(q for q in _pl.Path(__file__).resolve().parents if (q / 'frontier').is_dir() and (q / 'GENESIS.md').is_file()))
import sys, math, json, pathlib, importlib.util
import numpy as np
ROOT = pathlib.Path(_ROOT + "")
spec = importlib.util.spec_from_file_location("split", ROOT / "frontier/B1795_the_doublet_triplet_split_at_the_canonical_end/verification/split.py")
SP = importlib.util.module_from_spec(spec); spec.loader.exec_module(SP)
B = SP._modules()["B"]
T = complex(0.37, 2.2)


def Dc(a, b, ql=-3, qr=-3):
    w = a * T + b; x, y = B.sector_twists(w, T, ql, qr); R = B.residues(x, y, T); c = B.cA(x, y, T, R)
    vals = [abs(v) for v in c.values() if v is not None]
    D = sum(c[s] * R[s] ** 2 for s in B.UNITS if c[s] is not None); return D, max(vals) * B.nR2(R)


def newton(a, b, it=14, h=1e-6):
    for _ in range(it):
        D, sc = Dc(a, b); Da = (Dc(a + h, b)[0] - D) / h; Db = (Dc(a, b + h)[0] - D) / h
        J = np.array([[Da.real, Db.real], [Da.imag, Db.imag]])
        try: step = np.linalg.solve(J, -np.array([D.real, D.imag]))
        except np.linalg.LinAlgError: break
        a, b = a + step[0], b + step[1]
        if abs(D) / sc < 1e-14: break
    D, sc = Dc(a, b); return a, b, abs(D) / sc


cells = [(0.0, 0.0741), (0.0370, 0.0556), (0.0370, 0.1389), (0.0741, 0.0), (0.0833, 0.0741), (0.0833, 0.1574)]
S = SP.higgs(T); Ls = SP.Ls_at(2.2)
for (a0, b0) in cells:
    a, b, dn = newton(a0 + 0.0046, b0 + 0.0046)
    r = SP.sector(T, a * T + b, -3, -3, S, Ls)
    light = min(r[k][2] / r[k][0] for k in r if k.startswith("sv|"))
    # nearest torsion point of order <= 60 (is the root a rational line?)
    from fractions import Fraction as Fr
    fa, fb = Fr(a).limit_denominator(60), Fr(b).limit_denominator(60)
    print("cell from (%.4f, %.4f): root (a, b) = (%.10f, %.10f), Dn %.2e; LL least sigma3/sigma1 %.2e; nearest p/q (q <= 60) (%s, %s) off by %.1e" % (a0, b0, a, b, dn, light, fa, fb, max(abs(a - fa), abs(b - fb))))
print("r9 exit 0")
