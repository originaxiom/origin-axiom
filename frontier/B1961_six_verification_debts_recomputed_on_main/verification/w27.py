# CLAIMS (SM seat W27, relay lines 617-636): three chiral 27s of E6 -> SM content; 18 SU(2) doublets;
# every gauge and mixed-grav anomaly sum zero; Witten parity ok; Dobrescu-Poppitz 6D SU(2) condition
# holds iff number of parity sectors is a multiple of 3. EXPECT: first parts hold; DP 'iff' holds only if
# each sector counts 4 doublets (one SM generation); with a full 27 (6 doublets) it is trivially satisfied.
import itertools
from fractions import Fraction as F
from collections import Counter
h=(1,1,-2)
def split(x,kind):
    c=sum(F(x[i])*h[i] for i in range(3)); t3=F(x[3]-x[4])/2; t3r=F(x[3]+x[4])/2
    bl=-F(2,3)*sum(x[:3]); Y=t3r+bl/2
    return c,t3,Y
states=[]
# 16-type spinor: choose parity giving quark doublets; 1/2 weights
for s in itertools.product([F(1,2),F(-1,2)],repeat=5):
    if sum(1 for v in s if v<0)%2==1: states.append(('16',s))
for i in range(5):
    for sg in (1,-1):
        x=[F(0)]*5; x[i]=F(sg); states.append(('10',tuple(x)))
states.append(('1',(F(0),)*5))
psi={'16':1,'10':-2,'1':4}
print("dim of 27 =",len(states))
# U(1)_psi E6xSO(10) anomalies
for p,name in ((3,'U1^3'),(1,'U1')):
    print(name,sum(psi[k]**p for k,_ in states))
# SM content
cont=Counter()
for k,x in states:
    c,t3,Y=split(x,k); cont[(k,c,t3,Y)]+=1
S3=S2Y=S3Y=Y3=Y1=0;nd=0;nm=0
for k,x in states:
    c,t3,Y=split(x,k)
    S3+=c**3; S3Y+=Y*c**2; S2Y+=Y*t3**2; Y3+=Y**3; Y1+=Y
    if t3==F(1,2): nd+=1
    if t3==F(-1,2): nm+=1
    # SU(3)^3 uses h with tr_fund h^3=-6 nonzero so sum is proportional to anomaly
print("per 27: SU3^3",S3,"SU3^2Y",S3Y,"SU2^2Y",S2Y,"Y^3",Y3,"grav Y",Y1,"doublets(T3=+1/2)",nd,"(T3=-1/2)",nm)
# sanity: quark doublet charge content: list SM multiplets
for k in ('16','10','1'):
    print(k,sorted(Counter((c,t3,Y) for kk,c,t3,Y in [(a,)+split(x,a) for a,x in states] if kk==k).items()))
# U(1)Y charges should include Q 1/6 (3x2), L -1/2, etc.
Yset=Counter(split(x,k)[2] for k,x in states); print("Y values (counts over states):",dict(Yset))
# three 27s
N=3
print("three 27s: doublets",N*nd,"SU3^3",N*S3,"SU3^2Y",N*S3Y,"SU2^2Y",N*S2Y,"Y^3",N*Y3,"grav",N*Y1)
print("Witten 4D: doublet count even?",(N*nd)%2==0, "per SM generation doublets (Q:3,L:1)=4")
# SM generation only (16) check anomalies too
g=[(k,x) for k,x in states if k=='16']
print("16 only: Y^3",sum(split(x,k)[2]**3 for k,x in g),"grav",sum(split(x,k)[2] for k,x in g),
 "SU2^2Y",sum(split(x,k)[2]*split(x,k)[1]**2 for k,x in g),"SU3^2Y",sum(split(x,k)[2]*split(x,k)[0]**2 for k,x in g),
 "SU3^3",sum(split(x,k)[0]**3 for k,x in g),"doublets",sum(1 for k,x in g if split(x,k)[1]==F(1,2)))
# DP condition as stated: N_doublets = 0 mod 6 (6D SU(2), pi_6(SU(2)) condition as quoted; not re-derived)
for per,name in ((4,'SM generation only (3Q+1L)'),(nd,'full 27')):
    print(name,"doublets per sector",per,"n with n*per%6==0 for n=1..12:",[n for n in range(1,13) if (n*per)%6==0])
