#!/usr/bin/env python3
"""Exact finite-permutation check of the Q8 cover defined by the input holonomies."""
from itertools import product
from pathlib import Path
import json

# Normal form A^a B^b with A^4=1, B^2=A^2, BA=A^-1 B.
G=list(product(range(4),range(2)))
e=(0,0); A=(1,0); B=(0,1)
def mul(x,y):
    a,b=x; c,d=y
    return ((a+(-1)**b*c+2*b*d)%4,(b+d)%2)
def power(x,n):
    r=e
    for _ in range(n): r=mul(r,x)
    return r
def inv(x):
    return next(y for y in G if mul(x,y)==e and mul(y,x)==e)
def comm(x,y):
    return mul(mul(mul(x,y),inv(x)),inv(y))
def cycles(perm):
    seen=set();out=[]
    for start in range(len(perm)):
        if start in seen:continue
        cyc=[];now=start
        while now not in seen:
            seen.add(now);cyc.append(now);now=perm[now]
        out.append(cyc)
    return out
checks=[]
def check(name,v):
    assert v,name
    checks.append(name)
check('Q8 associative: all 512 triples',all(mul(mul(x,y),z)==mul(x,mul(y,z)) for x,y,z in product(G,repeat=3)))
check('input holonomies generate all eight sheets',len({mul(power(A,a),power(B,b)) for a,b in G})==8)
z=comm(A,B)
check('peripheral monodromy is central -1 of order two',z==(2,0) and power(z,2)==e and all(mul(z,x)==mul(x,z) for x in G))
perms={name:[G.index(mul(x,g)) for g in G] for name,x in [('A',A),('B',B),('peripheral',z)]}
peripheral_cycles=cycles(perms['peripheral'])
check('peripheral permutation has four 2-cycles',sorted(map(len,peripheral_cycles))==[2,2,2,2])
chi_punctured=-len(G)
ends=len(peripheral_cycles)
chi_compact=chi_punctured+ends
genus=(2-chi_compact)//2
check('compactification genus three by Euler characteristic',genus==3 and chi_compact==-4)
check('Riemann-Hurwitz independently gives genus three',2*genus-2==sum(len(c)-1 for c in peripheral_cycles))
automorphisms={}
for name,aa,bb in [('L',A,mul(A,B)),('R',mul(A,B),B)]:
    f=lambda x: mul(power(aa,x[0]),power(bb,x[1]))
    table={x:f(x) for x in G}
    check(name+' descends to bijective Q8 homomorphism, all 64 products',len(set(table.values()))==8 and all(table[mul(x,y)]==mul(table[x],table[y]) for x,y in product(G,repeat=2)))
    check(name+' fixes central peripheral element',table[z]==z)
    automorphisms[name]=[G.index(table[x]) for x in G]
result={'degree':len(G),'normal_form':'A^a B^b, A^4=1, B^2=A^2, BA=A^-1 B',
        'sheet_labels':G,'permutations':perms,'peripheral_cycles':peripheral_cycles,
        'punctured_euler_characteristic':chi_punctured,'number_lifted_punctures':ends,
        'compact_genus':genus,'L_R_quotient_automorphisms':automorphisms,'checks':checks,
        'grade':'COMPUTED EXACTLY: topological cover and quotient automorphisms only',
        'not_computed':['spin-structure lift','fermion determinant/Pfaffian','chiral block space','metaplectic comparison of the twisted theory','anomalies','physical spectrum']}
out=Path(__file__).with_name('cover_results.json')
out.write_text(json.dumps(result,indent=2)+'\n')
print(f'{len(checks)} exact cover checks passed. Degree={len(G)}, punctures={ends}, compact genus={genus}.')
print('L and R both preserve the Q8 quotient kernel. Quantum determinant is NOT computed.')
