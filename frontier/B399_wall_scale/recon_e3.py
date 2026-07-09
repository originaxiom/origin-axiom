import json, math, sys, os
from fractions import Fraction as F
sys.path.insert(0, os.path.join("..","B391_existence_general"))
from census_big import primitive_root
files=["singles_1215.json","singles_1215_p3.json","singles_1215_p456.json","singles_1215_p7_10.json"]
DATA={}
for f in files:
    try: DATA.update(json.load(open(f)))
    except: pass
primes=sorted(map(int,DATA))
def s5(p):
    g=primitive_root(p); z=pow(g,(p-1)//5,p)
    return (z-pow(z,2,p)-pow(z,3,p)+pow(z,4,p))%p
def e3v(p):
    v=[int(DATA[str(p)][str(c)]) for c in (121,256,391)]; return (v[0]*v[1]*v[2])%p
M=1
for p in primes: M*=p
def crt(vals):
    r=0
    for v,p in zip(vals,primes): Mi=M//p; r=(r+v*Mi*pow(Mi,-1,p))%M
    return r
S=crt([s5(p) for p in primes]); R=crt([e3v(p) for p in primes])
def dot(u,v): return sum(x*y for x,y in zip(u,v))
def lll(b):
    n=len(b); B=[[F(x) for x in r] for r in b]
    Bs=[None]*n; mu=[[F(0)]*n for _ in range(n)]; Bn=[F(0)]*n
    def gso():
        for i in range(n):
            Bs[i]=[F(x) for x in B[i]]
            for j in range(i):
                mu[i][j]=(sum(B[i][k]*Bs[j][k] for k in range(3))/Bn[j]) if Bn[j]!=0 else F(0)
                Bs[i]=[Bs[i][k]-mu[i][j]*Bs[j][k] for k in range(3)]
            Bn[i]=sum(x*x for x in Bs[i])
    gso(); k=1
    while k<n:
        for j in range(k-1,-1,-1):
            if abs(mu[k][j])>F(1,2):
                q=round(mu[k][j]); B[k]=[B[k][t]-q*B[j][t] for t in range(3)]; gso()
        if Bn[k]>=(F(3,4)-mu[k][k-1]**2)*Bn[k-1]: k+=1
        else: B[k],B[k-1]=B[k-1],B[k]; gso(); k=max(k-1,1)
    return [[int(x) for x in r] for r in B]
red=lll([[M,0,0],[S%M,1,0],[(-R)%M,0,1]])
best=None
for A,Bc,D in red:
    if D==0: continue
    if D<0: A,Bc,D=-A,-Bc,-D
    n2=A*A+Bc*Bc+D*D
    if best is None or n2<best[0]: best=(n2,F(A,D),F(Bc,D))
_,a,b=best
p=primes[0]
lhs=(int(a.numerator)*pow(int(a.denominator),p-2,p)+int(b.numerator)*pow(int(b.denominator),p-2,p)*s5(p))%p
ok=(lhs==e3v(p))
norm=a*a-5*b*b
def pf(n):
    s=set();n=abs(int(n));d=2
    while d*d<=n:
        while n%d==0:s.add(d);n//=d
        d+=1
    if n>1:s.add(n)
    return s
prs=set()
for x in (a,b,norm):
    if x: prs|=pf(x.numerator)|pf(x.denominator)
prs|={2,3}
print("e3 =",a,"+",b,"*sqrt5   verify:",ok)
print("Norm =",norm,"  primes:",sorted(prs))
json.dump(dict(e1="0",e2="-1/48",e3_a=str(a),e3_b=str(b),norm=str(norm),verify=ok,primes=sorted(prs)),
          open("triple_e3.json","w"),indent=1)
print("DONE")
