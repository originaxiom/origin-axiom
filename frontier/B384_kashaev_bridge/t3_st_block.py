"""B384 T3 -- the seam sector's 2x2 (S,T) block, canonical vs theta, exact (level 15).

Sector: the slot = the mult-1 W1-eigenpair at exponents {6,14} (P56/P60). Basis: v_a = P_a w
(rank-1 projectors, generic seed w). T-data: the W1-eigenphases zeta20^6, zeta20^14 (the
sector's twist diagonal) and the model T-generator compressed (theta D vs canonical C).
S-data: the Fourier kernel F compressed to the sector: P_a F P_b = c_ab * (transporter);
extract c_ab exactly; normalize by the Gauss sum g = sum_j zeta15^{j^2} (computed exactly as
an H-element) to present S_block = c/g. Compare the shape against U(1)_k / Weil-TQFT
S = (1/sqrt k) [[1,1],[1,-1]]-type families. Match/no-match banks either way."""
import json, os, sys
from fractions import Fraction as Fr
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "B358_seam_certification"))
sys.path.insert(0, os.path.join(HERE, "..", "B367_value_map"))
import cyclo_engine as E
import seam_certification as SC
from step0_exact_matrices import build_theta_W, matrix_order

N = 15
W1 = build_theta_W(1)
o1, pw = matrix_order(W1)
assert o1 == 20

def proj(a):
    M = [[E.ZERO]*N for _ in range(N)]
    for j in range(o1):
        c = E.scal(Fr(1,o1), E.zeta((-3*j*a) % 60))
        for i in range(N):
            row = pw[j][i]
            for k in range(N):
                if row[k] != E.ZERO:
                    M[i][k] = E.add(M[i][k], E.mul(c, row[k]))
    return M

P6, P14 = proj(6), proj(14)
# generic seed: e_1 + e_2 (avoid symmetric traps)
w = [E.ONE if i in (1,2) else E.ZERO for i in range(N)]
def apply(M, v):
    out = []
    for i in range(N):
        acc = E.ZERO
        for k in range(N):
            if v[k] != E.ZERO and M[i][k] != E.ZERO:
                acc = E.add(acc, E.mul(M[i][k], v[k]))
        out.append(acc)
    return out
v6, v14 = apply(P6, w), apply(P14, w)
assert any(x!=E.ZERO for x in v6) and any(x!=E.ZERO for x in v14)

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
        pv=M[c][c]; M[c]=[x/pv for x in M[c]]
        for r in range(n):
            if r!=c and M[r][c]!=0:
                f=M[r][c]; M[r]=[M[r][i]-f*M[c][i] for i in range(n+1)]
    return [M[i][n] for i in range(n)]

F  = [[E.e15((i*j)%15) for j in range(N)] for i in range(N)]
Dt = [[E.e15((j*(j-1)//2)%15) if i==j else E.ZERO for j in range(N)] for i in range(N)]
Cc = [[E.e15((8*j*j)%15) if i==j else E.ZERO for j in range(N)] for i in range(N)]

def block(Op):
    """c_ab with P_a Op v_b = c_ab v_a (valid since P_a rank-1 on the slot)."""
    out = {}
    basis = {6: v6, 14: v14}
    Pm = {6: P6, 14: P14}
    for a in (6, 14):
        for b in (6, 14):
            u = apply(Pm[a], apply(Op, basis[b]))
            nz = next((i for i in range(N) if basis[a][i] != E.ZERO), None)
            c = E.mul(u[nz], field_inv(basis[a][nz]))
            # verify proportionality globally
            ok = all(E.mul(c, basis[a][i]) == u[i] for i in range(N))
            out[(a,b)] = (c, ok)
    return out

def show(t):
    sol = SC.solve_H(SC.H_avg(t))
    return [str(x) for x in sol] if sol else "notH:"+str([str(x) for x in t[:4]])

res = {}
for name, Op in (("F", F), ("D_theta", Dt), ("C_canon", Cc)):
    B = block(Op)
    res[name] = {}
    print(f"{name} block on the slot (H-avg components; prop-check):")
    for k,(c,ok) in B.items():
        res[name][f"{k[0]},{k[1]}"] = dict(HAvg=show(c), proportional=ok)
        print("  ", k, show(c), ok)
# Gauss sum g(15) as H-element
g = E.ZERO
for j in range(15): g = E.add(g, E.e15((j*j)%15))
print("g(15) H-avg:", show(g))
res["gauss15"] = show(g)
json.dump(res, open(os.path.join(HERE,"t3_block.json"),"w"), indent=1, default=str)
print("DONE")
