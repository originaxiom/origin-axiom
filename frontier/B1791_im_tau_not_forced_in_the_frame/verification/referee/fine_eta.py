"""The Higgs alone, exactly (mpmath): |dR|(tau) from B1691's q-series (te.B[1], te.ev, as B1726's compute()), |eta| by its
product, and the Petersson norms N_m(tau) = y^((3+m)/4) |eta|^m |dR| (modular-invariant in modulus for every m).
m = 6 is the rho' = rho_R (x) chi_i dressing (B1691: rho' sections are eta^6 times rho_R's, ratios unchanged).
Also the dressed matter triplet eta^6 R (W72's mode, weight 5/2) and eta^6 d2R.  Locates the maximum in Im tau at fixed Re tau
by golden-section search."""
import sys, io, contextlib, importlib.util, pathlib, math
import mpmath as mp
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
P = ROOT / "frontier/B1691_the_exponents_at_the_two_fixed_points/verification"; sys.path.insert(0, str(P))
spec = importlib.util.spec_from_file_location("te", P / "the_exponents.py"); te = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(te)
mp.mp.dps = 30


def eta(t):
    q = mp.exp(2j * mp.pi * t); p = mp.mpf(1)
    for n in range(1, 400):
        p *= (1 - q ** n)
        if abs(q) ** n < mp.mpf(10) ** -35: break
    return mp.exp(2j * mp.pi * t / 24) * p


def vnorm(vec, t): return mp.sqrt(sum(abs(te.ev(c, t)) ** 2 for c in vec))


def N(gen, k, m, re, y):
    t = mp.mpc(re, y); return y ** ((k + m / 2) / 2) * abs(eta(t)) ** m * vnorm(te.B[gen], t)


def argmax(f, a, b, it=40):
    g = (math.sqrt(5) - 1) / 2; c, d = b - g * (b - a), a + g * (b - a); fc, fd = f(c), f(d)
    for _ in range(it):
        if fc > fd: b, d, fd = d, c, fc; c = b - g * (b - a); fc = f(c)
        else: a, c, fc = c, d, fd; d = a + g * (b - a); fd = f(d)
    return (a + b) / 2


# weights in rho_R: R -1/2, dR 3/2, d2R 7/2
for gen, k, lab in ((0, -0.5, "R"), (1, 1.5, "dR"), (2, 3.5, "d2R")):
    for m in (6,):
        for re in (0.0, 0.1, 0.25, 0.3145, 0.5):
            y = argmax(lambda yy: float(N(gen, k, m, re, yy)), 0.8, 9.0)
            print("eta^%d %-3s (weight %.1f) Re tau %.4f: Petersson-norm maximum at Im tau = %.4f   [leading order 2k'/pi = %.4f]"
                  % (m, lab, k + m / 2, re, y, 2 * (k + m / 2) / math.pi), flush=True)
# the m-family for dR at Re tau 0.3145 (P-373's optimum's Re tau)
for m in (4, 5, 6, 7, 8, 9, 12):
    y = argmax(lambda yy: float(N(1, 1.5, m, 0.3145, yy)), 0.8, 12.0)
    print("y^((3+m)/4)|eta|^m|dR|, m = %2d: max at Im tau = %.4f (leading 3(3+m)/(pi(m-3)) = %.4f)" % (m, y, 3 * (3 + m) / (math.pi * (m - 3))), flush=True)
print("fine_eta exit 0")
