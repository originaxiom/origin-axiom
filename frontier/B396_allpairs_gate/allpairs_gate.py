"""B396 -- the P64 factorization gate over all six banked pairs."""
import json, os, sys
from fractions import Fraction as Fr
from math import gcd
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "B358_seam_certification"))
sys.path.insert(0, os.path.join(HERE, "..", "B367_value_map"))
import cyclo_engine as E
from step0_exact_matrices import build_theta_W, matrix_order, par_trace

N = 15
X  = [[E.ONE if i == (j+1) % N else E.ZERO for j in range(N)] for i in range(N)]
Z  = [[E.e15(j % 15) if i == j else E.ZERO for j in range(N)] for i in range(N)]
Par = [[E.ONE if i == (-j) % N else E.ZERO for j in range(N)] for i in range(N)]
z6i = E.zeta(50)
Jm = E.mmul(E.mmul(X, Z), Par)
J = [[E.mul(z6i, Jm[i][j]) for j in range(N)] for i in range(N)]
Jinv = [[E.ZERO]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if J[i][j] != E.ZERO:
            for k in range(60):
                if J[i][j] == E.zeta(k): Jinv[j][i] = E.zeta((-k) % 60); break

def m2(A, B): return [[(A[i][0]*B[0][j] + A[i][1]*B[1][j]) % 15 for j in range(2)] for i in range(2)]
def tr15(M):
    t = E.ZERO
    for i in range(N): t = E.add(t, M[i][i])
    return t

PAIRS = [(1,2),(1,3),(1,4),(2,3),(2,4),(3,4)]
res = {}
for (ma, mb) in PAIRS:
    Wa = build_theta_W(ma); Wb = build_theta_W(mb)
    oa, pa = matrix_order(Wa); ob, pb = matrix_order(Wb)
    ga = [[(1+ma*ma) % 15, ma % 15], [ma % 15, 1]]
    gb = [[(1+mb*mb) % 15, mb % 15], [mb % 15, 1]]
    Ga = [[[1,0],[0,1]]]
    for _ in range(oa-1): Ga.append(m2(Ga[-1], ga))
    Gb = [[[1,0],[0,1]]]
    for _ in range(ob-1): Gb.append(m2(Gb[-1], gb))
    match = boundary = mismatch = 0
    for j in range(oa):
        for l in range(ob):
            Wjl = E.mmul(pa[j], pb[l])
            Cc = par_trace(pa[j], pb[l])
            gp = m2(Ga[j], Gb[l])
            gm = [[(-gp[0][0]-1) % 15, (-gp[0][1]) % 15], [(-gp[1][0]) % 15, (-gp[1][1]-1) % 15]]
            det = (gm[0][0]*gm[1][1] - gm[0][1]*gm[1][0]) % 15
            if gcd(det, 15) != 1:
                boundary += 1; continue
            di = pow(det, -1, 15)
            Mi = [[gm[1][1]*di % 15, -gm[0][1]*di % 15], [-gm[1][0]*di % 15, gm[0][0]*di % 15]]
            w1_, w2_ = (Mi[0][0]+Mi[0][1]) % 15, (Mi[1][0]+Mi[1][1]) % 15
            Q = (8*((w2_ - w1_) % 15) + 7) % 15
            chi = tr15(E.mmul(Wjl, Jinv))
            pred = E.mul(E.mul(z6i, chi), E.e15(Q))
            if pred == Cc: match += 1
            else: mismatch += 1
    res[f"{ma},{mb}"] = dict(ords=[oa, ob], match=match, boundary=boundary, mismatch=mismatch)
    print(f"({ma},{mb}) ords {oa}x{ob}: match {match}, boundary {boundary}, MISMATCH {mismatch}", flush=True)
json.dump(res, open(os.path.join(HERE, "allpairs_gate.json"), "w"), indent=1)
print("ALLDONE", flush=True)
