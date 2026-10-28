"""Referee B1795, r7: what makes the light state at the strip.  det Y = 4 det S det M tr(eps S M^T) (r3); decompose
sigma3/sigma1 = [|det Y| / sigma1^3] * [sigma1 / sigma2] and |det Y| into the normalised factors |det S|/(|S|^2/2),
|det M|/(|M|^2/2), |tr(eps S M^T)|/(|S||M|), for H and D on the carriers and two off-slope lines, both readings, L_max.
Uses r4's independent functions."""
import pathlib as _pl; _ROOT = str(next(q for q in _pl.Path(__file__).resolve().parents if (q / 'frontier').is_dir() and (q / 'GENESIS.md').is_file()))
import sys, math, json, pathlib, importlib.util
from fractions import Fraction as Fr
import numpy as np
sys.argv = [sys.argv[0], "48", "48"]
spec = importlib.util.spec_from_file_location("r4", pathlib.Path(__file__).resolve().parent / "r4_independent_recompute.py")
src = (pathlib.Path(__file__).resolve().parent / "r4_independent_recompute.py").read_text()
head = src.split("spec = importlib.util.spec_from_file_location(\"split\"")[0]           # the functions only, not the comparison loop
ns = {"__name__": "r4funcs", "__file__": __file__}; exec(compile(head, "r4_head", "exec"), ns)
ROOT = pathlib.Path(_ROOT + "")
spec = importlib.util.spec_from_file_location("split", ROOT / "frontier/B1795_the_doublet_triplet_split_at_the_canonical_end/verification/split.py"); SP = importlib.util.module_from_spec(spec); spec.loader.exec_module(SP)
EPS = ns["EPS"]
for pk in ("strip", "g1"):
    re_t, im_t = SP.POINTS[pk]; t = complex(re_t, im_t); Sx = SP.higgs(t); L = SP.Ls_at(im_t)["L_max"]
    for a, b in ((Fr(2, 5), Fr(49, 60)), (Fr(2, 5), Fr(7, 60)), (Fr(1, 6), Fr(1, 12)), (Fr(1, 4), Fr(3, 8))):
        for p in ("H", "D"):
            ql, qr = SP.PAIRS[p]
            x = (float(ql * a), float(2 * ql * b)); y = (float(qr * a), float(2 * qr * b))
            Rm = ns["residue_matrix"](x, y, t); R = {s: complex(ns["chan"]([[Rm[0, 0], Rm[0, 1]], [Rm[1, 0], Rm[1, 1]]], s)) for s in ns["UN"]}
            c = ns["norms"](x, y, t, R)
            M = sum((math.sqrt(2 * math.pi * L + c[s]) * R[s] if c[s] is not None else 0) * ns["EDU"][s] for s in ns["UN"])
            out = []
            for rn, S in Sx.items():
                Y = ns["Ycoup"](S, M); sv = np.linalg.svd(Y, compute_uv=False)
                fS = abs(np.linalg.det(S)) / (np.linalg.norm(S) ** 2 / 2); fM = abs(np.linalg.det(M)) / (np.linalg.norm(M) ** 2 / 2)
                fT = abs(np.trace(EPS @ S @ M.T)) / (np.linalg.norm(S) * np.linalg.norm(M))
                out.append("%-2s s3/s1 %.1e s2/s1 %.1e | detS %.1e detM %.1e tr %.1e" % (rn, sv[2] / sv[0], sv[1] / sv[0], fS, fM, fT))
            print("%-5s (%s, %s) %s: %s" % (pk, a, b, p, " || ".join(out)))
