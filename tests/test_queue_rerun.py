"""2026-11-27 (the framework's thin path, patch T5, rebuilt by T7b; main's M58, M59, M62, M64 and M65; register row P-885):
the sandboxed rerun, scripts/queue/rerun.py.

On small repositories built here: a script whose decisive lines are the card's and whose failing control fails is
REPRODUCED, and each break returns it; what a script, its control and the modules beside them may import (M64 items 3 and
4); a symlinked script, control or module is refused, and a commit's .gitattributes cannot change what runs (items 1, 2);
every check that needs no run comes before HEAVY (item 7); a slow control cannot turn a failed rerun into HEAVY (item 6);
the numbers are normalised to 12 digits, no more and no fewer (item 25); the wrap is trusted only when it cuts the network
AND refuses a write outside its own directory, seat code cannot write into the runner's directories (M62), and where no
wrap works no seat code runs (item 4); the pins file is the allowed list; the command runs by hand."""
import hashlib
import importlib.util
import json
import os
import pathlib
import subprocess
import sys

import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]


def _load(name, rel):
    spec = importlib.util.spec_from_file_location(name, ROOT / rel)
    m = importlib.util.module_from_spec(spec)
    sys.dont_write_bytecode = True
    spec.loader.exec_module(m)
    return m


RR = _load("rerun_under_test", "scripts/queue/rerun.py")
GOOD = """import sys
if "--plant" in sys.argv:
    raise SystemExit(1)
print("a line that decides nothing, timed at 0.0123 s")
print("DECISIVE: classes at level 5 = 12")
print("DECISIVE: ratio = 0.30000000000000004")
"""
LINES = RR.decisive("DECISIVE: classes at level 5 = 12\nDECISIVE: ratio = 0.3\n")
CARD = """# CLAIM CARD — a count

- decisive script: {script}, SHA-256 {h}, depends on the standard library, run as {cmd}, output SHA-256 0011223344556677{heavy}
- decisive lines: {n} lines marked "DECISIVE:", SHA-256 {d}
- failing control: {control}
"""
SANDBOX = RR.sandbox_prefix()


def _commit(tmp_path, files, links=None):
    tmp_path.mkdir(parents=True, exist_ok=True)
    g = lambda *a: subprocess.run(["git", "-c", "user.name=t", "-c", "user.email=t@t", *a], cwd=tmp_path,
                                  capture_output=True, text=True, check=True).stdout
    g("init", "-q")
    for name, text in files.items():
        (tmp_path / name).parent.mkdir(parents=True, exist_ok=True)
        (tmp_path / name).write_text(text, encoding="utf-8")
    for name, target in (links or {}).items():
        os.symlink(target, tmp_path / name)
    g("add", "-A")
    g("commit", "-q", "-m", "c")
    return g("rev-parse", "HEAD").strip()


def _card(repo=None, script="x.py", cmd=None, control=None, n=LINES[0], d=LINES[1], h=None, heavy=""):
    if h is None:
        h = hashlib.sha256((repo / script).read_bytes()).hexdigest()[:16] if repo else "0" * 16
    return CARD.format(script=script, h=h, cmd=cmd or "python3 %s" % script, n=n, d=d, heavy=heavy,
                       control=control or "python3 %s --plant" % script)


def _rerun(repo, card, **kw):
    kw.setdefault("limit", 60)
    kw.setdefault("allow_static", True)
    c = subprocess.run(["git", "rev-parse", "HEAD"], cwd=repo, capture_output=True, text=True).stdout.strip()
    return RR.rerun(repo, c, card, **kw)


def _returned(res, words):
    return res["status"] == "RETURNED_AT_INTAKE" and any(words in r for r in res["reasons"])


def test_a_script_that_holds_is_reproduced_and_each_break_returns_it(tmp_path):
    repo = tmp_path / "ok"
    _commit(repo, {"x.py": GOOD, "c.py": "raise SystemExit(1)\n"})
    res = _rerun(repo, _card(repo))
    assert res["status"] == "REPRODUCED", res
    assert res["decisive"] == {"lines": 2, "sha256": LINES[1]} and res["control_exit"] == 1
    for card, words in (
            (_card(repo, d="0" * 16), "the decisive lines are 2 with hash"),
            (_card(repo, control="python3 c.py --other"), "REPRODUCED"),
            (_card(repo, control="python3 x.py"), "the failing control is the decisive command itself"),
            (_card(repo, cmd="python3 x.py; curl example.org"), "not a plain run"),
            (_card(repo, cmd="python3 c.py"), "not a plain run of the decisive script"),
            (_card(repo, cmd="python3 /etc/x.py", script="x.py"), "not a plain run"),
            (_card(repo, control="bash -c true"), "failing control is not a plain run"),
            (_card(repo, h="0" * 16), "is not the one the card hashes"),
            (_card(script="../x.py", h="0" * 16), "leaves the commit")):
        res = _rerun(repo, card)
        if words == "REPRODUCED":                      # another script of the commit as the control, exiting 1: it holds
            assert res["status"] == "REPRODUCED", res
            continue
        assert _returned(res, words), (words, res)


@pytest.mark.parametrize("src, words", [
    ("import pandas\n", "not allowed: pandas"),
    ("import urllib.request\n", "not allowed: urllib"),
    ("from socket import create_connection\n", "not allowed: socket"),
    ("import _socket\n", "not allowed: _socket"),
    ("import ctypes\n", "not allowed: ctypes"),
    ("import multiprocessing\n", "not allowed: multiprocessing"),
    ("import logging.handlers\n", "imports logging.handlers"),
    ("from logging import handlers\n", "imports logging.handlers"),
    ("import importlib\n", "not allowed: importlib"),
    ("exec('import socket')\n", "calls exec"),
    ("getattr(__builtins__, '__import__')('socket')\n", "__import__"),
    ("import sys\nsys.path.append('/x')\n", "changes sys.path"),
    ("import sys\nsys.path = ['/x']\n", "changes sys.path"),
])
def test_what_a_script_may_import(tmp_path, src, words):
    _commit(tmp_path, {"x.py": src + GOOD})
    res = _rerun(tmp_path, _card(tmp_path))
    assert _returned(res, words), res


def test_the_controls_imports_and_the_modules_beside_are_guarded_too(tmp_path):
    repo = tmp_path / "c"
    _commit(repo, {"x.py": GOOD, "c.py": "import socket\nraise SystemExit(1)\n"})
    assert _returned(_rerun(repo, _card(repo, control="python3 c.py")), "not allowed: socket")
    repo = tmp_path / "sib"
    _commit(repo, {"x.py": "import helper\n" + GOOD, "helper.py": "import math\n"})
    assert _rerun(repo, _card(repo))["status"] == "REPRODUCED"
    repo = tmp_path / "sib2"
    _commit(repo, {"x.py": "import helper\n" + GOOD, "helper.py": "import requests\n"})
    assert _returned(_rerun(repo, _card(repo)), "not allowed: requests")


def test_symlinks_are_refused_and_gitattributes_change_nothing(tmp_path):
    outside = tmp_path / "outside.py"
    outside.write_text(GOOD, encoding="utf-8")
    repo = tmp_path / "link"
    _commit(repo, {"c.py": "raise SystemExit(1)\n"}, links={"x.py": str(outside)})
    assert _returned(_rerun(repo, _card(h="0" * 16, control="python3 c.py")), "is a symlink at the commit")
    repo = tmp_path / "ctl"
    _commit(repo, {"x.py": GOOD}, links={"c.py": str(outside)})
    assert _returned(_rerun(repo, _card(repo, control="python3 c.py")), "c.py is a symlink at the commit")
    repo = tmp_path / "mod"
    _commit(repo, {"x.py": "import helper\n" + GOOD}, links={"helper.py": str(outside)})
    assert _returned(_rerun(repo, _card(repo)), "helper.py, which is a symlink at the commit")
    # export-subst would rewrite $Format:...$ on the way out of `git archive`; the blob is what is written and hashed
    repo = tmp_path / "attrs"
    src = GOOD.replace("timed at 0.0123 s", "commit $Format:%H$")
    _commit(repo, {"x.py": src, ".gitattributes": "x.py export-subst\n"})
    res = _rerun(repo, _card(repo))
    assert res["status"] == "REPRODUCED", res


def test_every_check_that_needs_no_run_comes_before_heavy(tmp_path):
    repo = tmp_path / "sage"
    _commit(repo, {"x.py": "from sage.all import QQ\n" + GOOD})
    assert _rerun(repo, _card(repo))["status"] == "HEAVY"
    assert _returned(_rerun(repo, _card(repo, h="0" * 16)), "not the one the card hashes")
    assert _returned(_rerun(repo, _card(repo, control="bash -c true")), "failing control is not a plain run")
    repo = tmp_path / "dotsage"
    _commit(repo, {"x.sage": "print('DECISIVE: n = 12')\n", "c.py": "raise SystemExit(1)\n"})
    ok = _card(repo, script="x.sage", cmd="sage x.sage", control="python3 c.py")
    assert _rerun(repo, ok)["status"] == "HEAVY"
    assert _returned(_rerun(repo, _card(repo, script="x.sage", cmd="sage x.sage", control="sage x.sage")),
                     "the failing control is the decisive command itself")
    assert _returned(_rerun(repo, _card(repo, script="x.sage", cmd="sage x.sage", control="gap notes.txt")),
                     "failing control is not a plain run")
    heavy = _card(repo=None, h="0" * 16, heavy=", heavy")
    repo = tmp_path / "decl"
    _commit(repo, {"x.py": GOOD})
    assert _returned(_rerun(repo, heavy), "not the one the card hashes")
    assert _rerun(repo, _card(repo, heavy=", heavy"))["status"] == "HEAVY"


def test_a_slow_control_does_not_turn_a_failed_rerun_into_heavy(tmp_path):
    _commit(tmp_path, {"x.py": GOOD, "c.py": "import time\ntime.sleep(30)\n"})
    res = _rerun(tmp_path, _card(tmp_path, d="0" * 16, control="python3 c.py"), limit=3)
    assert _returned(res, "the decisive lines are"), res
    res = _rerun(tmp_path, _card(tmp_path, control="python3 c.py"), limit=3)
    assert res["status"] == "HEAVY" and "control ran past" in res["reasons"][0]


def test_the_numbers_are_normalised_to_twelve_digits():
    a = RR.decisive("DECISIVE:  x =  0.30000000000000004\nDECISIVE: n = 12\nnoise 1.5\n")
    assert a == RR.decisive("DECISIVE: x = 0.3\n  DECISIVE: n = 12\n") and a[0] == 2
    assert RR.normalise("DECISIVE: 0.1234567890123") == RR.normalise("DECISIVE: 0.1234567890124")    # the 13th digit
    assert RR.normalise("DECISIVE: 0.123456789012") != RR.normalise("DECISIVE: 0.123456789013")      # the 12th
    assert RR.normalise("DECISIVE: 1e-3 and 2.50 and 7") == "DECISIVE: 0.001 and 2.5 and 7"


def test_the_wrap_is_trusted_only_when_it_cuts_the_network_and_refuses_a_write(monkeypatch):
    monkeypatch.setattr(RR, "STRATEGIES", [(lambda: True, ["env", "--"], "a wrap that cuts nothing")])
    assert RR.sandbox_prefix() == ([], "no sandbox")
    if os.geteuid() == 0:                             # the network cut, the user not dropped: writes still go through
        monkeypatch.setattr(RR, "STRATEGIES", [(lambda: True, ["unshare", "-n", "--"], "the network alone")])
        assert RR.sandbox_prefix() == ([], "no sandbox")
    monkeypatch.undo()
    prefix, name = RR.sandbox_prefix()
    if not prefix:
        pytest.skip("no unprivileged user in a network namespace on this machine (%s)" % name)
    assert "nobody" in name


def test_seat_code_cannot_write_into_the_runners_directories(tmp_path):
    """main's M62: a script that writes into a directory the runner owns (the queue's folder, scripts/queue/) fails to,
    and the round's result is the same as without it"""
    prefix, name = SANDBOX
    if not prefix:
        pytest.skip("no unprivileged user in a network namespace on this machine (%s)" % name)
    runners = tmp_path / "runner_owned"
    runners.mkdir()
    runners.chmod(0o755)
    (runners / "Q0001.json").write_text('{"status": "FILED"}', encoding="utf-8")
    src = ("import sys\nif '--plant' in sys.argv:\n    raise SystemExit(1)\ntry:\n"
           "    open(%r, 'w').write('{\"status\": \"VERIFIED\"}')\n    print('DECISIVE: wrote = yes')\n"
           "except OSError:\n    print('DECISIVE: wrote = no')\n" % str(runners / "Q0001.json"))
    repo = tmp_path / "repo"
    _commit(repo, {"x.py": src})
    n, d = RR.decisive("DECISIVE: wrote = no\n")
    res = _rerun(repo, _card(repo, n=n, d=d), allow_static=False)
    assert res["status"] == "REPRODUCED", res
    assert (runners / "Q0001.json").read_text(encoding="utf-8") == '{"status": "FILED"}'


def test_where_no_wrap_works_no_seat_code_runs(tmp_path):
    marker = tmp_path / "ran"
    _commit(tmp_path / "r", {"x.py": "open(%r, 'w').write('x')\n" % str(marker) + GOOD})
    res = _rerun(tmp_path / "r", _card(tmp_path / "r"), prefix=[], allow_static=False)
    assert res["status"] == "HEAVY" and "no seat code runs" in res["reasons"][0] and not marker.exists()
    res = _rerun(tmp_path / "r", _card(tmp_path / "r"), prefix=[], allow_static=True)
    assert res["status"] == "REPRODUCED" and marker.exists() and "the author's choice" in res["guard"]


def test_a_script_that_reaches_for_the_network_by_a_child_process_finds_it_cut(tmp_path):
    prefix, name = SANDBOX
    if not prefix:
        pytest.skip("no unprivileged user in a network namespace on this machine (%s)" % name)
    probe = "import socket\nraise SystemExit(7 if [n for _, n in socket.if_nameindex()] == ['lo'] else 0)\n"
    src = ("import subprocess, sys\nif '--plant' in sys.argv:\n    raise SystemExit(1)\n"
           "r = subprocess.run([sys.executable, '-c', %r])\nprint('DECISIVE: probe =', r.returncode)\n" % probe)
    _commit(tmp_path, {"x.py": src})
    n, d = RR.decisive("DECISIVE: probe = 7\n")
    assert _rerun(tmp_path, _card(tmp_path, n=n, d=d), allow_static=False)["status"] == "REPRODUCED"


def test_the_pins_file_is_the_allowed_list():
    pins = json.loads((ROOT / "scripts/queue/ALLOWED_PACKAGES.json").read_text(encoding="utf-8"))
    assert RR.PACKAGES == {k: v["module"] for k, v in pins["packages"].items()}
    assert set(pins["heavy"]) == {"sage", "GAP"}
    for name in ("socket", "_socket", "ssl", "ctypes", "multiprocessing", "importlib"):
        assert name not in RR.STDLIB, name
    assert {"json", "math", "subprocess"} <= RR.STDLIB


def test_the_command_runs_by_hand(tmp_path):
    _commit(tmp_path, {"x.py": GOOD})
    card = "# CLAIM CARD — a\n\n" + _card(tmp_path).split("\n", 2)[2]
    (tmp_path / "relays" / "claims").mkdir(parents=True)
    (tmp_path / "relays" / "claims" / "CLAIM_a.md").write_text(card, encoding="utf-8")
    g = lambda *a: subprocess.run(["git", "-c", "user.name=t", "-c", "user.email=t@t", *a], cwd=tmp_path,
                                  capture_output=True, text=True, check=True).stdout
    g("add", "-A")
    g("commit", "-q", "-m", "the card")
    rec = {"commit": g("rev-parse", "HEAD").strip(), "card_path": "relays/claims/CLAIM_a.md"}
    (tmp_path / "rec.json").write_text(json.dumps(rec), encoding="utf-8")
    r = subprocess.run([sys.executable, "-B", str(ROOT / "scripts/queue/rerun.py"), "--record", str(tmp_path / "rec.json"),
                        "--root", str(tmp_path), "--limit", "60", "--allow-static-guard"],
                       capture_output=True, text=True, timeout=300)
    assert r.returncode == 0 and json.loads(r.stdout)["status"] == "REPRODUCED", r.stdout + r.stderr
