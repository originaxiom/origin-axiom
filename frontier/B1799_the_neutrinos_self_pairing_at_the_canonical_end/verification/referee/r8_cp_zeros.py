"""Referee B1799: the LL (Weinberg pair) exact zeros on the CP lines found by r3, examined.  For representative lines:
the residues, the regularised norms (any clipped / None channel?), D, Dn, and the coupling's full spectrum through B1795's
sector() (S and S~, both horocycles); on Re tau = 0 and 1/2 at several Im tau, and just off them (Re tau +- 0.01) to see
whether the zero is a CP-line phenomenon (P-292's kind).  Read-only."""
import pathlib as _pl; _ROOT = str(next(q for q in _pl.Path(__file__).resolve().parents if (q / 'frontier').is_dir() and (q / 'GENESIS.md').is_file()))
import sys, math, pathlib, importlib.util
from fractions import Fraction as Fr
import numpy as np
ROOT = pathlib.Path(_ROOT + "")
spec = importlib.util.spec_from_file_location("split", ROOT / "frontier/B1795_the_doublet_triplet_split_at_the_canonical_end/verification/split.py")
SP = importlib.util.module_from_spec(spec); spec.loader.exec_module(SP)
B = SP._modules()["B"]


def look(re_t, im_t, a, b, ql=-3, qr=-3, verbose=False):
    t = complex(re_t, im_t); w = float(a) * t + float(b); S = SP.higgs(t); Ls = SP.Ls_at(im_t)
    r = SP.sector(t, w, ql, qr, S, Ls)
    light = min(r[k][2] / r[k][0] for k in r if k.startswith("sv|"))
    if verbose:
        print("    R:", {s: "%.3e%+.3ej" % tuple(r["R"][s]) for s in r["R"]})
        print("    c:", {s: (None if r["c"][s] is None else round(r["c"][s], 6)) for s in r["c"]}, " 2piL_2 = %.3f" % (2 * math.pi * Ls["L_2"]))
    return r["Dn"], light, r["R1_rel"]


for (re_t, a, b) in ((0.0, Fr(1, 8), Fr(1, 8)), (0.0, Fr(3, 8), Fr(5, 8)), (0.5, Fr(0), Fr(1, 4)), (0.5, Fr(1, 3), Fr(1, 12)), (0.5, Fr(1, 6), Fr(3, 4))):
    print("LL on line (%s, %s), Re tau = %.2f:" % (a, b, re_t))
    for k, im_t in enumerate((1.7, 2.2, 2.6, 3.0375)):
        Dn, light, r1 = look(re_t, im_t, a, b, verbose=(k == 1))
        print("  Im tau %.4f: Dn %.2e, least sigma3/sigma1 over S, S~ and both horocycles %.2e, R1_rel %.1e" % (im_t, Dn, light, r1))
    for dr in (-0.01, 0.01):
        Dn, light, _ = look(re_t + dr, 2.2, a, b)
        print("  off the CP line, Re tau %.2f, Im 2.2: Dn %.2e, least sigma3/sigma1 %.2e" % (re_t + dr, Dn, light))
# the same lines for nucnuc and Lnuc and the charged leptons at the CP points (for comparison)
for (re_t, a, b) in ((0.0, Fr(1, 8), Fr(1, 8)), (0.5, Fr(0), Fr(1, 4))):
    for nm, (ql, qr) in (("Lnuc", (-3, 0)), ("L e", (-3, 6)), ("nucnuc", (0, 0))):
        Dn, light, _ = look(re_t, 2.2, a, b, ql, qr); print("  %s on (%s, %s) at Re tau %.1f + 2.2i: Dn %.2e, least sigma3/sigma1 %.2e" % (nm, a, b, re_t, Dn, light))
print("r8 exit 0")
