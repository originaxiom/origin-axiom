#!/usr/bin/env python3
"""P-510, the web seat's frame check (data-free: no Standard Model value is read or compared).

The question. In field form the frame of KIND_TABLE's pair channel is "the kinetic (Kahler) normalisation of the
generations" (B1643, section 2). Canonical normalisation sends a sector's coupling matrix Y to
    Y' = (K_L^(-1/2))^T  Y  K_R^(-1/2),
with K_L the left fields' metric (the doublet's, shared by the up and down sectors) and K_R the right fields' metric.
Which outputs move under which kind of frame freedom?

    F0  the reference frame: K = I for every field;
    F1  one overall scale per field (K = k I, a different k for each field);
    F2  per-generation factors common to every field, times one scale per field (K = a B, B = diag(1, 2, 3));
    F3  kinetic mixing: K = I + e H for every field, H Hermitian with zero diagonal, e = 0.3 (each field its own H).

Outputs per instance:
    the six same-sector mass ratios m1/m3 and m2/m3 (up, down, lepton);
    the nine CKM moduli |V_ij|, V = U_u^dagger U_d from the left singular vectors (lightest first);
    J = Im(V_12 V_23 V_13^* V_22^*);
    the double ratio DR = (m2/m1)_lepton / (m2/m1)_down, B1643's (y_mu y_d)/(y_s y_e).

Instance classes (seeded): generic complex Gaussian couplings; hierarchical couplings Y_ij = c_ij eps^(p_i + q_j)
(c_ij complex Gaussian, eps = 0.2, p = (3, 2, 0), q = (2, 1, 0)); diagonal couplings (each Y diagonal in the
generation basis, magnitudes uniform in [0.5, 1.5] times eps^(4, 2, 0), so the generation order is the mass order).

Reported for each class and frame: the median and the largest change against F0 (relative for the ratios and DR;
absolute for |V| and for J; J relative too, over the instances with |J| > 1e-14 in F0, "n/a" when there are none).

Plus the two-by-two example: up = diag(1, 0), down = [[1, 1], [1, 1]]; with K_Q^(-1/2) = diag(d1, d2) the heavy
states' mixing angle moves from 45 degrees to arctan(d2/d1).

What the seat expects, written before the run: F1 moves none of the four output classes (to rounding); F2 moves the
six ratios, |V| and J for generic and hierarchical couplings, and leaves DR exactly for diagonal couplings (DR moves
for generic couplings, and for hierarchical ones by an amount set by the hierarchy); F3 moves all four.

Run once; the output is committed unread.
"""
import numpy as np

N_INST = 200
SEED = 51020  # P-510; fixed before the run
EPS = 0.2
P = np.array([3, 2, 0])
Q = np.array([2, 1, 0])
FIELDS = ("Q", "u", "d", "L", "e")


def inv_sqrt_herm(K):
    w, U = np.linalg.eigh(K)
    if np.min(w) <= 0:
        raise ValueError("metric not positive definite")
    return U @ np.diag(w ** -0.5) @ U.conj().T


def canon(Y, KL, KR):
    return inv_sqrt_herm(KL).T @ Y @ inv_sqrt_herm(KR)


def svd_light_first(Y):
    U, s, _ = np.linalg.svd(Y)
    order = np.argsort(s)
    return U[:, order], s[order]


def outputs(Yu, Yd, Ye):
    Uu, su = svd_light_first(Yu)
    Ud, sd = svd_light_first(Yd)
    _, se = svd_light_first(Ye)
    ratios = np.array([su[0] / su[2], su[1] / su[2], sd[0] / sd[2], sd[1] / sd[2], se[0] / se[2], se[1] / se[2]])
    V = Uu.conj().T @ Ud
    J = np.imag(V[0, 1] * V[1, 2] * np.conj(V[0, 2]) * np.conj(V[1, 1]))
    DR = (se[1] / se[0]) / (sd[1] / sd[0])
    return ratios, np.abs(V), J, DR


def cgauss(rng, shape):
    return (rng.standard_normal(shape) + 1j * rng.standard_normal(shape)) / np.sqrt(2)


def instance(rng, kind):
    if kind == "generic":
        return [cgauss(rng, (3, 3)) for _ in range(3)]
    if kind == "hierarchical":
        tex = EPS ** (P[:, None] + Q[None, :])
        return [cgauss(rng, (3, 3)) * tex for _ in range(3)]
    if kind == "diagonal":
        return [np.diag(rng.uniform(0.5, 1.5, 3) * EPS ** np.array([4, 2, 0])).astype(complex) for _ in range(3)]
    raise ValueError(kind)


def hermitian_offdiag(rng):
    A = cgauss(rng, (3, 3))
    H = (A + A.conj().T) / 2
    np.fill_diagonal(H, 0)
    return H / np.max(np.abs(np.linalg.eigvalsh(H)))  # spectral radius 1, so I + 0.3 H stays positive


def frame(rng, name):
    I = np.eye(3)
    if name == "F0":
        return {f: I for f in FIELDS}
    if name == "F1":
        return {f: rng.uniform(0.5, 2.0) * I for f in FIELDS}
    if name == "F2":
        B = np.diag([1.0, 2.0, 3.0])
        return {f: rng.uniform(0.5, 2.0) * B for f in FIELDS}
    if name == "F3":
        return {f: I + 0.3 * hermitian_offdiag(rng) for f in FIELDS}
    raise ValueError(name)


def run_class(kind, rng):
    rows = {}
    changes = {fr: {"ratios": [], "absV": [], "J": [], "Jrel": [], "DR": []} for fr in ("F1", "F2", "F3")}
    for _ in range(N_INST):
        Yu, Yd, Ye = instance(rng, kind)
        r0, v0, j0, d0 = outputs(Yu, Yd, Ye)
        for fr in ("F1", "F2", "F3"):
            K = frame(rng, fr)
            r1, v1, j1, d1 = outputs(canon(Yu, K["Q"], K["u"]), canon(Yd, K["Q"], K["d"]), canon(Ye, K["L"], K["e"]))
            changes[fr]["ratios"].append(np.max(np.abs(r1 - r0) / np.abs(r0)))
            changes[fr]["absV"].append(np.max(np.abs(v1 - v0)))
            changes[fr]["J"].append(abs(j1 - j0))
            if abs(j0) > 1e-14:
                changes[fr]["Jrel"].append(abs(j1 - j0) / abs(j0))
            changes[fr]["DR"].append(abs(d1 - d0) / abs(d0))
    for fr in ("F1", "F2", "F3"):
        rows[fr] = {k: ((float(np.median(v)), float(np.max(v))) if len(v) else None) for k, v in changes[fr].items()}
    return rows


def main():
    print("P-510 frame check (data-free). numpy", np.__version__, "; seed", SEED, "; instances per class", N_INST)
    print("change against F0: median / largest. ratios and DR relative; |V| and J absolute; J rel. over |J0| > 1e-14.")
    print("F1: one scale per field. F2: common per-generation factors diag(1,2,3) times one scale per field.")
    print("F3: kinetic mixing, K = I + 0.3 H for every field.")
    rng = np.random.default_rng(SEED)
    for kind in ("generic", "hierarchical", "diagonal"):
        rows = run_class(kind, rng)
        print()
        print(f"[{kind}]")
        print(f"  {'frame':5s} {'six ratios':>24s} {'CKM |V|':>24s} {'J (abs)':>24s} {'J (rel)':>24s} {'double ratio':>24s}")
        for fr in ("F1", "F2", "F3"):
            cells = []
            for k in ("ratios", "absV", "J", "Jrel", "DR"):
                if rows[fr][k] is None:
                    cells.append("n/a")
                    continue
                med, mx = rows[fr][k]
                cells.append(f"{med:9.2e} / {mx:9.2e}")
            print(f"  {fr:5s} " + " ".join(f"{c:>24s}" for c in cells))
    print()
    print("[the two-by-two example] up = diag(1, 0), down = [[1, 1], [1, 1]], K_Q^(-1/2) = diag(d1, d2)")
    Yu = np.diag([1.0, 0.0])
    Yd = np.array([[1.0, 1.0], [1.0, 1.0]])
    for d1, d2 in ((1.0, 1.0), (1.0, 2.0), (2.0, 1.0)):
        M = np.diag([d1, d2])
        Uu, _ = np.linalg.svd(M @ Yu)[:2]
        Ud, _ = np.linalg.svd(M @ Yd)[:2]
        heavy_u, heavy_d = Uu[:, 0], Ud[:, 0]
        angle = np.degrees(np.arccos(min(1.0, abs(np.vdot(heavy_u, heavy_d)))))
        print(f"  d = ({d1:.0f}, {d2:.0f}): heavy-state mixing angle {angle:.4f} deg; arctan(d2/d1) = "
              f"{np.degrees(np.arctan2(d2, d1)):.4f} deg")


if __name__ == "__main__":
    main()
