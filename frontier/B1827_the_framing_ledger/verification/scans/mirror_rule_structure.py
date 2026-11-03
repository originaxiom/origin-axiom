"""P-555 exploration (labelled; no measured value read): the mirror rule's mixing at the frame's own hierarchical points.
At random addresses (a census line of order <= 12, a direction of the twelve, a radius, readings, tau in the band), the
frame's V = U_up(A)^H U_down(A) and the rule's V_mir = U_up(A)^H U_down(A*), A* = (-conj tau, (alpha, -b)).  Kept: points
where up and down are both hierarchical (m2/m3 < 0.1, m1/m3 < 0.01; a coarse filter, disclosed).  Reported: the
distributions of |V_ud|, |V_us|, |V_cb|, |V_ub|, |V_td|, |V_ub|/|V_td|, sin(delta) for both."""
import json, math, pathlib, sys
from fractions import Fraction as F
from multiprocessing import Pool
import numpy as np
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))


def lines():
    out = set()
    for N in range(1, 13):
        for a in range(N):
            for b in range(N):
                if math.gcd(math.gcd(a, b), N) == 1: out.add((F(a, N), F(b, N)))
    return sorted(out)


def one(seed):
    from mirror_rule_probe import sector_U, Z
    rng = np.random.default_rng(seed); L_ = lines(); dirs = [d for d in Z.DIRS if d != "F_-2"]; res = []
    for _ in range(60):
        line = L_[int(rng.integers(len(L_)))]; tau = complex(float(rng.uniform(0.0, 0.5)), float(rng.uniform(1.0, 4.0)))
        d = dirs[int(rng.integers(len(dirs)))]; L = Z.radii(tau)[int(rng.integers(2))]; ru, rd = int(rng.integers(2)), int(rng.integers(2))
        try:
            Uu, su = sector_U(tau, line, d, L, ru, "up"); Ud, sd = sector_U(tau, line, d, L, rd, "down")
            Udm, sdm = sector_U(complex(-tau.real, tau.imag), (line[0], -line[1]), d, L, rd, "down")
        except Exception:
            continue
        hier = all(s[2] > 0 and s[1] / s[2] < 0.1 and s[0] / s[2] < 0.01 and s[0] / s[2] > 1e-12 for s in (su, sd))
        if not hier: continue
        out = {}
        for name, V in (("same", Uu.conj().T @ Ud), ("mirror", Uu.conj().T @ Udm)):
            A = np.abs(V); J = float(np.imag(V[0, 1] * V[1, 2] * np.conj(V[0, 2]) * np.conj(V[1, 1])))
            s12, s23, s13 = A[0, 1], A[1, 2], A[0, 2]
            c13 = math.sqrt(max(1 - s13 ** 2, 1e-300)); jm = s12 * s23 * s13 * math.sqrt(max(1 - s12 ** 2 - s13 ** 2, 0)) * math.sqrt(max(1 - s23 ** 2 - s13 ** 2, 0)) / c13 ** 2
            out[name] = [A[0, 0], A[0, 1], A[1, 2], A[0, 2], A[2, 0], J, abs(J) / jm if jm > 0 else float("nan")]
        res.append(out)
    return res


if __name__ == "__main__":
    with Pool(4) as P:
        R = [r for chunk in P.map(one, range(40)) for r in chunk]
    print("hierarchical points kept:", len(R))
    names = ["|V_ud|", "|V_us|", "|V_cb|", "|V_ub|", "|V_td|", "J", "sin d"]
    summary = {}
    for key in ("same", "mirror"):
        M = np.array([r[key] for r in R]); summary[key] = {}
        print("==", key)
        for i, n in enumerate(names):
            col = M[:, i]; col = col[np.isfinite(col)]
            q = np.quantile(np.abs(col) if n == "J" else col, [.1, .5, .9]); summary[key][n] = q.tolist()
            print("   %-7s q10 %.3g  median %.3g  q90 %.3g" % (n, *q))
        ratio = M[:, 3] / np.maximum(M[:, 4], 1e-300)
        frac = float(np.mean(ratio < 1)); summary[key]["frac |V_ub|<|V_td|"] = frac
        print("   |V_ub|/|V_td|: median %.3g ; fraction with |V_ub| < |V_td| = %.3f ; with |V_ud| > 0.9: %.3f" % (np.median(ratio), frac, float(np.mean(M[:, 0] > 0.9))))
        both = (ratio < 1) & (M[:, 0] > 0.9); summary[key]["frac SM-ordered corner & |V_ud|>0.9"] = float(np.mean(both))
        print("   both (|V_ub| < |V_td| and |V_ud| > 0.9): %.3f" % float(np.mean(both)))
    pathlib.Path(__file__).with_suffix(".json").write_text(json.dumps({"n": len(R), "summary": summary}, indent=1))
