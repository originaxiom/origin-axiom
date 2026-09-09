"""S1 cell 2 -- does the object actually NOMINATE E6? The load-bearing fact is
pi_1(m004) ->> 2T (binary tetrahedral, = SL(2,3), order 24); McKay then gives E6.
Brute force over ALL homomorphisms: enumerate pairs (A,B) in SL(2,3)^2 satisfying
every relator of the presentation, then test which generate the WHOLE group."""
import itertools, json, snappy

# SL(2,3): 2x2 matrices over F_3 with det 1
def mats():
    out=[]
    for a,b,c,d in itertools.product(range(3),repeat=4):
        if (a*d-b*c) % 3 == 1: out.append((a,b,c,d))
    return out
def mul(X,Y):
    a,b,c,d=X; e,f,g,h=Y
    return ((a*e+b*g)%3,(a*f+b*h)%3,(c*e+d*g)%3,(c*f+d*h)%3)
def inv(X):
    a,b,c,d=X; return (d%3,(-b)%3,(-c)%3,a%3)          # det 1
I=(1,0,0,1)
G=mats(); assert len(G)==24, len(G)
print(f"SL(2,3) = 2T : order {len(G)}")

M=snappy.Manifold('m004'); P=M.fundamental_group()
gens=P.generators(); rels=P.relators()
print(f"pi_1(m004): generators {gens}, relators {rels}")

def word_val(w, asg):
    v=I
    for ch in w:
        g = asg[ch.lower()]
        v = mul(v, g if ch.islower() else inv(g))
    return v

def gen_subgroup(elts):
    S={I}; frontier=[I]
    while frontier:
        x=frontier.pop()
        for g in elts:
            for y in (mul(x,g), mul(x,inv(g))):
                if y not in S: S.add(y); frontier.append(y)
    return S

homs=0; surj=0
for A,B in itertools.product(G,repeat=2):
    asg={gens[0]:A, gens[1]:B}
    if all(word_val(r,asg)==I for r in rels):
        homs+=1
        if len(gen_subgroup([A,B]))==24: surj+=1
print(f"\nhomomorphisms pi_1(m004) -> 2T : {homs}")
print(f"  of which SURJECTIVE           : {surj}")
print(f"  pi_1(m004) ->> 2T ?           : {surj>0}   <- the nomination")

# control: the trefoil should behave differently from the object
ctrl={}
for name in ['4_1','3_1','5_2']:
    try:
        K=snappy.Manifold(name); Q=K.fundamental_group()
        g2,r2=Q.generators(),Q.relators()
        if len(g2)!=2: ctrl[name]="skip (not 2-generator)"; continue
        s=0
        for A,B in itertools.product(G,repeat=2):
            asg={g2[0]:A,g2[1]:B}
            if all(word_val(r,asg)==I for r in r2) and len(gen_subgroup([A,B]))==24: s+=1
        ctrl[name]=s
    except Exception as e: ctrl[name]=f"err {e}"
print(f"\ncontrol -- surjections onto 2T by knot: {ctrl}")
print("  (B993/B996: surjecting onto 2T is GENERIC -- ~1/3 of manifolds do.")
print("   So the nomination is REAL but NOT distinctive; S1 tests acceptance, not uniqueness.)")
json.dump({"order":24,"homs":homs,"surjective":surj,"nominates_E6":surj>0,"control":ctrl,
           "fence":"B993/B996: surjection onto 2T is generic (~1/3); the nomination is real, not distinctive"},
          open("frontier/B1228_S1_the_nomination/nomination_results.json","w"), indent=1)
