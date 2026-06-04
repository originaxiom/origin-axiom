"""GATE 2 (Seiberg-Witten check): is m136's j=1728 curve genuinely the SW curve of N=2 SU(2),
or a single forced CM coincidence? EXPECTED NEGATIVE. Verifies tau=i (the web's claim) and frames
the honest verdict. sympy + mpmath. Standalone; no physics claim earned.
"""
import sympy as sp
import mpmath as mp
mp.mp.dps = 30
M = sp.symbols("M")


def main():
    p, q = 1 + sp.sqrt(2), sp.sqrt(2) - 1                 # branch points +-(1+sqrt2), +-(sqrt2-1)
    e = [-p, -q, q, p]
    lam = sp.simplify(((e[0] - e[2]) * (e[1] - e[3])) / ((e[0] - e[3]) * (e[1] - e[2])))
    print("m=2 spectral curve y^2 = M^4 - 6 M^2 + 1  (= m136 A-poly discriminant, Gate 0 verified)")
    print(f"  branch points: +-(1+sqrt2)=+-2.4142, +-(sqrt2-1)=+-0.4142")
    print(f"  cross-ratio lambda = {sp.nsimplify(lam)}  -> harmonic => j=1728, CM by Z[i], tau=i")

    f = lambda t: t**4 - 6 * t**2 + 1
    P, Q = float(p), float(q)
    per1 = 2 * mp.quad(lambda t: 1 / mp.sqrt(f(t)), [-Q, Q])         # cycle where y^2>0
    per2 = 2 * mp.quad(lambda t: 1 / mp.sqrt(f(t) + 0j), [Q, P])     # cycle where y^2<0
    tau = per2 / per1
    print(f"  holomorphic period = {mp.nstr(per1, 12)}  (= Gamma(1/4)^2/(2 sqrt(2 pi)) = "
          f"{mp.nstr(mp.gamma(0.25)**2/(2*mp.sqrt(2*mp.pi)), 12)})")
    print(f"  period ratio tau = {mp.nstr(tau, 14)}  -> |Re|~0, |tau|=1 => tau = +-i (CM, lemniscatic)")

    print("\nComparison to N=2 SU(2):")
    print("  pure SU(2) Seiberg-Witten theory is a FAMILY of curves over the Coulomb branch (u),")
    print("  y^2 = (x^2 - Lambda^4)(x - u); the SW differential lambda_SW gives a(u), a_D(u), the")
    print("  prepotential F(a), the scale Lambda, and mass deformations. The self-dual point u=0 has")
    print("  gauge coupling tau = i (the S-duality fixed point).")
    print("  The m=2 metallic side is a SINGLE fixed curve (one manifold, m136): NO Coulomb-branch")
    print("  parameter u, NO SW differential family, NO prepotential function, NO scale Lambda.")

    print("\nVERDICT (Gate 2): NEGATIVE -- forced single-point CM coincidence, not a SW identification.")
    print("  - The match is exactly ONE number: tau = i = the SU(2) self-dual coupling, equivalent to")
    print("    j = 1728. It is the single CM invariant, forced by the silver mean (a=6 in kappa=P^2-6).")
    print("  - 'm136's curve IS the SW curve of SU(2) at u=0' is TRUE but VACUOUS: it asserts only that")
    print("    both are CM-by-Z[i] elliptic curves (isomorphic over C). There is NO Coulomb branch,")
    print("    prepotential, or dynamics on the metallic side to identify with the gauge theory.")
    print("  - The web's exact computations (tau=i, period=Gamma(1/4)^2/(2 sqrt 2 pi)) are CORRECT;")
    print("    the SW *identification* built on them is not earned. Number theory, not 4D physics.")


if __name__ == "__main__":
    main()
