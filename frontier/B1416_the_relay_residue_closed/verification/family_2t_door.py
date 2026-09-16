#!/usr/bin/env python3
"""Does Q(sqrt-3) imply the 2T door? B1186's 112-member shape-field family vs surjections pi_1 -> SL(2,3), counted with B993's own method
(homomorphisms by brute force on the group table; surjective = image of order 24). Relay CC_TO_CC3_2026-08-21 asked for a theorem
'Q(sqrt-3) => 2T'; this counts the family members that have the door."""
import json, itertools, snappy, sys
fam=json.load(open(__import__('pathlib').Path(__file__).resolve().parents[3]/'frontier'/'B1186_family_is_112'/'verification'/'family_census.json'))['members_B']
els=[]
for a,b,c,d in itertools.product(range(3),repeat=4):
    if (a*d-b*c)%3==1: els.append((a,b,c,d))
def mul(x,y):
    a,b,c,d=x; e,f,g,h=y; return ((a*e+b*g)%3,(a*f+b*h)%3,(c*e+d*g)%3,(c*f+d*h)%3)
INV={x:next(y for y in els if mul(x,y)==(1,0,0,1)) for x in els}
def ev(word,img):
    r=(1,0,0,1)
    for ch in word: r=mul(r, img[ch.lower()] if ch.islower() else INV[img[ch.lower()]])
    return r
def gen(S):
    seen={(1,0,0,1)}; fr=[(1,0,0,1)]
    while fr:
        nx=[]
        for s in fr:
            for g in S:
                t=mul(s,g)
                if t not in seen: seen.add(t); nx.append(t)
        fr=nx
    return len(seen)
rows=[]
for name in fam:
    M=snappy.Manifold(name); G=M.fundamental_group(); gens=G.generators(); rels=G.relators()
    if len(gens)>3: rows.append((name,len(gens),None)); continue
    cnt=sum(1 for imgs in itertools.product(els,repeat=len(gens)) if all(ev(r,dict(zip(gens,imgs)))==(1,0,0,1) for r in rels) and gen(imgs)==24)
    rows.append((name,len(gens),cnt))
have=[r for r in rows if r[2]]; none=[r for r in rows if r[2]==0]; skipped=[r for r in rows if r[2] is None]
print(f'family members {len(rows)}: with a 2T surjection {len(have)}, without {len(none)}, skipped (>3 generators) {len(skipped)}')
print('with the door:', [(n,c) for n,g,c in have])
print('skipped:', [n for n,g,c in skipped])
json.dump({'rows':rows},open(__import__('pathlib').Path(__file__).with_suffix('.json'),'w'),indent=1)
