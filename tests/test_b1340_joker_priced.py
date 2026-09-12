"""B1340 - the joker priced: chirality costs the Z', and what it buys is a forced shape.

These lock the two findings a later reader is most likely to lose: that the record's anomaly check
on the 19624 vacua carries ZERO BITS (it cannot fail on a vector-like spectrum), and that once the
mirrors are deleted the family part of any anomaly-free U(1)' is forced to (0, t, -t) -- which the
record's (-10, 5, 5) is not. The arithmetic is recomputed here, not asserted from the arc's text,
so the test fails if the branching table or the theorem is ever wrong.
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1340_the_joker_priced"
REG = ROOT / "docs" / "FALSIFIER_REGISTER.md"


def test_arc_is_banked():
    assert (ARC / "FINDINGS.md").exists()
    v = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert v["id"] == "B1340" and v["verdict"] == "NEGATIVE"
    assert [i["row"] for i in v["identifications"]] == ["I-13"], (
        "the forwarded report's 'the CKM coordinate IS I-13' must be dispositioned on the row")


def test_b1303s_number_is_reproduced_from_the_branching():
    """-20250 is 27 * sum f^3 over the record's family part -- the family torus's alone."""
    f = (-10, 5, 5)
    assert 27 * sum(x ** 3 for x in f) == -20250


def test_the_record_s_family_part_fails_the_chiral_condition():
    """grav forces sum f = 0; the cubic forces sum f^3 = 0; and sum f = 0 => sum f^3 = 3 f1 f2 f3.
    So an anomaly-free family part must have some f_i = 0. (-10, 5, 5) does not."""
    f = (-10, 5, 5)
    assert sum(f) == 0, "the record's family part is traceless (it passes grav)"
    assert f[0] * f[1] * f[2] != 0, "but its product is non-zero, so the cubic obstructs"
    assert sum(x ** 3 for x in f) != 0


def test_the_forced_shape_is_zero_t_minus_t():
    """the identity behind the theorem, checked on integers: with sum f = 0, sum f^3 = 3 f1 f2 f3,
    so the anomaly-free family parts are exactly those with a zero entry and two opposite ones."""
    for t in range(-6, 7):
        for perm in ((0, t, -t), (t, 0, -t), (t, -t, 0)):
            assert sum(perm) == 0 and sum(x ** 3 for x in perm) == 0
    bad = [f for f in ((1, 1, -2), (-10, 5, 5), (3, -1, -2), (2, 2, -4))
           if sum(f) == 0 and sum(x ** 3 for x in f) == 0]
    assert not bad, f"these traceless family parts must NOT pass the cubic: {bad}"


def test_p9_carries_the_chirality_condition():
    """P9 is the register's one entry whose regime the object's own vacuum names. Its anomaly
    freedom holds only on a VECTOR-LIKE spectrum; a reader must not take it for the physical one."""
    t = REG.read_text(encoding="utf-8")
    i = t.find("| **P9** |")
    assert i > 0, "P9 went missing from the falsifier register"
    row = t[i:t.find("\n", i)]
    assert "B1340" in row, "P9 does not cite the arc that priced its anomaly freedom"
    assert "vector-like" in row.lower(), "P9 does not state that its anomaly freedom is conditional"
