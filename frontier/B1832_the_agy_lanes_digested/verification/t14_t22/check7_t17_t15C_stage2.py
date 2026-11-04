"""CHECK 7 (agy Theorem 17 Parts B-C, Theorem 15 Part C (commutants), relay section 2 Stage 2 arithmetic, section 6.1 R4).
First principles (mpmath, exact fractions); nothing from the lane imported.

 T17 B.1  sum_f n_f B2({q_f alpha}) over Q(6, 1), u^c(3, -4), d^c(3, 2), L(2, -3), e^c(1, 6): -7/10 at 2/5, -3/10 at 1/5.
 T17 B.2  V0 = -ln(y |eta|^4) and V_ferm = sum n_f (ln|th1(a_f tau)/eta|^2 - 2 pi a_f^2 y) (a_f = {q_f 2/5} centred,
          b_f = 0 as in the lane's code) increasing on Re tau = 1/sqrt5, Im tau in [1, 3.5]; the large-y slope of V_ferm
          against -2 pi sum n_f B2(|a_f|).
 T17 C    theta4^20 + theta2^20 - theta3^20 = -80 eta^12 E4 at 4 points; |F10(rho)| at rho = e^{2 pi i/3}; F10(iy) < 0;
          M w = -w + (4, -2) for M = [[13, -8], [-8, 5]], w = (2/5, 1/5) (so J diag(chi, chi^-1) J^-1 = rho(M gamma)).
 Stage 2  det(A^3 - I) = -16, det(A^3 + I) = 20, (A^3 + I) w = (4, -2), B = (A^3 - I)/4, U B = -I, U w = 2 w mod 1.
 T15 C    dim of the commutant in Sym3(R): C3, S3 -> 2; with V4 = diag sign group: A4, S4 -> 1; |A4| = 12, |S4| = 24.
 6.1 R4   0.01 * 2^13.4.
"""
import itertools, json, math, pathlib
from fractions import Fraction as Fr
import numpy as np
import mpmath as mp

HERE = pathlib.Path(__file__).resolve().parent
out = {}
SM = [("Q", 6, 1), ("u^c", 3, -4), ("d^c", 3, 2), ("L", 2, -3), ("e^c", 1, 6)]
B2 = lambda x: x * x - x + Fr(1, 6)
out["B2_sum"] = {str(a): str(sum(n * B2((q * a) % 1) for _, n, q in SM)) for a in (Fr(2, 5), Fr(1, 5))}

mp.mp.dps = 25
def eta(t):
    q = mp.exp(2j * mp.pi * t); return mp.exp(1j * mp.pi * t / 12) * mp.qp(q)
def th1(z, t):
    return mp.jtheta(1, mp.pi * z, mp.exp(1j * mp.pi * t))
re0 = 1 / mp.sqrt(5); ys = [1 + 0.1 * k for k in range(26)]
af = []
for _, n, q in SM:
    a = (q * Fr(2, 5)) % 1
    if a > Fr(1, 2): a -= 1
    af.append((n, float(a)))
V0, VF = [], []
for y in ys:
    t = mp.mpc(re0, y); e = eta(t)
    V0.append(float(-mp.log(y * abs(e) ** 4)))
    VF.append(float(sum(n * (mp.log(abs(th1(a * t, t) / e) ** 2) - 2 * mp.pi * a * a * y) for n, a in af)))
out["V0_min_step"] = min(np.diff(V0)); out["Vferm_min_step"] = min(np.diff(VF))
out["Vferm_last_slope"] = (VF[-1] - VF[-2]) / 0.1
out["Vferm_asymptotic_slope_pred"] = float(-2 * math.pi * sum(n * float(B2(Fr(abs(a)).limit_denominator(10))) for n, a in af))

def F10(t):
    q = mp.exp(1j * mp.pi * t); t2, t3, t4 = mp.jtheta(2, 0, q), mp.jtheta(3, 0, q), mp.jtheta(4, 0, q)
    E4 = (t2 ** 8 + t3 ** 8 + t4 ** 8) / 2
    return t4 ** 20 + t2 ** 20 - t3 ** 20, -80 * eta(t) ** 12 * E4
pts = [mp.mpc(1 / mp.sqrt(5), (1 + mp.sqrt(5)) ** 2 / 4), mp.mpc(0.25, 1.4), mp.mpc(0, 1.8), mp.mpc(-0.37, 1.1)]
out["F10_identity_rel_err"] = [float(abs(a - b) / abs(b)) for a, b in (F10(t) for t in pts)]
rho = mp.exp(2j * mp.pi / 3); out["F10_at_rho_abs"] = float(abs(F10(rho)[0])); out["F10_scale_near_rho"] = float(abs(F10(rho + 0.05j)[0]))
out["F10_on_imag_axis"] = [complex(F10(mp.mpc(0, y))[0]) for y in (1.0, 1.8, 3.0)]
M = np.array([[13, -8], [-8, 5]]); w = np.array([Fr(2, 5), Fr(1, 5)], dtype=object)
Mw = [sum(M[i, j] * w[j] for j in range(2)) for i in range(2)]
out["Mw_plus_w"] = [str(Mw[i] + w[i]) for i in range(2)]
I2 = np.eye(2, dtype=int)
out["det_A3_minus_I"] = round(np.linalg.det(M - I2)); out["det_A3_plus_I"] = round(np.linalg.det(M + I2))
out["(A3+I)w"] = [str(sum((M + I2)[i, j] * w[j] for j in range(2))) for i in range(2)]
Bm = (M - I2) // 4; U = np.array([[1, 2], [2, 3]])
out["B"] = Bm.tolist(); out["(A3-I) divisible by 4"] = bool(((M - I2) % 4 == 0).all()); out["UB"] = (U @ Bm).tolist()
out["Uw_minus_2w_mod1"] = [str((sum(U[i, j] * w[j] for j in range(2)) - 2 * w[i]) % 1) for i in range(2)]

Pc = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], float); Ps = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 1]], float)
V4 = [np.diag(d) for d in ([1, 1, 1], [1, -1, -1], [-1, 1, -1], [-1, -1, 1])]
basis = []
for i in range(3):
    for j in range(i, 3):
        b = np.zeros((3, 3)); b[i, j] = b[j, i] = 1; basis.append(b)
def comm_dim(gens):
    A = np.column_stack([np.concatenate([(g.T @ b @ g - b).ravel() for g in gens]) for b in basis])
    return int(sum(np.linalg.svd(A, compute_uv=False) < 1e-10))
def gorder(gens):
    els = [np.eye(3)]; fr = list(els)
    while fr:
        nw = []
        for g in fr:
            for s in gens:
                p = g @ s
                if not any(np.allclose(p, h) for h in els): els.append(p); nw.append(p)
        fr = nw
    return len(els)
out["commutant_dims_C3_S3_A4_S4"] = [comm_dim([Pc]), comm_dim([Pc, Ps]), comm_dim([Pc] + V4), comm_dim([Pc, Ps] + V4)]
out["orders_A4_S4"] = [gorder([Pc] + V4), gorder([Pc, Ps] + V4)]
out["R4_0.01*2^13.4"] = 0.01 * 2 ** 13.4
for k, v in out.items():
    print(k, v)
(HERE / "check7_t17_t15C_stage2_out.json").write_text(json.dumps(out, indent=1, default=str))
