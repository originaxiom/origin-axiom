"""S302 check of the lane's Theorem 66 STRUCTURE only (no frame Yukawa, no tau, no output of the frame):
(a) the two integers K_u^-1 = 201, K_d^-1 = 5 from the frame's sector charges (q_L, q_R) = 6Y: the first is
    3 sheets x the sum of squares over ALL three sectors' six charges, the second the down sector's two charges on ONE sheet;
(b) the 'one Higgs = two Higgs' identity is algebraic: for ANY complex 3x3 Y_u, Y_d and positive scalars z_u, z_d,
    sv(z_d Y_d)/sv(z_u Y_u) == (sv(Y_d)/sv(Y_u)) / (z_u/z_d) and |V_CKM| is unchanged by the scalar rescalings, so the
    test can only pass (random matrices, deviations only; the ratio itself is not printed);
(c) the lane rescales BOTH sides of Y_u by K_u^-1/2 and of Y_d by K_d^-1/2, i.e. gives u_L and d_L different kinetic
    normalisations; a common doublet metric K_Q (SU(2)_L) leaves only the right-handed factors, and any positive scalars
    reproduce any inter-sector ratio -> a free normalisation (the scoreboard's B12), not a derivation."""
import numpy as np

CH = {"up": (1, -4), "down": (1, 2), "lep": (-3, 6)}
tot = 3 * sum(ql * ql + qr * qr for ql, qr in CH.values())
down1 = sum(q * q for q in CH["down"])
print("3 sheets x sum over all sectors of q_L^2 + q_R^2 =", tot, "; down sector, one sheet =", down1)

rng = np.random.default_rng(20261104)
def cplx(): return rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
def left(Y): return np.linalg.svd(Y)[0][:, ::-1]
worst_ratio = worst_ckm = 0.0
for _ in range(200):
    Yu, Yd = cplx(), cplx(); zu, zd = rng.uniform(0.1, 300), rng.uniform(0.1, 300)
    su, sd = np.sort(np.linalg.svd(Yu, compute_uv=False)), np.sort(np.linalg.svd(Yd, compute_uv=False))
    one = (zd * sd) / (zu * su[-1]); two = (sd / su[-1]) / (zu / zd)
    worst_ratio = max(worst_ratio, float(np.max(np.abs(one - two) / np.abs(two))))
    V0 = np.abs(left(Yu).conj().T @ left(Yd)); V1 = np.abs(left(zu * Yu).conj().T @ left(zd * Yd))
    worst_ckm = max(worst_ckm, float(np.max(np.abs(V0 - V1))))
print("200 random pairs: max rel. deviation one-Higgs vs two-Higgs ratio %.1e ; max |V_CKM| change %.1e" % (worst_ratio, worst_ckm))
# (c) with a common left metric K_Q = kQ*I: Y_s^phys = kQ^-1/2 * ks^-1/2 * Y_s, the inter-sector factor is sqrt(k_d/k_u):
kQ, ku, kd = 2.0, 1 / 201, 1 / 5
fac_lane = (1 / kd) / (1 / ku)                     # lane: both sides per sector -> (K_d^-1/K_u^-1)
fac_doublet = np.sqrt(kd / ku) ** -1 * 1.0         # doublet-consistent: right-handed factor only -> sqrt(K_d^-1/K_u^-1)
print("doublet-consistent factor equals the lane's factor:", bool(abs(fac_lane - fac_doublet) < 1e-12),
      "(the lane's both-sides rescaling needs u_L and d_L to carry different metrics)")
