"""B1957: the web seat's W-C6 part 2 (its second computation of B1919 and B1921), run the other way: main's own
B1919 routines at the SEAT'S twelve points (none of them a named point).  Data-free.
 K1  B1919: N(c, tau) = F_u(tau) + pi log Im tau - 2 pi (gamma + log pi), u = c - (1/2, 1/2), at the twelve points;
     the controls (u's components swapped; pi log Im tau left out).
 K2  B1921: N(c', -1/tau) = N(c, tau) - 2 pi log|tau|, c' = (b, -a), at the twelve points; the control c' = c.
 K3  the seat's remark, which it did not claim: F at the transported point equals F at the point (it follows from the
     lattice sum by hand: S carries u + Z^2 to (u2, -u1) + Z^2); checked numerically at the twelve points.
 K4  the constant the seat's sealed run dropped: sqrt(pi) Gamma(s - 1/2)/Gamma(s) = pi (1 + (s - 1) kappa + ...),
     kappa = psi(1/2) - psi(1) = -2 log 2, so pi kappa = -2 pi log 2 = -4.355172."""
import functools, sys, pathlib, math, warnings
import mpmath as mp
print = functools.partial(print, flush=True)
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(next(HERE.parents[2].glob("B1919_*")) / "verification"))
with warnings.catch_warnings():
    warnings.simplefilter("ignore"); import seat_formula as SF, step3_norm as S
CS = [(0.13, 0.71), (0.30, 0.20), (0.77, 0.41), (0.62, 0.09)]; TS = [complex(0.21, 1.13), complex(-0.35, 0.90), complex(0.10, 1.70)]
if __name__ == "__main__":
    C = -2 * mp.pi * (mp.euler + mp.log(mp.pi)); k1 = k2 = k3 = 0; c1 = []; c1b = []; c2 = []
    Fm = lambda u1, u2, t: (SF.E_shift(u1, u2, t, 1 + mp.mpf("1e-6"), R=80, Mk=40) + SF.E_shift(u1, u2, t, 1 - mp.mpf("1e-6"), R=80, Mk=40)) / 2
    for t in TS:
        tau = mp.mpc(t.real, t.imag)
        for c in CS:
            n = S.norm(c, t); u = (c[0] - .5, c[1] - .5); f = Fm(u[0], u[1], tau); r = float(f + mp.pi * mp.log(tau.imag) + C)
            k1 = max(k1, abs(n - r)); c1.append(abs(n - float(Fm(u[1], u[0], tau) + mp.pi * mp.log(tau.imag) + C))); c1b.append(abs(n - float(f + C)))
            cp = (c[1], -c[0]); ts = -1 / t; nS = S.norm(cp, ts); k2 = max(k2, abs(nS + 2 * math.pi * math.log(abs(t)) - n)); c2.append(abs(S.norm(c, ts) + 2 * math.pi * math.log(abs(t)) - n))
            fS = Fm(cp[0] - .5, cp[1] - .5, mp.mpc(ts.real, ts.imag)); k3 = max(k3, abs(float(fS - f)))
            print("tau %.2f%+.2fi c %s: N %.9f; B1919 residual %.1e; B1921 residual %.1e; F(c', -1/tau) - F(c, tau) %.1e" % (t.real, t.imag, c, n, abs(n - r), abs(nS + 2 * math.pi * math.log(abs(t)) - n), abs(float(fS - f))))
    print("K1: B1919 at the seat's twelve points: largest residual %.1e; control with u's components swapped: off by %.2f to %.2f; with pi log Im tau left out: off by %.2f to %.2f" % (k1, min(c1), max(c1), min(c1b), max(c1b)))
    print("K2: B1921 at the twelve points: largest residual %.1e; the control c' = c: off by %.2f to %.2f" % (k2, min(c2), max(c2)))
    print("K3: F at the transported point minus F at the point: largest %.1e" % k3)
    mp.mp.dps = 30; kap = mp.digamma(mp.mpf(1) / 2) - mp.digamma(1); h = mp.mpf("1e-8"); num = (mp.sqrt(mp.pi) * mp.gamma(mp.mpf(1) / 2 + h) / mp.gamma(1 + h) / mp.pi - 1) / h
    print("K4: kappa = psi(1/2) - psi(1) = %s = -2 log 2: %s; the factor's slope at s = 1 numerically: %s; pi kappa = %s" % (mp.nstr(kap, 12), abs(kap + 2 * mp.log(2)) < mp.mpf("1e-25"), mp.nstr(num, 10), mp.nstr(mp.pi * kap, 8)))
