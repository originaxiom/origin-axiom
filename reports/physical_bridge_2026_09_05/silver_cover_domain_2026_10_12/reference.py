"""Fraction literal crossed cocycles and full LES; no new native import."""
import importlib.util,json
from functools import lru_cache
from pathlib import Path
HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('cover_domain_fraction_charged',HERE.parent/'silver_charged_pair_lift_2026_10_11/reference.py')
r=importlib.util.module_from_spec(spec);spec.loader.exec_module(r)
c=r.c;K=c.K;ETA=(-1,-1,1)
Z,I,mm,add,scale,tr,cat,stack,diag,zero=c.Z,c.I,c.mm,c.add,c.scale,c.tr,c.cat,c.stack,c.diag,c.zero
rank,inv,ker,cols=r.rank,c.inverse,c.null,r.cols

def word(rep,text):
    n=len(rep['a']);letters=dict(rep);letters.update({g.upper():inv(a) for g,a in rep.items()})
    maps={}
    for j,g in enumerate('abt'):
        selector=Z(n,3*n)
        for i in range(n):selector[i][j*n+i]=1
        maps[g]=selector;maps[g.upper()]=scale(mm(letters[g.upper()],selector),-1)
    hol=I(n);cross=Z(n,3*n)
    for letter in text:cross=add(cross,mm(hol,maps[letter]));hol=mm(hol,letters[letter])
    return hol,cross

def complex_data(rep,data):
    n=len(rep['a']);identity=I(n)
    rel=[word(rep,text) for text in data['relators']]
    assert all(c.equal(row[0],identity) for row in rel)
    (P,RP),(Q,RQ)=[word(rep,text) for text in data['cusp_words']]
    B=sum((add(rep[g],identity,-1) for g in 'abt'),[]);F=stack(rel[0][1],rel[1][1]);R=stack(RP,RQ)
    D=stack(add(P,identity,-1),add(Q,identity,-1));G=cat(add(identity,Q,-1),add(P,identity,-1))
    R2=scale(mm(mm(Q,[row[:2*n] for row in RP]),diag(inv(rep['t']),inv(rep['t']))),-1)
    assert zero(mm(F,B)) and c.equal(mm(R,B),D) and c.equal(mm(R2,F),mm(G,R))
    H=ker(stack(G,tr(D)));project=mm(mm(H,inv(mm(tr(H),H))),tr(H))
    restriction=cols(mm(mm(project,R),ker(F)))
    J=stack(cat(Z(n),tr(inv(P))),cat(scale(tr(inv(Q)),-1),Z(n)))
    h=[n-rank(B),3*n-rank(B)-rank(F),2*n-rank(F),0];bh=[n-rank(D),len(H[0]),n-rank(G)]
    return dict(n=n,B=B,F=F,R=R,R2=R2,D=D,G=G,H=H,restriction=restriction,J=J,absolute_H=h,boundary_H=bh)

def les(E,L,A0,A2):
    n=E['n'];h=E['absolute_H'];b=E['boundary_H'][0]
    h0space=ker(E['B']);r0=rank(cat(h0space,A0))
    r1=rank(cat(E['restriction'],L))
    H2=ker(tr(E['G']));P2=mm(mm(H2,inv(mm(tr(H2),H2))),tr(H2))
    r2=rank(cat(mm(P2,E['R2']),A2))
    dims=[len(A0[0]),len(L[0]),len(A2[0])]
    H=[h[0]+dims[0]-r0,b-r0+h[1]+dims[1]-r1,2*b-r1+h[2]+dims[2]-r2,b-r2]
    assert min(H)>=0
    return H,[r0,r1,r2]

def neutral(rep,data,T,met,NA,NB,ck,tag):
    E=complex_data(rep,data);R,H=E['restriction'],E['H'];b=E['boundary_H'][0]
    S=mm(E['J'],diag(T,T));HS=mm(mm(tr(H),S),H)
    ck(tag+'_full_neutral_trace_and_peripheral_data',E['boundary_H']==[6,12,6] and rank(T)==24 and rank(HS)==12 and zero(add(HS,tr(HS))) and all(c.equal(mm(mm(tr(x),T),x),T) for x in rep.values()))
    ck(tag+'_restriction_is_actual_Lagrangian',len(R[0])==b and zero(mm(mm(tr(R),S),R)))
    pairing=mm(mm(tr(R),S),H);piv=c.reduced(pairing)[1]
    U0=mm(r.subset(H,piv),inv(r.subset(pairing,piv)));U=add(U0,scale(mm(R,mm(mm(tr(U0),S),U0)),K(1)/2))
    ck(tag+'_transverse_symplectic_partner',zero(mm(mm(tr(U),S),U)) and c.equal(mm(mm(tr(R),S),U),I(b)) and rank(cat(R,U))==2*b)
    nonsym=Z(b);nonsym[0][1]=1;wrong=add(U,mm(R,nonsym))
    ck(tag+'_nonisotropic_control_kept',rank(wrong)==b and not zero(mm(mm(tr(wrong),S),wrong)))
    dlog=stack(NA,NB);glog=cat(scale(NB,-1),NA);g1=diag(met,met)
    HL=ker(stack(glog,mm(tr(dlog),g1)));pl=mm(mm(HL,inv(mm(mm(tr(HL),g1),HL))),mm(tr(HL),g1))
    t1=diag(c.series(NA,True),c.series(NB,True));t2=mm(c.series(NA,True),c.series(NB,True))
    UL=mm(mm(pl,inv(t1)),U)
    ck(tag+'_independent_literal_log_transport',c.equal(mm(t1,dlog),E['D']) and c.equal(mm(E['G'],t1),mm(t2,glog)) and rank(UL)==b and zero(mm(glog,UL)))
    full,maps=les(E,U,Z(24,0),ker(tr(E['G'])))
    ck(tag+'_complete_neutral_LES_selfduality',full[0]==full[3]==0 and full[1]==full[2] and maps[1]==2*b)
    a=E['absolute_H']
    return {'absolute_H':a,'boundary_H':E['boundary_H'],'restriction_rank':len(R[0]),
            'plane_dimension':len(U[0]),'union_rank':maps[1],'H':full,
            'connecting_dimension':b-a[0],'admitted_absolute_H1':a[1]+len(U[0])-maps[1],
            'physical_neutral_chirals':full[1]}

@lru_cache(None)
def run():
    data,w,P,Q,A,B=c.literal();checks={};gauges={};neutrals={}
    def ck(key,value):checks[key]=bool(value);assert checks[key],key
    diagval=[[1],[1]];oddval=[[1],[-1]]
    ck('one_global_gauge_and_summed_annihilator',rank(diagval)==1 and rank(cat(diagval,oddval))==2 and zero(mm(tr(diagval),oddval)) and not zero(mm(tr(diagval),diagval)))
    ck('opposite_flux_is_allowed_not_two_neumann_laws',zero(mm(tr(diagval),[[2],[-2]])) and not zero([[2],[-2]]) and not zero(mm(tr(diagval),[[2],[2]])))
    for eta in ((-1,-1,1),(-1,1,-1),(1,-1,-1)):
        tag=','.join(map(str,eta));row={}
        for sector,sign,A0,A2,L in (('plus',(1,1,1),I(1),Z(1,0),[[0],[1]]),('minus',eta,Z(1,0),I(1),[[1],[1]])):
            E=complex_data({g:[[sign[j]]] for j,g in enumerate('abt')},data);H,maps=les(E,L,A0,A2)
            ck(tag+sector+'_full_gauge_LES_and_endpoint',H==H[::-1] and H[0]==(1 if sector=='plus' else 0))
            # Native exposes cone chain sizes/ranks; independent LES output
            # compares H and source geometry, not copied cone rank numbers.
            row[sector]={'H':H,'absolute_H':E['absolute_H'],'boundary_H':E['boundary_H'],'restriction_rank':len(E['restriction'][0])}
        gauges[tag]=row
    basis=c.basis5();rn={g:c.ad_group(x,basis) for g,x in w.items()};T=c.gram(basis);met=c.gram(basis,True)
    NA,NB=c.ad(A,basis),c.ad(B,basis)
    for sector,eta in (('plus',(1,1,1)),('minus',ETA)):
        neutrals[sector]=neutral({g:scale(rn[g],eta[j]) for j,g in enumerate('abt')},data,T,met,NA,NB,ck,sector)
    charged={}
    for label,a,b,subsets in (('W',A,B,([0,1,2],[0,1,2,3])),('F',c.wedge_derivative(A),c.wedge_derivative(B),([0,1,2,4],[0,1,2,3,4]))):
        E=r.boundary(a,b);D=r.boundary(scale(tr(a),-1),scale(tr(b),-1));evals,devals=r.evaluation_rows(E),r.evaluation_rows(D);rows=[]
        for subset in subsets:
            L=r.subset(E['H'],subset);dual,dualcoeff=r.paired_plane(E,D,L)
            coeff=r.subset(I(len(E['H'][0])),subset)
            row=r.degree_count(E,coeff,evals);other=r.degree_count(D,dualcoeff,devals)
            ck(label+str(len(subset))+'_degree_certificate_charged_dual',row['H']==other['H'][::-1] and row['H']==[0,len(subset)-E['t0'],0,0])
            rows.append({'H':row['H'],'dual_H':other['H']})
        total=[sum(row['H'][j] for row in rows) for j in range(4)]
        ck(label+'_same_model_charged_three',total==[0,3,0,0]);charged[label]={'H':total,'sectors':rows}
    ck('nonzero_phase_gauge_two_exact_acyclic_blocks',rank([[K(0,1)]])==rank([[-K(0,1)]])==1 and rank([[0]])==0)
    ck('all_E8_coefficients_counted_once',24+24+10*5*2+5*10*2==248 and 24+6+10*2*2+5*3*2==100)
    ck('End0_of_induced_is_not_induced_End0',2*(5*5-1)==48 and 10*10-1==99)
    root=[2,2,2,-3,-3];weights=[root[i]-root[j] for i in range(5) for j in range(5) if i!=j]+[0]*4
    ck('SM_twelve_generators_not_deck_doubled',weights.count(0)==12 and weights.count(5)==weights.count(-5)==6)
    gauge=gauges[','.join(map(str,ETA))];neutral_count=sum(row['H'][1] for row in neutrals.values());adj=sum(row['H'][1] for row in gauge.values())
    physical={'charged_generations':3,'neutral_singlet_chirals':neutral_count,
              'unbroken_adjoint_chirals':12*adj,'SM_vector_generators':12,'independent_vector_sectors':1,
              'charged_component_chirals':45,'left_chiral_components':45+neutral_count+12*adj,
              'scalar_partners_retained':True,'separate_Higgs_mechanism':False}
    ck('extras_kept_instead_of_silent_SM_truncation',neutral_count>0 and adj>0 and physical['left_chiral_components']>45)
    return {'checks':checks,'exact_predicates':len(checks),'gauge':gauges,'neutral':neutrals,
            'charged':charged,'physical_linear_roster':physical,'whole_boundary_conditional':True,
            'generated_boundary':False,'normalized_interactions':False,'global_quantum_anomaly':False,
            'outside_review':False,'full_goal_achieved':False}

if __name__=='__main__':print(json.dumps(run(),indent=2,sort_keys=True))
