#!/usr/bin/env python3
"""B1418 cell 1 -- THE CLASS CENSUS: all 112 members of B1186's Q(sqrt-3) family, on canonical isometries (E81):
cusps, A/B membership, cover of m004 (degree <= 10), chirality, the 2T door (surjections onto SL(2,3), every member),
the count of three, and for one-cusped members the Alexander polynomial's root classes."""
import json, itertools, pathlib, sys, time, sympy as sp, snappy
HERE=pathlib.Path(__file__).resolve().parent; ROOT=HERE.parents[2]
fam=json.load(open(ROOT/'frontier/B1186_family_is_112/verification/family_census.json')); A=set(fam['members_A']); B=fam['members_B']
def det2(m): return m[0][0]*m[1][1]-m[0][1]*m[1][0]
def cm(iso,i):
    c=iso.cusp_maps()[i]; return [[int(c[0][0]),int(c[0][1])],[int(c[1][0]),int(c[1][1])]]
# SL(2,3) table
els=[(a,b,c,d) for a,b,c,d in itertools.product(range(3),repeat=4) if (a*d-b*c)%3==1]
def mul(x,y):
    a,b,c,d=x; e,f,g,h=y; return ((a*e+b*g)%3,(a*f+b*h)%3,(c*e+d*g)%3,(c*f+d*h)%3)
INV={x:next(y for y in els if mul(x,y)==(1,0,0,1)) for x in els}
def gen_order(S):
    seen={(1,0,0,1)}; fr=[(1,0,0,1)]
    while fr:
        nx=[]
        for s in fr:
            for g in S:
                t=mul(s,g)
                if t not in seen: seen.add(t); nx.append(t)
        fr=nx
    return len(seen)
def door(G):
    gens=G.generators(); rels=G.relators(); cnt=0
    for imgs in itertools.product(els,repeat=len(gens)):
        img=dict(zip(gens,imgs)); ok=True
        for r in rels:
            x=(1,0,0,1)
            for ch in r: x=mul(x, img[ch.lower()] if ch.islower() else INV[img[ch.lower()]])
            if x!=(1,0,0,1): ok=False; break
        if ok and gen_order(imgs)==24: cnt+=1
    return cnt
t=sp.symbols('t')
def alexander(M):
    G=M.fundamental_group(); gens=G.generators(); rels=G.relators(); n=len(gens)
    E=sp.Matrix([[sum((1 if ch.islower() else -1) for ch in r if ch.lower()==g) for g in gens] for r in rels]); ns=E.nullspace()
    if len(ns)!=1: return None
    w=ns[0]; w=w*sp.ilcm(*[x.q for x in w]); w=[int(x) for x in w]; g0=int(sp.gcd(w)) or 1; w=[x//g0 for x in w]
    img={g:t**w[i] for i,g in enumerate(gens)}
    def fox(word,var):
        total=0; prefix=1
        for ch in word:
            g=ch.lower(); e=1 if ch.islower() else -1; im=img[g]
            if g==var: total+= prefix if e==1 else -prefix*im**-1
            prefix*=im**e
        return sp.expand(total)
    J=sp.Matrix([[fox(r,g) for g in gens] for r in rels]); D=0
    for cols in itertools.combinations(range(n),n-1):
        for rws in itertools.combinations(range(len(rels)),n-1):
            m=sp.expand(J.extract(list(rws),list(cols)).det()*t**40); D=sp.gcd(D,m) if D!=0 else m
    f=sp.factor_list(sp.expand(D)); facs=[(str(p),int(e)) for p,e in f[1] if p.free_symbols]
    return [(p,e) for p,e in facs if p!='t']
def root_class(p):
    P=sp.Poly(sp.sympify(p),t)
    if P.degree()==0: return 'unit'
    if sp.sympify(p)==t**2-3*t+1: return 'golden'
    for k in range(1,25):
        if sp.rem(P, sp.Poly(sp.cyclotomic_poly(k,t),t)).is_zero and P.degree()==sp.Poly(sp.cyclotomic_poly(k,t),t).degree(): return f'roots of unity, order {k}'
    return 'other'
covers=set(['m206','s961','t12839','t12840','o10_150685','o10_150696','o10_150703'])
rows=[]; t0=time.time()
for name in B:
    M=snappy.Manifold(name); L=M.is_isometric_to(M,return_isometries=True); nc=M.num_cusps()
    amph=any(det2(cm(iso,0))==-1 for iso in L)
    vals=set()
    for iso in L:
        for i in range(nc):
            if iso.cusp_images()[i]!=i: continue
            X=cm(iso,i)
            if det2(X)!=1: continue
            vals.add(abs(det2([[X[0][0]-1,X[0][1]],[X[1][0],X[1][1]-1]])))
    G=M.fundamental_group(); d=door(G)
    alex=alexander(M) if nc==1 else None
    rows.append({'name':name,'cusps':nc,'A':name in A,'cover_of_m004':name in covers,'H1':str(M.homology()),'sym':len(L),'chiral':not amph,'door':d,'three':3 in vals,'det_values':sorted(vals),'gens':len(G.generators()),
                 'alexander':alex,'root_classes':[root_class(p) for p,e in alex] if alex else None})
    print(f"{name:12s} cusps {nc} A={name in A!s:5} cover={name in covers!s:5} chiral={not amph!s:5} door={d:5d} three={3 in vals!s:5} {str(M.homology()):16s} alex={alex}", flush=True)
json.dump(rows,open(HERE/'c1_class_census.json','w'),indent=1)
one=[r for r in rows if r['cusps']==1]
print('\nQ1.1 one-cusped members with chirality AND the door:', [r['name'] for r in one if r['chiral'] and r['door']>0], '; with the three:', [r['name'] for r in one if r['three']])
print('Q1.2 members with all four (chiral, atom, door, three):', [(r['name'],r['cusps'],r['A']) for r in rows if r['chiral'] and r['door']>0 and r['three']])
from collections import Counter
print('Q1.3 partition of A by (chiral, door>0, three):', Counter((r['chiral'],r['door']>0,r['three']) for r in rows if r['A']))
print('    partition of B\\A:', Counter((r['chiral'],r['door']>0,r['three']) for r in rows if not r['A']))
m=[r for r in rows if r['name']=='m004'][0]; print('control m004:', m['chiral'], m['door'], m['det_values'], '| m202:', [r for r in rows if r['name']=='m202'][0]['det_values'])
print('seconds', round(time.time()-t0))
