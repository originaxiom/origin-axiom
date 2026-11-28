"""2026-11-26 (the framework's thin path, patch T7; main's M54; register row P-885): the intake runner,
scripts/queue/intake.py, and its workflow, .github/workflows/intake.yml.

On a repository built here, one round files every card, sights it, and moves each as its checks decide: a card that holds
is REPRODUCED with `deciding` set; a card whose form fails, whose script is not the one it hashes, or whose rerun fails is
RETURNED_AT_INTAKE; a card that waits on an unverified card stays FILED; a card declared heavy stays FILED, marked heavy;
words of a comparison with data are flagged in the report. A second round changes nothing. The written queue holds its
schema. A round that cannot cut the network stops unless told otherwise. The workflow reads only, except the one job that
records, which runs no seat code; it has no pull-request trigger and names only standard runners."""
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


IN = _load("intake_under_test", "scripts/queue/intake.py")
SCRIPT = ("import sys\nif '--plant' in sys.argv:\n    raise SystemExit(1)\nprint('DECISIVE: {name} = 12')\n")


def _script(name):
    return SCRIPT.format(name=name)


AT = "2026-11-26T12:00:00Z"


def _card(title, name, h=None, touches="P-885", premises="B335", note="", heavy="", kind="computation", printed=None,
          stated="0" * 40):
    """a full card for the script s_<name>.py, which prints one decisive line; `printed` is the line the card says it
    prints (the script's own unless given), so a card can be made to say what its script does not print"""
    script = "s_%s.py" % name
    h = h or hashlib.sha256(_script(name).encode()).hexdigest()[:16]
    n, d = IN.RR.decisive((printed or "DECISIVE: %s = 12" % name) + "\n")
    return """# CLAIM CARD — {title}

- card id: new
- seat code: fam2-v5-high-01
- seat, branch, commit: fam2-v5-high-01, seat/a, {stated}
- kind: {kind}
- touches: {touches}
- effect: supports — {touches}
- scope: frame: F-HE; object: m004; reach: single; hypotheses: none
- identifications: none
- definitions: a class is an orbit of the group on the level's states
- imports: none
- premises on main: {premises}
- decisive script: {script}, SHA-256 {h}, depends on the standard library, run as python3 {script}, output SHA-256 0011223344556677{heavy}
- decisive lines: {n} lines marked "DECISIVE:", SHA-256 {d}
- failing control: python3 {script} --plant
- second computation: none
- already on main?: none found
- what would make it fail: the planted level{note}
""".format(title=title, script=script, h=h, touches=touches, premises=premises, note=note, heavy=heavy, kind=kind,
           n=n, d=d, stated=stated)


CODES = {"seat/a": "fam2-v5-high-01"}


def _repo(tmp_path):
    g = lambda *a: subprocess.run(["git", "-c", "user.name=t", "-c", "user.email=t@t", *a], cwd=tmp_path,
                                  capture_output=True, text=True, check=True).stdout
    g("init", "-q", "-b", "seat/a")
    names = ("good", "form", "hash", "rerun", "waits", "heavy", "flag")
    for name in names:
        (tmp_path / ("s_%s.py" % name)).write_text(_script(name), encoding="utf-8")
    g("add", "-A")
    g("commit", "-q", "-m", "the scripts")
    stated = g("rev-parse", "HEAD").strip()           # a card names a commit before the one that adds it (M65)
    (tmp_path / "relays" / "claims").mkdir(parents=True)
    cards = {
        "CLAIM_good.md": _card("a count that holds", "good", stated=stated),
        "CLAIM_form.md": _card("a card of the wrong kind", "form", kind="a guess", stated=stated),
        "CLAIM_hash.md": _card("a card whose script is not the one it hashes", "hash", h="0" * 16, stated=stated),
        "CLAIM_rerun.md": _card("a card whose lines differ", "rerun", printed="DECISIVE: rerun = 13", stated=stated),
        "CLAIM_waits.md": _card("a card built on an unverified card", "waits", premises="Q0099", stated=stated),
        "CLAIM_heavy.md": _card("a card declared heavy", "heavy", heavy=", heavy", stated=stated),
        "CLAIM_flag.md": _card("a card that compares", "flag", note="; compared with data at the pole", stated=stated),
    }
    for name, text in cards.items():
        (tmp_path / "relays" / "claims" / name).write_text(text, encoding="utf-8")
    g("add", "-A")
    g("commit", "-q", "-m", "seven cards")
    g("update-ref", "refs/remotes/origin/seat/a", "HEAD")
    return g


def _by_path(cards):
    return {pathlib.Path(r["card_path"]).name: r for r in cards.values()}


def test_one_round_moves_each_card_as_its_checks_decide(tmp_path):
    repo, q = tmp_path / "repo", tmp_path / "queue"
    repo.mkdir()
    _repo(repo)
    cards, log, attached, report, status = IN.round_(q, root=repo, refs=[("a", "origin/seat/a")], codes=CODES, at=AT, limit=60,
                                                      allow_static=True)
    assert status == 0, report
    by = _by_path(cards)
    assert len(by) == 7 and all(r["history"][0]["by"] == "runner" for r in by.values())
    assert by["CLAIM_good.md"]["status"] == "REPRODUCED" and by["CLAIM_good.md"]["deciding"] is True
    assert by["CLAIM_form.md"]["status"] == "RETURNED_AT_INTAKE" and "kind is not" in by["CLAIM_form.md"]["history"][-1]["note"]
    assert by["CLAIM_hash.md"]["status"] == "RETURNED_AT_INTAKE" and "custody" in by["CLAIM_hash.md"]["history"][-1]["note"]
    assert by["CLAIM_rerun.md"]["status"] == "RETURNED_AT_INTAKE" and "decisive lines" in by["CLAIM_rerun.md"]["history"][-1]["note"]
    assert by["CLAIM_waits.md"]["status"] == "FILED" and any("waits on Q0099" in r for r in report)
    assert by["CLAIM_heavy.md"]["status"] == "FILED" and by["CLAIM_heavy.md"]["heavy"] is True
    assert any("FLAG for the author (A3)" in r for r in report)
    entries, bad = IN.CU.read_log(log)
    assert bad == [] and {e["what"] for e in entries} == {"card", "script"} and len(entries) == 14
    IN.write(q, cards, log, attached)
    assert IN.QS.queue_problems(IN.QS.read_dir(q / "cards")) == []
    good = by["CLAIM_good.md"]["id"]
    assert json.loads((q / "checks" / ("%s.json" % good)).read_text())["rerun"]["status"] == "REPRODUCED"
    # a second round changes nothing that was decided, and sights nothing again
    cards2, log2, _, report2, status2 = IN.round_(q, root=repo, refs=[("a", "origin/seat/a")], codes=CODES, at="2026-11-26T15:00:00Z",
                                                  limit=60, allow_static=True)
    assert status2 == 0 and log2 == log
    assert {k: v["status"] for k, v in cards2.items()} == {k: v["status"] for k, v in cards.items()}


def test_where_no_sandbox_can_be_made_no_seat_code_runs_and_the_round_goes_on(tmp_path):
    """T7b (main's M64 item 4): every rerun is HEAVY; the form, custody and the record check still run"""
    repo = tmp_path / "repo"
    repo.mkdir()
    _repo(repo)
    cards, _, _, report, status = IN.round_(tmp_path / "q", root=repo, refs=[("a", "origin/seat/a")], codes=CODES, at=AT,
                                            prefix=[])
    by = _by_path(cards)
    assert status == 0 and "no seat code runs this round" in report[0]
    assert by["CLAIM_good.md"]["status"] == "FILED" and by["CLAIM_good.md"]["heavy"] is True
    assert by["CLAIM_form.md"]["status"] == "RETURNED_AT_INTAKE" and by["CLAIM_hash.md"]["status"] == "RETURNED_AT_INTAKE"


def test_the_round_writes_only_what_it_holds_and_the_record_job_refuses_what_it_did_not_write(tmp_path):
    """T7b (main's M62): a folder changed while the round ran is not written over; a file the round did not write, or one
    changed after it, fails the manifest"""
    repo, q = tmp_path / "repo", tmp_path / "queue"
    repo.mkdir()
    _repo(repo)
    before = IN.snapshot(q)
    cards, log, att, _, _ = IN.round_(q, root=repo, refs=[("a", "origin/seat/a")], codes=CODES, at=AT, limit=60,
                                      allow_static=True)
    q.mkdir(parents=True)
    (q / "cards").mkdir()
    (q / "cards" / "Q0001.json").write_text('{"status": "VERIFIED"}', encoding="utf-8")
    assert IN.write(q, cards, log, att, before) != []
    (q / "cards" / "Q0001.json").unlink()
    assert IN.write(q, cards, log, att, IN.snapshot(q)) == [] and IN.manifest_problems(q) == []
    (q / "cards" / "Q0099.json").write_text("{}", encoding="utf-8")
    assert any("a file the round did not write" in b for b in IN.manifest_problems(q))
    (q / "cards" / "Q0099.json").unlink()
    (q / "SIGHTINGS.jsonl").write_text("", encoding="utf-8")
    assert any("not as the round wrote it" in b for b in IN.manifest_problems(q))


def test_a_seat_script_cannot_write_the_queues_folder(tmp_path):
    """T7b (main's M62, its own probe): a commit whose script prints its decisive lines and writes a VERIFIED card into the
    queue's folder comes out REPRODUCED with the folder untouched, the round's result the same as without the write"""
    prefix, name = IN.RR.sandbox_prefix()
    if not prefix:
        import pytest
        pytest.skip("no unprivileged user in a network namespace on this machine (%s)" % name)
    repo, q = tmp_path / "repo", tmp_path / "queue"
    (q / "cards").mkdir(parents=True)
    q.chmod(0o755)
    (q / "cards").chmod(0o755)
    g = lambda *a: subprocess.run(["git", "-c", "user.name=t", "-c", "user.email=t@t", *a], cwd=repo, capture_output=True,
                                  text=True, check=True).stdout
    repo.mkdir()
    g("init", "-q", "-b", "seat/a")
    evil = (_script("evil").replace("print(", "try:\n    open(%r, 'w').write('{\"status\": \"VERIFIED\"}')\nexcept OSError:\n"
                                    "    pass\nprint(" % str(q / "cards" / "Q0002.json"), 1))
    (repo / "s_evil.py").write_text(evil, encoding="utf-8")
    g("add", "-A")
    g("commit", "-q", "-m", "a script")
    stated = g("rev-parse", "HEAD").strip()
    (repo / "relays" / "claims").mkdir(parents=True)
    text = _card("a card whose script writes the queue", "evil", stated=stated,
                 h=hashlib.sha256(evil.encode()).hexdigest()[:16])
    (repo / "relays" / "claims" / "CLAIM_evil.md").write_text(text, encoding="utf-8")
    g("add", "-A")
    g("commit", "-q", "-m", "the card")
    g("update-ref", "refs/remotes/origin/seat/a", "HEAD")
    before = IN.snapshot(q)
    cards, log, att, report, status = IN.round_(q, root=repo, refs=[("a", "origin/seat/a")], codes=CODES, at=AT, limit=60,
                                                prefix=prefix)
    assert [r["status"] for r in cards.values()] == ["REPRODUCED"], report
    assert not (q / "cards" / "Q0002.json").exists() and IN.snapshot(q) == before


def test_the_workflow_reads_only_but_where_it_records_and_runs_no_seat_code_there():
    """read as text (the repository has no YAML reader among its dependencies): the triggers, the permissions, the two
    jobs and what each runs"""
    text = (ROOT / ".github" / "workflows" / "intake.yml").read_text(encoding="utf-8")
    head, jobs = text.split("\njobs:\n", 1)
    round_job, record = jobs.split("\n  record:\n", 1)
    on = head.split("\non:\n", 1)[1].split("\n\n", 1)[0]
    triggers = [l.strip().split(":")[0] for l in on.splitlines() if l.startswith("  ") and not l.startswith("    ")]
    assert triggers == ["schedule", "workflow_dispatch"]                 # no pull-request trigger: no fork's code runs
    assert "\npermissions:\n  contents: read" in head
    assert "permissions:" not in round_job and "permissions:" not in record                # read, as the top says
    assert "secrets." not in round_job and record.count("secrets.") == 1               # M73: the record job alone
    assert "ssh-key: ${{ secrets.QUEUE_DEPLOY_KEY }}" in record and "contents: write" not in text
    push, check = record.split('git push origin "HEAD:${QUEUE_BRANCH}"', 1)
    assert "rules/branches/${QUEUE_BRANCH}" in check and "exit 1" in check              # the ruleset read after the push
    assert "    needs: round" in record
    assert round_job.count("runs-on: ubuntu-latest") == 1 and record.count("runs-on: ubuntu-latest") == 1
    assert "runs-on" not in text.replace("runs-on: ubuntu-latest", "")   # no other runner, larger or self-hosted
    assert "secrets." not in round_job and "persist-credentials: false" in round_job
    assert "intake.py --queue-dir" in round_job and "--allow-static-guard" not in text
    assert "intake.py --queue-dir" not in record and "rerun.py" not in record      # the recording job runs no round
    assert "intake.py --check-manifest incoming" in record                          # T7b: only what the round wrote
    assert "queue_schema.py --dir incoming/cards" in record and "custody.py --history HEAD --root ." in record
    # ADDED 2026-11-28 (M78 points 1 and 4): the hidden manifest is uploaded, and a round with no sandbox is not recorded
    upload = round_job.split("actions/upload-artifact@", 1)[1]
    assert IN.MANIFEST.startswith(".") and "include-hidden-files: true" in upload
    step = round_job.split("intake.py --queue-dir", 1)[1].split("actions/upload-artifact@", 1)[0]
    assert "set -o pipefail" in round_job and 'grep -q "^the network guard: no sandbox"' in step and "exit 1" in step
    # ADDED 2026-11-28 (M78 point 2): the tool cache loses others' write bit after the packages and before the round
    install, rest = round_job.split("python3 -m pip install", 1)
    assert 'sudo chmod -R o-w "${RUNNER_TOOL_CACHE:-/opt/hostedtoolcache}"' in rest.split("intake.py --queue-dir", 1)[0]


def test_the_settings_the_author_makes_are_written_down():
    page = (ROOT / "queue" / "README.md").read_text(encoding="utf-8")
    for words in ("$0", "Main is protected from the runner's token", "written by one key alone", "restrict updates",
                  "QUEUE_DEPLOY_KEY", "no pull-request trigger", "the network guard"):
        assert words in page, words


def test_the_one_workflow_file_is_the_only_path_under_github_that_may_be_tracked(monkeypatch):
    """the gate tracked-forbidden kept .github/ out of the record whole; draft 1's section 9 puts the intake on GitHub
    Actions, so exactly one workflow file is allowed, and every other path there is still refused"""
    gates = _load("gates_for_the_workflow_test", "scripts/gates/gates.py")
    for files, ok in (([".github/workflows/intake.yml", "README.md"], True),
                      ([".github/workflows/intake.yml", ".github/workflows/other.yml"], False),
                      ([".github/dependabot.yml"], False)):
        monkeypatch.setattr(gates, "_git", lambda *a, files=files: (0, "\n".join(files)))
        got, bad = gates.gate_tracked_forbidden()
        assert got is ok, (files, bad)
        assert ".github/workflows/intake.yml" not in bad


def test_a_card_refiled_by_a_later_card_is_not_taken_further(tmp_path):
    """Review 88's A24: once a new version refiles a card, the old version stays where it is and is not rerun"""
    repo, q = tmp_path / "repo", tmp_path / "queue"
    repo.mkdir()
    g = _repo(repo)
    cards, log, att, report, _ = IN.round_(q, root=repo, refs=[("a", "origin/seat/a")], codes=CODES, at=AT, prefix=[])
    by = _by_path(cards)
    heavy = by["CLAIM_heavy.md"]                      # FILED and heavy: left for the author's machine
    good = by["CLAIM_waits.md"]                       # FILED, waiting on Q0099
    later = dict(good, id="Q0100", refiles=[good["id"]], history=[dict(good["history"][0])])
    cards[later["id"]] = later
    IN.write(q, cards, log, att)
    _, _, _, report, _ = IN.round_(q, root=repo, refs=[("a", "origin/seat/a")], codes=CODES, at="2026-11-27T18:00:00Z",
                                   prefix=[])
    assert any("%s is refiled by a later card, and is not taken further" % good["id"] in r for r in report)
    assert not any(("%s waits on" % good["id"]) in r for r in report) and heavy["id"]
