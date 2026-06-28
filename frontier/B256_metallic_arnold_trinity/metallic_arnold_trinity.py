"""B256 -- the metallic Arnold trinity: E7 is the SILVER bundle's discriminant field (where the "missing" E7 lives).

THE HUNT LEAD (2026-06-28 deep-dive): the program long treated E7 as "excluded/absent" (B249 Niven; B237 no 2O
pi_1-quotient). But that conflated two levels. The monodromy phi=R^m L^m has trace t=m^2+2 and discriminant
t^2-4 = m^2(m^2+4), so the eigenvalue/DISCRIMINANT field is Q(sqrt(m^2+4)). Its McKay-exceptional values:
    m=1 (golden): Q(sqrt5)  -> 2I -> E8
    m=2 (silver): Q(sqrt2)  -> 2O -> E7     <-- the "missing" third Arnold group
    m>=3: Q(sqrt13), Q(sqrt29), ... (non-McKay)   [m=4 -> sqrt20 = sqrt5 -> E8 again]
Together with the figure-eight's IMAGINARY trace field Q(sqrt-3) -> 2T -> E6, the metallic family's arithmetic
realizes ALL THREE Arnold-trinity groups E6, E7, E8:
    E6 = figure-eight TRACE field      Q(sqrt-3)   (hyperbolic end, 2T)             [B210/B248]
    E8 = figure-eight DISCRIMINANT     Q(sqrt5)    (spherical end, 2I, cover L(5,2)) [B210/B248]
    E7 = SILVER DISCRIMINANT           Q(sqrt2)    (m=2, 2O)                          [NEW]

RECONCILIATION (this resolves the "where is E7" puzzle without contradicting anything banked):
  - B237 found silver has NO 2O *pi_1-quotient* (GQuotients=0) -- CORRECT, but golden has no 2I pi_1-quotient
    either (golden 2I:0 in B237); golden's E8 is the discriminant/homological McKay, NOT a pi_1-quotient. So
    silver's E7 sits at the SAME level as golden's E8. Neither E7 nor E8 is ever a pi_1-quotient; both are
    discriminant-field McKay. The asymmetry in B237's phrasing ("golden E8 banked" vs "silver E7 = field-only
    coincidence") is removed: they are the same kind of object.
  - B249 (Niven) excludes E7 from the figure-eight's ORBIFOLD trinity (sqrt2 is never a rational 2cos(pi/n)).
  - B251: silver is not a knot complement -> no orbifold / no double-branched-cover lens space.
  => E7 is ARITHMETICALLY present (silver discriminant) but GEOMETRICALLY homeless: unlike golden's E6 (hyperbolic
     orbifold) and E8 (spherical orbifold / lens cover), E7 has no cone-manifold or covering realization. The
     Arnold trinity is ARITHMETICALLY COMPLETE across the metallic family but GEOMETRICALLY PARTIAL (only golden's
     E6/E8 are realized as geometries).

FIREWALL: E6/E7/E8 are McKay/Arnold labels, not gauge groups. The discriminant field is an arithmetic invariant of
the monodromy; no physics. Nothing to CLAIMS.md.

Run: python metallic_arnold_trinity.py (pyenv; sympy).
"""
import sympy as sp

# McKay: binary polyhedral character field -> ADE
FIELD_TO_MCKAY = {3: ("2T", "E6"), 2: ("2O", "E7"), 5: ("2I", "E8")}   # keyed by squarefree radicand (|.|)


def monodromy_trace(m):
    return m * m + 2


def discriminant(m):
    """disc of x^2 - t x + 1, t = m^2+2: equals m^2 (m^2+4)."""
    t = monodromy_trace(m)
    return t * t - 4


def discriminant_field_radicand(m):
    """squarefree radicand of the discriminant field Q(sqrt(m^2+4))."""
    n = m * m + 4
    sf = sp.factorint(n)
    return int(sp.prod([p ** (e % 2) for p, e in sf.items()]))


def mckay_of_metallic(m):
    """the McKay/Arnold group of the m-th metallic discriminant field, or None if non-exceptional."""
    return FIELD_TO_MCKAY.get(discriminant_field_radicand(m))


if __name__ == "__main__":
    print("=== B256: the metallic Arnold trinity ===\n")
    print("discriminant field of phi=R^m L^m (disc = m^2(m^2+4) => Q(sqrt(m^2+4))):")
    for m in range(1, 7):
        rad = discriminant_field_radicand(m)
        mck = mckay_of_metallic(m)
        tag = f"{mck[0]} -> {mck[1]}" if mck else "(non-McKay)"
        assert discriminant(m) == m * m * (m * m + 4)
        print(f"  m={m}: disc={discriminant(m):>4} = {m}^2*{m*m+4}  -> Q(sqrt{rad})  {tag}")

    print("\nthe trinity:")
    print("  E6 = figure-eight TRACE field  Q(sqrt-3)  [2T]   (hyperbolic, B210/B248)")
    print("  E8 = figure-eight DISCRIMINANT Q(sqrt5)   [2I]   (spherical, B210/B248)")
    print("  E7 = SILVER DISCRIMINANT       Q(sqrt2)   [2O]   (m=2; NEW)")

    assert mckay_of_metallic(1) == ("2I", "E8")        # golden discriminant -> E8
    assert mckay_of_metallic(2) == ("2O", "E7")        # silver discriminant -> E7  (the missing third)
    assert mckay_of_metallic(4) == ("2I", "E8")        # m=4: sqrt20 = sqrt5 -> E8 again
    assert mckay_of_metallic(3) is None and mckay_of_metallic(5) is None
    # the three Arnold groups all appear across the metallic arithmetic (E6 from the trace field, E7/E8 from disc):
    appearing = {"E6"} | {mckay_of_metallic(m)[1] for m in (1, 2) if mckay_of_metallic(m)}
    assert appearing == {"E6", "E7", "E8"}
    print("\n=> Arnold trinity arithmetically COMPLETE across {golden trace, golden disc, silver disc};")
    print("   E7 is the silver discriminant (same level as golden E8), geometrically homeless. ALL CHECKS PASS")
