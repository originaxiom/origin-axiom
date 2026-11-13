"""Test the SM seat's step-3 calibration statement against main's channel norm, directly:
    c_s(tau) = F_u(tau) + pi log Im tau + C,   C = -2 pi (gamma + log pi),
F_u = the constant term at s = 1 of E^(u)(tau, s) = sum over (m, n) in u + Z^2 of y^s |m tau + n|^(-2s) (pole pi/(s-1) removed).
E^(u) by its Fourier expansion in n (Poisson in the n-direction, shift u2): for each m in u1 + Z,
  sum_n |m tau + n|^(-2s) = sqrt(pi) G(s-1/2)/G(s) |m y|^(1-2s)
                          + (2 pi^s / G(s)) |m y|^(1/2-s) sum_{r != 0} |r|^(s-1/2) K_(s-1/2)(2 pi |r m| y) e(r (m x + u2)) [sign as below]
and the m-sum of the first term is a pair of Hurwitz zetas. F_u is taken as (E(1+d) + E(1-d))/2 at small d (the pole is
odd in d). Main's code (mpmath); nothing of the seat's is read or run; u is tried at the placements c - (1/2, 1/2) and
its rotation."""
import mpmath as mp
import step3_norm as S
mp.mp.dps = 20


def E_shift(u1, u2, tau, s, R=30, Mk=40):
    x, y = mp.re(tau), mp.im(tau)
    a = mp.mpf(u1) % 1
    # first term: sum over m in u1 + Z of |m|^(1-2s), m = a + k (k >= 0) and m = -(1 - a) - k
    h = (mp.zeta(2 * s - 1, a) if a != 0 else mp.zeta(2 * s - 1)) + mp.zeta(2 * s - 1, 1 - a) if a != 0 else 2 * mp.zeta(2 * s - 1)
    first = mp.sqrt(mp.pi) * mp.gamma(s - mp.mpf(1) / 2) / mp.gamma(s) * y ** (1 - s) * h
    # the m = 0 row exists only when u1 is an integer: sum over n in u2 + Z of |n|^(-2s)
    zero_row = 0
    if a == 0:
        b = mp.mpf(u2) % 1
        zero_row = y ** s * (mp.zeta(2 * s, b) + mp.zeta(2 * s, 1 - b)) if b != 0 else 0
    bess = 0
    for k in range(-Mk, Mk + 1):
        m = a + k
        if m == 0:
            continue
        am = abs(m)
        inner = 0
        for r in range(1, R + 1):
            ph = mp.cos(2 * mp.pi * r * (m * x + u2))         # e(r(...)) + e(-r(...)), the n-shift u2 entering as a phase
            inner += 2 * r ** (s - mp.mpf(1) / 2) * mp.besselk(s - mp.mpf(1) / 2, 2 * mp.pi * r * am * y) * ph
        bess += (2 * mp.pi ** s / mp.gamma(s)) * y ** s * (am * y) ** (mp.mpf(1) / 2 - s) * inner / y ** 0
    return first + zero_row + bess


def F(u1, u2, tau, d=mp.mpf("1e-6")):
    return (E_shift(u1, u2, tau, 1 + d) + E_shift(u1, u2, tau, 1 - d)) / 2


if __name__ == "__main__":
    t = complex(0.5, 1.1180339887498949); tau = mp.mpc(t.real, t.imag)
    C = -2 * mp.pi * (mp.euler + mp.log(mp.pi))
    for c in [(0.1, 0.0), (0.3, 0.6), (0.7, 0.2), (0.4, 0.9)]:
        N = S.norm(c, t)
        for name, (u1, u2) in (("c-1/2", (c[0] - .5, c[1] - .5)), ("rot", (c[1] - .5, -(c[0] - .5)))):
            f = F(u1, u2, tau)
            print(c, name, "N %.8f" % N, "F_u + pi log y + C %.8f" % float(f + mp.pi * mp.log(tau.imag) + C),
                  "diff %.2e" % abs(N - float(f + mp.pi * mp.log(tau.imag) + C)), flush=True)
