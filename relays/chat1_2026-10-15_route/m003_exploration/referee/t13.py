import sys; sys.path.insert(0,'.')
from ref3 import *
exec(open("s2.py").read().split("for w in")[0].replace("def word","def word2"))
mp.mp.dps = 30
S = {"up":(1,-4),"down":(1,2),"lep":(-3,6)}
def vecs(N,a,b,tau):
    out={}
    for nm,(qL,qR) in S.items():
        vu=(mp.mpf((qL+qR)*b)/N, mp.mpf((qL+qR)*a)/N); vd=(mp.mpf((qL-qR)*b)/N, mp.mpf((qL-qR)*a)/N)
        out[nm]=quat(tau,vu,vd)
    return out
def cmp(x,y):  # ratio x/y per channel (0..3), as (modulus, phase/pi)
    return [("0" if abs(y[s])<1e-25 and abs(x[s])<1e-25 else (f"{mp.nstr(abs(x[s]/y[s]),5)}@{mp.nstr(mp.arg(x[s]/y[s])/mp.pi,4)}" if abs(y[s])>1e-25 else "y=0")) for s in range(4)]
for tau in (mp.mpc(0.13,1.07), mp.mpc(-0.31,0.95)):
    print("tau",tau)
    for N,(a,b) in ((5,(1,3)),(5,(2,1)),(7,(1,4)),(7,(1,6)),(9,(1,3)),(11,(1,10))):
        v=vecs(N,a,b,tau)
        print(f"  N={N} ({a},{b}) [ch 1,i,j,k]  lep/down {cmp(v['lep'],v['down'])}\n{'':16s}lep/up {cmp(v['lep'],v['up'])}\n{'':16s}down/up {cmp(v['down'],v['up'])}")
for w in ("LLLLRRLRRR","LLRLRLRLRRLRLRLR"):
    A,B,C,D=word2(w); th,m,t=true_height(w,120)
    print(w,(A,B,C,D),"trace",t,"true height",round(th,3),"det(g-I)",(A-1)*(D-1)-B*C,"gcd",math.gcd(math.gcd(A-1,B),math.gcd(C,D-1)))
    for (a,b) in [(k%7,(4*k)%7) for k in range(1,7)]:
        ok=((a*D+b*B)-a)%7==0 and ((a*C+b*A)-b)%7==0; Q=C*a*a+(A-D)*a*b-B*b*b
        print("   line",(a,b),"fixed(+)",ok,"Q",Q,"N^2|Q",Q%49==0)
    if w=="LLLLRRLRRR": break
