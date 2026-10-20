import numpy as np, itertools
from fractions import Fraction as Fr
from collections import Counter
exec(open("v1.py").read().split("# ---- 1.")[0])
ML,MR=W.ML,W.MR; TB=cp.TB
TL=cp.restrict(ML,TB); TR=cp.restrict(MR,TB)
D=TL@inv(TR)@TL
print("Delta^4 on T:",np.round(np.linalg.matrix_power(D,4),6).real.diagonal(), "is -I:",np.allclose(np.linalg.matrix_power(D,4),-np.eye(3)))
Pa=np.diag([W.chi(p,"a") for p in W.PAR for _ in range(2)]).astype(complex); Pb=np.diag([W.chi(p,"b") for p in W.PAR for _ in range(2)]).astype(complex)
Pa3,Pb3=cp.restrict(Pa,TB),cp.restrict(Pb,TB)
comm=Pa3@inv(Pb3)@inv(Pa3)@Pb3
print("[Pa,Pb^-1]-type commutators on T: Pa Pb^-1 Pa^-1 Pb =",np.allclose(comm,np.eye(3)),"; Pa,Pb on T:",np.round(np.diag(Pa3),3).real if np.allclose(Pa3,np.diag(np.diag(Pa3))) else "nondiag")
print("Pa,Pb commute:",np.allclose(Pa@Pb,Pb@Pa))
# chi_eta^3 of Delta^4: B3 abelianisation. Delta = L R^-1 L : 3 letters, L->+1, R^-1 -> +1 (R=sigma2^-1)
zeta=lambda k: np.exp(2j*np.pi*k/24)
# eta multiplier on T-generator: e^{2 pi i/24}; chi_eta^3(Delta)=zeta(3*3)=?  Delta has abelianisation degree 3 -> chi(Delta^4)=zeta(3*12)
print("chi_eta^3(Delta^4)=",np.round(zeta(3*12),6))
print("chi_eta^k(Delta^4) for k=1..6:",[np.round(zeta(k*12),3).real for k in range(1,7)])
# twisted T0
TL0=np.exp(3j*np.pi/12)*TL; TR0=np.exp(-3j*np.pi/12)*TR
D0=TL0@inv(TR0)@TL0
print("T0 Delta^4=I:",np.allclose(np.linalg.matrix_power(D0,4),np.eye(3)),"det L0,R0",np.round(np.linalg.det(TL0),6),np.round(np.linalg.det(TR0),6))
def order(gens,maxn=500):
    G=[np.eye(3,dtype=complex)];q=[G[0]];keys={tuple(np.round(G[0],5).flatten())}
    while q:
        c=q.pop()
        for g in gens:
            n=c@g;k=tuple(np.round(n,5).flatten()+0)
            if k not in keys: keys.add(k);G.append(n);q.append(n)
            if len(G)>maxn: return G
    return G
print("order <T0_L,T0_R>:",len(order([TL0,TR0])),"order <TL,TR>:",len(order([TL,TR])))
print("order of group <T0_L,T0_R,Pa,Pb>:",len(order([TL0,TR0,Pa3,Pb3])))
# which eta-power k also kills the obstruction and gives octahedral? any odd k
for k in range(0,24):
    a=np.exp(2j*np.pi*k/24)
    A=a*TL; B=TR/a
    ok=np.allclose(np.linalg.matrix_power(A@inv(B)@A,4),np.eye(3))
    G=order([A,B,Pa3,Pb3],3000)
    print(k,"Delta4=I",ok,"order",len(G)) if ok else None
# ---------- E8 / hypercharge
y=[Fr(1,6)]*3+[Fr(-1,2),Fr(1,2),Fr(-1,2)]
print("trace Y",sum(y))
# E6 -> SU6 x SU2 : 27=(15bar?,1)+(6,2): compute both
c15=Counter(y[i]+y[j] for i,j in itertools.combinations(range(6),2))
c6x2=Counter(yi for yi in y for _ in range(2))
c15b=Counter(-k for k in c15.elements()); c6b=Counter(-k for k in c6x2.elements())
print("27 = (15,1)+(6b,2)  Y:",dict(sorted(Counter(list(c15.elements())+list(c6b.elements())).items())))
print("27 = (15b,1)+(6,2)  Y:",dict(sorted(Counter(list(c15b.elements())+list(c6x2.elements())).items())))
# SM 27 content (SO(10): 16+10+1, E6 normalisation): Y multiset of SM 16 (left-handed fields) : Q(1/6)x6,u^c(-2/3)x3,d^c(1/3)x3,L(-1/2)x2,e^c(1)x1,nu^c(0)x1
sm16=Counter({Fr(1,6):6,Fr(-2,3):3,Fr(1,3):3,Fr(-1,2):2,Fr(1):1,Fr(0):1})
for name,c in [("A",Counter(list(c15.elements())+list(c6b.elements()))),("B",Counter(list(c15b.elements())+list(c6x2.elements())))]:
    print(name,"contains SM16 multiset:",all(c[k]>=v for k,v in sm16.items()))
# mixed: does 'Q_L = y_6[0]' reading make sense: weights of 6 are individual y_i
print("tr over 27 of Y (A):",sum(k*v for k,v in Counter(list(c15.elements())+list(c6b.elements())).items()))
# E8 branching dims
print("dim check SU6xSU2xSU3:",35+3+8+6*2*3*2+15*3*2+20*2)
print("dim check E6xSU3:",78+8+27*3*2)
# central element trivial?
import cmath
z6=cmath.exp(1j*np.pi/3); w3=cmath.exp(2j*np.pi/3)
g=(z6,-1,w3)
reps={"(6,2,3)":(1,1,1),"(6b,2,3b)":(-1,1,-1),"(15,1,3b)":(2,0,-1),"(15b,1,3)":(-2,0,1),"(20,2,1)":(3,1,0)}
print("generator of Z6 acts:",{k:np.round(z6**a*(-1)**b*w3**c,6) for k,(a,b,c) in reps.items()})
print("c=g^3 =",(z6**3,(-1)**3,w3**3))
