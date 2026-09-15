#!/usr/bin/env python3
"""F6 --- the chi=0 wall: I is a truncation, not an index; and the mapping-torus
construction forces chi=0 at EVERY dimension, so the existing 4d lift inherits it."""
import sympy as sp, snappy
ok=True
a0,a1,a2,A0,A1,A2,t0,r1=sp.symbols('a0 a1 a2 A0 A1 A2 t0 r1')
print("="*76); print("1. is I = t0 - r1 an index, or a truncation?"); print("="*76)
red=sp.simplify(((a0-A0)-(a1-A1)).subs(a1,(A1+(a0-A0)+r1-t0)))
c1=(sp.simplify(red-(t0-r1))==0)
print(f"  from B1297's F:  (a0-a0*)-(a1-a1*) = {red}  == I : {c1}")
full=sp.simplify(((a0-A0)-(a1-A1)+(a2-A2)).subs({a2:a1-a0, A2:A1-A0}))
c2=(full==0)
print(f"  chi(M)=0 for V and V* => FULL alternating difference = {full}  (identically zero): {c2}")
print( "  therefore  I = -(a2 - a2*)  : a PARTIAL SUM of something that vanishes by dimension.")
print( "  => no index theorem stands behind I. Nothing forces its value either way ---")
print( "     which is exactly B1329's 'the identities leave I free'.")
ok &= c1 and c2
print()
print("="*76); print("2. is it only m004, or the whole geometric family?"); print("="*76)
fam=['m004','m003','m136','s958','v2873','t12833','t12835','m000','m202','s464','m206']
allc=True
for nm in fam:
    M=snappy.Manifold(nm)
    top={c['topology'] for c in M.cusp_info()}
    good = top <= {'torus cusp','Klein bottle cusp'}
    allc &= good
    print(f"   {nm:8s} cusps={M.num_cusps()}  boundary={sorted(top)}  -> chi = 0 : {good}")
print("  every compact 3-manifold with torus/Klein-bottle boundary has chi = 0.")
print("  => the ENTIRE geometric family shares the vanishing. B1330 could not have")
print("     escaped it by searching inside the family.")
ok &= allc
print()
print("="*76); print("3. does the existing 4d lift escape it?"); print("="*76)
print("  chi is multiplicative in fibrations and chi(S^1) = 0")
print("     => EVERY mapping torus, EVERY dimension, has chi = 0.")
print("  X23's canonical lift (B277/B1104-C3/B1190): orientation double cover = M x S^1")
print("     chi(M x S^1) = chi(M)*chi(S^1) = 0*0 = 0   <-- INHERITED")
print("  X23's own verdict 'N=2, non-chiral' is the same fact in physics language.")
print()
print("="*76); print("4. a chi != 0 four-manifold already one step off the chain"); print("="*76)
C=sp.Matrix([[2,-1,0,0,0,0],[-1,2,-1,0,0,0],[0,-1,2,-1,0,-1],
             [0,0,-1,2,-1,0],[0,0,0,-1,2,0],[0,0,-1,0,0,2]])
edges=sum(1 for i in range(6) for j in range(i+1,6) if C[i,j]!=0)
chi=2*6-edges
c3=(chi==7 and C.det()==3 and edges==5)
print(f"  minimal resolution of C^2/2T (the E6 Kleinian singularity, banked at B267):")
print(f"     6 (-2)-curves in the E6 tree, {edges} intersection points")
print(f"     chi = 2*6 - {edges} = {chi}   b2 = 6   form = -E6   det(Cartan) = {C.det()}")
print(f"  chi != 0, and it fibres over NOTHING.  checks: {c3}")
ok &= c3
print()
print("  FENCE (B727, carried verbatim in the handoff): McKay <-> Lie <-> CIZ <-> du Val")
print("  are ONE ADE classification, so this adds NO evidential weight for E6. It is a")
print("  candidate GEOMETRIC HOME with chi != 0 --- a different use of the same fact.")
raise SystemExit(0 if ok else 1)
