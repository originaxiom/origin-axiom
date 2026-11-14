"""Where does the frame's zero test (|R_s| > 1e-12) misfire? For frame C's 24 points of order 5 and the three sectors,
the channel residues by B1906's closed form at 40 digits; an exact zero is a characteristic = (1/2, 1/2) mod 1 (exact
rationals). Reports, per height, the smallest non-zero |R_s| relative to the largest, and how many non-zero residues fall
below the frame's 1e-12."""
import sys, pathlib
from fractions import Fraction as Fr
import mpmath as mp
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
sys.path.insert(0, str(ROOT / "frontier" / "B1723_the_golden_valley" / "verification")); sys.argv = ["x"]
import b1656_funcs as B
mp.mp.dps = 40; I = mp.mpc(0, 1); H = Fr(1, 2)
POINTS = [(Fr(i, 5), Fr(j, 5)) for i in range(5) for j in range(5) if (i, j) != (0, 0)]
def chars(p1, p2, ql, qr):
    x = (ql * p1, -2 * ql * p2); y = (qr * p1, -2 * qr * p2)          # twist_of(q w) with w = p1 tau - p2 (exact)
    ap, am = x[0] + y[0], x[0] - y[0]; bp, bm = (x[1] + y[1]) / 2, (x[1] - y[1]) / 2
    cs = {"1": (ap + H, bp + H), "i": (ap + H, bp), "j": (ap, bp + H), "k": (ap, bp)}
    ds = {"1": (am + H, bm + H), "i": (am + H, bm), "j": (am, bm + H), "k": (am, bm)}
    return x, cs, ds
def is_zero(c): return (c[0] - H) % 1 == 0 and (c[1] - H) % 1 == 0
for yv in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12]:
    t = mp.mpc("0.13", yv); eta = mp.exp(I * mp.pi * t / 12) * mp.qp(mp.exp(2 * I * mp.pi * t)); t1p = 2 * mp.pi * eta ** 3
    small, below, nz = mp.inf, 0, 0
    for p1, p2 in POINTS:
        for sec, (lf, rf) in B.SECTORS.items():
            x, cs, ds = chars(p1, p2, B.SIXY[lf], B.SIXY[rf])
            e = mp.exp(-2 * I * mp.pi * mp.mpf(x[0].numerator) / x[0].denominator)
            kap = {"1": -I * e, "i": mp.mpf(-1), "j": -e, "k": I}
            R = {}
            for s in B.UNITS:
                if is_zero(cs[s]) or is_zero(ds[s]): R[s] = None; continue
                R[s] = abs(kap[s] * B.thc_mp(mp.mpf(cs[s][0].numerator) / cs[s][0].denominator, mp.mpf(cs[s][1].numerator) / cs[s][1].denominator, 0, t)
                           * B.thc_mp(mp.mpf(ds[s][0].numerator) / ds[s][0].denominator, mp.mpf(ds[s][1].numerator) / ds[s][1].denominator, 0, t) / t1p)
            live = [r for r in R.values() if r is not None]; mx = max(live)
            for r in live:
                nz += 1; small = min(small, r / mx); below += r < 1e-12
    print("y %4.1f  smallest non-zero |R_s|/max %.2e  non-zero residues below 1e-12: %d of %d" % (yv, float(small), below, nz), flush=True)
