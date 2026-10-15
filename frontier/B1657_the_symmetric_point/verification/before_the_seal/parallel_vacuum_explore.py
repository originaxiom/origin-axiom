"""EXPLORATION (main, firewalled), after the reviewer's blocker: near the PARALLEL isotropic vacuum a ~ R, v ~ R,
first order gives the light block diag(0, -(alpha+beta).R eps): the masses are elementary symmetric functions of the two
complex defects d_a = a.a/|a|^2, d_v = v.v/|v|^2: m2/m3 = |d_a + d_v|/4, m1/m3 = |d_a d_v|/4 ? (conjugate vacuum: {|d_a|, |d_v|})."""
import numpy as np, sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from symmetric_point_explore import Rvec, Y, sv
rng = np.random.default_rng(7)
for tau in [np.exp(2j*np.pi/3), 1j, 0.13+1.07j]:
    R = Rvec(tau); R = R/np.linalg.norm(R); w2 = w3 = 0
    for _ in range(300):
        ea, ev = 10**rng.uniform(-5, -2), 10**rng.uniform(-5, -2)
        al = rng.normal(size=3)+1j*rng.normal(size=3); be = rng.normal(size=3)+1j*rng.normal(size=3)
        a = 2.0*(R + ea*al/np.linalg.norm(al)); v = 3.0*(R + ev*be/np.linalg.norm(be))
        s = sv(Y(a, v)); da = (a@a)/np.linalg.norm(a)**2; dv = (v@v)/np.linalg.norm(v)**2
        p2, p3 = abs(da+dv)/4, abs(da*dv)/4
        w2 = max(w2, abs(s[1]/s[0]/p2 - 1)/max(ea, ev)); w3 = max(w3, abs(s[2]/s[0]/p3 - 1)/max(ea, ev))
    print(f"tau={tau:.3f}: parallel vacuum: max |m2/m3 / (|da+dv|/4) - 1|/eps = {w2:.3g};  max |m1/m3 / (|da dv|/4) - 1|/eps = {w3:.3g}")
