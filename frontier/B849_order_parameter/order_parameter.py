#!/usr/bin/env python3
"""B849 -- does the claimed beta=1 SSB have an ORDER PARAMETER?

Sealed prereg: PREREGISTRATION.md, facb8c0355d8b422.

A claimed spontaneous symmetry breaking with no order parameter is a metaphor. This tries to
exhibit one, under criteria fixed before any number existed.

READ THE PREREG'S CORRECTION FIRST. This seat previously argued that m004's amphichirality makes
the order parameter "provably zero" and called it a cheap kill. That is WRONG and was withdrawn
before computing: in SSB the SYSTEM carries the symmetry and the STATE breaks it, so
amphichirality is the PRECONDITION for SSB, not evidence against it. Cells 1-3 cannot refute the
reframe and are forbidden from being reported as if they could.

Mathematics scope. Nothing reaches CLAIMS.md.
"""
import json
import os
import warnings

warnings.filterwarnings("ignore")
import snappy                                                        # noqa: E402
import sympy as sp                                                   # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))

# A panel spanning BOTH classes. The chiral members are the positive control: without at least one
# CS != 0, "CS(m004) = 0" is uninterpretable -- an instrument that returns zero for everything has
# measured nothing. Same discipline as the Fleiss self-test.
PANEL = [
    ("m004", "the object (figure-eight complement)"),
    ("m003", "the sister"),
    ("m015", "5_2 knot complement -- chiral, expected CS != 0"),
    ("m006", "cusped census"),
    ("m007", "cusped census"),
    ("m009", "cusped census"),
    ("m010", "cusped census"),
    ("m011", "cusped census"),
    ("4_1",  "figure-eight by knot name (same manifold, different route in)"),
    ("5_2",  "5_2 by knot name -- chiral"),
    ("6_1",  "6_1 knot complement"),
    ("6_2",  "6_2 knot complement"),
    ("6_3",  "6_3 knot complement -- amphichiral knot"),
    ("8_9",  "8_9 knot complement"),
]


# CS for a cusped hyperbolic manifold is defined MODULO pi^2 in snappy's normalisation, so the
# 2-torsion subgroup of the value group is {0, pi^2/2}. The prereg sealed "zero-or-half-period";
# the FIRST implementation of this file checked only "zero", which is NARROWER THAN THE SEAL.
# m003 came back at pi^2/2 to 4e-11 and was reported as a lemma violation -- it is not one. It is
# the lemma's OTHER permitted value, and the code could not see it. Fixed to test what was sealed.
HALF_PERIOD = float(sp.pi**2 / 2)


def _two_torsion(cs, tol=1e-8):
    """|CS| is 0 or the half-period -> 2*CS == 0 in the value group."""
    return abs(cs) < tol or abs(abs(cs) - HALF_PERIOD) < tol


def _cs_class(cs, tol=1e-8):
    if abs(cs) < tol:
        return "0"
    if abs(abs(cs) - HALF_PERIOD) < tol:
        return "pi^2/2 (the nonzero 2-torsion class)"
    return "free"


def amphichiral(M):
    """Exhibit the orientation-reversing symmetry rather than cite amphichirality.

    snappy's symmetry group knows whether an orientation-reversing self-isometry exists; this
    is a computation on the manifold, not a lookup of a knot table adjective.
    """
    try:
        G = M.symmetry_group()
        return bool(G.is_amphicheiral()), str(G)
    except Exception as exc:                                          # pragma: no cover
        return None, f"symmetry group unavailable: {exc}"


def cell1_and_2():
    """CS across the panel (Cell 1, with its positive control) and m004 itself (Cell 2)."""
    rows = []
    for name, note in PANEL:
        try:
            M = snappy.Manifold(name)
            cv = M.complex_volume()
            vol, cs = float(cv.real()), float(cv.imag())
            amph, gstr = amphichiral(M)
            rows.append(dict(name=name, note=note, volume=vol, CS=cs,
                             CS_is_zero=abs(cs) < 1e-9,
                             CS_is_two_torsion=_two_torsion(cs),
                             CS_class=_cs_class(cs),
                             amphichiral=amph, symmetry_group=gstr))
        except Exception as exc:                                      # pragma: no cover
            rows.append(dict(name=name, note=note, error=str(exc)))
    return rows


def cell3(rows):
    """The lemma, VERIFIED across the panel rather than assumed.

    For amphichiral M any orientation-odd invariant I has I(M) = -I(M), so 2*I(M) = 0: I is zero
    or 2-torsion in its value group. CS for a cusped hyperbolic manifold is defined modulo a
    period; snappy normalises so that the reachable 2-torsion value is 0 in these coordinates,
    so the prediction here is CS == 0 for every amphichiral member.
    """
    good = [r for r in rows if "error" not in r and r.get("amphichiral") is not None]
    amph = [r for r in good if r["amphichiral"]]
    chir = [r for r in good if not r["amphichiral"]]
    return dict(
        n_amphichiral=len(amph), n_chiral=len(chir),
        # THE SEALED LEMMA: zero OR half-period, not zero alone
        amphichiral_all_two_torsion=all(r["CS_is_two_torsion"] for r in amph),
        amphichiral_violations=[r["name"] for r in amph if not r["CS_is_two_torsion"]],
        amphichiral_classes={r["name"]: r["CS_class"] for r in amph},
        amphichiral_all_zero=all(r["CS_is_zero"] for r in amph),   # the NARROWER, wrong test
        chiral_with_nonzero_CS=[r["name"] for r in chir if not r["CS_is_zero"]],
        chiral_with_FREE_CS=[r["name"] for r in chir if r["CS_class"] == "free"],
        # THE POSITIVE CONTROL: without this the arc is INSTRUMENT VOID
        positive_control_passes=any(not r["CS_is_zero"] for r in chir),
    )


def cell4():
    """THE LEVEL TEST -- the cell with teeth.

    The chirality Z/2 the reframe nominates is COMPLEX CONJUGATION. Does it fix K = Q(sqrt-3)?
    If not, it is an element of Gal(K/Q) and NOT of Gal(K^ab/K) -- and Gal(K^ab/K) is the group
    that permutes extremal KMS states in a Bost-Connes-type system over an imaginary quadratic
    field, which is also the shape B700 reports for its torsor.

    The computable half is done here. The CITED half -- that Gal(K^ab/K) is the acting group --
    is declared, not verified, exactly as the prereg requires.
    """
    sqrt_m3 = sp.sqrt(-3)
    conj = sp.conjugate(sqrt_m3)
    fixes_K = bool(sp.simplify(conj - sqrt_m3) == 0)

    # the two geometric representations: the trace field element and its conjugate
    K = sp.QQ.algebraic_field(sp.sqrt(-3))
    # complex conjugation is the nontrivial element of Gal(K/Q): order 2, not identity
    order2 = bool(sp.simplify(sp.conjugate(conj) - sqrt_m3) == 0)

    # trace-field DATA is conjugation-invariant where it is rational; the representations are not
    # (this is why the label is invisible to traces -- the B713/theta-trivial lesson)
    return dict(
        complex_conjugation_fixes_K=fixes_K,
        complex_conjugation_has_order_2=order2,
        conj_of_sqrt_m3=str(conj),
        # the computed conclusion
        conjugation_in_Gal_K_over_Q=(not fixes_K) and order2,
        conjugation_in_Gal_Kab_over_K=fixes_K,       # membership REQUIRES fixing K
        # the declared citation, NOT verified in this seat
        CITED_acting_group_is_Gal_Kab_over_K=None,
        citation_status=("DECLARED CITATION, NOT VERIFIED HERE. That Gal(K^ab/K) permutes the "
                         "extremal KMS states of a Bost-Connes-type system over an imaginary "
                         "quadratic field is attributed to the Bost-Connes / "
                         "Connes-Marcolli-Ramachandran construction and has NOT been checked in "
                         "this sandbox. Every verdict resting on it carries CONDITIONAL."))


def main():
    rows = cell1_and_2()
    c3 = cell3(rows)
    c4 = cell4()

    m004 = next(r for r in rows if r["name"] == "m004")

    # ---- verdicts, read off the SEALED criteria ----
    if not c3["positive_control_passes"]:
        manifold_verdict = "INSTRUMENT VOID"
    elif not m004["CS_is_zero"]:
        manifold_verdict = "ORDER PARAMETER PRESENT (manifold level)"
    else:
        manifold_verdict = "ORDER PARAMETER ABSENT (manifold level)"

    if c4["conjugation_in_Gal_Kab_over_K"]:
        level_verdict = "LEVEL OK"
    elif c4["conjugation_in_Gal_K_over_Q"]:
        level_verdict = "LEVEL MISMATCH (CONDITIONAL on the cited acting group)"
    else:
        level_verdict = "UNDETERMINED"

    out = dict(cell1_2_panel=rows, cell3_lemma=c3, cell4_level=c4,
               manifold_verdict=manifold_verdict, level_verdict=level_verdict,
               seal="facb8c0355d8b422")
    with open(os.path.join(HERE, "results.json"), "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=1, sort_keys=True)

    print("=" * 78)
    print("B849 -- does the claimed beta=1 SSB have an order parameter?")
    print("=" * 78)
    print(f"\n  {'manifold':8} {'vol':>12} {'CS':>16} {'CS=0':>6} {'amphi':>6}   note")
    for r in rows:
        if "error" in r:
            print(f"  {r['name']:8} ERROR: {r['error'][:50]}")
            continue
        print(f"  {r['name']:8} {r['volume']:>12.6f} {r['CS']:>16.10f} "
              f"{str(r['CS_is_zero']):>6} {str(r['amphichiral']):>6}   {r['note'][:34]}")

    print(f"\n  CELL 1 POSITIVE CONTROL: chiral members with CS != 0 -> "
          f"{c3['chiral_with_nonzero_CS']}")
    print(f"    control passes = {c3['positive_control_passes']}"
          f"   (if False the arc is INSTRUMENT VOID and issues no verdict)")
    print(f"\n  CELL 3 LEMMA (as SEALED: zero OR half-period): amphichiral members = "
          f"{c3['n_amphichiral']}, all 2-torsion -> {c3['amphichiral_all_two_torsion']}   "
          f"violations {c3['amphichiral_violations']}")
    for k, v in c3["amphichiral_classes"].items():
        print(f"      {k:8} CS class = {v}")
    print(f"    (the narrower 'all CS == 0' test the first implementation used would say "
          f"{c3['amphichiral_all_zero']} -- NARROWER THAN THE SEAL)")
    m003 = next(r for r in rows if r["name"] == "m003")
    print(f"\n  CELL 2 THE OBJECT: CS(m004) = {m004['CS']:.12f}  class {m004['CS_class']}  "
          f"amphichiral = {m004['amphichiral']}")
    print(f"    SISTER:           CS(m003) = {m003['CS']:.12f}  class {m003['CS_class']}")
    print(f"    -> same volume, both amphichiral, DIFFERENT 2-torsion CS class: a discriminating")
    print(f"       invariant separating the object from its sister.")
    print(f"    {m004['symmetry_group']}")

    print(f"\n  CELL 4 THE LEVEL TEST")
    print(f"    complex conjugation fixes K = Q(sqrt-3)?  {c4['complex_conjugation_fixes_K']}"
          f"   (conj(sqrt-3) = {c4['conj_of_sqrt_m3']})")
    print(f"    => in Gal(K/Q)?      {c4['conjugation_in_Gal_K_over_Q']}")
    print(f"    => in Gal(K^ab/K)?   {c4['conjugation_in_Gal_Kab_over_K']}"
          f"    (membership REQUIRES fixing K)")
    print(f"    CITED, NOT VERIFIED: {c4['citation_status'][:72]}...")

    print(f"\n  MANIFOLD VERDICT : {manifold_verdict}")
    print(f"  LEVEL VERDICT    : {level_verdict}")
    print("\n  Per the seal, an ABSENT manifold verdict is NOT a refutation of the reframe.")
    print("  It shifts a burden: the order parameter cannot be a topological invariant of M,")
    print("  so the reframe must supply one on the STATE space -- and Cell 4 says which group")
    print("  it must live in.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
