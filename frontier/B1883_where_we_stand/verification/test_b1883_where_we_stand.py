"""B1883 lock -- the status page is its builder's output, its numbers are its sources', and each refusal fires.

What could fail: a committed page that is not what the builder gives; a number on the page that is not the programme's, the
map's or the register's; a refusal that no planted disagreement can make fire."""
import copy
import importlib.util
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[3]
ARC = pathlib.Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("build_where_we_stand_lock", ARC / "verification" / "build_where_we_stand.py")
bw = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bw)
B = bw.build()
P = json.loads(bw.PROGRAMME.read_text(encoding="utf-8"))


def test_the_committed_page_is_the_builders_output():
    assert B["fails"] == []
    for name, text in bw.generated(B).items():
        assert (ARC / name).read_text(encoding="utf-8") == text, name


def test_every_number_is_a_sources_number():
    S, st = B["stats"], P["stats"]
    assert S["packages"]["all"] == st["packages"] == len(P["packages"])
    assert (S["packages"]["done"], S["packages"]["started"], S["packages"]["not_started"]) == (
        st["packages_by_status"].get("DONE", 0), st["packages_by_status"].get("STARTED", 0), st["packages_by_status"].get("NOT STARTED", 0))
    assert S["map"]["nodes"] == len(json.loads(bw.NODES.read_text(encoding="utf-8"))) and S["map"]["nodes_that_need_a_path"] == st["nodes_needing_a_path"]
    assert S["put_in_by_hand"]["independent_choices"] == st["independent_choices"] == len(P["inputs"])
    assert S["audit"]["by_state"] == st["audit_findings_by_state"] and sum(S["audit"]["by_state"].values()) == S["audit"]["findings"]
    assert S["values_earned"] == json.loads(bw.SCOREBOARD.read_text(encoding="utf-8"))["earned"]
    # the register, by a recount written apart from the builder's
    rows = [l.split(" | ") for l in bw.REGISTER.read_text(encoding="utf-8").split("\n") if re.match(r"^\| P-\d+ \|", l)]
    rows = [c for c in rows if len(c) == 7]
    assert S["register"]["points"] == len(rows) and S["register"]["open"] == sum(c[4] in ("QUEUED", "LEAD", "OWNER") for c in rows)
    assert S["register"]["owner_calls_open"] == [c[0][2:] for c in rows if c[4] == "OWNER"]
    assert sum(m["packages"] for m in S["milestones"]) == len(P["packages"]) and [m["id"] for m in S["milestones"]] == ["M1", "M2", "M3"]


def test_ready_means_the_card_and_everything_it_waits_on():
    S = B["stats"]
    assert S["ready_for_the_final_reading"] is False and "**Ready for the final reading: NO.**" in (ARC / "WHERE_WE_STAND.md").read_text(encoding="utf-8")
    prog = copy.deepcopy(P)
    for p in prog["packages"]:
        if p["title"] == "The sealed card" or p["id"] in prog["stats"]["packages_the_sealed_card_must_wait_on_for_that"]:
            p["status"] = "DONE"
    prog["stats"]["packages_by_status"] = {}
    for p in prog["packages"]:
        k = "NOT STARTED" if p["status"].startswith("NOT STARTED") else p["status"].split()[0]
        prog["stats"]["packages_by_status"][k] = prog["stats"]["packages_by_status"].get(k, 0) + 1
    assert bw.build(_programme=prog)["stats"]["ready_for_the_final_reading"] is True              # and only then
    one = copy.deepcopy(prog)
    w = one["stats"]["packages_the_sealed_card_must_wait_on_for_that"][0]
    next(p for p in one["packages"] if p["id"] == w)["status"] = "STARTED"
    one["stats"]["packages_by_status"]["DONE"] -= 1; one["stats"]["packages_by_status"]["STARTED"] = one["stats"]["packages_by_status"].get("STARTED", 0) + 1
    assert bw.build(_programme=one)["stats"]["ready_for_the_final_reading"] is False


def test_each_refusal_fires():
    sb = json.loads(bw.SCOREBOARD.read_text(encoding="utf-8"))
    f = bw.build(_scoreboard=dict(sb, earned=sb["earned"] + 1))["fails"]
    assert any("the scoreboard's page says" in x for x in f), f
    f = bw.build(_page="a page with no headline")["fails"]
    assert any("has no line" in x for x in f), f
    prog = copy.deepcopy(P); prog["stats"]["packages_by_status"]["DONE"] = prog["stats"]["packages_by_status"].get("DONE", 0) + 1
    assert any("is not a recount of its packages" in x for x in bw.build(_programme=prog)["fails"])
    prog = copy.deepcopy(P); prog["stats"]["packages_the_sealed_card_must_wait_on_for_that"].append("WP-9.9")
    assert any("waits on a package the programme does not hold: WP-9.9" in x for x in bw.build(_programme=prog)["fails"])
    prog = copy.deepcopy(P); next(p for p in prog["packages"] if p["title"] == "The sealed card")["title"] = "A card"
    assert any("does not hold exactly one package each" in x for x in bw.build(_programme=prog)["fails"])
    assert any("the map has" in x for x in bw.build(_nodes=[])["fails"])
    assert bw.build()["fails"] == []


def test_the_arc_keeps_no_copied_count_and_the_gate_runs_the_builder():
    f = (ARC / "FINDINGS.md").read_text(encoding="utf-8")
    assert "Its numbers are not copied here" in f and "## Seen first" in f and "## Disclosed" in f and "0 of 19" in f
    assert not re.search(r"\b\d+ packages\b|\b\d+ of \d+ map nodes\b", f)               # no live count in the prose
    spec2 = importlib.util.spec_from_file_location("gates_b1883_lock", ROOT / "scripts" / "gates" / "gates.py")
    g = importlib.util.module_from_spec(spec2); spec2.loader.exec_module(g)
    assert ("frontier/B1883_where_we_stand", "build_where_we_stand.py", "the status page") in g.CLOSURE_GENERATED
    line = bw.one_line(B["stats"])
    assert line.startswith("%d of %d earned; sealed card " % (B["stats"]["values_earned"], B["stats"]["values_in_all"]))
