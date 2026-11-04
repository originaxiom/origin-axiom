"""c10: Theorem 23 step 1's 'the up-quark Pauli-singlet residue vanishes (R_1^{(1,-4)}(alpha tau) = 0)' at N = 5 -- which up-sector
channel residues vanish on the ten slope-2/5 lines (main's residues; B1761/P-384 on record: the up i-residue vanishes iff 5w == 1/2)."""
import pathlib, sys
from fractions import Fraction as F
ROOT = pathlib.Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "frontier" / "B1821_the_frames_mirror_symmetry_in_re_tau" / "verification"))
import cm_zero_line as Z
B = Z.mods()["B"]
out = []
def say(*a):
    s = " ".join(str(x) for x in a); print(s); out.append(s)
for tau in (complex(0.3, 2.1), complex(-0.17, 2.9)):
    for k in range(10):
        line = (F(2, 5), F(k, 10)); w = B.line_w(line[0], line[1], tau); x, yy = B.sector_twists(w, tau, 1, -4)
        R = B.residues(x, yy, tau); nrm = max(abs(v) for v in R.values())
        say("tau %s line %-10s up (1,-4): channels with |R_s|/max < 1e-10: %s" % (tau, "(%s,%s)" % line, [s for s, v in R.items() if abs(v) / nrm < 1e-10]))
pathlib.Path(__file__).with_name("c10_up_residue_zeros_on_2_5_out.txt").write_text("\n".join(out) + "\n")
