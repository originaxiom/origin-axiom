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
    probe = ("import fcntl, socket, struct\nup = []\nfor _, n in socket.if_nameindex():\n    s = socket.socket()\n"
             "    f = struct.unpack('16sH', fcntl.ioctl(s.fileno(), 0x8913, struct.pack('16sH', n.encode(), 0)))[1]\n"
             "    if f & 1 and n != 'lo':\n        up.append(n)\nraise SystemExit(7 if not up else 0)\n")   # M68: up, not present
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



def test_a_runs_temporary_directories_are_its_own_m68(tmp_path):
    """main's M68 point 2: one card's run wrote /tmp and changed a later card's line. Each run has its own /tmp, /var/tmp
    and /dev/shm: a file written there is not seen outside, nor by the next run"""
    prefix, name = SANDBOX
    if not prefix:
        pytest.skip("no unprivileged user in a network namespace on this machine (%s)" % name)
    plant = "/tmp/plant_%s" % os.urandom(4).hex()
    writer = ("import sys\nif '--plant' in sys.argv:\n    raise SystemExit(1)\nopen(%r, 'w').write('x')\n"
              "print('DECISIVE: wrote = yes')\n" % plant)
    reader = ("import os, sys\nif '--plant' in sys.argv:\n    raise SystemExit(1)\n"
              "print('DECISIVE: seen =', 'yes' if os.path.exists(%r) else 'no')\n" % plant)
    _commit(tmp_path / "w", {"x.py": writer})
    _commit(tmp_path / "r", {"x.py": reader})
    n, d = RR.decisive("DECISIVE: wrote = yes\n")
    assert _rerun(tmp_path / "w", _card(tmp_path / "w", n=n, d=d), allow_static=False)["status"] == "REPRODUCED"
    assert not os.path.exists(plant)
    n, d = RR.decisive("DECISIVE: seen = no\n")
    assert _rerun(tmp_path / "r", _card(tmp_path / "r", n=n, d=d), allow_static=False)["status"] == "REPRODUCED"


def _probe_in(pre, cover=None, wrap=None):
    """the probe's report, run in the wrap after the shell commands `pre` (as root, inside the namespaces)"""
    import shutil
    import tempfile
    with RR.one_at_a_time():
        return _probe_in_held(pre, cover, wrap, shutil, tempfile)


def _probe_in_held(pre, cover, wrap, shutil, tempfile):
    cover = RR.world_writable() if cover is None else cover
    run_dir = pathlib.Path(tempfile.mkdtemp())
    os.chown(run_dir, 65534, 65534)
    marker = pathlib.Path(tempfile.mkdtemp(dir=RR._marker_base(cover)))
    marker.chmod(0o755)
    token = "probe_%s" % os.urandom(4).hex()
    try:
        cmd = RR.NAMESPACES + ["sh", "-c", pre + ' && exec "$@"', "sh", sys.executable, "-I", "-c", wrap or RR.WRAP,
                               str(run_dir), json.dumps(cover), sys.executable, "-I", "-c", RR.PROBE, str(marker / "x"),
                               token]
        try:
            r = subprocess.run(cmd, capture_output=True, text=True, cwd="/")
        finally:
            RR.reap(["unshare"])
        return RR.probe_holds(r.stdout, token, cover), json.loads(r.stdout.strip().splitlines()[-1])
    finally:
        shutil.rmtree(marker, ignore_errors=True)
        shutil.rmtree(run_dir, ignore_errors=True)


def test_a_namespace_with_interfaces_down_beside_the_loopback_is_accepted_m68():
    """main's M68 point 1: a kernel with tunnel modules shows tunl0, gre0, sit0 and others, all down, in a new namespace.
    The probe asks that none is up, not that none is there: a dummy interface, down, is planted beside the loopback"""
    import shutil
    if not SANDBOX[0] or not shutil.which("ip"):
        pytest.skip("planting an interface needs the wrap and ip")
    (ok, why), r = _probe_in("ip link add d0 type dummy")
    assert ok and r["up"] == [], why
    (ok, why), r = _probe_in("ip link add d0 type dummy && ip link set d0 up")
    assert not ok and r["up"] == ["d0"]                                   # an interface up: the wrap is not trusted


def test_a_wrap_that_keeps_root_is_refused_and_the_write_is_refused_for_want_of_permission_m70(monkeypatch):
    """main's M70 point 1: the probe's marker was under /tmp, hidden inside the wrap by its tmpfs, so a wrap that kept root
    passed. The marker is now where no tmpfs covers it; the write must be refused for want of permission, and the run must
    be nobody, with no groups"""
    if not SANDBOX[0]:
        pytest.skip("no wrap on this machine (%s)" % SANDBOX[1])
    cover = RR.world_writable()
    base = RR._marker_base(cover)
    assert base and not any(base == c or base.startswith(c + "/") for c in cover)
    hidden_home = pathlib.Path(cover[0]) / ("home_%s" % os.urandom(3).hex())      # a home under a tmpfs is passed over
    hidden_home.mkdir()
    try:
        monkeypatch.setenv("HOME", str(hidden_home))
        assert RR._marker_base(cover) != str(hidden_home) and RR._marker_base([]) == str(hidden_home)
    finally:
        monkeypatch.undo()
        hidden_home.rmdir()
    (ok, why), r = _probe_in("true")
    assert ok and r["write"] == "denied" and r["ids"] == [65534] * 4 and r["groups"] == [], why
    root_kept = RR.WRAP.replace("os.setgroups([])\nos.setgid(65534)\nos.setuid(65534)\n", "")
    assert root_kept != RR.WRAP
    (ok, why), r = _probe_in("true", wrap=root_kept)
    assert not ok and r["write"] == "wrote" and r["ids"] == [0] * 4
    monkeypatch.setattr(RR, "WRAP", root_kept)
    assert RR.sandbox_prefix() == ([], "no sandbox")
    hidden = {"up": [], "write": "not denied: FileNotFoundError", "ids": [65534] * 4, "groups": [], "put": [],
              "writable": []}
    assert RR.probe_holds(json.dumps(hidden), "t", [])[0] is False      # hidden is not refused


def _plant_dirs():
    """two world-writable directories the wrap must cover: /run/lock, as on Ubuntu's runners, and /dev/mqueue, made when
    the machine has none; and a third of the test's own, outside every place the code names"""
    made = []
    for d in ("/run/lock", "/dev/mqueue", "/opt/plant_ww_%s" % os.urandom(3).hex()):
        if not os.path.isdir(d):
            os.makedirs(d)
            made.append(d)
        os.chmod(d, 0o1777)
    return made


def test_every_world_writable_directory_is_the_runs_own_and_a_wrap_that_misses_one_is_refused_m70(tmp_path, monkeypatch):
    """main's M70 point 2: /run/lock and /dev/mqueue were shared between runs. The runner finds every world-writable
    directory and the wrap covers each with a fresh tmpfs; the probe searches, as nobody, for any directory it can write
    outside its folder and its tmpfs, and refuses the wrap that misses one"""
    if not SANDBOX[0] or os.geteuid() != 0:
        pytest.skip("the wrap, as root, is needed to plant the directories")
    with RR.one_at_a_time():                         # no probe of another test lists the directories meanwhile
        made = _plant_dirs()
    try:
        cover = RR.world_writable()
        assert {"/run/lock", "/dev/mqueue", made[-1]} <= set(cover)
        token = "plant_%s" % os.urandom(4).hex()
        writer = ("import os, sys\nif '--plant' in sys.argv:\n    raise SystemExit(1)\nn = 0\n"
                  "for d in %r:\n    try:\n        open(os.path.join(d, %r), 'w').write('x')\n        n += 1\n"
                  "    except OSError:\n        pass\nprint('DECISIVE: wrote =', n == %d)\n" % (cover, token, len(cover)))
        reader = ("import os, sys\nif '--plant' in sys.argv:\n    raise SystemExit(1)\n"
                  "print('DECISIVE: seen =', any(os.path.exists(os.path.join(d, %r)) for d in %r))\n" % (token, cover))
        _commit(tmp_path / "w", {"x.py": writer})
        _commit(tmp_path / "r", {"x.py": reader})
        n, d = RR.decisive("DECISIVE: wrote = True\n")
        res = _rerun(tmp_path / "w", _card(tmp_path / "w", n=n, d=d), prefix=SANDBOX[0])   # probed before the plant
        assert res["status"] == "REPRODUCED", res
        assert not any(os.path.exists(os.path.join(c, token)) for c in cover)
        n, d = RR.decisive("DECISIVE: seen = False\n")
        res = _rerun(tmp_path / "r", _card(tmp_path / "r", n=n, d=d), prefix=SANDBOX[0])
        assert res["status"] == "REPRODUCED", res
        # a wrap that covers only the three of M68 is refused: the probe finds /run/lock and the others writable
        (ok, why), r = _probe_in("true", cover=cover + ["/opt/plant_gone_%s" % os.urandom(3).hex()])
        assert r["put"] == cover                     # a directory gone since the list was made is passed over
        (ok, why), r = _probe_in("true", cover=["/tmp", "/var/tmp", "/dev/shm"])
        assert not ok and {"/run/lock", "/dev/mqueue", made[-1]} <= set(r["writable"]), why
        monkeypatch.setattr(RR, "world_writable", lambda top="/": ["/tmp", "/var/tmp", "/dev/shm"])
        assert RR.sandbox_prefix() == ([], "no sandbox")
    finally:
        with RR.one_at_a_time():                     # no run of another test is mounting over them meanwhile
            for d in made:
                os.rmdir(d)


LEAVER = "\n".join([
    "import os, subprocess, sys",
    "if '--plant' in sys.argv:",
    "    raise SystemExit(1)",
    "child = ('import os, time\\n'",
    "         'for _ in range(100):\\n'",
    "         '    time.sleep(0.1)\\n'",
    "         '    for p in os.listdir(\"/proc\"):\\n'",
    "         '        try:\\n'",
    "         '            open(\"/proc/%s/cwd/data.txt\" % p, \"w\").write(\"rewritten\")\\n'",
    "         '        except OSError:\\n'",
    "         '            pass\\n')",
    "subprocess.Popen([sys.executable, '-c', child], start_new_session=True, stdout=subprocess.DEVNULL,",
    "                 stderr=subprocess.DEVNULL)",
    "print('DECISIVE: left = a child')", ""])
READER = ("import sys, time\nif '--plant' in sys.argv:\n    raise SystemExit(1)\ntime.sleep(2)\n"
          "print('DECISIVE: data =', open('data.txt').read())\n")


def _leave_then_read(tmp_path, prefix):
    _commit(tmp_path / "a", {"x.py": LEAVER})
    _commit(tmp_path / "b", {"x.py": READER, "data.txt": "as committed"})
    n, d = RR.decisive("DECISIVE: left = a child\n")
    a = _rerun(tmp_path / "a", _card(tmp_path / "a", n=n, d=d), prefix=prefix)
    n, d = RR.decisive("DECISIVE: data = as committed\n")
    b = _rerun(tmp_path / "b", _card(tmp_path / "b", n=n, d=d), prefix=prefix)
    return a, b


def test_a_process_left_by_one_run_cannot_reach_the_next_m70(tmp_path, monkeypatch):
    """main's M70 point 3: card A left a detached child, which reached card B's folder through /proc/<pid>/cwd and
    rewrote its committed data.txt. Each run has its own PID namespace, and every process of nobody is killed after it.
    Each wall is tried alone"""
    if not SANDBOX[0]:
        pytest.skip("no wrap on this machine (%s)" % SANDBOX[1])
    a, b = _leave_then_read(tmp_path / "both", SANDBOX[0])
    assert a["status"] == "REPRODUCED" and b["status"] == "REPRODUCED", (a, b)
    with monkeypatch.context() as m:                # the PID namespace alone
        m.setattr(RR, "reap", lambda prefix: True)
        a, b = _leave_then_read(tmp_path / "pid", SANDBOX[0])
        assert a["status"] == "REPRODUCED" and b["status"] == "REPRODUCED", (a, b)
    no_pid = [x for x in SANDBOX[0] if x not in ("-p", "-f", "--kill-child", "--mount-proc")]
    a, b = _leave_then_read(tmp_path / "kill", no_pid)   # the kill alone: no PID namespace
    assert a["status"] == "REPRODUCED" and b["status"] == "REPRODUCED", (a, b)
    # and the kill comes after each run, not only before the next: here the control, the card's last run, leaves a child
    _commit(tmp_path / "after", {"x.py": LEAVER.replace("if '--plant' in sys.argv:\n    raise SystemExit(1)\n", "")
                                 .replace("print('DECISIVE: left = a child')", "print('DECISIVE: left = a child')\n"
                                          "if '--plant' in sys.argv:\n    raise SystemExit(1)")})
    n, d = RR.decisive("DECISIVE: left = a child\n")
    assert _rerun(tmp_path / "after", _card(tmp_path / "after", n=n, d=d), prefix=no_pid)["status"] == "REPRODUCED"
    with RR.one_at_a_time():                         # no other run is alive while the lock is held
        assert subprocess.run(["pgrep", "-U", "65534", "-r", "R,S,D,T,t,I"], capture_output=True).returncode == 1
    with RR.one_at_a_time():                         # a process of nobody outside any namespace is killed
        p = subprocess.Popen(["setpriv", "--reuid=65534", "--regid=65534", "--clear-groups", "sleep", "30"])
        try:
            assert RR.reap(no_pid) and p.wait(timeout=10) == -9
        finally:
            p.kill()


def test_the_guard_follows_builtins_by_its_aliases_m70(tmp_path):
    for src, ok in (("from builtins import exec as e\ne('1')\n", False), ("import builtins as b\nb.exec('1')\n", False),
                    ("import builtins\nb = builtins\nb.eval('1')\n", False), ("from builtins import *\n", False),
                    ("from builtins import print as p\np('x')\n", True), ("import builtins as b\nb.print('x')\n", True)):
        repo = tmp_path / str(abs(hash(src)))
        _commit(repo, {"x.py": src + GOOD})
        res = _rerun(repo, _card(repo))
        assert (res["status"] == "REPRODUCED") is ok, (src, res)


def test_re_compile_passes_the_guard_and_the_builtin_does_not_m69(tmp_path):
    for src, ok in (("import re\nre.compile('x')\n", True), ("compile('1', 'x', 'eval')\n", False),
                    ("import builtins\nbuiltins.compile('1', 'x', 'eval')\n", False), ("class C:\n    def eval(self):\n        return 1\nC().eval()\n", True)):
        repo = tmp_path / str(abs(hash(src)))
        _commit(repo, {"x.py": src + GOOD})
        res = _rerun(repo, _card(repo))
        assert (res["status"] == "REPRODUCED") is ok, (src, res)


def test_where_its_tools_are_the_wrap_is_found_and_a_wrap_that_shares_tmp_is_not_m68(monkeypatch):
    """the sandbox's tests skip where no wrap can be made; so where the tools stand (root, unshare, mount, pkill, pgrep) the
    wrap must be found, or a broken wrap would pass as a skip. A wrap that cuts the network and drops the user but shares
    /tmp is refused by the probe"""
    import shutil
    if os.geteuid() != 0 or not all(shutil.which(c) for c in ("unshare", "setpriv", "mount", "pkill", "pgrep")):
        pytest.skip("not root, or unshare, setpriv, mount, pkill or pgrep missing")
    assert RR.sandbox_prefix()[0], "root with unshare, mount, pkill and pgrep, and no wrap found"
    shared = ["unshare", "-n", "--", "setpriv", "--reuid=65534", "--regid=65534", "--clear-groups", "--"]
    monkeypatch.setattr(RR, "STRATEGIES", [(lambda: True, shared, "the network and the user, /tmp shared")])
    assert RR.sandbox_prefix() == ([], "no sandbox")


def test_the_probes_report_is_read_field_by_field_m70(tmp_path):
    cover = [str(tmp_path / "c")]
    good = {"up": [], "write": "denied", "ids": [65534] * 4, "groups": [], "put": cover, "writable": []}
    assert RR.probe_holds(json.dumps(good), "t", cover) == (True, "")
    for field, value, words in (("up", ["eth0"], "interfaces up"), ("write", "wrote", "was wrote"),
                                ("write", "not denied: FileNotFoundError", "not denied"),
                                ("ids", [65534, 65534, 0, 0], "not nobody alone"), ("groups", [0], "not nobody alone"),
                                ("writable", ["/run/lock"], "can write outside"), ("put", [], "shared with the runner")):
        ok, why = RR.probe_holds(json.dumps(dict(good, **{field: value})), "t", cover)
        assert not ok and words in why, (field, why)
    (tmp_path / "c").mkdir()
    (tmp_path / "c" / "t").write_text("x")                     # the probe's file, seen outside: the tmpfs is shared
    assert RR.probe_holds(json.dumps(good), "t", cover)[0] is False
    assert RR.probe_holds("no report", "t", cover) == (False, "the probe printed no report")


def test_two_runs_at_once_on_one_machine_do_not_end_each_other_m70(tmp_path):
    """the kill ends every process of nobody, so runs at once on one machine (two rounds, or tests in parallel) take the
    machine's sandbox lock, one at a time: a slow run and a quick one, started together, both hold"""
    import threading
    if not SANDBOX[0]:
        pytest.skip("no wrap on this machine (%s)" % SANDBOX[1])
    _commit(tmp_path / "slow", {"x.py": READER, "data.txt": "as committed"})
    _commit(tmp_path / "quick", {"x.py": GOOD})
    n, d = RR.decisive("DECISIVE: data = as committed\n")
    slow_card = _card(tmp_path / "slow", n=n, d=d)
    out = {}
    t = threading.Thread(target=lambda: out.update(slow=_rerun(tmp_path / "slow", slow_card, prefix=SANDBOX[0])))
    t.start()
    import time
    time.sleep(0.5)
    out["quick"] = _rerun(tmp_path / "quick", _card(tmp_path / "quick"), prefix=SANDBOX[0])
    t.join()
    assert out["slow"]["status"] == "REPRODUCED" and out["quick"]["status"] == "REPRODUCED", out


def test_no_filesystem_walk_where_no_wrap_is_usable(monkeypatch):
    """main, 2026-11-28, at landing: where no wrap can be made the probe answers "no sandbox" without walking the disk"""
    def walk(*a, **k):
        raise AssertionError("world_writable was called although no wrap is usable")
    monkeypatch.setattr(RR, "world_writable", walk)
    monkeypatch.setattr(RR, "STRATEGIES", [(lambda: False, ["unshare", "--", "true"], "never usable"),
                                           (lambda: True, ["no-such-tool-anywhere", "--", "true"], "no tool")])
    assert RR.sandbox_prefix() == ([], "no sandbox")
