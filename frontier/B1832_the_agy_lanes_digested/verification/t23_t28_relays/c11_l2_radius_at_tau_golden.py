"""c11: the radius used by Theorems 23, 25, 26 (toe_closure.py:4531, 4885, 5025: l2_val = 2.3577376878276057) against main's
L_2 (cm_zero_line.radii, B1667's canonical-cusp table) at Im tau_Golden = phi^2; sm_19_gate.py:690-696 (Theorem 8) interpolates."""
import math, pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "frontier" / "B1821_the_frames_mirror_symmetry_in_re_tau" / "verification"))
import cm_zero_line as Z
phi = (1 + math.sqrt(5)) / 2
lines = []
for y in (2.5, phi * phi, 2.75):
    lines.append("Im tau %.6f: (L_max, L_2) = %s" % (y, Z.radii(complex(1 / math.sqrt(5), y))))
lines.append("hard-coded l2_val in Theorems 23/25/26 = 2.3577376878276057 (= L_2 at Im tau 2.75, not at phi^2)")
print("\n".join(lines)); pathlib.Path(__file__).with_name("c11_l2_radius_at_tau_golden_out.txt").write_text("\n".join(lines) + "\n")
