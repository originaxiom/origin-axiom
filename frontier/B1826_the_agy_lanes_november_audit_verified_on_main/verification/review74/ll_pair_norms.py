"""Review 74 (S299): main's instrument, adopted from its P-086 reader after review -- the re-run of S298's claim (harvest rows 1512, 1538; B1826 dated note) that B1826 sec. 1.1's
sector-blind channel norms hold for the charged sectors (twist -+3; agreeing to ~7e-12 on three more lines) but the
LL pair (left twist -3w on both sides, total twist -+6) differs from them by order 10. B1826's own functions. Data-free."""
import pathlib, sys
from fractions import Fraction as F
ROOT = pathlib.Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "frontier" / "B1821_the_frames_mirror_symmetry_in_re_tau" / "verification"))
import cm_zero_line as Z
B = Z.mods()["B"]; keys = list(B.UNITS)
def cs(line, tau, ql, qr):
    w = B.line_w(line[0], line[1], tau); x, yy = B.sector_twists(w, tau, ql, qr)
    R = B.residues(x, yy, tau); return B.cA(x, yy, tau, R)
for line, tau in (((F(1, 3), F(1, 6)), complex(0.2, 2.3)), ((F(3, 10), F(1, 5)), complex(0.4, 1.9)),
                  ((F(5, 11), F(2, 11)), complex(0.05, 2.7)), ((F(2, 5), F(1, 10)), complex(0.3, 2.1))):
    ch = [cs(line, tau, ql, qr) for ql, qr in ((1, -4), (1, 2), (-3, 6))]
    ll = cs(line, tau, -3, -3)
    spread = max((max(v) - min(v)) for v in ([c[k] for c in ch] for k in keys) if None not in v)
    diff = max(abs(ll[k] - ch[1][k]) for k in keys if ll[k] is not None and ch[1][k] is not None)
    print(line, tau, "charged spread %.2e" % spread, " |LL - down| max %.3e" % diff,
          {k: (None if ll[k] is None else round(ll[k], 4), None if ch[1][k] is None else round(ch[1][k], 4)) for k in keys})
