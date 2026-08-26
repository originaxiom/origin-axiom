#!/usr/bin/env python3
"""MEMO-60 CELL: ONE QUADRATIC, TWO ENDS — on the character variety the
conserved pair (kappa, tr(ab^-1)) satisfies a single monic quadratic with
trace x^2 - 1; the hyperbolic end specializes it to the Eisenstein integral
X^2 - 3X + 3 (norm 3 ramified, disc -3) and the spherical end to the golden
unit X^2 + X - 1 (norm -1 unit, disc 5): memo 49's two arithmetic ends are
the two specializations of ONE polynomial family, and B981/B248's curvature
axis carries it.

Builds on memo 54 (the component relation P(x,z) = z^2 - x^2 z + 2x^2 - z - 1
and the identity kappa + tr(ab^-1) = x^2 - 1 on P = 0, both re-derived
in-run) and closes the flagged hook connecting memo 49 to the corpus's
cone-angle family (B248/B981: hyperbolic end at meridian trace x = 2,
spherical 2I end at x = 0 with tr(ab) = phi).

PREREGISTERED (two-outcome; every claim an assert):
  FACT 1 (re-derivation): P(x,z) from the relator (gcd extraction anchored
    at s=1 to the Riley t^2-t+1, exactly as memo 54).
  FACT 2 (the family): on P = 0, kappa + tr(ab^-1) = x^2 - 1 exactly, and
    the product G(x) = kappa * tr(ab^-1) mod P is a POLYNOMIAL in x alone
    — computed; so the pair satisfies X^2 - (x^2-1) X + G(x) = 0.
    Discriminant D(x) = (x^2-1)^2 - 4 G(x): computed and factored.
  FACT 3 (hyperbolic end, x = 2): the quadratic is X^2 - 3X + 3 — trace 3,
    norm 3 (ramified), disc -3 (memos 41/49 re-anchored).
  FACT 4 (spherical end, x = 0, from scratch): the relator factor at s = i
    is t^2 - 5t + 5, whose roots give z = phi or 1/phi' — the FULL relator
    is verified = I exactly over Q(sqrt5, i) at s=i, t=(5+sqrt5)/2, and
    P(0, phi) = 0 (the 2I end lies on the same nonabelian component).
    There the quadratic is X^2 + X - 1 — trace -1, norm -1 (a UNIT),
    disc 5 — with kappa = phi - 1 and tr(ab^-1) = -phi its two roots.
  FACT 5 (the flow): D(2) = -3 and D(0) = 5: the discriminant of the one
    conserved-pair quadratic flows from the Eisenstein end to the golden
    end along the meridian-trace axis — the exact seed of the curvature-
    sign crossover (INTERPRETIVE reading fenced in the memo).
"""
import sympy as sp

s,t,x,z,X = sp.symbols('s t x z X')
A=sp.Matrix([[s,1],[0,1/s]]); B=sp.Matrix([[s,0],[t,1/s]])
mats={'a':A,'b':B,'A':A.inv(),'B':B.inv()}
R=sp.eye(2)
for ch in 'abABaBAbaB': R=R*mats[ch]
R=sp.simplify(R)
nums=[sp.factor(sp.numer(sp.together(R[i,j]-(1 if i==j else 0)))) for i in range(2) for j in range(2)]
G0=nums[0]
for nm in nums[1:]: G0=sp.gcd(G0,nm)
cand=None
for (f,m) in sp.factor_list(G0)[1]:
    if t in f.free_symbols and sp.degree(sp.Poly(f,t))>=2: cand=f
Riley=sp.expand(cand)
assert sp.expand(Riley.subs(s,1)-(t**2-t+1))==0
# P(x,z) via symmetric-function fit (memo 54's method)
samples=[]
for sv in (2,3,sp.Rational(5,2),sp.Rational(7,3),4,sp.Rational(9,4),5,sp.Rational(11,5),sp.Rational(7,2),sp.Rational(8,3)):
    xv=sp.Rational(sv)+1/sp.Rational(sv)
    pol=sp.Poly(Riley.subs(s,sp.Rational(sv)),t)
    c2,c1,c0=pol.all_coeffs()
    tsum=-sp.Rational(c1)/c2; tprod=sp.Rational(c0)/c2
    e1=2*(xv**2-2)+tsum
    e2=(xv**2-2)**2+(xv**2-2)*tsum+tprod
    samples.append((xv,sp.nsimplify(e1),sp.nsimplify(e2)))
def fitpoly(pts,deg):
    Am=sp.Matrix([[pt[0]**k for k in range(deg+1)] for pt in pts[:deg+1]])
    bv=sp.Matrix([pt[1] for pt in pts[:deg+1]])
    co=Am.solve(bv)
    poly=sum(co[k]*x**k for k in range(deg+1))
    for pt in pts: assert sp.simplify(poly.subs(x,pt[0])-pt[1])==0
    return sp.expand(poly)
e1x=fitpoly([(a_,b_) for (a_,b_,c_) in samples],2)
e2x=fitpoly([(a_,c_) for (a_,b_,c_) in samples],4)
P=sp.expand(z**2 - e1x*z + e2x)
print("FACT 1: P(x,z) =",P)
assert sp.expand(P-(z**2-x**2*z+2*x**2-z-1))==0

# FACT 2: the conserved-pair quadratic
kap=sp.expand(2*x**2+z**2-x**2*z-2)     # tr[a,b] with x=y (Fricke)
tab=sp.expand(x**2-z)                   # tr(ab^-1)
ssum=sp.rem(sp.expand(kap+tab), P, z)
print("FACT 2: kappa + tr(ab^-1) mod P =",sp.expand(ssum))
assert sp.expand(ssum-(x**2-1))==0
Gx=sp.rem(sp.expand(kap*tab), P, z)
Gx=sp.expand(Gx)
print("        G(x) = kappa * tr(ab^-1) mod P =",Gx,"  (z-free:",z not in Gx.free_symbols,")")
assert z not in Gx.free_symbols
D=sp.expand((x**2-1)**2-4*Gx)
print("        conserved-pair quadratic: X^2 - (x^2-1) X + G(x);  disc D(x) =",sp.factor(D))

# FACT 3: hyperbolic end
q3=sp.expand((X**2-(x**2-1)*X+Gx).subs(x,2))
print("FACT 3: at x=2 (hyperbolic/Riley):",q3," disc",D.subs(x,2))
assert sp.expand(q3-(X**2-3*X+3))==0 and D.subs(x,2)==-3

# FACT 4: spherical end from scratch
phi_i=sp.expand(Riley.subs(s,sp.I))
polt=sp.Poly(phi_i,t)
c=polt.all_coeffs()
mon=sp.expand(phi_i/c[0])
print("FACT 4: relator factor at s=i:",mon)
assert sp.expand(mon-(t**2-5*t+5))==0
tv=(5+sp.sqrt(5))/2
zv=sp.simplify((sp.I+1/sp.I)**2-2+tv)   # z = x^2 - 2 + t with x = s+1/s = 0
phi=(1+sp.sqrt(5))/2
assert sp.simplify(zv-phi)==0
# full relator at s=i, t=tv over Q(sqrt5, i)
Av=A.subs(s,sp.I); Bv=B.subs([(s,sp.I),(t,tv)])
m2={'a':Av,'b':Bv,'A':Av.inv(),'B':Bv.inv()}
Rv=sp.eye(2)
for ch in 'abABaBAbaB': Rv=sp.simplify(sp.expand(Rv*m2[ch]))
assert sp.simplify(Rv-sp.eye(2))==sp.zeros(2)
print("        FULL relator = I verified exactly at s=i, t=(5+sqrt5)/2; z = phi")
assert sp.simplify(P.subs([(x,0),(z,phi)]))==0
q0=sp.expand((X**2-(x**2-1)*X+Gx).subs(x,0))
print("        at x=0 (spherical/2I):",q0," disc",D.subs(x,0))
assert sp.expand(q0-(X**2+X-1))==0 and D.subs(x,0)==5
kv=sp.simplify(kap.subs([(x,0),(z,phi)])); tv2=sp.simplify(tab.subs([(x,0),(z,phi)]))
print(f"        kappa = {sp.simplify(kv)} = phi-1;  tr(ab^-1) = {sp.simplify(tv2)} = -phi")
assert sp.simplify(kv-(phi-1))==0 and sp.simplify(tv2+phi)==0
assert sp.simplify(kv*tv2+1)==0   # norm -1: a unit
print("        the pair are the two roots of X^2+X-1: norm -1, a UNIT")

# COROLLARY (found in-run): trace = norm = x^2-1 on the whole component, so
#   kappa * tr(ab^-1) = kappa + tr(ab^-1)  <=>  (kappa-1)(tr(ab^-1)-1) = 1:
# the SHIFTED conserved pair are mutually inverse units, and at the Riley
# point kappa-1 = q is the field generator itself (q(1-q) = 1 in Q(q)).
assert sp.expand(Gx-(x**2-1))==0
shift=sp.rem(sp.expand((kap-1)*(tab-1)-1), P, z)
print("COROLLARY: (kappa-1)(tr(ab^-1)-1) - 1 mod P =",sp.expand(shift))
assert sp.expand(shift)==0
assert sp.simplify((kv-1)*(tv2-1)-1)==0   # spherical end check
print("   the shifted pair are mutually inverse UNITS on the whole component;")
print("   at the Riley point kappa-1 = q (the field generator), inverse 1-q")

print(f"""
ONE QUADRATIC, TWO ENDS: on the nonabelian component the conserved pair
(kappa, tr(ab^-1)) satisfies the single monic quadratic
    X^2 - (x^2-1) X + G(x),   G(x) = {Gx},   D(x) = {sp.factor(D)}
whose hyperbolic specialization (x=2) is the Eisenstein integral X^2-3X+3
(norm 3 = the ramified prime, disc -3) and whose spherical specialization
(x=0, the 2I end, relator verified from scratch) is the golden unit
X^2+X-1 (norm -1, disc 5).  Memo 49's two arithmetic ends are one
polynomial family read at the two ends of the meridian-trace axis —
the exact seed under B981/B248's curvature crossover.  The curvature
reading is INTERPRETIVE and fenced; every displayed identity is computed.
Gate 5 untouched.""")
