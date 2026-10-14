#!/usr/bin/env python3
"""B1651 -- WHERE A HIGGS CAN COUPLE THE ZERO MODES (sealed before this runs; PREREGISTRATION.md).

The zero modes' pairing (B1642's sealed R2): F_p^T eps C F_q = c_r th_r(0) th_r(z) / th_1(z), units (i, j, k) <-> thetas
(2, 4, 3), c = (-1, -1, i), z in the pi z convention (periods pi, pi tau). th_1 and th_2 are built from th_4 and th_3 with
the nome root q^(1/4) := exp(i pi tau / 4) explicit, so tau + 1 with Re tau > 1 takes no principal-branch phase.

  U1  read as a one-form g(z) dz, its residue at 0 is invariant under z = lam w + mu w^2; read as a quadratic differential
      g(z) dz^2, the coefficient of w^-1 scales as lam (the control); -lam/mu kept off the contour
  U2  every unit's pairing function has a non-trivial multiplier pair under z -> z + pi, z -> z + pi tau
  U3  (a) v(z) = c_r th_r(0) th_r(z) / th_1(z) is isotropic at EVERY z -- an identity (th4(z)^2 th4^2 + th2(z)^2 th2^2 =
      th3(z)^2 th3^2), checked in mpmath at the four fixed points and three generic points, not a test of the fixed
      points; (b) the three half-period triplets are independent of tau up to V4 and a phase; (c) the negative control:
      the puncture's R and three generic points (fixed lattice coordinates) are not
  U4  the triplet function is carried by the moves exactly: for L (tau -> tau + 1, z -> z) at s = -1 and R
      (tau -> tau/(tau + 1), z -> z/(tau + 1)) at s = +1, the triplet at the transformed point on the new fibre is
      Ad(g)^s of the old one up to a phase, with no V4 element, at all four fixed points; every power's tying V4 set is
      recorded; the transformed half-periods lie in the predicted classes; the negative control swaps the matrices
  U5  the lifts' group on M: 24 rotations (O); irreducible on M (x) C (commutant of dimension 1); the untwisted moves share
      no eigenline (max overlap 1/2); twisted by V4 the common eigenlines are exactly the four body diagonals (real); the
      elements fixing all three half-period classes are exactly V4, and the image is S3
  U6  read-out: single-point null vectors' overlaps |v_a^dag D v_b| / (|v_a||v_b|), one fixed point per sector, for each
      unordered pair and each D in V4, at fixed tau (not the orbit's mixing)

    python3 -B where_a_higgs_couples.py      # writes where_a_higgs_couples.json beside itself
"""
import itertools, json, pathlib
import mpmath as mp
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
mp.mp.dps = 30
C = [-1, -1, 1j]; TH = [2, 4, 3]
out = {}


def th(n, z, t):
    """Jacobi theta in the pi z convention, q = exp(i pi t), q^(1/4) := exp(i pi t / 4)"""
    q = mp.exp(1j * mp.pi * t)
    if n in (3, 4):
        return mp.jtheta(n, z, q)
    q4 = mp.exp(1j * mp.pi * t / 4); s = z + mp.pi * t / 2
    if n == 2:
        return q4 * mp.exp(1j * z) * mp.jtheta(3, s, q)
    return -1j * q4 * mp.exp(1j * z) * mp.jtheta(4, s, q)


def g_unit(t, r):
    n = TH[r]
    return lambda z: C[r] * th(n, 0, t) * th(n, z, t) / th(1, z, t)


def contour_coeff(f, k, rad=mp.mpf("0.02"), N=96):
    """coefficient of w^k of f's Laurent series at 0, by the trapezoid rule on |w| = rad"""
    s = 0
    for m in range(N):
        w = rad * mp.exp(2j * mp.pi * m / N); s += f(w) * w ** (-k)
    return s / N


def triplet(t, z0):
    if z0 == 0:
        return np.array([complex(C[r] * th(TH[r], 0, t) ** 2) for r in range(3)])
    return np.array([complex(C[r] * th(TH[r], 0, t) * th(TH[r], z0, t) / th(1, z0, t)) for r in range(3)])


def ov(u, w):
    return float(abs(np.vdot(u, w)) / (np.linalg.norm(u) * np.linalg.norm(w)))


V4 = [np.diag(d).astype(complex) for d in ([1, 1, 1], [1, -1, -1], [-1, 1, -1], [-1, -1, 1])]
V4_NAMES = ["1", "i", "j", "k"]                       # Ad of the unit: the half-turn about that axis


def best_v4(u, w, thr=1 - 1e-12):
    """best overlap over V4, and every V4 element attaining the threshold (the half-period lines tie under their own
    axis half-turn, so a single argmax would pick between ties by noise)"""
    vals = [ov(u, D @ w) for D in V4]
    return max(vals), [V4_NAMES[a] for a, x in enumerate(vals) if x > thr]


def triplet_mp(t, z0):
    if z0 == 0:
        return [C[r] * th(TH[r], 0, t) ** 2 for r in range(3)]
    return [C[r] * th(TH[r], 0, t) * th(TH[r], z0, t) / th(1, z0, t) for r in range(3)]


def isotropy_mp(t, z0):
    """|v.v| / |v|^2 in mpmath, before any conversion to double"""
    v = triplet_mp(t, z0)
    return float(abs(sum(x * x for x in v)) / sum(abs(x) ** 2 for x in v))


def fixed_points(t):
    return {"0": 0, "1/2": mp.pi / 2, "tau/2": mp.pi * t / 2, "(1+tau)/2": mp.pi * (1 + t) / 2}


def two_torsion_class(z, t):
    """z = pi (m + n t): returns the class of (2m, 2n) mod 2 as a fixed-point name, and the distance from the half-lattice"""
    w = complex(z / mp.pi); tt = complex(t)
    n = w.imag / tt.imag; m = w.real - n * tt.real
    M2, N2 = round(2 * m), round(2 * n)
    name = {(0, 0): "0", (1, 0): "1/2", (0, 1): "tau/2", (1, 1): "(1+tau)/2"}[(M2 % 2, N2 % 2)]
    return name, max(abs(2 * m - M2), abs(2 * n - N2))


# the lifts on M: Ad of unit quaternions on the imaginary units, as 3x3 rotations
def ad(g):
    w, x, y, z = g
    return np.array([[1 - 2 * (y * y + z * z), 2 * (x * y - z * w), 2 * (x * z + y * w)],
                     [2 * (x * y + z * w), 1 - 2 * (x * x + z * z), 2 * (y * z - x * w)],
                     [2 * (x * z - y * w), 2 * (y * z + x * w), 1 - 2 * (x * x + y * y)]])


s2 = 1 / np.sqrt(2)
AL, AR = ad((s2, s2, 0, 0)), ad((s2, 0, -s2, 0))      # g_L = (1 + i)/sqrt2, g_R = (1 - j)/sqrt2 (B1600's w10_check)
MOVES = {"L": (AL, lambda t: t + 1, lambda z, t: z), "R": (AR, lambda t: t / (t + 1), lambda z, t: z / (t + 1))}
PREDICTED_IMAGE = {"L": {"0": "0", "1/2": "1/2", "tau/2": "(1+tau)/2", "(1+tau)/2": "tau/2"},
                   "R": {"0": "0", "1/2": "(1+tau)/2", "tau/2": "tau/2", "(1+tau)/2": "1/2"}}

def key(Mx): return tuple(int(round(x)) for x in Mx.real.flatten())


def eig_clusters(A, tol=1e-6):
    out_ = []
    for x in np.linalg.eigvals(A):
        if all(abs(x - y) > tol for y in out_):
            out_.append(x)
    return out_


def common_lines(A, B, tol=1e-10):
    """joint eigenvectors of A and B: null space of [A - lam; B - mu] over distinct eigenvalue pairs; returns each joint
    eigenspace's basis vectors with its dimension, and the smallest sigma over all pairs"""
    lines, smin = [], np.inf
    for lam in eig_clusters(A):
        for mu in eig_clusters(B):
            Mx = np.vstack([A - lam * np.eye(3), B - mu * np.eye(3)])
            _, S, Vh = np.linalg.svd(Mx)
            smin = min(smin, S[-1])
            dim = int(sum(S < tol))
            for d in range(dim):
                lines.append((Vh[-1 - d].conj(), complex(lam), complex(mu), dim))
    return lines, float(smin)



rng = np.random.default_rng(1651)
taus = [mp.mpc(rng.uniform(-0.5, 0.5), rng.uniform(0.75, 1.8)) for _ in range(4)]
RAD = mp.mpf("0.02")

# U1
U1 = {"one_form_max_rel": 0.0, "quad_ratio_minus_lam_max": 0.0, "min_abs_lam_over_mu_over_rad": None}
ratios = []
for t in taus[:2]:
    for r in range(3):
        g = g_unit(t, r); res0 = contour_coeff(g, -1)
        for _ in range(3):
            lam = mp.mpc(rng.normal(), rng.normal()); mu = mp.mpc(rng.normal(), rng.normal()) * 0.3
            while abs(lam / mu) <= 5 * RAD:                 # keep the pole's second preimage -lam/mu off the contour
                mu = mp.mpc(rng.normal(), rng.normal()) * 0.3
            ratios.append(float(abs(lam / mu) / RAD))
            phi = lambda w: lam * w + mu * w * w; dphi = lambda w: lam + 2 * mu * w
            res1 = contour_coeff(lambda w: g(phi(w)) * dphi(w), -1)
            quad = contour_coeff(lambda w: g(phi(w)) * dphi(w) ** 2, -1)
            U1["one_form_max_rel"] = max(U1["one_form_max_rel"], float(abs(res1 - res0) / abs(res0)))
            U1["quad_ratio_minus_lam_max"] = max(U1["quad_ratio_minus_lam_max"], float(abs(quad / res0 - lam) / abs(lam)))
U1["min_abs_lam_over_mu_over_rad"] = min(ratios)
out["U1"] = U1

# U2
U2 = []
for t in taus[:2]:
    z0 = mp.mpc(0.13, 0.07)
    for r in range(3):
        g = g_unit(t, r)
        m1 = g(z0 + mp.pi) / g(z0); mt = g(z0 + mp.pi * t) / g(z0)
        U2.append([r, complex(m1), complex(mt)])
out["U2_multipliers"] = [[r, [round(x.real, 9), round(x.imag, 9)], [round(y.real, 9), round(y.imag, 9)]] for r, x, y in U2]
out["U2_max_dev_from_sign"] = max(min(abs(x - 1), abs(x + 1)) for _, a, b in U2 for x in (a, b))
out["U2_all_nontrivial"] = all(not (abs(a - 1) < 1e-9 and abs(b - 1) < 1e-9) for _, a, b in U2)

# U3: (a) isotropy everywhere -- an identity (th4(z)^2 th4^2 + th2(z)^2 th2^2 = th3(z)^2 th3^2), checked, not a test of
# the fixed points; (b) the half-periods' tau-independence; (c) the negative control: the puncture and three generic
# points (fixed lattice coordinates) are NOT tau-independent
GENERIC = [(0.31, 0.17), (0.62, 0.41), (0.13, 0.77)]
U3 = {"a_isotropy_max_fixed_points": 0.0, "a_isotropy_max_generic_points": 0.0,
      "b_half_period_tau_independence_min_overlap": 1.0, "c_control_max_overlap": {}}
trip = {}
for t in taus:
    for name, z0 in fixed_points(t).items():
        U3["a_isotropy_max_fixed_points"] = max(U3["a_isotropy_max_fixed_points"], isotropy_mp(t, z0))
        trip.setdefault(name, []).append(triplet(t, z0))
    for (m, n) in GENERIC:
        z0 = mp.pi * (m + n * t)
        U3["a_isotropy_max_generic_points"] = max(U3["a_isotropy_max_generic_points"], isotropy_mp(t, z0))
        trip.setdefault("generic(%g,%g)" % (m, n), []).append(triplet(t, z0))
for name, vs in trip.items():
    worst_or_best = []
    for a, b in itertools.combinations(range(len(vs)), 2):
        worst_or_best.append(best_v4(vs[a], vs[b])[0])
    if name in ("1/2", "tau/2", "(1+tau)/2"):
        U3["b_half_period_tau_independence_min_overlap"] = min(U3["b_half_period_tau_independence_min_overlap"], min(worst_or_best))
    else:
        U3["c_control_max_overlap"][name] = max(worst_or_best)
out["U3"] = U3

# U4: the exact law (D = 1) for L at s = -1 and R at s = +1 at all four points; every power's tying V4 set recorded; the
# images and the half-lattice distance; the negative control (each move's transformation against the other's matrix)
EXACT_S = {"L": -1, "R": 1}
U4 = {}
max_dist = 0.0
for mv, (A, ft, fz) in MOVES.items():
    res = {}
    for s_ in (1, -1):
        As = A if s_ == 1 else A.T
        rows = []
        for t in taus[:3]:
            t2 = ft(t)
            for name, z0 in fixed_points(t).items():
                z2 = fz(z0, t)
                img, dist = (("0", 0.0) if name == "0" else two_torsion_class(z2, t2))
                max_dist = max(max_dist, dist)
                v_new = triplet(t2, 0) if name == "0" else triplet(t2, z2)
                w = As @ triplet(t, z0)
                b, Ds = best_v4(v_new, w)
                rows.append({"point": name, "image": img, "image_as_predicted": img == PREDICTED_IMAGE[mv][name],
                             "overlap_D1": ov(v_new, w), "best_over_V4": b, "D_attaining": Ds})
        res[str(s_)] = {"min_overlap_D1": min(r["overlap_D1"] for r in rows),
                        "min_best_over_V4": min(r["best_over_V4"] for r in rows), "rows": rows}
    U4[mv] = res
out["U4"] = U4
out["U4_exact_law_D1"] = {mv: U4[mv][str(EXACT_S[mv])]["min_overlap_D1"] for mv in U4}
out["U4_images_as_predicted"] = all(r["image_as_predicted"] for mv in U4 for s_ in U4[mv] for r in U4[mv][s_]["rows"])
out["U4_max_half_lattice_dist"] = max_dist
ctrl = {}
for mv, (A, ft, fz) in MOVES.items():
    other = AR if mv == "L" else AL
    ctrl[mv] = max(best_v4(triplet(ft(t), 0), O @ triplet(t, 0))[0] for t in taus[:3] for O in (other, other.T))
out["U4_control_swapped_matrix_puncture_max"] = ctrl


# U5: the group, irreducibility, common eigenlines, the kernel on the half-period classes
grp = {key(np.eye(3)): np.eye(3)}; frontier = [np.eye(3)]
while frontier:
    nxt = []
    for Gm in frontier:
        for Hm in (AL, AR):
            P = np.rint(Hm @ Gm)
            if key(P) not in grp:
                grp[key(P)] = P; nxt.append(P)
    frontier = nxt
K = np.vstack([np.kron(np.eye(3), A) - np.kron(A.T, np.eye(3)) for A in (AL, AR)])
commutant_dim = int(sum(sv < 1e-10 for sv in np.linalg.svd(K, compute_uv=False)))


def canon(u):
    """a line's canonical representative: unit norm, first non-negligible component real positive"""
    u = u / np.linalg.norm(u); k0 = int(np.argmax(abs(u) > 1e-9))
    return u * np.exp(-1j * np.angle(u[k0]))


untw_lines, untw_smin = common_lines(AL, AR)
wl, VL = np.linalg.eig(AL)                            # eigenvalues 1, i, -i: non-degenerate, so eig's lines are the lines
untw_overlap = max(ov(VL[:, a], AR @ VL[:, a]) for a in range(3))
tw = []
for (n1, D1), (n2, D2) in itertools.product(zip(V4_NAMES, V4), repeat=2):
    lines, _ = common_lines(D1 @ AL, D2 @ AR)
    for v, lam, mu, dim in lines:
        u = canon(v)
        tw.append({"twist": [n1, n2], "line": [[round(float(x.real), 12), round(float(x.imag), 12)] for x in u],
                   "imag_max": float(abs(u.imag).max()), "joint_dim": dim,
                   "eigs": [[round(lam.real, 9), round(lam.imag, 9)], [round(mu.real, 9), round(mu.imag, 9)]],
                   "body_diagonal": bool(np.allclose(abs(u), 1 / np.sqrt(3), rtol=0, atol=1e-12)),
                   "isotropy": float(abs(np.dot(u, u)))})
distinct = []
for d in tw:
    u = np.array([complex(a, b) for a, b in d["line"]])
    if all(ov(u, w) < 1 - 1e-9 for w in distinct):
        distinct.append(u)
hp = {h: triplet(taus[0], z) for h, z in fixed_points(taus[0]).items() if h != "0"}
perms, kernel = set(), []
for kk, Gm in grp.items():
    img = []
    for h, v in hp.items():
        scores = {h2: best_v4(w, Gm @ v)[0] for h2, w in hp.items()}
        h2 = max(scores, key=scores.get); img.append(h2 if scores[h2] > 1 - 1e-9 else None)
    perms.add(tuple(img))
    if img == list(hp):
        kernel.append(kk)
out["U5"] = {"group_order": len(grp), "commutant_dim": commutant_dim,
             "untwisted_common_lines": len(untw_lines), "untwisted_min_sigma": untw_smin,
             "untwisted_max_overlap": untw_overlap,
             "twisted_common_lines": tw, "n_twisted_common_lines": len(tw), "max_joint_dim": max([d["joint_dim"] for d in tw] or [0]),
             "all_twisted_lines_body_diagonals_real": bool(tw and all(d["body_diagonal"] and d["imag_max"] < 1e-12 for d in tw)),
             "distinct_twisted_lines": len(distinct),
             "half_period_classes_permutations": sorted([list(p) for p in perms]),
             "n_permutations": len(perms), "all_images_resolved": all(None not in p for p in perms),
             "kernel": [list(k) for k in kernel],
             "kernel_is_V4": sorted(kernel) == sorted(key(D.real) for D in V4)}

# U6 (read-out) at the first tau: single-point null vectors' overlaps, one fixed point per sector, each V4 sign
t = taus[0]; fp = {n: triplet(t, z) for n, z in fixed_points(t).items()}
U6 = {}
for a, b in itertools.combinations(fp, 2):
    U6["%s|%s" % (a, b)] = sorted(ov(fp[a], D @ fp[b]) for D in V4)
out["U6_single_point_overlaps_by_pair_and_sign"] = U6
out["taus"] = [str(x) for x in taus]
json.dump(out, open(HERE / "where_a_higgs_couples.json", "w"), indent=1, default=str)
print(json.dumps(out, indent=1, default=str))
