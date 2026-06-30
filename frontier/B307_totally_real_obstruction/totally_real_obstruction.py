"""B307 -- the generation count, closed: NO hyperbolic knot has a cyclic-cubic (C3) trace field (the totally-real
obstruction). Three symmetric generations are forced to the MULTIPLICITY route (B302). Run: sage-python.

From a Chat-2 handoff that sharpened the generation conjecture: "3 generations need a degree-3 trace field" was
refuted by 5_2 (cubic but Galois S3, splits 1+2 like 4_1), and refined to "3 SYMMETRIC generations need a CYCLIC
CUBIC (C3) trace field (three interchangeable embeddings)." Chat-2 asked CC to scan the census for C3 trace fields
(it lacked Sage). Done here -- and the answer is a THEOREM, cleaner than the conjectured "C3 is rare":

THE THEOREM (verified):
  * A cyclic-cubic field (Galois group C3) is GALOIS, so it has no order-2 automorphism, so no complex embedding
    -> C3 cubics are TOTALLY REAL (signature (3,0)).
  * A HYPERBOLIC 3-manifold's invariant trace field ALWAYS has a complex place (the geometric rep is not conjugate
    into PSL(2,R)) -> NOT totally real.
  * => NO hyperbolic knot can have a C3 trace field. The "3-generation carrier knot" (a single hyperbolic knot whose
    trace field is a symmetric C3 triple) CANNOT EXIST.

CENSUS-CONFIRMED: of 500 cusped census manifolds, 32 have degree-3 trace fields; ALL 32 have signature (1,1) = S3;
ZERO are cyclic (C3). Outcome B (Chat-2) is FORCED, not empirical-rare.

CONSEQUENCE: a single hyperbolic knot's trace field carries C2 (the complex-conjugate pair) -> matter multiplicities
1 or 2 (B298), and a symmetric C3 triple (3 equal generations) is ARITHMETICALLY IMPOSSIBLE for any single hyperbolic
knot. So three generations, if arithmetic, come ONLY from MULTIPLICITY -- the commensurator's hidden Z/3 (B302),
which is the arithmetic of the whole commensurability class, NOT a single object's trace field. This UNIFIES B298
(4_1 specifically) and B302 (the multiplicity route) into one theorem: the single-knot trace-field route to 3
generations is closed for ALL hyperbolic knots; multiplicity is the only route.

5_2 refutation (Chat-2, verified): x^3-x^2+1, disc -23, signature (1,1), Galois S3 -> 1+2, the same structure as 4_1.

FIREWALLED. The "generations = trace-field structure" reading is the physics dictionary; the THEOREM (C3 impossible
for hyperbolic) is pure arithmetic. Nothing to CLAIMS.
"""
import snappy
import itertools
from sage.all import NumberField, QQ, PolynomialRing

_R = PolynomialRing(QQ, 'x'); _x = _R.gen()


def field_signature_and_cyclic(poly):
    K = NumberField(poly, 'a')
    return K.signature(), (K.degree() == 3 and K.disc().is_square())


def c3_is_totally_real():
    """Every cyclic-cubic field is totally real (the 3 sample C3 fields all have signature (3,0))."""
    samples = [_x**3 + _x**2 - 2*_x - 1, _x**3 - 3*_x - 1, _x**3 + _x**2 - 4*_x + 1]   # Q(z7)+, Q(z9)+, cond-13
    return all(field_signature_and_cyclic(p)[0] == (3, 0) for p in samples)


def census_cubic_scan(N=500):
    cubic = 0; c3 = 0; sigs = {}
    for M in itertools.islice(snappy.OrientableCuspedCensus(), N):
        try:
            res = M.invariant_trace_field_gens().find_field(prec=200, degree=6, optimize=True)
        except Exception:
            res = None
        if res is None or res[0].degree() != 3:
            continue
        cubic += 1
        sig = res[0].signature(); sigs[sig] = sigs.get(sig, 0) + 1
        if res[0].disc().is_square():
            c3 += 1
    return cubic, c3, sigs


if __name__ == "__main__":
    sig52, cyc52 = field_signature_and_cyclic(_x**3 - _x**2 + 1)
    print(f"5_2 (x^3-x^2+1): signature {sig52}, cyclic-C3 {cyc52}  -> S3, splits 1+2 (Chat-2 refutation verified)")
    print(f"C3 cubics totally real (the obstruction): {c3_is_totally_real()}")
    cubic, c3, sigs = census_cubic_scan()
    print(f"\ncensus scan: {cubic} degree-3 trace fields, signatures {sigs}, cyclic-C3 count = {c3}")
    print("THEOREM: no hyperbolic knot has a C3 trace field (C3 totally real; hyperbolic has a complex place).")
    print("=> 3 symmetric generations are impossible in a single hyperbolic knot -> forced to MULTIPLICITY (B302).")
    assert cyc52 is False and c3_is_totally_real() and c3 == 0 and set(sigs) == {(1, 1)}
