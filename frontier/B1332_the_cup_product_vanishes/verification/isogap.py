"""B1332 section 1 says: 'If L_V is isotropic then L_V <= L_V^perp = L_{V*}, so dim L_V <= t_1/2.
The same argument applied to V* gives dim L_{V*} <= t_1/2.'  The second sentence needs L_{V*} to be
isotropic TOO -- it is not automatic.

The m010 sector from B1335 is a concrete case: r_1 = 0, so L_V = 0, which is isotropic for free,
and yet I = 1. Check directly that L_{V*} is NOT isotropic there, which is what saves the identity.
"""
import sys, warnings, itertools; sys.path.insert(0,'/tmp/sweep'); warnings.filterwarnings("ignore")
import snappy
import index_lib as L
from mc_lib import analyse_mc, dual_rho
from broad import sym_p, chars_of_order
P=13
def inv_forms_p(mats,d,p):
    """all F with g^T F g = F, over F_p"""
    rows=[]
    for g in mats:
        for a in range(d):
            for b in range(d):
                row=[0]*(d*d)
                for i in range(d):
                    for j in range(d): row[i*d+j]=(row[i*d+j]+g[i][a]*g[j][b])%p
                row[a*d+b]=(row[a*d+b]-1)%p
                rows.append(row)
    ns=L.nullspace(rows,p,d*d)
    return [[[v[i*d+j] for j in range(d)] for i in range(d)] for v in ns]
def cocyc(A,B,d,p):
    rows=[]
    for x in range(d):
        row=[0]*(2*d)
        for y in range(d):
            row[y]=(-(B[x][y]-(1 if x==y else 0)))%p
            row[d+y]=(A[x][y]-(1 if x==y else 0))%p
        rows.append(row)
    return L.nullspace(rows,p,2*d)
def cup(z,zp,A,B,F,d,p):
    u,v=z[:d],z[d:]; up,vp=zp[:d],zp[d:]
    Avp=[sum(A[x][y]*vp[y] for y in range(d))%p for x in range(d)]
    Bup=[sum(B[x][y]*up[y] for y in range(d))%p for x in range(d)]
    def pr(a,b): return sum(F[i][j]*a[i]*b[j] for i in range(d) for j in range(d))%p
    return (pr(u,Avp)-pr(v,Bup))%p
def reduce_mod(basis,Bs,p):
    out=[];cur=[list(b) for b in Bs]
    for v in basis:
        if L.rank(cur+[v],p)>L.rank(cur,p): cur.append(list(v)); out.append(list(v))
    return out

M=snappy.Manifold('m010'); G=M.fundamental_group()
gens=list(G.generators()); rels=list(G.relators()); per=list(G.peripheral_curves()); mu,lam=per[0]
S=[[[a,b],[c,d]] for a in range(P) for b in range(P) for c in range(P) for d in range(P) if (a*d-b*c)%P==1]
reps=[]
for tup in itertools.product(S,repeat=len(gens)):
    rho=dict(zip(gens,tup))
    if all(L.word_eval(r,rho,P,2)==L.eye(2) for r in rels):
        reps.append(rho)
        if len(reps)>=2: break
rho2=reps[1]; chi=(4,12); m=3; d=m+1
base={g:sym_p(rho2[g],m,P) for g in gens}
V={g:[[(chi[i]*base[g][x][y])%P for y in range(d)] for x in range(d)] for i,g in enumerate(gens)}
Vd=dual_rho(V,gens,P,d)
# the SL2-invariant form on Sym^m, over F_p
g1=[[1,1],[0,1]]; g2=[[1,0],[1,1]]
Fs=inv_forms_p([sym_p(g1,m,P),sym_p(g2,m,P)],d,P)
# NOTE: this form is invariant for Sym^m, NOT for the DUAL module. Each module gets its own.
print(f"m010 Sym^{m} chi={chi} over F_{P}")
print(f"  SL2-invariant forms on Sym^{m}: {len(Fs)}")
F=Fs[0]
symm=all(F[i][j]==F[j][i] for i in range(d) for j in range(d))
alt =all((F[i][j]+F[j][i])%P==0 for i in range(d) for j in range(d))
print(f"  the form is symmetric={symm} alternating={alt} (m={m} odd -> alternating expected)")
for nm,W in (('V',V),('V*',Vd)):
    A=analyse_mc(gens,rels,per,W,P,d)
    Au=L.word_eval(mu,W,P,d); Bu=L.word_eval(lam,W,P,d)
    Bt=[]
    for k in range(d):
        Bt.append([(Au[x][k]-(1 if x==k else 0))%P for x in range(d)]+
                  [(Bu[x][k]-(1 if x==k else 0))%P for x in range(d)])
    Lv=reduce_mod(A['R'] if 'R' in A else [],Bt,P) if False else None
    # rebuild the restricted cocycles
    from mc_lib import cusp_data
    import mc_lib
    g=len(gens); J=[]
    for r in rels:
        bl=[L.fox(r,x,W,P,d) for x in gens]
        for a in range(d): J.append([bl[j][a][b] for j in range(g) for b in range(d)])
    Zs=L.nullspace(J,P,g*d)
    FXm=[L.fox(mu,x,W,P,d) for x in gens]; FXl=[L.fox(lam,x,W,P,d) for x in gens]
    R=[]
    for v in Zs:
        z=[v[j*d:(j+1)*d] for j in range(g)]; row=[]
        for FX in (FXm,FXl):
            o=[0]*d
            for j in range(g):
                for a in range(d): o[a]=(o[a]+sum(FX[j][a][b]*z[j][b] for b in range(d)))%P
            row+=o
        R.append(row)
    Lv=reduce_mod(R,Bt,P)
    # the form must be invariant for THIS module's own cusp matrices -- solve, do not reuse
    Fl=inv_forms_p([Au,Bu],d,P)
    Gms=[[[cup(x,y,Au,Bu,Fx,d,P) for y in Lv] for x in Lv] for Fx in Fl]
    iso=all(all(v==0 for row in Gm for v in row) for Gm in Gms)
    Gm=Gms[0] if Gms else []
    # the ambient pairing, for contrast
    Zt=cocyc(Au,Bu,d,P); H=reduce_mod(Zt,Bt,P)
    GH=[[cup(x,y,Au,Bu,Fl[0],d,P) for y in H] for x in H] if Fl else []
    print(f"  {nm}: t0={A['t0']} t1={A['t1']} r1={A['r1']} dim L={len(Lv)}"
          f" | invariant forms {len(Fl)} | L ISOTROPIC for ALL of them: {iso}"
          f" | ambient H^1 dim {len(H)}")
    if Gm: print(f"      Gram on L({nm}) w.r.t. one invariant form = {Gm}")
    print(f"      dim L = {len(Lv)} vs t_1/2 = {A['t1']/2}"
          f"  -> isotropy could give dim <= t_1/2: {len(Lv)<=A['t1']/2}")
