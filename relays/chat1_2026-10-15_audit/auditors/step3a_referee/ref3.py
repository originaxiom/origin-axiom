import math, numpy as np
from scipy.optimize import minimize
rng = np.random.default_rng(7)
def sig(w): return abs(w @ w) / np.vdot(w, w).real
def ratio(u, v): return abs(np.vdot(u, v)) ** 2 / (np.vdot(u, u).real * np.vdot(v, v).real)
def bnd(su, sv): return 0.5 * (1 + su * sv + math.sqrt(max(0, 1 - su * su) * max(0, 1 - sv * sv)))
# (a) exact-arithmetic-free check via angles: d(u,v) >= |a_u - a_v| on random draws in C^3 and C^5 (proof is dimension-free)
worst = -9
for n in (2, 3, 5):
    for _ in range(100000):
        u = rng.normal(size=n) + 1j * rng.normal(size=n); v = rng.normal(size=n) + 1j * rng.normal(size=n)
        # bias toward structured cases: sometimes make u isotropic-ish, v real-ish
        if rng.random() < 0.3:
            x, y = np.linalg.qr(rng.normal(size=(n, 2)))[0].T; u = x + 1j * y * rng.uniform(0.9, 1.0)
        if rng.random() < 0.3: v = rng.normal(size=n) * np.exp(1j * rng.uniform(0, 6.3)) + 1e-3j * rng.normal(size=n)
        d = math.acos(min(1, math.sqrt(ratio(u, v)))); au = 0.5 * math.acos(min(1, sig(u))); av = 0.5 * math.acos(min(1, sig(v)))
        worst = max(worst, abs(au - av) - d)
print("max(|a_u-a_v| - d(u,v)) over 3e5 draws, n=2,3,5:", worst)
# (b) adversarial: maximise ratio - bound with BFGS from many starts, n=3, parametrised on angles to avoid sqrt sensitivity
def gap_angle(p):
    u = p[0:3] + 1j * p[3:6]; v = p[6:9] + 1j * p[9:12]
    if np.vdot(u, u).real < 1e-9 or np.vdot(v, v).real < 1e-9: return 0
    d = math.acos(min(1, math.sqrt(ratio(u, v)))); au = 0.5 * math.acos(min(1, sig(u))); av = 0.5 * math.acos(min(1, sig(v)))
    return -(abs(au - av) - d)
adv = max(-minimize(gap_angle, rng.normal(size=12), method="Nelder-Mead", options={"maxiter": 6000, "xatol": 1e-13, "fatol": 1e-15}).fun for _ in range(300))
print("adversarial max(|a_u-a_v| - d):", adv)
# (c) sharp family, all (s_u, s_v)
sh = 0
for su in np.linspace(0, 1, 11):
    for sv in np.linspace(0, 1, 11):
        x, y = np.linalg.qr(rng.normal(size=(3, 2)))[0].T; au, av = 0.5 * math.acos(su), 0.5 * math.acos(sv)
        u = math.cos(au) * x + 1j * math.sin(au) * y; v = math.cos(av) * x + 1j * math.sin(av) * y
        sh = max(sh, abs(ratio(u, v) - bnd(sig(u), sig(v))))
print("sharp family max |ratio - bound| on 11x11 grid:", sh)
# (d) the isotropic vs real case, closed form: R=(x+iy)/sqrt2 -> |<R,v>|^2 = ((x.v)^2+(y.v)^2)/2 <= 1/2
# (e) numbers
s12, s13, ds12, ds13 = 0.3092, 0.02248, 0.0087, 0.00059
p = (1 - s12) * (1 - s13); dp1 = ds12 * (1 - s13); dp2 = math.hypot(dp1, (1 - s12) * ds13)
print(f"p={p:.6f} dp(theta12 only)={dp1:.6f} dp(+theta13)={dp2:.6f}  (p-1/2)/dp={((p-.5)/dp1):.3f}/{((p-.5)/dp2):.3f}  (1-p)/dp={((1-p)/dp1):.2f}")
print("sigma_nu_max data/TM1:", 2 * math.sqrt(p * (1 - p)), 2 * math.sqrt(2 / 9))
for name, P in (("data", p), ("TM1", 2 / 3)):
    turn = 45 - math.degrees(0.5 * math.acos(2 * P - 1))
    print(f"{name}: min electron turn off R = {turn:.4f} deg; sin^2(turn) = {math.sin(math.radians(turn))**2:.4f}")
# check the turn is attained: R=(x+iy)/sqrt2, nu=x, e=cos b x + i sin b y with cos^2 b = P
for P in (p, 2 / 3):
    b = math.acos(math.sqrt(P)); x = np.array([1, 0, 0.]); y = np.array([0, 1, 0.])
    R = (x + 1j * y) / math.sqrt(2); e = math.cos(b) * x + 1j * math.sin(b) * y
    print(f"  attained: |<e,nu>|^2={ratio(e, x):.6f}, FS(e,R)={math.degrees(math.acos(math.sqrt(ratio(e, R)))):.4f} deg")
# (f) T-NORM: a non-scalar metric K on M breaks the cap. tau = i: R ~ (-t4^2, -t4^2, i t3^2) with t3^4 = 2 t4^4
t4 = 1.0; t3 = 2 ** 0.25
R = np.array([-t4 ** 2, -t4 ** 2, 1j * t3 ** 2])
for kap in (1.0, 2.0, 2.08):
    K = np.diag([1, 1, kap]); ek = np.array([0, 0, 1.])
    ov = abs(R.conj() @ K @ ek) ** 2 / ((R.conj() @ K @ R).real * (ek @ K @ ek))
    print(f"  K=diag(1,1,{kap}): K-overlap of R with real e_k = {ov:.4f}")
