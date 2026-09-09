"""B1273 -- THE SEAT HARVEST: three independent routes separate the SAME binary, and the
central twist is reproduced on main's own data.

Owner: "lets integrate/digest verify work from all other seats, and reflect the new state
to the rest of repo."  Harvested, NOT merged (the standing integrate-don't-merge rule);
only what could be verified on main's data is asserted here.

THE CONVERGENCE ON I-6's BINARY.  Three routes, three seats, one structure:
  main   (B1263)   pi_1(m004) has 48 surjections onto 2T in exactly 2 Aut(2T)-orbits.
  owner  (Round 11) the orbits are separated by MERIDIAN ORDER: reduction mod (1-omega)
                   gives 3, the (0,0,0) quaternionic character gives 6; invariant triples
                   (3,6,4) and (6,6,4).  VERIFIED at B1272, including that the banked
                   holonomy reduced mod (1-omega) is surjective and lands in the order-3 class.
  codex  (R037)    "m000 and m004 each have 48 surjections = two Aut(2T) orbits" -- the same
                   count, independently; "exactly one of m004's two 2T quotient classes
                   extends over m000"; "the nonextendable class is the unique central H^1
                   twist of the extendable class".

VERIFIED HERE of codex R037, on main's enumeration:
  * Z(2T) has order 2 (codex: "center C2") -- computed;
  * H^1(m004; Z/2) = Hom(pi_1, Z/2) = Z/2 since H_1 = Z, and BOTH generators are meridians,
    so the unique nontrivial central twist negates BOTH;
  * under that twist ALL 48 surjections move to the OTHER orbit (48 moved, 0 fixed, 0
    invalid), carrying (3,6,4) -> (6,6,4).
  So codex's "central H^1 twist" relation is REPRODUCED exactly, and it is the SAME pairing
  the owner's meridian-order separator sees: negating by -I is what turns order 3 into 6.

A FIRST ATTEMPT AT THIS FAILED AND IS KEPT: twisting only ONE generator gives 0 valid
quotients, because the character must be a HOMOMORPHISM and both meridians generate H_1.
The seat printed a conclusion the data did not support and withdrew it; the control here
asserts the twist is valid (invalid == 0) before the orbit counts are read.

WHAT IS HARVESTED BUT NOT VERIFIED HERE (recorded with its own scope, not adopted):
  codex R037  the m000 EXTENSION half needs the covering inclusion pi_1(m004) < pi_1(m000);
              m000 is the Gieseking manifold, NON-orientable, and m004 is its orientation
              double cover (SnapPy 3.3.2: m000 = <a,b | aabbAB>, vol 1.0149; m004 orientable,
              vol 2.0299).  So codex's selector is an ORIENTATION selector.  Whether the
              GEOMETRIC class is the EXTENDABLE one is the open join of the two separators.
  codex R039  each m004 A4-map has two 2T lifts, exactly one extending over m000.
  codex R038  27 -> 10_2 + 5_-4 + 5bar_-6 + 5bar_4 + 1_0 + 1_10 under an SU(6)->SU(5) VEV,
              with its own NEGATIVE: one decomposable VEV is not D-flat.
  codex R040  all 1260 cusped nonorientable census orientation covers are CS-zero.
  SM-derivation seat  h1(M;27) = 3 = h1(M;27bar) EXACTLY over Q(omega) -- independently
              confirming B1267's numerically-obtained index 0; and a three-generation
              mechanism from E8 > E6 x SU(3).  The BRANCHING is verified here
              (248 = 78+8+(27,3)+(27bar,3bar); 240-72-6 = 162 = 6x27) and is standard; the
              object-specific claim (that the object's OWN order-3 element realises the
              family SU(3)) is NOT verified here, and that seat reports the Yukawa forces
              ZERO on the triplet.
  physics-seat  138 commits, Rounds 1-12; Round 12 already folded main @ 0ecd9557.

CONTROLS (MB12, both directions):
  * the centre is computed, not assumed;
  * the twist is checked to produce VALID quotients (invalid == 0) before orbits are counted
    -- the check that caught the one-generator error;
  * the twist must move EVERY surjection (48/48): a partial move would mean it is not the
    class-swapping H^1 character.
"""
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.normpath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(REPO, "frontier", "B1263_i6_side_a_verified", "verification"))
import two_2T_quotients as T

G, INV, I, mul = T.G, T.INV, T.I, T.mul


def order(X):
    n, M = 1, X
    while M != I:
        M = mul(M, X); n += 1
    return n


def ev(w, A, B):
    D = {'a': A, 'b': B, 'A': INV[A], 'B': INV[B]}
    M = I
    for c in w:
        M = mul(M, D[c])
    return M


def centre():
    return [g for g in G if all(mul(g, x) == mul(x, g) for x in G)]


def orbits():
    S = T.surjections()
    auts = T.automorphisms(*S[0])
    lab, k = {}, 0
    for p in S:
        if p in lab:
            continue
        for h in auts:
            lab[(h[p[0]], h[p[1]])] = k
        k += 1
    return S, lab, k


def selftest():
    print("B1273 -- the seat harvest: three routes, one binary (selftest)")
    Z = centre()
    print(f"  [ctl ] |Z(2T)| = {len(Z)}  (codex R037: 'center C2')")
    assert len(Z) == 2
    minus = [z for z in Z if z != I][0]

    S, lab, k = orbits()
    print(f"  [main] {len(S)} surjections, {k} Aut(2T)-orbits  (codex R037 independently: 48, two)")
    assert (len(S), k) == (48, 2)

    moved = same = invalid = 0
    for (A, B) in S:
        p2 = (mul(A, minus), mul(B, minus))
        if p2 not in lab:
            invalid += 1
            continue
        if lab[p2] != lab[(A, B)]:
            moved += 1
        else:
            same += 1
    print(f"  [ctl ] central H^1 twist yields VALID quotients: invalid = {invalid} (must be 0)")
    assert invalid == 0, "the twist must be a homomorphism -- twisting ONE generator fails here"
    print(f"  [R037] under the twist: moved {moved}, fixed {same}  (must be 48 / 0)")
    assert (moved, same) == (48, 0)

    ex = [p for p in S if lab[p] == 1][0]
    tw = (mul(ex[0], minus), mul(ex[1], minus))
    t1 = (order(ex[0]), order(mul(*ex)), order(ev("abAB", *ex)))
    t2 = (order(tw[0]), order(mul(*tw)), order(ev("abAB", *tw)))
    print(f"  [conv] {t1} --central twist--> {t2}")
    assert t1 == (3, 6, 4) and t2 == (6, 6, 4)

    print("\n  => codex R037's central-H^1-twist relation is REPRODUCED on main's data, and it")
    print("     is the SAME pairing the owner's meridian-order separator sees. Three routes,")
    print("     three seats, one binary. The open join: is the GEOMETRIC class the EXTENDABLE one?")
    print("\nSELFTEST: PASS")


if __name__ == "__main__":
    selftest()
