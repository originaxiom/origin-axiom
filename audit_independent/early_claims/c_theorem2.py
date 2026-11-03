"""(c) Theorem 2 checks with main's primitives (b1656_funcs via cm_zero_line) but my own algebra.
1. Is the Yukawa identity a generic bilinear identity? test on random complex S, M.
2. full 3x3 CKM at the B1825 best address and three other benchmark points; |V_td|, ratios, sin(delta).
3. theta12^(s) = |<u2^(s), h*hat>| etc.
4. Is the (0.7347,0.7347,1.3611) 'proof' just a least-norm solution of a linear constraint?"""
import json, math, pathlib, sys, itertools
from fractions import Fraction as Fr
import numpy as np

ROOT = pathlib.Path("/Users/dri/.gemini/antigravity/scratch/origin-axiom-independent-audit")
OUT = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "frontier/B1821_the_frames_mirror_symmetry_in_re_tau/verification"))
import cm_zero_line as Z
M_ = Z.mods(); B = M_["B"]
rng = np.random.default_rng(1)
res = {}

def skew(v):
    return np.array([[0, -v[2], v[1]], [v[2], 0, -v[0]], [-v[1], v[0], 0]])

def decomp(S):
    """S = s1 I + sI QI + sJ QJ + sK QK  (complex coefficients)"""
    basis = [np.eye(2), B.QI, B.QJ, B.QK]
    A = np.array([b.flatten() for b in basis]).T
    c, *_ = np.linalg.lstsq(A, S.flatten(), rcond=None)
    return c

# 1. generic identity: Y = coupling(S, weighted_M(u)) with S having no identity part
worst = 0.0; worst4 = 0.0; worst_hh = 0.0
for _ in range(200):
    aI, aJ, aK, a0 = rng.normal(size=4) + 1j*rng.normal(size=4)
    u = {k: complex(rng.normal() + 1j*rng.normal()) for k in B.UNITS}
    S = aI*B.QI + aJ*B.QJ + aK*B.QK
    Y = B.coupling(S, B.weighted_M(u))
    h = np.array([aJ, aI, aK]); m1 = u["1"]; m = np.array([u["j"], u["i"], u["k"]])
    pred = np.outer(h, m) + np.outer(m, h) - (h @ m)*np.eye(3) - m1*skew(h)
    sgn = min(np.abs(Y - pred).max(), np.abs(Y - (np.outer(h, m) + np.outer(m, h) - (h @ m)*np.eye(3) + m1*skew(h))).max())
    worst = max(worst, np.abs(Y - pred).max())
    worst_hh = max(worst_hh, np.abs(Y @ h - (h @ h)*m).max(), np.abs(Y.T @ h - (h @ h)*m).max())
    # 4D: add a0 I  (Theorem 3 / FR-COV formula)
    S4 = S + a0*np.eye(2)
    Y4 = B.coupling(S4, B.weighted_M(u))
    pred4 = np.outer(h, m) + np.outer(m, h) - (h @ m)*np.eye(3) + a0*m1*np.eye(3) - skew(m1*h + a0*m)
    worst4 = max(worst4, np.abs(Y4 - pred4).max())
    res.setdefault("det_check", []).append(abs(np.linalg.det(Y4) - (a0**2 + h @ h)*(m1**2 + m @ m)*(a0*m1 + h @ m)) / max(1, abs(np.linalg.det(Y4))))
res["identity_3D_max_abs_err_random"] = float(worst)
res["Yh_eq_hh_m_max_err_random"] = float(worst_hh)
res["identity_4D_max_abs_err_random"] = float(worst4)
res["theorem3_det_factorization_max_rel_err_random"] = float(max(res.pop("det_check")))
print({k: res[k] for k in list(res)})

def build(line, tau, dname, rad, reading):
    Lmax, L2 = Z.radii(tau); L = Lmax if rad == "L_max" else L2
    a = Z.direction(dname, tau); out = {}
    for (sn, ql, qr), r in zip(Z.SECTORS, reading):
        w = B.line_w(line[0], line[1], tau); x, yy = B.sector_twists(w, tau, ql, qr)
        R = B.residues(x, yy, tau); c = B.cA(x, yy, tau, R)
        S = a[0]*B.QI + a[1]*B.QJ + a[2]*B.QK
        if r: S = B.EPS @ S.conj() @ B.EPS.T
        u = {k: (math.sqrt(2*math.pi*L + c[k])*R[k] if c[k] is not None and 2*math.pi*L + c[k] > 0 else 0) for k in B.UNITS}
        out[sn] = (B.coupling(S, B.weighted_M(u)), S, u, R)
    return out

def svd_sorted(Y):
    U, s, Vh = np.linalg.svd(Y); o = np.argsort(s); return U[:, o], s[o]

def analyse(label, line, tau, dname, rad, reading):
    Ys = build(line, tau, dname, rad, reading)
    Uu, su = svd_sorted(Ys["up"][0]); Ud, sd = svd_sorted(Ys["down"][0])
    V = Uu.conj().T @ Ud; A = np.abs(V)
    J = float(np.imag(V[0, 1]*V[1, 2]*np.conj(V[0, 2])*np.conj(V[1, 1])))
    s13 = A[0, 2]; c13 = math.sqrt(1 - s13**2); s12 = A[0, 1]/c13; s23 = A[1, 2]/c13
    c12 = math.sqrt(1 - s12**2); c23 = math.sqrt(1 - s23**2)
    Jmax = c12*c13**2*c23*s12*s13*s23
    d = {"label": label, "absV": A.round(6).tolist(), "J": J, "sin_delta": abs(J)/Jmax,
         "Vub_over_VusVcb": A[0, 2]/(A[0, 1]*A[1, 2]), "Vtd_over_VusVcb": A[2, 0]/(A[0, 1]*A[1, 2]), "Vub_over_Vtd": A[0, 2]/A[2, 0],
         "mass_up": (su/su[2]).tolist(), "mass_down": (sd/sd[2]).tolist()}
    # Higgs vector: decompose the (possibly conjugated) S per sector; h = (sJ, sI, sK)
    th = {}
    for sn, U_ in (("up", Uu), ("down", Ud)):
        c = decomp(Ys[sn][1]); h = np.array([c[2], c[1], c[3]])
        r = abs(h @ h)/np.vdot(h, h).real
        hs = h.conj()/np.linalg.norm(h)
        th[sn] = {"identity_coef": abs(c[0]), "r_nullity": r, "|<u1,h*>|": abs(np.vdot(U_[:, 0], hs)), "|<u2,h*>|": abs(np.vdot(U_[:, 1], hs)),
                  "|<u3,h*>|": abs(np.vdot(U_[:, 2], hs)), "|<u1,h>|": abs(np.vdot(U_[:, 0], h/np.linalg.norm(h)))}
        # identity check on the real point
        u = Ys[sn][2]; m1 = u["1"]; m = np.array([u["j"], u["i"], u["k"]])
        pred = np.outer(h, m) + np.outer(m, h) - (h @ m)*np.eye(3) - m1*skew(h)
        th[sn]["identity_err_rel"] = float(np.abs(Ys[sn][0] - pred).max()/np.abs(Ys[sn][0]).max())
        R = Ys[sn][3]; th[sn]["R_null_4D"] = abs(sum(R[k]**2 for k in B.UNITS))/sum(abs(R[k])**2 for k in B.UNITS)
    d["higgs_alignment"] = th
    d["theta12u_over_theta12d"] = th["up"]["|<u2,h*>|"]/th["down"]["|<u2,h*>|"]
    print(json.dumps(d, indent=1, default=float)); return d

pts = [("B1825 best", (Fr(3, 8), Fr(3, 8)), complex(0.093359375, 2.742578125), "DR", "L_2", (1, 1, 0)),
       ("B1726 best nine (agy's spec, B1821 convention)", (Fr(2, 5), Fr(1, 10)), complex(0.55, 2.55), "DR", "L_max", (1, 1, 1)),
       ("P-377 strip (agy's spec)", (Fr(2, 5), Fr(1, 10)), complex(0.45, 3.0), "DR", "L_max", (1, 1, 1)),
       ("B1743 F_6 (agy's spec)", (Fr(2, 5), Fr(3, 10)), complex(0.3125, 3.3), "F_6", "L_max", (0, 0, 0))]
res["points"] = [analyse(*p) for p in pts]

# 4. the 'Lagrange compromise': least-norm solution of x13 - x12 - x23 = L
Vus, Vcb, Vub = 0.22501, 0.04183, 0.003732
L = math.log(Vus*Vcb/Vub); x = L/3*np.array([-1, -1, 1])
res["lagrange"] = {"ratio": Vus*Vcb/Vub, "solution_exp": np.exp(x).tolist(),
                   "check_B1743_r13/(r12 r23)": 1.213/(0.773*0.775), "check_P377_r13/(r12 r23)": 1.545/(0.692*0.761)}
print(res["lagrange"])
json.dump(res, open(OUT / "c_theorem2.json", "w"), indent=1, default=float)
