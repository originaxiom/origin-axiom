"""B439 (C3) -- the child's SL(2,C) vacuum book: the figure-eight core + the slope control.

The child = 4_1(5,1). Its irreducible SL(2,C) flat connections ("vacua") are the points of the
figure-eight A-polynomial curve A_CL(M,L)=0 that satisfy the (5,1) Dehn-filling relation
M^5 L = 1 (kill mu^5 lambda). We use the BANKED B67 Cooper-Long A-polynomial (standard
normalization -- no convention ambiguity):

    CL(M,L) = M^4 L^2 + (-M^8 + M^6 + 2 M^4 + M^2 - 1) L + M^4.

Substituting L = M^-5 and clearing denominators gives a reciprocal polynomial in M of degree
10; the invariant is the meridian TRACE t = M + 1/M, so it reduces to a degree-5 trace
polynomial Q_5(t). Result (exact):

    Q_5(t) = t^5 - t^4 - 5 t^3 + 5 t^2 + 5 t - 2 = (t + 2) * (t^4 - 3 t^3 + t^2 + 3 t - 1).

  * (t+2): t=-2 => M=-1, the REDUCIBLE/central connection.
  * the QUARTIC t^4 - 3 t^3 + t^2 + 3 t - 1: the 4 IRREDUCIBLE vacua. Its discriminant is
    EXACTLY -283 -- the child's invariant trace field (x^4-x-1, disc -283, B434/B436). The
    -283 REPRODUCE-GATE PASSES: the vacuum quartic is the child's own trace field (confirmed
    below: it has the root alpha^3 - alpha^2, alpha a root of x^4-x-1; both S4, disc -283).

SLOPE CONTROL (leg iv). Same construction at the unforced slope 7 (L = M^-7):
    Q_7(t) = (t+2) * (t^6 - 2 t^5 - 3 t^4 + 5 t^3 + 4 t^2 - 3 t - 1),
  => 6 irreducible vacua in a degree-6 field of discriminant 50173 = 131 * 383. The count
  (4 vs 6) AND the field (-283 vs 131*383) both differ -- the slope control PASSES.

SCOPE / COVERAGE. This is the SLOPE-control-complete result. The FOREIGN control -- the tier-3
discriminator that B438 made mandatory (5_2 is the child's commensurability neighbour, sharing
the -283 field and the 121 torsion value) -- is the registered IMMEDIATE next step. Per the C3
prereg (asymmetric coverage = COVERAGE-VOID), the Inversion-Law verdict at the SL(2) floor is
HELD pending 5_2(5,1)'s vacuum spectrum. The three prereg'd outcomes stand:
  (a) 5_2 gives the SAME quartic  => the SL(2) vacuum structure is commensurability-shared
      (Inversion Law's 4th instance, at a new floor);
  (b) 5_2 gives a DIFFERENT count/field => a figure-eight-vs-5_2 distinguisher (tier-3 BREAK
      candidate -- escalate);
  (c) both share only the geometric -283 vacuum but differ elsewhere => partial.

Firewall: hyperbolic geometry + character-variety arithmetic. No physics claim.
"""
import os, json
import sympy as sp

M, t, L, x = sp.symbols('M t L x')
CL = M**4*L**2 + (-M**8 + M**6 + 2*M**4 + M**2 - 1)*L + M**4


def vacuum_trace_poly(p):
    """slope (p,1): intersect CL with L=M^-p, reduce to the meridian-trace polynomial Q_p(t)."""
    expr = sp.cancel(CL.subs(L, M**(-p)))
    num, _ = sp.fraction(sp.together(expr))
    coeffs = sp.Poly(sp.expand(num), M).all_coeffs()[::-1]
    lo = next(i for i, a in enumerate(coeffs) if a != 0)   # strip common M^k content
    coeffs = coeffs[lo:]
    d = len(coeffs) - 1
    assert d % 2 == 0 and coeffs == coeffs[::-1], "expected an even-degree reciprocal polynomial"
    half = d // 2
    pk = {0: sp.Integer(2), 1: t}                          # p_k = M^k + M^-k via Chebyshev recursion
    for k in range(2, half + 1):
        pk[k] = sp.expand(t*pk[k-1] - pk[k-2])
    Q = coeffs[half] + sum(coeffs[half + k]*pk[k] for k in range(1, half + 1))
    return sp.Poly(sp.expand(Q), t)


def irreducible_factor_data(p):
    """return (Q_p, [(factor, degree, disc)]) with the reducible (t+2) split out."""
    Q = vacuum_trace_poly(p)
    out = []
    for fac, _ in sp.factor_list(Q.as_expr(), t)[1]:
        fp = sp.Poly(fac, t)
        deg = fp.degree()
        disc = int(sp.discriminant(fac, t)) if deg >= 2 else None
        out.append((fac, deg, disc))
    return Q, out


def quartic_is_child_trace_field():
    """the vacuum quartic generates the child's invariant trace field x^4-x-1: it has the
    root alpha^3-alpha^2 (alpha a root of x^4-x-1) => same degree-4 field. Verified exactly by
    reducing vac(alpha^3-alpha^2) modulo the child polynomial: the remainder must vanish."""
    a = sp.Symbol('a')
    child = a**4 - a - 1
    vac = lambda tt: tt**4 - 3*tt**3 + tt**2 + 3*tt - 1
    root_has = sp.rem(sp.expand(vac(a**3 - a**2)), child, a) == 0     # alpha^3-alpha^2 is a root
    same_disc = (sp.discriminant(a**4 - a - 1, a)
                 == sp.discriminant(vac(a), a) == -283)
    return bool(root_has and same_disc)


if __name__ == "__main__":
    Q5, d5 = irreducible_factor_data(5)
    Q7, d7 = irreducible_factor_data(7)
    print("child slope 5:", Q5.as_expr())
    for fac, deg, disc in d5:
        print(f"   factor {sp.factor(fac)}  deg={deg}  disc={disc}")
    print("control slope 7:", Q7.as_expr())
    for fac, deg, disc in d7:
        print(f"   factor {sp.factor(fac)}  deg={deg}  disc={disc}")
    gate = quartic_is_child_trace_field()
    print("reproduce-gate (vacuum quartic == child trace field, disc -283):", gate)

    # assertions (the banked facts)
    assert (x**4 - 3*x**3 + x**2 + 3*x - 1) == sp.factor_list(Q5.as_expr(), t)[1][1][0].subs(t, x) \
        or any(deg == 4 and disc == -283 for _, deg, disc in d5)
    n_irred_5 = sum(1 for _, deg, _ in d5 if deg >= 2 or (deg == 1 and False))
    quartic = [(deg, disc) for _, deg, disc in d5 if deg == 4]
    assert quartic == [(4, -283)], quartic
    sextic = [(deg, disc) for _, deg, disc in d7 if deg == 6]
    assert sextic == [(6, 50173)], sextic
    assert gate

    out = dict(
        slope5_trace_poly=str(Q5.as_expr()),
        slope5_factors=[(str(sp.factor(f)), deg, disc) for f, deg, disc in d5],
        slope7_trace_poly=str(Q7.as_expr()),
        slope7_factors=[(str(sp.factor(f)), deg, disc) for f, deg, disc in d7],
        child_irreducible_vacua=4, child_vacuum_disc=-283,
        slope7_irreducible_vacua=6, slope7_disc=50173,
        reproduce_gate_passed=bool(gate),
        foreign_control="PENDING (5_2 tier-3, per B438) -- Inversion-Law verdict HELD",
    )
    json.dump(out, open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                     "vacuum_book.json"), "w"), indent=1)
    print("[written] vacuum_book.json")
