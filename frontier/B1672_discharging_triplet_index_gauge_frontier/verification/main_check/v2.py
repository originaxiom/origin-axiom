import numpy as np
exec(open("v1.py").read().split("# ---- 1.")[0])  # loaders
exec("def red(w):\n o=[]\n for c in w:\n  if o and o[-1]==c.swapcase(): o.pop()\n  else: o.append(c)\n return ''.join(o)")
ML,MR=W.ML,W.MR; gL,gR=W.gL,W.gR
def blocks_action(m,g):
    A=np.zeros((6,6),dtype=complex)
    for i,u in enumerate(W.PAR):
        j=W.PAR.index(W.act_parity(m,u)); A[2*i:2*i+2,2*j:2*j+2]=g
    return A
Lm,Rm={"a":"a","b":"ab"},{"a":"ab","b":"b"}
T_L6=blocks_action(Lm,gL); T_R6=blocks_action(Rm,gR)
print("arc T_L6 == W.ML ?",np.allclose(T_L6,ML)," T_R6==MR?",np.allclose(T_R6,MR))
for nm_,A,B in [("L==ML",T_L6,ML),("R==MR",T_R6,MR)]: print(nm_,np.linalg.norm(A-B))
def commutant_dim(gens):
    n=gens[0].shape[0]
    A=np.vstack([np.kron(g.T,np.eye(n))-np.kron(np.eye(n),g) for g in gens])
    s=np.linalg.svd(A,compute_uv=False); return int(sum(s<1e-8))
Pa=np.diag([W.chi(p,"a") for p in W.PAR for _ in range(2)]).astype(complex)
Pb=np.diag([W.chi(p,"b") for p in W.PAR for _ in range(2)]).astype(complex)
Pc=np.diag([1,1,1,1,1,1]).astype(complex)
print("commutant {T_L6,T_R6}",commutant_dim([T_L6,T_R6]))
print("commutant {T_L6,T_R6,Pa,Pb}",commutant_dim([T_L6,T_R6,Pa,Pb]))
print("commutant {ML,MR}",commutant_dim([ML,MR]))
# swap element for order 192 (B1600): find it
import itertools
sw={"a":"b","b":"a"}
# parity-graded: add a parity-permuting swap on V? use B1600 swap script
print("---- arc's L6-module (blocks_action) words")
w1=T_R6@T_L6@T_L6@T_R6; w2=T_L6@T_R6@T_R6@T_L6
print("R L^2 R in arc L6-module == Pa?",np.allclose(w1,Pa),"==Pb?",np.allclose(w2,Pb), " diag-ness",np.linalg.norm(w1-np.diag(np.diag(w1))))
print(np.round(w1,3))
def order(gens,maxn=3000):
    G=[np.eye(6,dtype=complex)];q=[G[0]];keys={tuple(np.round(G[0],5).flatten())}
    while q:
        c=q.pop()
        for g in gens:
            n=c@g;k=tuple(np.round(n,5).flatten()+0)
            if k not in keys: keys.add(k);G.append(n);q.append(n)
            if len(G)>maxn: return G
    return G
print("order <T_L6,T_R6>",len(order([T_L6,T_R6])),"  with Pa,Pb",len(order([T_L6,T_R6,Pa,Pb])))
# Does conjugation relate arc-L6 to W-V? compare traces
G1=order([T_L6,T_R6]); G2=order([ML,MR])
print("sorted |tr| multiset equal?",sorted(np.round(abs(np.array([np.trace(g) for g in G1])),4))==sorted(np.round(abs(np.array([np.trace(g) for g in G2])),4)))
# is the move-word R L^2 R's image in arc L6 module in the arc group's centre?
print("w1 commutes with T_L6:",np.allclose(w1@T_L6,T_L6@w1))
# commutant of arc-group with Pa only vs Pb only
print("commutant {TL6,TR6,Pa}",commutant_dim([T_L6,T_R6,Pa]),"{..,Pb}",commutant_dim([T_L6,T_R6,Pb]))
