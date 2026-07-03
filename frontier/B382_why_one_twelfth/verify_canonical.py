"""B382 leg 2 cross-check (registered BEFORE running): the canonical model.

D = C . chi with C = diag zeta^{8 j^2} (canonical lift of the SAME unit shear;
8 = 2^{-1} mod 15) and chi = diag zeta^{-8 j} (the half-characteristic shift).
Build the canonical words W'_m = (F C^{-1} F^{-1})^m . C^m and fit the phase-ratio law.

PREDICTION: pure-phase + quadratic on the same words; SAME ordering constant s = 7 = -2^{-1};
linear part (D,E) = (0,0) for every word  ==>  the (7,8) linear fingerprint of the theta
model IS the half-characteristic chi, i.e. the twist isolated inside the trace formula."""
import json, os, sys
from fractions import Fraction as Fr
from math import gcd
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "B358_seam_certification"))
import cyclo_engine as E

N = 15
def diagm(f): return [[f(j) if i==j else E.ZERO for j in range(N)] for i in range(N)]
C  = diagm(lambda j: E.e15((8*j*j)%15))
Ci = diagm(lambda j: E.e15((-8*j*j)%15))
F  = [[E.e15((i*j)%15) for j in range(N)] for i in range(N)]
Fi = [[E.scal(Fr(1,15), E.e15((-i*j)%15)) for j in range(N)] for i in range(N)]
WRc = E.mmul(E.mmul(F,Ci),Fi)

def mpowm(M,k):
    R = [[E.ONE if i==j else E.ZERO for j in range(N)] for i in range(N)]
    for _ in range(k%60 if k else 0): R = E.mmul(R,M)
    return R
def build_canon_W(m):
    P = mpowm(WRc, m)
    return E.mmul(P, diagm(lambda j: E.e15((8*m*j*j)%15)))

def heis(a,b):
    M = [[E.ONE if i==(j+a)%N else E.ZERO for j in range(N)] for i in range(N)]
    return E.mmul(M, diagm(lambda j: E.e15((b*j)%15)))
def tr(M):
    t=E.ZERO
    for i in range(N): t=E.add(t,M[i][i])
    return t
def field_inv(y):
    cols=[]
    for k in range(E.DEG):
        mono=[Fr(0)]*E.DEG; mono[k]=Fr(1)
        cols.append(E.mul(y,mono))
    n=E.DEG
    M=[[cols[c][r] for c in range(n)]+[Fr(1) if r==0 else Fr(0)] for r in range(n)]
    for c in range(n):
        piv=next(r for r in range(c,n) if M[r][c]!=0)
        M[c],M[piv]=M[piv],M[c]
        pv=M[c][c]; M[c]=[v/pv for v in M[c]]
        for r in range(n):
            if r!=c and M[r][c]!=0:
                f=M[r][c]; M[r]=[M[r][i]-f*M[c][i] for i in range(n+1)]
    return [M[i][n] for i in range(n)]

ZETA = {k: E.e15(k%15) for k in range(15)}
def dlog15(x):
    for k in range(15):
        if x == ZETA[k]: return k
    return None

W1 = build_canon_W(1); W2 = build_canon_W(2)
# order caps: compute inverses as high powers
def matrix_order(W, cap=200):
    ident = [[E.ONE if i == j else E.ZERO for j in range(N)] for i in range(N)]
    powers=[ident]; P=W
    for k in range(1,cap+1):
        if P==ident: return k,powers
        powers.append(P); P=E.mmul(P,W)
    raise RuntimeError("cap")
o1,pow1 = matrix_order(W1); o2,pow2 = matrix_order(W2)
print("canonical orders:", o1, o2)

def word(j,l): return E.mmul(pow1[j%o1], pow2[l%o2])
def w_inv(j,l): return E.mmul(pow2[(o2-l)%o2], pow1[(o1-j)%o1])

results = {}
SAMPLE = [(1,0),(0,1),(1,1),(2,1),(2,3)]
for (j,l) in SAMPLE:
    U, Uinv = word(j,l), w_inv(j,l)
    t0 = tr(U)
    if t0 == E.ZERO:
        results[f"{j},{l}"] = dict(trace_zero=True); print((j,l),"trace 0"); continue
    t0i = field_inv(t0)
    def gam_of(v):
        T = heis(*v)
        Cj = E.mmul(E.mmul(U,T),Uinv)
        a1 = next(i for i in range(N) if Cj[i][0]!=E.ZERO)
        r0 = Cj[a1][0]; r1 = Cj[(1+a1)%N][1]
        slope = dlog15(E.mul(r1, field_inv(r0)))
        return (a1, slope)
    ga, gb = gam_of((1,0)), gam_of((0,1))
    qv = {}; okp = True
    for a in range(15):
        for b in range(15):
            k = dlog15(E.mul(tr(E.mmul(U, heis(a,b))), t0i))
            if k is None: okp=False; break
            qv[(a,b)] = k
        if not okp: break
    rec = dict(gamma_cols=[ga,gb], pure_phase=okp)
    if okp:
        q10,q20,q01,q02,q11 = qv[(1,0)],qv[(2,0)],qv[(0,1)],qv[(0,2)],qv[(1,1)]
        A = (q20-2*q10)*pow(2,-1,15)%15; Dd=(q10-A)%15
        Cc = (q02-2*q01)*pow(2,-1,15)%15; Ee=(q01-Cc)%15
        B = (q11-A-Cc-Dd-Ee)%15
        quad = all((A*a*a+B*a*b+Cc*b*b+Dd*a+Ee*b)%15==k for (a,b),k in qv.items())
        rec.update(quadratic=quad, Q=[A,B,Cc,Dd,Ee])
    results[f"{j},{l}"] = rec
    print((j,l), rec)
json.dump(results, open("canonical_check.json","w"), indent=1)

# verdict vs the registered prediction
ok_lin = all(r.get("Q",[0,0,0,1,1])[3:]==[0,0] for r in results.values() if r.get("quadratic"))
print("PREDICTION linear==(0,0):", ok_lin)
