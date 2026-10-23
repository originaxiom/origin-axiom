"""B1738: main's own check of W139 (P-338): under E6's cubic N = det Q + det L + det Q^c - tr(Q L Q^c) on
(3_C, 3b_L) + (3_L, 3b_R) + (3_R, 3b_C), with three families, a symmetric coupling lambda_abc and any colour- and charge-
preserving vevs of the 27s' neutral leptonic components, the extended charge -1/3 quark matrix and the extended charged-
lepton matrix have the same singular values (so D = 1).  Built from the invariance and the charge alone: Q_em = T3 + T8/sqrt3
on each SU(3) gives the charges; the mass matrices are the Hessian of the polarised cubic.  Controls: N's invariance under
random SU(3)^3; the neutral components counted (five); a broken cubic (det L doubled) must split them.
    python3 -B e6_down_equals_lepton.py
Importing computes nothing."""
import json, pathlib, itertools
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
QL = np.array([2 / 3, -1 / 3, -1 / 3])          # T3 + T8/sqrt3 on an SU(3) fundamental


def unpack(x):
    return x[0:9].reshape(3, 3), x[9:18].reshape(3, 3), x[18:27].reshape(3, 3)      # Q (C, Lbar), L (L, Rbar), Qc (R, Cbar)


def N(x, kL=1.0):
    Q, L, Qc = unpack(x)
    return np.linalg.det(Q) + kL * np.linalg.det(L) + np.linalg.det(Qc) - np.trace(Q @ L @ Qc)


def charges():
    q = np.zeros(27); col = np.zeros(27, dtype=int) - 1
    for a in range(3):
        for i in range(3):
            q[0 + 3 * a + i] = -QL[i]; col[0 + 3 * a + i] = a          # Q_{alpha i}: colour alpha, Lbar index i
            q[9 + 3 * a + i] = QL[a] - QL[i]                           # L_{i k}: L index a, Rbar index i
            q[18 + 3 * a + i] = QL[a]; col[18 + 3 * a + i] = i         # Qc_{k alpha}: R index a, colour i (as anti)
    return q, col


def polar(x, y, z, kL=1.0):
    """the symmetric trilinear form with N(x) = polar(x, x, x), by the polarisation identity"""
    f = lambda v: N(v, kL)
    return (f(x + y + z) - f(x + y) - f(y + z) - f(x + z) + f(x) + f(y) + f(z)) / 6


def rand_su3(rng):
    A = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3)); Qm, R = np.linalg.qr(A); Qm = Qm * (np.diag(R) / abs(np.diag(R)))
    return Qm / np.linalg.det(Qm) ** (1 / 3)


def main():
    rng = np.random.default_rng(139); q, col = charges(); E = np.eye(27)
    # control 1: invariance of N under SU(3)_C x SU(3)_L x SU(3)_R
    inv = 0.0
    for _ in range(5):
        x = rng.normal(size=27) + 1j * rng.normal(size=27); Q, L, Qc = unpack(x)
        Uc, Ul, Ur = rand_su3(rng), rand_su3(rng), rand_su3(rng)
        y = np.concatenate([(Uc @ Q @ np.linalg.inv(Ul)).ravel(), (Ul @ L @ np.linalg.inv(Ur)).ravel(), (Ur @ Qc @ np.linalg.inv(Uc)).ravel()])
        inv = max(inv, abs(N(y) - N(x)) / abs(N(x)))
    neutral = [k for k in range(9, 18) if abs(q[k]) < 1e-12]
    dq = [k for k in range(0, 9) if col[k] == 0 and abs(q[k] - 1 / 3) < 1e-12]          # colour 0, charge +1/3 in Q
    dqc = [k for k in range(18, 27) if col[k] == 0 and abs(q[k] + 1 / 3) < 1e-12]        # colour 0, charge -1/3 in Qc
    lm = [k for k in range(9, 18) if abs(q[k] + 1) < 1e-12]; lp = [k for k in range(9, 18) if abs(q[k] - 1) < 1e-12]
    def mats(lam, vev, kL):
        Md = np.zeros((6, 6), dtype=complex); Ml = np.zeros((6, 6), dtype=complex)
        for a, b in itertools.product(range(3), repeat=2):
            for c in range(3):
                v = np.zeros(27, dtype=complex); v[neutral] = vev[c]
                for (r, kx), (s, ky) in itertools.product(enumerate(dq), enumerate(dqc)):
                    Md[2 * a + r, 2 * b + s] += lam[a, b, c] * 6 * polar(E[kx], E[ky], v, kL)
                for (r, kx), (s, ky) in itertools.product(enumerate(lm), enumerate(lp)):
                    Ml[2 * a + r, 2 * b + s] += lam[a, b, c] * 6 * polar(E[kx], E[ky], v, kL)
        return Md, Ml
    worst, worst_broken, rows = 0.0, 0.0, []
    for t in range(8):
        lam = rng.normal(size=(3, 3, 3)) + 1j * rng.normal(size=(3, 3, 3))
        lam = sum(np.transpose(lam, p) for p in itertools.permutations(range(3))) / 6
        vev = rng.normal(size=(3, len(neutral))) + 1j * rng.normal(size=(3, len(neutral)))
        Md, Ml = mats(lam, vev, 1.0); sd, sl = np.linalg.svd(Md, compute_uv=False), np.linalg.svd(Ml, compute_uv=False)
        worst = max(worst, float(np.max(np.abs(sd - sl) / sd[0])))
        Md2, Ml2 = mats(lam, vev, 2.0); sd2, sl2 = np.linalg.svd(Md2, compute_uv=False), np.linalg.svd(Ml2, compute_uv=False)
        worst_broken = max(worst_broken, float(np.max(np.abs(sd2 - sl2) / sd2[0])))
    out = {"N_invariance_rel": inv, "neutral_leptonic_components": len(neutral), "down_type_pairs": [len(dq), len(dqc)],
           "lepton_pairs": [len(lm), len(lp)], "max_rel_singular_value_difference_E6": worst,
           "control_detL_doubled_max_rel_difference": worst_broken}
    json.dump(out, open(HERE / "e6_down_equals_lepton.json", "w"), indent=1); print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
