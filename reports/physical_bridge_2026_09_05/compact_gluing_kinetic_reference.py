"""Separate modular/rational witness checks, not a harmonic-metric PDE proof."""
from hashlib import sha256
import importlib.util
import json
from pathlib import Path
import sys

SOURCE=Path(__file__).with_name('parent_gluing_character_reference.py')
if sha256(SOURCE.read_bytes()).hexdigest()!='f7608983681f6ba96ff2d985de0406e442615f8ca526c134c7e821b082d61ba9':
    raise RuntimeError('Changed modular source')
spec=importlib.util.spec_from_file_location('r88_modular_parent',SOURCE)
R=importlib.util.module_from_spec(spec); spec.loader.exec_module(R); M=R.M

def trace(a,p):
    return sum(a[i][i] for i in range(len(a)))%p

def comm(a,b,p):
    return M.add(M.mul(a,b,p),M.mul(b,a,p),p,-1)

def tangent_word(w,gens,coc,p):
    h=M.eye(5); v=R.zero(5)
    for letter in w:
        g=gens[letter.lower()]; u=coc[letter.lower()]
        if letter.isupper():
            g=M.inv(g,p); u=R.scalar(M.mul(M.mul(g,u,p),gens[letter.lower()],p),-1,p)
        v=M.add(v,M.mul(M.mul(h,u,p),M.inv(h,p),p),p); h=M.mul(h,g,p)
    return h,v

def derivative(g,dg,p):
    h=M.inv(g,p); dh=R.scalar(M.mul(M.mul(h,dg,p),h,p),-1,p)
    a,b,da,db=[trace(v,p) for v in (g,h,dg,dh)]
    return (da*b+a*db+10*(da+db)+5*(a*da-trace(M.mul(g,dg,p),p)+b*db-trace(M.mul(h,dh,p),p)))%p

def root_trace():
    weights=R.roots_and_roster()[2]
    ds=[tuple(int(k==i)-int(k==4) for k in range(5)) for i in range(4)]
    ev=lambda w,d:sum(w[j+4]*sum(d[:j+1]) for j in range(4))
    gram=[[sum(n*ev(w,a)*ev(w,b) for w,n in weights.items()) for b in ds] for a in ds]
    return {'checks':{'independent_full_cartan_gram':gram==[[60*(1+int(i==j)) for j in range(4)] for i in range(4)],
                      'wrong_factor_rejected':gram[0][0]!=30*2},'gram':gram}

def verify(rec,p,r):
    w=rec['witness']; left={t:M.evaluate(a,p,r) for t,a in w['left'].items()}; right={t:M.evaluate(a,p,r) for t,a in w['right'].items()}
    names=str.maketrans('xyz','abc'); whole=dict(left,**{t.translate(names):a for t,a in right.items()})
    z=[[1 if i==j and i<4 else -4%p if i==j else 0 for j in range(5)] for i in range(5)]
    coc={t:R.zero(5) for t in left}; coc.update({t.translate(names):M.add(z,M.mul(M.mul(g,z,p),M.inv(g,p),p),p,-1) for t,g in right.items()})
    g=M.mul(left['x'],right['x'],p); dg=M.mul(left['x'],comm(z,right['x'],p),p)
    columns=[]
    for i in range(5):
        for j in range(5):
            e=R.unit(5,i,j)
            columns.append([v for a in whole.values() for row in M.add(M.mul(M.mul(a,e,p),M.inv(a,p),p),e,p,-1) for v in row])
    cb=[list(row) for row in zip(*columns)]; bend=[v for t in whole for row in coc[t] for v in row]
    aug=[row+[v] for row,v in zip(cb,bend)]; val=derivative(g,dg,p)
    basis=[[v for row in M.word(word,whole,p)[0] for v in row] for word in w['span_words']]
    checks={'prime_and_root':M.prime(p) and (r**6-34*r**3+1)%p==0,
            'literal_cocycle_export':all(M.evaluate(w['cocycle'][t],p,r)==coc[t] for t in whole),
            'actual_relators_and_tangents':all(tangent_word(word,whole,coc,p)==(M.eye(5),R.zero(5)) for word in M.relators()),
            'full_actual_matrix_algebra':len(basis)==25 and M.rank(basis,p)==25,
            'coboundary_rank24':M.rank(cb,p)==24,'bend_adds_one':M.rank(aug,p)==25,
            'actual_loop_and_velocity':g==M.evaluate(w['g'],p,r) and dg==M.evaluate(w['dg'],p,r),
            'exported_parent_derivative':val==M.evaluate(rec['parent_log_derivative'],p,r)[0][0],
            'parent_velocity_nonzero_modular':val!=0,
            'simultaneous_conjugation_zero':derivative(g,comm(z,g,p),p)==0}
    return {'prime':p,'root':r,'character':rec['character'],'checks':checks}

def controls():
    p=1031; a=M.eye(2); b=[[0,1],[1,0]]
    return {'checks':{'scalar_commutator_zero':comm(a,b,p)==[[0,0],[0,0]],
                      'singular_inverse_rejected':M.rank([[1,0],[0,0]],p)==1,
                      'rectangular_full_column_rank_control':M.rank([[1,0],[0,1],[1,1]],p)==2,
                      'nonzero_rank_control':M.rank([[0,0],[0,0]],p)==0}}

def run(path):
    rows=[json.loads(l) for l in Path(path).read_text().splitlines()]
    if not rows[-1].get('all'):
        raise ValueError('Native capture failed')
    cases=[r for r in rows if r.get('group')=='case']
    if [r['character'] for r in cases]!=[[0,1],[1,1],[1,0]]:
        raise ValueError('Wrong population')
    out=[]
    def emit(name,data):
        out.append(data); print(json.dumps({'group':name,**data},sort_keys=True),flush=True)
    emit('controls',controls()); emit('parent_trace',root_trace())
    for p,r in R.PRIME_ROOTS:
        for rec in cases:
            emit('case',verify(rec,p,r))
    cs=[v for d in out for v in d['checks'].values()]
    result={'all':all(cs),'passed':sum(cs),'total':len(cs),'scope':'same-author separate root/modular witness checks, not exact K or analytic PDE certification'}
    print(json.dumps(result,sort_keys=True),flush=True); return result

if __name__=='__main__':
    if len(sys.argv)!=2:
        raise SystemExit('Usage: compact_gluing_kinetic_reference.py NATIVE_LOG')
    raise SystemExit(0 if run(sys.argv[1])['all'] else 1)
