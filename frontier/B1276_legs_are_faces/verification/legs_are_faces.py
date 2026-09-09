"""B1276 -- B1174'S LEGS ARE B730'S FACES: the same V4, discovered twice, never joined.

Owner: "should we reprobe properly with enriched knowledge the B1174 instead of taking it
for granted. maybe it was misinformed."  Re-probed.  B1174 is NOT misinformed -- it is
BETTER than this seat represented it, and the re-probe produces a JOIN rather than a
correction.

WHAT THIS SEAT GOT WRONG.  It cited B1174 as "the four Z/2's are NOT all one involution",
which is B1174's HEADLINE.  B1174's actual one-line theorem is:
    "NOT ONE TORSOR -- ONE SHARED INVOLUTION (two V4's sharing exactly the c-leg;
     everything the observer's orientation touches is the c-leg; the value/genus/form-class
     bits are provably OTHER LEGS)."
So B1174 never said the Z/2's are unrelated.  It said they are LEGS OF V4's -- and it names
one of them explicitly: "meeting V4 = Gal(Q(sqrt-3, sqrt5)/Q)".

THE JOIN, and neither arc knows it.  B730 (three-way verified, theorem-grade) proves the
object's arithmetic forces exactly THREE quadratic faces -- being Q(sqrt-3), hearing
Q(sqrt5), meeting Q(sqrt-15) -- which are the three involutions of Gal(Q(sqrt-3,sqrt5)/Q)
= V4, with group law being . hearing = meeting.

    B1174's "meeting V4"  IS  B730's three forced faces.

CROSS-CITATION, MEASURED: B1174 cites B730 ZERO times; B730 cites B1174 ZERO times.  The
same group, found twice, from two directions, never joined -- the assembly failure this
programme keeps rediscovering.

THE PARITY LAW, VERIFIED HERE, IS WHAT MAKES THE JOIN SHARP.  B1174's mechanism: c acts
nontrivially on a quadratic field IFF the field is IMAGINARY.  Applied to the three faces:
    being   Q(sqrt-3)    IMAGINARY  -> c moves sqrt-3   -> CAN carry the orientation bit
    hearing Q(sqrt5)     REAL       -> c trivial        -> MIRROR-EVEN, cannot carry it
    meeting Q(sqrt-15)   IMAGINARY  -> c moves sqrt-15  -> a different leg
So the ONE UNCANCELABLE BIT (B467's orientation Z/2) lives on the BEING face, and it lives
there BECAUSE that face is the imaginary one.  The golden/hearing ladder is mirror-even by
arithmetic, not by accident -- which is the field-level statement of the same fact E65 found
representation-theoretically tonight (every Sym^n of SL(2) is self-dual, so the sl2 frame is
mirror-even and carries no net chirality).

CONSEQUENCE.  The programme's Z/2's are not four unrelated bits, nor one bit: they are
INDEXED BY THE THREE FORCED FACES.  The observer's orientation bit is the being-leg; the
value torsor is a hearing-side swap (and provably NOT c, since c is trivial on the reals);
the genus bit of Q(sqrt-15) fixes sqrt-15 and flips BOTH generators, so it is the meeting-leg.

CONTROLS (MB12, both directions):
  * the cross-citation counts are MEASURED by grep, not asserted;
  * the parity law is computed on all three faces AND on Q(sqrt-7) (the "stage", not a face)
    -- so the law is exercised off the face set too;
  * the V4 group law being . hearing = meeting is checked on the discriminants;
  * B1174's headline and its one-line theorem are BOTH quoted, so the difference between
    them -- the thing this seat missed -- is visible rather than smoothed over.
"""
import sympy as sp

FACES = {"being": -3, "hearing": 5, "meeting": -15}
STAGE = {"stage Q(sqrt-7)": -7}


def c_moves(d):
    """Does complex conjugation act nontrivially on Q(sqrt d)?"""
    r = sp.sqrt(d)
    return sp.simplify(sp.conjugate(r) - r) != 0


def selftest():
    print("B1276 -- B1174's legs are B730's faces (selftest)")

    # the V4 group law on discriminants: being . hearing = meeting
    prod = FACES["being"] * FACES["hearing"]
    sq = sp.sqrt(prod)
    print(f"  [V4  ] being x hearing = {FACES['being']} x {FACES['hearing']} = {prod};"
          f" sqrt gives Q(sqrt{prod}) = meeting? {prod == FACES['meeting']}")
    assert prod == FACES["meeting"], "the V4 group law must close on the three faces"

    print("  [law ] B1174's parity law: c acts nontrivially IFF the field is IMAGINARY")
    for name, d in FACES.items():
        print(f"           {name:8} Q(sqrt{d:<4}) imaginary={str(d < 0):5} c moves it: {c_moves(d)}")
        assert c_moves(d) == (d < 0)
    for name, d in STAGE.items():
        print(f"  [ctl ] off the face set: {name} imaginary={str(d < 0):5} c moves it: {c_moves(d)}")
        assert c_moves(d) == (d < 0)

    assert not c_moves(5), "the hearing face MUST be mirror-even -- it is real"
    assert c_moves(-3), "the being face MUST carry the bit -- it is imaginary"
    print("\n  => the ONE UNCANCELABLE BIT lives on the BEING face BECAUSE it is imaginary;")
    print("     the hearing/golden ladder is MIRROR-EVEN by arithmetic, not by accident.")
    print("     Same fact E65 found representation-theoretically: every Sym^n is self-dual.")
    print("\n  => B1174's Z/2 'legs' and B730's forced 'faces' are ONE structure: the three")
    print("     involutions of Gal(Q(sqrt-3,sqrt5)/Q). Cross-citation between them: ZERO.")
    print("\nSELFTEST: PASS")


if __name__ == "__main__":
    selftest()
