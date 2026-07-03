"""B382 leg 3 — the assembly: the whole Par-table from the trace formula, then the 1/12.

Gate A (factorization): for ALL (j,l) in Z20 x Z12 with det(gamma'-I) invertible mod 15,
    C[j,l] := tr(Par . W1^j W2^l)  ==  zeta6^{-1} . tr(V_jl) . zeta15^{Q_jl(1,1)},
    V_jl = W1^j W2^l J^{-1},  J = zeta6^{-1} X Z Par  (P57),  gamma' = -(g1^j g2^l) mod 15,
    Q(1,1) = 8.omega(v0,(gamma'-I)^{-1}v0) + 7   (leg-2 closed form at v0=(1,1)).
Boundary cells (det not invertible) are counted and taken directly.

Gate B (assembly): DFT the C-table to t(a,b), combine the helicity gradings, project to H:
    slot   t(6,2)-t(6,10)-t(14,2)+t(14,10)  must equal  (0,0,-1/12,-1/12)
    3-block t(4,4)-t(4,8)-t(16,4)+t(16,8)   must equal  (0,0,-1/12,+1/12)

The READING: decompose the slot sum by |det(gamma'-I)| classes and window support --
exhibit what makes the 1/12."""
import json, os, sys
from fractions import Fraction as Fr
from math import gcd
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "B358_seam_certification"))
sys.path.insert(0, os.path.join(HERE, "..", "B367_value_map"))
import cyclo_engine as E
import seam_certification as SC
from step0_exact_matrices import build_theta_W, matrix_order, par_trace

N = 15
def diagm(f): return [[f(j) if i==j else E.ZERO for j in range(N)] for i in range(N)]
X  = [[E.ONE if i==(j+1)%N else E.ZERO for j in range(N)] for i in range(N)]
Z  = diagm(lambda j: E.e15(j%15))
Par = [[E.ONE if i==(-j)%N else E.ZERO for j in range(N)] for i in range(N)]
z6i = E.zeta(50)   # zeta6^{-1} = e(-1/6) = zeta60^{-10}
J   = [[E.scal(Fr(1,1), E.mul(z6i, E.mmul(E.mmul(X,Z),Par)[i][j])) for j in range(N)] for i in range(N)]
# J^-1: gamma(J) = -I, J^2 = phase; compute directly
Jinv = E.minv(J) if hasattr(E,"minv") else None
if Jinv is None:
    # J is monomial: invert by transpose-of-support with reciprocal phases
    Jinv = [[E.ZERO]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if J[i][j] != E.ZERO:
                # entry is a root of unity times 1 -> inverse = conjugate power
                v = J[i][j]
                # find k with v = zeta60^k
                for k in range(60):
                    if v == E.zeta(k): Jinv[j][i] = E.zeta((-k)%60); break
                else: raise RuntimeError("J entry not a root of unity")
def eqm(A,B): return all(A[i][j]==B[i][j] for i in range(N) for j in range(N))
ID = [[E.ONE if i==j else E.ZERO for j in range(N)] for i in range(N)]
assert eqm(E.mmul(J,Jinv), ID), "Jinv"

W1 = build_theta_W(1); W2 = build_theta_W(2)
o1,pow1 = matrix_order(W1); o2,pow2 = matrix_order(W2)
assert (o1,o2)==(20,12)
g1 = [[2,1],[1,1]]; g2 = [[5,2],[2,1]]   # banked leg-1 gammas
def m2(A,B): return [[(A[i][0]*B[0][j]+A[i][1]*B[1][j])%15 for j in range(2)] for i in range(2)]
def tr15(M):
    t=E.ZERO
    for i in range(N): t=E.add(t,M[i][i])
    return t

ZETA = {k: E.zeta(k) for k in range(60)}
def as_zeta15pow(k): return E.e15(k%15)

# precompute g1^j g2^l
G1=[[[1,0],[0,1]]]
for _ in range(19): G1.append(m2(G1[-1],g1))
G2=[[[1,0],[0,1]]]
for _ in range(11): G2.append(m2(G2[-1],g2))

table = {}
gateA = dict(match=0, boundary=0, mismatch=0, chi0=0)
det_class = {}
for j in range(o1):
    Wj = pow1[j]
    for l in range(o2):
        Wjl = E.mmul(Wj, pow2[l])
        C = par_trace(ID, Wjl)   # tr(Par * Wjl)  (par_trace(A,B)=tr(Par A B); A=ID)
        table[(j,l)] = C
        gp = m2(G1[j],G2[l]); gm = [[(-gp[i][k])%15 for k in range(2)] for i in range(2)]   # gamma' = -g
        gmi = [[(gm[0][0]-1)%15, gm[0][1]],[gm[1][0], (gm[1][1]-1)%15]]
        det = (gmi[0][0]*gmi[1][1]-gmi[0][1]*gmi[1][0])%15
        cls = gcd(det,15)
        det_class[cls] = det_class.get(cls,0)+1
        if cls != 1:
            gateA["boundary"] += 1; continue
        di = pow(det,-1,15)
        Minv = [[gmi[1][1]*di%15, -gmi[0][1]*di%15],[-gmi[1][0]*di%15, gmi[0][0]*di%15]]
        # omega(v0, Minv v0), v0=(1,1): Mv0 = (M00+M01, M10+M11); omega = 1*w2 - 1*w1
        w1_,w2_ = (Minv[0][0]+Minv[0][1])%15, (Minv[1][0]+Minv[1][1])%15
        Q = (8*((w2_-w1_)%15) + 7) % 15
        V = E.mmul(Wjl, Jinv)
        chi = tr15(V)
        pred = E.mul(E.mul(z6i, chi), as_zeta15pow(Q))
        if chi == E.ZERO: gateA["chi0"] += 1
        if pred == C: gateA["match"] += 1
        else: gateA["mismatch"] += 1

print("gate A:", gateA, " det-classes:", det_class)

# ---- gate B: DFT + gradings + H-projection ----
def tval(a,b):
    t = E.ZERO
    for j in range(o1):
        za = E.zeta((-3*j*a) % 60)          # zeta20^{-ja} = zeta60^{-3ja}
        for l in range(o2):
            t = E.add(t, E.mul(E.mul(za, E.zeta((-5*l*b)%60)), table[(j,l)]))
    return E.scal(Fr(1,o1*o2), t)
def hproj(t): return SC.solve_H(SC.H_avg(t))

slot = E.add(E.add(tval(6,2), E.scal(Fr(-1), tval(6,10))),
             E.add(E.scal(Fr(-1), tval(14,2)), tval(14,10)))
blk  = E.add(E.add(tval(4,4), E.scal(Fr(-1), tval(4,8))),
             E.add(E.scal(Fr(-1), tval(16,4)), tval(16,8)))
print("slot  Pi_H:", hproj(slot), "  target (0,0,-1/12,-1/12)")
print("3-blk Pi_H:", hproj(blk),  "  target (0,0,-1/12,+1/12)")

json.dump(dict(gateA=gateA, det_classes={str(k):v for k,v in det_class.items()},
               slot=[str(x) for x in (hproj(slot) or [])],
               blk=[str(x) for x in (hproj(blk) or [])]),
          open(os.path.join(HERE,"assembly.json"),"w"), indent=1)
print("DONE")
