"""THE FORM-FREE STATEMENT.

Applying an invariant form F is just a functional on H^2(T;W(x)W) = (W(x)W)_{pi_1 T}.
Vanishing for EVERY invariant F therefore says the cup product CLASS itself is zero:

        L_V  u  L_V  =  0    in   H^2(T; W (x) W)

which is form-free, cusp-local, and implies isotropy for every form at once -- hence I = 0.
It is also NON-VACUOUS when dim L_V = 1, where the form-based test was empty:
an alternating form kills <z,z> automatically, but w(z,z) in W(x)W need not vanish.

        w(z,z') = z(mu) (x) mu.z'(lam)  -  z(lam) (x) lam.z'(mu)
"""
import sys, warnings; sys.path.insert(0,'/tmp/sweep'); warnings.filterwarnings("ignore")
from iso import restrict, sl2form
from cup import *
from q12 import *
from q12 import _dot
from fi_lib import get_rho, sym, blockdiag, order3_chars

def kron(P,Q):
    n=len(P); m=len(Q); d=n*m
    return [[mul(P[i//m][k//m],Q[i%m][k%m]) for k in range(d)] for i in range(d)]

NM=sys.argv[1]; MS=tuple(int(c) for c in sys.argv[2])
M,G,gens,rels,mu,lam,rho=get_rho(NM)
base={g:blockdiag([sym(rho[g],m) for m in MS]) for g in gens}
d=sum(m+1 for m in MS); D=d*d
print(f"{NM} germ Sym^{MS} d={d}  dim W(x)W={D}", flush=True)
for psi in [tuple([0]*len(gens))]+list(order3_chars(gens,rels,mu,lam)):
    V={g:scal(powe(OMEGA,psi[i]),base[g]) for i,g in enumerate(gens)}
    R,Bt,A,B,t0=restrict(gens,rels,mu,lam,V,d)
    LV=reduce_mod(R,Bt,2*d); r1=len(LV)
    AA=kron(A,A); BB=kron(B,B)
    # H^2(T; W(x)W) = coinvariants = (W(x)W) / <(AA-1)x, (BB-1)x>
    img=[row for row in msub(AA,eye(D))]+[row for row in msub(BB,eye(D))]
    img=[[img[i][j] for j in range(D)] for i in range(len(img))]
    # the image subspace is spanned by the COLUMNS of (AA-1),(BB-1) -> use transposes
    cols=[[msub(AA,eye(D))[i][j] for i in range(D)] for j in range(D)] + \
         [[msub(BB,eye(D))[i][j] for i in range(D)] for j in range(D)]
    rimg=rank(cols); h2=D-rimg
    ws=[]
    for p in range(r1):
        for q in range(r1):
            z,zp=LV[p],LV[q]
            u,v=z[:d],z[d:]; up,vp=zp[:d],zp[d:]
            Avp=[_dot(A[x],vp) for x in range(d)]; Bup=[_dot(B[x],up) for x in range(d)]
            w=[sub(mul(u[i],Avp[j]), mul(v[i],Bup[j])) for i in range(d) for j in range(d)]
            ws.append(w)
    nonzero_in_H2 = rank(cols+ws)-rimg
    print(f"  psi={psi}: t0={t0} dim L_V={r1} | dim H^2(T;WxW)={h2}"
          f" | CUP CLASSES span dim {nonzero_in_H2} in H^2"
          f" -> {'VANISHES (L_V u L_V = 0)' if nonzero_in_H2==0 else '** NONZERO **'}", flush=True)
