import json
d=json.load(open('batch_7.json'))
# idx: (kind,label,quote,conf)
P,F,N,O='PAIRING','FLATNESS','NON-UNIQUENESS','OTHER'
m={
20:(O,'no-landing-site',"has an order parameter at the manifold level",'low'),
21:(N,'genericity',"is object-specific to m004",'medium'),
22:(F,'zero-intertwiner',"zero-intertwiner",'low'),
23:(O,'value-miss',"registered-comparison-null",'medium'),
24:(O,'value-miss',"matches the measured low-energy couplings through a pure SM desert",'medium'),
25:(O,'no-landing-site',"killed by the chain's own algebra",'medium'),
26:(P,'rigidity-collapse',"rigidity-collapse-with-mechanism",None),
27:(F,'collapse-by-similarity',"rigidity-collapse-with-mechanism",'low'),
28:(O,'premise-false',"group-membership-refutation",'medium'),
29:(O,'premise-false',"stabilizer-computation",'medium'),
30:(O,'arithmetic-mismatch',"category-mismatch",'medium'),
31:(O,'no-landing-site',"rank-vs-reality-dichotomy",'medium'),
32:(O,'scope',"cross-family-counterexample",'medium'),
33:(O,'no-landing-site',"self-defeating-escape",'medium'),
34:(O,'scope',"kind-mismatch",'low'),
35:(F,'vacuity',"vacuity",'low'),
36:(O,'instrument',"vacuity",'medium'),
37:(O,'instrument',"ill-posed-conjunction (rarity implies separation)",'medium'),
38:(N,'genericity',"genericity",'medium'),
39:(O,'no-landing-site',"enumeration-exhausted",'low'),
40:(O,'absence-at-depth',"absence-at-depth",'medium'),
41:(O,'premise-false',"self-refuted-draft (instrument already existed)",'high'),
42:(O,'value-miss',"powered-exclusion (sealed crossing; both sectors powered)",'high'),
43:(O,'value-miss',"powered-exclusion (the sealed refresh windows, executed once)",'high'),
44:(P,'amphichirality-deletes',"the object's amphichirality deletes the quantized sector of its own boundary action",'low'),
45:(O,'value-miss',"powered-exclusion",'high'),
46:(O,'value-miss',"powered-exclusion",'high'),
47:(N,'element-specific',"every value-bearing quantity element-specific",'low'),
48:(F,'non-isolation',"has NO 0-dimensional fixed set",'low'),
49:(P,'Poincare-duality',"forces h1(D;27) = h1(D;27bar) in every cell",'high'),
50:(O,'no-landing-site',"every row rank 6",'medium'),
51:(F,'identical-vanishing',"every anomaly channel over the derived 16 is zero",'high'),
52:(O,'no-landing-site',"type mismatch, structural",'medium'),
53:(O,'value-miss',"0 of 18 SM targets involve a regulator across 216 cells",'medium'),
54:(F,'invariant-content-zero',"INVARIANT CONTENT ZERO",'medium'),
55:(N,'genericity',"GENERIC (Montgomery pair-correlation / Katz-Sarnak",'low'),
56:(O,'premise-false',"genericity",'low'),
57:(N,'genericity',"genericity",'medium'),
58:(N,'genericity',"genericity",'medium'),
59:(O,'arithmetic-mismatch',"category-mismatch",'medium'),
60:(O,'no-landing-site',"vacuity",'low'),
61:(O,'instrument',"vacuity",'high'),
62:(N,'symmetry-cannot-select',"symmetry-cannot-select",'high'),
63:(N,'dimension-count',"dimension-count",'medium'),
64:(F,'trivial-torsor',"trivial-torsor",'medium'),
65:(O,'premise-false',"premise refuted by population test",'high'),
66:(O,'arithmetic-mismatch',"arithmetic disjointness of the ACTION, not of the pieces.",'medium'),
67:(O,'premise-false',"kind-mismatch",'high'),
68:(O,'value-miss',"kind-mismatch",'high'),
69:(O,'arithmetic-mismatch',"cited-as-sufficient",'high'),
70:(O,'arithmetic-mismatch',"cited-as-sufficient",'high'),
71:(O,'premise-false',"pre-registered expectation falsified by its own run",'high'),
72:(O,'arithmetic-mismatch',"the discriminant forms are UNEQUAL on every invariant",'high'),
73:(N,'cannot-select',"IDENTICAL for both candidates",'medium'),
74:(O,'no-landing-site',"EVERY element of SO(2k+1) has eigenvalue +1",'medium'),
75:(O,'arithmetic-mismatch',"the GENUS GROUP HAS ORDER 2, against Gal's order 4",'high'),
76:(F,'rigid-zero-index',"BOTH h1 VANISH: W1 and W2 are RIGID",'high'),
77:(O,'no-landing-site',"The GEOMETRY forbids it",'medium'),
78:(O,'no-landing-site',"Exhaustive scan.",'medium'),
79:(P,'sigma-parity',"a Morse-Bott zero locus and a vortex locus along Fix(sigma) are sigma-EVEN",'medium'),
80:(P,'self-duality',"T-GALOIS-SELF-DUALITY",'high'),
81:(P,'symmetry-paired',"h^1(M; 27) != h^1(M; 27bar)",'low'),
82:(F,'zero-index',"every one of the four returns index ZERO",'low'),
83:(O,'no-landing-site',"The falsifier does not fire",'low'),
84:(F,'abelian-or-nothing',"ABELIAN OR NOTHING, by Borel density",'medium'),
85:(O,'instrument',"The instrument is itself blind, demonstrated by its own miss",'high'),
86:(F,'vacuity',"All three vacuous, two by theorem and one by identity.",'low'),
87:(N,'no-selection',"A basin, not a direction.",'medium'),
88:(N,'residual-freedom',"The residual freedom is 48",'medium'),
89:(O,'power',"branch B is dead on power",'medium'),
90:(O,'power',"the value channel needs ~1e-2 to 1e-3 relative precision",'medium'),
91:(O,'no-landing-site',"no background has its five charged sectors at class index two",'medium'),
92:(N,'non-separating',"none of six stated features takes disjoint values on the two sets",'low'),
93:(O,'instrument',"Under four hash seeds fourteen scripts print the same thing",'medium'),
94:(P,'dual-odd-index',"odd under dualising, so a module with V* isomorphic to sigma^*V has index zero",'high'),
95:(O,'no-landing-site',"Computation to completion with B1418's own driver",'low'),
}
out=[]
for i,e in enumerate(d):
    if i<20:
        out.append(dict(id=e['id'],kind=O,label='unstated',quote='',confidence='high')); continue
    k,l,q,c=m[i]
    txt=e['claim_killed']+' '+e['kill_form']
    if q is None or q not in txt:
        print('FIX',i,e['id'],q)
        q=' '.join(e['claim_killed'].split()[:15]) if q is None else q
    if len(q.split())>20: print('LONG',i)
    out.append(dict(id=e['id'],kind=k,label=l,quote=q,confidence=c or 'low'))
json.dump(out,open('out_7.json','w'),ensure_ascii=False,indent=1)
from collections import Counter
print(Counter(o['kind'] for o in out),len(out))
