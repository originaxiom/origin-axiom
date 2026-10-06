exec(open('cong3.py').read().split("import sys")[0])
import json, sys, warnings; warnings.filterwarnings('ignore')
sys.path.insert(0,__import__('os').path.dirname(__import__('os').path.dirname(__import__('os').path.abspath(__file__))))
import snappy
from common_cover import measure
N=4
H1=closure([red(m004[g],N) for g in m004]+[red(minv(m004[g]),N) for g in m004],N); H1l=list(H1)
def coset_key(x): return min(canon(rmm(h,x,N),N) for h in H1l)
Q=list(closure([red(g,N) for g in Gg],N))
# the 12 cosets
cos={}; 
for x in Q:
    k=coset_key(x)
    if k not in cos: cos[k]=x
keys=list(cos); idx={k:i for i,k in enumerate(keys)}
print('cosets',len(keys))
units=[(1,0),(0,1),(-1,-1)]  # 1, w, w^2 ; with -1 projectively these give all 6
def conjD(X,u):  # diag(1,u) X diag(1,u^-1): b -> b*u^-1, c -> c*u
    uinv={(1,0):(1,0),(0,1):(-1,-1),(-1,-1):(0,1)}[u]
    a,b,c,d=X; return (a,mul(b,uinv),mul(c,u),d)
def bar(X): return tuple(((e[0]-e[1]),(-e[1])) for e in X)  # complex conjugation: w -> w^2 = -1-w : x+yw -> (x-y) - y w
reps={}
for line in open('reps.txt'):
    nm,js=line.split(' ',1); d=json.loads(js)
    reps[nm]={'gens':d['gens'],'rep':{g:tuple(tuple(e) for e in [d['rep'][g][0],d['rep'][g][1],d['rep'][g][2],d['rep'][g][3]]) for g in d['gens']}}
reps['m202_B1302']={'gens':['a','b'],'rep':m202}
results=[]
seen=set()
for nm,R in reps.items():
    base=nm.split('_B')[0]
    for u in units:
        for b in (False,True):
            rep={g:(bar(conjD(R['rep'][g],u)) if b else conjD(R['rep'][g],u)) for g in R['gens']}
            perm={g:[idx[coset_key(canon(rmm(cos[k],red(rep[g],N),N),N))] for k in keys] for g in R['gens']}
            # orbits
            orbits=[]; left=set(range(len(keys)))
            while left:
                s=min(left); orb={s}; fr=[s]
                while fr:
                    x=fr.pop()
                    for g in R['gens']:
                        for y in (perm[g][x], perm[g].index(x)):
                            if y not in orb: orb.add(y); fr.append(y)
                orbits.append(sorted(orb)); left-=orb
            for orb in orbits:
                loc={x:i for i,x in enumerate(orb)}
                p=[[loc[perm[g][x]] for x in orb] for g in R['gens']]
                T=snappy.Manifold(base); C=T.cover(p)
                s=C.isometry_signature()
                key=(base,s)
                if key in seen: continue
                seen.add(key)
                r=measure(C); r.update({'target':base,'rep':nm,'unit':u,'mirror':b,'deg_over_target':len(orb),'deg_over_m004':round(float(C.volume()/snappy.Manifold('m004').volume())),'signature':s})
                print(json.dumps(r),flush=True); results.append(r)
json.dump(results,open('exact_results.json','w'),indent=1)
