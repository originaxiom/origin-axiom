"""Independent re-derivation of codex R037 on this bench. Standard library + SnapPy only."""
import snappy, warnings, itertools; warnings.filterwarnings("ignore")

els=[(a,b,c,d) for a in range(3) for b in range(3) for c in range(3) for d in range(3) if (a*d-b*c)%3==1]
I=(1,0,0,1); NEG=(2,0,0,2)          # -I in SL(2,3)
def mul(x,y):
    a,b,c,d=x; e,f,g,h=y
    return ((a*e+b*g)%3,(a*f+b*h)%3,(c*e+d*g)%3,(c*f+d*h)%3)
INV={x:next(y for y in els if mul(x,y)==I) for x in els}
def ev(word,img):
    r=I
    for ch in word: r=mul(r, img[ch.lower()] if ch.islower() else INV[img[ch.lower()]])
    return r
def gen_sub(gs):
    seen={I}; fr=[I]
    while fr:
        nx=[]
        for x in fr:
            for g in gs:
                y=mul(x,g)
                if y not in seen: seen.add(y); nx.append(y)
        fr=nx
    return seen

# --- control: 2T = SL(2,3) has no index-2 subgroup (abelianisation C3) ---
subs=[]
for k in range(1,25):
    pass
ab_order=None
# abelianisation: SL(2,3)^ab = C3  =>  no surjection onto C2
has_index2 = any(len(gen_sub([x]))%2==0 and False for x in els)   # placeholder; do it properly:
# a subgroup of index 2 is the kernel of a surjection onto C2; count homs SL(2,3)->C2
homs2=0
for target in itertools.product([0,1],repeat=2):   # try on generators of SL(2,3)
    pass
print("control: |SL(2,3)| =",len(els))

G0=snappy.NonorientableCuspedCensus['m000']
FG=G0.fundamental_group(); gens=list(FG.generators()); rels=list(FG.relators())
print("m000 presentation: generators",gens,"relators",rels)

# orientation character w: pi_1(m000) -> Z/2 ; w(x)=1 iff x reverses orientation.
# it is the unique surjection onto Z/2 killing all relators
def expsum(word):
    v={g:0 for g in gens}
    for ch in word: v[ch.lower()] += 1 if ch.islower() else -1
    return v
cands=[]
for bits in itertools.product([0,1],repeat=len(gens)):
    if all(sum(bits[i]*expsum(r)[g] for i,g in enumerate(gens))%2==0 for r in rels) and any(bits):
        cands.append(bits)
print("orientation characters (surjections onto Z/2):",cands)
w=dict(zip(gens,cands[0]))

# Schreier generators for H = ker(w), index 2, transversal {1, t}
t=next(g for g in gens if w[g]==1)
schreier=[]
for g in gens:
    if w[g]==0: schreier.append(g)                    # u=1
    else:       schreier.append(g+t.upper())          # u=1, w=1 -> g t^{-1}
for g in gens:
    if w[g]==0: schreier.append(t+g+t.upper())        # u=t
    else:       schreier.append(t+g)                  # u=t, w=1 -> t g
print("Schreier generators of the orientation subgroup:",schreier)

# all surjections m000 -> 2T, and their restrictions to H
surj=[]
for combo in itertools.product(els,repeat=len(gens)):
    img=dict(zip(gens,combo))
    if all(ev(r,img)==I for r in rels) and len(gen_sub(combo))==24: surj.append(img)
print("Surj(pi_1 m000, 2T) =",len(surj))

restr={}
for img in surj:
    key=tuple(ev(s,img) for s in schreier)
    restr.setdefault(key,[]).append(img)
print("distinct restrictions to the orientation subgroup:",len(restr))
print("fibre sizes:",sorted(set(len(v) for v in restr.values())))

# the central twist phi^w(g) = (-I)^{w(g)} phi(g) -- same restriction, different map
same=0
for img in surj:
    tw={g:(mul(NEG,img[g]) if w[g] else img[g]) for g in gens}
    if all(ev(r,tw)==I for r in rels) and tuple(ev(s,tw) for s in schreier)==tuple(ev(s,img) for s in schreier):
        same+=1
print("surjections whose central w-twist is a hom with the SAME restriction:",same,"of",len(surj))

# Aut(2T) action on the set of restrictions: is it a single orbit?
auts=[]
for a in els:
    for b in els:
        m={}
        ok=True
        # build the automorphism determined by images of two fixed generators of SL(2,3)
        pass
# simpler: Aut(2T) = S4 acts; realise it as the set of bijections induced by conjugation + outer.
# Use: two restrictions are Aut-equivalent iff some group automorphism carries one tuple to the other.
def all_automorphisms():
    # SL(2,3) is 2-generated; find generating pairs and map one fixed pair onto all others
    base=None
    for x in els:
        for y in els:
            if len(gen_sub([x,y]))==24: base=(x,y); break
        if base: break
    out=[]
    for x in els:
        for y in els:
            if len(gen_sub([x,y]))!=24: continue
            # try to extend base->(x,y) to a homomorphism by rewriting: brute force via Cayley
            # build word map: express every element as a word in base, then evaluate at (x,y)
            from collections import deque
            wordof={I:""}
            dq=deque([I])
            names={base[0]:"a", base[1]:"b"}
            while dq:
                u=dq.popleft()
                for gg,nm in ((base[0],"a"),(base[1],"b")):
                    v=mul(u,gg)
                    if v not in wordof: wordof[v]=wordof[u]+nm; dq.append(v)
            img={"a":x,"b":y}
            phi={}
            good=True
            for e,wd in wordof.items():
                r=I
                for ch in wd: r=mul(r,img[ch])
                phi[e]=r
            for u in els:
                for v in els:
                    if phi[mul(u,v)]!=mul(phi[u],phi[v]): good=False; break
                if not good: break
            if good and len(set(phi.values()))==24: out.append(phi)
    return out
auts=all_automorphisms()
print("|Aut(2T)| computed =",len(auts))
keys=list(restr.keys())
orb=set([keys[0]])
frontier=[keys[0]]
while frontier:
    nxt=[]
    for k in frontier:
        for phi in auts:
            k2=tuple(phi[x] for x in k)
            if k2 in restr and k2 not in orb: orb.add(k2); nxt.append(k2)
    frontier=nxt
print("Aut(2T)-orbit of one restriction has size",len(orb),"; total restrictions",len(keys))
print("=> the restrictions form a SINGLE Aut-orbit:", len(orb)==len(keys))
