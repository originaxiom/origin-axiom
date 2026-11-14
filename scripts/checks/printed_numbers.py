#!/usr/bin/env python3
"""Two transcripts of one computation, compared so that a number is compared as a number.

WHY (Review 80, 2026-11-12; main's word in its third folder for the builder, section 7).  Four locks compared, as text, a
float or a signed zero that a process printed: the residual of a check that is zero up to rounding ("at most 8.4e-16"), or
a zero with the sign its last operation left on it ("+1-0i").  Such digits differ between machines and between versions
of a library with nothing wrong, so the locks failed on a machine that had not made the kept transcript, and on main's
they passed and said nothing about the computation's own numbers.

THE RULE.  The two texts are the same where:
  - everything that is not a number is the same, character for character;
  - a zero carries no sign: "-0", "+0", "0" and "-0.00000000" are one number;
  - two numbers that are both smaller than SMALL in size are the same number, whatever their signs.  SMALL is 1e-9: a
    residual of a computation in double precision is of the order of 1e-16 times the size of what was computed, and the
    checks these locks run say themselves that anything near 1e-9 is a failure;
  - so the sign written directly before a zero, or before a number smaller than SMALL, is not compared: it is taken out;
  - any other two numbers agree to CLOSE of the larger, 1e-9: a float printed to its last digit, on two machines.
A whole number written as one is still compared: 3 and 4 differ, and so do 96 and 97.

What it does not do: it does not say that a number is RIGHT, only that two transcripts give the same one.  A residual of
1e-12 where the kept transcript has 1e-16 passes; whether that matters is for the script that prints it to check.

    from printed_numbers import same, differences
"""
import re

SMALL = 1e-9
CLOSE = 1e-9
# a number: digits with an optional point and exponent, not inside a word; an imaginary unit may follow it
_NUMBER = re.compile(r"(?<![A-Za-z_\d.])(?:\d+\.\d*|\.\d+|\d+)(?:[eE][-+]?\d+)?(?![A-Za-z_\d]|\.\d)"
                     r"|(?<![A-Za-z_\d.])(?:\d+\.\d*|\.\d+|\d+)(?:[eE][-+]?\d+)?(?=[ij](?![A-Za-z_\d]))")


def parts(text):
    """the text as a list of pieces, in order: ("text", str) and ("number", float).  The sign written directly before a
    number that is zero, or smaller than SMALL, is taken out of the text before it, so that it is not compared."""
    out, at = [], 0
    for m in _NUMBER.finditer(text):
        before, value = text[at:m.start()], float(m.group(0))
        if abs(value) < SMALL and before[-1:] in ("-", "+"):
            before = before[:-1]                                 # a sign stood here: whether one did, and which, is not compared
        out.append(("text", before))
        out.append(("number", value))
        at = m.end()
    out.append(("text", text[at:]))
    return out


def _same_number(a, b):
    if abs(a) < SMALL and abs(b) < SMALL:
        return True
    return abs(a - b) <= CLOSE * max(abs(a), abs(b))


def differences(got, kept, limit=5):
    """where two transcripts differ by the rule above, as short texts; an empty list where they are the same"""
    a, b = parts(got), parts(kept)
    out = []
    if len(a) != len(b):
        out.append("the two hold %d and %d numbers" % (len(a) // 2, len(b) // 2))
    for n, ((ka, va), (kb, vb)) in enumerate(zip(a, b)):
        if ka == "text" and va != vb:
            k = next((i for i, (x, y) in enumerate(zip(va, vb)) if x != y), min(len(va), len(vb)))
            out.append("the text differs: %r, kept %r" % (va[max(0, k - 30):k + 30], vb[max(0, k - 30):k + 30]))
        elif ka == "number" and not _same_number(va, vb):
            out.append("a number differs: %r, kept %r (after %r)" % (va, vb, a[n - 1][1][-40:]))
        if len(out) >= limit:
            break
    return out


def same(got, kept):
    return not differences(got, kept)
