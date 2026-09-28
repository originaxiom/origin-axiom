#!/usr/bin/env python3
"""B1395 -- the free cusp is charge-blind at finite energy: the cusp algebra, exact (sympy).

In the cusp (x, y, h), g = (dx^2 + dy^2 + dh^2)/h^2, dvol = dx dy dh / h^3, coordinate torus of area A.
  (a) a Higgs class alive on the torus (sealed cusp), omega = a dx + b dy: |omega|^2 = h^2 (a^2 + b^2); its L^2 norm up to height H
      is A (a^2 + b^2) log(H/h0) -- divergent, so a sealed Higgs class is not a normalizable (dynamical) 4d modulus;
  (b) a free cusp: omega = d(f), f = c h K_1(2 pi |k| h) e^{2 pi i k.x} (B1387's modes): the L^2 norm converges (exponential decay);
  (c) a gauge flux through the torus, F = phi dx^dy (flux A*phi, the same through every torus since dF = 0): |F|^2 = phi^2 h^4 and
      its energy up to height H is A phi^2 (H^2 - h0^2)/2 -- divergent quadratically, so no finite-energy field carries flux
      through a hyperbolic cusp;
  (d) a boundary condition uniform over the torus contributes -chi(T^2) = 0, whichever sector is relative and whichever absolute;
      the two charge-odd integers a torus end can carry are chi of a sign partition and the degree of a line bundle (Riemann-Roch
      on T^2: index = degree)."""
import sympy as sp

h, h0, H, A = sp.symbols("h h0 H A", positive=True)
a, b, phi, c = sp.symbols("a b phi c", real=True)
x, y = sp.symbols("x y", real=True)


def sealed_higgs_norm():
    norm2 = h ** 2 * (a ** 2 + b ** 2)              # |a dx + b dy|^2 with g^{xx} = g^{yy} = h^2
    integral = sp.integrate(A * norm2 / h ** 3, (h, h0, H))
    return sp.simplify(norm2), sp.simplify(integral), sp.limit(integral.subs({a: 1, b: 0, A: 1, h0: 1}), H, sp.oo)


def free_mode_norm(k=1):
    """|d(h K_1(2 pi k h) cos(2 pi k x))|^2 averaged over the torus (cos^2 and sin^2 average to 1/2) and integrated against
    dvol = dh/h^3 on [1, oo): finite; the averaged density times e^{2 pi k h} tends to 0 (exponential decay)"""
    import mpmath as mp
    mp.mp.dps = 30
    kk = 2 * mp.pi * k
    g = lambda t: t * mp.besselk(1, kk * t)
    dg = lambda t: mp.diff(g, t)
    dens = lambda t: t ** 2 / 2 * ((kk * g(t)) ** 2 + dg(t) ** 2)          # the torus average of |df|^2
    val = mp.quad(lambda t: dens(t) / t ** 3, [1, 2, 5, 10, mp.inf])
    tail = [dens(t) / t ** 3 * mp.e ** (kk * t) for t in (10, 20, 40)]
    return val, tail


def flux_energy():
    norm2 = phi ** 2 * h ** 4                         # |phi dx^dy|^2 with g^{xx} g^{yy} = h^4
    integral = sp.integrate(A * norm2 / h ** 3, (h, h0, H))
    return sp.simplify(norm2), sp.factor(integral), sp.limit(integral.subs({phi: 1, A: 1, h0: 1}), H, sp.oo)


def uniform_torus_condition():
    """chi(T^2) = 0: a condition uniform over a cusp torus (relative or absolute, per sector) adds -chi(T^2) = 0; a sign partition
    adds -chi(d+) (B1351 (ii)); a line bundle of degree n on T^2 has index n (Riemann-Roch, genus 1: n + 1 - g)"""
    genus = 1
    chi_T2 = 2 - 2 * genus
    rr_index = lambda n: n + 1 - genus
    return chi_T2, [rr_index(n) for n in (-2, -1, 0, 1, 2, 3)]


def mp_str(x):
    import mpmath as mp
    return mp.nstr(x, 8)


if __name__ == "__main__":
    n2, I, lim = sealed_higgs_norm()
    print("(a) sealed Higgs class: |omega|^2 =", n2, "; L^2 norm to height H:", I, "; H -> oo:", lim)
    val, tail = free_mode_norm()
    print("(b) free cusp, one mode (k = 1): L^2 norm on [1, oo) =", mp_str(val), "; the density times e^{2 pi h} at h = 10, 20, 40:",
          [mp_str(t) for t in tail])
    n2, I, lim = flux_energy()
    print("(c) gauge flux through the torus: |F|^2 =", n2, "; energy to height H:", I, "; H -> oo:", lim)
    chi, rr = uniform_torus_condition()
    print("(d) chi(T^2) =", chi, "; Riemann-Roch index on T^2 for degrees -2..3:", rr)
