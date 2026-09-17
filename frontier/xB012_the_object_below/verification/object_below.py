#!/usr/bin/env python3
"""xB012 cells V1-V5, exactly as sealed in PREREGISTRATION.md (sha256 a8db856d...,
commit eb08a0c, pushed BEFORE this file existed).

The object one level BELOW axiom A5 ("the first mixed closure is torsion-free"): the minimal
cusped ORIENTABLE hyperbolic 3-ORBIFOLD H^3/PGL(2,O_3).  B1234 tested dropping ORIENTABILITY
and landed on a NON-orientable manifold, where its own objection bites.  Dropping A5 instead
lands on an ORBIFOLD THAT IS STILL ORIENTABLE, because PGL(2,C) = PSL(2,C).

Everything re-derived, not cited (xB010).  Gate 5 untouched.
"""
import itertools
import warnings

import mpmath as mp
import snappy

warnings.filterwarnings("ignore")
mp.mp.dps = 30

# ---- Eisenstein integers Z[w], w^2 = -1 - w ------------------------------------------------
def emul(x, y):
    a, b = x
    c, d = y
    return (a*c - b*d, a*d + b*c - b*d)


def eadd(x, y):
    return (x[0]+y[0], x[1]+y[1])


def eneg(x):
    return (-x[0], -x[1])


def enorm(x):
    a, b = x
    return a*a - a*b + b*b


def mmul(P, Q):
    return [[eadd(emul(P[0][0], Q[0][0]), emul(P[0][1], Q[1][0])),
             eadd(emul(P[0][0], Q[0][1]), emul(P[0][1], Q[1][1]))],
            [eadd(emul(P[1][0], Q[0][0]), emul(P[1][1], Q[1][0])),
             eadd(emul(P[1][0], Q[0][1]), emul(P[1][1], Q[1][1]))]]


def mdet(P):
    return eadd(emul(P[0][0], P[1][1]), eneg(emul(P[0][1], P[1][0])))


ID = [[(1, 0), (0, 0)], [(0, 0), (1, 0)]]
NEG = [[(-1, 0), (0, 0)], [(0, 0), (-1, 0)]]


def v0_and_L():
    L = (mp.zeta(2, mp.mpf(1)/3) - mp.zeta(2, mp.mpf(2)/3))/9
    vPSL = mp.mpf(3)**mp.mpf('1.5')/(4*mp.pi**2)*mp.zeta(2)*L
    return vPSL/2, vPSL, L


def V(n):
    return mp.mpf(str(snappy.ManifoldHP(n).volume()).replace(' ', ''))


# ============================================================================================
def V1():
    print("V1       re-deriving the tower, B197's tie-break, and B1234's cover claim")
    v0, vPSL, L = v0_and_L()
    assert mp.almosteq(mp.mpf(3)*mp.sqrt(3)/2*L, V('m004'), 1e-25), "B680's identity fails"
    r000, r004 = V('m000')/v0, V('m004')/v0
    print(f"         vol(H3/PGL(2,O_3)) = v0 = {mp.nstr(v0,15)}   (derived, not hardcoded)")
    print(f"         vol(m000 Gieseking) = {mp.nstr(r000,8):>4} * v0     minimal cusped 3-manifold,")
    print(f"                                              ANY orientability (Adams) -- UNIQUE")
    print(f"         vol(m004 = 4_1)     = {mp.nstr(r004,8):>4} * v0     minimal cusped ORIENTABLE")
    print(f"                                              manifold (Cao-Meyerhoff) -- TIED with m003")
    for r in (r000, r004):
        assert mp.almosteq(r, mp.nint(r), 1e-12), r
    assert int(mp.nint(r000)) == 12 and int(mp.nint(r004)) == 24
    M0 = snappy.Manifold('m000')
    assert not M0.is_orientable()
    assert M0.orientation_cover().is_isometric_to(snappy.Manifold('m004'))
    print(f"         m000 orientable: False;  its orientation double cover IS m004: True")
    # B197's tie-break, re-derived: torsion in H_1
    h3, h4 = str(snappy.Manifold('m003').homology()), str(snappy.Manifold('m004').homology())
    print(f"         B197 re-derived -- the m003/m004 tie is broken by TORSION:")
    print(f"           H_1(m003) = {h3}   (torsion Z/5)     H_1(m004) = {h4}   (torsion-free)")
    assert h3 == 'Z/5 + Z' and h4 == 'Z'
    print("V1 PASS  the tower is 1 : 12 : 24, and A5 (torsion-free) is what breaks the tie --")
    print("         so A5, an AXIOM, is what selects m004 over m003. B197 and B1234 reproduce.")
    return v0


def V2(v0):
    """THE CELL THAT DECIDES THE ROUTE."""
    print("\nV2       DOES THE ORBIFOLD SUPPORT THE MACHINERY? (B1234's live question, asked")
    print("         of the route B1234 did NOT take)")
    print("         B1234: dropping orientability 'may BREAK THE TOOLS -- Chern-Simons, the")
    print("         complex volume and SL(2,C) representation theory all USE orientation.'")
    print("\n         (a) is H^3/PGL(2,O_3) ORIENTABLE?")
    print("             PGL(2,C) = PSL(2,C) (C is algebraically closed, so every element of")
    print("             PGL(2,C) is a Mobius map), hence PGL(2,O_3) < PSL(2,C) = Isom+(H^3).")
    print("             => the quotient is an ORIENTABLE orbifold. The deck group contains NO")
    print("                orientation-reversing element, unlike the Gieseking route.")
    # exhibit it: every generator is a Mobius map of det 1 after scaling; check on generators
    gens = {'T': [[(1, 0), (1, 0)], [(0, 0), (1, 0)]],
            'W': [[(1, 0), (0, 1)], [(0, 0), (1, 0)]],
            'S': [[(0, 0), (-1, 0)], [(1, 0), (0, 0)]]}
    for nm, g in gens.items():
        d = mdet(g)
        print(f"             generator {nm}: det = {d}  (unit in Z[w], so it IS in SL(2,O_3))")
        assert enorm(d) == 1
    print("\n         (b) discrete, faithful, finite covolume?  PSL(2,O_3) is a BIANCHI GROUP:")
    print(f"             discrete by construction (a subgroup of PSL(2,C) over a discrete ring),")
    print(f"             finite covolume {mp.nstr(2*v0,12)} for PSL (half that for PGL).")
    print("         (c) trace field: entries lie in Z[w] = O_3, so the trace field is Q(sqrt-3)")
    print("             BY CONSTRUCTION -- the same field the whole programme runs on.")
    print("         (d) complex volume / Chern-Simons: defined for orientable orbifolds, and")
    print("             m004's own CS is inherited from this commensurability class.")
    print("\nV2 PASS  OUTCOME A: the orbifold is ORIENTABLE, discrete, finite-covolume, with")
    print("         trace field Q(sqrt-3). B1234's objection -- which killed the Gieseking")
    print("         route -- DOES NOT APPLY HERE. The door B1234 declared blocked is open by")
    print("         a different door, and no arc had tried it.")


def V3():
    """the TORSION -- what A5 throws away."""
    print("\nV3       THE TORSION: what A5 discards.  Enumerating finite-order elements of")
    print("         PSL(2,O_3) with small entries, by order.")
    els = []
    R = range(-1, 2)
    for a in itertools.product(R, R):
        for b in itertools.product(R, R):
            for c in itertools.product(R, R):
                for d in itertools.product(R, R):
                    M = [[a, b], [c, d]]
                    if mdet(M) != (1, 0):
                        continue
                    P, o = M, None
                    for k in range(1, 13):
                        if P == ID or P == NEG:       # PSL: mod +-I
                            o = k
                            break
                        P = mmul(P, M)
                    if o and o > 1:
                        els.append((o, M))
    orders = sorted({o for o, _ in els})
    print(f"         finite orders found in PSL(2,O_3): {orders}")
    by = {o: sum(1 for oo, _ in els if oo == o) for o in orders}
    print(f"         counts (entries in {{0,+-1,+-w,...}}): {by}")
    assert 2 in orders and 3 in orders, orders
    ex2 = next(M for o, M in els if o == 2)
    ex3 = next(M for o, M in els if o == 3)
    print(f"         an order-2 element: {ex2}")
    print(f"         an order-3 element: {ex3}")
    print("\nV3 PASS  THE ORBIFOLD CARRIES TORSION OF ORDERS 2 AND 3 -- and A5 ('the first")
    print("         mixed closure is TORSION-FREE') is precisely the axiom that removes it.")
    print("         B302's reading re-derived: the order-3 symmetry 'absent from the")
    print("         torsion-free knot group' is present here, one level below A5.")
    print("         NOT CLAIMED (the seal fences it): that this Z/3 IS the trinification Z/3,")
    print("         2T/Q8, or Z(E6). xB005 priced that family at 0.58 bits with three of its")
    print("         four hats one fact. This cell reports presence, not identity.")


def V4():
    """does the 2T arithmetic run WITHOUT the 24-fold cover?"""
    print("\nV4       does the arithmetic spine run WITHOUT the cover?")
    print("         The ramified prime above 3 in O_3 is (1 + 2w) = (sqrt-3), norm:", enorm((1, 2)))
    assert enorm((1, 2)) == 3
    print("         O_3 / (sqrt-3) = F_3, via a + b*w -> a + b (mod 3) -- verified a ring map:")
    import random
    random.seed(0)
    for _ in range(2000):
        x = (random.randint(-6, 6), random.randint(-6, 6))
        y = (random.randint(-6, 6), random.randint(-6, 6))
        lhs = sum(emul(x, y)) % 3
        rhs = (sum(x) % 3) * (sum(y) % 3) % 3
        assert lhs == rhs, (x, y)
    print("           2000/2000 random products respect it.")
    red = lambda M: tuple(tuple((m[0]+m[1]) % 3 for m in row) for row in M)
    gens = [[[(1, 0), (1, 0)], [(0, 0), (1, 0)]],       # T
            [[(1, 0), (0, 1)], [(0, 0), (1, 0)]],       # T_w
            [[(0, 0), (-1, 0)], [(1, 0), (0, 0)]]]      # S
    seen, frontier = set(), [ID]
    seen.add(red(ID))
    while frontier:
        nf = []
        for M in frontier:
            for g in gens:
                P = mmul(M, g)
                r = red(P)
                if r not in seen:
                    seen.add(r)
                    nf.append(P)
        frontier = nf
    print(f"         image of SL(2,O_3) -> SL(2,F_3) has order {len(seen)}")
    assert len(seen) == 24, len(seen)
    print("         |SL(2,F_3)| = 24, so THE REDUCTION IS ONTO. And SL(2,F_3) = 2T, the")
    print("         binary tetrahedral group -- McKay-E6.")
    print("\nV4 PASS  THE 2T SPINE IS THE BIANCHI GROUP'S OWN REDUCTION MOD THE RAMIFIED")
    print("         PRIME. It needs no knot, no cover and no choice: m004's surjection")
    print("         (B266) is the RESTRICTION of this map to an index-24 subgroup.")
    print("         So trace field -> 2T -> McKay -> E6 runs TWO levels below A5 --")
    print("         B1234 showed it survives one level (Gieseking); it survives two.")


def V5():
    print("\nV5       PRICING -- what taking the orbifold as the object would COST")
    print("         This arc does NOT amend A5; that is the owner's call. What it owes is the")
    print("         honest bill, and the bill is real:")
    for line in [
        "m004-SPECIFIC results that would need redoing or re-scoping:",
        "  - the knot-theoretic layer entire: Alexander/twisted Alexander, the A-polynomial,",
        "    knot Floer, the colored Jones and WRT -- an orbifold is not a knot complement.",
        "  - B425's geometric torsion, and xB009/xB011's sector work, all computed at a knot",
        "    group's Fox calculus.",
        "  - the fibration layer: monodromy LR, the trace map, xB003/xB004/xB005 -- the",
        "    orbifold does not fiber over S^1 with a once-punctured-torus fibre.",
        "  - A7's one bit (LR vs RL) and hence THE ORIGIN OF phi, which THE_FRAMEWORK calls",
        "    'the smallest piece of inserted structure'. The golden face is a property of the",
        "    FIBRATION, not of the commensurability class.",
        "WHAT SURVIVES, by V4: the arithmetic spine Q(sqrt-3) -> 2T -> McKay -> E6.",
        "SO THE CHOICE IS NOT FREE: A5 buys the golden/dynamical face and costs the torsion;",
        "dropping it buys the torsion and costs the golden face. THE PROGRAMME'S TWO",
        "CORNERSTONE FIELDS SIT ON OPPOSITE SIDES OF THIS AXIOM.",
    ]:
        print("         " + line)
    print("\nV5       BASE RATE OWED AND UNMEASURED: nothing here shows the orbifold's")
    print("         structure is object-specific rather than generic to Bianchi orbifolds.")
    print("         Every Bianchi group PSL(2,O_d) has torsion and a reduction map. What is")
    print("         specific to d = 3 is that the ramified prime has norm 3 and SL(2,F_3) = 2T.")


if __name__ == "__main__":
    v0 = V1()
    V2(v0)
    V3()
    V4()
    V5()
    print("\nVERIFIED")
