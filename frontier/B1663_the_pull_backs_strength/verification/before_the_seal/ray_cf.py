"""The ray instrument by digits (design; disclosed): the geodesic coded by continued-fraction digits a_1, a_2, ... is cut at
its crossings of Re z = 0; between crossings k and k+1 it is the arc of the semicircle with endpoints
u_k = [a_k; a_{k+1}, ...] > 1 and v_k = -[0; a_{k-1}, a_{k-2}, ...] in (-1, 0), from Re z = 0 to Re z = a_k (then
z -> 1/(z - a_k) reflected, f being mirror-invariant, gives the next arc). Everything O(1); no precision loss.
ray_average(digits) = sum_k int_arc_k f ds / sum_k len_k over k = 2 .. K-20 (20 digits of look-ahead for u_k)."""
import sys, math, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import numpy as np
from motion_defect import f_fast as _f_fast, reduce
YCUT = 7.0
def f_fast(t):
    """f, set to 0 above height YCUT (f(4i) = 9.5e-4, f(6i) < 1e-5: the theta series underflow there)"""
    return 0.0 if t.imag > YCUT else _f_fast(t)
GX, GW = np.polynomial.legendre.leggauss(24)
def cf_val(ds):
    x = 0.0
    for a in reversed(ds): x = 1.0/(a + x) if (a + x) else float("inf")
    return x                      # [0; ds...]
def arc(u, v, a):
    c, r = (u + v)/2, (u - v)/2
    t0 = math.acos(max(-1.0, min(1.0, -c/r))); t1 = math.acos(max(-1.0, min(1.0, (a - c)/r)))   # theta at Re=0, Re=a (t1 < t0)
    s0, s1 = math.log(math.tan(t0/2)), math.log(math.tan(t1/2)); L = abs(s0 - s1); tot = 0.0
    n = max(1, int(math.ceil(L/0.6)))
    for j in range(n):
        lo, hi = s1 + (s0 - s1)*j/n, s1 + (s0 - s1)*(j + 1)/n
        for x, w in zip(GX, GW):
            s = (x + 1)/2*(hi - lo) + lo; th = 2*math.atan(math.exp(s))
            tot += w*(hi - lo)/2*f_fast(reduce(complex(c + r*math.cos(th), r*math.sin(th))))
    return tot, L
def ray_average(digits, look=20):
    num = den = 0.0
    for k in range(1, len(digits) - look):
        u = digits[k] + cf_val(digits[k + 1:k + 1 + look]); v = -cf_val(digits[max(0, k - look):k][::-1])
        t, L = arc(u, v, digits[k]); num += t; den += L
    return num/den, den
if __name__ == "__main__":
    import random
    rng = random.Random(5)
    def gauss_digits(n):
        x = rng.random(); out = []
        num, den = rng.getrandbits(400), 1 << 400
        while len(out) < n and den:
            q, r = divmod(num, den); out.append(q); num, den = den, r
        return [a for a in out[1:] if a > 0][:n]
    vals = [ray_average(gauss_digits(160))[0] for _ in range(40)]
    print(f"Lebesgue control (40 rays, ~140 digits each): {np.mean(vals):.4f} +- {np.std(vals)/math.sqrt(len(vals)):.4f} (Liouville 0.3150)")
    geo = []
    for _ in range(40):
        d = []
        while len(d) < 160:
            a = 1
            while rng.random() < 0.5: a += 1
            d.append(a)
        geo.append(ray_average(d)[0])
    print(f"geometric digits (the p = 0 walk's law): {np.mean(geo):.4f} +- {np.std(geo)/math.sqrt(len(geo)):.4f}")
