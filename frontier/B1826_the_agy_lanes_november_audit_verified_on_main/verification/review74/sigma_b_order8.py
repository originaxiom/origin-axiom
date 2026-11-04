"""Review 74 (S299): main's instrument, adopted from its P-086 reader after review -- the re-run of S298's claim (harvest row 1516; B1826/B1788 dated notes) that
sigma_b = c_j + c_k - c_1 - c_i is nonzero at finite tau on the order-8 lines (1/4, odd/8), about -+0.10 at
tau = 0.13 + 1.9i, using B1826's own functions (B1821's cm_zero_line module). Data-free."""
import pathlib, sys
from fractions import Fraction as F
ROOT = pathlib.Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "frontier" / "B1821_the_frames_mirror_symmetry_in_re_tau" / "verification"))
import cm_zero_line as Z
B = Z.mods()["B"]; keys = list(B.UNITS)
def cs(line, tau, ql, qr):
    w = B.line_w(line[0], line[1], tau); x, yy = B.sector_twists(w, tau, ql, qr)
    R = B.residues(x, yy, tau); return B.cA(x, yy, tau, R)
def sb(c):
    if None in [c[k] for k in keys]: return None
    return c[keys[2]] + c[keys[3]] - c[keys[0]] - c[keys[1]]
for b in (F(1, 8), F(3, 8), F(5, 8), F(7, 8), F(0), F(1, 2)):
    row = []
    for tau in (complex(0.13, 1.9), complex(0.0, 1.9), complex(0.13, 3.9), complex(1.0, 2.5)):
        for ql, qr in ((1, -4), (1, 2), (-3, 6)):
            v = sb(cs((F(1, 4), b), tau, ql, qr)); row.append(None if v is None else "%.3e" % v)
    print("line (1/4, %s): tau 0.13+1.9i [u,d,e], 0+1.9i, 0.13+3.9i, 1+2.5i:" % b, row)
