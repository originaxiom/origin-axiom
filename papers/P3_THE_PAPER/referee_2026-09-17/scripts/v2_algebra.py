"""Referee check 2: Proposition 'metallic grammar', anomaly census, hypercharge forcing."""
from sympy import Matrix, Rational, factorint, pi, zeta, N as ev, symbols, expand, factor, binomial
import itertools, math

print("="*70); print("PROPOSITION (metallic grammars / SL(2,Z/N))"); print("="*70)
def sl2_order(n):
    if n==1: return 1
    r=n**3
    for p in factorint(n): r=r*(p*p-1)//(p*p)
    return r
for n in range(1,9): print(f"  |SL(2,Z/{n})| = {sl2_order(n)}")
print("  claim |SL(2,Z/4)|=48=|2O|:", sl2_order(4)==48)
# involutions in SL(2,Z/4)
inv=[]
for a,b,c,d in itertools.product(range(4),repeat=4):
    if (a*d-b*c)%4!=1: continue
    X=[[a,b],[c,d]]
    X2=[[(a*a+b*c)%4,(a*b+b*d)%4],[(c*a+d*c)%4,(c*b+d*d)%4]]
    if X2==[[1,0],[0,1]] and X!=[[1,0],[0,1]]: inv.append(X)
print("  elements of order 2 in SL(2,Z/4):", len(inv), "(paper says seven)")
# bound 6/pi^2 N^3 > 120 for N>=6
for n in [5,6,7]: print(f"  6/pi^2*{n}^3 = {6/math.pi**2*n**3:.2f}")
# Lambda(m)=m^2+4 ; tr(R^m L^m)=m^2+2 ; disc = m^2(m^2+4)
m=symbols('m')
for mm in range(1,8):
    Rm=Matrix([[1,0],[mm,1]]); Lm=Matrix([[1,mm],[0,1]])
    T=(Rm*Lm); tr=T.trace(); disc=tr**2-4*T.det()
    print(f"  m={mm}: tr(R^mL^m)={tr} (m^2+2={mm*mm+2}) disc={disc} (m^2(m^2+4)={mm*mm*(mm*mm+4)}) Lambda={mm*mm+4}")
print("  m^2+4=3 solutions:", [k for k in range(1,50) if k*k+4==3], "; m^2+4=5:", [k for k in range(1,50) if k*k+4==5])
print("  field-conductor counterexample m=4,11,29 -> squarefree part of disc:")
for mm in [4,11,29]:
    d=mm*mm*(mm*mm+4); sq=1
    for p,e in factorint(d).items():
        if e%2: sq*=p
    print(f"    m={mm}: disc={d}, Q(sqrt{sq})")

print(); print("="*70); print("ANOMALY CONTENT CENSUS (252 / 222 / 2)"); print("="*70)
# six SM-visible types under SU(3)xSU(2): (3,2),(3b,2),(3,1),(3b,1),(1,2),(1,1)
# [SU(3)]^3 charges +2,-2,+1,-1,0,0  (as the paper states)
types=[('(3,2)',2),('(3b,2)',-2),('(3,1)',1),('(3b,1)',-1),('(1,2)',0),('(1,1)',0)]
cands=list(itertools.combinations_with_replacement(range(6),5))
print("  candidates C(10,5) =", len(cands), "== binomial:", binomial(10,5))
killed=[c for c in cands if sum(types[i][1] for i in c)!=0]
print("  killed by the pure colour cubic alone:", len(killed), "-> survivors:", len(cands)-len(killed))

print(); print("="*70); print("HYPERCHARGE FORCING (three linear conditions, then the cubic)"); print("="*70)
Yq,Yu,Yd,Yl,Ye,t=symbols('Yq Yu Yd Yl Ye t')
# all-left-handed convention, one generation: q(3,2)x1, u^c(3b,1), d^c(3b,1), l(1,2), e^c(1,1)
lin1=2*Yq+Yu+Yd            # [SU(3)]^2 Y
lin2=3*Yq+Yl               # [SU(2)]^2 Y
lin3=6*Yq+3*Yu+3*Yd+2*Yl+Ye  # grav^2 Y
sol={Yl:-3*Yq, Ye:6*Yq}
print("  [SU(3)]^2Y=0 -> Yu+Yd = -2Yq :", expand(lin1.subs(Yq,1))," (Yu+Yd=-2)")
print("  [SU(2)]^2Y=0 -> Yl = -3Yq   :", expand(lin2.subs({Yq:1,Yl:-3})) == 0)
print("  grav^2Y=0 with Yq=1,Yu+Yd=-2,Yl=-3 -> Ye =", 
      [v for v in [6] if expand(lin3.subs({Yq:1,Yu:-1+t,Yd:-1-t,Yl:-3,Ye:v}))==0])
cub=6*1**3+3*(-1+t)**3+3*(-1-t)**3+2*(-3)**3+6**3
print("  cubic [Y]^3 on the line =", factor(expand(cub)), " (paper: -18(t-3)(t+3))")
for tv in (3,-3):
    v=(1,(-1+tv),(-1-tv),-3,6)
    print(f"   t={tv:+d}: (Yq,Yu,Yd,Yl,Ye)={v}")
print("  SM hypercharges x6: q,u^c,d^c,l,e^c =", [Rational(x)*6 for x in (Rational(1,6),Rational(-2,3),Rational(1,3),Rational(-1,2),1)])

print(); print("="*70); print("sin^2(theta_W)=3/8 TRACES on one generation, Q=T3+Y"); print("="*70)
# 16 of SO(10) = q(6 states: 3 colours x 2), u^c(3), d^c(3), l(2), e^c(1), nu^c(1)
# T3 values; Y = Q - T3 with Y = half conventional hypercharge  => Y(q)=1/6? paper: Y half conventional
# use Y_conv/2: q:1/12? Let's instead use the definition Q=T3+Y directly with SM charges.
gen=[]  # (multiplicity, T3, Q)
gen+=[(3, Rational(1,2), Rational(2,3)), (3, Rational(-1,2), Rational(-1,3))]   # quark doublet
gen+=[(3, 0, Rational(-2,3)), (3, 0, Rational(1,3))]                            # u^c, d^c
gen+=[(1, Rational(1,2), 0), (1, Rational(-1,2), -1)]                           # lepton doublet
gen+=[(1, 0, 1), (1, 0, 0)]                                                     # e^c, nu^c
trT3sq=sum(m*T3**2 for m,T3,Q in gen); trYsq=sum(m*(Q-T3)**2 for m,T3,Q in gen); trT3Y=sum(m*T3*(Q-T3) for m,T3,Q in gen)
print(f"  over the 16: Tr(T3^2)={trT3sq}, Tr(Y^2)={trYsq}, Tr(T3Y)={trT3Y}, ratio={trT3sq/(trT3sq+trYsq)}")
print("  paper quotes Tr(T3^2)=3, Tr(Y^2)=5, Tr(T3Y)=0 on the 27 -> 3/8 =", Rational(3,8))

print(); print("="*70); print("E8 / E6 branching and 27x27"); print("="*70)
print("  248 = 78 + 8 + (27,3) + (27b,3b):", 78+8+27*3+27*3)
print("  27x27 = 351' + 351 + 27bar :", 351+351+27, "= 27^2 =", 27*27, "; sym part", 351+27, "= C(28,2)=", 27*28//2)
print("  adjoint 78 in 27x27? ", "no (78 not among {351',351,27bar})")
print("  A2+A1 Levi of E6: dim 8+3+3 =", 8+3+3, " rank", 2+1+3)
print("  c((E6)_1) = 78/(1+12) =", Rational(78,13))

print(); print("="*70); print("H_1 of cyclic branched covers Y_n of the figure-eight"); print("="*70)
import cmath
def order_H1(n):
    p=1.0
    for j in range(1,n):
        z=cmath.exp(2j*cmath.pi*j/n); p*=abs(z*z-3*z+1)
    return p
for n in [2,3,4,5,9,12]: print(f"  n={n}: |H_1(Y_n)| = {order_H1(n):.4f}")
print("  paper: H_1(Y_3) = (Z/4)^2, order 16")

print(); print("="*70); print("finite-order A in GL(2,Z): |det(A-I)| values"); print("="*70)
vals=set()
for a,b,c,d in itertools.product(range(-3,4),repeat=4):
    X=Matrix([[a,b],[c,d]])
    if abs(X.det())!=1: continue
    Y=X; ok=False
    for k in range(1,13):
        if Y==Matrix([[1,0],[0,1]]) and k>1: ok=True; break
        Y=Y*X
    if ok and X.det()==1: vals.add(abs((X-Matrix([[1,0],[0,1]])).det()))
print("  orientation-preserving finite order: |det(A-I)| in", sorted(vals), "(paper: {0,1,2,3,4})")
