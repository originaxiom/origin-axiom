"""B1889 lock -- the seats digested: the counts are the ledger's at one commit, every row falls to one seat, the readers'
quotes are in the rows they name, and the page says no more than was measured.

What could fail: a page that differs from what the builder gives at its commit; a row that no seat claims, or two; a class
that swallows another's leading words; a seat of the gate's registry that the digest leaves out; a reader's quote that is
not in its row; a number in the findings that is not the page's; a count of the plan that is not the programme's; or a
proposal that reads as if it were in force.

Three tests read main's history at the digest's commit.  In a clone that does not hold that commit they are skipped, and
say so: they cannot look there, and a skip is printed where a pass would be untrue."""
import importlib.util
import json
import pathlib
import re
import subprocess

import pytest

HERE = pathlib.Path(__file__).resolve().parent
ARC = HERE.parent


def _load(name):
    spec = importlib.util.spec_from_file_location("b1889_" + name, HERE / (name + ".py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


bs, qc = _load("build_seats"), _load("quote_check")
B = json.loads((ARC / "SEATS.json").read_text(encoding="utf-8"))
Q = json.loads((HERE / "quote_check.json").read_text(encoding="utf-8"))
F = (ARC / "FINDINGS.md").read_text(encoding="utf-8")
SEAT = {s["key"]: s for s in B["seats"]}


def _at(path):
    r = subprocess.run(["git", "-C", str(bs.ROOT), "show", "%s:%s" % (B["as_of"], path)], capture_output=True)
    if r.returncode != 0:
        pytest.skip("this clone does not hold main's commit %s, so the digest cannot be recomputed here" % B["as_of"][:9])
    return r.stdout.decode("utf-8")


def test_the_pages_are_what_the_builder_gives_at_their_commit():
    fresh = bs.build(B["as_of"], text=_at("docs/HARVEST_LEDGER.md"))
    assert json.loads(json.dumps(fresh, ensure_ascii=False)) == B
    assert bs.page(fresh) == (ARC / "SEATS.md").read_text(encoding="utf-8")


def test_every_row_falls_to_exactly_one_seat():
    assert B["rows_no_seat_claims"] == [] and B["rows_two_seats_claim"] == []
    assert sum(s["rows"] for s in B["seats"]) == B["rows"] == sum(B["totals"].values())
    for s in B["seats"]:
        assert sum(s["by_class"].values()) == s["rows"], s["key"]
    for k in bs.ORDER:
        assert sum(s["by_class"][k] for s in B["seats"]) == B["totals"][k], k


def test_a_row_no_seat_claims_and_a_row_two_seats_claim_are_reported():
    """the planted cases: the partition can fail, and says where"""
    planted = "\n".join([
        "| 1 | a seat nobody registered | x | y | z | **VERIFIED** — as it stood | B1 | 2026-01-01 |",
        "| 2 | cloud seat, with the codex seat | x | y | z | **SOMETHING NEW** | — | 2026-01-02 |",
        "| 3 | the independent audit lane (2026-11-03) | x | y | z | **REPRODUCED** | — | 2026-01-03 |",
        "| 4 | audit lane | x | y | z | **READ** | — | 2026-01-04 |"])
    P = bs.build("planted", text=planted)
    assert P["rows_no_seat_claims"] == [1]
    assert [n for n, _ in P["rows_two_seats_claim"]] == [2] and P["rows_two_seats_claim"][0][1] == ["cloud", "codex"]
    got = {s["key"]: s["rows"] for s in P["seats"] if s["rows"]}
    # the fault of main's first cut cannot return: the independent lane's rows are not the physical lane's
    assert got == {"independent": 1, "audit": 1}


def test_the_classes_read_the_leading_words_and_the_order_matters():
    cases = [("**VERIFIED-DIFFERS** — on one claim", "differed"), ("**VERIFIED WITH CORRECTIONS** (in full", "differed"),
             ("**VERIFIED** — re-derived", "verified"), ("**REPRODUCED** (\"VERIFIED\" until Review 66)", "verified"),
             ("**SCHEDULED** (no main text names it", "not read"), ("**REGISTERED; NOT READ (S306p)**: a working page", "not read"),
             ("**REGISTERED** at headline level", "registered"), ("**READ IN FULL (the relay)**", "read"),
             ("**READ; VERIFIED IN PART** (S287", "verified"), ("**CLOSED-HANDLED** (R76-1", "closed by triage"),
             ("**AUDITED** (S223", "other"), ("QUEUED (result pending", "not read")]
    for d, k in cases:
        assert bs.klass(d) == k, (d, bs.klass(d))
    names = [n for n, _ in bs.CLASSES]
    # a row that says it was registered and not read is not read: that class is tried before 'registered'
    assert names.index("not read") < names.index("registered") and names.index("differed") < names.index("verified")
    assert B["totals"]["other"] == len(B["other"]) and B["totals"]["not read"] == len(B["not_read"])


def test_every_seat_of_the_gates_registry_at_that_commit_is_in_the_digest():
    src = _at("scripts/checks/harvest_debt.py")
    keys = set(re.findall(r'^\s*dict\(key="(\w+)"', src, flags=re.M))
    assert len(keys) >= 20
    merged = {"agyaudit": "agy", "agysync": "agy", "agyloop": "agy", "refereeland": "referee"}
    assert {merged.get(k, k) for k in keys} <= set(SEAT), sorted({merged.get(k, k) for k in keys} - set(SEAT))


def test_the_readers_quotes_are_in_the_rows_they_name():
    fresh = qc.run(B["as_of"], text=_at("docs/HARVEST_LEDGER.md"))
    assert fresh == Q
    assert Q["quotes"] >= 400 and Q["exact"] >= 0.97 * Q["quotes"]
    loose = [x for r in Q["readers"].values() for x in r["not_exact"]]
    assert len(loose) == Q["quotes"] - Q["exact"]
    # what is not exact is a generic phrase or a paraphrase, and names no fact about one row: each is short
    assert all(len(x["quote"].split()) <= 12 for x in loose), loose
    # the control: a quote that is in no row is reported as not found
    R = qc.ledger("| 7 | web seat | an item | h | p | **VERIFIED** — every cell as committed | B1 | 2026-01-01 |")
    got = qc.check('- 7: "every cell as committed"\n- 7: "every cell was recomputed twice"', R)
    assert [g["verdict"] for g in got] == ["EXACT", "NOT FOUND"]


def test_the_findings_numbers_are_the_pages():
    T, n = B["totals"], B["rows"]
    rec = T["verified"] + T["differed"]
    web, adv, agy, phy, fork, sm = (SEAT[k] for k in ("chat1", "advisor", "agy", "audit", "auditfork", "sm"))
    for sentence in (
            "The seats have sent %s items in two months. Main has recomputed %d of them itself, %d%%." % (format(n, ","), rec, round(100 * rec / n)),
            "%d held and %d differed" % (T["verified"], T["differed"]),
            "%d items are registered and were never fully read by main." % T["registered"],
            "%d of them are the physical lane's" % (phy["by_class"]["registered"] + fork["by_class"]["registered"]),
            "and %d are the SM seat's" % sm["by_class"]["registered"],
            "%d items are not read." % T["not read"],
            "| sent | %d items since 2026-09-08 |" % web["rows"],
            "| recomputed by main | %d: %d held, %d differed |" % (web["recomputed"], web["by_class"]["verified"], web["by_class"]["differed"]),
            "| sent | %d items since 2026-11-10 |" % adv["rows"],
            "| sent | %d items since 2026-10-27, on four branches |" % agy["rows"],
            "| sent | %d items since 2026-09-08, and %d more on its fork lane |" % (phy["rows"], fork["rows"]),
            "| recomputed by main | %d, and all %d held |" % (phy["recomputed"], phy["recomputed"]),
            "%d items. Main recomputed %d: %d held, %d differed" % (sm["rows"], sm["recomputed"], sm["by_class"]["verified"], sm["by_class"]["differed"]),
            "The five readers flagged %d of them" % len(B["flagged"]),
            "%d of %d are in that row word for word" % (Q["exact"], Q["quotes"])):
        assert sentence in F, sentence
    assert phy["by_class"]["differed"] == 0 and SEAT["explore"]["by_class"]["verified"] == SEAT["explore"]["rows"] == 5
    carried = sum(1 for x in B["flagged"] if x["carried_by"])
    assert "**%d of the %d name a register row,**" % (carried, len(B["flagged"])) in F and "**%d name none.**" % (len(B["flagged"]) - carried) in F


def test_the_plans_counts_are_the_programmes_at_that_commit():
    P = json.loads(_at("frontier/B1861_the_closure_programme/PROGRAMME.json"))["packages"]

    def stage(w):
        return 1 if w["obligation"] == "C0" else (3 if w["obligation"] in ("C5", "C6") else 2)

    def state(w):
        return "done" if w["status"].startswith("DONE") else ("started" if w["status"].startswith("STARTED") else "not started")

    count = {s: {k: sum(1 for w in P if stage(w) == s and state(w) == k) for k in ("done", "started", "not started")} for s in (1, 2, 3)}
    size = {s: sum(1 for w in P if stage(w) == s) for s in (1, 2, 3)}
    assert "| 1. a record that can be trusted | %d |" % size[1] in F and "| %d done, %d started |" % (count[1]["done"], count[1]["started"]) in F
    assert "| 2. the mathematics complete | %d |" % size[2] in F and "| %d done, %d started |" % (count[2]["done"], count[2]["started"]) in F
    assert "| 3. the reading | %d |" % size[3] in F and "| %d started |" % count[3]["started"] in F
    alone = sum(1 for w in P if w["owner"].startswith("main") and not any(k in w["owner"] for k in ("web seat", "physical", "agy")))
    unowned = sum(1 for w in P if w["owner"].startswith("unowned"))
    assert "For %d of the plan's %d packages main is the only builder named, and %d have no owner." % (alone, len(P), unowned) in F
    assert "%d of the %d packages of mathematics are not started." % (count[2]["not started"], size[2]) in F


def test_the_proposal_is_marked_as_not_in_force_and_asks_no_question_of_fact():
    sec = F[F.index("## 7. The proposal main brings to the lock"):F.index("## Seen first")]
    assert sec.count("**Not in force.**") == 1 and "It is not in force." in F[:1200]
    asks = sec[sec.index("### 7.6 What only the owner can settle"):]
    assert len(re.findall(r"^\d\. \*\*", asks, flags=re.M)) == 3
    # the three are a standard, the team and an order of work: none asks him whether a statement of the mathematics is true
    assert [m for m in re.findall(r"^\d\. \*\*(.+?)\*\*", asks, flags=re.M)] == ["The standard.", "The team.", "The order."]


def test_the_builder_reads_every_numbered_row_of_the_ledger():
    """Added 2026-11-12 (Review 79).  The builder asked for eight cells and dropped thirteen rows that have six, and this lock,
    which compared the builder with its own committed output, could not see it: a reading on another family of model did.
    Here the ledger's rows are counted apart from the builder, at the commit the pages are of."""
    import re
    import subprocess
    commit = json.loads((ARC / "SEATS.json").read_text(encoding="utf-8"))["as_of"]
    r = subprocess.run(["git", "-C", str(ARC.parents[1]), "show", "%s:docs/HARVEST_LEDGER.md" % commit[:12]], capture_output=True, text=True)
    if r.returncode != 0:                                              # without the commit, the ledger as it stands gives a floor
        text = (ARC.parents[1] / "docs" / "HARVEST_LEDGER.md").read_text(encoding="utf-8")
        numbered = [int(m.group(1)) for m in re.finditer(r"^\| (\d+) \|", text, re.M)]
        assert len([n for n in numbered if n <= 1699]) == 1699
        return
    text = r.stdout
    numbered = [int(m.group(1)) for m in re.finditer(r"^\| (\d+) \|", text, re.M)]
    built = bs.rows(text)
    assert sorted(numbered) == list(range(1, max(numbered) + 1)) == sorted(x["n"] for x in built)          # every number once, and every one read
    six = [l for l in text.split("\n") if re.match(r"^\| \d+ \|", l) and len(l.strip().strip("|").split(" | ")) == 6]
    assert len(six) == 13 and len(built) == 1699
    # a row of a shape the builder does not know is refused, not dropped
    try:
        bs.rows("| 1 | a seat | an item | a headline |")
    except ValueError:
        pass
    else:
        raise AssertionError("a row of four cells was read or dropped without a word")
    # the cell for main's arc is read for the register row that carries an item
    D = json.loads((ARC / "SEATS.json").read_text(encoding="utf-8"))
    assert sum(1 for x in D["flagged"] if x["carried_by"]) == 53 and len(D["flagged"]) == 74

