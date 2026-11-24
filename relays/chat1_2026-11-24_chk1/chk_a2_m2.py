import numpy as np, sys
rng = np.random.default_rng(20261124)
sx = np.array([[0,1],[1,0]],complex); sy = np.array([[0,-1j],[1j,0]]); sz = np.array([[1,0],[0,-1]],complex)
SIG = [sx, sy, sz]
def Y(h, u, w):
    H = sum(h[k]*SIG[k] for k in range(3)); M = -1j*w*np.eye(2) + sum(u[k]*SIG[k] for k in range(3))
    return np.array([[0.5*np.trace(SIG[a]@H@SIG[b]@M) for b in range(3)] for a in range(3)]), H, M
worst = np.inf; viol = 0; N = 40000
for n in range(N):
    mode = n % 4
    h = rng.normal(size=3) + 1j*rng.normal(size=3)
    if mode == 1:   # nearly null Higgs
        e1 = rng.normal(size=3); e1 /= np.linalg.norm(e1); e2 = rng.normal(size=3); e2 -= e2.dot(e1)*e1; e2 /= np.linalg.norm(e2)
        h = e1 + 1j*e2 + 10**rng.uniform(-6, -1)*(rng.normal(size=3)+1j*rng.normal(size=3))
    if mode == 2:   # nearly real Higgs
        h = rng.normal(size=3) + 1j*10**rng.uniform(-6, -1)*rng.normal(size=3)
    u = rng.normal(size=3) + 1j*rng.normal(size=3); w = rng.normal() + 1j*rng.normal()
    if mode == 3:   # nearly rank-one channel
        u = rng.normal(size=3)+1j*rng.normal(size=3); w = np.sqrt(-(u@u)+0j) * (1 + 10**rng.uniform(-6,-1))
    Ym, H, M = Y(h, u, w)
    s = np.linalg.svd(Ym, compute_uv=False)          # descending
    r = abs(h@h)/np.vdot(h, h).real; t = r/(1+np.sqrt(max(0.0, 1-r*r)))
    mu = np.linalg.svd(M, compute_uv=False); kap = mu[1]/mu[0]
    sH = np.linalg.svd(H, compute_uv=False)
    lhs = s[1]/s[0]; rhs = max(t*kap, abs(t-kap)/2)
    if lhs < rhs*(1-1e-9) - 1e-13: viol += 1
    worst = min(worst, lhs - rhs)
    if n < 3: print("check t = sigma2/sigma1(H):", t, sH[1]/sH[0])
print("trials %d, violations %d, least (m2/m3 - floor) %.3e" % (N, viol, worst))
