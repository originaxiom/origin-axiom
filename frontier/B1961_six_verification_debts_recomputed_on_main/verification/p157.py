"""p157 -- CLAIMS AS STATED (debt P-157): an auditor, running B1620's own functions on MIXED tensor assignments, found
(a) Dirac charged lepton + Majorana neutrino (Sym^2 T) gives two-parameter TM2 families, and
(b) TM1 appears only with a Tbar(x)T neutrino.
EXPECTATION: (a) holds for some lepton tensor, (b) holds.  B1625 says same-tensor: TM1 only Tbar x T pairs, TM2 for T x T.
No data is read (no data.json imported): TM1/TM2 are identified by fixed |U|^2 columns (2/3,1/6,1/6) / (1/3,1/3,1/3).
Imports only B1620's breaking_the_weave_allows (group G, T, subgroup lattice); re-implements the rest.
Left-handed rotation convention (derived): Tbar x T sector: L = X L', X = eigvecs of M M^dagger.  T x T and Sym2 sectors
(mass term L^T M N): L = X* L'.  V = W_l^dagger W_nu with these W (matters for MIXED pairs only)."""
import pathlib as __pl
__ROOT__ = next(q for q in __pl.Path(__file__).resolve().parents if (q / 'frontier').is_dir() and (q / 'GENESIS.md').is_file())
import os, itertools, collections, importlib.util, pathlib
os.environ["OMP_NUM_THREADS"]="1"
import numpy as np
F = pathlib.Path(str(__ROOT__) + "/frontier/B1620_the_breaking_the_weave_allows/verification/breaking_the_weave_allows.py")
spec = importlib.util.spec_from_file_location("bw", F); bw = importlib.util.module_from_spec(spec); spec.loader.exec_module(bw)
G, T0 = bw.G, bw.T
K = sum(M.conj().T @ M for M in T0)/len(T0); w,E = np.linalg.eigh(K); Kh=E@np.diag(np.sqrt(w))@E.conj().T
T=[Kh@M@np.linalg.inv(Kh) for M in T0]
print("unitary defect", max(np.abs(M.conj().T@M-np.eye(3)).max() for M in T), "|G|", len(T))
def inv_basis(H,t):
    if t=="S2":
        Es=[]
        for i in range(3):
            for j in range(i,3):
                X=np.zeros((3,3),complex);X[i,j]=X[j,i]=1;Es.append(X)
    else: Es=[np.eye(9,dtype=complex)[k].reshape(3,3) for k in range(9)]
    def rey(X):
        return sum((T[h].conj().T@X@T[h]) if t=="TbT" else (T[h].T@X@T[h]) for h in H)/len(H)
    im=np.array([rey(X).ravel() for X in Es]); u,s,vh=np.linalg.svd(im); r=int((s>1e-9).sum())
    return [vh[k].reshape(3,3) for k in range(r)]
def mat(b,x):
    n=len(b); c=x[:n]+1j*x[n:]; return sum(ci*B for ci,B in zip(c,b))
def viable(b,seed):
    if not b: return False
    rng=np.random.default_rng(seed)
    for _ in range(3):
        s=np.sort(np.linalg.svd(mat(b,rng.normal(size=2*len(b))),compute_uv=False)); s/=s[-1]
        if not(s[0]>1e-6 and s[1]-s[0]>1e-6 and s[2]-s[1]>1e-6): return False
    return True
def Wof(M,t):
    _,W=np.linalg.eigh(M@M.conj().T); return W if t=="TbT" else W.conj()
def fdim(V,npar,seed):
    rng=np.random.default_rng(seed); best=0
    def inv(M):
        A=np.abs(M)**2; J=np.imag(M[0,0]*M[1,1]*np.conj(M[0,1])*np.conj(M[1,0])); return np.concatenate([A.ravel(),[J]])
    for _ in range(3):
        x=rng.normal(size=npar); h=1e-6
        Jm=np.array([(inv(V(x+h*e))-inv(V(x-h*e)))/(2*h) for e in np.eye(npar)]).T
        s=np.linalg.svd(Jm,compute_uv=False); best=max(best,int((s>max(1e-5,1e-6*s[0])).sum()))
    return best
def classify(V,npar,seed):
    """a TM tag is set when, at EVERY one of 6 random points of the family, some column (neutrino state) [or row] of |V|^2
    has the sorted entries (1/3,1/3,1/3) [TM2] or (1/6,1/6,2/3) [TM1]; eigenvector ordering may move it between samples"""
    rng=np.random.default_rng(seed); As=[np.abs(V(rng.normal(size=npar)))**2 for _ in range(6)]
    T1=np.array([1/6,1/6,2/3]); T2=np.array([1/3]*3)
    def has(A,tgt,axis):
        vecs=[A[:,j] for j in range(3)] if axis=="col" else [A[i,:] for i in range(3)]
        return any(np.allclose(np.sort(v),tgt,atol=1e-6) for v in vecs)
    tags=[]
    for nm,tgt in (("TM1",T1),("TM2",T2)):
        for ax in ("col","row"):
            if all(has(A,tgt,ax) for A in As): tags.append(nm+ax)
    return tuple(sorted(tags))
subs=bw.subgroup_lattice(); print("subgroups",len(subs))
vs={t:[(H,inv_basis(H,t)) for H in subs] for t in ("TbT","TT","S2")}
vs={t:[(H,b) for H,b in L if viable(b,len(H)*31+min(H)+max(H))] for t,L in vs.items()}
print({t:len(L) for t,L in vs.items()})
names={"TbT":"Tbar x T","TT":"T x T","S2":"Sym2 T"}
summary={}
for tl in ("TbT","TT","S2"):
  for tn in ("TbT","TT","S2"):
    tally=collections.Counter(); ex={}
    for (Hl,bl),(Hn,bn) in itertools.product(vs[tl],vs[tn]):
        nl,nn=2*len(bl),2*len(bn)
        def V(x,bl=bl,bn=bn,nl=nl):
            return Wof(mat(bl,x[:nl]),tl).conj().T@Wof(mat(bn,x[nl:]),tn)
        d=fdim(V,nl+nn,len(Hl)*997+len(Hn)); tg=classify(V,nl+nn,len(Hl)+13*len(Hn))
        tally[(d,tg)]+=1; ex.setdefault((d,tg),(len(Hl),len(Hn)))
    summary[(tl,tn)]=tally
    print(f"\nLEPTON {names[tl]} (Dirac) x NEUTRINO {names[tn]} ({'Majorana' if tn=='S2' else 'Dirac'}) pairs={sum(tally.values())}")
    for k,v in sorted(tally.items(),key=lambda kv:(kv[0][0],kv[0][1])): print("   dim",k[0],"tags",k[1],"count",v,"example orders",ex[k])
print("\nSUMMARY: pairs with a fixed TM column, by family dimension")
for (tl,tn),t in summary.items():
    tm1=sorted({k[0] for k in t if "TM1col" in k[1]}); tm2=sorted({k[0] for k in t if "TM2col" in k[1]})
    n1=sum(v for k,v in t.items() if "TM1col" in k[1]); n2=sum(v for k,v in t.items() if "TM2col" in k[1])
    print(f"lepton {names[tl]:9s} nu {names[tn]:9s}: TM1 dims {tm1} (pairs {n1}); TM2 dims {tm2} (pairs {n2})")
