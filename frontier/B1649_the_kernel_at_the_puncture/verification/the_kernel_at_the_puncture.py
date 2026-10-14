#!/usr/bin/env python3
"""B1649 -- THE KERNEL AT THE PUNCTURE (sealed before this runs; PREREGISTRATION.md).

The residue coupling of the zero modes to a Higgs S in End(C^2) = span(1, i, j, k) at the fibre's puncture (B1642's and
B1644's sealed definitions, reused unchanged): Y(S)_pq = res F_p^T eps S F_q.  Kept in mpmath end to end (dps 30).

  K1  for random complex S at 6 tau: Y(S) R = 0 and R^T Y(S) = 0, R the theta triplet (B1644's closed form)
  K2  two sectors sharing the fibre (random S_u, S_d at one tau): the left massless states coincide, so the mixing matrix
      is 1 (+) U(2): |V_ud| = 1, V_us = V_ub = V_cd = V_td = 0
  K3  read-out: the map (S_u, S_d) -> (m_c/m_t, m_s/m_b, |V_cb|) has full rank 3 (the 2-3 sector is free)
  K4  control: with R made non-isotropic (theta_3^2 scaled by 1.1 in the closed form) K1 and K2 fail

    python3 -B the_kernel_at_the_puncture.py      # writes the_kernel_at_the_puncture.json beside itself
"""
import json, os, pathlib
import mpmath as mp
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
FRONTIER = pathlib.Path(os.environ.get("OA_FRONTIER", HERE.parents[1]))
B1642 = FRONTIER / "B1642_the_golden_coupling_as_the_zero_modes_residue" / "verification" / "residue_coupling.py"
ns = {"__file__": str(B1642)}
exec(compile(open(B1642).read().split("rng = np.random.default_rng(1642)")[0], "residue_coupling_defs", "exec"), ns)
th, residue, BLOCKS, EPS, QI, QJ, QK = ns["th"], ns["residue"], ns["BLOCKS"], ns["EPS"], ns["QI"], ns["QJ"], ns["QK"]
mp.mp.dps = 30
ONE = mp.eye(2)
BLOCK_OF_UNIT = [1, 0, 2]                      # BLOCKS are (j, i, k); the units' labels are (i, j, k)
out = {}


def Y_of(s, t):
    """s = (s0, s_i, s_j, s_k) complex: S = s0 1 + s_i QI + s_j QJ + s_k QK; Y in the units' labels, an mp.matrix"""
    S = mp.mpc(s[0]) * ONE + mp.mpc(s[1]) * QI + mp.mpc(s[2]) * QJ + mp.mpc(s[3]) * QK
    Yb = mp.matrix(3, 3)
    for p, (_, Cp) in enumerate(BLOCKS):
        for q, (_, Cq) in enumerate(BLOCKS):
            Yb[p, q] = residue(Cp.T * EPS * S * Cq, t)
    Y = mp.matrix(3, 3)
    for a in range(3):
        for b in range(3):
            Y[a, b] = Yb[BLOCK_OF_UNIT[a], BLOCK_OF_UNIT[b]]
    return Y


def R_of(t, scale3=1):
    den = mp.pi * th(2, 0, t) * th(3, 0, t) * th(4, 0, t)
    return mp.matrix([-th(2, 0, t) ** 2 / den, -th(4, 0, t) ** 2 / den, scale3 * 1j * th(3, 0, t) ** 2 / den])


def nrm(v):
    return mp.sqrt(sum(abs(x) ** 2 for x in v))


def left_null_and_ratios(Y):
    A = np.array([[complex(Y[a, b]) for b in range(3)] for a in range(3)])
    W, s, Xh = np.linalg.svd(A)
    return W, s


def mixing(Yu, Yd):
    Wu, su = left_null_and_ratios(Yu); Wd, sd = left_null_and_ratios(Yd)
    V = Wu.conj().T @ Wd                              # columns ordered by decreasing mass: (3rd, 2nd, 1st generation)
    return np.abs(V)[::-1, ::-1], su, sd              # rows/cols (1st, 2nd, 3rd)


def Y_closed(s, Rp):
    a = mp.matrix([s[1], s[2], s[3]]); ar = sum(a[k] * Rp[k] for k in range(3))
    Y = a * Rp.T + Rp * a.T - ar * mp.eye(3)
    X = mp.matrix([[0, -Rp[2], Rp[1]], [Rp[2], 0, -Rp[0]], [-Rp[1], Rp[0], 0]])
    return Y + mp.mpc(s[0]) * X


rng = np.random.default_rng(1649)
taus = [mp.mpc(rng.uniform(-0.5, 0.5), rng.uniform(0.7, 1.8)) for _ in range(6)]
rand_s = lambda: [complex(rng.normal(), rng.normal()) for _ in range(4)]

# K1
K1 = {"right_max_rel": mp.mpf(0), "left_max_rel": mp.mpf(0)}
for t in taus:
    R = R_of(t)
    for _ in range(4):
        Y = Y_of(rand_s(), t); nY = mp.sqrt(sum(abs(Y[a, b]) ** 2 for a in range(3) for b in range(3)))
        K1["right_max_rel"] = max(K1["right_max_rel"], nrm(Y * R) / (nY * nrm(R)))
        K1["left_max_rel"] = max(K1["left_max_rel"], nrm(Y.T * R) / (nY * nrm(R)))
out["K1"] = {k: float(v) for k, v in K1.items()}


# K2
t0 = taus[0]; K2 = []
for _ in range(5):
    absV, su, sd = mixing(Y_of(rand_s(), t0), Y_of(rand_s(), t0))
    K2.append({"V_ud": float(absV[0, 0]), "V_us": float(absV[0, 1]), "V_ub": float(absV[0, 2]), "V_cd": float(absV[1, 0]),
               "V_td": float(absV[2, 0]), "V_cb": float(absV[1, 2]), "m1_over_m3_u": float(su[2] / su[0]), "m1_over_m3_d": float(sd[2] / sd[0])})
out["K2"] = K2


# K3: the rank of (S_u, S_d) -> (m_c/m_t, m_s/m_b, |V_cb|) by central differences in the 16 real parameters
def obs(p):
    su_ = [complex(p[2 * k], p[2 * k + 1]) for k in range(4)]; sd_ = [complex(p[8 + 2 * k], p[9 + 2 * k]) for k in range(4)]
    absV, su, sd = mixing(Y_of(su_, t0), Y_of(sd_, t0))
    return np.array([su[1] / su[0], sd[1] / sd[0], absV[1, 2]])


p0 = rng.normal(size=16); h = 1e-6
J = np.array([(obs(p0 + h * e) - obs(p0 - h * e)) / (2 * h) for e in np.eye(16)]).T
sv = np.linalg.svd(J, compute_uv=False)
out["K3"] = {"jacobian_sv": [float(x) for x in sv], "rank": int(np.sum(sv > 1e-6 * sv[0]))}

# K4: control -- a non-isotropic triplet in the closed form, Y = a R'^T + R' a^T - (a.R') 1 + s0 [R']_x
Rb = R_of(t0, scale3=1.1)
absV, su, sd = mixing(Y_closed(rand_s(), Rb), Y_closed(rand_s(), Rb))
out["K4"] = {"m1_over_m3_u": float(su[2] / su[0]), "V_us": float(absV[0, 1]), "V_ub": float(absV[0, 2])}

json.dump(out, open(HERE / "the_kernel_at_the_puncture.json", "w"), indent=1, default=str)
print(json.dumps(out, indent=1, default=str))
