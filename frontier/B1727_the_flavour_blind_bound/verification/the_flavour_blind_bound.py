"""B1727 (P-299): the flavour-blind bound.  In B1656's four-channel coupling (the functions B1723 sealed) a flavour-blind
Higgs S = 1 gives, in every sector, Y = c*1 + [a]_x (c the weight on the channel 1, a in C^3 from the weights on i, j, k),
and then m2/m3 >= 1/3, sharp.  Parts:
    A  the structure: the coupling is linear in the four channel weights; the unit weights give 1 and the three elementary
       antisymmetric matrices
    B  the minimum of m2/m3 over (c, a) by 400 Nelder-Mead starts (c = 1 without loss; a modulo SO(3) and conjugation)
    C  the proof's three steps on 200 000 random (c, a) over six decades of |a|:
         (i) |c| <= sigma_2 (M + M^T = 2c 1 and Weyl), (ii) sigma_1(A) = sigma_2(A), (iii) sigma_1 <= 3 sigma_2
    D  the equality case c = 1, a = 2i e_1 (singular values 3, 1, 1)
    python3 -B the_flavour_blind_bound.py      # writes the_flavour_blind_bound.json beside itself
Importing computes nothing."""
import sys, json, pathlib
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())


def frame():
    sys.path.insert(0, str(ROOT / "frontier" / "B1723_the_golden_valley" / "verification")); _a = sys.argv; sys.argv = ["x"]
    import b1656_funcs as B
    sys.argv = _a
    return B


def cross(a):
    return np.array([[0, -a[2], a[1]], [a[2], 0, -a[0]], [-a[1], a[0], 0]], dtype=complex)


def part_a():
    B = frame(); I2 = np.eye(2, dtype=complex)
    unit = {s: B.coupling(I2, B.weighted_M({k: (1.0 if k == s else 0.0) for k in B.UNITS})) for s in B.UNITS}
    rng = np.random.default_rng(1727); lin, sym = 0.0, 0.0
    for _ in range(20):
        u = {k: complex(*rng.normal(size=2)) for k in B.UNITS}
        Y = B.coupling(I2, B.weighted_M(u))
        lin = max(lin, float(np.max(np.abs(Y - sum(u[s] * unit[s] for s in B.UNITS)))))
        sym = max(sym, float(np.max(np.abs((Y + Y.T) / 2 - u["1"] * np.eye(3)))))
    anti = max(float(np.max(np.abs(unit[s] + unit[s].T))) for s in ("i", "j", "k"))
    return {"unit_images": {s: np.round(unit[s].real, 12).astype(int).tolist() for s in B.UNITS},
            "unit_images_imag_max": max(float(np.max(np.abs(unit[s].imag))) for s in B.UNITS),
            "linearity_max": lin, "symmetric_part_minus_c1_max": sym, "ijk_images_antisymmetry_max": anti}


def ratio(c, a):
    s = np.linalg.svd(c * np.eye(3) + cross(a), compute_uv=False); return float(s[1] / s[0])


def part_b():
    from scipy.optimize import minimize
    def f(p):
        X, Yn, th = p
        return ratio(1.0, np.array([X, 0, 0]) + 1j * np.array([Yn * np.cos(th), Yn * np.sin(th), 0]))
    rng = np.random.default_rng(299); best = None
    for _ in range(400):
        o = minimize(f, rng.normal(size=3) * 2, method="Nelder-Mead", options={"xatol": 1e-12, "fatol": 1e-14, "maxiter": 20000})
        if best is None or o.fun < best.fun: best = o
    X, Yn, th = best.x
    return {"min_ratio": float(best.fun), "at_abs_x": abs(float(X)), "at_abs_y": abs(float(Yn)), "starts": 400}


def part_c(n=200000, seed=299):
    rng = np.random.default_rng(seed); w1 = w2 = w3 = -np.inf; rmin = np.inf
    for _ in range(n):
        sc = 10 ** rng.uniform(-3, 3); c = complex(*rng.normal(size=2)); a = (rng.normal(size=3) + 1j * rng.normal(size=3)) * sc
        A = cross(a); s = np.linalg.svd(c * np.eye(3) + A, compute_uv=False); sa = np.linalg.svd(A, compute_uv=False)
        w1 = max(w1, (abs(c) - s[1]) / s[0]); w2 = max(w2, abs(sa[0] - sa[1]) / sa[0]); w3 = max(w3, (s[0] - 3 * s[1]) / s[0])
        rmin = min(rmin, s[1] / s[0])
    return {"draws": n, "step_i_max_(|c|-s2)/s1": float(w1), "step_ii_max_rel_(s1A-s2A)": float(w2),
            "step_iii_max_(s1-3s2)/s1": float(w3), "min_ratio_random": float(rmin)}


def part_d():
    return {"singular_values": np.linalg.svd(np.eye(3) + cross(np.array([2j, 0, 0])), compute_uv=False).tolist()}


def main():
    out = {"A": part_a(), "B": part_b(), "C": part_c(), "D": part_d()}
    json.dump(out, open(HERE / "the_flavour_blind_bound.json", "w"), indent=1)
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
