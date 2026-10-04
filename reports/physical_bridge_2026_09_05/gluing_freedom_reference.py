"""R86 same-author separate modular witness check; no native or SymPy import."""
from hashlib import sha256
import importlib.util
import json
from pathlib import Path
import sys

HERE=Path(__file__).resolve().parent
SOURCE=HERE/'joined_background_reference.py'
PIN='22e41effc4acf899172e4bd95c196c11542ebd58580d14ea9e20dbce49eae869'
if sha256(SOURCE.read_bytes()).hexdigest()!=PIN:
    raise RuntimeError('Changed R85 modular library')
spec=importlib.util.spec_from_file_location('r86_retained_modular',SOURCE)
M=importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
PRIME_ROOTS=((1031,695),(1033,162))


def flat(a):
    return [z for row in a for z in row]


def zero(n):
    return [[0]*n for _ in range(n)]


def unit(n,i,j):
    a=zero(n); a[i][j]=1
    return a


def trace(a,p):
    return sum(a[i][i] for i in range(len(a)))%p


def conjugate(g,z,p):
    return M.mul(M.mul(g,z,p),M.inv(g,p),p)


def commutant(gens,p,traceless=False):
    n=len(next(iter(gens.values()))); cols=[]
    for i in range(n):
        for j in range(n):
            e=unit(n,i,j)
            col=[z for g in gens.values() for z in flat(M.add(M.mul(g,e,p),M.mul(e,g,p),p,-1))]
            if traceless:
                col.append(trace(e,p))
            cols.append(col)
    a=[list(r) for r in zip(*cols)]
    return n*n-M.rank(a,p)


def tangent_word(w,gs,c,p):
    n=len(next(iter(gs.values()))); pref=M.eye(n); u=zero(n)
    for ch in w:
        g=gs[ch.lower()]; v=c[ch.lower()]
        if ch.isupper():
            g=M.inv(g,p); v=[[-z%p for z in row] for row in conjugate(g,v,p)]
        u=M.add(u,conjugate(pref,v,p),p); pref=M.mul(pref,g,p)
    return pref,u


def columns(cs,names):
    return [list(r) for r in zip(*[[z for t in names for z in flat(c[t])] for c in cs])]


def scale(t,p):
    return [[t%p if i==j and i<4 else pow(t,-4,p) if i==j else 0 for j in range(5)] for i in range(5)]


def verify(rec,p,r):
    w=rec['witness']; left={t:M.evaluate(a,p,r) for t,a in w['left'].items()}
    right={t:M.evaluate(a,p,r) for t,a in w['right'].items()}
    gs=dict(left,**{t.translate(str.maketrans('xyz','abc')):a for t,a in right.items()})
    names=list(gs); z=M.evaluate(w['s'],p,r)
    per={'z':left['z'],'l':M.word('yXYx',left,p)[0]}
    zs=[M.evaluate(a,p,r) for a in w['z_basis']]; cs=[]
    for a in zs:
        one={t:zero(5) for t in left}
        one.update({t.translate(str.maketrans('xyz','abc')):M.add(a,conjugate(g,a,p),p,-1) for t,g in right.items()})
        cs.append(one)
    q=columns(cs,names)
    cb=[{t:M.add(conjugate(g,unit(5,i,j),p),unit(5,i,j),p,-1) for t,g in gs.items()}
        for i in range(5) for j in range(5)]
    b=columns(cb,names); rb=M.rank(b,p); rq=M.rank(q,p); joined=M.rank([x+y for x,y in zip(b,q)],p)
    d=scale(2,p); changed=dict(left,**{t.translate(str.maketrans('xyz','abc')):conjugate(d,g,p) for t,g in right.items()})
    rows=lambda words,vs:[flat(M.word(u,vs,p)[0]) for u in words]
    tw=rec['trace_witness']; a=M.word(tw['left_word'],left,p)[0]; v=M.word(tw['right_word'],right,p)[0]
    coeff=M.evaluate(tw['coefficient'],p,r)[0][0]; const=M.evaluate(tw['constant'],p,r)[0][0]
    localcoeff=sum(a[i][4]*v[4][i] for i in range(4))%p
    tvals={str(t):trace(M.mul(a,conjugate(scale(t,p),v,p),p),p) for t in (1,2,3)}
    checks={'prime_root':M.prime(p) and (r**6-34*r**3+1)%p==0,
            'matching_block_diagonal':not any(z[i][4] or z[4][i] for i in range(4)),
            'left_upper_shape':not any(g[4][i] for g in left.values() for i in range(4)),
            'right_lower_shape':not any(g[i][4] for g in right.values() for i in range(4)),
            'left_word_rank21':len(w['left_words'])==21 and M.rank(rows(w['left_words'],left),p)==21,
            'right_word_rank21':len(w['right_words'])==21 and M.rank(rows(w['right_words'],right),p)==21,
            'piece_commutants_one':commutant(left,p)==commutant(right,p)==1,
            'centralizer5_traceless4':commutant(per,p)==5 and commutant(per,p,True)==4,
            'z_basis_independent4':len(zs)==4 and M.rank([flat(a) for a in zs],p)==4,
            'z_basis_trace_and_seam':all(trace(a,p)==0 and all(M.mul(a,g,p)==M.mul(g,a,p) for g in per.values()) for a in zs),
            'tangent_relators':all(tangent_word(u,gs,c,p)[1]==zero(5) for c in cs for u in M.relators()),
            'tangent_trace_zero':all(trace(a,p)==0 for c in cs for a in c.values()),
            'quotient_ranks24_4_28':rb==24 and rq==4 and joined==28,
            'scale_unit_determinant':M.det(d,p)==1,
            'scale_peripheral_commutation':all(M.mul(d,g,p)==M.mul(g,d,p) for g in per.values()),
            'changed_relators':all(M.word(u,changed,p)[0]==M.eye(5) for u in M.relators()),
            'changed_joint_word_rank25':len(w['changed_joint_words'])==25 and M.rank(rows(w['changed_joint_words'],changed),p)==25,
            'actual_trace_coefficient_nonzero':coeff==localcoeff!=0,
            'actual_trace_constant':const==(trace(M.mul(a,v,p),p)-coeff)%p,
            'trace_formula_all_declared_values':all(x==(const+coeff*pow(int(t),-5,p))%p for t,x in tvals.items()),
            'exported_trace_values':all(x==M.evaluate(tw['values'][t],p,r)[0][0] for t,x in tvals.items()),
            'trace_separates1_2':tvals['1']!=tvals['2']}
    return {'character':rec['character'],'prime':p,'root':r,'checks':checks,'coboundary_rank':rb,'joined_rank':joined}


def controls():
    p=1031; a=[[1,1],[0,1]]; b=[[1,0],[1,1]]; d=[[2,0],[0,1]]
    seam=[[2,0],[0,3]]; bad=unit(2,0,1); i=M.eye(2); h=[[1,0],[0,p-1]]
    checks={'singular_rank_rejected':M.rank([[1,2],[2,4]],p)==1,
            'relative_trace_positive':trace(M.mul(a,b,p),p)!=trace(M.mul(a,conjugate(d,b,p),p),p),
            'scalar_tangent_zero':M.add(i,conjugate(b,i,p),p,-1)==zero(2),
            'noncentral_seam_rejected':M.mul(seam,bad,p)!=M.mul(bad,seam,p),
            'traceless_seam_positive':M.mul(seam,h,p)==M.mul(h,seam,p) and trace(h,p)==0,
            'trivial_circle_positive':M.cohomology({'x':[[1]]},('',),p)['h1']==1,
            'trivial_point_opposite':M.cohomology({'x':[[1]]},('x',),p)['h1']==0}
    return {'checks':checks}


def run(path):
    records=[json.loads(x) for x in Path(path).read_text().splitlines()]
    if not records[-1].get('all'):
        raise ValueError('Native capture did not pass')
    cases=[x for x in records if x.get('group')=='case']
    if [x['character'] for x in cases]!=[[0,1],[1,1],[1,0]]:
        raise ValueError('Wrong character population')
    groups=[controls()]; print(json.dumps({'group':'controls',**groups[0]},sort_keys=True),flush=True)
    for p,r in PRIME_ROOTS:
        for rec in cases:
            out=verify(rec,p,r); groups.append(out)
            print(json.dumps({'group':'witness',**out},sort_keys=True),flush=True)
        out=M.cohomology({t:[[1]] for t in 'xyzabc'},M.relators(),p)
        g={'checks':{'trivial_h0_h1':out['h0']==out['h1']==1},'counts':out,'prime':p}
        groups.append(g); print(json.dumps({'group':'trivial',**g},sort_keys=True),flush=True)
    cs=[x for g in groups for x in g['checks'].values()]
    result={'passed':sum(cs),'total':len(cs),'all':all(cs),'scope':'same-author modular witness checks, not second exact or physical certificate'}
    print(json.dumps(result,sort_keys=True),flush=True)
    return result


if __name__=='__main__':
    if len(sys.argv)!=2:
        raise SystemExit('Usage: gluing_freedom_reference.py NATIVE_LOG')
    raise SystemExit(0 if run(sys.argv[1])['all'] else 1)
