"""B1668 -- THE PRICE OF THE NINETEEN: the sealed instrument.

Every claimed relation among the Standard Model's nineteen free parameters that the preregistration lists is
recomputed here from the data table below (PDG 2024 and Huang & Zhou 2021, sources in the preregistration), graded by
the sealed rubric, and the preregistration's cells C0 and T1-T11 are evaluated. No number is typed in from a paper
except the data and the published NNLO fit coefficients of R5 (Buttazzo et al. 2013, eqs. 55-67), which are named as
such. Output: the_price_of_the_nineteen.json and _run.txt.

The rubric (sealed):
  HOLDS        |pull| <= 2, pull = (relation - data)/sigma, sigma = data error (+) the stated theory error, in quadrature
  APPROXIMATE  |pull| > 2 but |relative deviation| <= 10 %
  FAILS        otherwise
  FIT          the relation contains a continuous parameter fitted to the data it describes (no status against data)
  STRUCTURE    the relation fixes a pattern, not a number (no status against data)
A relation 'buys' one degree of freedom (dof) of the nineteen per independent equation it imposes among them, when its
status is HOLDS or APPROXIMATE and it carries no fitted continuous parameter; two relations on the same dof count once.
"""
import json, math, os, sys, time
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq, fsolve
import rundec

T0 = time.time()
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "the_price_of_the_nineteen.json")
LOG = open(os.path.join(HERE, "the_price_of_the_nineteen_run.txt"), "w")
def log(s):
    print(s); LOG.write(s + "\n"); LOG.flush()

# ---------------------------------------------------------------- the data table (sources: PREREGISTRATION section 1)
D = dict(
    MZ=91.1880, MW=80.3692,                                  # PDG 2024 summary tables (GeV)
    alpha_inv_MZ=(127.930, 0.008),                           # MS-bar hat-alpha^-1(M_Z), PDG 2024 EW review 10.2.2
    s2W=(0.23129, 0.00004),                                  # MS-bar hat-s_Z^2, PDG 2024 EW review Table 10.2
    alpha_s=(0.1179, 0.0010),                                # PDG 2024 (quark masses review 60.7, citing the QCD review)
    mu2=(2.20e-3, 0.07e-3), md2=(4.69e-3, 0.05e-3), ms2=(92.74e-3, 0.54e-3),   # MS-bar at 2 GeV, PDG 2024 quark masses eqs 60.5-60.8
    mc_mc=(1.275, 0.009), mb_mb=(4.196, 0.012),              # eqs 60.23, 60.24
    mt=(172.57, 0.29),                                       # direct measurements, PDG 2024 summary table
    mt_pole_xs=(172.4, 0.7),                                 # pole mass from cross sections, PDG 2024 summary table
    mH=(125.20, 0.11),                                       # PDG 2024 summary table
    me_pole=0.51099895e-3, mmu_pole=0.1056583755, mtau_pole=(1.77693, 0.00009),   # PDG 2024
    me_Z=0.48307e-3, mmu_Z=0.101766, mtau_Z=1.72856,         # Huang & Zhou 2021 Table 3 (MS-bar at M_Z), GeV
    Vus=(0.22501, 0.00068), Vcb=(0.04183, 0.00079), Vub=(0.003732, 0.000090), J=(3.12e-5, 0.13e-5),   # PDG 2024 CKM eq 12.27
    v=246.22,
    # the published NNLO fit of Buttazzo, Degrassi, Giardino, Giudice, Sala, Salvio, Strumia 2013 (arXiv:1307.3536v2)
    BDGGSSS=dict(lam_Mt=(0.12711, 0.00206, -0.00004, 0.00030), yt_Mt=(0.93558, 0.00550, -0.00042, -0.00042, 0.00050),
                 g3_Mt=(1.1666, 0.00314, -0.00046), g2_Mt=0.64822, gY_Mt=0.35761,
                 Mh_crit=(129.1, 2.0, -0.5, 0.3), lam_Pl=(-0.0113, -0.0065, 0.0018, 0.0029), logLI=(11.3, 1.0, -1.2, 0.4),
                 ref=dict(Mt=173.10, as_=0.1184, das=0.0007, Mh=125.66, MW=80.384, dMW=0.014)),
    theory_err_double_ratio=0.02,       # EW and Yukawa running and GUT thresholds not in the 4-loop QCD running (sealed)
    theory_err_crit_total=1.5,          # eq. 65 of the NNLO fit: M_h > (129.1 +- 1.5) GeV (their total; we add the exp. pieces explicitly)
)
MZ, MW, v = D['MZ'], D['MW'], D['v']

# ---------------------------------------------------------------- quark masses at M_Z (4-loop QCD, CRunDec)
crd = rundec.CRunDec()
def run_masses(alpha_s, mb_mb, mc_mc, mu2, md2, ms2):
    as_mb = crd.AlphasExact(alpha_s, MZ, mb_mb, 5, 4)
    as_mb4 = crd.DecAsDownMS(as_mb, mb_mb, mb_mb, 4, 4)
    as_2 = crd.AlphasExact(as_mb4, mb_mb, 2.0, 4, 4)
    as_mc4 = crd.AlphasExact(as_mb4, mb_mb, mc_mc, 4, 4)
    def light(m2):
        m_mb = crd.mMS2mMS(m2, as_2, as_mb4, 4, 4); m_mb5 = crd.DecMqUpMS(m_mb, as_mb4, mb_mb, mb_mb, 4, 4)
        return crd.mMS2mMS(m_mb5, as_mb, alpha_s, 5, 4)
    mc_mb4 = crd.mMS2mMS(mc_mc, as_mc4, as_mb4, 4, 4); mc_mb5 = crd.DecMqUpMS(mc_mb4, as_mb4, mb_mb, mb_mb, 4, 4)
    return dict(u=light(mu2), d=light(md2), s=light(ms2), c=crd.mMS2mMS(mc_mb5, as_mb, alpha_s, 5, 4), b=crd.mMS2mMS(mb_mb, as_mb, alpha_s, 5, 4))
M = run_masses(D['alpha_s'][0], D['mb_mb'][0], D['mc_mc'][0], D['mu2'][0], D['md2'][0], D['ms2'][0])
log("quark masses at M_Z (GeV, 4-loop QCD from PDG 2024 inputs): " + ", ".join(f"{k} {x:.5g}" for k, x in M.items()))
HZ = dict(u=1.23e-3, d=2.67e-3, s=53.16e-3, c=0.620, b=2.839)             # Huang-Zhou 2021 Table 2, from THEIR inputs
HZin = dict(alpha_s=0.1179, mb_mb=4.18, mc_mc=1.27, mu2=2.16e-3, md2=4.67e-3, ms2=93e-3)   # their inputs (PDG 2020)
M_hz = run_masses(**HZin)
ctrl = {k: M_hz[k]/HZ[k] - 1 for k in M}       # the control: our 4-loop QCD running of THEIR inputs against THEIR table
log("   control: this running on Huang-Zhou's inputs against their table (the residual is their EW/Yukawa part): " + ", ".join(f"{k} {100*x:+.1f}%" for k, x in ctrl.items()))
log("   this running on PDG 2024 inputs against their table: " + ", ".join(f"{k} {100*(M[k]/HZ[k] - 1):+.1f}%" for k in M))

def status(value, target, sigma, label):
    pull = (value - target)/sigma; rel = value/target - 1
    st = "HOLDS" if abs(pull) <= 2 else ("APPROXIMATE" if abs(rel) <= 0.10 else "FAILS")
    log(f"   {label}: value {value:.6g} target {target:.6g} sigma {sigma:.3g} pull {pull:+.2f} rel {100*rel:+.2f}% -> {st}")
    return dict(value=value, target=target, sigma=sigma, pull=pull, rel=rel, status=st)

R = {}   # the relations

# ---------------------------------------------------------------- R1 Koide
log("\nR1 Koide (pole masses; and at M_Z)")
def koide(a, b, c): return (a + b + c)/(math.sqrt(a) + math.sqrt(b) + math.sqrt(c))**2
me, mmu, (mtau, dmtau) = D['me_pole'], D['mmu_pole'], D['mtau_pole']
Qp = koide(me, mmu, mtau); dQ = abs(koide(me, mmu, mtau + dmtau) - Qp)
s = math.sqrt(me) + math.sqrt(mmu); mtau_pred = max(np.roots([-1/3, 4/3*s, 2/3*s**2 - (me + mmu)]))**2
QZ = koide(D['me_Z'], D['mmu_Z'], D['mtau_Z'])
R['R1_koide_pole'] = status(Qp, 2/3, dQ, "Q(pole) vs 2/3")
R['R1_koide_pole']['mtau_predicted_MeV'] = mtau_pred*1000; R['R1_koide_pole']['mtau_measured_MeV'] = (mtau*1000, dmtau*1000)
R['R1_koide_pole']['mtau_pull'] = (mtau_pred - mtau)/dmtau
log(f"   m_tau from Q = 2/3 and (m_e, m_mu): {mtau_pred*1000:.2f} MeV vs {mtau*1000:.2f} +- {dmtau*1000:.2f} (pull {(mtau_pred - mtau)/dmtau:+.2f})")
R['R1_koide_MZ'] = dict(value=QZ, target=2/3, dev=QZ - 2/3, status="FAILS at M_Z (scale-specific)" if abs(QZ - 2/3) > 5e-4 else "HOLDS at M_Z")
log(f"   Q(M_Z running masses) = {QZ:.5f}, deviation {QZ - 2/3:+.2e} -> {R['R1_koide_MZ']['status']}")

# ---------------------------------------------------------------- R2 Gatto-Sartori-Tonin and the texture's second prediction
log("\nR2 Gatto-Sartori-Tonin")
gst = math.sqrt(D['md2'][0]/D['ms2'][0]); gst_err = gst*0.5*math.hypot(D['md2'][1]/D['md2'][0], D['ms2'][1]/D['ms2'][0])
R['R2_gst'] = status(gst, D['Vus'][0], math.hypot(gst_err, D['Vus'][1]), "sqrt(m_d/m_s) vs |V_us|")
vcb_tex = math.sqrt(M['s']/M['b'])
R['R2_texture_Vcb'] = status(vcb_tex, D['Vcb'][0], math.hypot(0.02*vcb_tex, D['Vcb'][1]), "sqrt(m_s/m_b) vs |V_cb|")

# ---------------------------------------------------------------- R3 Georgi-Jarlskog double ratios (RG-invariant under QCD)
log("\nR3 Georgi-Jarlskog")
te = D['theory_err_double_ratio']
gj1 = (D['mmu_Z']/D['mtau_Z'])/(M['s']/M['b']); e1 = gj1*math.sqrt((D['ms2'][1]/D['ms2'][0])**2 + (D['mb_mb'][1]/D['mb_mb'][0])**2 + te**2)
gj2 = (M['d']/M['b'])/(D['me_Z']/D['mtau_Z']); e2 = gj2*math.sqrt((D['md2'][1]/D['md2'][0])**2 + (D['mb_mb'][1]/D['mb_mb'][0])**2 + te**2)
R['R3_gj_mu_s'] = status(gj1, 3.0, e1, "(m_mu/m_tau)/(m_s/m_b) vs 3")
R['R3_gj_e_d'] = status(gj2, 3.0, e2, "(m_d/m_b)/(m_e/m_tau) vs 3")

# ---------------------------------------------------------------- the gauge couplings and the RGEs
a_em = 1/D['alpha_inv_MZ'][0]; s2 = D['s2W'][0]
a1, a2, a3 = (5/3)*a_em/(1 - s2), a_em/s2, D['alpha_s'][0]
bSM = np.array([41/10, -19/6, -7.0]); bMSSM = np.array([33/5, 1.0, -3.0]); MSUSY = 1000.0
def ainv_run(ainv0, b, t): return ainv0 - b/(2*math.pi)*t
def run_inv(model, mu, ainv0):
    if model == 'SM' or mu <= MSUSY: return ainv_run(ainv0, bSM, math.log(mu/MZ))
    return ainv_run(ainv_run(ainv0, bSM, math.log(MSUSY/MZ)), bMSSM, math.log(mu/MSUSY))

# ---------------------------------------------------------------- R4 unification (one loop)
log("\nR4 gauge unification, one loop (SM content; MSSM content above 1 TeV)")
R['R4'] = {}
for model in ('SM', 'MSSM'):
    ainv0 = np.array([1/a1, 1/a2, 1/a3]); meets = {}
    for (i, j) in ((0, 1), (0, 2), (1, 2)):
        meets[f"{i+1}{j+1}"] = brentq(lambda lm: run_inv(model, 10**lm, ainv0)[i] - run_inv(model, 10**lm, ainv0)[j], 3.5, 25)
    spread = max(meets.values()) - min(meets.values())
    def eqs(p):
        s2p, lm = p; a0 = np.array([(1 - s2p)/((5/3)*a_em), s2p/a_em, 1/a3]); r = run_inv(model, 10**lm, a0); return [r[0] - r[1], r[1] - r[2]]
    s2pred, lmpred = fsolve(eqs, [0.23, 16])
    st = status(s2pred, s2, math.hypot(D['s2W'][1], 0.01*s2), f"{model}: unification-predicted sin^2 theta_W")   # 1% theory for one loop + thresholds
    R['R4'][model] = dict(meeting_scales_log10=meets, spread_decades=spread, s2W_predicted=s2pred, logMX=lmpred, **st)
    log(f"   {model}: pairwise meeting scales log10 {dict((k, round(x, 2)) for k, x in meets.items())}, spread {spread:.2f} decades; M_X = 10^{lmpred:.2f}")

# ---------------------------------------------------------------- R5 criticality (the NNLO fit evaluated; one-loop control in-sandbox)
log("\nR5 criticality of the Higgs quartic")
B = D['BDGGSSS']; ref = B['ref']; mt, dmt = D['mt']; alpha_s, das = D['alpha_s']; mH, dmH = D['mH']
def crit(mt_, dmt_):
    c0, cmt, cas, cth = B['Mh_crit']
    val = c0 + cmt*(mt_ - ref['Mt']) + cas*(alpha_s - ref['as_'])/ref['das']
    err = math.sqrt((cmt*dmt_)**2 + (cas*das/ref['das'])**2 + cth**2 + 1.0**2)    # exp. pieces + the fit's 0.3 perturbative + 1.0 for the remaining theory (eq. 65's 1.5 total is a +-)
    return val, err
R['R5'] = {}
for key, (mt_, dmt_) in (('direct', D['mt']), ('pole_xs', D['mt_pole_xs'])):
    val, err = crit(mt_, dmt_)
    st = status(val, mH, math.hypot(err, dmH), f"M_h,crit({key} m_t) vs M_h")
    l0, lmt, las, lmh = B['lam_Pl']; lamPl = l0 + lmt*(mt_ - ref['Mt']) + las*(alpha_s - ref['as_'])/ref['das'] + lmh*(mH - ref['Mh'])
    L0, Lmh, Lmt, Las = B['logLI']; logLI = L0 + Lmh*(mH - ref['Mh']) + Lmt*(mt_ - ref['Mt']) + Las*(alpha_s - ref['as_'])/ref['das']
    R['R5'][key] = dict(gap_GeV=val - mH, lam_Pl_NNLO=lamPl, log10_Lambda_I=logLI, **st)
    log(f"   {key}: gap M_h,crit - M_h = {val - mH:+.2f} GeV; lambda(M_Pl) NNLO fit = {lamPl:+.4f}; log10 Lambda_I = {logLI:.1f}")
# one-loop control from the NNLO boundary values shifted to today's inputs
l0, lmh, lmt, lth = B['lam_Mt']; lam0 = l0 + lmh*(mH - ref['Mh']) + lmt*(mt - ref['Mt'])
y0, ymt, yas, ymw, yth = B['yt_Mt']; yt0 = y0 + ymt*(mt - ref['Mt']) + yas*(alpha_s - ref['as_'])/ref['das'] + ymw*(MW - ref['MW'])/ref['dMW']
g0, gas, gmt = B['g3_Mt']; g30 = g0 + gas*(alpha_s - ref['as_'])/ref['das'] + gmt*(mt - ref['Mt']); g20 = B['g2_Mt']; g10 = math.sqrt(5/3)*B['gY_Mt']
yb0, ytau0 = math.sqrt(2)*M['b']/v, math.sqrt(2)*D['mtau_Z']/v
def rge_SM(t, y):
    g1, g2, g3, yt, yb, ytau, lam = y; k = 1/(16*math.pi**2); Y2 = 3*yt**2 + 3*yb**2 + ytau**2
    return [k*41/10*g1**3, k*(-19/6)*g2**3, k*(-7)*g3**3,
            k*yt*(1.5*(yt**2 - yb**2) + Y2 - 8*g3**2 - 9/4*g2**2 - 17/20*g1**2),
            k*yb*(1.5*(yb**2 - yt**2) + Y2 - 8*g3**2 - 9/4*g2**2 - 1/4*g1**2),
            k*ytau*(1.5*ytau**2 + Y2 - 9/4*g2**2 - 9/4*g1**2),
            k*(24*lam**2 - 2*(3*yt**4 + 3*yb**4 + ytau**4) + 3/8*(2*g2**4 + (g2**2 + 3/5*g1**2)**2) + lam*(4*Y2 - 9*g2**2 - 9/5*g1**2))]
MPL = 1.22e19
sol = solve_ivp(rge_SM, [math.log(mt), math.log(MPL)], [g10, g20, g30, yt0, yb0, ytau0, lam0], rtol=1e-10, atol=1e-13, dense_output=True)
ts = np.linspace(math.log(mt), math.log(MPL), 6000); lams = sol.sol(ts)[6]
cross = (ts[np.argmax(lams < 0)]/math.log(10)) if (lams < 0).any() else None
R['R5']['one_loop_control'] = dict(lam_Pl=float(sol.y[6, -1]), lam_zero_log10=cross, boundary=dict(lam=lam0, yt=yt0, g3=g30, g2=g20, g1=g10))
log(f"   one-loop control: lambda(M_Pl) = {sol.y[6, -1]:+.4f}; lambda crosses zero at 10^{cross:.1f} GeV" if cross else f"   one-loop control: lambda(M_Pl) = {sol.y[6, -1]:+.4f}; no zero below M_Pl")

# ---------------------------------------------------------------- R6 quasi-infrared fixed point
log("\nR6 quasi-infrared fixed point of y_t (one loop)")
gPl = sol.y[:3, -1]; R['R6'] = {}
for yt_hi in (1.5, 3.0, 10.0):
    def rge_down(t, y):
        g1, g2, g3, yt = y; k = 1/(16*math.pi**2)
        return [k*41/10*g1**3, k*(-19/6)*g2**3, k*(-7)*g3**3, k*yt*(4.5*yt**2 - 8*g3**2 - 9/4*g2**2 - 17/20*g1**2)]
    s2d = solve_ivp(rge_down, [math.log(MPL), math.log(mt)], [gPl[0], gPl[1], gPl[2], yt_hi], rtol=1e-10, atol=1e-13)
    ytIR = float(s2d.y[3, -1]); mt_fp = ytIR*v/math.sqrt(2)
    R['R6'][str(yt_hi)] = status(mt_fp, mt, math.hypot(dmt, 0.03*mt_fp), f"y_t(M_Pl) = {yt_hi}: fixed-point m_t (tree) vs m_t")
    R['R6'][str(yt_hi)]['yt_IR'] = ytIR

# ---------------------------------------------------------------- R7 Veltman condition
log("\nR7 Veltman condition")
mHV = math.sqrt(4*mt**2 - 2*MW**2 - MZ**2)
R['R7_veltman'] = status(mHV, mH, math.hypot(dmH, 4*mt*dmt/mHV), "m_H from 4 m_t^2 - 2 M_W^2 - M_Z^2 vs M_h")

# ---------------------------------------------------------------- R8 the Cabibbo angle from Delta(6 7^2): pi/14
log("\nR8 theta_C = pi/14 (Delta(6 7^2))")
Vus, dVus = D['Vus']; thC = math.degrees(math.asin(Vus)); dthC = math.degrees(dVus/math.sqrt(1 - Vus**2))
R['R8_pi14'] = status(180/14, thC, dthC, "pi/14 (deg) vs theta_C")

# ---------------------------------------------------------------- R9 Froggatt-Nielsen exponents (structure; base rate)
log("\nR9 Froggatt-Nielsen exponents log_lambda of the six mass ratios (lambda = |V_us|)")
ex = {k: math.log(r)/math.log(Vus) for k, r in dict(u_t=M['u']/mt, c_t=M['c']/mt, d_b=M['d']/M['b'], s_b=M['s']/M['b'], e_tau=D['me_Z']/D['mtau_Z'], mu_tau=D['mmu_Z']/D['mtau_Z']).items()}
near = sum(1 for x in ex.values() if abs(x - round(x)) <= 0.2)
R['R9_FN'] = dict(exponents=ex, within_0p2_of_integer=near, of=6, base_rate_each=0.4, status="STRUCTURE")
log("   " + ", ".join(f"{k} {x:.2f}" for k, x in ex.items()) + f"; within 0.2 of an integer: {near} of 6 (base rate 0.4 each; binomial expectation 2.4)")

# ---------------------------------------------------------------- R10 b-tau unification (one loop, SM; MSSM with tan beta)
log("\nR10 b-tau unification at 2e16 GeV, one loop")
def btau_SM():
    sS = solve_ivp(rge_SM, [math.log(mt), math.log(2e16)], [g10, g20, g30, yt0, yb0, ytau0, lam0], rtol=1e-10, atol=1e-13)
    return float(sS.y[4, -1]/sS.y[5, -1])
def btau_MSSM(tanb):
    beta = math.atan(tanb)
    def rge_MSSM(t, y):
        g1, g2, g3, yt, yb, ytau = y; k = 1/(16*math.pi**2)
        return [k*33/5*g1**3, k*g2**3, k*(-3)*g3**3,
                k*yt*(6*yt**2 + yb**2 - 16/3*g3**2 - 3*g2**2 - 13/15*g1**2),
                k*yb*(6*yb**2 + yt**2 + ytau**2 - 16/3*g3**2 - 3*g2**2 - 7/15*g1**2),
                k*ytau*(4*ytau**2 + 3*yb**2 - 3*g2**2 - 9/5*g1**2)]
    sS = solve_ivp(rge_SM, [math.log(mt), math.log(MSUSY)], [g10, g20, g30, yt0, yb0, ytau0, lam0], rtol=1e-10, atol=1e-13)
    g1, g2, g3, yt, yb, ytau = sS.y[:6, -1]
    sM = solve_ivp(rge_MSSM, [math.log(MSUSY), math.log(2e16)], [g1, g2, g3, yt/math.sin(beta), yb/math.cos(beta), ytau/math.cos(beta)], rtol=1e-10, atol=1e-13)
    return float(sM.y[4, -1]/sM.y[5, -1])
R['R10'] = dict(ratio_MZ=M['b']/D['mtau_Z'], SM=btau_SM(), MSSM={str(tb): btau_MSSM(tb) for tb in (3, 10, 50)}, status="FIT (tan beta is a continuous input of the MSSM)")
log(f"   m_b/m_tau at M_Z {R['R10']['ratio_MZ']:.3f}; at 2e16 GeV: SM {R['R10']['SM']:.3f}; MSSM tan beta 3/10/50: " + ", ".join(f"{k}: {x:.3f}" for k, x in R['R10']['MSSM'].items()))

# ---------------------------------------------------------------- R11 the massless-up solution of strong CP (the data alone)
log("\nR11 m_u = 0?")
R['R11_mu_zero'] = status(0.0, D['mu2'][0], D['mu2'][1], "m_u = 0 vs m_u(2 GeV)")

# ---------------------------------------------------------------- the ledger: dof bought, prices, hypothesis sets
log("\nTHE LEDGER")
rows = [
 # name, dof (which of the 19), status key, price (list; empty = none), fitted continuous parameter in the relation?, hypothesis set
 dict(name="gauge unification (SU(5) 3/8 + MSSM content)", dof=["g_i: one relation among three"], status=R['R4']['MSSM']['status'], price=["a GUT group", "the particle content to M_GUT (TeV supersymmetry)", "thresholds"], fitted=False, hyp="SUSY GUT"),
 dict(name="gauge unification (SM content)", dof=["g_i: one relation among three"], status=R['R4']['SM']['status'], price=["a GUT group"], fitted=False, hyp="non-SUSY GUT"),
 dict(name="Koide (pole masses)", dof=["m_tau given m_e, m_mu"], status=R['R1_koide_pole']['status'], price=[], fitted=False, hyp="none (no accepted mechanism)"),
 dict(name="Gatto-Sartori-Tonin", dof=["theta_C"], status=R['R2_gst']['status'], price=["a texture zero in the (1,1) entries"], fitted=False, hyp="texture zeros"),
 dict(name="the same texture: |V_cb| = sqrt(m_s/m_b)", dof=["|V_cb|"], status=R['R2_texture_Vcb']['status'], price=["a texture zero in the (1,1) entries"], fitted=False, hyp="texture zeros"),
 dict(name="Georgi-Jarlskog m_mu = 3 m_s", dof=["m_s given m_mu (and m_b, m_tau)"], status=R['R3_gj_mu_s']['status'], price=["a Higgs with a colour-charged component (45 of SU(5) or (15,2,2))", "a GUT group", "running"], fitted=False, hyp="SUSY GUT"),
 dict(name="Georgi-Jarlskog m_e = m_d/3", dof=["m_d given m_e (and m_b, m_tau)"], status=R['R3_gj_e_d']['status'], price=["a Higgs with a colour-charged component", "a GUT group", "running"], fitted=False, hyp="SUSY GUT"),
 dict(name="criticality / asymptotic safety: lambda(M_Pl) = 0", dof=["m_H"], status=R['R5']['direct']['status'], price=["no new physics to M_Planck", "one UV boundary condition"], fitted=False, hyp="SM to M_Planck"),
 dict(name="quasi-infrared fixed point of y_t", dof=["y_t"], status=R['R6']['3.0']['status'], price=["a large top Yukawa at M_Planck"], fitted=False, hyp="SM to M_Planck"),
 dict(name="Veltman condition", dof=["m_H"], status=R['R7_veltman']['status'], price=["cancellation of the one-loop quadratic divergence"], fitted=False, hyp="none"),
 dict(name="theta_C = pi/14 from Delta(6 7^2)", dof=["theta_C"], status=R['R8_pi14']['status'], price=["a finite group of order 294 and a residual symmetry"], fitted=False, hyp="finite flavour group"),
 dict(name="Froggatt-Nielsen powers", dof=["the six light mass ratios"], status="STRUCTURE", price=["a U(1) charge per field", "lambda", "O(1) coefficients"], fitted=True, hyp="FN"),
 dict(name="b-tau unification", dof=["m_b given m_tau"], status="FIT", price=["a GUT group", "the MSSM with tan beta"], fitted=True, hyp="SUSY GUT"),
 dict(name="theta-bar = 0 by a mechanism (PQ, Nelson-Barr, weight-zero determinants)", dof=["theta-bar"], status="HOLDS", price=["a new U(1) and particle, or spontaneous CP with vector-like quarks, or CP + SUSY + reducible representations with chosen weights"], fitted=False, hyp="strong CP mechanism"),
 dict(name="theta-bar = 0 by m_u = 0", dof=["theta-bar"], status=R['R11_mu_zero']['status'], price=[], fitted=False, hyp="massless up"),
 dict(name="modular fits near fixed points / the cusp", dof=["the mass ratios and mixing of a sector"], status="FIT", price=["a finite modular group", "tau", "O(1) coefficients"], fitted=True, hyp="modular flavour"),
]
counted = {}
for r in rows:
    r['buys'] = (r['status'] in ('HOLDS', 'APPROXIMATE')) and not r['fitted']
    if r['buys']:
        for d in r['dof']: counted.setdefault(d, []).append(r['name'])
# the dof bought: unify synonyms (theta_C counted once; theta-bar once)
dof_bought = sorted(counted)
T1 = len(dof_bought)
T2 = [r['name'] for r in rows if r['status'] == 'HOLDS' and not r['price'] and not r['fitted']]
hyps = {}
for r in rows:
    if r['buys']:
        for d in r['dof']: hyps.setdefault(r['hyp'], set()).add(d)
T3 = max((len(v) for v in hyps.values()), default=0); T3_set = max(hyps, key=lambda h: len(hyps[h])) if hyps else None
T4 = 19 - T1
for r in rows: log(f"   {r['name']:72s} {r['status']:12s} buys {r['buys']!s:5s} price {'; '.join(r['price']) or '(none)'}")
log(f"\n   dof bought (T1) = {T1}: {dof_bought}")
log(f"   HOLDS with an empty price (T2) = {len(T2)}: {T2}")
log(f"   largest dof count of one hypothesis set (T3) = {T3} ({T3_set}: {sorted(hyps.get(T3_set, []))})")
log(f"   dof not bought (T4) = {T4}")

# ---------------------------------------------------------------- the cells
cells = {}
cells['C0'] = dict(holds=all(abs(x) < 0.025 for x in ctrl.values()) and abs(R['R1_koide_pole']['value'] - 2/3) < 1e-4, detail=dict(control_vs_HZ=ctrl), predicted="this running on Huang-Zhou's inputs within 2.5% of their table for every flavour; Koide within 1e-4")
cells['T1'] = dict(holds=4 <= T1 <= 8, value=T1, predicted="4..8")
cells['T2'] = dict(holds=len(T2) == 1 and T2[0].startswith("Koide"), value=T2, predicted="exactly one: Koide")
cells['T3'] = dict(holds=T3 <= 3, value=T3, predicted="<= 3")
cells['T4'] = dict(holds=T4 >= 11, value=T4, predicted=">= 11")
cells['T5'] = dict(holds=abs(R['R1_koide_pole']['value'] - 2/3) < 2e-5 and abs(R['R1_koide_pole']['mtau_pull']) < 2 and abs(R['R1_koide_MZ']['dev']) > 5e-4,
                   value=dict(Qpole=R['R1_koide_pole']['value'], mtau_pull=R['R1_koide_pole']['mtau_pull'], QMZ=R['R1_koide_MZ']['value']), predicted="|Q-2/3| < 2e-5, m_tau pull < 2, |Q(M_Z)-2/3| > 5e-4")
cells['T6'] = dict(holds=abs(R['R2_gst']['pull']) <= 2 and R['R2_texture_Vcb']['value']/D['Vcb'][0] > 2, value=dict(gst_pull=R['R2_gst']['pull'], Vcb_ratio=R['R2_texture_Vcb']['value']/D['Vcb'][0]), predicted="GST pull <= 2; texture |V_cb| off by > 2x")
cells['T7'] = dict(holds=R['R4']['SM']['spread_decades'] >= 1.5 and R['R4']['MSSM']['spread_decades'] <= 0.6 and abs(R['R4']['MSSM']['rel']) <= 0.02 and abs(R['R4']['SM']['rel']) >= 0.05,
                   value=dict(SM_spread=R['R4']['SM']['spread_decades'], MSSM_spread=R['R4']['MSSM']['spread_decades'], MSSM_rel=R['R4']['MSSM']['rel'], SM_rel=R['R4']['SM']['rel']), predicted="SM spread >= 1.5; MSSM spread <= 0.6; MSSM sin^2 within 2%; SM off by >= 5%")
cells['T8'] = dict(holds=1.0 <= R['R5']['direct']['gap_GeV'] <= 6.0 and (cross is not None), value=dict(gap=R['R5']['direct']['gap_GeV'], one_loop_zero_log10=cross), predicted="gap in [1, 6] GeV; one-loop lambda crosses zero below M_Pl")
cells['T9'] = dict(holds=all(R['R6'][k]['rel'] > 0.15 for k in R['R6']), value={k: R['R6'][k]['rel'] for k in R['R6']}, predicted="fixed-point m_t above the data by > 15% for every y_t(M_Pl)")
cells['T10'] = dict(holds=abs(R['R3_gj_mu_s']['rel']) <= 0.10 and abs(R['R3_gj_e_d']['rel']) > 0.10, value=dict(gj1=R['R3_gj_mu_s']['value'], gj2=R['R3_gj_e_d']['value']), predicted="m_mu/m_s double ratio within 10% of 3; the m_e/m_d one outside 10%")
cells['T11'] = dict(holds=R['R10']['SM'] < 0.8 and all(0.8 <= x <= 1.0 for x in R['R10']['MSSM'].values()), value=dict(SM=R['R10']['SM'], MSSM=R['R10']['MSSM']), predicted="SM ratio < 0.8 at 2e16; MSSM in [0.8, 1.0] at one loop for tan beta 3, 10, 50")
all_hold = all(c['holds'] for c in cells.values())
log("\nCELLS")
for k, c in cells.items(): log(f"   {k}: {'HOLDS' if c['holds'] else 'FAILS'}  value {json.dumps(c.get('value'), default=float)[:200]}  (predicted {c.get('predicted')})")
log(f"all_hold {all_hold}  [{time.time() - T0:.0f}s]")
def conv(o):
    if isinstance(o, (np.floating, np.integer)): return float(o)
    if isinstance(o, set): return sorted(o)
    if isinstance(o, np.ndarray): return o.tolist()
    return str(o)
json.dump(dict(data=D, masses_MZ=M, relations=R, ledger=rows, dof_bought=dof_bought, T2=T2, hypothesis_sets={k: sorted(v) for k, v in hyps.items()}, cells=cells, all_hold=all_hold, seconds=time.time() - T0),
          open(OUT, "w"), indent=1, default=conv)
LOG.close()
