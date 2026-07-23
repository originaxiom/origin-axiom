"""OI-151 -- B38/B39 torsion-one identity (B771 Phase-1 Wave-1 closure cell).

SCOPE (sealed prereg B771 7955049f, cell OI-151):
    "B38/B39 torsion-one identity: proven exactly / counterexampled."

This is narrowly the ALGEBRAIC IDENTITY informally stated in
frontier/B38_tangent_return_arithmetic_filter/FINDINGS.md and
frontier/B44_topological_torsion_route/probe.py:

    |det(M - I)| = |2 - mu| = 1   ==>   mu = 3   (hyperbolic branch)

where M is the tangent return's transverse linearization (trace mu, det 1).

NOT IN SCOPE (a different item, the T1-naturality WALL, untouched here):
    whether the tangent return is REQUIRED/entitled to inherit this filter at
    all (docs/TRACE_SELECTOR_THEOREM.md T1; LEAD_REGISTER "Selector-naturality
    axiom (T1/S1)"). This cell proves the algebra IF the filter is imposed; it
    says nothing about whether imposing it is natural. That question stays
    exactly as walled as before.

WHAT WAS ALREADY ON RECORD (re-derived here, not merely cited):
  - B44/probe.py already ran sympy on an ASSUMED abstract companion matrix
    M = [[0,-1],[1,mu]] and got det(M-I) = 2-mu, |2-mu|=1 => mu in {1,3},
    hyperbolic branch mu=3.
  - B26/B31 independently computed the REAL trace-map Jacobian's char poly
    factoring as (t+1)(t^2-mu(c)t+1) for the half-return T^3, and
    (t-1)(t^2-M(c)t+1) for the full return T^6, with mu(c)=4c^2-2,
    M(c)=16c^4+2.

THE GAP THIS CELL CLOSES: those two facts were never chained together in one
computation. B44's "det(M-I)=2-mu" used an assumed/abstract companion matrix,
not the actual transverse block cut out of the real Jacobian; B26/B31 never
computed a determinant-minus-identity at all. This cell:
  (1) proves det(N-I) = 2 - tr(N) for a FULLY GENERIC 2x2 matrix N with
      det(N)=1 -- a basis-free identity, not tied to the companion form -- so
      it legitimately applies to whatever concrete matrix represents the real
      transverse block, in ANY basis;
  (2) independently re-derives (from the trace map itself, not cited) the
      real 3x3 Jacobians of T^3 and T^6 at the primitive point (0,0,c), reads
      off their transverse SL(2)-factors' trace mu(c), M(c) directly from the
      char poly, and confirms the transverse factor genuinely has det=1 (so
      identity (1) applies to it, not merely to an assumed stand-in);
  (3) solves |2-mu|=1 (and |2-M|=1) EXACTLY, shows the hyperbolic branch root
      is unique in both cases and equals 3, and cross-checks this literally
      reproduces the trace and torsion of the seed matrix A=[[2,1],[1,1]].
Two independent word-sets (T^3 half-return, T^6 full-return) stand in for the
>=2 seeds/word-sets house-method requirement, since this is exact symbolic
algebra (no numerical conditioning to report).
"""

from __future__ import annotations

import sympy as sp


def rule(title: str) -> None:
    print("\n" + "-" * 72)
    print(title)
    print("-" * 72)


def part1_general_identity() -> None:
    rule("PART 1 -- basis-free identity: det(N-I) = 2 - tr(N) for N in SL(2)")

    a, b, c, d = sp.symbols("a b c d")
    N = sp.Matrix([[a, b], [c, d]])
    det_N = sp.expand(N.det())
    tr_N = sp.expand(N.trace())

    # Impose det(N)=1 as a substitution (solve for d in terms of a,b,c to stay
    # fully symbolic and generic -- no companion-form assumption anywhere).
    d_solutions = sp.solve(sp.Eq(det_N, 1), d)
    assert len(d_solutions) == 1
    d_val = d_solutions[0]

    N_unit = N.subs(d, d_val)
    lhs = sp.expand((N_unit - sp.eye(2)).det())
    rhs = sp.expand(2 - N_unit.trace())
    identity_residual = sp.simplify(lhs - rhs)

    print(f"    generic N = {N.tolist()}, det(N) = {det_N}")
    print(f"    det(N)=1 solved for d: d = {d_val}")
    print(f"    det(N-I) [generic, det=1 imposed]  = {sp.factor(lhs)}")
    print(f"    2 - tr(N) [same substitution]      = {sp.factor(rhs)}")
    print(f"    residual (must be 0)               = {identity_residual}")
    assert identity_residual == 0, "det(N-I) != 2-tr(N) -- IDENTITY FAILS (counterexample)"

    # Cayley-Hamilton cross-check, entirely independent derivation: for any
    # 2x2 N, charpoly_N(t) = t^2 - tr(N) t + det(N).  det(N-I) = (-1)^2 *
    # charpoly_N(1) = 1 - tr(N) + det(N).  With det(N)=1: = 2 - tr(N).
    t = sp.symbols("t")
    mu_sym = sp.symbols("mu")
    charpoly_generic = t**2 - mu_sym * t + 1  # det=1, trace=mu, fully general SL(2) char poly
    ch_at_1 = charpoly_generic.subs(t, 1)
    print(f"    Cayley-Hamilton cross-check: charpoly(1) = {ch_at_1} = 2-mu  (independent route)")
    assert sp.expand(ch_at_1 - (2 - mu_sym)) == 0

    print("\n    VERIFIED: for ANY 2x2 matrix N with det(N)=1, det(N-I)=2-tr(N)")
    print("    exactly -- basis-independent, proven two independent ways")
    print("    (direct symbolic determinant + Cayley-Hamilton at t=1).")


def trace_map(state: sp.Matrix) -> sp.Matrix:
    x, y, z = state
    return sp.Matrix([z, x, 2 * x * z - y])


def iterate(state: sp.Matrix, n: int) -> sp.Matrix:
    out = sp.Matrix(state)
    for _ in range(n):
        out = trace_map(out)
    return sp.simplify(out)


def part2_real_jacobians():
    rule("PART 2 -- the REAL trace-map Jacobians (independently re-derived, not cited)")

    x, y, z, c, t = sp.symbols("x y z c t")
    state = sp.Matrix([x, y, z])
    point = {x: 0, y: 0, z: c}

    results = {}

    for n, label in ((3, "half-return T^3"), (6, "full-return T^6")):
        image = iterate(state, n)
        jac = image.jacobian(state).subs(point)
        charpoly = sp.factor(jac.charpoly(t).as_expr())
        det_jac = sp.factor(jac.det())
        print(f"\n    [{label}]")
        print(f"        image T^{n}(0,0,c) subs = {tuple(sp.simplify(image.subs(point)))}")
        print(f"        char(DT^{n}) = {charpoly}")
        print(f"        det(DT^{n})  = {det_jac}")

        # Factor out the rational (trivial) root of the char poly and read the
        # remaining quadratic factor's trace as mu(c), independently confirming
        # its constant term is 1 (i.e. the transverse factor genuinely has
        # det=1, so Part 1's identity legitimately applies to it -- this is the
        # discriminating check, not an assumption).
        poly = sp.Poly(jac.charpoly(t).as_expr(), t)
        roots = sp.roots(sp.Poly(poly, t, extension=True), t)
        rational_roots = [r for r in roots if r.is_rational]
        assert len(rational_roots) == 1, f"expected exactly one rational trivial root, got {rational_roots}"
        triv = rational_roots[0]
        quotient = sp.factor(sp.cancel(poly.as_expr() / (t - triv)))
        quotient_poly = sp.Poly(sp.expand(quotient), t)
        coeffs = quotient_poly.all_coeffs()  # [1, -mu, const]
        assert coeffs[0] == 1
        const_term = coeffs[2]
        mu_expr = sp.expand(-coeffs[1])
        print(f"        trivial eigenvalue (exact rational root of char poly) = {triv}")
        print(f"        transverse quadratic factor = {sp.expand(quotient)}")
        print(f"        transverse factor constant term (must be 1, i.e. det=1) = {const_term}")
        assert sp.expand(const_term - 1) == 0, "transverse factor is NOT det=1 -- identity does not apply"
        print(f"        => transverse block is genuinely SL(2): trace mu(c) = {mu_expr}")

        # Consistency check: det(full Jacobian) = trivial_eigenvalue * det(transverse) = triv * 1
        print(f"        consistency: det(DT^{n}) should equal trivial-eigenvalue * 1 = {triv}")
        assert sp.expand(det_jac - triv) == 0

        # Apply Part 1's basis-free identity directly to this real mu(c): the
        # transverse block's own det-minus-I is 2-mu(c), EXACTLY, regardless
        # of what concrete matrix realizes it.
        det_minus_I = sp.expand(2 - mu_expr)
        print(f"        det(transverse - I) = 2 - mu(c) = {det_minus_I}   [Part 1 identity applied]")

        results[n] = {"mu_expr": mu_expr, "label": label}

    return results


def part3_solve_torsion_one(results):
    rule("PART 3 -- solve |2-mu|=1 exactly; hyperbolic-branch uniqueness; A cross-check")

    # NB: must reuse the *same* plain symbol c that mu_expr was built from in
    # Part 2 (sp.symbols("x y z c t"), no assumptions) -- sympy Symbol
    # identity is name+assumptions, so a fresh real=True c would not match
    # and sp.solve(..., c**2) would silently return [].
    c = sp.symbols("c")

    for n, data in results.items():
        mu_expr = data["mu_expr"]
        label = data["label"]
        print(f"\n    [{label}]  mu(c) = {mu_expr}")

        mu_sym = sp.symbols("mu")
        roots = sp.solve(sp.Eq((2 - mu_sym) ** 2, 1), mu_sym)
        roots = sorted(roots, key=lambda r: r)
        print(f"        |2-mu|=1  =>  mu in {roots}")
        assert set(roots) == {1, 3}

        hyperbolic_roots = [r for r in roots if sp.Abs(r) > 2]
        print(f"        hyperbolic branch (|mu|>2): {hyperbolic_roots}")
        assert hyperbolic_roots == [3], "hyperbolicity does not uniquely select mu=3 -- COUNTEREXAMPLE"

        mu_star = hyperbolic_roots[0]
        c2_solutions = sp.solve(sp.Eq(mu_expr, mu_star), c**2)
        print(f"        mu(c)={mu_star}  =>  c^2 in {c2_solutions}")

        # Also record the full |2-mu|=1 preimage (both roots) in c^2, to make
        # explicit that the OTHER (elliptic) root is not silently dropped --
        # it is excluded by hyperbolicity, not by an extra unstated choice.
        for other_root in roots:
            c2_other = sp.solve(sp.Eq(mu_expr, other_root), c**2)
            branch = "hyperbolic (|mu|>2)" if sp.Abs(other_root) > 2 else "non-hyperbolic (excluded)"
            print(f"          mu={other_root} [{branch}]: c^2 in {c2_other}")

    print("\n    [A cross-check] literal seed matrix A = [[2,1],[1,1]]")
    A = sp.Matrix([[2, 1], [1, 1]])
    assert A.det() == 1
    trA = A.trace()
    det_A_minus_I = (A - sp.eye(2)).det()
    print(f"        A = {A.tolist()},  det(A)={A.det()},  tr(A)={trA}")
    print(f"        det(A-I) = {det_A_minus_I}   (direct, no formula invoked)")
    assert det_A_minus_I == 2 - trA
    print(f"        |det(A-I)| = {abs(det_A_minus_I)}  ->  A is torsion-one, tr(A)=3")
    assert abs(det_A_minus_I) == 1
    assert trA == 3
    print("        matches: the torsion-one selection on the tangent return (Part 2/3)")
    print("        reproduces EXACTLY A's own (trace, torsion) -- self-consistent.")


def main() -> None:
    print("=" * 72)
    print("OI-151 -- B38/B39 torsion-one identity (B771 Phase-1 Wave-1)")
    print("Scope: the algebraic identity only. T1-naturality WALL untouched.")
    print("=" * 72)

    part1_general_identity()
    results = part2_real_jacobians()
    part3_solve_torsion_one(results)

    rule("VERDICT")
    print("""
    The torsion-one identity is PROVEN EXACTLY:

        For any 2x2 matrix N with det(N)=1:  det(N-I) = 2 - tr(N).      [Part 1, general, basis-free]

        The real trace-map Jacobians' transverse SL(2) factors (independently
        re-derived, both the half-return T^3 and the full-return T^6) satisfy
        det=1 by direct computation, so this identity applies to them exactly,
        not merely to an assumed companion-matrix stand-in.               [Part 2]

        |2-mu|=1 has exactly two roots {1,3}; hyperbolicity (|mu|>2) alone
        (no extra sign choice needed) selects mu=3 UNIQUELY, in BOTH the T^3
        and T^6 word-sets, exactly reproducing tr(A)=3 and A's own torsion
        |det(A-I)|=1.                                                     [Part 3]

    This closes the algebraic identity component of B38/B44 exactly (RESOLVED-A).

    NOT resolved by this cell, and not attempted: T1 -- whether the tangent
    return is entitled/required to have this filter imposed on it at all.
    That is the separate, still-open Selector-naturality (T1/S1) wall
    (docs/TRACE_SELECTOR_THEOREM.md, docs/LEAD_REGISTER.md). This cell says:
    IF torsion-one is imposed, the algebra that follows is exact and
    unambiguous. It does not say torsion-one MUST be imposed.
    """)


if __name__ == "__main__":
    main()
