"""Full finite boundary complexes, not analytic or physical domains."""
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
spec=importlib.util.spec_from_file_location('silver_complement_base',HERE.parent/'silver_global_boundary_2026_10_04/verify.py')
g=importlib.util.module_from_spec(spec)
spec.loader.exec_module(g)
m=g.m
red,mul,rank,kernel,zero,inverse=g.red,g.mul,g.rank,g.kernel,g.zero,g.inverse


def fiber(C,T,f,A):
    """Cone(C plus closed A -> T)[-1], with no dropped end degrees."""
    B,F=C
    D,G=T
    f0,f1,f2=f
    A0,A1,A2=A
    n0,n1,n2=B.cols,B.rows,F.rows
    t0,t1,t2=D.cols,D.rows,G.rows
    a0,a1,a2=[x.cols for x in A]
    assert F.cols==n1 and G.cols==t1
    assert [x.shape for x in f]==[(t0,n0),(t1,n1),(t2,n2)]
    assert [x.rows for x in A]==[t0,t1,t2]
    assert all(rank(x)==x.cols for x in A)
    assert zero(mul(F,B)) and zero(mul(G,D)), 'not a complex'
    assert zero(mul(f1,B)-mul(D,f0)), 'not a chain map in degree zero'
    assert zero(mul(f2,F)-mul(G,f1)), 'not a chain map in degree one'
    assert zero(mul(D,A0)) and zero(mul(G,A1)), 'A not closed'
    dims=[n0+a0,n1+a1+t0,n2+a2+t1,t2]
    d0=s.zeros(dims[1],dims[0])
    d0[:n1,:n0]=B
    d0[n1+a1:,:n0]=f0
    d0[n1+a1:,n0:]=-A0
    d1=s.zeros(dims[2],dims[1])
    d1[:n2,:n1]=F
    d1[n2+a2:,:n1]=f1
    d1[n2+a2:,n1:n1+a1]=-A1
    d1[n2+a2:,n1+a1:]=-D
    d2=s.zeros(dims[3],dims[2])
    d2[:,:n2]=f2
    d2[:,n2:n2+a2]=-A2
    d2[:,n2+a2:]=-G
    assert zero(mul(d1,d0)) and zero(mul(d2,d1))
    ranks=[rank(x) for x in (d0,d1,d2)]
    h=[dims[j]-([0]+ranks)[j]-(ranks+[0])[j] for j in range(4)]
    assert min(h)>=0
    chi=sum((-1)**j*x for j,x in enumerate(h))
    assert chi==sum((-1)**j*x for j,x in enumerate(dims))
    return {'cochain_dimensions':dims,'differential_ranks':ranks,
            'H':h,'odd_minus_even':-chi,'chain_identities':True}


def restriction2(E,state):
    assert state['cusp words'][0]=='abAB'
    assert state['cusp words'][1] in ('t','abt')
    n=E.n
    fp=E.fox('abAB')[:,:2*n]
    Ti=inverse(E.rep['t'])
    out=-mul(mul(E.Q,fp),s.diag(Ti,Ti))
    Ft=(s.eye(n)-E.Q).row_join(E.P-s.eye(n))
    assert zero(mul(out,E.F)-mul(Ft,E.R)), 'restriction2 chain identity'
    return out,Ft


def completed(E,L,state):
    R2,Ft=restriction2(E,state)
    H0=kernel(E.D)
    H2=kernel(Ft.conjugate().T)
    r2=rank(Ft.row_join(R2))-rank(Ft)
    patterns={'cone':(H0,L,s.zeros(E.n,0)),
              'reversed':(s.zeros(E.n,0),L,H2)}
    results={name:fiber((E.B,E.F),(E.D,Ft),(s.eye(E.n),E.R,R2),A)
             for name,A in patterns.items()}
    bad_sign_detected=not zero(mul(-R2,E.F)-mul(Ft,E.R))
    return {'models':results,'boundary_H2':H2.cols,'restriction2_rank':r2,
            'wrong_R2_sign_detected':bad_sign_detected}


def pair(result,state,L=None):
    E,D,BE,BD=result['E'],result['D'],result['BE'],result['BD']
    L=BE.L if L is None else L
    J=g.group_cup(E)
    LD=mul(BD.H,kernel(mul(mul(L.T,J),BD.H)))
    assert rank(BE.R.row_join(L))==BE.H.cols
    assert rank(BD.R.row_join(LD))==BD.H.cols
    left,right=completed(E,L,state),completed(D,LD,state)
    assert left['boundary_H2']==D.t0 and right['boundary_H2']==E.t0
    assert left['restriction2_rank']==D.t0-D.h0
    assert right['restriction2_rank']==E.t0-E.h0
    for U,V,row in ((E,D,left),(D,E,right)):
        cone=row['models']['cone']
        rev=row['models']['reversed']
        assert cone['H']==[U.h0,U.interior,V.interior,V.h0]
        assert rev['H']==[0,U.interior+U.t0-U.h0,U.h1-U.h0,0]
        assert cone['odd_minus_even']==rev['odd_minus_even']
    for name in ('cone','reversed'):
        assert left['models'][name]['H']==right['models'][name]['H'][::-1]
    differences={name:left['models'][name]['H'][1]-right['models'][name]['H'][1]
                 for name in ('cone','reversed')}
    return {'E':left,'dual':right,'H1_differences':differences,
            'interior_H1':[E.interior,D.interior],
            'global_H0':[E.h0,D.h0],'boundary_H0':[E.t0,D.t0],
            'complement_dimensions':[L.cols,LD.cols]}


@lru_cache(None)
def controls():
    z=s.zeros(0)
    C=(s.zeros(0,0),z)
    T=(s.zeros(0,1),z)
    f=(s.zeros(1,0),z,z)
    unmatched=fiber(C,T,f,(s.zeros(1,0),z,z))
    attached=fiber(C,T,f,(s.eye(1),z,z))
    global_removed=fiber((s.zeros(0,1),z),T,(s.eye(1),z,z),(s.zeros(1,0),z,z))
    assert unmatched['H']==[0,1,0,0]
    assert attached['H']==global_removed['H']==[0,0,0,0]
    # With no boundary, recover the source two-term complex.
    ordinary=fiber((s.Matrix([[1,0]]),s.zeros(0,1)),(z,z),
                   (s.zeros(0,2),s.zeros(0,1),z),(z,z,z))
    assert ordinary['H']==[1,0,0,0]
    rejected=False
    try:
        fiber((s.eye(1),s.zeros(0,1)),(s.eye(1),s.zeros(0,1)),
              (s.eye(1),2*s.eye(1),z),(s.zeros(1,0),s.zeros(1,0),z))
    except AssertionError as error:
        rejected='not a chain map' in str(error)
    assert rejected
    return {'status':'PASS','unmatched_boundary_H0':unmatched['H'],
            'attached_A0':attached['H'],'global_H0_cancels':global_removed['H'],
            'empty_boundary_recovers_source':ordinary['H'],
            'broken_chain_map_rejected':rejected}


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
            c=s.Matrix([s.sympify(x) for x in saved['peripherally_zero_cocycle']])
            V={k:char[k]*f[k] for k in m.GEN}
            print(json.dumps({'progress':'starting','carrier':state['SnapPy'],'character':char}),flush=True)
            amplitudes={}
            tilt=None
            for amplitude in (0,1):
                rep=old.extension(V,amplitude*c)
                reps={'W':rep,'wedge2W':{k:old.exterior(A) for k,A in rep.items()}}
                rows={}
                for sector,representation in reps.items():
                    key=('split'+sector if sector=='W' else 'split_wedge2W') if amplitude==0 else sector
                    base=g.analyze(representation,state,saved[key])
                    rows[sector]=pair(base,state)
                    if not output and amplitude==1:
                        BE=base['BE']
                        X=s.zeros(BE.R.cols,BE.L.cols)
                        for j in range(min(X.shape)):
                            X[j,j]=1
                        tilted=pair(base,state,red(BE.L+mul(BE.R,X)))
                        assert tilted==rows[sector]
                        tilt={} if tilt is None else tilt
                        tilt[sector]=True
                assert [rows[k]['H1_differences']['cone'] for k in reps]==([0,0] if amplitude==0 else [-1,-1])
                assert [rows[k]['H1_differences']['reversed'] for k in reps]==([0,0] if amplitude==0 else [0,-1])
                assert [rows[k]['E']['models']['cone']['odd_minus_even'] for k in reps]==([0,0] if amplitude==0 else [0,-1])
                amplitudes[str(amplitude)]=rows
            record={'carrier':state['SnapPy'],'signed_word':label,'character':char,
                    'amplitudes':amplitudes,'tilted_complement_control':tilt}
            output.append(record)
            print(json.dumps({'member':record},sort_keys=True),flush=True)
    assert any(r['E']['wrong_R2_sign_detected'] for row in output
               for a in row['amplitudes'].values() for r in a.values())
    return output


if __name__=='__main__':
    print(json.dumps({'controls':controls()},sort_keys=True),flush=True)
    rows=actual_members()
    print(json.dumps({'status':'PASS','members':len(rows),
                     'scope':'two finite cochain completions, no physical domain identified'}),flush=True)
