"""B1743 (POST HOC exploration, labelled; not a test): the nine's target on main's instrument.
(A) the web seat's INVERSE HIGGS one-Higgs optimum (one free direction h in CP^2, read S in every sector, c = 3)
    reproduced on main at its best rows, with the full complex direction: delta = e1 coefficient / leading null
    coefficient, epsilon = other null coefficient / leading, the invariant |h.h|/|h|^2, and the Fubini-Study distance to
    each record form at that tau (R, DR, D2R, F_a for a = -10, -6, -2, 6, 14, 22, each as is and conjugated).
(B) the web seat's R5 (revision_checks.py): in the idealised up channel (u = a3 n, n = (0, 1, i)/sqrt2, w = 0, h_0 = 0)
    B1736's closed form gives m1 = 0, m2 m3 = |a3|^2 |h.h| and m2/m3 >= |h.h|/4 for every unit h (2 000 random draws).
    python3 -B target.py      # writes target.json"""
import sys, json, math, pathlib
from fractions import Fraction as Fr
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import pencils as P        # noqa: E402

# the seat's A1 best rows (inverse_higgs_two_higgs_readout.json, its eight best) and its best L_max rows
ROWS = [(6, 0.4375, 2.1, "L_2"), (0, 0.5625, 2.1, "L_2"), (0, 0.6875, 2.0, "L_2"), (6, 0.3125, 2.0, "L_2"),
        (0, 0.5625, 2.2, "L_2"), (6, 0.4375, 2.2, "L_2"), (0, 0.4375, 2.3, "L_2"), (6, 0.5625, 2.3, "L_2"),
        (0, 0.1875, 3.2, "L_max"), (6, 0.8125, 3.2, "L_max")]
E1 = np.array([1, 0, 0], dtype=complex); N0 = np.array([0, 1, 1j]) / math.sqrt(2); N1 = np.array([0, 1, -1j]) / math.sqrt(2)


def decompose(h):
    c1, c0, c0b = np.vdot(E1, h), np.vdot(N0, h), np.vdot(N1, h)
    lead, other, name = (c0, c0b, "h0") if abs(c0) >= abs(c0b) else (c0b, c0, "conj h0")
    return {"leading": name, "|e1|,|h0|,|conj h0|": [round(abs(c1), 5), round(abs(c0), 5), round(abs(c0b), 5)],
            "delta": [round((c1 / lead).real, 5), round((c1 / lead).imag, 5)], "epsilon": [round((other / lead).real, 5), round((other / lead).imag, 5)],
            "|h.h|/|h|^2": round(float(abs(h @ h) / np.vdot(h, h).real), 5)}


def optimum(k, re_t, im_t, hor):
    a, b = P.LINES[k]; t = complex(re_t, im_t); B = P.R.CEN._modules()["B"]; M = P.SC.channels(re_t, im_t, a, b); F = P.forms(t)
    rng = np.random.default_rng(1720)
    starts = [F[x] for x in F] + [np.conj(F[x]) for x in F] + [rng.normal(size=3) + 1j * rng.normal(size=3) for _ in range(6)]
    c, x = P.fit_free(M, hor, B, starts); h = np.array([x[0] + 1j * x[1], x[2] + 1j * x[3], x[4] + 1j * x[5]]); h /= np.linalg.norm(h)
    n, J = P.nine_of(h, M, hor, B)
    out = {"line": "(%s, %s)" % (a, b), "tau": [re_t, im_t], "hor": hor, "chi2_nine": round(c, 3), "model/data": np.round(np.exp(n - P.T9), 4).tolist(), "J": J}
    out.update(decompose(h))
    out["FS distance to the record forms"] = {nm + s: round(float(np.arccos(min(1.0, abs(np.vdot(v, h))))), 3) for nm in F for s, v in (("", F[nm]), ("~", np.conj(F[nm])))}
    return out


def r5():
    rng = np.random.default_rng(5); worst_id, worst_bound, m1max = 0.0, np.inf, 0.0
    for _ in range(2000):
        h = rng.normal(size=3) + 1j * rng.normal(size=3); h /= np.linalg.norm(h)
        a3 = complex(rng.normal(), rng.normal()); u = a3 * N0
        Y = np.outer(u, h) + np.outer(h, u) - (u @ h) * np.eye(3)
        s = np.linalg.svd(Y, compute_uv=False)
        m1max = max(m1max, s[2] / s[0])
        worst_id = max(worst_id, abs(s[0] * s[1] - abs(a3) ** 2 * abs(h @ h)) / abs(a3) ** 2)
        worst_bound = min(worst_bound, (s[1] / s[0]) / (abs(h @ h) / 4))
    return {"draws": 2000, "max m1/m3": m1max, "max |m2 m3 - |a3|^2 |h.h|| / |a3|^2": worst_id, "min (m2/m3) / (|h.h|/4)": worst_bound}


if __name__ == "__main__":
    res = {"R5": r5()}; print("R5", res["R5"], flush=True)
    res["optima"] = []
    for row in ROWS:
        o = optimum(*row); res["optima"].append(o)
        print(o["line"], o["tau"], o["hor"], "chi2_nine", o["chi2_nine"], "delta", o["delta"], "epsilon", o["epsilon"], "|h.h|", o["|h.h|/|h|^2"],
              "nearest form", min(o["FS distance to the record forms"].items(), key=lambda kv: kv[1]), flush=True)
    (HERE / "target.json").write_text(json.dumps(res, indent=1) + "\n")
