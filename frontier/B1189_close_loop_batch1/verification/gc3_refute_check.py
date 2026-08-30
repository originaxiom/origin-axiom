"""Independent re-derivation of GC-3's discriminating facts. Fresh code, no reuse."""
import itertools, sys
from fractions import Fraction

def mm(A, B):
    return [[A[0][0]*B[0][0]+A[0][1]*B[1][0], A[0][0]*B[0][1]+A[0][1]*B[1][1]],
            [A[1][0]*B[0][0]+A[1][1]*B[1][0], A[1][0]*B[0][1]+A[1][1]*B[1][1]]]

def det(A): return A[0][0]*A[1][1]-A[0][1]*A[1][0]
def tr(A): return A[0][0]+A[1][1]
I2 = [[1,0],[0,1]]

fails = []
def check(name, ok):
    print(("PASS " if ok else "FAIL ")+name)
    if not ok: fails.append(name)

# (a) M, RL, square roots -------------------------------------------------
M = [[1,1],[1,0]]
R = [[1,1],[0,1]]; L = [[1,0],[1,1]]
RL = mm(R, L)
check("RL=[[2,1],[1,1]] and M^2=RL, det M=-1", RL==[[2,1],[1,1]] and mm(M,M)==RL and det(M)==-1)

# Cayley-Hamilton exhaustive: K^2=RL, K integer 2x2. K scalar impossible (RL not scalar).
# K^2 = t*K - d*I with t=tr K, d=det K. So RL = t*K - d*I -> if t!=0, K=(RL+dI)/t.
# constraints: d^2=det(RL)=1; tr(RL)=3=t^2-2d.
roots = []
for d in (1,-1):
    t2 = 3 + 2*d
    for t in set([x for x in range(-10,11) if x*x==t2]):
        if t == 0: continue
        K = [[Fraction(RL[i][j] + (d if i==j else 0), t) for j in range(2)] for i in range(2)]
        if all(v.denominator==1 for row in K for v in row):
            Ki = [[int(v) for v in row] for row in K]
            if mm(Ki,Ki)==RL: roots.append((Ki, det(Ki)))
# t=0 case: RL = -d*I, false. d=+1 -> t^2=5 no integer solution.
check("d=+1 gives t^2=5, no integer t", all(x*x!=5 for x in range(-10,11)))
check("only integer sqrt(RL) are +/-M via C-H", sorted(str(r[0]) for r in roots)==sorted([str(M),str([[-1,-1],[-1,0]])]) and all(r[1]==-1 for r in roots))
# independent brute force |entries|<=4
bf = [K for K in ([[a,b],[c,d0]] for a in range(-4,5) for b in range(-4,5) for c in range(-4,5) for d0 in range(-4,5)) if mm(K,K)==RL]
check("brute force |e|<=4 confirms exactly {+M,-M}", sorted(map(str,bf))==sorted([str(M),str([[-1,-1],[-1,0]])]))
check("det(M^j)=(-1)^j j=1..8", all(det([[1,0],[0,1]] if j==0 else __import__('functools').reduce(mm,[M]*j))==(-1)**j for j in range(1,9)))

# (b) conductor table -----------------------------------------------------
def matpow_mod(A, n, m):
    Rr = [[1,0],[0,1]]; B=[[x%m for x in row] for row in A]
    while n:
        if n&1: Rr=[[sum(Rr[i][k]*B[k][j] for k in range(2))%m for j in range(2)] for i in range(2)]
        B=[[sum(B[i][k]*B[k][j] for k in range(2))%m for j in range(2)] for i in range(2)]
        n>>=1
    return Rr

def ord_mod(A, m, cap=500000):
    X=[[x%m for x in row] for row in A]; P=[row[:] for row in X]
    for n in range(1, cap+1):
        if P==[[1%m,0],[0,1%m]]: return n
        P=[[sum(P[i][k]*X[k][j] for k in range(2))%m for j in range(2)] for i in range(2)]
    return None

banked = {4:1,5:10,6:12,7:8,8:12,9:36,10:60,11:20,12:12,13:28,14:24,15:60}
ordRL3k = {k: ord_mod(RL, 3*k) for k in range(4,16)}
claimed = dict(zip(range(4,16),(12,20,12,8,12,36,60,20,12,28,24,60)))
check("ord(RL mod 3k) table matches cell's claimed values", ordRL3k==claimed)
match_6_15 = sum(1 for k in range(6,16) if ordRL3k[k]==banked[k])
check("banked match 10/10 on kappa=6..15", match_6_15==10)
check("anomaly kappa=4: banked 1 vs ord 12", banked[4]==1 and ordRL3k[4]==12)
check("anomaly kappa=5: banked 10 = ord/2 = 20/2", banked[5]==10 and ordRL3k[5]==20)
ordM3k = {k: ord_mod(M, 3*k) for k in range(4,16)}
check("ord(M mod 3k) = 2*ord(RL mod 3k) all 12", all(ordM3k[k]==2*ordRL3k[k] for k in range(4,16)))
check("ord(M) values match cell (24,40,...)", [ordM3k[k] for k in range(4,16)]==[24,40,24,16,24,72,120,40,24,56,48,120])
U = [[1,1],[0,1]]
ordU = {k: ord_mod(U, 3*k) for k in range(4,16)}
check("CONTROL-: unipotent ord mod 3k == 3k, mismatch banked 12/12",
      all(ordU[k]==3*k for k in range(4,16)) and all(ordU[k]!=banked[k] for k in range(4,16)))
naive = {k: ord_mod(RL, k) for k in range(4,16)}
nm = sum(1 for k in range(4,16) if naive[k]==banked[k])
check("CONTROL-: naive ord(RL mod k) matches banked only 5/12", nm==5)

# (c) GL(2,Z) conjugacy ---------------------------------------------------
C = [[0,-1],[1,3]]
check("charpoly C = x^2-3x+1 = charpoly RL", tr(C)==3 and det(C)==1)
P = [[-3,-1],[5,2]]
check("det P = -1", det(P)==-1)
adjP = [[P[1][1],-P[0][1]],[-P[1][0],P[0][0]]]
Pinv = [[adjP[i][j]*det(P) if det(P)==1 else -adjP[i][j]*(-1) for j in range(2)] for i in range(2)]
# careful: inv = adj/det; det=-1 -> inv = -adj
Pinv = [[-adjP[i][j] for j in range(2)] for i in range(2)] if det(P)==-1 else adjP
check("P*C*P^-1 == RL", mm(mm(P,C),Pinv)==RL)
# count conjugators |entries|<=5
def conj_count(Cm, Tm, bound):
    cnt=0
    for a,b,c,d0 in itertools.product(range(-bound,bound+1),repeat=4):
        dd = a*d0-b*c
        if dd not in (1,-1): continue
        Q=[[a,b],[c,d0]]
        Qi=[[d0*dd if dd==1 else -d0, -b*dd if dd==1 else b],[-c*dd if dd==1 else c, a*dd if dd==1 else -a]]
        # inv = adj/det: dd=1 -> adj ; dd=-1 -> -adj
        adj=[[d0,-b],[-c,a]]
        Qi=adj if dd==1 else [[-x for x in row] for row in adj]
        if mm(mm(Q,Cm),Qi)==Tm: cnt+=1
    return cnt
n_conj = conj_count(C, RL, 5)
check("16 conjugators |e|<=5 for C->RL", n_conj==16)
n_ctrl = conj_count([[1,1],[0,1]], [[1,2],[0,1]], 5)
check("CONTROL-: [[1,1],[0,1]] vs [[1,2],[0,1]] gives 0 conjugators", n_ctrl==0)

# (d) depth vs order ------------------------------------------------------
# 3x3 nilpotency-3 unipotent J = I + N, N = shift
def mm3(A,B): return [[sum(A[i][k]*B[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
N3=[[0,1,0],[0,0,1],[0,0,0]]
J=[[1,1,0],[0,1,1],[0,0,1]]
Jp=J
vals=[]
for n in range(2,8): Jp=mm3(Jp,J)
check("J^7[0][2]==21 (binom(7,2)) infinite order char 0", Jp[0][2]==21)
def mod3(A): return [[x%3 for x in row] for row in A]
J1=mod3(J); J2=mod3(mm3(J,J)); J3=mod3(mm3(mm3(J,J),J))
I3=[[1,0,0],[0,1,0],[0,0,1]]
check("J order exactly 3 mod 3", J3==I3 and J1!=I3 and J2!=I3)

# (2) reconciliation ------------------------------------------------------
import sympy as sp
phi = (1+sp.sqrt(5))/2
check("(1-phi)^2 == phi^-2 exact", sp.simplify((1-phi)**2 - phi**-2)==0)
Minv = [[0,1],[1,-1]]
check("M^-1=[[0,1],[1,-1]], has negative entry", mm(M,Minv)==I2 and any(x<0 for row in Minv for x in row))
# sigma(a)=ab sigma(b)=a; enumerate images of all words length<=10
def sig(w): return ''.join('ab' if ch=='a' else 'a' for ch in w)
images = set()
for L_ in range(1,11):
    for w in itertools.product('ab',repeat=L_):
        images.add(sig(''.join(w)))
check("'bb' has no preimage (length<=10)", 'bb' not in images and not any('bb'==sig(''.join(w)) for L_ in range(1,11) for w in itertools.product('ab',repeat=L_)))
check("'aaa' = sigma('bbb')", sig('bbb')=='aaa')
# stronger: no image word contains 'bb' at all (structural)
check("no image contains substring bb", all('bb' not in im for im in images))

# (3) the join ------------------------------------------------------------
x,y,z = sp.symbols('x y z')
kap = x**2+y**2+z**2-x*y*z-2
# Goldman bracket on rank-2 free group char variety: {x,y}=xy-2z (cyclic)
def bracket(f,g):
    # Poisson bracket generated by {x,y}=xy-2z, {y,z}=yz-2x, {z,x}=zx-2y
    bxy = x*y-2*z; byz = y*z-2*x; bzx = z*x-2*y
    return (sp.diff(f,x)*sp.diff(g,y)-sp.diff(f,y)*sp.diff(g,x))*bxy \
         + (sp.diff(f,y)*sp.diff(g,z)-sp.diff(f,z)*sp.diff(g,y))*byz \
         + (sp.diff(f,z)*sp.diff(g,x)-sp.diff(f,x)*sp.diff(g,z))*bzx
check("kappa is Casimir: {kappa,x}={kappa,y}={kappa,z}=0",
      all(sp.expand(bracket(kap,v))==0 for v in (x,y,z)))
wrong = x**2+y**2+z**2
check("CONTROL-: x^2+y^2+z^2 NOT Casimir", sp.expand(bracket(wrong,x))!=0)
# anti-symplectic beat
B=[[1,0],[0,-1]]; Om=[[0,1],[-1,0]]
Bt=[[B[j][i] for j in range(2)] for i in range(2)]
check("B^T Omega B = -Omega, det B=-1, B^2=I", mm(mm(Bt,Om),B)==[[0,-1],[1,0]] and det(B)==-1 and mm(B,B)==I2)

print()
print("FAILURES:", fails if fails else "NONE — all facts independently confirmed")
sys.exit(1 if fails else 0)
