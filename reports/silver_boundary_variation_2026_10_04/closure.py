"""Post-native zero-degree closure check, not a full gauge algebra."""
import hashlib
import importlib.util
import json
from functools import lru_cache
from pathlib import Path

import sympy as s

HERE=Path(__file__).resolve().parent
for name,digest in {
    'verify.py':'1c4d540f0108016d4d91aac4b7a49f9b376bb6209c8a66d76b4952d8a2c43859',
    'NATIVE_FIRST.jsonl':'7707379c4796577ccc397cb01c76e79385c232152f5fb4ed9e22cf74688aee3c'
}.items():
    assert hashlib.sha256((HERE/name).read_bytes()).hexdigest()==digest,name
spec=importlib.util.spec_from_file_location('silver_zero_closure_base',HERE/'verify.py')
m=importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
t=m.t


def products(spaces):
    out={}
    for a,b,h,T in t.channels():
        A,B=spaces[a],spaces[b]
        C=t.columns([t.apply(T,A[:,i],B[:,j]) for i in range(A.cols) for j in range(B.cols)],T.rows)
        out[a+' x '+b+' -> '+h]=t.quotient(C,spaces[h])
    return out


@lru_cache(None)
def controls():
    spaces={k:s.eye(5 if k.startswith('E') else 10) for k in ('E','E*','F','F*')}
    assert all(r['rank']==0 for r in products(spaces).values())
    spaces={k:s.zeros(5 if k.startswith('E') else 10,0) for k in spaces}
    spaces['E']=s.eye(5)[:,4]
    spaces['F']=s.eye(10)[:,0]
    assert products(spaces)['E x F -> F*']['rank']==1
    return {'status':'PASS','full_invariant_positive':True,'restricted_opposite_rank':1}


@lru_cache(None)
def actual_members():
    old,data,records=t.m.inputs()
    native=[json.loads(l)['member'] for l in (HERE/'NATIVE_FIRST.jsonl').read_text().splitlines() if 'member' in json.loads(l)]
    out=[]
    for row in native:
        label,char=row['signed_word'],row['character']
        state=data['states'][label]
        saved=next(r for r in records if r['signed_word']==label and r['character']==char)
        c=s.Matrix([s.sympify(x) for x in saved['peripherally_zero_cocycle']])
        f=old.four(state)
        V={k:char[k]*f[k] for k in t.m.GEN}
        amps={}
        for amplitude in (0,1):
            E=t.m.Global(old.extension(V,amplitude*c),state)
            P,Q=old.exterior(E.P),old.exterior(E.Q)
            per={'E':(E.P,E.Q),'E*':(t.inverse(E.P).T,t.inverse(E.Q).T),
                 'F':(P,Q),'F*':(t.inverse(P).T,t.inverse(Q).T)}
            spaces={}
            for name,(p,q) in per.items():
                D=(p-s.eye(p.rows)).col_join(q-s.eye(q.rows))
                H=t.kernel(D)
                rec=row['amplitudes'][str(amplitude)]['parameters'][name]
                raw=rec['kernel_coordinates']
                K=s.Matrix(len(raw),rec['surviving'],lambda i,j:s.sympify(raw[i][j]))
                assert H.cols==rec['full_H0']==K.rows
                spaces[name]=t.mul(H,K)
                assert t.rank(spaces[name])==rec['surviving']
                assert t.zero(t.mul(D,spaces[name]))
            amps[str(amplitude)]=products(spaces)
        result={'carrier':row['carrier'],'character':char,'amplitudes':amps}
        print(json.dumps({'member':result},sort_keys=True),flush=True)
        out.append(result)
    assert len(out)==4
    return out


if __name__=='__main__':
    print(json.dumps({'controls':controls()},sort_keys=True),flush=True)
    rows=actual_members()
    print(json.dumps({'status':'PASS','members':len(rows),'scope':'six charged zero-degree products only'}),flush=True)
