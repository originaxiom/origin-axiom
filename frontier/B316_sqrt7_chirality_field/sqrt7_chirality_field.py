"""B316 -- H32 answered: does the object's arithmetic ladder extend past {sqrt-3, sqrt5} to Q(sqrt-7)? Run: python
(pyenv). The prediction from B234 (chat-2's trace-1 congruence law) was that -7 is "the next imaginary rung."

The metallic monodromy is unimodular (det = +/-1); a trace-t element has disc = t^2 - 4 det. On the IMAGINARY side
(disc < 0) the unimodular reachable discs are exactly:
    det=+1, t^2 < 4  ->  {-4 (t=0, Q(i), = RRLL),  -3 (t=1, Q(sqrt-3), = RL)}.
So the imaginary metallic ladder FLOORS at disc -4 (|disc| <= 4). These are the AMPHICHIRAL fields.

Q(sqrt-7) (disc -7):
  * PASSES the trace-1 congruence law: -7 == 1 (mod 4);
  * but is BELOW the unimodular imaginary floor (-7 < -4) -> UNREACHABLE by any unimodular monodromy.
  => permitted-by-congruence, forbidden-by-floor.

YET Q(sqrt-7) IS in the object's arithmetic (B147, verify-don't-trust confirmed): the CHIRAL pair RRL/RLL are
ARITHMETIC once-punctured-torus bundles with invariant trace field Q(sqrt-7) (a mirror pair; vol = 3 x the Bianchi
covolume of Q(sqrt-7)). The amphichiral bundles in range give RL -> Q(sqrt-3), RRLL -> Q(i).

VERDICT (H32): the metallic imaginary ladder {Q(sqrt-3), Q(i)} does NOT extend to Q(sqrt-7) -- disc -7 is below the
unimodular floor. Q(sqrt-7) is reached instead by BREAKING amphichirality (the non-palindromic RRL/RLL words, B147). So
sqrt-7 is the CHIRALITY field -- a third arithmetic at a DIFFERENT mechanism, not a monodromy-ladder rung. H32's
prediction (-7 appears in the object's data) is CONFIRMED, but the mechanism is chirality, not the ladder. The
two-ended {sqrt-3 Eisenstein, sqrt5 golden} arithmetic is amphichiral; sqrt-7 is chiral. FIREWALLED; nothing to CLAIMS.
"""


def metallic_disc(t, det):
    """disc of a trace-t, det-det unimodular element."""
    return t * t - 4 * det


def imaginary_unimodular_discs():
    """the imaginary-quadratic discs reachable by unimodular (det=+/-1) monodromy (the amphichiral floor)."""
    return sorted({metallic_disc(t, det) for det in (1, -1) for t in range(0, 4) if metallic_disc(t, det) < 0})


def neg7_passes_congruence():
    """the trace-1 congruence law: disc == 1 (mod 4)."""
    return (-7) % 4 == 1


def neg7_below_floor():
    """-7 is below the imaginary unimodular floor (min reachable disc = -4)."""
    return -7 < min(imaginary_unimodular_discs())


# --- the verdict facts ---
IMAGINARY_LADDER_FLOORS_AT_MINUS_4 = None      # set below: {-4 (Q(i)), -3 (Q(sqrt-3))}
NEG7_PERMITTED_BY_CONGRUENCE = True            # -7 == 1 mod 4
NEG7_UNREACHABLE_BY_MONODROMY = True           # below the unimodular floor
NEG7_IS_THE_CHIRALITY_FIELD = True             # RRL/RLL arithmetic chiral bundles, Q(sqrt-7) (B147)
LADDER_DOES_NOT_EXTEND_TO_NEG7 = True          # amphichiral ladder stops at {-3, -4}
NEG7_APPEARS_PREDICTION_CONFIRMED = True       # H32 said -7 appears -- it does, via chirality
DERIVES_SM_VALUES = False

IMAGINARY_LADDER_FLOORS_AT_MINUS_4 = (imaginary_unimodular_discs() == [-4, -3])


def verdict():
    return bool(
        IMAGINARY_LADDER_FLOORS_AT_MINUS_4
        and neg7_passes_congruence() and neg7_below_floor()
        and NEG7_PERMITTED_BY_CONGRUENCE and NEG7_UNREACHABLE_BY_MONODROMY
        and NEG7_IS_THE_CHIRALITY_FIELD and LADDER_DOES_NOT_EXTEND_TO_NEG7
        and NEG7_APPEARS_PREDICTION_CONFIRMED and not DERIVES_SM_VALUES
    )


if __name__ == "__main__":
    print("imaginary unimodular discs (amphichiral floor):", imaginary_unimodular_discs())
    print("Q(sqrt-7) disc -7: passes congruence (=1 mod 4):", neg7_passes_congruence(),
          "| below floor (unreachable by monodromy):", neg7_below_floor())
    print("Q(sqrt-7) is the chirality field (RRL/RLL, B147):", NEG7_IS_THE_CHIRALITY_FIELD)
    print("=> the ladder does NOT extend to -7; -7 is reached by breaking amphichirality (chirality), not the ladder.")
    print("verdict:", verdict())
