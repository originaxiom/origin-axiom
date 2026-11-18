"""B1957, for register row P-107 (the audit seat's scope of the SM seat's W57, 2026-10-13; data-free).

W57's rule said the hyperbolic measure is the only measure the moves keep.  The audit seat's counterexample:
    d mu_eps = (1 + eps/(1 + F)) dx dy / y^2,   F = sum over the three even theta constants of |theta_p / eta|^4,  eps > 0.
Main's own check, with mpmath's theta functions (nothing of the seat's is run):
 M1  F is invariant under tau -> tau + 1 and tau -> -1/tau (the three terms are permuted), at random points, 40 digits.
 M2  F is not constant: F(i) = 8 and F(omega) = 7.5595...; F is positive and tends to infinity at the cusp, so the factor
     1 + eps/(1 + F) lies strictly between 1 and 1 + eps.
 M3  the two normalised measures differ: the mean of 1/(1 + F) over the fundamental domain against its value at i, and the
     probability of the region Im tau > 2 under each (eps = 1)."""
import functools
import mpmath as mp
print = functools.partial(print, flush=True)
mp.mp.dps = 40


def terms(t):
    q = mp.exp(1j * mp.pi * t); eta = mp.exp(2j * mp.pi * t / 24) * mp.qp(mp.exp(2j * mp.pi * t))
    return [abs(mp.jtheta(n, 0, q) / eta) ** 4 for n in (2, 3, 4)]
F = lambda t: mp.fsum(terms(t))


if __name__ == "__main__":
    pts = [mp.mpc("0.13", "1.2"), mp.mpc("-0.31", "1.7"), mp.mpc("0.21", "2.3"), mp.mpc("0.47", "0.93")]
    print("M1: |F(tau + 1) - F(tau)| and |F(-1/tau) - F(tau)| at four points: at most %s and %s; the three terms at tau and at tau + 1 as sorted lists agree to %s" % (
        mp.nstr(max(abs(F(t + 1) - F(t)) for t in pts), 3), mp.nstr(max(abs(F(-1 / t) - F(t)) for t in pts), 3), mp.nstr(max(abs(a - b) for t in pts for a, b in zip(sorted(terms(t)), sorted(terms(t + 1)))), 3)))
    om = mp.mpc(-0.5, mp.sqrt(3) / 2)
    print("M2: F(i) = %s; F(omega) = %s; F at heights 2, 4, 8: %s (it grows as |q|^(-1/6)); the least value found on a grid of the fundamental domain: %s" % (
        mp.nstr(F(mp.mpc(0, 1)), 15), mp.nstr(F(om), 15), [mp.nstr(F(mp.mpc("0.2", h)), 8) for h in (2, 4, 8)],
        mp.nstr(min(F(mp.mpc(x / 20, y)) for x in range(-10, 11) for y in [mp.sqrt(1 - (x / 20) ** 2) + k * mp.mpf("0.15") for k in range(8)]), 10)))
    mp.mp.dps = 20
    dom = lambda g, lo=None: mp.quad(lambda x: mp.quad(lambda y: g(mp.mpc(x, y)) / y ** 2, [max(mp.sqrt(1 - x * x), lo) if lo else mp.sqrt(1 - x * x), 6, mp.inf]), [-0.5, 0, 0.5])
    area = dom(lambda t: 1); w = dom(lambda t: 1 / (1 + F(t))); a2 = dom(lambda t: 1, 2); w2 = dom(lambda t: 1 / (1 + F(t)), 2)
    print("M3: the area of the fundamental domain: %s (pi/3 = %s); the mean of 1/(1 + F) over it: %s, against 1/(1 + F(i)) = %s" % (mp.nstr(area, 12), mp.nstr(mp.pi / 3, 12), mp.nstr(w / area, 10), mp.nstr(1 / (1 + F(mp.mpc(0, 1))), 10)))
    print("M3: P(Im tau > 2) under the hyperbolic measure: %s; under the measure with eps = 1: %s. Two different invariant probability measures" % (mp.nstr(a2 / area, 10), mp.nstr((a2 + w2) / (area + w), 10)))
