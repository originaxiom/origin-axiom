"""Fraction End25/crossed-word response and characteristic-zero certificate."""
import hashlib
import importlib.util
import json
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path

HERE=Path(__file__).resolve().parent;OLD=HERE.parent
def load(name,path):
    sp=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m
r=load('quartic_fraction_charged',OLD/'silver_charged_cubic_2026_10_11/reference.py')
mp=load('quartic_fraction_End25',OLD/'silver_physical_multiplets_2026_10_11/reference.py')
c,K=r.c,r.K;PAIRS=r.PAIRS
def digest(x):return hashlib.sha256(json.dumps(x,separators=(',',':')).encode()).hexdigest()
def convert(a,field):return [[field(x.a,x.b) if hasattr(x,'a') else field(x) for x in row] for row in a]
def pairs(a):return [[[str((x if isinstance(x,K) else K(x)).a),str((x if isinstance(x,K) else K(x)).b)] for x in row] for row in a]
def cols(a):
    piv=c.reduced(a)[1]
    return [[row[i] for i in piv] for row in a]
def skew(f):
    out=c.Z(5)
    for x,(i,j) in zip(f,PAIRS):out[i][j]=x;out[j][i]=-x
    return out
def moment(f,g):
    x=c.mm(skew(f),c.tr(skew(g)));trace=sum(x[i][i] for i in range(5))/K(5)
    return c.add(x,c.scale(c.I(5),-trace))
def coords(x):
    assert sum(x[i][i] for i in range(5))==0
    return [x[i][j] for i in range(5) for j in range(5) if i!=j]+[x[i][i] for i in range(4)]
def in_N(x):return all(not x[i][j] for i in range(5) for j in range(5) if not(i<4 and j==4))
def quartic_detector(x,S,P):return c.scale(c.mm(c.mm(c.mm(c.tr(x),S),P),x),-1)

def response(w,data,A,B,ck):
    wm={g:convert(x,mp.K) for g,x in w.items()};rn,Tm=mp.end0(wm);N=mp.boundary(rn,data)
    R,HH=N['R'],N['H'];Sm=mp.mm(N['J'],mp.diag2(Tm))
    pair=mp.mm(mp.mm(mp.tr(R),Sm),HH);piv=mp.b.elimination(pair,True)[1]
    pick=lambda x:[[row[j] for j in piv] for row in x]
    U0=mp.mm(pick(HH),mp.inv(pick(pair)))
    U=mp.add(U0,[[mp.K(F(1,2))*x for x in row] for row in mp.mm(R,mp.mm(mp.mm(mp.tr(U0),Sm),U0))])
    ck('literal_End25_bulk_and_transverse',mp.zero(mp.mm(N['C'].F,N['C'].B))
       and [N['h0'],N['h1'],N['h2']]==[0,6,6] and mp.rank(mp.hc(R,U))==12)
    basis=c.basis5();T=c.gram(basis);met=c.gram(basis,True);met1=c.diag(met,met)
    NA,NB=c.ad(A,basis),c.ad(B,basis);d0=c.stack(NA,NB);d1=c.cat(c.scale(NB,-1),NA)
    hl=c.null(c.stack(d1,c.mm(c.tr(d0),met1)));ph=c.project(hl,met1)
    t1=c.diag(c.series(NA,True),c.series(NB,True));ti=c.inverse(t1)
    RL,UL=[c.mm(c.mm(ph,ti),convert(x,K)) for x in (R,U)]
    M=c.cat(cols(c.mm(c.inverse(met1),c.tr(d1))),UL);Z=c.cat(cols(d0),RL);C=c.cat(M,Z)
    ck('actual_log_transport_and_complement_dimensions',c.equal(c.mm(t1,d0),convert(N['C'].D,K))
       and (len(M[0]),len(Z[0]),c.rank(C))==(24,24,48))
    PP=c.mm(M,c.inverse(C)[:24]);S=c.stack(c.cat(c.Z(24),T),c.cat(c.scale(T,-1),c.Z(24)))
    ck('both_response_spaces_actual_trace_isotropic',c.zero(c.mm(c.mm(c.tr(M),S),M))
       and c.zero(c.mm(c.mm(c.tr(Z),S),Z)) and c.rank(S)==48)
    ck('actual_response_projection_and_source_equation',c.rank(PP)==24 and c.equal(c.mm(PP,PP),PP)
       and c.equal(c.mm(PP,M),M) and c.zero(c.mm(PP,Z)) and c.equal(c.mm(d1,PP),d1))
    wrong=c.cat(c.cat(cols(c.mm(c.inverse(met1),c.tr(d1))),RL),Z)
    ck('equal_restriction_is_singular_opposite',c.rank(wrong)==42)
    ck('zero_and_identity_response_are_rejected',not c.equal(c.mm(d1,c.Z(48)),d1)
       and not c.zero(c.mm(c.I(48),Z)))
    control=quartic_detector(c.I(48),S,PP)
    witness=next(((i,j,control[i][j]) for i in range(48) for j in range(48) if control[i][j]),None)
    ck('actual_response_nonzero_opposite',witness is not None and c.rank(control)==24)
    return dict(P=PP,S=S,d1=d1,basis=basis,
        spaces=dict(restriction=r.plane_hash(RL),admitted=r.plane_hash(M),closed=r.plane_hash(Z),projection=digest(pairs(PP))),
        control=dict(indices=list(witness[:2]),value_Qsqrt2=pairs([[witness[2]]])[0][0]))

@lru_cache(None)
def run():
    facts={}
    def ck(k,v):facts[k]=bool(v);assert facts[k],k
    data,w,P,Q,A,B=c.literal();rr=response(w,data,A,B,ck)
    model=json.loads((OLD/'silver_selective_boundary_2026_10_11/MODEL.json').read_text())
    a,b=c.wedge_derivative(A),c.wedge_derivative(B);da,db=c.scale(c.tr(a),-1),c.scale(c.tr(b),-1)
    E,D=r.r.boundary(a,b),r.r.boundary(da,db);L=r.r.subset(E['H'],model['F_weak_plane'])
    LD,_=r.r.paired_plane(E,D,L);M,MD=c.cat(E['U'],L),c.cat(D['U'],LD)
    pf=r.build(dict(a=a,b=b,M=M),3);pg=r.build(dict(a=da,b=db,M=MD),-3)
    ck('actual_weak_and_Hu_counts',[len(pf['free']),len(pg['free'])]==[2,1])
    degree=2*(pf['r']+pg['r']+1);ck('actual_degree_bound',degree==36)
    eye=c.I(10)
    moments={(u,v):moment([row[u] for row in eye],[row[v] for row in eye]) for u in range(10) for v in range(10)}
    ck('full_moment_Ward',all(sum(q[i][j]*moments[u,v][j][i] for i in range(5) for j in range(5))==eq[v][u]
        for q,eq in [(q,c.wedge_derivative(q)) for q in rr['basis']] for u in range(10) for v in range(10)))
    ck('nonzero_moment_opposite',not c.zero(moment([row[0] for row in eye],[row[0] for row in eye])))
    frames=[];samples=[];frame_rows=None;any_entry=False;any_det=False
    for t in range(1,111):
        ff,gg=r.evaluate(pf,t),r.evaluate(pg,t)
        if ff is None or gg is None:continue
        if frame_rows is None:frame_rows=[c.reduced(c.tr(x))[1] for x in (ff,gg)]
        subf=[[ff[i][j] for j in range(2)] for i in frame_rows[0]]
        subg=[[gg[i][0]] for i in frame_rows[1]]
        if not r.determinant(subf) or not r.determinant(subg):continue
        ff,gg=c.mm(ff,c.inverse(subf)),c.mm(gg,c.inverse(subg));u=[row[0] for row in gg]
        ck('actual_flags_at_'+str(t),all(not x for i,row in enumerate(ff) for x in row if 4 in PAIRS[i])
           and all(not gg[i][0] for i in range(10) if 4 not in PAIRS[i]))
        xi=[];gu,gv=r.mv(da,u),r.mv(c.add(db,c.scale(c.I(10),-3*t)),u)
        for j in range(2):
            v=[row[j] for row in ff];vx=r.mv(a,v);vy=r.mv(c.add(b,c.scale(c.I(10),3*t)),v)
            xx,yy=c.scale(moment(vx,u),-1),c.scale(moment(vy,u),-1)
            gamma=c.add(moment(vx,gv),moment(vy,gu),-1);x=coords(xx)+coords(yy);xi.append(x)
            ck('actual_source_exact_and_trace_null_'+str(t)+'_'+str(j),in_N(xx) and in_N(yy) and in_N(gamma)
               and r.mv(rr['d1'],x)==coords(gamma))
        X=c.tr(xi);KK=quartic_detector(X,rr['S'],rr['P'])
        ck('actual_quartic_symmetry_'+str(t),c.equal(KK,c.tr(KK)) and c.zero(c.mm(c.mm(c.tr(X),rr['S']),X)))
        any_entry|=not c.zero(KK);any_det|=bool(r.determinant(KK))
        samples.append(dict(t=t,entries=pairs(KK)));frames.append([t,pairs(ff),pairs(gg)])
        if len(samples)==73:break
    ck('characteristic_zero_comparison_points',len(samples)==73 and len({x['t'] for x in samples})==73)
    src=K(3);mass=K(7);heavy=-src/mass;eff=mass*heavy*heavy/2+src*heavy
    ck('physical_Gaussian_sign_factor_control',eff==K(F(-9,14)) and eff!=K(F(9,14)))
    return dict(facts=facts,predicates_passed=len(facts),response_spaces=rr['spaces'],response_control=rr['control'],
        boundary_plane_sha256=[r.plane_hash(M),r.plane_hash(MD)],
        quartic=dict(shape=[2,2],degree_bound=degree,rank=2 if any_det else 1 if any_entry else 0,
            zero=not any_entry,canonical_frame_rows=frame_rows,points=[v['t'] for v in samples],
            samples_sha256=digest(samples),frames_sha256=digest(frames),first_values=samples[:3]),
        same_boundary=True,actual_massive_trace_reduced=True,smooth_Green_hypotheses_conditional=True,
        global_PDE_numerically_solved=False,all_quartics_computed=False,normalized_values=False,
        generated_selection=False,outside_review=False,full_goal_achieved=False,new_native_imported=False)
if __name__=='__main__':print(json.dumps(run(),sort_keys=True,indent=2))
