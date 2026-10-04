"""Conditional dimension obstruction; not a universal physical no-go."""
import hashlib
import importlib.util
import json
from functools import lru_cache
from itertools import combinations
from pathlib import Path
from types import SimpleNamespace

import sympy as s

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
for line in (HERE/'STRUCTURAL_INPUT_HASHES.txt').read_text().splitlines():
    digest,path=line.split(maxsplit=1)
    assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==digest,path
spec=importlib.util.spec_from_file_location('silver_tensor_followup_base',HERE/'verify.py')
t=importlib.util.module_from_spec(spec)
spec.loader.exec_module(t)
red,mul,rank,kernel,zero,inverse=t.red,t.mul,t.rank,t.kernel,t.zero,t.inverse


def boundary(P,Q):
    n=P.rows
    assert zero(mul(P,Q)-mul(Q,P))
    D=(P-s.eye(n)).col_join(Q-s.eye(n))
    F=(s.eye(n)-Q).row_join(P-s.eye(n))
    assert zero(mul(F,D))
    H=kernel(F.col_join(D.conjugate().T))
    betti=[n-rank(D),2*n-rank(D)-rank(F),n-rank(F)]
    assert H.cols==betti[1]
    assert rank(D.row_join(H))==2*n-rank(F)
    return SimpleNamespace(n=n,P=P,Q=Q,D=D,F=F,H=H,betti=betti)


def map_data(A,B,J,Jd):
    for name in ('P','Q'):
        assert zero(mul(J,getattr(A,name))-mul(getattr(B,name),J))
        assert zero(mul(Jd,getattr(B,name))-mul(getattr(A,name),Jd))
    J1,Jd1=s.diag(J,J),s.diag(Jd,Jd)
    assert zero(mul(J1,A.D)-mul(B.D,J))
    assert zero(mul(J,A.F)-mul(B.F,J1))
    assert zero(mul(Jd1,B.D)-mul(A.D,Jd))
    assert zero(mul(Jd,B.F)-mul(A.F,Jd1))
    image=rank(B.D.row_join(mul(J1,A.H)))-rank(B.D)
    reverse=rank(A.D.row_join(mul(Jd1,B.H)))-rank(A.D)
    defect=mul(mul(Jd1,J1)-s.eye(2*A.n),A.H)
    dual_defect=mul(mul(J1,Jd1)-s.eye(2*B.n),B.H)
    return {'rank':image,'reverse_rank':reverse,
            'kernel':A.H.cols-image,'reverse_kernel':B.H.cols-reverse,
            'composition_defect':rank(A.D.row_join(defect))-rank(A.D),
            'dual_composition_defect':rank(B.D.row_join(dual_defect))-rank(B.D),
            'chain_maps':True}


def escape(J,L,target):
    return rank(target.row_join(mul(J,L)))-rank(target)


@lru_cache(None)
def controls():
    eps=s.eye(5)[:,4]
    T=t.tensor(1,2)
    J=t.columns([t.apply(T,eps,s.eye(10)[:,i]) for i in range(10)],10)
    pi=s.diag(*[int(4 not in ij) for ij in combinations(range(5),2)])
    assert zero(mul(J,J)-pi) and rank(J)==6
    I=s.eye(4)
    L=I[:,:2]
    assert escape(I,L,L)==0
    small,large=I[:,:1],I[:,:3]
    assert escape(I,small,large)==0 and escape(I,large,small)==2
    P=s.diag(1,1,1,1,0,0)
    A=s.eye(6)[:,:2]
    B=s.eye(6)[:,[0,1,4,5]]
    assert escape(P,A,B)==0 and escape(P,B,A)==0
    return {'status':'PASS','coefficient_rank':6,'coefficient_projector_identity':True,
            'equal_dimension_positive':True,'unequal_invertible_reverse_escape':2,
            'nonacyclic_unequal_dimension_positive':True}


@lru_cache(None)
def actual_members():
    old,data,records=t.m.inputs()
    native=[json.loads(line)['member'] for line in (HERE/'NATIVE_FIRST.jsonl').read_text().splitlines()
            if 'member' in json.loads(line)]
    assert len(native)==4
    eps=s.eye(5)[:,4]
    J=t.columns([t.apply(t.tensor(1,2),eps,s.eye(10)[:,i]) for i in range(10)],10)
    # In the ordered dual basis the dual-volume construction is the same matrix.
    Jd=J.copy()
    output=[]
    for label,state in data['states'].items():
        old.check_marking(label,state)
        f=old.four(state)
        for member in state['members']:
            char=member['nu on a, b, t']
            saved=next(r for r in records if r['signed_word']==label and r['character']==char)
            original=next(r for r in native if r['signed_word']==label and r['character']==char)
            c=s.Matrix([s.sympify(x) for x in saved['peripherally_zero_cocycle']])
            V={k:char[k]*f[k] for k in t.m.GEN}
            amps={}
            peripherals=[]
            for amplitude in (0,1):
                rep=old.extension(V,amplitude*c)
                E=t.m.Global(rep,state)
                for R in (E.P,E.Q):
                    assert zero(R-s.diag(R[:4,:4],s.ones(1)))
                    assert t.m.dm(R[:4,:4]).det()==t.m.FIELD.one
                    assert zero(mul(R,eps)-eps) and zero(mul(inverse(R).T,eps)-eps)
                peripherals.append((E.P,E.Q))
                VB=boundary(E.P[:4,:4],E.Q[:4,:4])
                P,Q=old.exterior(E.P),old.exterior(E.Q)
                F,Fd=boundary(P,Q),boundary(inverse(P).T,inverse(Q).T)
                maps=map_data(F,Fd,J,Jd)
                dimensions=original['amplitudes'][str(amplitude)]['dimensions']
                for name,B in (('F',F),('F*',Fd)):
                    assert [dimensions[name]['H0'],dimensions[name]['H1']]==B.betti[:2]
                l,ld=dimensions['F']['L'],dimensions['F*']['L']
                assert l+ld==F.H.cols
                frep={k:old.exterior(R) for k,R in rep.items()}
                h0=[]
                for r in (frep,t.m.dual(frep)):
                    h0.append(10-rank(s.Matrix.vstack(*(r[k]-s.eye(10) for k in t.m.GEN))))
                assert h0==[0,0]
                backward_bound=max(0,ld-maps['reverse_kernel']-l)
                forward_bound=max(0,l-maps['kernel']-ld)
                acyclic=VB.betti==[0,0,0]
                if acyclic:
                    assert maps['rank']==maps['reverse_rank']==F.H.cols==Fd.H.cols
                    assert maps['composition_defect']==maps['dual_composition_defect']==0
                amps[str(amplitude)]={'V_betti':VB.betti,'F_betti':F.betti,
                    'Fdual_betti':Fd.betti,'maps':maps,'chosen_L_dimensions':[l,ld],
                    'global_F_H0':h0,'forward_escape_lower_bound':forward_bound,
                    'reverse_escape_lower_bound':backward_bound,
                    'both_inverse_on_H1':acyclic,
                    'conditional_equal_dimension':F.H.cols//2 if acyclic else None,
                    'conditional_paired_H1_difference':F.H.cols//2-F.betti[0]+h0[0]-h0[1] if acyclic else None}
            assert all(zero(a-b) for a,b in zip(peripherals[0],peripherals[1]))
            row={'carrier':state['SnapPy'],'signed_word':label,'character':char,'amplitudes':amps}
            print(json.dumps({'member':row},sort_keys=True),flush=True)
            output.append(row)
    return output


if __name__=='__main__':
    print(json.dumps({'controls':controls()},sort_keys=True),flush=True)
    rows=actual_members()
    print(json.dumps({'status':'PASS','members':len(rows),
                     'scope':'necessary dimension condition for specified tensor trace algebra'}),flush=True)
