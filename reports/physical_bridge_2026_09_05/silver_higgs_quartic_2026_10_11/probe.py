"""Actual neutral boundary response and Higgs quartic; seal before science."""
import hashlib
import importlib.util
import json
from functools import lru_cache
from pathlib import Path
import sympy as s

HERE=Path(__file__).resolve().parent; OLD=HERE.parent
def load(name,path):
    sp=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m
c=load('quartic_charged_native',OLD/'silver_charged_cubic_2026_10_11/probe.py')
sel=load('quartic_selective_native',OLD/'silver_selective_boundary_2026_10_11/probe.py')
p=c.p; mm,rank,zero,ker,inv,cols=p.mm,p.rank,p.zero,sel.ker,sel.inv,sel.cols
z=p.z; PAIRS=c.PAIRS

def digest(value):
    return hashlib.sha256(json.dumps(value,separators=(',',':')).encode()).hexdigest()
def matrix_pairs(a):return [[c.pair(x) for x in row] for row in a.tolist()]
def skew(f):
    a=s.zeros(5)
    for x,(i,j) in zip(f,PAIRS):a[i,j]=x;a[j,i]=-x
    return a
def moment(f,g):
    a=skew(f)*skew(g).T
    return a-s.trace(a)*s.eye(5)/5
def coords(x):
    assert s.expand(s.trace(x))==0
    return s.Matrix([x[i,j] for i in range(5) for j in range(5) if i!=j]+[x[i,i] for i in range(4)])
def in_N(x):return all(s.expand(x[i,j])==0 for i in range(5) for j in range(5) if not (i<4 and j==4))
def quartic_detector(x,S,P):return -mm(mm(mm(x.T,S,z),P,z),x,z)
def canonical_profile(F):
    rr,piv=p.dm(F.T,z).rref();free=list(piv)
    # Pivot rows of F choose a reproducible frame for its COLUMN space.
    out=p.dm(F,z).matmul(p.dm(F[free,:],z).inv()).to_Matrix()
    return out,free

def response(w,data,A,B,ck):
    basis=p.cy.adjoint_basis(); rn={g:p.cy.adjoint_group(x,basis) for g,x in w.items()}
    T=s.Matrix([[s.trace(x*y) for y in basis] for x in basis])
    met=s.Matrix([[s.trace(x.T*y) for y in basis] for x in basis]);met1=s.diag(met,met)
    P,Q=[p.cy.word(rn,t) for t in data['cusp_words']]
    D=(P-s.eye(24)).col_join(Q-s.eye(24)); G=(s.eye(24)-Q).row_join(P-s.eye(24))
    F=s.Matrix.vstack(*(p.fox(rn,t) for t in data['relators']))
    Rmap=s.Matrix.vstack(*(p.fox(rn,t) for t in data['cusp_words']))
    bulk0=s.Matrix.vstack(*(rn[g]-s.eye(24) for g in p.GEN))
    ck('actual_neutral_bulk_chain',zero(mm(F,bulk0)) and zero(mm(Rmap,bulk0)-D))
    HH=ker(G.col_join(D.T)); pr=mm(mm(HH,inv(mm(HH.T,HH))),HH.T)
    R=cols(mm(mm(pr,Rmap),ker(F)))
    J=s.zeros(24).row_join(inv(P).T).col_join((-inv(Q).T).row_join(s.zeros(24)))
    S0=mm(J,s.diag(T,T)); pair=mm(mm(R.T,S0),HH)
    piv=list(p.dm(pair).rref()[1]); U0=mm(HH[:,piv],inv(pair[:,piv]))
    U=U0+mm(R,mm(mm(U0.T,S0),U0))/2
    NA,NB=p.cy.adjoint_lie(A,basis),p.cy.adjoint_lie(B,basis)
    d0=NA.col_join(NB);d1=(-NB).row_join(NA)
    hl=ker(d1.col_join(mm(d0.T,met1)))
    ph=mm(mm(hl,inv(mm(mm(hl.T,met1),hl))),mm(hl.T,met1))
    t1=s.diag(sel.integral(NA),sel.integral(NB))
    RL,UL=[mm(mm(ph,inv(t1)),x) for x in (R,U)]
    M=cols(mm(inv(met1),d1.T)).row_join(UL)
    Z=cols(d0).row_join(RL); C=M.row_join(Z)
    ck('actual_log_transport_and_complement_dimensions',zero(mm(t1,d0)-D)
       and (M.cols,Z.cols,rank(C))==(24,24,48))
    PP=mm(C[:,:24],inv(C)[:24,:])
    S=s.zeros(24).row_join(T).col_join((-T).row_join(s.zeros(24)))
    ck('both_response_spaces_actual_trace_isotropic',zero(mm(mm(M.T,S),M))
       and zero(mm(mm(Z.T,S),Z)) and rank(S)==48)
    ck('actual_response_projection_and_source_equation',rank(PP)==24 and zero(mm(PP,PP)-PP)
       and zero(mm(PP,M)-M) and zero(mm(PP,Z)) and zero(mm(d1,PP)-d1))
    wrong=cols(mm(inv(met1),d1.T)).row_join(RL).row_join(Z)
    ck('equal_restriction_is_singular_opposite',rank(wrong)==42)
    ck('zero_and_identity_response_are_rejected',not zero(mm(d1,s.zeros(48))-d1)
       and not zero(mm(s.eye(48),Z)))
    control=quartic_detector(s.eye(48),S,PP)
    witness=next(((i,j,control[i,j]) for i in range(48) for j in range(48) if control[i,j]!=0),None)
    ck('actual_response_nonzero_opposite',witness is not None and rank(control)==24)
    return dict(P=PP,S=S,d1=d1,A=NA,B=NB,basis=basis,
                spaces=dict(restriction=c.plane_hash(RL),admitted=c.plane_hash(M),
                    closed=c.plane_hash(Z),projection=digest(matrix_pairs(PP))),
                control=dict(indices=list(witness[:2]),value_Qsqrt2=c.pair(witness[2])))

@lru_cache(None)
def run():
    facts={}
    def ck(k,v):facts[k]=bool(v);assert facts[k],k
    _,data,w,P,Q,A,B=p.cy.literal(); rr=response(w,data,A,B,ck)
    model=json.loads((OLD/'silver_selective_boundary_2026_10_11/MODEL.json').read_text())
    a,b=p.cy.exterior_lie(A),p.cy.exterior_lie(B);da,db=-a.T,-b.T
    E,D=p.boundary(a,b),p.boundary(da,db);L=E['H'][:,model['F_weak_plane']]
    LD=p.dual_plane(E,D,L);M,MD=E['U'].row_join(L),D['U'].row_join(LD)
    f=c.primitives(dict(a=a,b=b,M=M),3,ck,'weak')
    g=c.primitives(dict(a=da,b=db,M=MD),-3,ck,'Hu')
    ck('actual_weak_and_Hu_counts',[f['F'].cols,g['F'].cols]==[2,1])
    ck('actual_flags_not_selected_free_coordinates',all(zero(f['F'][i,:],z) for i,ij in enumerate(PAIRS) if 4 in ij)
       and all(zero(g['F'][i,:],z) for i,ij in enumerate(PAIRS) if 4 not in ij))
    # ALL coefficient basis entries and ALL sl5 generators: actual moment Ward.
    moments={(i,j):moment(s.eye(10)[:,i],s.eye(10)[:,j]) for i in range(10) for j in range(10)}
    ck('full_moment_Ward',all(s.expand(s.trace(q*moments[i,j])-eq[j,i])==0
        for q,eq in [(q,p.cy.exterior_lie(q)) for q in rr['basis']] for i in range(10) for j in range(10)))
    ck('nonzero_moment_opposite',not zero(moment(s.eye(10)[:,0],s.eye(10)[:,0])))
    gv=g['F'][:,0];gx=da*gv;gy=(db-3*z*s.eye(10))*gv;xis=[]
    for i in range(2):
        fv=f['F'][:,i];fx=a*fv;fy=(b+3*z*s.eye(10))*fv
        xx,yy=-moment(fx,gv),-moment(fy,gv)
        gamma=moment(fx,gy)-moment(fy,gx); xi=coords(xx).col_join(coords(yy));xis.append(xi)
        ck('actual_source_exact_and_trace_null_'+str(i),in_N(xx) and in_N(yy) and in_N(gamma)
           and zero(mm(rr['d1'],xi,z)-coords(gamma),z))
    X=s.Matrix.hstack(*xis); K=quartic_detector(X,rr['S'],rr['P']);degree=2*(f['r']+g['r']+1)
    ck('actual_quartic_degree_and_exchange_symmetry',degree==36 and zero(K-K.T,z)
       and all(s.degree(x,z)<=degree for x in K if x!=0))
    ck('actual_primitive_trace_null_not_abelianized',zero(mm(mm(X.T,rr['S'],z),X,z),z))
    cf,fi=canonical_profile(f['F']);cg,gi=canonical_profile(g['F']);samples=[];frames=[]
    for t in range(1,111):
        ff,gg=cf.subs(z,t),cg.subs(z,t)
        if any(x.has(s.zoo,s.nan,s.oo,-s.oo) for x in list(ff)+list(gg)):continue
        ss=[]
        for i in range(2):
            v,u=ff[:,i],gg[:,0]
            ss.append(coords(-moment(a*v,u)).col_join(coords(-moment((b+3*t*s.eye(10))*v,u))))
        val=quartic_detector(s.Matrix.hstack(*ss),rr['S'],rr['P'])
        samples.append(dict(t=t,entries=matrix_pairs(val)))
        frames.append([t,matrix_pairs(ff),matrix_pairs(gg)])
        if len(samples)==73:break
    ck('characteristic_zero_comparison_points',len(samples)==73 and len({x['t'] for x in samples})==73)
    q=s.symbols('q');mass=s.Rational(7);src=s.Rational(3)*q*q
    heavy=-src/mass;eff=s.expand(mass*heavy**2/2+src*heavy)
    ck('physical_Gaussian_sign_factor_control',eff==-s.Rational(9,14)*q**4 and eff!=s.Rational(9,14)*q**4)
    return dict(facts=facts,predicates_passed=len(facts),response_spaces=rr['spaces'],
        response_control=rr['control'],boundary_plane_sha256=[c.plane_hash(M),c.plane_hash(MD)],
        quartic=dict(shape=[2,2],degree_bound=degree,rank=rank(K,z),zero=zero(K,z),
            polynomials=[str(s.expand(x)) for x in K],canonical_frame_rows=[fi,gi],
            points=[v['t'] for v in samples],samples_sha256=digest(samples),frames_sha256=digest(frames),
            first_values=samples[:3]),same_boundary=True,actual_massive_trace_reduced=True,
        smooth_Green_hypotheses_conditional=True,global_PDE_numerically_solved=False,
        all_quartics_computed=False,normalized_values=False,generated_selection=False,
        outside_review=False,full_goal_achieved=False)
if __name__=='__main__':print(json.dumps(run(),sort_keys=True,indent=2))
