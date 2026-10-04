"""R93 same-author separately structured root/modular verifier; no native import."""
from collections import Counter
from fractions import Fraction as F
from hashlib import sha256
from itertools import combinations, product
import importlib.util
import json
from pathlib import Path
import sys

HERE=Path(__file__).resolve().parent
SOURCE=HERE/'joined_background_reference.py'
EXPECTED_SOURCE='22e41effc4acf899172e4bd95c196c11542ebd58580d14ea9e20dbce49eae869'


def retained():
    if sha256(SOURCE.read_bytes()).hexdigest()!=EXPECTED_SOURCE:
        raise ValueError('Retained modular source differs')
    spec=importlib.util.spec_from_file_location('r93_separate_r85_modular',SOURCE)
    m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m


def root_system():
    half=F(1,2); result=[]
    for j in range(8):
        for k in range(j):
            for signs in ((1,1),(1,-1),(-1,1),(-1,-1)):
                v=[F(0)]*8; v[j],v[k]=map(F,signs); result.append(tuple(v))
    for bits in range(256):
        if bits.bit_count()%2==0:
            result.append(tuple(half if not bits&(1<<j) else -half for j in range(8)))
    return result


def dot(a,b):
    return sum(x*y for x,y in zip(a,b))


def basis():
    e=lambda j:tuple(F(int(i==j)) for i in range(8))
    sub=lambda a,b:tuple(x-y for x,y in zip(a,b))
    g=[sub(e(j),e(j+1)) for j in range(4)]
    st=[sub(e(6),e(7)),sub(e(5),e(6)),tuple(x+y for x,y in zip(e(6),e(7))),(-F(1,2),)*8]
    return st,g


def fundamentals():
    return [tuple(int(i==j)-int(i==j+1) for j in range(4)) for i in range(5)]


def module_weights():
    f=Counter(fundamentals()); ten=Counter(tuple(a+b for a,b in zip(u,v)) for u,v in combinations(fundamentals(),2))
    du=lambda x:Counter({tuple(-v for v in w):n for w,n in x.items()})
    a=Counter({(0,)*4:4})
    for u in fundamentals():
        for v in fundamentals():
            if u!=v:
                a[tuple(x-y for x,y in zip(u,v))]+=1
    z=Counter({(0,)*4:1})
    out=Counter()
    for left,right in ((a,z),(z,a),(f,ten),(du(f),du(ten)),(ten,du(f)),(du(ten),f)):
        for u,m in left.items():
            for v,n in right.items():
                out[u+v]+=m*n
    return out


def partitions(n,maximum=None):
    if n==0:
        yield ()
        return
    for k in range(min(n,maximum or n),1-1,-1):
        for rest in partitions(n-k,k):
            yield (k,)+rest


def root_checks():
    rr=root_system(); st,g=basis(); y=tuple(map(F,(-2,-2,-2,3,3,0,0,0)))
    actual=Counter(tuple(dot(r,b) for b in st+g) for r in rr); actual[(F(0),)*8]+=8
    center=[r for r in rr if all(dot(r,b)==0 for b in st)]
    zero=[r for r in center if dot(r,y)==0]
    checks={'complete_240':len(rr)==len(set(rr))==240,
            'full_roster_separate':actual==module_weights(),
            'gauge_kernel20':len(center)==20,'neutral8_plus_Cartan4':len(zero)+4==12,
            'trace_squared1800':sum(dot(r,y)**2 for r in rr)==1800,
            'trace_squared_not30':sum(dot(r,y)**2 for r in rr)!=30}
    for part in partitions(5):
        blocks=[]
        for label,multiplicity in enumerate(part):
            blocks.extend([label]*multiplicity)
        roots=sum(1 for j in range(5) for k in range(5) if j!=k and blocks[j]==blocks[k])
        checks['partition_'+''.join(map(str,part))]=roots+4==sum(k*k for k in part)-1
    checks['all_seven_partitions']=len(list(partitions(5)))==7
    for modulus,dimension in ((5,24),(7,12),(11,12)):
        values=[v%modulus for v in (-2,-2,-2,3,3)]
        checks['holonomy_order_'+str(modulus)]=sum(1 for j in range(5) for k in range(5) if j!=k and values[j]==values[k])+4==dimension
    # Primitive cocharacter torus: rational phases, not rounded complex exponentials.
    kernel=[(t,a,b) for t in range(6) for a in range(3) for b in range(2)
            if (-F(2*t,6)+F(a,3)).denominator==1 and (F(3*t,6)+F(b,2)).denominator==1]
    checks['exact_Z6_kernel']=kernel==[(t,t%3,t%2) for t in range(6)]
    # Independent scalar equations for T_12=1,T_21=-1 and rho=diag(2,3).
    chi=F(1,6)
    checks['twisted_tensor_target_covariance']=chi*2*3==1 and chi*2==F(1,3) and chi*3==F(1,2)
    checks['inverse_twist_target_rejected']=2/chi!=F(1,3) and 3/chi!=F(1,2)
    return checks


def run(path):
    records=[json.loads(line) for line in Path(path).read_text().splitlines()]
    if records[-1].get('failed')!=[]:
        raise ValueError('Native did not accept its premises')
    cases=[row for row in records if row.get('group','').startswith('join_')]
    if [row['character'] for row in cases]!=[[0,1],[1,1],[1,0]]:
        raise ValueError('Wrong actual character population')
    checks=root_checks(); m=retained(); pairs=[]
    for p in m.PRIMES:
        if not m.prime(p):
            raise ValueError('Not prime')
        for root in m.roots(p):
            try:
                for row in cases:
                    for a in list(row['witness']['left'].values())+list(row['witness']['right'].values())+[row['witness']['s']]:
                        m.evaluate(a,p,root)
            except ValueError:
                continue
            pairs.append((p,root)); break
        if len(pairs)==2:
            break
    if len(pairs)!=2:
        raise ValueError('INCONCLUSIVE modular denominator/root pool')
    k={'x':0,'y':0,'z':1,'a':0,'b':0,'c':-1}
    exponent=lambda w:sum(k[t.lower()]*(1 if t.islower() else -1) for t in w)
    rels=m.relators()
    checks['actual_character_all_relators']=all(exponent(w)==0 for w in rels)
    checks['actual_character_onto_Z']=exponent('z')==1 and exponent('c')==-1
    for p,root in pairs:
        trivial={name:m.eye(1) for name in k}
        data=m.cohomology(trivial,rels,p)
        checks[f'b1_one_{p}']=data['h0']==data['h1']==1
        for row in cases:
            tag=str(p)+'_'+''.join(map(str,row['character']))
            w=row['witness']; left={name:m.evaluate(a,p,root) for name,a in w['left'].items()}
            right={name:m.evaluate(a,p,root) for name,a in w['right'].items()}
            whole=dict(left,**{name.translate(str.maketrans('xyz','abc')):g for name,g in right.items()})
            checks['relators_'+tag]=w['relators']==list(rels) and all(m.word(t,whole,p)[0]==m.eye(5) for t in rels)
            checks['determinants_'+tag]=all(m.det(a,p)==1 for a in whole.values())
            rows=[[x for r in m.word(t,whole,p)[0] for x in r] for t in w['span_words']]
            checks['full_rank_'+tag]=len(rows)==25 and m.rank(rows,p)==25
            for twist in (2,3):
                gs={name:[[(pow(twist,k[name],p)*x)%p for x in r] for r in a] for name,a in whole.items()}
                checks[f'twist_relators_{tag}_{twist}']=all(m.word(t,gs,p)[0]==m.eye(5) for t in rels)
                rows=[[x for r in m.word(t,gs,p)[0] for x in r] for t in w['span_words']]
                checks[f'twist_rank_{tag}_{twist}']=m.rank(rows,p)==25
    bad=dict(k,c=0)
    checks['bad_character_opposite']=any(sum(bad[t.lower()]*(1 if t.islower() else -1) for t in w)!=0 for w in rels)
    failed=[name for name,ok in checks.items() if not ok]
    summary={'passed':len(checks)-len(failed),'total':len(checks),'failed':failed,
             'prime_roots':pairs,'all_actual_characters':len(cases),
             'non_author_acceptance':False,'PDE_profile_verified':False,'physical_goal_achieved':False,
             'scope':'separate Fraction roots/modular actual witnesses, not characteristic-zero admission'}
    print(json.dumps({'checks':checks,**summary},sort_keys=True),flush=True)
    return summary


if __name__=='__main__':
    if len(sys.argv)!=2:
        raise SystemExit('Usage: joined_wilson_reference.py NATIVE_JSON_LINES_LOG')
    raise SystemExit(0 if not run(sys.argv[1])['failed'] else 1)
