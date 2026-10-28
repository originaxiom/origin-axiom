"""Referee B1799, check 5: the symmetry of the LL coupling depends on the partner's typing.  With u1 = 0 (equal twists),
B1736's form gives Y = u h^T + h u^T - (u.h)1 + h0 [u]_x: symmetric iff h0 = 0.  The quaternion square of the pure Higgs
section, S.S = -(h.h) 1, is pure '1' (h = 0, h0 = -(h.h)), so a partner typed as S.S (one reading of 'H H') gives an exactly
ANTISYMMETRIC LL coupling, h0 [u]_x, spectrum (|u|, |u|, 0).  Also S S~ (a general quaternion).  Read-only."""
import pathlib as _pl; _ROOT = str(next(q for q in _pl.Path(__file__).resolve().parents if (q / 'frontier').is_dir() and (q / 'GENESIS.md').is_file()))
import sys, math, pathlib, importlib.util
from fractions import Fraction as Fr
import numpy as np
ROOT = pathlib.Path(_ROOT + "")
spec = importlib.util.spec_from_file_location("split", ROOT / "frontier/B1795_the_doublet_triplet_split_at_the_canonical_end/verification/split.py")
SP = importlib.util.module_from_spec(spec); spec.loader.exec_module(SP)
B = SP._modules()["B"]
for pk in ("g1", "strip"):
    re_t, im_t = SP.POINTS[pk]; t = complex(re_t, im_t); H = SP.higgs(t); L = SP.Ls_at(im_t)["L_max"]
    S = H["S"]; S2 = S @ S; SSt = S @ H["St"]
    print("point %s: S.S = %s (h.h-scalar? off-diagonal %.1e, diag diff %.1e)" % (pk, np.round(np.diag(S2), 6), abs(S2[0, 1]) + abs(S2[1, 0]), abs(S2[0, 0] - S2[1, 1])))
    for (a, b) in ((Fr(2, 5), Fr(49, 60)), (Fr(1, 7), Fr(3, 7))):
        w = float(a) * t + float(b); x, y = B.sector_twists(w, t, -3, -3); R = B.residues(x, y, t); c = B.cA(x, y, t, R)
        u = {s: (math.sqrt(2 * math.pi * L + c[s]) * R[s] if c[s] is not None and 2 * math.pi * L + c[s] > 0 else 0) for s in B.UNITS}
        M = B.weighted_M(u)
        for nm, P in (("S", S), ("S.S", S2), ("S.S~", SSt)):
            Y = B.coupling(P, M); sv = np.linalg.svd(Y, compute_uv=False)
            print("  line (%s, %s) partner %-5s |Y-Y^T|/|Y| %.2e  |Y+Y^T|/|Y| %.2e  sv %s" % (a, b, nm, np.linalg.norm(Y - Y.T) / np.linalg.norm(Y), np.linalg.norm(Y + Y.T) / np.linalg.norm(Y), np.array2string(sv / sv[0], precision=3)))
print("r6 exit 0")
