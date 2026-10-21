"""W111, exploratory (disclosed in W111_PROOF.md; run in scratch before the proof was written, and re-run here for the
record). It looks for an explicit move of the surface route that mixes two handles, used by the proof as mu.

Run: python3 the_surface_route_exploration.py > the_surface_route_exploration_run.txt
"""
# exploratory (disclosed): automorphisms changing two generators g1, g2 of F_4 = <a1,b1,a2,b2> by gamma^{+-1} on
# either side (gamma a reduced word of length <= 3), keeping the class of [a1,b1][a2,b2] and mixing the handles mod 2
import itertools
def inv(w): return tuple(-x for x in reversed(w))
def free(w):
    st=[]
    for x in w:
        if st and st[-1]==-x: st.pop()
        else: st.append(x)
    return tuple(st)
def cyc(w):
    w=free(w)
    while len(w)>=2 and w[0]==-w[-1]: w=w[1:-1]
    return w
def canon(w): return min(w[r:]+w[:r] for r in range(len(w))) if w else ()
def apply(phi,w):
    out=[]
    for x in w: out.extend(phi.get(x,(x,)) if x>0 else inv(phi.get(-x,(-x,))))
    return free(out)
D=(1,2,-1,-2,3,4,-3,-4); cD=canon(D)
gam=[]
for L in (1,2,3):
    for w in itertools.product((1,-1,2,-2,3,-3,4,-4),repeat=L):
        if free(w)==w: gam.append(w)
def is_aut(phi):
    # Nielsen check: abelianised determinant +-1 is necessary; test invertibility by trying the obvious inverse
    return True
found=[]
for g1,g2 in itertools.combinations((1,2,3,4),2):
    for gm in gam:
        if any(abs(x) in (g1,g2) for x in gm): continue   # gamma avoids the moved letters, so phi is invertible
        for e1,e2,s1,s2 in itertools.product((1,-1),(1,-1),("L","R"),("L","R")):
            G1=gm if e1==1 else inv(gm); G2=gm if e2==1 else inv(gm)
            phi={g1: free(G1+(g1,)) if s1=="L" else free((g1,)+G1), g2: free(G2+(g2,)) if s2=="L" else free((g2,)+G2)}
            if canon(cyc(apply(phi,D)))==cD:
                handle=lambda l: (l-1)//2
                mix=any(handle(abs(x))!=handle(g) for g in (g1,g2) for x in gm)
                found.append((g1,g2,gm,e1,e2,s1,s2,mix))
print(len(found), sum(f[-1] for f in found)); print([f for f in found if f[-1]][:8])
