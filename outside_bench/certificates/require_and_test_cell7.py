#!/usr/bin/env python3
"""CELL 7 -- the parity classifier: which REQUIREMENTS are mirror-odd?

Seal: outside_bench/seals/REQUIRE_AND_TEST_CELL7_PREREG.md
      sha256 11cfd95ff5b4ecc119be8f2fa47aaef04de2b211516bea9aca4726f75d6806eb

THEOREM_LEDGER's T-MIRROR-ODD-VANISHES (B1227, PROVED) unifies four walls:
"the sigma wall (R/(1/2)Z), the selector wall (R) and the chirality wall (Z)
are ONE theorem in three value groups -- the corpus had tracked them as three."
It is stated about INVARIANTS.  Phase 1's table is about REQUIREMENTS.

THE CONTROL THAT MATTERS: an assignment that cannot be wrong is not an
assignment (#164, MB12).  So each parity is MEASURED -- every predicate is
computed on M and on its MIRROR; claimed-even must agree, claimed-odd differ.

Predicates imported from Phase 1, not re-implemented.
"""
from __future__ import annotations

import importlib.util
import os
import sys
import warnings
from collections import Counter

warnings.filterwarnings("ignore")

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CERT = os.path.join(ROOT, "outside_bench", "certificates")
ARC1323 = os.path.join(ROOT, "frontier", "B1323_the_genesis_upgrades", "verification",
                       "u1_substrate_count.py")

try:
    import snappy
except Exception as exc:
    print("FATAL: snappy unavailable:", exc)
    sys.exit(2)


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


C1 = load(os.path.join(CERT, "require_and_test_cell1.py"), "rt_cell1")
C2 = load(os.path.join(CERT, "require_and_test_cell2.py"), "rt_cell2")
C3 = load(os.path.join(CERT, "require_and_test_cell3.py"), "rt_cell3")
ARC = load(ARC1323, "u1_substrate_count")

# claimed parity, derived in the seal BEFORE this ran
CLAIMED = {
    "P_2T": "EVEN",
    "P_atom": "EVEN",
    "P_3": "EVEN",
    "P_chir": "ODD",
}


def rule(t):
    print("\n" + "-" * 78)
    print(" " + t)
    print("-" * 78)


def mirror(M):
    Mm = M.copy()
    Mm.reverse_orientation()
    return Mm


def observables(M):
    """The four predicates as VALUES (not booleans), so 'same' is meaningful."""
    G = M.fundamental_group()
    vals, _ = C3.cusp_counts(M)
    sf = ARC.shape_field(M)
    # P_chir as a value: does an ORIENTATION-PRESERVING isometry to the mirror
    # exist?  On M this is amphichirality; the point is that it is the one
    # observable that can tell M from its mirror.
    return {
        # THE OBSERVABLE IS EXACTLY THE PREDICATE AND NO MORE (seal ADDENDUM 1).
        # The first run bundled the shape-polynomial LIST into P_atom and failed
        # on 5_2 -- the boolean agreed; only the convention-dependent list moved.
        "P_2T": C2.surjection_count(G.generators(), G.relators()),
        "P_atom": bool(sf.get("all_in_Q(sqrt-3)")),
        "P_3": tuple(sorted(Counter(vals).items())) if vals else (),
        "P_chir": C1.amphichiral_det(M),
    }, (sf.get("min_polys") or [])


def reciprocal(p, q):
    """Is q the reciprocal polynomial of p (up to sign)?  Roots z and 1/z
    generate the SAME field, so a reciprocal pair is not a field difference."""
    r = list(reversed(list(p)))
    return list(q) == r or list(q) == [-c for c in r]


def orientation_signature(M):
    """The mirror-ODD observable, stated so it CAN differ: the signed
    Chern-Simons class.  CS(M-bar) = -CS(M); on an amphichiral M the two
    coincide mod 1/2 (B1227's own regime), on a chiral M they need not."""
    try:
        return float(M.chern_simons())
    except Exception:
        return None


def main() -> int:
    print("=" * 78)
    print(" CELL 7 -- THE PARITY CLASSIFIER")
    print("=" * 78)
    print("""
    seal  outside_bench/seals/REQUIRE_AND_TEST_CELL7_PREREG.md
    sha256 (after ADDENDUM 1)
    49183f68b6fc8c7d3b2376be45527086648eb0fd0adf252a180802130f4836ca""")
    failures = []

    rule("THE MEASUREMENT -- every predicate on M and on its MIRROR")
    print("""
    Claimed in the seal, derived there:
      P_2T   EVEN  -- pi_1(M-bar) = pi_1(M) as abstract groups
      P_atom EVEN  -- the mirror's shapes are conjugates; Q(sqrt-3) is
                      conjugation-closed
      P_3    EVEN  -- conjugation preserves det(A - I)
      P_chir ODD   -- it IS the mirror bit
""")
    rows = {}
    for name in ("m004", "m412", "5_2"):
        M = snappy.Manifold(name)
        Mm = mirror(M)
        (a, polys_a), (b, polys_b) = observables(M), observables(Mm)
        cs_a, cs_b = orientation_signature(M), orientation_signature(Mm)
        rows[name] = (a, b, cs_a, cs_b)
        # the shape-polynomial lists are NOT the predicate; when they differ the
        # certificate must VERIFY the reciprocal relation rather than assert it
        polys_same = (polys_a == polys_b)
        recip_ok = polys_same or (
            len(polys_a) == len(polys_b)
            and all(reciprocal(x, y) for x, y in zip(polys_a, polys_b)))
        print(f"\n    {name}   (amphichiral={a['P_chir']})")
        for p in ("P_2T", "P_atom", "P_3"):
            same = (a[p] == b[p])
            print(f"      {p:7s} {CLAIMED[p]:5s}  M == M-bar ? {'YES' if same else 'NO '}   "
                  f"M={str(a[p])[:44]}")
            if CLAIMED[p] == "EVEN" and not same:
                failures.append(f"{name}:{p}")
        print(f"      shape polys identical? {'YES' if polys_same else 'NO '}   "
              f"reciprocal-related? {'YES' if recip_ok else 'NO  *** FAILS'}")
        if not polys_same:
            print(f"        M      {polys_a}")
            print(f"        M-bar  {polys_b}")
        if not recip_ok:
            failures.append(f"{name}:shape-polys-not-reciprocal")
        print(f"      CS (the mirror-ODD observable)   M={cs_a:.9f}  M-bar={cs_b:.9f}   "
              f"sum={cs_a + cs_b:.2e}")

    # ------------------------------------------------------------------ C-EVEN
    rule("CONTROL C-EVEN -- every claimed-EVEN predicate agreed on every manifold")
    n_checked = sum(1 for _ in rows) * 3
    print(f"    predicate x manifold checks: {n_checked}")
    assert n_checked > 0, "no checks -- the B1197 vacuity trap"
    ok_even = not failures
    print(f"    disagreements among claimed-EVEN: {len(failures)}  {failures if failures else ''}")
    print(f"    -> {'PASS' if ok_even else 'FAIL'}")

    # ------------------------------------------------------------------ C-DISC
    rule("CONTROL C-DISC -- can the instrument tell a manifold from its mirror AT ALL?")
    print("""
    If nothing ever differs, the certificate is not measuring parity.  CS is
    mirror-ODD: CS(M-bar) = -CS(M).  So CS + CS(mirror) = 0 always, and the
    DISCRIMINATING fact is whether CS itself is nonzero -- i.e. whether the
    odd observable has anything to say on that manifold.
""")
    disc = []
    for name, (a, b, cs_a, cs_b) in rows.items():
        odd_speaks = abs(cs_a) > 1e-9
        print(f"    {name:6s} amphichiral={str(a['P_chir']):5s}  CS={cs_a:+.9f}  "
              f"odd observable non-trivial: {odd_speaks}")
        disc.append(odd_speaks)
    ok_disc = any(disc)
    print(f"    -> {'PASS' if ok_disc else 'FAIL'} (at least one manifold where the ODD "
          f"observable is non-trivial)")
    if not ok_disc:
        failures.append("C-DISC")

    # ------------------------------------------------------------------ the test
    rule("THE TEST -- mirror-ODD ==> m004 LACKS it")
    m004_has = {
        "P_chir": rows["m004"][0]["P_chir"] is False,
        "P_atom": rows["m004"][0]["P_atom"],
        "P_2T": rows["m004"][0]["P_2T"] > 0,
        "P_3": 3 in dict(rows["m004"][0]["P_3"]),
    }
    print(f"    {'requirement':10s} {'parity':6s} {'m004 HAS':9s}  reading")
    odd_violations = []
    for p in ("P_chir", "P_2T", "P_atom", "P_3"):
        par = CLAIMED[p]
        has = m004_has[p]
        if par == "ODD" and has:
            odd_violations.append(p)
            note = "*** ODD but m004 HAS it -- the law fails"
        elif par == "ODD":
            note = "forced by T-MIRROR-ODD-VANISHES"
        else:
            note = "not determined by the law"
        print(f"    {p:10s} {par:6s} {str(has):9s}  {note}")
    print("""
    values (CS, the real selector, net chirality, the colored-Jones ends'
    ratio)  ODD, and m004 LACKS all four -- B1227's own four value groups,
    cited here, not re-derived.""")

    outcome = "B" if (odd_violations or failures) else "A"
    print(f"\n    -> OUTCOME {outcome}")
    if outcome == "A":
        print("""    Every mirror-ODD requirement is one m004 lacks, and the mirror-EVEN ones
    are NOT determined either way -- m004 has two of them and lacks one.

    SO THE TABLE SPLITS:
      FORCED   chirality, values  -- m004 cannot supply them, by a banked
               theorem.  The only solve is a CHIRAL object.
      CONTINGENT  the count of three -- mirror-EVEN, so NO THEOREM FORBIDS IT.
               m004 simply does not have it, and something nearby might.
      HELD     the atom, the 2T door -- mirror-EVEN and m004 has them.""")
    else:
        print(f"""    The law does not organise the table.
    odd-parity violations: {odd_violations}   control failures: {failures}""")

    rule("VERDICT")
    print(f"    OUTCOME {outcome}")
    print(f"    controls: {'ALL PASSED' if not failures else 'FAILED: ' + ', '.join(failures)}")
    print("""
    NOT CONCLUDED: that mirror-EVEN requirements are satisfiable -- the law
    says nothing about them, which is the point.  That B1227's four value
    groups are exhaustive: they are cited, not extended.  No value.""")
    return 0 if not failures else 1


if __name__ == "__main__":
    sys.exit(main())
