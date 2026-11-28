"""2026-11-26 (the framework's thin path, patch T6; main's M54 and M55; register row P-885): the record check,
scripts/queue/record_check.py.

"deciding" is computed from what the card touches and its effect, planted case by case; a premise card that is not
VERIFIED is waited on (door rule D6); words of a comparison with data raise the firewall's flag (the author's rule A3);
a premise arc that is RETRACTED or superseded, and a retracted phrase on the card, are found on the record itself; the
sweep's terms are the runner's, not the producer's line; the topic sweep and the already-banked check run on the record;
the command runs by hand."""
import glob
import importlib.util
import json
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location("record_check_under_test", ROOT / "scripts/queue/record_check.py")
RC = importlib.util.module_from_spec(_spec)
sys.dont_write_bytecode = True
_spec.loader.exec_module(RC)

CARD = """# CLAIM CARD — the classes at level five of the figure-eight cover, counted

- card id: new
- seat code: fam2-v5-high-01
- touches: {touches}
- effect: {effect}
- premises on main: {premises}
- already on main?: none found
"""


def _card(touches="P-885", effect="supports — P-885", premises="none"):
    return CARD.format(touches=touches, effect=effect, premises=premises)


def _fields(**kw):
    return RC.CF.read(_card(**kw))[1]


def test_deciding_is_computed_from_what_the_card_touches():
    for touches, want in (("P-885", True), ("I-26", True), ("A03", True), ("the Higgs mass", True),
                          ("B2011", False), ("none", False), ("a lemma of the record", False)):
        effect = "none" if touches == "none" else "supports — " + touches
        assert RC.deciding(_fields(touches=touches, effect=effect)) is want, touches
    assert RC.deciding(_fields(touches="P-885", effect="none")) is False


def test_a_premise_card_that_is_not_verified_is_waited_on_d6():
    f = _fields(premises="B2011, Q0003, Q0004 and Q0005")
    queue = {"Q0003": {"status": "VERIFIED"}, "Q0004": {"status": "REPRODUCED"}}
    assert RC.waits_on(f, queue) == ["Q0004", "Q0005"]
    assert RC.waits_on(_fields(premises="B2011"), queue) == []


def test_words_of_a_comparison_with_data_raise_the_firewall_flag_a3():
    assert RC.firewall(_card()) == []
    for words in ("its value against the PDG average", "0.2312 ± 0.0004", "compared with data at the Z pole",
                  "a sealed look at the angle", "experimentally 125 GeV"):
        assert RC.firewall(_card() + "- note: " + words + "\n"), words


def test_a_retracted_or_superseded_premise_and_a_retracted_phrase_are_found_on_the_record():
    gone = sup = None
    for v in sorted(glob.glob(str(ROOT / "frontier" / "B*" / "arc_verdict.json"))):
        d = json.loads(pathlib.Path(v).read_text(encoding="utf-8"))
        n = pathlib.Path(v).parent.name.split("_", 1)[0]
        if gone is None and d.get("verdict") == "RETRACTED":
            gone = n
        if sup is None and d.get("superseded_by"):
            sup = n
    assert gone and sup
    text = _card(premises="%s, %s" % (gone, sup))
    out = RC.retracted(ROOT, RC.CF.read(text)[1], text)
    assert any(p.startswith(gone + " is RETRACTED") for p in out["premises"])
    assert any(p.startswith(sup + " is superseded by") for p in out["premises"])
    rs = RC._load("retraction_sweep_for_the_test", ROOT / "scripts/checks/retraction_sweep.py")
    phrase = rs.phrases_in((ROOT / "docs" / "RETRACTED_PHRASES.md").read_text(encoding="utf-8"))[0]
    text = _card() + "- note: " + phrase + "\n"
    assert RC.retracted(ROOT, RC.CF.read(text)[1], text)["phrases"] == [phrase]
    assert RC.retracted(ROOT, _fields(premises="B335"), _card(premises="B335")) == {"premises": [], "phrases": []}


def test_the_sweeps_terms_are_the_runners_and_the_sweeps_run_on_the_record():
    res = RC.check(ROOT, _card(touches="P-885", premises="B2011, Q0003"))
    assert res["terms"]["codes"] == ["B2011", "P-885"] and "figure-eight" in res["terms"]["words"]
    assert res["producer_sweep"] == "none found"                  # kept as the producer's claim, not used
    assert res["topic"]["verdict"].startswith("VERDICT topic-sweep") and "B2011" in res["topic"]["matches"]
    assert res["banked"]["settled_or_scheduled"] in (True, False)
    assert res["deciding"] is True and res["waits_on"] == ["Q0003"] and res["firewall"] == []


def test_the_command_runs_by_hand(tmp_path):
    f = tmp_path / "CLAIM_a.md"
    f.write_text(_card(premises="Q0009"), encoding="utf-8")
    r = subprocess.run([sys.executable, "-B", str(ROOT / "scripts/queue/record_check.py"), str(f), "--queue",
                        str(tmp_path / "none")], capture_output=True, text=True, timeout=600)
    assert r.returncode == 0 and json.loads(r.stdout)["waits_on"] == ["Q0009"]


def test_review_88s_rules_on_the_record_check_t7b():
    """main's M61 (the law map; D6 on a premise arc with its own card) and M64 items 15 to 17, each planted"""
    # 15: the 19 by plural and common names, the scoreboard in any case, the law map's rows
    for touches in ("the quark Yukawas", "the Weinberg angle", "a03", "LISTENING 26", "the neutrino masses"):
        effect = "conditions — " + touches
        assert RC.deciding(_fields(touches=touches, effect=effect)) is True, touches
    # 16: the firewall's words
    for words in ("the measured values", "compared to data", "a comparison with data", "0.23 +/- 0.01",
                  "it agrees with experiment", "fitted to the data"):
        assert RC.firewall(_card() + "- note: " + words + "\n"), words
    # 17: the title's words beyond six are said, not dropped in silence
    long_title = "# CLAIM CARD — alpha bravo charlie delta echoes foxtrot golfing hotel indigo"
    codes, used, left = RC.terms({}, long_title.split("— ", 1)[1])
    assert len(used) == 6 and left and set(used) | set(left) == {"alpha", "bravo", "charlie", "delta", "echoes", "foxtrot",
                                                                 "golfing", "hotel", "indigo"}
    # M61.2: a premise arc that has its own card in the queue is waited on until that card is VERIFIED
    queue = {"Q0003": {"status": "REPRODUCED", "seat_code": RC.CF.QS.MAIN_CODE, "title": "B2011 A1: a count",
                       "card_path": "relays/claims/CLAIM_2026-11-27_B2011_main_trial.md"},
             "Q0004": {"status": "VERIFIED", "seat_code": RC.CF.QS.MAIN_CODE, "title": "B2012 a count",
                       "card_path": "relays/claims/CLAIM_2026-11-27_B2012_main_trial.md"}}
    assert RC.waits_on(_fields(premises="B2011, B2012"), queue) == ["Q0003"]
    assert RC.waits_on(_fields(premises="B335"), queue) == []


def test_a_card_never_waits_on_itself():
    """ADDED 2026-11-28 (M78 point 3): B2011's card names its own arc in its premises, and waited on its own id"""
    queue = {"Q0001": {"status": "FILED", "branch": "main", "card_path": "relays/claims/CLAIM_2026-11-27_B2011_main_trial.md",
                       "seat_code": "fam1-v1-unset-01", "arc": 2011}}
    own = {k: v for k, v in queue.items()}
    got = RC.waits_on(_fields(premises="B2002 (rebuilt in B2011's sectors_exact.py)"), own, "Q0001")
    assert "Q0001" not in got
    named = RC.waits_on(_fields(premises="Q0001"), own, "Q0002")
    assert named == ["Q0001"]                       # another card still waits on it


def test_the_firewall_flags_a_measured_value_with_its_error_and_not_a_sign_in_mathematics_m81():
    """main's M81 point 3: round 1 flagged Q0008's "x modulo ±" (a sign class) and Q0042's "3a ≡ ±1/5 mod 1" (a
    congruence). "±" is flagged before a number with a decimal point, or between a number and its uncertainty"""
    for line in ("the classes of x modulo ±", "3a ≡ ±1/5 mod 1", "a sign ± 1 on each leg"):
        assert RC.firewall(_card() + "- note: " + line + "\n") == [], line
    for line, got in (("0.2312 ± 0.0004", "0.2312 ± 0.0004"), ("12 ± 3 events", "12 ± 3"), ("0.23 +/- 0.01", "0.23 +/- 0.01"),
                      ("a mass ± 0.5 GeV", "± 0.5")):
        assert RC.firewall(_card() + "- note: " + line + "\n") == [got], line
