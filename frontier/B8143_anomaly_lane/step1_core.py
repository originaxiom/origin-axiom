"""B8143 step 1 -- reproduce B1160's core theorem EXACTLY, then solve the system WITHOUT
its normalisation.

B1160: on an SM-shaped 15-plet with state counts q:6, u:3, d:3, l:2, e:1, the four anomaly
conditions force Y to the SM direction, "unique up to scale and u<->d, zero non-SM, zero
multidimensional families".

Its parametrisation sets Y_q = 1. Anything with Y_q = 0 is invisible to that chart. This
script solves the full 5-dimensional system with no normalisation at all.
"""
import sympy as sp

Yq, Yu, Yd, Yl, Ye, t, s = sp.symbols("Yq Yu Yd Yl Ye t s")

# One SM-shaped generation, all fields as left-handed Weyl:
#   Q=(3,2)_Yq  u^c=(3bar,1)_Yu  d^c=(3bar,1)_Yd  L=(1,2)_Yl  e^c=(1,1)_Ye
A_su3 = 2 * Yq + Yu + Yd                      # [SU(3)]^2 U(1): weak multiplicity on Q
A_su2 = 3 * Yq + Yl                           # [SU(2)]^2 U(1): colour multiplicity on Q
A_grav = 6 * Yq + 3 * Yu + 3 * Yd + 2 * Yl + Ye
A_cube = 6 * Yq**3 + 3 * Yu**3 + 3 * Yd**3 + 2 * Yl**3 + Ye**3

print("A  the three LINEAR conditions")
lin = sp.solve([A_su3, A_su2, A_grav], [Yl, Ye, Yd], dict=True)[0]
print("   solved:", {str(k): sp.simplify(v) for k, v in lin.items()})
print("   B1160 states  Yl = -3Yq,  Ye = 6Yq,  Yu + Yd = -2Yq")
ok = (sp.simplify(lin[Yl] + 3 * Yq) == 0 and sp.simplify(lin[Ye] - 6 * Yq) == 0
      and sp.simplify(lin[Yd] + 2 * Yq + Yu) == 0)
print("   MATCHES B1160:", ok)

print("\nB  the cubic on that 2-plane, WITH B1160's normalisation Yq = 1, Yu = -1 + t")
cub = A_cube.subs(lin).subs({Yq: 1, Yu: -1 + t})
cub = sp.factor(sp.expand(cub))
print("   [Y]^3  =", cub)
print("   B1160 states  -18*(t-3)*(t+3) :", sp.simplify(cub - (-18 * (t - 3) * (t + 3))) == 0)
for r in sp.solve(cub, t):
    v = {Yq: 1, Yu: -1 + r}
    sol = (1, sp.simplify((-1 + r)), sp.simplify(lin[Yd].subs(v)),
           sp.simplify(lin[Yl].subs(v)), sp.simplify(lin[Ye].subs(v)))
    print("   t = %-3s ->  (Yq,Yu,Yd,Yl,Ye) = %s   /6 -> %s"
          % (r, sol, tuple(sp.nsimplify(x, rational=True) / 6 for x in sol)))

print("\nC  the SAME system with NO normalisation -- the full 5-dim solution set")
full = sp.solve([A_su3, A_su2, A_grav, A_cube], [Yq, Yu, Yd, Yl, Ye], dict=True)
print("   sympy returns %d solution branch(es):" % len(full))
for b in full:
    print("     ", {str(k): sp.simplify(v) for k, v in b.items()})

print("\nD  the branch B1160's chart cannot see:  Yq = 0")
sub0 = {Yq: 0, Yl: 0, Ye: 0, Yu: s, Yd: -s}
print("   try (Yq,Yu,Yd,Yl,Ye) = (0, s, -s, 0, 0):")
for nm, expr in (("[SU(3)]^2 Y", A_su3), ("[SU(2)]^2 Y", A_su2),
                 ("grav^2 Y", A_grav), ("[Y]^3", A_cube)):
    print("     %-12s -> %s" % (nm, sp.simplify(expr.subs(sub0))))
print("   => a ONE-PARAMETER anomaly-free family, for EVERY s. It is VECTOR-LIKE:")
print("      u^c and d^c carry opposite charge, everything else neutral.")
print("      B1160's normalisation Yq = 1 excludes it by construction.")
