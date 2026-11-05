"""B1836 § 4: mpmath's theta_2 from the nome takes the principal q^(1/4): against the defining series it is exact for
0 <= Re tau < 1 and off by a factor -i for Re tau >= 1 (P-670)."""
import mpmath as mp
mp.mp.dps = 30
def series(tau): return 2 * mp.nsum(lambda n: mp.exp(1j * mp.pi * tau * (n + mp.mpf(1) / 2) ** 2), [0, mp.inf])
for re in (0.3, 0.9, 1.3, 1.7, 2.4):
    tau = mp.mpc(re, 2.8); lib = mp.jtheta(2, 0, mp.exp(1j * mp.pi * tau)); ser = series(tau)
    print("Re tau %.1f: relative deviation %.1e ; ratio %s" % (re, float(abs(lib - ser) / abs(ser)), mp.nstr(lib / ser, 4)))
