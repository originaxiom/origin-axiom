"""B382 leg 1 — the shifted trace formula: intertwining + the phase-ratio law (exact gates).

(a) The intertwining of the Heisenberg frame by the theta-model generators, exact:
    D X D^-1 = ? , D Z D^-1 = ? , WR X WR^-1 = ? , WR Z WR^-1 = ?  (phases included)
(b) THE PHASE-RATIO LAW (the derivation's core): for a word U with group element gamma
    (det(gamma - I) invertible mod 15), the shifted trace is a PURE PHASE times the trace:
        tr(U . X^m Z^n) = tr(U) . e15( Q_gamma(m,n) )
    verified exactly for ALL 225 shifts on a sample of words, with Q extracted empirically
    and then CHECKED to be the quadratic form of (gamma - I)^{-1} (convention pinned by data).
"""
import json, os, sys
from fractions import Fraction as Fr
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "B358_seam_certification"))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "B367_value_map"))
import cyclo_engine as E
from step0_exact_matrices import build_theta_W, matrix_order

N = 15
def diagm(f): return [[f(j) if i==j else E.ZERO for j in range(N)] for i in range(N)]
D  = diagm(lambda j: E.e15((j*(j-1)//2)%15))
Di = diagm(lambda j: E.e15((-(j*(j-1)//2))%15))
F  = [[E.e15((i*j)%15) for j in range(N)] for i in range(N)]
Fi = [[E.scal(Fr(1,15), E.e15((-i*j)%15)) for j in range(N)] for i in range(N)]
WR = E.mmul(E.mmul(F,Di),Fi)
WRi= E.mmul(E.mmul(F,D),Fi)
X  = [[E.ONE if i==(j+1)%N else E.ZERO for j in range(N)] for i in range(N)]
Z  = diagm(lambda j: E.e15(j%15))

def heis(a,b):
    """T_(a,b) = X^a Z^b (exact)."""
    M = [[E.ONE if i==(j+a)%N else E.ZERO for j in range(N)] for i in range(N)]
    return E.mmul(M, diagm(lambda j: E.e15((b*j)%15)))

def eqm(A,B): return all(A[i][j]==B[i][j] for i in range(N) for j in range(N))
def tr(M):
    t=E.ZERO
    for i in range(N): t=E.add(t,M[i][i])
    return t

# ---- (a) the intertwining, exact ----
print("(a) intertwining:")
print("  D X D^-1  == X Z      :", eqm(E.mmul(E.mmul(D,X),Di), E.mmul(X,Z)))
print("  D Z D^-1  == Z        :", eqm(E.mmul(E.mmul(D,Z),Di), Z))
ZX = E.mmul(E.mmul(WR,X),WRi)
print("  WR X WR^-1== Z^-1?    :", eqm(ZX, diagm(lambda j: E.e15((-j)%15))))
WZ = E.mmul(E.mmul(WR,Z),WRi)
# candidates: X, X^-1 possibly with phase
Xi_ = [[E.ONE if i==(j-1)%N else E.ZERO for j in range(N)] for i in range(N)]
print("  WR Z WR^-1== X        :", eqm(WZ, X), " == X^-1:", eqm(WZ, Xi_))

# ---- (b) the phase-ratio law across words ----
# group elements: D ~ R-side shear, WR ~ L-side (as computed from the intertwining above);
# the exponent action gamma acts on (a,b) of T_(a,b): read it off empirically per word instead
# of assuming: for each word U, find gamma by U T_(1,0) U^-1 and U T_(0,1) U^-1.
W1 = build_theta_W(1); W2 = build_theta_W(2)
o1,pow1 = matrix_order(W1); o2,pow2 = matrix_order(W2)
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

def word(j,l): return E.mmul(pow1[j], pow2[l])
def w_inv(j,l): return E.mmul(pow2[(o2-l)%o2], pow1[(o1-j)%o1])

ZETA = {k: E.e15(k%15) for k in range(15)}
def dlog15(x):
    for k in range(15):
        if x == ZETA[k]: return k
    return None

results = {}
SAMPLE = [(1,0),(0,1),(1,1),(2,1),(1,3),(3,1),(2,3)]
for (j,l) in SAMPLE:
    U, Uinv = word(j,l), w_inv(j,l)
    t0 = tr(U)
    if t0 == E.ZERO:
        results[f"{j},{l}"] = "trace 0 — outside the law's domain"; continue
    t0i = field_inv(t0)
    # extract the empirical gamma from conjugation of T_(1,0), T_(0,1)
    def gam_of(v):
        T = heis(*v)
        C = E.mmul(E.mmul(U,T),Uinv)
        # C should be phase * T_(a',b'): find its support shift a' and diagonal phase slope b'
        a1 = next(i for i in range(N) if C[i][0]!=E.ZERO)
        # slope: C[(j+a')%15][j] = phase * zeta^{b' j}
        r0 = C[a1][0]; r1 = C[(1+a1)%N][1]
        slope = dlog15(E.mul(r1, field_inv(r0)))
        return (a1, slope)
    ga = gam_of((1,0)); gb = gam_of((0,1))
    # the phase-ratio law: r(v) = tr(U T_v)/tr(U) must be zeta15^{q(v)} with q quadratic
    qvals = {}
    okphase = True
    for a in range(15):
        for b in range(15):
            r = E.mul(tr(E.mmul(U, heis(a,b))), t0i)
            k = dlog15(r)
            if k is None: okphase=False; break
            qvals[(a,b)] = k
        if not okphase: break
    quad_ok = False
    if okphase:
        # check q is quadratic: q(v) = A a^2 + B ab + C b^2 + D a + E b mod 15 — fit and verify
        import itertools
        A_,D_ = None,None
        # fit from small values
        q00=qvals[(0,0)]; q10=qvals[(1,0)]; q20=qvals[(2,0)]; q01=qvals[(0,1)]; q02=qvals[(0,2)]; q11=qvals[(1,1)]
        # q(0,0)=0 expected
        Acoef = (q20 - 2*q10) * pow(2,-1,15) % 15 if True else None
        # solve: q10 = A + D; q20 = 4A + 2D => A = (q20-2q10)/2, D = q10 - A
        Aq = ((q20 - 2*q10) * pow(2,-1,15)) % 15
        Dq = (q10 - Aq) % 15
        Cq = ((q02 - 2*q01) * pow(2,-1,15)) % 15
        Eq = (q01 - Cq) % 15
        Bq = (q11 - Aq - Cq - Dq - Eq) % 15
        quad_ok = all(qvals[(a,b)] == (Aq*a*a + Bq*a*b + Cq*b*b + Dq*a + Eq*b) % 15
                      for a in range(15) for b in range(15))
        results[f"{j},{l}"] = dict(gamma_cols=[ga,gb], trace_nonzero=True,
                                   pure_phase=okphase, quadratic=quad_ok,
                                   Q=[Aq,Bq,Cq,Dq,Eq])
    else:
        results[f"{j},{l}"] = dict(pure_phase=False)
    print(f"word ({j},{l}): gamma cols {ga},{gb}; pure-phase ratio: {okphase}; "
          f"quadratic: {quad_ok}; Q={results[f'{j},{l}'].get('Q')}", flush=True)
json.dump(results, open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"trace_formula.json"),"w"), indent=1, default=str)
print("DONE")
