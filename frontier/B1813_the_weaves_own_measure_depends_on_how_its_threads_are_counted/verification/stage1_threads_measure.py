"""Stage 1 of the whole-existence computation (FRAME_CARD.md; data-free; exploratory, audit room): the measure the weave's
threads produce.  Every primitive positive class (both letters; B1720's necklaces) up to word length NMAX; for each, its
closed geodesic (the axis of a representative A, one period of length 2 arccosh(t/2)) sampled uniformly in arclength and
reduced to the standard fundamental domain.  Compared with hyperbolic area's height marginal on F (exact: density
proportional to w(y)/y^2, w(y) = 1 for y >= 1 and 1 - 2 sqrt(1 - y^2) below; total pi/3).  Beside it, the apex rule's
heights (Lagrange/2, B1720) and each thread's own flat lines by B1733's Smith rule (orders N <= 30).
    python3 stage1_threads_measure.py      # writes stage1_threads_measure.json beside itself"""
import glob, importlib.util, json, math, pathlib, sys
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / "frontier").is_dir())
def load(path, name):
    sp = importlib.util.spec_from_file_location(name, path); m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
TG = load(glob.glob(str(ROOT / "frontier/B1720_*/verification/thread_geometry.py"))[0], "tg")
OL = load(glob.glob(str(ROOT / "frontier/B1733_*/verification/the_threads_own_lines.py"))[0], "ol")

NMAX, DENS = 14, 40.0                       # word length bound; samples per unit hyperbolic length


def reduce(z):
    for _ in range(10000):
        z = complex(z.real - math.floor(z.real + 0.5), z.imag)
        if abs(z) < 1 - 1e-12: z = -1 / z
        else: return z
    return z


def geodesic_heights(A):
    a, b, c, d = float(A[0][0]), float(A[0][1]), float(A[1][0]), float(A[1][1]); t = a + d
    disc = (d - a) ** 2 + 4 * b * c; r1 = ((a - d) + math.sqrt(disc)) / (2 * c); r2 = ((a - d) - math.sqrt(disc)) / (2 * c)
    m, r = (r1 + r2) / 2, abs(r1 - r2) / 2; ell = 2 * math.acosh(abs(t) / 2)
    n = max(8, int(DENS * ell)); s = np.linspace(0.0, ell, n, endpoint=False)
    zs = m + r * (np.tanh(s) + 1j / np.cosh(s))
    return [reduce(complex(z)).imag for z in zs], ell


def hyp_cdf_above(Y):
    """P(y > Y) under hyperbolic area on F"""
    tot = math.pi / 3
    if Y >= 1: return (1 / Y) / tot
    ys = np.linspace(Y, 1, 4001); w = 1 - 2 * np.sqrt(np.maximum(0.0, 1 - ys ** 2))
    return (np.trapezoid(w / ys ** 2, ys) + 1.0) / tot


words = sorted(TG.necklaces(2, NMAX), key=lambda w: (len(w), w))
H, Wt, apex, lines = [], [], [], {}
for w in words:
    A = TG.mat(w); hs, ell = geodesic_heights(A)
    H.extend(hs); Wt.extend([ell / len(hs)] * len(hs))
    apex.append(TG.lagrange(w) / 2)
    M = [[int(A[0][0]), int(A[0][1])], [int(A[1][0]), int(A[1][1])]]
    for N in range(2, 31):
        k = len(OL.fixed(M, N)) if hasattr(OL, "fixed") else 0
        if k: lines[N] = lines.get(N, 0) + k
H, Wt, apex = np.array(H), np.array(Wt), np.array(apex)
grid = [0.9, 1.0, 1.2, 1.5, 2.0, 3.0, 4.0, 6.0]
geo = {str(Y): {"geodesics (arclength)": float(Wt[H > Y].sum() / Wt.sum()), "hyperbolic area": hyp_cdf_above(Y),
                "apex rule": float((apex > Y).mean())} for Y in grid}
out = {"classes": len(words), "word length": [2, NMAX], "samples": int(len(H)),
       "P(Im tau > Y)": geo,
       "max |geodesic - hyperbolic| over the grid": max(abs(v["geodesics (arclength)"] - v["hyperbolic area"]) for v in geo.values()),
       "lines fixed, by order N (summed over threads)": lines}
(HERE / "stage1_threads_measure.json").write_text(json.dumps(out, indent=1), encoding="utf-8")
print(json.dumps({k: v for k, v in out.items()}, indent=1))
