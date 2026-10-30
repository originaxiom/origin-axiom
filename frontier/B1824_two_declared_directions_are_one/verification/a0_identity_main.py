"""Main's own check of the identity a0 = eta^4 F_-2 / 6 (Step A v2's side finding; the referee's exact form).
R = (-th2^2, -th4^2, i th3^2)/(th2 th3 th4) (B1730 section 1), weight -1/2; a0 = D^2 R - E4 R/48 with Serre derivatives
D_k = q d/dq - (k/12) E2 (so D R = D_{-1/2} R, D^2 R = D_{3/2} D_{-1/2} R); F_-2 = eta^5 (th2^-2, th4^-2, i th3^-2)
(B1730's F_a at a = -2, eps = i^0 = 1).  Part 1: the algebra in sympy from the theta log-derivatives and Jacobi's
identity.  Part 2: mpmath at 40 digits, a0 by NUMERICAL differentiation of R (independent of part 1's formulas), against
eta^4 F_-2 / 6 with eta from its product.  Part 3: the three log-derivative formulas themselves, numerically."""
import json, pathlib
import sympy as sp
import mpmath as mp

# ---- part 1: algebra.  A = th2^4, B = th3^4, C = th4^4, B = A + C; l2, l3, l4 = q d/dq log th_j
A, C, e = sp.symbols("A C e")
B = A + C
E4 = (A ** 2 + B ** 2 + C ** 2) / 2
l2, l3, l4 = (e + B + C) / 24, (e + A - C) / 24, (e - A - B) / 24
dA, dB, dC = 4 * A * l2, 4 * B * l3, 4 * C * l4          # q d/dq of th_j^4
res1 = {}
# each component as R_k = s_k * (th_a / (th_b th_c)); q d/dq log R_k = l_a - l_b - l_c
for name, la, lb, lc in (("R1 (th2/(th3 th4))", l2, l3, l4), ("R2 (th4/(th2 th3))", l4, l2, l3), ("R3 (th3/(th2 th4))", l3, l2, l4)):
    dlog = la - lb - lc
    D1 = sp.expand(dlog + e / 24)                          # D_{-1/2} R_k / R_k
    # D_{3/2}(R_k D1) = q d/dq(R_k D1) - (3/2)/12 e R_k D1 ; divide by R_k
    dD1 = sum(sp.diff(D1, s) * ds for s, ds in ((A, dA), (C, dC)))   # q d/dq of D1 (D1 is free of e: checked below)
    assert sp.diff(D1, e) == 0
    D2 = sp.expand(D1 * dlog + dD1 - sp.Rational(1, 8) * e * D1)
    a0_over_R = sp.factor(sp.expand(D2 - E4 / 48))
    res1[name] = dict(D_R_over_R=str(sp.factor(D1)), a0_over_R=str(a0_over_R))
    print("part 1", name, ": D R / R =", sp.factor(D1), " a0 / R =", a0_over_R)

# ---- part 2: numerics
mp.mp.dps = 40
def th(t):
    # summed in tau directly (mpmath's jtheta(2, 0, q) takes the principal q^(1/4), which is the wrong branch for |Re tau| > 1)
    q = mp.exp(1j * mp.pi * t)
    t2 = mp.nsum(lambda n: mp.exp(1j * mp.pi * t * (n + mp.mpf(1) / 2) ** 2), [-mp.inf, mp.inf])
    return (t2, mp.jtheta(3, 0, q), mp.jtheta(4, 0, q))
def eta(t):
    qq = mp.exp(2j * mp.pi * t)
    return mp.exp(2j * mp.pi * t / 24) * mp.qp(qq)          # q^{1/24} prod (1 - q^n), principal branch of q^{1/24}
def E2(t):
    qq = mp.exp(2j * mp.pi * t); return 1 - 24 * mp.nsum(lambda n: n * qq ** n / (1 - qq ** n), [1, mp.inf])
def E4f(t):
    qq = mp.exp(2j * mp.pi * t); return 1 + 240 * mp.nsum(lambda n: n ** 3 * qq ** n / (1 - qq ** n), [1, mp.inf])
def R(t, k):
    a, b, c = th(t); d = a * b * c
    return [-a * a / d, -c * c / d, 1j * b * b / d][k]
qd = lambda f, t: mp.diff(f, t) / (2j * mp.pi)               # q d/dq = (1/2 pi i) d/dtau
out2 = []
for t in (mp.mpc("0.17", "1.23"), mp.mpc("1.7", "0.9"), mp.mpc("-2.3", "1.6"), mp.mpc("0.31", "0.62")):
    row = []
    for k in range(3):
        DR = lambda s: qd(lambda u: R(u, k), s) + E2(s) / 24 * R(s, k)
        D2R = qd(DR, t) - mp.mpf(3) / 2 / 12 * E2(t) * DR(t)
        a0 = D2R - E4f(t) * R(t, k) / 48
        a, b, c = th(t); h = eta(t)
        F = [h ** 5 / a ** 2, h ** 5 / c ** 2, 1j * h ** 5 / b ** 2][k]
        row.append(a0 / (h ** 4 * F / 6))
    eta3 = eta(t) ** 3 / (th(t)[0] * th(t)[1] * th(t)[2] / 2)
    out2.append(dict(tau=str(t), ratio_minus_1=[float(abs(r - 1)) for r in row], eta3_over_half_th2th3th4=complex(eta3)))
    print("part 2 tau=%s  |a0/(eta^4 F_-2/6) - 1| = %s   eta^3/(th2 th3 th4/2) = %s" % (mp.nstr(t, 4), [mp.nstr(abs(r - 1), 3) for r in row], mp.nstr(eta3, 6)))

# ---- part 3: the log-derivative formulas used in part 1
out3 = []
for t in (mp.mpc("0.17", "1.23"), mp.mpc("-0.4", "0.95")):
    a, b, c = th(t); E = E2(t); A_, B_, C_ = a ** 4, b ** 4, c ** 4
    errs = [abs(qd(lambda u: mp.log(th(u)[j]), t) - f) for j, f in ((0, (E + B_ + C_) / 24), (1, (E + A_ - C_) / 24), (2, (E - A_ - B_) / 24))]
    jac = abs(B_ - A_ - C_)
    e4id = abs(E4f(t) - (A_ ** 2 + B_ ** 2 + C_ ** 2) / 2)
    out3.append(dict(tau=str(t), logder_errors=[float(x) for x in errs], jacobi=float(jac), E4_identity=float(e4id)))
    print("part 3 tau=%s  log-derivative errors %s  Jacobi %s  E4 = (A^2+B^2+C^2)/2: %s" % (mp.nstr(t, 4), [mp.nstr(x, 3) for x in errs], mp.nstr(jac, 3), mp.nstr(e4id, 3)))
pathlib.Path(__file__).with_suffix(".json").write_text(json.dumps(dict(part1=res1, part2=out2, part3=out3), indent=1, default=str))
