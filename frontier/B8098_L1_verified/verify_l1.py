#!/usr/bin/env python3
"""B8098 -- L1's sharpest sub-claim, verified in-sandbox with SnapPy.

B985 flagged L1 as OVER-WIDE: proved as "m004 extremal along the metallic diagonal m=1..7",
banked as "m004 is THE selected object" -- noting that criterion 3 (arithmeticity) is
class-invariant and cannot discriminate, and that criterion 1 already TIES with m003.

This verifies the two checkable halves directly. Gate 5 untouched.
"""
import json, os
import snappy
HERE = os.path.dirname(os.path.abspath(__file__))
FAIL = []
def gate(l, ok, d=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {l}" + (f"  {d}" if d else ""))
    if not ok: FAIL.append(l)

A, B = snappy.Manifold('m003'), snappy.Manifold('m004')
va, vb = float(A.volume()), float(B.volume())
ha, hb = str(A.homology()), str(B.homology())
print(f"  m003: volume {va}  H_1 = {ha}")
print(f"  m004: volume {vb}  H_1 = {hb}")

print("\nCRITERION 1 -- VOLUME")
gate("m003 and m004 are ISOVOLUMETRIC to 1e-12", abs(va - vb) < 1e-12, f"|diff| = {abs(va-vb):.2e}")
gate("=> criterion 1 CANNOT discriminate the object from its sister", abs(va - vb) < 1e-12)

print("\nL73's FALSIFICATION -- the torsion at the hearing prime")
gate("m004 is torsion-free (H_1 = Z)", hb.replace(' ','') == 'Z')
gate("m003 has Z/5 torsion at the hearing prime", 'Z/5' in ha.replace(' ',''))
print("    'A property that fails inside the commensurability class is not a property")
print("     of the class' -- B985. Confirmed here independently.")

print("\nCRITERION 3 -- ARITHMETICITY (theorem, not computed here)")
print("""    Arithmeticity is a COMMENSURABILITY INVARIANT (Reid; banked as B803), and m003
    and m004 are commensurable (B985: index 12 in PSL(2,O_-3)). A class invariant takes
    the same value on every member, so criterion 3 cannot discriminate BY THEOREM --
    no computation can rescue it.""")

print("\nOBSERVATION, unweighted (B888 discipline) -- no mechanism claimed")
print("""    The Z/5 that the external Wilson-line proposal required, and that B8086 showed
    m004 does NOT have, is present on m003 -- the isovolumetric sister in the same
    commensurability class. This does NOT rescue that proposal (m003 is not the object
    either). It locates where the Z/5 lives: in the class, not on the member.""")

RES = {"m003": {"volume": va, "homology": ha}, "m004": {"volume": vb, "homology": hb},
       "isovolumetric": abs(va - vb) < 1e-12, "volume_diff": abs(va - vb),
       "criterion_1_can_discriminate": False,
       "criterion_3_can_discriminate": False,
       "criterion_3_reason": "arithmeticity is a commensurability invariant (Reid; B803) and m003 ~ m004 (index 12 in PSL(2,O_-3)) -- cannot discriminate BY THEOREM",
       "m004_torsion_free": hb.replace(' ','') == 'Z',
       "m003_has_Z5": 'Z/5' in ha.replace(' ',''),
       "L73_falsification_confirmed": True,
       "observation_unweighted": "the Z/5 the Wilson-menu proposal needed is on m003, not m004 -- in the class, not on the member; no mechanism claimed",
       "scope": ("Verifies TWO of L1's five criteria as non-discriminating between m004 and its "
                 "sister m003: criterion 1 computationally (isovolumetric), criterion 3 by theorem "
                 "(class invariance). Says NOTHING about the remaining criteria, and does NOT show "
                 "the object is unselected -- it shows the selection rests on fewer criteria than "
                 "banked. Gate 5 untouched.")}
json.dump(RES, open(os.path.join(HERE, "results.json"), "w"), indent=1, sort_keys=True)
print("\n  results.json written")
if FAIL: raise SystemExit(f"FAILED: {FAIL}")
print("\n  ALL CHECKS PASS")
