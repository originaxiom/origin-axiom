#!/usr/bin/env python3
"""Kac's classification of finite-order inner automorphisms of E6 (sm:B1363): Kac coordinates (s_0..s_6) with sum a_i s_i = m on the affine
E6 diagram (marks 1,1,2,3,2,1,2; three arms of length two on the trivalent node 3; diagram automorphism group S3 permuting the arms).
Exact order m requires gcd(s) = 1. Counts of classes and the fixed-subalgebra types."""
import itertools
from math import gcd
from functools import reduce
marks={0:1,1:1,2:2,3:3,4:2,5:1,6:2}; edges=[(1,2),(2,3),(3,4),(4,5),(3,6),(6,0)]; arms=[(1,2),(5,4),(0,6)]
def perms():
    for p in itertools.permutations(range(3)):
        m={3:3}
        for i,j in enumerate(p): m[arms[i][0]]=arms[j][0]; m[arms[i][1]]=arms[j][1]
        yield m
P=list(perms())
def comps(nodes):
    nodes=set(nodes); seen=set(); out=[]
    for n in nodes:
        if n in seen: continue
        stack=[n]; comp=set()
        while stack:
            x=stack.pop()
            if x in comp: continue
            comp.add(x); stack+=[b for a,b in edges if a==x and b in nodes]+[a for a,b in edges if b==x and a in nodes]
        seen|=comp; out.append(frozenset(comp))
    return out
def name(comp):
    n=len(comp); deg={x:sum(1 for a,b in edges if (a==x and b in comp) or (b==x and a in comp)) for x in comp}
    return f'A{n}' if max(deg.values())<=2 else {4:'D4',5:'D5',6:'E6'}[n]
def fixed(s):
    zero=[i for i in range(7) if s[i]==0]; f=sorted(name(c) for c in comps(zero)); nu=sum(1 for i in range(7) if s[i]>0)-1
    return '+'.join(f)+(f'+{nu}u(1)' if nu else '')
for m in (3,4):
    sol=[s for s in itertools.product(range(m+1),repeat=7) if sum(marks[i]*s[i] for i in range(7))==m]
    exact=[s for s in sol if reduce(gcd,s)==1]
    orb=lambda L:{min(tuple(s[p[i]] for i in range(7)) for p in P) for s in L}
    print(f'order {m}: Kac solutions {len(sol)}; exact order {len(exact)}; S3-classes exact {len(orb(exact))}, all {len(orb(sol))}; fixed types (exact): {sorted({fixed(s) for s in exact})}')
