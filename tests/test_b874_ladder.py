"""Locks B874 -- the measurement ladder."""
import json
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
_D = _ROOT / "frontier" / "B874_measurement_ladder"
RES = json.loads((_D / "results.json").read_text(encoding="utf-8"))
_F = " ".join((_D / "FINDINGS.md").read_text(encoding="utf-8").split()).lower().replace("*", "")


def test_the_census_is_a_two_value_cliff():
    c = RES["census"]
    assert len(c) == 15
    soft = {"x8", "x16", "x8+x16"}
    for k, v in c.items():
        assert v == (30 if k in soft else 12), (k, v)


def test_the_ladder_values():
    assert RES["ladder"] == [30, 12]


def test_cent_c_structure():
    assert RES["cent_dim"] == 12 and RES["closure_ok"] is True
    assert RES["derived_dim"] == 8 and RES["center_dim"] == 4


def test_derived_is_a2_su21_by_nondegenerate_killing_and_signature():
    assert RES["killing_rank"] == 8
    assert RES["killing_signature"] == [4, 4, 4]
    assert RES["derived_type"].startswith("A2")
    assert "su(2,1)" in RES["derived_real_form"]


def test_full_measurement_is_not_the_sm_stated_plainly():
    assert RES["full_measurement_is_sm"] is False
    assert 'the "full measurement = sm" reading is dead' in _F


def test_no_dictionary_asserted_and_step2_question_stays_open():
    assert "no dictionary to color is asserted" in _F
    assert "remains open" in _F


JOINT = json.loads((_D / "joint_results.json").read_text(encoding="utf-8"))


def test_addendum_enhancement_confirmed_at_13x_roots():
    """kern(s1) = 46 at every 13x-scaled banked root -- the normalization fact
    reconfirmed at the source."""
    assert JOINT["enhancement_confirmed_at_13x"] is True
    assert all(r["kern_s1"] == 46 for r in JOINT["rows"]) and len(JOINT["rows"]) == 3


def test_addendum_no_26_stratum_step2_not_retired():
    assert JOINT["no_26_stratum"] is True
    assert all(r["joint_x14"] == 12 and r["joint_x22"] == 12 for r in JOINT["rows"])
    assert "closes negatively for the object's 2t-charge system" in _F
    assert "the ranking is not retired by charge measurement" in _F


def test_the_verdict_line_scopes_its_ladder_and_says_where_each_statement_comes_from():
    """Added 2026-11-12 (Review 79's second round).  The verdict line called the ladder complete; the arc's own page had amended
    it twice.  The scope stands beside the old words now, and it says which part main computed and which is a seat's relay."""
    import json, pathlib
    arc = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B874_measurement_ladder"
    line = json.loads((arc / "arc_verdict.json").read_text(encoding="utf-8"))["claim_one_line"]
    old = "the complete ladder is {78, 46, 30, 12}"
    assert line.count(old) == 1
    after = line[line.index(old):]
    assert "SCOPED 2026-11-12" in after[:400] and "COMPUTED ON MAIN (B892)" in after and "BY THE AUDIT SEAT'S RELAY" in after and "locks not imported" in after
    # ADDED 2026-11-12 (Review 80; the SM seat's finding 41, not checked by main, made again here).  The line above asks for
    # four labels.  It does not ask what stands under them: a reader planted two false statements in the bracket and both
    # passed.  What main computed is held to B892's own kept check, and what is the seat's relay is held word for word.
    assert _what_the_bracket_says(after) == []
    # ADDED 2026-11-13 (C16; the same finding): a third, false sentence after the two, and one before them, are reported; the
    # twin, a dated note added inside the bracket, is not (what a note says is not read here, and the test says so)
    for planted in (after.replace("with 30 and 46 degenerately.", "with 30 and 46 degenerately. So the ladder is complete after all.", 1),
                    after.replace("The ladder is not complete as stated.", "The ladder is complete. The ladder is not complete as stated.", 1)):
        assert planted != after and _what_the_bracket_says(planted)
    noted = after.replace("with 30 and 46 degenerately.", "with 30 and 46 degenerately. [NOTED 2026-11-13: a note.]", 1)
    assert noted != after and _what_the_bracket_says(noted) == []
    for false, where in (("all real, to 16 and to 26", "all imaginary, to 14 and to 18"), ("so on the real line it reaches 26", "so on the real line it is 12 at every point but the plane stratum's")):
        planted = after.replace(where, false)
        assert planted != after and "COMPUTED ON MAIN (B892)" in planted and "BY THE AUDIT SEAT'S RELAY" in planted      # the four labels stand
        assert _what_the_bracket_says(planted), false


def _what_the_bracket_says(after):
    """what is wrong in the scope bracket of B874's verdict line, as a list: its two parts against their sources"""
    import json, pathlib
    out = []
    main_part = "COMPUTED ON MAIN (B892): on the line through a wall point the nullity jumps at four points, all imaginary, to 14 and to 18, so on the real line it is 12 at every point but the plane stratum's."
    if main_part not in after:
        out.append("what main computed is not stated as B892's check W3 states it")
    b892 = json.loads((pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B892_second_measurement" / "verification" / "walls_on_the_line.json").read_text(encoding="utf-8"))
    w3 = [k for k in b892 if k.startswith("W3 the walls at finite t are four, all purely imaginary: nullity 14 at a conjugate pair and nullity 18 at another; so on the real line the nullity is 12 at every point but pure x16")]
    if len(w3) != 1 or b892[w3[0]] is not True:
        out.append("B892's kept run does not hold the check W3")
    relay = "over the algebraic closure the strata from a wall point are {12, 14, 16, 18, 20, 26}, the 26 being attained at four points, and over the reals {12, 16, 18}, with 30 and 46 degenerately."
    if relay not in after or after.index(relay) < after.index("BY THE AUDIT SEAT'S RELAY"):
        out.append("the seat's strata are not as the relay gave them, or do not stand under the relay's label")
    if after.index("COMPUTED ON MAIN (B892)") > after.index("BY THE AUDIT SEAT'S RELAY") or main_part in after[after.index("BY THE AUDIT SEAT'S RELAY"):]:
        out.append("what main computed stands under the relay's label")
    # ADDED 2026-11-13 (C16; a cold reader's finding on R80b's part 3, patch 6, not checked by main, made again first).  The two
    # sentences above were held word for word, and a third, false sentence after them passed.  The bracket's own text, outside
    # the dated notes that stand inside it, is held whole: nothing is added to it and nothing taken out.
    if _the_brackets_own_text(after) != _THE_BRACKETS_OWN_TEXT:
        out.append("the scope bracket says something more, or less, than its four sentences")
    return out


_THE_BRACKETS_OWN_TEXT = " ".join((
    "SCOPED 2026-11-12 (Review 79; the scope this arc's page has carried since its amendments of 2026-08-05 and 2026-08-18 had not",
    "reached this line): that is the answer to the question the coordinate tests ask, a second charge on x14 or x22. The ladder is",
    "not complete as stated. COMPUTED ON MAIN (B892): on the line through a wall point the nullity jumps at four points, all",
    "imaginary, to 14 and to 18, so on the real line it is 12 at every point but the plane stratum's. BY THE AUDIT SEAT'S RELAY of",
    "2026-08-15, entered in this arc's addendum of 2026-08-18 with its backbone verified on the bench and its locks not imported:",
    "over the algebraic closure the strata from a wall point are {12, 14, 16, 18, 20, 26}, the 26 being attained at four points,",
    "and over the reals {12, 16, 18}, with 30 and 46 degenerately."))


def _the_brackets_own_text(after):
    """the text of the scope bracket that is not inside a bracket of its own (its dated notes), with its spaces made single"""
    start = after.find("[SCOPED 2026-11-12")
    if start == -1:
        return None
    depth, keep = 0, []
    for c in after[start:]:
        if c == "[":
            depth += 1
            if depth > 1:
                continue
        elif c == "]":
            depth -= 1
            if depth == 0:
                break
            continue
        elif depth == 1:
            keep.append(c)
    return " ".join("".join(keep).split()) if depth == 0 else None

