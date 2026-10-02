import json, itertools, random
import sympy as sp
from sympy import Rational as R, Matrix, eye, zeros
import mpmath as mp

import os as _os
OUT=_os.path.dirname(_os.path.abspath(__file__))+'/'   # the one change made when this file was placed in the arc: its output directory
# words: list of (gen, exp) gen in 'm','n'
def W(s):
    # string like "m n M N" with uppercase = inverse
    return [(c.lower(), -1 if c.isupper() else 1) for c in s.split()]
REL = W("m n M N m N M n m N")
LONG = W("n M N m m N M n")

def rho(q):
    t = sp.nsimplify(q)/2
    M = Matrix([[1,0,1,t-1],[0,1,1,t],[0,0,1,t+R(1,2)],[0,0,0,1]])
    N = Matrix([[1,0,0,0],[2+1/t,1,0,0],[2,1,1,0],[1,1,0,1]])
    return M,N
def dual(mats):
    return tuple((A.inv()).T for A in mats)

def ev(word, mats, one=None):
    M,N = mats
    d = M.shape[0]
    P = eye(d)
    for g,e in word:
        A = M if g=='m' else N
        P = P*(A if e==1 else A.inv())
    return P

SIGMAS={}
for a in (1,-1):
    for b in (1,-1):
        SIGMAS[f"(m,n)->(m^{a:+d},n^{b:+d})"] = ((('m',a),),(('n',b),))
        SIGMAS[f"(m,n)->(n^{a:+d},m^{b:+d})"] = ((('n',a),),(('m',b),))
IOTA = "(m,n)->(m^-1,n^-1)"
def apply_sigma(sig, word):
    sm, sn = sig
    out=[]
    for g,e in word:
        img = sm if g=='m' else sn
        if e==1: out += list(img)
        else: out += [(h,-f) for h,f in reversed(img)]
    return out

def sigma_mats(sig, mats):
    sm,sn = sig
    return (ev(list(sm),mats), ev(list(sn),mats))

def intertwiners(A, T):
    """solve X A[g] = T[g] X for g=m,n; A,T pairs of matrices. return nullspace basis list of 4x4"""
    d=4
    rows=[]
    for k in range(2):
        a,tt = A[k],T[k]
        for i in range(d):
            for j in range(d):
                row=[0]*(d*d)
                for p in range(d):
                    # sum_p X[i,p] a[p,j]
                    row[i*d+p] += a[p,j]
                    # - sum_p tt[i,p] X[p,j]
                    row[p*d+j] -= tt[i,p]
                rows.append(row)
    Mx = Matrix(rows)
    ns = Mx.nullspace()
    return [Matrix(d,d,list(v)) for v in ns]

def conj_decision(A,T,rng=random.Random(1)):
    B = intertwiners(A,T)
    dim=len(B)
    if dim==0: return dict(dim=0, conjugate=False, note="no nonzero intertwiner")
    if dim==1:
        det = sp.nsimplify(B[0].det())
        return dict(dim=1, conjugate=(det!=0), det=str(det))
    # generic
    dets=[]
    for _ in range(4):
        c=[rng.randint(-9,9) for _ in B]
        X=sum((ci*Bi for ci,Bi in zip(c,B)), zeros(4,4))
        dets.append(X.det())
    inv = any(d!=0 for d in dets)
    return dict(dim=dim, conjugate=inv, note="dim>1: generic combos tested", dets=[str(d) for d in dets])

QS=[R(2),R(3),R(5,2),R(7,3),R(1,5)]
RES={}
tmat = lambda q,star: (dual(rho(q)) if star else rho(q))
def targets(q):
    return {"rho_q":rho(q),"rho_q*":dual(rho(q)),"rho_1/q":rho(1/q),"rho_1/q*":dual(rho(1/q))}

# C0
C0={}
for q in QS+[R(1)]:
    r=rho(q); res={}
    res['relator_identity']=bool(ev(REL,r)==eye(4))
    res['rho_q~rho_1/q']=conj_decision(r,rho(1/q))
    res['rho_q~rho_q*']=conj_decision(r,dual(r))
    res['rho_q*~rho_1/q']=conj_decision(dual(r),rho(1/q))
    if q==1:
        T=targets(q)
        names=list(T)
        res['all_pairs_q=1']={f"{a}~{b}":conj_decision(T[a],T[b])['conjugate'] for a,b in itertools.combinations(names,2)}
    C0[str(q)]=res
RES['C0']=C0; print('C0 done',flush=True)

# C1
C1={}
for name,sig in SIGMAS.items():
    d={}
    d['relator_identity_at_q']={str(q):bool(ev(apply_sigma(sig,REL),rho(q))==eye(4)) for q in [R(2),R(3),R(5,2)]}
    # longitude trace
    tr={}
    for q in QS:
        r=rho(q)
        tl = ev(LONG,r).trace(); tli = ev(LONG,r).inv().trace()
        ts = ev(apply_sigma(sig,LONG),r).trace()
        tr[str(q)]=dict(tr_l=str(tl),tr_linv=str(tli),tr_sigma_l=str(ts),
                        eq_l=bool(ts==tl), eq_linv=bool(ts==tli))
    d['longitude']=tr
    C1[name]=d
RES['C1']=C1; print('C1 done',flush=True)

# orientation via SL2(C)
mp.mp.dps=60
def sl2(z):
    return (mp.matrix([[1,1],[0,1]]), mp.matrix([[1,0],[z,1]]))
def evmp(word,mats):
    P=mp.eye(2)
    for g,e in word:
        A=mats[0] if g=='m' else mats[1]
        P=P*(A if e==1 else mp.inverse(A))
    return P
cand=[]
for zs in (mp.mpc(-0.5,mp.sqrt(3)/2), mp.mpc(-0.5,-mp.sqrt(3)/2), mp.mpc(0.5,mp.sqrt(3)/2), mp.mpc(0.5,-mp.sqrt(3)/2)):
    P=evmp(REL,sl2(zs))
    err=mp.norm(P-mp.eye(2))
    cand.append((str(zs),float(err)))
RES['orient_candidates_z_and_relator_err']=cand
zgood=None
for zs in (mp.mpc(-0.5,mp.sqrt(3)/2), mp.mpc(-0.5,-mp.sqrt(3)/2), mp.mpc(0.5,mp.sqrt(3)/2), mp.mpc(0.5,-mp.sqrt(3)/2)):
    if mp.norm(evmp(REL,sl2(zs))-mp.eye(2))<mp.mpf(10)**-40: zgood=zs;break
ORI={}
if zgood is not None:
    P=sl2(zgood)
    # all words in m,n,M,N up to length 7 with zero exponent sum, no free reduction needed
    words=[]
    for L in range(1,9):
        for w in itertools.product([('m',1),('m',-1),('n',1),('n',-1)],repeat=L):
            if sum(e for g,e in w)==0:
                words.append(list(w))
    random.Random(5).shuffle(words)
    words=words[:1500]
    for name,sig in SIGMAS.items():
        pres=conj=True; npres=nconj=0; nonreal=0
        for w in words:
            t0=evmp(w,P); t0=t0[0,0]+t0[1,1]
            ws=apply_sigma(sig,w)
            t1=evmp(ws,P); t1=t1[0,0]+t1[1,1]
            if abs(t1-t0)>1e-35: pres=False
            else: npres+=1
            if abs(t1-mp.conj(t0))>1e-35: conj=False
            else: nconj+=1
            if abs(t0.imag)>1e-35: nonreal+=1
        ORI[name]=dict(preserved=pres,conjugated=conj,n_words=len(words),n_nonreal_chars=nonreal,
                       orientation=("preserving" if pres and not conj else "reversing" if conj and not pres else "both(real chars)" if pres and conj else "neither"))
    ORI['_z']=str(zgood)
RES['orientation']=ORI; print('ori done',flush=True)

# C2
C2={}
for q in QS:
    r=rho(q); T=targets(q)
    tab={}
    for name,sig in SIGMAS.items():
        S=sigma_mats(sig,r)
        row={}
        for tn,Tm in T.items():
            row[tn]=conj_decision(S,Tm)
        tab[name]=row
    C2[str(q)]=tab
RES['C2']=C2; print('C2 done',flush=True)

json.dump(RES,open(OUT+'route2_results_numeric.json','w'),indent=1,default=str)

# C2 symbolic for iota using DomainMatrix over QQ(q)
from sympy.polys.matrices import DomainMatrix
from sympy import QQ
q=sp.symbols('q')
def rho_sym():
    t=q/2
    M=Matrix([[1,0,1,t-1],[0,1,1,t],[0,0,1,t+R(1,2)],[0,0,0,1]])
    N=Matrix([[1,0,0,0],[2+1/t,1,0,0],[2,1,1,0],[1,1,0,1]])
    return M,N
def build_rows(A,T):
    d=4; rows=[]
    for k in range(2):
        a,tt=A[k],T[k]
        for i in range(d):
            for j in range(d):
                row=[0]*(d*d)
                for p in range(d):
                    row[i*d+p]+=a[p,j]; row[p*d+j]-=tt[i,p]
                rows.append(row)
    return Matrix(rows)
def ns_sym(A,T):
    Mx=build_rows(A,T).applyfunc(sp.cancel)
    K=QQ.frac_field(q)
    dm=DomainMatrix.from_Matrix(Mx).convert_to(K)
    ns=dm.nullspace()
    return [Matrix(4,4,list(v)) for v in ns.to_Matrix().tolist()]
rs=rho_sym()
SY={}
S=(rs[0].inv().applyfunc(sp.cancel), rs[1].inv().applyfunc(sp.cancel))
dualq=lambda ms: tuple(A.inv().T.applyfunc(sp.cancel) for A in ms)
rinv=tuple(A.subs(q,1/q).applyfunc(sp.cancel) for A in rs)
for tn,Tm in {"rho_q":rs,"rho_q*":dualq(rs),"rho_1/q":rinv,"rho_1/q*":dualq(rinv)}.items():
    B=ns_sym(S,Tm); d=dict(dim=len(B))
    if len(B)==1:
        X=B[0].applyfunc(sp.cancel)
        d['X']=str(X.tolist()); d['det']=str(sp.factor(sp.cancel(X.det())))
    elif len(B)>1:
        cs=sp.symbols('c0:%d'%len(B))
        X=sum((c*b for c,b in zip(cs,B)),zeros(4,4))
        d['det_generic']=str(sp.factor(sp.cancel(X.det())))
    print('sym',tn,d,flush=True)
    SY[tn]=d
RES['C2_symbolic_iota']=SY
json.dump(RES,open(OUT+'route2_results.json','w'),indent=1,default=str)

# print tables
print("C0")
for q,r in C0.items():
    print(q, 'relator_id',r['relator_identity'],
          'rho~rho1/q',r['rho_q~rho_1/q']['dim'],r['rho_q~rho_1/q']['conjugate'],
          'rho~rho*',r['rho_q~rho_q*']['dim'],r['rho_q~rho_q*']['conjugate'],
          'rho*~rho1/q',r['rho_q*~rho_1/q']['dim'],r['rho_q*~rho_1/q']['conjugate'])
    if 'all_pairs_q=1' in r: print('  q=1 pairs', r['all_pairs_q=1'])
print("C1")
for n,d in C1.items():
    print(n,d['relator_identity_at_q'])
    for q,t in d['longitude'].items():
        print('   q',q,'eq_l',t['eq_l'],'eq_linv',t['eq_linv'])
print("orientation",json.dumps(ORI,indent=1))
print(cand)
print("C2")
for q,tab in C2.items():
    print("q=",q)
    for n,row in tab.items():
        print("  ",n,{tn:(r['conjugate'],r['dim']) for tn,r in row.items()})
print("SYM",json.dumps(SY,indent=1))
