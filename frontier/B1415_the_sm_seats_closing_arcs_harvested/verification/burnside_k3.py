#!/usr/bin/env python3
"""B1359: Burnside count for a 2T action with isolated fixed points and Nikulin's numbers (order 2: 8, 3: 6, 4: 4, 6: 2)."""
import itertools
def qmul(p,q):
    a1,b1,c1,d1=p; a2,b2,c2,d2=q
    w=a1*a2-b1*b2-c1*c2-d1*d2; x=a1*b2+b1*a2+c1*d2-d1*c2; y=a1*c2-b1*d2+c1*a2+d1*b2; z=a1*d2+b1*c2-c1*b2+d1*a2
    assert all(v%2==0 for v in (w,x,y,z)); return (w//2,x//2,y//2,z//2)
def qinv(p): return (p[0],-p[1],-p[2],-p[3])
G=[(2,0,0,0),(-2,0,0,0),(0,2,0,0),(0,-2,0,0),(0,0,2,0),(0,0,-2,0),(0,0,0,2),(0,0,0,-2)]+[s for s in itertools.product((1,-1),repeat=4)]
E=(2,0,0,0)
def order(g):
    x=g; n=1
    while x!=E: x=qmul(x,g); n+=1
    return n
def gen(S):
    H={E}; fr=[E]
    while fr:
        nx=[]
        for h in fr:
            for s in S:
                t=qmul(h,s)
                if t not in H: H.add(t); nx.append(t)
        fr=nx
    return frozenset(H)
# all subgroups
subs=set()
for a in G:
    for b in G: subs.add(gen([a,b]))
def conj(H,g): return frozenset(qmul(qmul(g,h),qinv(g)) for h in H)
classes=[]
for H in sorted(subs,key=len):
    if not any(conj(H,g) in c for c in classes for g in [E]) and not any(H in c for c in classes):
        classes.append({conj(H,g) for g in G})
reps=[min(c,key=lambda H:sorted(H)) for c in classes]
print('subgroup classes of 2T by order:', sorted(len(H) for H in reps))
# fixed cosets: number of cosets gH of 2T/H fixed by x = #{gH : x g H = g H} = #{g: g^-1 x g in H}/|H|
def fixed_cosets(x,H): return sum(1 for g in G if qmul(qmul(qinv(g),x),g) in H)//len(H)
nik={2:8,3:6,4:4,6:2}
nontriv=[H for H in reps if len(H)>1]
# unknowns n_H >= 0 for nontrivial H; equations for one representative x of each nontrivial element order (all elements of the same order are conjugate? in 2T: order 4 elements: 6 (one class), order 6: 8 (two classes?), order 3: 8, order 2: 1) -- use every element
eqs=[]
for x in G:
    if x==E: continue
    eqs.append(([fixed_cosets(x,H) for H in nontriv], nik[order(x)]))
sols=[]
rng=range(0,9)
for n in itertools.product(rng,repeat=len(nontriv)):
    if all(sum(c*v for c,v in zip(co,n))==rhs for co,rhs in eqs): sols.append(n)
names={2:'A1',3:'A2',4:'A3',6:'A5',8:'D4',24:'E6'}
for n in sols:
    print('solution:', ' + '.join(f'{v}x{names[len(H)]}' for v,H in zip(n,nontriv) if v), ' rank', sum(v*(len(H) and {2:1,3:2,4:3,6:5,8:4,24:6}[len(H)]) for v,H in zip(n,nontriv)))
print('number of solutions:', len(sols))
