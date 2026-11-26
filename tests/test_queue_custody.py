"""2026-11-26 (the framework's thin path, patch T4; main's M54; register row P-885): custody, scripts/queue/custody.py.

On a small repository built here: a card filed and sighted holds custody, and fails it when its branch is rewritten past
its commit, when the runner never sighted it, when it was filed before it was sighted, when its decisive script is not at
the commit or is not the one it hashes. The sighting log's form is planted rule by rule; sighting is only ever appended;
along a branch's history the log is never rewritten and no card's fixed fields or past history change; the gate reads the
log; the command runs by hand."""
import copy
import hashlib
import importlib.util
import json
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]


def _load(name, rel):
    spec = importlib.util.spec_from_file_location(name, ROOT / rel)
    m = importlib.util.module_from_spec(spec)
    sys.dont_write_bytecode = True
    spec.loader.exec_module(m)
    return m


CU = _load("custody_under_test", "scripts/queue/custody.py")
D = _load("discover_for_custody", "scripts/queue/discover.py")
GATES = _load("gates_for_custody", "scripts/gates/gates.py")
SCRIPT = b"print('DECISIVE: 42')\n"
H16 = hashlib.sha256(SCRIPT).hexdigest()[:16]
CARD = """# CLAIM CARD — a count

- card id: new
- seat code: fam2-v5-high-01
- decisive script: x.py, SHA-256 {h}, depends on the standard library, run as python3 x.py, output SHA-256 0011223344556677
"""


def _repo(tmp_path, h=H16, script=True):
    tmp_path.mkdir(parents=True, exist_ok=True)
    g = lambda *a: subprocess.run(["git", "-c", "user.name=t", "-c", "user.email=t@t", *a], cwd=tmp_path,
                                  capture_output=True, text=True, check=True).stdout
    g("init", "-q", "-b", "seat/a")
    (tmp_path / "relays" / "claims").mkdir(parents=True)
    if script:
        (tmp_path / "x.py").write_bytes(SCRIPT)
    (tmp_path / "relays" / "claims" / "CLAIM_a.md").write_text(CARD.format(h=h), encoding="utf-8")
    g("add", "-A")
    g("commit", "-q", "-m", "a card")
    g("update-ref", "refs/remotes/origin/seat/a", "HEAD")
    new, _ = D.discover({}, [("a", "origin/seat/a")], root=tmp_path, at="2026-11-26T12:00:00Z")
    rec = new["Q0001"]
    log = [CU.sight(tmp_path, [], rec["branch"], rec["commit"], rec["card_path"], "card", "2026-11-26T11:59:00Z")]
    log.append(CU.sight(tmp_path, log, rec["branch"], rec["commit"], "x.py", "script", "2026-11-26T11:59:00Z"))
    return g, rec, [e for e in log if e]


def test_a_card_in_custody_holds_and_each_break_fails(tmp_path):
    g, rec, log = _repo(tmp_path / "ok")
    assert CU.custody_problems(tmp_path / "ok", rec, log) == []
    assert any("never sighted" in b for b in CU.custody_problems(tmp_path / "ok", rec, []))
    late = [dict(log[0], at="2026-11-26T12:30:00Z")]
    assert any("filed (2026-11-26T12:00:00Z) before the runner sighted it" in b
               for b in CU.custody_problems(tmp_path / "ok", rec, late))
    # the branch rewritten past the sealed commit
    g("checkout", "-q", "--orphan", "other")
    g("commit", "-q", "--allow-empty", "-m", "a new history")
    g("update-ref", "refs/remotes/origin/seat/a", "HEAD")
    assert any("no longer on origin/seat/a" in b for b in CU.custody_problems(tmp_path / "ok", rec, log))
    # the script the card hashes is not the one at the commit, or is not there
    _, rec2, log2 = _repo(tmp_path / "wrong", h="0" * 16)
    assert any("not the one the card hashes" in b for b in CU.custody_problems(tmp_path / "wrong", rec2, log2))
    _, rec3, log3 = _repo(tmp_path / "gone", script=False)
    assert any("is not at the sealed commit" in b for b in CU.custody_problems(tmp_path / "gone", rec3, log3))


def test_the_log_is_only_appended_to_and_a_version_is_sighted_once(tmp_path):
    g, rec, log = _repo(tmp_path)
    text = CU.append("", log)
    entries, bad = CU.read_log(text)
    assert bad == [] and len(entries) == 2 and {e["what"] for e in entries} == {"card", "script"}
    assert CU.sight(tmp_path, entries, rec["branch"], rec["commit"], rec["card_path"], "card", "2026-11-27T00:00:00Z") is None
    more = CU.append(text, [dict(log[0], path="relays/claims/CLAIM_b.md", at="2026-11-27T00:00:00Z")])
    assert more.startswith(text) and CU.read_log(more)[1] == []


def test_the_logs_form_is_planted_rule_by_rule(tmp_path):
    _, _, log = _repo(tmp_path)
    good = json.dumps(log[0])
    plants = {
        "is not JSON": "{",
        "does not hold exactly": json.dumps({k: v for k, v in log[0].items() if k != "what"}),
        "is not YYYY": json.dumps(dict(log[0], at="today")),
        "full 40-hex": json.dumps(dict(log[0], blob="abc")),
        "what 'output'": json.dumps(dict(log[0], what="output")),
        "goes back in time": json.dumps(dict(log[0], path="p", at="2026-01-01T00:00:00Z")),
        "sights again": good,
    }
    assert CU.read_log(good + "\n")[1] == []
    for words, line in plants.items():
        bad = CU.read_log(good + "\n" + line + "\n")[1]
        assert any(words in b for b in bad), (words, bad)


def test_along_the_history_nothing_of_the_queue_is_rewritten(tmp_path):
    g = lambda *a: subprocess.run(["git", "-c", "user.name=t", "-c", "user.email=t@t", *a], cwd=tmp_path,
                                  capture_output=True, text=True, check=True).stdout
    g("init", "-q", "-b", "queue")
    cards = tmp_path / "queue" / "cards"
    cards.mkdir(parents=True)
    card = json.loads(json.dumps(_load("schema_test_twin", "tests/test_queue_schema.py").TWIN))
    card["status"], card["history"] = "FILED", card["history"][:1]

    def commit(log, rec, msg):
        (tmp_path / "queue" / "SIGHTINGS.jsonl").write_text(log, encoding="utf-8")
        (cards / "Q0007.json").write_text(json.dumps(rec), encoding="utf-8")
        g("add", "-A")
        g("commit", "-q", "-m", msg)
    commit("a\n", card, "one")
    later = copy.deepcopy(card)
    later["history"].append({"at": "2026-11-26T10:20:00Z", "status": "REPRODUCED", "by": "runner", "note": "ok"})
    later["status"] = "REPRODUCED"
    commit("a\nb\n", later, "two")
    assert CU.history_problems(tmp_path, "HEAD") == []
    moved = dict(copy.deepcopy(later), commit="f" * 40)
    commit("a\nb\n", moved, "three")
    assert any("changes a field that never changes" in b for b in CU.history_problems(tmp_path, "HEAD"))
    g("reset", "-q", "--hard", "HEAD~1")
    commit("a\nb\n", dict(copy.deepcopy(later), history=later["history"][1:]), "three")
    assert any("rewrites the card's past history" in b for b in CU.history_problems(tmp_path, "HEAD"))
    g("reset", "-q", "--hard", "HEAD~1")
    commit("a\nc\n", later, "three")
    assert any("the log was rewritten" in b for b in CU.history_problems(tmp_path, "HEAD"))


def test_the_gate_reads_the_log_and_passes_on_the_record():
    ok, detail = GATES.gate_queue_schema({}, _log="{\n")
    assert not ok and "SIGHTINGS.jsonl: line 1 is not JSON" in detail
    assert GATES.gate_queue_schema({}, _log="")[0]
    assert GATES.gate_queue_schema()[0]


def test_the_command_runs_by_hand(tmp_path):
    f = tmp_path / "SIGHTINGS.jsonl"
    f.write_text("{\n", encoding="utf-8")
    run = lambda *a: subprocess.run([sys.executable, "-B", str(ROOT / "scripts/queue/custody.py"), *map(str, a)],
                                    capture_output=True, text=True, timeout=300)
    assert run("--log", f).returncode == 1
    f.write_text("", encoding="utf-8")
    assert run("--log", f, "--history", "HEAD").returncode == 0
