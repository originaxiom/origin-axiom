"""Direct quadratic-field replay; no SymPy or native-science imports."""
import importlib.util
import json
from functools import lru_cache
from itertools import combinations
from math import factorial
from pathlib import Path

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('cyclic_literal_reference',HERE.parent/'silver_operator_gate_2026_10_05/reference.py')
old=importlib.util.module_from_spec(spec);spec.loader.exec_module(old)
K=old.K


def Z(n,m=None):return [[0]*(n if m is None else m) for _ in range(n)]
def I(n):return [[int(i==j) for j in range(n)] for i in range(n)]
def tr(a):return [list(x) for x in zip(*a)]
def add(a,b,sign=1):return [[x+sign*y for x,y in zip(row,other)] for row,other in zip(a,b)]
def scale(a,c):return [[x*c for x in row] for row in a]
def zero(a):return not any(x for row in a for x in row)
def equal(a,b):return zero(add(a,b,-1))


def mm(a,b):
    out=Z(len(a),len(b[0]))
    for i,row in enumerate(a):
        for k,x in enumerate(row):
            if x:
                for j,y in enumerate(b[k]):
                    if y:out[i][j]+=x*y
    return out


def cat(a,b):return [x+y for x,y in zip(a,b)]
def stack(a,b):return a+b


def diag(*mats):
    out=Z(sum(len(a) for a in mats),sum(len(a[0]) for a in mats));r=c=0
    for a in mats:
        for i,row in enumerate(a):out[r+i][c:c+len(row)]=row
        r+=len(a);c+=len(a[0])
    return out


def reduced(a):
    out=[[x if isinstance(x,K) else K(x) for x in row] for row in a]
    piv=[];r=0
    for c in range(len(out[0])):
        p=next((j for j in range(r,len(out)) if out[j][c]),None)
        if p is None:continue
        out[r],out[p]=out[p],out[r];v=out[r][c];out[r]=[x/v for x in out[r]]
        for j in range(len(out)):
            if j!=r and out[j][c]:
                v=out[j][c];out[j]=[x-v*y if y else x for x,y in zip(out[j],out[r])]
        piv.append(c);r+=1
        if r==len(out):break
    return out,piv


def rank(a):return len(reduced(a)[1]) if a and a[0] else 0


def inverse(a):
    out,piv=reduced(cat(a,I(len(a))))
    assert piv[:len(a)]==list(range(len(a)))
    return [row[len(a):] for row in out]


def null(a):
    out,piv=reduced(a);free=[j for j in range(len(a[0])) if j not in piv];k=Z(len(a[0]),len(free))
    for i,j in enumerate(free):
        k[j][i]=1
        for r,p in enumerate(piv):k[p][i]=-out[r][j]
    return k


def project(k,g):
    if not k[0]:return Z(len(k))
    return mm(mm(k,inverse(mm(mm(tr(k),g),k))),mm(tr(k),g))


def logarithm(p):
    z=add(p,I(len(p)),-1);power=I(len(p));out=Z(len(p))
    for j in range(1,len(p)+1):
        power=mm(power,z)
        if zero(power):return out
        out=add(out,scale(power,K((-1)**(j+1))/j))
    raise ValueError('not unipotent')


def series(a,integral=False):
    power=I(len(a));out=I(len(a))
    for j in range(1,len(a)+1):
        power=mm(power,a)
        if zero(power):return out
        out=add(out,scale(power,K(1)/factorial(j+int(integral))))
    raise ValueError('not nilpotent')


def wedge_derivative(a):
    pairs=list(combinations(range(len(a)),2));out=Z(len(pairs))
    for i,(r,s) in enumerate(pairs):
        for j,(u,v) in enumerate(pairs):
            out[i][j]=a[r][u]*int(s==v)-a[s][u]*int(r==v)+int(r==u)*a[s][v]-int(s==u)*a[r][v]
    return out


def basis5():
    basis=[]
    for i in range(5):
        for j in range(5):
            if i!=j:
                a=Z(5);a[i][j]=1;basis.append(a)
    for i in range(4):
        a=Z(5);a[i][i]=1;a[4][4]=-1;basis.append(a)
    return basis


def ad(a,basis):
    cols=[]
    for b in basis:
        z=add(mm(a,b),mm(b,a),-1)
        assert sum(z[i][i] for i in range(5))==0
        cols.append([z[i][j] for i in range(5) for j in range(5) if i!=j]+[z[i][i] for i in range(4)])
    return tr(cols)


def gram(basis,hermitian=False):
    return [[sum(x[i][j]*y[i][j] if hermitian else x[i][j]*y[j][i] for i in range(5) for j in range(5)) for y in basis] for x in basis]


def ad_group(a,basis):
    ai=inverse(a);cols=[]
    for x in basis:
        z=mm(mm(a,x),ai)
        cols.append([z[i][j] for i in range(5) for j in range(5) if i!=j]+[z[i][i] for i in range(4)])
    return tr(cols)


def word(rep,text):
    letters=dict(rep);letters.update({g.upper():inverse(x) for g,x in rep.items()});out=I(len(rep['a']))
    for c in text:out=mm(out,letters[c])
    return out


@lru_cache(None)
def literal():
    data=json.loads((HERE.parent/'silver_operator_gate_2026_10_05/candidate.json').read_text())
    v=old.four(data);c=[K(a,b) for a,b in data['cocycle_Qsqrt2_pairs']];w=old.extension(v,c)
    assert all(equal(word(w,r),I(5)) for r in data['relators'])
    p,q=[word(w,r) for r in data['cusp_words']]
    assert all(equal(word(w,r),diag(word(v,r),I(1))) for r in data['cusp_words'])
    return data,w,p,q,logarithm(p),logarithm(q)


def contraction(a,b,g=None):
    n=len(a);g=I(n) if g is None else g;g1=diag(g,g);d0=stack(a,b);d1=cat(scale(b,-1),a)
    t0=mm(mm(inverse(g),tr(d0)),g1);t1=mm(mm(inverse(g1),tr(d1)),g)
    p0=project(null(d0),g);p2=project(null(t1),g)
    h1=mm(add(inverse(add(mm(t0,d0),p0)),p0,-1),t0)
    h2=mm(t1,add(inverse(add(mm(d1,t1),p2)),p2,-1))
    p1=add(add(I(2*n),mm(d0,h1),-1),mm(h2,d1),-1)
    d=Z(4*n);h=Z(4*n)
    for i in range(2*n):
        d[n+i][:n]=d0[i];h[n+i][3*n:]=h2[i]
    for i in range(n):
        d[3*n+i][n:3*n]=d1[i];h[i][n:3*n]=h1[i]
    return dict(d=d,h=h,p=diag(p0,p1,p2),n=n,betti=[rank(p0),rank(p1),rank(p2)])


def wedge_pair(g):
    n=len(g);out=Z(4*n)
    for i in range(n):
        out[i][3*n:]=g[i];out[3*n+i][:n]=g[i]
        out[n+i][2*n:3*n]=g[i];out[2*n+i][n:2*n]=[-x for x in g[i]]
    return out


def cyclic(E,D=None,trace=None):
    n=E['n'];parity=diag(I(n),scale(I(2*n),-1),I(n))
    if D is None:
        d,h,p=E['d'],E['h'],E['p'];pair=wedge_pair(trace)
    else:
        d,h,p=[diag(E[k],D[k]) for k in ('d','h','p')];j=wedge_pair(I(n));z=Z(4*n)
        pair=stack(cat(z,j),cat(j,z));parity=diag(parity,parity)
    return dict(d=zero(add(mm(tr(d),pair),mm(mm(parity,pair),d))),
        h=zero(add(mm(tr(h),pair),mm(mm(parity,pair),h),-1)),
        p=equal(mm(tr(p),pair),mm(pair,p)),isotropic=zero(mm(mm(tr(h),pair),h)))


def cell_checks(a,b):
    n=len(a);p,q=series(a),series(b);u,v=series(a,True),series(b,True);T=diag(u,v)
    d0=stack(a,b);d1=cat(scale(b,-1),a);g0=stack(add(p,I(n),-1),add(q,I(n),-1));g1=cat(add(I(n),q,-1),add(p,I(n),-1))
    td=diag(series(scale(tr(a),-1),True),series(scale(tr(b),-1),True))
    j=stack(cat(Z(n),tr(inverse(p))),cat(scale(tr(inverse(q)),-1),Z(n)))
    j0=stack(cat(Z(n),I(n)),cat(scale(I(n),-1),Z(n)))
    difference=add(mm(mm(tr(T),j),td),j0,-1)
    return dict(chain0=equal(mm(T,d0),g0),chain1=equal(mm(g1,T),mm(mm(u,v),d1)),
        invertible=old.determinant(T)==1 and old.determinant(mm(u,v))==1,
        cup_on_all_closed=zero(mm(mm(tr(null(d1)),difference),null(cat(tr(b),scale(tr(a),-1))))))


@lru_cache(None)
def words(n):
    if n==1:return ('x',)
    return tuple('('+a+b+')' for k in range(1,n) for a in words(k) for b in words(n-k))


def parent_cases(text):
    parents={};cursor=0;leaf=0
    def parse(root=True):
        nonlocal cursor,leaf
        if text[cursor]=='x':
            cursor+=1;idx=leaf;leaf+=1;return [idx]
        assert text[cursor]=='(';cursor+=1;left=parse(False);right=parse(False)
        assert text[cursor]==')';cursor+=1
        for child,other in ((left,right),(right,left)):
            if len(child)==1:parents[child[0]]='harmonic' if len(other)==1 else ('root_propagator' if root else 'internal_propagator')
        return left+right
    parse();assert cursor==len(text);return list(parents.values())


@lru_cache(None)
def run():
    data,w,P,Q,A,B=literal();checks={};blocks={}
    def ck(k,v):checks[k]=bool(v);assert checks[k],k
    ck('literal_relators_and_peripheral_split',all(equal(word(w,r),I(5)) for r in data['relators']))
    ck('two_unipotent_logs',equal(series(A),P) and equal(series(B),Q) and equal(mm(A,B),mm(B,A)))
    span=rank(tr([[x for row in m for x in row] for m in (A,B)]))
    ck('cusp_log_directions_not_principal_singleton',span==2)
    basis=basis5();trace,metric=gram(basis),gram(basis,True);NA,NB=ad(A,basis),ad(B,basis)
    ck('neutral_invariant_trace',zero(add(mm(tr(NA),trace),mm(trace,NA))) and zero(add(mm(tr(NB),trace),mm(trace,NB))))
    expected=diag(I(20),[[int(i==j)+1 for j in range(4)] for i in range(4)])
    ck('neutral_positive_induced_metric',equal(metric,expected) and old.determinant(metric)==5)
    logs={'W':(A,B),'F':(wedge_derivative(A),wedge_derivative(B)),'N':(NA,NB),'gauge':(Z(1),Z(1))}
    ck('induced_exterior_and_neutral_logs_are_actual_holonomies',all(equal(series(x),y) for x,y in ((logs['F'][0],old.exterior(P)),(logs['F'][1],old.exterior(Q)),(NA,ad_group(P,basis)),(NB,ad_group(Q,basis)))))
    for label,(a,b) in logs.items():
        E=contraction(a,b,metric if label=='N' else None);blocks[label]=E;n=E['n'];d,h,p=E['d'],E['h'],E['p'];identity=I(4*n)
        ck(label+'_SDR',zero(mm(d,d)) and equal(add(mm(d,h),mm(h,d)),add(identity,p,-1)) and zero(mm(h,h)) and zero(mm(h,p)) and zero(mm(p,h)) and equal(mm(p,p),p) and zero(mm(d,p)) and zero(mm(p,d)))
        ck(label+'_nonvacuous_sign_control',zero(d) if label=='gauge' else not equal(scale(add(mm(d,h),mm(h,d)),-1),add(identity,p,-1)))
        if label in ('W','F'):
            D=contraction(scale(tr(a),-1),scale(tr(b),-1));blocks[label+'dual']=D
            ck(label+'_dual_SDR',equal(add(mm(D['d'],D['h']),mm(D['h'],D['d'])),add(identity,D['p'],-1)) and zero(mm(D['h'],D['h'])) and zero(mm(D['p'],D['h'])) and zero(mm(D['h'],D['p'])))
            for key,value in cyclic(E,D).items():ck(label+'_cyclic_'+key,value)
            for key,value in cell_checks(a,b).items():ck(label+'_cell_'+key,value)
        else:
            for key,value in cyclic(E,trace=trace if label=='N' else I(1)).items():ck(label+'_cyclic_'+key,value)
            if label=='N':
                for key,value in cell_checks(a,b).items():ck(label+'_cell_'+key,value)
        ck(label+'_higher_gauge_leaf_contraction',zero(mm(h,p)) and zero(mm(h,h)) and zero(mm(p,h)))
    badmetric=[[i+1 if i==j else 0 for j in range(5)] for i in range(5)]
    wrong=contraction(scale(tr(A),-1),scale(tr(B),-1),badmetric)
    ck('wrong_dual_metric_still_SDR',equal(add(mm(wrong['d'],wrong['h']),mm(wrong['h'],wrong['d'])),add(I(20),wrong['p'],-1)))
    ck('wrong_dual_metric_not_cyclic',not cyclic(blocks['W'],wrong)['h'])
    x,y,z=add(basis[0],basis[4],-1),add(basis[5],basis[9],-1),add(basis[8],basis[1],-1)
    product=mm(x,add(mm(y,z),mm(z,y),-1))
    ck('compact_gauge_binary_action_not_deleted',all(equal(tr(t),scale(t,-1)) for t in (x,y,z)) and sum(product[i][i] for i in range(5))==2)
    ck('all24_gauge_generators_have_nonzero_5_and_10_actions',len(basis)==24 and all(not zero(x) and not zero(wedge_derivative(x)) and not zero(ad(x,basis)) for x in basis))
    cases={'harmonic':0,'internal_propagator':0,'root_propagator':0};nodes=0
    for n in range(3,8):
        for text in words(n):
            found=parent_cases(text);assert len(found)==n
            for key in found:cases[key]+=1;nodes+=1
    ck('complete_bounded_tree_instrument',nodes==sum(n*len(words(n)) for n in range(3,8)) and min(cases.values())>0)
    mult={'W':10,'Wdual':10,'F':5,'Fdual':5,'N':1,'gauge':24}
    H=[sum(mult[k]*v['betti'][j] for k,v in blocks.items()) for j in range(3)];fulln=sum(mult[k]*v['n'] for k,v in blocks.items())
    Ldim=10*blocks['W']['betti'][1]+5*blocks['F']['betti'][1]+blocks['N']['betti'][1]//2+24
    ck('full248_roster_and_harmonic_Lagrangian_dimension',fulln==248 and H==[100,200,100] and Ldim==100 and 24+Ldim+H[2]-24==sum(H)//2)
    return dict(checks=checks,passed=len(checks),failed=[],profile=dict(cusp_log_span=span,
        boundary_betti={k:v['betti'] for k,v in blocks.items()},full_coefficient_dimension=fulln,full_H=H,
        Ah_dimensions=[24,Ldim,H[2]-24],tree_leaf_cases=cases,tree_positions=nodes,gauge_basis_count=len(basis)),
        all_order_charged_physical_completion=False,physical_action_stationary=False,
        genesis_boundary_selected=False,physical_goal_achieved=False,non_author_acceptance=False)


if __name__=='__main__':print(json.dumps(run(),sort_keys=True,indent=2))
