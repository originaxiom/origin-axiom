"""B1743 (P-352), POST HOC exploration (labelled; not a test): is the web seat's one-Higgs optimum (one free direction
h in CP^2, read S in every sector, c = 3: chi2_nine 17.3 on its best rows) inside a PRINCIPLED PENCIL -- the span of two
forms on record, one complex number lambda free (2 reals) instead of a free direction (4 reals)?

Pencils (h = A + lambda B, lambda in C or infinity; and the conjugate pencil, i.e. reading S~ in every sector):
  DR|R     the covariant-derivative pencil (h_w = DR + (w/12) E2* R is this pencil at real-ish lambda)
  DR|D2R   the Serre tower's next step
  F22|Fm2  the h(20, 1) members (W143: F_-2 and F_22 share the multiplier, r = 20)
  F6|Fm6   the h(12, 1) members
  F14|Fm10 the h(4, 1) members
  FREE     the free direction (A1), for reference on main's instrument
On B1742's grid (ten (2/5, k/10) lines, Re tau 0.0625..0.9375, Im tau 2.0..3.5, both horocycles): the minimum chi2_nine
of each pencil, where, its lambda, and the chi2_six there.  Main's B1740 instrument via B1742's repro (unmodified)."""
import sys, json, math, pathlib, importlib.util
from fractions import Fraction as Fr
import numpy as np
from scipy.optimize import least_squares
ROOT = pathlib.Path(__file__).resolve().parents[3]
V42 = ROOT / "frontier" / "B1742_two_higgs_verified_on_main" / "verification"
sys.path.insert(0, str(V42))
import repro as R          # noqa: E402
import scan as SC          # noqa: E402

LINES = [(Fr(2, 5), Fr(k, 10)) for k in range(10)]
RES = [0.0625 + 0.125 * i for i in range(8)]
IMS = [round(2.0 + 0.1 * j, 10) for j in range(16)]
T6, T9 = R.targets(); S6, S9 = R.CMP.sigmas(); LC = math.log(3.0)


def forms(t):
    """the record's directions at tau, as complex 3-vectors"""
    import mpmath as mp
    te = R.CEN._modules()["te"]; T = mp.mpc(t.real, t.imag)
    f = {"R": [complex(te.ev(c, T)) for c in te.B[0]], "DR": [complex(te.ev(c, T)) for c in te.B[1]], "D2R": [complex(te.ev(c, T)) for c in te.B[2]]}
    for a in (-10, -6, -2, 6, 14, 22):
        f["F%s" % a if a > 0 else "Fm%d" % -a] = R.direction(a, t)
    return {k: np.array(v, dtype=complex) / np.linalg.norm(v) for k, v in f.items()}


PENCILS = [("DR", "R"), ("DR", "D2R"), ("F22", "Fm2"), ("F6", "Fm6"), ("F14", "Fm10")]


def nine_of(h, M, hor, B):
    S = R.Smat(list(h), B); Y = {s: B.coupling(S, M[(s, hor)]) for s in ("up", "down", "lep")}
    six = []
    for s in ("up", "down", "lep"):
        sv = np.maximum(np.linalg.svd(Y[s], compute_uv=False), 1e-300); six += [math.log(sv[1] / sv[0]), math.log(sv[2] / sv[0])]
    six = np.array(six) + np.array([0, 0, 0, 0, LC, -LC])
    Uu = np.linalg.svd(Y["up"])[0][:, ::-1]; Ud = np.linalg.svd(Y["down"])[0][:, ::-1]; V = np.conj(Uu.T) @ Ud
    ck = np.log(np.maximum([abs(V[0, 1]), abs(V[1, 2]), abs(V[0, 2])], 1e-300))
    J = float(np.imag(V[0, 1] * V[1, 2] * np.conj(V[0, 2]) * np.conj(V[1, 1])))
    return np.concatenate([six, ck]), J


def res9(h, M, hor, B):
    n, _ = nine_of(h, M, hor, B); return (n - T9) / S9


def fit_pencil(A, Bv, M, hor, B, conj=False):
    if conj: A, Bv = np.conj(A), np.conj(Bv)
    best = None
    for lam0 in [0, 1, -1, 1j, -1j, 3, -3, 3j, -3j, 0.3, -0.3, 0.3j, -0.3j]:
        f = lambda p: res9(A + (p[0] + 1j * p[1]) * Bv, M, hor, B)
        try:
            r = least_squares(f, [np.real(lam0), np.imag(lam0)], method="trf", max_nfev=200)
        except Exception:
            continue
        c = float((r.fun ** 2).sum())
        if best is None or c < best[0]: best = (c, complex(r.x[0], r.x[1]))
    try:
        cinf = float((res9(Bv, M, hor, B) ** 2).sum())
    except Exception:
        cinf = float("inf")
    if best is None or cinf < best[0]: best = (cinf, complex("inf"))
    return best


def fit_free(M, hor, B, starts):
    best = None
    for h0 in starts:
        f = lambda p: res9(np.array([p[0] + 1j * p[1], p[2] + 1j * p[3], p[4] + 1j * p[5]]), M, hor, B)
        r = least_squares(f, np.concatenate([[x.real, x.imag] for x in h0]), method="trf", max_nfev=400)
        c = float((r.fun ** 2).sum())
        if best is None or c < best[0]: best = (c, r.x)
    return best


def point(task):
    k, re_t, im_t = task; a, b = LINES[k]; t = complex(re_t, im_t)
    B = R.CEN._modules()["B"]; M = SC.channels(re_t, im_t, a, b); F = forms(t); out = []
    for hor in ("L_max", "L_2"):
        row = {"line": k, "Re": re_t, "Im": im_t, "hor": hor}
        for A, Bn in PENCILS:
            for cj in (False, True):
                c, lam = fit_pencil(F[A], F[Bn], M, hor, B, conj=cj)
                row["%s|%s%s" % (A, Bn, "~" if cj else "")] = [c, [lam.real, lam.imag] if np.isfinite(lam) else "inf"]
        out.append(row)
    return out


if __name__ == "__main__":
    from multiprocessing import Pool
    HERE = pathlib.Path(__file__).resolve().parent
    tasks = [(k, r, y) for k in range(10) for r in RES for y in IMS]
    allr = []
    with Pool(8) as P:
        for i, o in enumerate(P.imap_unordered(point, tasks, chunksize=2)):
            allr += o
            if i % 80 == 0: print("points", i, flush=True)
    (HERE / "pencils.json").write_text(json.dumps(allr) + "\n")
    keys = [k for k in allr[0] if "|" in k]
    for key in keys:
        best = min(allr, key=lambda r: r[key][0])
        n_below = sum(1 for r in allr if r[key][0] < 21.67)
        print("%-12s min chi2_nine %8.2f at line %d, %.4f + %.2fi, %s, lambda %s; rows below 21.67: %d" % (
            key, best[key][0], best["line"], best["Re"], best["Im"], best["hor"], best[key][1], n_below))
