import pathlib, sys
from fractions import Fraction as F
ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "frontier" / "B1821_the_frames_mirror_symmetry_in_re_tau" / "verification"))
import cm_zero_line as Z
B = Z.mods()["B"]; keys = list(B.UNITS)
for al, b in ((F(1, 12), F(1, 12)), (F(1, 12), F(5, 12)), (F(5, 12), F(1, 3)), (F(1, 4), F(1, 2)), (F(2, 5), F(1, 10))):
    out = []
    for tau in (complex(0.2, 1.8), complex(0.37, 2.9)):
        for ql, qr in ((1, -4), (1, 2), (-3, 6)):
            w = B.line_w(al, b, tau); x, yy = B.sector_twists(w, tau, ql, qr); R = B.residues(x, yy, tau); c = B.cA(x, yy, tau, R)
            out.append(None if None in [c[k] for k in keys] else c[keys[2]] + c[keys[3]] - c[keys[0]] - c[keys[1]])
    print("line (%s, %s):" % (al, b), ["%.1e" % v if v is not None else None for v in out])
