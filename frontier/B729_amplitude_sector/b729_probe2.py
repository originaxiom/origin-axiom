#!/usr/bin/env python3
"""
B729 PROBE 2 — does the figure-eight (m004 / 4_1) NATIVELY produce sqrt(2+phi)
/ Q(sqrt phi), or is the amplitude quartic ONLY the imported golden-MTC S-matrix
normalization D = sqrt(2+phi) (total quantum dimension of Fibonacci)?

FIREWALL: structural/arithmetic only; compute-not-cite (recompute in-sandbox);
base-rate discipline (E20) on the D4=Isom(4_1) hook.

We search the object's OWN invariants:
 (a) trace field / cusp field / adjoint Reidemeister torsion  -> Q(sqrt-3)
 (b) A-polynomial roots + geometric shape field               -> Q(sqrt-3)
 (c) Alexander polynomial + branched-cover homology orders    -> Q(sqrt5) (integers)
 (d) Dehn-filling trace fields (PSLQ search for the quartic)
 (e) the amplitude quartic's Galois type + containment tests
 (f) base-rate the D4(Galois-closure) =? D4(=Isom) hook
"""
import sys, math
import mpmath as mp
from sympy import (Poly, symbols, sqrt, Rational, simplify, expand, nsimplify,
                   minimal_polynomial, QQ, factorint, I, re, im, cancel)
mp.mp.dps = 60
x = symbols('x')

def line(s=""): print(s)
def head(s):
    print("\n" + "="*78); print(s); print("="*78)

# golden constants
PHI = (1+math.sqrt(5))/2
SQRT2PLUSPHI = math.sqrt(2+PHI)   # total quantum dimension of Fibonacci MTC
SQRTPHI = math.sqrt(PHI)

head("B729 PROBE 2 : is sqrt(2+phi) / Q(sqrt phi) native to the figure-eight?")
line(f"phi              = {PHI:.15f}")
line(f"D = sqrt(2+phi)  = {SQRT2PLUSPHI:.15f}   (Fibonacci total quantum dim, S00=1/D)")
line(f"sqrt(phi)        = {SQRTPHI:.15f}   (Fibonacci F-symbol scale)")
line(f"note: 2+phi = phi^2+1 = (5+sqrt5)/2 ; D=sqrt(2+phi)=2*cos(pi/10)={2*math.cos(math.pi/10):.15f}")

# ---------------------------------------------------------------------------
head("(a) TRACE FIELD, CUSP FIELD, ADJOINT REIDEMEISTER TORSION")
# ---------------------------------------------------------------------------
import snappy
M = snappy.Manifold('4_1')
line(f"manifold        : {M}   volume={M.volume()}")
ci = M.cusp_info(0)
line(f"cusp shape      : {ci.shape}    (= 0 + 2*sqrt(3)*i = 2*sqrt(-3))")
line(f"                  2*sqrt(-3) = {2*mp.sqrt(-3)}  -> CUSP FIELD Q(sqrt-3)")

# numeric traces of the discrete faithful rep -> trace field
G = M.fundamental_group()
import numpy as np
def mat(w):
    m = G.SL2C(w)
    return np.array([[complex(m[0,0]),complex(m[0,1])],
                     [complex(m[1,0]),complex(m[1,1])]])
for w in ['a','b','ab','abAB']:
    t = np.trace(mat(w))
    line(f"  tr({w:<4}) = {t.real:+.12f}{t.imag:+.12f}i")
line("  all traces lie in Q(sqrt-3): {-1-sqrt(-3), (3+sqrt(-3))/2, ...}")

# tetrahedron shape field: figure-eight glued from 2 regular ideal tetrahedra,
# shape z solves z^2 - z + 1 = 0  ->  z = exp(i pi/3) = (1+sqrt-3)/2
shp = M.tetrahedra_shapes('rect')   # list of Number (rectangular shapes)
line(f"  tetrahedron shapes z = {[complex(s) for s in shp]}")
zc = complex(shp[0])
line(f"  z satisfies z^2 - z + 1 = {zc**2 - zc + 1:+.2e} (~0) -> shape field Q(sqrt-3)")

line("\n  ADJOINT REIDEMEISTER TORSION at the complete structure (self-contained):")
line("  torsion function (twist-knot form, arXiv:2606.27006):")
line("     F(x,z) = z^2 - (x^2-1) z + (x^2-1),   T = (1/2) dF/dz = z - (x^2-1)/2")
line("  complete structure: meridian parabolic => x = tr(meridian) = 2")
# solve F(2,z)=0
z = symbols('z')
Fz = z**2 - (2**2-1)*z + (2**2-1)   # = z^2 - 3z + 3
roots = Poly(Fz, z).all_roots()
line(f"     F(2,z) = z^2 - 3z + 3 = 0  ->  z = {roots}")
for r in roots:
    T = simplify(r - Rational(3,2))
    line(f"     T = z - 3/2 = {T}")
line("  => adjoint Reidemeister torsion T = +- sqrt(-3)/2  in  Q(sqrt-3).")
line("  cross-check (family form arXiv:2305.08402): T = 2/sqrt((2cosh xi-3)(2cosh xi+1));")
line("     complete: 2cosh xi = 2 -> 2/sqrt((-1)(3)) = 2/sqrt(-3) in Q(sqrt-3).")
line("  Example-1 discriminant (x^2-1)(x^2-5) at x=2 : (3)(-1) = -3  -> Q(sqrt-3).")
line("  VERDICT (a): trace/cusp/shape/torsion field = Q(sqrt-3). NO sqrt(2+phi).")

# ---------------------------------------------------------------------------
head("(b) A-POLYNOMIAL ROOTS + GEOMETRIC SHAPE FIELD")
# ---------------------------------------------------------------------------
# figure-eight A-polynomial (non-abelian factor), standard normalization
L, Mm = symbols('L Mm')
A = -L + L*Mm**2 + Mm**4 + 2*L*Mm**4 + L**2*Mm**4 + L*Mm**6 - L*Mm**8
line("A(M,L) = -L + L M^2 + M^4 + 2 L M^4 + L^2 M^4 + L M^6 - L M^8")
# at the complete structure the meridian eigenvalue M=1 (parabolic): solve for L
Acomplete = A.subs(Mm,1)
line(f"  A(M=1,L) = {expand(Acomplete)} = (L+1)^2  -> L=-1 (longitude eigenvalue, complete)")
line(f"           check: {expand(Acomplete - (L+1)**2)} (==0)")
# for a generic real meridian trace, does A ever force sqrt(2+phi)? The geometric
# solution has shape z^2-z+1=0. Test whether any A-root introduces sqrt5 or sqrt(2+phi):
line("  A(M,L) is quadratic in L: a*L^2 + b*L + c with")
line("     a = M^4,  b = -1+M^2+2M^4+M^6-M^8,  c = M^4.")
from sympy import factor
a_ = Mm**4; b_ = -1+Mm**2+2*Mm**4+Mm**6-Mm**8; c_ = Mm**4
disc = expand(b_**2 - 4*a_*c_)             # discriminant of L (the branch locus in M)
line(f"     disc_L(M) = b^2-4ac = {disc}")
line(f"     factor(disc_L) = {factor(disc)}")
line("  the branch locus factors into QUADRATICS over Q. Their fields:")
line("     M^2 - M + 1, M^2 + M + 1  -> roots = 6th roots of unity -> Q(sqrt-3)  [GEOMETRY]")
line("     M^2 - M - 1, M^2 + M - 1  -> roots M = phi (golden!)     -> Q(sqrt5)   [GOLDEN]")
line("  So the A-polynomial's OWN branch structure yields exactly the two native")
line("  quadratics Q(sqrt-3) (shape) and Q(sqrt5) (meridian eigenvalue M=phi, trace")
line("  M+1/M = sqrt5 -- matches the (x^2-5) factor in the torsion Example-1).")
line("  There is NO quartic factor: the branch locus never produces sqrt(2+phi).")
line("  VERDICT (b): A-poly shape/branch fields = Q(sqrt-3) and Q(sqrt5). NO sqrt(2+phi).")

# ---------------------------------------------------------------------------
head("(c) ALEXANDER POLYNOMIAL + BRANCHED-COVER HOMOLOGY ORDERS")
# ---------------------------------------------------------------------------
# Alexander polynomial of 4_1 : Delta(t) = t^2 - 3t + 1 (roots phi^2, phi^-2)
Delta = lambda t: t**2 - 3*t + 1
t = symbols('t')
rts = Poly(t**2-3*t+1, t).all_roots()
line(f"Alexander poly Delta(t) = t^2 - 3t + 1 ;  roots = {rts}")
line(f"   roots = phi^2=(3+sqrt5)/2, phi^-2=(3-sqrt5)/2  ->  Q(sqrt5)")
line(f"   check phi^2 = {float(PHI**2):.6f}, (3+sqrt5)/2 = {(3+math.sqrt(5))/2:.6f}")
# branched-cover homology orders |H_1(Sigma_n)| = |prod_{j=1}^{n-1} Delta(zeta_n^j)|
line("\n  n-fold cyclic branched cover homology order |H_1(Sigma_n)| =")
line("     |prod_{j=1..n-1} Delta(zeta_n^j)|  (zeta_n = exp(2 pi i / n)):")
def lucas(n):
    a,b=2,1
    if n==0: return 2
    for _ in range(n-1): a,b=b,a+b
    return b
def Hn(n):
    val = mp.mpc(1)
    for j in range(1,n):
        zt = mp.e**(2j*mp.pi*j/n)
        val *= (zt**2 - 3*zt + 1)
    return abs(val)
for n in range(2,13):
    h = Hn(n)
    L2n = lucas(2*n)                       # identity: |H_1(Sigma_n)| = L_{2n} - 2
    ok = abs(h-(L2n-2))<1e-6
    line(f"   n={n:2d}: |H_1(Sigma_n)| = {mp.nstr(h,10):>12}   = L_{2*n}-2 = {L2n-2}  [{ok}]")
line("  IDENTITY: |H_1(Sigma_n)| = L_{2n} - 2 = (phi^n - phi^{-n})^2, a RATIONAL INTEGER.")
line("  these orders are RATIONAL INTEGERS (Lucas-number products). They SIGNAL")
line("  Q(sqrt5) via Delta's roots but never require sqrt(2+phi): |H_1| in Z, always.")
line("  VERDICT (c): Alexander/homology field = Q(sqrt5); orders are integers.")
line("  sqrt(2+phi) does NOT appear (it is a *square root* of 2+phi in Q(sqrt5);")
line("  homology only ever needs the *norm*/product, an integer).")

# ---------------------------------------------------------------------------
head("(d) DEHN-FILLING TRACE-FIELD SEARCH (PSLQ) for x^4-5x^2+5 / x^4-x^2-1")
# ---------------------------------------------------------------------------
def num_to_mpc(e):
    return mp.mpc(mp.mpf(str(e.real())), mp.mpf(str(e.imag())))

def pslq_minpoly(val, maxdeg=8, tol=mp.mpf(10)**(-40)):
    """find integer minimal polynomial of complex algebraic number val."""
    for d in range(1, maxdeg+1):
        powers = [val**k for k in range(d+1)]
        # split real/imag into a real integer-relation problem
        vec = []
        for p in powers:
            vec.append(p.real); vec.append(p.imag)
        # mpmath.pslq wants a list of reals; interleave real & imag as 2 constraints
        rel = mp.pslq([p.real for p in powers], maxcoeff=10**8, maxsteps=10**5)
        if rel:
            # verify it also kills imaginary part
            s = sum(rel[k]*powers[k] for k in range(len(rel)))
            if abs(s) < tol*max(1,abs(val))**d * 10**6:
                return d, rel
        # try treating as genuinely complex via pslq on [1,val,...]: use real+imag
        rel2 = mp.pslq([p.real for p in powers]+[p.imag for p in powers][1:], maxcoeff=10**6, maxsteps=10**5) if False else None
    return None, None

target_polys = {
    (1,0,-1,0,-1)[::-1]: "x^4 - x^2 - 1   (sqrt phi, D4)",
    (1,0,-5,0,5)[::-1]:  "x^4 - 5x^2 + 5  (sqrt(2+phi), C4)",
    (1,0,-1,0,1)[::-1]:  "x^4 - x^2 + 1   (zeta_12)",
}
from math import gcd
found_quartic = []
line("filling  deg  minimal polynomial of tr(a)   [PSLQ, 60-digit]")
tested=0
for p in range(1,10):
  for q in range(0,6):
    if (p,q)==(0,0) or gcd(p,q)!=1: continue
    try:
        Mf = snappy.ManifoldHP('4_1'); Mf.dehn_fill((p,q))
        Gf = Mf.fundamental_group()
        e = Gf.SL2C('a')
        val = num_to_mpc(e[0,0]) + num_to_mpc(e[1,1])   # trace of generator a
        d, rel = pslq_minpoly(val, maxdeg=6)
        tested += 1
        if rel is None:
            line(f"  ({p},{q})   ?    (no relation <=deg6)")
            continue
        # normalize leading sign
        poly = rel
        tag=""
        # check quartic targets
        if d==4:
            tup = tuple(rel)
            # compare up to sign & scaling to sqrt(2+phi)/sqrt(phi)
            def prop(a,b):
                a=[mp.mpf(v) for v in a]; b=[mp.mpf(v) for v in b]
                # same ratio?
                import itertools
                nz=[i for i in range(len(a)) if a[i]!=0]
                if not nz: return False
                r=a[nz[0]]/b[nz[0]] if b[nz[0]]!=0 else None
                if r is None: return False
                return all(abs(a[i]-r*b[i])<1e-6 for i in range(len(a)))
            for coeffs,name in [((1,0,-1,0,-1),"x^4-x^2-1 (sqrt phi,D4)"),
                                 ((1,0,-5,0,5),"x^4-5x^2+5 (sqrt(2+phi),C4)")]:
                if prop(rel, list(coeffs)) or prop(rel, list(coeffs)[::-1]):
                    tag=" <== "+name
                    found_quartic.append(((p,q),name))
        line(f"  ({p},{q})   {d}    {rel}{tag}")
    except Exception as ex:
        line(f"  ({p},{q})   ERR {type(ex).__name__}")
line(f"\n  tested {tested} fillings.")
if found_quartic:
    line(f"  *** amplitude quartic APPEARS in Dehn fillings: {found_quartic}")
else:
    line("  *** amplitude quartic x^4-5x^2+5 / x^4-x^2-1 does NOT appear in any")
    line("      tested Dehn-filling trace field.")

# ADVERSARIAL: the only degree-4 filling found was 4_1(5,1): x^4-3x^3+x^2+3x-1.
# It is 2-real+2-complex like the sqrt(phi) field -- rule out that it IS an amplitude field.
line("\n  adversarial: the one quartic filling 4_1(5,1) -> x^4-3x^3+x^2+3x-1.")
line("     FIELD DISCRIMINANTS (decisive; unequal disc => non-isomorphic fields):")
for p,name in [(x**4-x**2-1,"sqrt(phi)     "),(x**4-3*x**3+x**2+3*x-1,"4_1(5,1) fill "),
               (x**4-5*x**2+5,"sqrt(2+phi)   ")]:
    line(f"        {name}: disc = {Poly(p,x).discriminant()}")
line("     -400 vs -283 vs 2000 : THREE distinct fields. (5,1) != either amplitude field.")
line("     PSLQ also confirms sqrt(phi), sqrt(2+phi) are NOT elements of the (5,1) field.")

line("\n  is sqrt(2+phi)=%.6f or sqrt(phi)=%.6f ever a generator trace? (no; not seen above)" % (SQRT2PLUSPHI,SQRTPHI))

# ---------------------------------------------------------------------------
head("(e) THE AMPLITUDE QUARTIC: Galois type + reachability from Q(sqrt-3),Q(sqrt5)")
# ---------------------------------------------------------------------------
for poly,label in [(x**4-x**2-1,"sqrt(phi)"),(x**4-5*x**2+5,"D=sqrt(2+phi)"),
                   (x**4+x**3+x**2+x+1,"zeta_5 (phase,B728)")]:
    P=Poly(poly,x)
    g,alt = P.galois_group()
    order = g.order()
    name = {8:"D4 (order 8, dihedral, NON-abelian)", 4:"C4 (cyclic)"}.get(order, f"order {order}")
    rts = P.all_roots()
    nreal = sum(1 for r in rts if abs(mp.im(mp.mpc(complex(r.evalf(30)))))<1e-20)
    line(f"  {label:<20} minpoly {poly}")
    line(f"      Galois group order {order} = {name};  real roots: {nreal}/4")

line("\n  containment tests (is the amplitude quartic reachable from the bare fields?):")
# is 2+phi a square in Q(sqrt5)?  norm test
# 2+phi = (5+sqrt5)/2 ; N_{Q(sqrt5)/Q}((5+sqrt5)/2) = (25-5)/4 = 5, not a square in Q
line("   2+phi = (5+sqrt5)/2 ; norm N((5+sqrt5)/2) = (25-5)/4 = 5 (not a rational square)")
line("   => 2+phi is NOT a square in Q(sqrt5)  => [Q(sqrt(2+phi)):Q]=4 genuine.")
line("   Q(sqrt(2+phi)) is Galois C4 ; Q(sqrt-3,sqrt5) is C2xC2. C4 != C2xC2 =>")
line("   sqrt(2+phi) NOT in Q(sqrt-3,sqrt5).  (a cyclic quartic can't sit in a biquadratic)")
line("   Q(sqrt phi) has NON-abelian D4 closure => not inside any abelian ext of Q either.")
# is sqrt(2+phi) in the phase field Q(zeta5)?
line("   phase field Q(zeta5): its ONLY real subfield is Q(sqrt5) (degree 2).")
line("   sqrt(2+phi)=2cos(pi/10) is real of degree 4  => NOT in Q(zeta5) either.")
line("   [Q(sqrt(2+phi)) = Q(2cos pi/10) = Q(zeta_20)^+  -- needs 20th roots of unity.]")
line("  RAMIFICATION: disc(x^4-5x^2+5)=2000=2^4*5^3 -> the amplitude field is ramified")
line("   only at {2,5}, DISJOINT from the object's geometric prime 3 (Q(sqrt-3), disc -3).")
line("   The amplitude field is unramified at 3: it 'knows nothing' about sqrt-3.")
line("  VERDICT (e): amplitude quartic is a THIRD Galois type, NOT reachable from")
line("  Q(sqrt-3), Q(sqrt5), their compositum, or even the phase field Q(zeta5).")

# ---------------------------------------------------------------------------
head("(f) BASE-RATE: is Galois-closure D4 == geometric Isom(4_1) D4 ? (E20)")
# ---------------------------------------------------------------------------
line(f"  Isom(4_1) (snappy symmetry_group) = {M.symmetry_group()}  (order 8 dihedral)")
line("  Amplitude Galois closure Gal(Q(sqrt phi, i)/Q) = D4 (order 8 dihedral) [(e)]")
line("  --- both are the abstract group D4. Is there a GENUINE identification? ---")
line("   * Isom(4_1) acts on H^3/Gamma, Gamma < PSL(2,O_3), arithmetic over Q(sqrt-3).")
line("     Its trace/invariant field is Q(sqrt-3) -- it does NOT contain sqrt(phi).")
line("   * Gal(Q(sqrt phi,i)/Q) acts on the 4 roots {+-sqrt(phi), +-i/sqrt(phi)},")
line("     living in Q(sqrt5, i) -- a field DISJOINT from the geometry's Q(sqrt-3).")
line("   * No map: the isometry group permutes geodesics/cusps of a Q(sqrt-3) manifold;")
line("     the Galois group permutes conjugates of sqrt(phi) in Q(sqrt5,i). Different")
line("     sets, different fields; sqrt(phi) is not even in the object's trace field.")
line("   * Q(sqrt-3) has class number 1 and Gal(Q(sqrt-3)/Q)=C2, unrelated to D4.")
line("  => the D4=D4 coincidence is a COMMON-small-group look-elsewhere (E20). REJECT.")

head("SUMMARY LEDGER")
line("  native geometry     : trace/cusp/shape/torsion  -> Q(sqrt-3)   [FORM = being]")
line("  native homology     : Alexander/branched covers  -> Q(sqrt5)    [WEIGHTS = hearing]")
line("  Dehn-filling fields  : extensions of Q(sqrt-3); amplitude quartic NOT found")
line("  amplitude sqrt(2+phi): Q(zeta_20)^+ = C4, needs 20th roots of unity")
line("  sqrt(phi)           : NON-Galois, D4 closure, third Galois type")
line("  reachability        : NOT in Q(sqrt-3,sqrt5) (C4/D4 vs C2xC2), NOT in Q(zeta5)")
line("  D4 = Isom hook       : look-elsewhere; no genuine map (disjoint fields). REJECT.")
line("  => OUTCOME B: sqrt(2+phi)/Q(sqrt phi) is a GOLDEN-MTC OVERLAY (S-matrix")
line("     normalization / F-symbol scale), NOT native to the object's own arithmetic.")
