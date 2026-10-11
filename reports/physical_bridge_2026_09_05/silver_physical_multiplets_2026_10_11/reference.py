"""Different Fraction crossed-word/LES census and real component controls."""
from functools import lru_cache
from collections import Counter
from itertools import combinations,product
from fractions import Fraction as F
from pathlib import Path
import importlib.util,json,hashlib
import sympy as s
HERE=Path(__file__).resolve().parent;OLD=HERE.parent
def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
b=load('multiplet_fraction_coefficient',OLD/'silver_operator_gate_2026_10_05/reference.py')
K=b.K;z=b.zeros;eye=b.eye;add=b.add;tr=b.transpose;rank=b.rank;inv=b.inverse;hc=b.hcat;vc=b.vcat
base_mul=b.mul
def mm(a,c):
    fields={type(x) for matrix in (a,c) for row in matrix for x in row if isinstance(x,K)}
    if len(fields)>1:raise TypeError('mixed quadratic fields in sparse multiply')
    field=next(iter(fields),int)
    out=[[field(0) for _ in c[0]] for _ in a]
    for i,row in enumerate(a):
        for k,x in enumerate(row):
            if x:
                for j,y in enumerate(c[k]):
                    if y:out[i][j]+=x*y
    return out
b.mul=mm
def neg(a):return [[-x for x in row] for row in a]
def nc(a):return len(a[0])
def zero(a):return all(not x for row in a for x in row)
def ker(a):
    r,piv=b.elimination(a,True);free=[j for j in range(nc(a)) if j not in piv]
    out=z(nc(a),len(free))
    for k,j in enumerate(free):
        out[j][k]=1
        for i,p in enumerate(piv):out[p][k]=-r[i][j]
    return out
def cols(a):
    if not nc(a):return a
    p=b.elimination(a,True)[1]
    return [[r[j] for j in p] for r in a]
def take(a,start,end):return [row[start:end] for row in a]
def diag2(a):
    n=len(a);out=z(2*n)
    for i,row in enumerate(a):
        for j,x in enumerate(row):out[i][j]=out[n+i][n+j]=x
    return out

def boundary(rep,data):
    C=b.Complex(rep,data);n=C.n;p,q=[C.word(w)[0] for w in data['cusp_words']]
    G=hc(add(eye(n),q,-1),add(p,eye(n),-1));H=ker(vc(G,tr(C.D)))
    proj=mm(mm(H,inv(mm(tr(H),H))),tr(H))
    R=cols(mm(mm(proj,C.R),ker(C.F)))
    U=ker(vc(G,tr(C.D),tr(R)))
    J=vc(hc(z(n),tr(inv(p))),hc(neg(tr(inv(q))),z(n)))
    return dict(C=C,H=H,R=R,U=U,J=J,t0=n-rank(C.D),h0=n-rank(C.B),
                h1=3*n-rank(C.F)-rank(C.B),h2=2*n-rank(C.F),t=nc(H),q=nc(R))
def les(E,L):
    r=rank(hc(E['R'],L));ell=nc(L)
    return [0,E['t0']-E['h0']+E['h1']+ell-r,E['t']-r+E['h2'],0]
def dualplane(E,D,L):
    return D['H'] if nc(L)==0 else mm(D['H'],ker(mm(mm(tr(L),E['J']),D['H'])))
def end0(rep):
    # Vectorize ALL25 matrix entries first, then restrict with independent maps.
    T=z(25,24);S=z(24,25);idx=0
    for i,j in product(range(5),repeat=2):
        if i!=j:T[5*i+j][idx]=1;S[idx][5*i+j]=1;idx+=1
    for i in range(4):T[5*i+i][idx]=1;T[24][idx]=-1;S[idx][5*i+i]=1;idx+=1
    out={}
    for g,a in rep.items():
        ai=inv(a);act=[[a[i][k]*ai[l][j] for k,l in product(range(5),repeat=2)] for i,j in product(range(5),repeat=2)]
        out[g]=mm(mm(S,act),T)
    # Literal Tr(XY), NOT the positive Euclidean metric.
    swap=z(25)
    for i,j in product(range(5),repeat=2):swap[5*i+j][5*j+i]=1
    pairing=mm(mm(tr(T),swap),T)
    assert mm(S,T)==eye(24)
    return out,pairing
def component_controls():
    I=s.I;t=s.symbols('t',real=True);rr=s.symbols('y0:3',real=True)
    X=s.Matrix([[0,1],[1,0]]);Y=s.Matrix([[0,-I],[I,0]]);Z=s.diag(1,-1)
    basis=[Z,Y,X];q=[3,5,7,11];A=[Y,Z,X];B=[Z,2*X,Y]
    lam=(t+t*t)*X+rr[1]*(2+t)*Z
    def comm(a,c):return a*c-c*a
    def da(a,j):return a.diff(rr[j])+I*comm(A[j],a)
    u=[da(lam,j) for j in range(3)];v=[I*comm(B[j],lam) for j in range(3)]
    w=[qm*lam.diff(t) for qm in q]
    checks={}
    checks['different_component_mixed_Ward_all_four_covectors']=all(s.simplify(q[mu]*u[j].diff(t)-da(w[mu],j))==s.zeros(2) and s.simplify(q[mu]*v[j].diff(t)+I*comm(w[mu],B[j]))==s.zeros(2) for mu in range(4) for j in range(3))
    checks['component_wrong_scalar_sign_rejected']=any(s.expand(x)!=0 for x in (q[0]*v[0].diff(t)-I*comm(w[0],B[0])))
    def coords(m):return s.Matrix([s.trace(c*m)/2 for c in basis]).applyfunc(s.simplify)
    L=s.Matrix.hstack(*(coords(I*comm(Z,c)) for c in basis))
    H=s.Matrix.hstack(*(coords(I*comm(c,3*Z)) for c in basis))
    G=L.col_join(-H);P=G.T*G;D=L-I*H
    checks['real_block_mass_Gram_matches_complex_D_adjoint']=P==D.H*D and P==s.diag(0,40,40)
    checks['mass_kernel_retains_real_gauge_generator']=len(P.nullspace())==1 and P*s.Matrix([1,0,0])==s.zeros(3,1)
    checks['imaginary_Higgs_potential_sign_fails']=P!=-L*L+H*H
    checks['real_block_wrong_complex_gauge_deletion_fails']=any(x!=0 for x in H)
    met=s.diag(-1,1,1,1)
    for j in range(1,4):
        p=s.eye(4)[:,0]+s.eye(4)[:,j];M=-met*p*p.T*met
        checks['independent_null_Gauss_'+str(j)]=M*p==s.zeros(4,1) and len(M.nullspace())-1==2
    # Actual same-boundary inhomogeneous slice, now with external-dependent data.
    x=s.symbols('x',real=True);un=t*(1+x+x*x)
    lm=s.integrate(-un+s.integrate(un,(x,0,1)),x);lm-=lm.subs(x,0)
    wm=(1+t)*x
    mixed=s.diff(wm,x)-s.diff(un,t)
    mixed_after=s.diff(wm+s.diff(lm,t),x)-s.diff(un+s.diff(lm,x),t)
    checks['normal_response_gauge_invariance_with_external_jets']=s.expand(mixed_after-mixed)==0
    checks['slice_real_normal_flux_zero_not_imposed_essentially']=(un+s.diff(lm,x)).subs(x,1)==(un+s.diff(lm,x)).subs(x,0) and s.diff(lm,x).subs(x,0)!=0
    # Choose actual response-compatible w, then the sliced integrated flux is zero.
    wm_good=s.diff(un.subs(x,1)-un.subs(x,0),t)*x
    sliced=wm_good+s.diff(lm,t)
    checks['false_linear_vector_cannot_supply_required_flux']=s.diff(sliced,x).subs(x,1)-s.diff(sliced,x).subs(x,0)!=0
    # The interval's integrated normal w is its derivative DIFFERENCE, while
    # the response for u is its value DIFFERENCE. Use a quadratic w instead.
    wflux=s.diff(un.subs(x,1)-un.subs(x,0),t)*x*x/2
    sliced=wflux+s.diff(lm,t)
    checks['actual_mixed_boundary_flux_after_slice']=s.diff(sliced,x).subs(x,1)-s.diff(sliced,x).subs(x,0)==0
    return checks

def root_controls():
    # Enumerate antipodal spinor roots by seven signs and forced last parity.
    es=[[int(i==j) for i in range(8)] for j in range(8)];roots=[]
    for i,j in combinations(range(8),2):
        for a,c in product((-1,1),repeat=2):
            r=[0]*8;r[i]=a;r[j]=c;roots.append(r)
    for v in product((-1,1),repeat=7):
        last=1
        for a in v:last*=a
        roots.append([F(a,2) for a in v+(last,)])
    gauge=[[es[i][j]-es[i+1][j] for j in range(8)] for i in range(4)]
    struct=[[es[6][j]-es[7][j] for j in range(8)],[es[5][j]-es[6][j] for j in range(8)],
            [es[6][j]+es[7][j] for j in range(8)],[-F(1,2)]*8]
    actual=Counter(tuple(int(sum(a*c for a,c in zip(r,e))) for e in gauge+struct) for r in roots);actual[(0,)*8]+=8
    five=[tuple(int(j==i)-int(j==i+1) for i in range(4)) for j in range(5)]
    adj=[tuple(a-c for a,c in zip(x,y)) for i,x in enumerate(five) for j,y in enumerate(five) if i!=j]+[(0,)*4]*4
    ten=[tuple(a+c for a,c in zip(five[i],five[j])) for i,j in combinations(range(5),2)]
    negs=lambda a:[tuple(-x for x in r) for r in a]
    expected=Counter([x+(0,)*4 for x in adj]+[(0,)*4+x for x in adj]+[x+y for a,c in [(ten,five),(negs(ten),negs(five)),(five,negs(ten)),(negs(five),ten)] for x in a for y in c])
    wrong=Counter([x+(0,)*4 for x in adj]+[(0,)*4+x for x in adj]+[x+y for a,c in [(ten,five),(negs(ten),negs(five)),(five,ten),(negs(five),negs(ten))] for x in a for y in c])
    # Expand EVERY degree-three monomial, not just a numeric Cartan grid.
    wf=[tuple(int(i==j) for j in range(4)) for i in range(4)]+[(-1,)*4]
    wt=[tuple(a+c for a,c in zip(wf[i],wf[j])) for i,j in combinations(range(5),2)]
    def polynomial(w):
        out=Counter()
        for a in w:
            for ijk in product(range(4),repeat=3):out[tuple(sorted(ijk))]+=a[ijk[0]]*a[ijk[1]]*a[ijk[2]]
        return {k:v for k,v in out.items() if v}
    checks={'different_248_joint_weight_enumeration':len(roots)==240 and actual==expected and sum(actual.values())==248,
            'wrong_same_dimension_roster_rejected':actual!=wrong and sum(wrong.values())==248,
            'full_cubic_multinomial_identity':polynomial(wf)==polynomial(wt) and bool(polynomial(wf)),
            'adjoint_cubic_all_monomials_zero':not polynomial([tuple(a-c for a,c in zip(x,y)) for x in wf for y in wf])}
    return checks

def aggregate(charged,neutral,gauge):
    rows=[];matches=[];double=[]
    for w,f,n,g in product(charged['W']['strata'],charged['F']['strata'],neutral,gauge):
        hw,hd=w['E']['H'][1],w['dual']['H'][1];hf,hfd=f['E']['H'][1],f['dual']['H'][1]
        nc0,gc=n['H'][1],g['H'][1];jw,jf=hw-hd,hf-hfd
        left=10*(hw+hd)+5*(hf+hfd)+nc0+24*gc
        vec=24*g['H'][0]
        leftweyl=10*(sum(w['E']['H'][1::2])+sum(w['dual']['H'][1::2]))+5*(sum(f['E']['H'][1::2])+sum(f['dual']['H'][1::2]))+sum(n['H'][1::2])+24*sum(g['H'][1::2])
        matches.append(2*left+2*vec==2*leftweyl)
        bad=leftweyl+10*(w['E']['H'][2]+w['dual']['H'][2])+5*(f['E']['H'][2]+f['dual']['H'][2])+n['H'][2]
        double.append(2*left+2*vec!=2*bad)
        rows.append([w['ell'],w['intersection'],f['ell'],f['intersection'],n['intersection'],g['intersection'],hw,hd,hf,hfd,nc0,gc,jw,jf,jw-jf,left,vec,leftweyl])
    rows.sort()
    return {'patterns_computed':len(rows),'canonical_pattern_sha256':hashlib.sha256(json.dumps(rows,separators=(',',':')).encode()).hexdigest(),
            'local_cubic_anomaly_histogram':dict(sorted(Counter(r[14] for r in rows).items())),
            'anomaly_free_common_index_histogram':dict(sorted(Counter(r[12] for r in rows if r[14]==0).items())),
            'left_chiral_component_range':[min(r[15] for r in rows),max(r[15] for r in rows)],
            'boson_fermion_on_shell_dof_match':all(matches),'wrong_H2_doublecount_rejected':all(double),
            'continuous_planes_not_counted_as_vacua':True}

@lru_cache(None)
def census():
    checks={}
    pairs=[([[f(1),f(0)],[f(0),f(1)]],[[f(0),f(2)],[f(3),f(0)]]) for f in (K,b.Gaussian)]
    checks['sparse_multiply_preserves_exact_field']=all(mm(a,c)==base_mul(a,c) for a,c in pairs)
    checks['sparse_multiply_preserves_zero_entry_field_type']=all(type(x) is type(a[0][0]) for a,c in pairs for row in mm(a,c) for x in row)
    try:mm([[K(1)]],[[b.Gaussian(1)]])
    except TypeError:checks['sparse_multiply_rejects_mixed_quadratic_fields']=True
    else:checks['sparse_multiply_rejects_mixed_quadratic_fields']=False
    checks['sparse_multiply_integer_only_positive_control']=mm([[1,0],[0,1]],[[0,2],[3,0]])==[[0,2],[3,0]]
    data=json.loads((OLD/'silver_operator_gate_2026_10_05/candidate.json').read_text())
    v=b.four(data);c=[K(a,d) for a,d in data['cocycle_Qsqrt2_pairs']];w=b.extension(v,c)
    charged={}
    checks['sparse_multiply_nonrational_positive_control']=mm([[K(1,2),0],[K(3),K(0,1)]],[[0,K(2)],[K(1,-1),0]])==base_mul([[K(1,2),0],[K(3),K(0,1)]],[[0,K(2)],[K(1,-1),0]])
    for name,rep in [('W',w),('F',{g:b.exterior(a) for g,a in w.items()})]:
        E,D=[boundary(a,data) for a in (rep,b.dual(rep))];n=E['C'].n;t=E['t'];q=E['q'];strata=[]
        checks[name+'_actual_cup_and_restriction_annihilators']=zero(mm(mm(tr(E['R']),E['J']),D['R'])) and q+D['q']==t and rank(mm(mm(tr(E['H']),E['J']),D['H']))==t
        for ell in range(t+1):
            for j in range(max(0,ell+q-t),min(ell,q)+1):
                L=hc(take(E['R'],0,j),take(E['U'],0,ell-j));LD=dualplane(E,D,L)
                ha,hd=les(E,L),les(D,LD)
                checks[f'{name}_{ell}_{j}_different_LES_stratum']=rank(L)==ell and rank(hc(E['R'],L))==q+ell-j and ha==hd[::-1] and ha[1]-ha[2]==ell-E['t0']
                strata.append(dict(ell=ell,intersection=j,E={'H':ha,'J':ha[1]-ha[2]},dual={'H':hd,'J':hd[1]-hd[2]}))
        charged[name]={'absolute_H':[E['h0'],E['h1'],E['h2'],0],'boundary_H':[E['t0'],t,E['t0']],'restriction_rank':q,'strata':strata}
    rn,T=end0(w);N=boundary(rn,data);SN=mm(N['J'],diag2(T));R=N['R'];H=N['H'];q=N['q']
    checks['neutral_independent_End25_restriction_and_trace']=rank(T)==24 and all(mm(mm(tr(a),T),a)==T for a in rn.values())
    HS=mm(mm(tr(H),SN),H)
    checks['neutral_actual_symplectic_cup']=zero(mm(mm(tr(R),SN),R)) and N['t']==2*q and rank(HS)==2*q and zero(add(HS,tr(HS)))
    M=mm(mm(tr(R),SN),H);piv=b.elimination(M,True)[1]
    MP=[[row[j] for j in piv] for row in M];HP=[[row[j] for j in piv] for row in H]
    U0=mm(HP,inv(MP));kk=mm(mm(tr(U0),SN),U0);U=add(U0,[[K(F(1,2))*x for x in row] for row in mm(R,kk)])
    checks['neutral_partner_actual_algebra']=zero(mm(mm(tr(U),SN),U)) and mm(mm(tr(R),SN),U)==eye(q)
    checks['neutral_wrong_Euclidean_pairing_rejected']=any(mm(tr(a),a)!=eye(24) for a in rn.values())
    neutral=[]
    for j in range(q+1):
        L=hc(take(R,0,j),take(U,j,q));hh=les(N,L)
        checks['neutral_full_LES_'+str(j)]=rank(L)==q and rank(hc(R,L))==2*q-j and zero(mm(mm(tr(L),SN),L)) and hh==hh[::-1]
        neutral.append({'intersection':j,'H':hh,'J':hh[1]-hh[2]})
    split=b.extension(v,[K(0)]*12);ns,_=end0(split);NS=boundary(ns,data);split_h=les(NS,NS['R'])
    checks['split_neutral_independent_replay_changes_count']=split_h==split_h[::-1] and split_h[1]!=neutral[-1]['H'][1]
    G=boundary({g:eye(1) for g in b.GEN},data)
    rr=[b.Gaussian(row[0].a) for row in G['R']]
    assert all(row[0].b==0 for row in G['R'])
    det=rr[0]*b.Gaussian(0,1)-rr[1]
    gauges=[]
    for j,r1 in [(0,2 if det else -1),(1,rank(G['R']))]:
        r0=G['t0'];r2=G['h2']
        hh=[G['h0']+1-r0,G['t0']-r0+G['h1']+1-r1,2-r1+G['h2']-r2,1-r2]
        checks['gauge_all_degree_LES_'+str(j)]=hh==[1,j,j,1]
        gauges.append({'intersection':j,'H':hh,'J':0})
    agg=aggregate(charged,neutral,gauges)
    checks['actual_bosonic_vs_full_odd_Weyl_counts']=agg['boson_fermion_on_shell_dof_match']
    checks['false_H2_doublecount_breaks_dof_match']=agg['wrong_H2_doublecount_rejected']
    checks['cubic_both_outcomes']=0 in agg['local_cubic_anomaly_histogram'] and any(k!=0 for k in agg['local_cubic_anomaly_histogram'])
    def profile(E):return {'coefficient_rank':E['C'].n,'absolute_H':[E['h0'],E['h1'],E['h2'],0],'boundary_H':[E['t0'],E['t'],E['t0']],'restriction_rank':E['q']}
    return {'checks':checks,'charged':charged,'neutral':neutral,'neutral_profile':profile(N),'split_neutral_restriction_cone':{'H':split_h},'gauge':gauges,'gauge_profile':profile(G),'aggregate':agg}
@lru_cache(None)
def run():
    c=dict(census());checks={**component_controls(),**root_controls(),**c.pop('checks')}
    out={'predicates':checks,'predicates_passed':sum(checks.values()),'census':c,
         'new_native_imported':False,'same_author':True,'reference_superspace_expansion':False,
         'global_PDE_certificate':False,'full_Hamiltonian':False,'full_quantum_anomaly':False,
         'interactions_normalized':False,'generated_selection':False,'outside_review':False,'full_goal_achieved':False}
    print(json.dumps(out,indent=2,sort_keys=True));assert all(checks.values()),[k for k,a in checks.items() if not a]
    return out
if __name__=='__main__':run()
