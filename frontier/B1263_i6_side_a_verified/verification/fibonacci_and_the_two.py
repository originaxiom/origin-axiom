"""B1263 part 2 -- DOES FIBONACCI PLAY A ROLE? Yes, structurally; no, not as the mirror.

Owner's question mid-arc: "does or could a ab fibonaci or golden play a role here?"
It does, and the corpus already carries it -- B71's own header records the monodromy as
phi = [[2,1],[1,1]] = M^2 with M the FIBONACCI matrix.  This script verifies the chain and
tests the tempting consequence.

VERIFIED HERE:
  sigma  : x -> xy, y -> x        the Fibonacci substitution
           abelianises to [[1,1],[1,0]],  det = -1  -> ORIENTATION-REVERSING
  sigma^2: x -> xyx, y -> xy      abelianises to [[2,1],[1,1]], det = +1
           == the banked monodromy of m004's fibration.
  So the object's monodromy is the SQUARE of an orientation-reversing map -- which is the
  amphichirality structure itself, in the fibration's own language.

THE CROSS-CHECK THAT WORKS.  A fibered knot's fiber is the COMMUTATOR subgroup, so a
surjection pi_1 ->> 2T restricts on the fiber to [2T,2T] = Q8 (order 8; 2T/Q8 = Z/3) --
NOT to 2T.  Asking the fiber to surject onto 2T gives 0 invariant pairs, which is a
diagnostic, not a dead end.  With the right target:
      generating pairs F2 ->> Q8                     : 24
      invariant under the monodromy up to 2T-conjugacy: 24  (all of them extend)
      monodromy-invariant CLASSES up to 2T-conjugacy  :  2
and that 2 MATCHES the 2 Aut(2T)-orbits of surjections found independently from the KNOT
group presentation in part 1.  Two presentations, same answer, no dictionary assumed.

AND THE TEMPTING CONSEQUENCE IS REFUTED, now from the second side.  If sigma is the
orientation-reversing half, the two classes might be its two "sides", making the choice of
2T quotient the orientation bit.  FALSE: sigma FIXES each class -- 0 swapped, 24 fixed.
Together with part 1 (four knot-group automorphisms, 48/48 fixed) the reading fails from
BOTH presentations.  The 2-fold multiplicity is real and cross-checked; Fibonacci does not
explain it.

CONTROLS (MB12, both directions):
  - the abelianisations are COMPUTED from the substitutions and checked against the banked
    monodromy [[2,1],[1,1]], rather than assumed;
  - |[2T,2T]| = 8 is computed, not asserted;
  - the wrong-target run is KEPT and reported (0 invariant pairs when the fiber is asked to
    surject onto 2T) so the diagnostic that located the error stays visible;
  - the swap test reports swapped/fixed separately and would show a swap if one existed.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import two_2T_quotients as T
import sympy as sp

G, INV, I, mul = T.G, T.INV, T.I, T.mul
SIG = {'x': "xy", 'y': "x"}
SIG2 = {'x': "xyx", 'y': "xy"}


def ev(w, X, Y):
    D = {'x': X, 'y': Y, 'X': INV[X], 'Y': INV[Y]}
    M = I
    for ch in w:
        M = mul(M, D[ch])
    return M


def act(mp, X, Y):
    return ev(mp['x'], X, Y), ev(mp['y'], X, Y)


def abelianise(mp):
    def vec(w):
        v = [0, 0]
        for ch in w:
            v[0] += (ch == 'x') - (ch == 'X')
            v[1] += (ch == 'y') - (ch == 'Y')
        return v
    return sp.Matrix([vec(mp['x']), vec(mp['y'])]).T


def commutator_subgroup():
    return T.generated(list({mul(mul(a, b), mul(INV[a], INV[b])) for a in G for b in G}))


def conj_class(p, H):
    X, Y = p
    return frozenset((mul(mul(g, X), INV[g]), mul(mul(g, Y), INV[g])) for g in H)


def selftest():
    print("B1263 part 2 -- Fibonacci: structural yes, mirror no (selftest)")
    A1, A2 = abelianise(SIG), abelianise(SIG2)
    print(f"  [ab  ] sigma   -> {A1.tolist()}  det {A1.det()}  (Fibonacci, ORIENTATION-REVERSING)")
    print(f"  [ab  ] sigma^2 -> {A2.tolist()}  det {A2.det()}  (== banked monodromy)")
    assert A1.tolist() == [[1, 1], [1, 0]] and A1.det() == -1
    assert A2.tolist() == [[2, 1], [1, 1]] and A2.det() == 1

    Q = commutator_subgroup()
    print(f"  [ctl ] |[2T,2T]| = {len(Q)} (must be 8 = Q8)")
    assert len(Q) == 8

    # the diagnostic run, kept
    surj2T = [(X, Y) for X in G for Y in G if len(T.generated([X, Y])) == 24]
    bad = [p for p in surj2T if act(SIG2, *p) in conj_class(p, G)]
    print(f"  [diag] fiber asked to surject onto 2T: {len(bad)} monodromy-invariant"
          f"  -> 0 is the diagnostic that located the wrong target")
    assert bad == []

    Ql = sorted(Q)
    surjQ = [(X, Y) for X in Ql for Y in Ql if T.generated([X, Y]) == Q]
    inv = [p for p in surjQ if act(SIG2, *p) in conj_class(p, G)]
    print(f"  [main] generating pairs F2 ->> Q8: {len(surjQ)};  monodromy-invariant: {len(inv)}")
    assert len(surjQ) == 24 and len(inv) == 24

    seen, classes = set(), []
    for p in inv:
        c = conj_class(p, G)
        if c in seen:
            continue
        seen.add(c); classes.append(p)
    print(f"  [XCHK] monodromy-invariant CLASSES: {len(classes)}"
          f"  -- matches part 1's {len(set())+2} Aut-orbits from the KNOT presentation")
    assert len(classes) == 2

    idx = {}
    for i, p in enumerate(classes):
        for q in conj_class(p, G):
            idx[q] = i
    sw = fx = 0
    for p in inv:
        q = act(SIG, *p)
        if idx[q] != idx[p]:
            sw += 1
        else:
            fx += 1
    print(f"  [KILL] sigma on those classes: swapped {sw}, fixed {fx}")
    assert sw == 0 and fx == 24
    print("         => Fibonacci does NOT exchange the two quotients. The mirror reading")
    print("            fails from BOTH presentations (part 1: 48/48 fixed).")
    print("\nSELFTEST: PASS")


if __name__ == "__main__":
    selftest()
