"""B1668 draft (before the seal): prototype of the in-sandbox relations, run once to set the cells' thresholds.
Every number printed here is disclosed in the preregistration's section 0b. Inputs: PDG 2024 (accessed 2026-10-17),
Huang & Zhou 2021 (arXiv:2009.04851) for the charged-lepton masses at M_Z, 4-loop QCD running by CRunDec (rundec)."""
import math, numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq, fsolve
import rundec

# ---------------- data (PDG 2024 unless stated) ----------------
MZ, MW = 91.1880, 80.3692
alpha_inv_MZ = 127.930          # MS-bar hat-alpha^-1(M_Z), PDG 2024 EW review 10.2.2
s2W = 0.23129                   # MS-bar hat-s_Z^2, PDG 2024 Table 10.2
alpha_s = 0.1179                # PDG 2024 QCD/quark-mass review value
mu2, md2, ms2 = 2.20e-3, 4.69e-3, 92.74e-3      # MS-bar at 2 GeV (quark masses review eqs. 60.5-60.8), GeV
mc_mc, mb_mb = 1.275, 4.196                     # eqs. 60.23, 60.24
mt_direct, mt_direct_err = 172.57, 0.29         # summary table
mH, mH_err = 125.20, 0.11
me_pole, mmu_pole, mtau_pole, mtau_err = 0.51099895e-3, 0.1056583755, 1.77693, 0.00009
me_Z, mmu_Z, mtau_Z = 0.48307e-3, 0.101766, 1.72856     # Huang-Zhou 2021 Table 3, GeV
Vus, Vcb, Vub = 0.22501, 0.04183, 0.003732      # PDG 2024 CKM eq. 12.27
v = 246.22

# ---------------- quark masses at M_Z (4-loop QCD, nf thresholds at m_c, m_b) ----------------
crd = rundec.CRunDec()
as_mb = crd.AlphasExact(alpha_s, MZ, mb_mb, 5, 4)
as_mb4 = crd.DecAsDownMS(as_mb, mb_mb, mb_mb, 4, 4)
as_2 = crd.AlphasExact(as_mb4, mb_mb, 2.0, 4, 4)
as_mc4 = crd.AlphasExact(as_mb4, mb_mb, mc_mc, 4, 4)
def light_to_MZ(m2):
    m_mb = crd.mMS2mMS(m2, as_2, as_mb4, 4, 4); m_mb5 = crd.DecMqUpMS(m_mb, as_mb4, mb_mb, mb_mb, 4, 4)
    return crd.mMS2mMS(m_mb5, as_mb, alpha_s, 5, 4)
mu_Z, md_Z, ms_Z = light_to_MZ(mu2), light_to_MZ(md2), light_to_MZ(ms2)
mc_mb4 = crd.mMS2mMS(mc_mc, as_mc4, as_mb4, 4, 4); mc_mb5 = crd.DecMqUpMS(mc_mb4, as_mb4, mb_mb, mb_mb, 4, 4)
mc_Z = crd.mMS2mMS(mc_mb5, as_mb, alpha_s, 5, 4)
mb_Z = crd.mMS2mMS(mb_mb, as_mb, alpha_s, 5, 4)
print("quark masses at M_Z (GeV): u %.4e d %.4e s %.4e c %.4f b %.4f" % (mu_Z, md_Z, ms_Z, mc_Z, mb_Z))
print("   Huang-Zhou 2021 for comparison: u 1.23e-3 d 2.67e-3 s 5.316e-2 c 0.620 b 2.839")

# ---------------- R1 Koide ----------------
def koide(a, b, c): return (a + b + c)/(math.sqrt(a) + math.sqrt(b) + math.sqrt(c))**2
Qp = koide(me_pole, mmu_pole, mtau_pole); QZ = koide(me_Z, mmu_Z, mtau_Z)
s = math.sqrt(me_pole) + math.sqrt(mmu_pole)
t = max(np.roots([-1/3, 4/3*s, 2/3*s**2 - (me_pole + mmu_pole)]))
print("R1 Koide: Q(pole) = %.7f (2/3 = %.7f, diff %.1e); Q(M_Z) = %.5f (diff %.1e); m_tau predicted from Q=2/3: %.2f MeV vs %.2f +- %.2f" % (Qp, 2/3, Qp - 2/3, QZ, QZ - 2/3, t**2*1000, mtau_pole*1000, mtau_err*1000))
dQ = abs(koide(me_pole, mmu_pole, mtau_pole + mtau_err) - Qp)
print("   sigma_Q from m_tau: %.1e  -> pull %.2f" % (dQ, (Qp - 2/3)/dQ))

# ---------------- R2 GST ----------------
gst = math.sqrt(md2/ms2); gst_err = gst*0.5*math.sqrt((0.05/4.69)**2 + (0.54/92.74)**2)
print("R2 GST: sqrt(m_d/m_s) = %.5f +- %.5f vs |V_us| = %.5f +- 0.00068 -> pull %.2f; the same texture: sqrt(m_s/m_b)(M_Z) = %.4f vs |V_cb| = %.4f (ratio %.2f)" % (gst, gst_err, Vus, (gst - Vus)/math.hypot(gst_err, 0.00068), math.sqrt(ms_Z/mb_Z), Vcb, Vcb/math.sqrt(ms_Z/mb_Z)))

# ---------------- R3 Georgi-Jarlskog double ratios ----------------
gj1 = (mmu_Z/mtau_Z)/(ms_Z/mb_Z); gj2 = (md_Z/mb_Z)/(me_Z/mtau_Z)
e1 = gj1*math.sqrt((0.54/92.74)**2 + (0.012/4.196)**2 + 0.02**2); e2 = gj2*math.sqrt((0.05/4.69)**2 + (0.012/4.196)**2 + 0.02**2)
print("R3 GJ: (m_mu/m_tau)/(m_s/m_b) = %.3f +- %.3f vs 3 (pull %.1f, %.1f%%); (m_d/m_b)/(m_e/m_tau) = %.3f +- %.3f vs 3 (pull %.1f, %.1f%%)" % (gj1, e1, (gj1-3)/e1, (gj1/3-1)*100, gj2, e2, (gj2-3)/e2, (gj2/3-1)*100))

# ---------------- gauge couplings at M_Z (GUT normalisation) ----------------
a_em = 1/alpha_inv_MZ
a1 = (5/3)*a_em/(1 - s2W); a2 = a_em/s2W; a3 = alpha_s
print("alpha_i^-1(M_Z) = %.3f %.3f %.3f" % (1/a1, 1/a2, 1/a3))
bSM = np.array([41/10, -19/6, -7.0]); bMSSM = np.array([33/5, 1.0, -3.0])
def ainv(ainv0, b, t): return ainv0 - b/(2*math.pi)*t     # t = ln(mu/mu0)
def run_inv(model, mu, MS=1000.0):
    ainv0 = np.array([1/a1, 1/a2, 1/a3])
    if model == 'SM' or mu <= MS: return ainv(ainv0, bSM, math.log(mu/MZ))
    aS = ainv(ainv0, bSM, math.log(MS/MZ)); return ainv(aS, bMSSM, math.log(mu/MS))
for model in ('SM', 'MSSM'):
    meets = {}
    for (i, j) in ((0, 1), (0, 2), (1, 2)):
        f = lambda lm: run_inv(model, 10**lm)[i] - run_inv(model, 10**lm)[j]
        meets[(i+1, j+1)] = brentq(f, 3.5, 25)
    spread = max(meets.values()) - min(meets.values())
    # the unification prediction of sin^2 theta_W: solve for (s2, lnM) with alpha, alpha_s fixed
    def eqs(p, model=model):
        s2, lm = p; a1p = (5/3)*a_em/(1 - s2); a2p = a_em/s2
        ainv0 = np.array([1/a1p, 1/a2p, 1/a3]); MS = 1000.0
        if model == 'SM' or 10**lm <= MS: r = ainv(ainv0, bSM, math.log(10**lm/MZ))
        else: r = ainv(ainv(ainv0, bSM, math.log(MS/MZ)), bMSSM, math.log(10**lm/MS))
        return [r[0] - r[1], r[1] - r[2]]
    s2pred, lmpred = fsolve(eqs, [0.23, 16])
    print("R4 %s: pairwise one-loop meeting scales log10 = %s, spread %.2f decades; unification-predicted sin^2 theta_W = %.4f (data %.5f, %.1f%%), M_X = 10^%.2f" % (model, {k: round(x, 2) for k, x in meets.items()}, spread, s2pred, s2W, (s2pred/s2W - 1)*100, lmpred))

# ---------------- R5 criticality (Buttazzo et al. 2013 eqs. 64, 61e, 67) ----------------
for mt, mterr, label in ((mt_direct, mt_direct_err, 'direct 172.57+-0.29'), (172.4, 0.7, 'pole from cross sections 172.4+-0.7')):
    mcrit = 129.1 + 2.0*(mt - 173.10) - 0.5*(alpha_s - 0.1184)/0.0007
    err = math.sqrt((2.0*mterr)**2 + (0.5*0.0010/0.0007)**2 + 0.3**2 + 1.0**2)   # exp + perturbative + the 1 GeV th. of eq. 65's +-1.5? (eq.65 quotes +-1.5 total)
    lamPl = -0.0113 - 0.0065*(mt - 173.10) + 0.0018*(alpha_s - 0.1184)/0.0007 + 0.0029*(mH - 125.66)
    logLI = 11.3 + 1.0*(mH - 125.66) - 1.2*(mt - 173.10) + 0.4*(alpha_s - 0.1184)/0.0007
    print("R5 criticality (%s): M_h,crit = %.2f +- %.2f vs %.2f +- %.2f -> gap %.2f GeV (%.1f sigma); lambda(M_Pl) = %.4f; log10 Lambda_I = %.1f" % (label, mcrit, err, mH, mH_err, mcrit - mH, (mcrit - mH)/math.hypot(err, mH_err), lamPl, logLI))

# one-loop in-sandbox control: run from NNLO boundary values at M_t (eqs 55-60 shifted to today's inputs)
mt = mt_direct
lam0 = 0.12711 + 0.00206*(mH - 125.66) - 0.00004*(mt - 173.10)
yt0 = 0.93558 + 0.00550*(mt - 173.10) - 0.00042*(alpha_s - 0.1184)/0.0007 - 0.00042*(MW - 80.384)/0.014
g30 = 1.1666 + 0.00314*(alpha_s - 0.1184)/0.0007 - 0.00046*(mt - 173.10); g20 = 0.64822; gY0 = 0.35761; g10 = math.sqrt(5/3)*gY0
def rge_SM(t, y):
    g1, g2, g3, yt, yb, ytau, lam = y
    k = 1/(16*math.pi**2)
    Y2 = 3*yt**2 + 3*yb**2 + ytau**2
    return [k*41/10*g1**3, k*(-19/6)*g2**3, k*(-7)*g3**3,
            k*yt*(1.5*(yt**2 - yb**2) + Y2 - 8*g3**2 - 9/4*g2**2 - 17/20*g1**2),
            k*yb*(1.5*(yb**2 - yt**2) + Y2 - 8*g3**2 - 9/4*g2**2 - 1/4*g1**2),
            k*ytau*(1.5*ytau**2 + Y2 - 9/4*g2**2 - 9/4*g1**2),
            k*(24*lam**2 - 2*(3*yt**4 + 3*yb**4 + ytau**4) + 3/8*(2*g2**4 + (g2**2 + 3/5*g1**2)**2) + lam*(4*Y2 - 9*g2**2 - 9/5*g1**2))]
yb0, ytau0 = math.sqrt(2)*mb_Z/v, math.sqrt(2)*mtau_Z/v
sol = solve_ivp(rge_SM, [math.log(mt), math.log(1.22e19)], [g10, g20, g30, yt0, yb0, ytau0, lam0], rtol=1e-9, atol=1e-12, dense_output=True)
lamPl1 = sol.y[6, -1]
ts = np.linspace(math.log(mt), math.log(1.22e19), 4000); lams = sol.sol(ts)[6]
cross = ts[np.argmax(lams < 0)] if (lams < 0).any() else None
print("   one-loop control from the NNLO boundary values: lambda(M_Pl) = %.4f; lambda crosses zero at 10^%.1f GeV" % (lamPl1, (cross/math.log(10)) if cross else float('nan')))

# ---------------- R6 quasi-fixed point ----------------
for yt_hi in (1.5, 3.0, 10.0):
    def rge_down(t, y):
        g1, g2, g3, yt = y; k = 1/(16*math.pi**2)
        return [k*41/10*g1**3, k*(-19/6)*g2**3, k*(-7)*g3**3, k*yt*(4.5*yt**2 - 8*g3**2 - 9/4*g2**2 - 17/20*g1**2)]
    gPl = sol.y[:3, -1]
    s2 = solve_ivp(rge_down, [math.log(1.22e19), math.log(mt)], [gPl[0], gPl[1], gPl[2], yt_hi], rtol=1e-9, atol=1e-12)
    ytIR = s2.y[3, -1]
    print("R6 quasi-fixed point: y_t(M_Pl) = %.1f -> y_t(M_t) = %.3f -> m_t(tree) = %.0f GeV vs 172.57 (%.0f%%)" % (yt_hi, ytIR, ytIR*v/math.sqrt(2), (ytIR*v/math.sqrt(2)/172.57 - 1)*100))

# ---------------- R7 Veltman ----------------
mHV = math.sqrt(4*mt_direct**2 - 2*MW**2 - MZ**2)
print("R7 Veltman: m_H = %.1f GeV vs %.2f (%.0f%%)" % (mHV, mH, (mHV/mH - 1)*100))

# ---------------- R8 Cabibbo from Delta(6 7^2) ----------------
thC = math.degrees(math.asin(Vus)); thC_err = math.degrees(0.00068/math.sqrt(1 - Vus**2))
print("R8 pi/14 = %.3f deg vs theta_C = %.3f +- %.3f deg -> %.2f%%, pull %.1f" % (180/14, thC, thC_err, (180/14/thC - 1)*100, (180/14 - thC)/thC_err))

# ---------------- R9 Froggatt-Nielsen exponents ----------------
lam = Vus
ex = {k: math.log(r)/math.log(lam) for k, r in dict(u_t=mu_Z/172.57, c_t=mc_Z/172.57, d_b=md_Z/mb_Z, s_b=ms_Z/mb_Z, e_tau=me_Z/mtau_Z, mu_tau=mmu_Z/mtau_Z).items()}
print("R9 FN exponents log_lambda of the mass ratios (lambda = 0.225):", {k: round(x, 2) for k, x in ex.items()}, " within 0.2 of an integer:", sum(1 for x in ex.values() if abs(x - round(x)) <= 0.2), "of 6 (base rate 0.4 each)")

# ---------------- R10 b-tau unification, one loop SM and MSSM ----------------
def run_btau(model, tanb=10.0):
    if model == 'SM':
        y0 = [g10, g20, g30, yt0, yb0, ytau0, lam0]
        s = solve_ivp(rge_SM, [math.log(mt), math.log(2e16)], y0, rtol=1e-9, atol=1e-12)
        return s.y[4, -1]/s.y[5, -1]
    beta = math.atan(tanb)
    def rge_MSSM(t, y):
        g1, g2, g3, yt, yb, ytau = y; k = 1/(16*math.pi**2)
        return [k*33/5*g1**3, k*g2**3, k*(-3)*g3**3,
                k*yt*(6*yt**2 + yb**2 - 16/3*g3**2 - 3*g2**2 - 13/15*g1**2),
                k*yb*(6*yb**2 + yt**2 + ytau**2 - 16/3*g3**2 - 3*g2**2 - 7/15*g1**2),
                k*ytau*(4*ytau**2 + 3*yb**2 - 3*g2**2 - 9/5*g1**2)]
    s = solve_ivp(rge_SM, [math.log(mt), math.log(1000.0)], [g10, g20, g30, yt0, yb0, ytau0, lam0], rtol=1e-9, atol=1e-12)
    g1, g2, g3, yt, yb, ytau = s.y[:6, -1]
    y0 = [g1, g2, g3, yt/math.sin(beta), yb/math.cos(beta), ytau/math.cos(beta)]
    s2 = solve_ivp(rge_MSSM, [math.log(1000.0), math.log(2e16)], y0, rtol=1e-9, atol=1e-12)
    return s2.y[4, -1]/s2.y[5, -1]
print("R10 b-tau: m_b/m_tau at M_Z = %.3f; at 2e16 GeV one loop: SM %.3f; MSSM tan beta 3: %.3f, 10: %.3f, 50: %.3f" % (mb_Z/mtau_Z, run_btau('SM'), run_btau('MSSM', 3), run_btau('MSSM', 10), run_btau('MSSM', 50)))
