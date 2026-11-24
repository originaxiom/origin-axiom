#!/usr/bin/env python3
"""CHK-2a: the agy lane's M-theory scale chain (C21, C22, C37), checked against its standard source. Data-free: no
measured constant is used and nothing is compared with data.

    python3 -I -u chk_agy_mtheory.py

The source is Friedmann and Witten, hep-th/0211269, section 4: (4.4) G_N = kappa^2 / (8 pi V_X); (4.10)
alpha_GUT = (4 pi)^(1/3) kappa^(2/3) / V_Q; 2 kappa^2 = (2 pi)^8 M_11^-9; (3.25) V_Q = L(Q) / M_GUT^3, where
L(Q) = exp(T_omega - T_O) is a ratio of Ray-Singer torsions (for a lens space, 4 q sin^2(5 pi w / q)).

Expectations, written before the run:
  A1  Vol(4_1) from L(chi_-3, 2), from 6 Lambda(pi/3), and from SnapPy agree to 1e-25.                     95 %
  A2  Friedmann-Witten give (M_11 / M_GUT)^3 = (2 pi)^3 alpha^-1 / L(Q).                                      90 %
  A3  C22's coefficient 4 pi^3 is half of A2's 8 pi^3.                                                       85 %
  A4  C37's formula is A2's with L(Q) = 8 Vol(m004) and alpha^-1 = 40.                                       85 %
  A5  2 kappa^2 T_M2^3 = (2 pi)^2 gives T_M2 = M_11^3 / (2 pi)^2, and C37's 16 pi G_4 = (2 pi)^2 / (T^3 V) is (4.4). 90 %
  A6  S = 8 pi^2 Q / g^2 with g^2 = 4 pi / 40 gives 48 pi / 5 at Q = 3/25, 10 pi at 1/8, 16 pi / 5 at 1/25.     95 %
  A7  Every cyclic cover of m004 of degree 8 or 40 has at least one cusp and b_1 >= 1.                        99 %
"""
import mpmath as mp
import sympy as sp

mp.mp.dps = 40
out = {}

# A1: the volume of the figure-eight knot complement, three ways.
L2 = (mp.psi(1, mp.mpf(1) / 3) - mp.psi(1, mp.mpf(2) / 3)) / 9          # L(chi_-3, 2)
v_l = 3 * mp.sqrt(3) / 2 * L2
v_lob = 6 * (mp.clsin(2, 2 * mp.pi / 3) / 2)                               # Lambda(x) = Cl_2(2x) / 2
try:
    import snappy
    v_snap = mp.mpf(str(snappy.ManifoldHP("m004").volume()))
except Exception as exc:  # noqa: BLE001
    v_snap = None
    print("SnapPy unavailable:", exc)
print("A1  Vol(4_1): L-function %s, Lobachevsky %s, SnapPy %s" % (mp.nstr(v_l, 30), mp.nstr(v_lob, 30),
                                                                    mp.nstr(v_snap, 30) if v_snap else None))
a1 = abs(v_l - v_lob) < mp.mpf("1e-25") and (v_snap is None or abs(v_l - v_snap) < mp.mpf("1e-25"))
print("    holds:", a1, "| |L - Lob| = %s" % mp.nstr(abs(v_l - v_lob), 3),
      "| |L - SnapPy| = %s" % (mp.nstr(abs(v_l - v_snap), 3) if v_snap else "n/a"))

# A2: Friedmann-Witten's coefficient, symbolically.
al, M, VQ, L, MG = sp.symbols("alpha M_11 V_Q L M_GUT", positive=True)
kap2 = (2 * sp.pi) ** 8 / (2 * M ** 9)
eq = sp.Eq(al, (4 * sp.pi) ** sp.Rational(1, 3) * kap2 ** sp.Rational(1, 3) / VQ)
VQ_sol = sp.solve(eq, VQ)[0]
ratio3 = sp.simplify((M / MG) ** 3 * (VQ_sol / (L / MG ** 3)) / (M / MG) ** 3)   # = V_Q(alpha) M_GUT^3 / L
# (M_11 / M_GUT)^3 such that V_Q(alpha, M_11) = L / M_GUT^3:
x = sp.symbols("x", positive=True)  # x = (M_11 / M_GUT)^3
sol = sp.solve(sp.Eq(VQ_sol.subs(M, (x ** sp.Rational(1, 3)) * MG), L / MG ** 3), x)[0]
coef = sp.simplify(sol * al * L)
print("A2  (M_11 / M_GUT)^3 * alpha * L(Q) =", coef, "| equals (2 pi)^3:", sp.simplify(coef - (2 * sp.pi) ** 3) == 0)

# A3, A4: the agy lane's two versions.
ainv = 40
c22 = (4 * ainv * mp.pi ** 3 / (40 * v_l)) ** (mp.mpf(1) / 3)
fw_at_c22_choice = ((2 * mp.pi) ** 3 * ainv / (40 * v_l)) ** (mp.mpf(1) / 3)
c37 = (40 * (2 * mp.pi) ** 3 / (8 * v_l)) ** (mp.mpf(1) / 3)
print("A3  C22's coefficient / FW's = %s (C22: 4 pi^3; FW: 8 pi^3)" % mp.nstr(4 * mp.pi ** 3 / (2 * mp.pi) ** 3, 6))
print("    M_11/M_GUT: C22 (L = 40 Vol, 4 pi^3) %s; FW with C22's L %s; C37 (L = 8 Vol, (2 pi)^3) %s"
      % (mp.nstr(c22, 8), mp.nstr(fw_at_c22_choice, 8), mp.nstr(c37, 8)))
print("    C37 / C22 = %s" % mp.nstr(c37 / c22, 8))
print("A4  C37 = FW with L = 8 Vol(m004), alpha^-1 = 40:",
      abs(c37 - ((2 * mp.pi) ** 3 * ainv / (8 * v_l)) ** (mp.mpf(1) / 3)) < mp.mpf("1e-35"))

# A5: the membrane tension and Newton's constant.
T = sp.symbols("T", positive=True)
Tsol = sp.solve(sp.Eq(2 * kap2 * T ** 3, (2 * sp.pi) ** 2), T)[0]
print("A5  T_M2 =", sp.simplify(Tsol), "| equals M^3/(2 pi)^2:", sp.simplify(Tsol - M ** 3 / (2 * sp.pi) ** 2) == 0)
V = sp.symbols("V", positive=True)
G_c37 = (2 * sp.pi) ** 2 / (16 * sp.pi * Tsol ** 3 * V)
G_fw = kap2 / (8 * sp.pi * V)
print("    C37's G_4 equals FW (4.4):", sp.simplify(G_c37 - G_fw) == 0)
# The two transverse benchmarks of C37: (M_Pl^ISO / M_Pl^SD)^2 = (M_11 / M_GUT)^4.
print("    C37's benchmarks: (M_Pl^ISO / M_Pl^SD)^2 = (M_11/M_GUT)^4 = %s, so M_Pl differs by a factor %s"
      % (mp.nstr(c37 ** 4, 6), mp.nstr(c37 ** 2, 6)))

# A6: the toron actions of C21.
g2 = 4 * mp.pi / 40
for q, name in ((mp.mpf(3) / 25, "S_A"), (mp.mpf(1) / 8, "S_B"), (mp.mpf(1) / 25, "S_nu")):
    s = 8 * mp.pi ** 2 * q / g2
    print("A6  %s = 8 pi^2 Q / g^2 = %s = %s pi" % (name, mp.nstr(s, 12), mp.nstr(s / mp.pi, 12)))
print("    e^(48 pi / 5) is then read as M_GUT / v_EW (C22's docstring). That reading is a dictionary entry.")

# A7: cusps and first Betti numbers of the covers.
try:
    import snappy
    M0 = snappy.Manifold("m004")
    for n in (8, 40):
        covs = M0.covers(n, cover_type="cyclic")
        info = [(C.num_cusps(), C.homology().betti_number()) for C in covs]
        print("A7  cyclic covers of degree %d: %d; (cusps, b_1) = %s; all b_1 >= 1: %s"
              % (n, len(covs), sorted(set(info)), all(b >= 1 and c >= 1 for c, b in info)))
    for n in (2, 3, 4, 5, 6, 7, 8):
        covs = M0.covers(n)
        bs = [C.homology().betti_number() for C in covs]
        print("    all covers of degree %d: %d; least b_1 %d; least cusps %d"
              % (n, len(covs), min(bs), min(C.num_cusps() for C in covs)))
except Exception as exc:  # noqa: BLE001
    print("A7 not run:", exc)
print("done")
