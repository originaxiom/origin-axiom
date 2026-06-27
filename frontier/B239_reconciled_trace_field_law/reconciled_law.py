"""B239 -- the RECONCILED unimodular trace-field law (referee-proof), reconciling the unit-determinant
closure (B234/B235) and the trace-parity framing into one stronger statement. From chat2's correctness
catch. Nothing to CLAIMS.md.

THE FRAGILE VERSION (superseded): "trace-1, disc = 1-4*det". A referee computes the actual monodromy
RL = [[2,1],[1,1]] and finds trace 3, NOT 1 -> thinks the law is wrong. "Trace 1" was only a representative
(the homological monodromy M_1=[[1,1],[1,0]] has trace 1; the bundle monodromy RL has trace 3).

THE ROBUST LAW (B239): the object's holonomy/monodromy elements are UNIMODULAR (det = +-1). For a 2x2
unimodular integer matrix with trace t, char poly x^2 - t x + det, discriminant disc = t^2 - 4*det.
  (1) sqrt5 is ROBUST: both RL (trace 3, det +1 -> disc 5) and M_1 (trace 1, det -1 -> disc 5) give Q(sqrt5).
  (2) THE ONLY imaginary quadratic trace fields a unimodular element can have are Q(i) and Q(sqrt-3):
      disc < 0 forces det = +1 and |t| <= 1, so disc in {-4 (t=0 -> Q(i)), -3 (t=+-1 -> Q(sqrt-3))}.
      The floor is disc = -4. The object sits at Q(sqrt-3) (prime 3, the figure-eight geometry); the only
      OTHER available imaginary field is Q(i) (prime 2) = the Whitehead/Borromean parent (L44, the 40a1
      conductor's 2-part). Two possible points; the object lands on one.
  (3) E7's Q(sqrt2) (disc 8) needs EVEN trace (t=+-2, det -1 = silver M_2) -> lives at silver/even-m;
      odd trace => disc ≡ 1 (mod 4), so E7 is parity-excluded from the (odd-trace) object.
  (4) Q(sqrt-7) (disc -7 < -4) is below the floor -> unreachable by ANY unimodular element (cleaner than
      the earlier "needs det=2 / non-unimodular").

This makes the dual-McKay / field-ladder sections referee-proof: E6+E8 (the real Q(sqrt5) + the imaginary
Q(sqrt-3)) with E7 parity-excluded and the imaginary ladder closed at {Q(i), Q(sqrt-3)} by the -4 floor.

Run: python reconciled_law.py (pyenv).
"""
from sympy import factorint


def sqfree(n):
    s = 1
    for p, e in factorint(abs(n)).items():
        if e % 2:
            s *= p
    return s if n >= 0 else -s


def disc(t, det):
    return t * t - 4 * det


def imaginary_trace_fields(trange=8):
    """all imaginary quadratic trace fields Q(sqrt d) reachable by a unimodular (det=+-1) element."""
    out = {}
    for det in (1, -1):
        for t in range(-trange, trange + 1):
            d = disc(t, det)
            if d < 0:
                out.setdefault(sqfree(d), []).append((t, det, d))
    return out


def trace_of_field(target_sf):
    """which (trace, det) give Q(sqrt target_sf)?"""
    return [(t, det) for det in (1, -1) for t in range(-6, 7) if sqfree(disc(t, det)) == target_sf]


if __name__ == "__main__":
    print("B239 -- the reconciled unimodular trace-field law\n")

    print("(1) sqrt5 is robust across representatives (real field):")
    for nm, t, det in [("RL bundle monodromy [[2,1],[1,1]]", 3, 1), ("M_1 homological [[1,1],[1,0]]", 1, -1)]:
        print(f"    {nm}: trace {t}, det {det:+d} -> disc {disc(t, det)} -> Q(sqrt{sqfree(disc(t, det))})")
    assert sqfree(disc(3, 1)) == 5 and sqfree(disc(1, -1)) == 5

    print("\n(2) the ONLY imaginary quadratic trace fields of a unimodular element:")
    imag = imaginary_trace_fields()
    for sf in sorted(imag):
        reps = imag[sf][0]
        print(f"    Q(sqrt{sf})  (e.g. t={reps[0]}, det={reps[1]:+d}, disc={reps[2]})")
    assert set(imag) == {-1, -3}            # Q(i) and Q(sqrt-3) ONLY
    print("    => exactly {Q(i), Q(sqrt-3)}; the floor is disc=-4 (t=0,det=+1).")
    print("       object geometry = Q(sqrt-3) (prime 3); the other point = Q(i) (prime 2 = Whitehead/Borromean parent).")

    print("\n(3) E7's Q(sqrt2) needs EVEN trace (parity exclusion):")
    print(f"    Q(sqrt2) (disc 8) at (trace,det): {trace_of_field(2)}  (even trace = silver M_2)")
    assert all(t % 2 == 0 for t, det in trace_of_field(2))      # only even traces give sqrt2
    assert all(disc(t, det) % 4 == 1 for det in (1, -1) for t in (-3, -1, 1, 3))   # odd trace -> disc=1 mod 4

    print("\n(4) Q(sqrt-7) is below the -4 floor -> unreachable:")
    print(f"    any unimodular element with sqfree(disc)=-7? {trace_of_field(-7)}  (none: disc -7 < -4)")
    assert trace_of_field(-7) == []

    print("\nReconciled: unimodular + odd-trace; E6+E8 (Q(sqrt-3)+Q(sqrt5)); E7 parity-excluded;")
    print("imaginary ladder closed at {Q(i), Q(sqrt-3)} by the disc=-4 floor. Referee-proof.")
    print("ALL CHECKS PASS")
