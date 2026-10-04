"""R91 separate stdlib reflection/sparse/Fraction/modular reference. Same author."""
from collections import Counter
from fractions import Fraction as F
from itertools import combinations, product
import json


def reflection_roots():
    e=[tuple(2*int(i==j) for j in range(8)) for i in range(8)]
    diff=lambda a,b:tuple(x-y for x,y in zip(a,b))
    simple=[(1,-1,-1,-1,-1,-1,-1,1),tuple(x+y for x,y in zip(e[0],e[1]))]
    simple += [diff(e[j+1],e[j]) for j in range(6)]
    seen=set(simple); pending=list(simple)
    while pending:
        v=pending.pop()
        for a in simple:
            d=sum(x*y for x,y in zip(v,a)); assert d%4==0
            w=tuple(x-d//4*y for x,y in zip(v,a))
            if w not in seen:
                seen.add(w); pending.append(w)
    return seen


def transpose(m):
    return {(j,i):v for (i,j),v in m.items()}


def plus(a,b,scale=1):
    out=dict(a)
    for key,v in b.items():
        out[key]=out.get(key,0)+scale*v
    return {key:v for key,v in out.items() if v}


def times(a,b):
    out={}
    for (i,j),v in a.items():
        for (k,l),w in b.items():
            if j==k:
                out[i,l]=out.get((i,l),0)+v*w
    return {key:v for key,v in out.items() if v}


def comm(a,b):
    return plus(times(a,b),times(b,a),-1)


def closure_mod(seed,p):
    basis={}; matrices=[]
    def insert(m):
        v=[m.get((i,j),0)%p for i,j in product(range(6),repeat=2)]
        for k,row in sorted(basis.items()):
            a=v[k]; v=[(x-a*y)%p for x,y in zip(v,row)]
        k=next((i for i,a in enumerate(v) if a),None)
        if k is None:
            return
        inv=pow(v[k],-1,p); v=[x*inv%p for x in v]; basis[k]=v
        matrices.append({(i,j):v[6*i+j] for i,j in product(range(6),repeat=2) if v[6*i+j]})
    for m in seed:
        insert(m)
    k=0
    while k<len(matrices):
        for m in matrices[:k]:
            insert(comm(matrices[k],m))
        k+=1
    return len(matrices)


def run():
    checks=[]
    def test(name,ok):
        checks.append((name,bool(ok)))
    rr=reflection_roots(); test('reflection_240',len(rr)==240)
    color=((2,-2,0,0,0,0,0,0),(0,2,-2,0,0,0,0,0)); weak=(0,0,0,2,-2,0,0,0)
    y=(-2,-2,-2,3,3,0,0,0); yp=(-2,-2,-2,-3,-3,0,0,0)
    t=(-2,-2,-2,-2,-2,0,0,0); r4=(0,0,0,2,2,0,0,0)
    dot=lambda a,b:sum(x*z for x,z in zip(a,b))
    refl=lambda a:tuple(x-dot(a,r4)//4*z for x,z in zip(a,r4))
    test('explicit_reflector_present',r4 in rr and dot(r4,r4)==8)
    test('explicit_Y_reflection',refl(y)==yp and yp==tuple(-(F(a)-6*b)/5 for a,b in zip(y,t)))
    test('color_weak_fixed',all(refl(a)==a for a in color+(weak,)))
    test('centralizer_roots',sum(all(dot(v,a)==0 for a in color+(weak,)) for v in rr)==30)
    test('ordinary_Y_roots',sum(all(dot(v,a)==0 for a in color+(weak,y)) for v in rr)==20)
    test('transported_Y_roots',sum(all(dot(v,a)==0 for a in color+(weak,yp)) for v in rr)==20)
    for v in sorted(rr):
        test('root_transport_'+str(v),refl(v) in rr and refl(refl(v))==v and dot(refl(v),yp)==dot(v,y))
    test('adjoint_trace_Y',sum(F(dot(v,y),2)**2 for v in rr)==1800)
    cs=[{(0,5):1,(5,i):1} for i in range(1,4)]
    j={}
    for c in cs:
        j=plus(j,comm(c,transpose(c)))
    target={(0,0):3,(1,1):-1,(2,2):-1,(3,3):-1}
    test('full_sparse_current',j==target)
    yy={(i,i):a for i,a in enumerate((1,1,1,1,1,-5))}
    yyp={(i,i):a for i,a in enumerate((1,1,1,1,-5,1))}
    test('gauge_moment_zero',sum(yy[i,i]*v for (i,k),v in j.items() if i==k)==0)
    test('gauge_breaking_nonzero',sum(v*v for c in cs for v in comm(yy,c).values())==216)
    test('transported_gauge_preserved',all(not comm(yyp,c) for c in cs))
    test('three_flag_balances',[sum((4*int(i<k)-k)*j.get((i,i),0) for i in range(4)) for k in (1,2,3)]==[12,8,4])
    for p in (101,103):
        test('separate_modular_Lie_closure_'+str(p),closure_mod(cs+[transpose(c) for c in cs],p)==24)
    for a in [F(k,4) for k in range(-12,13)]:
        cc=[{key:a*v for key,v in c.items()} for c in cs]; jj={}
        for c in cc:
            jj=plus(jj,comm(c,transpose(c)))
        ff=[comm(cc[i],cc[k]) for i,k in combinations(range(3),2)]
        nf=sum(v*v for f in ff for v in f.values()); nj=sum(v*v for v in jj.values())
        test('exact_scaled_current_'+str(a),jj=={key:a*a*v for key,v in target.items() if a})
        test('all_scaled_curvature_'+str(a),nf==6*a**4 and nj==12*a**4)
        test('bare_not_shifted_action_'+str(a),2*(nf+F(nj)/4)==18*a**4)
        test('stationarity_direction_'+str(a),a==0 or 72*a**3!=0)
    test('zero_normal_control',not comm(yy,yyp) and not comm(yy,transpose(yy)))
    failed=[name for name,ok in checks if not ok]
    out=dict(total=len(checks),passed=sum(ok for _,ok in checks),failed=failed,
             native_imported=False,independent_authorship=False,physical_completion=False)
    print(json.dumps(out,sort_keys=True),flush=True)
    assert not failed,failed
    return out


if __name__=='__main__':
    run()
