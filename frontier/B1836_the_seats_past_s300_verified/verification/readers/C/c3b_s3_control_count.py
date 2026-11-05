"""C3b: S3's control as a count: on how many of the 42 sector-lines does the residue parity ALSO hold without b -> -b
(expected only where the sector's twists satisfy b = -b modulo the theta periods)?  Main's code."""
import contextlib, io, pathlib, sys
import numpy as np
ROOT = pathlib.Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "frontier/B1821_the_frames_mirror_symmetry_in_re_tau/verification"))
with contextlib.redirect_stdout(io.StringIO()):
    import cm_zero_line as Z
    B = Z.mods()["B"]
SG = {"1": -1, "i": 1, "j": 1, "k": -1}; mir = lambda z: -np.conj(z)
lines = [(2/5, 1/10), (2/5, 3/10), (1/5, 2/5), (3/8, 1/8), (1/4, 1/4), (1/3, 1/6), (1/10, 3/10)]
hold, tot, which = 0, 0, []
for t in (complex(0.13, 1.7), complex(-0.31, 2.6)):
    for (p1, p2) in lines:
        for sn, ql, qr in Z.SECTORS:
            R = B.residues(*B.sector_twists(B.line_w(p1, p2, t), t, ql, qr), t)
            Rc = B.residues(*B.sector_twists(B.line_w(p1, p2, mir(t)), mir(t), ql, qr), mir(t))
            dev = max(abs(Rc[s] - SG[s] * np.conj(R[s])) for s in B.UNITS) / max(abs(R[s]) for s in B.UNITS)
            tot += 1
            if dev < 1e-9: hold += 1; which.append((sn, round(p1, 3), round(p2, 3)))
s = "S3 control (b NOT flipped): parity holds on %d of %d sector-lines: %s" % (hold, tot, sorted(set(which)))
print(s); pathlib.Path(__file__).with_name("c3b_run.txt").write_text(s + "\n")
