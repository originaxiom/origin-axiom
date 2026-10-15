"""EXPLORATION (main, firewalled): near the isotropic Higgs line a ~ Rbar, are the two light masses (relative to the heavy)
exactly the two isotropy defects |a.a|/|a|^2 (the Higgs's) and |v.v|/|v|^2 (the zero-mode triplet's) at first order?"""
import numpy as np, sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from symmetric_point_explore import Rvec, Y, sv
rng = np.random.default_rng(20261015)
for tau in [np.exp(2j*np.pi/3), 1j, 0.13+1.07j, 0.5+1.118034j]:
    R = Rvec(tau); R = R/np.linalg.norm(R)
    worst = 0
    for t in range(200):
        eps_a, eps_v = 10**rng.uniform(-6, -2), 10**rng.uniform(-6, -2)
        al = rng.normal(size=3)+1j*rng.normal(size=3); be = rng.normal(size=3)+1j*rng.normal(size=3)
        a = R.conj() + eps_a*al/np.linalg.norm(al); v = R + eps_v*be/np.linalg.norm(be)
        s = sv(Y(a, v)); da = abs(a@a)/np.linalg.norm(a)**2; dv = abs(v@v)/np.linalg.norm(v)**2
        pred = np.sort([da, dv])[::-1]; got = s[1:]/s[0]
        rel = np.abs(got/pred - 1).max(); worst = max(worst, rel/ max(eps_a, eps_v))
    print(f"tau={tau:.4f}: max |light/defect - 1| / max(eps) = {worst:.3f}  (O(1) => first-order law holds, error O(eps))")
# the a <-> v symmetry and the exact determinant
a = rng.normal(size=3)+1j*rng.normal(size=3); v = rng.normal(size=3)+1j*rng.normal(size=3)
print("Y(a,v)=Y(v,a):", np.abs(Y(a, v)-Y(v, a)).max(), "  |det| vs |a.v||a.a||v.v|:", abs(np.linalg.det(Y(a, v))), abs(a@v)*abs(a@a)*abs(v@v))
