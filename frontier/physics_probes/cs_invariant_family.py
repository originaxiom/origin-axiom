"""CS-invariant family of the metallic mapping tori, m=1,2,3 (topology / number theory).

For the once-punctured-torus bundle with monodromy phi_m^2 (phi_m: a->a^m b, b->a), at the
COMPLETE hyperbolic structure (kappa = tr[A,B] = -2, both peripheral elements parabolic), compute
the normal Reidemeister-type torsion tau_m(geom) = det'(I - D(T_m^2)|_normal) and the trace field.

This CORRECTS the earlier evaluation at kappa=+2 (which included the IDENTITY rep x=2 and gave the
abelian determinant 5/32, not the geometric torsion). At the genuine kappa=-2 complete structure
the discrete-faithful rep is the root with REAL torsion (others are Galois conjugates).

Uniform method (one code path, m=1,2,3): branch y=beta_m z/(1-alpha_m) from p_m(x,y,z)=y; z-branch
from T_m^2[0]=x; kappa=x^2+y^2+z^2-xyz-2 (Fricke); rationalize kappa=-2; the discrete-faithful root
= the one whose normal torsion is real. Labels: standalone topology/number theory, NO thesis claim.
"""
import sympy as sp
import mpmath as mp
mp.mp.dps = 30
x, y, z, t = sp.symbols("x y z t")


def pseq(mm, X, Y, Z):
    p = [Y, Z]
    for _ in range(2, mm + 2):
        p.append(sp.expand(X * p[-1] - p[-2]))
    return p


def Tm(mm, v):
    X, Y, Z = v
    p = pseq(mm, X, Y, Z)
    return (p[mm], X, p[mm + 1])


def Tm_sq(mm):
    return Tm(mm, Tm(mm, (x, y, z)))


VOL = {1: "2.0298832 (figure-eight 4_1)", 2: "3.6638623 (census m136)",
       3: "(one-cusped bundle, monodromy [[10,3],[3,1]]; needs SnapPy)"}
APOLY = {1: "M^4 L^2 +(-M^8+M^6+2M^4+M^2-1)L +M^4  (Cooper-Long 1996; B67, exact)",
         2: "M^2 L^2 -(M^4-4M^2+1)L +M^2  (verified, this work)",
         3: "FLAGGED: tr(t)^2(x) carries sqrt(5x^4-10x^3-x^2+6x+1); not a clean rational eliminant"}

for mm in (1, 2, 3):
    print("=" * 70)
    print(f"m = {mm}")
    print("=" * 70)
    F = Tm_sq(mm)
    pm = pseq(mm, x, y, z)[mm]
    yb = sp.solve(sp.Eq(pm, y), y)[0]                       # y = beta z/(1-alpha)
    eq0 = sp.expand((F[0] - x).subs(y, yb))
    zsols = sp.solve(sp.Eq(sp.numer(sp.together(eq0)), 0), z)
    J = sp.Matrix([[sp.diff(F[i], v) for v in (x, y, z)] for i in range(3)]).subs({y: yb})

    # choose the geometric z-branch: non-constant kappa
    branch = None
    for zc in zsols:
        yc = yb.subs(z, zc)
        kap = sp.simplify(x**2 + yc**2 + zc**2 - x * yc * zc - 2)
        if not kap.is_number:
            branch = (zc, sp.together(kap))
            break
    zc, kap = branch
    zf = sp.lambdify(x, zc, "mpmath")

    def torsion_at(xv):
        zv = zf(xv)
        Jn = mp.matrix([[mp.mpc(complex(J[i, j].subs({x: xv, z: zv}))) for j in range(3)]
                        for i in range(3)])
        E = sorted(mp.eig(Jn, left=False, right=False), key=lambda e: abs(e - 1))
        return (1 - E[1]) * (1 - E[2])

    # rationalize kappa = -2 ; the numerator gives the candidate x's
    A_ = kap.subs(sp.sqrt(sp.Symbol('__')), 0) if False else None
    P = sp.numer(sp.together(kap + 2))
    # kappa may contain a sqrt: rationalize by P_rat = numer((A+2)^2 - B^2 disc)
    sq = [a for a in kap.atoms(sp.Pow) if a.exp == sp.Rational(1, 2)]
    if sq:
        s = sq[0]
        A = sp.expand(kap.subs(s, 0)); B = sp.simplify((kap - A) / s)
        P = sp.numer(sp.together((A + 2)**2 - B**2 * s.base))
    roots = sp.Poly(P, x).all_roots()
    # discrete-faithful geometric root = complex root with REAL torsion
    geom, tau = None, None
    for r in roots:
        rv = complex(r)
        if abs(rv) < 1e-9 or abs(rv - 1) < 1e-9 or abs(rv.imag) < 1e-9:
            continue
        tv = torsion_at(mp.mpc(rv))
        if abs(tv.imag) < 1e-12 * max(1, abs(tv)):
            geom, tau = r, tv.real
            break
    mpoly = sp.minimal_polynomial(geom, sp.Symbol('u'))
    print(f"  geometric rep (kappa=-2, discrete-faithful): x ~ {mp.nstr(mp.mpc(complex(geom)),8)}")
    print(f"  trace-field min poly of x: {mpoly}   (degree {sp.degree(mpoly)})")
    print(f"  tau_{mm}(geom) = {mp.nstr(tau, 16)}")
    rec = mp.identify(tau) or mp.findpoly(tau, 4, maxcoeff=10**4)
    print(f"  tau recognized: {rec if rec else '(not a low-degree clean number)'}")
    # branch check: do the +/- sqrt(disc) fixed-locus branches agree? (clean for m=1,2; not m=3)
    if sq:
        zc2 = [s_ for s_ in zsols if sp.simplify(s_ - zc) != 0 and not (yb.subs(z, s_)).is_number]
        if zc2:
            zf2 = sp.lambdify(x, zc2[0], "mpmath")
            taus2 = []
            for r in roots:
                rv = complex(r)
                if abs(rv) < 1e-9 or abs(rv - 1) < 1e-9 or abs(rv.imag) < 1e-9:
                    continue
                zv = zf2(mp.mpc(rv))
                Jn = mp.matrix([[mp.mpc(complex(J[i, j].subs({x: mp.mpc(rv), z: zv}))) for j in range(3)] for i in range(3)])
                Ee = sorted(mp.eig(Jn, left=False, right=False), key=lambda e: abs(e - 1))
                tv = (1 - Ee[1]) * (1 - Ee[2])
                if abs(tv.imag) < 1e-10 * max(1, abs(tv)):
                    taus2.append(tv.real)
            print(f"  BRANCH CHECK (other sqrt-branch real torsions): {[mp.nstr(v,8) for v in taus2]}"
                  f"  -> {'AGREES (clean)' if any(abs(v-tau)<1e-6 for v in taus2) else 'DISAGREES => m='+str(mm)+' torsion is branch-AMBIGUOUS'}")
    print(f"  A-polynomial: {APOLY[mm]}")
    print(f"  hyperbolic volume: {VOL[mm]}")
    print()

print("=" * 70)
print("SUMMARY (corrected, at the kappa=-2 complete structure)")
print("=" * 70)
print("  m  tau_m(geom)        trace-field degree")
print("  1     -3   (clean)        2   (Q(sqrt(-3)); |tau|=3=|disc|)")
print("  2    -16   (clean)        4")
print("  3    branch-AMBIGUOUS     8   (the +/-sqrt(disc) fixed-locus branches give different")
print("        (-2.64 or -52.08)       real torsions; NOT cleanly determined without pinning the")
print("                                discrete-faithful rep via SnapPy)")
print("  -> the family has NO tidy arithmetic pattern. m=1,2 give clean integers (-3,-16) and m=1")
print("     (|tau|=3=|disc Q(sqrt-3)|) is special; by m=3 the trace field is degree 8 and the")
print("     geometric torsion is already branch-ambiguous. The metallic CS family is genuinely")
print("     complicated -- no clean new invariant pattern.")
print("  Earlier kappa=+2 values (5, 32) were at the WRONG (non-geometric) point and are abelian.")
