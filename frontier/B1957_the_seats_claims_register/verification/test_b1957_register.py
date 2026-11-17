"""B1957's lock: the register's state is what the units and the records give, and nothing is settled without a record."""
import json, pathlib, sys
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import build


def test_every_unit_is_registered_once_and_every_record_names_real_units():
    U, ids, status, read = build.state()
    assert len(ids) == len(U["units"]) and len(U["files"]) == sum(1 for f in U["files"])
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
    assert "HARVEST COMPLETE" not in page or all(L["PENDING"] == 0 for L in lanes.values())
