#!/usr/bin/env python3
"""The sandboxed rerun (the framework's thin path, patch T5; draft 1 § 9; main's M54; register row P-885).

The intake reruns a card's decisive script at its sealed commit and requires its failing control to fail. It decides:
  REPRODUCED          the script ran, printed as many lines marked "DECISIVE:" as the card says, their normalised hash is
                      the card's, and the failing control exited with a failure;
  RETURNED_AT_INTAKE  any of these did not hold, or the script imports what is not allowed, or its command is not a plain
                      run of a script of the commit; the reasons are given;
  HEAVY               the script needs sage (or GAP), or ran past the time limit: it is rerun by the same code on the
                      author's machine, when the author chooses (§ 9). Heavy is not a failure.

THE SANDBOX.
  - The commit is checked out on its own, in a temporary directory; nothing of the runner's checkout is reachable from it.
  - No network. The run is wrapped in a new network namespace (`unshare -rn`, or `sudo -n unshare -n` where unprivileged
    namespaces are closed, as on some hosted runners), and the wrap is tested before it is trusted: a connection made
    inside it must fail. Where no wrap works (a machine without unshare), the static guard below still holds, and the
    result says which guard ran.
  - The static guard: the script's imports, read from its syntax tree, are the standard library less its network modules,
    and the allowed packages; a module that is a file beside the script is read the same way.
  - About 30 minutes a run (TIME_LIMIT), the control's run included.

THE DECISIVE LINES, NORMALISED: each line the script prints that opens "DECISIVE:", with its spaces collapsed and every
number with a point or an exponent written to 12 significant digits, so the same values print the same on any machine.
The lines are joined with newlines, a newline after the last, and hashed with SHA-256; the card gives the first 16 hex.
The full output's hash, which the card also gives, is recorded and not decided on: a timing line changes it.

THE ALLOWED PACKAGES and their pins are in ALLOWED_PACKAGES.json beside this file. The versions found are recorded with
every result; a version that differs from its pin is said, and does not fail the card (the author's machine may differ).

    python3 scripts/queue/rerun.py --record queue/cards/Q0001.json            # rerun one card at its sealed commit
    python3 scripts/queue/rerun.py --record F --root REPO --limit SECONDS
Prints the result as JSON. Exit 0 when REPRODUCED or HEAVY, 1 when returned."""
import ast
import hashlib
import importlib.metadata
import importlib.util
import json
import os
import pathlib
import re
import shlex
import shutil
import subprocess
import sys
import tempfile
import time

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]
TIME_LIMIT = 1800


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    sys.dont_write_bytecode = True
    spec.loader.exec_module(m)
    return m


CF = _load("card_form_for_the_rerun", HERE / "card_form.py")
PINS = json.loads((HERE / "ALLOWED_PACKAGES.json").read_text(encoding="utf-8"))
PACKAGES = {name: pin["module"] for name, pin in PINS["packages"].items()}       # distribution -> module
HEAVY_MODULES = {"sage", "gappy", "sage_all"}
NETWORK = {"socket", "ssl", "http", "urllib", "ftplib", "smtplib", "poplib", "imaplib", "telnetlib", "xmlrpc",
           "socketserver", "asyncio", "selectors", "webbrowser", "nntplib"}
STDLIB = set(sys.stdlib_module_names) - NETWORK
NUMBER = re.compile(r"[-+]?(?:\d+\.\d*|\.\d+|\d+)(?:[eE][-+]?\d+)?")
# inside a new network namespace the only interface is the loopback: the probe exits 7 there and 0 anywhere else (a
# connection that fails is no proof, since an address can be unreachable with the network on)
PROBE = "import socket\nraise SystemExit(7 if [n for _, n in socket.if_nameindex()] == ['lo'] else 0)\n"


def normalise(line):
    """one decisive line as the rerun compares it"""
    text = " ".join(line.split())

    def num(m):
        s = m.group(0)
        if "." in s or "e" in s or "E" in s:
            return "%.12g" % float(s)
        return s
    return NUMBER.sub(num, text)


def decisive(stdout):
    """(the number of decisive lines, the first 16 hex of their normalised hash)"""
    lines = [normalise(l) for l in stdout.splitlines() if l.lstrip().startswith("DECISIVE:")]
    blob = "".join(l + "\n" for l in lines).encode("utf-8")
    return len(lines), hashlib.sha256(blob).hexdigest()[:16]


def imports_of(path, root, seen=None):
    """(the top-level modules the script imports, the sibling files it imports, problems), read from the syntax tree and
    followed into a module that is a file beside the script"""
    seen = set() if seen is None else seen
    seen.add(path)
    try:
        tree = ast.parse(path.read_text(encoding="utf-8"), str(path))
    except (SyntaxError, UnicodeDecodeError) as exc:
        return set(), ["%s cannot be read as Python (%s)" % (path.relative_to(root), exc.__class__.__name__)]
    mods, bad = set(), []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            mods |= {a.name.split(".")[0] for a in node.names}
        elif isinstance(node, ast.ImportFrom):
            if node.level:
                bad.append("%s imports relatively" % path.relative_to(root))
            elif node.module:
                mods.add(node.module.split(".")[0])
        elif isinstance(node, ast.Call) and getattr(node.func, "id", getattr(node.func, "attr", "")) in (
                "__import__", "import_module"):
            bad.append("%s imports by a call, which cannot be read" % path.relative_to(root))
    out = set()
    for m in sorted(mods):
        sib = path.parent / (m + ".py")
        if sib.is_file():
            if sib not in seen:
                more, more_bad = imports_of(sib, root, seen)
                out |= more
                bad += more_bad
        else:
            out.add(m)
    return out, bad


STRATEGIES = [(["unshare", "-rn", "--"], "unshare -rn"), (["sudo", "-n", "unshare", "-n", "--"], "sudo unshare -n")]


def sandbox_prefix():
    """(the command prefix that cuts the network, its name), tested; ([], "static guard only") when none works"""
    for prefix, name in STRATEGIES:
        if not shutil.which(prefix[0]):
            continue
        try:
            r = subprocess.run(prefix + [sys.executable, "-c", PROBE], capture_output=True, timeout=30)
        except (OSError, subprocess.TimeoutExpired):
            continue
        if r.returncode == 7:
            return prefix, name
    return [], "static guard only"


def _command(cmd, script_path):
    """the argument list of a plain run of the decisive script (python3 <a .py of the commit> [arguments]), or None"""
    try:
        argv = shlex.split(cmd)
    except ValueError:
        return None
    if len(argv) < 2 or argv[0] not in ("python3", "python") or not argv[1].endswith(".py") or argv[1].startswith(("/", "-")) \
            or ".." in pathlib.PurePosixPath(argv[1]).parts:
        return None
    if any(c in cmd for c in ";|&`$><"):
        return None
    return [sys.executable, "-E", "-s"] + argv[1:]


def _run(prefix, argv, cwd, limit):
    env = {"PATH": "/usr/bin:/bin", "HOME": str(cwd), "LANG": "C.UTF-8", "PYTHONHASHSEED": "0"}
    t0 = time.time()
    try:
        r = subprocess.run(prefix + argv, cwd=cwd, capture_output=True, text=True, timeout=limit, env=env)
        return r.returncode, r.stdout, r.stderr, time.time() - t0
    except subprocess.TimeoutExpired:
        return None, "", "", time.time() - t0


def versions():
    out = {"python": "%d.%d.%d" % sys.version_info[:3]}
    for dist in PACKAGES:
        try:
            out[dist] = importlib.metadata.version(dist)
        except importlib.metadata.PackageNotFoundError:
            out[dist] = None
    return out


def rerun(root, commit, card_text, limit=TIME_LIMIT, prefix=None):
    """the result of rerunning one card at one commit: {status, reasons, ...}"""
    _title, f, _ = CF.read(card_text)
    res = {"status": None, "reasons": [], "commit": commit, "guard": None, "versions": versions(), "pins_differ": []}
    res["pins_differ"] = sorted(d for d, v in res["versions"].items()
                                if d in PINS["packages"] and v is not None and v != PINS["packages"][d]["pin"])
    m = CF.SCRIPT.match(f.get("decisive script", ""))
    d = CF.DECISIVE.fullmatch(f.get("decisive lines", ""))
    if not m or not d:
        res.update(status="RETURNED_AT_INTAKE", reasons=["the card's decisive script or decisive lines are not in form"])
        return res
    script, cmd, control = m.group(1), m.group(3).strip(), f.get("failing control", "")
    tmp = pathlib.Path(tempfile.mkdtemp(prefix="rerun_"))
    try:
        p = subprocess.run(["git", "archive", "--format=tar", commit], cwd=root, capture_output=True)
        if p.returncode != 0:
            res.update(status="RETURNED_AT_INTAKE", reasons=["the sealed commit cannot be read"])
            return res
        subprocess.run(["tar", "-x", "-C", str(tmp)], input=p.stdout, check=True)
        if script.endswith((".sage", ".g", ".gap")):
            res.update(status="HEAVY", reasons=["the decisive script is run by sage or GAP"])
            return res
        path = tmp / script
        if not path.is_file():
            res.update(status="RETURNED_AT_INTAKE", reasons=["the decisive script %s is not at the commit" % script])
            return res
        mods, bad = imports_of(path, tmp)
        heavy = sorted(mods & HEAVY_MODULES)
        allowed = STDLIB | set(PACKAGES.values()) | HEAVY_MODULES
        outside = sorted(mods - allowed)
        if bad or outside:
            res.update(status="RETURNED_AT_INTAKE", reasons=bad + (["the script imports what is not allowed: %s"
                                                                     % ", ".join(outside)] if outside else []))
            return res
        if heavy:
            res.update(status="HEAVY", reasons=["the decisive script imports %s" % ", ".join(heavy)])
            return res
        argv, cargv = _command(cmd, script), _command(control, script)
        if argv is None or argv[3] != script:
            res["reasons"].append("the decisive command is not a plain run of the decisive script: %r" % cmd)
        if cargv is None:
            res["reasons"].append("the failing control is not a plain run of a script of the commit: %r" % control)
        if res["reasons"]:
            res["status"] = "RETURNED_AT_INTAKE"
            return res
        if prefix is None:
            prefix, res["guard"] = sandbox_prefix()
        else:
            res["guard"] = " ".join(prefix) or "static guard only"
        rc, out, err, secs = _run(prefix, argv, tmp, limit)
        res["seconds"] = round(secs, 1)
        if rc is None:
            res.update(status="HEAVY", reasons=["the decisive script ran past %d seconds" % limit])
            return res
        res["output_sha256"] = hashlib.sha256(out.encode("utf-8")).hexdigest()[:16]
        n, h = decisive(out)
        res["decisive"] = {"lines": n, "sha256": h}
        if rc != 0:
            res["reasons"].append("the decisive script exited with %d: %s" % (rc, err.strip().splitlines()[-1:] or ""))
        if (n, h) != (int(d.group(1)), d.group(2)):
            res["reasons"].append("the decisive lines are %d with hash %s; the card says %s with %s"
                                  % (n, h, d.group(1), d.group(2)))
        crc, _, _, csecs = _run(prefix, cargv, tmp, max(1, limit - int(secs)))
        res["control_exit"] = crc
        if crc is None:
            res.update(status="HEAVY", reasons=res["reasons"] + ["the failing control ran past the time limit"])
            return res
        if crc == 0:
            res["reasons"].append("the failing control exited 0: it did not fail")
        res["status"] = "RETURNED_AT_INTAKE" if res["reasons"] else "REPRODUCED"
        return res
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def main(argv):
    rec = json.loads(pathlib.Path(argv[argv.index("--record") + 1]).read_text(encoding="utf-8"))
    root = pathlib.Path(argv[argv.index("--root") + 1]) if "--root" in argv else ROOT
    limit = int(argv[argv.index("--limit") + 1]) if "--limit" in argv else TIME_LIMIT
    card = subprocess.run(["git", "show", "%s:%s" % (rec["commit"], rec["card_path"])], cwd=root, capture_output=True,
                          text=True)
    if card.returncode != 0:
        print(json.dumps({"status": "RETURNED_AT_INTAKE", "reasons": ["the card is not at its sealed commit"]}))
        return 1
    res = rerun(root, rec["commit"], card.stdout, limit)
    print(json.dumps(res, indent=1, sort_keys=True))
    return 0 if res["status"] in ("REPRODUCED", "HEAVY") else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
