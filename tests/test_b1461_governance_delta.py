"""B1461 -- Review 58's governance delta switched on: the review fires, carried items age, the core gains three checks."""
import json, os, sys, textwrap
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts", "gates")); sys.path.insert(0, os.path.join(ROOT, "scripts", "review"))
import gates, review_tools as rt


def test_the_four_gates_are_registered_and_green_on_the_record():
    for g in ("review-fires", "carry-age", "gate-controls", "review-core"):
        assert g in gates.GATES; ok, why = gates.GATES[g](); assert ok, (g, why)
    assert gates.REVIEW_HARD == 40 and gates.CARRY_LIMIT == 3 and gates.REVIEW_CORE_FROM == 59


def test_review_fires_past_twice_the_period_unless_waived(monkeypatch):
    monkeypatch.setenv("OA_REVIEW_MERGES", "40")
    monkeypatch.setattr(gates, "_read", lambda rel: "" if rel == gates.REVIEW_WAIVER else open(os.path.join(ROOT, rel)).read())
    ok, why = gates.gate_review_fires(); assert ok is False and "FIRES" in why
    monkeypatch.setattr(gates, "_read", lambda rel: "- waived 2026-10-03 by the owner through 60 merges: reason\n" if rel == gates.REVIEW_WAIVER else open(os.path.join(ROOT, rel)).read())
    monkeypatch.setattr(os.path, "isfile", lambda p: True)
    ok, why = gates.gate_review_fires(); assert ok is True and "waived" in why
    monkeypatch.setenv("OA_REVIEW_MERGES", "61"); assert gates.gate_review_fires()[0] is False   # the waiver expired
    monkeypatch.setenv("OA_REVIEW_MERGES", "39"); assert gates.gate_review_fires()[0] is True
    assert gates.review_waiver_covers(10, "") is False


REV = textwrap.dedent("""\
    # Review 60 (2026-11-01) — x

    ### Action items (Review 60)

    - [ ] R60-1: new (owner: cc)
    - [>] R57-1: carried (carried from R57)
    - [>] R57-2: carried — declined: the premise was withdrawn (carried from R57)
    - [>] R57-3: carried — waived by the owner 2026-11-01 (carried from R57)

    **anchor-commit: `abcdef12`**

    # Review 61 (2026-11-20) — y

    ### Action items (Review 61)

    - [>] R57-1: carried again (carried from R60)
    - [>] R57-2: declined: the premise was withdrawn (carried from R60)
    - [>] R57-3: waived by the owner 2026-11-01 (carried from R60)

    **anchor-commit: `abcdef34`**

    # Review 62 (2026-12-10) — z

    ### Action items (Review 62)

    - [>] R57-1: carried a third time (carried from R61)
    - [>] R57-2: declined: the premise was withdrawn (carried from R61)
    - [>] R57-3: waived by the owner 2026-11-01 (carried from R61)

    **anchor-commit: `abcdef56`**
    """)


def test_carry_age_fails_on_a_third_carry_without_disposition():
    bad = gates.carry_age_problems(REV); assert bad and bad[0].startswith("R57-1 carried 3 times") and len(bad) == 1
    assert gates.carry_age_problems(REV.replace("- [>] R57-1: carried a third time", "- [x] R57-1: paid")) == []
    # the baseline items are exempt only at the review the rule was switched on
    assert gates.carry_age_problems(REV, baseline_review=62, baseline=frozenset({"R57-1"})) == []
    assert gates.carry_age_problems(REV, baseline_review=61, baseline=frozenset({"R57-1"})) != []


def test_the_live_register_is_exactly_at_its_baseline():
    text = open(os.path.join(ROOT, "docs", "progress", "REVIEWS.md")).read()
    over = {k for k, n in rt.action_loop(text)["carried"] if n >= gates.CARRY_LIMIT}
    assert over <= gates.CARRY_BASELINE, over - gates.CARRY_BASELINE          # nothing new past the limit
    assert gates.carry_age_problems(text) == []


def test_gate_controls_fails_on_an_unregistered_gate_and_a_missing_function(tmp_path, monkeypatch):
    reg = json.load(open(os.path.join(ROOT, gates.GATE_CONTROLS)))
    partial = dict(reg); partial.pop("framing")
    monkeypatch.setattr(gates, "_read", lambda rel: json.dumps(partial) if rel == gates.GATE_CONTROLS else open(os.path.join(ROOT, rel)).read())
    ok, why = gates.gate_gate_controls(); assert ok is False and "framing" in why
    broken = dict(reg); broken["framing"] = "tests/test_gate_failing_paths.py::test_that_does_not_exist"
    monkeypatch.setattr(gates, "_read", lambda rel: json.dumps(broken) if rel == gates.GATE_CONTROLS else open(os.path.join(ROOT, rel)).read())
    ok, why = gates.gate_gate_controls(); assert ok is False and "not defined" in why
    monkeypatch.setattr(gates, "ROOT", str(tmp_path)); assert gates.gate_gate_controls()[0] is False   # file gone


def test_review_core_fails_on_an_entry_without_its_three_lines():
    old = "# Review 58 (2026-10-02) — x\n\nbody\n"; assert gates.review_core_missing(old) == []     # before the rule
    new = "# Review 59 (2026-10-20) — y\n\nbody without the lines\n"
    assert gates.review_core_missing(new) == list(gates.REVIEW_CORE_LINES)
    full = new + "fresh-clone: PASS @ abcdef12\nsample seed: abcdef00\ngate controls: 40 registered\n"
    assert gates.review_core_missing(full) == []
    assert gates.review_core_missing(old + full) == []        # only the latest entry is read


def test_review_tools_render_carries_the_core_lines():
    R = dict(window=dict(anchor="a", head="b", commits=1, first_parent=1, arcs_n=0, arcs=[], sealed_commits=[]),
             remotes=dict(mirrors=[], missing_mirrors=[], ignored=[]), loop=dict(review=59, open=[], carried=[], superseded_open=[]),
             branches=dict(rows=[], unregistered=[], on_one_remote_only=[], out_of_step=[]), seals=[],
             provenance=dict(lines_scanned=0, hits=[]), law_map_rows_added=[], theorem_rows_added=[], errors=dict(new_classes=[], instances=[]),
             terms=dict(unglossed=[]), gates=dict(controlled=0, uncontrolled=[], registered=40, unregistered=[]), relays={}, sample=["B1"],
             fresh_clone=dict(status="PASS", commit="abcdef12", detail="gates 40/40; belt ok"))
    out = rt.render(R)
    for l in gates.REVIEW_CORE_LINES: assert l in out, (l, out)


def test_the_waiver_file_exists_with_the_grammar_and_no_live_waiver():
    w = open(os.path.join(ROOT, gates.REVIEW_WAIVER)).read()
    assert "- waived <YYYY-MM-DD> by the owner through <N> merges: <reason>" in w
    assert gates.review_waiver_covers(40, w) is False
