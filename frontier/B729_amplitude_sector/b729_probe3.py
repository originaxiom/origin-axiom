#!/usr/bin/env python3
# B729 Probe 3 -- complete the Born-content ledger. AMPLITUDE sector: forced-native or overlay?
# COMPUTE-NOT-CITE (E19): every discriminating fact recomputed in-sandbox.
# BASE-RATE DISCIPLINE (E20): the D4 = Isom(4_1) coincidence is a TRAP unless a genuine map is exhibited.
#
# Structure:
#   PART 1  Galois type of every Born quartic sector, recomputed (phase / amplitude-S / F-symbol / bare compositum)
#   PART 2  Identify the actual field of the Fibonacci S-matrix Born amplitudes (1/D, phi/D, D=sqrt(2+phi))
#           -- is it really Q(sqrt phi) [D4] as the prereg says, or a different Galois type?
#   PART 3  Reachability: is the amplitude field inside the object's two bare faces Q(sqrt-3,sqrt5)?
#   PART 4  OBJECT-NATIVE search: does sqrt(2+phi) appear in 4_1's OWN invariants
#           (trace field, Alexander, det, cyclic branched-cover homology), or ONLY at a level-5 evaluation?
#   PART 5  BASE-RATE the D4 = Isom(4_1) hook (snappy symmetry group vs arithmetic Galois D4)
#   PART 6  Final Born-content ledger + A/B verdict

import sympy as sp
from sympy import sqrt, Rational, I, pi, sin, cos, nsimplify, symbols, Poly, QQ, factor_list
from sympy import minimal_polynomial as minpoly
from sympy.combinatorics.galois import S4TransitiveSubgroups

x = symbols('x')
LINE = "="*78

def galois_type_biquad(b, c):
    """Galois group of irreducible x^4 + b x^2 + c over Q (classical resolvent criterion)."""
    if sp.sqrt(sp.Rational(c)).is_rational:
        return "C2xC2 (Klein)  [c is a square]"
    if sp.sqrt(sp.Rational(c*(b*b - 4*c))).is_rational:
        return "C4 (cyclic)    [c*(b^2-4c) is a square]"
    return "D4 (dihedral, order 8, NON-Galois quartic)  [neither square]"

print(LINE); print("PART 1 -- Galois type of every Born quartic sector (recomputed)"); print(LINE)

# PHASE field Q(zeta_5): min poly of zeta5
z5 = sp.exp(2*sp.pi*I/5)
mp_z5 = minpoly(z5, x)
print(f"PHASE  Q(zeta5): min poly = {mp_z5}")
gg_z5 = sp.polys.numberfields.galoisgroups.galois_group(Poly(mp_z5, x))
print(f"       Galois group (sympy) = {gg_z5[0]}  -> cyclic C4 (unique quad subfield Q(sqrt5))")

# F-SYMBOL field Q(sqrt phi): sqrt of golden ratio, min poly x^4 - x^2 - 1
phi = (1 + sqrt(5))/2
sphi = sqrt(phi)
mp_sphi = minpoly(sphi, x)
print(f"\nF-SYM  Q(sqrt phi): min poly = {mp_sphi}   (this is the F-matrix/associator entry field)")
# irreducible x^4 + b x^2 + c with b=-1,c=-1
print(f"       resolvent verdict (b=-1,c=-1): {galois_type_biquad(-1,-1)}")
# confirm non-Galois: count real roots of x^4 - x^2 - 1
rts_sphi = sp.Poly(x**4 - x**2 - 1, x).all_roots()
nreal = sum(1 for r in rts_sphi if sp.im(r) == 0)
print(f"       roots of x^4-x^2-1: {nreal} real + {4-nreal} imaginary -> NOT Galois; closure Q(sqrt phi, i), order 8")

# AMPLITUDE field Q(D), D = sqrt(2+phi): min poly x^4 - 5x^2 + 5
D = sqrt(2 + phi)
mp_D = minpoly(D, x)
print(f"\nAMPL   Q(D)=Q(sqrt(2+phi)): min poly = {mp_D}   (this is the S-matrix Born-amplitude entry field)")
print(f"       resolvent verdict (b=-5,c=5): {galois_type_biquad(-5,5)}")
rts_D = sp.Poly(x**4 - 5*x**2 + 5, x).all_roots()
nreal_D = sum(1 for r in rts_D if sp.im(r) == 0)
print(f"       roots of x^4-5x^2+5: {nreal_D} real + {4-nreal_D} imaginary -> TOTALLY REAL, Galois")
gg_D = sp.polys.numberfields.galoisgroups.galois_group(Poly(mp_D, x))
print(f"       Galois group (sympy) = {gg_D[0]}")

# BARE compositum Q(sqrt-3, sqrt5)
print(f"\nBARE   Q(sqrt-3, sqrt5): compositum of FORM (being) and WEIGHTS (hearing)")
mp_comp = minpoly(sqrt(-3) + sqrt(5), x)
print(f"       min poly of sqrt-3+sqrt5 = {mp_comp}")
gg_comp = sp.polys.numberfields.galoisgroups.galois_group(Poly(mp_comp, x))
print(f"       Galois group (sympy) = {gg_comp[0]}  -> Klein C2xC2 (three quad subfields: sqrt-3, sqrt5, sqrt-15)")

print(f"\n>>> FOUR DISTINCT GALOIS TYPES AT DEGREE 4:")
print(f"    phase Q(zeta5)          = C4  (CM, totally imaginary)")
print(f"    amplitude Q(sqrt(2+phi))= C4  (totally REAL)   <-- corrected: NOT D4")
print(f"    F-symbol  Q(sqrt phi)   = D4  (non-Galois)     <-- the D4 the prereg named")
print(f"    bare      Q(sqrt-3,sqrt5)= C2xC2 (Klein)")

print(); print(LINE); print("PART 2 -- WHICH field do the Born amplitudes (S-matrix entries) actually live in?"); print(LINE)

# Fibonacci MTC data, entries computed explicitly.
Dsym = sqrt(2 + phi)                       # total quantum dimension = sqrt(1+phi^2)=sqrt(2+phi)
S = sp.Matrix([[1/Dsym, phi/Dsym],
               [phi/Dsym, -1/Dsym]])       # modular S-matrix (Born amplitudes)
T = sp.diag(1, sp.exp(4*sp.pi*I/5))        # twist / T-matrix (PHASE sector: theta_tau = zeta5^2)
invphi = 1/phi
Fm = sp.Matrix([[invphi, sqrt(invphi)],
                [sqrt(invphi), -invphi]])  # F-symbol (associator)

print("Fibonacci total quantum dimension D = sqrt(1+phi^2) = sqrt(2+phi):",
      "1+phi^2 == 2+phi ?", sp.simplify((1+phi**2) - (2+phi)) == 0)
print("\nS-matrix Born amplitudes (entries): 1/D and phi/D")
for val,name in [(1/Dsym,"1/D"), (phi/Dsym,"phi/D")]:
    mp = minpoly(val, x)
    deg = sp.degree(mp, x)
    print(f"   {name:6s} = {str(sp.nsimplify(val)):>22} , min poly {mp}  (deg {deg})")
print("   => S-entries generate Q(1/D)=Q(D)=Q(sqrt(2+phi))  [C4, totally real].")

print("\nT-matrix twist (phase): theta_tau = exp(4 pi i/5) = zeta5^2, min poly",
      minpoly(sp.exp(4*sp.pi*I/5), x), " => Q(zeta5) [C4, CM].  (B728: IMPORTED)")

print("\nF-symbol (associator) entry: sqrt(1/phi) = phi^(-1/2), min poly",
      minpoly(sqrt(invphi), x), " => Q(sqrt phi) [D4].  (a FIFTH ingredient, not a Born sector)")

print("\n>>> CORRECTION TO PREREG: the Born AMPLITUDES (S-matrix) live in Q(sqrt(2+phi)) = C4,")
print("    NOT the D4 field Q(sqrt phi). Q(sqrt phi) [D4] is the F-symbol/associator field.")

print(); print(LINE); print("PART 3 -- Reachability: is the amplitude field inside the two bare faces Q(sqrt-3,sqrt5)?"); print(LINE)

# The bare compositum is Klein C2xC2, degree 4. Each quartic sector is ALSO degree 4.
# Containment at equal degree <=> equality; and equality fails by Galois type (C4/D4 vs Klein)
# AND by: the quartics do NOT contain sqrt(-3) (their unique/only quadratic subfield is Q(sqrt5)).
for nm, gen, mp in [("phase Q(zeta5)", z5, x**4+x**3+x**2+x+1),
                    ("amplitude Q(sqrt(2+phi))", D, x**4-5*x**2+5),
                    ("F-symbol Q(sqrt phi)", sphi, x**4-x**2-1)]:
    # does it contain sqrt(-3)? sqrt(-3) has degree 2; test if minpoly(sqrt(-3)) factors over the field
    contains_m3 = sp.factor_list(x**2+3, extension=gen)[1]
    splits = any(sp.degree(f,x)==1 for f,_ in contains_m3)
    print(f"{nm:28s}: contains sqrt(-3)? {splits}  -> {'IN' if splits else 'NOT IN'} Q(sqrt-3,sqrt5)")
print(">>> NONE of the three quartic sectors sits inside the Klein biquadratic Q(sqrt-3,sqrt5):")
print("    they contain sqrt5 (the hearing seam) but NEVER sqrt-3 (the being).")
print("    Same structural refutation B728 used for the phase, now confirmed for the amplitude.")

print(); print(LINE); print("PART 4 -- OBJECT-NATIVE search: does sqrt(2+phi) appear in 4_1's OWN invariants?"); print(LINE)

# 4a. Identify D arithmetically: D = 2 sin(2pi/5) = 2 cos(pi/10); and i*D = zeta5 - zeta5^{-1}.
D_num = sp.N(D, 30)
print(f"D = sqrt(2+phi) = {D_num}")
print(f"   2 sin(2pi/5)  = {sp.N(2*sin(2*pi/5),30)}   equal? {sp.simplify(D - 2*sin(2*pi/5))==0}")
print(f"   2 cos(pi/10)  = {sp.N(2*cos(pi/10),30)}   equal? {sp.simplify(D - 2*cos(pi/10))==0}")
iD_check = complex(sp.N(z5 - 1/z5, 30)) - complex(sp.N(I*D, 30))
print(f"   zeta5 - zeta5^-1 - i*D  numerically = {iD_check:.2e}  -> zeta5-zeta5^-1 = i*D EXACTLY (i*D IN Q(zeta5))")
i_in_z5 = any(sp.degree(f,x)==1 for f,_ in sp.factor_list(x**2+1, extension=z5)[1])
print(f"   but D itself needs i, and i in Q(zeta5)? {i_in_z5}  -> D NOT in Q(zeta5): amplitude field != phase field")
print("   => D is the level-5 total quantum dimension; Q(zeta20)+ = Q(2cos pi/10). NOT a bare-geometry number.")

# 4b. The object 4_1 = m004: trace field, invariant trace field, Alexander, determinant.
import snappy
M = snappy.Manifold('4_1')
zshape = complex(M.tetrahedra_shapes()[0]['rect'])
print(f"\n4_1 = m004 tetrahedron shape z = {zshape:.6f}  (root of z^2 - z + 1 => trace field Q(sqrt-3))")
print(f"   z^2 - z + 1 at z: {abs(zshape**2 - zshape + 1):.2e} (approx 0 -> Q(sqrt-3), the BEING/FORM field)")

# --- Alexander polynomial derived IN-SANDBOX (two independent ways), no citation ---
t = symbols('t')
# (i) Fox calculus on snappy's ACTUAL presentation <a,b | abbbaBAAB>.
G = M.fundamental_group()
rel = G.relators()[0]           # 'abbbaBAAB'; lowercase=gen, UPPER=inverse
# abelianization H1=Z: a-expsum=0, b-expsum=1 => H1=Z^2/<(0,1)>, map a->t, b->1
phimap = {'a': t, 'A': 1/t, 'b': sp.Integer(1), 'B': sp.Integer(1)}
def fox_ab(rel, gen):
    """abelianized Fox derivative phi(d rel / d gen), gen in {'a','b'}."""
    P = sp.Integer(1); total = sp.Integer(0)
    for ch in rel:
        if ch == gen:                     # d x / d x = 1
            total += P
        elif ch == gen.upper():           # d x^-1 / d x = -x^-1  -> -phi(x^-1)
            total += P * (-phimap[ch])
        P *= phimap[ch]                   # advance prefix abelianization
    return sp.expand(total)
da, db = fox_ab(rel, 'a'), fox_ab(rel, 'b')
print(f"\n   Fox calculus on <a,b|{rel}>:  phi(dr/da) = {da} ,  phi(dr/db) = {db}")
# Alexander ideal E1 = <phi(dr/da), phi(dr/db)>; one is 0 (b null-homologous), Delta = the other, normalized
cand = db if da == 0 else da
alex_fox = sp.Poly(sp.expand(cand * (-1)), t)     # normalize sign -> t^2 - 3t + 1
print(f"   => Alexander polynomial Delta(t) = {alex_fox.as_expr()}   (Fox-derived, in-sandbox)")
# (ii) independent check: genus-1 Seifert matrix of 4_1, Delta = det(V - t V^T)
V = sp.Matrix([[-1, 1], [0, 1]])
alex_seifert = sp.expand((V - t*V.T).det())
print(f"   cross-check via Seifert matrix V=[[-1,1],[0,1]]: det(V - tV^T) = {alex_seifert}"
      f"  (= -Delta, agrees? {sp.simplify(alex_seifert + alex_fox.as_expr())==0})")
# roots of t^2 - 3t + 1 = phi^2 , phi^-2  -> Q(sqrt5), the HEARING/WEIGHTS field
alex_roots = sp.solve(t**2 - 3*t + 1, t)
print(f"\n   roots of Delta: {alex_roots}  = phi^2, phi^-2  -> Q(sqrt5) (the WEIGHTS/hearing field)")
print(f"   phi^2 = {sp.simplify(phi**2)} = (3+sqrt5)/2 ? {sp.simplify(phi**2-(3+sqrt(5))/2)==0}")
detK = abs(sp.Poly(t**2-3*t+1,t).eval(-1))
print(f"   determinant |Delta(-1)| = {detK}  (H1 of double branched cover = Z/5)")

# 4c. Cyclic branched-cover homology orders |H1(Sigma_n)| = prod_{j=1}^{n-1}|Delta(zeta_n^j)|
#     = |L_{2n} - 2| (Lucas) = (phi^n - phi^-n)^2 ; = 5 F_n^2 for n even, L_n^2 for n odd. ALL integers in Q.
print("\n   n-fold cyclic branched cover homology |H1(Sigma_n)| = prod_{j=1}^{n-1} |Delta(zeta_n^j)|:")
def lucas(n):
    a,b=2,1
    for _ in range(n): a,b=b,a+b
    return a
def fib(n):
    a,b=0,1
    for _ in range(n): a,b=b,a+b
    return a
for n in range(2,7):
    prod = 1.0
    for j in range(1,n):
        zj = complex(sp.N(sp.exp(2*sp.pi*I*j/n), 30))
        prod *= abs(zj**2 - 3*zj + 1)
    prod = round(prod)
    closed = lucas(2*n) - 2
    alt = f"5*F_{n}^2={5*fib(n)**2}" if n%2==0 else f"L_{n}^2={lucas(n)**2}"
    print(f"      n={n}: |H1| = {prod:>4}   = L_{2*n}-2 = {closed}  ({alt})   integer & rational? {prod==closed}")
print("   => the orders are rational INTEGERS in Q(sqrt5) (Alexander roots phi^2, phi^-2): sqrt5 = the")
print("      hearing, NATIVE. sqrt(2+phi)=2sin(2pi/5) NEVER appears -- no golden quantum dimension in the covers.")

# 4d. Where sqrt(2+phi) DOES appear: only at the level-5 (q=zeta5) evaluation = golden MTC / Fibonacci S.
print("\n   sqrt(2+phi) appears ONLY as the total quantum dimension D of the Fibonacci/SO(3)_3 MTC,")
print("   i.e. when the object's colored Jones is EVALUATED at q = zeta5 (level 5). Parallel to B728's")
print("   phase: an evaluation/level choice, not a bare invariant -> the base-rate trap, caught.")

print(); print(LINE); print("PART 5 -- BASE-RATE the D4 = Isom(4_1) hook"); print(LINE)
sg = M.symmetry_group()
print(f"   Isom(4_1) = m004 symmetry group (snappy): {sg}  order {sg.order()}")
print("   Arithmetic 'amplitude' D4 (if one insists on the F-symbol field): Gal closure of x^4-x^2-1,")
print("   acting on Q(sqrt phi, i) = {+-sqrt phi, +-i/sqrt phi}.  Field Q(sqrt phi, i).")
print("   Geometric D4 = Isom(m004): acts on the hyperbolic structure, trace field Q(sqrt-3).")
print("   Q(sqrt phi, i) vs Q(sqrt-3): DISJOINT (share only Q). NO genuine map identifies the two D4's.")
print("   AND the actual Born-amplitude field is C4 (Part 2), not D4 -- the hook never even applies to S.")
print("   => E20 base-rate trap: two abstract D4's, distinct fields/actions, NO identification. REJECT.")

print(); print(LINE); print("PART 6 -- FINAL BORN-CONTENT LEDGER + VERDICT"); print(LINE)
ledger = [
 ("FORM  |.|^2 conjugation-norm", "Q(sqrt-3)",        "C2 (quad)",  "FORCED-NATIVE", "hyperbolic trace field of 4_1 (tetra shape z^2-z+1)"),
 ("WEIGHTS non-uniform 1:phi^2", "Q(sqrt5)",          "C2 (quad)",  "FORCED-NATIVE", "Alexander roots phi^2,phi^-2 ; |H1(Sigma_n)|=5F_n^2"),
 ("AMPLITUDES S-entries 1/D,phi/D","Q(sqrt(2+phi))",  "C4 (real)",  "OVERLAY",       "D=2sin(2pi/5) = level-5 total quantum dim; not a bare invariant"),
 ("PHASE theta_tau=zeta5^2",      "Q(zeta5)",         "C4 (CM)",    "OVERLAY (B728)","golden-MTC twist; ruled out of resummation by C4 != C2xC2"),
]
print(f"{'sector':32s} {'field':16s} {'Galois':11s} {'status':15s} why")
print("-"*112)
for a,b,c,d,e in ledger:
    print(f"{a:32s} {b:16s} {c:11s} {d:15s} {e}")

print("\n   Note also (not a Born sector): F-symbol/associator field Q(sqrt phi) = D4 -- the ONLY D4;")
print("   it is what base-rate-traps against Isom(4_1)=D4, and the trap is rejected (Part 5).")
print("\n   Quantum-content home: compositum of the two quartic quantum sectors")
comp_q = minpoly(D + z5, x)
print(f"      Q(sqrt(2+phi)) . Q(zeta5)  has degree {sp.degree(comp_q,x)} over Q  = Q(zeta20)")
print(f"      contains sqrt5 (native seam)? {any(sp.degree(f,x)==1 for f,_ in sp.factor_list(x**2-5, extension=D+z5)[1])}"
      f"   contains sqrt-3 (being)? {any(sp.degree(f,x)==1 for f,_ in sp.factor_list(x**2+3, extension=D+z5)[1])}")
print("      => the quantum content lives in Q(zeta20) >= Q(sqrt5) but NOT >= Q(sqrt-3):")
print("         it meets the object ONLY along the hearing seam sqrt5, never along the being sqrt-3.")

print("\n" + "#"*78)
print("VERDICT: OUTCOME B -- the ledger completes cleanly.")
print("  Classical content (FORM+WEIGHTS = the two QUADRATIC fields Q(sqrt-3), Q(sqrt5)) is object-NATIVE.")
print("  Quantum content (AMPLITUDES Q(sqrt(2+phi)) C4  +  PHASE Q(zeta5) C4) are golden-MTC OVERLAYS:")
print("  degree-4 extensions the object's bare invariants do NOT force (not inside Q(sqrt-3,sqrt5);")
print("  sqrt(2+phi) appears only at the level-5 evaluation; the D4=Isom hook fails the base-rate).")
print("  Amplitude sector: OVERLAY, not forced-native. The pattern is NOT broken. Outcome B.")
print("#"*78)
