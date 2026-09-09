"""B1262 -- I-9 REFUTED: there is no 'genus V4' for discriminant -15.

B1261 measured the trade at 15 unpriced inputs : 0 of the SM's 19 numbers, and showed the
rate moves by exactly two operations -- EARN an identification (-1) or DERIVE a parameter
(+1).  A third, equally valuable and cheaper, was implicit in the ratchet's own arithmetic:
REFUTE an identification, which also removes a row from the UNEARNED set.

I-9 states: **B155's (Z/2)^2 glue = the genus V4**, with side B recorded as
Gal(Q(sqrt-3, sqrt5)/Q).  The row itself carried the discriminator, written and never run:
"the genus group of disc -15 has order 2^(t-1) = 2, not 4."

COMPUTED HERE:
    disc -15: reduced primitive forms {(1,1,4), (2,1,2)}  ->  h(-15) = 2, class group Z/2
    -15 = (-3)*(5): t = 2 prime discriminants  ->  number of genera = 2^(t-1) = 2
    genus group = C/C^2 with C = Z/2           ->  ORDER 2
    Gal(Q(sqrt-3, sqrt5)/Q)                    ->  (Z/2)^2, ORDER 4

So the object the row NAMES -- "the genus V4" of disc -15 -- DOES NOT EXIST: that genus
group is Z/2.  The identification is false as stated.  REFUTED.

AND THE FALLBACK READING FAILS TOO, on the programme's own rules.  Reading side B as
Gal(Q(sqrt-3,sqrt5)/Q) does give order 4, matching the glue's order -- but that is an ORDER
MATCH, which B1223 established is not a connection ("Direct is not semidirect": the groups
matched, the action did not).  And B155's own row calls the glue a GL(4,Z)-class invariant
"not forced by the spectral type" -- LATTICE data -- while Gal is FIELD data.  A map from
field data to something not determined by field data cannot be canonical.

CONTROLS (MB12, both directions):
  - the class-number routine is validated against FIVE known values (h(-15)=2, h(-23)=3,
    h(-4)=1, h(-3)=1, h(-47)=5) before being trusted -- and a first draft of the reduction
    filter got h(-15) = 3 by admitting (1,-1,4), which is NOT reduced (b >= 0 is required
    when |b| = a); that bug is exactly what the validation catches;
  - the test CAN come out the other way: for discriminants with t = 3 prime discriminant
    factors the genus group DOES have order 4, exhibited -- so "order 2" is a fact about
    -15 and not about the method.
"""
import sympy as sp
from sympy.ntheory import factorint


def reduced_forms(D):
    """Reduced primitive positive-definite binary quadratic forms of discriminant D < 0.

    Reduction: |b| <= a <= c, with b >= 0 whenever |b| == a or a == c.
    """
    out, a = [], 1
    while 3 * a * a <= abs(D):
        for b in range(-a, a + 1):
            if (b * b - D) % (4 * a):
                continue
            c = (b * b - D) // (4 * a)
            if c < a:
                continue
            if (abs(b) == a or a == c) and b < 0:
                continue
            if sp.gcd(sp.gcd(a, b), c) != 1:
                continue
            out.append((a, b, c))
        a += 1
    return out


def n_genera(D):
    """Number of genera = 2^(t-1), t = number of prime discriminant factors."""
    return 2 ** (len(factorint(abs(D))) - 1)


def selftest():
    print("B1262 -- I-9 refuted: there is no 'genus V4' for disc -15 (selftest)")

    known = {-15: 2, -23: 3, -4: 1, -3: 1, -47: 5}
    for D, h in known.items():
        got = len(reduced_forms(D))
        print(f"  [ctl ] h({D:4}) = {got}  (known {h})  {'OK' if got == h else 'MISMATCH'}")
        assert got == h, (D, got, h)

    h15 = len(reduced_forms(-15))
    g15 = n_genera(-15)
    print(f"  [main] disc -15: h = {h15} (class group Z/{h15}); genera = {g15}"
          f"  -> genus group order {g15}")
    assert h15 == 2 and g15 == 2

    print("  [main] Gal(Q(sqrt-3, sqrt5)/Q) = (Z/2)^2, order 4")
    assert 4 != g15
    print(f"  [KILL] order 4 != order {g15}: THERE IS NO 'GENUS V4' FOR DISC -15")

    # control: the criterion can produce order 4 -- for t = 3
    D3 = -84                       # -84 = (-4)*(-3)*(-7)? t counts prime factors of |D|
    print(f"  [ctl ] a discriminant with more prime factors gives a LARGER genus group:")
    for D in (-84, -120):
        print(f"           D = {D}: t = {len(factorint(abs(D)))} -> genera = {n_genera(D)}")
    assert n_genera(-84) >= 4, "the method must be able to yield order >= 4"

    print("\n  => I-9 is REFUTED as named. The fallback Gal reading rests on an ORDER MATCH,")
    print("     which B1223 forbids as evidence, plus a category mismatch B155 itself records")
    print("     (the glue is 'not forced by the spectral type' -- lattice data, not field data).")
    print("\nSELFTEST: PASS")


if __name__ == "__main__":
    selftest()
