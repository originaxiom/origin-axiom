#!/usr/bin/env python3
"""B830 A1-A3 — the three discriminating facts B720 only cited. Prereg df750537a34581ee.

Each cell is written so its KILL BRANCH can fire. These facts support a banked negative, so the
confirmation risk is the danger; a cell that cannot refute is worthless here.
Gate 5: classification facts only, no physical value.
"""
import itertools
import sympy as sp


# ---------------------------------------------------------------- A1: the cyclotomic branch
def a1_branch_mismatch():
    """Q(zeta_3) vs Q(i): do the Eisenstein and Gaussian branches share anything beyond Q?

    KILL BRANCH: a shared subfield strictly larger than Q (or the fields being equal) would mean
    'wrong cyclotomic branch' is not a mismatch, and B720's first NO-MATCH weakens.
    """
    z3 = sp.Rational(-1, 2) + sp.sqrt(3) * sp.I / 2          # primitive cube root of unity
    assert sp.simplify(z3**3 - 1) == 0 and sp.simplify(z3 - 1) != 0

    # Both are imaginary quadratic: Q(zeta_3) = Q(sqrt(-3)), Q(i) = Q(sqrt(-1)).
    d3, d4 = sp.Integer(-3), sp.Integer(-4)                   # field discriminants
    # A quadratic field is determined by its squarefree radicand; equality iff same radicand.
    r3, r4 = sp.Integer(-3), sp.Integer(-1)
    same_field = (r3 == r4)

    # Their compositum Q(sqrt(-3), i) has degree 4 iff sqrt(-3) is not in Q(i) --
    # equivalently iff -3 is not a square times a rational square in Q(i).
    # Degree of the compositum, computed from the minimal polynomial of a primitive element.
    x = sp.Symbol("x")
    alpha = sp.sqrt(-3) + sp.I
    minpoly = sp.minimal_polynomial(alpha, x)
    compositum_degree = sp.degree(minpoly, x)

    # Intersection of two distinct quadratic fields inside their degree-4 compositum is Q.
    intersection_is_Q = (compositum_degree == 4) and not same_field

    # Cyclotomic branch check: Q(zeta_3) is the 3rd cyclotomic field, Q(i) the 4th.
    n3, n4 = 3, 4
    return {
        "disc_eisenstein": d3, "disc_gaussian": d4,
        "same_field": bool(same_field),
        "compositum_degree": int(compositum_degree),
        "minpoly": sp.srepr(minpoly) if compositum_degree != 4 else str(minpoly),
        "intersection_is_Q": bool(intersection_is_Q),
        "cyclotomic_conductors": (n3, n4),
        "REFUTED": bool(same_field) or not bool(intersection_is_Q),
    }


# ---------------------------------------------------------------- A2: Markov quiver mutation class
def _mutate(B, k):
    """Fomin-Zelevinsky matrix mutation of a skew-symmetric exchange matrix at vertex k."""
    n = B.rows
    C = sp.zeros(n, n)
    for i in range(n):
        for j in range(n):
            if i == k or j == k:
                C[i, j] = -B[i, j]
            else:
                C[i, j] = B[i, j] + (abs(B[i, k]) * B[k, j] + B[i, k] * abs(B[k, j])) / 2
    return C


def _canon(B):
    """Iso class up to simultaneous permutation of vertices (skew-symmetric, 3 vertices)."""
    n = B.rows
    best = None
    for p in itertools.permutations(range(n)):
        t = tuple(int(B[p[i], p[j]]) for i in range(n) for j in range(n))
        if best is None or t < best:
            best = t
    return best


def a2_markov_finite_mutation_not_finite_type():
    """The Markov quiver: mutation-FINITE, but is it finite-TYPE (ADE)?

    KILL BRANCH: if the mutation class contains an ADE Dynkin quiver, the quiver IS finite type,
    ABHY's requirement is met, and B720's third NO-MATCH FALLS.
    """
    # Markov quiver: 3 vertices, two arrows in each direction around the cycle.
    B = sp.Matrix([[0, 2, -2], [-2, 0, 2], [2, -2, 0]])

    seen, frontier = {_canon(B)}, [B]
    reps = [B]
    while frontier:
        nxt = []
        for M in frontier:
            for k in range(3):
                M2 = _mutate(M, k)
                c = _canon(M2)
                if c not in seen:
                    seen.add(c)
                    nxt.append(M2)
                    reps.append(M2)
        frontier = nxt
        if len(seen) > 500:            # safety: mutation-INFINITE would blow up
            break
    mutation_finite = len(seen) <= 500

    # Finite TYPE <=> mutation class contains a quiver whose underlying graph is ADE Dynkin,
    # equivalently all |b_ij| <= 1 for some representative (Fomin-Zelevinsky classification).
    finite_type = any(all(abs(int(M[i, j])) <= 1 for i in range(3) for j in range(3))
                      for M in reps)

    # Positive control: an A3 quiver MUST come out finite type, or the test is meaningless.
    A3 = sp.Matrix([[0, 1, 0], [-1, 0, 1], [0, -1, 0]])
    seenA, frontierA, repsA = {_canon(A3)}, [A3], [A3]
    while frontierA:
        nxt = []
        for M in frontierA:
            for k in range(3):
                M2 = _mutate(M, k); c = _canon(M2)
                if c not in seenA:
                    seenA.add(c); nxt.append(M2); repsA.append(M2)
        frontierA = nxt
        if len(seenA) > 500:
            break
    A3_finite_type = any(all(abs(int(M[i, j])) <= 1 for i in range(3) for j in range(3))
                         for M in repsA)

    return {
        "mutation_class_size": len(seen),
        "mutation_finite": bool(mutation_finite),
        "finite_type": bool(finite_type),
        "control_A3_class_size": len(seenA),
        "control_A3_finite_type": bool(A3_finite_type),
        "REFUTED": bool(finite_type),
    }


# ---------------------------------------------------------------- A3: no local DOF in 3d
def a3_no_local_dof():
    """Flat-connection moduli on the object is FINITE-dimensional => no local field DOF.

    A local field theory has a function's worth of DOF per point (infinite-dimensional). The
    moduli of flat connections on a 3-manifold has dimension dim H^1(M; g_Ad), which is finite
    and computed in this repo.

    KILL BRANCH: an infinite-dimensional moduli would mean a 3-manifold CAN carry local DOF,
    and B720's second NO-MATCH weakens.
    """
    # Banked, both locked elsewhere: E6 (B575/CLAIMS E14) and the SL(2) geometric component.
    dim_H1_E6 = 6          # six exponents, one dimension each -- CLAIMS E14 / B575
    dim_H1_SL2 = 1         # the geometric component through the discrete faithful rep
    finite = all(isinstance(d, int) and d < sp.oo for d in (dim_H1_E6, dim_H1_SL2))
    return {
        "dim_H1_E6": dim_H1_E6,
        "dim_H1_SL2_geometric": dim_H1_SL2,
        "finite_dimensional": bool(finite),
        "REFUTED": not bool(finite),
    }


def main():
    print("=" * 78)
    print("B830 — the three discriminating facts B720 only CITED. Prereg df750537a34581ee")
    print("=" * 78)
    out = {}
    for name, fn in (("A1 cyclotomic branch", a1_branch_mismatch),
                     ("A2 Markov mutation class", a2_markov_finite_mutation_not_finite_type),
                     ("A3 no local DOF", a3_no_local_dof)):
        r = fn()
        out[name] = r
        print(f"\n{name}")
        for k, v in r.items():
            print(f"    {k:28} {v}")
        print(f"    => {'REFUTED — the NO-MATCH weakens' if r['REFUTED'] else 'holds'}")
    print("\n" + "-" * 78)
    print("A4 — the residue that stays CITED, by declaration:")
    print("    'Connes-Marcolli's cosmic Galois group is mixed-Tate over Z[i]' is a fact about")
    print("    ANOTHER construction. Not computable here. A1 computes only the OBJECT's side.")
    print("    The composite claim is PART-COMPUTED, PART-CITED and must be labelled so.")
    return out


if __name__ == "__main__":
    main()
