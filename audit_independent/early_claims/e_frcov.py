"""(e) Theorems 3, 4, Gate 0 / FR-COV.
- Theorem 4: DR.DR vs eta^6 with MAIN's DR (B1691 te.B[1], via cm_zero_line.direction) and with agy's normalisation.
- FR-COV: add a scalar a0*I to the (reading-transformed) Higgs at the B1825 address, using main's coupling(); compare
  agy's hard-coded h, m vectors with mine; scan the a0 plane: chi2 over the 8 quark observables, the flip criterion
  (|V_ub|/|V_td| < 1 and sin delta > 0.5), and the best chi2 reachable with this 2-real-parameter freedom."""
import json, math, pathlib, sys
from fractions import Fraction as Fr
import numpy as np
import mpmath as mp

ROOT = pathlib.Path("/Users/dri/.gemini/antigravity/scratch/origin-axiom-independent-audit")
OUT = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "frontier/B1821_the_frames_mirror_symmetry_in_re_tau/verification"))
import cm_zero_line as Z
M_ = Z.mods(); B = M_["B"]
res = {}

# ---- Theorem 4
mp.mp.dps = 30
for tau in (complex(0.093359375, 2.742578125), complex(0.3, 1.1), complex(-0.2, 0.8)):
    DR = Z.direction("DR", tau); R = Z.direction("R", tau)
    q = mp.exp(1j*mp.pi*mp.mpc(tau.real, tau.imag))
    th2, th3, th4 = (complex(mp.jtheta(k, 0, q)) for k in (2, 3, 4))
    eta3 = th2*th3*th4/2
    drdr = sum(x*x for x in DR); rr = sum(x*x for x in R)
    Ragy = np.array([-th2**2, -th4**2, 1j*th3**2])/(th2*th3*th4)
    res.setdefault("thm4", []).append({"tau": [tau.real, tau.imag], "R.R(main)": abs(rr), "|R_main/R_agy| componentwise": (np.abs(np.array(R)/Ragy)).tolist(),
                                       "DR.DR(main)/eta^6": complex(drdr/eta3**2), "pi^2 * DR.DR(main)/eta^6": complex(math.pi**2*drdr/eta3**2)})
print(json.dumps(res["thm4"], indent=1, default=str))

# ---- FR-COV at the B1825 address
tau = complex(0.093359375, 2.742578125); line = (Fr(3, 8), Fr(3, 8)); reading = (1, 1, 0)
Lmax, L2 = Z.radii(tau); a = Z.direction("DR", tau)
sec = {}
for (sn, ql, qr), r in zip(Z.SECTORS, reading):
    w = B.line_w(line[0], line[1], tau); x, yy = B.sector_twists(w, tau, ql, qr)
    R = B.residues(x, yy, tau); c = B.cA(x, yy, tau, R)
    S = a[0]*B.QI + a[1]*B.QJ + a[2]*B.QK
    if r: S = B.EPS @ S.conj() @ B.EPS.T
    u = {k: (math.sqrt(2*math.pi*L2 + c[k])*R[k] if c[k] is not None and 2*math.pi*L2 + c[k] > 0 else 0) for k in B.UNITS}
    sec[sn] = (S, B.weighted_M(u), u)
def hvec(S):
    basis = [np.eye(2), B.QI, B.QJ, B.QK]; A = np.array([b.flatten() for b in basis]).T
    c = np.linalg.lstsq(A, S.flatten(), rcond=None)[0]; return c
cu = hvec(sec["up"][0]); my_h = np.array([cu[2], cu[1], cu[3]])
agy_h = np.array([0.3594460736539532 + 0.026026644987911976j, -0.03856855412812964 + 0.0028331111016811515j, -0.026594553687845735 + 0.3569061299455392j])
agy_m1u = -0.5849058859703657 + 0.012492790220353949j
res["agy_hardcoded_h_vs_mine_maxdiff"] = float(np.abs(my_h - agy_h).max())
res["agy_hardcoded_m1u_vs_mine"] = abs(sec["up"][2]["1"] - agy_m1u)
res["|h|"] = float(np.linalg.norm(my_h))
print("h diff", res["agy_hardcoded_h_vs_mine_maxdiff"], "m1u diff", res["agy_hardcoded_m1u_vs_mine"], "|h|", res["|h|"])

DATA = ROOT / "frontier/B1637_fits_on_the_ruled_branch/received/HZ2021_running_masses_MZ.json"
CKMDATA = ROOT / "frontier/B1612_the_mixing_patterns_the_weave_fixes/verification/data.json"
v = json.loads(DATA.read_text())["masses_GeV"]["value"]; Cd = json.loads(CKMDATA.read_text())["ckm_abs"]["value"]
T8 = np.log(np.array([v["c"]/v["t"], v["u"]/v["t"], v["s"]/v["b"], v["d"]/v["b"], Cd[0][1], Cd[1][2], Cd[0][2], 3.12e-5]))
sig = np.array(json.loads((ROOT / "scripts/stepb/sigma/SIGMA_ONLY.json").read_text())["sigma_natural_log"])
S8 = np.concatenate([sig[:4], sig[6:10]])

def obs(a0):
    Us = {}; ms = {}
    for sn in ("up", "down"):
        S, Mm, _ = sec[sn]
        Y = B.coupling(S + a0*np.eye(2), Mm)
        U, s, _ = np.linalg.svd(Y); o = np.argsort(s); s = s[o]; Us[sn] = U[:, o]; ms[sn] = s/s[2]
    V = Us["up"].conj().T @ Us["down"]; A = np.abs(V)
    J = float(np.imag(V[0, 1]*V[1, 2]*np.conj(V[0, 2])*np.conj(V[1, 1])))
    s13 = A[0, 2]; c13 = math.sqrt(1 - s13**2); s12 = A[0, 1]/c13; s23 = A[1, 2]/c13
    sd = abs(J)/(math.sqrt(1 - s12**2)*c13**2*math.sqrt(1 - s23**2)*s12*s13*s23)
    f = np.log(np.array([ms["up"][1], ms["up"][0], ms["down"][1], ms["down"][0], A[0, 1], A[1, 2], A[0, 2], abs(J)]))
    z = (f - T8)/S8
    return {"chi2_8": float(z @ z), "z": z.tolist(), "Vub/Vtd": A[0, 2]/A[2, 0], "sin_delta": sd, "mc/mt": ms["up"][1], "ms/mb": ms["down"][1],
            "mu/mt": ms["up"][0], "md/mb": ms["down"][0], "Vus": A[0, 1], "Vcb": A[1, 2], "Vub": A[0, 2], "J": J}
res["a0=0"] = obs(0.0)
a0_agy = 0.20*np.exp(1j*7*math.pi/8)
res["a0=agy"] = obs(a0_agy)
print("a0=0:", res["a0=0"]); print("a0=agy:", res["a0=agy"])
# scan
grid = []; nflip = 0; ntot = 0; best = (1e99, None)
for rad in np.linspace(0.02, 1.0, 50):
    for ph in np.linspace(0, 2*math.pi, 96, endpoint=False):
        o = obs(rad*np.exp(1j*ph)); ntot += 1
        flip = o["Vub/Vtd"] < 1 and o["sin_delta"] > 0.5
        nflip += flip
        if o["chi2_8"] < best[0]: best = (o["chi2_8"], (float(rad), float(ph)), o)
        if rad <= 0.3: grid.append((float(rad), float(ph), o["chi2_8"], flip))
res["scan"] = {"n": ntot, "fraction_flip(|a0|<=1)": nflip/ntot, "best_chi2_8": best[0], "best_a0(|a0|,phase)": best[1], "best_obs": best[2],
               "flip_fraction_|a0|<=0.3": sum(g[3] for g in grid)/len(grid)}
print("scan:", res["scan"])
json.dump(res, open(OUT / "e_frcov.json", "w"), indent=1, default=str)
