"""A gate reads all it is about, and what it does not read it says (the closure programme's WP-0.7, series 3).

The seat's planted cases PV16, PV17, PV20, PV21 and PV24.  Five gates passed because each read less than it is about: three
kinds of file of many, two shapes of row of three, a control's name and not the control, a cited lock and not whether one is
cited, an assert and not whether it can fail.  After this series each of the five reads the whole of what it is about, counts
in its sentence what it did not read, and holds by name what stood on the day the rule came.

Each test makes the situation in a small repository of its own, which holds this repository's gates and checkers and a few
pages, and runs the gate there.  Nothing in the environment moves a gate."""
import importlib.util
import json
import pathlib
import shutil
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]


def _gates():
    spec = importlib.util.spec_from_file_location("gates_for_the_reach_rule", ROOT / "scripts" / "gates" / "gates.py")
    g = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(g)
    return g


def _git(repo, *a):
    r = subprocess.run(["git", "-C", str(repo), "-c", "user.name=t", "-c", "user.email=t@example.invalid", *a], capture_output=True, text=True)
    assert r.returncode == 0, r.stderr
    return r.stdout.strip()


def _commit(repo, message, files=None):
    for rel, text in (files or {}).items():
        p = repo / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        if isinstance(text, bytes):
            p.write_bytes(text)
        else:
            p.write_text(text, encoding="utf-8")
    _git(repo, "add", "-A")
    _git(repo, "commit", "-q", "--allow-empty", "-m", message)
    return _git(repo, "rev-parse", "HEAD")


def _scratch(tmp_path, files):
    """a small repository holding this repository's gates and checkers, and `files`, committed"""
    repo = tmp_path / "repo"
    skip = shutil.ignore_patterns("__pycache__", "*.pyc")
    shutil.copytree(ROOT / "scripts" / "gates", repo / "scripts" / "gates", ignore=skip)
    shutil.copytree(ROOT / "scripts" / "checks", repo / "scripts" / "checks", ignore=skip)
    _git(repo, "init", "-q")
    _commit(repo, "a small repository", files)
    return repo


_RUN = ("import sys, json, importlib.util\n"
        "sys.dont_write_bytecode = True\n"
        "s = importlib.util.spec_from_file_location('scratch_gates', 'scripts/gates/gates.py')\n"
        "g = importlib.util.module_from_spec(s); s.loader.exec_module(g)\n"
        "r = g.GATES[%r]()\n"
        "print(json.dumps([bool(r[0]), r[1] if isinstance(r[1], str) else ' | '.join(map(str, r[1]))]))\n")


def _gate(repo, name):
    """the gate `name` of the small repository's own copy of the gates"""
    r = subprocess.run([sys.executable, "-B", "-c", _RUN % name], cwd=str(repo), capture_output=True, text=True)
    assert r.returncode == 0, r.stderr[-800:]
    ok, detail = json.loads(r.stdout.strip().splitlines()[-1])
    return ok, detail


# ---- PV21: the framing gate read three kinds of file, and compared letter for letter -----------------------------------
def _banned():
    """one of the gate's banned phrases, taken from the gate and not typed here"""
    phrase = _gates().BANNED[2]
    assert "'" in phrase and " " in phrase          # the tests below break it at a space and change its apostrophe
    return phrase


def test_a_banned_phrase_written_as_the_gate_holds_it_fails_the_framing_gate(tmp_path):
    """the control: this held before the series"""
    repo = _scratch(tmp_path, {"docs/PAGE.md": "In this note " + _banned() + ".\n"})
    ok, detail = _gate(repo, "framing")
    assert ok is False and "docs/PAGE.md" in detail


def test_a_banned_phrase_in_a_tex_file_fails_the_framing_gate(tmp_path):
    repo = _scratch(tmp_path, {"papers/note.tex": "In this note " + _banned() + ".\n"})
    ok, detail = _gate(repo, "framing")
    assert ok is False, "a banned phrase in a .tex file under papers/, and the framing gate passed: " + detail
    assert "papers/note.tex" in detail


def test_a_banned_phrase_in_capitals_fails_the_framing_gate(tmp_path):
    repo = _scratch(tmp_path, {"README.md": "# A page\n\n" + _banned().upper() + ".\n"})
    ok, detail = _gate(repo, "framing")
    assert ok is False, "a banned phrase in capitals on the front page, and the framing gate passed: " + detail
    assert "README.md" in detail


def test_a_banned_phrase_is_read_as_a_reader_reads_it(tmp_path):
    """broken over two lines; with the apostrophe a typesetter sets; with a word in emphasis"""
    phrase = _banned()
    first, rest = phrase.split(" ", 1)
    for name, text in (("two_lines", first + "\n" + rest), ("apostrophe", phrase.replace("'", "’")),
                       ("emphasis", first + " **" + rest.split(" ", 1)[0] + "** " + rest.split(" ", 1)[1])):
        repo = _scratch(tmp_path / name, {"docs/PAGE.md": "It is said that " + text + ", and more.\n"})
        ok, detail = _gate(repo, "framing")
        assert ok is False, f"a banned phrase ({name}) passed the framing gate: {detail}"


def test_the_framing_gate_reads_a_file_whatever_its_name_ends_in(tmp_path):
    phrase = _banned()
    for rel in ("docs/page.rst", "frontier/B1_an_arc/arc_verdict.json", "papers/refs.bib", "story/chapter", "NOTES"):
        text = json.dumps({"claim_one_line": phrase}) if rel.endswith(".json") else "Here: " + phrase + "\n"
        repo = _scratch(tmp_path / rel.replace("/", "_"), {rel: text})
        ok, detail = _gate(repo, "framing")
        assert ok is False, f"a banned phrase in {rel} passed the framing gate: {detail}"
        assert rel in detail


def test_the_framing_gate_says_what_it_did_not_read(tmp_path):
    limit = getattr(_gates(), "FRAMING_MAX_BYTES", 5_000_000)
    data = "0123456789abcdef\n" * (limit // 17 + 2)                                    # a file above the limit: data, not a page
    repo = _scratch(tmp_path, {"docs/PAGE.md": "A page that claims nothing.\n", "frontier/B1_an_arc/census.jsonl": data,
                               "frontier/B1_an_arc/picture.png": b"\x89PNG\r\n\x1a\n\xff\xfe\x00\x00"})
    ok, detail = _gate(repo, "framing")
    assert ok is True, detail
    assert "1 above" in detail and "1 that are not text" in detail, "the gate does not say what it did not read: " + detail


def test_what_the_framing_gate_exempts_is_held_by_name():
    """an exemption is a file in which a banned phrase may stand.  A new one shows here as well as in the gate."""
    g = _gates()
    assert g.FRAMING_EXEMPT == {"GOVERNANCE.md", "scripts/gates/gates.py", "tests/test_repo_gates.py", "docs/atlas/FAILURE_ATLAS.md",
                                "frontier/B887_gate_audit/audit_reports.json"}
    ok, detail = g.GATES["framing"]()
    assert ok is True, detail
