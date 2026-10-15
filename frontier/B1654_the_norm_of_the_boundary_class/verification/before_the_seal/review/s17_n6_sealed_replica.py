# Replica of the sealed N6 block (same rng, same code) with c from cA; written to see whether the thresholds are reachable
import sys, math; sys.path.insert(0,'.')
import numpy as np, pre
ns = pre.load(); cA=ns['cA']; R_A=ns['R_A']; D_of=ns['D_of']; nR2=ns['nR2']; TAUS=ns['TAUS']; Y=ns['Y']; vec=ns['vec']
C={name:{r:cA(r,TAUS[name],1e-5) for r in (2,3,4)} for name in ("omega","i","t1")}
rng = np.random.default_rng(1654)
def cplx(n): return rng.normal(size=n) + 1j*rng.normal(size=n)
n6 = {}
dirs = [cplx(3) for _ in range(3)]
for name in ("omega", "i", "t1"):
    tau = TAUS[name]; R = R_A(tau); Rv = vec(R); c = C[name]; cv = np.array([c[2], c[4], c[3]])
    D = D_of(c, R); recs = []
    near = np.conj(Rv) + 0.1*np.linalg.norm(Rv)*cplx(3)/math.sqrt(6)
    for a in dirs + [near]:
        s0 = np.linalg.svd(Y(a, Rv), compute_uv=False)
        lim = abs(a @ a)*abs(D)*abs(a @ Rv)/(2*np.pi*s0[0]**2*s0[1])
        rows = []
        for L in (40.0, 160.0, 640.0, 2560.0):
            u = np.sqrt(2*np.pi*L + cv)*Rv
            U, s, Vh = np.linalg.svd(Y(a, u)); v3 = np.conj(Vh[2])
            ang = math.acos(min(1.0, abs(np.vdot(v3, Rv))/np.linalg.norm(Rv)))
            rows.append({"L": L, "m1_m3": s[2]/s[0], "m2_m3": s[1]/s[0], "L_m1_m3": L*s[2]/s[0], "angle": ang,
                         "angle_over_sqrt_m1_m2": ang/math.sqrt(s[2]/s[1]) if s[2] > 0 else None})
        recs.append({"limit": lim, "rows": rows})
    n6[name] = recs
for name in ("i","t1"):
    for k,rec in enumerate(n6[name]):
        r=rec["rows"]
        print(f"{name:3s} dir{k}: lim err@2560={abs(r[-1]['L_m1_m3']/rec['limit']-1):.2e}  angL ratio={r[3]['angle']*2560/(r[2]['angle']*640):.5f}  halving={r[3]['angle_over_sqrt_m1_m2']/r[2]['angle_over_sqrt_m1_m2']:.5f}  angle@640={r[2]['angle']:.2e} @2560={r[3]['angle']:.2e}")
