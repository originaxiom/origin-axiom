"""B1957's lock: the register's state is what the units and the records give, and nothing is settled without a record."""
import json, pathlib, sys
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import build


def test_every_unit_is_registered_once_and_every_record_names_real_units():
    U, ids, status, read = build.state()
    assert len(ids) == len(U["units"]) and len(ids) == len(set(ids))                    # mended at Review 84: the second clause compared a length with itself
    per, lanes = build.summary()
    assert sum(1 for u in U["units"] if u[2] == "s") == sum(L["statements"] for L in lanes.values())     # every statement is in one lane's count
    for uid, (verdict, rid) in status.items():
        assert uid in ids and verdict in build.VERDICTS


def test_the_summary_is_the_state():
    per, lanes = build.summary()
    S = json.loads((HERE / "SUMMARY.json").read_text())
    assert S["lanes"] == json.loads(json.dumps(lanes)) and S["files"] == json.loads(json.dumps(per))
    for L in lanes.values():
        assert L["statements"] == L["PENDING"] + sum(L[v] for v in build.VERDICTS)


def test_no_lane_is_called_complete_while_a_statement_is_pending():
    per, lanes = build.summary()
    page = (HERE.parent / "REGISTER.md").read_text()
    for n, L in lanes.items():
        assert ("| %s | %d | %d | %d |" % (n, L["files"], L["read"], L["statements"])) in page
    # mended at Review 84: the line below read `"HARVEST COMPLETE" not in page or ...`, which could not fail (the generated
    # page never carries the words).  What can be held here: the page shows each lane's pending count as the state has
    # it, and main's own page of the arc says a lane has none pending only where the state agrees.
    for n, L in lanes.items():
        row = next(l for l in page.split("\n") if l.startswith("| %s |" % n)); assert row.rstrip().endswith("| **%d** |" % L["PENDING"]), (n, row[-40:])
    verdict = json.loads((HERE.parent / "arc_verdict.json").read_text())
    assert verdict["verdict"] == "OPEN" or all(L["PENDING"] == 0 for L in lanes.values())


def test_the_verdict_file_carries_no_count_that_the_summary_does_not():
    """added at Review 84: the verdict file said 275 files and 14,878 statements while the summary said 406 and 20,863"""
    import re
    per, lanes = build.summary(); verdict = json.loads((HERE.parent / "arc_verdict.json").read_text())
    text = verdict["claim_one_line"] + " " + " ".join(str(v) for v in verdict["scope"].values())
    files = sum(L["files"] for L in lanes.values()); statements = sum(L["statements"] for L in lanes.values())
    for m in re.finditer(r"([\d,]+) (?:markdown )?files", text): assert int(m.group(1).replace(",", "")) == files, m.group(0)
    for m in re.finditer(r"([\d,]+) statements", text): assert int(m.group(1).replace(",", "")) == statements, m.group(0)
