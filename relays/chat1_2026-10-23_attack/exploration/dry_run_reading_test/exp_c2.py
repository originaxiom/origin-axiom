import importlib.util, json, sys, math, time, pathlib
from fractions import Fraction as Fr
import numpy as np
from scipy.optimize import least_squares
HERE = pathlib.Path(__file__).resolve().parent
sys.argv = ["x"]
spec = importlib.util.spec_from_file_location("rt", HERE / "reading_test.py"); rt = importlib.util.module_from_spec(spec); sys.modules["rt"] = rt; spec.loader.exec_module(rt)
sms = rt.sms; T9, SIG = rt.T9, rt.SIG
st = np.load(HERE / "reading_test_store.npz"); U, H = st["U"], st["H"]
rng = np.random.default_rng(1741)
cases = []
for n in range(24):
    p = int(rng.integers(0, 20)); hr = int(rng.integers(0, 2))
    if n < 12:
        t = complex(*rng.normal(size=2)); r = 10 ** rng.uniform(-4, -1); ph = rng.uniform(0, 2 * math.pi)
        h0 = np.array([2 * t, 1 - t * t, 1j * (1 + t * t)]); h0 /= np.linalg.norm(h0)
        hp = h0 + r * np.exp(1j * ph) * np.conj(h0)
    else:
        z = rng.normal(size=6); hp = z[:3] + 1j * z[3:]
    hp = hp / np.linalg.norm(hp)
    cases.append((n, p, hr, hp, t if n < 12 else None, r if n < 12 else None))

def tube_h(y):
    # y = (t_re, t_im, log10|s|, arg s); chart: |t| <= 1 uses h0(t); else h0 at 1/t from the n-bar side
    t = complex(y[0], y[1]); s = 10 ** y[2] * np.exp(1j * y[3])
    h0 = np.array([2 * t, 1 - t * t, 1j * (1 + t * t)]); h0 = h0 / np.linalg.norm(h0)
    return h0 + s * np.conj(h0)

def refine_tube(Uh, y0, Tp):
    def res(y):
        L, _, _ = sms.nine_batch(Uh, tube_h(y)[None], Tp, SIG); return (L[0] - Tp) / SIG
    try:
        r = least_squares(res, y0, method="trf", max_nfev=2000, xtol=1e-12, ftol=1e-12)
        return float(np.sum(r.fun ** 2)), r.x
    except Exception as e:
        return None

def to_tube(h):
    # find t, s with h ∝ h0(t) + s conj h0(t): h = a h0 + b conj(h0), h0 null in span(Re h, Im h)
    # via: the null directions of the plane P = span_R(Re h, Im h): solve on the 2x2 Gram
    a_, b_ = h.real, h.imag
    # orthonormal basis of P
    e1 = a_ / np.linalg.norm(a_); b2 = b_ - (b_ @ e1) * e1; e2 = b2 / np.linalg.norm(b2)
    n0 = (e1 + 1j * e2) / math.sqrt(2)   # null
    # t from n0: n0 ∝ (2t, 1-t^2, i(1+t^2)) -> t = n0[0] / (n0[1] - i n0[2]) ... use: 1 - t^2 = c n1, i(1+t^2) = c n2 => n1 - i n2 ... solve
    c1, c2 = np.vdot(n0, h), np.vdot(np.conj(n0), h)
    if abs(c2) > abs(c1):
        n0 = np.conj(n0); c1, c2 = c2, c1
    # t: h0 = (2t, 1-t^2, i(1+t^2)); h0[1] - i*h0[2]... (1-t^2) + (1+t^2) = 2 -> h0[1] - i h0[2] = 2 ; h0[1] + i h0[2] = -2t^2
    k = n0[1] - 1j * n0[2]
    t = n0[0] / k   # since h0[0] = 2t and h0[1]-i h0[2] = 2
    h0 = np.array([2 * t, 1 - t * t, 1j * (1 + t * t)]); h0 /= np.linalg.norm(h0)
    s = np.vdot(np.conj(h0), h) / np.vdot(h0, h)
    return np.array([t.real, t.imag, math.log10(max(abs(s), 1e-12)), np.angle(s)])

for (n, p, hr, hp, t, r) in cases:
    if n >= 12:
        continue
    Uh = U[p, :, hr]
    Tp = sms.nine_batch(Uh, hp[None], T9, SIG)[0][0]
    t0 = time.time()
    g, (c, x) = sms.search(Uh, H[p], Tp, SIG, n_extra=4)
    t1 = time.time() - t0
    out = [f"n {n} |hh| {abs(hp @ hp):.1e} |t| {abs(t):.2f} search {c:.3g} ({t1:.1f}s)"]
    if c > 1e-6:
        h = sms.vec(x); y0 = to_tube(h)
        o = refine_tube(Uh, y0, Tp)
        out.append(f"tube-refine from it {o[0]:.3g}" if o else "tube fail")
        # check the planted point's tube coordinates
        yp = to_tube(hp); out.append(f"planted tube y {np.round(yp, 3)}; found y {np.round(y0, 3)}")
    print(" | ".join(out), flush=True)
