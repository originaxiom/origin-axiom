"""C1 exploration (main, unsealed): singular values of Y(a,u) = a u^T + u a^T - (a.u) 1 near the double isotropic point.
Does m1/m3 scale like the smaller defect and m2/m3 like the larger, with defects d_a = |a.a|/|a|^2, d_u = |u.u|/|u|^2?"""
import numpy as np
rng = np.random.default_rng(7)
def iso(rng):
    x, y = rng.normal(size=3), rng.normal(size=3)
    y -= x*(x@y)/(x@x); y *= np.linalg.norm(x)/np.linalg.norm(y)        # x.y = 0, |x| = |y|  =>  (x+iy).(x+iy) = 0
    return x + 1j*y
def Y(a, u): return np.outer(a, u) + np.outer(u, a) - (a@u)*np.eye(3)
for trial in range(4):
    a0, u0 = iso(rng), iso(rng); na, nu = rng.normal(size=3)+1j*rng.normal(size=3), rng.normal(size=3)+1j*rng.normal(size=3)
    print(f"trial {trial}: |a0.u0|/(|a0||u0|) = {abs(a0@u0)/np.linalg.norm(a0)/np.linalg.norm(u0):.3f}")
    for ea, eu in [(1e-2, 1e-4), (1e-3, 1e-5), (1e-4, 1e-2), (1e-3, 1e-3)]:
        a, u = a0 + ea*na, u0 + eu*nu
        da, du = abs(a@a)/np.vdot(a, a).real, abs(u@u)/np.vdot(u, u).real
        s = np.linalg.svd(Y(a, u), compute_uv=False)
        print(f"   d_a={da:.2e} d_u={du:.2e}  m1/m3={s[2]/s[0]:.2e} m2/m3={s[1]/s[0]:.2e}  "
              f"(m1/m3)/min={s[2]/s[0]/min(da,du):.3f} (m2/m3)/max={s[1]/s[0]/max(da,du):.3f}  m3/(|a||u|)={s[0]/np.linalg.norm(a)/np.linalg.norm(u):.3f}")
