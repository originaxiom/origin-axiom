#!/usr/bin/env sage-python
"""B485 continuing: SL(2,C) A-polynomial of the metallic bundles via character-variety
elimination. Build symbolic SL2C rep of pi_1(bundle), impose relators, extract meridian M
and longitude L eigenvalues, eliminate. Report the A-poly + genus per m."""
import snappy
from sage.all import QQ, PolynomialRing, ideal, Curve
def apoly_via_group(name, tag):
    M=snappy.Manifold(name)
    G=M.fundamental_group()
    gens=G.generators(); rels=G.relators()
    print(f"=== {tag} ({name}): gens={gens}, {len(rels)} relators ===", flush=True)
    # symbolic SL2C: g0 = [[s,1],[0,1/s]], g1=[[a,0],[c,1/a]] (up to conj), etc. -- 2-gen case
    if len(gens)!=2:
        print("  (not 2-generator; skipping symbolic route)", flush=True); return
    R=PolynomialRing(QQ,['s','a','c','Mv','Lv']); s,a,c,Mv,Lv=R.gens()
    import sage.all as S
    F=S.FractionField(R)
    A=S.matrix(F,[[s,1],[0,1/s]]); B=S.matrix(F,[[a,0],[c,1/a]])
    def word(w):
        m=S.identity_matrix(F,2)
        for ch in w:
            g=A if ch.lower()==gens[0] else B
            if ch.isupper(): g=g.inverse()
            m=m*g
        return m
    # relator = identity (up to sign)
    try:
        rel=word(rels[0])
        eqs=[rel[0,0]-1, rel[0,1], rel[1,0]]  # =I
        print("  relator equations built; running elimination (may be heavy)...", flush=True)
        # meridian, longitude from peripheral curves
        mer,lon=M.fundamental_group().peripheral_curves()[0]
        Mmat=word(mer); Lmat=word(lon)
        eqs += [Mmat[0,0]+Mmat[1,1]-(Mv+1/Mv), Lmat[0,0]+Lmat[1,1]-(Lv+1/Lv)]
        num=[F(e).numerator() for e in eqs]
        I=ideal(R,num)
        elim=I.elimination_ideal([s,a,c])
        print(f"  A-poly ideal (in Mv,Lv):", elim.gens(), flush=True)
        for g in elim.gens():
            try:
                print(f"    genus:", Curve(g).genus(), flush=True)
            except Exception as e:
                print(f"    genus err {str(e)[:40]}", flush=True)
    except Exception as e:
        print(f"  elimination failed: {str(e)[:120]}", flush=True)
for name,tag in [('m136','m=2'),('s464','m=3')]:
    apoly_via_group(name,tag)
print("APOLY ELIM DONE", flush=True)
