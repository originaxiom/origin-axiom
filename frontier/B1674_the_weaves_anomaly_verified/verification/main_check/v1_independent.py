"""Independent verification of W101 claims (own code; does not import the lane's script)."""
import itertools, mpmath as mp, numpy as np
mp.mp.dps = 30
out = {}
def eta(t): return mp.exp(2j*mp.pi*t/24)*mp.qp(mp.exp(2j*mp.pi*t))
def th2sq_bf(t): return (2*mp.nsum(lambda n: mp.exp(1j*mp.pi*t*(n+mp.mpf(1)/2)**2),[0,mp.inf]))**2
def th3sq(t): return mp.jtheta(3,0,mp.exp(1j*mp.pi*t))**2
def th4sq(t): return mp.jtheta(4,0,mp.exp(1j*mp.pi*t))**2
def f(t): return mp.matrix([th2sq_bf(t),th3sq(t),th4sq(t)])
# (a) derive rho_u from the thetas: f(t+1)=A f, f(-1/t)= t B f  (solve by 3 generic points)
pts=[mp.mpc(0.13,1.1),mp.mpc(-0.21,0.9),mp.mpc(0.31,1.4)]
F=mp.matrix(3,3)
for j,t in enumerate(pts):
    for i in range(3): F[i,j]=f(t)[i]
A=mp.matrix(3,3);B=mp.matrix(3,3)
G1=mp.matrix(3,3);G2=mp.matrix(3,3)
for j,t in enumerate(pts):
    for i in range(3):
        G1[i,j]=f(t+1)[i]; G2[i,j]=f(-1/t)[i]/t
A=G1*F**-1; B=G2*F**-1
An=np.array(A.tolist(),dtype=complex); Bn=np.array(B.tolist(),dtype=complex)
print("A_u (T on theta^2 triplet) =\n",np.round(An,10)); print("B_u (S) =\n",np.round(Bn,10))
# eta multipliers: eta(t+1)=e^{2pi i/24} eta, eta(-1/t)=sqrt(-it) eta -> chi_s=e^{-i pi/4} w/ weight 1/2 (sqrt t convention)
cT=np.exp(2j*np.pi/24); cS=np.exp(-1j*np.pi/4)
rT=cT**21*An; rS=cS**21*Bn
print("T exponents (turns):",sorted(round(float(x)*24)/24 % 1 for x in (np.angle(np.linalg.eigvals(rT))/(2*np.pi))%1))
print("det rho(t)/chi(t)^9 =",np.linalg.det(rT)/cT**9, " det rho(s)/chi(s)^9 =",np.linalg.det(rS)/cS**9)
print("which e mod 24 for t:",[k for k in range(24) if abs(np.linalg.det(rT)-cT**k)<1e-9],"for s (e mod 8 since chi_s order 8):",[k for k in range(24) if abs(np.linalg.det(rS)-cS**k)<1e-9])
st=rS@rT
print("s^2=(st)^3",np.allclose(rS@rS,np.linalg.matrix_power(st,3)),"s^4=-1",np.allclose(np.linalg.matrix_power(rS,4),-np.eye(3)),"s^8=1",np.allclose(np.linalg.matrix_power(rS,8),np.eye(3)))
seen={(tuple(np.round(np.eye(3),6).ravel())):np.eye(3,dtype=complex)};fr=[np.eye(3,dtype=complex)]
while fr:
    nx=[]
    for g in fr:
        for h in (rT,rS):
            x=g@h;k=tuple(np.round(x,6).ravel())
            if k not in seen: seen[k]=x;nx.append(x)
    fr=nx
print("image order",len(seen))
# determinant is a character of the group: check on random words det(word)=chi^9 evaluated multiplicatively
import random
random.seed(1)
okc=True
for _ in range(200):
    w=[random.choice("ts") for _ in range(random.randint(1,12))]
    M=np.eye(3,dtype=complex);c=1
    for ch in w:
        M=M@(rT if ch=="t" else rS); c*= (cT if ch=="t" else cS)**9
    okc&=abs(np.linalg.det(M)-c)<1e-9
print("det rho(word)=chi_eta^9 on 200 random words:",okc)

# (b) anomaly table
F6=["Q","u","d","L","e","nu"]
Wt={"SU3":dict(Q=2,u=1,d=1),"SU2":dict(Q=3,L=1),"grav":dict(Q=6,u=3,d=3,L=2,e=1,nu=1)}
asg=[dict(zip(F6,v)) for v in itertools.product((1,-1),repeat=6)]
n=lambda G,s:(9*sum(w*s[f_] for f_,w in Wt[G].items()))%24
su3=[s for s in asg if n("SU3",s)==0]
print("SU3 free:",len(su3), all(s["u"]==s["d"]==-s["Q"] for s in su3), len([s for s in asg if s["u"]==s["d"]==-s["Q"]]))
print("SU2 values:",sorted({n("SU2",s) for s in asg}))
gf=[s for s in su3 if n("grav",s)==0]
print("grav free | SU3 free:",len(gf),all(s["e"]==s["nu"]==-s["L"] for s in gf),len([s for s in su3 if s["e"]==s["nu"]==-s["L"]]))
# without nu^c: drop nu term
nn=lambda s:(9*sum(w*s[f_] for f_,w in Wt["grav"].items() if f_!="nu"))%24
print("grav free without nu^c (over all 32 assignments of 5 fields, and over SU3-free ones):",
  sum(1 for v in itertools.product((1,-1),repeat=5) if nn(dict(zip(F6[:5],v),nu=0))==0),
  sum(1 for s in su3 if nn(s)==0))
# SU3-free values for reference and distribution of SU3 values
from collections import Counter
print("SU3 values:",Counter(n("SU3",s) for s in asg))
print("grav values given SU3 free:",Counter(n("grav",s) for s in su3))
# (c) determinant conditions
res=[]
for sQ,su,sd in itertools.product((1,-1),repeat=3):
    m=(-9*(2*sQ+su+sd))%24
    Ks=[K for K in range(0,15) if (m-6*K)%24==0]
    res.append(((sQ,su,sd),m,sorted({K%4 for K in Ks})))
print("m and K mod 4:",res)
# det Y1 = 2 th2^2 th3^2 th4^2 = 8 eta^6
for t in [mp.mpc(0.137,1.291),mp.mpc(-0.3,0.8),mp.mpc(0.5,2.0)]:
    Y=mp.matrix([[0,th4sq(t),th3sq(t)],[th4sq(t),0,th2sq_bf(t)],[th3sq(t),th2sq_bf(t),0]])
    print("detY1/(8 eta^6)-1:",mp.nstr(mp.det(Y)/(8*eta(t)**6)-1,3), " vs 2*prod:",mp.nstr(mp.det(Y)-2*th2sq_bf(t)*th3sq(t)*th4sq(t),3))
# arg eta
for y in [0.9,1.2,2.5]:
    t=mp.mpc(0.5,y);v=(-12*mp.arg(eta(t)))
    print("x=1/2 y=",y," -12 arg eta mod pi - pi/2:",mp.nstr(((v-mp.pi/2+mp.pi/2)%mp.pi)-mp.pi/2,3))
for x,y in [(0.2,1.5),(0.3,2.0),(0.1,3.0),(0.4,1.0)]:
    t=mp.mpc(x,y);d=-12*mp.arg(eta(t))+mp.pi*x
    print("x,y",x,y," -12 argeta + pi x =",mp.nstr(d,4)," e^{-2 pi y}=",mp.nstr(mp.exp(-2*mp.pi*y),4))
# E6, zero curve (own series)
def E6(t):
    q=mp.exp(2j*mp.pi*t); return 1-504*mp.nsum(lambda n: n**5*q**n/(1-q**n),[1,mp.inf])
def E4(t):
    q=mp.exp(2j*mp.pi*t); return 1+240*mp.nsum(lambda n: n**3*q**n/(1-q**n),[1,mp.inf])
P=lambda x,y: 12*mp.arg(eta(mp.mpc(x,y)))+2*mp.arg(E6(mp.mpc(x,y)))
def root(y):
    xs=[mp.mpf(k)/200 for k in range(10,101)]
    out=[]
    for a,b in zip(xs,xs[1:]):
        if mp.sin(P(a,y))*mp.sin(P(b,y))<0:
            out.append(mp.findroot(lambda x: mp.sin(P(x,y)),(a,b),solver='anderson'))
    return out
for y in [1.0,1.05,1.1,1.15,1.2,1.3,1.5,2.0]:
    print("zero(s) of sin(12 arg eta+2 arg E6) with 0.05<=x<=0.5 at y=",y,[mp.nstr(r,8) for r in root(mp.mpf(y))], " |tau| =",[mp.nstr(abs(mp.mpc(r,y)),5) for r in root(mp.mpf(y))])
# counterterm: g
for t in [mp.mpc(0.137,1.291),mp.mpc(-0.33,1.02)]:
    j=1728*E4(t)**3/(E4(t)**3-E6(t)**2)
    print("det/eta^6 vs E6 weight3:  (eta^6E6)^2/eta^36 / E6^2*eta^24... ratio g/(j-1728) with g=E6^2/Delta*(norm):", mp.nstr(E6(t)**2/ (( (E4(t)**3-E6(t)**2)/1728 )) /(j-1728),8))
# C1 independent
w24=lambda k: np.exp(2j*np.pi*k/24)
T2=np.array([[1,1],[0,1]]);S2=np.array([[0,-1],[1,0]]);
GEN={"t":(T2,rT),"s":(S2,rS)}
def wd(w):
    M=np.eye(2);P_=np.eye(3,dtype=complex)
    for ch in w: a,b=GEN[ch]; M=M@a;P_=P_@b
    return M,P_
words=["t","s","ts","st","tst","sts","ttst","stss","tsttsts","sttstts","tttttsttts","stststst"]
bad=0
for w in words:
    M,P_=wd(w); pred=np.linalg.det(P_)**-2
    for t in [mp.mpc(0.137,1.291),mp.mpc(-0.284,2.173),mp.mpc(0.41,0.95)]:
        a,b,c,d=[mp.mpf(int(round(x))) for x in M.ravel()]
        gt=(a*t+b)/(c*t+d)
        meas=eta(gt)**6/((c*t+d)**3*eta(t)**6)
        if abs(meas-mp.mpc(pred))>1e-12: bad+=1
print("C1 via eta^6 (branch-free) mismatches:",bad,"of",len(words)*3)
# mpmath jtheta(2) branch defect
t=mp.mpc(0.3,1.0)
for sh in [0,1,2,8]:
    tt=t+sh
    a=mp.jtheta(2,0,mp.exp(1j*mp.pi*tt)); b=2*mp.nsum(lambda n: mp.exp(1j*mp.pi*tt*(n+mp.mpf(1)/2)**2),[0,mp.inf])
    print("shift",sh,"Re tau=",mp.nstr(tt.real,3),"jtheta2/branchfree =",mp.nstr(a/b,6))
