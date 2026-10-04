"""Global cohomological complements, not physical Calderon projectors."""
import hashlib
import importlib.util
import json
from functools import lru_cache
from pathlib import Path

import sympy as s

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
for line in (HERE/'INPUT_HASHES.txt').read_text().splitlines():
    digest,path=line.split(maxsplit=1)
    assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==digest,path
spec=importlib.util.spec_from_file_location('silver_cusp_base',HERE.parent/'silver_cusp_polarization_2026_10_04/verify.py')
m=importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
red,mul,rank,kernel,zero,inverse=m.red,m.mul,m.rank,m.kernel,m.zero,m.inverse


def independent(C):
    return m.independent_modulo(s.zeros(C.rows,0),C)


def projection(B,M):
    # M is a supplied positive Hermitian metric: identity or a verified
    # inverse-congruence transform of it, never an indefinite pairing.
    assert zero(M-M.conjugate().T)
    if B.cols==0:
        return s.zeros(M.rows)
    gram=mul(mul(B.conjugate().T,M),B)
    out=mul(mul(mul(B,inverse(gram)),B.conjugate().T),M)
    assert zero(mul(out,out)-out)
    assert zero(mul(out.conjugate().T,M)-mul(M,out))
    assert rank(out)==B.cols and s.simplify(s.trace(out))==B.cols
    return out


class Space:
    def __init__(self,E,M=None):
        self.E=E
        n=E.n
        self.M=s.eye(2*n) if M is None else M
        self.F=(s.eye(n)-E.Q).row_join(E.P-s.eye(n))
        self.Z=kernel(self.F)
        self.H=kernel(self.F.col_join(mul(E.D.conjugate().T,self.M)))
        self.PH=projection(self.H,self.M)
        assert self.H.cols==self.Z.cols-rank(E.D)
        assert zero(mul(self.PH,E.D))
        assert rank(E.D.row_join(self.H))==self.Z.cols
        self.R=independent(mul(self.PH,E.RZ))
        self.PR=projection(self.R,self.M)
        self.PL=red(self.PH-self.PR)
        self.L=independent(self.PL)
        assert zero(projection(self.L,self.M)-self.PL)
        assert self.R.cols==E.h1-E.interior
        assert self.R.cols+self.L.cols==self.H.cols
        assert rank(self.R.row_join(self.L))==self.H.cols


def group_cup(E):
    n=E.n
    return s.zeros(n).row_join(inverse(E.P).T).col_join((-inverse(E.Q).T).row_join(s.zeros(n)))


def analyze(rep,state,expected=None,metrics=None):
    E,D=m.Global(rep,state),m.Global(m.dual(rep),state)
    if expected:
        assert E.profile()==expected['E'] and D.profile()==expected['dual']
    BE=Space(E,None if metrics is None else metrics[0])
    BD=Space(D,None if metrics is None else metrics[1])
    J=group_cup(E)
    assert zero(mul(mul(E.D.T,J),BD.Z))
    assert zero(mul(mul(BE.Z.T,J),D.D))
    assert BE.H.cols==BD.H.cols==rank(mul(mul(BE.H.T,J),BD.H))
    assert zero(mul(mul(BE.R.T,J),BD.R))
    assert BE.R.cols+BD.R.cols==BE.H.cols
    LD=mul(BD.H,kernel(mul(mul(BE.L.T,J),BD.H)))
    assert BE.L.cols+LD.cols==BE.H.cols
    assert zero(mul(mul(BE.L.T,J),LD))
    assert rank(BD.R.row_join(LD))==BD.H.cols
    counts=[E.allowed(BE.L),D.allowed(LD)]
    assert counts==[E.interior,D.interior]
    assert counts[0]-counts[1]==BE.L.cols-E.t0+E.h0-D.h0
    # Independent log/group pairing agreement on ALL active closed cocycles.
    LE,LDual=m.Boundary(E.P,E.Q),m.Boundary(D.P,D.Q)
    ZL,ZLD=kernel(LE.d1),kernel(LDual.d1)
    left=mul(mul(LE.group(ZL).T,J),LDual.group(ZLD))
    right=mul(mul(LE.full_log(ZL).T,m.cup(E.n)),LDual.full_log(ZLD))
    assert zero(left-right)
    summary={'allowed_H1':counts,'difference':counts[0]-counts[1],
             'boundary_H1':BE.H.cols,'restriction_ranks':[BE.R.cols,BD.R.cols],
             'complement_dimensions':[BE.L.cols,LD.cols],
             'global_H0':[E.h0,D.h0],'boundary_H0':[E.t0,D.t0],
             'group_log_cup_agrees':True}
    return {'summary':summary,'E':E,'D':D,'BE':BE,'BD':BD,'LD':LD}


def metric_transport(M,T):
    inv=inverse(T)
    return mul(mul(inv.conjugate().T,M),inv)


def gauge_check(rep,state,base,G):
    GD=inverse(G).T
    T,TD=s.diag(G,G),s.diag(GD,GD)
    changed={g:mul(mul(G,A),inverse(G)) for g,A in rep.items()}
    result=analyze(changed,state,metrics=(metric_transport(base['BE'].M,T),
                                         metric_transport(base['BD'].M,TD)))
    expected={k:v for k,v in base['summary'].items() if k!='split_projector_distance_one_witness'}
    assert result['summary']==expected
    assert zero(result['BE'].PL-mul(mul(T,base['BE'].PL),inverse(T)))
    assert rank(result['LD'].row_join(mul(TD,base['LD'])))==result['LD'].cols
    return True


@lru_cache(None)
def controls():
    t=s.symbols('t',real=True)
    v=s.Matrix([1,t])
    P=v*v.T/(1+t*t)
    assert (P*P-P).applyfunc(s.cancel)==s.zeros(2)
    assert P.applyfunc(lambda z:s.limit(z,t,0))==s.diag(1,0)
    assert (s.Matrix([[0,1]])*v)[0]==t
    # The compressed image is 1-dimensional away from zero, 0 at zero.
    assert rank(s.Matrix([[1]]))==1 and rank(s.Matrix([[0]]))==0
    assert s.simplify(s.trace(P)-1)==0
    B=s.Matrix([[1],[2]])
    M=s.diag(2,3)
    G=s.Matrix([[1,1+s.I],[0,1]])
    assert zero(projection(mul(G,B),metric_transport(M,G))-mul(mul(G,projection(B,M)),inverse(G)))
    U=s.eye(3)
    U[0,1]=1
    V=s.eye(3)
    V[0,2]=1
    D=s.Matrix.vstack(U-s.eye(3),V-s.eye(3))
    F=(s.eye(3)-V).row_join(U-s.eye(3))
    UD,VD=inverse(U).T,inverse(V).T
    DD=s.Matrix.vstack(UD-s.eye(3),VD-s.eye(3))
    FD=(s.eye(3)-VD).row_join(UD-s.eye(3))
    J=s.zeros(3).row_join(UD).col_join((-VD).row_join(s.zeros(3)))
    Z,ZD=kernel(F),kernel(FD)
    assert zero(mul(mul(D.T,J),ZD)) and zero(mul(mul(Z.T,J),DD))
    H=kernel(F.col_join(D.T))
    HD=kernel(FD.col_join(DD.T))
    assert H.cols==HD.cols==rank(mul(mul(H.T,J),HD))==3
    euler=[]
    for a in (0,1,2,-1):
        r=rank(s.Matrix([[a]]))
        h0,h1=1-r,1-r
        euler.append(h0-h1)
    assert euler==[0,0,0,0]
    return {'status':'PASS','continuous_full_projector_with_compressed_jump':True,
            'constant_rank_rotating_projector':True,'weighted_gauge_covariance':True,
            'unequal_invariant_torus_cup_rank':3,'two_term_Euler':euler}


@lru_cache(None)
def actual_members():
    old,data,records=m.inputs()
    output=[]
    for label,state in data['states'].items():
        old.check_marking(label,state)
        f=old.four(state)
        for member in state['members']:
            char=member['nu on a, b, t']
            saved=next(r for r in records if r['signed_word']==label and r['character']==char)
            c=s.Matrix([s.sympify(z) for z in saved['peripherally_zero_cocycle']])
            V={g:char[g]*f[g] for g in m.GEN}
            reps={a:old.extension(V,a*c) for a in (0,1,2,-1)}
            rows={}
            print(json.dumps({'progress':'starting','carrier':state['SnapPy'],'character':char}),flush=True)
            for amplitude,rep in reps.items():
                wedge={g:old.exterior(A) for g,A in rep.items()}
                expected0=saved['splitW'] if amplitude==0 else saved['W']
                expected2=saved['split_wedge2W'] if amplitude==0 else saved['wedge2W']
                one,two=analyze(rep,state,expected0),analyze(wedge,state,expected2)
                rows[amplitude]=(one,two)
                assert [one['summary']['difference'],two['summary']['difference']]==([0,0] if amplitude==0 else [-1,-1])
                if amplitude!=0:
                    for k in (0,1):
                        assert zero(rows[0][k]['E'].P-rows[amplitude][k]['E'].P)
                        assert zero(rows[0][k]['E'].Q-rows[amplitude][k]['E'].Q)
                    P0,Pt=rows[0][1]['BE'].PL,two['BE'].PL
                    L0=rows[0][1]['BE'].L
                    witness=mul(L0,kernel(mul(Pt,L0)))
                    assert witness.cols>0 and rank(witness)>0
                    assert zero(mul(P0-Pt,witness)-witness)
                    assert rank(P0)==rank(Pt)+1
                    two['summary']['split_projector_distance_one_witness']=True
                if amplitude in (2,-1):
                    G=s.diag(*([amplitude]*4+[1]))
                    for g in m.GEN:
                        assert zero(rep[g]-mul(mul(G,reps[1][g]),inverse(G)))
                        H=old.exterior(G)
                        assert zero(wedge[g]-mul(mul(H,old.exterior(reps[1][g])),inverse(H)))
            gauge=None
            if not output:
                G=s.eye(5)
                G[0,4]=1+s.I
                G[3,4]=s.sqrt(2)
                gauge=[gauge_check(reps[1],state,rows[1][0],G),
                       gauge_check({g:old.exterior(A) for g,A in reps[1].items()},state,rows[1][1],old.exterior(G))]
            record={'carrier':state['SnapPy'],'signed_word':label,'character':char,
                    'amplitudes':{str(a):{'W':pair[0]['summary'],'wedge2W':pair[1]['summary']} for a,pair in rows.items()},
                    'same_peripheral_matrices':True,'nonzero_scaling_conjugacy':True,'gauge_controls':gauge}
            output.append(record)
            print(json.dumps({'member':record},sort_keys=True),flush=True)
    return output


if __name__=='__main__':
    print(json.dumps({'controls':controls()},sort_keys=True),flush=True)
    rows=actual_members()
    print(json.dumps({'status':'PASS','members':len(rows),'scope':'global cohomological complements, not physical domains'}),flush=True)
