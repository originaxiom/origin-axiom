"""Two displayed formulas of the paper (P9, draft 3, Section 5) checked numerically (chat1; no data).

1. Proposition 16 (B1654): "at the cusp D/(q|rho|^2) = 8 pi^2 Im tau + 8 pi (1 - 4 ln 2) + O(Im tau q)".
   D = sum_r c_r rho_r^2 with W87's c_r = -2 pi ln((pi/2)|theta_r(0)|^2) and the paper's theta triplet
   rho = (-theta_2^2, -theta_4^2, i theta_3^2) / (2 pi eta^3); q is the nome e^{i pi tau} (the value at 4i reproduces
   the formula). Lemma 21 gives D(tau + 1) = i D(tau) while q(tau + 1) = -q(tau), so the left side cannot be real for
   all Re tau: it is evaluated at Re tau = 0, 0.3, 0.5 and 1 at Im tau = 4 and 5, with the general leading term
   e^{-i pi x/2} [8 pi^2 y + 4 pi (1 + e^{-2 pi i x}) - 32 pi ln 2] (tau = x + iy), which is the displayed one at x = 0.
2. Proposition 13 (chat1's O6, verified in B1650): the paper displays "the bilinear sum_r rho_r^2 wp(z - z_r)", with
   i <-> 1/2, j <-> tau/2, k <-> (1 + tau)/2. The record's statement is Phi^2 = -[(rho.rho) wp(z) - sum_r rho_r^2 wp(z_r)]
   dz^2, which vanishes identically. Both sums are evaluated at generic tau and z.
3. Proposition 13's Status line: "the constant term cancels because rho . rho = 0". B1650 computed wp as -(log theta_1)''
   up to an additive constant, which cancels because rho . rho = 0. With the residue-one f_r (f_r^2 = wp(z) - wp(z_r)),
   rho . rho = 0 removes the wp(z) term; the bilinear's own constant sum_r rho_r^2 wp(z_r) is checked here
   as a polynomial in theta_2^4, theta_3^4, theta_4^4 with Jacobi's identity NOT imposed (seeded random complex values).
Usage: python3 -B paper_checks.py > paper_checks_run.txt
"""
import mpmath as mp
mp.mp.dps = 40


def nome(tau): return mp.exp(1j * mp.pi * tau)
def th(r, tau, z=0): return mp.jtheta(r, z, nome(tau))
def eta(tau): return mp.exp(2j * mp.pi * tau / 24) * mp.qp(mp.exp(2j * mp.pi * tau))


def rho(tau):
    e3 = 2 * mp.pi * eta(tau) ** 3
    return [-th(2, tau) ** 2 / e3, -th(4, tau) ** 2 / e3, 1j * th(3, tau) ** 2 / e3]


def D(tau):
    c = [-2 * mp.pi * mp.log((mp.pi / 2) * abs(th(k, tau)) ** 2) for k in (2, 4, 3)]
    return sum(ci * ri ** 2 for ci, ri in zip(c, rho(tau)))


def wp(z, tau):
    """Weierstrass p for the lattice Z + tau Z: e_2 + pi^2 theta_2^2 theta_3^2 (theta_4(pi z)/theta_1(pi z))^2"""
    e2 = -(mp.pi ** 2 / 3) * (th(2, tau) ** 4 + th(3, tau) ** 4)
    return e2 + mp.pi ** 2 * th(2, tau) ** 2 * th(3, tau) ** 2 * (th(4, tau, mp.pi * z) / th(1, tau, mp.pi * z)) ** 2


print("1. Proposition 16: D/(q |rho|^2), q = e^{i pi tau}; the formula's right side 8 pi^2 Im tau + 8 pi (1 - 4 ln 2)")
for y in (4, 5):
    rhs = 8 * mp.pi ** 2 * y + 8 * mp.pi * (1 - 4 * mp.log(2))
    for x in (0, 0.3, 0.5, 1):
        tau = mp.mpc(x, y); r = rho(tau); n2 = sum(abs(v) ** 2 for v in r)
        lhs = D(tau) / (nome(tau) * n2)
        gen = mp.exp(-1j * mp.pi * x / 2) * (8 * mp.pi ** 2 * y + 4 * mp.pi * (1 + mp.exp(-2j * mp.pi * x))
                                             - 32 * mp.pi * mp.log(2))
        print(f"   tau = {x} + {y}i: D/(q|rho|^2) = {mp.nstr(lhs, 7)} (modulus {mp.nstr(abs(lhs), 7)}); right side "
              f"{mp.nstr(rhs, 7)}; |D|/|rho|^2 = {mp.nstr(abs(D(tau)) / n2, 7)}; general leading term "
              f"{mp.nstr(gen, 7)}, off by {mp.nstr(abs(lhs - gen), 2)}")
print(f"   D(tau + 1)/D(tau) at 0.2 + 1.3i: {mp.nstr(D(mp.mpc(1.2, 1.3)) / D(mp.mpc(0.2, 1.3)), 10)}")

print("2. Proposition 13: the displayed sum against the record's identity")
for tau, z in ((mp.mpc(0.13, 1.07), mp.mpc(0.21, 0.37)), (mp.mpc(-0.31, 1.4), mp.mpc(0.4, 0.15))):
    r = rho(tau); zs = [mp.mpf(1) / 2, tau / 2, (1 + tau) / 2]
    # a check of wp: the Laurent leading term and the half-period values' sum (e_1 + e_2 + e_3 = 0)
    lau = wp(mp.mpf("1e-8"), tau) * mp.mpf("1e-16")
    esum = sum(wp(zz, tau) for zz in zs)
    shown = sum(ri ** 2 * wp(z - zr, tau) for ri, zr in zip(r, zs))
    record = sum(ri ** 2 * (wp(z, tau) - wp(zr, tau)) for ri, zr in zip(r, zs))
    print(f"   tau = {mp.nstr(tau, 4)}, z = {mp.nstr(z, 4)}: z^2 wp(z) at z = 1e-8: {mp.nstr(lau, 12)}; e1 + e2 + e3 = "
          f"{mp.nstr(esum, 3)}")
    print(f"      the paper's sum_r rho_r^2 wp(z - z_r) = {mp.nstr(shown, 10)}")
    print(f"      the record's sum_r rho_r^2 (wp(z) - wp(z_r)) = {mp.nstr(record, 3)}  (rho.rho = {mp.nstr(sum(v*v for v in r), 3)})")

print("3. Proposition 13's constant: sum_r rho_r^2 wp(z_r) as a polynomial in a = theta_2^4, b = theta_3^4, c = theta_4^4")
print("   (rho_r^2 proportional to a, c, -b; wp(1/2) = pi^2 (b + c)/3, wp(tau/2) = -pi^2 (a + b)/3,")
print("   wp((1 + tau)/2) = pi^2 (a - c)/3; the overall factors dropped)")
tau = mp.mpc(0.13, 1.07); a, b, c = th(2, tau) ** 4, th(3, tau) ** 4, th(4, tau) ** 4
ev = [wp(mp.mpf(1) / 2, tau), wp(tau / 2, tau), wp((1 + tau) / 2, tau)]
print(f"   the three values against wp at tau = 0.13 + 1.07i: largest difference "
      f"{mp.nstr(max(abs(e - mp.pi ** 2 * f / 3) for e, f in zip(ev, (b + c, -(a + b), a - c))), 3)}")
mp.mp.dps = 30
import random
rng = random.Random(2026)
for k in range(3):
    a, b, c = [mp.mpc(rng.uniform(-1, 1), rng.uniform(-1, 1)) for _ in range(3)]
    print(f"   random a, b, c (a + c - b = {mp.nstr(a + c - b, 4)}): a (b + c) - c (a + b) - b (a - c) = "
          f"{mp.nstr(a * (b + c) - c * (a + b) - b * (a - c), 3)}")
print("   so the constant vanishes identically in the theta constants; rho . rho = 0 (Jacobi) is what removes wp(z)")
