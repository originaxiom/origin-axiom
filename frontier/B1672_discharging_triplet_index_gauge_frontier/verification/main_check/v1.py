# Independent check: Nielsen shears, Gamma(2) words, lifts, group order, irreducibility
import importlib.util, io, contextlib, itertools, numpy as np, sys
import pathlib; F=str(pathlib.Path(__file__).resolve().parents[3])+"/"
def load(name, rel):
    spec=importlib.util.spec_from_file_location(name,F+rel); m=importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(m)
    return m
om=load("om","B1617_the_weave_at_tau_omega/verification/weave_at_omega.py")
W,cp=om.W,om.cp
inv=np.linalg.inv
# ---- 1. shears, own implementation (free group words, lowercase gens, uppercase inverses)
def red(w):
    o=[]
    for c in w:
        if o and o[-1]==c.swapcase(): o.pop()
        else: o.append(c)
    return "".join(o)
def winv(w): return "".join(c.swapcase() for c in reversed(w))
def app(f,w): return red("".join(f[c] if c.islower() else winv(f[c.lower()]) for c in w))
def comp(f,g): # (f o g)(x)=f(g(x))
    return {x:app(f,g[x]) for x in "ab"}
Lab={"a":"a","b":"ab"};Lba={"a":"a","b":"ba"};Rab={"a":"ab","b":"b"};Rba={"a":"ba","b":"b"}
def autinv(f):
    # brute: invert via search of the shears
    return None
Lab_i={"a":"a","b":"Ab"}; Rba_i={"a":"Ba","b":"b"}
assert comp(Lab,Lab_i)=={"a":"a","b":"b"}
assert comp(Rba,Rba_i)=={"a":"a","b":"b"}
print("Lab^-1 o Lba =",comp(Lab_i,Lba), " (f o g = f after g)")
print("Lba o Lab^-1 =",comp(Lba,Lab_i))
print("Rba^-1 o Rab =",comp(Rba_i,Rab))
print("Rab o Rba^-1 =",comp(Rab,Rba_i))
def conj(c): # a-> c a c^-1
    return {x:red(c+x+winv(c)) for x in "ab"}
print("conj(A)",conj("A"),"conj(B)",conj("B"),"conj(a)",conj("a"),"conj(b)",conj("b"))
# group generated: image in SL2Z and contains Inn
def h1(f): return np.array([[f[x].count("a")-f[x].count("A"),f[x].count("b")-f[x].count("B")] for x in "ab"]).T
for n,f in [("Lab",Lab),("Lba",Lba),("Rab",Rab),("Rba",Rba)]: print(n,"H1=",h1(f).tolist(),"det",round(np.linalg.det(h1(f))))
# ---- 2. lifts via repo
ML,MR=W.ML,W.MR
print("ML shape",ML.shape)
def order(gens,maxn=2000):
    G=[np.eye(gens[0].shape[0],dtype=complex)];q=[G[0]];keys={tuple(np.round(G[0],6).flatten())}
    while q:
        c=q.pop()
        for g in gens:
            n=c@g;k=tuple(np.round(n,6).flatten()+0)
            if k not in keys: keys.add(k);G.append(n);q.append(n)
            if len(G)>maxn: return G
    return G
Pa=np.diag([W.chi(p,"a")*1 for p in W.PAR for _ in range(2)]).astype(complex)
Pb=np.diag([W.chi(p,"b")*1 for p in W.PAR for _ in range(2)]).astype(complex)
print("PAR",W.PAR,[W.chi(p,'a') for p in W.PAR],[W.chi(p,'b') for p in W.PAR])
RL2R=MR@ML@ML@MR; LR2L=ML@MR@MR@ML
print("RL2R==Pa",np.allclose(RL2R,Pa)," ==Pb",np.allclose(RL2R,Pb)," LR2L==Pb",np.allclose(LR2L,Pb),"==Pa",np.allclose(LR2L,Pa))
print("RL2R diag",np.round(np.diag(RL2R),3).real, "offdiag norm",np.linalg.norm(RL2R-np.diag(np.diag(RL2R))))
print("LR2L diag",np.round(np.diag(LR2L),3).real)
# also other composition order (MR order)
G=order([ML,MR]); print("order <ML,MR> =",len(G))
G2=order([ML,MR,Pa,Pb]); print("order <ML,MR,Pa,Pb> =",len(G2))
# Is Pa in <ML,MR>?
print("Pa in G:",any(np.allclose(g,Pa) for g in G),"Pb in G:",any(np.allclose(g,Pb) for g in G))
# character inner product
def ip(G): return sum(abs(np.trace(g))**2 for g in G)/len(G)
print("<chi,chi> on V (G)",ip(G),"(G2)",ip(G2))
# commutant dim via solving
def commutant_dim(gens):
    n=gens[0].shape[0]
    A=np.vstack([np.kron(g.T,np.eye(n))-np.kron(np.eye(n),g) for g in gens])
    s=np.linalg.svd(A,compute_uv=False); return int(sum(s<1e-8))
print("commutant dim <ML,MR>:",commutant_dim([ML,MR])," <ML,MR,Pa,Pb>:",commutant_dim([ML,MR,Pa,Pb]))
# T / Tbar decomposition
TB=cp.TB
P_T=TB@TB.conj().T
print("T invariant under ML,MR:",[np.linalg.norm((np.eye(6)-P_T)@g@P_T) for g in (ML,MR)])
# Is the 6D module V = TB + Tbar identical to W's space where ML acts? check swap element order 192
