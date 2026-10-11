"""Same-action vector algebra and exact all-rank-strata linear multiplets."""
from functools import lru_cache
from collections import Counter
from itertools import combinations,product
from pathlib import Path
import importlib.util,json,hashlib
import sympy as s
HERE=Path(__file__).resolve().parent
OLD=HERE.parent
def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
def norm(a):return a.applyfunc(s.expand)
def eq(a,b):return norm(a-b)==s.zeros(*a.shape)
def comm(a,b):return a*b-b*a

def vector_controls():
    p=load('multiplet_canonical_grassmann',OLD/'silver_fermion_action_2026_10_11/probe.py')
    I=s.I;R=s.Rational;t,e=s.symbols('tau amplitude',real=True)
    rr=s.symbols('r0:3',real=True);q=[2,3,5,7];eta=[-1,1,1,1]
    X=s.Matrix([[0,1],[1,0]]);Y=s.Matrix([[0,-I],[I,0]]);Z=s.diag(1,-1)
    A=[Z,X,Y];B=[X,Y,Z]
    u=[t*X+rr[0]*Z,t*Y+rr[1]*X,t*Z+rr[2]*Y]
    v=[(1+t+t*t)*Y+rr[0]*X,(2+t)*Z+rr[1]*Y,(1+t*t)*X+rr[2]*Z]
    w=[(1+t+rr[0])*X+Y,(1+t+rr[1])*Y+Z,(2+t+rr[2])*Z+X,(1+2*t+rr[0])*X+Z]
    facts={}
    def ck(k,a):facts[k]=bool(a)
    def ed(a,mu):return p.clean({m:q[mu]*c.diff(t) for m,c in a.items()})
    def ider(a,j):return p.clean({m:c.diff(rr[j]) for m,c in a.items()})
    XX=[p.add(*(p.scale(p.mul(p.gen(a),p.gen(b+2)),p.SIG[mu][a,b]) for a in range(2) for b in range(2))) for mu in range(4)]
    def shift(a):
        return p.add(a,p.add(*(p.scale(p.mul(XX[mu],ed(a,mu)),I) for mu in range(4))),
                     p.add(*(p.scale(p.mul(XX[mu],p.mul(XX[nu],ed(ed(a,nu),mu))),-R(1,2)) for mu in range(4) for nu in range(4))))
    def D(a,al):return p.add(p.left(a,al),*(p.scale(p.mul(p.gen(b+2),ed(a,mu)),I*p.SIG[mu][al,b]) for mu in range(4) for b in range(2)))
    def BD(a,b):return p.add(p.scale(p.left(a,b+2),-1),*(p.scale(p.mul(p.gen(al),ed(a,mu)),-I*p.SIG[mu][al,b]) for mu in range(4) for al in range(2)))
    def BD2(a):return p.scale(BD(BD(a,1),0),-2)
    V=p.scale(p.add(*(p.mul(XX[mu],{0:w[mu]}) for mu in range(4))),-e)
    G=p.add({0:s.eye(2)},p.scale(V,2),p.scale(p.mul(V,V),2))
    Gi=p.add({0:s.eye(2)},p.scale(V,-2),p.scale(p.mul(V,V),2))
    PP=[shift({0:A[j]+I*B[j]+e*(u[j]+I*v[j])}) for j in range(3)]
    ZZ=[p.add(p.mul(Gi,ider(G,j)),p.scale(p.mul(p.mul(Gi,p.dag(PP[j])),G),I),p.scale(PP[j],-I)) for j in range(3)]
    ck('canonical_vector_real_and_exact_exponential',p.eq(V,p.dag(V)) and p.eq(p.mul(G,Gi),{0:s.eye(2)}) and bool(p.mul(V,V)) and not p.mul(p.mul(V,V),V))
    ck('actual_even_chirality_with_external_second_jets',all(not BD(a,b) for a in PP for b in range(2)) and any(c.diff(t,2)!=s.zeros(2) for a in PP for c in a.values()))
    raw=s.expand(s.trace(p.d4(p.add(*(p.mul(z,z) for z in ZZ))).get(0,s.zeros(2)))/4).coeff(e,2)
    XXc=[[norm(q[mu]*u[j].diff(t)-w[mu].diff(rr[j])-I*comm(A[j],w[mu])) for j in range(3)] for mu in range(4)]
    YYc=[[norm(q[mu]*v[j].diff(t)+I*comm(w[mu],B[j])) for j in range(3)] for mu in range(4)]
    expected=-sum(eta[mu]*s.trace(XXc[mu][j]**2+YYc[mu][j]**2)/2 for mu in range(4) for j in range(3))
    div=sum(eta[mu]*q[mu]**2*s.diff(s.trace(v[j]*v[j].diff(t)),t)/2 for mu in range(4) for j in range(3))
    ck('direct_mixed_boson_coefficient_and_retained_divergence',s.expand(raw-expected-div)==0)
    ck('omitted_external_divergence_rejected',s.expand(raw-expected)!=0)
    ck('wrong_mixed_coefficient_rejected',s.expand(raw-2*expected-div)!=0)
    ck('wrong_spacetime_metric_rejected',s.expand(raw-expected-div+sum(s.trace(XXc[0][j]**2+YYc[0][j]**2) for j in range(3)))!=0)
    Ws=[p.scale(BD2(p.mul(Gi,D(G,al))),-R(1,4)) for al in range(2)]
    WW=p.add(p.mul(Ws[0],Ws[1]),p.scale(p.mul(Ws[1],Ws[0]),-1))
    hol=p.scale(p.d2(WW),R(1,16));gym=s.expand(s.trace(p.add(hol,p.dag(hol)).get(0,s.zeros(2))))
    ff={(mu,nu):norm(e*(q[mu]*w[nu].diff(t)-q[nu]*w[mu].diff(t))+I*e**2*comm(w[mu],w[nu])) for mu,nu in combinations(range(4),2)}
    gym_expected=-sum(eta[mu]*eta[nu]*s.trace(f*f)/2 for (mu,nu),f in ff.items())
    ck('direct_Yang_Mills_coefficient_all_components',s.expand(gym-gym_expected)==0)
    ck('nonabelian_vector_quartic_retained',s.expand(gym).coeff(e,4)!=0 and any(not eq(comm(a,b),s.zeros(2)) for a,b in combinations(w,2)))
    ck('wrong_vector_coefficient_rejected',s.expand(gym-2*gym_expected)!=0)
    # Project the actual NORMAL response at a commuting global-k comparator.
    aa,bb=Z,2*Z;un=t*Z+rr[0]*X;vn=(1+t)*Z+rr[0]*Y
    pn=shift({0:aa+I*bb+e*(un+I*vn)})
    zn=p.add(p.mul(Gi,ider(G,0)),p.scale(p.mul(p.mul(Gi,p.dag(pn)),G),I),p.scale(pn,-I))
    linear=p.clean({m:norm(c).applyfunc(lambda x:s.expand(x).coeff(e,1)) for m,c in zn.items()})
    projected={m:s.expand(s.trace(Z*c)) for m,c in linear.items() if s.expand(s.trace(Z*c))!=0}
    target=p.add({0:2*vn},*(p.scale(p.mul(XX[mu],{0:norm(q[mu]*un.diff(t)-w[mu].diff(rr[0]))}),2) for mu in range(4)))
    targettr={m:s.expand(s.trace(Z*c)) for m,c in target.items() if s.expand(s.trace(Z*c))!=0}
    ck('actual_projected_mixed_response_keeps_normal_scalar_derivative',projected==targettr)
    ck('normal_scalar_derivative_not_an_essential_zero_law',any(s.trace(Z*un.diff(t))*qm!=0 for qm in q))
    lam=t*t*Z+rr[0]*(1+t)*(X+Z)
    def DA(f,j):return norm(f.diff(rr[j])+I*comm(A[j],f))
    ug=[DA(lam,j) for j in range(3)];vg=[I*comm(B[j],lam) for j in range(3)]
    wg=[qm*lam.diff(t) for qm in q]
    ck('mixed_compact_gauge_Ward_with_spacetime_and_normal_jets',all(eq(q[mu]*ug[j].diff(t)-DA(wg[mu],j),s.zeros(2)) and eq(q[mu]*vg[j].diff(t)+I*comm(wg[mu],B[j]),s.zeros(2)) for mu in range(4) for j in range(3)))
    badug=[I*comm(A[j],lam) for j in range(3)]
    ck('frozen_internal_parameter_derivatives_rejected',any(not eq(q[mu]*badug[j].diff(t)-DA(wg[mu],j),s.zeros(2)) for mu in range(4) for j in range(3)))
    # Actual real compact vector mass form; comparison not an E8/PDE census.
    basis=[X,Y,Z]
    ops=[(I*comm(Z,b),I*comm(b,2*Z)) for b in basis]
    gram=s.Matrix([[s.trace(a[0]*b[0]+a[1]*b[1]) for b in ops] for a in ops])
    ck('positive_real_vector_mass_kernel_not_flat_complex_H0',gram==s.diag(40,40,0) and len(gram.nullspace())==1)
    Q=s.Matrix(q);met=s.diag(*eta);q2=(Q.T*met*Q)[0]
    maxwell=q2*met-met*Q*Q.T*met
    null=s.Matrix([1,0,0,1]);mnull=-met*null*null.T*met
    ck('off_shell_Maxwell_Gauss_gauge_kernel',maxwell*Q==s.zeros(4,1) and maxwell.rank()==3)
    ck('on_shell_two_vector_polarizations_after_Gauss',mnull*null==s.zeros(4,1) and len(mnull.nullspace())-1==2)
    ck('complex_norm_is_real_mixed_norm',all(s.expand(s.trace((x+I*y).H*(x+I*y))-s.trace(x*x+y*y))==0 for x,y in zip(XXc[0],YYc[0])))
    return {'facts':facts,'normalizations':{'vector':'-F_mu_nu F^mu_nu/4','mixed':'-sum eta_mu (X_mu^2+Y_mu^2)/2','retained_divergence':'partial_mu Tr(v partial^mu v)/2'},'global_PDE_solved':False,'full_Hamiltonian':False}

def root_controls():
    e=list(s.eye(8).columnspace());roots=[]
    for i,j in combinations(range(8),2):
        for a,b in product((-1,1),repeat=2):roots.append(a*e[i]+b*e[j])
    for signs in product((-1,1),repeat=8):
        if signs.count(-1)%2==0:roots.append(s.Matrix(signs)/2)
    gauge=[e[i]-e[i+1] for i in range(4)]
    structure=[e[6]-e[7],e[5]-e[6],e[6]+e[7],-sum(e,s.zeros(8,1))/2]
    actual=Counter(tuple(int(r.dot(a)) for a in gauge+structure) for r in roots);actual[(0,)*8]+=8
    f=[tuple(int(j==i)-int(j==i+1) for i in range(4)) for j in range(5)]
    neg=lambda w:tuple(-x for x in w)
    ten=[tuple(a+b for a,b in zip(f[i],f[j])) for i,j in combinations(range(5),2)]
    reps={'1':[(0,)*4],'5':f,'bar5':list(map(neg,f)),'10':ten,'bar10':list(map(neg,ten)),
          '24':[tuple(a-b for a,b in zip(f[i],f[j])) for i in range(5) for j in range(5) if i!=j]+[(0,)*4]*4}
    branches=[('24','1'),('1','24'),('10','5'),('bar10','bar5'),('5','bar10'),('bar5','10')]
    def bc(br):return Counter(a+b for ra,rb in br for a in reps[ra] for b in reps[rb])
    wrong=bc(branches[:4]+[('5','10'),('bar5','bar10')])
    h=s.symbols('h0:4');weights=list(h)+[-sum(h)]
    cubic5=s.expand(sum(a**3 for a in weights));cubic10=s.expand(sum((weights[i]+weights[j])**3 for i,j in combinations(range(5),2)))
    facts={'all_240_roots_and_248_joint_weights':len(roots)==240 and len(set(map(tuple,roots)))==240 and sum(actual.values())==248 and actual==bc(branches),
           'dimension_preserving_wrong_conjugates_rejected':sum(wrong.values())==248 and actual!=wrong,
           'whole_SU5_cubic_weight_identity':cubic5==cubic10 and cubic5!=0,
           'real_adjoint_and_singlet_cubic_zero':s.expand(sum((a-b)**3 for a in weights for b in weights))==0}
    return {'facts':facts,'branching':branches,'root_count':len(roots)}

def end_trace_basis():
    basis=[]
    for i,j in product(range(5),repeat=2):
        if i!=j:
            a=s.zeros(5);a[i,j]=1;basis.append(a)
    for i in range(4):
        a=s.zeros(5);a[i,i]=1;a[4,4]=-1;basis.append(a)
    return basis,s.Matrix([[s.trace(a*b) for b in basis] for a in basis])

def aggregate(charged,neutral,gauge):
    rows=[];matches=[];double=[]
    for w,f,n,g in product(charged['W']['strata'],charged['F']['strata'],neutral,gauge):
        hw,hd=w['E']['H'][1],w['dual']['H'][1]
        hf,hfd=f['E']['H'][1],f['dual']['H'][1]
        nc,gc=n['H'][1],g['H'][1];jw,jf=hw-hd,hf-hfd
        left=10*(hw+hd)+5*(hf+hfd)+nc+24*gc
        vec=24*g['H'][0]
        leftweyl=10*(sum(w['E']['H'][1::2])+sum(w['dual']['H'][1::2]))+5*(sum(f['E']['H'][1::2])+sum(f['dual']['H'][1::2]))+sum(n['H'][1::2])+24*sum(g['H'][1::2])
        matches.append(2*left+2*vec==2*leftweyl)
        bad=leftweyl+10*(w['E']['H'][2]+w['dual']['H'][2])+5*(f['E']['H'][2]+f['dual']['H'][2])+n['H'][2]
        double.append(2*left+2*vec!=2*bad)
        rows.append([w['ell'],w['intersection'],f['ell'],f['intersection'],n['intersection'],g['intersection'],hw,hd,hf,hfd,nc,gc,jw,jf,jw-jf,left,vec,leftweyl])
    rows.sort()
    return {'patterns_computed':len(rows),'canonical_pattern_sha256':hashlib.sha256(json.dumps(rows,separators=(',',':')).encode()).hexdigest(),
            'local_cubic_anomaly_histogram':dict(sorted(Counter(r[14] for r in rows).items())),
            'anomaly_free_common_index_histogram':dict(sorted(Counter(r[12] for r in rows if r[14]==0).items())),
            'left_chiral_component_range':[min(r[15] for r in rows),max(r[15] for r in rows)],
            'boson_fermion_on_shell_dof_match':all(matches),'wrong_H2_doublecount_rejected':all(double),
            'continuous_planes_not_counted_as_vacua':True}

@lru_cache(None)
def census():
    p=load('multiplet_spectral_native',OLD/'silver_spectral_completion_2026_10_05/probe.py')
    old=p.load('multiplet_coefficient_native',OLD/'silver_operator_gate_2026_10_05/probe.py')
    data=json.loads((OLD/'silver_operator_gate_2026_10_05/candidate.json').read_text())
    v=old.four(data);c=s.Matrix([s.Rational(a)+s.sqrt(2)*s.Rational(b) for a,b in data['cocycle_Qsqrt2_pairs']]);w=old.extension(v,c)
    facts={};sectors={}
    def ck(k,a):facts[k]=bool(a)
    vc=p.Complex(v,data);cr=c
    ck('literal_marking_and_nonsplit_cocycle',data['relators']==old.marked_relators() and p.zero(p.mul(vc.F,cr)) and p.zero(p.mul(vc.R,cr)) and p.rank(vc.B.row_join(cr))>p.rank(vc.B))
    bad=cr.copy();bad[0]+=1
    ck('changed_cocycle_rejected',not p.zero(p.mul(vc.F,bad)))
    for name,rep in [('W',w),('F',{g:old.wedge(a) for g,a in w.items()})]:
        E,D=[p.Complex(r,data) for r in (rep,{g:p.inv(a).T for g,a in rep.items()})]
        J=p.cup(E);n=E.n;t0=n-p.rank(E.D);qdim=E.res.cols;t=E.H.cols
        ck(name+'_restriction_images_are_cup_annihilators',p.zero(p.mul(p.mul(E.res.T,J),D.res)) and E.res.cols+D.res.cols==t and p.rank(p.mul(p.mul(E.H.T,J),D.H))==t)
        profile={'absolute_H':[n-p.rank(E.B),3*n-p.rank(E.F)-p.rank(E.B),2*n-p.rank(E.F),0],
                 'boundary_H':[t0,t,t0],'restriction_rank':qdim,'cone_strata':[]}
        h0,h1,h2,_=profile['absolute_H'];strata=[]
        for ell in range(t+1):
            for j in range(max(0,ell+qdim-t),min(ell,qdim)+1):
                L=E.res[:,:j].row_join(E.L[:,:ell-j])
                res=p.paired(E,D,L);r=qdim+ell-j
                les=[0,t0-h0+h1+ell-r,t-r+h2,0]
                ck(f'{name}_{ell}_{j}_actual_stratum_cone_and_LES',p.rank(L)==ell and p.rank(E.res.row_join(L))==r and res['E']['H']==les and res['E']['J']==ell-t0)
                ck(f'{name}_{ell}_{j}_dual_and_endpoints',res['dual']['H']==les[::-1] and les[0]==les[3]==0)
                strata.append(dict(ell=ell,intersection=j,union_rank=r,**res))
        ck(name+'_wrong_degree_two_restriction_sign_rejected',not p.zero(p.mul(-E.R2,E.F)-p.mul(E.G,E.R)))
        ck(name+'_same_dimension_can_have_different_full_counts',any(a['ell']==b['ell'] and a['E']['H']!=b['E']['H'] and a['E']['J']==b['E']['J'] for a,b in combinations(strata,2)))
        sectors[name]={'coefficient_rank':n,**profile,'strata':strata}
        del sectors[name]['cone_strata']
    # Neutral actual trace self-duality and symplectic partners.
    basis,T=end_trace_basis();N=p.Complex(p.adjoint0(w),data);S=p.mul(p.cup(N),s.diag(T,T))
    R=N.res;H=N.H;qs=R.cols;ts=H.cols
    ck('neutral_actual_trace_form_self_duality',T.det()!=0 and all(p.zero(p.mul(p.mul(a.T,T),a)-T) for a in N.rep.values()))
    ck('neutral_wrong_positive_unitary_shortcut_rejected',any(not p.zero(a.T*a-s.eye(24)) for a in N.rep.values()))
    hs=p.mul(p.mul(H.T,S),H)
    ck('neutral_restriction_is_Lagrangian',p.zero(p.mul(p.mul(R.T,S),R)) and 2*qs==ts and p.rank(hs)==ts and p.zero(hs+hs.T))
    M=p.mul(p.mul(R.T,S),H);piv=p.dm(M).rref()[1]
    U0=p.mul(H[:,list(piv)],p.inv(M[:,list(piv)]));K=p.mul(p.mul(U0.T,S),U0);U=p.red(U0+p.mul(R,K)/2)
    ck('neutral_symplectic_partner_exact',p.zero(p.mul(p.mul(U.T,S),U)) and p.mul(p.mul(R.T,S),U)==s.eye(qs))
    neutral=[]
    for j in range(qs+1):
        L=R[:,:j].row_join(U[:,j:]);co=p.cone(N,L)
        ck(f'neutral_{j}_full_cone_stratum',p.rank(L)==qs and p.rank(R.row_join(L))==2*qs-j and p.zero(p.mul(p.mul(L.T,S),L)) and co['H']==co['H'][::-1] and co['J']==0)
        neutral.append(dict(intersection=j,**co))
    split=old.extension(v,s.zeros(12,1));Ns=p.Complex(p.adjoint0(split),data);split_n=p.cone(Ns,Ns.res)
    ck('neutral_split_comparator_preserved',split_n['H'][1]!=neutral[-1]['H'][1] and split_n['H']==split_n['H'][::-1])
    # Actual gauge cone with both possible line strata.
    C=p.Complex({g:s.eye(1) for g in p.GEN},data);gauges=[]
    trans=s.Matrix([1,s.I]);lines=[trans,C.res]
    for j,L in enumerate(lines):
        co=p.cone(C,L,s.eye(1),s.zeros(1,0),ranker=lambda a:a.rank())
        ck(f'gauge_{j}_full_endpoints_and_optional_adjoint',co['H']==[1,j,j,1] and C.res.row_join(L).rank()==2-j)
        gauges.append(dict(intersection=j,**co))
    out=aggregate(sectors,neutral,gauges)
    ck('local_anomaly_has_both_outcomes',0 in out['local_cubic_anomaly_histogram'] and any(k!=0 for k in out['local_cubic_anomaly_histogram']))
    ck('all_dimension_pairs_and_only_expected_cubic_relation',{(a['ell'],b['ell']) for a,b in product(sectors['W']['strata'],sectors['F']['strata'])}==set(product(range(sectors['W']['boundary_H'][1]+1),range(sectors['F']['boundary_H'][1]+1))) and all((a['E']['J']==b['E']['J'])==(b['ell']==a['ell']+1) for a,b in product(sectors['W']['strata'],sectors['F']['strata'])))
    ck('no_three_common_index_in_THIS_menu_not_architecture',all(abs(k)<3 for k in out['anomaly_free_common_index_histogram']))
    ck('actual_bosonic_vs_full_odd_Weyl_counts',out['boson_fermion_on_shell_dof_match'])
    ck('false_H2_doublecount_breaks_dof_match',out['wrong_H2_doublecount_rejected'])
    def profile(E):return {'coefficient_rank':E.n,'absolute_H':[E.n-p.rank(E.B),3*E.n-p.rank(E.F)-p.rank(E.B),2*E.n-p.rank(E.F),0],'boundary_H':[E.n-p.rank(E.D),E.H.cols,E.H2.cols],'restriction_rank':E.res.cols}
    return {'facts':facts,'charged':sectors,'neutral':neutral,'neutral_profile':profile(N),'split_neutral_restriction_cone':split_n,'gauge':gauges,'gauge_profile':profile(C),'aggregate':out}

@lru_cache(None)
def run():
    v,r,c=vector_controls(),root_controls(),census()
    facts={**v['facts'],**r['facts'],**c['facts']}
    out={'facts':facts,'predicates_passed':sum(facts.values()),'vector':{k:a for k,a in v.items() if k!='facts'},
         'root_roster':r,'census':{k:a for k,a in c.items() if k!='facts'},
         'conditional_linear_massless_dictionary':all(facts.values()),'all_rank_strata_not_all_continuous_vacua':True,
         'global_PDE_solved_numerically':False,'full_Hamiltonian':False,'full_quantum_anomaly':False,
         'interactions_normalized':False,'boundary_or_vacuum_selected':False,'outside_review':False,'full_goal_achieved':False}
    print(json.dumps(out,indent=2,sort_keys=True))
    assert all(facts.values()),[k for k,a in facts.items() if not a]
    return out
if __name__=='__main__':run()
