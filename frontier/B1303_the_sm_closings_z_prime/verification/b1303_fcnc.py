"""B1303 Q2 -- the FCNC regime of sm:B1283's Z', computed from Langacker-Pluemacher's own equations (hep-ph/0001204, read in full;
DESIGN sealed 9f44f4c3). Nothing here is a literature number: eq. (41) is re-evaluated with current inputs to reproduce eq. (54)
(the convention control), then eqs. (54)-(56) are applied to the record's charge table under the two cases the record cannot
decide between (which family character carries the third family). Outputs M_Z'/g_2 floors in TeV. PASS/FAIL per DESIGN Q2."""
import json, math, sys
fails = []
def check(label, ok):
    print(("  [PASS] " if ok else "  [FAIL] ") + label)
    if not ok: fails.append(label)

# ---------------- inputs (PDG 2024 Review of Particle Physics; FLAG 2024 for f_K) ----------------
GF = 1.1663788e-5          # GeV^-2
mK = 0.497611              # GeV  (K0)
dmK = 3.484e-12 * 1e-3     # GeV  ((3.484 +- 0.006) x 10^-12 MeV)
fK_156 = 0.1557            # GeV  (FLAG N_f = 2+1+1, the f_pi = 130 MeV convention)
fK_110 = 0.1557 / math.sqrt(2)   # the f_pi = 92 MeV convention (LP's F_P follows ref. [30]; the two brackets cover both)
ms, md = 0.0935, 0.00467   # GeV, MSbar at 2 GeV
v = 246.22                 # GeV
mZ = 91.1880
# CKM magnitudes (PDG 2024 global fit)
V = {'ud': 0.97435, 'us': 0.22501, 'ub': 0.003732, 'cd': 0.22487, 'cs': 0.97349, 'cb': 0.04183, 'td': 0.008575, 'ts': 0.04111, 'tb': 0.999118}
LP = dict(K_Re=1e-8, epsK_Im=8e-11, Bd=6e-8, Bs=2e-6, D=1e-7)    # LP eqs. (54), (56), (54), (55), (55): y |Re/Im B^2| < ...

print("=== (a) convention control: LP eq. (41), pure left-handed coupling, against dm_K -> the bound of eq. (54) ===")
def yB2_bound(fK):
    # dm_K = 4 sqrt2 G_F m_K F_K^2 y (1/3) B^2  <  dm_K^exp
    return dmK / (4 * math.sqrt(2) * GF * mK * fK ** 2 / 3)
b156, b110 = yB2_bound(fK_156), yB2_bound(fK_110)
print(f"   y |B_12|^2 < {b156:.3e} (F_K = 155.7 MeV)   |   < {b110:.3e} (F_K = 110.1 MeV)   |   LP eq. (54): < 1e-8")
check("(a) eq. (54)'s 10^-8 reproduces from eq. (41) within a factor 3 in both decay-constant conventions", 5e-9 <= b156 <= 3e-8 and 5e-9 <= b110 <= 3e-8)
# the LR bracket of eq. (41) if both chiralities mix alike (B_L = B_R = B): coefficient of y B^2 is 2/3 - [1/2 + (1/3)(m_K/(m_s+m_d))^2]
lr = 2 / 3 - (0.5 + (mK / (ms + md)) ** 2 / 3)
print(f"   LR bracket if B_L = B_R: {lr:.2f} (vs 1/3 pure-L): the K floor on M_Z' rises by sqrt({abs(lr) / (1/3):.1f}) = {math.sqrt(abs(lr) / (1/3)):.1f}")

print("=== (b) the record's charge table, normalised so that Tr Q'^2 over the three 27s = Tr Y_GUT^2 = 9 ===")
states = {'Q': 6, 'u^c': 3, 'e^c': 1, 'd^c': 3, 'L': 2, 'nu^c': 1, 'N': 1, 'H_u': 2, 'D': 3, 'H_d': 2, 'Dbar': 3}
gen_g = {'Q': -6, 'u^c': -6, 'e^c': -6, 'd^c': -12, 'L': -12, 'nu^c': 0, 'N': 0, 'H_u': -18, 'D': -18, 'H_d': -12, 'Dbar': -12}
gen_h = {'Q': 9, 'u^c': 9, 'e^c': 9, 'd^c': 3, 'L': 3, 'nu^c': 15, 'N': 15, 'H_u': -3, 'D': -3, 'H_d': 3, 'Dbar': 3}
tr = sum(states[m] * gen_g[m] ** 2 for m in states) + 2 * sum(states[m] * gen_h[m] ** 2 for m in states)
Y = {'Q': 1/6, 'u^c': -2/3, 'e^c': 1, 'd^c': 1/3, 'L': -1/2, 'nu^c': 0, 'N': 0, 'H_u': 1/2, 'D': -1/3, 'H_d': -1/2, 'Dbar': 1/3}
trY = 3 * sum(states[m] * (3 / 5) * Y[m] ** 2 for m in states)
s = math.sqrt(trY / tr)
print(f"   Tr Q'^2 (integer table) = {tr};  Tr Y_GUT^2 = {trY:.3f};  scale s = {s:.5f} (DESIGN: sqrt(9/6210) = {math.sqrt(9/6210):.5f})")
check("(b) Tr Q'^2 = 6210 and Tr Y_GUT^2 = 9 on the three 27s", tr == 6210 and abs(trY - 9) < 1e-12)
dq = {m: gen_h[m] - gen_g[m] for m in states}
print(f"   charge differences heavy - VEV'd (integer units): {dq}")
check("(b) the difference is 15 units on Q, u^c, e^c, d^c, L (both quark chiralities and both lepton chiralities)", all(dq[m] == 15 for m in ('Q', 'u^c', 'e^c', 'd^c', 'L')))
de = 15 * s
print(f"   normalised difference De = {de:.4f}")

def floor_TeV(bound, B):
    """y |B|^2 < bound, y = g2^2 v^2 / (4 M^2)  ->  M / g2 > v |B| / (2 sqrt(bound)); in TeV"""
    if B == 0: return 0.0
    return v * abs(B) / (2 * math.sqrt(bound)) / 1000
def case(name, eps):
    """eps = family-basis charges (e1, e2, e3) in normalised units, assuming V_L^d = V_CKM (LP's illustration): B_ij = sum_k V_ik eps_k V_jk^*
    magnitudes: with two equal charges, B_ij = (eps_odd - eps_equal) V_i,odd V_j,odd^*"""
    odd = [k for k in (0, 1, 2) if list(eps).count(eps[k]) == 1][0]
    d = eps[odd] - [e for e in eps if e != eps[odd]][0]
    col = ['d', 's', 'b'][odd]     # the down-type column of the distinguished family (V_L^d = V_CKM: rows u, c, t; columns d, s, b)
    Vcol = {'u': V['u' + col], 'c': V['c' + col], 't': V['t' + col]}
    B12, B13, B23 = d * Vcol['u'] * Vcol['c'], d * Vcol['u'] * Vcol['t'], d * Vcol['c'] * Vcol['t']
    fl = dict(K_dmK=floor_TeV(LP['K_Re'], B12), K_epsK_O1phase=floor_TeV(LP['epsK_Im'], B12), Bd=floor_TeV(LP['Bd'], B13), Bs=floor_TeV(LP['Bs'], B23),
              D_if_CKM_is_up_sector=floor_TeV(LP['D'], B12))   # V_L^d = 1 => V_L^u = V_CKM: the same magnitude appears in B^u_12
    print(f"   {name}: |B_12| = {abs(B12):.3e}, |B_13| = {abs(B13):.3e}, |B_23| = {abs(B23):.3e}")
    print(f"      floors on M_Z'/g_2 [TeV]: " + ", ".join(f"{k} {x:.3g}" for k, x in fl.items()))
    return fl
print("=== (c) Case I: the VEV'd generation is a light family (g = first, and g = second) ===")
c1 = case("g = first family ", (gen_g['Q'] * s, gen_h['Q'] * s, gen_h['Q'] * s))
c2 = case("g = second family", (gen_h['Q'] * s, gen_g['Q'] * s, gen_h['Q'] * s))
print("=== (d) Case II: the VEV'd generation is the third family ===")
c3 = case("g = third family ", (gen_h['Q'] * s, gen_h['Q'] * s, gen_g['Q'] * s))
routesI = [c1['K_dmK'], c1['K_epsK_O1phase'], c1['D_if_CKM_is_up_sector'], c2['K_dmK'], c2['K_epsK_O1phase'], c2['D_if_CKM_is_up_sector']]
check("(c) Case I: every route (dm_K, eps_K with O(1) phase, and the up-sector escape via D mixing) gives M_Z'/g_2 >= 10 TeV", min(routesI) >= 10)
check("(c) Case I: dm_K floor ~ 10^2 TeV and eps_K floor ~ 10^3 TeV (within a factor 3 of 150 and 1500 TeV)", 50 <= c1['K_dmK'] <= 450 and 500 <= c1['K_epsK_O1phase'] <= 4500)
check("(d) Case II: the K floor is empty (< 1 TeV) and both B floors are below 10 TeV -- the fork between the cases is real", c3['K_dmK'] < 1 and c3['Bd'] < 10 and c3['Bs'] < 10)
print("=== (e)/(f) the scale link and the fine-tuning scaling (reported, not derived) ===")
ft = {M: (M * 1e3 / mZ) ** 2 for M in (5, 100, 1000)}
print(f"   LHC universal-coupling benchmarks (ATLAS 2607.28334): Z'_SSM 5.5, Z'_chi 5.1, Z'_psi 4.8 TeV -- the Case II regime")
print(f"   if M_Z' ~ M_soft (radiative U(1)' breaking, LP intro / Cvetic-Langacker): Delta ~ (M_soft/m_Z)^2 = " + ", ".join(f"{M} TeV -> {x:.2g}" for M, x in ft.items()))
json.dump(dict(convention_control=dict(fK156=b156, fK110=b110, LR_bracket=lr), norm=dict(trQ2=tr, trY2=trY, s=s, de=de),
               caseI_first=c1, caseI_second=c2, caseII_third=c3, fine_tuning=ft, fails=fails), open("b1303_fcnc.json", "w"), indent=1)
print("Q2:", "PASS" if not fails else f"FAIL ({len(fails)})")
sys.exit(0 if not fails else 1)
