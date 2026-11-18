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


def test_the_second_readings_decisions_are_the_records_verdicts():
    """added 2026-11-18: the web lane's second reading lists every statement a sorter marked and main's decision on it; the
    records must carry that decision, each statement in one record, a narrowed one in its parent's companion"""
    owner = {}
    for q in (HERE / "records").glob("*.json"):
        d = json.loads(q.read_text())
        for u in d.get("units", []): owner.setdefault(u, []).append((d["id"], d["verdict"]))
    want = {"K": "VERIFIED", "N": "NOTED", "C": "CONDITIONAL", "P": "PARTIAL", "S": "SUPERSEDED"}      # S added 2026-11-18: a kept line the seat itself later withdrew
    for name in ("web.json", "others.json"):                                                       # the second list (the other lanes) added the same day
        L = json.loads((HERE / "second_reading" / name).read_text())
        assert len(L["units"]) == L["candidates"] == sum(L["decisions"].values()) and L["decisions"]["K"] < L["candidates"] // 2      # most candidates were narrowed [2026-11-18: the bound was a quarter; the web seat's own reading showed 194 narrowed lines of its lane to be computed by main's own scripts and arcs, and they are restored, so its kept are 284 of 950]
        for x in L["units"]:
            o = owner.get(x["unit"]); assert o and len(o) == 1, x["unit"]
            assert o[0][1] == want[x["decision"]], (x["unit"], o)
            assert o[0][0] == x["record"] if x["decision"] == "K" else o[0][0] == "%s-r2%s" % (x["record"], x["decision"].lower()), (x["unit"], o)
        # the check can fail: a narrowed statement put back under its parent is caught by the rule above
        x = next(y for y in L["units"] if y["decision"] == "P"); assert owner[x["unit"]][0][0] != x["record"]


def test_every_verified_statement_of_the_web_lane_was_read_by_main_one_by_one():
    """added 2026-11-18 at the web seat's section 15.3: the list of the unmarked lines main read, against the records; and that
    no statement of the lane stands verified without having been read by main beside its record's ground"""
    import collections
    V = pathlib.Path(__file__).resolve().parent; L = json.loads((V / "second_reading" / "web_unmarked.json").read_text()); M = json.loads((V / "second_reading" / "web.json").read_text())
    owner = collections.defaultdict(list)
    for q in (V / "records").glob("web-*.json"):
        d = json.loads(q.read_text())
        for u in d.get("units", []): owner[u].append((d["id"], d["verdict"]))
    want = {"P": "PARTIAL", "N": "NOTED", "C": "CONDITIONAL"}; narrowed = {x["unit"] for x in L["units"]}
    assert L["read"] == len(L["read_units"]) == 990 and narrowed <= set(L["read_units"]) and 0 < len(narrowed) < L["read"] // 10 and L["kept"] == L["read"] - len(narrowed)
    for x in L["units"]:
        home = x["record"] if x.get("whole_record") else "%s-r3%s" % (x["record"], x["decision"].lower())
        assert owner[x["unit"]] == [(home, want[x["decision"]])], x["unit"]
    read = (set(L["read_units"]) - narrowed) | {x["unit"] for x in M["units"] if x["decision"] == "K"} | {e["unit"] for e in json.loads((V / "second_reading" / "web_rv55.json").read_text())["entries"] if e["main"] == "V"}
    unread = [u for u, o in owner.items() if o[0][1] == "VERIFIED" and u not in read and not o[0][0].startswith(("web-st14-", "web-st15-", "web-st16-", "web-st17-", "web-st18-", "web-st18b-", "web-st19-", "web-st19b-", "web-st20-", "web-st20b-", "web-st21-", "web-st22-", "web-st21b-", "web-st23-", "web-st24-", "web-st24j-", "web-wp1-", "web-st25-", "web-st26-", "web-st17-03b", "web-rv55-"))]
    assert unread == [], unread[:3]
    assert any(x["decision"] == "P" for x in L["units"]) and owner[next(x["unit"] for x in L["units"] if x["decision"] == "P" and not x.get("whole_record"))][0][1] != "VERIFIED"   # a narrowed line is not verified


def test_every_record_a_ground_cites_exists_and_no_companion_is_without_its_parent():
    """added 2026-11-18: the second reading removed 54 parents with their grounds while other records cited them; restored.
    A cited id must exist (two replaced records are named as history); a companion's parent must exist."""
    import re
    V = pathlib.Path(__file__).resolve().parent; R = V / "records"; ids = {q.stem for q in R.glob("*.json")}
    replaced = {"web-wa2-05r", "web-wz1-04"}; assert not (replaced & ids)
    pat = re.compile(r"\b(?:%s)-[a-z0-9]+(?:-[a-z0-9]+)*-\d+[a-z]?(?:-r[23][pnc])?\b" % "|".join(map(re.escape, sorted({i.split("-")[0] for i in ids}))))
    cited = set()
    for q in R.glob("*.json"):
        d = json.loads(q.read_text()); cited |= set(pat.findall(d.get("how", "") + " " + d.get("note", "")))
    assert len(cited) > 500 and cited - ids <= replaced, sorted(cited - ids)[:5]
    assert pat.findall("see web-wa1-02 and agy002-g2-03-r2p") == ["web-wa1-02", "agy002-g2-03-r2p"]                      # the pattern does find ids
    comp = [i for i in ids if re.search(r"-r[23][pnc]$", i)]; assert len(comp) > 300 and all(re.sub(r"-r[23][pnc]$", "", i) in ids for i in comp)



def test_a_companions_ground_is_its_readings_account():
    """added 2026-11-18 (the web seat's section 24.5, item 1): THE CONVENTION. A companion record's ground (-r2x, -r3x) is its
    reading's account and is not rewritten when a line it lists later moves; such a line must be held where its unit now is,
    by exactly one record, whose ground or note names the move (corrected 2026-11-18 at the seat's section 25.1: the lock tests
    that the move is named, mostly by a review or harvest row; it does not test a date, and most receivers carry none). Checked on the web lane, whose companions'
    grounds list lines by file-stable numbers (checks/companion_grounds.py); the one line with two candidates is resolved in
    its record's note.  (In lanes whose status pages are recut, a ground's line numbers are those of the cut it was written
    at, and the record's units are authoritative.)"""
    import importlib.util
    V = pathlib.Path(__file__).resolve().parent; spec = importlib.util.spec_from_file_location("cg", V / "checks" / "companion_grounds.py")
    src = (V / "checks" / "companion_grounds.py").read_text(); g = {"__name__": "cg"}; exec(src[:src.index("for at, lab in")], g)
    import os; cwd = os.getcwd(); os.chdir(V.parents[2])
    try: comps, silent, placed, by, amb, undated = g["survey"](g["load"](None), "web-")
    finally: os.chdir(cwd)
    assert comps >= 100 and placed >= 266 and undated == [], undated[:5]
    for k, n, c in amb: assert "RESOLVED 2026-11-18" in json.loads((V / "records" / (k + ".json")).read_text())["note"] and ("line %s" % n) in json.loads((V / "records" / (k + ".json")).read_text())["note"], (k, n)

def test_the_other_lanes_verified_statements_were_each_read_by_main():
    """added 2026-11-18: the six other lanes of the second reading: every statement verified now was either marked and kept
    (others.json) or read among the unmarked (others_unmarked.json)"""
    import collections
    V = pathlib.Path(__file__).resolve().parent; L = json.loads((V / "second_reading" / "others_unmarked.json").read_text()); M = json.loads((V / "second_reading" / "others.json").read_text())
    lanes = ("agy-002-verify:", "agy-002-endgame:", "agy-002-closure:", "agy-exp:", "agy-audit:", "sm:"); owner = collections.defaultdict(list)
    for q in (V / "records").glob("*.json"):
        d = json.loads(q.read_text())
        for u in d.get("units", []): owner[u].append((d["id"], d["verdict"]))
    want = {"P": "PARTIAL", "N": "NOTED", "C": "CONDITIONAL"}; narrowed = {x["unit"] for x in L["units"]}
    assert L["read"] == len(L["read_units"]) > 200 and narrowed <= set(L["read_units"]) and len(narrowed) == len(L["units"]) > 0
    for x in L["units"]: assert owner[x["unit"]] == [("%s-r3%s" % (x["record"], x["decision"].lower()), want[x["decision"]])], x["unit"]
    read = (set(L["read_units"]) - narrowed) | {x["unit"] for x in M["units"] if x["decision"] == "K"}
    since = ("agyexp-xsv-", "agyexp-f3n-", "agyexp-b36-", "agyexp-wc2a-", "agyexp-xcan-", "agyexp-c1-", "agyexp-xc2-", "agyexp-xc3-", "agyexp-xms-", "agyexp-xown-", "agyexp-xnv-", "agyexp-p781-", "agyexp-ph4-", "agyexp-r79b-", "agyexp-r80-", "agyexp-xl5-", "sm-c22-", "agyaudit-st18-", "agy002v-x1-", "agy002v-st-x1-", "agy002v-m51-", "agyexp-hr2-", "sm-hr-", "agy002v-m53-", "agyexp-hr3-", "agyaudit-st20-")      # records written after the second reading from main's own reading of new pushes
    unread = [(u, o) for u, o in owner.items() if u.startswith(lanes) and o[0][1] == "VERIFIED" and u not in read and not o[0][0].startswith(since)]
    assert unread == [], unread[:3]
