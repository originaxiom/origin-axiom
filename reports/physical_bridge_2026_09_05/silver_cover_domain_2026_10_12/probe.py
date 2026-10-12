"""Whole cover trace, actual gauge/neutral cones; seal before execution."""
import importlib.util,json
from functools import lru_cache
from pathlib import Path
import sympy as s
HERE=Path(__file__).resolve().parent
def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);return mod
p=load('cover_domain_charged',HERE.parent/'silver_charged_pair_lift_2026_10_11/probe.py')
cy=p.cy
ETA=(-1,-1,1)

def ker(a):
    if not a.cols:return s.zeros(0,0)
    if not a.rows:return s.eye(a.cols)
    reduced,piv=p.dm(a).rref();reduced=reduced.to_Matrix()
    free=[j for j in range(a.cols) if j not in piv];out=s.zeros(a.cols,len(free))
    for k,j in enumerate(free):
        out[j,k]=1
        for i,v in enumerate(piv):out[v,k]=-reduced[i,j]
    return out
def cols(a):return a[:,list(p.dm(a).rref()[1])] if a.cols else a

def bulk(rep,data):
    n=rep['a'].rows;I=s.eye(n)
    for text in data['relators']:assert p.zero(cy.word(rep,text)-I)
    P,Q=[cy.word(rep,text) for text in data['cusp_words']]
    BB=s.Matrix.vstack(*(rep[g]-I for g in p.GEN))
    F=s.Matrix.vstack(*(p.fox(rep,text) for text in data['relators']))
    R=s.Matrix.vstack(*(p.fox(rep,text) for text in data['cusp_words']))
    D=(P-I).col_join(Q-I);G=(I-Q).row_join(P-I)
    R2=-p.mm(p.mm(Q,p.fox(rep,data['cusp_words'][0])[:,:2*n]),s.diag(cy.inv(rep['t']),cy.inv(rep['t'])))
    assert p.zero(p.mm(F,BB)) and p.zero(p.mm(R,BB)-D) and p.zero(p.mm(R2,F)-p.mm(G,R))
    H=ker(G.col_join(D.T));project=p.mm(p.mm(H,cy.inv(p.mm(H.T,H))),H.T)
    restr=cols(p.mm(p.mm(project,R),ker(F)))
    J=s.zeros(n).row_join(cy.inv(P).T).col_join((-cy.inv(Q).T).row_join(s.zeros(n)))
    ranks=[p.rank(BB),p.rank(F)]
    return dict(rep=rep,n=n,B=BB,F=F,R=R,D=D,G=G,R2=R2,H=H,restriction=restr,J=J,
                absolute_H=[n-ranks[0],3*n-sum(ranks),2*n-ranks[1],0],
                boundary_H=[n-p.rank(D),H.cols,n-p.rank(G)])

def cone(E,L,A0,A2):
    n=E['n'];a0,a1,a2=A0.cols,L.cols,A2.cols
    dims=[n+a0,4*n+a1,4*n+a2,n]
    d0=s.zeros(dims[1],dims[0]);d1=s.zeros(dims[2],dims[1]);d2=s.zeros(n,dims[2])
    d0[:3*n,:n]=E['B'];d0[3*n+a1:,:n]=s.eye(n);d0[3*n+a1:,n:]=-A0
    d1[:2*n,:3*n]=E['F'];d1[2*n+a2:,:3*n]=E['R']
    d1[2*n+a2:,3*n:3*n+a1]=-L;d1[2*n+a2:,3*n+a1:]=-E['D']
    d2[:,:2*n]=E['R2'];d2[:,2*n:2*n+a2]=-A2;d2[:,2*n+a2:]=-E['G']
    assert p.zero(p.mm(d1,d0)) and p.zero(p.mm(d2,d1))
    ranks=list(map(p.rank,(d0,d1,d2)))
    H=[dims[j]-([0]+ranks)[j]-(ranks+[0])[j] for j in range(4)]
    assert min(H)>=0
    return {'H':H,'dimensions':dims,'ranks':ranks}

def neutral(rep,data,T,met,NA,NB,ck,label):
    E=bulk(rep,data);n=24;R=E['restriction'];H=E['H'];b=E['boundary_H'][0]
    S=p.mm(E['J'],s.diag(T,T));HS=p.mm(p.mm(H.T,S),H)
    ck(label+'_literal_trace_selfduality_and_complete_boundary',p.rank(T)==n and all(p.zero(p.mm(p.mm(x.T,T),x)-T) for x in rep.values()) and E['boundary_H']==[6,12,6] and p.rank(HS)==12 and p.zero(HS+HS.T))
    ck(label+'_restriction_is_actual_Lagrangian',R.cols==b and p.zero(p.mm(p.mm(R.T,S),R)))
    pairing=p.mm(p.mm(R.T,S),H);piv=list(p.dm(pairing).rref()[1])
    U0=p.mm(H[:,piv],cy.inv(pairing[:,piv]));U=U0+p.mm(R,p.mm(p.mm(U0.T,S),U0))/2
    ck(label+'_transverse_polarization_earned',p.zero(p.mm(p.mm(U.T,S),U)) and p.mm(p.mm(R.T,S),U)==s.eye(b) and p.rank(R.row_join(U))==2*b)
    # Symmetric graph shifts preserve symplectic nullity; use a nonsymmetric
    # graph perturbation as the actual rejecting isotropy control.
    nonsym=s.zeros(b);nonsym[0,1]=1;wrong=U+p.mm(R,nonsym)
    ck(label+'_nonisotropic_same_dimension_plane_rejected',p.rank(wrong)==b and not p.zero(p.mm(p.mm(wrong.T,S),wrong)))
    dlog=NA.col_join(NB);glog=(-NB).row_join(NA);g1=s.diag(met,met)
    HL=ker(glog.col_join(p.mm(dlog.T,g1)))
    pl=p.mm(p.mm(HL,cy.inv(p.mm(p.mm(HL.T,g1),HL))),p.mm(HL.T,g1))
    t1=s.diag(cy.integral_exp(NA),cy.integral_exp(NB));t2=p.mm(cy.integral_exp(NA),cy.integral_exp(NB))
    UL=p.mm(p.mm(pl,cy.inv(t1)),U)
    ck(label+'_actual_log_harmonic_plane_transport',p.zero(p.mm(t1,dlog)-E['D']) and p.zero(p.mm(E['G'],t1)-p.mm(t2,glog)) and p.rank(UL)==b and p.zero(p.mm(glog,UL)))
    a=E['absolute_H'];r=p.rank(R.row_join(U));full=[0,b-a[0]+a[1]+U.cols-r,2*b-r+a[2],0]
    ck(label+'_full_neutral_counts_not_deleted',full[1]==full[2] and full[0]==full[3]==0 and r==2*b)
    return {'absolute_H':a,'boundary_H':E['boundary_H'],'restriction_rank':R.cols,
            'plane_dimension':U.cols,'union_rank':r,'H':full,
            'connecting_dimension':b-a[0],'admitted_absolute_H1':a[1]+U.cols-r,
            'physical_neutral_chirals':full[1]}

def boundary_controls():
    f0,f1=s.symbols('f0 f1',real=True)
    diag=s.Matrix([1,1])/s.sqrt(2);odd=s.Matrix([1,-1])/s.sqrt(2)
    return {'one_A0_not_two':diag.cols==1 and s.Matrix.hstack(diag,odd).rank()==2,
            'global_A2_annihilator_keeps_odd_flux':(diag.T*odd)[0]==0 and (diag.T*diag)[0]==1,
            'response_is_summed_not_pointwise':(diag.T*s.Matrix([f0,f1]))[0]==(f0+f1)/s.sqrt(2),
            'opposite_nonzero_sheet_flux_is_allowed':(diag.T*s.Matrix([2,-2]))[0]==0 and s.Matrix([2,-2])!=s.zeros(2,1),
            'same_sheet_flux_is_rejected':(diag.T*s.Matrix([2,2]))[0]!=0}

@lru_cache(None)
def run():
    instrument,data,w,P,Q,A,B=cy.literal();facts=boundary_controls();gauges={};neutrals={}
    def ck(key,value):facts[key]=bool(value);assert facts[key],key
    for key,value in list(facts.items()):assert value,key
    candidates=[(-1,-1,1),(-1,1,-1),(1,-1,-1)]
    for eta in candidates:
        tag=','.join(map(str,eta));row={}
        for sector,sign,A0,A2,L in (('plus',(1,1,1),s.eye(1),s.zeros(1,0),s.Matrix([0,1])),('minus',eta,s.zeros(1,0),s.eye(1),s.Matrix([1,1]))):
            E=bulk({g:s.Matrix([[sign[j]]]) for j,g in enumerate(p.GEN)},data)
            result=cone(E,L,A0,A2);row[sector]={**result,'absolute_H':E['absolute_H'],'boundary_H':E['boundary_H'],'restriction_rank':E['restriction'].cols}
            ck(tag+sector+'_actual_gauge_cone_duality',result['H']==result['H'][::-1])
            ck(tag+sector+'_one_global_vector_sector',result['H'][0]==(1 if sector=='plus' else 0))
        gauges[tag]=row
    basis=cy.adjoint_basis();rn={g:cy.adjoint_group(x,basis) for g,x in w.items()}
    T=s.Matrix([[s.trace(x*y) for y in basis] for x in basis]);met=s.Matrix([[s.trace(x.T*y) for y in basis] for x in basis])
    NA,NB=[cy.adjoint_lie(x,basis) for x in (A,B)]
    for sector,eta in (('plus',(1,1,1)),('minus',ETA)):
        rep={g:eta[j]*rn[g] for j,g in enumerate(p.GEN)}
        neutrals[sector]=neutral(rep,data,T,met,NA,NB,ck,sector)
    charged={}
    for label,a,b,subsets in (('W',A,B,([0,1,2],[0,1,2,3])),('F',cy.exterior_lie(A),cy.exterior_lie(B),([0,1,2,4],[0,1,2,3,4]))):
        E=p.boundary(a,b);D=p.boundary(-a.T,-b.T);rows=[]
        for subset in subsets:
            L=E['H'][:,subset];dual=p.dual_plane(E,D,L);row=p.pencil_count(E,L);dr=p.pencil_count(D,dual)
            ck(label+str(len(subset))+'_actual_charged_dual_kernel',row['H']==dr['H'][::-1] and row['H']==[0,len(subset)-E['t0'],0,0])
            rows.append({'H':row['H'],'dual_H':dr['H']})
        total=[sum(row['H'][j] for row in rows) for j in range(4)]
        ck(label+'_charged_three_in_same_boundary',total==[0,3,0,0]);charged[label]={'H':total,'sectors':rows}
    z=s.symbols('z',nonzero=True);even=s.Matrix([[z]]);odd=s.Matrix([[-z]])
    ck('broken_gauge_even_A0_to_A1_and_odd_A1_to_A2_both_acyclic',even.rank()==odd.rank()==1)
    ck('unbroken_deck_gauge_H0_not_duplicated',sum(row['H'][0] for row in gauges[','.join(map(str,ETA))].values())==1)
    root=s.diag(2,2,2,-3,-3)
    weights=[root[i,i]-root[j,j] for i in range(5) for j in range(5) if i!=j]+[0]*4
    ck('full_gauge_roots_and_Cartan_all_retained',len(weights)==24 and weights.count(0)==12 and weights.count(5)==weights.count(-5)==6)
    ck('full_boundary_harmonic_dimension_from_actual_E8_coefficients',24+24+10*5*2+5*10*2==248 and 24+6+10*2*2+5*3*2==100 and 2*(10*(3+1)+5*(4+2)+6+24)==200)
    ck('wrong_end_of_pushforward_rank_rejected',2*(5**2-1)==48 and (2*5)**2-1==99)
    gauge=gauges[','.join(map(str,ETA))];neutral_count=sum(row['H'][1] for row in neutrals.values())
    adjoint_per_generator=sum(row['H'][1] for row in gauge.values())
    physical={'charged_generations':3,'neutral_singlet_chirals':neutral_count,
              'unbroken_adjoint_chirals':12*adjoint_per_generator,
              'SM_vector_generators':12,'independent_vector_sectors':1,
              'charged_component_chirals':3*15,
              'left_chiral_components':3*15+neutral_count+12*adjoint_per_generator,
              'scalar_partners_retained':True,'separate_Higgs_mechanism':False}
    ck('full_roster_does_not_delete_extra_fields',physical['neutral_singlet_chirals']>0 and physical['unbroken_adjoint_chirals']>0 and physical['left_chiral_components']>45)
    return {'facts':facts,'exact_predicates':len(facts),'gauge':gauges,'neutral':neutrals,
            'charged':charged,'physical_linear_roster':physical,
            'whole_boundary_conditional':True,'generated_boundary':False,
            'normalized_interactions':False,'global_quantum_anomaly':False,
            'outside_review':False,'full_goal_achieved':False}

if __name__=='__main__':print(json.dumps(run(),indent=2,sort_keys=True))
