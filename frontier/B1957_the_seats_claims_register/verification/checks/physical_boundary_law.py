"""B1957: the physical lane's package 'relative register boundary law' (2026-11-15; PROOF.md and
SAME_ACTION_REGISTER_FUNCTIONAL.md), rebuilt by main.  Data-free.  Nothing of the lane's is run (its own checker's
sealed output is read as text and two of its figures are recomputed here from the formulas).
 W1  the figure-eight exterior (SnapPy): H_1 = Z; the longitude is null-homologous and the meridian generates, so the
     restriction H^1(X) -> H^1(boundary) is k -> (k, 0) and its cokernel, which is H^2(X, boundary), is Z.
 W2  the reduced energy: for B = circulation and Phi = 2 pi n, E = (r B^2 + p (B - Phi)^2)/2 is minimal at
     B* = p Phi/(r + p) with E_n = r p Phi^2 / (2 (r + p)) and second derivative r + p; the screened flux p n/(r + p)
     and the relative number n (the proof's (5) and (6)).
 W3  the same from the field equations themselves, on a flat disc with the boundary phase: the Maxwell equation, the
     Robin condition and the phase equation solved directly give the same circulation and energy (so the reduction's
     sign and coefficients are those of the action (2)); and the inequality (4) on trial fields that are not uniform.
 W4  the radial control on a solid torus: a(r) = B0 r^2/R^2, the energy and its minimum (the proof's (7)).
 W5  the two sewing problems: fixed flux (b* = Phi A_T/(A_C + A_T), equal curvature Phi/A on both sides, energy
     c_H Phi^2/(2 G A) for every cut) and the seam source ((8): a unique minimum that moves with the cut); and that
     the two reduced forms have the same shape and different total flux.
 W6  a rank-three bundle on a curve: chi(V(m p)) - chi(V) = 3 m (Riemann-Roch).
 W7  two figures of the lane's sealed run, from the formulas: the energy coefficient 77/380 needs r and p it does not
     print; what can be recomputed is its cut table (areas 1/2 + 5/2, 1 + 2, 5/2 + 1/2: circulations 5/2, 2, 1/2 and one
     energy 7/5), which fixes c_H Phi^2/G = 42/5."""
import functools
from fractions import Fraction as Fr
import sympy as sp
import numpy as np
print = functools.partial(print, flush=True)

if __name__ == "__main__":
    try:
        import warnings
        with warnings.catch_warnings():
            warnings.simplefilter("ignore"); import snappy
        M = snappy.Manifold("4_1"); G = M.fundamental_group(); mer, lon = G.peripheral_curves()[0]; gens = G.generators(); rels = G.relators()
        ab = lambda w: [sum((1 if ch == g else -1 if ch == g.upper() else 0) for ch in w) for g in gens]
        A = sp.Matrix([ab(r) for r in rels]); ker = A.nullspace()                                                    # H^1 = functionals vanishing on the relators
        f = ker[0] / sp.gcd(list(ker[0])); val = lambda w: sum(a * b for a, b in zip(f, ab(w)))
        print("W1: SnapPy's 4_1: H_1 = %s; H^1 has rank %d; its generator takes the value %s on the meridian and %s on the longitude; so restriction is k -> (k, 0) and Z^2/<(1,0)> = Z" % (M.homology(), len(ker), abs(val(mer)), val(lon)))
    except ImportError:
        print("W1: SnapPy not available; not checked here")
    r, p, B, n, Phi = sp.symbols("r p B n Phi", positive=True); E = (r * B ** 2 + p * (B - Phi) ** 2) / 2; Bs = sp.solve(sp.diff(E, B), B)[0]
    print("W2: B* = %s; E at B* = %s; second derivative %s; B* - Phi = %s; flux over 2 pi at Phi = 2 pi n: %s; relative number (flux - (B* - Phi))/(2 pi) = %s" % (
        sp.simplify(Bs), sp.factor(sp.simplify(E.subs(B, Bs))), sp.diff(E, B, 2), sp.simplify(Bs - Phi), sp.simplify(Bs.subs(Phi, 2 * sp.pi * n) / (2 * sp.pi)), sp.simplify((Bs - (Bs - Phi)).subs(Phi, 2 * sp.pi * n) / (2 * sp.pi))))
    # W3: the disc of radius R: A = a(rho) d theta, phi = n theta; action (c_H/2G) int F ^ *F + (kappa/2) oint eta ^ * eta
    R, cH, Gc, kap, rho, f0 = sp.symbols("R c_H G kappa rho f_0", positive=True)
    a = f0 * rho ** 2 / 2                                                 # d * F = 0 with a regular at 0: the curvature density f = a'/rho is constant
    etas = (a.subs(rho, R) - n) / R                                       # eta = (a(R) - n) d theta, in arclength s = R theta
    robin = sp.Eq((cH / Gc) * f0 + kap * etas, 0); f0s = sp.solve(robin, f0)[0]; Bdisc = 2 * sp.pi * a.subs({rho: R, f0: f0s})
    rr, pp = cH / (Gc * sp.pi * R ** 2), kap / (2 * sp.pi * R); Bred = (pp * 2 * sp.pi * n / (rr + pp)); Edisc = (cH / (2 * Gc)) * f0s ** 2 * sp.pi * R ** 2 + (kap / 2) * etas.subs(f0, f0s) ** 2 * 2 * sp.pi * R
    print("W3: on the disc, the field equations with the Robin condition (c_H/G) f + kappa eta_s = 0 give circulation %s; the reduced formula p Phi/(r + p): difference %s; the energy against r p Phi^2/(2(r + p)): difference %s; with the other sign in the Robin condition the difference is %s" % (
        sp.simplify(Bdisc), sp.simplify(Bdisc - Bred), sp.simplify(Edisc - rr * pp * (2 * sp.pi * n) ** 2 / (2 * (rr + pp))), sp.simplify(2 * sp.pi * a.subs({rho: R, f0: sp.solve(sp.Eq((cH / Gc) * f0 - kap * etas, 0), f0)[0]}) - Bred)))
    rng = np.random.default_rng(11); worst = np.inf; Rn, cn, Gn, kn, nn = 1.3, 0.7, 0.9, 1.1, 2; rn_, pn_ = cn / (Gn * np.pi * Rn ** 2), kn / (2 * np.pi * Rn)
    xs = np.linspace(0, Rn, 4001); th = np.linspace(0, 2 * np.pi, 2001)
    for _ in range(200):
        c1, c2, c3 = rng.normal(size=3); fx = 0.4 + c1 * 0.3 * np.cos(3 * xs) + c2 * 0.2 * xs                        # a non-uniform radial curvature density
        Bn = 2 * np.pi * np.trapezoid(fx * xs, xs); eta = (Bn / (2 * np.pi) - nn) / Rn + c3 * 0.3 * np.cos(th) / Rn      # eta_s with the same period and a non-constant part
        En = (cn / (2 * Gn)) * 2 * np.pi * np.trapezoid(fx ** 2 * xs, xs) + (kn / 2) * np.trapezoid(eta ** 2, th) * Rn
        worst = min(worst, En - (rn_ * Bn ** 2 + pn_ * (Bn - 2 * np.pi * nn) ** 2) / 2)
    print("W3: the inequality (4) on 200 trial fields that are not uniform: the least value of E minus the bound is %.3e (never negative)" % worst)
    # W4: the solid torus
    Ls, B0 = sp.symbols("L B_0", positive=True); af = sp.Function("a"); ode = sp.dsolve(sp.Eq(sp.diff(sp.diff(af(rho), rho) / rho, rho), 0), af(rho)).rhs
    ar = B0 * rho ** 2 / R ** 2; bulk = sp.integrate((1 / (2 * Gc)) * (sp.diff(ar, rho) / rho) ** 2 * rho, (rho, 0, R)) * 2 * sp.pi * Ls; bdry = (kap / 2) * ((B0 - n) / R) ** 2 * R * 2 * sp.pi * Ls
    Et = bulk + bdry; B0s = sp.solve(sp.diff(Et, B0), B0)[0]
    print("W4: the Maxwell equation's general solution %s (regular at 0: a = B_0 rho^2/R^2); bulk energy %s; boundary energy %s; B_0* = %s; E_n = %s; the lane's (7): differences %s and %s" % (
        ode, sp.simplify(bulk), sp.simplify(bdry), sp.simplify(B0s), sp.factor(sp.simplify(Et.subs(B0, B0s))), sp.simplify(B0s - kap * Gc * R * n / (2 + kap * Gc * R)), sp.simplify(Et.subs(B0, B0s) - 2 * sp.pi * Ls * kap * n ** 2 / (R * (2 + kap * Gc * R)))))
    # W5: sewing
    AC, AT, b = sp.symbols("A_C A_T b", positive=True); Eg = (cH / (2 * Gc)) * ((Phi - b) ** 2 / AC + b ** 2 / AT); bs = sp.solve(sp.diff(Eg, b), b)[0]
    print("W5: fixed flux: b* = %s; the curvature on the core %s and on the tail %s; the energy %s (the cut enters only through A_C + A_T)" % (sp.simplify(bs), sp.simplify((Phi - bs) / AC), sp.simplify(bs / AT), sp.factor(sp.simplify(Eg.subs(b, bs)))))
    rC, rT = cH / (Gc * AC), cH / (Gc * AT); Es = ((rC + rT) * b ** 2 + p * (b - 2 * sp.pi * n) ** 2) / 2; bss = sp.solve(sp.diff(Es, b), b)[0]
    print("W5: the seam source (8): b* = %s, which depends on where the cut is (its derivative in A_C at fixed total area is not zero: %s); its added curvature on the two sides is -b and +b, total 0, against Phi for the fixed-flux problem" % (
        sp.simplify(bss), sp.simplify(sp.diff(bss.subs(AT, sp.Symbol("A") - AC), AC)) != 0))
    print("W5: the retained transition's energy at Phi = 2 pi n: %s (the lane: 2 pi^2 c_H n^2/(G A))" % sp.factor(sp.simplify(Eg.subs(b, bs).subs(Phi, 2 * sp.pi * n))))
    # W6
    rk, dg, g, m = sp.symbols("rk deg g m"); chi = lambda d: d + rk * (1 - g)
    print("W6: Riemann-Roch: chi(V(m p)) - chi(V) = %s; at rank 3: %s" % (sp.simplify(chi(dg + rk * m) - chi(dg)), sp.simplify(chi(dg + rk * m) - chi(dg)).subs(rk, 3)))
    # W7: the lane's sealed cut table
    K = Fr(42, 5)                                                         # c_H Phi^2 / G, fixed by one printed energy 7/5 = K/(2 A) at A = 3
    for ac, at, circ in ((Fr(1, 2), Fr(5, 2), Fr(5, 2)), (Fr(1), Fr(2), Fr(2)), (Fr(5, 2), Fr(1, 2), Fr(1, 2))):
        print("W7: cut %s + %s: energy K/(2 A) = %s (the run: 7/5); circulation over Phi = A_T/A = %s, so the run's %s is that times Phi = 3" % (ac, at, K / (2 * (ac + at)), at / (ac + at), circ))
