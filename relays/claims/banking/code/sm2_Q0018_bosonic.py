#!/usr/bin/env python3
"""sm2 (fam1-v1-unset-05): what card Q0018 defines and a banking seat can recompute: the bosonic potentials. mpmath and the
standard library. Written from the card's definitions only. The fermion potentials rest on Yukawa matrices the card does
not define, and are not computed here.

    python3 relays/claims/banking/code/sm2_Q0018_bosonic.py            # invariance, minima on Re tau = 0, E(i,3), E(omega,3)
    python3 relays/claims/banking/code/sm2_Q0018_bosonic.py --control  # E2 without -3/(pi y): the S-invariance must fail

eta by its q-product, E_2 by its Lambert series, E2_hat = E_2 - 3/(pi y); V_FILQ,n = (2y)^(-3n) |eta|^(-12n)
((n pi^2 y^2 / 3) |E2_hat|^2 - 3); E(tau, s) by direct summation of its Fourier (Chowla-Selberg) expansion.
"""
import sys
import mpmath as mp

mp.mp.dps = 40
CONTROL = "--control" in sys.argv

def eta(t):
    q = mp.exp(2j * mp.pi * t)
    return mp.exp(2j * mp.pi * t / 24) * mp.qp(q)

def E2(t):
    q = mp.exp(2j * mp.pi * t)
    return 1 - 24 * mp.nsum(lambda n: n * q ** n / (1 - q ** n), [1, mp.inf])

def E2hat(t):
    return E2(t) - (0 if CONTROL else 3 / (mp.pi * mp.im(t)))

def VFILQ(n, t):
    y = mp.im(t)
    return (2 * y) ** (-3 * n) * abs(eta(t)) ** (-12 * n) * ((n * mp.pi ** 2 * y ** 2 / 3) * abs(E2hat(t)) ** 2 - 3)

def Eis(t, s):
    """sum' y^s / |m tau + n|^(2s)"""
    x, y = mp.re(t), mp.im(t)
    c0 = 2 * mp.zeta(2 * s) * y ** s
    c1 = 2 * mp.sqrt(mp.pi) * mp.gamma(s - mp.mpf(1) / 2) * mp.zeta(2 * s - 1) / mp.gamma(s) * y ** (1 - s)
    tail = 0
    for k in range(1, 40):
        sig = sum(mp.mpf(d) ** (1 - 2 * s) for d in range(1, k + 1) if k % d == 0)
        tail += k ** (s - mp.mpf(1) / 2) * sig * mp.sqrt(y) * mp.besselk(s - mp.mpf(1) / 2, 2 * mp.pi * k * y) * mp.cos(2 * mp.pi * k * x)
    return c0 + c1 + 8 * mp.pi ** s / mp.gamma(s) * tail

pts = [mp.mpc(0.13, 1.4), mp.mpc(-0.31, 1.05), mp.mpc(0.4, 2.2)]
worst = 0
for t in pts:
    for n in (1, 2, 3):
        v = VFILQ(n, t)
        worst = max(worst, abs(VFILQ(n, t + 1) - v) / abs(v), abs(VFILQ(n, -1 / t) - v) / abs(v))
print("DECISIVE: V_FILQ,n (n = 1, 2, 3) T and S invariance, worst relative difference at three points: %s"
      % mp.nstr(worst, 3))
if CONTROL:
    ok = worst < mp.mpf("1e-25")
    print("CONTROL: with E2 for E2_hat the S-invariance %s" % ("holds" if ok else "fails, as it must"))
    print("RESULT: the control %s" % ("did not fail" if ok else "fails"))
    sys.exit(1)
mins = {}
for n in (1, 2, 3):
    f = lambda y: VFILQ(n, mp.mpc(0, y))
    ys = [1 + 0.01 * k for k in range(0, 301)]
    vals = [f(y) for y in ys]
    loc = [ys[i] for i in range(1, len(ys) - 1) if vals[i] < vals[i - 1] and vals[i] < vals[i + 1]]
    found = []
    for y0 in loc:
        y = mp.findroot(lambda y: mp.diff(f, y), y0)
        found.append((y, f(y), mp.diff(f, y, 2)))
    mins[n] = found
    for y, v, d2 in found:
        print("   V_FILQ,%d on Re tau = 0: local minimum at y = %s, V = %s, V'' = %s" % (n, mp.nstr(y, 10), mp.nstr(v, 8), mp.nstr(d2, 5)))
e_i, e_w = Eis(mp.mpc(0, 1), 3), Eis(mp.mpc(0.5, mp.sqrt(3) / 2), 3)
print("DECISIVE: E(i, 3) = %s, E(omega_+, 3) = %s, E(i, 3) - E(omega_+, 3) = %s"
      % (mp.nstr(e_i, 12), mp.nstr(e_w, 12), mp.nstr(e_i - e_w, 12)))
y3 = [y for y, v, d2 in mins[3]]
print("DECISIVE: V_FILQ,3 local minima on Re tau = 0 in [1, 4]: %s" % [mp.nstr(y, 8) for y in y3])
print("NOT COMPUTED: V_CW^(all-288), V_CW^(tr), c_B^crit, c_F^crit, y* = 3.380451106, V_xx, EWSB, Majorana: the Yukawa "
      "matrices Y_f(w; tau) of Frame C are not defined on the card")
ok = worst < mp.mpf("1e-25")
print("RESULT: the bosonic part %s; the card is not decidable as filed" % ("holds" if ok else "does not hold"))
sys.exit(0 if ok else 1)
