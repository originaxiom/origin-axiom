"""B915 THE CROSSING (R4) — computed per the sealed prereg, data contacted after seal.

Input: alpha_em(M_Z). Structure: E6 unification (g1=g2=g3 at M_U; the banked
3/8 boundary is the unification value by construction). Imports: 2-loop SM
gauge beta (3 families, 1 Higgs doublet; GUT-normalized g1), 1-loop matching,
the desert. The prediction: the one-parameter curve C in (sin2thetaW, alpha_s)
at M_Z. Verdict: sealed band d <= 3 HIT else MISS.
DATA (PDG 2024 world averages, contacted post-seal):
  1/alpha_em_hat(M_Z) = 127.951 +- 0.009 (MSbar)
  sin2thetaW_hat(M_Z) = 0.23122 +- 0.00004 (MSbar)
  alpha_s(M_Z) = 0.1180 +- 0.0009
"""
import json, os, math
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

MZ = 91.1876
INV_AEM = 127.951; S_INV_AEM = 0.009
SW2_EXP = 0.23122; S_SW2 = 0.00004
AS_EXP = 0.1180; S_AS = 0.0009

b1 = np.array([41/10, -19/6, -7.0])
B2 = np.array([[199/50, 27/10, 44/5],
               [9/10, 35/6, 12.0],
               [11/10, 9/2, -26.0]])

def run(alphas_mz, tmax, two_loop=True):
    """alphas at MZ -> alphas at scale exp(tmax)*MZ; t = ln(mu/MZ)."""
    def rhs(t, x):
        # x = 1/alpha_i ; d(1/a_i)/dt = -b_i/(2pi) - (1/8pi^2) sum_j B_ij / x_j... 
        a = 1.0/np.array(x)
        d = -b1/(2*math.pi)
        if two_loop:
            d = d - (B2 @ a)/(8*math.pi**2)
        return d
    sol = solve_ivp(rhs, (0, tmax), list(1.0/np.array(alphas_mz)),
                    rtol=1e-10, atol=1e-12, dense_output=True)
    return sol

def alphas_from(sw2, als, inv_aem=INV_AEM):
    aem = 1.0/inv_aem
    a1 = (5.0/3.0)*aem/(1.0 - sw2)
    a2 = aem/sw2
    return [a1, a2, als]

def curve_point(MU, two_loop=True):
    """given M_U: solve g1(MU)=g2(MU) for sw2, then g2(MU)=g3(MU) for alpha_s."""
    t = math.log(MU/MZ)
    def f_sw(sw2):
        s = run(alphas_from(sw2, 0.118), t, two_loop)
        x = s.y[:, -1]
        return x[0] - x[1]
    sw2 = brentq(f_sw, 0.18, 0.30, xtol=1e-12)
    def f_as(als):
        s = run(alphas_from(sw2, als), t, two_loop)
        x = s.y[:, -1]
        return x[1] - x[2]
    als = brentq(f_as, 0.06, 0.30, xtol=1e-12)
    return sw2, als

MUs = np.logspace(np.log10(1e3), np.log10(1.22e19), 61)
C1 = []; C2 = []
for MU in MUs:
    try: C1.append(curve_point(MU, False))
    except Exception: C1.append((float("nan"),)*2)
    try: C2.append(curve_point(MU, True))
    except Exception: C2.append((float("nan"),)*2)
C1 = np.array(C1); C2 = np.array(C2)

# the sealed distance: at each curve point, sigma_th,i = |C2-C1|_i; d per point
ds = []
for k in range(len(MUs)):
    if any(np.isnan(C2[k])) or any(np.isnan(C1[k])): ds.append(np.inf); continue
    sth = np.abs(C2[k] - C1[k])
    st_sw = math.sqrt(S_SW2**2 + sth[0]**2)
    st_as = math.sqrt(S_AS**2 + sth[1]**2)
    d = math.sqrt(((SW2_EXP - C2[k][0])/st_sw)**2 + ((AS_EXP - C2[k][1])/st_as)**2)
    ds.append(d)
kmin = int(np.argmin(ds)); dmin = float(ds[kmin])
# max-component reading at the same point (reported, secondary)
sth = np.abs(C2[kmin] - C1[kmin])
dmax_comp = max(abs(SW2_EXP - C2[kmin][0])/math.sqrt(S_SW2**2 + sth[0]**2),
                abs(AS_EXP - C2[kmin][1])/math.sqrt(S_AS**2 + sth[1]**2))

# failure geometry: pairwise meeting scales at 2 loops from the MEASURED point
def meet(i, j):
    x0 = 1.0/np.array(alphas_from(SW2_EXP, AS_EXP))
    def g(t):
        s = run(alphas_from(SW2_EXP, AS_EXP), t, True)
        x = s.y[:, -1]
        return x[i] - x[j]
    lo, hi = 1.0, math.log(1e22/MZ)
    try: return MZ*math.exp(brentq(g, lo, hi, xtol=1e-9))
    except Exception: return None
M12, M13, M23 = meet(0, 1), meet(0, 2), meet(1, 2)

verdict = "HIT" if dmin <= 3 else "MISS"
res = {
 "input": {"inv_alpha_em_MZ": INV_AEM, "sigma": S_INV_AEM},
 "test_pair": {"sw2": [SW2_EXP, S_SW2], "alpha_s": [AS_EXP, S_AS],
               "source": "PDG 2024 world averages, contacted post-seal"},
 "curve_2loop_at_dmin": {"MU_GeV": float(MUs[kmin]),
                         "sw2": float(C2[kmin][0]), "alpha_s": float(C2[kmin][1])},
 "truncation_sigma_at_dmin": {"sw2": float(sth[0]), "alpha_s": float(sth[1])},
 "d_min_euclidean_sigma": dmin, "d_max_component": float(dmax_comp),
 "sealed_verdict": verdict,
 "failure_geometry": {
   "pairwise_meeting_scales_GeV": {"g1=g2": M12, "g1=g3": M13, "g2=g3": M23},
   "sw2_gap_at_dmin": float(SW2_EXP - C2[kmin][0]),
   "alpha_s_gap_at_dmin": float(AS_EXP - C2[kmin][1])},
 "curve_samples": {"MU": [float(x) for x in MUs],
                   "two_loop": [[float(a), float(b)] for a, b in C2],
                   "one_loop": [[float(a), float(b)] for a, b in C1]},
}
json.dump(res, open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                 "results.json"), "w"), indent=1)
print("d_min =", round(dmin, 2), "sigma (euclidean);", "max-comp", round(dmax_comp, 2))
print("nearest curve point: MU = %.3e GeV, sw2 = %.5f, alpha_s = %.4f"
      % (MUs[kmin], C2[kmin][0], C2[kmin][1]))
print("measured:            sw2 = %.5f, alpha_s = %.4f" % (SW2_EXP, AS_EXP))
print("pairwise meeting scales: g1=g2 %.2e | g1=g3 %.2e | g2=g3 %.2e" % (M12 or 0, M13 or 0, M23 or 0))
print("SEALED VERDICT:", verdict)
