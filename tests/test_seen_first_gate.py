"""seen-first lock -- from B1454 on an arc says what it looked at before it claimed anything.

Pins: (1) the gate is registered; (2) an arc below the threshold is not asked; (3) an arc above it with no section
fails, with a section that cites no sweep fails, with a sweep and no word on the literature fails, and with both
passes (the gate can fail and can pass); (4) the topic sweep finds a planted subject and reports a planted absence;
(5) the rule is in WORKING_RULES with the owner's words.
"""
import importlib.util
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts" / "gates"))


def _gates():
    import gates
    return gates


def _arc(tmp, name, findings):
    d = tmp / "frontier" / name; d.mkdir(parents=True); (d / "FINDINGS.md").write_text(findings)


def test_the_gate_is_registered_and_passes_on_the_record():
    g = _gates()
    assert "seen-first" in g.GATES and g.SEEN_FIRST_FROM == 1454
    assert g.seen_first_missing() == []


def test_the_gate_fails_and_passes(tmp_path):
    g = _gates()
    _arc(tmp_path, "B1453_before_the_rule", "# B1453\nno section\n")
    _arc(tmp_path, "B1454_no_section", "# B1454\n## 1. Something\ntext\n")
    _arc(tmp_path, "B1455_no_sweep", "# B1455\n## Seen first\nthe literature was read.\n## 1\n")
    _arc(tmp_path, "B1456_no_literature", "# B1456\n## 0. Seen first\nVERDICT topic-sweep /x/: 3 of 1300 arcs.\n## 1\n")
    _arc(tmp_path, "B1457_complete", "# B1457\n## 0. Seen first\n- Repo: VERDICT topic-sweep /x/: 3 of 1300 arcs; read B1, B2.\n- Literature: searched for X; read Y's Theorem 2 with its hypotheses.\n## 1\n")
    bad = g.seen_first_missing(root=tmp_path)
    assert len(bad) == 3 and not any("B1453" in b or "B1457" in b for b in bad)
    assert any("B1454" in b and "no 'Seen first'" in b for b in bad)
    assert any("B1455" in b and "no repo sweep" in b for b in bad)
    assert any("B1456" in b and "literature" in b for b in bad)


def test_the_topic_sweep_answers_both_ways():
    spec = importlib.util.spec_from_file_location("topic_sweep", ROOT / "scripts" / "checks" / "topic_sweep.py")
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    rows = [dict(id="B1", dir="B1_x", verdict="PROVED", claim="a monodromy-preserving flow", title="# B1")]
    assert [h["id"] for h in m.sweep("monodromy", rows)] == ["B1"] and m.sweep("no-such-subject", rows) == []
    r = subprocess.run([sys.executable, str(ROOT / "scripts" / "checks" / "topic_sweep.py"), "--selftest"], capture_output=True, text=True)
    assert r.returncode == 0 and "PASS" in r.stdout
    real = m.sweep(r"dynamics", m.arcs())
    assert any(h["id"] == "B944" for h in real), "the dynamics sweep of 2026-08 is found by a sweep for dynamics"


def test_the_rule_is_written_with_the_owners_words():
    t = (ROOT / "WORKING_RULES.md").read_text()
    assert "SEE THE REPO AND THE LITERATURE FIRST" in t and "make a rule to see the repo first and literature" in t
    assert "topic_sweep.py" in t and "Seen first" in t
