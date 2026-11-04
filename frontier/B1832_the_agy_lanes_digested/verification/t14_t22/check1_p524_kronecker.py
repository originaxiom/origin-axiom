"""CHECK 1 (P-524; agy Theorem 19 Part A, Theorem 15 Part B Result 3; P-591 RI-1).  Data-free.  MAIN's code only.

Claim under test (P-524): every normalised channel kernel K_s = P_s/R_s and every c_s depends on the offsets only
through b_x + b_y.  Proof route checked here (first principles, Jacobi's product formula at period 2 tau):

  with s = a_x + a_y, beta = (b_x + b_y)/2, d = a_x - a_y, delta = b_x - b_y and thc(a, b, u, T) main's theta,
     P_s(u) = C_s(d, delta, tau) * thc(s + h_s, beta + g_s, u, tau) / th1(u, tau),
     (h, g) = k: (0, 0), j: (0, 1/2), i: (1/2, 0), 1: (1/2, 1/2),
  with C_s a u-independent theta constant of the DIFFERENCE twist (d, delta).  Hence K_s(u) = th1'(0) Theta_s(u) /
  (Theta_s(0) th1(u)), a twisted Kronecker kernel of the summed twist, so K_s and c_s (a functional of K_s alone) see
  only (s, beta); the residues carry (d, delta) through C_s only.  Corollaries checked: a0_s = (log Theta_s)'(0)
  (main's a0_of), and RI-1: a0(up) = -a0(down) = -a0(lepton) on every line (q_L + q_R = -3, +3, +3).

Tests: (A) the ratio P_s th1 / Theta_s is constant in u (32 points on a ring of radius 0.3, away from the pole) at 12
random twists and two tau; (B) two offset pairs with equal b_x + b_y: K_s identical pointwise, main's cA identical;
a pair with the same b_x - b_y but different b_x + b_y as the control that must differ; (C) a0_of against the log
derivative; (D) RI-1 on 30 random lines x 3 tau with main's own sector twists, and K_lepton == K_down pointwise.
"""
import json, math, pathlib
import numpy as np
import mainB

B = mainB.B()
HERE = pathlib.Path(__file__).resolve().parent
rng = np.random.default_rng(524)
HG = {"k": (0.0, 0.0), "j": (0.0, 0.5), "i": (0.5, 0.0), "1": (0.5, 0.5)}


def theta_s(s_key, x, y, u, t):
    (ax, bx), (ay, by) = x, y
    h, g = HG[s_key]
    return B.thc(ax + ay + h, 0.5 * (bx + by) + g, u, t)


def dlog_theta(s_key, x, y, t, eps=1e-6):
    f = lambda u: complex(theta_s(s_key, x, y, np.array([u]), t)[0])
    return (f(eps) - f(-eps)) / (2 * eps) / f(0.0)


out = {}
# (A) the closed form
ring = 0.3 * np.exp(2j * np.pi * (np.arange(32) + 0.37) / 32)
worstA = 0.0
for t in (0.23 + 1.7j, -0.41 + 2.9j):
    for _ in range(12):
        x = (rng.uniform(-1, 1), rng.uniform(-1, 1)); y = (rng.uniform(-1, 1), rng.uniform(-1, 1))
        P = B.pairs(x, y, ring, t); T1 = B.th1(ring, t)
        for s in B.UNITS:
            r = P[s] * T1 / theta_s(s, x, y, ring, t)
            worstA = max(worstA, float(np.max(np.abs(r - r.mean())) / abs(r.mean())))
out["A_ratio_P_th1_over_Theta_constant_in_u_max_rel_spread"] = worstA

# (B) only b_x + b_y: kernels pointwise and main's cA
t = 0.17 + 2.2j
ax, ay = 0.37, -0.81
x1, y1 = (ax, -0.25), (ay, -0.35)          # sum -0.60
x2, y2 = (ax, +0.20), (ay, -0.80)          # sum -0.60, different difference
x3, y3 = (ax, -0.05), (ay, -0.15)          # control: difference 0.10 as in pair 1, sum -0.20
ring2 = 0.21 * np.exp(2j * np.pi * (np.arange(48) + 0.11) / 48)
def kern(x, y):
    R = B.residues(x, y, t); P = B.pairs(x, y, ring2, t)
    return {s: P[s] / R[s] for s in B.UNITS}, R
k1, R1 = kern(x1, y1); k2, R2 = kern(x2, y2); k3, R3 = kern(x3, y3)
out["B_kernel_maxdiff_same_sum"] = max(float(np.max(np.abs(k1[s] - k2[s]))) for s in B.UNITS)
out["B_kernel_maxdiff_control_same_difference_other_sum"] = max(float(np.max(np.abs(k1[s] - k3[s]))) for s in B.UNITS)
c1 = B.cA(x1, y1, t, R1); c2 = B.cA(x2, y2, t, R2); c3 = B.cA(x3, y3, t, R3)
out["B_cA_pair1"] = c1; out["B_cA_pair2"] = c2; out["B_cA_control"] = c3
out["B_cA_maxdiff_same_sum"] = max(abs(c1[s] - c2[s]) for s in B.UNITS)
out["B_cA_maxdiff_control"] = max(abs(c1[s] - c3[s]) for s in B.UNITS)
out["B_residue_moduli_pair1_vs_pair2"] = {s: [abs(R1[s]), abs(R2[s])] for s in B.UNITS}

# (C) a0 = log-derivative of Theta_s at 0 (main's a0_of)
worstC = 0.0
for _ in range(8):
    x = (rng.uniform(-1, 1), rng.uniform(-1, 1)); y = (rng.uniform(-1, 1), rng.uniform(-1, 1))
    R = B.residues(x, y, t); A0 = B.a0_of(x, y, t, R)
    for s in B.UNITS:
        worstC = max(worstC, abs(A0[s] - dlog_theta(s, x, y, t)) / max(1.0, abs(A0[s])))
out["C_a0_of_vs_dlogTheta_max_rel"] = worstC

# (D) RI-1 sign identity, every channel, random lines and tau; lepton kernel == down kernel
worst_odd = worst_dl = worst_k = 0.0; n = 0; minabs = 1e9
for t in (0.31 + 1.9j, -0.12 + 2.6j, 0.5 + 3.3j):
    for _ in range(10):
        p1, p2 = rng.uniform(0, 1), rng.uniform(0, 1)
        w = B.line_w(p1, p2, t); a0 = {}; K = {}
        for sec, (ql, qr) in mainB.SECTORS.items():
            x, y = B.sector_twists(w, t, ql, qr); R = B.residues(x, y, t); a0[sec] = B.a0_of(x, y, t, R)
            P = B.pairs(x, y, ring2, t); K[sec] = {s: P[s] / R[s] for s in B.UNITS}
        for s in B.UNITS:
            if a0["up"][s] is None or a0["down"][s] is None or a0["lepton"][s] is None:
                continue
            n += 1; minabs = min(minabs, abs(a0["down"][s]))
            worst_odd = max(worst_odd, abs(a0["up"][s] + a0["down"][s]) / max(1, abs(a0["down"][s])))
            worst_dl = max(worst_dl, abs(a0["down"][s] - a0["lepton"][s]) / max(1, abs(a0["down"][s])))
            worst_k = max(worst_k, float(np.max(np.abs(K["lepton"][s] - K["down"][s]))))
out["D_RI1_cases"] = n
out["D_RI1_min_abs_a0_down"] = minabs
out["D_RI1_max_rel_up_plus_down"] = worst_odd
out["D_RI1_max_rel_down_minus_lepton"] = worst_dl
out["D_kernel_lepton_minus_down_max"] = worst_k
(HERE / "check1_p524_kronecker_out.json").write_text(json.dumps(out, indent=1, default=str))
for k_, v in out.items():
    print(k_, v)
