"""agy digest: the modular claims of Theorem 11, audit_395b27210 finding 9 and Phases 2/9/Theorem 13's scalar comparison,
checked from first principles (sympy for the algebra, mpmath jtheta / eta at 40 digits).  Nothing imported from the agy
lane.  Data-free.

  T11b  F := th2^20 + th4^20 - th3^20 = -80 eta^12 E4   (symbolic: X^5 + Y^5 - (X+Y)^5 with X = th2^4, Y = th4^4,
        th3^4 = X + Y (Jacobi), th2 th3 th4 = 2 eta^3, E4 = (th2^8 + th3^8 + th4^8)/2; numeric at five tau)
  T11c  F(rho) = 0 (rho = e^{i pi/3}), F(iy) < 0 on the imaginary axis, the q_h-expansion -80 q_h + O(q_h^3)
  A3    |F(tau_G)| = |b_10|^2 = 0.02143382, |eta(tau_G)^6/4| = 0.00409212, ratio 5.2378 (tau_G = 1/sqrt5 + i phi^2)
  EXT   main's census directions F_a (a = 2 mod 4, B1730/cm_zero_line): v.v = th2^(2a) + th4^(2a) - th3^(2a)
        = -16 eta^12 P_n(X, Y), n = a/2; the factor (X^2 + XY + Y^2) = E4 appears exactly when n = 5 mod 6
        (and squared when n = 1 mod 6, n > 1) -- the classical Cauchy-Mirimanoff factorisation.
"""
import json, pathlib
import sympy as sp
import mpmath as mp

mp.mp.dps = 40
OUT = {}
def rec(k, v): OUT[k] = v; print(k, ":", v)

X, Y = sp.symbols("X Y")
rec("T11b X^5+Y^5-(X+Y)^5 factored", str(sp.factor(X ** 5 + Y ** 5 - (X + Y) ** 5)))

def th(n, tau): return mp.jtheta(n, 0, mp.exp(1j * mp.pi * tau))
def eta(tau):
    q = mp.exp(2j * mp.pi * tau); return mp.exp(2j * mp.pi * tau / 24) * mp.qp(q)
def E4(tau):
    q = mp.exp(2j * mp.pi * tau)
    return 1 + 240 * mp.nsum(lambda n: n ** 3 * q ** n / (1 - q ** n), [1, mp.inf])

phi = (1 + mp.sqrt(5)) / 2
pts = {"tau_G": mp.mpc(1 / mp.sqrt(5), phi ** 2), "2i": mp.mpc(0, 2), "0.31+1.45i": mp.mpc(0.31, 1.45),
       "rho": mp.exp(1j * mp.pi / 3), "-0.4+0.9i": mp.mpc(-0.4, 0.9)}
for name, t in pts.items():
    t2, t3, t4 = th(2, t), th(3, t), th(4, t)
    F = t2 ** 20 + t4 ** 20 - t3 ** 20
    rhs = -80 * eta(t) ** 12 * E4(t)
    rec("T11b %s: |F + 80 eta^12 E4|, |F|" % name, [mp.nstr(abs(F - rhs), 3), mp.nstr(abs(F), 12)])
    rec("T11b %s: Jacobi |th3^4 - th2^4 - th4^4|, |th2 th3 th4 - 2 eta^3|, |E4 - (th2^8+th3^8+th4^8)/2|" % name,
        [mp.nstr(abs(t3 ** 4 - t2 ** 4 - t4 ** 4), 3), mp.nstr(abs(t2 * t3 * t4 - 2 * eta(t) ** 3), 3),
         mp.nstr(abs(E4(t) - (t2 ** 8 + t3 ** 8 + t4 ** 8) / 2), 3)])
# T11c
rec("T11c E4(rho)", mp.nstr(abs(E4(pts["rho"])), 3))
ys = [0.6, 1.0, 1.5, 2.0, 3.0, 5.0]
rec("T11c F(iy) for y in %s (real part, imag part)" % ys,
    [(mp.nstr(mp.re(th(2, 1j * y) ** 20 + th(4, 1j * y) ** 20 - th(3, 1j * y) ** 20), 6),
      mp.nstr(mp.im(th(2, 1j * y) ** 20 + th(4, 1j * y) ** 20 - th(3, 1j * y) ** 20), 3)) for y in ys])
qh = sp.symbols("q")
# th2^20 = 2^20 q_h^5 (1 + ...) starts at q_h^5, so F to q_h^4 is th4^20 - th3^20 there (exact polynomial truncation)
t3s = 1 + 2 * qh + 2 * qh ** 4; t4s = 1 - 2 * qh + 2 * qh ** 4
Fs = sp.expand(t4s ** 20 - t3s ** 20)
Fs = sum(Fs.coeff(qh, k) * qh ** k for k in range(0, 5))
rec("T11c q_h-expansion of F to q_h^4 (th2^20 enters at q_h^5)", str(Fs))
e = sp.expand(-80 * qh * (1 - qh ** 2) ** 12 * (1 + 240 * qh ** 2))   # -80 eta^12 E4 = -80 q_h prod(1-q_h^2n)^12 (1 + 240 q_h^2 + ...)
rec("T11c -80 eta^12 E4 to q_h^4 (control)", str(sum(e.coeff(qh, k) * qh ** k for k in range(0, 5))))
# T11c': the relay calls F 'a modular form of weight 10 for SL(2, Z)'; its multiplier is eta^12's (order 2)
def Fv(t): return th(2, t) ** 20 + th(4, t) ** 20 - th(3, t) ** 20
t0 = mp.mpc(0.13, 1.21)
rec("T11c' F(tau+1)/F(tau) and F(-1/tau)/(tau^10 F(tau)) at 0.13+1.21i", [mp.nstr(Fv(t0 + 1) / Fv(t0), 12), mp.nstr(Fv(-1 / t0) / (t0 ** 10 * Fv(t0)), 12)])
# A3
tG = pts["tau_G"]
Fg = abs(th(2, tG) ** 20 + th(4, tG) ** 20 - th(3, tG) ** 20); e6 = abs(eta(tG) ** 6 / 4)
rec("A3 |F(tau_G)| = |b_10|^2", mp.nstr(Fg, 10)); rec("A3 |eta(tau_G)^6|/4", mp.nstr(e6, 10))
rec("A3 ratio |b_10|^2 / |eta^6/4|", mp.nstr(Fg / e6, 8)); rec("A3 inverse ratio", mp.nstr(e6 / Fg, 8))
rec("A3 closed form of the ratio: 320 |eta|^6 |E4| at tau_G", mp.nstr(320 * abs(eta(tG)) ** 6 * abs(E4(tG)), 8))
# EXT: every census direction F_a
facts = {}
for a in (-10, -6, -2, 6, 10, 14, 18, 22, 26):
    n = a // 2
    if n > 0:
        poly = sp.factor(X ** n + Y ** n - (X + Y) ** n)
    else:   # negative a: th^(2a) = 1/th^(2|a|); v.v = X^n + Y^n - (X+Y)^n with n < 0, a rational function
        poly = sp.factor(sp.together(X ** n + Y ** n - (X + Y) ** n))
    facts["F_%d (n=%d)" % (a, n)] = str(poly)
rec("EXT factorisation of v.v for the census's F_a in X = th2^4, Y = th4^4 (th3^4 = X + Y; XY(X+Y) = 16 eta^12)", facts)
pathlib.Path(__file__).with_suffix(".json").write_text(json.dumps(OUT, indent=1, default=str))
