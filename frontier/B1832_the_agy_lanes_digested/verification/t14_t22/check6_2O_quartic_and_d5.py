"""CHECK 6 (agy Theorem 14 Parts B-C, Theorem 15 Part C, Theorem 21 Part B; P-593 'an invariant separating the three 2O
classes'; P-592's own-code item (d): the quartic under 2O with a fixed versus a co-moving reference).  Pure linear algebra,
written here from the definitions (F_i = diag(i, -i), F_j = [[0, 1], [-1, 0]], g_L = (1 + F_i)/sqrt2, g_R = (1 - F_j)/sqrt2;
the D5 carrier matrices E, G, H, N10, I10 re-typed from their definition because the claim is about them).

(1) group census: |<g_L, g_R>|, element orders against 2O's (1:1, 2:1, 3:8, 4:18, 6:8, 8:12); the stabiliser
    St = {g : conj(g) sx g^T = +-sx}, its order and element orders against Dic4 = 2D4 (1:1, 2:1, 4:10, 8:4); its normal
    core and that core's orders against Q8 (1:1, 2:1, 4:6); the action of the group on the cosets G/St (image order).
(2) the quartic, derived here: for the pair U.Phi0 = U (E, G)/(2 sqrt2) on the commuting nilpotent plane,
    (8/5) kappa([X, X^dag]^2) with X = z1 Q + z2 R equals |z|^4 + |z^dag conj(U) sx U^T z|^2 (checked on the D5 matrices
    for all 48 U and random z); at the lane's fixed probes z0 = (1, 1)/sqrt2, zL = (1, i)/sqrt2, zR = (1, 0):
    the per-coset vectors and S = Q(z0) + 2 Q(zL) + 4 Q(zR); with a CO-MOVING probe z = conj(U) z0 the value is constant.
    Also the distributions of T15's (5/8)(1 + |z_EW^dag U^dag sx U z_EW|^2) and of the relay's section-2 item-6 formula.
(3) Theorem 14 B/C: the 16 elements of St realised on Phi0 by unitary elements of SO(10, I10) commuting with H
    (K1(a) = exp(i (a/2)(H+ - H-)) for exp(i a sx); K_Fi = exp(i pi H/4) (i N10) for F_i); and no element outside St is
    realisable by ANY unitary conjugation (the probe vector differs, and it is invariant under unitary conjugation).
"""
import itertools, json, math, pathlib
from collections import Counter
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
out = {}
Fi = np.array([[1j, 0], [0, -1j]]); Fj = np.array([[0, 1], [-1, 0]], dtype=complex); Fk = Fi @ Fj
gL = (np.eye(2) + Fi) / math.sqrt(2); gR = (np.eye(2) - Fj) / math.sqrt(2); sx = np.array([[0, 1], [1, 0]], dtype=complex)


def close(gens):
    els = [np.eye(2, dtype=complex)]; frontier = list(els)
    while frontier:
        new = []
        for g in frontier:
            for s in gens:
                p = g @ s
                if not any(np.allclose(p, h, atol=1e-10) for h in els):
                    els.append(p); new.append(p)
        frontier = new
    return els


def order(g):
    p = g.copy()
    for k in range(1, 50):
        if np.allclose(p, np.eye(2), atol=1e-9):
            return k
        p = p @ g


def idx(g, els):
    return next(i for i, h in enumerate(els) if np.allclose(g, h, atol=1e-9))


G = close([gL, gR, gL.conj().T, gR.conj().T])
out["order_G"] = len(G); out["G_element_orders"] = dict(sorted(Counter(order(g) for g in G).items()))
St = [g for g in G if np.allclose(g.conj() @ sx @ g.T, sx, atol=1e-9) or np.allclose(g.conj() @ sx @ g.T, -sx, atol=1e-9)]
out["order_St"] = len(St); out["St_element_orders"] = dict(sorted(Counter(order(g) for g in St).items()))
out["St_is_subgroup"] = all(any(np.allclose(a @ b, c, atol=1e-9) for c in St) for a in St for b in St)
core = [h for h in St if all(any(np.allclose(g @ h @ g.conj().T, c, atol=1e-9) for c in St) for g in G)]
out["order_core"] = len(core); out["core_element_orders"] = dict(sorted(Counter(order(g) for g in core).items()))
cosets = []
for g in G:
    if not any(any(np.allclose(g, c, atol=1e-9) for c in cs) for cs in cosets):
        cosets.append([g @ h for h in St])
out["n_cosets"] = len(cosets)
coset_of = lambda g: next(i for i, cs in enumerate(cosets) if any(np.allclose(g, c, atol=1e-9) for c in cs))
perms = set(tuple(coset_of(g @ cs[0]) for cs in cosets) for g in G)
out["image_of_G_on_cosets"] = sorted(perms); out["image_order"] = len(perms)
out["gL_gR_in_which_coset"] = [coset_of(np.eye(2)), coset_of(gL), coset_of(gR)]

# D5 carrier (re-typed definitions)
e5 = np.zeros((5, 5));
for j, c in enumerate([2.0, math.sqrt(6), math.sqrt(6), 2.0]): e5[j + 1, j] = c
h5 = np.diag([-4.0, -2, 0, 2, 4]); j5 = np.zeros((5, 5))
for j, c in enumerate([1.0, -1, 1, -1, 1]): j5[j, 4 - j] = c
bz = np.zeros((5, 5)); bz[1, 4] = math.sqrt(2 / 5); bz[4, 1] = -bz[1, 4]; bz[2, 3] = -math.sqrt(3 / 5); bz[3, 2] = -bz[2, 3]
Z5 = np.zeros((5, 5))
E = np.block([[e5, Z5], [Z5, -e5.T]]).astype(complex); Gm = (math.sqrt(10) * np.block([[Z5, bz], [j5 @ bz @ j5, Z5]])).astype(complex)
H = np.block([[h5, Z5], [Z5, -h5.T]]).astype(complex); I10 = np.block([[Z5, np.eye(5)], [np.eye(5), Z5]]).astype(complex)
N10 = np.block([[np.eye(5), Z5], [Z5, -np.eye(5)]]).astype(complex)
Ep, Em = (E + Gm) / 2, (E - Gm) / 2
Hp, Hm = Ep @ Ep.conj().T - Ep.conj().T @ Ep, Em @ Em.conj().T - Em.conj().T @ Em
kap = lambda X: 0.5 * np.trace(X)
out["d5_structure"] = {"so10_I10_E_G_H": float(max(np.abs(X.T @ I10 + I10 @ X).max() for X in (E, Gm, H, N10))),
                       "[E+,E-]": float(np.abs(Ep @ Em - Em @ Ep).max()), "[E+,E-dag]": float(np.abs(Ep @ Em.conj().T - Em.conj().T @ Ep).max()),
                       "kappa(H+^2), kappa(H-^2), kappa(H+H-)": [complex(kap(Hp @ Hp)), complex(kap(Hm @ Hm)), complex(kap(Hp @ Hm))],
                       "Hp+Hm-H": float(np.abs(Hp + Hm - H).max())}
n0 = 1 / (2 * math.sqrt(2)); Phi0 = (n0 * E, n0 * Gm)
act = lambda U, P: (U[0, 0] * P[0] + U[0, 1] * P[1], U[1, 0] * P[0] + U[1, 1] * P[1])
def quart(P, z):
    X = z[0] * P[0] + z[1] * P[1]; C = X @ X.conj().T - X.conj().T @ X; return float(np.real(0.8 * np.trace(C @ C)))
formula = lambda U, z: float(np.linalg.norm(z) ** 4 + abs(z.conj() @ U.conj() @ sx @ U.T @ z) ** 2)
rng = np.random.default_rng(14)
ferr = 0.0
for U in G:
    for _ in range(3):
        z = rng.normal(size=2) + 1j * rng.normal(size=2)
        ferr = max(ferr, abs(quart(act(U, Phi0), z) - formula(U, z)) / formula(U, z))
out["quartic_formula_max_rel_err"] = ferr
z0 = np.array([1, 1]) / math.sqrt(2); zL = np.array([1, 1j]) / math.sqrt(2); zR = np.array([1, 0], dtype=complex)
vecs = {}
for ci, cs in enumerate(cosets):
    vv = set((round(formula(U, z0), 10), round(formula(U, zL), 10), round(formula(U, zR), 10)) for U in cs)
    vecs[ci] = sorted(vv)
out["fixed_probe_vectors_by_coset"] = vecs
out["S2O_by_coset"] = {ci: sorted(set(round(v[0] + 2 * v[1] + 4 * v[2], 10) for v in vv)) for ci, vv in vecs.items()}
out["co_moving_probe_values"] = sorted(set(round(formula(U, U.conj() @ z0), 10) for U in G))
out["single_probe_z0_distribution"] = dict(Counter(round(formula(U, z0), 10) for U in G))
zEW = z0
out["T15_I4hat_distribution(U^dag sx U)"] = dict(Counter(round(0.625 * (1 + abs(zEW.conj() @ U.conj().T @ sx @ U @ zEW) ** 2), 10) for U in G))
item6 = lambda u: 0.625 * (1 - 4 * (u[0, 0] * u[0, 1].conjugate()).real * (u[1, 0] * u[1, 1].conjugate()).real + 2 * (abs(u[0, 0] * u[1, 1]) ** 2 + abs(u[0, 1] * u[1, 0]) ** 2))
out["relay_sec2_item6_distribution"] = dict(Counter(round(item6(U), 10) for U in G))

# (3) gauge realisations of St
def expm_h(Hh, c):
    w, V = np.linalg.eigh(Hh); return (V * np.exp(c * w)) @ V.conj().T
Kfi = expm_h(H, 1j * math.pi / 4) @ (1j * N10)
worst_real = 0.0; worst_member = 0.0; realised = 0
cands = []
for k in range(8):
    a = k * math.pi / 4; Urot = math.cos(a) * np.eye(2) + 1j * math.sin(a) * sx; Krot = expm_h(Hp - Hm, 1j * a / 2)
    cands += [(Urot, Krot), (Urot @ Fi, Kfi @ Krot)]
for U, K in cands:
    tgt = act(U, Phi0); got = (K @ Phi0[0] @ K.conj().T, K @ Phi0[1] @ K.conj().T)
    e = max(float(np.abs(got[0] - tgt[0]).max()), float(np.abs(got[1] - tgt[1]).max()))
    worst_real = max(worst_real, e); realised += e < 1e-12
    worst_member = max(worst_member, float(np.abs(K @ K.conj().T - np.eye(10)).max()), float(np.abs(K.T @ I10 @ K - I10).max()),
                       abs(abs(np.linalg.det(K)) - 1), float(np.abs(K @ H - H @ K).max()))
out["St_realised_count"] = realised; out["St_realisation_max_err"] = worst_real; out["K_unitary_SO10I10_commute_H_max_err"] = worst_member
out["realised_set_equals_St"] = sorted(idx(U, G) for U, _ in cands) == sorted(idx(U, G) for U in St)
for k_, v in out.items():
    print(k_, v)
(HERE / "check6_2O_quartic_and_d5_out.json").write_text(json.dumps(out, indent=1, default=str))
