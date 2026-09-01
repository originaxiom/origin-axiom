#!/usr/bin/env python3
"""T2_cp_bit — bite control for SEALED_DESIGN.md (HALF 2).

Runs the design's two reading functions on HYPOTHETICAL inputs only.
Gate 5: no measured Standard Model value appears anywhere in this script;
every input below is a synthetic label or a synthetic CS value.

The design is HELD: this script demonstrates only that the criterion is
two-sided (MB12) — that each side of the comparison can output either
element of Z/2, and that a hypothetical object at CS = 1/4 reads CP-ODD.
"""
import sys

TOL = 1e-6


def object_bit(cs_mod_half, amphichiral=True):
    """Design section D1: the object-side reading (same rule as HALF 1)."""
    if not amphichiral:
        return "UNDEFINED-CHIRAL"
    r = cs_mod_half % 0.5
    if min(r, 0.5 - r) < TOL:
        return "CP-EVEN"
    if abs(r - 0.25) < TOL:
        return "CP-ODD"
    return "NOT-2-TORSION"


def reader_bit(configuration_class):
    """Design section D2: the reader-side reading, applied to an ABSTRACT
    classification label (which the reader, not this cell, will produce
    from measurement on the owner's election).

    configuration_class is one of:
      "CONSISTENT-WITH-CP-EVEN-POINT"  -> CP-EVEN
      "EXCLUDES-ALL-CP-EVEN-POINTS"    -> CP-ODD
      "UNRESOLVED"                     -> UNRESOLVED (no bit; comparison void)
    """
    table = {
        "CONSISTENT-WITH-CP-EVEN-POINT": "CP-EVEN",
        "EXCLUDES-ALL-CP-EVEN-POINTS": "CP-ODD",
        "UNRESOLVED": "UNRESOLVED",
    }
    return table[configuration_class]


def main():
    checks = {}

    # --- Named bite control: hypothetical object at CS = 1/4 -> CP-ODD ---
    checks["bite_hypothetical_cs_quarter_is_cp_odd"] = (
        object_bit(0.25) == "CP-ODD")

    # --- Both elements reachable on the object side ---
    checks["object_side_cp_even_reachable"] = (object_bit(0.0) == "CP-EVEN")
    checks["object_side_cp_odd_reachable"] = (object_bit(0.25) == "CP-ODD")
    # --- and the object-side reading can FAIL (not vacuous) ---
    checks["object_side_can_fail_not_torsion"] = (
        object_bit(0.1) == "NOT-2-TORSION")
    checks["object_side_can_fail_chiral"] = (
        object_bit(0.0, amphichiral=False) == "UNDEFINED-CHIRAL")

    # --- Both elements reachable on the reader side (hypothetical labels) ---
    checks["reader_side_cp_even_reachable"] = (
        reader_bit("CONSISTENT-WITH-CP-EVEN-POINT") == "CP-EVEN")
    checks["reader_side_cp_odd_reachable"] = (
        reader_bit("EXCLUDES-ALL-CP-EVEN-POINTS") == "CP-ODD")
    checks["reader_side_can_abstain"] = (
        reader_bit("UNRESOLVED") == "UNRESOLVED")

    # --- The comparison itself is two-sided: all four (object, reader)
    #     agree/disagree combinations are expressible ---
    outcomes = set()
    for ob in ("CP-EVEN", "CP-ODD"):
        for rb in ("CP-EVEN", "CP-ODD"):
            outcomes.add(("MATCH" if ob == rb else "MISMATCH"))
    checks["comparison_can_match_and_mismatch"] = outcomes == {"MATCH",
                                                              "MISMATCH"}

    print("=== SEALED-DESIGN BITE CONTROLS (hypotheticals only) ===")
    ok = True
    for k, v in checks.items():
        print(f"  {k}: {v}")
        ok = ok and v
    print(f"\nDESIGN BITE VERDICT: {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
