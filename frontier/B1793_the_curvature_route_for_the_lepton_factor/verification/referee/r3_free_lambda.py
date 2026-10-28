"""Since K_s(down) == K_s(lep), every weight on the pair kernel gives one common channel vector lam2_s (the cut norms).  Scan it
freely (log-uniform over 6 decades per channel, projective) and over the curvature-reachable set lam2 = lam0^2 + sum m_k v(z_k)
(v(z) = (|K_s(z)|^2)_s; a positive bump of W/W0 - 1 at z_k): range of R2 and R1, and where R2 = 3 is crossed."""
import sys, math, json, numpy as np
from fractions import Fraction as Fr
sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent)); import ref_lib as RL
B = RL.B; rng = np.random.default_rng(20261028); KEYS = list(B.UNITS)
res = {}
for (a, b, im) in ((Fr(2,5), Fr(1,10), 3.0), (Fr(2,5), Fr(23,30), 3.0), (Fr(2,5), Fr(9,10), 3.0), (Fr(2,5), Fr(1,10), 6.0)):
    t = complex(0.3, im); S = RL.higgs_S(t); L = RL.L_of(im); sd = RL.sector_data(a, b, t)
    Rd, Rl = sd["down"][2], sd["lep"][2]; x, y, _ = sd["down"]
    c0, _ = RL.c_weighted(x, y, t, Rd); lam0 = {s: 2*math.pi*L + c0[s] for s in KEYS}
    R20, R10, _ = RL.ratios_from_lam2(lam0, Rd, Rl, S)
    # (a) free
    N = 60000; R2s = np.empty(N); R1s = np.empty(N); LAM = np.empty((N, 4))
    for i in range(N):
        l = 10**rng.uniform(-3, 3, 4); lam = dict(zip(KEYS, l)); R2s[i], R1s[i], _ = RL.ratios_from_lam2(lam, Rd, Rl, S); LAM[i] = l/l.max()
    # (b) reachable: lam0 + positive bumps at random z (1-3 points, masses log-uniform 1e-3..1e4 in units of the area)
    zz = (rng.uniform(-.5, .5, 4000) + rng.uniform(-.5, .5, 4000)*t); P = B.pairs(x, y, zz, t)
    V = np.array([np.abs(P[s]/Rd[s])**2 for s in KEYS]).T          # v(z)
    M2 = 40000; R2b = np.empty(M2); R1b = np.empty(M2)
    for i in range(M2):
        k = rng.integers(1, 4); idx = rng.integers(0, len(zz), k); m = 10**rng.uniform(-3, 4, k)
        l = np.array([lam0[s] for s in KEYS]) + (m[:, None]*V[idx]).sum(0)
        R2b[i], R1b[i], _ = RL.ratios_from_lam2(dict(zip(KEYS, l)), Rd, Rl, S)
    q = lambda arr: [float(np.quantile(arr, p)) for p in (0, .01, .5, .99, 1)]
    near3 = (R2s > 2.5) & (R2s < 3.5)
    print("(%s,%s) Im %g: frame R2 %.4f R1 %.4f | lam0 %s" % (a, b, im, R20, R10, {s: round(v, 3) for s, v in lam0.items()}))
    print("   FREE lam (60k): R2 q[0,1,50,99,100]%% %s ; R1 %s ; frac R2 in [2.5,3.5] %.4f ; frac R2>1.5 %.4f" % (np.round(q(R2s), 4), np.round(q(R1s), 3), near3.mean(), (R2s > 1.5).mean()))
    if near3.any():
        i = np.argmax(near3); print("   e.g. lam/max %s -> R2 %.3f R1 %.3f" % (np.round(LAM[i], 5), R2s[i], R1s[i]))
        print("   lam spread (max/min) among R2 in [2.5,3.5]: min %.1f median %.1f" % (np.min(1/LAM[near3].min(1)), np.median(1/LAM[near3].min(1))))
    print("   REACHABLE (lam0 + positive bumps, 40k): R2 %s ; R1 %s ; frac R2 in [2.5,3.5] %.4f" % (np.round(q(R2b), 4), np.round(q(R1b), 3), ((R2b > 2.5) & (R2b < 3.5)).mean()), flush=True)
    vn = V/V.sum(1, keepdims=True); print("   v(z) directions (normalised): min per channel %s max %s" % (np.round(vn.min(0), 3), np.round(vn.max(0), 3)))
    res["%s|%s|%g" % (a, b, im)] = dict(frame=[R20, R10], free_R2=q(R2s), free_R1=q(R1s), free_frac_near3=float(near3.mean()), reach_R2=q(R2b), reach_R1=q(R1b))
json.dump(res, open(__import__("pathlib").Path(__file__).resolve().parent / "r3_free_lambda.json", "w"), indent=1)
