"""P-555, data-free: r = |h.h|/||h||^2 (the Higgs direction's distance from the C^3 null cone) at tau and at the mirror -conj(tau)."""
import pathlib, sys
import numpy as np
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[4] / "frontier" / "B1821_the_frames_mirror_symmetry_in_re_tau" / "verification"))
import cm_zero_line as Z
rng = np.random.default_rng(7); worst = 0.0
for d in [x for x in Z.DIRS if x != "F_-2"]:
    for _ in range(4):
        tau = complex(float(rng.uniform(0.02, 0.48)), float(rng.uniform(1.0, 4.0)))
        r = []
        for t in (tau, complex(-tau.real, tau.imag)):
            h = np.array(Z.direction(d, t)); r.append(abs(h @ h) / np.vdot(h, h).real)
        worst = max(worst, abs(r[0] - r[1]) / max(r[0], 1e-300))
    print("%-9s r(tau) %.3e  r(mirror) %.3e" % (d, r[0], r[1]))
print("largest relative difference:", worst)
