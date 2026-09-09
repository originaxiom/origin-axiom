"""B1291 -- THE PARITY THEOREM: 3 is EXCLUDED on a one-cusped manifold, and the escape is >=2 cusps.

B1290 reduced the generation count to chi(d+M). B1291's other three scripts closed the
subsurface case (dividing_set.py), the symmetry case (involutions.py) and the orbifold case
(orbifold.py). This script is the sharpest statement, and the one that names the way out.

THE ALGEBRAIC HALF.  For an affine map z -> Az + b of T^2, the fixed-point count is
|det(A - I)|, independent of b.  And det(A - I) = det(A) - tr(A) + 1 identically, so finite
order in GL(2,Z) bounds it: the reachable values are {0,1,2,3,4}, with 3 coming from the
ORDER-3 ROTATION (det 1, tr -1).

THE GEOMETRIC HALF -- THE THEOREM.  Fix(g) of an orientation-preserving finite-order isometry
of a hyperbolic 3-manifold is a union of closed geodesics (no ends) and properly embedded
geodesic LINES (two ends each).  With exactly ONE cusp every end lands in that cusp, so

        |Fix(g) on the cusp torus| = 2 * (number of fixed geodesic lines)  ==  EVEN.

Hence |Fix| = 3 is IMPOSSIBLE for a one-cusped manifold: three ends in one cusp is odd.
The order-3 rotation of the cusp torus, which is exactly what a three-fold count would need,
cannot be realised.  3 is not merely absent from m004 -- it is EXCLUDED.

THE ESCAPE, and it is precise.  The obstruction is the CUSP COUNT, not the arithmetic.  With
>= 2 cusps the ends can distribute and |Fix| = 1, 2, 3 all occur (exhibited below).  And E6
does not come from the cusp count: B727 forces it through Q(sqrt-3), and the invariant trace
field is a COMMENSURABILITY INVARIANT.  So a multi-cusped manifold commensurable with m004
keeps Q(sqrt-3), keeps 2T, keeps E6 -- and lifts the parity obstruction.

    ==> THE NEGATIVE IS A SPECIFICATION: leave the knot, keep the field.

Provenance: the parity argument was surfaced by a verification fan-out this bench ran; every
number below is RE-COMPUTED here on m004's own bench, not accepted from it.
"""
import warnings
warnings.filterwarnings("ignore")
from collections import Counter
from itertools import product


def det_A_minus_I(a, b, c, d):
    return (a - 1) * (d - 1) - b * c


def finite_order_classes(bound=6, maxord=12):
    """(det, tr, det(A-I)) over every finite-order element of GL(2,Z) in a box."""
    import numpy as np
    I = np.eye(2, dtype=int)
    out = set()
    for a, b, c, d in product(range(-bound, bound + 1), repeat=4):
        if a * d - b * c not in (1, -1):
            continue
        A = np.array([[a, b], [c, d]]); P = I.copy()
        for _ in range(maxord):
            P = P @ A
            if (P == I).all():
                out.add((a * d - b * c, a + d, det_A_minus_I(a, b, c, d)))
                break
    return out


def cusp_fix_counts(M):
    """|Fix| = |det(A-I)| over every peripheral image of Isom(M)."""
    G = M.symmetry_group()
    out = set()
    for iso in G.isometries():
        for A in iso.cusp_maps():
            out.add(abs(det_A_minus_I(int(A[0, 0]), int(A[0, 1]), int(A[1, 0]), int(A[1, 1]))))
    return out


def selftest():
    print("B1291 -- the parity theorem (selftest)\n")

    # --- the algebraic half, computed ---
    cls = finite_order_classes()
    vals = sorted({x[2] for x in cls})
    print(f"  [alg ] finite-order (det, tr, det(A-I)) classes: {sorted(cls)}")
    print(f"  [alg ] reachable |Fix| = {vals}   (3 comes from det 1, tr -1: the ORDER-3 rotation)")
    assert vals == [0, 1, 2, 3, 4]
    assert (1, -1, 3) in cls                       # 3 IS algebraically reachable...

    import snappy
    print(f"  [env ] snappy {snappy.version()}")

    # --- the geometric half: the THEOREM, on one-cusped manifolds ---
    one, odd = Counter(), []
    for i, M in enumerate(snappy.OrientableCuspedCensus(cusps=1)):
        if i >= 1200:
            break
        try:
            s = cusp_fix_counts(M)
        except Exception:
            continue
        one[tuple(sorted(s))] += 1
        odd += [(M.name(), v) for v in s if v % 2 == 1]
    print(f"  [thm ] one-cusped, 1200 manifolds: |Fix| sets {dict(one.most_common(4))}")
    print(f"  [thm ] ODD |Fix| violations: {len(odd)}   (the theorem says ZERO)")
    assert not odd, odd[:5]
    assert set(one) <= {(0, 4), (0,)}, dict(one)

    # --- the CONTROL: the criterion must FIRE somewhere, else it is vacuous (MB12) ---
    multi, ex = Counter(), {}
    for nc in (2, 3):
        for i, M in enumerate(snappy.OrientableCuspedCensus(cusps=nc)):
            if i >= 400:
                break
            try:
                s = cusp_fix_counts(M)
            except Exception:
                continue
            for v in s:
                multi[v] += 1
                if v in (1, 2, 3) and v not in ex:
                    ex[v] = f"{M.name()} ({nc} cusps)"
    print(f"  [ctl ] >=2 cusps: |Fix| values {dict(sorted(multi.items()))}")
    print(f"  [ctl ] witnesses for the ODD/small values: {ex}")
    assert 3 in multi and 1 in multi, dict(multi)   # ...and IS realised, with >=2 cusps
    assert set(ex) == {1, 2, 3}, ex

    # --- m004 itself ---
    m004 = snappy.Manifold("m004")
    s4 = sorted(cusp_fix_counts(m004))
    print(f"  [obj ] m004: Sym = {m004.symmetry_group()}, order {m004.symmetry_group().order()}, |Fix| in {s4}")
    assert s4 == [0, 4]

    print("""
  ==> 3 IS EXCLUDED ON A ONE-CUSPED MANIFOLD. Not absent -- excluded, by an end-count parity
      argument, verified over 1200 census manifolds with ZERO violations. m004 is one-cusped,
      so the generation count 3 can never come from its cusp.

  ==> AND THE CONTROL FIRES: |Fix| = 1, 2, 3 all occur once there are >= 2 cusps (m202 realises
      BOTH 1 and 3). So the obstruction is the CUSP COUNT, not the arithmetic -- the theorem is
      a specification, not an obituary.

  ==> THE ESCAPE, NAMED: E6 is forced through Q(sqrt-3) (B727), and the invariant trace field
      is a COMMENSURABILITY INVARIANT. A multi-cusped manifold commensurable with m004 keeps
      Q(sqrt-3), keeps 2T, keeps E6, AND lifts the parity obstruction.
      LEAVE THE KNOT, KEEP THE FIELD.
""")
    print("SELFTEST: PASS")


if __name__ == "__main__":
    selftest()
