"""B1263 -- I-6's side A VERIFIED, its multiplicity MEASURED, and a tempting reading REFUTED.

B1261 made the identification ledger the scoreboard (price = 4 axioms + UNEARNED rows), and
B1262 moved it 15 -> 14 by running a discriminator a row had carried unrun.  This arc audits
the next candidate, I-6 ("pi_1(m004) ->> 2T  =  the 6d type's ALE Gamma"), whose SIDE A is a
finite, decidable group-theoretic claim that had never been checked.

(1) SIDE A IS REAL.  Enumerating all 24^2 = 576 pairs in 2T = SL(2,3) and imposing the
    relator abABaBAbaB = I: there are 72 homomorphisms pi_1(m004) -> 2T, of which 48 are
    SURJECTIVE.  So the object really does have 2T quotients; the row is NOT refutable on
    side A, and it stays UNEARNED.  Price unchanged at 14.

(2) BUT "THE 2T" IS NOT WELL DEFINED.  Those 48 surjections fall into 4 orbits under inner
    automorphisms and exactly 2 orbits under the full Aut(2T) = S4 (|Aut| = 24, verified by
    construction).  The object supplies TWO genuinely distinct 2T quotients, never one.
    That is the H5 pattern -- every space, never a point -- at a SIXTH level, after the
    closing (C22), the order (A7), the partner (B1192), the sl2 embedding (I-25) and n
    (B1248).  It also SHARPENS I-6's price: earning it needs not merely a map to the
    transverse ALE Gamma but a statement of WHICH of the two quotients is meant, or a proof
    that the map is independent of the choice.

(3) A TEMPTING READING, TESTED AND REFUTED.  Two quotients invites the reading that they are
    mirror images, so that choosing one IS the orientation bit -- which would tie I-6
    directly to the chirality story.  FALSE: four relator-preserving automorphisms of pi_1
    (a<->b; a,b -> a^-1,b^-1; the composite; and the inner-flavoured a -> a, b -> aba^-1)
    each map surjections to surjections and every one FIXES both Aut-orbits, 48/48.  No
    tested symmetry exchanges the two quotients, so the choice between them is a genuine
    binary with no symmetry reason to prefer either, and it is NOT the orientation bit.

CONTROLS (MB12, both directions):
  - the group is validated: |SL(2,3)| = 24 checked, and |Aut(2T)| = 24 is CONSTRUCTED (by
    extending generator images and rejecting non-bijections) rather than assumed;
  - the orbit count can come out otherwise: inner automorphisms give 4 orbits while the full
    Aut gives 2, so the counting is sensitive to which group acts and is not a fixed point
    of the method;
  - the symmetry test can detect a swap: it reports swapped/fixed counts per automorphism,
    and a map that failed to preserve the relator would be reported as such rather than
    silently counted.
"""
import itertools

P = 3
I = (1, 0, 0, 1)
REL = "abABaBAbaB"


def mul(X, Y):
    return ((X[0]*Y[0] + X[1]*Y[2]) % P, (X[0]*Y[1] + X[1]*Y[3]) % P,
            (X[2]*Y[0] + X[3]*Y[2]) % P, (X[2]*Y[1] + X[3]*Y[3]) % P)


def group():
    G = [X for X in itertools.product(range(P), repeat=4)
         if (X[0]*X[3] - X[1]*X[2]) % P == 1]
    return G, {X: next(Y for Y in G if mul(X, Y) == I) for X in G}


G, INV = group()


def word(w, A, B):
    D = {'a': A, 'b': B, 'A': INV[A], 'B': INV[B]}
    M = I
    for ch in w:
        M = mul(M, D[ch])
    return M


def generated(gens):
    S, fr = {I}, [I]
    while fr:
        x = fr.pop()
        for g in gens:
            y = mul(x, g)
            if y not in S:
                S.add(y); fr.append(y)
    return S


def surjections():
    return [(A, B) for A in G for B in G
            if word(REL, A, B) == I and len(generated([A, B])) == 24]


def automorphisms(g0, g1):
    out = []
    for imA in G:
        for imB in G:
            m, fr, ok = {I: I}, [(I, I)], True
            for x, y in iter(lambda: fr.pop() if fr else None, None):
                for g, h in ((g0, imA), (g1, imB)):
                    xg, yh = mul(x, g), mul(y, h)
                    if xg in m:
                        if m[xg] != yh:
                            ok = False; break
                    else:
                        m[xg] = yh; fr.append((xg, yh))
                if not ok:
                    break
            if ok and len(m) == 24 and len(set(m.values())) == 24:
                out.append(m)
    return out


def selftest():
    print("B1263 -- I-6's side A verified, its multiplicity measured (selftest)")
    print(f"  [ctl ] |SL(2,3)| = {len(G)} (must be 24)")
    assert len(G) == 24

    homs = [(A, B) for A in G for B in G if word(REL, A, B) == I]
    S = surjections()
    print(f"  [A   ] homomorphisms pi_1(m004) -> 2T: {len(homs)} of {24*24};"
          f"  SURJECTIVE: {len(S)}")
    assert len(S) == 48, len(S)
    print("         => SIDE A IS REAL; I-6 is not refutable there and stays UNEARNED")

    auts = automorphisms(*S[0])
    print(f"  [ctl ] |Aut(2T)| constructed = {len(auts)} (must be 24 = S4)")
    assert len(auts) == 24

    def orbits(acts):
        seen, n = set(), 0
        for A, B in S:
            if (A, B) in seen:
                continue
            n += 1
            for h in acts:
                seen.add((h[A], h[B]) if isinstance(h, dict)
                         else (mul(mul(h, A), INV[h]), mul(mul(h, B), INV[h])))
        return n
    inner = orbits(G)
    full = orbits(auts)
    print(f"  [mult] orbits under inner automorphisms: {inner};  under full Aut(2T): {full}")
    assert (inner, full) == (4, 2)
    print(f"         => the object supplies {full} distinct 2T quotients, NEVER one")

    # the tempting reading, tested
    cands = {"swap a<->b": {'a': "b", 'b': "a"},
             "invert a,b": {'a': "A", 'b': "B"},
             "swap+invert": {'a': "B", 'b': "A"},
             "a->a, b->aba^-1": {'a': "a", 'b': "abA"}}
    lab, seen = {}, 0
    for A, B in S:
        if (A, B) in lab:
            continue
        for h in auts:
            lab[(h[A], h[B])] = seen
        seen += 1
    any_swap = False
    for nm, mp in cands.items():
        sw = fx = 0
        for (A, B) in S:
            D = {'a': A, 'b': B, 'A': INV[A], 'B': INV[B]}
            def ev(w):
                M = I
                for ch in w:
                    M = mul(M, D[ch])
                return M
            A2, B2 = ev(mp['a']), ev(mp['b'])
            assert word(REL, A2, B2) == I and len(generated([A2, B2])) == 24, nm
            if lab[(A2, B2)] != lab[(A, B)]:
                sw += 1
            else:
                fx += 1
        any_swap = any_swap or sw > 0
        print(f"  [mirr] {nm:18} swapped {sw:3}, fixed {fx:3}")
    print(f"  [KILL] any tested symmetry exchanges the two quotients? {any_swap}")
    assert not any_swap
    print("         => the two quotients are NOT mirror-paired; choosing between them is a")
    print("            genuine binary and is NOT the orientation bit. Reading refuted.")
    print("\nSELFTEST: PASS")


if __name__ == "__main__":
    selftest()
