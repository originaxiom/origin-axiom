"""RECOGNITION CONTROL R1 (B1827; main, 2026-11-03; the owner's 'could we identify the answer if we ever get to it').
A positive control of THE TEST, not of the frame: no frame output enters.  If a theory gave the ten EXACTLY right at a high
scale Lambda, B1825's test (tree-level comparison at M_Z, no running) would score nature-at-Lambda against nature-at-M_Z.
This script runs the measured ten (the test's own inputs: HZ2021's MS-bar masses at M_Z and the CKM moduli of B1612's
data.json, J = 3.12e-5 as B1825 pinned) up with the Standard Model's ONE-LOOP RGEs (full 3x3 Yukawa matrices, gauge
couplings with b = (41/10, -19/6, -7), g1 in GUT normalisation) and reports chi2_ten, chi2_six, chi2_4 against the M_Z values
with B1825's sigma-only file, and the misfit's price on K, chi2/2 log2(e) bits (compression.misfit_bits).
Disclosed inputs beyond the test's: alpha_s(M_Z) = 0.1179, 1/alpha(M_Z) = 127.951, sin^2 theta_W(M_Z) = 0.23121 (MS-bar),
v = 246 GeV (HZ2021's scheme).  One loop; two-loop and threshold effects move the ratios by a few per cent (not computed).
Convention: L = -Qbar Y_u u_R H~ - Qbar Y_d d_R H - Lbar Y_e e_R H; left-handed rotations from Y Y^dagger;
16 pi^2 dY_u/dt = [3/2 (Y_u Y_u^+ - Y_d Y_d^+) + T - (17/20 g1^2 + 9/4 g2^2 + 8 g3^2)] Y_u, likewise d (1/4 g1^2) and e
(3/2 Y_e Y_e^+, 9/4 g1^2 + 9/4 g2^2), T = Tr(3 Y_u Y_u^+ + 3 Y_d Y_d^+ + Y_e Y_e^+)."""
import json, math, pathlib
import numpy as np
ROOT = pathlib.Path(__file__).resolve().parents[4]
M = json.loads((ROOT / "frontier/B1637_fits_on_the_ruled_branch/received/HZ2021_running_masses_MZ.json").read_text())["masses_GeV"]["value"]
CK = json.loads((ROOT / "frontier/B1612_the_mixing_patterns_the_weave_fixes/verification/data.json").read_text())["ckm_abs"]["value"]
SIG = np.array(json.loads((ROOT / "scripts/stepb/sigma/SIGMA_ONLY.json").read_text())["sigma_natural_log"])
J0, MZ, V = 3.12e-5, 91.1876, 246.0
a_s, a_inv, s2w = 0.1179, 127.951, 0.23121
e2 = 4 * math.pi / a_inv
g = np.array([math.sqrt(5 / 3 * e2 / (1 - s2w)), math.sqrt(e2 / s2w), math.sqrt(4 * math.pi * a_s)])
b = np.array([41 / 10, -19 / 6, -7.0])

def ckm(s12, s23, s13, d):
    c12, c23, c13 = (math.sqrt(1 - x * x) for x in (s12, s23, s13)); e = np.exp(1j * d)
    return np.array([[c12 * c13, s12 * c13, s13 / e],
                     [-s12 * c23 - c12 * s23 * s13 * e, c12 * c23 - s12 * s23 * s13 * e, s23 * c13],
                     [s12 * s23 - c12 * c23 * s13 * e, -c12 * s23 - s12 * c23 * s13 * e, c23 * c13]])
s13 = CK[0][2]; s12 = CK[0][1] / math.sqrt(1 - s13 ** 2); s23 = CK[1][2] / math.sqrt(1 - s13 ** 2)
c12, c23, c13 = (math.sqrt(1 - x * x) for x in (s12, s23, s13))
delta = math.asin(J0 / (c12 * c23 * c13 ** 2 * s12 * s23 * s13))
V0 = ckm(s12, s23, s13, delta)
y = lambda f: math.sqrt(2) * M[f] / V
Yu0 = np.diag([y("u"), y("c"), y("t")]).astype(complex)
Yd0 = V0 @ np.diag([y("d"), y("s"), y("b")]).astype(complex)
Ye0 = np.diag([y("e"), y("mu"), y("tau")]).astype(complex)

def rhs(state):
    Yu, Yd, Ye, gg = state
    Hu, Hd, He = Yu @ Yu.conj().T, Yd @ Yd.conj().T, Ye @ Ye.conj().T
    T = np.real(np.trace(3 * Hu + 3 * Hd + He)); g1, g2, g3 = gg ** 2; k = 1 / (16 * math.pi ** 2); I3 = np.eye(3)
    dYu = k * (1.5 * (Hu - Hd) + (T - 17 / 20 * g1 - 9 / 4 * g2 - 8 * g3) * I3) @ Yu
    dYd = k * (1.5 * (Hd - Hu) + (T - 1 / 4 * g1 - 9 / 4 * g2 - 8 * g3) * I3) @ Yd
    dYe = k * (1.5 * He + (T - 9 / 4 * g1 - 9 / 4 * g2) * I3) @ Ye
    return [dYu, dYd, dYe, k * b * gg ** 3]

def run(mu, n_per_efold=200):
    st = [Yu0.copy(), Yd0.copy(), Ye0.copy(), g.copy()]
    t0, t1 = math.log(MZ), math.log(mu); n = max(1, int(abs(t1 - t0) * n_per_efold)); h = (t1 - t0) / n
    for _ in range(n):
        k1 = rhs(st); k2 = rhs([s + h / 2 * d for s, d in zip(st, k1)]); k3 = rhs([s + h / 2 * d for s, d in zip(st, k2)])
        k4 = rhs([s + h * d for s, d in zip(st, k3)])
        st = [s + h / 6 * (a + 2 * bb + 2 * c + d) for s, a, bb, c, d in zip(st, k1, k2, k3, k4)]
    return st

def ten(st):
    Yu, Yd, Ye, gg = st
    def left(Y):
        w, U = np.linalg.eigh(Y @ Y.conj().T); return np.sqrt(np.maximum(w, 0)), U
    mu_, Uu = left(Yu); md, Ud = left(Yd); me, _ = left(Ye)
    Vc = Uu.conj().T @ Ud
    J = np.imag(Vc[0, 1] * Vc[1, 2] * np.conj(Vc[0, 2]) * np.conj(Vc[1, 1]))
    q = [mu_[1] / mu_[2], mu_[0] / mu_[2], md[1] / md[2], md[0] / md[2], me[1] / me[2], me[0] / me[2],
         abs(Vc[0, 1]), abs(Vc[1, 2]), abs(Vc[0, 2]), abs(J)]
    return np.log(np.array(q)), dict(mt=mu_[2] * V / math.sqrt(2), mb=md[2] * V / math.sqrt(2), mtau=me[2] * V / math.sqrt(2), g=gg)

f0, x0 = ten(run(MZ))
LOG2E = math.log2(math.e)
names = ["c/t", "u/t", "s/b", "d/b", "mu/tau", "e/tau", "|V_us|", "|V_cb|", "|V_ub|", "|J|"]
print("check at M_Z (should equal the inputs): J %.3e  |V_ub| %.5f  m_t %.2f" % (math.exp(f0[9]), math.exp(f0[8]), x0["mt"]))
out = {"inputs": {"alpha_s": a_s, "alpha_inv": a_inv, "sin2w": s2w, "v": V, "J": J0, "delta_rad": delta}, "scales": []}
for mu in (1e3, 1e6, 1e9, 1e12, 2e16, 1.2e19):
    f, x = ten(run(mu)); pull = (f - f0) / SIG
    c10, c6, c4 = float(pull @ pull), float(pull[:6] @ pull[:6]), float(pull[6:] @ pull[6:])
    row = {"mu_GeV": mu, "shift_percent": {n: round(100 * (math.exp(d) - 1), 2) for n, d in zip(names, f - f0)},
           "pulls": dict(zip(names, np.round(pull, 3).tolist())), "chi2_ten": c10, "chi2_six": c6, "chi2_four": c4,
           "K_price_bits_ten": c10 / 2 * LOG2E, "m_t": x["mt"], "m_b": x["mb"], "m_tau": x["mtau"], "mb_over_mtau": x["mb"] / x["mtau"],
           "g1g2g3": x["g"].tolist()}
    out["scales"].append(row)
    print("mu %.1e GeV: chi2_ten %6.2f (six %5.2f, four %5.2f); K price %5.2f bits | m_t %.1f m_b %.3f m_tau %.3f m_b/m_tau %.3f | shifts %%: %s" % (
        mu, c10, c6, c4, row["K_price_bits_ten"], x["mt"], x["mb"], x["mtau"], row["mb_over_mtau"],
        " ".join("%s %+.1f" % (n, s) for n, s in row["shift_percent"].items())))
pathlib.Path(__file__).with_suffix(".json").write_text(json.dumps(out, indent=1))
