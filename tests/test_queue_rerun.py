"""2026-11-26 (the framework's thin path, patch T5; main's M54; register row P-885): the sandboxed rerun,
scripts/queue/rerun.py.

On small repositories built here: a script whose decisive lines are the card's and whose failing control fails is
REPRODUCED; it is returned when its lines differ, when the control does not fail, when it imports a package not allowed or
a network module, or when its command is not a plain run; it is heavy when it needs sage or runs past the limit. The same
values printed two ways normalise alike; a module beside the script is read too; the network cut is tested before it is
trusted; the pins file names every allowed package; the command runs by hand."""
import importlib.util
import json

import pytest
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

- decisive script: x.py, SHA-256 0123456789abcdef, depends on the standard library, run as {cmd}, output SHA-256 0011223344556677
- decisive lines: {n} lines marked "DECISIVE:", SHA-256 {h}
- failing control: {control}
"""


def _commit(tmp_path, files):
    tmp_path.mkdir(parents=True, exist_ok=True)
    g = lambda *a: subprocess.run(["git", "-c", "user.name=t", "-c", "user.email=t@t", *a], cwd=tmp_path,
                                  capture_output=True, text=True, check=True).stdout
    g("init", "-q")
    for name, text in files.items():
        (tmp_path / name).parent.mkdir(parents=True, exist_ok=True)
        (tmp_path / name).write_text(text, encoding="utf-8")
    g("add", "-A")
    g("commit", "-q", "-m", "c")
    return g("rev-parse", "HEAD").strip()


def _card(cmd="python3 x.py", control="python3 x.py --plant", n=LINES[0], h=LINES[1]):
    return CARD.format(cmd=cmd, control=control, n=n, h=h)


def test_a_script_that_holds_is_reproduced_and_each_break_returns_it(tmp_path):
    c = _commit(tmp_path / "ok", {"x.py": GOOD})
    res = RR.rerun(tmp_path / "ok", c, _card(), limit=60)
    assert res["status"] == "REPRODUCED", res
    assert res["decisive"] == {"lines": 2, "sha256": LINES[1]} and res["control_exit"] == 1 and res["guard"]
    cases = [
        (_card(h="0" * 16), "the decisive lines are 2 with hash"),
        (_card(control="python3 x.py"), "did not fail"),
        (_card(cmd="python3 x.py; curl example.org"), "not a plain run"),
        (_card(cmd="python3 y.py"), "not a plain run"),
        (_card(cmd="python3 x.py > out.txt"), "not a plain run"),
        (_card(control="bash -c true"), "failing control is not a plain run"),
        (CARD.format(cmd="python3 x.py", control="python3 x.py --plant", n=2, h="short"), "not in form"),
    ]
    for card, words in cases:
        res = RR.rerun(tmp_path / "ok", c, card, limit=60)
        assert res["status"] == "RETURNED_AT_INTAKE" and any(words in r for r in res["reasons"]), (words, res)


def test_what_a_script_may_import(tmp_path):
    for name, src, words in (("pkg", "import pandas\n", "not allowed: pandas"),
                             ("net", "import urllib.request\n", "not allowed: urllib"),
                             ("sock", "from socket import create_connection\n", "not allowed: socket"),
                             ("call", "__import__('json')\n", "imports by a call")):
        c = _commit(tmp_path / name, {"x.py": src + GOOD})
        res = RR.rerun(tmp_path / name, c, _card(), limit=60)
        assert res["status"] == "RETURNED_AT_INTAKE" and any(words in r for r in res["reasons"]), (name, res)
    # a module beside the script is read too, and its own imports with it
    c = _commit(tmp_path / "sib", {"x.py": "import helper\n" + GOOD, "helper.py": "import math\n"})
    assert RR.rerun(tmp_path / "sib", c, _card(), limit=60)["status"] == "REPRODUCED"
    c = _commit(tmp_path / "sib2", {"x.py": "import helper\n" + GOOD, "helper.py": "import requests\n"})
    res = RR.rerun(tmp_path / "sib2", c, _card(), limit=60)
    assert res["status"] == "RETURNED_AT_INTAKE" and "not allowed: requests" in res["reasons"][0]


def test_heavy_cards_are_not_failures(tmp_path):
    c = _commit(tmp_path / "sage", {"x.py": "from sage.all import QQ\n" + GOOD})
    assert RR.rerun(tmp_path / "sage", c, _card(), limit=60)["status"] == "HEAVY"
    c = _commit(tmp_path / "slow", {"x.py": "import time\ntime.sleep(30)\n" + GOOD})
    res = RR.rerun(tmp_path / "slow", c, _card(), limit=2)
    assert res["status"] == "HEAVY" and "ran past 2 seconds" in res["reasons"][0]


def test_the_same_values_normalise_alike():
    a = RR.decisive("DECISIVE:  x =  0.30000000000000004\nDECISIVE: n = 12\nnoise 1.5\n")
    b = RR.decisive("DECISIVE: x = 0.3\n  DECISIVE: n = 12\n")
    assert a == b and a[0] == 2
    assert RR.decisive("DECISIVE: x = 0.31\nDECISIVE: n = 12\n") != a
    assert RR.decisive("DECISIVE: n = 13\nDECISIVE: x = 0.3\n") != a
    assert RR.normalise("DECISIVE: 1e-3 and 2.50 and 7") == "DECISIVE: 0.001 and 2.5 and 7"


def test_the_network_cut_is_tested_before_it_is_trusted(monkeypatch):
    monkeypatch.setattr(RR, "STRATEGIES", [(["env", "--"], "a wrap that cuts nothing")])
    assert RR.sandbox_prefix() == ([], "static guard only")
    monkeypatch.undo()
    prefix, name = RR.sandbox_prefix()
    if prefix:
        r = subprocess.run(prefix + [sys.executable, "-c", RR.PROBE], capture_output=True)
        assert r.returncode == 7, name
    else:
        assert name == "static guard only"


def test_the_pins_name_every_allowed_package_and_flint_and_sage_are_there():
    pins = json.loads((ROOT / "scripts/queue/ALLOWED_PACKAGES.json").read_text(encoding="utf-8"))
    assert set(pins["packages"]) == {"mpmath", "sympy", "numpy", "scipy", "python-flint"}
    assert pins["packages"]["python-flint"]["module"] == "flint" and set(pins["heavy"]) == {"sage", "GAP"}
    assert not (RR.NETWORK & RR.STDLIB) and "socket" not in RR.STDLIB and "json" in RR.STDLIB


def test_the_command_runs_by_hand(tmp_path):
    c = _commit(tmp_path, {"x.py": GOOD, "relays/claims/.keep": ""})
    (tmp_path / "relays" / "claims" / "CLAIM_a.md").write_text("# CLAIM CARD — a\n\n" + _card().split("\n", 2)[2],
                                                                encoding="utf-8")
    g = lambda *a: subprocess.run(["git", "-c", "user.name=t", "-c", "user.email=t@t", *a], cwd=tmp_path,
                                  capture_output=True, text=True, check=True).stdout
    g("add", "-A")
    g("commit", "-q", "-m", "the card")
    rec = {"commit": g("rev-parse", "HEAD").strip(), "card_path": "relays/claims/CLAIM_a.md"}
    (tmp_path / "rec.json").write_text(json.dumps(rec), encoding="utf-8")
    r = subprocess.run([sys.executable, "-B", str(ROOT / "scripts/queue/rerun.py"), "--record", str(tmp_path / "rec.json"),
                        "--root", str(tmp_path), "--limit", "60"], capture_output=True, text=True, timeout=300)
    assert r.returncode == 0 and json.loads(r.stdout)["status"] == "REPRODUCED", r.stdout + r.stderr


def test_a_script_that_reaches_for_the_network_by_a_child_process_finds_it_cut(tmp_path):
    """the static guard does not see `subprocess`; the namespace does: the child's connection fails inside the run"""
    prefix, name = RR.sandbox_prefix()
    if not prefix:                                        # main's M59: say so, not pass in silence
        pytest.skip("no network namespace on this machine (%s): only the static guard runs here" % name)
    src = ("import subprocess, sys\nr = subprocess.run([sys.executable, '-c', %r])\nprint('DECISIVE: probe =', r.returncode)\n"
           % RR.PROBE)
    c = _commit(tmp_path, {"x.py": src + "if '--plant' in sys.argv:\n    raise SystemExit(1)\n"})
    n, h = RR.decisive("DECISIVE: probe = 7\n")
    res = RR.rerun(tmp_path, c, _card(n=n, h=h), limit=60)
    assert res["status"] == "REPRODUCED", res


def test_a_control_fails_only_by_exiting_1_with_no_traceback_t1b(tmp_path):
    """main's M58 and M59: a control that crashes also exits 1, and was counted as failing; a control that exits 2 is
    invalid too. Both return the card; a control that exits 1 cleanly still passes"""
    crash = GOOD.replace('    raise SystemExit(1)', '    raise RuntimeError("planted before anything is tested")')
    c = _commit(tmp_path / "crash", {"x.py": crash})
    res = RR.rerun(tmp_path / "crash", c, _card(), limit=60)
    assert res["status"] == "RETURNED_AT_INTAKE" and any("with a traceback" in r for r in res["reasons"]), res
    two = GOOD.replace('    raise SystemExit(1)', '    raise SystemExit(2)')
    c = _commit(tmp_path / "two", {"x.py": two})
    res = RR.rerun(tmp_path / "two", c, _card(), limit=60)
    assert res["status"] == "RETURNED_AT_INTAKE" and any("it exited 2" in r for r in res["reasons"]), res
    c = _commit(tmp_path / "ok", {"x.py": GOOD})
    assert RR.rerun(tmp_path / "ok", c, _card(), limit=60)["status"] == "REPRODUCED"


def test_a_card_declared_heavy_is_heavy_after_its_checks_t1b(tmp_path):
    """main's M58: a card may declare its script heavy (one that runs sage as a child process is not seen in its
    imports); the declaration only adds work: a script that fails a check before the run is still returned"""
    heavy = _card().replace("output SHA-256 0011223344556677", "output SHA-256 0011223344556677, heavy")
    c = _commit(tmp_path / "h", {"x.py": GOOD})
    res = RR.rerun(tmp_path / "h", c, heavy, limit=60)
    assert res["status"] == "HEAVY" and "declares" in res["reasons"][0]
    c = _commit(tmp_path / "bad", {"x.py": "import pandas\n" + GOOD})
    assert RR.rerun(tmp_path / "bad", c, heavy, limit=60)["status"] == "RETURNED_AT_INTAKE"
