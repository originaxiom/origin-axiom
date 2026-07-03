"""B402 Q2' -- the seam landscape over the 15 D-side twist addresses."""
import json, os, sys
from fractions import Fraction as Fr
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "B358_seam_certification"))
sys.path.insert(0, os.path.join(HERE, "..", "B367_value_map"))
import cyclo_engine as E
import seam_certification as SC

N = 15
def diagm(f): return [[f(j) if i==j else E.ZERO for j in range(N)] for i in range(N)]
F  = [[E.e15((i*j)%15) for j in range(N)] for i in range(N)]
Fi = [[E.scal(Fr(1,15), E.e15((-i*j)%15)) for j in range(N)] for i in range(N)]

def model(r):
    Dr  = diagm(lambda j: E.e15((8*j*j + r*j) % 15))
    Dri = diagm(lambda j: E.e15((-(8*j*j + r*j)) % 15))
    WR = E.mmul(E.mmul(F, Dri), Fi)
    W1 = E.mmul(WR, Dr)
    W2 = E.mmul(E.mmul(WR, WR), E.mmul(Dr, Dr))
    return W1, W2

def order_pows(W, cap=200):
    I = [[E.ONE if i==j else E.ZERO for j in range(N)] for i in range(N)]
    pw=[I]; P=W
    for k in range(1,cap+1):
        if P==I: return k,pw
        pw.append(P); P=E.mmul(P,W)
    raise RuntimeError("cap")

def par_tr(A,B):
    t=E.ZERO
    for x in range(N):
        Ar=A[(-x)%N]
        for y in range(N):
            if Ar[y]!=E.ZERO and B[y][x]!=E.ZERO:
                t=E.add(t,E.mul(Ar[y],B[y][x]))
    return t

out = {}
for r in range(15):
    W1, W2 = model(r)
    o1,p1 = order_pows(W1); o2,p2 = order_pows(W2)
    z1, z2 = 60//o1, 60//o2
    C = {(j,l): par_tr(p1[j],p2[l]) for j in range(o1) for l in range(o2)}
    s_cells = 0
    for a in range(o1):
        for b in range(o2):
            t=E.ZERO
            for j in range(o1):
                za=E.zeta((-z1*j*a)%60)
                for l in range(o2):
                    t=E.add(t,E.mul(E.mul(za,E.zeta((-z2*l*b)%60)),C[(j,l)]))
            sol=SC.solve_H(SC.H_avg(E.scal(Fr(1,o1*o2),t)))
            if sol and sol[3]!=0: s_cells+=1
    out[str(r)] = dict(ords=[o1,o2], s_cells=s_cells, bright=bool(s_cells))
    print(f"r={r:2d}: ords {o1}x{o2}, s-cells {s_cells} -> {'BRIGHT' if s_cells else 'NULL'}", flush=True)
json.dump(out, open(os.path.join(HERE,"q2_landscape.json"),"w"), indent=1)
print("ALLDONE", flush=True)
