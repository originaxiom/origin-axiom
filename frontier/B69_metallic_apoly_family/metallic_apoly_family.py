"""B69 -- the metallic family of trace-relation (A-polynomial) curves F_m(x, kappa), m=1..4,
with the CUSP-TORSION LAW: the ideal points (cusps, poles of kappa) sit at the elliptic torsion
values x = 2 cos(pi/k).  Extends B67 (figure-eight, m=1) to the family.

This re-derives and verifies the "breakthrough chat" handoff result (apoly_family.py / cusp_verify.py)
INDEPENDENTLY, with two corrections from the script audit:
  (1) the handoff's "geometric points (kappa=2)" used the WRONG sign -- the complete hyperbolic
      structure is kappa = tr[a,b] = -2 (not +2), as established in V30 (kappa=+2 is the identity rep
      x=2 + torsion points). Fixed here.
  (2) F_m from the raw elimination carries spurious branches (x, x+1, K-x^2+2); the MAIN component is
      taken (matching the handoff's cusp_verify hand-extraction).

CROSS-CHECK to committed work: the m=2 main component kappa(x)=(x^4-6x^2+12)/(x^2-2) equals the
verified V33 relation kappa=P^2-6 with P^2=tr(t)^2=x^4/(x^2-2):  x^4/(x^2-2)-6=(x^4-6x^2+12)/(x^2-2). OK

Labels: cusp-torsion law = computer-assisted, VERIFIED m=1..4; m=5,6 predicted {3,5,7}/{4,6,8} but
NOT computationally confirmed (elimination too slow -- same wall the chat hit); NOVELTY NOT ESTABLISHED
(ideal points of character varieties at torsion values is mathematically natural -- needs a literature
check vs twist-knot A-polynomials, Hoste-Shanahan, before any novelty claim). m=1 only is PROVED (B67).
"""
import sympy as sp

x, y, z, K = sp.symbols("x y z K")

# main components F_m(x, kappa) (spurious branches removed), from the verified elimination:
Fmain = {
    1: -K * (x - 1)**2 + (x**4 - 3*x**3 + x**2 + 4*x - 2),
    2: -K * (x**2 - 2) + (x**4 - 6*x**2 + 12),
    4: -K * (x**6 - 7*x**4 + 16*x**2 - 12) + (x**8 - 9*x**6 + 27*x**4 - 24*x**2 - 8),
}
cusp3 = (x - 1)**2 * (x**2 - x - 1)        # m=3 is degree-2-in-K (irrational double cover)

tor = {k: sp.nsimplify(2 * sp.cos(sp.pi / k)) for k in range(3, 10)}


def idk(r):
    for k, v in tor.items():
        if sp.simplify(sp.nsimplify(r) - v) == 0 or sp.simplify(sp.nsimplify(r) + v) == 0:
            return k
    return None


print("B69 -- metallic A-poly family F_m(x,kappa) + cusp-torsion law\n")
for m in (1, 2, 4):
    F = sp.Poly(sp.expand(Fmain[m]), K)
    cusp = sp.factor(F.all_coeffs()[0])     # leading-K coeff = cusp polynomial (poles of kappa)
    roots = [r for r in sp.solve(sp.Eq(cusp, 0), x) if r.is_real]
    tags = sorted((float(r), idk(r)) for r in roots)
    ks = sorted({k for _, k in tags if k})
    print(f"m={m}: cusp poly = {cusp}")
    print(f"      cusps at x=2cos(pi/k), k-set = {ks}  (real roots: "
          + ", ".join(f"{rr:+.4f}={'2cos(pi/'+str(kk)+')' if kk else '?(conjugate)'}" for rr, kk in tags) + ")")
print(f"m=3: cusp poly = {sp.factor(cusp3)}  (degree-2 curve)")
r3 = sorted((float(r), idk(r)) for r in sp.solve(sp.Eq(cusp3, 0), x) if r.is_real)
print(f"      cusps: " + ", ".join(f"{rr:+.4f}={'2cos(pi/'+str(kk)+')' if kk else '?(conjugate -1/phi)'}" for rr, kk in r3))

print("\nCUSP-TORSION LAW (VERIFIED m=1,2,3,4): cusps of F_m at x=2cos(pi/k),")
print("  k in {3,...,m+2}, k = m (mod 2).  m=1->{3}, m=2->{4}, m=3->{3,5}, m=4->{4,6}.")
print("  (m=3,5,... also carry algebraic CONJUGATE roots e.g. -1/phi, not of the form 2cos(pi/k).)")

print("\nCROSS-CHECK m=2 vs committed V33:")
kx = (x**4 - 6*x**2 + 12) / (x**2 - 2)          # handoff kappa(x)
v33 = x**4 / (x**2 - 2) - 6                      # kappa = P^2 - 6, P^2 = tr(t)^2 = x^4/(x^2-2)
print(f"  kappa(x) handoff == (P^2-6) [V33]:  {sp.simplify(kx - v33) == 0}")

print("\nGEOMETRIC POINTS -- corrected sign (complete structure is kappa=-2, NOT the handoff's +2):")
for m in (1, 2):
    F = Fmain[m]
    print(f"  m={m}: kappa=-2 -> x = {sp.solve(F.subs(K, -2), x)}")
print("  (kappa=+2, the handoff value, returns the identity rep x=2 + torsion points -- NOT geometric.)")

print("\nDISPOSITION: cusp law computer-assisted VERIFIED m=1..4 (m=1 PROVED via B67); m=5,6 PREDICTED")
print("  {3,5,7}/{4,6,8} but elimination too slow to confirm this pass; NOVELTY NOT ESTABLISHED")
print("  (needs twist-knot / Hoste-Shanahan literature check -- ideal-points-at-torsion is natural).")
