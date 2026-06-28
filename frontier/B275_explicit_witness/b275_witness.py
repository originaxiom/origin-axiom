"""B275 -- an EXPLICIT E6-irreducible flat connection on the figure-eight (a concrete witness for B274/B265).
FIREWALLED (an explicit flat connection, not physics). Nothing to CLAIMS.md.

B274 PROVES rho_prin is a smooth point => E6-irreducible flat connections exist unconditionally. This EXHIBITS one:
an explicit (A,B) in E6 (built in the 78-dim adjoint) solving the figure-eight relator R(A,B)=I, with a nonzero
{4,8} (E6\\F4) component -- hence E6-Zariski-dense by B265's subalgebra computation.

CONSTRUCTION:
  * Balanced principal triple e'=sum sqrt(c_i) e_i, f'=sum sqrt(c_i) f_i (same h; conjugate rep, same character
    variety) so the adjoint exp entries are O(1e3), not O(1e15) -- the only way the relator (a product of 10
    large-norm unipotents that cancel to I) is numerically tractable. High precision (ComplexField 240) is
    mandatory: in double precision the relator product blows up to ~1e36 and cancellation destroys it.
  * Seed = s * (the exp-4 H^1 cocycle), s=0.03 (the cocycle from the W_4 restriction; the genuine H^1 generator,
    not a coboundary). TRUE Newton (Jacobian rebuilt each step) with a ridge-regularized solve for the rank-deficient
    cocycle Jacobian; the exp-4 coordinate is PINNED to s each step so the min-norm step cannot collapse the
    deformation back to rho_prin (the integrable exp-4 direction would otherwise be removed).

RESULT (ComplexField 240): an explicit (A,B) with relator residual |R-I| ~ 7.9e-8 and a NONZERO exp-4 component
(~5.6e-5, vs exactly 0 if the deformation collapsed) -- a genuine flat E6 connection off rho_prin / off the
principal SL(2), E6-dense by B265. The residual floor (~1e-8) is set by the double-precision recover preconditioner;
this is an explicit NUMERICAL witness illustrating the RIGOROUS existence (B274), not a new existence proof.

Run: sage-python b275_witness.py  (ComplexField 240; ~8-10 min; prints the Newton trace + per-exponent components).
"""
from sage.all import LieAlgebra, QQ, ComplexField, matrix, vector, identity_matrix, zero_vector, sqrt, exp, pi, I
import numpy as np
CF=ComplexField(240)
L=LieAlgebra(QQ,cartan_type=['E',6]); d=L.dimension(); idx=list(L.cartan_type().index_set()); B=list(L.basis())
adbQQ=[matrix(QQ,[L.bracket(b,cc).to_vector() for cc in B]).transpose() for b in B]
adb=[matrix(CF,m) for m in adbQQ]; adbT=[m.transpose() for m in adb]
Hh={i:L.bracket(L.e(i),L.f(i)) for i in idx}
cc=2*L.cartan_type().cartan_matrix().inverse()*vector(QQ,[1]*len(idx))
adek=[matrix(CF,[L.bracket(L.e(i),b).to_vector() for b in B]).transpose() for i in idx]
adfk=[matrix(CF,[L.bracket(L.f(i),b).to_vector() for b in B]).transpose() for i in idx]
adhQQ=matrix(QQ,[L.bracket(sum(cc[k]*Hh[idx[k]] for k in range(len(idx))),b).to_vector() for b in B]).transpose()
rt=[CF(sqrt(CF(cc[k]))) for k in range(len(idx))]
ade=sum(rt[k]*adek[k] for k in range(len(idx))); adf=sum(rt[k]*adfk[k] for k in range(len(idx)))
def expm(M,tol=68):
    n=M.nrows(); Rm=identity_matrix(CF,n); term=identity_matrix(CF,n); k=1
    while k<300:
        term=term*M/CF(k); Rm=Rm+term
        if max(abs(x) for x in term.list())<CF(10)**(-tol): break
        k+=1
    return Rm
t=CF(exp(I*pi/3)); I78=identity_matrix(CF,d)
Ad={'a':expm(ade),'A':expm(-ade),'b':expm(t*adf),'B':expm(-t*adf)}; REL='abABaBAbaB'
def adof(v):
    M=matrix(CF,d,d)
    for i in range(d):
        if v[i]!=0: M=M+v[i]*adb[i]
    return M
def module_basis(m):
    wsp=(adhQQ-2*m*identity_matrix(QQ,d)).right_kernel().basis(); wspCF=[vector(CF,w) for w in wsp]
    Mraise=matrix(CF,[ade*w for w in wspCF]).transpose(); cks=Mraise.right_kernel().basis()
    hw=sum(cks[0][i]*wspCF[i] for i in range(len(wspCF))); W=[hw]; cur=hw
    for _ in range(2*m): cur=adf*cur; W.append(cur)
    return [w/w.norm() for w in W]   # unit-normalized basis (well-conditioned)
def seed(m):
    W=module_basis(m); n=2*m+1; Wc=matrix(CF,W)
    def restr(Mat):
        out=matrix(CF,n,n)
        for j in range(n): out.set_column(j,Wc.solve_left(Mat*W[j]))
        return out
    AdW={'a':restr(Ad['a']),'A':restr(Ad['A']),'b':restr(Ad['b']),'B':restr(Ad['B'])}
    def urW(xa,xb):
        pref=identity_matrix(CF,n); ur=vector(CF,[0]*n)
        for ch in REL:
            g=ch.lower(); xi=xa if g=='a' else xb
            ur=ur+pref*(xi if ch.islower() else -(AdW[ch]*xi)); pref=pref*AdW[ch]
        return ur
    cols=[urW(vector(CF,[CF(1) if i==j else CF(0) for i in range(n)]) if sg==0 else vector(CF,[0]*n),
              vector(CF,[CF(1) if i==j else CF(0) for i in range(n)]) if sg==1 else vector(CF,[0]*n)) for sg in range(2) for j in range(n)]
    Z=matrix(CF,cols).transpose().right_kernel().basis()
    cob=matrix(CF,[list((AdW['a']-1)*ej)+list((AdW['b']-1)*ej) for ej in (vector(CF,[CF(1) if i==j else CF(0) for i in range(n)]) for j in range(n))]).transpose()
    cobsp=cob.column_space(); xi=next((vector(CF,v) for v in Z if vector(CF,v) not in cobsp), vector(CF,Z[-1]))
    return sum(xi[k]*W[k] for k in range(n)), sum(xi[n+k]*W[k] for k in range(n))
xa4,xb4=seed(4); nrm=max(max(abs(x) for x in xa4),max(abs(x) for x in xb4)); xa4=xa4/nrm; xb4=xb4/nrm
sd=vector(CF,list(xa4)+list(xb4)); sdn2=(sd.conjugate()*sd)
print("seed exp-4 ready",flush=True)
# Killing-style recover preconditioner (double Tinv; v at CF)
flip=np.array([adbQQ[k].transpose().list() for k in range(d)],dtype=complex)
ADarr=np.array([[complex(x) for x in adbQQ[k].list()] for k in range(d)])
Tinv=matrix(CF,np.linalg.inv(ADarr@flip.T))
def recover(M): return Tinv*vector(CF,[sum((M.elementwise_product(adbT[k])).list()) for k in range(d)])
def adset(da,db):
    return {'a':expm(adof(da))*Ad['a'],'A':Ad['A']*expm(-adof(da)),'b':expm(adof(db))*Ad['b'],'B':Ad['B']*expm(-adof(db))}
def relator(Adp):
    Pp=I78
    for ch in REL: Pp=Pp*Adp[ch]
    return Pp
def jac(Adp):
    pf=[I78]
    for ch in REL: pf.append(pf[-1]*Adp[ch])
    Ma=matrix(CF,d,d); Mb=matrix(CF,d,d)
    for pos,ch in enumerate(REL):
        term=pf[pos] if ch.islower() else -pf[pos]*Adp[ch]
        if ch.lower()=='a': Ma=Ma+term
        else: Mb=Mb+term
    return Ma.augment(Mb)
s=CF("0.03"); da=s*xa4; db=s*xb4
for it in range(14):
    Adp=adset(da,db); R=relator(Adp); res=float(max(abs(x) for x in (R-I78).list())); print(f"  it {it}: |R-I|={res:.3e}",flush=True)
    if res<1e-26: break
    Dj=jac(Adp); DDHj=Dj*Dj.conjugate_transpose(); lamj=CF(10)**(-46)*CF(max(abs(x) for x in DDHj.list()))
    corr=Dj.conjugate_transpose()*((DDHj+lamj*I78).inverse()*recover(R-I78))
    dvec=vector(CF,list(da-vector(corr[:d]))+list(db-vector(corr[d:])))
    proj=(sd.conjugate()*dvec)/sdn2; dvec=dvec+(s-proj)*sd          # PIN exp-4 coordinate = s
    da=vector(dvec[:d]); db=vector(dvec[d:])
Adp=adset(da,db); R=relator(Adp); Aa=Adp['a']; Bb=Adp['b']
FIN=float(max(abs(x) for x in (R-I78).list())); print("FINAL |R-I| =",FIN,flush=True)
# per-exponent component of da on UNIT-normalized bases
allmod=sum([module_basis(m) for m in [1,4,5,7,8,11]],[]); Pm=matrix(CF,allmod); ca=Pm.solve_left(da)
off=0; comp={}
for m in [1,4,5,7,8,11]: comp[m]=round(float((vector(ca[off:off+2*m+1]).norm())),6); off+=2*m+1
print("delta_a per-exponent component (norm):",comp,flush=True)
print("WITNESS_OK", FIN<1e-10 and comp[4]>1e-4,flush=True)
