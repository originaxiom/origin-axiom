#!/usr/bin/env python3
"""Which of B1330's objects are protected by B1297 sec5.2 mechanism (ii)?

Mechanism (ii): an ORIENTATION-PRESERVING symmetry that INVERTS the order-3 character
forces J(psi) = J(psi^-1) = -J(psi) = 0.  B1330 selected for CHIRAL (no MIRROR) --- a
different condition, which does not exclude this.

TEST: let Delta = Z/3 be the deck group of the cusp-trivial cyclic cover Mt -> M.
Every symmetry Q of M lifts (ker chi = ker chi^2), and Qt normalises Delta with
Qt g Qt^-1 = g^eps ;  eps = +1  iff  Q FIXES chi.
  * if <Delta, lifts> is ABELIAN  -> eps = +1 for every lift -> NO symmetry inverts chi
                                     -> the object is UNPROTECTED (mechanism (ii) dead)
  * if it is NON-ABELIAN          -> some lift inverts chi  -> PROTECTED
The lifted group has order 3*|Sym(M)|; if that equals |Sym(Mt)| there are no hidden
symmetries and the verdict is exact.  If |Sym(Mt)| is larger, the verdict is UNDETERMINED.
"""
import snappy

def analyse(name):
    M = snappy.Manifold(name)
    symM = M.symmetry_group(); nM = symM.order()
    best = None
    for C in M.covers(3, method='low_index'):
        if C.num_cusps() != M.num_cusps()*3:      # cusp-trivial: every cusp splits
            continue
        G = C.symmetry_group()
        if G.order() % 3 != 0:                    # must contain the deck Z/3 -> regular
            continue
        lifted = 3*nM
        exact  = (G.order() == lifted)
        if best is None or exact:
            best = (str(M.homology()), str(symM), nM, str(G), G.order(),
                    G.is_abelian(), lifted, exact)
    return best

print("="*92)
print("Are B1330's objects protected by B1297 mechanism (ii)?  (chirality does not exclude it)")
print("="*92)
rows = {}
for nm in ['s958','v2873','t12833','t12835']:
    r = analyse(nm)
    rows[nm] = r
    if r is None:
        print(f"  {nm:9s} no regular cusp-trivial Z/3 cover found"); continue
    h, sM, nM, sC, nC, ab, lift, exact = r
    if not exact:      verdict = "UNDETERMINED (hidden symmetries in the cover)"
    elif ab:           verdict = "UNPROTECTED  -- no symmetry inverts chi"
    else:              verdict = "PROTECTED    -- a lift inverts chi"
    print(f"  {nm:9s} H1={h:14s} Sym(M)={sM:9s}({nM})  Sym(cover)={sC:9s}({nC}) "
          f" abelian={str(ab):5s} 3|Sym(M)|={lift:2d} exact={str(exact):5s}")
    print(f"            -> {verdict}")

print()
print("-"*92)
# C-alive: m004 has H1 = Z, so it has NO cusp-trivial Z/3 cover. B1297 used the CYCLIC
# cover C_3 instead. Cross-check against B1297 sec4.2's recorded values: Tors H1(C_3) = (Z/4)^2
# and 12 orientation-preserving + 12 reversing = 24 symmetries, with P acting as -1.
M4 = snappy.Manifold('m004'); n4 = M4.symmetry_group().order()
ctrl = None
for C in M4.covers(3, method='low_index'):
    G = C.symmetry_group()
    if G.order() % 3 == 0 and G.order() == 3*n4:
        ctrl = (str(C.homology()), str(G), G.order(), G.is_abelian()); break
if ctrl:
    print(f"  CONTROL m004 cyclic C_3: H1={ctrl[0]}  Sym={ctrl[1]}({ctrl[2]})  abelian={ctrl[3]}")
    print(f"           B1297 sec4.2 records Tors H1(C_3) = (Z/4)^2 and |Sym| = 12+12 = 24")
torsion_ok = bool(ctrl) and ('Z/4 + Z/4' in ctrl[0])
order_ok   = bool(ctrl) and (ctrl[2] == 24)
alive      = bool(ctrl) and (ctrl[3] is False)      # must be NON-abelian: P inverts
print(f"  C-alive  (m004 C_3 non-abelian -> a lift inverts)   : {alive}")
print(f"  C-match  (torsion (Z/4)^2 as B1297 records)         : {torsion_ok}")
print(f"  C-match  (|Sym(C_3)| = 24 as B1297 records)         : {order_ok}")
alive = alive and torsion_ok and order_ok
if not alive:
    print("  VERDICT: VOID -- control failed, no conclusion admissible."); raise SystemExit(1)

unprot = [k for k,v in rows.items() if k!='m004' and v and v[7] and v[5]]
prot   = [k for k,v in rows.items() if k!='m004' and v and v[7] and not v[5]]
undet  = [k for k,v in rows.items() if k!='m004' and v and not v[7]]
print()
print(f"  UNPROTECTED (mechanism (ii) provably dead) : {unprot}")
print(f"  PROTECTED   (a lift inverts chi)           : {prot}")
print(f"  UNDETERMINED                               : {undet}")
print()
print("  CONSEQUENCE: B1331 computed L_V on s958; B1330's 952-sector scan was on v2873.")
print("  These have DIFFERENT protection status. Any reading of the two arcs together")
print("  must say which object it is talking about.")
raise SystemExit(0)
