"""Independent check of W34 / 'no thread keeps a record' (own code; does not import the lane's)."""
import itertools, numpy as np
from collections import Counter
from math import comb
np.set_printoptions(precision=4, suppress=True)
# --- free group words: 1=a 2=b -1,-2 inverses
def red(w):
    o=[]
    for x in w:
        if o and o[-1]==-x:o.pop()
        else:o.append(x)
    return o
def inv(w): return [-x for x in reversed(w)]
def app(al,w):
    o=[]
    for x in w: o+= al[x] if x>0 else inv(al[-x])
    return red(o)
def comp(al,be): return {g:app(al,be[g]) for g in (1,2)}   # al o be
AUT={"L":{1:[1],2:[1,2]},"R":{1:[1,2],2:[2]},"P":{1:[2],2:[1]},"I":{1:[-1],2:[-2]}}
def aut_of_word(word,sign=+1):
    phi={1:[1],2:[2]}
    for c in word: phi=comp(phi,AUT[c])   # same composition order as the lane (phi o move); an order-independence check is below
    return comp(AUT["I"],phi) if sign<0 else phi
# --- SU(2) quaternion point
I2=np.eye(2,dtype=complex)
qi=np.array([[1j,0],[0,-1j]]); qj=np.array([[0,1],[-1,0]],dtype=complex)
rho={1:qi,2:qj}; rho[-1]=np.linalg.inv(qi); rho[-2]=np.linalg.inv(qj)
def R2(w):
    M=I2.copy()
    for x in w: M=M@rho[x]
    return M
def sym(g,n):
    # matrix of Sym^n(g) on basis x^{n-r} y^r : (g.f)(x,y)=f(g11 x+g21 y, g12 x+g22 y)  (substitution -> may be anti-hom; fixed below)
    S=np.zeros((n+1,n+1),dtype=complex)
    a,b,c,d=g[0,0],g[0,1],g[1,0],g[1,1]
    import numpy.polynomial.polynomial as P
    for r in range(n+1):
        # (a x + c y)^{n-r} (b x + d y)^r, polynomial in t=y/x
        p1=np.array([1.0+0j]); 
        for _ in range(n-r): p1=np.convolve(p1,[a,c])
        p2=np.array([1.0+0j])
        for _ in range(r): p2=np.convolve(p2,[b,d])
        pr=np.convolve(p1,p2)
        for s in range(n+1): S[s,r]=pr[s]
    return S
rng=np.random.default_rng(0)
def rand_su2():
    v=rng.normal(size=4);v/=np.linalg.norm(v);return np.array([[v[0]+1j*v[1],v[2]+1j*v[3]],[-v[2]+1j*v[3],v[0]-1j*v[1]]])
g1,g2=rand_su2(),rand_su2()
for n in (2,4,6):
    hom=np.allclose(sym(g1@g2,n),sym(g1,n)@sym(g2,n)); anti=np.allclose(sym(g1@g2,n),sym(g2,n)@sym(g1,n))
    assert hom or anti
SYMHOM=np.allclose(sym(g1@g2,4),sym(g1,4)@sym(g2,4))
def S(g,n):
    M=sym(g,n)
    if not SYMHOM: M=M.T   # make a left action? transpose of antihom is hom
    return M
# verify now a hom
assert np.allclose(S(g1@g2,4),S(g1,4)@S(g2,4)),"not hom"
class Block:
    def __init__(s,k):
        s.n=2*k; s.d=s.n+1
        s.rep={x:S(rho[x],s.n) for x in (1,2,-1,-2)}
        d=s.d
        # coboundary space B: v -> ((rho(a)-1)v,(rho(b)-1)v)
        Bm=np.vstack([s.rep[1]-np.eye(d),s.rep[2]-np.eye(d)])
        s.Bm=Bm
        # restriction z->z(c), c=a b a^-1 b^-1 : z(xy)=z(x)+x z(y); z(x^-1)=-x^-1 z(x)
        s.Rc=s.zmap([1,2,-1,-2])
        # basis of B (column space), K = null(Rc)
        s.rB=np.linalg.matrix_rank(Bm,tol=1e-9)
        u,sv,vh=np.linalg.svd(s.Rc); r=(sv>1e-9).sum(); s.rank_res=r
        s.K=vh[r:].conj().T          # columns span K
        ub,sb,vhb=np.linalg.svd(Bm); s.Bcols=ub[:,:s.rB]
        # Q: projection onto complement of B
        s.Q=ub[:,s.rB:].conj().T
        s.h1=2*d-s.rB
        s.private=s.K.shape[1]-s.rB
    def zmap(s,w):
        """matrix (d x 2d) sending (z_a,z_b) to z(w)"""
        d=s.d
        pref=np.eye(d,dtype=complex)   # rho(prefix)
        acc=np.zeros((d,2*d),dtype=complex)
        for x in w:
            ax=abs(x); sel=np.zeros((d,2*d),dtype=complex); sel[:,(ax-1)*d:ax*d]=np.eye(d)
            if x>0: term=sel
            else: term=-s.rep[x]@sel
            acc+= pref@term
            pref=pref@s.rep[x]
        return acc
    def pullback(s,phi):
        """matrix of phi^* on Z^1 = V^2:  (phi^*z)(x)=g^-1 z(phi(x)),  g rho(x) g^-1 = rho(phi x)"""
        # solve g from g rho(x) = rho(phi x) g for x=a,b, g in SL2
        rows=[]
        for x in (1,2):
            Y=R2(phi[x]); X=rho[x]
            # g X - Y g =0 -> (X^T kron I - I kron Y) vec(g)=0 (column-major)
            rows.append(np.kron(X.T,np.eye(2))-np.kron(np.eye(2),Y))
        A=np.vstack(rows); u,sv,vh=np.linalg.svd(A)
        assert sv[-1]<1e-9 and sv[-2]>1e-6, sv
        g=vh[-1].conj().reshape(2,2,order='F'); g/=np.sqrt(np.linalg.det(g))
        Gi=S(np.linalg.inv(g),s.n)
        d=s.d
        P=np.zeros((2*d,2*d),dtype=complex)
        for i,x in enumerate((1,2)):
            P[i*d:(i+1)*d,:]=Gi@s.zmap(phi[x])
        return P
    def kept(s,phis,private=True):
        """dim of classes (private or all) fixed by every phi"""
        mats=[s.Q@(s.pullback(p)-np.eye(2*s.d)) for p in phis]
        M=np.vstack(mats)
        Kb=s.K if private else np.eye(2*s.d)
        T=M@Kb
        sv=np.linalg.svd(T,compute_uv=False)
        sv=np.concatenate([sv,np.zeros(Kb.shape[1]-len(sv))])
        null=(sv<1e-8).sum()
        gap=sv[sv>=1e-8].min() if (sv>=1e-8).any() else np.inf
        base=s.rB
        return null-(s.rB if True else 0), gap
if __name__=="__main__":
    blocks={k:Block(k) for k in (1,2,3)}
    print("table (dim V, h1, rank to puncture, private):",[(b.d,b.h1,b.rank_res,b.private) for b in blocks.values()])
    names={"L":aut_of_word("L"),"R":aut_of_word("R"),"P":aut_of_word("",+1)}
    names["P"]=AUT["P"]; names["-I"]=AUT["I"]
    # NOTE kept() subtracts rB since B-classes are in the null space; for 'all H1' the same
    for nm in ("L","R","P","-I"):
        row={}
        for k,b in blocks.items():
            row[k]=(b.kept([AUT[nm if nm!="-I" else "I"]],True)[0],b.kept([AUT[nm if nm!="-I" else "I"]],False)[0])
        print(nm,"kept (private, all H1) by block k=1,2,3:",row)
    for k,b in blocks.items():
        print("joint L,R  k=",k,b.kept([AUT["L"],AUT["R"]],True),b.kept([AUT["L"],AUT["R"]],False),
              " joint L,R,P,-I:",b.kept([AUT["L"],AUT["R"],AUT["P"],AUT["I"]],True)[0])
    # rank three = k in {1,2}: private total and L,R,P kept
    for nm in ("L","R","P"):
        print("rank 3 (k=1,2) private kept by",nm,sum(blocks[k].kept([AUT[nm]],True)[0] for k in (1,2)),
              "| rank 4 (k=1,2,3):",sum(blocks[k].kept([AUT[nm]],True)[0] for k in (1,2,3)))
    # states
    from itertools import product
    def states(nmax=12):
        out=[]
        for n in range(2,nmax+1):
            seen=set()
            for bits in product("LR",repeat=n):
                w="".join(bits)
                if "L" not in w or "R" not in w: continue
                rots=[w[i:]+w[:i] for i in range(n)]
                if len(set(rots))<n: continue
                sw=w.translate(str.maketrans("LR","RL"))
                canon=min(rots+[sw[i:]+sw[:i] for i in range(n)])
                if canon in seen: continue
                seen.add(canon);out.append(canon)
        return out
    st=states(); print("number of cyclic states",len(st),"x2 =",2*len(st))
    worst=np.inf; nfix=0; nfixall=Counter() if False else {}
    allfix={}
    for w in st:
        for sg in (+1,-1):
            phi=aut_of_word(w,sg)
            for k,b in blocks.items():
                kp,gap=b.kept([phi],True)
                worst=min(worst,gap)
                if kp: nfix+=1
                ka,_=b.kept([phi],False)
                allfix[(k,ka)]=allfix.get((k,ka),0)+1
    print("threads keeping a private class (any block):",nfix," smallest nonzero singular value of (phi*-1) on private part:",worst)
    print("kept on ALL of H1 by (block k, dimension kept) -> count:",allfix)
    # robustness: compose in the opposite order
    nfix2=0
    for w in st[:200]:
        for sg in (+1,-1):
            phi={1:[1],2:[2]}
            for c in reversed(w): phi=comp(phi,AUT[c])
            if sg<0: phi=comp(AUT["I"],phi)
            for k,b in blocks.items(): nfix2+= b.kept([phi],True)[0]>0
    print("opposite composition order on first 200 states: keeping count",nfix2)
    for w in ["LR","RL","LLR","LRLLR","LLLLLLLLLLLR","LRLRLRLRLRLL","LLRLLRLLRLLR","LLRRLRLLRRLR"]:
        phi=aut_of_word(w,+1)
        print(w,"private kept k=1,2,3:",[blocks[k].kept([phi],True)[0] for k in (1,2,3)],"| minus sign:",[blocks[k].kept([aut_of_word(w,-1)],True)[0] for k in (1,2,3)])
