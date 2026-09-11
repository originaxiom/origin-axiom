"""Where does the cup class live when it does NOT vanish?

For W = (+)_i Sym^{m_i}, W(x)W splits into blocks (i,j).  The duality pairing V (x) V* -> C
only ever sees the DIAGONAL blocks i=j (Sym^a and Sym^b are non-isomorphic for a != b, so
Hom_{SL2}(Sym^a, (Sym^b)^*) = 0).  Prediction: any surviving cup class sits purely off-diagonal,
i.e. in a part of H^2 that no SL2-invariant form -- and hence no duality statement -- can see.
"""
import sys, warnings; sys.path.insert(0,'/tmp/sweep'); warnings.filterwarnings("ignore")
from iso import restrict
from cup import *
from q12 import *
from q12 import _dot
from fi_lib import get_rho, sym, blockdiag, order3_chars

NM=sys.argv[1]; MS=tuple(int(c) for c in sys.argv[2])
M,G,gens,rels,mu,lam,rho=get_rho(NM)
base={g:blockdiag([sym(rho[g],m) for m in MS]) for g in gens}
dims=[m+1 for m in MS]; d=sum(dims); off=[sum(dims[:i]) for i in range(len(dims))]
blk=lambda x: max(i for i in range(len(dims)) if off[i]<=x)
def kron(P,Q):
    n=len(P); m=len(Q); D=n*m
    return [[mul(P[i//m][k//m],Q[i%m][k%m]) for k in range(D)] for i in range(D)]
D=d*d
print(f"{NM} germ Sym^{MS}  d={d}  blocks={dims}", flush=True)
for psi in [tuple([0]*len(gens))]+list(order3_chars(gens,rels,mu,lam)):
    V={g:scal(powe(OMEGA,psi[i]),base[g]) for i,g in enumerate(gens)}
    R,Bt,A,B,t0=restrict(gens,rels,mu,lam,V,d)
    LV=reduce_mod(R,Bt,2*d); r1=len(LV)
    AA=kron(A,A); BB=kron(B,B)
    cols=[[msub(AA,eye(D))[i][j] for i in range(D)] for j in range(D)] + \
         [[msub(BB,eye(D))[i][j] for i in range(D)] for j in range(D)]
    rimg=rank(cols)
    ws=[]
    for p in range(r1):
        for q in range(r1):
            z,zp=LV[p],LV[q]
            u,v=z[:d],z[d:]; up,vp=zp[:d],zp[d:]
            Avp=[_dot(A[x],vp) for x in range(d)]; Bup=[_dot(B[x],up) for x in range(d)]
            ws.append([sub(mul(u[i],Avp[j]), mul(v[i],Bup[j])) for i in range(d) for j in range(d)])
    tot=rank(cols+ws)-rimg
    # project each w onto the DIAGONAL blocks (i=j) and onto the OFF-diagonal blocks
    def proj(w,diag):
        return [w[i*d+j] if ((blk(i)==blk(j))==diag) else Z for i in range(d) for j in range(d)]
    wd=[proj(w,True) for w in ws]; wo=[proj(w,False) for w in ws]
    dd=rank(cols+wd)-rimg; do=rank(cols+wo)-rimg
    print(f"  psi={psi}: dim L_V={r1} | cup class spans {tot} in H^2"
          f" | DIAGONAL blocks (what duality sees): {dd} -> {'VANISHES' if dd==0 else '** NONZERO **'}"
          f" | off-diagonal blocks: {do}", flush=True)
