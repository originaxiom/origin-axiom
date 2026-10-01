"""The doc-currency gate's own lock (B1437).

From 2026-08-09 to 2026-10-01 the checker, PRACTICES and a generated view all said "the lock fails if the declared-debt
set grows", naming a test file that did not exist. This is that lock, with the planted controls the checker never had:
a stale document must be caught, a current one must pass, a frozen one must be reported, and the debt report must use
the metric the check uses.
"""
import importlib.util
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]


def _dc():
    spec = importlib.util.spec_from_file_location("doc_currency_under_test", ROOT / "scripts" / "checks" / "doc_currency.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def _gates():
    sys.path.insert(0, str(ROOT / "scripts" / "gates"))
    import gates
    return gates


def test_the_gate_is_registered():
    assert "doc-currency" in _gates().GATES


def test_the_declared_debt_set_is_pinned():
    """A debt may be added or paid only by editing this list in the same commit: the set cannot grow unseen."""
    assert sorted(_dc().DECLARED_DEBT) == [
        "CLAIMS.md",
        "docs/GUT_REQUIREMENTS_LEDGER.md",
        "docs/THEOREM_LEDGER.md",
        "docs/TOOLBOX.md",
    ]


def test_every_declared_debt_is_a_registered_living_document_with_a_date():
    dc = _dc()
    for rel, (why, when) in dc.DECLARED_DEBT.items():
        assert rel in dc.LIVING, rel
        assert len(when) == 10 and when[4] == "-" and when[7] == "-", (rel, when)
        assert why.strip()


def test_a_planted_stale_document_is_caught(tmp_path):
    dc = _dc()
    ids = dc.existing_arc_ids()
    old = ids[len(ids) // 2]                                   # an arc with hundreds of arcs after it
    (tmp_path / "STALE.md").write_text(f"# a living document\n\nlast touched at B{old}.\n")
    stale, frozen = dc.check(living={"STALE.md": 10}, root=tmp_path, debt={})
    assert len(stale) == 1 and "STALE.md" in stale[0] and f"B{old}" in stale[0]
    assert frozen == []


def test_a_planted_current_document_passes(tmp_path):
    dc = _dc()
    head = dc.newest_arc_in_repo()
    (tmp_path / "CURRENT.md").write_text(f"# a living document\n\ncurrent through B{head}.\n")
    stale, frozen = dc.check(living={"CURRENT.md": 10}, root=tmp_path, debt={})
    assert stale == [] and frozen == []


def test_a_missing_living_document_fails(tmp_path):
    stale, _ = _dc().check(living={"NOT_THERE.md": 10}, root=tmp_path, debt={})
    assert len(stale) == 1 and "MISSING" in stale[0]


def test_frozen_is_a_marker_not_a_mention(tmp_path):
    dc = _dc()
    (tmp_path / "FROZEN.md").write_text("<!-- doc-currency: frozen -->\n# a record\n\nB5.\n")
    (tmp_path / "MENTION.md").write_text("# how to opt out\n\nwrite `<!-- doc-currency: frozen -->` at the top. B5.\n")
    stale, frozen = dc.check(living={"FROZEN.md": 10, "MENTION.md": 10}, root=tmp_path, debt={})
    assert frozen == ["FROZEN.md"]
    assert len(stale) == 1 and "MENTION.md" in stale[0]


def test_a_declared_debt_passes_the_check_and_only_that(tmp_path):
    dc = _dc()
    (tmp_path / "OWED.md").write_text("# owed a read\n\nB5.\n")
    stale, _ = dc.check(living={"OWED.md": 10}, root=tmp_path, debt={"OWED.md": ("declared", "2026-10-01")})
    assert stale == []
    stale, _ = dc.check(living={"OWED.md": 10}, root=tmp_path, debt={})
    assert len(stale) == 1


def test_one_metric(capsys):
    """the lag counts arcs that exist; the debt report prints the same number the check uses"""
    dc = _dc()
    ids = dc.existing_arc_ids()
    assert dc.lag_of(max(ids), ids) == 0
    assert dc.lag_of(ids[0], ids) == len(ids) - 1
    assert dc.lag_of(ids[-2], ids) == 1
    dc.main()
    out = capsys.readouterr().out
    for rel in dc.DECLARED_DEBT:
        cited = dc.newest_arc_cited(dc.ROOT / rel)
        assert f"{rel}: B{cited} vs B{dc.newest_arc_in_repo()} (lag {dc.lag_of(cited, ids)} existing arcs)" in out
