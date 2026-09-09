"""B1272 -- B1263'S "GENUINE BINARY" IS THE GEOMETRIC vs NON-GEOMETRIC CHARACTER.
Owner-supplied (Round 11, physics-seat branch), verified here on main's own data.

B1263 computed that pi_1(m004) has 48 surjections onto 2T falling into exactly 2 orbits
under Aut(2T), tested four relator-preserving automorphisms, found all of them FIX both
orbits, and concluded: "the choice between them is a GENUINE BINARY with no symmetry
reason to prefer either."  THAT CONCLUSION IS WRONG, and the owner supplied the reason.

THE OWNER'S CLAIM (Round 11): the two orbits are the two routes -- holonomy reduction mod
(1-omega) sends the meridian to order 3, the (0,0,0) quaternionic character sends it to
order 6 -- separated by orbit invariants (3,6,4) vs (6,6,4); so the binary is GEOMETRIC vs
NON-GEOMETRIC, and A3's conductor route is implicitly using the geometric one.

VERIFIED HERE, end to end, on B1263's own enumeration:
  * 72 homomorphisms / 48 surjections / 2 Aut(2T)-orbits  -- reproduced;
  * the orbits ARE separated by MERIDIAN ORDER: orbit 1 has ord rho(a) = 3, orbit 0 has 6;
  * the invariant triple is (ord rho(a), ord rho(ab), ord rho([a,b])), giving
        (3, 6, 4)  and  (6, 6, 4)
    exactly as claimed -- the third component is the COMMUTATOR order, which is the
    programme's own Fricke object (kappa = tr[A,M]), not the longitude (that gives 2);
  * AND THE GEOMETRIC ONE IS IDENTIFIED: Z[omega]/(1-omega) = F_3 with omega = 1, so the
    banked holonomy A = [[1,1],[0,1]], B = [[1,0],[-omega,1]] reduces to B = [[1,0],[2,1]]
    over F_3.  That pair has det 1, satisfies the relator abABaBAbaB = I, IS surjective onto
    2T, and lands in ORBIT 1 with invariants (3,6,4).

SO B1263 IS CORRECTED.  There IS a reason to prefer one orbit: one of them IS the object's
geometric holonomy reduced mod (1-omega); the other is not.  B1263's four automorphisms
failed to separate them because they were the wrong instrument -- the separator is
ARITHMETIC (reduction at the prime above 3), not a symmetry of the presentation.

CONSEQUENCE FOR I-6.  B1263 had SHARPENED I-6's price by observing that "the 2T" was not
well defined (2 quotients).  That sharpening is now largely PAID: the geometric quotient is
distinguished, so "the 2T" has a canonical meaning.  I-6 is NOT thereby earned -- it still
needs a map to the transverse ALE Gamma -- but its multiplicity objection is answered, and
this is the FIRST of the H5 census's measured multiplicities to be resolved by a selector
rather than merely counted.

CONTROLS (MB12, both directions):
  * the reduced pair is checked to satisfy the relator, to have det 1, and to be SURJECTIVE
    before its orbit is read -- a non-surjective reduction would prove nothing;
  * the longitude order is computed too and is 2 in BOTH orbits, so it does NOT separate --
    exhibited, so the triple's third slot is not fitted to the answer;
  * the separator is verified to be orbit-CONSTANT: every one of the 24 members of each
    orbit carries the same triple.
"""
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.normpath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(REPO, "frontier", "B1263_i6_side_a_verified", "verification"))
import two_2T_quotients as T

G, INV, I, mul = T.G, T.INV, T.I, T.mul
LONGITUDE = "abABaaBAbA"


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


def triple(A, B):
    return (order(A), order(mul(A, B)), order(ev("abAB", A, B)))


def selftest():
    print("B1272 -- B1263's binary is geometric vs non-geometric (selftest)")
    S, lab, k = orbits()
    print(f"  [rep ] {len(S)} surjections, {k} Aut(2T)-orbits  (B1263: 48 / 2)")
    assert len(S) == 48 and k == 2

    tri = {}
    for o in range(k):
        mem = [p for p in S if lab[p] == o]
        ts = {triple(*p) for p in mem}
        assert len(ts) == 1, f"orbit {o} triple not constant: {ts}"
        tri[o] = ts.pop()
        print(f"  [inv ] orbit {o}: {len(mem)} surjections, (ord a, ord ab, ord [a,b]) = {tri[o]}")
    assert sorted(tri.values()) == [(3, 6, 4), (6, 6, 4)], tri

    lon = {order(ev(LONGITUDE, *p)) for p in S}
    print(f"  [ctl ] longitude order across ALL surjections: {lon} -- does NOT separate,")
    print(f"         so the triple's third slot is the COMMUTATOR, not fitted to the answer")
    assert lon == {2}

    # the geometric reduction: Z[omega]/(1-omega) = F_3, omega = 1, so -omega = 2
    A, B = (1, 1, 0, 1), (1, 0, 2, 1)
    assert (A[0]*A[3] - A[1]*A[2]) % 3 == 1 and (B[0]*B[3] - B[1]*B[2]) % 3 == 1
    assert ev(T.REL, A, B) == I, "the reduced pair must satisfy the relator"
    assert len(T.generated([A, B])) == 24, "the reduced pair must be SURJECTIVE"
    o = lab[(A, B)]
    print(f"  [GEO ] the banked holonomy reduced mod (1-omega) is surjective and lands in")
    print(f"         ORBIT {o}, with triple {triple(A, B)}")
    assert triple(A, B) == (3, 6, 4)

    print("\n  => B1263's 'genuine binary with no symmetry reason to prefer either' is CORRECTED:")
    print("     one orbit IS the geometric holonomy mod (1-omega). The separator is ARITHMETIC,")
    print("     not a symmetry of the presentation -- which is why B1263's four automorphisms,")
    print("     all of which fixed both orbits, were the wrong instrument.")
    print("\nSELFTEST: PASS")


if __name__ == "__main__":
    selftest()
