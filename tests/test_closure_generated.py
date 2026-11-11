"""The closure map (B1858) and the closure programme (B1861) are generated files, and a push cannot carry a stale one
(Review 77's R77-7, P-754; made a gate at Review 78).

For twenty landings both were rebuilt by hand before each commit.  Their own locks fail when a committed file is not its
builder's output, but the push gate does not run the suite.  The gate runs both builders and compares."""
import importlib.util
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
MAP = ROOT / "frontier" / "B1858_the_closure_map"
PROG = ROOT / "frontier" / "B1861_the_closure_programme"


def _gates():
    spec = importlib.util.spec_from_file_location("gates_for_closure_generated", ROOT / "scripts" / "gates" / "gates.py")
    g = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(g)
    return g


def _stale(target):
    """a reader of committed files that returns one of them with a line added, as if its source had moved on"""
    def read(f):
        text = f.read_text(encoding="utf-8")
        return text + "a stale line\n" if f == target else text
    return read


def test_the_gate_is_green_on_this_repository():
    g = _gates()
    ok, why = g.gate_closure_generated()
    assert ok, why
    problems, skipped = g.closure_generated_problems()
    assert not problems and (why == "ok") == (not skipped)


def test_a_stale_map_is_refused():
    g = _gates()
    for name in ("MAP.md", "EDGES.json"):                     # one page and one data file; the comparison is the same code for all four
        ok, why = g.gate_closure_generated(_read=_stale(MAP / name))
        assert not ok and ("frontier/B1858_the_closure_map/%s is not its builder's output" % name) in why, (name, why)


def test_a_stale_programme_is_refused_in_every_clone(monkeypatch):
    """As first written, a clone without the seats' pinned revisions skipped the page's whole comparison, and a count changed by
    hand on the page passed there (the advisor seat's fifth re-audit, its case g1).  The page no longer depends on the clone:
    it is compared everywhere, and only the check of the seats' quoted words is skipped where their branches are absent."""
    g = _gates()
    for name in ("PROGRAMME.md", "PROGRAMME.json"):
        ok, why = g.gate_closure_generated(_read=_stale(PROG / name))
        assert not ok and ("frontier/B1861_the_closure_programme/%s is not its builder's output" % name) in why, (name, why)
    # the same in a clone that holds no seat's branch: git answers that no revision is there
    import subprocess
    real = subprocess.run
    def no_seats(cmd, *a, **k):
        if isinstance(cmd, (list, tuple)) and "cat-file" in cmd:
            return subprocess.CompletedProcess(cmd, 1, b"", b"")
        return real(cmd, *a, **k)
    monkeypatch.setattr(subprocess, "run", no_seats)
    problems, skipped = g.closure_generated_problems()
    assert not problems and skipped and "quotes of other seats, not its page" in skipped[0], (problems, skipped)
    ok, why = g.gate_closure_generated()
    assert ok and "every generated page compared with its builder; skipped in part" in why
    assert g.result_line("closure-generated", ok, why).strip().startswith("SKIP")          # said so, never a bare ok
    for name in ("PROGRAMME.md", "PROGRAMME.json"):
        ok, why = g.gate_closure_generated(_read=_stale(PROG / name))
        assert not ok and ("frontier/B1861_the_closure_programme/%s is not its builder's output" % name) in why, (name, why)


def test_a_stale_status_page_is_refused():
    """B1883: the page that says how far the record is from the final reading is generated from the programme, the map and the
    scoreboard's data, and is compared with its builder at every push like the two it reads"""
    g = _gates()
    here = ROOT / "frontier" / "B1883_where_we_stand"
    for name in ("WHERE_WE_STAND.md", "WHERE_WE_STAND.json"):
        ok, why = g.gate_closure_generated(_read=_stale(here / name))
        assert not ok and ("frontier/B1883_where_we_stand/%s is not its builder's output" % name) in why, (name, why)
    assert [c[0].split("/")[1].split("_")[0] for c in g.CLOSURE_GENERATED] == ["B1858", "B1861", "B1883"]       # in the order they must be built


def test_the_gate_is_registered_with_a_control_and_a_practice():
    import json
    g = _gates()
    assert "closure-generated" in g.GATES
    controls = json.loads((ROOT / "tests" / "GATE_CONTROLS.json").read_text(encoding="utf-8"))
    assert controls["closure-generated"] == "tests/test_closure_generated.py::test_a_stale_map_is_refused"
    assert "`closure-generated`" in (ROOT / "docs" / "PRACTICES.md").read_text(encoding="utf-8")
