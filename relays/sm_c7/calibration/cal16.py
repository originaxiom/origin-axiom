# calibration C16: is the tau-only part h(tau) = c_s - F_u modular? (tau, tau + 1, -1/tau, a shear by 2)
import sys, pathlib, math
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import numpy as np, b1656_kernel as B, sm_c7_lib as L
def h_of(t, p1=0.13, p2=0.37):
    w = B.line_w(p1, p2, t); x, y = B.sector_twists(w, t, 1, 0); R = B.residues(x, y, t); c = B.cA(x, y, t, R)
    a1 = w.imag / t.imag; a2 = w.real - a1 * t.real
    return c["1"] - L.F_shift((a1, a2), t)
for t in [0.21 + 1.13j, -0.37 + 0.92j]:
    print("tau", t, " h(tau) %.9f  h(tau+1) %.9f  h(tau+2) %.9f  h(-1/tau) %.9f  log(Im tau) %.6f" %
          (h_of(t), h_of(t + 1), h_of(t + 2), h_of(-1 / t), math.log(t.imag)))
